import binascii
import os
import sys

__author__ = "Oz"
__copyright__ = "Apple BOOT2 Parser"


model_list = \
    {
        "A1431": "iPhone 4S",
        "A1387": "iPhone 4S",
        "A1533": "iPhone 5S",
        "A1453": "iPhone 5S",
        "A1428": "iPhone 5",
        "A1429": "iPhone 5",
        "A1442": "iPhone 5",
        "A1532": "iPhone 5C",
        "A1456": "iPhone 5C",
        "A1507": "iPhone 5C",
        "A1529": "iPhone 5C",
        "A1516": "iPhone 5C",
        "A1526": "iPhone 5C",
        "A1457": "iPhone 5S",
        "A1530": "iPhone 5S",
        "A1518": "iPhone 5S",
        "A1528": "iPhone 5S",
        "A1549": "iPhone 6",
        "A1586": "iPhone 6",
        "A1589": "iPhone 6",
        "A1522": "iPhone 6P",
        "A1524": "iPhone 6P",
        "A1593": "iPhone 6P",
        "A1421": "iPod Touch 5",
        "A1509": "iPod Touch 5",
        "A1574": "iPod Touch 6",
        "A1219": "iPad 1",
        "A1337": "iPad 1",
        "A1395": "iPad 2",
        "A1396": "iPad 2",
        "A1397": "iPad 2",
        "A1416": "iPad 3",
        "A1403": "iPad 3",
        "A1430": "iPad 3",
        "A1458": "iPad 4",
        "A1459": "iPad 4",
        "A1460": "iPad 4",
        "A1474": "iPad Air",
        "A1475": "iPad Air",
        "A1476": "iPad Air",
        "A1566": "iPad Air 2",
        "A1567": "iPad Air 2",
        "A1432": "iPad Mini",
        "A1454": "iPad Mini",
        "A1455": "iPad Mini",
        "A1489": "iPad Mini 2",
        "A1490": "iPad Mini 2",
        "A1491": "iPad Mini 2",
        "A1599": "iPad Mini 3",
        "A1600": "iPad Mini 3",
        "A1601": "iPad Mini 3",
        "A1538": "iPad Mini 4",
        "A1550": "iPad Mini 4",
        "A1822": "iPad 2017",
        "A1823": "iPad 2017",
        "A1662": "iPhone SE",
        "A1723": "iPhone SE",
        "A1724": "iPhone SE",
        "A1633": "iPhone 6S",
        "A1688": "iPhone 6S",
        "A1700": "iPhone 6S",
        "A1691": "iPhone 6S",
        "A1634": "iPhone 6SP",
        "A1687": "iPhone 6SP",
        "A1699": "iPhone 6SP",
        "A1690": "iPhone 6SP",
        "A1660": "iPhone 7",
        "A1778": "iPhone 7",
        "A1779": "iPhone 7",
        "A1661": "iPhone 7P",
        "A1784": "iPhone 7P",
        "A1785": "iPhone 7P",
        "Not Found!": "Not Found!"
    }


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
        "00020000d8d9d700e3e4e10000000000": "White",
        # iPad 3,4,iPhone 4S,iPhone 5
        "43726c4301000000010000000000000000000000": "White",
        "43726c4300000000000000000000000000000000": "Black",
        # iPad Mini 1 Unknown
        "43726c4301000000000000000000000000000000": "Unknown",
        # Gold Universal
        "00020000b3c5d400e3e4e10000000000": "Gold",
        "00020000b5cce100e3e4e10000000000": "Unknown"
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
                print("DEVICE  : " + model_list[device] + " [ " + device + " ]")
                print("COLOR   : " + str(color).upper())
                # board ID .
            else:
                print("Empty ?")
    else:
        print("File not found")
        sys.exit()
