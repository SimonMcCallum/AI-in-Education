from openai import OpenAI
client = OpenAI()

system = [{"role": "system",
           "content": """You are a creative writing expert."""}]
user = [{"role": "user", "content":
         "Produce: a paragraph story about an escaped chimpanzee."}]

for seed in [444, 444, 666, 666]:
    response = client.chat.completions.create(
        messages = system + user,
        model="gpt-3.5-turbo",
        temperature = 1.1, stream=True,
        seed = seed, max_tokens = 100)
    print(f"\n==Response with seed {seed}==")
    for delta in response:
        if not delta.choices[0].finish_reason:
            word = delta.choices[0].delta.content or ""
            print(word, end ="")