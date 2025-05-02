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