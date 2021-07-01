import tkinter
from tkinter import BOTH, END
root = tkinter.Tk()
root.title('Altimeter Calculator')
#root.iconbitmap('altimeter.ico')
root.geometry('300x150')
root.resizable(0,0)

#Frames
data_frame = tkinter.LabelFrame(root, text='Operational Data', height=100)
output_frame = tkinter.LabelFrame(root, text='Altimeter Setting', height=50)

#Packing to frames
data_frame.pack(fill=BOTH, expand=True)
output_frame.pack(fill=BOTH)

#Operational Data Layout
tkinter.Label(data_frame, text='DAF Elevation').grid(row=0, column=0)
tkinter.Label(data_frame, text='DZ Elevation').grid(row=1, column=0)

#Altimeter settings Layout
tkinter.Label(output_frame, text='Set altimeter to').grid(row=0, column=0)

#Inputs
DAF_entry = tkinter.Entry(data_frame)
DAF_entry.grid(row=0, column=1)
DZ_entry = tkinter.Entry(data_frame)
DZ_entry.grid(row=1, column=1)

#Define Calculate function
def calculate():
    #global setting
    daf = DAF_entry.get()
    dz = DZ_entry.get()
    a = int(daf)
    b = int(dz) 
    #DAF_entry.delete(0, END)
    #DZ_entry.delete(0, END)

#If the DAF is below the DZ, and they are BOTH above seal level.
    if a < b and a > 0 and b > 0:
        setting = ((b-a) * -1),'(-) back on altimeter'
   
#If the DAF is above the DZ, and they are BOTH above sea level.
    if a > b and a > 0 and b > 0:
        setting = (a-b),'(+) forward on altimeter'

#If the DAF is at Sea Level, and the DZ is above Sea Level.    
    if a == 0 and b > 0: 
        setting = (b * -1),'(-) back on altimeter'
    
#If the DAF is above Sea Level, and the DZ is at Sea Level. 
    if a > 0 and b == 0: 
        setting = a,'(+) forward on altimeter'

#If the DAF is below Sea Level, and the DZ is at Sea Level.
    if a < 0 and b == 0:
        setting = ((a + b) * -1), 'back on altimeter'

#If the DAF is below Sea Level, and the DZ is above Sea Level.
    if a < 0 and b > 0:
        setting = ((((a) * -1) + b) * -1),'back on altimeter'

#If the DAF is above Sea Level, and the DZ is below Sea Level.
    if a > 0 and b < 0:
        setting = (a + (b * -1)), 'forward on altimeter'

#If the DAF is equal to the DZ
    if a == b: 
        setting = 'Set at 0'

    text = tkinter.Label(output_frame, text = setting)
    text.grid(row=0, column=1, sticky='WE')

#Calculate
calc_button = tkinter.Button(data_frame, text='Calculate', command=lambda:calculate())
calc_button.grid(row=2, column=1, columnspan=1, sticky='W')

#Run the mainloop
root.mainloop()