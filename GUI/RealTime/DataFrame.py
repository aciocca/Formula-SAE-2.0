class DataFrame:

    __doc__='''Documentation for DataFrame.py instance functions:
    
-getEngineFrame():
    return the dictionary with engine sensors values

-getGPSFrame():
    return the dictionary with GPS values

-getWheelSensorsFrame():
    return the dictionary with proprietary sensors values

-getGyroScopeFrame():
    return the dictionary with the gyroscope (and the accelerometer) sensor values

-setEngineFrame(key, value)
-setGPSFrame(key, value)
-setWheelSensorsFrame(key, value)
-setGyroscopeFrame(key, value):
    return:
        True    if set the value in the dictionary with the same key
        False   if can't set the value in the dictionary (there isn't the key in the dictionary)

Since all the data structures are dictionaries, to see the list of keys, call the keys() function on the dictionary'''

    def __init__(self):
        #DEFINITION OF DICTIONARIES' FIELDS
        self.__engineFrame = {"rpm": 0, "tps": 0.0, "t_h20": 0, "t_air": 0, "t_oil": 0, "vbb": 0.0, "lambda1_avg": 0.0, "lambda1_raw": 0.0, "k_lambda1": 0.0, "inj_low": 0.0, "inj_high": 0.0, "gear": 0}
        self.__GPSFrame = {"hour": 0, "minutes": 0, "seconds": 0, "micro_seconds": 0.0, "n_s": "?", "e_w": "?", "fixQuality": 0, "n_sats": 0, "hdop": 0.0, "latitude": "?", "longitude": "?", "velGPS": 0.0}
        self.__wheelSensorsFrame = {"vel_fsx": 0.0, "vel_fdx": 0.0, "vel_rdx": 0.0, "vel_rsx": 0.0, "pot_fsx": 0.0, "pot_fdx": 0.0, "pot_rdx": 0.0, "pot_rsx": 0.0, "potRAccuracy": 0.0, "potFAccuracy": 0.0, "steeringEncoder": 0.0}
        self.__gyroscopeFrame = {"gyro_x": 0.0, "gyro_y": 0.0, "gyro_z": 0.0, "accel_x": 0.0, "accel_y": 0.0, "accel_z": 0.0, }


    #GETTING DICTIONARIES FUNCTIONS
    def getEngineFrame(self):
        return (self.__engineFrame)

    def getGPSFrame(self):
        return (self.__GPSFrame)

    def getWheelSensorsFrame(self):
        return (self.__wheelSensorsFrame)

    def getGyroscopeFrame(self):
        return (self.__gyroscopeFrame)


    #SETTING DICTIONARIES FUNCTIONS
    def setEngineFrame(self, key, value):
        if key in self.__engineFrame.keys():
            self.__engineFrame[key] = value
            return True
        else:
            return False

    def setGPSFrame(self, key, value):
        if key in self.__GPSFrame.keys():
            self.__GPSFrame[key] = value
            return True
        else:
            return False

    def  setWheelSensorsFrame(self, key, value):
        if key in self.__wheelSensorsFrame.keys():
            self.__wheelSensorsFrame[key] = value
            return True
        else:
            return False

    def setGyroscopeFrame(self, key, value):
        if key in self.__gyroscopeFrame.keys():
            self.__gyroscopeFrame[key] = value
            return True
        else:
            return False

    def fillDict(self,decodedMessage):
        pass
        #TO-DO