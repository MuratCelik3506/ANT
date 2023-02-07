# Currently we are only getting data without full text. 
from pymed import PubMed
import json

pubmed = PubMed(tool="DSCP - Ant", email="selma@cs.hacettepe.edu.tr")
results = pubmed.query("FMF", max_results=500)

with open("out.json", "w") as outfile:
    articles = []
    for article in results:
        articles.append(json.loads(article.toJSON()))
    outfile.write(json.dumps(articles))