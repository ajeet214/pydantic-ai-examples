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
    result = await agent.run('What is the capital of France?')
    print(result.output)
    # > The capital of France is Paris.


if __name__ == "__main__":
    asyncio.run(main())
