"""
@author Jaylord Cris C. Borres
# CC  15 A
# Café Management System GUI with File Menu

"""

from tkinter import *
import random
import time
from tkinter import filedialog
from tkinter import messagebox


cms = Tk()
cms.geometry('1380x720+260+200')
cms.title('Cafe Management System')
cms.resizable(False, False)

# Frames
titleFrame = Frame(cms, width=1380, height=180, bg='Azure', bd=18, relief=RAISED)
titleFrame.pack(side=TOP)

# Receipt and Button Frame holder
rcptBtnFrame = Frame(cms, width=400, height=650, bg='Azure', bd=9, relief=RAISED)
rcptBtnFrame.pack(side=RIGHT)

ttlReceipt = Frame(rcptBtnFrame, width=54, height=6)
ttlReceipt.pack(side=TOP)

lblReceipt = Label(ttlReceipt, font=('Arial', 12, 'bold'), text='Receipt:\t\t\t\t\t  ', bg='Azure',
                fg='Black', justify=RIGHT)
lblReceipt.grid(row=0, column=0)

# Receipt Frame
rcptFrame = Frame(rcptBtnFrame, width=400, height=450, bg='Azure', bd=9, relief=RAISED)
rcptFrame.pack(side=TOP)

# frame for receipt display
dispReceipt = Text(rcptFrame, width=54, height=28, bg='White', bd=3, font=('arial', 9, 'bold'))
dispReceipt.grid(row=0, column=0)


# Button Frame
btnFrame = Frame(rcptBtnFrame, width=400, height=100, bg='Azure', bd=9, relief=RAISED)
btnFrame.pack(side=BOTTOM)

# Drinks, Cakes, Cost Frame Holder
menuFrame = Frame(cms, width=980, height=600, bg='Azure', bd=5, relief=RAISED)
menuFrame.pack(side=LEFT)

# Drinks, Cake Frame Holder
drnkCakeFrame = Frame(menuFrame, width=490, height=350, bg='Azure', bd=5, relief=RAISED)
drnkCakeFrame.pack(side=TOP)

# Drinks, Cake Frame
drinkFrame = Frame(drnkCakeFrame, width=490, height=350, bg='Azure', bd=10, relief=RAISED)
drinkFrame.pack(side=LEFT)
cakeFrame = Frame(drnkCakeFrame, width=490, height=350, bg='Azure', bd=10, relief=RAISED)
cakeFrame.pack(side=RIGHT)

# Cost, Total Frame holder
totalFrame = Frame(menuFrame, width=490, height=250, bg='Azure', bd=5, relief=RAISED)
totalFrame.pack(side=BOTTOM)

# Cost, Total Frame
costFrame = Frame(totalFrame, width=490, height=250, bg='Azure', bd=10, relief=RAISED)
costFrame.pack(side=LEFT)
ttlFrame = Frame(totalFrame, width=490, height=250, bg='Azure', bd=10, relief=RAISED)
ttlFrame.pack(side=RIGHT)

# Background Colors
cms.configure(background='Black')

# Software Header
lblTitle = Label(titleFrame, font=('Univers', 74, 'bold'), text='  Cafe Management System  ', bd=5,
                 bg='Azure',  fg='Black',  justify=CENTER)
lblTitle.grid(row=0, column=0)

# ======================================================================================================================
# variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

# item_cost variables
drink_Price = IntVar()
cake_Price = IntVar()
orderDate = StringVar()
refReceipt = StringVar()
costDrinks = StringVar()
costCake = StringVar()
totalSub = StringVar()
chargeService = StringVar()
taxPaid = StringVar()
costTotal = StringVar()
# item_cost variables
rcptTax = DoubleVar()
rcptSCharge = DoubleVar()
rcptTotalCost = DoubleVar()
rcptDrinkCost = DoubleVar()
rcptCakeCost = DoubleVar()


latte = StringVar()
espresso = StringVar()
iLatte = StringVar()
vCoffee = StringVar()
cappuccino = StringVar()
afCoffee = StringVar()
amCoffee = StringVar()
iCappuccino = StringVar()

cCake = StringVar()
rvCake = StringVar()
bfCake = StringVar()
bCake = StringVar()
lcCake = StringVar()
kcCake = StringVar()
chcCake = StringVar()
qpcCake = StringVar()

