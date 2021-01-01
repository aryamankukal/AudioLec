import urllib.request
import re
import ssl

def searchVideoForKeyword(searchKeyword):
    if len(searchKeyword.split(" ")) > 1:
        searchKeyword  = searchKeyword.replace(" ", "+")

    searchKeyword = searchKeyword.replace("!web ", "")
    url = "https://www.youtube.com/results?search_query=" + searchKeyword
    gcontext = ssl.SSLContext()
    html = urllib.request.urlopen(url, context=gcontext)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print("https://www.youtube.com/watch?v=" + video_ids[0])
    print("https://www.youtube.com/watch?v=" + video_ids[1])
    print("https://www.youtube.com/watch?v=" + video_ids[2])


searchVideoForKeyword("mr beast")