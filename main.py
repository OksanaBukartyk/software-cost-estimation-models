from tkinter import *
from tkinter import messagebox

from tkinter import ttk

root = Tk()
root.geometry('800x1100')
root.title("Calculations")

Language = StringVar()
Kilkist = DoubleVar()
Kilkist2 = DoubleVar()

FTR1 = DoubleVar()
FTR2 = DoubleVar()
FTR3 = DoubleVar()
DET1 = DoubleVar()
DET2 = DoubleVar()
DET3 = DoubleVar()
RET4 = DoubleVar()
RET5 = DoubleVar()
DET4 = DoubleVar()
DET5 = DoubleVar()

Rvvody = StringVar()

Klvyvody = DoubleVar()
Rvyvody = StringVar()

Rzapyty = StringVar()
Klzapyty = DoubleVar()

KlLokVnF = DoubleVar()
RLokVnF = StringVar()

KlZovIntF = DoubleVar()
RZovIntF = StringVar()

cocomo_stad = StringVar()
cocomo_level = StringVar()
cocomo_types = StringVar()
RELY = StringVar()
DATA = StringVar()
CPLX = StringVar()
TIME = StringVar()
STOR = StringVar()
VIRT = StringVar()
TURN = StringVar()
ACAP = StringVar()
AEXP = StringVar()
PCAP = StringVar()
VEXP = StringVar()
LEXP = StringVar()
MODP = StringVar()
TOOL = StringVar()
SCED = StringVar()

PREC = StringVar()
FLEX = StringVar()
RESL = StringVar()
TEAM = StringVar()
PMAT = StringVar()

PERS = StringVar()
PREX = StringVar()
RCPX = StringVar()
RUSE1 = StringVar()
PDIF = StringVar()
FCIL = StringVar()
SCED1 = StringVar()

ACAP2 = StringVar()
AEXP2 = StringVar()
PCAP2 = StringVar()
PCON = StringVar()
PEXP = StringVar()
LTEX = StringVar()
RELY2 = StringVar()
DATA2 = StringVar()
CPLX2 = StringVar()
RUSE2 = StringVar()
DOCU = StringVar()
TIME2 = StringVar()
STOR2 = StringVar()
PVOL = StringVar()
TOOL2 = StringVar()
SITE = StringVar()
SCED2 = StringVar()

DACO = DoubleVar()
DIFU = DoubleVar()
PERF = DoubleVar()
HEUS = DoubleVar()
TRRA = DoubleVar()
ONDA = DoubleVar()
ENUS = DoubleVar()
ONUP = DoubleVar()
COPR = DoubleVar()
REUS = DoubleVar()
INEA = DoubleVar()
OPEA = DoubleVar()
MULT = DoubleVar()
FACH = DoubleVar()


def zap_and_exit(a, b):
    if (0 <= a <= 1 and (1 <= b <= 5 or 6 <= b <= 19)) or \
            (2 <= a <= 3 and 1 <= b <= 5):
        c = 'Low'
    elif (0 <= a <= 1 and b >= 20) or \
            (2 <= a <= 3 and 6 <= b <= 19) or \
            (a >= 4 and 1 <= b <= 5):
        c = 'Average'
    elif (a == 0 and b == 0):
        c = 'None'
    else:
        c = 'High'
    return c


def inputs(a, b):
    if (0 <= a <= 1 and (1 <= b <= 4 or 5 <= b <= 15)) or \
            (a == 2 and 1 <= b <= 4):
        c = 'Low'
    elif (0 <= a <= 1 and b >= 16) or \
            (a == 2 and 5 <= b <= 15) or \
            (a >= 3 and 1 <= b <= 4):
        c = 'Average'
    elif (a == 0 and b == 0):
        c = 'None'
    else:
        c = 'High'
    return c


def files(a, b):
    if (a == 1 and (1 <= b <= 19 or 20 <= b <= 50)) or \
            (2 <= a <= 5 and 1 <= b <= 19):
        c = 'Low'
    elif (a == 1 and b >= 51) or \
            (2 <= a <= 5 and 20 <= b <= 50) or \
            (a >= 6 and 1 <= b <= 19):
        c = 'Average'
    elif (a == 0 or b == 0):
        c = 'None'
    else:
        c = 'High'
    return c


def rez():
    if cocomo_level.get() == "Базовий":
        if cocomo_types.get() == "Organic":
            calc(0)
        elif cocomo_types.get() == "Semidetached":
            calc(1)
        elif cocomo_types.get() == "Embedded":
            calc(2)
        else:
            print("Eror")
    elif cocomo_level.get() == "Промiжний":
        if cocomo_types.get() == "Organic":
            calc1(0)
        elif cocomo_types.get() == "Semidetached":
            calc1(1)
        elif cocomo_types.get() == "Embedded":
            calc1(2)
        else:
            print("Eror")
    else:
        print("eror")


def rez2():
    if cocomo_stad.get() == "Early Design":
        calc2()

    elif cocomo_stad.get() == "Post Architecture":
        calc3()
    else:
        print("eror")


def rez3():
    if cocomo_types.get() == "Organic":
        calc4(0)
    elif cocomo_types.get() == "Semidetached":
        calc4(1)
    elif cocomo_types.get() == "Embedded":
        calc4(2)
    else:
        print("Eror")


