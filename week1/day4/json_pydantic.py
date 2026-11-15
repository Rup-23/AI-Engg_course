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


# Structure it
from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema=Ticket.model_json_schema() 

response_format={
    "type":"json_object"
}

system_prompt =f"""
Extract the personal information from the ticket strictly based on this schema.and give a json output.
{schema}
"""

system_message={
    "role":"system",
    "content":system_prompt
}

text = "Hello my name is Rupesh. yesterday i got angry and through it the water. I have a Google pixel phone which is not working at all. My address is Bargarh. My email is rkm23@gmail.com. My contact number is 76821"

prompt= f"""
This is a customer ticket. Please extract the personal information from this.
{text}
"""

# message me role and content 
message={
    "role":"user",
    "content":prompt
}
messages=[system_message, message]

response = client.chat.completions.create(
    model=model,
    messages=messages,
   response_format=response_format
)

answer = response.choices[0].message.content

print(answer)



# How to read 
import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.email)
print(ticket.name)
print(ticket.issue)