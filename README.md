# Readme generator

Readme generator is a small python application that uses autogen to create an agent that generates readme files based on package.json files.

## Getting Started

To get started with the project, follow these steps:

To clone the repository go to the following URL and clone the project.

```
https://github.com/Tadiaki/readme-generator
```
Navigate to the root directory and run the following command to install the required dependencies.

```
pip install -r requirements.txt
```

Creating the LLM config file.

To run the application, the agent framework needs an [LLM config object](https://microsoft.github.io/autogen/0.2/docs/topics/llm_configuration/) so that it knows where and what LLM to use. To create this object create a file in the root/autogen_mistralai directory called 'config.py' and create the LLM config object. In our case it looked like the following:

```
LLM_CONFIG = {
    "config_list": [
        {
            "model": "open-mistral-nemo",
            "api_key": <YOU API KEY HERE>,
            "api_type": "mistral",
            "api_rate_limit": 0.25,
            "num_predict": -1, # no limit on the number of tokens to predict
            "repeat_penalty": 1.1,
            "seed": 42,
            "stream": False,
            "temperature": 0.1,
            "top_k": 50,
            "top_p": 0.8,
            "native_tool_calls": False,
            "cache_seed": None,
        }
    ]
}
```

In our case the agent uses the open-mistral-nemo model, which is a hosted free tier model provided by Mistral AI API, which requires an API key. To learn more about Mistral's hosted sollutions read [here](https://docs.mistral.ai/getting-started/quickstart/).

If you want to run it all locally, you can use an option such as [Ollama](https://ollama.com/).

## Usage

To run the application run the following command from the root directory:

```
python -m autogen_mistralai.agent.readme_generator_agent
```


## Dependencies

| Package | Version |
|---------|---------|
| Python | 3.10+ |
| [mistralai](https://github.com/mistralai/client-python) | 1.2.3 |
| Autogen from @git+https://github.com/patrickstolc/autogen.git@0.2#egg=autogen-agentchat | 0.2 |

## Authors

- [Simon Tved Nielsen](https://github.com/Tadiaki)
- [Jan Wohlgehagen](https://github.com/JanWohlgehagen)
- [Mikkel Theut](https://github.com/Theut94)

## License

MIT

## Repository

[GitHub](https://github.com/Tadiaki/readme-generator)