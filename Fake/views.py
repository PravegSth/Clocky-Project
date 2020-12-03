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


def bol(request):
    driver_set()

    def yes(uri, mode):
        file = finders.find('Fake/log/bol.csv')
        csv_file = open(file, mode)
        csv_writer = csv.writer(csv_file)
        if mode == 'w':
            csv_writer.writerow(['Product', 'Link'])

        session = HTMLSession()
        r = session.get(uri)
        r.html.render(timeout=20)

        article = r.html.find('a.product-title')
        for i in article:
            title = i.text
            link = i.absolute_links
            for li in link:
                csv_writer.writerow([title, li])

        csv_file.close()
        session.close()

    yes('https://www.bol.com/nl/s/?searchtext=Digitale+Rijdende+Wekker&searchContext=media_all&appliedSearchContextId=media_all&suggestFragment=&adjustedSection=&originalSection=&originalSearchContext=&section=main&N=0&defaultSearchContext=media_all', 'w')
    yes('https://www.bol.com/nl/s/?searchtext=Rollende+Wekker&searchContext=media_all&appliedSearchContextId=media_all&suggestFragment=&adjustedSection=&originalSection=&originalSearchContext=&section=main&N=0&defaultSearchContext=media_all', 'a')
    yes('https://www.bol.com/nl/s/?searchtext=Digitale+Rollende+Wekker+met+Sluimerfunctie&searchContext=media_all&appliedSearchContextId=media_all&suggestFragment=&adjustedSection=&originalSection=&originalSearchContext=&section=main&N=0&defaultSearchContext=media_all', 'a')

    return render(request, 'Fake/bol.html')


def jpyahoo(request):
    driver_set()

    def yes(uri, mode):
        file = finders.find('Fake/log/JapanYahoo.csv')
        csv_file = open(file, mode, encoding="utf-8")
        csv_writer = csv.writer(csv_file)
        if mode == 'w':
            csv_writer.writerow(['Product', 'Link'])

        session = HTMLSession()
        r = session.get(uri)
        r.html.render(timeout=20)

        article = r.html.find('li.product_whole')
        for i in article:
            aa = i.find('a', first=True)
            link = aa.absolute_links
            pp = i.find('p', first=True)
            title = pp.text
            for li in link:
                csv_writer.writerow([title, li])

        csv_file.close()
        session.close()

    yes('https://buyee.jp/item/search/yahoo/shopping?query=clocky', 'w')
    yes('https://buyee.jp/item/search/yahoo/shopping?query=alarm%20clock%20on%20wheels&searchHis=1', 'a')

    return render(request, 'Fake/JapanYahoo.html')


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


def amazonUSADefault(file, uri, mode):
    csv_file = open(file, mode)
    csv_writer = csv.writer(csv_file)
    if mode == 'w':
        csv_writer.writerow(['Product', 'Link'])

    session = HTMLSession()
    r = session.get(uri)
    r.html.render()

    clockyAsin = ['B000PWLTNA', 'B084Z63RP4', 'B08CVQBZ4M', 'B006KLC1SW', 'B0013CTFQ4', 'B000TAS9XQ', 'B004MSMUGI',
                  'B005USCIZC', 'B009MQM2WW', 'B001989WIS', 'B0114174MK', 'B07DJ9XFMK']

    article = r.html.find('div.s-asin')

    for asin in article:
        if asin.attrs['data-asin'] not in clockyAsin:
            title = asin.find('span.a-text-normal', first=True).text
            link = asin.find('h2.a-size-mini', first=True).absolute_links
            for li in link:
                csv_writer.writerow([title, li])
                break

    csv_file.close()
    session.close()

def amazonScrap(file, uri):
    driver_set()

    csv_file = open(file, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Product', 'Link'])

    session = HTMLSession()
    r = session.get(uri)
    r.html.render()

    clockyAsin = ['B000PWLTNA', 'B084Z63RP4', 'B08CVQBZ4M', 'B006KLC1SW', 'B0013CTFQ4', 'B000TAS9XQ', 'B004MSMUGI',
                  'B005USCIZC', 'B009MQM2WW', 'B001989WIS', 'B0114174MK', 'B07DJ9XFMK']
    titles = ['Alarm Clock on Wheels', 'Alarm Clock Wheels', 'Runaway Alarm Clock', 'Run-Away', 'Running Alarm',
              'Clocky', 'Wheel Alarm Clock', 'Jumping Alarm Clock', 'Alarm Wheels', 'Run Alarm Clock', 'Moving',
              'Running', 'Flying', 'Rolling', 'Wake Up', 'Creative']

    article = r.html.find('div.s-asin')

    if uri == 'https://www.amazon.com/s?k=clocky&ref=nb_sb_noss' or uri == 'https://www.amazon.co.uk/s?k=clocky&ref=nb_sb_noss_1' or uri == 'https://www.amazon.com.au/s?k=clocky&ref=nb_sb_noss_1':
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

    if uri == "https://www.amazon.com.au/s?k=clocky&ref=nb_sb_noss_1":
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

    else:
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


def clockyKey(request):
    driver_set()
    result = finders.find('Fake/log/clocky.csv')
    url = "https://www.amazon.com/s?k=clocky&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=clocky&page=2&qid=1602716537&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'clockyKey'})


def ALOW(request):
    driver_set()
    result = finders.find('Fake/log/Alarm_Clock_On_Wheels.csv')
    url = "https://www.amazon.com/s?k=alarm+clock+on+wheels&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=alarm+clock+on+wheels&page=2&qid=1602718020&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=alarm+clock+on+wheels&page=3&qid=1602718044&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=alarm+clock+on+wheels&page=4&qid=1602718095&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'ALOW'})


def ALOW2(request):
    driver_set()
    result = finders.find('Fake/log/Alarm_Clock_On_Wheels2.csv')
    url = "https://www.amazon.com/s?k=alarm+clock+on+wheels&page=5&qid=1602718115&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=alarm+clock+on+wheels&page=6&qid=1602718133&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=alarm+clock+on+wheels&page=7&qid=1602718156&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'ALOW2'})


def RAC(request):
    driver_set()
    result = finders.find('Fake/log/Running_Alarm_Clock.csv')
    url = "https://www.amazon.com/s?k=running+alarm+clock&ref=nb_sb_noss_2"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=running+alarm+clock&page=2&qid=1602719811&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=running+alarm+clock&page=3&qid=1602720011&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=running+alarm+clock&page=4&qid=1602720031&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'RAC'})


