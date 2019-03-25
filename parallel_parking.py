import time

class find_spot(object):
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

                if (length < 1000):
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
            
            print('Throttle: 0.95')
            return 0.95, self.flag
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

class parallel_park(object):
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
                angle = 0
                throttle = 0
            if self.stage == 1:
                if (time.time() < self.start_time + 0.6): #0.6
                    print('Backwards a little bit')
                    throttle = -0.95
                    angle = 0
                else:
                    self.start_time = time.time()
                    self.stage = 2
            if self.stage == 2:
                if (time.time() < self.start_time + 2): #2
                    if distance4 > 150 and self.flag == 0:
                        print('First turn')
                        throttle = -0.95
                        angle = 0.88
                    else:
                        self_flag = 1
                    
                    if self.flag == 1:
                        if distance4 < 215:
                            print('move forward a little bit')
                            throttle = 0.95
                            angle = -0.5
                        else:
                            self.start_time = time.time()
                            self.stage = 3
                else:
                    self.start_time = time.time()
                    self.stage = 3
            if self.stage == 3:
                if (time.time() < self.start_time + 2.3):
                    if distance4 > 150:
                        print('Second turn')
                        throttle = -0.95
                        angle = -1
                    else:
                        angle = 0.53
                        throttle = 0.95
                else:
                    self.start_time = time.time()
                    self.stage = 4
            if self.stage == 4:
                if (time.time() < self.start_time + 0.4):
                    if distance1 > 200:
                        print('move forward')
                        throttle = 0.95
                        angle = 0
                    else:
                        self.stage = 5
                else:
                    self.stage = 5
            if self.stage >= 5:
                if self.stage == 5:
                    angle = 0
                    throttle = -0.95
                    self.stage = 6
                elif self.stage == 6:
                    angle = 0
                    throttle = 0
                    self.stage = 7
                elif self.stage == 7:
                    angle = 0
                    throttle = -0.95
                    self.stage = 8
                elif self.stage == 8:
                    angle = 0
                    throttle = 0

            return throttle, angle

        return throttle, 0



