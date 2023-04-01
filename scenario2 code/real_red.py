# things to work on:
# design
# amount of variables
# functions to calculate the result
# implies and the other one
# the submit button

# the check button
# the display answer button
# the generate exercises button

import tkinter as tk
from tkinter import ttk
from tkinter import *
from utils import *
  
 
LARGEFONT =("Verdana", 35, "bold")
MIDFONT =("Verdana", 18, "bold")


class Minterms(object):
    def __init__(self, minterms=None):
        if minterms is None:
            minterms = []
        self.minterms = minterms
        
    def simplify(self):
        return find_essential_prime_implicants(find_prime_implicants(self.minterms), self.minterms)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("KMap Solver")
        self.geometry("600x400")
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, CalcVar, Calc2, Calc3, Calc4, ExerVar, Exercise2, Exercise3, Exercise4, Add2, Add3, Add4):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="KMap Solver", font = LARGEFONT, background='#23c7d9', foreground="red")
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 1, columnspan=4, pady = 10)

        spacing_label = ttk.Label(
            self, text="", background="#23c7d9"
        )
        spacing_label.grid(row = 1, column = 4, pady = 10)

  
        button1 = ttk.Button(self, text ="Simplification Calculator",
        command = lambda : controller.show_frame(CalcVar))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, columnspan=4, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Simplification Exercises",
        command = lambda : controller.show_frame(ExerVar))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, columnspan=4 , pady = 10)
  
          

class CalcVar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Choose The Amount of Variable Used", font = MIDFONT, background='#23c7d9', foreground="red")
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 1, columnspan=4, pady = 10)

        spacing_label = ttk.Label(
            self, text="", background="#23c7d9"
        )
        spacing_label.grid(row = 1, column = 4, pady = 10)

  
        button1 = ttk.Button(self, text ="2",
        command = lambda : controller.show_frame(Calc2))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, columnspan=4, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="3",
        command = lambda : controller.show_frame(Calc3))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, columnspan=4 , pady = 10)

        ## button to show frame 2 with text layout2
        button3 = ttk.Button(self, text ="4",
        command = lambda : controller.show_frame(Calc4))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 3, column = 1, columnspan=4 , pady = 10)

class Calc2(tk.Frame):
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Simplification Calculator", font = LARGEFONT)
        label.grid(row = 0, column = 1, columnspan=4)

        # creating text_input variable
        self.text_input = StringVar()

        self.operator = ""
        self.result = ""
        self.lst = []
        self.str = ""

        input_field = ttk.Entry(self, font=('arial', 18, 'bold'), textvariable=self.text_input,  justify=LEFT, width=50)

        input_field.grid(row=1, column=1, columnspan=4, pady=10)

       
        # first row

        andOp = ttk.Button(self, text = "∧", cursor = "hand2", command = lambda: self.btn_click("∧"))
        andOp.grid(row = 3, column = 1, pady = 1)
        orOp = ttk.Button(self, text = "∨", cursor = "hand2", command = lambda: self.btn_click("∨"))
        orOp.grid(row = 3, column = 2, pady = 1)
        notOp = ttk.Button(self, text = "¬", cursor = "hand2", command = lambda: self.btn_click("¬"))
        notOp.grid(row = 3, column = 3, pady = 1)
        backOp = ttk.Button(self, text = "Back", cursor = "hand2", command = lambda: self.backspace())
        backOp.grid(row = 3, column = 4, pady = 1)

        # second row
        var1 = ttk.Button(self, text = "A", cursor = "hand2", command = lambda: self.btn_click("A"))
        var1.grid(row = 4, column = 1, pady = 1)
        var2 = ttk.Button(self, text = "B", cursor = "hand2", command = lambda: self.btn_click("B"))
        var2.grid(row = 4, column = 2, pady = 1)


        # third row
        var5 = ttk.Button(self, text = "(", cursor = "hand2", command = lambda: self.btn_click("("))
        var5.grid(row = 5, column = 1,   pady = 1)
        var6 = ttk.Button(self, text = ")", cursor = "hand2", command = lambda: self.btn_click(")"))
        var6.grid(row = 5, column = 2,  pady = 1)
        clearOp = ttk.Button(self, text = "Clear", cursor = "hand2", command = lambda: self.btn_clear())
        clearOp.grid(row = 5, column = 3, pady = 1)

        # Change function to submit
        var7 = ttk.Button(self, text = "Submit", cursor = "hand2", command = lambda: self.btn_submit())
        var7.grid(row = 5, column = 4,  pady = 1)
        

        # idk if implies and the other one is needed or not
        # put another row to display the results
        self.label2 = ttk.Label(self, text ="Result: " + self.result)
        self.label2.grid(row = 6, column = 1, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="HomePage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 7, column = 1)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Exercises",
                            command = lambda : controller.show_frame(ExerVar))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 8, column = 1)
    
    

    def btn_click(self, number):
        self.operator = self.operator + str(number)
        self.text_input.set(self.operator)

    def btn_clear(self):
        self.operator
        self.operator = ""
        self.text_input.set("")

    # The function below is wrong
    def btn_submit(self):
        self.label2['text'] = "Result: "
        self.convert()
        self.evaluate()
        self.result = self.finalize(self.lst)
        self.label2['text'] = "Result: " + self.result
        print(self.lst)

    def backspace(self):
        self.operator = self.operator[:-1]
        self.text_input.set(self.operator)
    
    def convert(self):
        self.str = self.operator
        self.str = self.str.replace("∧", " and ")
        self.str = self.str.replace("∨", " or ")
        self.str = self.str.replace("¬", " not ")

    def evaluate(self):
        A, B = 1, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B))
        A, B = 1, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B))
        A, B = 0, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B))
        A, B = 0, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B))

    
    def conversion(self, result):
        conversion_dict_1 = {0:"A", 1:"B", 2:"C", 3:"D"}
        conversion_dict_0 = {0:"¬A", 1:"¬B", 2:"¬C", 3:"¬D"}
        final = []
        for i in result:
            i = str(i)
            string = ""
            for j in range(len(i)):
                if i[j] == "0":
                    string += conversion_dict_0[j]
                elif i[j] == "1":
                    string += conversion_dict_1[j]
            final.append(string)
        final_str = ""
        for i in range(len(final)-1):
            final_str += final[i] + " ∨ "
        final_str += final[-1] 
        return final_str

    def finalize(self, str_terms):
        t_minterms = [Term(term) for term in str_terms]
        minterms = Minterms(t_minterms)
        result = minterms.simplify()
        return self.conversion(result)

