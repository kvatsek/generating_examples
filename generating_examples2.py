from tkinter import *
import random
w=Tk()
w.title(" Генерируем примеры")
w.geometry('500x500')
operation = 0
nb = 0

def sms(list):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    e = a + b
    f = c + d
    g = max(a, b) - min(a, b)
    h = max(c, d) - min(c, d)
    if f != 0 and e % f == 0:
        k = e // f
        str0 = "(" + str(a) + " + " + str(b) + ") : (" + str(c) + " + " + str(d) + ") = \n"
        str1 = str(k) + "\n"
    elif e != 0 and f % e == 0:
        k = f // e
        str0 = "(" + str(c) + " + " + str(d) + ") : (" + str(a) + " + " + str(b) + ") = \n"
        str1 = str(k) + "\n"
    elif g != 0 and f % g == 0:
        k = f // g
        str0 = "(" + str(c) + " + " + str(d) + ") : (" + str(max(a, b)) + " - " + str(min(a, b)) + ") = \n"
        str1 = str(k) + "\n"
    elif g != 0 and h % g == 0:
        k = h // g
        str0 = "(" + str(max(c, d)) + " - " + str(min(c, d)) + ") : (" + str(max(a, b)) + " - " + str(min(a, b)) + ") = \n"
        str1 = str(k) + "\n"
    else:
        k = g * h
        str0 = "(" + str(max(a, b)) + " - " + str(min(a, b)) + ") * (" + str(max(c, d)) + " - " + str(min(c, d)) + ") = \n"
        str1 = str(k) + "\n"
    list.append((str0, str1))
def mms(list):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    if a % b == 0:
        k = a // b * c + d
        str0 = str(a) + " : " + str(b) + " * " + str(c) + " + " + str(d) + " = \n"
        str1 = str(k) + "\n"
    elif a * b % c == 0:
        k = a * b // c + d
        str0 = str(a) + " * " + str(b) + " : " + str(c) + " + " + str(d) + " = \n"
        str1 = str(k) + "\n"
    elif a * b * c % d == 0:
        k = a * b * c // d
        str0 = str(a) + " * " + str(b) + " * " + str(c) + " : " + str(d) + " = \n"
        str1 = str(k) + "\n"
    elif (a + b) % c == 0:
        k = (a + b) / c + d
        str0 = "(" + str(a) + " + " + str(b) + ") :  " + str(c) + " + " + str(d) + " = \n"
        str1 = str(k) + "\n"
    elif (a + b + c) % d == 0:
        k = (a + b + c) / d
        str0 = "(" + str(a) + " + " + str(b) + " +  " + str(c) + ") : " + str(d) + " = \n"
        str1 = str(k) + "\n"
    else:
        k = a * b * c + d
        str0 = str(a) + " * " + str(b) + " *  " + str(c) + " + " + str(d) + " = \n"
        str1 = str(k) + "\n"
    list.append((str0, str1))

def msm(list):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    e = max(b, c) - min(b, c)
    if a % (b + c) == 0:
        k = a // (b + c) * d
        str0 = str(a) + " : (" + str(b) + " + " + str(c) + ") * " + str(d) + " = \n"
        str1 = str(k) + "\n"
    elif e != 0 and a % e == 0:
        k = a // e * d
        str0 = str(a) + " : (" + str(max(b, c)) + " - " + str(min(b, c)) + ") * " + str(d) + " = \n"
        str1 = str(k) + "\n"
    elif a * (b + c) % d == 0:
        k = a * (b + c) // d
        str0 = str(a) + " * (" + str(b) + " + " + str(c) + ") : " + str(d) + " = \n"
        str1 = str(k) + "\n"
    elif a * e % d == 0:
        k = a * e / d
        str0 = str(a) + " * (" + str(max(b, c)) + " - " + str(min(b, c)) + ") : " + str(d) + " = \n"
        str1 = str(k) + "\n"
    else:
        k = a * (b + c) * d
        str0 = str(a) + " * (" + str(b) + " + " + str(c) + ") * " + str(d) + " = \n"
        str1 = str(k) + "\n"
    list.append((str0, str1))
    

def add(f, a, b, f1, i):
    global nb
    c = a + b
    f.write(str(nb + i + 1) + ") " + str(a) + " + " + str(b) + " = \n")
    f1.write(str(nb + i + 1) + ". " + str(c) + "\n")
def sub(f, a, b, f1, i):
    global nb
    c = a + b
    f.write(str(nb + i + 1) + ") " + str(c) + " - " + str(b) + " = \n")
    f1.write(str(nb + i + 1) + ". " + str(a) + "\n")
