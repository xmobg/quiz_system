import os


class Question:

    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer


def load_questions(file_path):
    questions = []
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return questions

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) < 3:
                continue
            text = parts[0]
            options = parts[1].split(",")
            correct_answer = parts[2]
            questions.append(Question(text, options, correct_answer))
    return questions


def save_score(player_name, score, total_questions):
    with open("leaderboard.txt", "a", encoding="utf-8") as f:
        f.write(f"{player_name}|{score}|{total_questions}\n")


def show_leaderboard():
    print("\n---  LEADERBOARD  ---")
    if not os.path.exists("leaderboard.txt"):
        print("No records yet. Be the first!")
        return

    scores = []
    with open("leaderboard.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, score, total = line.strip().split("|")
            scores.append({"name": name, "score": int(score), "total": total})


    sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)

    for i, entry in enumerate(sorted_scores[:5], 1):
        print(f"{i}. {entry['name']} - {entry['score']}/{entry['total']}")


def run_quiz():

    questions = load_questions("questions.txt")
    if not questions:
        return

    score = 0
    print("Welcome to the Ultimate Python Quiz!\n")

    for q in questions:
        print(f"Question: {q.text}")
        for i, option in enumerate(q.options, 1):
            print(f"  {i}) {option}")

        user_input = input("Your answer: ").strip()

        if user_input.lower() == q.correct_answer.lower():
            print(" Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was: {q.correct_answer}\n")

    print(f"Quiz finished! Final Score: {score}/{len(questions)}")
    name = input("Enter your name for the leaderboard: ")
    save_score(name, score, len(questions))
    show_leaderboard()


if __name__ == "__main__":
    run_quiz()