def calc4(i):
    ai = [2.4, 3.0, 3.6]
    bi = [1.05, 1.12, 1.20]
    listLeng = {'Пакетні файли DOS': 128, 'Basic': 107, 'PL/1': 80, 'C#': 58, 'Розширений LISP': 56, 'Java': 55,
                'JavaScript': 54, \
                'C++': 53, 'Visual Basic': 50, 'Мови баз даних': 40, 'Access': 38, 'VBScript': 38,
                'Мови підтримки прийняття': 35, \
                'FoxPro 2.5': 34, 'DELPHI': 29, "Стандартні об'єктно орієнтовані": 29, 'VB.NET': 28, \
                'Стандартні мови 4-го покоління': 20, 'HTML 3.0': 15, 'SQL': 13, 'SQL Forms': 11, 'Excel': 6}
    leng = Language.get()

    ############################
    if files(RET4.get(), DET4.get()) == 'Low':
        ILF = 7
    elif files(RET4.get(), DET4.get()) == 'Average':
        ILF = 10
    elif files(RET4.get(), DET4.get()) == 'High':
        ILF = 15
    else:
        ILF = 0

    if files(RET5.get(), DET5.get()) == 'Low':
        EIF = 5
    elif files(RET5.get(), DET5.get()) == 'Average':
        EIF = 7
    elif files(RET5.get(), DET5.get()) == 'High':
        ILF = 10
    else:
        EIF = 0

    if inputs(FTR1.get(), DET1.get()) == 'Low':
        EI = 3
    elif inputs(FTR1.get(), DET1.get()) == 'Average':
        EI = 4
    elif inputs(FTR1.get(), DET1.get()) == 'High':
        EI = 6
    else:
        EI = 0

    if zap_and_exit(FTR2.get(), DET2.get()) == 'Low':
        EO = 4
    elif zap_and_exit(FTR2.get(), DET2.get()) == 'Average':
        EO = 5
    elif zap_and_exit(FTR2.get(), DET2.get()) == 'High':
        EO = 7
    else:
        EO = 0

    if zap_and_exit(FTR3.get(), DET3.get()) == 'Low':
        EQ = 3
    elif zap_and_exit(FTR3.get(), DET3.get()) == 'Average':
        EQ = 4
    elif zap_and_exit(FTR3.get(), DET3.get()) == 'High':
        EQ = 6
    else:
        EQ = 0
    UFPC = ILF + EIF + EI + + EO + EQ

    TDI = DACO.get() + DIFU.get() + PERF.get() + HEUS.get() + TRRA.get() + ONDA.get() + ENUS.get() + ONUP.get() + COPR.get() + REUS.get() + INEA.get() + OPEA.get() + MULT.get() + FACH.get()
    VAF = 0.65 + (0.01 * TDI)
    AFPC = UFPC * VAF
    SLOC = AFPC * listLeng[leng]
    KLOC = SLOC / 1000
    T = ai[i] * (KLOC) ** (bi[i])

    label_3 = Label(tab3, text="Результати: ", width=20, font=("bold", 20))
    label_3.place(x=460, y=285)

    label_4 = Label(tab3, text="Трудомісткість = " + str(T) + " люд./міс.", width=50, font=("bold", 10))
    label_4.place(x=400, y=315)


def calc2():
    A = 2.94
    B = 0.91
    list1 = {'Very Low': 6.20, 'Low': 4.96, 'Nominal': 3.72, 'High': 2.48, 'Very High': 1.24, 'Extra High': 0.00}
    list2 = {'Very Low': 5.07, 'Low': 4.05, 'Nominal': 3.04, 'High': 2.03, 'Very High': 1.01, 'Extra High': 0.00}
    list3 = {'Very Low': 7.07, 'Low': 5.65, 'Nominal': 4.24, 'High': 2.83, 'Very High': 1.41, 'Extra High': 0.00}
    list4 = {'Very Low': 5.78, 'Low': 4.38, 'Nominal': 3.29, 'High': 2.19, 'Very High': 1.10, 'Extra High': 0.00}
    list5 = {'Very Low': 7.80, 'Low': 6.24, 'Nominal': 4.68, 'High': 3.12, 'Very High': 1.56, 'Extra High': 0.00}
    plec = PREC.get()
    flex = FLEX.get()
    resl = RESL.get()
    team = TEAM.get()
    pmat = PMAT.get()
    list01 = {'Extra Low': 2.12, 'Very Low': 1.62, 'Low': 1.26, 'Nominal': 1.00, 'High': 0.83, 'Very High': 0.63,
              'Extra High': 0.50}
    list02 = {'Extra Low': 1.59, 'Very Low': 1.33, 'Low': 1.22, 'Nominal': 1.00, 'High': 0.87, 'Very High': 0.74,
              'Extra High': 0.62}
    list03 = {'Extra Low': 0.49, 'Very Low': 0.60, 'Low': 0.83, 'Nominal': 1.00, 'High': 1.33, 'Very High': 1.91,
              'Extra High': 2.72}
    list04 = {'Low': 0.95, 'Nominal': 1.00, 'High': 1.07, 'Very High': 1.15, 'Extra High': 1.24}
    list05 = {'Low': 0.87, 'Nominal': 1.00, 'High': 1.29, 'Very High': 1.81, 'Extra High': 2.61}
    list06 = {'Extra Low': 1.43, 'Very Low': 1.30, 'Low': 1.10, 'Nominal': 1.00, 'High': 0.87, 'Very High': 0.73,
              'Extra High': 0.62}
    list07 = {'Very Low': 1.43, 'Low': 1.14, 'Nominal': 1.00, 'High': 1.00}
    pers = PERS.get()
    prex = PREX.get()
    rcpx = RCPX.get()
    ruse1 = RUSE1.get()
    pdif = PDIF.get()
    fcil = FCIL.get()
    sced1 = SCED1.get()

    sum_SF = list1[plec] + list2[flex] + list3[resl] + list4[team] + list5[pmat]
    dob_EM = list01[pers] * list02[prex] * list03[rcpx] * list04[ruse1] * list05[pdif] * list06[fcil] * list07[sced1]
    E = B + 0.01 * sum_SF
    print(sum_SF)
    print(dob_EM)
    PM = A * dob_EM * (Kilkist2.get()) ** E
    print(E)
    print((Kilkist2.get()) ** E)
    print(PM)
    label_3 = Label(tab2, text="Результати: ", width=20, font=("bold", 20))
    label_3.place(x=10, y=490)

    label_4 = Label(tab2, text="Трудомісткість = " + str(PM) + " люд./міс.", width=0, font=("bold", 10))
    label_4.place(x=0, y=530)


