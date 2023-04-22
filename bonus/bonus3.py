import json

with open('questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question['questions_text'])
    for i, alternatives in enumerate(question['alternatives']):
        print(f"{i + 1}. {alternatives}")
    answer = int(input("Your answer? "))
    question["user_choice"] = answer

score = 0
for i, question in enumerate(data):
    if question["user_choice"] == question['correct_answer']:
        score = score + 1
        result = "Correct answer"
    else:
        result = "Wrong answer"
    message = f"{i + 1} {result} - Your answer: {question['user_choice']}, Correct answer: {question['correct_answer']}"
    print(message)
results = f"You got {score} / {len(data)} questions right!"
print(results)
