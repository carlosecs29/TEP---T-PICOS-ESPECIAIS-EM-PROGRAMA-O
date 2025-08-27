from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Qual o melhor time do brasil"
)

print(response.output_text)