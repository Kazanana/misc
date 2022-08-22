from tracemalloc import stop
from googlesearch import search
import urllib.request
import re

query = "wig 20"
list_of_links = []
for j in search(query, tld="com", num=5, stop=5, pause=2):
    list_of_links.append(j)

# print(list_of_links)

# open connection to a URL using urllib list_of_links[0]
webUrl = urllib.request.urlopen(list_of_links[0])

# # get result code and print it
# #print ("result code: " + str(webUrl.getCode()))

# # read the data from the URL and print it
data = webUrl.read()
# print(data)
phrase_to_find = '<div id="boxProfilHeader" class="box975 boxInfo border1">'
# span = re.findall(phrase_to_find, data)
# print(span)
string_html = data.decode("utf-8")
# print(type(string_html))
span = re.findall(phrase_to_find, string_html)
print(span)

