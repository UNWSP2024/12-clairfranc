# UNWSP-Python-Week-12

# Claire Francis, Week12_program1, April 25, 2025.
# Write a GUI program that calculates a car's gas mileage.
# The program's window should have Entry widgets that let the
# user enter the number of gallons of gas the car holds,
# and the number of miles it can be driven on a full tank.
# When a Calculate MPG button is clicked,
# the program should display the number of miles that the car may
# be driven per gallon of gas.
# Use the following formula to calculate miles per gallon:  MPG = miles / gallons.


import tkinter
import tkinter.messagebox


class MilesperGallonGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)



        self.gallon_label = tkinter.Label(self.top_frame, text = 'Enter number of gallons car holds:')
        self.g_entry = tkinter.Entry(self.top_frame, width = 10)

        self.mile_label = tkinter.Label(self.top_frame, text='Enter number miles car can be driven per full tank:')
        self.m_entry = tkinter.Entry(self.top_frame, width=10)



        self.gallon_label.pack(side='left')
        self.g_entry.pack(side='left')

        self.mile_label.pack(side='left')
        self.m_entry.pack(side='left')


        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Convert', command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')


        self.top_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop()



    def convert(self):


        g = float(self.g_entry.get())
        m = float(self.m_entry.get())

        MPG = m / g


        tkinter.messagebox.showinfo('Results', ' This car can be driven ' + str(MPG) + ' miles per gallon.')

if __name__ == '__main__':
    miles_conv = MilesperGallonGUI()























# Claire Francis, April 25, 2025, Week12_program2
# Joe's Automotive performs the following routine maintenance service:
#
# Oil Change - $30.00
# Lube Job - $20.00
# Radiator Flush - $40.00
# Transmission Fluid - $100.00
# Inspection - $35.00
# Muffler replacement - $200.00
# Tire Rotation - $20.00
# Write a GUI with check buttons that allows the user to select any or all of these services.
# When the user clicks a button, the total charges should be displayed.



import tkinter
import tkinter.messagebox


class MyGUI:

    def __init__(self):

        self.main_window = tkinter.Tk()


        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()




        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame, text = 'Oil Change - $30.00', variable = self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text = 'Lube Job - $20.00', variable = self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text = 'Radiator Flush - $40.00', variable = self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text = 'Transmission Fluid - $100.00', variable = self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text = 'Inspection - $35.00', variable = self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text = 'Muffler replacement - $200.00', variable = self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text = 'Tire Rotation - $20.00', variable = self.cb_var7)



        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()


        self.ok_button = tkinter.Button(self.bottom_frame, text = 'OK', command = self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)


        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


    def show_choice(self):
        t = 0


        if self.cb_var1.get() == 1:
            t += 30

        if self.cb_var2.get() == 1:
            t += 20

        if self.cb_var3.get() == 1:
            t += 40

        if self.cb_var4.get() == 1:
            t += 100

        if self.cb_var5.get() == 1:
            t += 35

        if self.cb_var6.get() == 1:
            t += 200

        if self.cb_var7.get() == 1:
            t += 20

        total = str(t)

        tkinter.messagebox.showinfo('Result', 'Your total is $' + total)

if __name__ == '__main__':
    mygui = MyGUI()























# Claire Francis, April 25, 2025, Week12_program3
# A long-distance provider charges the following rates for telephone calls:
# Rate Category	Rate per Minute
# Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02
# Evening (6:00 P.M.  through 11:59 P.M.) 	$0.12
# Off-Peak (midnight through 5:59 P.M.) 	$0.05
#
# Write a GUI application that allows the user to select a rate category (from a set of radio buttons),
# and enter the number of minutes of the call into an Entry widget.
# An info dialog box  should display the charge for the call.



import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create an IntVar object to use with the Radibuttons
        self.radio_var = tkinter.IntVar()

        # Set the intVa object to 1
        self.radio_var.set(1)

        # Create the Radiobutton widgets in the top_frame
        self.rb1 = tkinter.Radiobutton(self.top_frame, text = 'Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02', variable = self.radio_var, value = 0.02)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text = 'Evening (6:00 P.M.  through 11:59 P.M.) 	$0.12', variable = self.radio_var, value = 0.12)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text = 'Off-Peak (midnight through 5:59 P.M.) 	$0.05', variable = self.radio_var, value = 0.05)

        self.minutes_label = tkinter.Label(self.top_frame, text = 'Enter number of minutes for call:')
        self.min_entry = tkinter.Entry(self.top_frame, width = 10)

        # Pack the Radiobuttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.minutes_label.pack(side='left')
        self.min_entry.pack(side='left')

        # create OK button and Quit button
        self.ok_button = tkinter.Button(self.bottom_frame, text = 'OK', command = self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)

        # Pack the Buttons
        self.ok_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()


        # Start the mainloop
        tkinter.mainloop()

        # The show_chioce method is the callback function for the OK button

    def show_choice(self):
        t = 0
        m = float(self.min_entry.get())



        if self.rb1:
            t = m * 0.02

        if self.rb2:
            t = m * 0.12

        if self.rb3:
            t = m * 0.05


        total = str(t)

        tkinter.messagebox.showinfo('Result', 'Your total is $' + total)
if __name__ == '__main__':
    my_gui = MyGUI()
