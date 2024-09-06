from openai import OpenAI
client = OpenAI()

response = client.images.generate(
    prompt="A strong dog",
    n=2,
    size="1024x1024"
)

image_url = response.data[0].url
print(image_url)