orderDate.set(time.strftime('%d/%m/%Y'))

latte.set('0')
espresso.set('0')
iLatte.set('0')
vCoffee.set('0')
cappuccino.set('0')
afCoffee.set('0')
amCoffee.set('0')
iCappuccino.set('0')

cCake.set('0')
rvCake.set('0')
bfCake.set('0')
bCake.set('0')
lcCake.set('0')
kcCake.set('0')
chcCake.set('0')
qpcCake.set('0')

# =============================================== Drinks ===============================================================
# Latte Check button and entry
def is_latte():
    if var1.get():
        entryLatte.configure(state=NORMAL)
        entryLatte.focus()
        latte.set('')
    elif not var1.get():
        entryLatte.configure(state=DISABLED)
        latte.set('0')


Latte = Checkbutton(drinkFrame, text='Latte', variable=var1, onvalue=1, offvalue=0, font=('arial', 17, 'bold'),
                    bg='Azure', command=is_latte).grid(row=0, sticky=W)
entryLatte = Entry(drinkFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                   textvariable=latte, state=DISABLED)
entryLatte.grid(row=0, column=1)

# Espresso Check button and entry ======================================================================================
def is_espresso():
    if var2.get():
        entryEspresso.configure(state=NORMAL)
        entryEspresso.focus()
        espresso.set('')
    elif not var2.get():
        entryEspresso.configure(state=DISABLED)
        espresso.set('0')

Espresso = Checkbutton(drinkFrame, text='Espresso', variable=var2, onvalue=1, offvalue=0, font=('arial', 17, 'bold'),
                    bg='Azure', command=is_espresso).grid(row=1, sticky=W)
entryEspresso = Entry(drinkFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                      textvariable=espresso, state=DISABLED)
entryEspresso.grid(row=1, column=1)

# Iced Latte Check button and entry ====================================================================================
def is_iLatte():
    if var3.get():
        entryILatte.configure(state=NORMAL)
        entryILatte.focus()
        iLatte.set('')
    elif not var3.get():
        entryILatte.configure(state=DISABLED)
        iLatte.set('0')

icedLatte = Checkbutton(drinkFrame, text='Iced Latte', variable=var3, onvalue=1, offvalue=0,
                        font=('arial', 17, 'bold'), bg='Azure', command=is_iLatte).grid(row=2, sticky=W)
entryILatte = Entry(drinkFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                    textvariable=iLatte, state=DISABLED)
entryILatte.grid(row=2, column=1)

# Vale Coffee Check button and entry ===================================================================================
def is_vCoffee():
    if var4.get():
        entryVCoffee.configure(state=NORMAL)
        entryVCoffee.focus()
        vCoffee.set('')
    elif not var4.get():
        entryVCoffee.configure(state=DISABLED)
        vCoffee.set('0')

valeCoffee = Checkbutton(drinkFrame, text='Vale Coffee', variable=var4, onvalue=1, offvalue=0,
                         font=('arial', 17, 'bold'), bg='Azure', command=is_vCoffee).grid(row=3, sticky=W)
entryVCoffee = Entry(drinkFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                     textvariable=vCoffee, state=DISABLED)
entryVCoffee.grid(row=3, column=1)

# Cappuccino Check button and entry ====================================================================================
def is_cappuccino():
    if var5.get():
        entryCappuccino.configure(state=NORMAL)
        entryCappuccino.focus()
        cappuccino.set('')
    elif not var5.get():
        entryCappuccino.configure(state=DISABLED)
        cappuccino.set('0')

Cappuccino = Checkbutton(drinkFrame, text='Cappuccino', variable=var5, onvalue=1, offvalue=0,
                         font=('arial', 17, 'bold'), bg='Azure', command=is_cappuccino).grid(row=4, sticky=W)
entryCappuccino = Entry(drinkFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                        textvariable=cappuccino, state=DISABLED)
entryCappuccino.grid(row=4, column=1)

# African Coffee Check button and entry ================================================================================
def is_afCoffee():
    if var6.get():
        entryAfCoffee.configure(state=NORMAL)
        entryAfCoffee.focus()
        afCoffee.set('')
    elif not var6.get():
        entryAfCoffee.configure(state=DISABLED)
        afCoffee.set('0')

