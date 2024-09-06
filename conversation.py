from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role" : "system", "content": "You are a professional sports analyst"},
        {"role" : "user", "content": "What is the latest news in the NBA?"},
        {"role" : "assistant", "content": "The Raptors signed the new contract with Immanuel Quickley this summer."},
        {"role" : "user", "content" : "What is the name of the Raptors point guard?"}
    ]
)

print(response.choices[0].message.content)