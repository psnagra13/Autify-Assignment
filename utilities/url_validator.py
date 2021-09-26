import re

class UrlValidator:

    '''
        isUrlvalid(webUrl)
            returns True is the url is valid
    '''
    def isUrlValid(self, webUrl: str) -> bool:
        regex = re.compile(
                r'^(?:http|ftp)s?://'  # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
                r'localhost|'  # localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
                r'(?::\d+)?'  # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if re.match(regex, webUrl):
            return True
        return False



if __name__ == "__main__":
    object = UrlValidator()
    url1 = 'https://'
    url2 = 'https://abc.cp'
    url3 = 'https://www.abc.cp'
    url4 = 'hts://abc.cp'

    assert object.isUrlValid(url1) == False
    assert object.isUrlValid(url2) == True
    assert object.isUrlValid(url3) == True
    assert object.isUrlValid(url4) == False

    print('All Test Cases passed')


