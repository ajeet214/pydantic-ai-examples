import os
import asyncio
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider
from dotenv import load_dotenv

load_dotenv()

model = GroqModel(
    'openai/gpt-oss-20b', provider=GroqProvider(api_key=os.getenv("GROQ_API_KEY"))
)

agent = Agent(model)


async def main():

    async with agent.run_stream('What is the capital of the UK?') as response:
        async for text in response.stream_text():
            print(text)
            #> The capital of
            #> The capital of the UK is
            #> The capital of the UK is London.


if __name__ == "__main__":
    asyncio.run(main())
