# Asynchronous Example
import asyncio
from mistralai import Mistral
import os
from dotenv import load_dotenv
load_dotenv()

async def generate(content):
    s = Mistral(
        api_key= os.getenv("AI_TOKEN"),
    )
    res = await  s.chat.complete_async(model="mistral-large-latest", messages=[
        {
            "content": content,
            "role": "user",
        },
    ])
    if res is not None:
         return res


 