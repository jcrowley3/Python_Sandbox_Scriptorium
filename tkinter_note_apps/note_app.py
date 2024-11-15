import json
import tkinter as tk
from tkinter import ttk, messagebox


class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note App")
        self.root.geometry("800x600")

        self.notes = {}
        self.current_note = None

        self.create_widgets()
        self.load_notes()
        self.organize_notes()
        self.get_first_note_id()
        self.open_note()

    def create_widgets(self):
        self.sidebar = ttk.Treeview(self.root, columns=("Title", "Category"))
        self.sidebar.column("#0", width=0, stretch=tk.NO)
        self.sidebar.column("Title", width=200, minwidth=150)
        self.sidebar.column("Category", width=80, minwidth=50)

        self.sidebar.heading("#0", text="")
        self.sidebar.heading("Title", text="Title")
        self.sidebar.heading("Category", text="Category")
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.bind("<<TreeviewSelect>>", self.on_note_selected)

        self.note_content = tk.Frame(self.root)
        self.note_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.toolbar = tk.Frame(self.note_content)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.save_button = tk.Button(self.toolbar, text="Save", command=self.save_current_note)
        self.save_button.pack(side=tk.LEFT)

        self.create_button = tk.Button(self.toolbar, text="Create", command=self.create_note)
        self.create_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.toolbar, text="Delete", command=self.delete_note)
        self.delete_button.pack(side=tk.LEFT)

        self.organize_button = tk.Menubutton(self.toolbar, text="Organize")
        self.organize_button.pack(side=tk.LEFT)

        self.search_button = tk.Button(self.toolbar, text="Search", command=self.search_notes)
        self.search_button.pack(side=tk.LEFT)

        self.search_entry = tk.Entry(self.toolbar)
        self.search_entry.pack(side=tk.LEFT)

        self.info_frame = tk.Frame(self.note_content)
        self.info_frame.pack(side=tk.TOP, fill=tk.X)

        self.title_label = tk.Label(self.info_frame, text="Title:")
        self.title_label.pack(side=tk.LEFT, padx=(5, 0))

        self.title_entry = tk.Entry(self.info_frame)
        self.title_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.category_label = tk.Label(self.info_frame, text="Category:")
        self.category_label.pack(side=tk.LEFT, padx=(5, 0))

        self.category_entry = tk.Entry(self.info_frame)
        self.category_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.filter_var = tk.StringVar(self.root)
        self.filter_var.set("All")

        self.filter_menu = tk.OptionMenu(self.toolbar, self.filter_var, "All", *self.get_unique_categories(), command=self.filter_by_category)
        self.filter_menu.pack(side=tk.LEFT, padx=(0, 5))

        self.note_frame = tk.Frame(self.note_content)
        self.note_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.content = tk.Text(self.note_frame, wrap=tk.WORD)
        self.content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def create_note(self):
        title = "Untitled"
        category = "Uncategorized"
        content = ""

        id_ = self.sidebar.insert("", "end", text=title, values=(title, category))
        self.notes[id_] = {"title": title, "category": category, "content": content}
        self.sidebar.selection_set(id_)
        self.current_note = id_
        self.content.delete(1.0, tk.END)
        self.content.insert(tk.END, content)
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, title)
        self.category_entry.delete(0, tk.END)
        self.category_entry.insert(0, category)

        self.save_notes()

    def delete_note(self):
        if not self.current_note:
            return

        result = messagebox.askquestion("Delete Note", "Are you sure you want to delete this note?")
        if result == "yes":
            self.sidebar.delete(self.current_note)
            del self.notes[self.current_note]
            self.current_note = None
            self.content.delete(1.0, tk.END)

        self.save_notes()

    def search_notes(self):
        query = self.search_entry.get().lower()

        for note in self.notes.values():
            if query in note["title"].lower() or query in note["content"].lower() or query in note["category"].lower():
                self.sidebar.selection_set(note)
                break

    def organize_notes(self):
        categories = []
        for note in self.notes.values():
            if note["category"] not in categories:
                categories.append(note["category"])

        menu = tk.Menu(self.toolbar, tearoff=0)
        for category in categories:
            menu.add_command(label=category, command=lambda c=category: self.filter_notes(c))

        self.organize_button.config(menu=menu)

    def filter_notes(self, category):
        self.sidebar.delete(*self.sidebar.get_children())
        for id_, note in self.notes.items():
            if note["category"] == category:
                self.sidebar.insert("", "end", id_, text=note["title"], values=(note["title"], note["category"]))

    def save_notes(self):
        with open("notes.json", "w") as f:
            json.dump(self.notes, f)
        self.organize_notes()
        self.update_filter_menu()

    def load_notes(self):
        try:
            with open("notes.json", "r") as f:
                self.notes = json.load(f)

            for id_, note in self.notes.items():
                self.sidebar.insert("", "end", id_, text=note["title"], values=(note["title"], note["category"]))
            self.update_filter_menu()
        except FileNotFoundError:
            pass

    def save_current_note(self):
        content = self.content.get(1.0, tk.END).strip()
        title = self.title_entry.get().strip()
        category = self.category_entry.get().strip()
        if self.current_note:
            # update the title and category in the sidbar if they have changed
            if title != self.notes[self.current_note]["title"]:
                self.notes[self.current_note]["title"] = title
                self.sidebar.item(self.current_note, text=title, values=(title, category))
            if category != self.notes[self.current_note]["category"]:
                self.notes[self.current_note]["category"] = category
                self.sidebar.item(self.current_note, text=title, values=(title, category))
            self.save_notes()
        elif self.content:
            title = self.title_entry.get().strip()
            category = self.category_entry.get().strip()
            id_ = self.sidebar.insert("", "end", text=title, values=(title, category))
            self.notes[id_] = {"title": title, "category": category, "content": content}
            self.sidebar.selection_set(id_)
            self.current_note = id_
            self.save_notes()
        else:
            messagebox.showerror("Error", "No note selected.")

    def on_note_selected(self, event):
        selected_id = self.sidebar.selection()[0]

        if self.current_note and self.current_note != selected_id:
            current_content = self.content.get(1.0, tk.END).strip()
            if current_content != self.notes[self.current_note]["content"]:
                result = messagebox.askquestion("Save Note", "Do you want to save the current note before opening the selected note?")
                if result == "yes":
                    self.save_current_note()

        if selected_id in self.notes:
            self.current_note = selected_id
            self.content.delete(1.0, tk.END)
            self.content.insert(tk.END, self.notes[selected_id]["content"])
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(tk.END, self.notes[selected_id]["title"])
            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(tk.END, self.notes[selected_id]["category"])

    # function that gets the first id in self.notes and sets it as the current note
    def get_first_note_id(self):
        if self.notes:
            self.current_note = self.sidebar.get_children()[0]

    def open_note(self):
        if not self.current_note:
            return

        self.content.delete(1.0, tk.END)
        self.content.insert(tk.END, self.notes[self.current_note]["content"])
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(tk.END, self.notes[self.current_note]["title"])
        self.category_entry.delete(0, tk.END)
        self.category_entry.insert(tk.END, self.notes[self.current_note]["category"])

    def get_unique_categories(self):
        categories = set()
        for note in self.notes.values():
            categories.add(note["category"])
        return sorted(list(categories))

    def filter_by_category(self, category):
        self.sidebar.selection_remove(self.sidebar.selection())
        if category == "All":
            for note_id in self.notes:
                self.sidebar.move(note_id, "", "end")
        else:
            for note_id, note in self.notes.items():
                if note["category"] == category:
                    self.sidebar.move(note_id, "", "end")
                else:
                    self.sidebar.move(note_id, "", 0)

    def update_filter_menu(self):
        categories = self.get_unique_categories()
        self.filter_menu["menu"].delete(0, tk.END)
        for category in ["All"] + categories:
            self.filter_menu["menu"].add_command(label=category, command=lambda value=category: self.filter_var.set(value) or self.filter_by_category(value))


if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
