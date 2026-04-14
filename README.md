# PyQuiz - Python Knowledge Tester
A simple, interactive command-line interface (CLI) application built with Python to test your knowledge of basic Python concepts. Whether you're a beginner or just looking for a quick refresher, PyQuiz provides a randomized set of questions to keep you on your toes.

# Features
Randomized Questions: Every session pulls 5 unique questions from a larger question bank, ensuring a different experience each time you play.

Instant Feedback: Find out immediately if your answer was correct, or learn the right answer if you missed it.

Scoring System: Track your performance with a final tally and a personalized encouragement message based on your results.

Wide Topic Coverage: Questions cover data types, operators, string methods, loops, and more.

# How It Works
The quiz uses a structured list of dictionaries to manage question data and the random module to shuffle the deck.

Shuffle: The entire question bank is shuffled.

Select: The script slices the list to select exactly 5 questions.

Loop: It iterates through the selected questions, printing the prompt and options.

Validate: User input is converted to uppercase to prevent case-sensitivity errors and compared against the stored answer.

Score: A final score is calculated and displayed with a custom rating.



# Example Question Format
Each question in the questions list follows this schema:

Python
{
    "q": "What keyword starts a function?",
    "options": ["A) function", "B) def", "C) func", "D) fn"],
    "answer": "B"
}
