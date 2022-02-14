import tkinter
from tkinter import *
root = tkinter.Tk()
root.title('FreeFall Jump Calculator')
root.geometry('700x600')
root.resizable(0,0)

def main():
    #Frames
    data_frame = tkinter.LabelFrame(root, text='Operational Data', width=400, height=250, pady=5)
    output_frame = tkinter.LabelFrame(root, text='Calculations', width=700, height=300)

    #Packing to frames
    data_frame.pack(fill=BOTH, expand=True)
    output_frame.pack(fill=BOTH, expand=True)

    #Operational Data Layout
    tkinter.Label(data_frame, text='ALT').grid(row=0, column=1, padx=5)
    tkinter.Label(data_frame, text='DIR').grid(row=0, column=2, padx=5)
    tkinter.Label(data_frame, text='VEL').grid(row=0, column=3, padx=5)
    
    #get operational data & constants
    gm_angle_true_to_grid = 1
    gm_angle_magnetic_to_grid = 11
    K = 3
    CD_K = 25
    ac_track_magnetic = 69
    ac_highperf = 300

    #Jump Altitude Input
    jump_alt = tkinter.Entry(data_frame, width = 5)
    jump_alt.grid(row=0, column=4, padx=10)

    #EXPERIMENTAL USE OF THE FOLLOWING:#######################
    dir_entry_list = []
    vel_entry_list = []

    #function to create user input database 
    def entry_convert(counter, dir_input, vel_input): ##original function##

        for direction in range(counter - 1):
                direction = int(dir_input.get())
                dir_entry_list.append(direction)

        for velocity in range(counter - 1):
                velocity = int(vel_input.get())
                vel_entry_list.append(velocity)


    #generate full altitude list based on release altitude
    def jump_altitude():
        ja = int(jump_alt.get())
        full_alt_list = [*range(0,ja + 1,1)]
    
        #generate low and high altitude lists
        low_alt_list = full_alt_list[0:6]
        high_alt_list = full_alt_list[6:ja+1:1]

        #generate altitude display
        grid_count = 1
        grid_count_list = [] 
        dir_getter_list = []  
        vel_getter_list = [] 
        full_alt_list_reversed = sorted(full_alt_list, reverse=True)
        for altitude in full_alt_list_reversed:
            grid_count += 1
            tkinter.Label(data_frame, text=(altitude)).grid(row= grid_count, column= 1, padx=5)
        #direction input
            dir_input = tkinter.Entry(data_frame, width = 5)
            dir_input.grid(row= grid_count, column=2, padx=5)
            dir_getter_list.append(dir_input)
        #velocity input
            vel_input = tkinter.Entry(data_frame, width = 5)
            vel_input.grid(row= grid_count, column=3, padx=5)
            vel_getter_list.append(vel_input)

        def calculate():
            new_direction_input_list = []
            new_velocity_input_list = []
            for direction in dir_getter_list:
                new_direction_input_list.append(float(direction.get()))
            for velocity in vel_getter_list:
                new_velocity_input_list.append(float(velocity.get()))

            #wind direction input
            full_direction_list = new_direction_input_list[::-1]
            full_low_dir_input = full_direction_list[:6] 
            full_high_dir_input = full_direction_list[6:]
            print(full_low_dir_input) #test the list
            print(full_high_dir_input) #test the list
            
            #wind velocity input
            full_velocity_list = new_velocity_input_list[::-1]
            full_low_vel_input = full_velocity_list[:6]
            full_high_vel_input = full_velocity_list[6:]
            print(full_low_vel_input) #test the list
            print(full_high_vel_input) #test the list
            
            #calculate average wind direction and velocity while in freefall
            ffd_direction_grid = sum(full_high_dir_input) / len(full_high_dir_input) - gm_angle_true_to_grid
            ffd_direction_grid_rounded = round(ffd_direction_grid, 1)
            ffd_velocity = sum(full_high_vel_input) / len(full_high_vel_input)
            ffd_velocity_rounded = round(ffd_velocity, 1)
            free_fall_drift = (K * (len(full_high_dir_input) * 2)) * ffd_velocity_rounded
            print(free_fall_drift, "meters @", ffd_direction_grid_rounded, "degrees grid")
            tkinter.Label(output_frame, text=f"{free_fall_drift} meters @ {ffd_direction_grid_rounded} degrees grid").grid(row=0, column=0, padx=5) 

            #calculate average wind direction and velocity while under canopy
            cd_direction_grid = sum(full_low_dir_input) / len(full_low_dir_input) - gm_angle_true_to_grid
            cd_direction_grid_rounded = round(cd_direction_grid,1)
            cd_velocity = sum(full_low_vel_input) / len(full_low_vel_input)
            cd_velocity_rounded = round(cd_velocity,1)
            canopy_drift = (CD_K * (len(full_low_vel_input))) * cd_velocity_rounded
            print(canopy_drift, "meters @", cd_direction_grid_rounded, "degrees grid")
            tkinter.Label(output_frame, text=f"{canopy_drift} meters @ {cd_direction_grid_rounded} degrees grid").grid(row=1, column=0, padx=5)

            #calculate forward throw from the HARP
            if ac_track_magnetic <= 180:
                forward_throw = (ac_track_magnetic + 180) + gm_angle_magnetic_to_grid
                print('Forward throw is:', forward_throw, 'Grid @', ac_highperf, 'meters, from the HARP')
                tkinter.Label(output_frame, text=f"Forward throw is: {forward_throw} Grid @ {ac_highperf} meters, from the HARP").grid(row=2, column=0, padx=5)
            else:
                forward_throw = (ac_track_magnetic - 180) + gm_angle_magnetic_to_grid
                print('Forward throw is:', forward_throw, 'Grid @', ac_highperf, 'meters, from the HARP')
                tkinter.Label(output_frame, text=f"Forward throw is: {forward_throw} Grid @ {ac_highperf} meters, from the HARP").grid(row=2, column=0, padx=5)

            #calculate from PRP to OP
            print(free_fall_drift, "meters @", ffd_direction_grid_rounded, "degrees grid, from the preliminary release point to the opening point.")
            print(canopy_drift, "meters @", cd_direction_grid_rounded, "degrees grid, from the opening point to the designated impact point")
            tkinter.Label(output_frame, text=f"{free_fall_drift} meters @ {ffd_direction_grid_rounded} degrees grid, from the preliminary release point to the opening point.").grid(row=3, column=0, padx=5)
            tkinter.Label(output_frame, text=f"{canopy_drift} meters @ {cd_direction_grid_rounded} degrees grid, from the opening point to the designated impact point").grid(row=4, column=0, padx=5)




        calc_button = tkinter.Button(data_frame, text='Calculate', command=lambda:calculate())
        calc_button.grid(row=13, column=4, columnspan=2)

    jumpalt_button = tkinter.Button(data_frame, text='Input Jump Alt', command=lambda:jump_altitude())
    jumpalt_button.grid(row=2, column=4, columnspan=2)

    root.mainloop()
     
main()
