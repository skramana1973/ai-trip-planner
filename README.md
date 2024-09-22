# ai-trip-planner
This AI based app takes care of booking flights hotels etc for trip based on calender  based on personal information and Large Language Model and RAG and Agent approach. 



# Install Fetch AI and Tools  related (One Time):

# Follow the documentation from 
```
https://fetch.ai
https://fetch.ai/docs
 
```
# Create Fetch.AI account and continue deploying Agents as per docs and provided code in this repo.

We have many agents that work together to book flights and hotels for the trip.

![alt text](image.png)




# Create CrewAi Project :

```bash
crewai create crew poc-topic-generator
cd poc-topic-generator
 
```

# Create .env to be used locally (its added in gitignore) and add below values 

```bash
OPENAI_API_KEY=OPEN_API_KEY
SERPER_API_KEY=SERPER_API_KEY

```

# Generating SERPER_API_KEY 
```bash
https://serper.dev

# Signup with email and password and once login left panel click on api key copy that to used in code

```

# PocTopicGenerator Crew

Welcome to the PocTopicGenerator Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry (One Time):

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/poc_topic_generator/config/agents.yaml` to define your agents
- Modify `src/poc_topic_generator/config/tasks.yaml` to define your tasks
- Modify `src/poc_topic_generator/crew.py` to add your own logic, tools and specific args
- Modify `src/poc_topic_generator/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

To run via api :

```bash
$ uvicorn src.api:app --reload
```
To generate file as raw text , change topic as needed in below curl or use postman :

```bash
$ curl --location 'http://127.0.0.1:8000/generate' \
--header 'Content-Type: application/json' \
--data '{"topic": "AI in healthcare"}'
``

To generate file , change topic as needed in below curl or use postman :

```bash
$ curl --location 'http://127.0.0.1:8000/report' \
--header 'Content-Type: application/json' \
--data '{"topic": "AI in healthcare"}'
```








This command initializes the poc-topic-generator Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The poc-topic-generator Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the PocTopicGenerator Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