class Calc3(tk.Frame):
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Simplification Calculator", font = LARGEFONT)
        label.grid(row = 0, column = 1, columnspan=4)

        # creating text_input variable
        self.text_input = StringVar()

        self.operator = ""
        self.result = ""
        self.lst = []
        self.str = ""

        input_field = ttk.Entry(self, font=('arial', 18, 'bold'), textvariable=self.text_input,  justify=LEFT, width=50)

        input_field.grid(row=1, column=1, columnspan=4, pady=10)

       
        # first row

        andOp = ttk.Button(self, text = "∧", cursor = "hand2", command = lambda: self.btn_click("∧"))
        andOp.grid(row = 3, column = 1, pady = 1)
        orOp = ttk.Button(self, text = "∨", cursor = "hand2", command = lambda: self.btn_click("∨"))
        orOp.grid(row = 3, column = 2, pady = 1)
        notOp = ttk.Button(self, text = "¬", cursor = "hand2", command = lambda: self.btn_click("¬"))
        notOp.grid(row = 3, column = 3, pady = 1)
        backOp = ttk.Button(self, text = "Back", cursor = "hand2", command = lambda: self.backspace())
        backOp.grid(row = 3, column = 4, pady = 1)

        # second row
        var1 = ttk.Button(self, text = "A", cursor = "hand2", command = lambda: self.btn_click("A"))
        var1.grid(row = 4, column = 1, pady = 1)
        var2 = ttk.Button(self, text = "B", cursor = "hand2", command = lambda: self.btn_click("B"))
        var2.grid(row = 4, column = 2, pady = 1)
        var3 = ttk.Button(self, text = "C", cursor = "hand2", command = lambda: self.btn_click("C"))
        var3.grid(row = 4, column = 3,  pady = 1)


        # third row
        var5 = ttk.Button(self, text = "(", cursor = "hand2", command = lambda: self.btn_click("("))
        var5.grid(row = 5, column = 1,   pady = 1)
        var6 = ttk.Button(self, text = ")", cursor = "hand2", command = lambda: self.btn_click(")"))
        var6.grid(row = 5, column = 2,  pady = 1)
        clearOp = ttk.Button(self, text = "Clear", cursor = "hand2", command = lambda: self.btn_clear())
        clearOp.grid(row = 5, column = 3, pady = 1)

        # Change function to submit
        var7 = ttk.Button(self, text = "Submit", cursor = "hand2", command = lambda: self.btn_submit())
        var7.grid(row = 5, column = 4,  pady = 1)
        

        # idk if implies and the other one is needed or not
        # put another row to display the results
        self.label2 = ttk.Label(self, text ="Result: " + self.result)
        self.label2.grid(row = 6, column = 1, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="HomePage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 7, column = 1)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Exercises",
                            command = lambda : controller.show_frame(ExerVar))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 8, column = 1)
    
    

    def btn_click(self, number):
        self.operator = self.operator + str(number)
        self.text_input.set(self.operator)

    def btn_clear(self):
        self.operator
        self.operator = ""
        self.text_input.set("")

    # The function below is wrong
    def btn_submit(self):
        self.label2['text'] = "Result: "
        self.convert()
        self.evaluate()
        self.result = self.finalize(self.lst)
        self.label2['text'] = "Result: " + self.result
        print(self.lst)

    def backspace(self):
        self.operator = self.operator[:-1]
        self.text_input.set(self.operator)
    
    def convert(self):
        self.str = self.operator
        self.str = self.str.replace("∧", " and ")
        self.str = self.str.replace("∨", " or ")
        self.str = self.str.replace("¬", " not ")

    def evaluate(self):
        A, B, C = 1, 1, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C))
        A, B, C = 1, 1, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C))
        A, B, C = 1, 0, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C))
        A, B, C = 0, 1, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C))
        A, B, C = 1, 0, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C))
        A, B, C = 0, 1, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C))
        A, B, C = 0, 0, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C))
        A, B, C = 0, 0, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C))
        

    
    def conversion(self, result):
        conversion_dict_1 = {0:"A", 1:"B", 2:"C", 3:"D"}
        conversion_dict_0 = {0:"¬A", 1:"¬B", 2:"¬C", 3:"¬D"}
        final = []
        for i in result:
            i = str(i)
            string = ""
            for j in range(len(i)):
                if i[j] == "0":
                    string += conversion_dict_0[j]
                elif i[j] == "1":
                    string += conversion_dict_1[j]
            final.append(string)
        final_str = ""
        for i in range(len(final)-1):
            final_str += final[i] + " ∨ "
        final_str += final[-1] 
        return final_str

    def finalize(self, str_terms):
        t_minterms = [Term(term) for term in str_terms]
        minterms = Minterms(t_minterms)
        result = minterms.simplify()
        return self.conversion(result)

