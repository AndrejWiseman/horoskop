from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, url_for

def fetch_horoscope(url):
    req = Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    })
    html_text = urlopen(req).read()
    soup = BeautifulSoup(html_text, 'lxml')
    return soup.find('div', class_='article-details').text

def blizanci():
    url_dnevni = 'http://www.horoskopius.com/dnevni-horoskop/blizanci/'
    url_nedeljni = 'http://www.horoskopius.com/nedeljni-horoskop/blizanci/'
    url_mesecni = 'http://www.horoskopius.com/mesecni-horoskop/blizanci/'
    url_godisnji = 'http://www.horoskopius.com/godisnji-horoskop/blizanci/'

    dnevni = fetch_horoscope(url_dnevni)
    nedeljni = fetch_horoscope(url_nedeljni)
    mesecni = fetch_horoscope(url_mesecni)
    godisnji = fetch_horoscope(url_godisnji)

    return render_template('blizanci.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji)

def vodolija():
    url_dnevni = 'http://www.horoskopius.com/dnevni-horoskop/vodolija/'
    url_nedeljni = 'http://www.horoskopius.com/nedeljni-horoskop/vodolija/'
    url_mesecni = 'http://www.horoskopius.com/mesecni-horoskop/vodolija/'
    url_godisnji = 'http://www.horoskopius.com/godisnji-horoskop/vodolija/'

    dnevni = fetch_horoscope(url_dnevni)
    nedeljni = fetch_horoscope(url_nedeljni)
    mesecni = fetch_horoscope(url_mesecni)
    godisnji = fetch_horoscope(url_godisnji)

    return render_template('vodolija.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji)






#
# from urllib.request import Request, urlopen
#
# from bs4 import BeautifulSoup
# from flask import Flask, render_template, request, url_for
#
#
# # Blizanci
# def blizanci():
#     url = 'http://www.horoskopius.com/dnevni-horoskop/blizanci/'
#     url_n = 'http://www.horoskopius.com/nedeljni-horoskop/blizanci/'
#     url_m = 'http://www.horoskopius.com/mesecni-horoskop/blizanci/'
#     url_g = 'http://www.horoskopius.com/godisnji-horoskop/blizanci/'
#
#     req = Request(url, headers={
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
#     })
#     req_n = Request(url_n, headers={
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
#     })
#     req_m = Request(url_m, headers={
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
#     })
#     req_g = Request(url_g, headers={
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
#     })
#
#     html_text = urlopen(req).read()
#     html_text_n = urlopen(req_n).read()
#     html_text_m = urlopen(req_m).read()
#     html_text_g = urlopen(req_g).read()
#
#     soup = BeautifulSoup(html_text, 'lxml')
#     soup_n = BeautifulSoup(html_text_n, 'lxml')
#     soup_m = BeautifulSoup(html_text_m, 'lxml')
#     soup_g = BeautifulSoup(html_text_g, 'lxml')
#
#     dnevni = soup.find('div', class_='article-details').text
#     nedeljni = soup_n.find('div', class_='article-details').text
#     mesecni = soup_m.find('div', class_='article-details').text
#     godisnji = soup_g.find('div', class_='article-details').text
#
#     return render_template('blizanci.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji)
#
#
#
# # Vodolija
# def vodolija():
#     url = 'http://www.horoskopius.com/dnevni-horoskop/vodolija/'
#     url_n = 'http://www.horoskopius.com/nedeljni-horoskop/vodolija/'
#     url_m = 'http://www.horoskopius.com/mesecni-horoskop/vodolija/'
#     url_g = 'http://www.horoskopius.com/godisnji-horoskop/vodolija/'
#
#     req = Request(url, headers={
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
#     })
#     req_n = Request(url_n, headers={
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
#     })
#     req_m = Request(url_m, headers={
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
#     })
#     req_g = Request(url_g, headers={
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
#     })
#
#     html_text = urlopen(req).read()
#     html_text_n = urlopen(req_n).read()
#     html_text_m = urlopen(req_m).read()
#     html_text_g = urlopen(req_g).read()
#
#     soup = BeautifulSoup(html_text, 'lxml')
#     soup_n = BeautifulSoup(html_text_n, 'lxml')
#     soup_m = BeautifulSoup(html_text_m, 'lxml')
#     soup_g = BeautifulSoup(html_text_g, 'lxml')
#
#     dnevni = soup.find('div', class_='article-details').text
#     nedeljni = soup_n.find('div', class_='article-details').text
#     mesecni = soup_m.find('div', class_='article-details').text
#     godisnji = soup_g.find('div', class_='article-details').text
#
#     return render_template('vodolija.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji)
