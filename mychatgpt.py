# -----------------------------------------------------
# myChatGpt script
# modify the path to the openai.yaml
# -----------------------------------------------------

import openai
import pyperclip
import yaml
from pathlib import Path
from yaml import load,CLoader as Loader

# Path to your openai.yaml in your home directory
openaipath = "/private/openai.yaml"
# openaipath = "/mychatgpt/openai.yaml"

# Get home path
home = str(Path.home())

# Load openai api key
with open(home + openaipath, "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=Loader)

# Set up the OpenAI API client
openai.api_key = cfg["openai"]["api-key"]

# Set up the model and prompt
model_engine = "text-davinci-003"

prompt = str(input("Hello, how can I help you? "))
print('...')

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)

pyperclip.copy(response)
print("...")
print("Output has been copied to the clipboard")
