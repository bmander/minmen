import termios
import time

def calc_checksum( command ):
    cs = 0
    for char in command:
        cs = cs ^ ord(char)
    cs &= 0xff

    return cs
    
def main(command, port="/dev/ttyUSB0"):
    # open port
    mendel = open(port, "rw+")

    # send command and flush the serial port
    send_command( command, mendel )
    mendel.flush()

    # give it a little time to respond
    time.sleep(1)

    # take a look at the response
    print mendel.read()
    
def send_command( command, port_file ):
    # figure out the command we're sending
    checksum = calc_checksum( command+" " )

    # send the command
    port_file.write( "%s *%d\n"%(command, checksum) )

if __name__=='__main__':

    # simple moving-around functions
    #main("N67 G1 X0 Y0 Z-1 F1539.5")
    #main("N91 G1 Z3.0 F40.0")
    
    # get current temp
    #main("N28 M105")
    
    # set temp
    main("N92 M104 S20")
    
    #extrude a set amount
    #main("N57 G1 E200")
    
    
