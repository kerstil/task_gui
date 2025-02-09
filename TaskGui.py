# graafiline osa
from tkinter import Frame, Text, messagebox
from tkinter.ttk import Combobox, Button, Entry, Label

from Circle import Circle
from Rectangle import Rectangle
from Cone import Cone


class TaskGui:
    def __init__(self, main):

        self.main = main
        main.title("Task GUI") #Võib ka ilma self.antud versioonis
        self.main.geometry("500x280")

        # Frame
        self.frame = Frame(self.main, background="lightgreen")
        self.frame.pack(fill="both", expand=True)

        # Create Combobox
        self.cmb = Combobox(self.frame, values=("Vali kujund", "Ring ", "Ristkülik", "Koonus"))
        self.cmb.current(0)  #Vali kujund
        self.cmb["state"] = "readonly"  # Comboboxi sisu ei saa muuta
        self.cmb.grid(row=0, column=0, padx=3, pady=3,columnspan=2, sticky="ew")


        # Ujuvad vidinad  (Ring ja Ristkülik)
        self.lbl_circle, self.txt_circle = self.create_circle_widget()
        self.lbl_a, self.lbl_b, self.txt_a, self.txt_b = self.create_rectangle_widget()
        self.lbl_r, self.txt_r, self.lbl_h, self.txt_h = self.create_cone_widget()

        # Create button
        self.btn_submit = self.create_button()
        # Create result text
        self.result = self.create_result()


        # Peidame ringi ja Ristküliku "asjad"
        self.forget_circle()  # Unusta või peida ring
        self.forget_rectangle()  # Unusta/Peida ristkülik
        # Kuula comboboxi muutusi
        self.cmb.bind("<<ComboboxSelected>>", self.changed)

    def create_button(self):
        button = Button(self.frame, text="Näita", command=lambda:self.calculate())
        button["state"] = "disabled"
        button.grid(row=3, column=0, padx=3, pady=3, columnspan=2, sticky="ew")
        return button

    def create_result(self):
        result = Text(self.frame, height=5, width=25)
        result.grid(row=4, column=0, padx=3, pady=3, columnspan=2, sticky="ew")
        result["state"] = "disabled"  # Kasti kirjutada ei saa
        return result

    def create_circle_widget(self):
        label = Label(self.frame, text= "Raadius")
        label.grid(row=1, column=0, padx=3, pady=3, sticky="ew")
        text = Entry(self.frame , width=12)
        text.focus()
        text.grid(row=1, column=1, padx=3, pady=3, sticky="ew")

        return label, text

    def create_rectangle_widget(self):
        label_a = Label(self.frame, text= "Külg a")
        label_a.grid(row=1, column=0, padx=3, pady=3, sticky="ew")

        text_a = Entry(self.frame, width=12)
        text_a.focus()
        text_a.grid(row=1, column=1, padx=3, pady=3, sticky="ew")


        label_b = Label(self.frame, text="Külg b")
        label_b.grid(row=2, column=0, padx=3, pady=3, sticky="ew")

        text_b = Entry(self.frame, width=12)
        text_b.grid(row=2, column=1, padx=3, pady=3, sticky="ew")

        return label_a, label_b, text_a, text_b
    
    def create_cone_widget(self):
        label_r = Label(self.frame, text="Raadius")
        label_r.grid(row=1, column=0, padx=3, pady=3, sticky="ew")

        text_r = Entry(self.frame, width=12)
        text_r.focus()
        text_r.grid(row=1, column=1, padx=3, pady=3, sticky="ew")

        label_h = Label(self.frame, text="Kõrgus")
        label_h.grid(row=2, column=0, padx=3, pady=3, sticky="ew")

        text_h = Entry(self.frame, width=12)
        text_h.grid(row=2, column=1, padx=3, pady=3, sticky="ew")

        return label_r, text_r, label_h, text_h
    
    def forget_circle(self):
        self.lbl_circle.grid_forget()
        self.txt_circle.grid_forget()
        self.btn_submit["state"] = "disabled"  # Nuppu ei sa klikkida

    def forget_rectangle(self):
        self.lbl_a.grid_forget()
        self.lbl_b.grid_forget()
        self.txt_a.grid_forget()
        self.txt_b.grid_forget()
        self.btn_submit ["state"] = "disabled"
        
    def forget_cone(self):
        self.lbl_r.grid_forget()
        self.txt_r.grid_forget()
        self.lbl_h.grid_forget()
        self.txt_h.grid_forget()
        self.btn_submit["state"] = "disabled"

    def changed(self, event= None):
        combo_index = self.cmb.current()    # Mitmes valik comboboxist (0, 1, 2)
       # print(combo_index)   # Test
        if combo_index == 0:
            self.forget_circle()
            self.forget_rectangle()
            self.btn_submit ["state"] = "disabled"
        elif combo_index == 1:  # Ring
            self.lbl_circle, self.txt_circle = self.create_circle_widget()
            self.forget_rectangle()
            self.btn_submit ["state"] = "normal"
        elif combo_index == 2:  # Ristkülik
            self.lbl_a, self.lbl_b, self.txt_a, self.txt_b = self.create_rectangle_widget()
            self.forget_circle()
            self.btn_submit ["state"] = "normal"
        elif combo_index == 3:  # Koonus
            self.lbl_r, self.txt_r, self.lbl_h, self.txt_h = self.create_cone_widget()
            self.forget_circle()
            self.forget_rectangle()
            self.btn_submit["state"] = "normal"
        self.clear_result()  # Tulemuskasti sisu kustutamine

    def clear_result(self):
        self.result.config(state="normal")  # tulemuskasti sisu saab muuta
        self.result.delete("1.0", "end")  # Tühjenda tulemuskast
        self.result.config(state="disabled")  # Tulemuskasti sisu EI SAA muuta

    def calculate (self):
        cmb_index = self.cmb.current()
        if cmb_index == 1:
            try:
                radius = float(self.txt_circle.get().strip())  # Loe vormilt raadius ja tee
                circle = Circle(radius)  # Loo objekt Ring
                self.clear_result()  # Tühjenda vastuse kast
                self.result.config(state="normal")  # Vastuse lisamiseks
                self.result.insert("1.0",str(circle))   #Täis vastus klassist Circle
                self.result.config(state="disabled")    # Et vastust ei saaks näppida
                self.txt_circle.delete(0, "end")  # Tühjenda raadiuse kast
                self.txt_circle.focus()


            except ValueError:
                messagebox.showerror("Viga", "Raadius peab olema number.")
            self.txt_circle.delete(0, "end")
            self.txt_circle.focus()

        elif cmb_index == 2:  #Ristkülik

            try:
                rectangle_a = float(self.txt_a.get().strip())
                rectangle_b = float(self.txt_b.get().strip())

                rectangle = Rectangle(rectangle_a, rectangle_b)

                self.clear_result()
                self.result.config(state="normal")

                self.result.insert("1.0",str(rectangle))
                self.result.config(state="disabled")

            except ValueError:
                messagebox.showerror("Viga", " Peab olema nr")

            self.txt_a.delete(0, "end")
            self.txt_b.delete(0, "end")
            self.txt_a.focus()

        elif cmb_index == 3:  # Koonus
    
            try:
                radius = float(self.txt_r.get().strip())
                height = float(self.txt_h.get().strip())
                cone = Cone(radius, height)
        
                self.clear_result()
                self.result.config(state="normal")
                self.result.insert("1.0", str(cone))
                self.result.config(state="disabled")
                self.txt_r.delete(0, "end")
                self.txt_h.delete(0, "end")
                self.txt_r.focus()
    
            except ValueError:
                messagebox.showerror("Viga", "Raadius ja kõrgus peavad olema numbrid.")
        
            self.txt_r.delete(0, "end")
            self.txt_h.delete(0, "end")
            self.txt_r.focus()





































