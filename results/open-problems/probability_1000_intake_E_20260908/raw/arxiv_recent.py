import sys, urllib.parse
import requests, xml.etree.ElementTree as ET
q = sys.argv[1]; mx=int(sys.argv[2]) if len(sys.argv)>2 else 60
url="https://export.arxiv.org/api/query?search_query="+urllib.parse.quote(q)+f"&start=0&max_results={mx}&sortBy=submittedDate&sortOrder=descending"
r=requests.get(url,timeout=60,headers={"User-Agent":"ProbabilityResearch/1.0"}); r.raise_for_status()
ns={'a':'http://www.w3.org/2005/Atom'}
for e in ET.fromstring(r.text).findall('a:entry',ns):
    aid=e.find('a:id',ns).text.rsplit('/',1)[-1]
    t=' '.join(e.find('a:title',ns).text.split()); pub=e.find('a:published',ns).text[:7]
    print(f"{aid}\t{pub}\t{t}")
