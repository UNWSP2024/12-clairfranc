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

    # Create the main window.
        self.main_window = tkinter.Tk()

    # Create two frames to group widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


  # Create the widgets for the top frame.

        self.gallon_label = tkinter.Label(self.top_frame, text = 'Enter number of gallons car holds:')
        self.g_entry = tkinter.Entry(self.top_frame, width = 10)

        self.mile_label = tkinter.Label(self.top_frame, text='Enter number miles car can be driven per full tank:')
        self.m_entry = tkinter.Entry(self.top_frame, width=10)


    # Pack the top frame's widgets.

        self.gallon_label.pack(side='left')
        self.g_entry.pack(side='left')

        self.mile_label.pack(side='left')
        self.m_entry.pack(side='left')

  # Create the button widgets for the bottom frame.

        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Convert', command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)
  # Pack the buttons.

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

  # Pack the frames.

        self.top_frame.pack()
        self.bottom_frame.pack()

  # Enter the tkinter main loop.

        tkinter.mainloop()

  # The convert method is a callback function for
  # the Calculate button.


    def convert(self):
        # Get the value entered by the user into the

        # kilo_entry widget.

        g = float(self.g_entry.get())
        m = float(self.m_entry.get())
        # Convert kilometers to miles.

        MPG = m / g

        # Display the results in an info dialog box.

        tkinter.messagebox.showinfo('Results', ' This car can be driven ' + str(MPG) + ' miles per gallon.')

  # Create an instance of the KiloConverterGUI class.
if __name__ == '__main__':
    miles_conv = MilesperGallonGUI()
