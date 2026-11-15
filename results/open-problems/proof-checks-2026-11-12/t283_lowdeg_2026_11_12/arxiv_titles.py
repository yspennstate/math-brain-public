"""Print id, date, authors and title of each entry of an arXiv API answer (Atom XML).  usage: arxiv_titles.py FILE"""
import sys
import xml.etree.ElementTree as ET

ns = {"a": "http://www.w3.org/2005/Atom"}
root = ET.parse(sys.argv[1]).getroot()
sys.stdout.reconfigure(encoding="utf-8")
entries = root.findall("a:entry", ns)
print("entries:", len(entries))
for e in entries:
    i = e.find("a:id", ns).text.rsplit("/", 1)[-1]
    d = e.find("a:published", ns).text[:10]
    u = e.find("a:updated", ns).text[:10]
    t = " ".join(e.find("a:title", ns).text.split())
    au = [x.find("a:name", ns).text for x in e.findall("a:author", ns)]
    print("%s  pub %s upd %s  %s  | %s" % (i, d, u, t[:110], ", ".join(au[:4]) + (" et al." if len(au) > 4 else "")))
