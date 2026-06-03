import random
import datetime
import time
import re

# Ask for name once at startup
user_name = input("Before we begin, what is your name? ").strip()
if not user_name:
    user_name = "Friend"
print(f"\nNice to meet you, {user_name}! 😊\n")

BOT_NAME = "OdicosonBot"

def display_welcome():
    print("=" * 30)
    print(f"  Welcome! I am {BOT_NAME}")
    print("  A Rule-Based AI Chatbot")
    print("=" * 30)
    print("Type 'bye', 'see you' to exit.\n")

# -- Dictionary: exact match intents --
responses = {
    'hello':        random.choice(["Hello! How can I help?", "Hey! Great to see you!"]),
    'hi':           'Hey there! What can I do for you?',
    'hey':          'Hi! What is on your mind?',
    'how are you':  'I am doing great! How about you?',
    'how are you doing':  'I am doing great! How about you?',
    'same':          'I bet',
    'xup':          'I am doing great! How about you?',
    'good morning': 'Good morning! Have an amazing day! ☀️',
    'good night':   'Good night! Sleep well! 🌙',
    'good afternoon':'Good afternoon! Hope your day is great! 🌤️',
    'good evening': 'Good evening! Hope you had a wonderful day! 🌆',
    'help':         'I respond to: greetings, moods, food, jokes, time, weather, motivation, bye.',
    'weather':      'Always carry an umbrella just in case! 🌂',
    'name':         f'I am {BOT_NAME}, your rule-based chatbot!',
    'who are you':  f'I am {BOT_NAME}, your rule-based chatbot!',
    'thanks':       'You are welcome! 😊',
    'thank you':    'Anytime! That is what I am here for.',
    'i love you': random.choice(["'Love you too', 'then the love is mutual"]),
    'i like you': random.choice(["'Like you too', 'then the love is mutual"]),
    'sorry':        'No worries at all! 😊',
    'bye':          '__EXIT__',
    'exit':         '__EXIT__',
    'quit':         '__EXIT__',
    'see you':      '__EXIT__',
}

# -- Keyword checker: handles natural sentences --
def keyword_response(text):
    # --- Moods ---
    if "sad" in text or "unhappy" in text or "depressed" in text or "anxious" in text:
        return random.choice([
            "I am sorry to hear that. Want to talk about it?",
            "Cheer up! Things will get better 💪",
            "I am here for you. What is going on?",
        ])
    elif "happy" in text or "feel great" in text or "excited" in text:
        return random.choice([
            "That is awesome! Keep that energy going! 🎉",
            "Love to hear it! What is making you happy?",
        ])
    elif "tired" in text or "exhausted" in text or "sleepy" in text:
        return random.choice([
            "You should rest! Sleep is super important 😴",
            "Take a break, you deserve it!",
        ])
    elif "bored" in text:
        return random.choice([
            "Want to hear a joke?!",
            "Boredom is just creativity waiting to happen!",
        ])
    elif "hungry" in text or "need food" in text:
        return random.choice([
            "Time to eat! What are you craving? 🍕",
            "Go grab a snack, that's what your body needs now 🍔. You feel me",
        ])
    elif "stressed" in text or "anxious" in text:
        return random.choice([
            "Take a deep breath. One thing at a time 🧘",
            "Remember to take breaks. You have got this 💪",
        ])
    elif "sick" in text or "ill" in text or "not well" in text:
        return random.choice([
            "Oh no! Please rest and drink lots of water 💧",
            "Feel better soon! Rest is the best medicine.",
        ])

    # ---- Food & Drinks ----
    elif any(word in text for word in ["food", "eat", "lunch", "dinner", "breakfast"]):
        return random.choice([
            "Food talk! 🍽️ I would recommend something healthy today!",
            "Eat well, live well! What is on the menu?",
        ])
    elif any(word in text for word in ["coffee", "tea", "drink"]):
        return random.choice([
            "A coffee lover! ☕ I run on code, not caffeine!",
            "Stay hydrated! Water is great too 💧",
        ])

    # --- Time & Date ---
    elif "time" in text:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now} ⏰"
    elif "date" in text or "today" in text or "what day" in text:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today} 📅"

    # --- Jokes ---
    elif any(word in text for word in ["joke", "funny", "laugh"]):
        jokes = [
            "Why do programmers prefer dark mode? Light attracts bugs! 🐛",
            "How many devs to change a bulb? None, that is a hardware problem!",
            "Why did the computer go to the doctor? It had a virus! 🦠",
        ]
        return random.choice(jokes)

    # --- Motivation ----
    elif any(word in text for word in ["motivate", "inspire", "give up", "motivation"]):
        return random.choice([
            "Keep going! Every expert was once a beginner 💪",
            "You have got this! One step at a time 🚀",
            "Believe in yourself — you are capable of amazing things! 🌟",
        ])

    # --- Personal questions ---
    elif "how old" in text or "your age" in text:
        return "I am ageless! I was born the moment I was coded 🤖"
    elif "where are you from" in text or "where do you live" in text:
        return "I live in the cloud ☁️: everywhere and nowhere!"
    elif "are you human" in text or "are you real" in text:
        return "I am a rule-based AI chatbot; not human, but I try! 🤖"

    return None  # no keyword matched


# --- SINGLE get_response (keep only this one!) ----
def get_response(user_input):
    clean_input = user_input.lower().strip()
    clean_input = re.sub(r'[^\w\s]', '', clean_input)  # remove ? ! . , etc.

    if clean_input in responses:
        return responses[clean_input]

    keyword_result = keyword_response(clean_input)
    if keyword_result:
        return keyword_result

    return random.choice([
        "I did not quite catch that. Try typing 'help'!",
        "Hmm, that is outside my rules for now 😅",
        "I do not understand. Can you rephrase?",
    ])


def run_chatbot():
    display_welcome()

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            response = get_response(user_input)

            if response == '__EXIT__':
                print(f"{BOT_NAME}: Goodbye! Take care 👋")
                break

            def typing_indicator(seconds=2):
                for i in range(seconds * 2):
                    dots = "." * ((i % 3) + 1)
                    print(f"\r{BOT_NAME} is typing{dots:<3}", end="", flush=True)
                    time.sleep(0.5)
                print(f"\r{' ' * 30}\r", end="", flush=True)  # ← clears the typing line

            typing_indicator(2)
            print(f"{BOT_NAME}: {response}\n")

        except KeyboardInterrupt:
            print("\nSession ended. Goodbye!")
            break

if __name__ == "__main__":
    run_chatbot()