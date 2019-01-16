import binascii
import os
import sys

__author__ = "Oz"
__copyright__ = "Apple BOOT2 Parser"

# TODO :
# https://www.theiphonewiki.com/wiki/Models


model_list = \
    {
        "MC769": "[ iPad2 ] iPad2,1",
        "MC770": "[ iPad2 ] iPad2,1",
        "MC916": "[ iPad2 ] iPad2,1",
        "MC979": "[ iPad2 ] iPad2,1",
        "MD002": "[ iPad2 ] iPad2,1",
        "MC980": "[ iPad2 ] iPad2,1",
        "MC981": "[ iPad2 ] iPad2,1",
        "MC773": "[ iPad2 ] iPad2,2",
        "MC957": "[ iPad2 ] iPad2,2",
        "MC774": "[ iPad2 ] iPad2,2",
        "MC775": "[ iPad2 ] iPad2,2",
        "MC982": "[ iPad2 ] iPad2,2",
        "MC992": "[ iPad2 ] iPad2,2",
        "MC983": "[ iPad2 ] iPad2,2",
        "MC984": "[ iPad2 ] iPad2,2",
        "MC755": "[ iPad2 ] iPad2,3",
        "MC763": "[ iPad2 ] iPad2,3",
        "MC764": "[ iPad2 ] iPad2,3",
        "MC985": "[ iPad2 ] iPad2,3",
        "MC986": "[ iPad2 ] iPad2,3",
        "MC987": "[ iPad2 ] iPad2,3",
        "MC954": "[ iPad2 ] iPad2,4",
        "MC960": "[ iPad2 ] iPad2,4",
        "MC988": "[ iPad2 ] iPad2,4",
        "MC989": "[ iPad2 ] iPad2,4",
        "MC705": "[ iPad3 ] iPad3,1",
        "MD333": "[ iPad3 ] iPad3,1",
        "MC706": "[ iPad3 ] iPad3,1",
        "MD334": "[ iPad3 ] iPad3,1",
        "MC707": "[ iPad3 ] iPad3,1",
        "MD335": "[ iPad3 ] iPad3,1",
        "MD328": "[ iPad3 ] iPad3,1",
        "MD336": "[ iPad3 ] iPad3,1",
        "MD329": "[ iPad3 ] iPad3,1",
        "MD337": "[ iPad3 ] iPad3,1",
        "MD330": "[ iPad3 ] iPad3,1",
        "MD338": "[ iPad3 ] iPad3,1",
        "MC733": "[ iPad3 ] iPad3,2",
        "MC744": "[ iPad3 ] iPad3,2",
        "MC756": "[ iPad3 ] iPad3,2",
        "MD363": "[ iPad3 ] iPad3,2",
        "MD364": "[ iPad3 ] iPad3,2",
        "MD365": "[ iPad3 ] iPad3,2",
        "MD366": "[ iPad3 ] iPad3,3",
        "MD404": "[ iPad3 ] iPad3,3",
        "MD367": "[ iPad3 ] iPad3,3",
        "MD405": "[ iPad3 ] iPad3,3",
        "MD368": "[ iPad3 ] iPad3,3",
        "MD406": "[ iPad3 ] iPad3,3",
        "MD369": "[ iPad3 ] iPad3,3",
        "MD407": "[ iPad3 ] iPad3,3",
        "MD370": "[ iPad3 ] iPad3,3",
        "MD408": "[ iPad3 ] iPad3,3",
        "MD371": "[ iPad3 ] iPad3,3",
        "MD409": "[ iPad3 ] iPad3,3",
        "MD510": "[ iPad4 ] iPad3,4",
        "MD511": "[ iPad4 ] iPad3,4",
        "MD512": "[ iPad4 ] iPad3,4",
        "ME392": "[ iPad4 ] iPad3,4",
        "MD513": "[ iPad4 ] iPad3,4",
        "MD514": "[ iPad4 ] iPad3,4",
        "MD515": "[ iPad4 ] iPad3,4",
        "ME393": "[ iPad4 ] iPad3,4",
        "MD516": "[ iPad4 ] iPad3,5",
        "MG932": "[ iPad4 ] iPad3,5",
        "MD517": "[ iPad4 ] iPad3,5",
        "MD518": "[ iPad4 ] iPad3,5",
        "MD944": "[ iPad4 ] iPad3,5",
        "ME400": "[ iPad4 ] iPad3,5",
        "MD519": "[ iPad4 ] iPad3,5",
        "MG942": "[ iPad4 ] iPad3,5",
        "MD520": "[ iPad4 ] iPad3,5",
        "MD521": "[ iPad4 ] iPad3,5",
        "ME401": "[ iPad4 ] iPad3,5",
        "MD522": "[ iPad4 ] iPad3,6",
        "ME195": "[ iPad4 ] iPad3,6",
        "MD523": "[ iPad4 ] iPad3,6",
        "ME196": "[ iPad4 ] iPad3,6",
        "MD524": "[ iPad4 ] iPad3,6",
        "ME197": "[ iPad4 ] iPad3,6",
        "ME406": "[ iPad4 ] iPad3,6",
        "ME410": "[ iPad4 ] iPad3,6",
        "MD525": "[ iPad4 ] iPad3,6",
        "ME198": "[ iPad4 ] iPad3,6",
        "MD526": "[ iPad4 ] iPad3,6",
        "ME199": "[ iPad4 ] iPad3,6",
        "MD527": "[ iPad4 ] iPad3,6",
        "ME200": "[ iPad4 ] iPad3,6",
        "ME407": "[ iPad4 ] iPad3,6",
        "ME411": "[ iPad4 ] iPad3,6",
        "MD788": "[ iPad Air ] iPad4,1",
        "MD789": "[ iPad Air ] iPad4,1",
        "MD790": "[ iPad Air ] iPad4,1",
        "ME906": "[ iPad Air ] iPad4,1",
        "MD785": "[ iPad Air ] iPad4,1",
        "MD786": "[ iPad Air ] iPad4,1",
        "MD787": "[ iPad Air ] iPad4,1",
        "ME898": "[ iPad Air ] iPad4,1",
        "MD794": "[ iPad Air ] iPad4,2",
        "ME997": "[ iPad Air ] iPad4,2",
        "ME999": "[ iPad Air ] iPad4,2",
        "MF021": "[ iPad Air ] iPad4,2",
        "MF502": "[ iPad Air ] iPad4,2",
        "MD795": "[ iPad Air ] iPad4,2",
        "MF025": "[ iPad Air ] iPad4,2",
        "MF527": "[ iPad Air ] iPad4,2",
        "MF529": "[ iPad Air ] iPad4,2",
        "MF532": "[ iPad Air ] iPad4,2",
        "MD796": "[ iPad Air ] iPad4,2",
        "MF012": "[ iPad Air ] iPad4,2",
        "MF013": "[ iPad Air ] iPad4,2",
        "MF027": "[ iPad Air ] iPad4,2",
        "MF539": "[ iPad Air ] iPad4,2",
        "ME988": "[ iPad Air ] iPad4,2",
        "MF018": "[ iPad Air ] iPad4,2",
        "MF019": "[ iPad Air ] iPad4,2",
        "MF029": "[ iPad Air ] iPad4,2",
        "MF563": "[ iPad Air ] iPad4,2",
        "MD791": "[ iPad Air ] iPad4,2",
        "ME991": "[ iPad Air ] iPad4,2",
        "ME993": "[ iPad Air ] iPad4,2",
        "MF020": "[ iPad Air ] iPad4,2",
        "MF496": "[ iPad Air ] iPad4,2",
        "MD792": "[ iPad Air ] iPad4,2",
        "MF003": "[ iPad Air ] iPad4,2",
        "MF004": "[ iPad Air ] iPad4,2",
        "MF024": "[ iPad Air ] iPad4,2",
        "MF520": "[ iPad Air ] iPad4,2",
        "MD793": "[ iPad Air ] iPad4,2",
        "MF009": "[ iPad Air ] iPad4,2",
        "MF010": "[ iPad Air ] iPad4,2",
        "MF026": "[ iPad Air ] iPad4,2",
        "MF534": "[ iPad Air ] iPad4,2",
        "ME987": "[ iPad Air ] iPad4,2",
        "MF015": "[ iPad Air ] iPad4,2",
        "MF016": "[ iPad Air ] iPad4,2",
        "MF028": "[ iPad Air ] iPad4,2",
        "MF558": "[ iPad Air ] iPad4,2",
        "MF230": "[ iPad Air ] iPad4,3",
        "MF233": "[ iPad Air ] iPad4,3",
        "MF234": "[ iPad Air ] iPad4,3",
        "MF236": "[ iPad Air ] iPad4,3",
        "MD797": "[ iPad Air ] iPad4,3",
        "MD798": "[ iPad Air ] iPad4,3",
        "MD799": "[ iPad Air ] iPad4,3",
        "MF235": "[ iPad Air ] iPad4,3",
        "MH0W2": "[ iPad Air 2 ] iPad5,3",
        "MNV72": "[ iPad Air 2 ] iPad5,3",
        "MH182": "[ iPad Air 2 ] iPad5,3",
        "MH1J2": "[ iPad Air 2 ] iPad5,3",
        "MGLW2": "[ iPad Air 2 ] iPad5,3",
        "MNV62": "[ iPad Air 2 ] iPad5,3",
        "MGKM2": "[ iPad Air 2 ] iPad5,3",
        "MGTY2": "[ iPad Air 2 ] iPad5,3",
        "MGL12": "[ iPad Air 2 ] iPad5,3",
        "MNV22": "[ iPad Air 2 ] iPad5,3",
        "MGKL2": "[ iPad Air 2 ] iPad5,3",
        "MGTX2": "[ iPad Air 2 ] iPad5,3",
        "MH2W2": "[ iPad Air 2 ] iPad5,4",
        "MH1C2": "[ iPad Air 2 ] iPad5,4",
        "MNW32": "[ iPad Air 2 ] iPad5,4",
        "MH2P2": "[ iPad Air 2 ] iPad5,4",
        "MH172": "[ iPad Air 2 ] iPad5,4",
        "MHWP2": "[ iPad Air 2 ] iPad5,4",
        "MH332": "[ iPad Air 2 ] iPad5,4",
        "MH2D2": "[ iPad Air 2 ] iPad5,4",
        "MH1G2": "[ iPad Air 2 ] iPad5,4",
        "MH2V2": "[ iPad Air 2 ] iPad5,4",
        "MGHC2": "[ iPad Air 2 ] iPad5,4",
        "MNW22": "[ iPad Air 2 ] iPad5,4",
        "MH2N2": "[ iPad Air 2 ] iPad5,4",
        "MGHY2": "[ iPad Air 2 ] iPad5,4",
        "MGK02": "[ iPad Air 2 ] iPad5,4",
        "MH322": "[ iPad Air 2 ] iPad5,4",
        "MGWM2": "[ iPad Air 2 ] iPad5,4",
        "MGGX2": "[ iPad Air 2 ] iPad5,4",
        "MH2U2": "[ iPad Air 2 ] iPad5,4",
        "MGH62": "[ iPad Air 2 ] iPad5,4",
        "MNW12": "[ iPad Air 2 ] iPad5,4",
        "MH2M2": "[ iPad Air 2 ] iPad5,4",
        "MGHX2": "[ iPad Air 2 ] iPad5,4",
        "MGJY2": "[ iPad Air 2 ] iPad5,4",
        "MH312": "[ iPad Air 2 ] iPad5,4",
        "MGWL2": "[ iPad Air 2 ] iPad5,4",
        "MD528": "[ iPad Mini ] iPad2,5",
        "MF432": "[ iPad Mini ] iPad2,5",
        "MD529": "[ iPad Mini ] iPad2,5",
        "MD530": "[ iPad Mini ] iPad2,5",
        "MD531": "[ iPad Mini ] iPad2,5",
        "MD532": "[ iPad Mini ] iPad2,5",
        "MD533": "[ iPad Mini ] iPad2,5",
        "MD534": "[ iPad Mini ] iPad2,6",
        "ME030": "[ iPad Mini ] iPad2,6",
        "MF442": "[ iPad Mini ] iPad2,6",
        "MF743": "[ iPad Mini ] iPad2,6",
        "MD535": "[ iPad Mini ] iPad2,6",
        "ME031": "[ iPad Mini ] iPad2,6",
        "MD536": "[ iPad Mini ] iPad2,6",
        "ME032": "[ iPad Mini ] iPad2,6",
        "MD537": "[ iPad Mini ] iPad2,6",
        "ME033": "[ iPad Mini ] iPad2,6",
        "MF746": "[ iPad Mini ] iPad2,6",
        "MD538": "[ iPad Mini ] iPad2,6",
        "ME034": "[ iPad Mini ] iPad2,6",
        "MD539": "[ iPad Mini ] iPad2,6",
        "ME035": "[ iPad Mini ] iPad2,6",
        "MD540": "[ iPad Mini ] iPad2,7",
        "ME215": "[ iPad Mini ] iPad2,7",
        "MF450": "[ iPad Mini ] iPad2,7",
        "MF453": "[ iPad Mini ] iPad2,7",
        "MD541": "[ iPad Mini ] iPad2,7",
        "ME216": "[ iPad Mini ] iPad2,7",
        "MD542": "[ iPad Mini ] iPad2,7",
        "ME217": "[ iPad Mini ] iPad2,7",
        "MD543": "[ iPad Mini ] iPad2,7",
        "ME218": "[ iPad Mini ] iPad2,7",
        "MD544": "[ iPad Mini ] iPad2,7",
        "ME219": "[ iPad Mini ] iPad2,7",
        "MD545": "[ iPad Mini ] iPad2,7",
        "ME220": "[ iPad Mini ] iPad2,7",
        "ME279": "[ iPad Mini 2 ] iPad4,4",
        "ME280": "[ iPad Mini 2 ] iPad4,4",
        "ME281": "[ iPad Mini 2 ] iPad4,4",
        "ME860": "[ iPad Mini 2 ] iPad4,4",
        "ME276": "[ iPad Mini 2 ] iPad4,4",
        "ME277": "[ iPad Mini 2 ] iPad4,4",
        "ME278": "[ iPad Mini 2 ] iPad4,4",
        "ME856": "[ iPad Mini 2 ] iPad4,4",
        "ME814": "[ iPad Mini 2 ] iPad4,5",
        "ME818": "[ iPad Mini 2 ] iPad4,5",
        "MF074": "[ iPad Mini 2 ] iPad4,5",
        "MF075": "[ iPad Mini 2 ] iPad4,5",
        "MF076": "[ iPad Mini 2 ] iPad4,5",
        "MF544": "[ iPad Mini 2 ] iPad4,5",
        "ME824": "[ iPad Mini 2 ] iPad4,5",
        "MF083": "[ iPad Mini 2 ] iPad4,5",
        "MF084": "[ iPad Mini 2 ] iPad4,5",
        "MF085": "[ iPad Mini 2 ] iPad4,5",
        "MF569": "[ iPad Mini 2 ] iPad4,5",
        "ME832": "[ iPad Mini 2 ] iPad4,5",
        "MF089": "[ iPad Mini 2 ] iPad4,5",
        "MF090": "[ iPad Mini 2 ] iPad4,5",
        "MF091": "[ iPad Mini 2 ] iPad4,5",
        "MF580": "[ iPad Mini 2 ] iPad4,5",
        "ME840": "[ iPad Mini 2 ] iPad4,5",
        "MF120": "[ iPad Mini 2 ] iPad4,5",
        "MF121": "[ iPad Mini 2 ] iPad4,5",
        "MF123": "[ iPad Mini 2 ] iPad4,5",
        "MF594": "[ iPad Mini 2 ] iPad4,5",
        "ME800": "[ iPad Mini 2 ] iPad4,5",
        "MF066": "[ iPad Mini 2 ] iPad4,5",
        "MF069": "[ iPad Mini 2 ] iPad4,5",
        "MF070": "[ iPad Mini 2 ] iPad4,5",
        "MF078": "[ iPad Mini 2 ] iPad4,5",
        "MF519": "[ iPad Mini 2 ] iPad4,5",
        "ME820": "[ iPad Mini 2 ] iPad4,5",
        "MF080": "[ iPad Mini 2 ] iPad4,5",
        "MF081": "[ iPad Mini 2 ] iPad4,5",
        "MF082": "[ iPad Mini 2 ] iPad4,5",
        "MF552": "[ iPad Mini 2 ] iPad4,5",
        "ME828": "[ iPad Mini 2 ] iPad4,5",
        "MF086": "[ iPad Mini 2 ] iPad4,5",
        "MF087": "[ iPad Mini 2 ] iPad4,5",
        "MF088": "[ iPad Mini 2 ] iPad4,5",
        "MF575": "[ iPad Mini 2 ] iPad4,5",
        "ME836": "[ iPad Mini 2 ] iPad4,5",
        "MF116": "[ iPad Mini 2 ] iPad4,5",
        "MF117": "[ iPad Mini 2 ] iPad4,5",
        "MF118": "[ iPad Mini 2 ] iPad4,5",
        "MF585": "[ iPad Mini 2 ] iPad4,5",
        "MF248": "[ iPad Mini 2 ] iPad4,6",
        "MF252": "[ iPad Mini 2 ] iPad4,6",
        "MF246": "[ iPad Mini 2 ] iPad4,6",
        "MF244": "[ iPad Mini 2 ] iPad4,6",
        "MF247": "[ iPad Mini 2 ] iPad4,6",
        "MF251": "[ iPad Mini 2 ] iPad4,6",
        "MF245": "[ iPad Mini 2 ] iPad4,6",
        "MF243": "[ iPad Mini 2 ] iPad4,6",
        "MKH62": "[ iPod Touch 6 ] iPod7,1",
        "Not Found!": "Not Found!"
    }

