from GUI.RealTime import FileHandler

class FormatData:

    __doc__='''Documentation for FormatData.py functions:

    @classmethod
    formatData(encodedMessage):
        it decodes the encodedMessage given as attribute to the function
        if the encodedMessage had been received without errors (the pattern is: every four bytes only three are data bytes):
            returns: a list composed by the headerIndex (to know which block (100Hz, 10Hz, 4Hz) the message belongs to) and the data bytes

        else:
            returns: ['E', 'R', 'R', 'O', 'R'] to emphasize that an error has occured
 
    @classmethod
    setData(dataFrame, encodedMessage, fileHandler):
        using formatData() function, it decodes the message and updates the dictionaries inside the dataFrame object.
        if (decodedMessage[0]==0x3F):   checks if the transmitted block is the 100Hz one
        elif (decodedMessage[0]==0x0A): checks if the transmitted block is the 10Hz one
        elif(decodedMessage[0]==0x04):  checks if the transmitted block is the 4Hz one

        Once the update is completed, the function uses the fileHandler object to save data to .csv file
 '''
    
    @classmethod
    def formatData(cls, encodedMessage):
        encodedMessage = list(encodedMessage)
        mask = 0x3F
        if len(encodedMessage)%4 != 1:
            return ['E', 'R', 'R', 'O', 'R']
        else:
            decodedMessage = []
            headerIndex=encodedMessage[0]&mask
            decodedMessage.append(headerIndex)
            for i in range(0, len(encodedMessage)//4):
                firstByte = ((encodedMessage[4*i+1] & mask)<<2 | (encodedMessage[4*i+2] & mask)>>4) & 0xFF
                secondByte = ((encodedMessage[4*i+2] & mask) << 4 | (encodedMessage[4*i+3] & mask)>>2) & 0xFF
                thirdByte = ((encodedMessage[4*i+3] & mask) << 6 | (encodedMessage[4*i+4] & mask)) & 0xFF
                decodedMessage.append(firstByte)
                decodedMessage.append(secondByte)
                decodedMessage.append(thirdByte)
            return decodedMessage

    @classmethod
    def setData(cls, dataFrame, encodedMessage, fileHandler):
        decodedMessage=FormatData.formatData(encodedMessage)
        if (decodedMessage[0]==0x3F):
                dataFrame.setEngineFrame("rpm", int(decodedMessage[1]) << 8 | int(decodedMessage[2]))
                dataFrame.setEngineFrame("tps", (float(int(decodedMessage[3]) << 8 | int (decodedMessage[4]))) / 10)
                
                dataFrame.setGyroscopeFrame("accel_x", (float(int(decodedMessage[5]) << 8 | int (decodedMessage[6]))) / 8192)
                dataFrame.setGyroscopeFrame("accel_y", (float(int(decodedMessage[7]) << 8 | int (decodedMessage[8]))) / 8192)
                dataFrame.setGyroscopeFrame("accel_z", (float(int(decodedMessage[9]) << 8 | int (decodedMessage[10]))) / 8192)
                
                dataFrame.setGyroscopeFrame("gyro_x", (float(int(decodedMessage[11]) << 8 | int (decodedMessage[12]))) / 8192)
                dataFrame.setGyroscopeFrame("gyro_y", (float(int(decodedMessage[13]) << 8 | int (decodedMessage[14]))) / 8192)
                dataFrame.setGyroscopeFrame("gyro_z", (float(int(decodedMessage[15]) << 8 | int (decodedMessage[16]))) / 8192)

                #L'offset dei potenziometri (il numero sottratto in fondo) va ricontrollato ad ogni prova della macchina
                dataFrame.setWheelSensorsFrame("pot_fsx", (int(decodedMessage[17]) | ((int(decodedMessage[19]&0x0F))<<8))-610)
                dataFrame.setWheelSensorsFrame("pot_fdx", (int(decodedMessage[18]) | ((int(decodedMessage[19]&0xF0))<<4))-410)
                dataFrame.setWheelSensorsFrame("potFAccuracy", int(decodedMessage[20]))
                dataFrame.setWheelSensorsFrame("pot_rsx", (int(decodedMessage[21]) | ((int(decodedMessage[23]&0x0F))<<8))-300)
                dataFrame.setWheelSensorsFrame("pot_rdx", (int(decodedMessage[22]) | ((int(decodedMessage[23]&0xF0))<<4))-310)
                dataFrame.setWheelSensorsFrame("potRAccuracy", int(decodedMessage[24]))

                dataFrame.setWheelSensorsFrame("countFSx", (int(decodedMessage[27] & 0x0F) << 8) | int(decodedMessage[25]))
                dataFrame.setWheelSensorsFrame("countFDx", (int(decodedMessage[27] & 0xF0) << 4) | int(decodedMessage[26]))
                dataFrame.setWheelSensorsFrame("dtF", int(decodedMessage[28]))
                
                # dataFrame.setWheelSensorsFrame("vel_fsx", SPEED_VALUE)    # NON IN USO (NON ABBIAMO LE SPECIFICHE DELLE RUOTE FONICHE)
                # dataFrame.setWheelSensorsFrame("vel_fdx", SPEED_VALUE)
                
                dataFrame.setWheelSensorsFrame("countRSx", (int(decodedMessage[32] & 0x0F) << 8) | int(decodedMessage[30]))
                dataFrame.setWheelSensorsFrame("countRDx", (int(decodedMessage[32] & 0xF0) << 4) | int(decodedMessage[31]))
                dataFrame.setWheelSensorsFrame("dtR", int(decodedMessage[33]))
                
                # dataFrame.setWheelSensorsFrame("vel_rsx", SPEED_VALUE)
                # dataFrame.setWheelSensorsFrame("vel_rdx", SPEED_VALUE)

                dataFrame.setEngineFrame("gear", int(decodedMessage[34]))
                
                fileHandler.write100Hz()

        elif (decodedMessage[0]==0x0A):
            dataFrame.setEngineFrame("t_h20", int(decodedMessage[1]) -40)
            dataFrame.setEngineFrame("t_air", int(decodedMessage[2]) -40)
            dataFrame.setEngineFrame("t_oil", int(decodedMessage[3]) -40)
            dataFrame.setEngineFrame("vbb", (float(int(decodedMessage[4])))*0.0705)
            dataFrame.setEngineFrame("lambda1_avg", (float(int(decodedMessage[5])))/100)
            dataFrame.setEngineFrame("lambda1_raw", (float(int(decodedMessage[6])))/100)
            dataFrame.setEngineFrame("k_lambda1", (float(int(decodedMessage[7]) << 8 | int (decodedMessage[8])))/656)
            dataFrame.setEngineFrame("inj_low", (float(int(decodedMessage[9]) << 8 | int (decodedMessage[10])))/2)
            dataFrame.setEngineFrame("inj_high", (float(int(decodedMessage[11]) << 8 | int (decodedMessage[12])))/2)
  
            fileHandler.write10Hz()

        elif(decodedMessage[0]==0x04):
            dataFrame.setGPSFrame("hour", int(decodedMessage[1]))
            dataFrame.setGPSFrame("minutes", int(decodedMessage[2]))
            dataFrame.setGPSFrame("seconds", int(decodedMessage[3]))
            dataFrame.setGPSFrame("micro_seconds", (int(decodedMessage[4]) << 8) | (int(decodedMessage[5])))
            dataFrame.setGPSFrame("n_sats", int(decodedMessage[6] & 0x0F))
            dataFrame.setGPSFrame("fixQuality", int((decodedMessage[6] & 0x30) >> 4))
            e_w = int((decodedMessage[6] >> 6) & 0x01)
            if (e_w == 1):
                dataFrame.setGPSFrame("e_w", "E")
            else:
                dataFrame.setGPSFrame("e_w", "W")

            n_s = int(decodedMessage[6] >> 7)
            if (n_s == 1):
                dataFrame.setGPSFrame("n_s", "N")
            else:
                dataFrame.setGPSFrame("n_s", "S")

            dataFrame.setGPSFrame("hdop", int(decodedMessage[7] << 8) | int(decodedMessage[8]))                                    
            dataFrame.setGPSFrame("latitude", ((int(decodedMessage[9]) << 8) | int(decodedMessage[10])) + ((float((int(decodedMessage[11]) << 24) | (int(decodedMessage[12]) << 16) | (int(decodedMessage[13]) << 8) | int(decodedMessage[14]))) / 100000))
            dataFrame.setGPSFrame("longitude", ((int(decodedMessage[15]) << 24) | (int(decodedMessage[16]) << 16) | (int(decodedMessage[17]) << 8) | int(decodedMessage[18])) + ((float((int(decodedMessage[19]) << 24) | (int(decodedMessage[20]) << 16) | (int(decodedMessage[21]) << 8) | int(decodedMessage[22]))) / 100000))
            dataFrame.setGPSFrame("velGPS", float(decodedMessage[23]) + ((float(decodedMessage[23])) / 10))

            fileHandler.write4Hz()
            
