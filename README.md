# prime-number-or-not
🔢 Prime Number Checker (Python)

A simple Python program that checks whether a given number is a prime number or not, using a for loop and conditional statements.

This project is ideal for beginners learning Python fundamentals.

📌 Features

📥 Takes number input from the user

🔁 Uses a for loop for divisibility check

⚖️ Determines prime or non-prime numbers

🧠 Demonstrates for-else logic

🧑‍🎓 Beginner-friendly code

🛠️ Technologies Used

Python 3

Conditional statements (if-else)

Looping (for)

Modulus operator (%)

📂 Project Structure
Prime-Number-Checker/
│
├── prime_checker.py   # Main Python file
└── README.md          # Project documentation

▶️ How to Run the Program
1️⃣ Clone the Repository
git clone https://github.com/your-username/Prime-Number-Checker.git

2️⃣ Navigate to the Project Folder
cd Prime-Number-Checker

3️⃣ Run the Program
python prime_checker.py

🧪 Example Output
Input
Enter a number: 7

Output
It is a prime number

Input
Enter a number: 9

Output
Not a prime number

📄 Source Code
num1 = int(input("Enter a number: "))

if num1 > 1:
    for i in range(2, num1):
        if num1 % i == 0:
            print("Not a prime number")
            break
    else:
        print("It is a prime number")
else:
    print("Not a prime number")

🧠 How the Logic Works

Numbers ≤ 1 are not prime

The loop checks divisibility from 2 to num - 1

If divisible → not prime

If no divisors found → prime

for-else executes else only if loop does not break

📚 Learning Outcomes

This project helps you understand:

Prime number logic

for-else loop usage

Conditional statements

Modulus operator

Basic algorithm thinking

🚀 Future Enhancements

Optimize using sqrt(n)

Validate input (handle negative numbers)

Check multiple numbers at once

GUI version using Tkinter

👨‍💻 Author

Syam Sundar
📍 India
💡 Python Beginner | Java | Programming Enthusiast

📄 License

This project is open-source and free to use for educational purposes.

⭐ If you find this project useful, please star the repository on GitHub!

If you want:

✅ Optimized version

✅ Interview explanation

✅ Flowchart

✅ Resume project description
