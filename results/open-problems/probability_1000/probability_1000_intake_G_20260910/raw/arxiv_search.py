"""Query the arXiv API by title words so that no arXiv number is ever guessed from memory."""
import sys, time, json, re, urllib.parse, requests, xml.etree.ElementTree as ET
NS={"a":"http://www.w3.org/2005/Atom"}
def search(q, n=3):
    url="https://export.arxiv.org/api/query?"+urllib.parse.urlencode({"search_query":q,"max_results":n})
    r=requests.get(url,timeout=60); r.raise_for_status()
    root=ET.fromstring(r.content); out=[]
    for e in root.findall("a:entry",NS):
        aid=e.find("a:id",NS).text.rsplit("/abs/",1)[-1]
        title=" ".join(e.find("a:title",NS).text.split())
        auth=", ".join(a.find("a:name",NS).text for a in e.findall("a:author",NS))[:80]
        out.append((aid,title,auth))
    return out
if __name__=="__main__":
    for q in sys.argv[1:]:
        print("##",q)
        try:
            for aid,t,a in search(q): print("  ",aid,"|",t[:90],"|",a)
        except Exception as ex: print("  ERR",ex)
        time.sleep(3.2)
