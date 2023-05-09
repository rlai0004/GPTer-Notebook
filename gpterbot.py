import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

system = "System: "
user = "You: "
start_instruction = "\nTo start working through these step one by one. Type 'Start'"
welcome_instruction = """Welcome! I am Jupyter Bot. Your personal Jupyter Notebook assistant. 
To get started. Please provide me the context of your notebook and the datasets.
Here is an example:
The notebook I am writing is about .... These are the given dataset:
games.csv - metadata about games
turns.csv - all turns from start to finish of each game

To end type '$'.
"""

log = [
    {"role": "system", "content": "You are a Jupyter Notebook code assistant for data scientists. Follow the instruction carefully"}
] 
custom_prompts = []
more_detail_prompt = """\nAsk me to provide you with more detail about each dataset e.g., Can you please provide more detail about each dataset and their variables? Do not generate extra informations."""
goal_prompt = """\nAsk me what my goal is e.g., What is your goal for this task based on the data provided?"""
general_step_prompt = """\nGenerate the required step that I can take as detail as possible. Do not generate any code."""
custom_prompts.append(more_detail_prompt)
custom_prompts.append(goal_prompt)
custom_prompts.append(general_step_prompt)


def run():
    num_prompts = 0
    print(f"{system}{welcome_instruction}")
    while True:
        user_prompt = input(f"{user}")
        # stop the program
        if user_prompt == '$':
            break
        if num_prompts < len(custom_prompts):   
            user_prompt += custom_prompts[num_prompts]
        # append the user input to the log
        log.append({"role": "user", "content": f"{user_prompt}"},)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=log
        )
        answer = response.choices[0].message.content
        # append the gpt answer to the log
        log.append({"role": "assistant", "content": f"{answer}"},)
        if num_prompts == len(custom_prompts)-1:
            answer += start_instruction
        num_prompts += 1
        print(f"{system}{answer}\n")
