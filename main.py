
def io(i, g):
    i = float(i)
    g = float(g)
    p = ((1 + i) / (1 + g) - 1)
    return p


def pain(a, i, n):  # Series Present Worth
    a = float(a)
    i = float(i)
    n = float(n)
    p = a * ((((1 + i) ** n) - 1) / (i(1 + i) ** n))
    return p


def pagin(a, g, i, n):  # USE IO IN PLACE OF I WITH PAGIN

    a = float(a)
    g = float(g)
    i = float(i)
    n = float(n)
    p = a * ((((1 + i) ** n) - 1) / (i(1 + i) ** n)) * (1 / (1 + g))
    return p


def pfin(f, i, n):
    f = float(f)
    i = float(i)
    n = float(n)
    p = f * (1 / ((1 + i) ** n))
    return p


def fpin(p, i, n):
    p = float(p)
    i = float(i)
    n = float(n)
    f = p * (1 + i) ** n
    return f


def ipfn(p, f, n):
    p = float(p)
    f = float(f)
    n = float(n)
    i = ((p / f) ** (1 / n)) - 1
    return i


def fain(a, i, n):
    pass


def afin(f, i, n):
    pass


def apin(p, i, n):
    pass


def agin(g, i, n):
    pass


def pgin(g, i, n):
    pass

inp = input("Enter necessary function.\nFunctions available:"
            "\nIo, (P/A,i,n), (P/A,g,i,n), (P/F,i,n), (F/P,i,n).\n")
args = input("Enter arguments, separated by spaces.\n")

args = args.split(" ")

for x in args:
    x = float(x)
# https://staff.emu.edu.tr/gokhanizbirak/Documents/courses/ieng323-mane323/assignments-homeworks/Formulas-Engineering-Economy.pdf
# i = Interest rate per interest period.
# n = Number of interest periods.
# P = A present sum of money.
# F = A future sum of money.
# A = An end-of-period cash receipt or disbursement in a uniform series continuing for n periods.
# G = Uniform period-by-period increase or decrease in cash receipts or disbursements.
# g = Uniform rate of cash flow increase or decrease from period to period; the geometric gradient.
# r = Nominal interest rate per interest period.
# m = Number of compounding subperiods per period.
if inp == 'io':
    print(io(args[0], args[1]))
elif inp == 'pain':
    print(pain(args[0], args[1], args[2]))
elif inp == 'pagin':
    print(pagin(args[0], args[1], args[2], args[3]))
elif inp == 'pfin':
    print(pfin(args[0], args[1], args[2]))
elif inp == 'fpin':
    print(fpin(args[0], args[1], args[2]))
elif inp == 'ipfn':
    print(ipfn(args[0], args[1], args[2]))
