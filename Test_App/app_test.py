from calendar import Calendar
from cgitb import text
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from turtle import onclick
from tkcalendar import DateEntry
from datetime import date
import tkinter , os , json 
from tkinter import ttk
from pathlib import Path
from ttkbootstrap import Style
from os import pipe ,path
from tkinter.tix import *
from tkinter.scrolledtext import ScrolledText
import sys

local       = os.path.dirname(Path(__file__).absolute())
json_name   = "\\cm_config.json"
json_file   = local + json_name
with open(json_file) as json_file:
    data = json.load(json_file)
    
tooltips          = data["tooltips"]
function_Mail     = data["mail"]
function_Board    = data["board"]
function_Vacation = data["vacation"]
menu_List         = data["menu_list"]
folder_List       = data["folder_list"]
result_page_1     = ""
    
class ShowRemove:
    def RemoveTextDomain(event):
        domain_value_text = domain_text.get()
        if domain_value_text == tooltips["domain"]:
            domain_value.delete(0, END)
            domain_value.config(foreground="#000000")

    def RemoveTextId(event):
        id_value_text =  id_text.get()
        if id_value_text == tooltips["id"]:
            id_value.delete(0, END)
            id_value.config(foreground="#000000")

    def RemoveTextPw(event):
        pw_value_text = pw_text.get()
        if pw_value_text == tooltips["pw"]:
            pw_value.delete(0, END)
            pw_value.config(foreground="#000000")

    def RemoveTextEm(event):
        pw_value_text = em_text.get()
        if pw_value_text == tooltips["em"]:
            em_value.delete(0, END)
            em_value.config(foreground="#000000")


    def ShowTextDomain(event):
        domain_value.config(state=NORMAL)
        domain_value_text = domain_text.get()

        if bool(domain_value_text) == False:
            domain_value.insert(0, tooltips["domain"])
            domain_value.config(foreground="#d3d3d3")

    def ShowTextId(event):
        id_value.config(state=NORMAL)
        id_value_text = id_text.get()
        if bool(id_value_text) == False:
            id_value.insert(0, tooltips["id"])
            id_value.config(foreground="#d3d3d3")

    def ShowTextPw(event):
        pw_value.config(state=NORMAL)
        pw_value_text = pw_text.get()

        if bool(pw_value_text) == False:
            pw_value.insert(0, tooltips["pw"])
            pw_value.config(foreground="#d3d3d3")

    def ShowTextEm(event):
        em_value.config(state=NORMAL)
        em_value_text = em_text.get()

        if bool(em_value_text) == False:
            em_value.insert(0, tooltips["em"])
            em_value.config(foreground="#d3d3d3")       

class  CheckBox:
    def SetLocal(cb):
        function_list.text.window_create('end', window=cb)
        function_list.text.insert('end', '\n')
        
    def CheckboxAll():
        global run_all  
        run_all         = tk.BooleanVar()
        checkbox_list   = [mail_checkbox, board_checkbox, contact_checkbox, approval_checkbox, circular_checkbox , todo_checkbox , archive_checkbox ,
                        task_checkbox , project_checkbox, resource_checkbox, expense_checkbox , clouddisk_checkbox, calendar_checkbox, asset_checkbox, 
                        whisper_checkbox , timecard_checkbox, vacation_checkbox, postmaster_checkbox]
        for checkbox in checkbox_list:
            if  all_menus.get() == True:
                checkbox.select()
            else:
                checkbox.deselect()
        if  all_menus.get() == True:
            function_list.text.delete('1.0', tk.END)
            cb = tk.Label(function_list.text, text="All Menus Will Be Run" ,width=45,bg='white', anchor="center")
            function_list.text.window_create('end', window=cb)
            function_list.text.insert('end', '\n')
        else :
            function_list.text.delete('1.0', tk.END)
            cb = tk.Label(function_list.text, text="" ,width=45,bg='white', anchor="center")
    
    def CheckMail():
        if  mail.get() == True :
            if  all_menus.get() == False:
                for name, data1 in function_Mail.items() :
                    cb = tk.Checkbutton(function_list.text, text=data1 ,width=40,bg='white', anchor="w")
                    function_list.text.window_create('end', window=cb)
                    function_list.text.insert('end', '\n')
    
    def CheckBoard():
        global  board_setting
        board_setting       = tk.BooleanVar()
        if  all_menus.get() == False:
            if  board.get() == True :
                cb = tk.Checkbutton(function_list.text, text=function_Board["board_setting"],var=board_setting ,width=40,bg='white', anchor="w")
                CheckBox.SetLocal(cb)
    def CheckVacation():
        global vacation_my , vacation_manager , vacation_admin
        vacation_my      = tk.BooleanVar()
        vacation_admin   = tk.BooleanVar()
        vacation_manager = tk.BooleanVar()
    
        if  all_menus.get() == False:
            if  vacation.get() == True :
                cb = tk.Checkbutton(function_list.text, text=function_Vacation["vacation_my"],var=vacation_my ,width=40,bg='white', anchor="w")
                CheckBox.SetLocal(cb)
                
                cb1 = tk.Checkbutton(function_list.text, text=function_Vacation["vacation_admin"],var=vacation_admin ,width=40,bg='white', anchor="w")
                CheckBox.SetLocal(cb1)
                
                cb2 = tk.Checkbutton(function_list.text, text=function_Vacation["vacation_manager"],var=vacation_manager ,width=40,bg='white', anchor="w")
                CheckBox.SetLocal(cb2)
                
                   
