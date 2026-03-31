import joblib
import json
import pandas as pd
from datetime import datetime
import random
import sys
import os
from colorama import Fore, init

init(autoreset=True)

model = joblib.load("../model/model.pkl")
le_backlog = joblib.load("../model/le_backlog.pkl")
le_difficulty = joblib.load("../model/le_difficulty.pkl")
le_mood = joblib.load("../model/le_mood.pkl")
le_subject = joblib.load("../model/le_subject.pkl")

def save_history(data):
    path = "../storage/history.json"
    os.makedirs("../storage", exist_ok=True)

    if os.path.exists(path):
        with open(path, "r") as f:
            history = json.load(f)
    else:
        history = []

    data["session"] = len(history) + 1
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M")

    history.append(data)

    with open(path, "w") as f:
        json.dump(history, f, indent=4)


def predict_subject(hours, backlog, difficulty, mood):
    backlog = le_backlog.transform([backlog])[0]
    difficulty = le_difficulty.transform([difficulty])[0]
    mood = le_mood.transform([mood])[0]

    df = pd.DataFrame([[hours, backlog, difficulty, mood]],
                      columns=['hours_available', 'backlog_level', 'subject_difficulty', 'mood'])

    pred = model.predict(df)
    return le_subject.inverse_transform(pred)[0]
def get_subjects_by_stream(stream):
    if stream == "science":
        return ["Physics", "Chemistry", "Math", "Biology"]
    elif stream == "commerce":
        return ["Accounts", "Economics", "Business", "Math"]
    elif stream == "arts":
        return ["History", "Political Science", "Geography", "English"]
    else:
        return ["General Study"]
def smart_subject(hours, backlog, difficulty, mood, stream, custom):
    stream_subjects = get_subjects_by_stream(stream)

    if custom != "":
        return custom

    predicted = predict_subject(hours, backlog, difficulty, mood)

    if predicted not in stream_subjects:
        return random.choice(stream_subjects)

    return predicted

def generate_timetable(main_subject, hours, stream):
    subjects = get_subjects_by_stream(stream) + [main_subject]

    print("\n📅 Smart Study Timetable:\n")
    print(f"{'Hour':<6}{'Activity':<25}{'Break'}")
    print("-" * 55)

    for i in range(1, hours + 1):

        if i % 3 == 0:
            subject = "Revision"
        elif i % 2 == 0:
            subject = random.choice(subjects)
        else:
            subject = main_subject
        if subject == "Physics":
            color = Fore.RED
        elif subject == "Chemistry":
            color = Fore.GREEN
        elif subject == "Math":
            color = Fore.BLUE
        elif subject == "Revision":
            color = Fore.YELLOW
        else:
            color = Fore.WHITE

        subject_colored = color + subject

    
        break_msg = ""
        if i % 5 == 0:
            break_msg = Fore.MAGENTA + "30 min long break"
        elif i % 2 == 0:
            break_msg = Fore.CYAN + "10 min break"

        print(f"{str(i):<6}{subject_colored:<25}{break_msg}")

def give_motivation(mood):
    print("\n Motivation:")
    if mood == "tired":
        print("Start small. Even 1 hour matters ")
    elif mood == "normal":
        print("Stay consistent, you're doing great 📚")
    else:
        print("You're unstoppable today 🚀")

def view_history():
    try:
        with open("../storage/history.json", "r") as f:
            data = json.load(f)

        if not data:
            print("No history found.")
            return

        print("\n History:\n")
        for d in data:
            print(f"Session {d['session']} | {d['timestamp']}")
            print(f"{d['subject']} | {d['hours']} hrs | {d['stream']}")
            print("-" * 30)
    except:
        print("No history found.")

def main():
    print("\n📚 ML STUDY PLANNER CHATBOT\n")

    while True:
        print("\n1. Get Study Plan")
        print("2. View History")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            try:
                hours = int(input("\nEnter available hours: "))

                if hours <= 0:
                    print("❌ Invalid hours")
                    continue
                if hours > 12:
                    print(" Too much study is not effective")
                if hours > 16:
                    print("❌ Max 16 hours allowed")
                    continue
                print("\nBacklog options → none / low / medium / high")
                backlog = input("Enter backlog: ").lower()
                if backlog == "none":
                    backlog = "low"

                if backlog not in ["low", "medium", "high"]:
                    print("❌ Invalid backlog!")
                    continue
                print("\nDifficulty options → easy / medium / hard")
                difficulty = input("Enter difficulty: ").lower()
                if difficulty not in ["easy", "medium", "hard"]:
                    print("❌ Invalid difficulty!")
                    continue
                print("\nMood options → tired / normal / energetic")
                mood = input("Enter mood: ").lower()

                if mood not in ["tired", "normal", "energetic"]:
                    print("❌ Invalid mood!")
                    continue                
                print("\nStream options → science / commerce / arts")
                stream = input("Enter stream: ").lower()

                if stream not in ["science", "commerce", "arts"]:
                    print("❌ Invalid stream!")
                    continue

                
                custom = input("\nEnter subject (or press Enter for AI): ").strip().capitalize()

                subject = smart_subject(hours, backlog, difficulty, mood, stream, custom)

                print(f"\n Final Subject: {subject}")

                generate_timetable(subject, hours, stream)
                give_motivation(mood)

                print("\n Keep your streak going!")

                save_history({
                    "hours": hours,
                    "subject": subject,
                    "stream": stream
                })

            except ValueError:
                print("❌ Enter valid number!")

        elif choice == '2':
            view_history()

        elif choice == '3':
            print("\n🙏 Thank you! Keep following the planner 📚")
            break

        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🙏 Thank you! Keep following the planner ")
        sys.exit(0)
