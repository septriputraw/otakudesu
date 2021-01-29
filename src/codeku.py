from bs4 import BeautifulSoup
from requests import get
import json

class Script:

    def query(self, url):
        datas = get(url)
        soup = BeautifulSoup(datas.text, 'html.parser')
        tag = soup.find_all('li')
        data = []

        for i in tag:
            try:
                title = i.find('h2', class_="jdlflm").text
                link = i.find('a').get('href')
                gambar = i.find('img').get('src')
                eps = i.find('div', class_="epz").text
                waktu = i.find('div', class_="newnime").text
                data.append({
                    "judul": title,
                    "link": link,
                    "poster": gambar,
                    "eps": eps,
                    "waktu": waktu
                })
            except:
                pass

        return data

    def index(self):
        return self.query('https://otakudesu.tv/')
    '''def movie(self):
        return self.query('https://gomunime.me/movie')
       
    def nasional(self):
        return self.query('https://www.cnnindonesia.com/nasional')
    def internasional(self):
        return self.query('https://www.cnnindonesia.com/internasional')
    def ekonomi(self):
        return self.query('https://www.cnnindonesia.com/ekonomi')
    def olahraga(self):
        return self.query('https://www.cnnindonesia.com/olahraga')

    def teknologi(self):
        return self.query('https://www.cnnindonesia.com/teknologi')

    def hiburan(self):
        return self.query('https://www.cnnindonesia.com/hiburan')

    def social(self):
        return self.query('https://www.cnnindonesia.com/gaya-hidup')'''
    def detail(self, url):
        datas = get(url)
        soup = BeautifulSoup(datas.text, 'html.parser')
        tag = soup.find_all('li')
        data = []
        for i in tag:
            try:
                ##req = get(url)
                ##soup = BeautifulSoup(req.text, 'html.parser')
                tag = soup.find('div', class_="infozingle")
                gambar = soup.find('div', class_='fotoanime').find('img').get('src')
                judul = soup.find('h1').text
                body = tag.text
                data.append({
                    "judul": judul,
                    "poster": gambar,
                    "body": body,
                })
            except:
                data.append({
                    "message": "network error",
                })

        return data

    def search(self,q):
        return self.query('https://otakudesu.tv/s?=' + q +'&post_type=anime' )

if __name__ != '__main__':
    Codeku = Script()