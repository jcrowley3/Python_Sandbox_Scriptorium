import tkinter as tk
from tkinter import filedialog


class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note App")
        self.root.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Create menu bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Create file menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Create text widget for notes
        self.text_widget = tk.Text(self.root, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill=tk.BOTH)

    def new_file(self):
        self.text_widget.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.INSERT, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_widget.get(1.0, tk.END)
                file.write(content)


if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
