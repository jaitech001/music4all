from bs4 import BeautifulSoup
#import csv
import requests
import pandas
from openpyxl import load_workbook

homepage = requests.get("https://www.raaga.com/tamil/movies")
soup = BeautifulSoup(homepage.content, 'html.parser')

#print(soup.prettify())

#final_link = soup.p.a
#final_link.decompose()

writer = pandas.ExcelWriter('Webscrap.xlsx', engine='xlsxwriter')

#f = csv.writer(open("Webscrap.csv", "w")) # needed when import csv is used
#f.writerow(["MovieName", "MovieLink"])    # Write column headers as the first line # needed when import csv is used

links = soup.find_all('div',class_="browseresult_index_album01", limit=10)

MovieName = []
MovieLink = []

for link in links:
    Movie_Name = link.text #   print(MovieName)
    MovieName.append(Movie_Name)
    Movie_Link = link.find('a').get('href') #   print(MovieLink)
    MovieLink.append(Movie_Link)
#   f.writerow([MovieName, MovieLink]) # needed when import csv is used
#    data = [[MovieName,MovieLink]]
#    print(data)

data = list(zip(MovieName,MovieLink))    

#creating the pandas dataframe
df1 = pandas.DataFrame(data,columns = ["MovieName","MovieLink"])
#output = pandas.ExcelWriter("Webscrap.xlsx",engine="xlsxwriter")
#df1.to_excel(output,sheet_name='MovieLists',index=False)
#output.save()

# Writing the data frame to a new Excel File 
try: 
    df1.to_excel("Webscrap.xlsx",sheet_name='MovieLists',index=False)
except:
    print("\nSomething went wrong ! Please check errors and execute again.")
else:
    print("\nMovie data scrapped and written to excel")
finally:
    print("\nProgram execution completed successfully")
    
excel = pandas.read_excel("Webscrap.xlsx", "MovieLists")
df2 = pandas.DataFrame(excel, columns = ["MovieName","MovieLink"])

#SongDetails = []
Song_Name = []
#Song_Time = []
Song_Singers = []
Song_Lyricist = []

for i,j in df2.iterrows():
#   print("Second loop started")
#   Movie=i.loc[1]
#   print(Movie)
#   link=df2["MovieLink"].to_string(index=False) # to remove index column
    moviepage=requests.get(j.iloc[1])
#   print(moviepage)
    soup = BeautifulSoup(moviepage.content, 'html.parser')
    links = soup.find_all('div',class_="new-album-track-details", limit=10)
    
    for link in links:
        Song_Details = link.get_text(strip=True) #   print(MovieName)
#       Song_Details = link.get_text().replace("\r\n","|") #   print(MovieName)
        print(Song_Details)
        Song_Name = link.find('Singers')
#       Song_Time = link.find()
#       Song_Singers = link.find('Singers')
#       Song_Lyricist = link.find('Lyricist')
#       print(Song_Details.attrs)
#       song_data = list(zip(Song_Name,Song_Singers,Song_Lyricist))
#       df3 = pandas.DataFrame(song_data,columns = ["Song_Name","Song_Singers","Song_Lyricist"])
#       df3 = pandas.DataFrame(Song_Details)
#       print(df3)
#       df3[["Song_Name","Song_Time","Song_Singers","Song_Lyricist"]] = df3.Song_Details_ALL.str.split('\n',expand=True) 
#       print(df3)

#df4 = pandas.DataFrame(song_data,columns = ["MovieName","SongName"])
#print(df4)