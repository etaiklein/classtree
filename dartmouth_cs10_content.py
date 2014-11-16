from bs4 import BeautifulSoup

import requests
import re
import pprint

link_header = "http://www.cs.dartmouth.edu/~scot/cs10/"
def soupify_link(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text)
    return soup

def scrape_url_links (soup, list_of_links):
    for link in soup.find_all('a'):
        link = str(link.get('href'))
        if not ("http") in link: #complete incomplete link paths
            link = link_header + link
        if ("http://www.cs.dartmouth.edu/~scot/cs10/") in link and "html" in link:
            list_of_links.append(link)

soup = soupify_link("http://www.cs.dartmouth.edu/~scot/cs10/syllabus.html")
 
 

link_list_initial = []
link_list_result = []

def crawl_all_pages(soup, link_list_initial, link_list_result):
    scrape_url_links(soup, link_list_result)
    i = 10
    while link_list_initial != link_list_result and i > 0:
        link_list_initial = link_list_result[:]
    
        for link in link_list_initial:
            try:
                scrape_url_links (soup, link_list_result)
                soup = soupify_link(link)
    
            except Exception as e:
                pass 
        link_list_result = list(set(link_list_result))
    
        i -= 1
        
    link_list_result.sort()

def create_populate_pages ():
    for page in link_list_result:
    
        #TODO: replace with regex
        p = page.replace("/","")
        p = p.replace("~","")
        p = p.replace(".","")
        p = p.replace(":","")
        
        with open ("output/" + p[29:-4] + ".html", "w") as infile:
            try:
                infile.write("%s"%(soupify_link(page)))
                
            except Exception as e:
                pass
            
crawl_all_pages(soup, link_list_initial, link_list_result)
create_populate_pages()