import os
from pydantic_ai.direct import model_request_sync
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider
from pydantic_ai.messages import ModelRequest
from dotenv import load_dotenv

load_dotenv()

model = GroqModel(
    'openai/gpt-oss-20b', provider=GroqProvider(api_key=os.getenv("GROQ_API_KEY"))
)


model_response = model_request_sync(
    model,
    [ModelRequest.user_text_prompt('What is the capital of France?')],
    model_settings={"temperature": 0, "max_tokens": 4028}
)
print(model_response.parts[0].content)