def RAC2(request):
    driver_set()
    result = finders.find('Fake/log/Running_Alarm_Clock2.csv')
    url = "https://www.amazon.com/s?k=running+alarm+clock&page=5&qid=1602720046&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=running+alarm+clock&page=6&qid=1602720060&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=running+alarm+clock&page=7&qid=1602720086&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'RAC2'})


def CAC(request):
    driver_set()
    result = finders.find('Fake/log/Creative_Alarm_Clock.csv')
    url = "https://www.amazon.com/s?k=creative+alarm+clock&crid=377SNYSBJLBKR&sprefix=creative+alarm+c%2Caps%2C183&ref=nb_sb_ss_i_1_16"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=creative+alarm+clock&page=2&crid=377SNYSBJLBKR&qid=1602720364&sprefix=creative+alarm+c%2Caps%2C183&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=creative+alarm+clock&page=3&crid=377SNYSBJLBKR&qid=1602720411&sprefix=creative+alarm+c%2Caps%2C183&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=creative+alarm+clock&page=4&crid=377SNYSBJLBKR&qid=1602720428&sprefix=creative+alarm+c%2Caps%2C183&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'CAC'})


def CAC2(request):
    driver_set()
    result = finders.find('Fake/log/Creative_Alarm_Clock2.csv')
    url = "https://www.amazon.com/s?k=creative+alarm+clock&page=5&crid=377SNYSBJLBKR&qid=1602720443&sprefix=creative+alarm+c%2Caps%2C183&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=creative+alarm+clock&page=6&crid=377SNYSBJLBKR&qid=1602720460&sprefix=creative+alarm+c%2Caps%2C183&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=creative+alarm+clock&page=7&crid=377SNYSBJLBKR&qid=1602720478&sprefix=creative+alarm+c%2Caps%2C183&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'CAC2'})


def RunAC(request):
    driver_set()
    result = finders.find('Fake/log/Runaway_Alarm_Clock.csv')
    url = "https://www.amazon.com/s?k=runaway+alarm+clock&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=runaway+alarm+clock&page=2&qid=1602720701&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=runaway+alarm+clock&page=3&qid=1602720727&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=runaway+alarm+clock&page=4&qid=1602720798&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'RunAC'})


def RunAC2(request):
    driver_set()
    result = finders.find('Fake/log/Runaway_Alarm_Clock2.csv')
    url = "https://www.amazon.com/s?k=runaway+alarm+clock&page=5&qid=1602720812&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=runaway+alarm+clock&page=6&qid=1602720826&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=runaway+alarm+clock&page=7&qid=1602720839&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'RunAC2'})


def EAC(request):
    driver_set()
    result = finders.find('Fake/log/Escape_Alarm_Clock.csv')
    url = "https://www.amazon.com/s?k=escape+alarm+clock&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=escape+alarm+clock&page=2&qid=1602721077&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=escape+alarm+clock&page=3&qid=1602721103&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=escape+alarm+clock&page=4&qid=1602721118&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'EAC'})


def EAC2(request):
    driver_set()
    result = finders.find('Fake/log/Escape_Alarm_Clock2.csv')
    url = "https://www.amazon.com/s?k=escape+alarm+clock&page=5&qid=1602721231&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=escape+alarm+clock&page=6&qid=1602721250&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=escape+alarm+clock&page=7&qid=1602721265&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'EAC2'})


def WAC(request):
    driver_set()
    result = finders.find('Fake/log/Wheel_Alarm_Clock.csv')
    url = "https://www.amazon.com/s?k=wheel+alarm+clock&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=wheel+alarm+clock&page=2&qid=1602721491&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=wheel+alarm+clock&page=3&qid=1602721507&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=wheel+alarm+clock&page=4&qid=1602721533&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'WAC'})


