from GUI.RealTime import FileHandler

class FormatData:
    
    @classmethod
    def formatData(cls, encodedMessage):
        encodedMessage = list(encodedMessage)
        mask = 0x3F
        if len(encodedMessage)%4!=1:
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
                dataFrame.setEngineFrame("tps", (float(int(decodedMessage[3]) << 8 | int (decodedMessage[4])))/10)
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
            pass
            
