import copy
from autogen import AssistantAgent, UserProxyAgent, register_function
from autogen.coding import LocalCommandLineCodeExecutor
from autogen_mistralai.tools.md_writer_tool import MarkdownHelper as MH
from autogen_mistralai.config import LLM_CONFIG

ReAct_prompt = """
    Your task is to create a README file based on the `package.json`. 
    Use the tools to generate content and call the file-writing function to save it.

    Steps:
    1. Parse the `package.json` and reason about the required sections.
    2. Use tools to generate Markdown appropriate content.
    3. Verify 
    3. Call `write_to_file` to save the content incrementally.

    Remember:
    - Each tool generates content but does not write files.
    - Only the `write_to_file` function should write to the file.
    - Follow step-by-step reasoning.
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
            You are a markdown generator assistant. 
            Your task is to analyze the fields in a `package.json` file and generate an appropriate README file using only the tools provided.
            Include information logically based on the following guidelines:
            - Always include the project name and description.
            - Include scripts if they are present in the package.json file the scripts should be constructed as follows:
                1. A description of what the script is used for in a paragraph.
                2. A code block with the script's command using the mh_code_block tool prefixed with npm run.
            - Add sections for dependencies (and their versions), license, and author if applicable.
            - Use the registered Markdown functions to generate the content.

            Do not output anything other than the tools' results or the final answer. Reply with TERMINATE when the task is done.
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
        is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().lower().endswith("TERMINATE"),
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        code_execution_config={
        "executor": code_executor,
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
    readme_generator_agent = create_readme_generator_agent()

    # Add the different methods from the md writer tool.
    print("registering readme generator header")
    register_function(
        MH.header, 
        caller=readme_generator_agent, 
        executor=user_proxy, 
        name="mh_header", 
        description="Generates a markdown header based on the input text and level."
    )
    
    print("registering readme generator paragraph")
    register_function(
        MH.paragraph, 
        caller=readme_generator_agent, 
        executor=user_proxy, 
        name="mh_paragraph", 
        description="Generates a markdown paragraph based on the input text."
    )
    
    print("registering readme generator list")
    register_function(
        MH.list, 
        caller=readme_generator_agent, 
        executor=user_proxy, 
        name="mh_list", 
        description="Generates a markdown list based on the input items and ordered flag."
    )
    
    print("registering readme generator code_block")
    register_function(
        MH.code_block, 
        caller=readme_generator_agent, 
        executor=user_proxy, 
        name="mh_code_block", 
        description="Generates a markdown code_block based on the input code and language."
    )
    
    print("registering readme generator link")
    register_function(
        MH.link, 
        caller=readme_generator_agent, 
        executor=user_proxy, 
        name="mh_link", 
        description="Generates a markdown link based on the input text and url."
    )
    
    print("registering readme generator image")
    register_function(
        MH.image, 
        caller=readme_generator_agent, 
        executor=user_proxy, 
        name="mh_image", 
        description="Generates a markdown image based on the input alt_text and url."
    )
    
    print("registering readme generator table")
    register_function(
        MH.table, 
        caller=readme_generator_agent, 
        executor=user_proxy, 
        name="mh_table", 
        description="Generates a markdown table based on the input headers and rows."
    )
    
    print("registering readme generator blockquote")
    register_function(
        MH.blockquote, 
        caller=readme_generator_agent, 
        executor=user_proxy, 
        name="mh_blockquote", 
        description="Generates a markdown blockquote based on the input text."
    )
    
    print("registering readme generator horizontal_rule")
    register_function(
        MH.horizontal_rule, 
        caller=readme_generator_agent, 
        executor=user_proxy, 
        name="mh_horizontal_rule", 
        description="Generates a markdown horizontal_rule whenever needed."
    )
    
    
    print("registering parse_package_json")
    register_function(
        MH.parse_package_json, 
        caller=readme_generator_agent, 
        executor=user_proxy, 
        name="mh_parse_package_json", 
        description="Parses a package.json file and returns relevant fields like name, description, scripts, author, and license."
    )
    
    print("registering write_to_file")
    register_function(
        MH.write_to_file, 
        caller=readme_generator_agent, 
        executor=user_proxy, 
        name="mh_write_to_file", 
        description="Writes the specified content to a file at the given path, with support for different write modes (e.g., append or overwrite)."
    )
    
    return user_proxy, readme_generator_agent



def main():
    # Setup the agents
    user_proxy, feedback_analysis_agent = setup_agents()

    # Define the task
    task = "Generate a README for a project using the provided project example data and write a readme.md file."

    # Initiate the chat
    user_proxy.initiate_chat(
        feedback_analysis_agent,
        message=task,
    )
    


if __name__ == "__main__":
    main()