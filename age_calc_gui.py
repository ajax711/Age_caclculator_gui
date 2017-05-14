import datetime
import tkinter as tk 
from tkinter import PhotoImage

class Person:
	def __init__(self, name,birthdate):
	   self.name=name
	   self.birthdate=birthdate
	   
	def age(self):
		now = datetime.date.today()
		age = (now.year-self.birthdate.year)
		return age
		
work_place = tk.Tk()
work_place.geometry("750x750")
work_place.title("Age calculator")


p1=PhotoImage(file='capture.png')
label1=tk.Label(height='300',width='500',image=p1)
label1.grid(column=1,row=1)

#Labels

name_label =tk.Label(text = "Enter you name")
name_label.grid(column=0 , row =2)

year_label =tk.Label(text = "Enter the year")
year_label.grid(column=0 , row =3)

month_label =tk.Label(text = "Enter the month")
month_label.grid(column=0 , row =4)

day_label =tk.Label(text = "Enter the day")
day_label.grid(column=0 , row =5)

#Entries
name_entry =tk.Entry()
name_entry.grid(column=1 , row =2)

year_entry =tk.Entry()
year_entry.grid(column=1 , row =3)

month_entry =tk.Entry()
month_entry.grid(column=1 , row =4)

day_entry =tk.Entry()
day_entry.grid(column=1 , row =5)

#Calculate function
def calculate_age():
  print(year_entry.get())
  print(month_entry.get())
  print(day_entry.get())
  print("Button clicked")
  Shobhit= Person("Shobhit",datetime.date(int(year_entry.get()),
                                          int(month_entry.get()),
                                          int(day_entry.get())))
  print (Shobhit.age())

  answer= tk.Text(master=work_place, height=10, width=25)
  answer.grid (column=1 , row=7)
  answer_text= "{name}, you are {age} years old".format(name=name_entry.get(), age=Shobhit.age())
  answer.insert(tk.END,answer_text)
  
#Calculate Button 
calc_button= tk.Button(text="Calculate",command=calculate_age)
calc_button.grid(column=1 , row= 6)


work_place.mainloop()