# second window frame for simplification calculator
class Calc4(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Simplification Calculator", font = LARGEFONT)
        label.grid(row = 0, column = 1, columnspan=4)

        # creating text_input variable
        self.text_input = StringVar()

        self.operator = ""
        self.result = ""
        self.lst = []
        self.str = ""

        input_field = ttk.Entry(self, font=('arial', 18, 'bold'), textvariable=self.text_input, justify=LEFT, width=50)

        input_field.grid(row=1, column=1, columnspan=4, pady=10)

       
        # first row

        andOp = ttk.Button(self, text = "∧", cursor = "hand2", command = lambda: self.btn_click("∧"))
        andOp.grid(row = 3, column = 1, pady = 1)
        orOp = ttk.Button(self, text = "∨", cursor = "hand2", command = lambda: self.btn_click("∨"))
        orOp.grid(row = 3, column = 2, pady = 1)
        notOp = ttk.Button(self, text = "¬", cursor = "hand2", command = lambda: self.btn_click("¬"))
        notOp.grid(row = 3, column = 3, pady = 1)
        backOp = ttk.Button(self, text = "Back", cursor = "hand2", command = lambda: self.backspace())
        backOp.grid(row = 3, column = 4, pady = 1)

        # second row
        var1 = ttk.Button(self, text = "A", cursor = "hand2", command = lambda: self.btn_click("A"))
        var1.grid(row = 4, column = 1, pady = 1)
        var2 = ttk.Button(self, text = "B", cursor = "hand2", command = lambda: self.btn_click("B"))
        var2.grid(row = 4, column = 2, pady = 1)
        var3 = ttk.Button(self, text = "C", cursor = "hand2", command = lambda: self.btn_click("C"))
        var3.grid(row = 4, column = 3,  pady = 1)
        var4 = ttk.Button(self, text = "D", cursor = "hand2", command = lambda: self.btn_click("D"))
        var4.grid(row = 4, column = 4, pady = 1)


        # third row
        var5 = ttk.Button(self, text = "(", cursor = "hand2", command = lambda: self.btn_click("("))
        var5.grid(row = 5, column = 1,   pady = 1)
        var6 = ttk.Button(self, text = ")", cursor = "hand2", command = lambda: self.btn_click(")"))
        var6.grid(row = 5, column = 2,  pady = 1)
        clearOp = ttk.Button(self, text = "Clear", cursor = "hand2", command = lambda: self.btn_clear())
        clearOp.grid(row = 5, column = 3, pady = 1)

        # Change function to submit
        var7 = ttk.Button(self, text = "Submit", cursor = "hand2", command = lambda: self.btn_submit())
        var7.grid(row = 5, column = 4,  pady = 1)
        

        # idk if implies and the other one is needed or not
        # put another row to display the results
        self.label2 = ttk.Label(self, text ="Result: " + self.result)
        self.label2.grid(row = 6, column = 1, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="HomePage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 7, column = 1)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Exercises",
                            command = lambda : controller.show_frame(ExerVar))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 8, column = 1)
    
    

    def btn_click(self, number):
        self.operator = self.operator + str(number)
        self.text_input.set(self.operator)

    def btn_clear(self):
        self.operator
        self.operator = ""
        self.text_input.set("")

    # The function below is wrong
    def btn_submit(self):
        self.label2['text'] = "Result: "
        self.convert()
        self.evaluate()
        self.result = self.finalize(self.lst)
        self.label2['text'] = "Result: " + self.result
        print(self.lst)

    def backspace(self):
        self.operator = self.operator[:-1]
        self.text_input.set(self.operator)
    
    def convert(self):
        self.str = self.operator
        self.str = self.str.replace("∧", " and ")
        self.str = self.str.replace("∨", " or ")
        self.str = self.str.replace("¬", " not ")

    def evaluate(self):
        A, B, C, D = 1, 1, 1, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 1, 1, 1, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 1, 1, 0, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 1, 0, 1, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 0, 1, 1, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 1, 1, 0, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 1, 0, 1, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 1, 0, 0, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 0, 1, 1, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 0, 1, 0, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 0, 0, 1, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 1, 0, 0, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 0, 1, 0, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 0, 0, 1, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 0, 0, 0, 1
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        A, B, C, D = 0, 0, 0, 0
        if eval(self.str) == 1:
            self.lst.append(str(A) + str(B) + str(C) + str(D))
        

    
    def conversion(self, result):
        conversion_dict_1 = {0:"A", 1:"B", 2:"C", 3:"D"}
        conversion_dict_0 = {0:"¬A", 1:"¬B", 2:"¬C", 3:"¬D"}
        final = []
        for i in result:
            i = str(i)
            string = ""
            for j in range(len(i)):
                if i[j] == "0":
                    string += conversion_dict_0[j]
                elif i[j] == "1":
                    string += conversion_dict_1[j]
            final.append(string)
        final_str = ""
        for i in range(len(final)-1):
            final_str += final[i] + " ∨ "
        final_str += final[-1] 
        return final_str

    def finalize(self, str_terms):
        t_minterms = [Term(term) for term in str_terms]
        minterms = Minterms(t_minterms)
        result = minterms.simplify()
        return self.conversion(result)

