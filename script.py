import random

vocab = {
    "你好": "Hello",
    "再见": "Goodbye",
    "狗": "Dog",
    "猴子": "Monkey",
    "爸爸": "Dad",
    "妈妈": "Mom",
    "爷爷": "Grandpa",
    "奶奶": "Grandma"
}

print("Translate the Chinese Words")

questions = list(vocab.items())
random.shuffle(questions)

for word, definition in questions:
    print(f"\nWhat is the translation of `{word}`?")
    answer = input("Your answer: ").strip().lower()

    if answer == definition.lower():
        print("Correct.")
    else:
        print(f"Incorrect. The correct answer is: {definition}")
