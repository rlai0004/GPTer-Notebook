import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

system = "System: "
user = "You: "
welcome_msg = """Welcome! I am Jupyter Bot. Your personal Jupyter Notebook assistant. 
To get started. Please provide me the context of your notebook and the datasets.
Here is an example:
The notebook I am writing is about ... . These are the given dataset:
games.csv - metadata about games
turns.csv - all turns from start to finish of each game
"""
log = [
    {"role": "system", "content": "You are a Jupyter Notebook code assistant for data scientists."}
]


def run():
    print(f"{system}{welcome_msg}")
    while True:
        user_prompt = input(f"{user}")
        # stop the program
        if user_prompt == '$':
            break
        # append the user input to the log
        log.append({"role": "user", "content": f"{user_prompt}"},)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=log
        )
        answer = response.choices[0].message.content
        log.append({"role": "assistant", "content": f"{answer}"},)
        print(f"{system}{answer}\n")
    print(log)


if __name__ == "__main__":
    run()