africanCoffee = Checkbutton(drinkFrame, text='African Coffee', variable=var6, onvalue=1, offvalue=0,
                            font=('arial', 17, 'bold'), bg='Azure', command=is_afCoffee).grid(row=5, sticky=W)
entryAfCoffee = Entry(drinkFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                      textvariable=afCoffee, state=DISABLED)
entryAfCoffee.grid(row=5, column=1)

# American Coffee Check button and entry ===============================================================================
def is_amCoffee():
    if var7.get():
        entryAmCoffee.configure(state=NORMAL)
        entryAmCoffee.focus()
        amCoffee.set('')
    elif not var7.get():
        entryAmCoffee.configure(state=DISABLED)
        amCoffee.set('0')

americanCoffee = Checkbutton(drinkFrame, text='American Coffee', variable=var7, onvalue=1, offvalue=0,
                             font=('arial', 17, 'bold'), bg='Azure', command=is_amCoffee).grid(row=6, sticky=W)
entryAmCoffee = Entry(drinkFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                      textvariable=amCoffee, state=DISABLED)
entryAmCoffee.grid(row=6, column=1)

# Iced Cappuccino Check button and entry ===============================================================================
def is_iCappuccino():
    if var8.get():
        entryICappuccino.configure(state=NORMAL)
        entryICappuccino.focus()
        iCappuccino.set('')
    elif not var8.get():
        entryICappuccino.configure(state=DISABLED)
        iCappuccino.set('0')

icedCappuccino = Checkbutton(drinkFrame, text='Iced Cappuccino\t   ', variable=var8, onvalue=1, offvalue=0,
                             font=('arial', 17, 'bold'), bg='Azure', command=is_iCappuccino).grid(row=7, sticky=W)
entryICappuccino = Entry(drinkFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                         textvariable=iCappuccino, state=DISABLED)
entryICappuccino.grid(row=7, column=1)

# ==================================================== Cakes ===========================================================
# Coffee Cake Check button and entry
def is_cCake():
    if var9.get():
        entryCCake.configure(state=NORMAL)
        entryCCake.focus()
        cCake.set('')
    elif not var9.get():
        entryCCake.configure(state=DISABLED)
        cCake.set('0')

coffeeCake = Checkbutton(cakeFrame, text='Coffee Cake', variable=var9, onvalue=1, offvalue=0,
                         font=('arial', 17, 'bold'), bg='Azure', command=is_cCake).grid(row=0, sticky=W)
entryCCake = Entry(cakeFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                   textvariable=cCake, state=DISABLED)
entryCCake.grid(row=0, column=1)

# Red Velvet Cake Check button and entry ===============================================================================
def is_rvCake():
    if var10.get():
        entryRVCake.configure(state=NORMAL)
        entryRVCake.focus()
        rvCake.set('')
    elif not var10.get():
        entryRVCake.configure(state=DISABLED)
        rvCake.set('0')

redvCake = Checkbutton(cakeFrame, text='Red Velvet Cake', variable=var10, onvalue=1, offvalue=0,
                       font=('arial', 17, 'bold'), bg='Azure', command=is_rvCake).grid(row=1, sticky=W)
entryRVCake = Entry(cakeFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                    textvariable=rvCake, state=DISABLED)
entryRVCake.grid(row=1, column=1)

# Black Forest Cake Check button and entry =============================================================================
def is_bfCake():
    if var11.get():
        entryBFCake.configure(state=NORMAL)
        entryBFCake.focus()
        bfCake.set('')
    elif not var11.get():
        entryBFCake.configure(state=DISABLED)
        bfCake.set('0')

blckfCake = Checkbutton(cakeFrame, text='Black Forest Cake', variable=var11, onvalue=1, offvalue=0,
                        font=('arial', 17, 'bold'), bg='Azure', command=is_bfCake).grid(row=2, sticky=W)
entryBFCake = Entry(cakeFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                    textvariable=bfCake, state=DISABLED)
entryBFCake.grid(row=2, column=1)

# Boston Cream Cake Check button and entry =============================================================================
def is_bCake():
    if var12.get():
        entryBCake.configure(state=NORMAL)
        entryBCake.focus()
        bCake.set('')
    elif not var12.get():
        entryBCake.configure(state=DISABLED)
        bCake.set('0')

