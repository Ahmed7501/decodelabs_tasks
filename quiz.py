questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "How many planets are in our solar system?", "answer": "8"},
    {"question": "What gas do plants absorb from the air?", "answer": "carbon dioxide"}
]

score = 0

for i, q in enumerate(questions, 1):
    print(f"\nQuestion {i}: {q['question']}")
    user_answer = input("Your answer: ").strip().casefold()

    if user_answer == q["answer"]:
        score += 1
        print("Correct! ✓")
    else:
        print(f"Wrong! The answer was: {q['answer']}")

print(f"\nQuiz Complete! Your Score: {score}/3")

if score == 3:
    print("Excellent! Perfect Score!")
elif score == 2:
    print("Good Job!")
elif score == 1:
    print("Keep Practicing!")
else:
    print("Better luck next time!")