class ExerVar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Choose The Amount of Variable Used", font = MIDFONT, background='#23c7d9', foreground="red")
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 1, columnspan=4, pady = 10)

        spacing_label = ttk.Label(
            self, text="", background="#23c7d9"
        )
        spacing_label.grid(row = 1, column = 4, pady = 10)

  
        button1 = ttk.Button(self, text ="2",
        command = lambda : controller.show_frame(Exercise2))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, columnspan=4, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="3",
        command = lambda : controller.show_frame(Exercise3))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, columnspan=4 , pady = 10)

        ## button to show frame 2 with text layout2
        button3 = ttk.Button(self, text ="4",
        command = lambda : controller.show_frame(Exercise4))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 3, column = 1, columnspan=4 , pady = 10)

        button4 = ttk.Button(self, text ="Add Exercises with two variables", command = lambda : controller.show_frame(Add2))
        button4.grid(row = 4, column = 1, columnspan=4, pady = 10)

        button5 = ttk.Button(self, text ="Add Exercises with three variables", command = lambda : controller.show_frame(Add3))
        button5.grid(row = 5, column = 1, columnspan=4, pady = 10)

        button6 = ttk.Button(self, text ="Add Exercises with four variables", command = lambda : controller.show_frame(Add4))
        button6.grid(row = 6, column = 1, columnspan=4, pady = 10)

class Add2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Add Exercises with two variables", font = MIDFONT)
        label.grid(row = 0, column = 1, columnspan=4, pady = 10)
        self.text_box = tk.Text(self, height = 10, width = 30, font = ("Calibri", 11))
        self.text_box.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        open_button = ttk.Button(self, text = "Open", command = self.open_text)
        open_button.grid(row = 2, column = 1, padx = 10, pady = 10)

        save_button = ttk.Button(self, text = "Save", command = self.save_text)
        save_button.grid(row = 2, column = 2, padx = 10, pady = 10)

        homepage = ttk.Button(self, text = "Homepage", command = lambda : controller.show_frame(StartPage))
        homepage.grid(row = 3, column = 1, padx = 10, pady = 10)

    def open_text(self):
        text_file = open("ex2.txt", "r")
        content = text_file.read()
        self.text_box.insert(END, content)
        text_file.close()

    def save_text(self):
        text_file = open("ex2.txt", "w")
        text_file.write(self.text_box.get(1.0, END))
        text_file.close()

class Add3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Add Exercises with three variables", font = MIDFONT)
        label.grid(row = 0, column = 1, columnspan=4, pady = 10)
        self.text_box = tk.Text(self, height = 10, width = 30, font = ("Calibri", 11))
        self.text_box.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        open_button = ttk.Button(self, text = "Open", command = self.open_text)
        open_button.grid(row = 2, column = 1, padx = 10, pady = 10)

        save_button = ttk.Button(self, text = "Save", command = self.save_text)
        save_button.grid(row = 2, column = 2, padx = 10, pady = 10)

        homepage = ttk.Button(self, text = "Homepage", command = lambda : controller.show_frame(StartPage))
        homepage.grid(row = 3, column = 1, padx = 10, pady = 10)

    def open_text(self):
        text_file = open("ex3.txt", "r")
        content = text_file.read()
        self.text_box.insert(END, content)
        text_file.close()

    def save_text(self):
        text_file = open("ex3.txt", "w")
        text_file.write(self.text_box.get(1.0, END))
        text_file.close()

class Add4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Add Exercises with four variables", font = MIDFONT)
        label.grid(row = 0, column = 1, columnspan=4, pady = 10)
        self.text_box = tk.Text(self, height = 10, width = 30, font = ("Calibri", 11))
        self.text_box.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        open_button = ttk.Button(self, text = "Open", command = self.open_text)
        open_button.grid(row = 2, column = 1, padx = 10, pady = 10)

        save_button = ttk.Button(self, text = "Save", command = self.save_text)
        save_button.grid(row = 2, column = 2, padx = 10, pady = 10)
        homepage = ttk.Button(self, text = "Homepage", command = lambda : controller.show_frame(StartPage))
        homepage.grid(row = 3, column = 1, padx = 10, pady = 10)

    def open_text(self):
        text_file = open("ex4.txt", "r")
        content = text_file.read()
        self.text_box.insert(END, content)
        text_file.close()

    def save_text(self):
        text_file = open("ex4.txt", "w")
        text_file.write(self.text_box.get(1.0, END))
        text_file.close()
    
