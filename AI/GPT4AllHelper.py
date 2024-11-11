"""
GPT4AllHelper.py

Voor je verder gaat moet ik je even waarschuwen dat dit de eindbaas van het eerste semester is.
Om hiermee te kunnen werken heb je de volgende dingen nodig:

1. Een vrij stevige computer om lokaal een taalmodel te kunnen draaien
2. Enige kennis van taalmodellen (met name tokenization en temperatuur)
3. Enige kennis van objectgeoriënteerd programmeren
4. Kennis van API's
5. Enige kennis van type hints + goede kennis van datatypes

Voor uitgebreidere instructies, zie GTP4AllHelper.md. Voor voorbeeldcode,
zie het voorbeeldje onderaan. Je kunt deze file ook runnen.

@author     Lina Blijleven (@LinaBlijlevenHU op GitHub)
"""
from typing import Optional

import requests
import json

class GPT4AllHelper:

    # Base URL from local API hosted by GPT4All, defaults to port 4891
    host = "http://localhost:4891/v1"

    # Endpoints for specific goals
    prompt_url = f"{host}/chat/completions"
    models_url = f"{host}/models"

    # There are more endpoints!
    # Check out https://docs.gpt4all.io/gpt4all_api_server/home.html
    # model_url = /v1/models/<name>
    # chat_url = /v1/chat/completions

    # LLM config
    model: str
    max_tokens: int
    temperature: float


    def __init__(self, model = "Llama 3.2 1B Instruct", max_tokens = 50, temperature = 0.28):
        """
        Construct a new model using GPT4All's local API

        :param  model           Preferred model to use (optional, default Phi-3 Mini Instruct)
        :param  max_tokens      Maximum number of tokens for the response
        :param  temperature     Desired temperature for the model
        """
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def get_models(self) -> Optional[dict]:
        """
        Get the available models from where the API is hosted

        :return:    requests.Response   Response object
        """
        response = requests.get(self.models_url)

        return response.json() if response.status_code == 200 else None


    def post(self, prompt: str) -> requests.Response:
        """
        Send a prompt to the completion endpoint of GPT4All to
        complete text/answer questions/etc.

        :param      prompt:     Prompt for the model (text-only)
        :return:    Response:   Response object containing status code, JSON and more
        """
        # Compile our data into the desired format for the API call
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 50,
            "temperature": 0.28
        }

        # Send the request to the server
        response = requests.post(
            self.prompt_url,                                       # Endpoint
            data=json.dumps(data),                          # JSON-ified data
            headers={"Content-Type": "application/json"}    # We want to receive JSON back
        )

        return response

    def prompt(self, prompt: str) -> requests.Response:
        """ Alias for the post function """
        return self.post(prompt)

# Example usage
if __name__ == "__main__":
    # Example prompt
    example_prompt: str = "Who is Lionel Messi?"
    # Create a default GPT
    gpt: GPT4AllHelper = GPT4AllHelper()

    # Ask which models are available
    models_response: Optional[dict] = gpt.get_models()
    print(f"Available models response:\n{models_response}")

    # Send our example prompt to the language model and get a response :D
    example_response: requests.Response = gpt.post(example_prompt)

    # Print some information about the response
    print(f"API responded with {example_response.status_code}")
    print(f"JSON response:\n{example_response.json()}")