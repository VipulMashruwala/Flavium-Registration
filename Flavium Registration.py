from tkinter import*
import calendar
import re
import mysql.connector
class Flavium:
    def __init__(self,win):
        self.win=win
        self.win.title("Flavium 2020 Registration Form")
        self.win.geometry("1200x690")
        self.main_menu = Menu(self.win)

        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label="Submit",command=self.submit_action)
        self.file_menu.add_command(label="Clear",command=self.clear_action)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",command=self.win.destroy)

        self.edit_menu = Menu(self.main_menu, tearoff=0)
        self.edit_menu.add_command(label="Undo")
        self.edit_menu.add_command(label="Redo")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copy")
        self.edit_menu.add_command(label="Cut")
        self.edit_menu.add_command(label="Paste")

        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.win.config(menu=self.main_menu)

        self.flavium_frame = Frame(self.win, bg="#f0ebeb",relief=RIDGE, bd=4)
        self.flavium_frame.place(x=10, y=1, height=70, width=1180)

        self.flavium_label = Label(self.flavium_frame, text="Flavium 2020", font=("Verdana", 25),bg="#f0ebeb")
        self.flavium_label.place(x=275,y=6)

        self.frame=Frame(self.win,bg="crimson",relief=RIDGE,bd=4)
        self.frame.place(x=10,y=75,height=605,width=1180)

        self.button_frame = Frame(self.frame, bg="grey", bd=2, relief=RIDGE)
        self.button_frame.place(x=20, y=520, width=335, height=50)

        self.c=Canvas(win, bg="#f0ebeb",relief=GROOVE, bd=3)
        self.flavium_img=PhotoImage(file="flavium.png")
        self.image=self.c.create_image(310,110,anchor=E,image=self.flavium_img)
        self.c.place(x=850, y=100, height=220, width=320)

        self.mg_title_label = Label(self.frame, text="Register Here", font=("Verdana", 20), bg="crimson",
                               fg="white")
        self.mg_title_label.grid(row=0, columnspan=2, padx=20, pady=10)

        self.name_label = Label(self.frame, text="Player Name : ",bg="crimson",fg="white",font=("Verdana", 12))
        self.name_label.grid(row=1, column=0,padx=5, pady=5)

        self.branch_label = Label(self.frame, text="Branch : ",bg="crimson",fg="white",font=("Verdana", 12))
        self.branch_label.grid(row=2, column=0, padx=5, pady=5)

        self.sapid_label = Label(self.frame, text="Enter SAP ID : ", bg="crimson", fg="white", font=("Verdana", 12))
        self.sapid_label.grid(row=3, column=0, padx=5, pady=5)

        self.sport_label = Label(self.frame, text="Select Sports : ", bg="crimson", fg="white", font=("Verdana", 12))
        self.sport_label.grid(row=5, column=0,padx=5,pady=5)

        self.year_label = Label(self.frame, text="Select Year : ", bg="crimson", fg="white", font=("Verdana", 12))
        self.year_label.grid(row=9, column=0,padx=5, pady=5)

        self.dob_label = Label(self.frame, text="Select DOB : ", bg="crimson", fg="white", font=("Verdana", 12))
        self.dob_label.grid(row=10, column=0, padx=5, pady=5)

        self.name_var = StringVar()
        self.name_entry_box=Entry(self.frame,width=20,textvariable=self.name_var,relief=RIDGE,bd=2,font=("Verdana", 12))
        self.name_entry_box.grid(row=1, column=1, padx=5, pady=5)
        self.name_entry_box.focus()

        self.branch_var = StringVar()
        self.branch_entry_box=Entry(self.frame,width=20,textvariable=self.branch_var,relief=RIDGE,bd=2,font=("Verdana",12))
        self.branch_entry_box.grid(row=2, column=1, padx=5, pady=5)

        self.sapid_var = StringVar()
        self.sapid_entry_box = Entry(self.frame, width=20, textvariable=self.sapid_var,relief=RIDGE, bd=2,
                                      font=("Verdana", 12))
        self.sapid_entry_box.grid(row=3, column=1, padx=5, pady=5)

        self.program_type_var = StringVar()
        self.btech_program= Radiobutton(self.frame, text="B.Tech", value="B.Tech", variable=self.program_type_var,
                                        bg="crimson",fg="white",selectcolor="crimson",font=("Verdana", 12),
                                        tristatevalue=0,activebackground="crimson",activeforeground="white")
        self.btech_program.grid(row=4, column=0)

        self.mbabtech_program = Radiobutton(self.frame, text="MBA Tech",value="MBATech", variable=self.program_type_var,
                                        bg="crimson",fg="white",selectcolor="crimson",font=("Verdana", 12),
                                        tristatevalue=0,activebackground="crimson",activeforeground="white")
        self.mbabtech_program.grid(row=4, column=1)

        self.cricket_checkbtn_var = IntVar()
        self.cricket_checkbtn = Checkbutton(self.frame, text="Cricket    ",
                                        variable=self.cricket_checkbtn_var,bg="crimson",fg="white",font=("Verdana", 12),
                                        activebackground="crimson",activeforeground="white",selectcolor="crimson")
        self.cricket_checkbtn.grid(row=5, columnspan=3)

        self.football_checkbtn_var = IntVar()
        self.football_checkbtn = Checkbutton(self.frame, text="Football   ",
                                    variable=self.football_checkbtn_var,bg="crimson", fg="white", font=("Verdana", 12),
                                             activebackground="crimson",activeforeground="white",selectcolor="crimson")
        self.football_checkbtn.grid(row=6, columnspan=3)

        self.badminton_checkbtn_var = IntVar()
        self.badminton_checkbtn = Checkbutton(self.frame, text="Badminton",
                                    variable=self.badminton_checkbtn_var,bg="crimson", fg="white",font=("Verdana", 12),
                                            activebackground="crimson",activeforeground="white",selectcolor="crimson")
        self.badminton_checkbtn.grid(row=7, columnspan=3)

        self.basketball_checkbtn_var = IntVar()
        self.basketball_checkbtn = Checkbutton(self.frame, text="Basketball",
                                    variable=self.basketball_checkbtn_var,bg="crimson",fg="white",font=("Verdana", 12),
                                            activebackground="crimson",activeforeground="white",selectcolor="crimson")
        self.basketball_checkbtn.grid(row=8, columnspan=3)

        self.year_var = IntVar()
        self.year_spin_box = Spinbox(self.frame,from_=1, to=4,textvariable=self.year_var,width=15,fg='black',bg='white',
                          font=('Verdana', 14),state='readonly')
        self.year_spin_box.grid(row=9,column=1,padx=5, pady=5)

        self.date_text=Text(self.frame,width=3,height=1,relief=RIDGE, bd=2,font=("Verdana", 12),wrap=WORD)
        self.date_text.place(x=150,y=355)

        self.month_text = Text(self.frame, width=9, height=1, relief=RIDGE, bd=2,font=("Verdana", 12),wrap=WORD)
        self.month_text.place(x=200,y=355)

        self.year_text = Text(self.frame, width=10, height=1, relief=RIDGE, bd=2,font=("Verdana", 12),wrap=WORD)
        self.year_text.place(x=310,y=355)

        self.date_list = Listbox(self.frame,font="Verdana 12",fg="black",bg="white",height=4, width=3,selectmode=BROWSE)
        self.date_list.place(x=150,y=400)
        for i in range(1,32):
            self.date_list.insert(END, i)
        self.date_list.bind('<<ListboxSelect>>', self.on_select_date)

        self.month_list = Listbox(self.frame,font="Verdana 12",fg="black",bg="white",height=4,width=9,selectmode=BROWSE)
        self.month_list.place(x=200,y=400)
        for i in range(1,13):
            self.month_list.insert(END,calendar.month_name[i])
        self.month_list.bind('<<ListboxSelect>>', self.on_select_month)

        self.year_list = Listbox(self.frame, font="Verdana 12", fg="black", bg="white", height=4, width=10,
                            selectmode=BROWSE)
        self.year_list.place(x=310,y=400)
        for i in range(1995,2004):
            self.year_list.insert(END, i)
        self.year_list.bind('<<ListboxSelect>>', self.on_select_year)

        self.submit_btn = Button(self.button_frame, text="Submit", width=10,height=1,
                                 command=self.submit_action)
        self.submit_btn.grid(row=0, column=0, padx=10, pady=10)

        self.clear_btn = Button(self.button_frame, text="Clear", width=10,height=1, font=("Verdana", 10),
                                 command=self.clear_action)
        self.clear_btn.grid(row=0, column=1, padx=10, pady=10)

        self.cancel_btn = Button(self.button_frame, text="Cancel", width=10,height=1, font=("Verdana", 10),
                                 command=self.win.destroy)
        self.cancel_btn.grid(row=0, column=2, padx=10, pady=10)

        self.sapid_fetch_label = Label(self.frame, text="Enter SAP ID", bg="crimson", fg="white",font=("Verdana",12))
        self.sapid_fetch_label.place(x=400, y=15)

        self.sapid_fetch_var=StringVar()
        self.sapid_fetch_entry = Entry(self.frame,width=17,textvariable=self.sapid_fetch_var,relief=RIDGE,bd=2,font=("Verdana",12))
        self.sapid_fetch_entry.place(x=520, y=15)

        self.sapid_fetch_button = Button(self.frame,text="Show Data",relief=RIDGE,bd=2,font=("Verdana", 10),
                                         command=self.fetch_button)
        self.sapid_fetch_button.place(x=710, y=15,height=28,width=90)

    def on_select_date(self,event):
        self.ls = []
        indexes = self.date_list.curselection()
        for i in indexes:
            self.ls.append(self.date_list.get(i))
            self.date_text.delete(0.0, END)
            self.date_text.insert(0.0, self.ls)
    def on_select_month(self,event):
        self.ls = []
        indexes = self.month_list.curselection()
        for i in indexes:
            self.ls.append(self.month_list.get(i))
            self.month_text.delete(0.0, END)
            self.month_text.insert(0.0, self.ls)
    def on_select_year(self,event):
        self.ls = []
        indexes = self.year_list.curselection()
        for i in indexes:
            self.ls.append(self.year_list.get(i))
            self.year_text.delete(0.0, END)
            self.year_text.insert(0.0, self.ls)

    def fetch_button(self):
        str=self.sapid_fetch_entry.get()
        conn = mysql.connector.connect(host='localhost',database='Flavium',user='root',password='Vipul2000*')
        cursor = conn.cursor()
        str = "select * from Player where SapID='" + str + "'"
        cursor.execute(str)
        row = cursor.fetchone()
        if row is not None:
            lbl = Label(text=f"Name : {row[0]}\n\n Branch : {row[1]}\n\n SAP ID : {row[2]}\n\n Program : {row[3]}\n\n"
                             f"Year : {row[4]}nd Year\n\n DOB : {row[5]}",
                        font=("Verdana", 12),bg="crimson",fg="white")
            lbl.place(x=520, y=135)
        cursor.close()
        conn.close()

    def submit_action(self):
        new_date=re.findall(r"\d+",self.date_text.get("1.0",END))
        new_month = re.findall(r"\w+", self.month_text.get("1.0",END))
        new_year = re.findall(r"\w+", self.year_text.get("1.0",END))
        dob=f"{new_date[0]}-{new_month[0]}-{new_year[0]}"

        conn = mysql.connector.connect(host='localhost', database='Flavium', user='root', password='Vipul2000*')
        if conn.is_connected():
            print('Connected to MySQL database')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Player values(%s,%s,%s,%s,%s,%s)",(self.name_var.get(),self.branch_var.get(),
                                                                     self.sapid_var.get(),self.program_type_var.get(),
                                                                     self.year_var.get(),dob))
        conn.commit()
        conn.close()

        list = [self.cricket_checkbtn_var.get(), self.football_checkbtn_var.get(),
                self.badminton_checkbtn_var.get(), self.basketball_checkbtn_var.get()]

        sport_list = []
        if list[0] == 1:
            sport_list.append("Cricket")
        if list[1] == 1:
            sport_list.append("Football")
        if list[2] == 1:
            sport_list.append("Badminton")
        if list[3] == 1:
            sport_list.append("Basketball")

        self.detail_frame=Frame(self.win,bg="#f0ebeb",relief=RIDGE, bd=4)
        self.detail_frame.place(x=500,y=350,height=260,width=450)

        self.data_label = Label(text=f"Player Name : {self.name_var.get()}\n\n Branch : {self.branch_var.get()}\n\n"
                                f"SAP ID : {self.sapid_var.get()}\n\n Program : {self.program_type_var.get()}\n\n Sports : {[i for i in sport_list]}\n\n"
                                f"Year : {self.year_var.get()}\n\n DOB : {dob}"
                                ,fg="black",bg="#f0ebeb",
                                font=("Verdana", 11))
        self.data_label.place(x=510,y=360)

        # self.branch_label = Label(self.detail_frame, text=f"Branch : {self.branch_var.get()}",fg="black",bg="#f0ebeb",
        #                           font=("Verdana", 11))
        # self.branch_label.grid(row=1, column=1, padx=5, pady=5)
        #
        # self.sapid_label = Label(self.detail_frame, text=f"SAP ID : {self.sapid_var.get()}", fg="black", bg="#f0ebeb",
        #                           font=("Verdana", 11))
        # self.sapid_label.grid(row=2, column=1, padx=5, pady=5)
        #
        # self.program_label = Label(self.detail_frame, text=f"Program : {self.program_type_var.get()}", fg="black",
        #                            bg="#f0ebeb",font=("Verdana", 11))
        # self.program_label.grid(row=3, column=1, padx=5, pady=5)
        #
        # self.select_sports_label = Label(self.detail_frame, text=f"Sports :\n {[i for i in sport_list]}", fg="black",
        #                            bg="#f0ebeb",
        #                            font=("Verdana", 11))
        # self.select_sports_label.grid(row=4, column=1, padx=5, pady=5)
        #
        # self.year_label = Label(self.detail_frame, text=f"Year : {self.year_var.get()}", fg="black",bg="#f0ebeb",
        #                            font=("Verdana", 11))
        # self.year_label.grid(row=5, column=1, padx=10, pady=10)
        #
        # self.dob_label = Label(self.detail_frame, text=f"DOB : {dob}", fg="black", bg="#f0ebeb",
        #                         font=("Verdana", 11))
        # self.dob_label.grid(row=5, column=1, padx=10, pady=10)

        self.msg_box=Message(self.frame,text="Data Inserted",bg="orange",fg="white",font=("Verdana", 11))
        self.msg_box.place(x=620, y=540, width=200)
        self.clear_action()

    def clear_action(self):
        self.name_entry_box.delete(0, 'end')
        self.branch_entry_box.delete(0, 'end')
        self.sapid_entry_box.delete(0, 'end')
        self.cricket_checkbtn_var.set(0)
        self.football_checkbtn_var.set(0)
        self.badminton_checkbtn_var.set(0)
        self.basketball_checkbtn_var.set(0)
        self.btech_program.deselect()
        self.mbabtech_program.deselect()
        self.date_text.delete("1.0", 'end')
        self.month_text.delete("1.0", 'end')
        self.year_text.delete("1.0", 'end')
        self.year_var.set(1)
win=Tk()
fl=Flavium(win)
win.mainloop()