from openai import OpenAI

def main():
    client = OpenAI(
        api_key="", # Replace YOUR_OPENAI_API_KEY
    )
    messages = []

    while True:
        user_input = input("\n[Input](or 'exit'): ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        bot_response = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": bot_response})

        print(bot_response)

if __name__ == "__main__":
    main()
