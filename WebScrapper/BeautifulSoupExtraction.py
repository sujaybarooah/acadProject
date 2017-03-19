from bs4 import BeautifulSoup
import urllib.request
import re


r = urllib.request.urlopen('http://whed.net/detail_institution.php?id=8').read()
soup = BeautifulSoup(r, 'lxml')


pageContent = soup.section
# print(pageContent)
countryName= pageContent.find("p", class_="country")
print(countryName.get_text())

############################
sectionHeader =''
sectionKeys =''
sectionValues =''
anchorName = re.compile("^ancre")
aTags = pageContent.find_all('a', attrs={'name': anchorName})
print(len(aTags))

for i in range (len(aTags)):
    print(aTags[i].get('name'))
    #print(pageContent.aTags[i].nextSibling)

# for i in range(len(aTags)):

    # print(pageContent.aTags[i].nextSibling.name)

    # if aTags[i].get('name')==("ancre%s", i):
    #     print(aTags[i].get('name'))
    #     sectionHeader = pageContent.find('h3')
    #     print(sectionHeader.get_text())
    #     break



# for i in aTags:
#     if (aTags[i].get('name')=='ancre1'):
#         sectionHeader = pageContent.find('h3')
#         print(sectionHeader.get_text())
#         break
#     if (aTags[i].get('name')=='ancre2'):
#         break



# for aTags in pageContent.find_all('a'):
#     print(aTags.get('name'))
#     if (aTags.get('name')=='ancre1'):
#         sectionHeader = pageContent.find('h3')
#         sectionKeys = pageContent.find_all('span', class_='dt')
#         sectionValues= pageContent.find_all('div', class_='dd')
#         break
# print(sectionHeader.get_text())
# print(sectionKeys[0].get_text())
# print(sectionValues[0].get_text())



# instituteName= soup.find("h2")
# countryName= soup.find("p", class_="country")
# sectionHeader= soup.find_all("h3",)
# keys = soup.find_all("span", class_="dt")
# values = soup.find_all("div", class_="dd")
#
# print(instituteName.get_text())
# print(countryName.get_text())
# print(sectionHeader[1])
# print(keys[1].get_text())
# print(keys)
# print(values[1].get_text())

# a= sectionHeader[1].find_parent("a")
# print(a)
#print (soup.get_text())
# tag = soup.find_all("a", name_="ancre1")
# print(tag[0])

# sectionContent = u""
# for tag in soup.find("a",name_="ancre1").next_siblings:
#     if tag.name=="ancre2":
#         break;
#     else:
#        sectionContent += tag

# print(sectionContent)
