LLM_CONFIG = {
    "config_list": [
        {
            "model": "open-mistral-nemo", # model name from the Mistral AI API docs
            "api_key": "123xxx", # TODO: replace with your API key
            "api_type": "mistral",
            "api_rate_limit": 0.25,
            "num_predict": -1, # no limit on the number of tokens to predict
            "repeat_penalty": 1.1,
            "seed": 42,
            "stream": False,
            "temperature": 0.5,
            "top_k": 50,
            "top_p": 0.8,
            "native_tool_calls": False,
            "cache_seed": None,
        }
    ]
}