import serial

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def main():

    ack = '0x6e'          #0
    numBytes = '0x4b'     #1
    secl = '0xff'         #2
    engineStat = '0xcc'   #3
    dwell = '0x0f'        #4
    mapLowByte = '0x28'   #5
    mapHighByte = '0x00'  #6
    IAT = '0x12'          #7
    CLT = '0x55'          #8
    batCorrect = '0x05'   #9
    batVolt = '0x80'      #10
    o2 = '0x89'           #11
    ego = '0x00'          #12
    iatCorrect = '0x00'   #13
    wueCorrect = '0x00'   #14
    rpmLowByte = '0x80'   #15
    rpmHighByte = '0x04'  #16
    tae = '0x00'          #17
    totalCorrect = '0x14' #18
    ve1 = '0x54'          #19
    afrTarget = '0x89'    #20
    pw1LowByte = '0x00'   #21
    pw1HighByte = '0x00'  #22
    tpdDOT = '0x00'       #23
    sparkAdv = '0x16'     #24
    tpsPercent = '0x21'   #25
    loopsPerSecLB = '0x00'#26
    loopsPerSecHB = '0x00'#27
    freeRAMLB = '0x00'    #28
    freeRAMHB = '0x04'    #29
    boostTarget = '0xaa'  #30
    boostPWM = '0x32'     #31
    sparkBit = '0xff'     #32
    rpmDOTLB = '0x00'     #33
    rpmDOTHB = '0x00'     #34
    flexPercent = '0x00'  #35
    flexCorrect = '0x00'  #36
    idleLoad = '0x1b'     #37
    testBits = '0xdd'     #38
    secondO2 = '0x00'     #39
    baro = '0x64'         #40
    canin0LB = '0x55'     #41
    canin0HB = '0x00'     #42
    canin1LB = '0x5a'     #43
    canin1HB = '0x00'     #44
    canin2LB = '0x00'     #45
    canin2HB = '0x00'     #46
    canin3LB = '0x00'     #47
    canin3HB = '0x00'     #48
    canin4LB = '0x00'     #49
    canin4HB = '0x00'     #50
    canin5LB = '0x00'     #51
    canin5HB = '0x00'     #52
    canin6LB = '0x00'     #53
    canin6HB = '0x00'     #54
    canin7LB = '0x00'     #55
    canin7HB = '0x00'     #56
    canin8LB = '0x00'     #57
    canin8HB = '0x00'     #58
    canin9LB = '0x00'     #59
    canin9HB = '0x00'     #60
    canin10LB = '0x00'    #61
    canin10HB = '0x00'    #62
    canin11LB = '0x00'    #63
    canin11HB = '0x00'    #64
    canin12LB = '0x00'    #65
    canin12HB = '0x00'    #66
    canin13LB = '0x00'    #67
    canin13HB = '0x00'    #68
    canin14LB = '0x00'    #69
    canin14HB = '0x00'    #70
    canin15LB = '0x00'    #71
    canin15HB = '0x00'    #72
    tpsADC = '0x80'       #73
    nextError = '0x00'    #74

    input = [ack, numBytes, secl, engineStat, dwell, mapLowByte, mapHighByte, IAT, CLT, batCorrect, batVolt, o2, ego,
             iatCorrect, wueCorrect, rpmLowByte, rpmHighByte, tae, totalCorrect, ve1, afrTarget, pw1LowByte,
             pw1HighByte, tpdDOT, sparkAdv, tpsPercent, loopsPerSecLB, loopsPerSecHB, freeRAMLB, freeRAMHB, boostTarget,
             boostPWM, sparkBit, rpmDOTLB, rpmDOTHB, flexPercent, flexCorrect, idleLoad, testBits, secondO2, baro,
             canin0LB, canin0HB, canin1LB, canin1HB, canin2LB, canin2HB, canin3LB, canin3HB, canin4LB, canin4HB,
             canin5LB, canin5HB, canin6LB, canin6HB, canin7LB, canin7HB, canin8LB, canin8HB, canin9LB, canin9HB,
             canin10LB, canin10HB, canin11LB, canin11HB, canin12LB, canin12HB, canin13LB, canin13HB, canin14LB,
             canin14HB, canin15LB, canin15HB, tpsADC, nextError]

    payload = bytearray([int(x, 0) for x in input])

    while True:
        in_byte = arduino.readline()
        in_hex = in_byte.hex()

        if (in_hex):
            print("From Arduino Byte: ", in_byte)
            print("From Arduino Hex: " , in_hex)

        if (in_hex == "6e"):
            print("Received realtime data request 0x6e")
            print(payload)
            arduino.write(payload)
            print("Payload Sent")


if __name__ == "__main__":
    main()