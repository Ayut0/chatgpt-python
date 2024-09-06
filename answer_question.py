from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are the best, dude!!"},
        {"role": "user", "content": "What is the meaning of life?"}
    ]
)

print(completion.choices[0].message)