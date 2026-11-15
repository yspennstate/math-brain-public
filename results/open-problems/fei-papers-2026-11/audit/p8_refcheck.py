"""Check every reference in a paper's thebibliography against the record it names.
DOI -> Crossref (DataCite for Zenodo), arXiv id -> arXiv API, GitHub/other URL -> HTTP status.
Prints the record's title, first author, year, venue next to the bibitem so a reader compares them.
usage: python p8_refcheck.py main.tex"""
import json, re, sys, time, urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET

UA = {"User-Agent": "refcheck/1.0 (bibliography audit)"}


def get(url, accept=None):
    h = dict(UA)
    if accept:
        h["Accept"] = accept
    err = "retries exhausted"
    for t in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=40) as r:
                return r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                err = f"HTTP {e.code}"; time.sleep(10 * (t + 1)); continue
            return e.code, ""
        except Exception as e:
            time.sleep(3); err = str(e)
    return None, err


tex = open(sys.argv[1], encoding="utf-8").read()
bib = tex[tex.index("\\begin{thebibliography}"):tex.index("\\end{thebibliography}")]
items = re.split(r"\\bibitem\{", bib)[1:]
for it in items:
    key, body = it.split("}", 1)
    body = " ".join(body.split())
    print("=" * 100); print(key, "|", body[:260])
    for doi in re.findall(r"doi:(10\.[^\s;,]+?)(?:[;,]?\s|$)", body + " "):
        doi = doi.rstrip(".").replace("\\_", "_")
        if "zenodo" in doi:
            s, t = get("https://api.datacite.org/dois/" + doi)
            if s == 200:
                a = json.loads(t)["data"]["attributes"]
                print(f"  DataCite {doi}: {a['titles'][0]['title'][:150]} | {[c.get('name') for c in a['creators']][:3]} | {a.get('publicationYear')}")
            else:
                print(f"  DataCite {doi}: HTTP {s}  <-- CHECK")
        else:
            s, t = get("https://api.crossref.org/works/" + doi)
            if s == 200:
                m = json.loads(t)["message"]
                au = [f"{x.get('given','')} {x.get('family','')}" for x in m.get("author", [])]
                yr = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
                print(f"  Crossref {doi}: {(m.get('title') or [''])[0][:150]} | {au[:5]} | {(m.get('container-title') or [''])[0]} "
                      f"vol {m.get('volume')} no {m.get('issue')} pp {m.get('page')} art {m.get('article-number')} | {yr}")
            else:
                print(f"  Crossref {doi}: HTTP {s}  <-- CHECK")
        time.sleep(1)
    for ax in re.findall(r"arXiv:(\d{4}\.\d{4,5})", body):
        s, t = get("https://export.arxiv.org/api/query?id_list=" + ax)
        if s == 200:
            ns = {"a": "http://www.w3.org/2005/Atom"}
            e = ET.fromstring(t).find("a:entry", ns)
            if e is None or e.find("a:title", ns) is None:
                print(f"  arXiv {ax}: no entry  <-- CHECK")
            else:
                ti = " ".join(e.find("a:title", ns).text.split())
                au = [x.find("a:name", ns).text for x in e.findall("a:author", ns)]
                print(f"  arXiv {ax}: {ti[:150]} | {au[:5]} | {e.find('a:published', ns).text[:10]}")
        else:
            print(f"  arXiv {ax}: HTTP {s}  <-- CHECK")
        time.sleep(3)
    for u in re.findall(r"\\url\{([^}]+)\}", body):
        s, _ = get(u)
        print(f"  URL {u}: HTTP {s}" + ("" if s == 200 else "  <-- CHECK"))
    if not re.search(r"doi:|\\url\{", body):
        # no DOI: ask Crossref for the best bibliographic match to the item's own text
        q = re.sub(r"[\\{}~'`^]", " ", body)
        s, t = get("https://api.crossref.org/works?rows=2&query.bibliographic=" + urllib.parse.quote(q[:300]))
        if s == 200:
            for m in json.loads(t)["message"]["items"]:
                au = [f"{x.get('given','')} {x.get('family','')}" for x in m.get("author", [])]
                yr = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
                print(f"  Crossref search: {(m.get('title') or [''])[0][:140]} | {au[:4]} | {(m.get('container-title') or [''])[0]} "
                      f"vol {m.get('volume')} pp {m.get('page')} | {yr} | doi {m.get('DOI')}")
        else:
            print(f"  Crossref search: HTTP {s}  <-- CHECK")
        time.sleep(1)
