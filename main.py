from auth import signup, login
from quiz import start_quiz

def main():
    print("Welcome to the DSA MCQ Quiz CLI App")
    while True:
        print("\n1. Signup\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            signup()
        elif choice == '2':
            user_id = login()
            if user_id:
                start_quiz(user_id)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
