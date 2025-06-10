import tkinter as tk
from tkinter import filedialog, messagebox
from src.ue5_resource_handler import UE5ResourceHandler


class UE5ResourceHandlerGUI:
    def __init__(self, root):
        self.handler = None
        self.root = root
        self.root.title("UE5 Resource Handler")

        # UnrealPak path
        self.unrealpak_label = tk.Label(root, text="Path to UnrealPak:")
        self.unrealpak_label.grid(row=0, column=0, padx=10, pady=10)
        self.unrealpak_entry = tk.Entry(root, width=50)
        self.unrealpak_entry.grid(row=0, column=1, padx=10, pady=10)
        self.unrealpak_button = tk.Button(root, text="Browse", command=self.browse_unrealpak)
        self.unrealpak_button.grid(row=0, column=2, padx=10, pady=10)

        # File selection for .pak
        self.pak_label = tk.Label(root, text=".pak File:")
        self.pak_label.grid(row=1, column=0, padx=10, pady=10)
        self.pak_entry = tk.Entry(root, width=50)
        self.pak_entry.grid(row=1, column=1, padx=10, pady=10)
        self.pak_button = tk.Button(root, text="Browse", command=lambda: self.browse_file(self.pak_entry))
        self.pak_button.grid(row=1, column=2, padx=10, pady=10)

        # Extraction directory
        self.extract_label = tk.Label(root, text="Extract to:")
        self.extract_label.grid(row=2, column=0, padx=10, pady=10)
        self.extract_entry = tk.Entry(root, width=50)
        self.extract_entry.grid(row=2, column=1, padx=10, pady=10)
        self.extract_browse_button = tk.Button(
            root, text="Browse", command=lambda: self.browse_directory(self.extract_entry)
        )
        self.extract_browse_button.grid(row=2, column=2, padx=10, pady=10)

        # Execute extraction
        self.extract_button = tk.Button(root, text="Extract .pak", command=self.extract_pak)
        self.extract_button.grid(row=3, column=1, pady=10)

        # File selection for .ucas and .utoc
        self.ucas_label = tk.Label(root, text=".ucas File:")
        self.ucas_label.grid(row=4, column=0, padx=10, pady=10)
        self.ucas_entry = tk.Entry(root, width=50)
        self.ucas_entry.grid(row=4, column=1, padx=10, pady=10)
        self.ucas_button = tk.Button(root, text="Browse", command=lambda: self.browse_file(self.ucas_entry))
        self.ucas_button.grid(row=4, column=2, padx=10, pady=10)

        self.utoc_label = tk.Label(root, text=".utoc File:")
        self.utoc_label.grid(row=5, column=0, padx=10, pady=10)
        self.utoc_entry = tk.Entry(root, width=50)
        self.utoc_entry.grid(row=5, column=1, padx=10, pady=10)
        self.utoc_button = tk.Button(root, text="Browse", command=lambda: self.browse_file(self.utoc_entry))
        self.utoc_button.grid(row=5, column=2, padx=10, pady=10)

        # Execute parsing
        self.parse_button = tk.Button(root, text="Parse .ucas and .utoc", command=self.parse_ucas_utoc)
        self.parse_button.grid(row=6, column=1, pady=10)

        # File selection for .ubulk
        self.ubulk_label = tk.Label(root, text=".ubulk File:")
        self.ubulk_label.grid(row=7, column=0, padx=10, pady=10)
        self.ubulk_entry = tk.Entry(root, width=50)
        self.ubulk_entry.grid(row=7, column=1, padx=10, pady=10)
        self.ubulk_button = tk.Button(root, text="Browse", command=lambda: self.browse_file(self.ubulk_entry))
        self.ubulk_button.grid(row=7, column=2, padx=10, pady=10)

        # Ubulk extraction directory
        self.ubulk_extract_label = tk.Label(root, text="Export to:")
        self.ubulk_extract_label.grid(row=8, column=0, padx=10, pady=10)
        self.ubulk_extract_entry = tk.Entry(root, width=50)
        self.ubulk_extract_entry.grid(row=8, column=1, padx=10, pady=10)
        self.ubulk_extract_button = tk.Button(root, text="Browse", command=lambda: self.browse_directory(self.ubulk_extract_entry))
        self.ubulk_extract_button.grid(row=8, column=2, padx=10, pady=10)

        # Execute ubulk processing
        self.ubulk_button = tk.Button(root, text="Process .ubulk", command=self.process_ubulk)
        self.ubulk_button.grid(row=9, column=1, pady=10)

    def get_handler(self):
        if not self.handler:
            self.handler = UE5ResourceHandler(self.unrealpak_entry.get())
        return self.handler

    def browse_unrealpak(self):
        path = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
        if path:
            self.unrealpak_entry.delete(0, tk.END)
            self.unrealpak_entry.insert(0, path)

    def browse_file(self, entry):
        path = filedialog.askopenfilename()
        if path:
            entry.delete(0, tk.END)
            entry.insert(0, path)

    def browse_directory(self, entry):
        path = filedialog.askdirectory()
        if path:
            entry.delete(0, tk.END)
            entry.insert(0, path)

    def extract_pak(self):
        pak_path = self.pak_entry.get()
        extract_to = self.extract_entry.get()
        if not all([pak_path, extract_to]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        handler = self.get_handler()
        handler.extract_pak(pak_path, extract_to)
        messagebox.showinfo("Info", "Extraction finished")

    def parse_ucas_utoc(self):
        ucas_path = self.ucas_entry.get()
        utoc_path = self.utoc_entry.get()

        if not all([ucas_path, utoc_path]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        info = self.get_handler().parse_ucas(ucas_path, utoc_path)
        messagebox.showinfo("Info", f"Magic: {info['magic']}\nVersion: {info['version']}")

    def process_ubulk(self):
        ubulk_path = self.ubulk_entry.get()
        export_to = self.ubulk_extract_entry.get()

        if not all([ubulk_path, export_to]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        dest = self.get_handler().extract_ubulk(ubulk_path, export_to)
        messagebox.showinfo("Info", f"Saved to {dest}")


if __name__ == "__main__":
    root = tk.Tk()
    gui = UE5ResourceHandlerGUI(root)
    root.mainloop()