bstncCake = Checkbutton(cakeFrame, text='Boston Cream Cake', variable=var12, onvalue=1, offvalue=0,
                        font=('arial', 17, 'bold'), bg='Azure', command=is_bCake).grid(row=3, sticky=W)
entryBCake = Entry(cakeFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                   textvariable=bCake, state=DISABLED)
entryBCake.grid(row=3, column=1)

# Lagos Chocolate Cake Check button and entry ==========================================================================
def is_lcCake():
    if var13.get():
        entryLCCake.configure(state=NORMAL)
        entryLCCake.focus()
        lcCake.set('')
    elif not var13.get():
        entryLCCake.configure(state=DISABLED)
        lcCake.set('0')

lgscCake = Checkbutton(cakeFrame, text='Lagos Chocolate Cake', variable=var13, onvalue=1, offvalue=0,
                       font=('arial', 17, 'bold'), bg='Azure', command=is_lcCake).grid(row=4, sticky=W)
entryLCCake = Entry(cakeFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                    textvariable=lcCake, state=DISABLED)
entryLCCake.grid(row=4, column=1)

# Kilburn Chocolate Cake Check button and entry ========================================================================
def is_kcCake():
    if var14.get():
        entryKCCake.configure(state=NORMAL)
        entryKCCake.focus()
        kcCake.set('')
    elif not var14.get():
        entryKCCake.configure(state=DISABLED)
        kcCake.set('0')

kbncCake = Checkbutton(cakeFrame, text='Kilburn Chocolate Cake', variable=var14, onvalue=1, offvalue=0,
                       font=('arial', 17, 'bold'), bg='Azure', command=is_kcCake).grid(row=5, sticky=W)
entryKCCake = Entry(cakeFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                    textvariable=kcCake, state=DISABLED)
entryKCCake.grid(row=5, column=1)

# Carlton Hill Chocolate Cake Check button and entry ===================================================================
def is_chcCake():
    if var15.get():
        entryCHCCake.configure(state=NORMAL)
        entryCHCCake.focus()
        chcCake.set('')
    elif not var15.get():
        entryCHCCake.configure(state=DISABLED)
        chcCake.set('0')

cthcCake = Checkbutton(cakeFrame, text='Carlton Hill Chocolate Cake', variable=var15, onvalue=1, offvalue=0,
                       font=('arial', 17, 'bold'), bg='Azure', command=is_chcCake).grid(row=6, sticky=W)
entryCHCCake = Entry(cakeFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                     textvariable=chcCake, state=DISABLED)
entryCHCCake.grid(row=6, column=1)

# Queen's Park Chocolate Cake Check button and entry ===================================================================
def is_qpcCake():
    if var16.get():
        entryQPCCake.configure(state=NORMAL)
        entryQPCCake.focus()
        qpcCake.set('')
    elif not var16.get():
        entryQPCCake.configure(state=DISABLED)
        qpcCake.set('0')

qnpcCake = Checkbutton(cakeFrame, text='Queen\'s Park Chocolate Cake\t', variable=var16, onvalue=1, offvalue=0,
                       font=('arial', 17, 'bold'), bg='Azure', command=is_qpcCake).grid(row=7, sticky=W)

entryQPCCake = Entry(cakeFrame, font=('arial', 17, 'bold'), bd=8, width=6, justify=RIGHT,
                     textvariable=qpcCake, state=DISABLED)
entryQPCCake.grid(row=7, column=1)

# =========================================== Cost and Total ===========================================================
# Drink Cost label and entry
drinkCost = Label(costFrame, font=('arial', 17, 'bold'), text='Cost of Drinks\t', bg='Azure',  fg='Black')
drinkCost.grid(row=0, column=0, sticky=W)
entryDCost = Entry(costFrame, font=('arial', 17, 'bold'), bd=7, bg='White',  insertwidth=2,
                   textvariable=costDrinks, justify=LEFT)
entryDCost.grid(row=0, column=1)

# Cake Cost label and entry ============================================================================================
cakeCost = Label(costFrame, font=('arial', 17, 'bold'), text='Cost of Cakes', bg='Azure',  fg='Black')
cakeCost.grid(row=1, column=0, sticky=W)
entryCCost = Entry(costFrame, font=('arial', 17, 'bold'), bd=7, bg='White',  insertwidth=2,
                   textvariable=costCake, justify=LEFT)
