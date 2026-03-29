import random

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the Python programmer need glasses? Because he couldn't C#.",
    "What's a programmer's favorite hangout place? Foo Bar.",
    "Why do Java developers wear glasses? Because they can't C#.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "Why was the computer cold? It left its Windows open.",
    "What do you call a snake that's 3.14 meters long? A Pi-thon.",
    "Why did the developer go broke? Because he used up all his cache.",
    "What's a computer's least favorite food? Spam.",
    "Why do Python programmers have low self-esteem? They're constantly comparing themselves to others.",
]


def tell_joke():
    return random.choice(jokes)


def main():
    print("Welcome to the Jokes App!")
    print("This is very funny")
    print("-" * 30)

    while True:
        print(f"\n{tell_joke()} babab\n")
        again = input("Want another joke? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye! Hope you had a laugh!")
            break


if __name__ == "__main__":
    main()
