import tkinter as tk
import re
from tkinter import ttk
import csv
from tkinter import filedialog
from tkinter import messagebox


class TrainScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Расписание пригородных поездов")

        self.tree = ttk.Treeview(root, columns=(
            'Время отправления', 'Время прибытия', 'Номер поезда'), show='headings')
        for col in self.tree['columns']:
            self.tree.heading(col, text=col, anchor='center')
            self.tree.column(col, anchor='center')

        self.tree.pack(expand=True, fill='both')

        tk.Label(root, text="Время отправления:").pack()
        self.entry_departure = tk.Entry(root)
        self.entry_departure.pack()
        tk.Label(root, text="Время прибытия:").pack()
        self.entry_arrival = tk.Entry(root)
        self.entry_arrival.pack()
        tk.Label(root, text="Номер поезда:").pack()
        self.entry_train_number = tk.Entry(root)
        self.entry_train_number.pack()

        self.add_button = tk.Button(
            root, text="Добавить", command=self.add_data)
        self.add_button.config(width=20, height=2)
        self.add_button.pack()

        self.save_button = tk.Button(
            root, text="Сохранить", command=self.save_data)
        self.save_button.config(width=20, height=2)
        self.save_button.pack()
        self.load_button = tk.Button(
            root, text="Загрузить", command=self.load_data)
        self.load_button.config(width=20, height=2)
        self.load_button.pack()

    def add_data(self):
        if self.validate_data(self.entry_departure.get(), self.entry_arrival.get(), self.entry_train_number.get()):
            self.tree.insert('', 'end', values=(self.entry_departure.get(
            ), self.entry_arrival.get(), self.entry_train_number.get()))
        else:
            messagebox.showerror("Ошибка", "Некорректные данные")

    def validate_data(self, departure, arrival, train_number):
        return re.match(r'\d{1,2}:\d{2}', departure.strip()) != None and re.match(r'\d{1,2}:\d{2}', arrival.strip()) != None and train_number.strip().isdigit() == True

    def save_data(self):
        with open(filedialog.asksaveasfilename(defaultextension=".csv"), mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for row_id in self.tree.get_children():
                row = self.tree.item(row_id)['values']
                writer.writerow(row)

    def load_data(self):
        self.tree.delete(*self.tree.get_children())
        with open(filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")]), mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                self.tree.insert('', 'end', values=row)


if __name__ == "__main__":
    root = tk.Tk()
    app = TrainScheduleApp(root)
    root.mainloop()
