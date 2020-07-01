import xml.etree.ElementTree as ET
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 59595))
s.listen(1)

while True:
    clinet, addres = s.accept()
    temp = ""
    reading = True
    help(clinet.recv())
    with open('temp.xml', 'w') as temp_file:
        while True:
            data_to_save = (clinet.recv(1680)).decode("utf-8")
            temp_file.write(data_to_save.replace('\n', ''))
            if data_to_save == "":
                break
    clinet.close()
    with open('csv_from_xml.csv', 'w') as f2:
        tree = ET.parse('temp.xml')
        root = tree.getroot()
        books = root.findall('book')
        is_first = True
        for book in books:
            id = book.get('id')
            f2.write(id)
            l = []
            if is_first:
                for elm in book:
                    f2.write(elm.tag)
                    is_first = False
            for elm in book:
                f2.write(',')
                f2.write(elm.text)
            f2.write('\n')

