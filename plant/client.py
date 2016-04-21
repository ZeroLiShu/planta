#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

from .common import *

class EfloraClient:

    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update(Default_Header)

    def _get_plant_list_from_page(self, name, pageindex):
        plantlist = []

        pageurl = Eflora_Search_URL + '/' + name + '?page=' + str(pageindex)
        r = self._session.get(pageurl)
        soup = BeautifulSoup(r.content)

        for tr in soup.find_all('tr'):
            if tr.has_attr('style'):
                for td in tr.children:
                    print td

        #for tr in table:
        #    plantdict = {}
        #    tdlist = BeautifulSoup(tr).find_all('td')
        #    assert 5 == len(tdlist)
        #    plantdict['name'] = tdlist[0].text
        #    plantdict['latin'] = tdlist[1].text
        #    plantdict['alias'] = tdlist[2].text
        #    plantdict['slug'] = tdlist[3].text
        #    plantdict['url'] = Eflora_URL + tdlist[4]['href']

        #    print '----one row---'
        #    print plantdict
        #    plantlist.append(plantdict)

        return plantlist

    def search(self, name):
        plantlist = []

        pageurl = Eflora_Search_URL + '/' + name + '?page=1'
        r = self._session.get(pageurl)
        soup = BeautifulSoup(r.content)
        alist = soup.select('div#divpage > a')
        print alist
        alist_len = len(alist)
        if alist_len < 2:
            return
        pagenum = int(alist[len(alist) - 2].text)
        print pagenum

        for pageindex in range(1, pagenum + 1):
            plantlist.extend(self._get_plant_list_from_page(name, pageindex))

        print plantlist
        return json.dumps(plantlist)
