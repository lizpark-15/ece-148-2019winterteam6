import time

class find_spot_pp(object):
    def __init__(self):
        self._init_dist_1 = 200
        self._init_dist_2 = 200
        self.side_1_flag = 0
        self.side_2_flag = 0
        self.side_1_time = 0
        self.side_2_time = 0
        self.flag = 0
    
    def run(self, distance2, distance3):
        if (self.flag == 0):
            if (self.side_1_flag == 0):
                if (distance2 - self._init_dist_1 > 50):
                    self.side_1_flag = 1
                    self.side_1_time = time.time()
                    print('SIDE 1 detected')
            elif (self.side_2_flag == 0):
                if (self._init_dist_2 - distance3 > 50):
                    self.side_2_flag = 1
                    self.side_2_time = time.time()
                    print('SIDE 2 detected')
            else:
                time_diff = self.side_2_time - self.side_1_time
                print('Time difference:', time_diff)
                length = 600 * (time_diff)
                print('Spot length:', length)
                
                if (length < 500):
                    print('Spot too narrow!')
                    self.side_1_flag = 0
                    self.side_2_flag = 0
                    self.side_1_time = 0
                    self.side_2_time = 0
                else:
                    print('Start to park')
                    self.flag = 1
                    print('Throttle: -1')
                    return -0.95, self.flag
            
            self._init_dist_2 = distance3
            
            print('Throttle: 1')
            return 1, self.flag
        else:
            if(self.flag == 1):
                self.flag = 2
                print('Throttle: 0')
                return 0, self.flag
            elif (self.flag == 2):
                self.flag = 3
                print('Throttle: -1')
                return -0.95, self.flag
            elif (self.flag == 3):
                print('Throttle: 0')
                return 0, self.flag

class perpendicular_park(object):
    def __init__(self):
        self.start_time = 0
        self.stage = 0
        self.flag = 0
    
    def run(self, flag, throttle, distance4, distance1):
        if flag == 3:
            if self.stage == 0:
                self.start_time = time.time()
                print('wait for 1s')
                time.sleep(1)
                self.stage = 1
                self.start_time = time.time()
                angle = 0.07
                throttle = 0
            if self.stage == 1:
                if (time.time() < self.start_time + 0.8): #0.6
                    print('Backwards a little bit')
                    throttle = -0.95
                    angle = 0.07
                else:
                    self.start_time = time.time()
                    self.stage = 2
            if self.stage == 2:
                if (time.time() < self.start_time + 10): #2
                    if distance4 > 160:
                        print('Turn')
                        throttle = -1
                        angle = 1
                    else:
                        self.start_time = time.time()
                        self.stage = 3
                else:
                    self.start_time = time.time()
                    self.stage = 4
            if self.stage == 3:
                if (time.time() < self.start_time + 0.6): #2
                        print('Move forward1')
                        throttle = 1
                        angle = 0.07
                else:
                    self.start_time = time.time()
                    self.stage = 4
            if self.stage == 4:
                if (time.time() < self.start_time + 6): #2
                    if self.flag == 0:
                        throttle = 0
                        angle = 0.07
                        self.flag = 1
                    elif self.flag == 1:
                        throttle = -1
                        angle = 0.07
                        self.flag = 2
                    elif self.flag == 2:
                        throttle = 0
                        angle = 0.07
                        self.flag = 3
                    elif self.flag == 3:
                        if distance4 > 200:
                            print('Turn')
                            throttle = -1
                            angle = 0.55
                        else:
                            self.start_time = time.time()
                            self.stage = 6
                else:
                    self.start_time = time.time()
                    self.stage = 5
            if self.stage == 5:
                if (time.time() < self.start_time + 1):
                    if distance4 > 150:
                        print('Backwards')
                        throttle = -0.95
                        angle = 0.07
                    else:
                        self.start_time = time.time()
                        self.stage = 6
                else:
                    self.start_time = time.time()
                    self.stage = 6
            if self.stage == 6:
                if (time.time() < self.start_time + 0.3):
                    if distance4 < 100:
                        print('move forward')
                        throttle = 0.95
                        angle = 0.07
                    else:
                        self.stage = 7
                else:
                    self.stage = 7
            if self.stage >= 7:
                if self.stage == 7:
                    angle = 0
                    throttle = -0.95
                    self.stage = 8
                elif self.stage == 8:
                    angle = 0
                    throttle = 0
                    self.stage = 8
                elif self.stage == 8:
                    angle = 0
                    throttle = -0.95
                    self.stage = 9
                elif self.stage == 9:
                    angle = 0
                    throttle = 0
            
            return throttle, angle
        
        return throttle, 0.07