# third window frame for simplification exercises
class Exercise2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Simplification Exercises", font = LARGEFONT)
        label.grid(row = 0, column = 1, columnspan=4)

        f = open("ex2.txt", "r")
        self.str_lst = f.readlines()
        f.close()
        self.cnt = 0
        self.label_exercise = ttk.Label(self, text = self.conversion(eval(self.str_lst[self.cnt][:-1])))
        self.label_exercise.grid(row = 1, column = 1, columnspan=4)
        print(self.str_lst[self.cnt][:-1])
        print(self.conversion(eval(self.str_lst[self.cnt][:-1])))

        label1 = ttk.Label(self, text ="A")
        label1.grid(row = 2, column = 2)
        label2 = ttk.Label(self, text ="A'")
        label2.grid(row = 2, column = 3)
        label3 = ttk.Label(self, text ="B")
        label3.grid(row = 3, column = 1)
        label2 = ttk.Label(self, text ="B'")
        label2.grid(row = 4, column = 1)
        self.buttontxt1 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt1))
        self.buttontxt1.grid(row = 3, column = 2)
        self.buttontxt2 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt2))
        self.buttontxt2.grid(row = 3, column = 3)
        self.buttontxt3 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt3))
        self.buttontxt3.grid(row = 4, column = 2)
        self.buttontxt4 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt4))
        self.buttontxt4.grid(row = 4, column = 3)

        self.result = []
        check = ttk.Button(self, text = "Check", command = lambda: self.check())
        check.grid(row = 5, column = 1)

        answer = ttk.Button(self, text = "Answer", command = lambda: self.answer())
        answer.grid(row = 5, column = 2)

        next_exercise = ttk.Button(self, text = "Next", command = lambda: self.next_exercise())
        next_exercise.grid(row = 5, column = 3)

        self.label1 = ttk.Label(self, text ="")
        self.label1.grid(row = 6, column = 1)
        self.label_result = ttk.Label(self, text ="")
        self.label_result.grid(row = 6, column = 3)
        self.label_check = ttk.Label(self, text ="")
        self.label_check.grid(row = 6, column = 2)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Calculator",
                            command = lambda : controller.show_frame(CalcVar))

        # putting the button in its place by
        # using grid
        button1.grid(row = 8, column = 1)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="HomePage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 7, column = 1)

    def change_text(self, button):
        if button['text'] == "0":
            button['text'] = "1"
        else:
            button['text'] = "0"
        self.result = []
        if self.buttontxt1['text'] == "1":
            self.result.append(self.buttontxt1['text'] + self.buttontxt1['text'])
        if self.buttontxt2['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt2['text'])) + self.buttontxt2['text'])
        if self.buttontxt3['text'] == "1":
            self.result.append(self.buttontxt3['text'] + str(1 - int(self.buttontxt3['text'])))
        if self.buttontxt4['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt4['text'])) + str(1 - int(self.buttontxt4['text'])))
        self.label1['text'] = ""
        print(self.result)
        for i in range(len(self.result)):
            self.label1['text'] += self.result[i]
    
    def next_exercise(self, ):
        if self.cnt == len(self.str_lst)-1:
            self.cnt = 0
        else:
            self.cnt += 1
        self.label_exercise['text'] = self.conversion(eval(self.str_lst[self.cnt][:-1]))
        self.result = []
        self.label1['text'] = ""
        self.label_check['text'] = ""
        self.label_result['text'] = ""
        self.buttontxt1['text'] = "0"
        self.buttontxt2['text'] = "0"
        self.buttontxt3['text'] = "0"
        self.buttontxt4['text'] = "0"
        
    def conversion(self, result):
        conversion_dict_1 = {0:"A", 1:"B", 2:"C", 3:"D"}
        conversion_dict_0 = {0:"¬A", 1:"¬B", 2:"¬C", 3:"¬D"}
        final = []
        for i in result:
            i = str(i)
            string = ""
            for j in range(len(i)):
                if i[j] == "0":
                    string += conversion_dict_0[j]
                elif i[j] == "1":
                    string += conversion_dict_1[j]
            final.append(string)
        final_str = ""
        for i in range(len(final)-1):
            final_str += final[i] + " ∨ "
        final_str += final[-1] 
        return final_str

    def finalize(self, str_terms):
        t_minterms = [Term(term) for term in str_terms]
        minterms = Minterms(t_minterms)
        result = minterms.simplify()
        return self.conversion(result)
    
    def answer(self):
        self.label_result['text'] = self.finalize(eval(self.str_lst[self.cnt][:-1]))

    def check(self):
        if self.finalize(self.result) == self.finalize(eval(self.str_lst[self.cnt][:-1])):
            self.label_check['text'] = "Correct"
        else:
            self.label_check['text'] = "Wrong"

class Exercise3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Simplification Exercises", font = LARGEFONT)
        label.grid(row = 0, column = 1, columnspan=5)

        f = open("ex3.txt", "r")
        self.str_lst = f.readlines()
        f.close()
        self.cnt = 0
        self.label_exercise = ttk.Label(self, text = self.conversion(eval(self.str_lst[self.cnt][:-1])))
        self.label_exercise.grid(row = 1, column = 1, columnspan=4)
        print(self.str_lst[self.cnt][:-1])
        print(self.conversion(eval(self.str_lst[self.cnt][:-1])))

        label1 = ttk.Label(self, text ="AB")
        label1.grid(row = 2, column = 2)
        label2 = ttk.Label(self, text ="AB'")
        label2.grid(row = 2, column = 3)
        label3 = ttk.Label(self, text ="A'B'")
        label3.grid(row = 2, column = 4)
        label4 = ttk.Label(self, text ="A'B")
        label4.grid(row = 2, column = 5)
        label5 = ttk.Label(self, text ="C")
        label5.grid(row = 3, column = 1)
        label6 = ttk.Label(self, text ="C'")
        label6.grid(row = 4, column = 1)
        self.buttontxt1 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt1))
        self.buttontxt1.grid(row = 3, column = 2)
        self.buttontxt2 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt2))
        self.buttontxt2.grid(row = 3, column = 3)
        self.buttontxt3 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt3))
        self.buttontxt3.grid(row = 3, column = 4)
        self.buttontxt4 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt4))
        self.buttontxt4.grid(row = 3, column = 5)
        self.buttontxt5 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt5))
        self.buttontxt5.grid(row = 4, column = 2)
        self.buttontxt6 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt6))
        self.buttontxt6.grid(row = 4, column = 3)
        self.buttontxt7 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt7))
        self.buttontxt7.grid(row = 4, column = 4)
        self.buttontxt8 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt8))
        self.buttontxt8.grid(row = 4, column = 5)

        self.result = []
        check = ttk.Button(self, text = "Check", command = lambda: self.check())
        check.grid(row = 5, column = 1)

        answer = ttk.Button(self, text = "Answer", command = lambda: self.answer())
        answer.grid(row = 5, column = 2)

        next_exercise = ttk.Button(self, text = "Next", command = lambda: self.next_exercise())
        next_exercise.grid(row = 5, column = 3)

        self.label1 = ttk.Label(self, text ="")
        self.label1.grid(row = 6, column = 1)
        self.label_result = ttk.Label(self, text ="")
        self.label_result.grid(row = 6, column = 3)
        self.label_check = ttk.Label(self, text ="")
        self.label_check.grid(row = 6, column = 2)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Calculator",
                            command = lambda : controller.show_frame(CalcVar))

        # putting the button in its place by
        # using grid
        button1.grid(row = 8, column = 1)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="HomePage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 7, column = 1)

    def change_text(self, button):
        if button['text'] == "0":
            button['text'] = "1"
        else:
            button['text'] = "0"
        self.result = []
        if self.buttontxt1['text'] == "1":
            self.result.append(self.buttontxt1['text'] + self.buttontxt1['text'] + self.buttontxt1['text'])
        if self.buttontxt2['text'] == "1":
            self.result.append(self.buttontxt2['text'] + str(1 - int(self.buttontxt2['text'])) + self.buttontxt2['text'])
        if self.buttontxt3['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt3['text'])) + str(1 - int(self.buttontxt3['text'])) + self.buttontxt3['text'])
        if self.buttontxt4['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt4['text'])) + self.buttontxt4['text'] + self.buttontxt4['text'])
        if self.buttontxt5['text'] == "1":
            self.result.append(self.buttontxt5['text'] + self.buttontxt5['text'] + str(1 - int(self.buttontxt5['text'])))
        if self.buttontxt6['text'] == "1":
            self.result.append(self.buttontxt6['text'] + str(1 - int(self.buttontxt6['text'])) + str(1 - int(self.buttontxt6['text'])))
        if self.buttontxt7['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt7['text'])) + str(1 - int(self.buttontxt7['text'])) + str(1 - int(self.buttontxt7['text'])))
        if self.buttontxt8['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt8['text'])) + self.buttontxt8['text'] + str(1 - int(self.buttontxt8['text'])))
        self.label1['text'] = ""
        print(self.result)
        for i in range(len(self.result)):
            self.label1['text'] += self.result[i]
    
    def next_exercise(self, ):
        if self.cnt == len(self.str_lst)-1:
            self.cnt = 0
        else:
            self.cnt += 1
        self.label_exercise['text'] = self.conversion(eval(self.str_lst[self.cnt][:-1]))        
        self.result = []
        self.label1['text'] = ""
        self.label_check['text'] = ""
        self.label_result['text'] = ""
        self.buttontxt1['text'] = "0"
        self.buttontxt2['text'] = "0"
        self.buttontxt3['text'] = "0"
        self.buttontxt4['text'] = "0"
        self.buttontxt5['text'] = "0"
        self.buttontxt6['text'] = "0"
        self.buttontxt7['text'] = "0"
        self.buttontxt8['text'] = "0"
        
    def conversion(self, result):
        conversion_dict_1 = {0:"A", 1:"B", 2:"C", 3:"D"}
        conversion_dict_0 = {0:"¬A", 1:"¬B", 2:"¬C", 3:"¬D"}
        final = []
        for i in result:
            i = str(i)
            string = ""
            for j in range(len(i)):
                if i[j] == "0":
                    string += conversion_dict_0[j]
                elif i[j] == "1":
                    string += conversion_dict_1[j]
            final.append(string)
        final_str = ""
        for i in range(len(final)-1):
            final_str += final[i] + " ∨ "
        final_str += final[-1] 
        return final_str

    def finalize(self, str_terms):
        t_minterms = [Term(term) for term in str_terms]
        minterms = Minterms(t_minterms)
        result = minterms.simplify()
        return self.conversion(result)
    
    def answer(self):
        self.label_result['text'] = self.finalize(eval(self.str_lst[self.cnt][:-1]))

    def check(self):
        if self.finalize(self.result) == self.finalize(eval(self.str_lst[self.cnt][:-1])):
            self.label_check['text'] = "Correct"
        else:
            self.label_check['text'] = "Wrong"

class Exercise4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Simplification Exercises", font = LARGEFONT)
        label.grid(row = 0, column = 1, columnspan=5)

        f = open("ex4.txt", "r")
        self.str_lst = f.readlines()
        f.close()
        self.cnt = 0
        self.label_exercise = ttk.Label(self, text = self.conversion(eval(self.str_lst[self.cnt][:-1])))
        self.label_exercise.grid(row = 1, column = 1, columnspan=4)
        print(self.str_lst[self.cnt][:-1])
        print(self.conversion(eval(self.str_lst[self.cnt][:-1])))

        label1 = ttk.Label(self, text ="AB")
        label1.grid(row = 2, column = 2)
        label2 = ttk.Label(self, text ="AB'")
        label2.grid(row = 2, column = 3)
        label3 = ttk.Label(self, text ="A'B'")
        label3.grid(row = 2, column = 4)
        label4 = ttk.Label(self, text ="A'B")
        label4.grid(row = 2, column = 5)
        label5 = ttk.Label(self, text ="CD")
        label5.grid(row = 3, column = 1)
        label6 = ttk.Label(self, text ="CD'")
        label6.grid(row = 4, column = 1)
        label7 = ttk.Label(self, text ="C'D'")
        label7.grid(row = 5, column = 1)
        label8 = ttk.Label(self, text ="C'D")
        label8.grid(row = 6, column = 1)

        self.buttontxt1 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt1))
        self.buttontxt1.grid(row = 3, column = 2)
        self.buttontxt2 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt2))
        self.buttontxt2.grid(row = 3, column = 3)
        self.buttontxt3 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt3))
        self.buttontxt3.grid(row = 3, column = 4)
        self.buttontxt4 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt4))
        self.buttontxt4.grid(row = 3, column = 5)
        self.buttontxt5 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt5))
        self.buttontxt5.grid(row = 4, column = 2)
        self.buttontxt6 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt6))
        self.buttontxt6.grid(row = 4, column = 3)
        self.buttontxt7 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt7))
        self.buttontxt7.grid(row = 4, column = 4)
        self.buttontxt8 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt8))
        self.buttontxt8.grid(row = 4, column = 5)
        self.buttontxt9 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt9))
        self.buttontxt9.grid(row = 5, column = 2)
        self.buttontxt10 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt10))
        self.buttontxt10.grid(row = 5, column = 3)
        self.buttontxt11 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt11))
        self.buttontxt11.grid(row = 5, column = 4)
        self.buttontxt12 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt12))
        self.buttontxt12.grid(row = 5, column = 5)
        self.buttontxt13 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt13))
        self.buttontxt13.grid(row = 6, column = 2)
        self.buttontxt14 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt14))
        self.buttontxt14.grid(row = 6, column = 3)
        self.buttontxt15 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt15))
        self.buttontxt15.grid(row = 6, column = 4)
        self.buttontxt16 = ttk.Button(self, text =  "0", command = lambda: self.change_text(self.buttontxt16))
        self.buttontxt16.grid(row = 6, column = 5)

        self.result = []
        check = ttk.Button(self, text = "Check", command = lambda: self.check())
        check.grid(row = 7, column = 1)

        answer = ttk.Button(self, text = "Answer", command = lambda: self.answer())
        answer.grid(row = 7, column = 2)

        next_exercise = ttk.Button(self, text = "Next", command = lambda: self.next_exercise())
        next_exercise.grid(row = 7, column = 3)

        self.label1 = ttk.Label(self, text ="")
        self.label1.grid(row = 8, column = 1)
        self.label_result = ttk.Label(self, text ="")
        self.label_result.grid(row = 8, column = 3)
        self.label_check = ttk.Label(self, text ="")
        self.label_check.grid(row = 8, column = 2)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Calculator",
                            command = lambda : controller.show_frame(CalcVar))

        # putting the button in its place by
        # using grid
        button1.grid(row = 10, column = 1)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="HomePage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 9, column = 1)

    def change_text(self, button):
        if button['text'] == "0":
            button['text'] = "1"
        else:
            button['text'] = "0"
        self.result = []
        if self.buttontxt1['text'] == "1":
            self.result.append(self.buttontxt1['text'] + self.buttontxt1['text'] + self.buttontxt1['text'] + self.buttontxt1['text'])
        if self.buttontxt2['text'] == "1":
            self.result.append(self.buttontxt2['text'] + str(1 - int(self.buttontxt2['text'])) + self.buttontxt2['text'] + self.buttontxt2['text'])
        if self.buttontxt3['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt3['text'])) + str(1 - int(self.buttontxt3['text'])) + self.buttontxt3['text'] + self.buttontxt3['text'])
        if self.buttontxt4['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt4['text'])) + self.buttontxt4['text'] + self.buttontxt4['text'] + self.buttontxt4['text'])
        if self.buttontxt5['text'] == "1":
            self.result.append(self.buttontxt5['text'] + self.buttontxt5['text'] + self.buttontxt5['text'] +str(1 - int(self.buttontxt5['text'])))
        if self.buttontxt6['text'] == "1":
            self.result.append(self.buttontxt6['text'] + str(1 - int(self.buttontxt6['text'])) + self.buttontxt6['text'] + str(1 - int(self.buttontxt6['text'])))
        if self.buttontxt7['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt7['text'])) + str(1 - int(self.buttontxt7['text'])) + self.buttontxt6['text'] + str(1 - int(self.buttontxt7['text'])))
        if self.buttontxt8['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt8['text'])) + self.buttontxt8['text'] + self.buttontxt6['text'] + str(1 - int(self.buttontxt8['text'])))
        if self.buttontxt9['text'] == "1":
            self.result.append(self.buttontxt9['text'] + self.buttontxt9['text'] + str(1 - int(self.buttontxt9['text'])) + str(1 - int(self.buttontxt9['text'])))
        if self.buttontxt10['text'] == "1":
            self.result.append(self.buttontxt10['text'] + str(1 - int(self.buttontxt10['text'])) + str(1 - int(self.buttontxt10['text'])) + str(1 - int(self.buttontxt10['text'])))
        if self.buttontxt11['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt11['text'])) + str(1 - int(self.buttontxt11['text'])) + str(1 - int(self.buttontxt11['text'])) + str(1 - int(self.buttontxt11['text'])))
        if self.buttontxt12['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt12['text'])) + self.buttontxt12['text'] + str(1 - int(self.buttontxt12['text'])) + str(1 - int(self.buttontxt12['text'])))
        if self.buttontxt13['text'] == "1":
            self.result.append(self.buttontxt13['text'] + self.buttontxt13['text'] + str(1 - int(self.buttontxt13['text'])) + self.buttontxt13['text'])
        if self.buttontxt14['text'] == "1":
            self.result.append(self.buttontxt14['text'] + str(1 - int(self.buttontxt14['text'])) + str(1 - int(self.buttontxt14['text'])) + self.buttontxt14['text'])
        if self.buttontxt15['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt15['text'])) + str(1 - int(self.buttontxt15['text'])) + str(1 - int(self.buttontxt15['text'])) + self.buttontxt15['text'])
        if self.buttontxt16['text'] == "1":
            self.result.append(str(1 - int(self.buttontxt16['text'])) + self.buttontxt16['text'] + str(1 - int(self.buttontxt16['text'])) + self.buttontxt16['text'])
        
        self.label1['text'] = ""
        print(self.result)
        for i in range(len(self.result)):
            self.label1['text'] += self.result[i]
    
    def next_exercise(self, ):
        if self.cnt == len(self.str_lst)-1:
            self.cnt = 0
        else:
            self.cnt += 1
        self.label_exercise['text'] = self.conversion(eval(self.str_lst[self.cnt][:-1]))        
        self.result = []
        self.label1['text'] = ""
        self.label_check['text'] = ""
        self.label_result['text'] = ""
        self.buttontxt1['text'] = "0"
        self.buttontxt2['text'] = "0"
        self.buttontxt3['text'] = "0"
        self.buttontxt4['text'] = "0"
        self.buttontxt5['text'] = "0"
        self.buttontxt6['text'] = "0"
        self.buttontxt7['text'] = "0"
        self.buttontxt8['text'] = "0"
        self.buttontxt9['text'] = "0"
        self.buttontxt10['text'] = "0"
        self.buttontxt11['text'] = "0"
        self.buttontxt12['text'] = "0"
        self.buttontxt13['text'] = "0"
        self.buttontxt14['text'] = "0"
        self.buttontxt15['text'] = "0"
        self.buttontxt16['text'] = "0"
        
    def conversion(self, result):
        conversion_dict_1 = {0:"A", 1:"B", 2:"C", 3:"D"}
        conversion_dict_0 = {0:"¬A", 1:"¬B", 2:"¬C", 3:"¬D"}
        final = []
        for i in result:
            i = str(i)
            string = ""
            for j in range(len(i)):
                if i[j] == "0":
                    string += conversion_dict_0[j]
                elif i[j] == "1":
                    string += conversion_dict_1[j]
            final.append(string)
        final_str = ""
        for i in range(len(final)-1):
            final_str += final[i] + " ∨ "
        final_str += final[-1] 
        return final_str

    def finalize(self, str_terms):
        t_minterms = [Term(term) for term in str_terms]
        minterms = Minterms(t_minterms)
        result = minterms.simplify()
        return self.conversion(result)
    
    def answer(self):
        self.label_result['text'] = self.finalize(eval(self.str_lst[self.cnt][:-1]))

    def check(self):
        if self.finalize(self.result) == self.finalize(eval(self.str_lst[self.cnt][:-1])):
            self.label_check['text'] = "Correct"
        else:
            self.label_check['text'] = "Wrong"

# Driver Code
app = tkinterApp()
app.mainloop()
