"""Duplicate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Fake import views as fv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fv.home, name='list'),
    path('ebayList/', fv.ebay, name='ebay'),
    path('ebayUS/', fv.ebayUS, name='ebayUS'),
    path('ebayUK/', fv.ebayUK, name='ebayUK'),
    path('ebayES/', fv.ebayES, name='ebayES'),
    path('ebayDE/', fv.ebayDE, name='ebayDE'),
    path('ebayFR/', fv.ebayFR, name='ebayFR'),
    path('ebayAU/', fv.ebayAU, name='ebayAU'),
    path('ebayIT/', fv.ebayIT, name='ebayIT'),
    path('AmazonList/', fv.amazon, name='amazon'),
    path('AmazonUS/', fv.amazonUS, name='amazonUS'),
    path('AmazonCA/', fv.amazonCA, name='amazonCA'),
    path('AmazonFR/', fv.amazonFR, name='amazonFR'),
    path('AmazonDE/', fv.amazonDE, name='amazonDE'),
    path('AmazonES/', fv.amazonSpain, name='amazonES'),
    path('AmazonIT/', fv.amazonIT, name='amazonIT'),
    path('AmazonUAE/', fv.amazonAE, name='amazonUAE'),
    path('AmazonJP/', fv.amazonJP, name='amazonJP'),
    path('AmazonCH/', fv.amazonCH, name='amazonCH'),
    path('AmazonSG/', fv.amazonSG, name='amazonSG'),
    path('AmazonNL/', fv.amazonNL, name='amazonNL'),
    path('AmazonUK/', fv.amazonUK, name='amazonUK'),
    path('AmazonAU/', fv.amazonAU, name='amazonAU'),
    path('AmazonMX/', fv.amazonMX, name='amazonMX'),
    path('OtherSites/', fv.other, name='other'),
    path('Walmart/', fv.walmart, name='Walmart'),
    path('Alibaba/', fv.alibaba, name='Alibaba'),
    path('Aliexpress/', fv.aliexpress, name='Aliexpress'),
    path('Mercari/', fv.mercari, name='Mercari'),
    path('Allegro/', fv.allegro, name='Allegro'),
    path('Bol/', fv.bol, name='Bol'),
    path('JapanYahoo/', fv.jpyahoo, name='JapanYahoo'),
    path('Clocky/', fv.clockyKey, name='clockyKey'),
    path('Alarm_Clock_on_Wheels/', fv.ALOW, name='ALOW'),
    path('Alarm_Clock_on_Wheels2/', fv.ALOW2, name='ALOW2'),
    path('Running_Alarm_Clock/', fv.RAC, name='RAC'),
    path('Running_Alarm_Clock2/', fv.RAC2, name='RAC2'),
    path('Creative_Alarm_Clock/', fv.CAC, name='CAC'),
    path('Creative_Alarm_Clock/', fv.CAC2, name='CAC2'),
    path('Runaway_Alarm_Clock/', fv.RunAC, name='RunAC'),
    path('Runaway_Alarm_Clock/', fv.RunAC2, name='RunAC2'),
    path('Escape_Alarm_Clock/', fv.EAC, name='EAC'),
    path('Escape_Alarm_Clock/', fv.EAC2, name='EAC2'),
    path('Wheel_Alarm_Clock/', fv.WAC, name='WAC'),
    path('Wheel_Alarm_Clock/', fv.WAC2, name='WAC2'),
    path('Jumping_Alarm_Clock/', fv.JAC, name='JAC'),
    path('Jumping_Alarm_Clock/', fv.JAC2, name='JAC2'),
    path('Alarm_Wheels/', fv.AW, name='AW'),
    path('Alarm_Wheels/', fv.AW2, name='AW2'),
    path('Moving_Alarm_Clock/', fv.MAC, name='MAC'),
    path('Moving_Alarm_Clock/', fv.MAC2, name='MAC2'),
    path('Run_Alarm_Clock/', fv.RRAC, name='RRAC'),
    path('Run_Alarm_Clock/', fv.RRAC2, name='RRAC2'),
    path('alarma_fugitivo/', fv.ES1, name='ES1'),
    path('despertador_sobre_ruedas/', fv.ES2, name='ES2'),
    path('reloj_despertador_fugitivo/', fv.ES3, name='ES3'),
    path('clockySpain/', fv.ES4, name='ES4'),
    path('depertador_creativo/', fv.ES51, name='ES51'),
    path('depertador_creativo/', fv.ES52, name='ES52'),
    path('despertador_ruedas/', fv.ES6, name='ES6'),
    path('IT11/', fv.IT11, name='IT11'),
    path('IT12/', fv.IT12, name='IT12'),
    path('IT21/', fv.IT21, name='IT21'),
    path('IT22/', fv.IT22, name='IT22'),
    path('IT31/', fv.IT31, name='IT31'),
    path('IT32/', fv.IT32, name='IT32'),
    path('IT41/', fv.IT41, name='IT41'),
    path('IT42/', fv.IT42, name='IT42'),
    path('IT51/', fv.IT51, name='IT51'),
    path('IT52/', fv.IT52, name='IT52'),
    path('IT61/', fv.IT61, name='IT61'),
    path('IT62/', fv.IT62, name='IT62'),
    path('FR11/', fv.FR11, name='FR11'),
    path('FR12/', fv.FR12, name='FR12'),
    path('FR21/', fv.FR21, name='FR21'),
    path('FR31/', fv.FR31, name='FR31'),
    path('FR41/', fv.FR41, name='FR41'),
    path('FR51/', fv.FR51, name='FR51'),
    path('FR61/', fv.FR61, name='FR61'),
    path('DE11/', fv.DE11, name='DE11'),
    path('DE12/', fv.DE12, name='DE12'),
    path('DE21/', fv.DE21, name='DE21'),
    path('DE22/', fv.DE22, name='DE22'),
    path('DE31/', fv.DE31, name='DE31'),
    path('DE32/', fv.DE32, name='DE32'),
    path('DE41/', fv.DE41, name='DE41'),
    path('DE51/', fv.DE51, name='DE51'),
    path('DE61/', fv.DE61, name='DE61'),
    path('DE62/', fv.DE62, name='DE62'),
    path('ClockyCA/', fv.clockyKeyCA, name='clockyKeyCA'),
    path('Alarm_Clock_on_WheelsCA/', fv.ALOWCA, name='ALOWCA'),
    path('Alarm_Clock_on_Wheels2CA/', fv.ALOW2CA, name='ALOW2CA'),
    path('Running_Alarm_ClockCA/', fv.RACCA, name='RACCA'),
    path('Running_Alarm_Clock2CA/', fv.RAC2CA, name='RAC2CA'),
    path('Creative_Alarm_ClockCA/', fv.CACCA, name='CACCA'),
    path('Creative_Alarm_ClockCA/', fv.CAC2CA, name='CAC2CA'),
    path('Runaway_Alarm_ClockCA/', fv.RunACCA, name='RunACCA'),
    path('Runaway_Alarm_ClockCA/', fv.RunAC2CA, name='RunAC2CA'),
    path('Escape_Alarm_ClockCA/', fv.EACCA, name='EACCA'),
    path('Escape_Alarm_ClockCA/', fv.EAC2CA, name='EAC2CA'),
    path('Wheel_Alarm_ClockCA/', fv.WACCA, name='WACCA'),
    path('Wheel_Alarm_ClockCA/', fv.WAC2CA, name='WAC2CA'),
    path('Jumping_Alarm_ClockCA/', fv.JACCA, name='JACCA'),
    path('Jumping_Alarm_ClockCA/', fv.JAC2CA, name='JAC2CA'),
    path('Alarm_WheelsCA/', fv.AWCA, name='AWCA'),
    path('Alarm_WheelsCA/', fv.AW2CA, name='AW2CA'),
    path('Moving_Alarm_ClockCA/', fv.MACCA, name='MACCA'),
    path('Moving_Alarm_ClockCA/', fv.MAC2CA, name='MAC2CA'),
    path('Run_Alarm_ClockCA/', fv.RRACCA, name='RRACCA'),
    path('Run_Alarm_ClockCA/', fv.RRAC2CA, name='RRAC2CA'),
]