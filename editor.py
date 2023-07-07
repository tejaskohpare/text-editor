import tkinter as tk
from tkinter import filedialog, messagebox, font

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.create_menu()
        self.word_count_label = tk.Label(self.root, text="Word Count: 0")
        self.word_count_label.pack(anchor=tk.SE, padx=10, pady=5)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=self.text_area.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: self.text_area.event_generate("<<Paste>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Find", accelerator="Ctrl+F", command=self.find_text)
        edit_menu.add_command(label="Replace", accelerator="Ctrl+R", command=self.replace_text)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        format_menu = tk.Menu(menubar, tearoff=0)
        format_menu.add_command(label="Font", accelerator="Ctrl+T", command=self.change_font)
        menubar.add_cascade(label="Format", menu=format_menu)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def find_text(self):
        search_text = tk.simpledialog.askstring("Find", "Enter text to find:")
        if search_text:
            text_content = self.text_area.get(1.0, tk.END)
            start_index = text_content.find(search_text)
            if start_index != -1:
                self.text_area.tag_remove("search", 1.0, tk.END)
                end_index = f"{start_index}+{len(search_text)}c"
                self.text_area.tag_add("search", f"1.0+{start_index}c", end_index)
                self.text_area.tag_config("search", background="yellow")
                self.text_area.mark_set(tk.INSERT, f"1.0+{start_index}c")
                self.text_area.see(tk.INSERT)
            else:
                messagebox.showinfo("Find", "Text not found.")

    def replace_text(self):
        search_text = tk.simpledialog.askstring("Replace", "Enter text to find:")
        if search_text:
            replace_text = tk.simpledialog.askstring("Replace", "Enter text to replace:")
            if replace_text:
                text_content = self.text_area.get(1.0, tk.END)
                updated_content = text_content.replace(search_text, replace_text)
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, updated_content)

    def change_font(self):
        selected_font = font.Font(font=self.text_area["font"])
        new_font = font.askfont(self.root, font=selected_font)
        if new_font:
            self.text_area["font"] = new_font

    def update_word_count(self, event=None):
        content = self.text_area.get(1.0, tk.END)
        word_count = len(content.split())
        self.word_count_label.config(text=f"Word Count: {word_count}")

if __name__ == "__main__":
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.bind("<KeyRelease>", text_editor.update_word_count)
    root.mainloop()
