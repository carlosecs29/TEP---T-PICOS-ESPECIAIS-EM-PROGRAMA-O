 import requests
 API_BASE_URL =
 "https: api.cloudflare.com/client/v4/accounts/<ID_ACCOUNT>/ai/run/"
 headers = {"Authorization": "Bearer {LAaW1mBGoMxeR0-zHn3aBw65Rn5e3E0NjO5j_rT3}"}
 def run(model, inputs)
 input = { "messages": inputs }
 response = requests.post(f"{API_BASE_URL}{model}", headers=headers,
 json=input)
 return response.json()
inputs = [
 { "role": "system", "content": "You are a friendly assistan that helps
 write stories" },
 { "role": "user", "content": "Write a short story about a llama that
 goes on a journey to fnd an orange cloud "}
 ];
 output = run("@cf/meta/llama-3-8binstruct", inputs)
 print(output)