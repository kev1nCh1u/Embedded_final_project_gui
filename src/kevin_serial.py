import serial
import glob
import sys

def serial_ports():
    """ Lists serial port names
 
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
 
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

class SerialFuc():
    def __init__(self, port='nan'):
        super().__init__()
        if port == 'nan':
            self.ser = serial.Serial()
            self.ser.baudrate = 115200
            self.ser.timeout = 0.1
        else:
            self.ser = serial.Serial(port, 115200, timeout=0.1)  # open serial port
            # print(self.ser.name)         # check which port was really used

    def changePort(self, port):
        msg = ''
        msg = self.ser.close()
        self.ser.port = port
        msg = self.open()
        # print(self.ser.name)         # check which port was really used
        # print(self.ser)
        return msg
        

    def read(self):
        data = (0,0)
        try:
            self.ser.reset_input_buffer()

            while 1:
                self.ser.write(1)
                
                buff = self.ser.read().decode()        # read one byte
                if buff != '':
                    buff = ord(buff)
                # print(buff)
                if buff == 53:
                    break

            # data[0] = ord(self.ser.read().decode('utf-8'))        # read one byte
            # data[1] = ord(self.ser.read().decode('utf-8'))        # read one byte

            x = ord(self.ser.read().decode('utf-8'))        # read one byte
            y = ord(self.ser.read().decode('utf-8'))        # read one byte
            data = (x, y)

        except:
            data = (1,1)

        # print(data)

        return data
    
    def write(self):
        ser.write(b'hello')     # write a string

    def portStatus(self):
        return self.ser.isOpen

    def open(self):
        msg = ''
        # print(self.ser)
        try:
            if self.ser.name != None:
                self.ser.open()             # open port
                msg = 'Connect'
            else:
                msg = 'no port set'
        except:
            if self.ser.isOpen == True:
                msg = 'Already connect'
            else:
                msg = 'Error can not connect !!!'
        # print(msg)
        return msg

    def close(self):
        msg = ''
        self.ser.close()             # close port
        msg = 'Disconnect'
        # print(msg)
        return msg


if __name__ == '__main__':
    ports = serial_ports()
    for i in range(len(ports)):
        print(i, ':', ports[i], ' ', sep='')

    # port_num = int(input('Please chose a port(0,1,2...): '))

    ser = SerialFuc(ports[0])
    while 1:
        input()
        print(ser.read())