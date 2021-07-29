import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)
def main():
    access_token = 'sl.A1UlOdxqV5Fk2jSj7coODznS4C5uVTS0hAaYB6IzZ6B-N0MIUcFhCPOZ98pduG3JtGQEXq2lBrio9FaeuLSC9H_OmL3LL3HJcgOeOj4tWU9kmlNTJND_KKKpfzI1eikp2sdwuS0'
    transferData = TransferData(access_token)
    file_from = input("enter the file path to transfer")
    file_to = input("enter the full path to upload to dropbox")

    transferData.upload_file(file_from, file_to)
    print("file has been moved")

main()