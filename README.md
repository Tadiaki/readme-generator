# AI Agent using Mistral AI API with Autogen

This repository contains a example specific to using the Mistral AI API with Autogen.
In order to use the Mistral AI API with Autogen, you need to install a fork of the `autogen` package that has a fix for the `api_rate_limit` parameter. This is already done in the `requirements.txt` file, just be aware that you're using a forked version of `autogen`.

> [!NOTE]
> In order to use the Mistral Cloud API, you need to have a valid API key. [Mistral has a generous free tier that you can use to get started](https://mistral.ai/).

---

## Setup

Install the Python dependencies.

```bash
pip install -r requirements.txt
```

Modify the `config.py` file to include your Mistral AI API key.

```python
LLM_CONFIG = {
    "config_list": [
        {
            "model": "open-mistral-nemo",
            "api_key": "<your-api-key>",
            ...
        }
    ]
}
```

---

## Dependencies

- Python 3.10+
- autogen (https://github.com/patrickstolc/autogen)
- mistralai

---

## Run the agent

```bash
python -m autogen_mistralai.agent.feedback_analysis_agent
```
