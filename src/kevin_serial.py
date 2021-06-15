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
        if(port == 'nan'):
            self.ser = serial.Serial()
            self.ser.baudrate = 115200
            self.ser.timeout = 1
        else:
            self.ser = serial.Serial(port, 115200, timeout=1)  # open serial port
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
        # ser.write(b'hello')     # write a string

        # x = self.ser.read()          # read one byte
        # print(x)

        # s = self.ser.read(10)        # read up to ten bytes (timeout)
        # print(s)
        
        line = self.ser.readline()   # read a '\n' terminated line
        print(line)

        print()

    def portStatus(self):
        return self.ser.isOpen

    def open(self):
        msg = ''
        # print(self.ser)
        try:
            if(self.ser.name != None):
                self.ser.open()             # open port
                msg = 'Connect'
            else:
                msg = 'no port set'
        except:
            if(self.ser.isOpen == True):
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

    port_num = int(input('Please chose a port(0,1,2...): '))

    ser = SerialFuc(ports[port_num])
    while 1:
        ser.read()