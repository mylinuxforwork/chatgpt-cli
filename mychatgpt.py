import openai
import pyperclip

# Set up the OpenAI API client
openai.api_key = "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"

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
