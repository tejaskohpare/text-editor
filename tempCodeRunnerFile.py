 def create_menu(self):
#         menubar = tk.Menu(self.root)
#         file_menu = tk.Menu(menubar, tearoff=0)
#         file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
#         file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
#         file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
#         file_menu.add_separator()
#         file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.root.quit)
#         menubar.add_cascade(label="File", menu=file_menu)
#         self.root.config(menu=menubar)

#         edit_menu = tk.Menu(menubar, tearoff=0)
#         edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.text_area.edit_undo)
#         edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=self.text_area.edit_redo)
#         edit_menu.add_separator()
#         edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: self.text_area.event_generate("<<Cut>>"))
#         edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: self.text_area.event_generate("<<Copy>>"))
#         edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: self.text_area.event_generate("<<Paste>>"))
#         menubar.add_cascade(label="Edit", menu=edit_menu)

#     def new_file(self):
#         self.text_area.delete(1.0, tk.END)

#     def open_file(self):
#         file_path = filedialog.askopenfilename()
#         if file_path:
#             with open(file_path, "r") as file:
#                 self.text_area.delete(1.0, tk.END)
#                 self.text_area.insert(tk.END, file.read())

#     def save_file(self):
#         file_path = filedialog.asksaveasfilename(defaultextension=".txt")
#         if file_path:
#             with open(file_path, "w") as file:
#                 file.write(self.text_area.get(1.0, tk.END))

# if __name__ == "__main__":
#     root = tk.Tk()
#     text_editor = TextEditor(root)
#     root.mainloop()
