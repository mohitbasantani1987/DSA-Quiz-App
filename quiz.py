from db import get_connection

def start_quiz(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()

    score = 0

    for q in questions:
        print(f"\n{q[1]}")
        print(f"A. {q[2]}")
        print(f"B. {q[3]}")
        print(f"C. {q[4]}")
        print(f"D. {q[5]}")
        ans = input("Your answer (A/B/C/D): ").upper()

        correct = ans == q[6]
        if correct:
            score += 1

        cursor.execute("""
            INSERT INTO user_answers (user_id, question_id, selected_option, is_correct)
            VALUES (%s, %s, %s, %s)
        """, (user_id, q[0], ans, correct))

    conn.commit()
    conn.close()
    print(f"\nQuiz complete! You scored {score}/{len(questions)}.")