def WAC2(request):
    driver_set()
    result = finders.find('Fake/log/Wheel_Alarm_Clock2.csv')
    url = "https://www.amazon.com/s?k=wheel+alarm+clock&page=5&qid=1602721548&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=wheel+alarm+clock&page=6&qid=1602721567&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=wheel+alarm+clock&page=7&qid=1602721582&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'WAC2'})


def JAC(request):
    driver_set()
    result = finders.find('Fake/log/Jumping_Alarm_Clock.csv')
    url = "https://www.amazon.com/s?k=jumping+alarm+clock&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=jumping+alarm+clock&page=2&qid=1602721756&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=jumping+alarm+clock&page=3&qid=1602721773&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=jumping+alarm+clock&page=4&qid=1602721785&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'JAC'})


def JAC2(request):
    driver_set()
    result = finders.find('Fake/log/Jumping_Alarm_Clock2.csv')
    url = "https://www.amazon.com/s?k=jumping+alarm+clock&page=5&qid=1602721809&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=jumping+alarm+clock&page=6&qid=1602721832&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=jumping+alarm+clock&page=7&qid=1602721847&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'JAC2'})


def AW(request):
    driver_set()
    result = finders.find('Fake/log/Alarm_Wheels.csv')
    url = "https://www.amazon.com/s?k=alarm+wheels&crid=1RLBQ10RNZ5RP&sprefix=alarm+wheels%2Caps%2C172&ref=nb_sb_ss_i_1_12"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=alarm+wheels&page=2&crid=1RLBQ10RNZ5RP&qid=1602722090&sprefix=alarm+wheels%2Caps%2C172&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=alarm+wheels&page=3&crid=1RLBQ10RNZ5RP&qid=1602722120&sprefix=alarm+wheels%2Caps%2C172&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=alarm+wheels&page=4&crid=1RLBQ10RNZ5RP&qid=1602722134&sprefix=alarm+wheels%2Caps%2C172&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'AW'})


def AW2(request):
    driver_set()
    result = finders.find('Fake/log/Alarm_Wheels2.csv')
    url = "https://www.amazon.com/s?k=alarm+wheels&page=5&crid=1RLBQ10RNZ5RP&qid=1602722148&sprefix=alarm+wheels%2Caps%2C172&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=alarm+wheels&page=6&crid=1RLBQ10RNZ5RP&qid=1602722161&sprefix=alarm+wheels%2Caps%2C172&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=alarm+wheels&page=7&crid=1RLBQ10RNZ5RP&qid=1602722174&sprefix=alarm+wheels%2Caps%2C172&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'AW2'})


def MAC(request):
    driver_set()
    result = finders.find('Fake/log/Moving_Alarm_Clock.csv')
    url = "https://www.amazon.com/s?k=moving+alarm+clock&crid=FZ0N5B2H2BU5&sprefix=moving+ala%2Caps%2C153&ref=nb_sb_ss_i_1_10"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=moving+alarm+clock&page=2&crid=FZ0N5B2H2BU5&qid=1602722414&sprefix=moving+ala%2Caps%2C153&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=moving+alarm+clock&page=3&crid=FZ0N5B2H2BU5&qid=1602722423&sprefix=moving+ala%2Caps%2C153&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=moving+alarm+clock&page=4&crid=FZ0N5B2H2BU5&qid=1602722436&sprefix=moving+ala%2Caps%2C153&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'MAC'})


def MAC2(request):
    driver_set()
    result = finders.find('Fake/log/Moving_Alarm_Clock2.csv')
    url = "https://www.amazon.com/s?k=moving+alarm+clock&page=5&crid=FZ0N5B2H2BU5&qid=1602722450&sprefix=moving+ala%2Caps%2C153&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=moving+alarm+clock&page=6&crid=FZ0N5B2H2BU5&qid=1602722462&sprefix=moving+ala%2Caps%2C153&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=moving+alarm+clock&page=7&crid=FZ0N5B2H2BU5&qid=1602722474&sprefix=moving+ala%2Caps%2C153&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'MAC2'})


def RRAC(request):
    driver_set()
    result = finders.find('Fake/log/Run_Alarm_Clock.csv')
    url = "https://www.amazon.com/s?k=run+alarm+clock&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=run+alarm+clock&page=2&qid=1602722640&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=run+alarm+clock&page=3&qid=1602722657&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=run+alarm+clock&page=4&qid=1602722671&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'RRAC'})


def RRAC2(request):
    driver_set()
    result = finders.find('Fake/log/Run_Alarm_Clock2.csv')
    url = "https://www.amazon.com/s?k=run+alarm+clock&page=5&qid=1602722683&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.com/s?k=run+alarm+clock&page=6&qid=1602722696&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.com/s?k=run+alarm+clock&page=7&qid=1602722709&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'RRAC2'})


def ES1(request):
    driver_set()
    result = finders.find('Fake/log/alarma_fugitivo.csv')
    url = "https://www.amazon.es/s?k=alarma+fugitivo&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')

    return render(request, 'Fake/amazonOnly.html', {'page': 'ES1'})