def calc3():
    A = 2.45
    B = 0.91
    list1 = {'Very Low': 6.20, 'Low': 4.96, 'Nominal': 3.72, 'High': 2.48, 'Very High': 1.24, 'Extra High': 0.00}
    list2 = {'Very Low': 5.07, 'Low': 4.05, 'Nominal': 3.04, 'High': 2.03, 'Very High': 1.01, 'Extra High': 0.00}
    list3 = {'Very Low': 7.07, 'Low': 5.65, 'Nominal': 4.24, 'High': 2.83, 'Very High': 1.41, 'Extra High': 0.00}
    list4 = {'Very Low': 5.78, 'Low': 4.38, 'Nominal': 3.29, 'High': 2.19, 'Very High': 1.10, 'Extra High': 0.00}
    list5 = {'Very Low': 7.80, 'Low': 6.24, 'Nominal': 4.68, 'High': 3.12, 'Very High': 1.56, 'Extra High': 0.00}
    plec = PREC.get()
    flex = FLEX.get()
    resl = RESL.get()
    team = TEAM.get()
    pmat = PMAT.get()
    list01 = {'Very Low': 1.42, 'Low': 1.29, 'Nominal': 1.00, 'High': 0.85, 'Very High': 0.71}
    list02 = {'Very Low': 1.22, 'Low': 1.10, 'Nominal': 1.00, 'High': 0.88, 'Very High': 0.81}
    list03 = {'Very Low': 1.34, 'Low': 1.15, 'Nominal': 1.00, 'High': 0.88, 'Very High': 0.76}
    list04 = {'Very Low': 1.29, 'Low': 1.12, 'Nominal': 1.00, 'High': 0.90, 'Very High': 0.81}
    list05 = {'Very Low': 1.19, 'Low': 1.09, 'Nominal': 1.00, 'High': 0.91, 'Very High': 0.85}
    list06 = {'Very Low': 1.20, 'Low': 1.09, 'Nominal': 1.00, 'High': 0.91, 'Very High': 0.84}

    list07 = {'Very Low': 0.84, 'Low': 0.92, 'Nominal': 1.00, 'High': 1.10, 'Very High': 1.26}
    list08 = {'Low': 0.23, 'Nominal': 1.00, 'High': 1.14, 'Very High': 1.28}
    list09 = {'Very Low': 0.73, 'Low': 0.87, 'Nominal': 1.00, 'High': 1.17, 'Very High': 1.34, 'Extra High': 1.74}
    list010 = {'Low': 0.95, 'Nominal': 1.00, 'High': 1.07, 'Very High': 1.15, 'Extra High': 1.24}
    list011 = {'Very Low': 0.81, 'Low': 0.91, 'Nominal': 1.00, 'High': 1.11, 'Very High': 1.23}

    list012 = {'Nominal': 1.00, 'High': 1.11, 'Very High': 1.29, 'Extra High': 1.63}
    list013 = {'Nominal': 1.00, 'High': 1.05, 'Very High': 1.17, 'Extra High': 1.46}
    list014 = {'Low': 0.87, 'Nominal': 1.00, 'High': 1.15, 'Very High': 1.30}

    list015 = {'Very Low': 1.17, 'Low': 1.09, 'Nominal': 1.00, 'High': 0.90, 'Very High': 0.78}
    list016 = {'Very Low': 1.22, 'Low': 1.09, 'Nominal': 1.00, 'High': 0.93, 'Very High': 0.86, 'Extra High': 0.80}
    list017 = {'Very Low': 1.43, 'Low': 1.14, 'Nominal': 1.00, 'High': 1.00, 'Very High': 1.00}

    acap2 = ACAP2.get()
    aexp2 = AEXP2.get()
    pcap2 = PCAP2.get()
    pcon = PCON.get()
    pexp = PEXP.get()
    ltex = LTEX.get()
    rely2 = RELY2.get()
    data2 = DATA2.get()
    cplx2 = CPLX2.get()
    ruse2 = RUSE2.get()
    docu = DOCU.get()
    time2 = TIME2.get()
    stor2 = STOR2.get()
    pvol = PVOL.get()
    tool2 = TOOL2.get()
    site = SITE.get()
    sced2 = SCED2.get()

    sum_SF = list1[plec] + list2[flex] + list3[resl] + list4[team] + list5[pmat]
    dob_EM = list01[acap2] * list02[aexp2] * list03[pcap2] * list04[pcon] * list05[pexp] * list06[ltex] \
             * list07[rely2] * list08[data2] * list09[cplx2] * list010[ruse2] * list011[docu] * list012[time2] \
             * list013[stor2] * list014[pvol] * list015[tool2] * list016[site] * list017[sced2]

    E = B + 0.01 * sum_SF
    PM = A * dob_EM * (Kilkist2.get()) ** E
    print()
    print(sum_SF)
    print(dob_EM)

    print(E)
    print((Kilkist2.get()) ** E)
    print(PM)
    print()
    label_3 = Label(tab2, text="Результати: ", width=20, font=("bold", 20))
    label_3.place(x=10, y=490)

    label_4 = Label(tab2, text="Трудомісткість = " + str(PM) + " люд./міс.", width=50, font=("bold", 10))
    label_4.place(x=0, y=530)