class Function(): 
    def Distance(start,x):
        return start + 40*x
    
    def CheckStart(Domain_Name,Id,Pass):
        Check_Domain   = True
        Check_ID       = True
        Check_Pass     = True
        Check_Menu     = True
        Number_Checked = 0
        Menu_List   = [all_menus.get() , whisper.get() , contact.get()  , approval.get() ,
                        circular.get()   , todo.get()    , archive.get()  , clouddisk.get(),
                        project.get()    , asset.get()   , expense.get()  , calendar.get(),
                        resource.get()   , board.get()   , task.get()     , timecard.get(),
                        vacation.get()   , postmaster.get() 
                        ]
        if  Id == tooltips["id"] :
            tooltips_domain = tooltips["tt_id"]
            id_value.config(foreground="red",highlightbackground="red")
            Check_ID = False
            
        if  Pass == tooltips["pw"] :
            tooltips_domain = tooltips["tt_pw"]
            pw_value.config(foreground="red",highlightbackground="red")
            Check_Pass = False
            
        if  Domain_Name == tooltips["domain"] :
            tooltips_domain = tooltips["tt_domain"]
            domain_value.config(foreground="red",highlightbackground="red")
            Check_Domain = False
            
        for menu in  Menu_List :
            if  menu == True :
                Number_Checked = Number_Checked + 1
        if  Number_Checked == 0 :
            tooltip_menu.config(foreground="red")
            Check_Menu = False
            
        
        if  Check_Domain  == False \
            or Check_ID   == False \
            or Check_Pass == False \
            or Check_Menu == False:
            return False
        else:
            return True
        
    def StartFunction():
        Domain_Name = domain_text.get()
        Id          = id_text.get()
        Pass        = pw_text.get()
        Domain      = tooltips["dm"] % Domain_Name
        Input_Data  = Function.CheckStart(Domain_Name,Id,Pass)
        
        if  Input_Data == True :
            #   Run all Menu
            if  all_menus.get() == True:
                for Menu, Folder in folder_List.items() :
                    local      = os.path.dirname(Path(__file__).absolute())
                    local      = local.replace("Test_App",Folder)
                    sys.path.insert(0, local)
                    match  Menu:
                        case "LUU":
                            from luu_run_file import Luu_My_Execution
                            Luu_My_Execution(Domain)
                        
                        # case "NGOC GW":
                        #     from MN_run_file  import My_Execution
                        #     My_Execution(Domain)
                        # case "NGOC COMANAGE":
                        #     from new_comanage import access_hr , comanage
                        # case "NHU QUYNH":
                        #     from NQ_run_file  import My_Execution
                        #     My_Execution(Domain)
                        case "KIM QUYNH":
                            from vacation_run import run
                            run(Domain_Name,Id,Pass)
                        # case "HANH":
                        #     from H_run_file   import My_Execution
                        #     My_Execution(Domain_Name,Id,Pass)
                return True
            else :
                #checkbutton of KQ :vacation_my , vacation_manager , vacation_admin#
                
                
                if     vacation_my.get()      == True \
                    or vacation_manager().get == True \
                    or vacation_admin().get   == True :
                        
                    local         = os.path.dirname(Path(__file__).absolute())
                    local         = local.replace("Test_App","KQ_Auto")
                    sys.path.insert(0, local)
                        
                    from vacation_run import TestApp
                    ResultLogin , Info_User   =  TestApp.Login(Domain_Name,Id,Pass)
                    if  vacation_my.get()     == True :
                        if ResultLogin        == True : 
                            TestApp.RunSubMyVacation(Info_User)
                    if  vacation_manager.get()== True :
                        if ResultLogin        == True : 
                            TestApp.RunSubManagerProcessing()
                    if  vacation_admin.get()  == True :
                        if ResultLogin        == True : 
                            TestApp.RunSubAdminSettings()
                
                
                #checkbutton of LUU :board_setting#
                if  board_setting.get()      == True :
                    local         = os.path.dirname(Path(__file__).absolute())
                    local         = local.replace("Test_App","Luu_Auto")
                    sys.path.insert(0, local)
                    
                    from luu_run_file import TestApp
                    TestApp.Login(Domain)
                    TestApp.RunBoardSetting(Domain)
                    
                return True
        else :
            return False
            
        


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.container = tk.Frame(self) 
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {} 
        
        for F in (StartPage,Page1):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
            
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        global domain_value, domain_text , canvas , title_x , start_y , content_x
        domain_text  = tk.StringVar()
        height       = 35
        title_x      = 110
        start_y      = 70
        content_x    = 220
        canvas = Canvas(self,width=700,height=750)
        canvas.grid(row=0, column=0, sticky="nsew")

        # Title App #
        Title = tk.Label(canvas,text = "TEST APP",font=('Arial',20,'bold'),fg="black")
        canvas.create_window(300, 10, anchor="nw", window=Title)
        
        # Domain #
        domain_1    = tk.Label(canvas,text = "Domain *",font=('Arial',8,'bold'),fg="#6A6A6A")
        canvas.create_window(title_x,Function.Distance(start_y,0),height=height , anchor="nw", window = domain_1 )

        domain_value = tk.Entry(canvas, textvariable = domain_text,width=59,bg="#F9FAFE",relief="flat",highlightthickness=2)
        domain_value.insert(0, tooltips["domain"])
        domain_value.config(foreground="#d3d3d3")
        domain_value.bind("<FocusIn>", ShowRemove.RemoveTextDomain)
        domain_value.bind("<FocusOut>", ShowRemove.ShowTextDomain)
        canvas.create_window(content_x, Function.Distance(start_y,0),height=height, anchor="nw", window=domain_value)

        # ID #
        global id_value, id_text
        id_text = tk.StringVar()
        
        user_id   = tk.Label(canvas,text = "ID *",font=('Arial',8,'bold'),fg="#6A6A6A")
        canvas.create_window(title_x, Function.Distance(start_y,1), anchor="nw", window=user_id,height=height)
        
        id_value = tk.Entry(canvas, textvariable = id_text,width=59,bg="#F9FAFE",relief="flat",highlightthickness=2)
        id_value.insert(0, tooltips["id"])
        id_value.config(foreground="#d3d3d3")
        id_value.bind("<FocusIn>", ShowRemove.RemoveTextId)
        id_value.bind("<FocusOut>", ShowRemove.ShowTextId)
        canvas.create_window(content_x, Function.Distance(start_y,1), anchor="nw", window=id_value,height=height)

        # Password #
        global pw_value, pw_text
        pw_text = tk.StringVar()
        
        uer_password = tk.Label(canvas,text = "Password *",font=('Arial',8,'bold'),fg="#6A6A6A")
        canvas.create_window(title_x, Function.Distance(start_y,2), anchor="nw", window=uer_password,height=height)

        pw_value = tk.Entry(canvas, textvariable = pw_text,width=59,bg="#F9FAFE",relief="flat",highlightthickness=2)
        pw_value.insert(0, tooltips["pw"])
        pw_value.config(foreground="#d3d3d3")
        pw_value.bind("<FocusIn>", ShowRemove.RemoveTextPw)
        pw_value.bind("<FocusOut>", ShowRemove.ShowTextPw)
        canvas.create_window(content_x, Function.Distance(start_y,2), anchor="nw", window=pw_value,height=height)
        
        # Mail
        global em_value, em_text
        em_text = tk.StringVar()
        
        uer_password = tk.Label(canvas,text = "Email *",font=('Arial',8,'bold'),fg="#6A6A6A")
        canvas.create_window(title_x, Function.Distance(start_y,3), anchor="nw", window=uer_password,height=height)

        placeholder_pw = tooltips["em"]
        em_value = tk.Entry(canvas, textvariable = em_text,width=59,bg="#F9FAFE",relief="flat",highlightthickness=2)
        em_value.insert(0, placeholder_pw)
        em_value.config(foreground="#d3d3d3")
        em_value.bind("<FocusIn>", ShowRemove.RemoveTextEm)
        em_value.bind("<FocusOut>", ShowRemove.ShowTextEm)
        canvas.create_window(content_x, Function.Distance(start_y,3), anchor="nw", window=em_value,height=height)
        
        
        # Menu
        global function_list
        global all_checkbox, mail_checkbox, board_checkbox, contact_checkbox,tooltip_menu
        global approval_checkbox, circular_checkbox, todo_checkbox, archive_checkbox
        global task_checkbox, project_checkbox, resource_checkbox, expense_checkbox
        global clouddisk_checkbox,calendar_checkbox,asset_checkbox, whisper_checkbox
        global timecard_checkbox,vacation_checkbox,postmaster_checkbox
        global all_menus, mail, board, contact, approval, circular , todo , archive , task , postmaster
        global project , resource , expense , calendar , asset , whisper , clouddisk , timecard , vacation
        
        all_menus = tk.BooleanVar()
        mail        = tk.BooleanVar()
        board       = tk.BooleanVar()
        contact     = tk.BooleanVar()
        calendar    = tk.BooleanVar()
        approval    = tk.BooleanVar()
        circular    = tk.BooleanVar()
        todo        = tk.BooleanVar()
        archive     = tk.BooleanVar()
        asset       = tk.BooleanVar()
        whisper     = tk.BooleanVar()
        task        = tk.BooleanVar()
        project     = tk.BooleanVar()
        resource    = tk.BooleanVar()
        expense     = tk.BooleanVar()
        clouddisk   = tk.BooleanVar()
        timecard    = tk.BooleanVar()
        vacation    = tk.BooleanVar()
        postmaster  = tk.BooleanVar()
        

        menu_label = tk.Label(canvas,text = "Menu",font=('Arial',8,'bold'),fg="#6A6A6A")
        canvas.create_window(title_x, Function.Distance(start_y,5), anchor="nw", window=menu_label)

        # Text #
        tooltip_menu = tk.Label(canvas,text = "Select Menu / Function Of Menu To Run",fg="black")
        canvas.create_window(content_x, Function.Distance(start_y,5), anchor="nw", window=tooltip_menu)
        
        # Menu row1 #
        all_checkbox = tk.Checkbutton(canvas, text="All", var=all_menus, command = CheckBox.CheckboxAll)
        canvas.create_window(content_x, Function.Distance(start_y,6), anchor="nw", window=all_checkbox)

        mail_checkbox = tk.Checkbutton(canvas, text="Mail", var=mail, command = CheckBox.CheckMail)
        canvas.create_window(content_x + 100, Function.Distance(start_y,6), anchor="nw", window=mail_checkbox)
       
        board_checkbox = tk.Checkbutton(canvas, text="Board", var=board, command = CheckBox.CheckBoard)
        canvas.create_window(content_x + 200, Function.Distance(start_y,6), anchor="nw", window=board_checkbox)
        
        contact_checkbox = tk.Checkbutton(canvas, text="Contact", var=contact, command = CheckBox.CheckMail)
        canvas.create_window(content_x + 300, Function.Distance(start_y,6), anchor="nw", window=contact_checkbox)

        
        # Menu row2 #
        approval_checkbox = tk.Checkbutton(canvas, text="Approval", var=approval, command = CheckBox.CheckMail)
        canvas.create_window(content_x, Function.Distance(start_y,7), anchor="nw", window=approval_checkbox)

        circular_checkbox = tk.Checkbutton(canvas, text="Circular", var=circular, command = CheckBox.CheckMail)
        canvas.create_window(content_x + 100, Function.Distance(start_y,7), anchor="nw", window=circular_checkbox)

        todo_checkbox = tk.Checkbutton(canvas, text="ToDo", var=todo, command = CheckBox.CheckMail)
        canvas.create_window(content_x + 200, Function.Distance(start_y,7), anchor="nw", window=todo_checkbox)
        
        archive_checkbox = tk.Checkbutton(canvas, text="Archive", var=archive, command = CheckBox.CheckMail)
        canvas.create_window(content_x + 300, Function.Distance(start_y,7), anchor="nw", window=archive_checkbox)

        
        # Menu row3 #
        
        task_checkbox = tk.Checkbutton(canvas, text="Task", var=task, command = CheckBox.CheckMail)
        canvas.create_window(content_x , Function.Distance(start_y,8), anchor="nw", window=task_checkbox)
        
        project_checkbox = tk.Checkbutton(canvas, text="Project", var=project, command = CheckBox.CheckMail)
        canvas.create_window(content_x + 100, Function.Distance(start_y,8), anchor="nw", window =project_checkbox)

        resource_checkbox = tk.Checkbutton(canvas, text="Resource", var=resource, command = CheckBox.CheckMail)
        canvas.create_window(content_x + 200, Function.Distance(start_y,8), anchor="nw", window=resource_checkbox)
        
        expense_checkbox = tk.Checkbutton(canvas, text="Expense", var=expense, command = CheckBox.CheckMail)
        canvas.create_window(content_x + 300, Function.Distance(start_y,8), anchor="nw", window=expense_checkbox)
        
        # Menu row4 #
        
        calendar_checkbox = tk.Checkbutton(canvas, text="Calendar", var=calendar, command = CheckBox.CheckMail)
        canvas.create_window(content_x , Function.Distance(start_y,9), anchor="nw", window=calendar_checkbox)
        
        asset_checkbox = tk.Checkbutton(canvas, text="Asset", var=asset, command = CheckBox.CheckMail)
        canvas.create_window(content_x + 100, Function.Distance(start_y,9), anchor="nw", window=asset_checkbox)

        whisper_checkbox = tk.Checkbutton(canvas, text="Whisper", var=whisper, command = CheckBox.CheckMail)
        canvas.create_window(content_x + 200, Function.Distance(start_y,9), anchor="nw", window=whisper_checkbox)
        
        clouddisk_checkbox = tk.Checkbutton(canvas, text="Clouddisk", var=clouddisk, command = CheckBox.CheckMail)
        canvas.create_window(content_x + 300, Function.Distance(start_y,9), anchor="nw", window=clouddisk_checkbox)
        
        
        # Menu row6 #
        
        timecard_checkbox = tk.Checkbutton(canvas, text="Time Card", var=timecard, command = CheckBox.CheckMail)
        canvas.create_window(content_x , Function.Distance(start_y,10), anchor="nw", window=timecard_checkbox)
        
        vacation_checkbox = tk.Checkbutton(canvas, text="Vacation", var=vacation, command = CheckBox.CheckVacation)
        canvas.create_window(content_x + 100, Function.Distance(start_y,10), anchor="nw", window=vacation_checkbox)

        postmaster_checkbox = tk.Checkbutton(canvas, text="Posmaster", var=postmaster, command = CheckBox.CheckMail)
        canvas.create_window(content_x + 200, Function.Distance(start_y,10), anchor="nw", window=postmaster_checkbox)
        
        function_list = ToggledFrameFunction(canvas, text= 'Select function to run', relief="raised", borderwidth=1 )
        canvas.create_window(content_x , Function.Distance(start_y,11), anchor="nw", window=function_list )

        #Button start #
        start_button = ttk.Button(canvas, text="Start", width=20, command=lambda:self.GetDataForPage1(controller))
        canvas.create_window(320, Function.Distance(start_y,16), anchor="nw", window = start_button)
        
        
    def GetDataForPage1(self,controller):
        Check_Start = Function.StartFunction()
        if  Check_Start == True :
            controller.show_frame(Page1)
            controller.frames[Page1].Load_UI()
       
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.height       = 35
        self.title_x      = 110
        self.start_Y      = 100
        self.content_x    = 190
       
    def Load_UI(self)  :
    
        canvas = Canvas(self,width=700,height=600,relief=RIDGE,background="red")
        canvas.grid(row=0, column=0, sticky="nsew")
        
        '''
        # Title App #
        Title = tk.Label(canvas,text = "TEST APP",font=('Arial',20,'bold'),fg="black")
        canvas.create_window(self.content_x, 0, anchor="nw", window=Title)
        
        # Back #
        back = tk.Label(self,text = "Back to main page",font=('Arial',8,'bold'),fg="#6A6A6A")
        canvas.create_window(self.title_x, Function.Distance(self.start_Y,0),height=30 , anchor="nw", window=back )

        # Button Move #
        move_spam_btn = ttk.Button(canvas, text="Move to Spam", width=15, command="")
        canvas.create_window(self.content_x + 200, Function.Distance(self.start_Y,0),height=30 , anchor="nw", window=move_spam_btn)

        # Button Mark #
        mark_read_btn = ttk.Button(canvas, text="Mark as read", width=15)
        canvas.create_window(self.content_x + 300, Function.Distance(self.start_Y,0),height=30 , anchor="nw", window=mark_read_btn)
        '''
        # Title App #
        Title = tk.Label(canvas,text = "TEST APP",font=('Arial',20,'bold'),fg="black")
        canvas.create_window(self.content_x, 0, anchor="nw", window=Title)
        
        Finished = tk.Label(canvas, text= "Finished Running" ,width=45,bg='white', anchor="center")
        canvas.create_window(self.title_x + 100, Function.Distance(self.start_Y,0),height=30 , anchor="nw", window=Finished )
       

