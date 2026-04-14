print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Welcome to PyQuiz - test your Python knowledge")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

import random

# question bank
questions = [
    { "q": "What is the output of: print(2 + 3)?",
        "options": ["A) 5", "B) 23", "C) Error", "D) '5'"],
        "answer": "A"},
    { "q": "Which of the following is a valid variable name in Python?",
        "options": ["A) 1variable", "B) variable_name", "C) variable-name", "D) variable name"],
        "answer": "B"},
    { "q": "What is the output of: print(len('Hello'))?",
        "options": ["A) 4", "B) 5", "C) 6", "D) Error"],
        "answer": "B"},
    { "q": "Which of the following is a Python data type?",
        "options": ["A) String", "B) Integer", "C) List", "D) All of the above"],
        "answer": "D"},
    { "q": "What is the output of: print(10 // 3)?",
        "options": ["A) 3.33", "B) 3", "C) 4", "D) Error"],
        "answer": "B"},
    {
        "q": "Which is used to create a list?",
        "options": ["A) {}", "B) ()", "C) []", "D) <>"],
        "answer": "C"
    },
    {
        "q": "What is the output of: print(5 ** 2)?",
        "options": ["A) 10", "B) 25", "C) 7", "D) Error"],
        "answer": "B"
    },
    {
        "q": "What is the output of: print('Hi' * 2)?",
        "options": ["A) Hi2", "B) HiHi", "C) Hi Hi", "D) Error"],
        "answer": "B"
    },
    {
        "q": "What keyword starts a function?",
        "options": ["A) function", "B) def", "C) func", "D) fn"],
        "answer": "B"
    },
    {
        "q": "How do you write a comment?",
        "options": ["A) // comment", "B) /* comment */", "C) # comment", "D) -- comment"],
        "answer": "C"
    },
    {
        "q": "What does True and False return?",
        "options": ["A) True", "B) False", "C) 1", "D) Error"],
        "answer": "B"
    },
    {
        "q": "What method adds to the end of a list?",
        "options": ["A) add()", "B) push()", "C) append()", "D) insert()"],
        "answer": "C"
    },
    {
        "q": "What is the output of: print(type(5))?",
        "options": ["A) int", "B) <class 'int'>", "C) number", "D) integer"],
        "answer": "B"
    },
    {
        "q": "What is the output of: print(3 > 2)?",
        "options": ["A) True", "B) False", "C) 1", "D) Error"],
        "answer": "A"
    },
    {
        "q": "Which of the following is a loop in Python?",
        "options": ["A) for", "B) while", "C) do-while", "D) Both A and B"],
        "answer": "D"
    },
]

score = 0
random.shuffle(questions) 
questions = questions[:5] 

for q in questions:
    print("\n" + q["q"])
    for option in q["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.")

print(f"\nYour final score is: {score}/{len(questions)}")

if score == 5:
    print("Perfect! 🎉")
elif score >= 3:
    print("Good job! Keep practicing! 👍")
else:
    print("Needs more practice! 📚")