entryCCost.grid(row=1, column=1)

# Service Charge label and entry =======================================================================================
serviceCharge = Label(costFrame, font=('arial', 17, 'bold'), text='Service Charge', bg='Azure',  fg='Black')
serviceCharge.grid(row=2, column=0, sticky=W)
entrySCharge = Entry(costFrame, font=('arial', 17, 'bold'), bd=7, bg='White',  insertwidth=2,
                     textvariable=chargeService, justify=LEFT)
entrySCharge.grid(row=2, column=1)

# Paid tax label and entry =============================================================================================
paidTax = Label(ttlFrame, font=('arial', 17, 'bold'), text='Paid Tax\t', bg='Azure',  fg='Black')
paidTax.grid(row=0, column=0, sticky=W)
entryPTax = Entry(ttlFrame, font=('arial', 17, 'bold'), bd=7, bg='White',  insertwidth=2,
                  textvariable=taxPaid, justify=LEFT)
entryPTax.grid(row=0, column=1)

# Sub Total label and entry ============================================================================================
subTotal = Label(ttlFrame, font=('arial', 17, 'bold'), text='Sub Total', bg='Azure',  fg='Black')
subTotal.grid(row=1, column=0, sticky=W)
entrySTotal = Entry(ttlFrame, font=('arial', 17, 'bold'), bd=7, bg='White',  insertwidth=2,
                    textvariable=totalSub, justify=LEFT)
entrySTotal.grid(row=1, column=1)

# Total Cost label and entry ===========================================================================================
totalCost = Label(ttlFrame, font=('arial', 17, 'bold'), text='Total Cost  ', bg='Azure',  fg='Black')
totalCost.grid(row=2, column=0, sticky=W)
entryTCost = Entry(ttlFrame, font=('arial', 17, 'bold'), bd=7, bg='White',  insertwidth=2,
                   textvariable=costTotal, justify=LEFT)
entryTCost.grid(row=2, column=1)

# ========================================== Functions & Buttons =======================================================

def openfile():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Open File",
                                          filetypes=(("Text Files", "*.txt"), ("All files",
                                                                               "*.*")))
    try:
        if filename:
            # mode 'rb' = read binary and decode to display unicodes (e.g. peso sign)
            the_file = open(filename, 'rb')
            dispReceipt.insert(END, the_file.read().decode())
            the_file.close()
        elif filename == '':
            messagebox.showinfo('Cancel', 'Cancelled Operation')
    except IOError:
        messagebox.showinfo('Error', 'Could not Open the File')


def save_as():
    # mode 'wb' write binary including unicodes (e.g. peso sign)
    save_text_as = filedialog.asksaveasfile(mode='wb', defaultextension='.txt', title="Save as",
                                            filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))

    if save_text_as:
        # assign the texts in the receipt to a variable and encode to include unicodes (e.g. peso sign)
        text_to_save = dispReceipt.get(1.0, END).encode()
        save_text_as.write(text_to_save)
        save_text_as.close()
    else:
        messagebox.showinfo('Error', 'Cancelled')


def close_file():
    dispReceipt.delete('1.0', END)  # start from line 1 character 0 to END


menuBar = Menu(cms)

fileMenuItems = Menu(menuBar, tearoff=0)

fileMenuItems.add_command(label="Open", command=openfile)
fileMenuItems.add_command(label="Save as", command=save_as)
fileMenuItems.add_command(label="Close", command=close_file)
fileMenuItems.add_command(label="Quit", command=cms.quit)

menuBar.add_cascade(label="File", menu=fileMenuItems)
cms.config(menu=menuBar)


