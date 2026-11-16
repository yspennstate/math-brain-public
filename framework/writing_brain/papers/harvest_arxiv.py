"""The modern paper shelf: refereed arXiv papers under an open licence, in the fields we write in.

Step 1, meta: list a set's records through arXiv's OAI-PMH feed and keep a paper only when
  - its licence is CC BY, CC BY-SA or CC0 (we may keep and show its text with attribution), and
  - it has a journal reference (it went through a referee and appeared somewhere).
Step 2, src: fetch the LaTeX source of the kept papers (arxiv.org/e-print/<id>), keep the main .tex.
Both steps pace themselves at one request every 3.5 seconds, as arXiv asks of harvesters, and resume where
they stopped. Texts are data: run with python -I.

  python -I harvest_arxiv.py meta --set math:math:PR --from 2015-01-01 [--until 2026-11-01]
  python -I harvest_arxiv.py src [--max 400]
Data lives in $PAPER_SHELF_DATA (meta.jsonl, src/<id>.tex); the cut passages go to
writing_brain/papers/shelf (cut_papers.py).
"""
import gzip, io, json, os, re, sys, tarfile, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

DATA = os.environ.get("PAPER_SHELF_DATA", "writing_brain_data/papers")  # raw harvest: meta.jsonl, src/
UA = {"User-Agent": "writing-shelf-harvester/0.1 (research reading list)"}
OAI = "https://oaipmh.arxiv.org/oai"
NS = {"o": "http://www.openarchives.org/OAI/2.0/", "a": "http://arxiv.org/OAI/arXiv/"}
OPEN = re.compile(r"creativecommons\.org/(licenses/(by|by-sa)/|publicdomain/zero/)")
PACE = 3.5


def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 503:
                wait = int(e.headers.get("Retry-After") or 30)
                time.sleep(min(wait, 120))
                continue
            if e.code in (403, 404):
                return None
            time.sleep(10 * (i + 1))
        except Exception:
            time.sleep(10 * (i + 1))
    return None


def meta(argv):
    a = dict(zip(argv[::2], argv[1::2]))
    st, frm, until = a["--set"], a.get("--from", "2015-01-01"), a.get("--until", "")
    os.makedirs(DATA, exist_ok=True)
    out = os.path.join(DATA, "meta.jsonl")
    have = set()
    if os.path.exists(out):
        for line in open(out, encoding="utf-8"):
            have.add(json.loads(line)["id"])
    tokf = os.path.join(DATA, "token_" + re.sub(r"\W", "_", st) + ".txt")
    tok = open(tokf).read().strip() if os.path.exists(tokf) else ""
    seen = kept = 0
    while True:
        if tok:
            url = OAI + "?verb=ListRecords&resumptionToken=" + urllib.parse.quote(tok)
        else:
            url = f"{OAI}?verb=ListRecords&metadataPrefix=arXiv&set={st}&from={frm}" + (f"&until={until}" if until else "")
        raw = get(url)
        time.sleep(PACE)
        if raw is None:
            print("no answer; stopping, rerun to resume", flush=True)
            return
        root = ET.fromstring(raw)
        with open(out, "a", encoding="utf-8") as f:
            for rec in root.iter("{%s}record" % NS["o"]):
                m = rec.find(".//a:arXiv", NS)
                if m is None:
                    continue
                seen += 1
                t = lambda k: (m.findtext("a:" + k, default="", namespaces=NS) or "").strip()
                lic, jr = t("license"), t("journal-ref")
                if not OPEN.search(lic) or not jr or t("id") in have:
                    continue
                auth = [" ".join(x for x in (au.findtext("a:forenames", default="", namespaces=NS),
                                             au.findtext("a:keyname", default="", namespaces=NS)) if x)
                        for au in m.findall("a:authors/a:author", NS)]
                row = {"id": t("id"), "title": re.sub(r"\s+", " ", t("title")), "authors": auth,
                       "year": (t("created") or "")[:4], "cats": t("categories"), "journal_ref": re.sub(r"\s+", " ", jr),
                       "doi": t("doi"), "license": lic, "abstract": re.sub(r"\s+", " ", t("abstract")), "set": st}
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
                have.add(row["id"])
                kept += 1
        rt = root.find(".//o:resumptionToken", NS)
        tok = (rt.text or "").strip() if rt is not None else ""
        open(tokf, "w").write(tok)
        print(f"{st}: seen {seen} kept {kept}", flush=True)
        if not tok:
            return


def main_tex(blob):
    """The .tex holding \\documentclass from an e-print (a tar.gz, a gzipped single file, or plain text)."""
    try:
        data = gzip.decompress(blob)
    except Exception:
        data = blob
    try:
        tf = tarfile.open(fileobj=io.BytesIO(data))
        best = None
        for mem in tf.getmembers():
            if mem.isfile() and mem.name.lower().endswith(".tex") and mem.size < 3_000_000:
                txt = tf.extractfile(mem).read().decode("utf-8", "replace")
                if "\\documentclass" in txt and (best is None or len(txt) > len(best)):
                    best = txt
        return best
    except tarfile.ReadError:
        txt = data.decode("utf-8", "replace")
        return txt if "\\documentclass" in txt else None


def src(argv):
    a = dict(zip(argv[::2], argv[1::2]))
    mx = int(a.get("--max", 400))
    d = os.path.join(DATA, "src")
    os.makedirs(d, exist_ok=True)
    rows = [json.loads(l) for l in open(os.path.join(DATA, "meta.jsonl"), encoding="utf-8")]
    rows.sort(key=lambda r: r["year"], reverse=True)
    done = got = 0
    tried = set(os.listdir(d))  # one listing, not two stat calls per paper
    for r in rows:
        if got >= mx:
            break
        base = r["id"].replace("/", "_") + ".tex"
        fn = os.path.join(d, base)
        if base in tried or base + ".none" in tried:
            continue
        blob = get("https://arxiv.org/e-print/" + r["id"])
        time.sleep(PACE)
        tex = main_tex(blob) if blob else None
        if tex:
            open(fn, "w", encoding="utf-8").write(tex)
            got += 1
        else:
            open(fn + ".none", "w").close()
        done += 1
        if done % 20 == 0:
            print(f"src: tried {done} kept {got}", flush=True)
    print(f"src: tried {done} kept {got}", flush=True)


if __name__ == "__main__":
    {"meta": meta, "src": src}[sys.argv[1]](sys.argv[2:])
