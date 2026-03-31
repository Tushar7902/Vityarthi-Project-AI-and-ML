# 📚 AI Smart Study Planner (CLI Project)

---

## 🧠 About This Project

This project is a **Command Line based AI Study Planner** that suggests:

* What subject you should study
* A proper timetable
* Breaks and revision slots
* Even a small motivation boost

It uses **Machine Learning** to make decisions based on your current situation.

---

## What This Project Does

You simply enter:

* Available study hours
* Backlog level
* Difficulty level
* Your mood
* Your stream (Science / Commerce / Arts)

And the system will:

* Predict the best subject using AI
* Generate a smart timetable
* Suggest breaks
* Save your session history

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* JSON
* Colorama (for colored output)

---

##  How It Works 

Instead of hardcoding everything, I trained a **Machine Learning model**.

 The model learns patterns like:

* If backlog is high → focus serious subjects
* If mood is tired → keep it light
* If difficulty is hard → prioritize wisely

Then:

1. Your inputs are converted into numbers
2. Model predicts best subject
3. System creates a timetable
4. Everything is shown in terminal

---

##  How to Run This Project

### 1. Clone the Repository

```bash
git clone (https://github.com/Tushar7902/Vityarthi-Project-AI-and-ML)
```

---

### 2. Install Requirements

```bash
pip install pandas scikit-learn joblib colorama
```

---

### 3. Run the Chatbot

```bash
python chatbot.py
```

---

## How to Use

After running, you’ll see:

```
📚 ML STUDY PLANNER CHATBOT

1. Get Study Plan
2. View History
3. Exit
```

### Example Flow:

* Enter study hours → 5
* Backlog → medium
* Difficulty → hard
* Mood → tired
* Stream → science

 Output:

* Suggested subject
* Full timetable
* Break schedule
* Motivation message

---

##  Features

* ✅ AI-based subject recommendation
* ✅ Stream-based filtering
* ✅ Smart timetable generation
* ✅ Break management
* ✅ Mood-based suggestions
* ✅ History tracking
* ✅ Input validation

---

## 📂 Project Structure

```
AI-Study-Planner/
│
├── screenshots/            # Images of output (for README/demo)
│
├── README.md              # Project documentation
├── chatbot.py             # Main CLI-based application
├── model.py               # Machine learning model training script
├── generate_data.py       # Script to generate dataset
├── data.csv               # Dataset used for training
│
├── model.pkl              # Trained ML model
├── le_backlog.pkl         # Encoder for backlog
├── le_difficulty.pkl      # Encoder for difficulty
├── le_mood.pkl            # Encoder for mood
├── le_subject.pkl         # Encoder for subject
│
├── history.json           # Stores user session history
├── requirements.txt       # Required dependencies
│
└── (other files if added)
```

---

##  Sample Output

```
Final Subject: Chemistry

Hour 1 → Chemistry
Hour 2 → Math (10 min break)
Hour 3 → Revision
Hour 4 → Physics
...
```

---

##  Challenges I Faced

* Making dataset realistic
* Handling user inputs correctly
* Matching prediction with stream
* Keeping the system simple but useful

---

##  What I Learned

* How ML works in real projects
* Data preprocessing (Label Encoding)
* Building CLI applications
* Writing structured code
* Solving real-life problems using AI

---

##  Limitations

* Dataset is synthetic (not real user data)
* Limited subjects
* No GUI (CLI only as per requirement)

---

##  Future Improvements

* Add GUI or web version
* Use real student data
* Add performance tracking
* Add notifications/reminders

---

##  Final Note

This project is not just about machine learning…
It’s about solving a real student problem in a simple way.

Sometimes, the hardest part of studying is just deciding where to start —
this project tries to make that easier.

---



## 👤 Author

**Author:** Tushar Chauhan 

**Reg No:** 25BAI11335