class ToggledFrame(tk.Frame):

    def __init__(self, parent,controller, text="", *args, **options):
        tk.Frame.__init__(self, parent, *args, **options)
        
        self.show = tk.IntVar()
        self.show.set(0)

        self.title_frame = ttk.Frame(self)
        self.title_frame.pack(fill="x", expand=1)

        ttk.Label(self.title_frame, text=text , width=65 ).pack(side="left")
        self.toggle_button = ttk.Checkbutton(self.title_frame, width=10, text='Hide List', command=self.toggle,
                                            variable=self.show, style='Toolbutton')
        self.toggle_button.pack(side="left")
        self.sub_frame = tk.Frame(self)
       
    def toggle(self):
        if bool(self.show.get()):
            self.sub_frame.pack(fill="x", expand=1)
            self.toggle_button.configure(text='Hide List')
        else:
            self.sub_frame.forget()
            
            self.toggle_button.configure(text='View List')


class ToggledFrameFunction(tk.Frame):
    
    def __init__(self, parent, text="", *args, **options):
        tk.Frame.__init__(self, parent, *args, **options)

        self.show = tk.IntVar()
        self.show.set(0)

        title_frame = ttk.Frame(self)
        title_frame.pack(fill="x", expand=1)
        
        ttk.Label(title_frame, text=text , width= 52).pack(side="left", fill="x", expand=1 )

        self.toggle_button = ttk.Checkbutton(title_frame, width=2, text='+', command=self.toggle,
                                            variable=self.show, style='Toolbutton')
        self.toggle_button.pack(side="left")

        self.sub_frame = tk.Frame(self, relief="sunken", borderwidth=1)
        
        self.text = ScrolledText(self.sub_frame, width=54, height=10 , bd=0)
        self.text.pack()
        
    
    def toggle(self):
        if bool(self.show.get()):
            self.sub_frame.pack(fill="x", expand=1)
            self.toggle_button.configure(text='-')
            
        else:
            self.sub_frame.forget()
            self.toggle_button.configure(text='+')
            
def MainUI():
    app = tkinterApp()
    app.resizable(True, True)
    app.mainloop()
    
MainUI()