# Receipt function for receipt button
def receipt():
    dispReceipt.delete('1.0', END)
    ref = random.randint(1000000, 99999999)
    refNum = str(ref)
    refReceipt.set(refNum)

    dispReceipt.insert(END, 'Receipt Ref: ' + refReceipt.get() + '\t\t\t\tPurchase Date: ' + orderDate.get() + '\n')
    dispReceipt.insert(END, 'Items \t\t\t\t\tQuantity\n')
    dispReceipt.insert(END, '\n')

    if drink_Price.get():
        dispReceipt.insert(END, '---------------------- Coffees --------------------------------------------------'
                            '----------\n')
    if var1.get():
        dispReceipt.insert(END, 'Latte \t\t\t\t\t' + latte.get() + '\n')
    if var2.get():
        dispReceipt.insert(END, 'Espresso \t\t\t\t\t' + espresso.get() + '\n')
    if var3.get():
        dispReceipt.insert(END, 'Iced Latte \t\t\t\t\t' + iLatte.get() + '\n')
    if var4.get():
        dispReceipt.insert(END, 'Vale Coffee \t\t\t\t\t' + vCoffee.get() + '\n')
    if var5.get():
        dispReceipt.insert(END, 'Cappuccino \t\t\t\t\t' + cappuccino.get() + '\n')
    if var6.get():
        dispReceipt.insert(END, 'African Coffee \t\t\t\t\t' + afCoffee.get() + '\n')
    if var7.get():
        dispReceipt.insert(END, 'American Coffee \t\t\t\t\t' + amCoffee.get() + '\n')
    if var8.get():
        dispReceipt.insert(END, 'Iced Cappuccino \t\t\t\t\t' + iCappuccino.get() + '\n')

    if drink_Price.get():
        dispReceipt.insert(END, '\n')
    if cake_Price.get():
        dispReceipt.insert(END, '---------------------- Cakes ----------------------------------------------------'
                            '----------\n')

    if var9.get():
        dispReceipt.insert(END, 'Coffee Cake \t\t\t\t\t' + cCake.get() + '\n')
    if var10.get():
        dispReceipt.insert(END, 'Red Velvet Cake \t\t\t\t\t' + rvCake.get() + '\n')
    if var11.get():
        dispReceipt.insert(END, 'Black Forest Cake \t\t\t\t\t' + bfCake.get() + '\n')
    if var12.get():
        dispReceipt.insert(END, 'Boston Cream Cake \t\t\t\t\t' + bCake.get() + '\n')
    if var13.get():
        dispReceipt.insert(END, 'Lagos Chocolate Cake \t\t\t\t\t' + lcCake.get() + '\n')
    if var14.get():
        dispReceipt.insert(END, 'Kilburn Chocolate Cake \t\t\t\t\t' + kcCake.get() + '\n')
    if var15.get():
        dispReceipt.insert(END, 'Carlton Hill Chocolate Cake \t\t\t\t\t' + chcCake.get() + '\n')
    if var16.get():
        dispReceipt.insert(END, 'Queen\'s Park Chocolate Cake \t\t\t\t\t' + qpcCake.get())

    dispReceipt.insert(END, '\n\n')

    if drink_Price.get():
        dispReceipt.insert(END, 'Drink Cost \t\t\t\t\t₱ ' + str('%.2f' %(rcptDrinkCost.get()) + '\n'))
    if cake_Price.get():
        dispReceipt.insert(END, 'Cake Cost \t\t\t\t\t₱ ' + str('%.2f' %(rcptCakeCost.get()) + '\n'))

    dispReceipt.insert(END, 'Service Charge \t\t\t\t\t₱ ' + str('%.2f' % (rcptSCharge.get()) + '\n'))
    dispReceipt.insert(END, 'Tax \t\t\t\t\t₱ ' + str('%.2f' % (rcptTax.get()) + '\n'))
    dispReceipt.insert(END, 'Total Cost \t\t\t\t\t₱ ' + str('%.2f'%(rcptTotalCost.get()) + '\n'))