# 72 6C 43 44
colors = \
    {
        # iPhone 5C / 32 bit universal ?
        "726c434401000000010000000000000000000000": "White",
        "0002000089f1fa003c3b3b0000000000": "Yellow",
        "000200007a76fe003c3b3b0000000000": "Red",  
        "00020000f7f4f5003c3b3b0000000000": "Black",
        "0002000077e8a1003c3b3b0000000000": "Green",
        "00020000e0ab46003c3b3b0000000000": "Blue",
        # iPhone 5S , iPad 5 , iPad 6 , iPad Mini 2 , iPhone 6 , iPhone 6 P
        "000200009b9899003c3b3b0000000000": "Black", 
        "00020000d8d9d700e3e4e10000000000": "White", # Silver
        # iPad 3,4,iPhone 4S,iPhone 5
        "43726c4301000000010000000000000000000000": "White",
        "43726c4300000000000000000000000000000000": "Black",
        # iPad Mini 1 Unknown
        "43726c4301000000000000000000000000000000": "Unknown",
        # Gold Universal
        "00020000b3c5d400e3e4e10000000000": "Gold",
        "00020000b5cce100e3e4e10000000000": "Unknown",
        "000200006d6a6b003c3b3b0000000000": "Space Grey"
        # TODO : iPOD Color work.
    }