def ES2(request):
    driver_set()
    result = finders.find('Fake/log/despertador_sobre_ruedas.csv')
    url = "https://www.amazon.es/s?k=despertador+sobre+ruedas&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')

    return render(request, 'Fake/amazonOnly.html', {'page': 'ES2'})


def ES3(request):
    driver_set()
    result = finders.find('Fake/log/reloj_despertador_fugitivo.csv')
    url = "https://www.amazon.es/s?k=reloj+despertador+fugitivo&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')

    return render(request, 'Fake/amazonOnly.html', {'page': 'ES3'})


def ES4(request):
    driver_set()
    result = finders.find('Fake/log/clockySpain.csv')
    url = "https://www.amazon.es/s?k=clocky&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.es/s?k=clocky&page=2&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603134648&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.es/s?k=clocky&page=3&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603134656&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'ES4'})


def ES51(request):
    driver_set()
    result = finders.find('Fake/log/depertador_creativo1.csv')
    url = "https://www.amazon.es/s?k=depertador+creativo&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.es/s?k=despertador+creativo&page=2&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603134700&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.es/s?k=despertador+creativo&page=3&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603134717&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.es/s?k=despertador+creativo&page=4&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603134731&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'ES51'})


def ES52(request):
    driver_set()
    result = finders.find('Fake/log/depertador_creativo2.csv')
    url = "https://www.amazon.es/s?k=despertador+creativo&page=5&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603134757&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.es/s?k=despertador+creativo&page=6&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603134777&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.es/s?k=despertador+creativo&page=7&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603134789&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'ES52'})


def ES6(request):
    driver_set()
    result = finders.find('Fake/log/despertador_ruedas.csv')
    url = "https://www.amazon.es/s?k=despertador+ruedas&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.es/s?k=despertador+ruedas&page=2&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603134834&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.es/s?k=despertador+ruedas&page=3&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603134855&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'ES6'})


def IT11(request):
    driver_set()
    result = finders.find('Fake/log/sveglia_scappa1.csv')
    url = "https://www.amazon.it/s?k=sveglia+scappa&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.it/s?k=sveglia+scappa&page=2&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209439&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=sveglia+scappa&page=3&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209461&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=sveglia+scappa&page=4&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209476&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'IT11'})


def IT12(request):
    driver_set()
    result = finders.find('Fake/log/sveglia_scappa2.csv')
    url = "https://www.amazon.it/s?k=sveglia+scappa&page=5&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209491&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.it/s?k=sveglia+scappa&page=6&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209509&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=sveglia+scappa&page=7&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209523&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'IT12'})


def IT21(request):
    driver_set()
    result = finders.find('Fake/log/sveglia_con_le_ruote1.csv')
    url = "https://www.amazon.it/s?k=sveglia+con+le+ruote&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.it/s?k=sveglia+con+le+ruote&page=2&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209809&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=sveglia+con+le+ruote&page=3&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209842&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=sveglia+con+le+ruote&page=4&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209862&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'IT21'})


def IT22(request):
    driver_set()
    result = finders.find('Fake/log/sveglia_con_le_ruote2.csv')
    url = "https://www.amazon.it/s?k=sveglia+con+le+ruote&page=5&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209876&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.it/s?k=sveglia+con+le+ruote&page=6&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209892&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=sveglia+con+le+ruote&page=7&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209909&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'IT22'})


def IT31(request):
    driver_set()
    result = finders.find('Fake/log/orologio_ruote1.csv')
    url = "https://www.amazon.it/s?k=orologio+ruote&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.it/s?k=orologio+ruote&page=2&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209951&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=orologio+ruote&page=3&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209971&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=orologio+ruote&page=4&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603209989&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'IT31'})


def IT32(request):
    driver_set()
    result = finders.find('Fake/log/orologio_ruote2.csv')
    url = "https://www.amazon.it/s?k=orologio+ruote&page=5&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210001&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.it/s?k=orologio+ruote&page=6&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210018&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=orologio+ruote&page=7&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210236&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'IT32'})


def IT41(request):
    driver_set()
    result = finders.find('Fake/log/clockyIT1.csv')
    url = "https://www.amazon.it/s?k=clocky&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.it/s?k=clocky&page=2&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210288&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=clocky&page=3&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210302&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=clocky&page=4&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210318&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'IT41'})


def IT42(request):
    driver_set()
    result = finders.find('Fake/log/clockyIT2.csv')
    url = "https://www.amazon.it/s?k=clocky&page=5&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210331&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.it/s?k=clocky&page=6&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210367&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=clocky&page=7&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210384&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'IT42'})


def IT51(request):
    driver_set()
    result = finders.find('Fake/log/sveglia_ruote1.csv')
    url = "https://www.amazon.it/s?k=sveglia+ruote&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.it/s?k=sveglia+ruote&page=2&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210417&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=sveglia+ruote&page=3&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210434&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=sveglia+ruote&page=4&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210446&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'IT51'})


def IT52(request):
    driver_set()
    result = finders.find('Fake/log/sveglia_ruote2.csv')
    url = "https://www.amazon.it/s?k=sveglia+ruote&page=5&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210459&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.it/s?k=sveglia+ruote&page=6&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210473&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=sveglia+ruote&page=7&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210486&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'IT52'})


