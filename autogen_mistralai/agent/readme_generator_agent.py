import ast
import copy
from autogen import AssistantAgent, UserProxyAgent, ChatResult, register_function
from autogen.coding import LocalCommandLineCodeExecutor
from autogen_mistralai.tools.md_writer_tool import MarkdownHelper as MH
# from autogen_mistralai.tools.sentiment_analysis_tool import sentiment_analysis
# from autogen_mistralai.tools.calculate_average_tool import calculate_average
from autogen_mistralai.config import LLM_CONFIG
#from project_examples.project1 import generate_project1 as project1
#from project_examples.project1 import generate_project2 as project2

ReAct_prompt = """
Answer the following questions as best you can. You have access to the tools provided.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do and what tool to use
Action: the action to take is ALWAYS one of the provided tools
Action Input: the input to the action
Observation: the result of the action. Only observe tools' outputs.
... (this thought/action/action input/observation can repeat N times)
Thought: I can now generate the README
Final Answer: the final answer to the original input question and should be a result of the provided tools and nothing else

Begin!
Question: {input}
"""


def react_prompt_message(sender, recipient, context):
    """
    Return the ReAct prompt message interpolated with the input question.
    """
    return ReAct_prompt.format(input=context["question"])


def create_readme_generator_agent() -> AssistantAgent:
    """
    Create a readme generator agent.
    """
    agent = AssistantAgent(
        name="Assistant",
        system_message="""
        Only use tools. Don't try to reason. Reply TERMINATE when the task is done.
        """,
        llm_config=copy.deepcopy(LLM_CONFIG)
    )

    return agent

def create_user_proxy(code_executor: LocalCommandLineCodeExecutor):
    """
    Return a new user proxy agent.
    """
    user_proxy = UserProxyAgent(
        name="User",
        llm_config=None,
        is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().lower().endswith("terminate"),
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        code_execution_config={
        "executor": LocalCommandLineCodeExecutor(work_dir="readmes"),
        },
    )
    return user_proxy


def create_local_code_executor():
    """
    Return a new local code executor.
    """
    return LocalCommandLineCodeExecutor(
        timeout=100,
    )


def setup_agents():
    """
    Setup the agents.
    """
    # Create the code executor, user proxy, and feedback analysis agent
    code_executor = create_local_code_executor()
    user_proxy = create_user_proxy(code_executor)
    create_readme_generator_agent = create_readme_generator_agent()

    # Add the different methods from the md writer tool.
    print("registering readme generator header")
    register_function(
        MH.header, 
        caller=create_readme_generator_agent, 
        executor=user_proxy, 
        name="mh_header", 
        description="Generates a markdown header based on the input text and level."
    )
    
    # Add the different methods from the md writer tool.
    print("registering readme generator paragraph")
    register_function(
        MH.paragraph, 
        caller=create_readme_generator_agent, 
        executor=user_proxy, 
        name="mh_paragraph", 
        description="Generates a markdown paragraph based on the input text."
    )
    
    # Add the different methods from the md writer tool.
    print("registering readme generator list")
    register_function(
        MH.list, 
        caller=create_readme_generator_agent, 
        executor=user_proxy, 
        name="mh_list", 
        description="Generates a markdown list based on the input items and ordered flag."
    )
    
    # Add the different methods from the md writer tool.
    print("registering readme generator code_block")
    register_function(
        MH.code_block, 
        caller=create_readme_generator_agent, 
        executor=user_proxy, 
        name="mh_code_block", 
        description="Generates a markdown code_block based on the input code and language."
    )
    
    # Add the different methods from the md writer tool.
    print("registering readme generator link")
    register_function(
        MH.link, 
        caller=create_readme_generator_agent, 
        executor=user_proxy, 
        name="mh_link", 
        description="Generates a markdown link based on the input text and url."
    )
    
    # Add the different methods from the md writer tool.
    print("registering readme generator image")
    register_function(
        MH.image, 
        caller=create_readme_generator_agent, 
        executor=user_proxy, 
        name="mh_image", 
        description="Generates a markdown image based on the input alt_text and url."
    )
    
    # Add the different methods from the md writer tool.
    print("registering readme generator table")
    register_function(
        MH.table, 
        caller=create_readme_generator_agent, 
        executor=user_proxy, 
        name="mh_table", 
        description="Generates a markdown table based on the input headers and rows."
    )
    
    # Add the different methods from the md writer tool.
    print("registering readme generator blockquote")
    register_function(
        MH.blockquote, 
        caller=create_readme_generator_agent, 
        executor=user_proxy, 
        name="mh_blockquote", 
        description="Generates a markdown blockquote based on the input text."
    )
    
    # Add the different methods from the md writer tool.
    print("registering readme generator horizontal_rule")
    register_function(
        MH.horizontal_rule, 
        caller=create_readme_generator_agent, 
        executor=user_proxy, 
        name="mh_horizontal_rule", 
        description="Generates a markdown horizontal_rule whenever needed."
    )
    
    # Add the different methods from the md writer tool.
    print("registering readme generator annotation_wrapper")
    register_function(
        MH.annotation_wrapper, 
        caller=create_readme_generator_agent, 
        executor=user_proxy, 
        name="mh_annotation_wrapper", 
        description="Generates a markdown annotation_wrapper."
    )
    
    return user_proxy, create_readme_generator_agent


def get_tool_calls(chat_result: ChatResult):
    """
    Return the tool calls from the chat result.
    """
    tool_call_history = []

    for message in chat_result.chat_history:
        if "tool_calls" in message.keys():
            tool_calls = map(lambda x: { "name": x["function"]["name"], "arguments": ast.literal_eval(x["function"]["arguments"]) }, message["tool_calls"])
            tool_call_history.extend(list(tool_calls))

    return tool_call_history


def find_final_answer(chat_result: ChatResult):
    """
    Generate the final answer from the chat results in a newly generated README in the specified directory.
    """

    # Get the chat history
    messages = chat_result.chat_history
    final_answer = None

    # Iterate over the chat history in reverse order
    for message in reversed(messages):
        # Check if the message contains the final answer
        if "final answer:" in message.get("content", "").lower():
            # Get the final answer block    
            final_answer_block = message.get("content", "")

            # Split the final answer block into lines
            answer_block_lines = final_answer_block.split("\n")

            # Get the final answer
            final_answer = answer_block_lines[-1].split("Final Answer:")[1].strip()
            break

    # Return the final answer
    return final_answer


def main():
    # Setup the agents
    user_proxy, feedback_analysis_agent = setup_agents()

    # Define the task
    task = "Generate a README for a project using the provided project example data."

    # Initiate the chat
    user_proxy.initiate_chat(
        feedback_analysis_agent,
        message=task,
    )


if __name__ == "__main__":
    main()