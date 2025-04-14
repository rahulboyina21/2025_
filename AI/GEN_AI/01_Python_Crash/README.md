# 🐍 Python for Generative AI (Complete Guide)

This markdown serves as a **comprehensive Python guide** tailored specifically for **Generative AI development**.  
Whether you're working with **LangChain, LLMs, HuggingFace, Transformers**, or building your own GenAI apps — this is your foundation.

---

## 📌 Table of Contents
1. Python Essentials
2. Object-Oriented Programming (OOP)
3. File Handling
4. Working with Libraries (NumPy, Pandas)
5. Virtual Environments
6. API Integration (Requests, JSON)
7. Async Programming
8. Regex Basics
9. Web Scraping
10. Data Serialization
11. Working with External Files (YAML, CSV, JSON)
12. Debugging & Logging
13. GenAI Specific Libraries
14. Final Project Template

---

## 1. 🧠 Python Essentials

```python
# Variables & Types
name = "Rahul"
age = 25
is_active = True

# Lists
fruits = ["apple", "banana", "mango"]
fruits.append("kiwi")

# Dictionaries
person = {"name": "Rahul", "age": 25}
print(person["name"])

# Loops
for fruit in fruits:
    print(fruit)

# Functions
def greet(name):
    return f"Hello, {name}"

print(greet("LangChain"))



⸻

2. 🔧 Object-Oriented Programming

class LLM:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def describe(self):
        return f"{self.name} v{self.version}"

model = LLM("GPT", "4.0")
print(model.describe())



⸻

3. 📁 File Handling

# Writing to a file
with open("output.txt", "w") as f:
    f.write("This is a test file")

# Reading from a file
with open("output.txt", "r") as f:
    content = f.read()
    print(content)



⸻

4. 🔢 NumPy and Pandas

import numpy as np
import pandas as pd

arr = np.array([1, 2, 3])
df = pd.DataFrame({"name": ["A", "B"], "score": [90, 80]})
print(df)



⸻

5. 🧪 Virtual Environment

# Setup
python -m venv genai-env
source genai-env/bin/activate  # or .\\genai-env\\Scripts\\activate (Windows)
pip install -r requirements.txt



⸻

6. 🌐 API Integration

import requests
import json

response = requests.get("https://api.github.com")
data = response.json()
print(data["current_user_url"])



⸻

7. 🌀 Async Programming

import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    return "Data fetched!"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())



⸻

8. 🔍 Regular Expressions

import re

text = "LangChain uses LLMs like GPT"
match = re.search(r"LLM.*", text)
print(match.group())  # LLMs like GPT



⸻

9. 🕸 Web Scraping

import requests
from bs4 import BeautifulSoup

res = requests.get("https://example.com")
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.title.text)



⸻

10. 💾 Data Serialization

import pickle

data = {"lang": "Python", "type": "AI"}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)



⸻

11. 🧾 External File Types

import json, yaml, csv

# JSON
with open("data.json", "r") as f:
    print(json.load(f))

# YAML
with open("config.yaml", "r") as f:
    print(yaml.safe_load(f))

# CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



⸻

12. 🐞 Debugging and Logging

import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")



⸻

13. 🤖 GenAI-Specific Libraries

pip install langchain openai transformers streamlit huggingface_hub

from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')
print(generator("AI will change", max_length=20))



⸻

14. 🧱 Final GenAI Project Skeleton

GenAI-Project/
│
├── app.py                # Streamlit or main app
├── utils/
│   └── helpers.py        # Helper functions
├── config.yaml           # Config
├── data/
│   └── prompts.txt
├── models/
│   └── fine_tuned_llm/
├── README.md
└── requirements.txt



⸻

🏁 Tips for Success
	•	Use Jupyter/Colab for fast prototyping
	•	Keep notes as .md in each project
	•	Learn by building
	•	Stay updated with HuggingFace, LangChain, OpenAI docs

⸻

This is your launchpad. Let Python be your sword in the GenAI journey. 🧠⚔️
