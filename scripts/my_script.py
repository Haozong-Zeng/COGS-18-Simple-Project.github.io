
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter.messagebox as messagebox
import sys
sys.path.append('../')
from my_module.functions import *
import webbrowser

# Create a window called 'Orb Effect and Buff Placer Comparator'
root = Tk()
root.title('Orb Effect and Buff Placer Comparator')
root.geometry('580x360')


# Create the introduction text 'This is a simple app used to compare 2 Orb spells to see if they can co-exist or they will contradict each other'
basicLabel = Label(root, text='This is a simple app used to compare 2 Orb spells to see if they can co-exist or they will contradict each other.')
basicLabel.grid(columnspan=2)


# Create the searching entry and its description.
EmptyLabel_1 = Label(root, text='')
EmptyLabel_1.grid(row=1, columnspan=2)
searchEntry_1 = Entry(root)
searchEntry_1.grid(row=2)
searchLabel_1 = Label(root, text='Input Spell 1')
searchLabel_1.grid(row=3)
searchEntry_2 = Entry(root)
searchEntry_2.grid(row=2, column=1)
searchLabel_2 = Label(root, text='Input Spell 2')
searchLabel_2.grid(row=3, column=1)


# Create a funstion used to get the weapon type.
v = IntVar()
lis=['Normal','Missile','Missile-Splash','Missile-Bounce', 'Artillery', 'Instant', 'Missile-Line', 'Artillery-Line']
Weapon_Type = 'Normal'
def GetWeaponType():
	global Weapon_Type
	for i in range(8):
		if v.get() == i:
			Weapon_Type = lis[i]


# Create the selection button of the unit's weapon type. For more information, search 'Warcraft 3 weapon type'.
EmptyLabel_2 = Label(root, text='')
EmptyLabel_2.grid(row=4, columnspan=2)
Weapon_Type_Label = Label(root, text='Choose Unit Weapon Type')
Weapon_Type_Label.grid(row=9, columnspan=2)
Weapon_Type_1 = Radiobutton(root, text='Normal', value=0, indicatoron=0, variable=v, command=GetWeaponType, width=12)
Weapon_Type_1.grid(row=5, column=0)
Weapon_Type_2 = Radiobutton(root, text='Missile', value=1, indicatoron=0, variable=v, command=GetWeaponType, width=12)
Weapon_Type_2.grid(row=5, column=1)
Weapon_Type_3 = Radiobutton(root, text='Missile-Splash', value=2, indicatoron=0, variable=v, command=GetWeaponType, width=12)
Weapon_Type_3.grid(row=6, column=0)
Weapon_Type_4 = Radiobutton(root, text='Missile-Bounce', value=3, indicatoron=0, variable=v, command=GetWeaponType, width=12)
Weapon_Type_4.grid(row=6, column=1)
Weapon_Type_5 = Radiobutton(root, text='Artillery', value=4, indicatoron=0, variable=v, command=GetWeaponType, width=12)
Weapon_Type_5.grid(row=7, column=0)
Weapon_Type_6 = Radiobutton(root, text='Instant', value=5, indicatoron=0, variable=v, command=GetWeaponType, width=12)
Weapon_Type_6.grid(row=7, column=1)
Weapon_Type_7 = Radiobutton(root, text='Missile-Line', value=6, indicatoron=0, variable=v, command=GetWeaponType, width=12)
Weapon_Type_7.grid(row=8, column=0)
Weapon_Type_8 = Radiobutton(root, text='Artillery-Line', value=7, indicatoron=0, variable=v, command=GetWeaponType, width=12)
Weapon_Type_8.grid(row=8, column=1)



# Create the exploring button
def GetResult():
	Spell_1 = searchEntry_1.get() or '' 
	Spell_2 = searchEntry_2.get() or ''
	global Weapon_Type
	messagebox.showinfo('Comparason Result', Comparason(Spell_1, Spell_2, Weapon_Type))
EmptyLabel_3 = Label(root, text='')
EmptyLabel_3.grid(row=10, columnspan=2)
Explore_Button = Button(root, text='Compare', command=GetResult, width=24, borderwidth=1, relief='solid')
Explore_Button.grid(row=11, columnspan=2)




# Create the button that open the website link - my article about Orb Effects and Buff Placers.
EmptyLabel_4 = Label(root, text='')
EmptyLabel_4.grid(row=12, columnspan=2)
def OpenLink():
	url = 'https://zhuanlan.zhihu.com/p/67990347'
	webbrowser.open(url, new=0, autoraise=True)

Link_Button = Button(root, text='More Info', command=OpenLink, width=24, borderwidth=1, relief='solid')
Link_Button.grid(row=13, columnspan=2)


# Loop the window
root.mainloop()


