import sys, urllib.parse, re, json
import requests, xml.etree.ElementTree as ET
q = sys.argv[1]
mx = int(sys.argv[2]) if len(sys.argv)>2 else 40
url = "https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(q) + f"&start=0&max_results={mx}&sortBy=relevance"
r = requests.get(url, timeout=60, headers={"User-Agent":"ProbabilityResearch/1.0"})
r.raise_for_status()
ns={'a':'http://www.w3.org/2005/Atom'}
root=ET.fromstring(r.text)
for e in root.findall('a:entry',ns):
    idu=e.find('a:id',ns).text
    aid=idu.rsplit('/',1)[-1]
    t=' '.join(e.find('a:title',ns).text.split())
    pub=e.find('a:published',ns).text[:7]
    cats=[c.get('term') for c in e.findall('a:category',ns)]
    print(f"{aid}\t{pub}\t{cats[0]}\t{t}")