def calc(i):
    ai = [2.4, 3.0, 3.6]
    bi = [1.05, 1.12, 1.20]
    ci = [2.5, 2.5, 2.5]
    di = [0.38, 0.35, 0.32]
    PM = ai[i] * (Kilkist.get()) ** bi[i]
    TM = ci[i] * (PM) ** di[i]
    SS = PM / TM
    P = Kilkist.get() / PM

    label_3 = Label(tab1, text="Результати: ", width=20, font=("bold", 20))
    label_3.place(x=225, y=580)

    label_4 = Label(tab1, text="Трудомісткість = " + str(PM) + " люд./міс.", width=50, font=("bold", 10))
    label_4.place(x=175, y=615)

    label_5 = Label(tab1, text="Час розробки = " + str(TM) + " міс.", width=50, font=("bold", 10))
    label_5.place(x=175, y=635)

    label_6 = Label(tab1, text="Середня чисельність персоналу = " + str(SS) + " люд.", width=0, font=("bold", 10))
    label_6.place(x=175, y=655)

    label_7 = Label(tab1, text="Продуктивність = " + str(P), width=50, font=("bold", 10))
    label_7.place(x=175, y=675)


def calc1(i):
    ai = [3.2, 3.0, 2.8]
    bi = [1.05, 1.12, 1.20]
    list1 = {'Very Low': 0.75, 'Low': 0.88, 'Nominal': 1.00, 'High': 1.15, 'Very High': 1.40}
    list2 = {'Low': 0.94, 'Nominal': 1.00, 'High': 1.08, 'Very High': 1.16}
    list3 = {'Very Low': 0.70, 'Low': 0.85, 'Nominal': 1.00, 'High': 1.15, 'Very High': 1.30, 'Extra High': 1.65}
    list4 = {'Nominal': 1.00, 'High': 1.11, 'Very High': 1.30, 'Extra High': 1.65}
    list5 = {'Nominal': 1.00, 'High': 1.06, 'Very High': 1.21, 'Extra High': 1.56}
    list6 = {'Low': 0.87, 'Nominal': 1.00, 'High': 1.15, 'Very High': 1.30}
    list7 = {'Low': 0.87, 'Nominal': 1.00, 'High': 1.07, 'Very High': 1.15}
    list8 = {'Very Low': 1.46, 'Low': 1.19, 'Nominal': 1.00, 'High': 0.86, 'Very High': 0.71}
    list9 = {'Very Low': 1.29, 'Low': 1.13, 'Nominal': 1.00, 'High': 0.91, 'Very High': 0.82}
    list10 = {'Very Low': 1.42, 'Low': 1.17, 'Nominal': 1.00, 'High': 0.86, 'Very High': 0.70}
    list11 = {'Very Low': 1.21, 'Low': 1.10, 'Nominal': 1.00, 'High': 0.90}
    list12 = {'Very Low': 1.14, 'Low': 1.07, 'Nominal': 1.00, 'High': 0.95}
    list13 = {'Very Low': 1.24, 'Low': 1.10, 'Nominal': 1.00, 'High': 0.91, 'Very High': 0.82}
    list14 = {'Very Low': 1.24, 'Low': 1.10, 'Nominal': 1.00, 'High': 0.91, 'Very High': 0.83}
    list15 = {'Very Low': 1.23, 'Low': 1.08, 'Nominal': 1.00, 'High': 1.04, 'Very High': 1.10}

    rely = RELY.get()
    data = DATA.get()
    cplx = CPLX.get()
    time = TIME.get()
    stor = STOR.get()
    virt = VIRT.get()
    turn = TURN.get()
    acap = ACAP.get()
    aexp = AEXP.get()
    pcap = PCAP.get()
    vexp = VEXP.get()
    lexp = LEXP.get()
    modp = MODP.get()
    tool = TOOL.get()
    sced = SCED.get()

    EAF = list1[rely] * list2[data] * list3[cplx] * list4[time] * list5[stor] * list6[virt] * list7[turn] * list8[
        acap] * \
          list9[aexp] * list10[pcap] * list11[vexp] * list12[lexp] * list13[modp] * list14[tool] * list15[sced]

    PM = EAF * ai[i] * (Kilkist.get()) ** bi[i]

    label_3 = Label(tab1, text="Результати: ", width=20, font=("bold", 20))
    label_3.place(x=225, y=580)

    label_4 = Label(tab1, text="Трудомісткість = " + str(PM) + " люд./міс.", width=50, font=("bold", 10))
    label_4.place(x=165, y=615)

    label_host = Label(tab1, text="         ", width=20, font=("bold", 50))
    label_host.place(x=-5, y=640)


