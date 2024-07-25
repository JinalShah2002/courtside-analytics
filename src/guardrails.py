"""

@author: Jinal Shah


This script is a guardrail model
for the agent. I want to ensure
that the user only inputs questions
related to NBA statistics.

As a guardrail, I will utilize GPT-4o.

"""
from openai import OpenAI

class Guardrails:
    # Constructor
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
    
    # Method to check if input is a question about the NBA
    def nbaQuestion(self,input_text,model="gpt-4"):
        system_prompt = """
                        You are a guardrail model. Your job is to determine whether or not a given text is related to the 
                        National Basketball Association (NBA). You are to only respond with 'Y' (for yes) and 'N' (for no).
                        """
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_text}
            ]
        )

        if response.choices[0].message.content == 'Y':
            return True
        else:
            return False 

# Testing out the guardrails
if __name__ == "__main__":
    api_key = input('Open AI API Key: ')
    guardrails = Guardrails(api_key=api_key)

    # Test 1
    input_text = "How many points per game does LeBron James average?"
    print(input_text)
    print(guardrails.nbaQuestion(input_text))
    print()

    # Test 2
    input_text = "What is the capital of France?"
    print(input_text)
    print(guardrails.nbaQuestion(input_text))
    print()

    # Test 3 
    input_text = "Who is the best player in the NBA?"
    print(input_text)
    print(guardrails.nbaQuestion(input_text))
    print()

    # Test 4
    input_text = "Who won the 2021 NBA Championship?"
    print(input_text)
    print(guardrails.nbaQuestion(input_text))
    print()

    # Test 5
    input_text = "Who is Jakob Poeltl?"
    print(input_text)
    print(guardrails.nbaQuestion(input_text))
    print()

    # Test 6
    input_text = "What is the square root of 144?"
    print(input_text)
    print(guardrails.nbaQuestion(input_text))
    print()

    # Test 7
    input_text = "Who is Joe Biden?"
    print(input_text)
    print(guardrails.nbaQuestion(input_text))
    print()