def IT61(request):
    driver_set()
    result = finders.find('Fake/log/sveglia_che_scappa1.csv')
    url = "https://www.amazon.it/s?k=sveglia+che+scappa&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.it/s?k=sveglia+che+scappa&page=2&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210521&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=sveglia+che+scappa&page=3&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210539&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=sveglia+che+scappa&page=4&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210560&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'IT61'})


def IT62(request):
    driver_set()
    result = finders.find('Fake/log/sveglia_che_scappa2.csv')
    url = "https://www.amazon.it/s?k=sveglia+che+scappa&page=5&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210571&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.it/s?k=sveglia+che+scappa&page=6&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210590&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.it/s?k=sveglia+che+scappa&page=7&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603210603&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'IT62'})


def FR11(request):
    driver_set()
    result = finders.find('Fake/log/reveil_sur_ruote1.csv')
    url = "https://www.amazon.fr/s?k=reveil+sur+ruote&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.fr/s?k=reveil+sur+route&page=2&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603213327&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.fr/s?k=reveil+sur+route&page=3&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603213345&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.fr/s?k=reveil+sur+route&page=4&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603213359&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'FR11'})


def FR12(request):
    driver_set()
    result = finders.find('Fake/log/reveil_sur_ruote2.csv')
    url = "https://www.amazon.fr/s?k=reveil+sur+route&page=5&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603213372&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.fr/s?k=reveil+sur+route&page=6&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603213388&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.fr/s?k=reveil+sur+route&page=7&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603213403&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'FR12'})


def FR21(request):
    driver_set()
    result = finders.find('Fake/log/reveil_persecucion1.csv')
    url = "https://www.amazon.fr/s?k=reveil+persecuci%C3%B3n&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')

    return render(request, 'Fake/amazonOnly.html', {'page': 'FR21'})


def FR31(request):
    driver_set()
    result = finders.find('Fake/log/reveil_ruotes1.csv')
    url = "https://www.amazon.fr/s?k=reveil+ruote&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')

    return render(request, 'Fake/amazonOnly.html', {'page': 'FR31'})


def FR41(request):
    driver_set()
    result = finders.find('Fake/log/clockyFR1.csv')
    url = "https://www.amazon.fr/s?k=clocky&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.fr/s?k=clocky&page=2&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603213636&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.fr/s?k=clocky&page=3&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603213659&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.fr/s?k=clocky&page=4&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603213672&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'FR41'})


def FR51(request):
    driver_set()
    result = finders.find('Fake/log/reveil_creatif_ruote1.csv')
    url = "https://www.amazon.fr/s?k=reveil+creatif+ruote&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')

    return render(request, 'Fake/amazonOnly.html', {'page': 'FR51'})


def FR61(request):
    driver_set()
    result = finders.find('Fake/log/reveil_fugitif1.csv')
    url = "https://www.amazon.fr/s?k=reveil+fugitif&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')

    return render(request, 'Fake/amazonOnly.html', {'page': 'FR61'})


def DE11(request):
    driver_set()
    result = finders.find('Fake/log/wecker_auf_radern_1.csv')
    url = "https://www.amazon.de/s?k=wecker+auf+radern&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.de/s?k=wecker+auf+r%C3%A4dern&page=2&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725344&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=wecker+auf+r%C3%A4dern&page=3&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725371&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=wecker+auf+r%C3%A4dern&page=4&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725387&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'DE11'})


def DE12(request):
    driver_set()
    result = finders.find('Fake/log/wecker_auf_radern_2.csv')
    url = "https://www.amazon.de/s?k=wecker+auf+r%C3%A4dern&page=5&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725405&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.de/s?k=wecker+auf+r%C3%A4dern&page=6&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725424&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=wecker+auf+r%C3%A4dern&page=7&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725478&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'DE12'})


def DE21(request):
    driver_set()
    result = finders.find('Fake/log/wecker_radern1.csv')
    url = "https://www.amazon.de/s?k=wecker+radern&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.de/s?k=wecker+radern&page=2&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725515&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=wecker+radern&page=3&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725534&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=wecker+radern&page=4&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725551&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'DE21'})


def DE22(request):
    driver_set()
    result = finders.find('Fake/log/wecker_radern2.csv')
    url = "https://www.amazon.de/s?k=wecker+radern&page=5&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725569&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.de/s?k=wecker+radern&page=6&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725586&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=wecker+radern&page=7&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725605&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'DE22'})


def DE31(request):
    driver_set()
    result = finders.find('Fake/log/wecker_weglaufender1.csv')
    url = "https://www.amazon.de/s?k=wecker+weglaufender&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.de/s?k=wecker+weglaufender&page=2&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725657&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=wecker+weglaufender&page=3&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725675&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=wecker+weglaufender&page=4&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725691&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'DE31'})


def DE32(request):
    driver_set()
    result = finders.find('Fake/log/wecker_weglaufender2.csv')
    url = "https://www.amazon.de/s?k=wecker+weglaufender&page=5&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725705&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.de/s?k=wecker+weglaufender&page=6&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725722&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=wecker+weglaufender&page=7&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725741&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'DE32'})