def drav1():
    label_0 = Label(tab1, text="COCOMO I ", width=20, fg='black', font=("bold", 20))
    label_0.place(x=250, y=0)

    label_11 = Label(tab1, text="Рівeнь: ", width=20, font=("bold", 10))
    label_11.place(x=260, y=40)
    list1 = ['Базовий', 'Промiжний'];
    droplist = OptionMenu(tab1, cocomo_level, *list1)
    droplist.config(width=15)
    cocomo_level.set(list1[0])
    droplist.place(x=400, y=40)

    label_1 = Label(tab1, text="Тип проекта: ", width=20, font=("bold", 10))
    label_1.place(x=260, y=65)
    list1 = ['Organic', 'Semidetached', 'Embedded'];
    droplist = OptionMenu(tab1, cocomo_types, *list1)
    droplist.config(width=15)
    cocomo_types.set(list1[0])
    droplist.place(x=400, y=65)

    label_2 = Label(tab1, text="Кількість рядків коду в тис. ", width=0, font=("bold", 10))
    label_2.place(x=240, y=95)
    entry_2 = Entry(tab1, textvar=Kilkist)
    entry_2.place(x=450, y=95)

    label_ymova = Label(tab1, text="Характеристики для проміжного рівня:", width=80, font=("bold", 12))
    label_ymova.place(x=60, y=125)

    label_5 = Label(tab1, text="Необхідна надійність ПЗ(RELY) : ", width=30, font=("bold", 10))
    label_5.place(x=200, y=155)
    list_1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab1, RELY, *list_1)
    droplist.config(width=15)
    RELY.set('Nominal')
    droplist.place(x=450, y=155)

    label_6 = Label(tab1, text="Розмір БД додатку(DATA) : ", width=30, font=("bold", 10))
    label_6.place(x=200, y=180)
    list_2 = ['Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab1, DATA, *list_2)
    droplist.config(width=15)
    DATA.set('Nominal')
    droplist.place(x=450, y=180)

    label_7 = Label(tab1, text="Складність продукту(CPLX) : ", width=30, font=("bold", 10))
    label_7.place(x=200, y=205)
    list_3 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab1, CPLX, *list_3)
    droplist.config(width=15)
    CPLX.set('Nominal')
    droplist.place(x=450, y=205)

    label_8 = Label(tab1, text="Обмеження швидкодії(TIME) : ", width=30, font=("bold", 10))
    label_8.place(x=200, y=230)
    list1 = ['Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab1, TIME, *list1)
    droplist.config(width=15)
    TIME.set('Nominal')
    droplist.place(x=450, y=230)

    label_9 = Label(tab1, text="Обмеження пам'яті(STOR) : ", width=30, font=("bold", 10))
    label_9.place(x=200, y=255)
    list1 = ['Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab1, STOR, *list1)
    droplist.config(width=15)
    STOR.set(list1[0])
    droplist.place(x=450, y=255)

    label_10 = Label(tab1, text="Нестійкість оточення (VIRT) : ", width=30, font=("bold", 10))
    label_10.place(x=200, y=280)
    list1 = ['Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab1, VIRT, *list1)
    droplist.config(width=15)
    VIRT.set('Nominal')
    droplist.place(x=450, y=280)

    label_11 = Label(tab1, text="Необхідний час відновлення(TURN) : ", width=0, font=("bold", 10))
    label_11.place(x=190, y=305)
    list1 = ['Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab1, TURN, *list1)
    droplist.config(width=15)
    TURN.set('Nominal')
    droplist.place(x=450, y=305)

    label_12 = Label(tab1, text="Аналітичні здібності(ACAP) : ", width=30, font=("bold", 10))
    label_12.place(x=200, y=330)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab1, ACAP, *list1)
    droplist.config(width=15)
    ACAP.set('Nominal')
    droplist.place(x=450, y=330)

    label_13 = Label(tab1, text="Досвід розробки(EAXP) : ", width=30, font=("bold", 10))
    label_13.place(x=200, y=355)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab1, AEXP, *list1)
    droplist.config(width=15)
    AEXP.set('Nominal')
    droplist.place(x=450, y=355)

    label_14 = Label(tab1, text="Здібності до розробки ПЗ(PCAP) : ", width=30, font=("bold", 10))
    label_14.place(x=200, y=380)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab1, PCAP, *list1)
    droplist.config(width=15)
    PCAP.set('Nominal')
    droplist.place(x=450, y=380)

    label_15 = Label(tab1, text="Досвід використ. вірт. машин(VEXP) : ", width=0, font=("bold", 10))
    label_15.place(x=180, y=405)
    list1 = ['Very Low', 'Low', 'Nominal', 'High'];
    droplist = OptionMenu(tab1, VEXP, *list1)
    droplist.config(width=15)
    VEXP.set('Nominal')
    droplist.place(x=450, y=405)

    label_16 = Label(tab1, text="Досвід на мовах програмув.(LEXP) : ", width=0, font=("bold", 10))
    label_16.place(x=180, y=430)
    list1 = ['Very Low', 'Low', 'Nominal', 'High'];
    droplist = OptionMenu(tab1, LEXP, *list1)
    droplist.config(width=15)
    LEXP.set('Nominal')
    droplist.place(x=450, y=430)

    label_17 = Label(tab1, text="Застос. методів розробки ПЗ(MODP) : ", width=0, font=("bold", 10))
    label_17.place(x=180, y=455)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab1, MODP, *list1)
    droplist.config(width=15)
    MODP.set('Nominal')
    droplist.place(x=450, y=455)

    label_18 = Label(tab1, text="Використання інструментарію(TOOL) : ", width=0, font=("bold", 10))
    label_18.place(x=180, y=480)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab1, TOOL, *list1)
    droplist.config(width=15)
    TOOL.set('Nominal')
    droplist.place(x=450, y=480)

    label_19 = Label(tab1, text="Дотримання графіка розробки(SCED) : ", width=0, font=("bold", 10))
    label_19.place(x=180, y=505)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab1, SCED, *list1)
    droplist.config(width=15)
    SCED.set('Nominal')
    droplist.place(x=450, y=505)

    Button(tab1, text='Розрахувати', command=rez, width=20, bg='brown', fg='white').place(x=340, y=550)


