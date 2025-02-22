from __future__ import annotations

# Import essentials
import openai

# Import helpers, constants and typing
from termcolor import colored
from typing import Optional
from typing import List
from src.utils.helpers import sum_content_length
from src.utils.logs_and_env import Logger

logger = Logger()
OPENAI_API_KEY = logger._get_env_variable('OPENAI_API_KEY')
MODEL = logger._get_env_variable('MODEL')
SUPER_CHARGED = logger._get_env_variable('SUPER_CHARGED')

class ChatCompletionGenerator:
    def __init__(self, temperature: Optional[float]=0.33, prompt_num: Optional[int] = 0, openai_api_key: Optional[str] = OPENAI_API_KEY, model: Optional[str] = MODEL, super_charged: Optional[str] = SUPER_CHARGED, default_compilation: Optional[str] = ""):
        """
        Constructor for the SystemMessageMaker class.
        
        Args:
            prompt_num (int, optional): The number of the prompt to use. Defaults to None.
            openai_api_key (str, optional): The API key for OpenAI. Defaults to None.
            model (str, optional): The model for OpenAI. Defaults to None.
            super_charged (str, optional): The super charged mode for GPT-4. Defaults to None.
        """
        self.prompt_num = prompt_num
        self.openai_api_key = openai_api_key if openai_api_key else OPENAI_API_KEY
        self.model = model if model else MODEL
        self.super_charged = super_charged if super_charged else SUPER_CHARGED
        openai.api_key = self.openai_api_key

    def generate_completion(self, messages: List[dict], model: Optional[str]=MODEL, temperature: Optional[float]=0.33) -> str:
        print(colored(f"\nMODEL ACTUALLY BEING USED: {model}\n", 'red'))
        """
        Generates a completion using OpenAI's ChatCompletion API.

        Args:
            messages (List[dict]): A list of messages to start the completion. Each message is a dictionary containing 'role' and 'content' keys.
            model (str, optional): The model to use for the completion. Defaults to "gpt-3.5-turbo".
            temperature (float, optional): The higher the number used, the more statistical variation / randomness. Between 0.1-0.5 is reocmmended for coding and facts.

        Returns:
            str: The content of the completion generated by the model.
        """
        print(colored("\nGenerating completion...\n", 'magenta'))
        print(colored(f"Current context length: {sum_content_length(messages)}\n", 'red'))

        response = openai.ChatCompletion.create(
            model=model,
            messages = messages,
            max_tokens = 4000,
            temperature = temperature
        )
        print(colored("--Successfully completed last API call--\n", 'blue'))
        return response['choices'][0]['message']['content']