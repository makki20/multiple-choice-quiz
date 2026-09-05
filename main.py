"""
Multiple Choice Quiz Application
--------------------------------
A simple command-line Python quiz script that evaluates user answers
against a predefined set of questions and outputs the final score.
"""

# List of question dictionaries containing the prompt, choices, and correct answer key
questions = [
    {
        "prompt": "Where is Miami located?",
        "options": ["A. Florida", "B. Washington D.C.", "C. Idaho", "D. New York"],
        "answer": "A",
    },
    {
        "prompt": "What is the capital city of Saudi Arabia?",
        "options": ["A. Riyadh", "B. Dammam", "C. Jeddah", "D. Makkah"],
        "answer": "A",
    },
    {
        "prompt": "What primary language is spoken in Saudi Arabia?",
        "options": ["A. English", "B. Arabic", "C. Spanish", "D. Urdu"],
        "answer": "B",
    },
    {
        "prompt": "Where is the White House located?",
        "options": ["A. New York", "B. Chicago", "C. Washington D.C.", "D. San Diego"],
        "answer": "C",
    },
]


def run_quiz(quiz_questions):
    """
    Iterates through quiz questions, prompts user for input,
    checks responses, and displays final score.
    """
    score = 0

    # Display welcome banner
    print("=== Welcome to the Multiple Choice Quiz ===\n")

    # Loop through each question block
    for question in quiz_questions:
        print(question["prompt"])

        # Display answer options
        for option in question["options"]:
            print(f"  {option}")

        # Get user response, strip whitespace, and normalize to uppercase
        user_answer = input("\nEnter your answer (A, B, C, or D): ").strip().upper()

        # Check if user answer matches the correct answer key
        if user_answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {question['answer']}.\n")

    # Display final results summary
    print("=" * 40)
    print(f"Quiz Complete! Your final score is {score}/{len(quiz_questions)}.")
    print("=" * 40)


if __name__ == "__main__":
    # Execute the quiz
    run_quiz(questions)
