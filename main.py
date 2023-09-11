# 202309.10
# version 0.5

from tkinter import Tk, Button, Text, ttk, Frame
from tkinter.filedialog import askopenfilename
from modules.objects.application_object import ObjectApp
from modules.file_processing import file_processing


class AppNS:
    def __init__(self):
        self.text_output1 = None
        self.root = Tk()
        self.root.title("Перинатальный центр: анализ файлов (НС)")

        self.window_width = 460
        self.window_height = 240

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x_coordinate = int((self.screen_width / 2) - (self.window_width / 2))
        self.y_coordinate = int((self.screen_height / 2) - (self.window_height / 2))

        self.root.geometry(
            '{}x{}+{}+{}'.format(self.window_width, self.window_height, self.x_coordinate, self.y_coordinate))
        self.root.resizable(False, False)

        self.column1 = ttk.Frame(self.root, width=150)
        self.column2 = ttk.Frame(self.root, width=150)
        self.column3 = ttk.Frame(self.root, width=150)

        self.column1.grid(row=0, column=0, sticky='nsew')
        self.column2.grid(row=0, column=1, sticky='nsew')
        self.column3.grid(row=0, column=2, sticky='nsew')
        self.root.grid_columnconfigure(0, weight=1, minsize=150)
        self.root.grid_columnconfigure(1, weight=1, minsize=150)
        self.root.grid_columnconfigure(2, weight=1, minsize=150)

        self.application_object = ObjectApp()

        self.show_upload_file_block()

    def show_upload_file_block(self):
        button1 = Button(self.column1, text="Выберите файл", command=self.button1_click)
        button1.grid(row=0, column=0)

        frame = Frame(self.root)
        frame.grid(row=0, column=1, columnspan=2)

        self.text_output1 = Text(frame, height=5, width=300)
        self.text_output1.pack(fill='x')

    def button1_click(self):
        file_path = askopenfilename()
        self.text_output1.delete(1.0, 'end')
        self.text_output1.insert('end', "Выбранный файл: " + file_path)

        self.application_object.file_path = file_path

        file_processing(self.application_object)

    def main(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = AppNS()
    app.main()
