import tkinter as tk
from logic import process_text


class App:
    def __init__(self, root):
        self.root = root
        root.title("Модульна програма")

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Обробити", command=self.run_logic)
        self.button.pack()

        self.result = tk.Label(root, text="")
        self.result.pack(pady=10)

    def run_logic(self):
        text = self.entry.get()
        self.result.config(text=process_text(text))