def drav2():
    label_0 = Label(tab2, text="COCOMO II ", width=0, fg='black', font=("bold", 20))
    label_0.place(x=250, y=0)

    label_11 = Label(tab2, text="Стадія оцінки: ", width=20, font=("bold", 10))
    label_11.place(x=100, y=45)
    list1 = ['Early Design', 'Post Architecture'];
    droplist = OptionMenu(tab2, cocomo_stad, *list1)
    droplist.config(width=15)
    cocomo_stad.set(list1[0])
    droplist.place(x=230, y=40)

    label_2 = Label(tab2, text="Кількість рядків коду в тис. ", width=0, font=("bold", 10))
    label_2.place(x=415, y=45)
    entry_2 = Entry(tab2, textvar=Kilkist2)
    entry_2.place(x=600, y=45)

    label_ymova = Label(tab2, text="Чинники масштабу: ", width=80, font=("bold", 12))
    label_ymova.place(x=50, y=70)

    label_5 = Label(tab2, text="Прецедентність, наявність досвіду(PREC): ", width=0, font=("bold", 10))
    label_5.place(x=120, y=90)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, PREC, *list1)
    droplist.config(width=10)
    PREC.set('Nominal')
    droplist.place(x=430, y=90)

    label_6 = Label(tab2, text="Гнучкість процесу(FLEX) : ", width=30, font=("bold", 10))
    label_6.place(x=200, y=115)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, FLEX, *list1)
    droplist.config(width=10)
    FLEX.set('Nominal')
    droplist.place(x=430, y=115)

    label_7 = Label(tab2, text="Архітектура і дозвіл ризиків(RESL) : ", width=0, font=("bold", 10))
    label_7.place(x=175, y=140)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, RESL, *list1)
    droplist.config(width=10)
    RESL.set('Nominal')
    droplist.place(x=430, y=140)

    label_8 = Label(tab2, text="Спрацьованість(TEAM) : ", width=30, font=("bold", 10))
    label_8.place(x=200, y=165)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, TEAM, *list1)
    droplist.config(width=10)
    TEAM.set('Nominal')
    droplist.place(x=430, y=165)

    label_9 = Label(tab2, text="Зрілість процесів(PMAT) : ", width=30, font=("bold", 10))
    label_9.place(x=200, y=190)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, PMAT, *list1)
    droplist.config(width=10)
    PMAT.set('Nominal')
    droplist.place(x=430, y=190)

    label_10 = Label(tab2, text=" Множн. трудомісткості для Early Design: ", width=40, font=("bold", 13))
    label_10.place(x=10, y=220)
    label_11 = Label(tab2, text=" Множн. трудомісткості для Post Architecture: ", width=40, font=("bold", 13))
    label_11.place(x=400, y=220)

    label_12 = Label(tab2, text="Кваліфікація персоналу(PERS) : ", width=0, font=("bold", 10))
    label_12.place(x=0, y=250)
    list1 = ['Extra Low', 'Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, PERS, *list1)
    droplist.config(width=8)
    PERS.set('Nominal')
    droplist.place(x=260, y=250)

    label_13 = Label(tab2, text="Досвід персоналу(PREX) : ", width=0, font=("bold", 10))
    label_13.place(x=0, y=275)
    list1 = ['Extra Low', 'Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, PREX, *list1)
    droplist.config(width=8)
    PREX.set('Nominal')
    droplist.place(x=260, y=275)

    label_14 = Label(tab2, text="Склад. і надійн. продукту(RCPX) : ", width=0, font=("bold", 10))
    label_14.place(x=0, y=300)
    list1 = ['Extra Low', 'Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, RCPX, *list1)
    droplist.config(width=8)
    RCPX.set('Nominal')
    droplist.place(x=260, y=300)

    label_15 = Label(tab2, text="Розроб. для повтор.викрист.(RUSE) : ", width=0, font=("bold", 10))
    label_15.place(x=0, y=325)
    list1 = ['Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, RUSE1, *list1)
    droplist.config(width=8)
    RUSE1.set('Nominal')
    droplist.place(x=260, y=325)

    label_16 = Label(tab2, text="Складн. платформи розробки(PDIF) : ", width=0, font=("bold", 10))
    label_16.place(x=0, y=350)
    list1 = ['Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, PDIF, *list1)
    droplist.config(width=8)
    PDIF.set('Nominal')
    droplist.place(x=260, y=350)

    label_17 = Label(tab2, text="Обладнання(FCIL) : ", width=0, font=("bold", 10))
    label_17.place(x=0, y=375)
    list1 = ['Extra Low', 'Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, FCIL, *list1)
    droplist.config(width=8)
    FCIL.set('Nominal')
    droplist.place(x=260, y=375)

    label_18 = Label(tab2, text="Необхідний графік(SCED) : ", width=0, font=("bold", 10))
    label_18.place(x=0, y=400)
    list1 = ['Very Low', 'Low', 'Nominal', 'High'];
    droplist = OptionMenu(tab2, SCED1, *list1)
    droplist.config(width=8)
    SCED1.set('Nominal')
    droplist.place(x=260, y=400)
    #####################################################2stovp
    label_19 = Label(tab2, text="Можливості аналітики(ACAP) : ", width=0, font=("bold", 10))
    label_19.place(x=380, y=250)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab2, ACAP2, *list1)
    droplist.config(width=8)
    ACAP2.set('Nominal')
    droplist.place(x=680, y=250)

    label_20 = Label(tab2, text="Досвід розробки додатків(AEXP) : ", width=0, font=("bold", 10))
    label_20.place(x=380, y=275)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab2, AEXP2, *list1)
    droplist.config(width=8)
    AEXP2.set('Nominal')
    droplist.place(x=680, y=275)

    label_21 = Label(tab2, text="Можливості програміста(PCAP) : ", width=0, font=("bold", 10))
    label_21.place(x=380, y=295)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab2, PCAP2, *list1)
    droplist.config(width=8)
    PCAP2.set('Nominal')
    droplist.place(x=680, y=295)

    label_22 = Label(tab2, text="Тривалість роботи персоналу(PCON) : ", width=0, font=("bold", 10))
    label_22.place(x=380, y=320)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab2, PCON, *list1)
    droplist.config(width=8)
    PCON.set('Nominal')
    droplist.place(x=680, y=320)

    label_23 = Label(tab2, text="Досвід роботи з платформою(PEXP) : ", width=0, font=("bold", 10))
    label_23.place(x=380, y=345)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab2, PEXP, *list1)
    droplist.config(width=8)
    PEXP.set('Nominal')
    droplist.place(x=680, y=345)

    label_24 = Label(tab2, text="Досвід викор. мови програмув.(LTEX) : ", width=0, font=("bold", 10))
    label_24.place(x=380, y=370)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab2, LTEX, *list1)
    droplist.config(width=8)
    LTEX.set('Nominal')
    droplist.place(x=680, y=370)

    label_25 = Label(tab2, text="Надійність програми(RELY) : ", width=0, font=("bold", 10))
    label_25.place(x=380, y=395)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab2, RELY2, *list1)
    droplist.config(width=8)
    RELY2.set('Nominal')
    droplist.place(x=680, y=395)

    label_26 = Label(tab2, text="Розмір бази даних(DATA) : ", width=0, font=("bold", 10))
    label_26.place(x=380, y=420)
    list1 = ['Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab2, DATA2, *list1)
    droplist.config(width=8)
    DATA2.set('Nominal')
    droplist.place(x=680, y=420)

    label_27 = Label(tab2, text="Складність програми(CPLX) : ", width=0, font=("bold", 10))
    label_27.place(x=380, y=445)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, CPLX2, *list1)
    droplist.config(width=8)
    CPLX2.set('Nominal')
    droplist.place(x=680, y=445)

    label_28 = Label(tab2, text="Можливість багатораз.використ.(RUSE) : ", width=0, font=("bold", 10))
    label_28.place(x=380, y=470)
    list1 = ['Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, RUSE2, *list1)
    droplist.config(width=8)
    RUSE2.set('Nominal')
    droplist.place(x=680, y=470)

    label_29 = Label(tab2, text="Відповідн. документац. потребам(DOCU) : ", width=0, font=("bold", 10))
    label_29.place(x=380, y=495)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab2, DOCU, *list1)
    droplist.config(width=8)
    DOCU.set('Nominal')
    droplist.place(x=680, y=495)

    label_30 = Label(tab2, text="Обмеження часу вик.(TIME) : ", width=0, font=("bold", 10))
    label_30.place(x=380, y=520)
    list1 = ['Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, TIME2, *list1)
    droplist.config(width=8)
    TIME2.set('Nominal')
    droplist.place(x=680, y=520)

    label_31 = Label(tab2, text="Обмеження пам'яті(STOR) : ", width=0, font=("bold", 10))
    label_31.place(x=380, y=545)
    list1 = ['Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, STOR2, *list1)
    droplist.config(width=8)
    STOR2.set('Nominal')
    droplist.place(x=680, y=545)

    label_32 = Label(tab2, text="Змінність платформи(PVOL) : ", width=0, font=("bold", 10))
    label_32.place(x=380, y=570)
    list1 = ['Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab2, PVOL, *list1)
    droplist.config(width=8)
    PVOL.set('Nominal')
    droplist.place(x=680, y=570)

    label_33 = Label(tab2, text="Викор.інстумент. прогр. засобів(TOOL) : ", width=0, font=("bold", 10))
    label_33.place(x=380, y=595)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab2, TOOL2, *list1)
    droplist.config(width=8)
    TOOL2.set('Nominal')
    droplist.place(x=680, y=595)

    label_34 = Label(tab2, text="Віддалена розробка(SITE) : ", width=0, font=("bold", 10))
    label_34.place(x=380, y=620)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High'];
    droplist = OptionMenu(tab2, SITE, *list1)
    droplist.config(width=8)
    SITE.set('Nominal')
    droplist.place(x=680, y=620)

    label_35 = Label(tab2, text="Необід. викон. графіка робіт(SCED) : ", width=0, font=("bold", 10))
    label_35.place(x=380, y=645)
    list1 = ['Very Low', 'Low', 'Nominal', 'High', 'Very High'];
    droplist = OptionMenu(tab2, SCED2, *list1)
    droplist.config(width=8)
    SCED2.set('Nominal')
    droplist.place(x=680, y=645)

    Button(tab2, text='Розрахувати', command=rez2, width=20, bg='brown', fg='white').place(x=90, y=455)


def drav3():
    label_0 = Label(tab3, text=" Метод функціональних точок ", width=30, fg='black', font=("bold", 20))
    label_0.place(x=180, y=0)

    label_2 = Label(tab3, text="Зовнішні вводи (EI): ", width=0, font=("bold", 10))
    label_2.place(x=20, y=50)

    label_2 = Label(tab3, text="FTR: ", width=8, font=("bold", 10))
    label_2.place(x=260, y=50)

    entry_2 = Entry(tab3, textvar=FTR1)
    entry_2.place(x=320, y=50)

    label_2 = Label(tab3, text="DET: ", width=10, font=("bold", 10))
    label_2.place(x=500, y=50)

    entry_2 = Entry(tab3, textvar=DET1)
    entry_2.place(x=570, y=50)

    label_2 = Label(tab3, text="Ззовнішні виводи (EO): ", width=0, font=("bold", 10))
    label_2.place(x=20, y=75)

    label_2 = Label(tab3, text="FTR: ", width=8, font=("bold", 10))
    label_2.place(x=260, y=75)

    entry_2 = Entry(tab3, textvar=FTR2)
    entry_2.place(x=320, y=75)

    label_2 = Label(tab3, text="DET: ", width=10, font=("bold", 10))
    label_2.place(x=500, y=75)

    entry_2 = Entry(tab3, textvar=DET2)
    entry_2.place(x=570, y=75)

    label_2 = Label(tab3, text="Зовнішні запити (EQ): ", width=0, font=("bold", 10))
    label_2.place(x=20, y=100)

    label_2 = Label(tab3, text="FTR: ", width=8, font=("bold", 10))
    label_2.place(x=260, y=100)

    entry_2 = Entry(tab3, textvar=FTR3)
    entry_2.place(x=320, y=100)

    label_2 = Label(tab3, text="DET: ", width=10, font=("bold", 10))
    label_2.place(x=500, y=100)

    entry_2 = Entry(tab3, textvar=DET3)
    entry_2.place(x=570, y=100)

    label_2 = Label(tab3, text="Лок. внут. логічні файли (ILF): ", width=0, font=("bold", 10))
    label_2.place(x=20, y=125)

    label_2 = Label(tab3, text="RET: ", width=8, font=("bold", 10))
    label_2.place(x=260, y=125)

    entry_2 = Entry(tab3, textvar=RET4)
    entry_2.place(x=320, y=125)

    label_2 = Label(tab3, text="DET: ", width=10, font=("bold", 10))
    label_2.place(x=500, y=125)

    entry_2 = Entry(tab3, textvar=DET4)
    entry_2.place(x=570, y=125)

    label_2 = Label(tab3, text="Зовн. інтерфейсні файли(EIF): ", width=0, font=("bold", 10))
    label_2.place(x=20, y=150)

    label_2 = Label(tab3, text="RET: ", width=8, font=("bold", 10))
    label_2.place(x=260, y=150)

    entry_2 = Entry(tab3, textvar=RET5)
    entry_2.place(x=320, y=150)

    label_2 = Label(tab3, text="DET: ", width=10, font=("bold", 10))
    label_2.place(x=500, y=150)

    entry_2 = Entry(tab3, textvar=DET5)
    entry_2.place(x=570, y=150)

    label_11 = Label(tab3, text=" Опис факторів середовища: ", width=0, font=("bold", 13))
    label_11.place(x=20, y=180)

    label_12 = Label(tab3, text="Обмін даними: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=210)
    list1 = [0, 1, 2, 3, 4, 5];
    droplist = OptionMenu(tab3, DACO, *list1)
    DACO.set(0)
    droplist.place(x=270, y=205)

    label_12 = Label(tab3, text="Розподілені функції: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=235)
    droplist = OptionMenu(tab3, DIFU, *list1)
    DIFU.set(0)
    droplist.place(x=270, y=230)

    label_12 = Label(tab3, text="Продуктивність: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=260)
    droplist = OptionMenu(tab3, PERF, *list1)
    PERF.set(0)
    droplist.place(x=270, y=255)

    label_12 = Label(tab3, text="Інтенс. використ. конфігурація: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=285)
    droplist = OptionMenu(tab3, HEUS, *list1)
    HEUS.set(0)
    droplist.place(x=270, y=280)

    label_12 = Label(tab3, text="Інтенсивність транзакцій: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=310)
    droplist = OptionMenu(tab3, TRRA, *list1)
    TRRA.set(0)
    droplist.place(x=270, y=305)

    label_12 = Label(tab3, text="Діалоговтий ввід даних: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=335)
    droplist = OptionMenu(tab3, ONDA, *list1)
    ONDA.set(0)
    droplist.place(x=270, y=330)

    label_12 = Label(tab3, text="Ефективн. для кінц. користувача: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=360)
    droplist = OptionMenu(tab3, ENUS, *list1)
    ENUS.set(0)
    droplist.place(x=270, y=355)

    label_12 = Label(tab3, text="Оперативне обновлення: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=385)
    droplist = OptionMenu(tab3, ONUP, *list1)
    ONUP.set(0)
    droplist.place(x=270, y=380)

    label_12 = Label(tab3, text="Складн. обробки даних: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=410)
    droplist = OptionMenu(tab3, COPR, *list1)
    COPR.set(0)
    droplist.place(x=270, y=405)

    label_12 = Label(tab3, text="Повторне використання: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=435)
    droplist = OptionMenu(tab3, REUS, *list1)
    REUS.set(0)
    droplist.place(x=270, y=430)

    label_12 = Label(tab3, text="Легкість установлення: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=460)
    droplist = OptionMenu(tab3, INEA, *list1)
    INEA.set(0)
    droplist.place(x=270, y=455)

    label_12 = Label(tab3, text="Простота використання: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=485)
    droplist = OptionMenu(tab3, OPEA, *list1)
    OPEA.set(0)
    droplist.place(x=270, y=480)

    label_12 = Label(tab3, text="Поширюваність: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=510)
    droplist = OptionMenu(tab3, MULT, *list1)
    MULT.set(0)
    droplist.place(x=270, y=505)

    label_12 = Label(tab3, text="Легкість зміни: ", width=0, font=("bold", 10))
    label_12.place(x=20, y=535)
    droplist = OptionMenu(tab3, FACH, *list1)
    FACH.set(0)
    droplist.place(x=270, y=530)

    label_12 = Label(tab3, text="Мова програмування: ", width=0, font=("bold", 10))
    label_12.place(x=350, y=190)
    list111 = ['Пакетні файли DOS', 'Basic', 'PL/1', 'C#', 'Розширений LISP', 'Java', 'JavaScript', 'C++', \
               'Visual Basic', 'Мови баз даних', 'Access', 'VBScript', 'Мови підтримки прийняття', \
               'FoxPro 2.5', 'DELPHI', "Стандартні об'єктно-орієнтовані", 'VB.Net', 'Стандартні мови 4-го покоління',
               'HTML 3.0', 'SQL', 'SQL Forms', 'Excel'];
    droplist = OptionMenu(tab3, Language, *list111)
    droplist.config(width=20)
    Language.set(list111[0])
    droplist.place(x=550, y=185)

    label_1 = Label(tab3, text="Тип проекта: ", width=20, font=("bold", 10))
    label_1.place(x=390, y=215)
    list1 = ['Organic', 'Semidetached', 'Embedded'];
    droplist = OptionMenu(tab3, cocomo_types, *list1)
    droplist.config(width=15)
    cocomo_types.set(list1[0])
    droplist.place(x=550, y=213)

    Button(tab3, text='Розрахувати', command=rez3, width=20, bg='brown', fg='white').place(x=520, y=255)


tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Cocomo 1')
tab_control.add(tab2, text='Cocomo 2')
tab_control.add(tab3, text='Метод функціональних точок')
drav1()
drav2()
drav3()
tab_control.pack(expand=1, fill='both')

root.mainloop()
