from urllib.request import urlopen
import bs4
class WebpageDownloader:

    '''
        downloadWebPageFromUrl(weburl)
            downloads the html for the url provided and return result as a string

            weburl : string
                url of the webpage to be downloaded

            return string
                html of th page as string

    '''
    def downloadWebPageFromUrl(self, weburl: str) :

        try:
            response = urlopen(weburl)
            content = response.read().decode("utf-8", errors='ignore')
            soup = bs4.BeautifulSoup(content, features='html.parser')
            imageCount = len(soup.findAll('img'))
            linkCount = len(soup.find_all('a'))
            return content, imageCount, linkCount
        except Exception as e:
            print(e)
            return None, None, None




if __name__ == "__main__":
    object = WebpageDownloader()
    result, imageCount, linkCount = object.downloadWebPageFromUrl("http://www.google.com")
    print(result)
    print(imageCount)
    print(linkCount)
