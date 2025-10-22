import tkinter as tk
import google.generativeai as genai
import os

#AI Configuration
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# Send Messages Function
def send_message():
    user_text = entry.get()
    if not user_text.strip():
        return

    chat_box.insert(tk.END, f"You: {user_text}\n", "user")
    entry.delete(0, tk.END)

    try:
        response = model.generate_content(user_text)
        answer = response.text.strip()
        chat_box.insert(tk.END, f"AI: {answer}\n\n", "ai")
    except Exception as e:
        chat_box.insert(tk.END, f"ERRO: {e}\n", "error")

root = tk.Tk()
root.title("AI Chat - Gemini")
root.geometry("600x700")
root.configure(bg="#222")

chat_box = tk.Text(root, wrap="word", bg="#111", fg="white", font=("Arial", 12))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=10, fill=tk.X)

button = tk.Button(root, text="Enviar", font=("Arial", 14), command=send_message)
button.pack(pady=5)

chat_box.tag_config("user", foreground="#00bfff")
chat_box.tag_config("ai", foreground="#98fb98")
chat_box.tag_config("error", foreground="#ff6347")

root.mainloop()