from openai import OpenAI
client = OpenAI()

system = [{"role": "system",
           "content": """You are an vet."""}]
user = [{"role": "user", "content":
         "Produce: a sentence describing my cat."}]

seeds = [444, 555, 666, 777,888,999,1011,2022,3033,4044]

print(f"==Response context {user[0]["content"]}==")
for emphasis in ["my", "MY"]:
    user[0]["content"] = user[0]["content"].replace("my", emphasis)
    for seed in seeds:
        response = client.chat.completions.create(
            messages = system + user,
            model="gpt-3.5-turbo",
            temperature = 1, stream=True,
            seed = seed, max_tokens = 100)
        print(f"\n==Response word {emphasis} seed {seed} ==")
        for delta in response:
            if not delta.choices[0].finish_reason:
                word = delta.choices[0].delta.content or ""
                print(word, end ="")