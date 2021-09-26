import datetime
import pickle

'''
    Class to save last download times for a url
'''
class Logger:

    def __init__(self):

        # { url : lastDownload time}
        self.logs = {}
        self.FILENAME = 'logs.pickle'

        try:
            # load logs from file if present
            with open(self.FILENAME, 'rb') as handle:
                self.logs = pickle.load(handle )
        except Exception as e:
            print(e)
            pass
        print(self.logs)

    def getLastDownloadTime(self, url):

        if url in self.logs:
            return self.logs[url]
        return None

    def setLastDownloadTime(self, url):
        self.logs[url] = datetime.datetime.now()

        # save logs from file
        with open(self.FILENAME, 'wb') as handle:
            pickle.dump(self.logs, handle, protocol=pickle.HIGHEST_PROTOCOL)



if __name__ == "__main__":
    object = Logger()
    result = object.getLastDownloadTime(" http://www.google.com")
    print(result)
    result = object.setLastDownloadTime(" http://www.google.com")
    print(result)
