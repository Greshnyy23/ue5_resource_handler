import tkinter as tk
from tkinter import filedialog, messagebox
from .ue5_resource_handler import UE5ResourceHandler

class UE5ResourceHandlerGUI:
    def __init__(self, root):
        self.handler = None
        self.root = root
        self.root.title("UE5 Resource Handler GUI")

        self.unrealpak_path = tk.StringVar()
        self.pak_path = tk.StringVar()
        self.extract_dir = tk.StringVar()

        tk.Label(root, text="UnrealPak.exe:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.unrealpak_path, width=40).grid(row=0, column=1)
        tk.Button(root, text="...", command=self.browse_unrealpak).grid(row=0, column=2)

        tk.Label(root, text="PAK-файл:").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.pak_path, width=40).grid(row=1, column=1)
        tk.Button(root, text="...", command=self.browse_pak).grid(row=1, column=2)

        tk.Label(root, text="Каталог для извлечения:").grid(row=2, column=0)
        tk.Entry(root, textvariable=self.extract_dir, width=40).grid(row=2, column=1)
        tk.Button(root, text="...", command=self.browse_extract_dir).grid(row=2, column=2)

        tk.Button(root, text="Извлечь pak", command=self.extract_pak).grid(row=3, column=1)

    def browse_unrealpak(self):
        path = filedialog.askopenfilename(filetypes=[("Executable", "*.exe")])
        if path:
            self.unrealpak_path.set(path)

    def browse_pak(self):
        path = filedialog.askopenfilename(filetypes=[("PAK files", "*.pak")])
        if path:
            self.pak_path.set(path)

    def browse_extract_dir(self):
        path = filedialog.askdirectory()
        if path:
            self.extract_dir.set(path)

    def extract_pak(self):
        try:
            handler = UE5ResourceHandler(self.unrealpak_path.get())
            handler.extract_pak(self.pak_path.get(), self.extract_dir.get())
            messagebox.showinfo("Успех", "Извлечение завершено.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

def main():
    root = tk.Tk()
    app = UE5ResourceHandlerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()