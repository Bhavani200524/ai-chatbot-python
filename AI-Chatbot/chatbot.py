
from tkinter import *
from responses import bot_response

def send():
    user = entry.get()
    if user.strip() == "":
        return
    chat.config(state=NORMAL)
    chat.insert(END, "You: " + user + "\n", "user")
    response = bot_response(user)
    chat.insert(END, "Bot: " + response + "\n\n", "bot")
    chat.config(state=DISABLED)
    entry.delete(0, END)
    chat.see(END)
root = Tk()
root.title("AI Chatbot")
root.geometry("600x650")
root.configure(bg="#1e1e1e")
header = Label(
    root,
    text="AI CHATBOT",
    bg="#0f62fe",
    fg="white",
    font=("Arial", 20, "bold"),
    pady=15
)
header.pack(fill=X)
chat = Text(
    root,
    bg="#252526",
    fg="white",
    font=("Arial", 12),
    padx=10,
    pady=10,
    wrap=WORD
)

chat.pack(padx=10, pady=10, fill=BOTH, expand=True)
chat.tag_config("user", foreground="#4FC3F7", font=("Arial", 12, "bold"))
chat.tag_config("bot", foreground="#81C784", font=("Arial", 12, "bold"))
chat.config(state=DISABLED)
bottom_frame = Frame(root, bg="#1e1e1e")
bottom_frame.pack(fill=X, padx=10, pady=10)
entry = Entry(
    bottom_frame,
    font=("Arial", 14),
    bg="#3c3c3c",
    fg="white",
    insertbackground="white",
    relief=FLAT
)
entry.pack(side=LEFT, fill=X, expand=True, ipady=10, padx=(0, 10))
send_button = Button(
    bottom_frame,
    text="Send",
    command=send,
    bg="#0f62fe",
    fg="white",
    font=("Arial", 12, "bold"),
    relief=FLAT,
    padx=20,
    pady=10
)
send_button.pack(side=RIGHT)
root.mainloop()
