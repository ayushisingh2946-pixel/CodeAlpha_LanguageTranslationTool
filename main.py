import tkinter as tk
from tkinter import ttk, messagebox

try:
    from deep_translator import GoogleTranslator
except ImportError:
    GoogleTranslator = None

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-CN",
    "Japanese": "ja"
}

def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Warning", "Please enter text.")
            return

        source = languages[source_lang.get()]
        target = languages[target_lang.get()]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END))
    messagebox.showinfo("Copied", "Translated text copied!")

root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("700x500")

tk.Label(root, text="Enter Text", font=("Arial", 12)).pack()

input_text = tk.Text(root, height=8)
input_text.pack(fill="x", padx=10)

frame = tk.Frame(root)
frame.pack(pady=10)

source_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly"
)
source_lang.set("English")
source_lang.grid(row=0, column=0, padx=10)

target_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly"
)
target_lang.set("Hindi")
target_lang.grid(row=0, column=1, padx=10)

translate_btn = tk.Button(
    frame,
    text="Translate",
    command=translate_text
)
translate_btn.grid(row=0, column=2, padx=10)

tk.Label(root, text="Translated Text", font=("Arial", 12)).pack()

output_text = tk.Text(root, height=8)
output_text.pack(fill="x", padx=10)

copy_btn = tk.Button(
    root,
    text="Copy Translation",
    command=copy_text
)
copy_btn.pack(pady=10)

root.mainloop()