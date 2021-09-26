import sys
from utilities.webpage_downloader import WebpageDownloader
from utilities.save_to_file import SaveToFile
from utilities.url_validator import UrlValidator
from utilities.utility_functions import *
from utilities.logger import Logger

# create objects for the utility classes
downlaoderObject = WebpageDownloader()
saveToFileObject = SaveToFile()
urlValidator = UrlValidator()
logger = Logger()

# get system arguments
arguments = sys.argv

# extract urls from arguments
urls = getUrls(arguments)

# to store and print summary at the end
summary = []

# process each url
for url in urls:

    print('\nInfo: Processing Url : ', url)

    # Validate URL
    if urlValidator.isUrlValid(url) is False:
        print('Error: URL invalid ' , url)
        continue

    # download webpage
    print('Info: Downloading web Page...')
    htmlData, imagesCount, linksCount = downlaoderObject.downloadWebPageFromUrl(url)
    if htmlData is None:
        print('Error: Error downloading webpage ', url)
        continue

    # save html to file
    print('Info: Saving to file...')
    fileName = saveToFileObject.SaveToFile(url, htmlData)
    if fileName is None:
        print('Error: Error saving to file... ', url)
        continue
    print('Info: saved to file = ', fileName)

    lastDownloadTime = logger.getLastDownloadTime(url)
    summary.append([url, linksCount, imagesCount, lastDownloadTime])
    logger.setLastDownloadTime(url)

print('\nInfo: Finished...\n\n')

# print the summary
printSummary(summary)




