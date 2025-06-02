import tkinter as tk
from tkinter import messagebox
import re

# defined a function to check password strength
def check_password_strength():
    password = entry.get()
    feedback = []
    strength = 0

    # code to check for password criteria
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r"[a-z]", password)
    uppercase_criteria = re.search(r"[A-Z]", password)
    digit_criteria = re.search(r"\d", password)
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if length_criteria: strength += 1
    else: feedback.append("🔸 Use at least 8 characters.")

    if lowercase_criteria: strength += 1
    else: feedback.append("🔸 Add lowercase letters.")

    if uppercase_criteria: strength += 1
    else: feedback.append("🔸 Add uppercase letters.")

    if digit_criteria: strength += 1
    else: feedback.append("🔸 Include numbers.")

    if special_char_criteria: strength += 1
    else: feedback.append("🔸 Include special characters (e.g. !, @, #).")

    # to determine the strength level of the password being inputted
    if strength == 5:
        result_label.config(text="🟢 Strong Password", fg="green")
    elif strength >= 3:
        result_label.config(text="🟡 Moderate Password", fg="orange")
    else:
        result_label.config(text="🔴 Weak Password", fg="red")

    # to display a feedback on passwords
    feedback_text.delete(1.0, tk.END)
    if feedback:
        for item in feedback:
            feedback_text.insert(tk.END, item + "\n")

# for the GUI window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.config(padx=20, pady=20)

# the GUI elements
tk.Label(root, text="Enter Password:", font=("Helvetica", 12)).pack()
entry = tk.Entry(root, width=30, show='*', font=("Helvetica", 12))
entry.pack(pady=10)

tk.Button(root, text="Check Strength", command=check_password_strength, font=("Helvetica", 12), bg="#007acc", fg="white").pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)

tk.Label(root, text="Suggestions:", font=("Helvetica", 12, "underline")).pack()
feedback_text = tk.Text(root, height=5, width=45, font=("Helvetica", 10))
feedback_text.pack()

root.mainloop()