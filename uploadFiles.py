import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        drbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    drbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A2186qqFin8FgHn5A49kJh5rJhTHQzkQuorlL-MHK8MzwNoiQQzOnTfGVkGyXFK6I2Vsxe88XQxeHmvF1rUc_5N7tuWm1kjkXmbpnWn3r6uasrfxRDU4bfMeC2F-tYzvddLU2xk'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder chosen to transfer : -"))
    file_to = input("enter to upload to dropbox:- ")  
    transferData.upload_file(file_from,file_to)
    print("The file has been moved WooHoo !!!!!!!!!!! :)")

main()