search = \
    {
        "bt": "63614d42",
        "wifi": "63614d57",
        "sn": "6d4e7253",
        "model": "23646f4d",
        "region": "6e676552",
        "device": "23644d52",
        "color": "726c434400020000"
    }


def color_search(this_hex):
    for key in colors:
        if key in this_hex:
            return colors[key]


def searching(text_hex, chunk):
    dis = []
    if text_hex in chunk:
        for item in chunk.split("0000"):
            if text_hex in item:
                dis = item.strip().split(text_hex)
                break
        return str(dis[1])
    else:
        return "4E6F7420466F756E6421"


def is_not_empty(s):  # if string is empty or not
    """
    :param s: String
    :return: Bool value given the string if empty will return True
    """
    return bool(s and s.strip())


def end_zero(mihex):
    x = len(mihex)
    if x % 2 == 0:
        return True


if __name__ == '__main__':

    if os.path.isfile("boot2.bin") is True:
        if os.path.getsize("boot2.bin") > 2105344:
            print("File size for boot2.bin should be 2 MBytes")
            sys.exit()
        else:
            f = open("boot2.bin", "rb")
            file_contents = f.read()
            f.close()
            if is_not_empty(file_contents) is True:
                my_hex = bytearray(binascii.hexlify(file_contents))  # fast
                # my_hex = ''.join(x.encode('hex') for x in file_contents) # slow
                """
                # Debug :
                f = open("ecsd1.txt", "w")
                f.write(my_hex)
                f.close()           
                """

                # TODO : check wifi - bt compatibility .

                wifi = searching(search["wifi"], my_hex)
                if len(wifi) < 12:
                    wifi = wifi.ljust(12, "0")
                else:
                    pass
                # format AA:BB:CC:DD:EE:FF
                wifi = ":".join([wifi[i:i + 2]
                                 for i in range(0, len(wifi), 2)])
                bluetooth = searching(search["bt"], my_hex)
                if len(bluetooth) < 12:
                    bluetooth = bluetooth.ljust(12, "0")
                else:
                    pass
                # format AA:BB:CC:DD:EE:FF
                bluetooth = ":".join([bluetooth[i:i + 2]
                                      for i in range(0, len(bluetooth), 2)])
                serial = searching(search["sn"], my_hex)
                if end_zero(serial) is not True:
                    serial = serial + "0"
                serial = serial.decode("hex")
                model = searching(search["model"], my_hex).decode("hex")
                region = searching(search["region"], my_hex).decode("hex")
                device = searching(search["device"], my_hex).decode("hex")
                color = color_search(my_hex)
                # Print out details
                print("WIFI ID : " + wifi.upper())
                print("BLT. ID : " + bluetooth.upper())
                print("SERIAL  : " + serial)
                print("MODEL   : " + model + region)
                print("DEVICE  : " + model_list[model] + " [ " + device + " ]")
                print("COLOR   : " + str(color).upper())
                # board ID .
            else:
                print("Empty ?")
    else:
        print("File not found")
        sys.exit()
