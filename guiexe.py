import tkinter as tk
from tkinter import ttk, Scrollbar, Text, Entry, Button

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TASKbot")

        # Create a custom style for themed widgets
        style = ttk.Style()
        style.configure("TFrame", background="#4CAF50")
        style.configure("TButton", background="#FF9800", font=("Arial", 12))
        style.configure("TLabel", background="#4CAF50", font=("Arial", 12))
        style.configure("TEntry", font=("Arial", 12))
        style.configure("TText", font=("Arial", 12))

        # Create a Frame for the chat display
        chat_frame = ttk.Frame(root)
        chat_frame.pack(padx=10, pady=10)

        # Create a Text widget for displaying the chat
        self.chat_display = Text(chat_frame, height=20, width=50, state="disabled")
        self.chat_display.pack(side="left", padx=10)

        # Create a Scrollbar for the Text widget
        scrollbar = Scrollbar(chat_frame, command=self.chat_display.yview)
        scrollbar.pack(side="right", fill="y")

        # Set the Scrollbar to control the Text widget
        self.chat_display.config(yscrollcommand=scrollbar.set)

        # Create an Entry widget for user input
        self.user_input = ttk.Entry(root, width=50)
        self.user_input.pack(padx=10, pady=10)

        # Create a Send button to send user input
        send_button = ttk.Button(root, text="Send", command=self.send_message)
        send_button.pack(pady=5)

    def send_message(self):
        user_message = self.user_input.get()
        self.display_message("You: " + user_message)

        # TODO: Add chatbot processing logic here

        # Clear the user input after sending the message
        self.user_input.delete(0, "end")

    def display_message(self, message):
        # Enable the Text widget to append the message
        self.chat_display.config(state="normal")
        self.chat_display.insert("end", message + "\n")
        self.chat_display.config(state="disabled")

# Create the main window
root = tk.Tk()

# Create an instance of the ChatbotGUI class
chatbot_gui = ChatbotGUI(root)

# Run the main event loop
root.mainloop()
