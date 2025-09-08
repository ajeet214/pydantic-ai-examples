import os
import asyncio
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider
from pydantic_graph import End
from dotenv import load_dotenv

load_dotenv()

model = GroqModel(
    'openai/gpt-oss-20b', provider=GroqProvider(api_key=os.getenv("GROQ_API_KEY"))
)

agent = Agent(model=model)


async def main():
    nodes = []
    # Begin an AgentRun, which is an async-iterable over the nodes of the agent's graph
    async with agent.iter('What is the capital of France?') as agent_run:
        node = agent_run.next_node

        all_nodes = [node]

        # drive the iteration manually
        while not isinstance(node, End):
            node = await agent_run.next(node)

            # retrieve usage statistics (tokens, requests, etc.) at any time from the AgentRun object via
            # agent_run.usage()
            print(agent_run.usage())

            all_nodes.append(node)

        print(all_nodes)

        # Once the run finishes, agent_run.result becomes a AgentRunResult object containing the
        # final output (and related metadata)
        print(agent_run.result)



if __name__ == "__main__":
    asyncio.run(main())