def mul(f, a, b, f1, i):
    global nb
    c = a * b
    f.write(str(nb + i + 1) + ") " + str(a) + " * " + str(b) + " = \n")
    f1.write(str(nb + i + 1) + ". " + str(c) + "\n")
def div(f, a, b, f1, i):
    global nb
    c = a * b
    f.write(str(nb + i + 1) + ") " + str(c) + " : " + str(b) + " = \n")
    f1.write(str(nb + i + 1) + ". " + str(a) + "\n")


def execute_all_actions(nb_ex):
    global nb
    list = []
    f = open('action.txt', 'a')
    f1 = open('answers.txt', 'a')
    n = nb_ex // 3
    for i in range(n):
        sms(list)
        mms(list)
        msm(list)
    random.shuffle(list)
    i = nb + 1
    for j in list:
        f.write(str(i) + ") " + j[0])
        f1.write(str(i) + ". " + j[1])
        i += 1
    nb += n * 3
    f.close()
    
def execute_one_action(op, nb_ex, first, second):
    global nb
    f = open('action.txt', 'a')
    f1 = open('answers.txt', 'a')
    if op == 4:
        first -= second
    a = 10 ** first
    b = 10 ** second
    for i in range(nb_ex):
        ran_a = random.randint(1, (a - 1))
        ran_b = random.randint(1, (b - 1))
        if op == 1:
            add(f, ran_a, ran_b, f1, i);
        elif op == 2:
            sub(f, ran_a, ran_b, f1, i);
        elif op == 3:
            mul(f, ran_a, ran_b, f1, i);
        elif op == 4:
            div(f, ran_a, ran_b, f1, i);
    nb += nb_ex
    f.close()

def radio():
    global operation
    operation = var.get()
def clik():
    global operation
    first_component = 0
    second_component = 0
    namber_of_examples = 0
    first_component = vvod.get()
    second_component = vvod1.get()
    namber_of_examples = vvod2.get()
    try:
        if operation == 0:
            execute_all_actions(int(namber_of_examples))
        else:
            execute_one_action(operation, int(namber_of_examples), int(first_component), int(second_component))
        txt_del = " Примеры сгенерированы, \n находятся в файле action.txt \n \
текущей директории, \n ответы в файле answers.txt"
        txt_ex.configure(text=txt_del, fg = 'green')
    except:
        exc = " Пожалуйста, проверьте, \n что во все поля введены целые числа.\n \
Не рекомендуется  указывать \n количество разрядов более 6"
        txt_ex.configure(text=exc, fg = 'red' )
    
#creating the main window
var = IntVar()
var.set(0)
rad0 = Radiobutton(w, text = "Примеры на все действия", variable = var,
                   value = 0, command = radio)
rad1 = Radiobutton(w, text = "Сложение", variable = var, value = 1, command = radio )
rad2 = Radiobutton(w, text = "Вычитание", variable = var, value = 2,command = radio )
rad3 = Radiobutton(w, text = "Умножение", variable = var, value = 3, command = radio)
rad4 = Radiobutton(w, text = "Деление", variable = var, value = 4, command = radio)

rad0.grid(column = 0, row = 0)
rad1.grid(column = 0, row = 1)
rad2.grid(column = 0, row = 2)
rad3.grid(column = 0, row = 3)
rad4.grid(column = 0, row = 4)

txt = Label(w, text = "Количество разрядов в первом компоненте?",
                font = ("Arial Bold", 10))
txt.grid(column = 0, row = 6)
vvod = Entry(w, width = 10)
vvod.grid(column = 1,row = 6)
vvod.focus()

txt1 = Label(w, text = "Количество разрядов во втором компоненте?",
            font = ("Arial Bold", 10))
txt1.grid(column = 0, row = 7)
vvod1 = Entry(w, width = 10)
vvod1.grid(column = 1, row = 7)
vvod1.focus()

txt2 = Label(w, text = "Количество примеров:", font = ("Arial Bold", 10))
txt2.grid(column = 0, row = 8)
vvod2 = Entry(w, width = 10)
vvod2.grid(column = 1, row = 8)
vvod2.focus()

txt_ex = Label(w, text = "", font = ("Arial Bold", 10), fg = 'red', width = 40, height = 8, justify = 'left')
txt_ex.grid(column = 0, row = 11)


kn=Button(w,text="Сгенерировать", command=clik)
kn.grid(column=1,row=10)

w.mainloop()
