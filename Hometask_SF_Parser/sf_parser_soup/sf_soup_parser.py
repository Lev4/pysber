import requests
import pandas as pd
from bs4 import BeautifulSoup
from multiprocessing import Pool
import os 
import pickle

def get_vacs(fpth):
    vacs = pd.read_excel(fpth)
    vacs = vacs.ids.astype('str').unique().tolist()
    vacs = [x for x in vacs if x.isdigit()]
    return vacs

def links_maker(vacs):
    links = []
    
    for v_id in vacs:
        
        url = 'https://career18.sapsf.com/career?'
        url += 'career_ns=job_listing&company=paosberbanP2&navBarLevel=JOB_SEARCH&rcm_site_locale=ru_RU&'
        url += 'career_job_req_id={}&selected_lang=ru_RU&jobAlertController_jobAlertId'.format(v_id)
        url += '=&jobAlertCon=troller_jobAlertName=&_s.crb=ihl8rnb5dyInCnbwshM%2b3Ks%2b%2bCg%3d'
        links.append(url)
        
    
    return links

def get_info(url):
    res = requests.get(url)
    page = res.content
    soup = BeautifulSoup(page,'html.parser')
    result = soup.find_all(['h1','b','li','ul'])
    vac_description = []
    for el in result:
        vac_description.append(el.text)
    return vac_description

def main():
    
    files = os.listdir()
    for el in files:
        if el.endswith('.xlsx'):
            fpth = el
            break
    
    vacs = get_vacs(fpth)
    sf_links = links_maker(vacs)
    
    data = []
    for url in sf_links[:30]:
        data.append(get_info(url))

    with Pool(10) as p:
        records = p.map(get_info, sf_links)

    with open('vacs_records.pkl', 'wb') as f:
        pickle.dump(records,f)


if __name__ == '__main__':
    main()