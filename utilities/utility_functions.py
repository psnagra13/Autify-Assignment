def getUrls(args:list):

    urls = []

    for i in range(1, len(args)) :
        urls.append(args[i])

    # If no url provided
    if len(urls) == 0:
        print("Error: No Url Provided.")
        exit()

    print('Info: Number of Urls Provided = ', len(urls))

    return urls

def printSummary(summary):
    for entry in summary:
        url = entry[0]
        linksCount = entry[1]
        imagesCount = entry[2]
        lastDownloadTime = entry[3]
        print()
        print('site : ', url)
        print('num_links : ', linksCount)
        print('images : ', imagesCount)
        print('last_fetch : ', lastDownloadTime)