def DE41(request):
    driver_set()
    result = finders.find('Fake/log/clockyDE1.csv')
    url = "https://www.amazon.de/s?k=clocky&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.de/s?k=clocky&page=2&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725778&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=clocky&page=3&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725826&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=clocky&page=4&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725831&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'DE41'})


def DE51(request):
    driver_set()
    result = finders.find('Fake/log/wecker_clocky1.csv')
    url = "https://www.amazon.de/s?k=wecker+clocky&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.de/s?k=wecker+clocky&page=2&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725940&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=wecker+clocky&page=3&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725961&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=wecker+clocky&page=4&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603725975&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'DE51'})


def DE61(request):
    driver_set()
    result = finders.find('Fake/log/rollender_wecker1.csv')
    url = "https://www.amazon.de/s?k=rollender+wecker&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.de/s?k=rollender+wecker&page=2&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603726053&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=rollender+wecker&page=3&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603726069&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=rollender+wecker&page=4&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603726084&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'DE61'})


def DE62(request):
    driver_set()
    result = finders.find('Fake/log/rollender_wecker2.csv')
    url = "https://www.amazon.de/s?k=rollender+wecker&page=5&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603726098&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.de/s?k=rollender+wecker&page=6&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603726150&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.de/s?k=rollender+wecker&page=7&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1603726163&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'DE62'})


def clockyKeyCA(request):
    driver_set()
    result = finders.find('Fake/log/clockyCA.csv')
    url = "https://www.amazon.ca/s?k=clocky&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')

    return render(request, 'Fake/amazonOnly.html', {'page': 'clockyKeyCA'})


def ALOWCA(request):
    driver_set()
    result = finders.find('Fake/log/Alarm_Clock_On_WheelsCA.csv')
    url = "https://www.amazon.ca/s?k=alarm+clock+on+wheels&crid=8XIMGPNNY1SI&sprefix=alarm+clock+on+wheels%2Caps%2C149&ref=nb_sb_ss_i_1_21"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=alarm+clock+on+wheels&page=2&crid=8XIMGPNNY1SI&qid=1603735282&sprefix=alarm+clock+on+wheels%2Caps%2C149&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=alarm+clock+on+wheels&page=3&crid=8XIMGPNNY1SI&qid=1603735298&sprefix=alarm+clock+on+wheels%2Caps%2C149&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=alarm+clock+on+wheels&page=4&crid=8XIMGPNNY1SI&qid=1603735313&sprefix=alarm+clock+on+wheels%2Caps%2C149&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'ALOWCA'})


def ALOW2CA(request):
    driver_set()
    result = finders.find('Fake/log/Alarm_Clock_On_Wheels2CA.csv')
    url = "https://www.amazon.ca/s?k=alarm+clock+on+wheels&page=5&crid=8XIMGPNNY1SI&qid=1603735327&sprefix=alarm+clock+on+wheels%2Caps%2C149&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=alarm+clock+on+wheels&page=6&crid=8XIMGPNNY1SI&qid=1603735342&sprefix=alarm+clock+on+wheels%2Caps%2C149&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=alarm+clock+on+wheels&page=7&crid=8XIMGPNNY1SI&qid=1603735359&sprefix=alarm+clock+on+wheels%2Caps%2C149&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'ALOW2CA'})


def RACCA(request):
    driver_set()
    result = finders.find('Fake/log/Running_Alarm_ClockCA.csv')
    url = "https://www.amazon.ca/s?k=running+alarm+clock&crid=3EOR89P0R5FK0&sprefix=running+alarm+%2Caps%2C165&ref=nb_sb_ss_i_1_14"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=running+alarm+clock&page=2&crid=3EOR89P0R5FK0&qid=1603735393&sprefix=running+alarm+%2Caps%2C165&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=running+alarm+clock&page=3&crid=3EOR89P0R5FK0&qid=1603735408&sprefix=running+alarm+%2Caps%2C165&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=running+alarm+clock&page=4&crid=3EOR89P0R5FK0&qid=1603735420&sprefix=running+alarm+%2Caps%2C165&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'RACCA'})


def RAC2CA(request):
    driver_set()
    result = finders.find('Fake/log/Running_Alarm_Clock2CA.csv')
    url = "https://www.amazon.ca/s?k=running+alarm+clock&page=5&crid=3EOR89P0R5FK0&qid=1603735432&sprefix=running+alarm+%2Caps%2C165&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=running+alarm+clock&page=6&crid=3EOR89P0R5FK0&qid=1603735452&sprefix=running+alarm+%2Caps%2C165&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=running+alarm+clock&page=7&crid=3EOR89P0R5FK0&qid=1603735464&sprefix=running+alarm+%2Caps%2C165&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'RAC2CA'})


