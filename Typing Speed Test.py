import tkinter as tk
import time
import random

# Sentences to type
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing is a valuable skill for programmers.",
    "Python makes automation easier and fun.",
    "Stay calm and type accurately at your pace.",
    "Coding every day improves your thinking."
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x300")
        self.root.resizable(False, False)

        self.text_to_type = random.choice(sentences)
        self.start_time = None

        self.label = tk.Label(root, text="Type this:", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.target_text = tk.Label(root, text=self.text_to_type, wraplength=550,
                                    font=("Courier", 14), fg="blue")
        self.target_text.pack(pady=10)

        self.entry = tk.Entry(root, font=("Courier", 14), width=60)
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>", self.start_timer)
        self.entry.bind("<Return>", self.check_result)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart)
        self.restart_button.pack(pady=5)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def check_result(self, event):
        typed_text = self.entry.get()
        end_time = time.time()

        time_taken = end_time - self.start_time
        wpm = self.calculate_wpm(typed_text, time_taken)
        accuracy = self.calculate_accuracy(self.text_to_type, typed_text)

        self.result_label.config(
            text=f"Time: {round(time_taken, 2)}s | WPM: {wpm} | Accuracy: {accuracy}%"
        )

    def calculate_wpm(self, typed, seconds):
        words = len(typed.split())
        return round((words / seconds) * 60, 2) if seconds > 0 else 0

    def calculate_accuracy(self, original, typed):
        original_words = original.split()
        typed_words = typed.split()
        correct = sum(1 for o, t in zip(original_words, typed_words) if o == t)
        return round((correct / len(original_words)) * 100, 2)

    def restart(self):
        self.text_to_type = random.choice(sentences)
        self.target_text.config(text=self.text_to_type)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = None

# Run the app
root = tk.Tk()
app = TypingSpeedTest(root)
root.mainloop()


