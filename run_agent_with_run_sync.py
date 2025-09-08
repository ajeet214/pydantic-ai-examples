import os
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider
from dotenv import load_dotenv

load_dotenv()

model = GroqModel(
    'openai/gpt-oss-20b', provider=GroqProvider(api_key=os.getenv("GROQ_API_KEY"))
)


agent = Agent(model)

result_sync = agent.run_sync('What is the capital of Italy?')
print(result_sync.output)
