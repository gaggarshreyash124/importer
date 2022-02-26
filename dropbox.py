from os import access
from pip import main
import dropbox

class Transfer:

    def __init__(self,accesstoken):
        self.accesstoken = accesstoken

    def upload_file(self,filefrom,fileto) :
        ddx = dropbox.Dropbox(self.accesstoken)
        f = open(filefrom,"rb")
        ddx.files_upload(f.read(),fileto)

def main () :
    accesstoken = ("sl.BCxqe9VjsMNHDrLDb82Qsk8hWl6zNSgCHE25wVMnvS0Vk27ayWCYkxBX3ENvW-Y7PzQgUjtJ1OvBHxCWVseQguCm0oOE49mCkASDefXigwt7zN4I6BUp-vahuguIooeGBKRXJtA")
    transferdata = Transfer(accesstoken)
    filefrom = input("enter file to transfer:-")
    fileto  = input("where is ur file go to go:-")
    transferdata.upload_file(filefrom,fileto)
    print("all done")

main()