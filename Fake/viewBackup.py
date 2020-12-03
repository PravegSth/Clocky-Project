from django.shortcuts import render
import os
from selenium import webdriver
from requests_html import HTMLSession
import csv
from django.contrib.staticfiles import finders


def home(request):
    return render(request, 'Fake/home.html')


def amazon(request):
    return render(request, 'Fake/amazon.html')


def ebay(request):
    return render(request, 'Fake/ebay.html')


def other(request):
    return render(request, 'Fake/other.html')


def driver_set():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")


def walmart(request):
    driver_set()

    file = finders.find('Fake/log/walmart.csv')
    csv_file = open(file, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Product', 'Link'])

    session = HTMLSession()
    r = session.get('https://www.walmart.com/search/?query=clocky%20alarm%20clock')
    r.html.render()

    article = r.html.find('li.Grid-col')
    damn = ['$39.99', '$45,99']

    for i in article:
        title = i.find('a.product-title-link', first=True).text
        title = title.split()
        title = " ".join(title)
        # price = i.find('span.price-group', first=True).text
        # if price not in damn:
        #     link = i.find('a.product-title-link', first=True).absolute_links
        #     for li in link:
        #         csv_writer.writerow([title, li])
        #         break
        link = i.find('a.product-title-link', first=True).absolute_links
        for li in link:
            csv_writer.writerow([title, li])

    csv_file.close()

    pp = session.get('https://www.walmart.com/search/?query=runaway%20alarm%20clock')
    pp.html.render(timeout=20)

    csv_file = open(file, 'a', encoding="utf-8")
    csv_writer = csv.writer(csv_file)

    article = pp.html.find('li.Grid-col')

    for i in article:
        title = i.find('a.product-title-link', first=True).text
        title = title.split()
        title = " ".join(title)
        link = i.find('a.product-title-link', first=True).absolute_links
        for li in link:
            csv_writer.writerow([title, li])

    csv_file.close()

    pz = session.get('https://www.walmart.com/search/?query=wheel%20alarm%20clock')
    pz.html.render(timeout=20)

    csv_file = open(file, 'a', encoding="utf-8")
    csv_writer = csv.writer(csv_file)

    article = pz.html.find('li.Grid-col')

    for i in article:
        title = i.find('a.product-title-link', first=True).text
        title = title.split()
        title = " ".join(title)
        link = i.find('a.product-title-link', first=True).absolute_links
        for li in link:
            csv_writer.writerow([title, li])

    csv_file.close()
    session.close()

    return render(request, 'Fake/walmart.html')


def alibaba(request):
    driver_set()

    file = finders.find('Fake/log/alibaba.csv')
    csv_file = open(file, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Product', 'Link'])

    session = HTMLSession()
    r = session.get('https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=clocky+alarm+clock+on+wheels')
    r.html.render(timeout=20)

    damn = ["$39.99-$45.99", "$39.99", "$45.99"]
    article = r.html.find('div.organic-gallery-offer-inner')
    for i in article:
        haha = i.find('a.elements-title-normal', first=True)
        title = haha.attrs['title']
        link = haha.attrs['href']
        price = i.find('p.elements-offer-price-normal', first=True)
        price = price.attrs['title']
        if price not in damn:
            csv_writer.writerow([title, link])

    csv_file.close()
    session.close()

    return render(request, 'Fake/alibaba.html')


def aliexpress(request):
    driver_set()

    file = finders.find('Fake/log/aliexpress.csv')
    csv_file = open(file, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Product', 'Link'])

    session = HTMLSession()
    r = session.get('https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20200915084958&SearchText=clocky+alarm+clock')
    r.html.render(timeout=20)

    damn = ["US $39.99", "$39.99", "$45.99", "US $45.99", "US $39.99 - 45.99"]
    article = r.html.find('li.list-item')
    for i in article:
        haha = i.find('a.item-title', first=True)
        title = haha.attrs['title']
        link = haha.attrs['href']
        price = i.find('span.price-current', first=True).text
        if price not in damn:
            csv_writer.writerow([title, link])

    csv_file.close()

    csv_file = open(file, 'a')
    csv_writer = csv.writer(csv_file)

    rr = session.get(
        'https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20200921081517&SearchText=QMJHVX+Led+Wake+Up+Light+Alarm+Clock')
    rr.html.render(timeout=20)

    article = rr.html.find('li.list-item')
    for i in article:
        haha = i.find('a.item-title', first=True)
        title = haha.attrs['title']
        link = haha.attrs['href']
        price = i.find('span.price-current', first=True).text
        if price not in damn:
            csv_writer.writerow([title, link])

    csv_file.close()
    session.close()

    return render(request, 'Fake/aliexpress.html')


def mercari(request):
    driver_set()

    file = finders.find('Fake/log/mercari.csv')
    csv_file = open(file, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Product', 'Link'])

    session = HTMLSession()
    r = session.get('https://www.mercari.com/search/?keyword=clocky%20alarm%20clock')
    r.html.render(timeout=20)

    damn = ["$39.99", "$45.99"]
    article = r.html.find('div.Grid2__Col-mpt2p4-0')
    for i in article:
        aa = i.find('a', first=True)
        title = aa.attrs['alt']
        link = aa.absolute_links
        price = i.find('span', first=True).text
        if price not in damn:
            for li in link:
                csv_writer.writerow([title, li])

    csv_file.close()
    session.close()

    return render(request, 'Fake/mercari.html')


def allegro(request):
    driver_set()

    file = finders.find('Fake/log/allegro.csv')
    csv_file = open(file, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Product', 'Link'])

    session = HTMLSession()
    r = session.get('https://allegro.pl/listing?string=clocky&bmatch=baseline-product-cl-eyesa2-engag-dict45-nodict-ele-1-0-0717')
    r.html.render(timeout=20)

    article = r.html.find('a._9c44d_2vTdY')
    for i in article:
        title = i.text
        link = i.attrs['href']
        csv_writer.writerow([title, link])

    csv_file.close()
    session.close()

    return render(request, 'Fake/allegro.html')


def amazonScrap(file, uri):
    driver_set()

    csv_file = open(file, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Product', 'Link'])

    session = HTMLSession()
    r = session.get(uri)
    r.html.render()

    clockyAsin = ['B000PWLTNA', 'B084Z63RP4', 'B08CVQBZ4M', 'B006KLC1SW', 'B0013CTFQ4', 'B000TAS9XQ', 'B004MSMUGI', 'B005USCIZC', 'B009MQM2WW', 'B001989WIS', 'B0114174MK', 'B07DJ9XFMK']
    titles = ['Alarm Clock on Wheels', 'Alarm Clock Wheels', 'Runaway Alarm Clock', 'Run-Away', 'Running Alarm',
              'Clocky', 'Wheel Alarm Clock', 'Jumping Alarm Clock', 'Alarm Wheels', 'Run Alarm Clock', 'Moving',
              'Running', 'Flying', 'Rolling']

    article = r.html.find('div.s-asin')

    if uri == 'https://www.amazon.com/s?k=Clocky&ref=nb_sb_noss_2' or uri == 'https://www.amazon.co.uk/s?k=clocky&ref=nb_sb_noss_1' or uri == 'https://www.amazon.com.au/s?k=clocky&ref=nb_sb_noss_1':
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                for word in titles:
                    if word.lower() in title.lower():
                        link = asin.find('h2.a-size-mini', first=True).absolute_links
                        for li in link:
                            csv_writer.writerow([title, li])
                            break
                        break

    else:
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break


    csv_file.close()


    if uri == "https://www.amazon.es/s?k=clocky&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1":
        url = "https://www.amazon.es/s?k=reloj+despertador+fugitivo&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

        csv_file.close()

        uuu = "https://www.amazon.es/s?k=alarma+fugitivo&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

    elif uri == "https://www.amazon.it/s?k=clocky&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1":
        url = "https://www.amazon.it/s?k=sveglia+scappa&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

        csv_file.close()

        uuu = "https://www.amazon.it/s?k=orologio+ruote&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

    elif uri == "https://www.amazon.de/s?k=clocky&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1":
        url = "https://www.amazon.de/s?k=wecker+auf+radern&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

        csv_file.close()

        uuu = "https://www.amazon.de/s?k=Rollender+wecker&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

    elif uri == "https://www.amazon.fr/s?k=clocky&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1":
        url = "https://www.amazon.fr/s?k=reveil+sur+ruote&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

        csv_file.close()

        uuu = "https://www.amazon.fr/s?k=reveil+persecuci%C3%B3n&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

        csv_file.close()

        vvv = "https://www.amazon.fr/s?k=r%C3%A9veil+paresseux&page=2&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1601590112&ref=sr_pg_2"
        pp = session.get(vvv)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

        csv_file.close()

        xxx = "https://www.amazon.fr/s?k=r%C3%A9veil+paresseux&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
        pp = session.get(xxx)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break


    elif uri == "https://www.amazon.com.au/s?k=clocky&ref=nb_sb_noss_1":
        url = "https://www.amazon.com.au/s?k=wheel+alarm+clock&ref=nb_sb_noss"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                for word in titles:
                    if word.lower() in title.lower():
                        link = asin.find('h2.a-size-mini', first=True).absolute_links
                        for li in link:
                            csv_writer.writerow([title, li])
                            break
                        break

        csv_file.close()

        uuu = "https://www.amazon.com.au/s?k=jumping+alarm+clock&ref=nb_sb_noss"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                for word in titles:
                    if word.lower() in title.lower():
                        link = asin.find('h2.a-size-mini', first=True).absolute_links
                        for li in link:
                            csv_writer.writerow([title, li])
                            break
                        break

    elif uri == "https://www.amazon.nl/s?k=clocky&__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2":
        url = "https://www.amazon.nl/s?k=wheel+alarm+clock&__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

        csv_file.close()

        uuu = "https://www.amazon.nl/s?k=jumping+alarm+clock&__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

    elif uri == "https://www.amazon.ae/s?k=clocky&ref=nb_sb_noss":
        url = "https://www.amazon.ae/s?k=wheel+alarm+clock&ref=nb_sb_noss"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

        csv_file.close()

        uuu = "https://www.amazon.ae/s?k=jumping+alarm+clock&ref=nb_sb_noss"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

    elif uri == "https://www.amazon.com.mx/s?k=clocky&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2":
        url = "https://www.amazon.com.mx/s?k=wheel+alarm+clock&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

        csv_file.close()

        uuu = "https://www.amazon.com.mx/s?k=jumping+alarm+clock&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

    elif uri == "https://www.amazon.ca/s?k=clocky&ref=nb_sb_noss_2":
        url = "https://www.amazon.ca/s?k=wheel+alarm+clock&ref=nb_sb_noss_2"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

        csv_file.close()

        uuu = "https://www.amazon.ca/s?k=runaway+alarm+clock&page=2&crid=53391VO7005M&qid=1601588903&sprefix=runaway+%2Caps%2C162&ref=sr_pg_2"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

        csv_file.close()

        vvv = "https://www.amazon.ca/s?k=wheel+alarm+clock&page=2&qid=1601588770&ref=sr_pg_2"
        pp = session.get(vvv)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break


    elif uri == "https://www.amazon.co.jp/s?k=clocky&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss_1":
        url = "https://www.amazon.co.jp/s?k=wheel+alarm+clock&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

        csv_file.close()

        uuu = "https://www.amazon.co.jp/s?k=jumping+alarm+clock&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                link = asin.find('h2.a-size-mini', first=True).absolute_links
                for li in link:
                    csv_writer.writerow([title, li])
                    break

    elif uri == "https://www.amazon.co.uk/s?k=clocky&ref=nb_sb_noss_1":
        url = "https://www.amazon.co.uk/s?k=wheel+alarm+clock&ref=nb_sb_noss_2"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                for word in titles:
                    if word.lower() in title.lower():
                        link = asin.find('h2.a-size-mini', first=True).absolute_links
                        for li in link:
                            csv_writer.writerow([title, li])
                            break
                        break

        csv_file.close()

        uuu = "https://www.amazon.co.uk/s?k=jumping+alarm+clock&ref=nb_sb_noss_1"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                for word in titles:
                    if word.lower() in title.lower():
                        link = asin.find('h2.a-size-mini', first=True).absolute_links
                        for li in link:
                            csv_writer.writerow([title, li])
                            break
                        break

    else:
        url = "https://www.amazon.com/s?k=wheel+alarm+clock&ref=nb_sb_noss_1"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                for word in titles:
                    if word.lower() in title.lower():
                        link = asin.find('h2.a-size-mini', first=True).absolute_links
                        for li in link:
                            csv_writer.writerow([title, li])
                            break
                        break

        csv_file.close()

        uuu = "https://www.amazon.com/s?k=runaway+alarm+clock&page=2&qid=1600704110&ref=sr_pg_2"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                for word in titles:
                    if word.lower() in title.lower():
                        link = asin.find('h2.a-size-mini', first=True).absolute_links
                        for li in link:
                            csv_writer.writerow([title, li])
                            break
                        break

        csv_file.close()

        vvv = "https://www.amazon.com/s?k=runaway+alarm+clock&ref=nb_sb_noss"
        pp = session.get(vvv)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-asin')
        for asin in article:
            if asin.attrs['data-asin'] not in clockyAsin:
                title = asin.find('span.a-text-normal', first=True).text
                for word in titles:
                    if word.lower() in title.lower():
                        link = asin.find('h2.a-size-mini', first=True).absolute_links
                        for li in link:
                            csv_writer.writerow([title, li])
                            break
                        break


    csv_file.close()
    session.close()


def ebayScrap(file, uri):
    driver_set()

    csv_file = open(file, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Product', 'Link'])

    session = HTMLSession()
    r = session.get(uri)
    r.html.render()

    article = r.html.find('div.s-item__info')
    damn = ['£39.99', '£45.99', '$39.99', '$45.99', '39,99 EUR', '45,99 EUR', 'EUR 39,99', 'EUR 45,99', 'AU $39.99', 'AU $45.99']

    for i in article:
        title = i.find('h3.s-item__title', first=True).text
        price = i.find('span.s-item__price', first=True).text
        link = i.find('a.s-item__link', first=True).absolute_links
        if price in damn:
            continue
        for li in link:
            csv_writer.writerow([title, li])
            break

    csv_file.close()

    if uri == "https://www.ebay.es/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=clocky&_sacat=0":
        url = "https://www.ebay.es/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=alarma+fugitivo&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=clocky"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-item__info')
        for i in article:
            title = i.find('h3.s-item__title', first=True).text
            price = i.find('span.s-item__price', first=True).text
            link = i.find('a.s-item__link', first=True).absolute_links
            if price in damn:
                continue
            for li in link:
                csv_writer.writerow([title, li])
                break

        csv_file.close()

        uuu = "https://www.ebay.es/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=reloj+despertador+fugitivo&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=despertador+ruedas"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-item__info')
        for i in article:
            title = i.find('h3.s-item__title', first=True).text
            price = i.find('span.s-item__price', first=True).text
            link = i.find('a.s-item__link', first=True).absolute_links
            if price in damn:
                continue
            for li in link:
                csv_writer.writerow([title, li])
                break

    elif uri == "https://www.ebay.it/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=clocky&_sacat=0&LH_TitleDesc=0&_odkw=clock+alarm+clock&_osacat=0":
        url = "https://www.ebay.it/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=sveglia+con+le+ruote&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=sveglia+scappa"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-item__info')
        for i in article:
            title = i.find('h3.s-item__title', first=True).text
            price = i.find('span.s-item__price', first=True).text
            link = i.find('a.s-item__link', first=True).absolute_links
            if price in damn:
                continue
            for li in link:
                csv_writer.writerow([title, li])
                break

        csv_file.close()

        uuu = "https://www.ebay.it/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=sveglia+che+scappa&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=orologio+ruote"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-item__info')
        for i in article:
            title = i.find('h3.s-item__title', first=True).text
            price = i.find('span.s-item__price', first=True).text
            link = i.find('a.s-item__link', first=True).absolute_links
            if price in damn:
                continue
            for li in link:
                csv_writer.writerow([title, li])
                break

    elif uri == "https://www.ebay.de/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=clocky&_sacat=0":
        url = "https://www.ebay.de/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=wecker+auf+radern&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=clocky"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-item__info')
        for i in article:
            title = i.find('h3.s-item__title', first=True).text
            price = i.find('span.s-item__price', first=True).text
            link = i.find('a.s-item__link', first=True).absolute_links
            if price in damn:
                continue
            for li in link:
                csv_writer.writerow([title, li])
                break


    elif uri == "https://www.ebay.fr/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=clocky&_sacat=0":
        url = "https://www.ebay.fr/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=reveil+sur+ruote&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=clocky"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-item__info')
        for i in article:
            title = i.find('h3.s-item__title', first=True).text
            price = i.find('span.s-item__price', first=True).text
            link = i.find('a.s-item__link', first=True).absolute_links
            if price in damn:
                continue
            for li in link:
                csv_writer.writerow([title, li])
                break


    elif uri == "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=clocky&_sacat=0":
        url = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=wheel+alarm+clock&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=clocky"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-item__info')
        for i in article:
            title = i.find('h3.s-item__title', first=True).text
            price = i.find('span.s-item__price', first=True).text
            link = i.find('a.s-item__link', first=True).absolute_links
            if price in damn:
                continue
            for li in link:
                csv_writer.writerow([title, li])
                break

        csv_file.close()

        uuu = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=jumping+alarm+clock&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=wheel+alarm+clock"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-item__info')
        for i in article:
            title = i.find('h3.s-item__title', first=True).text
            price = i.find('span.s-item__price', first=True).text
            link = i.find('a.s-item__link', first=True).absolute_links
            if price in damn:
                continue
            for li in link:
                csv_writer.writerow([title, li])
                break

    else:
        url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=wheel+alarm+clock&_sacat=0"
        pp = session.get(url)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-item__info')
        for i in article:
            title = i.find('h3.s-item__title', first=True).text
            price = i.find('span.s-item__price', first=True).text
            link = i.find('a.s-item__link', first=True).absolute_links
            if price in damn:
                continue
            for li in link:
                csv_writer.writerow([title, li])
                break

        csv_file.close()

        uuu = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=jumping+alarm+clock&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=wheel+alarm+clock"
        pp = session.get(uuu)
        pp.html.render()

        csv_file = open(file, 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)

        article = pp.html.find('div.s-item__info')
        for i in article:
            title = i.find('h3.s-item__title', first=True).text
            price = i.find('span.s-item__price', first=True).text
            link = i.find('a.s-item__link', first=True).absolute_links
            if price in damn:
                continue
            for li in link:
                csv_writer.writerow([title, li])
                break

    csv_file.close()
    session.close()


def ebayUS(request):
    result = finders.find('Fake/log/ebayUS.csv')
    url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=clocky&_sacat=0"
    ebayScrap(result, url)

    return render(request, 'Fake/ebayUS.html')


def ebayUK(request):
    result = finders.find('Fake/log/ebayUK.csv')
    url = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=clocky&_sacat=0"
    ebayScrap(result, url)

    return render(request, 'Fake/ebayUK.html')


def ebayDE(request):
    result = finders.find('Fake/log/ebayDE.csv')
    url = "https://www.ebay.de/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=clocky&_sacat=0"
    ebayScrap(result, url)

    return render(request, 'Fake/ebayDE.html')


def ebayFR(request):
    result = finders.find('Fake/log/ebayFR.csv')
    url = "https://www.ebay.fr/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=clocky&_sacat=0"
    ebayScrap(result, url)

    return render(request, 'Fake/ebayFR.html')


def ebayES(request):
    result = finders.find('Fake/log/ebayES.csv')
    url = "https://www.ebay.es/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=clocky&_sacat=0"
    ebayScrap(result, url)

    return render(request, 'Fake/ebayES.html')


def ebayAU(request):
    result = finders.find('Fake/log/ebayAU.csv')
    url = "https://www.amazon.com.au/s?k=clocky+alarm+clock&ref=nb_sb_noss_2"
    ebayScrap(result, url)

    return render(request, 'Fake/ebayAU.html')


def ebayIT(request):
    result = finders.find('Fake/log/ebayIT.csv')
    url = "https://www.ebay.it/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=clocky&_sacat=0&LH_TitleDesc=0&_odkw=clock+alarm+clock&_osacat=0"
    ebayScrap(result, url)

    return render(request, 'Fake/ebayIT.html')


def amazonUS(request):
    result = finders.find('Fake/log/amazonUS.csv')
    url = "https://www.amazon.com/s?k=Clocky&ref=nb_sb_noss_2"
    amazonScrap(result, url)

    return render(request, 'Fake/amazonUS.html')


def amazonUK(request):
    result = finders.find('Fake/log/amazonUK.csv')
    url = "https://www.amazon.co.uk/s?k=clocky&ref=nb_sb_noss_1"
    amazonScrap(result, url)

    return render(request, 'Fake/amazonUK.html')


def amazonMX(request):
    result = finders.find('Fake/log/amazonMX.csv')
    url = "https://www.amazon.com.mx/s?k=clocky&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2"
    amazonScrap(result, url)

    return render(request, 'Fake/amazonMX.html')


def amazonAU(request):
    result = finders.find('Fake/log/amazonAU.csv')
    url = "https://www.amazon.com.au/s?k=clocky&ref=nb_sb_noss_1"
    amazonScrap(result, url)

    return render(request, 'Fake/amazonAU.html')


def amazonES(request):
    result = finders.find('Fake/log/amazonES.csv')
    url = "https://www.amazon.es/s?k=clocky&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
    amazonScrap(result, url)

    return render(request, 'Fake/amazonES.html')


def amazonIT(request):
    result = finders.find('Fake/log/amazonIT.csv')
    url = "https://www.amazon.it/s?k=clocky&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
    amazonScrap(result, url)

    return render(request, 'Fake/amazonIT.html')


def amazonAE(request):
    result = finders.find('Fake/log/amazonUAE.csv')
    url = "https://www.amazon.ae/s?k=clocky&ref=nb_sb_noss"
    amazonScrap(result, url)

    return render(request, 'Fake/amazonAE.html')


def amazonFR(request):
    result = finders.find('Fake/log/amazonFR.csv')
    url = "https://www.amazon.fr/s?k=clocky&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
    amazonScrap(result, url)

    return render(request, 'Fake/amazonFR.html')


def amazonCA(request):
    result = finders.find('Fake/log/amazonCA.csv')
    url = "https://www.amazon.ca/s?k=clocky&ref=nb_sb_noss_2"
    amazonScrap(result, url)

    return render(request, 'Fake/amazonCA.html')


def amazonJP(request):
    result = finders.find('Fake/log/amazonJP.csv')
    url = "https://www.amazon.co.jp/s?k=clocky&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss_1"
    amazonScrap(result, url)

    return render(request, 'Fake/amazonJP.html')


def amazonNL(request):
    result = finders.find('Fake/log/amazonNL.csv')
    url = "https://www.amazon.nl/s?k=clocky&__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2"
    amazonScrap(result, url)

    return render(request, 'Fake/amazonNL.html')


def amazonDE(request):
    result = finders.find('Fake/log/amazonDE.csv')
    url = "https://www.amazon.de/s?k=clocky&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
    amazonScrap(result, url)

    return render(request, 'Fake/amazonDE.html')

