from bs4 import BeautifulSoup
import requests
import pandas
import numpy as np
from openpyxl import load_workbook
from openpyxl import Workbook
import xlsxwriter

homepage = requests.get("https://www.raaga.com/tamil/movies")
soup = BeautifulSoup(homepage.content, 'html.parser')

#links = soup.find_all('div',class_="browseresult_index_album01")
links = soup.find_all('div',class_="browseresult_index_album01", limit=100)

MovieName = []
MovieLink = []

for link in links:
    Movie_Name = link.text.replace("\n","") #   print(MovieName)
    MovieName.append(Movie_Name)
    Movie_Link = link.find('a').get('href').replace("\n","") #   print(MovieLink)
    MovieLink.append(Movie_Link)

data_movie = list(zip(MovieName,MovieLink))    

#creating the pandas dataframe
df1 = pandas.DataFrame(data_movie,columns = ["MovieName","MovieLink"])
df1.index += 1

# Writing the data frame to a new Excel File 
try: 
    df1.to_excel("Webscrap.xlsx",sheet_name='MovieLists',index=True)
except:
    print("\nSomething went wrong during Movie scrapping!! Please check errors and execute again.")
    quit()
else:
    print("\nMovie data scrapped and written to excel")
finally:
    print("Continuing to scrap Song data...\n")
    
excel = pandas.read_excel("Webscrap.xlsx", "MovieLists")
df2 = pandas.DataFrame(excel, columns = ["MovieName","MovieLink"])

df3 = []
Song_Details_ALL = []
movie_name = []
movie_year = []
movie_music_director = []
song_name = []
song_time = []
song_singer = []
song_lyricist = []
SongDetailsFull = []


for i,j in df2.iterrows():
    moviepage=requests.get(j.iloc[1]) #   print(moviepage)
    soup = BeautifulSoup(moviepage.content, 'html.parser')
#    links = soup.find_all('div',class_="new-album-track-details")
    try:
        movie_nm = soup.find('div',class_="album-details").find(class_="album-name")
        movie_name = movie_nm['title'].replace(" songs","")
    except:
        movie_name = "Not Available"
    else:
        dummy = ""
    try:
        movie_yr = soup.find('div',class_="album-details").find(class_="album-name").find(class_="history-ajaxy")
        movie_year = movie_yr.string
    except:
        movie_year = "Not Available"
    else:
        dummy = ""
    try:
        movie_music_dir = soup.find('div',class_="album-details").find(class_="album-artist-detail").find(class_="artist-name")
        movie_music_director = movie_music_dir.text.replace("Music: ","")
    except:
        movie_music_director = "Not Available"
    else:
        dummy = ""
    try:
        movie_cst = soup.find('div',class_="album-details").find(class_="album-artist-detail").find(class_="newalb_smalltitle").find_next("h2")
        movie_cast = movie_cst.text.replace("\r\n","").replace("\xa0","").replace("\t","").replace("\n","").replace("Cast: ","").replace("  ","").strip()
    except:
        movie_cast = "Not Available"
    else:
        dummy = ""
    song_list = soup.find_all('div',class_="new-album-track-details")
    
    for song in song_list:
        try:
            song_name = song.div.a.text
        except:
            song_name = "Not Available"
        else:
            dummy = ""
        try:
            song_time = song.span.text
        except:
            song_time = "Not Available"
        else:
            dummy = ""
        try:
            song_singer = song.find(class_="new-singers-name").text.replace("/n","").replace("Singers:","").strip()
        except:
            song_singer = "Not Available"
        else:
            dummy = ""
        try:
            song_lyr = song.div.next_sibling.next_sibling.next_sibling.next_sibling
            song_lyricist = song_lyr.text.replace("\n","").replace("Lyricist:","").strip()
        except:
            song_lyricist = "Not Available"
        else:
            dummy = ""
        song_details_full = {'MovieName': movie_name, 'MovieYear': movie_year, 'MusicDirector': movie_music_director, 'MovieCast': movie_cast, 'SongName': song_name, 'SongTime': song_time, 'Singers': song_singer,'Lyricist': song_lyricist }
        SongDetailsFull.append(song_details_full)

df3 = pandas.DataFrame(SongDetailsFull)
df3.index += 1

book = load_workbook('Webscrap.xlsx')
writer = pandas.ExcelWriter('Webscrap.xlsx', engine='openpyxl')
writer.book = book

# Writing the data frame to a new Excel File 
try: 
     df3.to_excel(writer,sheet_name='SongLists',index=True)
     writer.save()
except:
    print("\nSomething went wrong during Song scrapping!! Please check errors and execute again.")
    quit()
else:
    print("\nSong data scrapped and written to excel")
finally:
    print("Program execution completed successfully\n")