def CACCA(request):
    driver_set()
    result = finders.find('Fake/log/Creative_Alarm_ClockCA.csv')
    url = "https://www.amazon.ca/s?k=creative+alarm+clock&crid=32SRZ7GQJPN2&sprefix=creative+alarm+clock%2Caps%2C140&ref=nb_sb_ss_i_1_20"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=creative+alarm+clock&page=2&crid=32SRZ7GQJPN2&qid=1603735499&sprefix=creative+alarm+clock%2Caps%2C140&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=creative+alarm+clock&page=3&crid=32SRZ7GQJPN2&qid=1603735524&sprefix=creative+alarm+clock%2Caps%2C140&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=creative+alarm+clock&page=4&crid=32SRZ7GQJPN2&qid=1603735537&sprefix=creative+alarm+clock%2Caps%2C140&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'CACCA'})


def CAC2CA(request):
    driver_set()
    result = finders.find('Fake/log/Creative_Alarm_Clock2CA.csv')
    url = "https://www.amazon.ca/s?k=creative+alarm+clock&page=5&crid=32SRZ7GQJPN2&qid=1603735549&sprefix=creative+alarm+clock%2Caps%2C140&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=creative+alarm+clock&page=6&crid=32SRZ7GQJPN2&qid=1603735567&sprefix=creative+alarm+clock%2Caps%2C140&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=creative+alarm+clock&page=7&crid=32SRZ7GQJPN2&qid=1603735580&sprefix=creative+alarm+clock%2Caps%2C140&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'CAC2CA'})


def RunACCA(request):
    driver_set()
    result = finders.find('Fake/log/Runaway_Alarm_ClockCA.csv')
    url = "https://www.amazon.ca/s?k=runaway+alarm+clock&crid=2QM773QX6L040&sprefix=runaway+alarm+clock%2Caps%2C148&ref=nb_sb_ss_i_1_19"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=runaway+alarm+clock&page=2&crid=2QM773QX6L040&qid=1603735619&sprefix=runaway+alarm+clock%2Caps%2C148&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=runaway+alarm+clock&page=3&crid=2QM773QX6L040&qid=1603735630&sprefix=runaway+alarm+clock%2Caps%2C148&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=runaway+alarm+clock&page=4&crid=2QM773QX6L040&qid=1603735642&sprefix=runaway+alarm+clock%2Caps%2C148&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'RunACCA'})


def RunAC2CA(request):
    driver_set()
    result = finders.find('Fake/log/Runaway_Alarm_Clock2CA.csv')
    url = "https://www.amazon.ca/s?k=runaway+alarm+clock&page=5&crid=2QM773QX6L040&qid=1603735654&sprefix=runaway+alarm+clock%2Caps%2C148&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=runaway+alarm+clock&page=6&crid=2QM773QX6L040&qid=1603735666&sprefix=runaway+alarm+clock%2Caps%2C148&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=runaway+alarm+clock&page=7&crid=2QM773QX6L040&qid=1603735679&sprefix=runaway+alarm+clock%2Caps%2C148&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'RunAC2CA'})


def EACCA(request):
    driver_set()
    result = finders.find('Fake/log/Escape_Alarm_ClockCA.csv')
    url = "https://www.amazon.ca/s?k=escape+alarm+clock&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=escape+alarm+clock&page=2&qid=1603735715&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=escape+alarm+clock&page=3&qid=1603735728&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=escape+alarm+clock&page=4&qid=1603735742&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'EACCA'})


def EAC2CA(request):
    driver_set()
    result = finders.find('Fake/log/Escape_Alarm_Clock2CA.csv')
    url = "https://www.amazon.ca/s?k=escape+alarm+clock&page=5&qid=1603735755&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=escape+alarm+clock&page=6&qid=1603735771&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=escape+alarm+clock&page=7&qid=1603735782&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'EAC2CA'})


def WACCA(request):
    driver_set()
    result = finders.find('Fake/log/Wheel_Alarm_ClockCA.csv')
    url = "https://www.amazon.ca/s?k=wheel+alarm+clock&ref=nb_sb_noss_1"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=wheel+alarm+clock&page=2&qid=1603735821&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=wheel+alarm+clock&page=3&qid=1603735834&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=wheel+alarm+clock&page=4&qid=1603735847&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'WACCA'})


def WAC2CA(request):
    driver_set()
    result = finders.find('Fake/log/Wheel_Alarm_Clock2CA.csv')
    url = "https://www.amazon.ca/s?k=wheel+alarm+clock&page=5&qid=1603735860&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=wheel+alarm+clock&page=6&qid=1603735873&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=wheel+alarm+clock&page=7&qid=1603735886&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'WAC2CA'})


def JACCA(request):
    driver_set()
    result = finders.find('Fake/log/Jumping_Alarm_ClockCA.csv')
    url = "https://www.amazon.ca/s?k=jumping+alarm+clock&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=jumping+alarm+clock&page=2&qid=1603735920&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=jumping+alarm+clock&page=3&qid=1603735935&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=jumping+alarm+clock&page=4&qid=1603735948&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'JACCA'})


def JAC2CA(request):
    driver_set()
    result = finders.find('Fake/log/Jumping_Alarm_Clock2CA.csv')
    url = "https://www.amazon.ca/s?k=jumping+alarm+clock&page=5&qid=1603735964&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=jumping+alarm+clock&page=6&qid=1603735979&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=jumping+alarm+clock&page=7&qid=1603735992&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'JAC2CA'})


