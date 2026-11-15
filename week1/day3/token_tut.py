import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROK_API_KEY")

if not my_api_key:
    raise ValueError("Api key not found")

client=Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

role = "user"
# prompt = "Who is rohit sharma?"

# 3 prompt to understand the token usage
prompt1 = "Hi!"
prompt2 = "Explain time travel in 100 words"
prompt3 = "Write a 1000 word essay on machine learning"

prompts=[prompt1, prompt2, prompt3]
for prompt in prompts:
    message={
    "role":role,
    "content":prompt
}
    messages=[message]
    response = client.chat.completions.create( model=model, messages=messages, max_tokens=500)
    usage = response.usage
    print(f"Prompt: {prompt}-->your token:{usage.prompt_tokens} complition token:{usage.completion_tokens} total token:{usage.total_tokens} finish reason:{response.choices[0].finish_reason}")
    

# message={
#     "role":role,
#     "content":prompt
# }
# messages=[message]

# response = client.chat.completions.create(
#     model=model,
#     messages=messages
# )

# print(response.choices[0].message.content)
