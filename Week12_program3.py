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