# Item Cost for total button
def item_cost():
    item1 = float(latte.get())
    item2 = float(espresso.get())
    item3 = float(iLatte.get())
    item4 = float(vCoffee.get())
    item5 = float(cappuccino.get())
    item6 = float(afCoffee.get())
    item7 = float(amCoffee.get())
    item8 = float(iCappuccino.get())
    item9 = float(cCake.get())
    item10 = float(rvCake.get())
    item11 = float(bfCake.get())
    item12 = float(bCake.get())
    item13 = float(lcCake.get())
    item14 = float(kcCake.get())
    item15 = float(chcCake.get())
    item16 = float(qpcCake.get())

    drinkPrice = (item1 * 140) + (item2 * 120) + (item3 * 120) + (item4 * 155) + (item5 * 170) + (item6 * 180) \
                 + (item7 * 170) + (item8 *165)
    cakePrice = (item9 * 120) + (item10 * 130) + (item11 * 120) + (item12 * 125) + (item13 * 140) + (item14 * 135) \
                 + (item15 * 170) + (item16 *185)

    drinks = '₱', str('%.2f'%(drinkPrice))
    cakes = '₱', str('%.2f'%(cakePrice))
    costDrinks.set(drinks)
    costCake.set(cakes)
    sCharge = '₱', str('%.2f'%(10))
    chargeService.set(sCharge)

    itemSubTotal = '₱', str('%.2f'%(drinkPrice + cakePrice + 10))
    totalSub.set(itemSubTotal)
    Tax = '₱', str('%.2f'%((drinkPrice + cakePrice + 10) * 0.12))
    taxPaid.set(Tax)
    totalTax = (drinkPrice + cakePrice + 10) * 0.12
    cost = '₱', str('%.2f'%(drinkPrice + cakePrice + 10 + totalTax))
    costTotal.set(cost)

    # For Receipt Display
    drink_Price.set(drinkPrice)
    cake_Price.set(cakePrice)

    rcptDrinkCost.set(drinkPrice)
    rcptCakeCost.set(cakePrice)
    tCost = drinkPrice + cakePrice + 10 + totalTax
    rcptTotalCost.set(tCost)
    pTax = (drinkPrice + cakePrice + 10) * 0.12
    rcptTax.set(pTax)
    rcptSCharge.set(10)

# Reset function for reset button
def reset():
    taxPaid.set('')
    costTotal.set('')
    totalSub.set('')
    costDrinks.set('')
    costCake.set('')
    chargeService.set('')
    dispReceipt.delete('1.0', END)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    drink_Price.set(0)
    cake_Price.set(0)
    rcptTax.set(0.00)
    rcptSCharge.set(0.00)
    rcptTotalCost.set(0.00)
    rcptDrinkCost.set(0.00)
    rcptCakeCost.set(0.00)

    latte.set('0')
    espresso.set('0')
    iLatte.set('0')
    vCoffee.set('0')
    cappuccino.set('0')
    afCoffee.set('0')
    amCoffee.set('0')
    iCappuccino.set('0')
    cCake.set('0')
    rvCake.set('0')
    bfCake.set('0')
    bCake.set('0')
    lcCake.set('0')
    kcCake.set('0')
    chcCake.set('0')
    qpcCake.set('0')

    entryLatte.configure(state=DISABLED)
    entryEspresso.configure(state=DISABLED)
    entryILatte.configure(state=DISABLED)
    entryVCoffee.configure(state=DISABLED)
    entryCappuccino.configure(state=DISABLED)
    entryAfCoffee.configure(state=DISABLED)
    entryAmCoffee.configure(state=DISABLED)
    entryICappuccino.configure(state=DISABLED)
    entryCCake.configure(state=DISABLED)
    entryRVCake.configure(state=DISABLED)
    entryBFCake.configure(state=DISABLED)
    entryBCake.configure(state=DISABLED)
    entryLCCake.configure(state=DISABLED)
    entryKCCake.configure(state=DISABLED)
    entryCHCCake.configure(state=DISABLED)
    entryQPCCake.configure(state=DISABLED)

# Exit function for exit button
def is_exit():
    is_exit = messagebox.askyesno('Confirm Exit', 'Are you sure you want to exit?')
    if is_exit:
        cms.destroy()
        return

# frame for buttons display
btnTotal = Button(btnFrame, padx=15, pady=1, fg='Black', text='Total', font=('arial', 16, 'bold'), width=4,
                  bg='Azure', bd=5, command=item_cost).grid(row=0, column=0)
btnReceipt = Button(btnFrame, padx=15, pady=1, fg='Black', text='Receipt', font=('arial', 16, 'bold'), width=4,
                  bg='Azure', bd=5, command=receipt).grid(row=0, column=1)
btnReset = Button(btnFrame, padx=15, pady=1, fg='Black', text='Reset', font=('arial', 16, 'bold'), width=4,
                  bg='Azure', bd=5, command=reset).grid(row=0, column=2)
btnExit = Button(btnFrame, padx=15, pady=1, fg='Black', text='Exit', font=('arial', 16, 'bold'), width=4,
                  bg='Azure', bd=5, command=is_exit).grid(row=0, column=3)

cms.mainloop()
