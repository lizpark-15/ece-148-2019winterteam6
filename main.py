#!/usr/bin/python
import sys
sys.path.insert(0,"VL53L0X_rasp_python/")
from straight_park import *
from parallel_parking import *
from perpendicular_parking import *
from tof import *
import donkeycar as dk

# main flow
def park(cfg, option):       #this part will be in manage.py
    #option 1 is straight parking
    from donkeycar.parts.actuator import PCA9685, PWMSteering, PWMThrottle
    if option == '1':
        print('Starting straight parking')
        #Initialize car
        V = dk.vehicle.Vehicle()
        
        #initialize sensor class
        tof = TOF()
        #tof has four outputs
        #distance 1 is from the FRONT sensor
        #distance 2 is from the FIRST SIDE sensor
        #distance 3 is from the SECOND SIDE sensor
        #distance 4 is from the BACK sensor
        V.add(tof, outputs=['distance1', 'distance2', 'distance3', 'distance4'])
        
        #initialize park class (specifically for straight parking)
        park1 = straight_park()
        #straight park takes one distance input returned from TOF() class
        #we only need the front sensor in this case
        #it generates one output which controls the throttle
        V.add(park1,
              inputs = ['distance1', 'trigger'],
              outputs = ['throttle', 'trigger'])
            
        #creating throttle part
        throttle_controller = PCA9685(cfg.THROTTLE_CHANNEL)
        throttle = PWMThrottle(controller=throttle_controller,
                             max_pulse=cfg.THROTTLE_FORWARD_PWM,
                             zero_pulse=cfg.THROTTLE_STOPPED_PWM,
                             min_pulse=cfg.THROTTLE_REVERSE_PWM)
        V.add(throttle, inputs=['throttle'])
      
        #start parking
        V.start()

    if option == '2':
        print('Starting parallel parking')
        #Initialize car
        V = dk.vehicle.Vehicle()
        
        #initialize sensor class
        tof = TOF()
        #tof has four outputs
        #distance 1 is from the FRONT sensor
        #distance 2 is from the FIRST SIDE sensor
        #distance 3 is from the SECOND SIDE sensor
        #distance 4 is from the BACK sensor
        V.add(tof, outputs=['distance1', 'distance2', 'distance3', 'distance4'])
        
        #initialize park class (specifically for straight parking)
        find = find_spot()
        #straight park takes one distance input returned from TOF() class
        #we only need the front sensor in this case
        #it generates one output which controls the throttle
        V.add(find,
              inputs = ['distance2', 'distance3'],
              outputs = ['throttle', 'flag'])
              
        park2 = parallel_park()
        V.add(park2,
              inputs = ['flag', 'throttle', 'distance4', 'distance1'],
              outputs = ['throttle', 'angle'])
        
        #creating throttle part
        steering_controller = PCA9685(cfg.STEERING_CHANNEL)
        steering = PWMSteering(controller=steering_controller,
                               left_pulse=cfg.STEERING_LEFT_PWM,
                               right_pulse=cfg.STEERING_RIGHT_PWM)
        
        throttle_controller = PCA9685(cfg.THROTTLE_CHANNEL)
        throttle = PWMThrottle(controller=throttle_controller,
                             max_pulse=cfg.THROTTLE_FORWARD_PWM,
                             zero_pulse=cfg.THROTTLE_STOPPED_PWM,
                             min_pulse=cfg.THROTTLE_REVERSE_PWM)
                             
        V.add(steering, inputs=['angle'])
        V.add(throttle, inputs=['throttle'])
      
        #start parking
        V.start()


    if option == '3':
        print('Starting perpendicular parking')
        #Initialize car
        V = dk.vehicle.Vehicle()
            
        #initialize sensor class
        tof = TOF()
        #tof has four outputs
        #distance 1 is from the FRONT sensor
        #distance 2 is from the FIRST SIDE sensor
        #distance 3 is from the SECOND SIDE sensor
        #distance 4 is from the BACK sensor
        V.add(tof, outputs=['distance1', 'distance2', 'distance3', 'distance4'])
        
        #initialize park class (specifically for straight parking)
        find = find_spot_pp()
        #straight park takes one distance input returned from TOF() class
        #we only need the front sensor in this case
        #it generates one output which controls the throttle
        V.add(find,
              inputs = ['distance2', 'distance3'],
              outputs = ['throttle', 'flag'])

        park3 = perpendicular_park()
        V.add(park3,
            inputs = ['flag', 'throttle', 'distance4', 'distance1'],
            outputs = ['throttle', 'angle'])
      
        #creating throttle part
        steering_controller = PCA9685(cfg.STEERING_CHANNEL)
        steering = PWMSteering(controller=steering_controller,
                             left_pulse=cfg.STEERING_LEFT_PWM,
                             right_pulse=cfg.STEERING_RIGHT_PWM)
      
        throttle_controller = PCA9685(cfg.THROTTLE_CHANNEL)
        throttle = PWMThrottle(controller=throttle_controller,
                             max_pulse=cfg.THROTTLE_FORWARD_PWM,
                             zero_pulse=cfg.THROTTLE_STOPPED_PWM,
                             min_pulse=cfg.THROTTLE_REVERSE_PWM)
      
        V.add(steering, inputs=['angle'])
        V.add(throttle, inputs=['throttle'])
              
        #start parking
        V.start()
        

