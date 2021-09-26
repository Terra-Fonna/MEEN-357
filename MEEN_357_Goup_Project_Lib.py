# project Funcitons & libreary


def get_mass(rov):
    #Computes the total mass of the rover. Uses information in the rover dict

    #print(rov)
    wheels = rov['wheel_assembly']['wheel']['mass']*6
    sRed = rov['wheel_assembly']['speed_reducer']['mass']*6
    chassis = rov['chassis']['mass']
    science_pay = rov['science_payload']['mass']
    power_sub = rov['power_subsys']['mass']
    
    rov_mass = wheels+ sRed+chassis+science_pay+power_sub

    return rov_mass

def get_gear_ratio(Speed_red_dic):
    #returns the speed reduction ratio for the speed reducer based on speed_reducer dict.
    sr_ratio = 0 

    return sr_ratio

def tau_dcmotor(v,MoterSpec_dic):
    #Returns the motor shaft torque when given motor shaft speed and a dictionary containing important specifications for the motor. 
    tourqe =0

    return tourqe