def AWCA(request):
    driver_set()
    result = finders.find('Fake/log/Alarm_WheelsCA.csv')
    url = "https://www.amazon.ca/s?k=alarm+wheels&ref=nb_sb_noss_2"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=alarm+wheels&page=2&qid=1603736029&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=alarm+wheels&page=3&qid=1603736035&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=alarm+wheels&page=4&qid=1603736070&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'AWCA'})


def AW2CA(request):
    driver_set()
    result = finders.find('Fake/log/Alarm_Wheels2CA.csv')
    url = "https://www.amazon.ca/s?k=alarm+wheels&page=5&qid=1603736084&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=alarm+wheels&page=6&qid=1603736132&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=alarm+wheels&page=7&qid=1603736147&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'AW2CA'})


def MACCA(request):
    driver_set()
    result = finders.find('Fake/log/Moving_Alarm_ClockCA.csv')
    url = "https://www.amazon.ca/s?k=moving+alarm+clock&crid=22YTY6NVBAPSB&sprefix=moving+alarm+%2Caps%2C145&ref=nb_sb_ss_i_1_13"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=moving+alarm+clock&page=2&crid=22YTY6NVBAPSB&qid=1603736181&sprefix=moving+alarm+%2Caps%2C145&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=moving+alarm+clock&page=3&crid=22YTY6NVBAPSB&qid=1603736192&sprefix=moving+alarm+%2Caps%2C145&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=moving+alarm+clock&page=4&crid=22YTY6NVBAPSB&qid=1603736204&sprefix=moving+alarm+%2Caps%2C145&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'MACCA'})


def MAC2CA(request):
    driver_set()
    result = finders.find('Fake/log/Moving_Alarm_Clock2CA.csv')
    url = "https://www.amazon.ca/s?k=moving+alarm+clock&page=5&crid=22YTY6NVBAPSB&qid=1603736217&sprefix=moving+alarm+%2Caps%2C145&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=moving+alarm+clock&page=6&crid=22YTY6NVBAPSB&qid=1603736233&sprefix=moving+alarm+%2Caps%2C145&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=moving+alarm+clock&page=7&crid=22YTY6NVBAPSB&qid=1603736245&sprefix=moving+alarm+%2Caps%2C145&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'MAC2CA'})


def RRACCA(request):
    driver_set()
    result = finders.find('Fake/log/Run_Alarm_ClockCA.csv')
    url = "https://www.amazon.ca/s?k=run+alarm+clock&ref=nb_sb_noss_2"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=run+alarm+clock&page=2&qid=1603736278&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=run+alarm+clock&page=3&qid=1603736292&ref=sr_pg_3"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=run+alarm+clock&page=4&qid=1603736304&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'RRACCA'})


def RRAC2CA(request):
    driver_set()
    result = finders.find('Fake/log/Run_Alarm_Clock2CA.csv')
    url = "https://www.amazon.ca/s?k=run+alarm+clock&page=5&qid=1603736331&ref=sr_pg_5"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.ca/s?k=run+alarm+clock&page=6&qid=1603736347&ref=sr_pg_6"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.ca/s?k=run+alarm+clock&page=7&qid=1603736363&ref=sr_pg_7"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'RRAC2CA'})


def amazonCH(request):
    driver_set()
    result = finders.find('Fake/log/Amazon_China.csv')
    url = "https://www.amazon.cn/s?k=clocky&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.cn/s?k=%E8%BD%A6%E8%BD%AE%E4%B8%8A%E7%9A%84%E9%97%B9%E9%92%9F&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.cn/s?k=%E8%BD%A6%E8%BD%AE%E9%97%B9%E9%92%9F&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'amazonCH'})


def amazonSG(request):
    driver_set()
    result = finders.find('Fake/log/Amazon_SG.csv')
    url = "https://www.amazon.sg/s?k=run+alarm+clock&qid=1606075282&ref=sr_pg_1"
    amazonUSADefault(result, url, 'w')
    url = "https://www.amazon.sg/s?k=run+alarm+clock&page=2&qid=1606075361&ref=sr_pg_2"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.sg/s?k=run+alarm+clock&page=4&qid=1606075414&ref=sr_pg_4"
    amazonUSADefault(result, url, 'a')
    url = "https://www.amazon.sg/s?k=escape+alarm+clock&ref=nb_sb_noss"
    amazonUSADefault(result, url, 'a')

    return render(request, 'Fake/amazonOnly.html', {'page': 'amazonSG'})


def amazonUS(request):
    return render(request, 'Fake/amazonUSList.html')


def amazonCA(request):
    return render(request, 'Fake/amazonCAList.html')


def amazonSpain(request):
    return render(request, 'Fake/amazonSpainList.html')


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


def amazonIT(request):
    return render(request, 'Fake/amazonITList.html')


def amazonAE(request):
    result = finders.find('Fake/log/amazonUAE.csv')
    url = "https://www.amazon.ae/s?k=clocky&ref=nb_sb_noss"
    amazonScrap(result, url)

    return render(request, 'Fake/amazonAE.html')


def amazonFR(request):
    return render(request, 'Fake/amazonFRList.html')


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
    return render(request, 'Fake/amazonDEList.html')

