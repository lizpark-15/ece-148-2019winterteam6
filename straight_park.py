#straight parking
class straight_park(object):
    def run(self, distance1, trigger):
        #we need to find the relationship between the throttle and distance
        #calculated speed is a ratio of maximum speed (-1, 1)
        #negative ratio means backwards
        
        ''' some magic equation here
            CALCULATED_SPEED = EQA
            '''
        a = 0.005
        pd = 170
        if distance1 > pd:
            throttle = min(1, (distance1 - pd)*a)
            trigger = 0
        elif distance1 <= pd:
            if trigger <= 2 or trigger == None:
                if trigger == 1:
                    throttle = 0
                    print('Throttle speed: ' + str(throttle))
                    trigger += 1
                    return throttle, trigger
                else:
                    throttle = -1
                    print('Throttle speed: ' + str(throttle))
                    trigger += 1
                    return throttle, trigger
            elif trigger > 2:
                print('Throttle speed: ', 0)
                return 0, trigger
        
        print('Throttle speed: ', throttle)
        return throttle, trigger #return back to main flow





