# Currently we are only getting data without full text. 
from pymed import PubMed
import requests
from bs4 import BeautifulSoup
import json

# pubmed = PubMed(tool="DSCP - Ant", email="selma@cs.hacettepe.edu.tr")
# results = pubmed.query("FMF", max_results=50000)

# with open("out2.json", "w") as outfile:
#     articles = []
#     for article in results:
#         articles.append(json.loads(article.toJSON()))
#     outfile.write(json.dumps(articles))

with open("out2.json", "r", encoding="utf-8") as json_file:
    articles = json.loads(json_file.read())
    print('Found', len(articles), 'articles.')

    full_text_dict = {}

    for article in articles:
        id = article["pubmed_id"].split('\n')[0]
        doi = article["doi"]
        r = requests.get('https://pubmed.ncbi.nlm.nih.gov/' + id)
        if r.status_code == 200:
            links = []
            soup = BeautifulSoup(r.text, "html.parser")
            
            links_div = soup.select("#article-page > aside > div > div.full-text-links > div.full-view > div")

            if len(links_div) != 0:
                
                links_div = links_div[0]
                children = links_div.findChildren("a" , recursive=False)
                for link in children:
                    links.append(link.get('href'))
            
            full_text_dict[doi] = links
    
    with open("full_text.json", "w", encoding="utf-8") as json_out:
        json_out.write(json.dumps(full_text_dict))




# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")