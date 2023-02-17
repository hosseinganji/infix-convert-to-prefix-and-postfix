from tkinter import *
from tkinter import ttk

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[self.size()-1]

     def size(self):
         return len(self.items)

class InfixConverter:
    def __init__(self):
        self.precedence = {'+':1 , '-':1 , '*':2 , '/':2 , '^':3}

    def hasLessOrEqualPriority(self, a, b):
        if a not in self.precedence:
            return False
        if b not in self.precedence:
            return False
        return self.precedence[a] <= self.precedence[b]

    def isOperand(self, ch):
        return ch.isalpha() or ch.isdigit()

    def isOpenParenthesis(self, ch):
        return ch == '('

    def isCloseParenthesis(self, ch):
        return ch == ')'

    def toPostfix(self, expr):
        expr = expr.replace(" ", "")
        self.stack = Stack()
        output = ''
        for c in expr:
            #for numbers
            if self.isOperand(c): 
                output += c

            #for operators
            else:
                #for open patenthesis
                if self.isOpenParenthesis(c):
                    self.stack.push(c)
                #for close patenthesis
                elif self.isCloseParenthesis(c):
                    operator = self.stack.pop()
                    while not self.isOpenParenthesis(operator):
                        output += operator
                        operator = self.stack.pop()  
                        
                #for other operators            
                else:
                    while (not self.stack.isEmpty()) and self.hasLessOrEqualPriority(c,self.stack.peek()):
                        output += self.stack.pop()

                    self.stack.push(c)

        while (not self.stack.isEmpty()):
            #insert all other elements in stack
            output += self.stack.pop()
        return output
    
    def toPrefix(self, expr):
        reverse_expr =''
        for c in expr[::-1]:
            if c == '(':
                reverse_expr += ")"
            elif c == ')':
                reverse_expr += "("
            else:
                reverse_expr += c
        reverse_postfix = self.toPostfix(reverse_expr)
        return reverse_postfix[::-1]


win= Tk()
win.title("Convert Infix")
win.geometry("500x250")

def display_text():
   global entry
   global string
   string= entry.get()
   Label(win, text= "Infix: " + string, font=("Courier 22 bold")).pack()
   Label(win, text= "Postfix: " + InfixConverter().toPostfix(string), font=("Courier 22 bold")).pack()
   Label(win, text= "Prefix: " + InfixConverter().toPrefix(string), font=("Courier 22 bold")).pack()

entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

win.mainloop()