import re

class SaveToFile:

    '''
        SaveToFile(weburl, data)
            saves the data to a file

            weburl : string
                url of the webpage
            data : string
                html data of the webpage

            return str
                filename : if success, returns file name
                None : if error

    '''
    def SaveToFile(self, weburl: str, data:str) -> str:
        try:
            fileName = self.__getFileName(weburl)
            with open(fileName, "w") as text_file:
                text_file.write(data)

            return fileName
        except Exception as e:
            print(e)
            return None

    def __getFileName(self, webUrl) -> str:
        regex = re.compile(r"https?://(www\.)?")
        webUrl = regex.sub('', webUrl).strip().strip('/')
        webUrl = webUrl.replace('/', '_')
        return webUrl+ '.html'





if __name__ == "__main__":
    object = SaveToFile()
    result = object.SaveToFile(" http://www.google.com", 'xyz')
    if result == None:
        print('Error saving to file')
    else:
        print('File Name = ', result)
