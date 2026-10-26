"""Collect every work cited by the papers in the public math-brain repo (.bib entries and thebibliography lists),
merge them and write docs/cited-works.md. Bibliographic data only; the cited works themselves are not copied.
usage: python cited_works.py <repo> [--write]"""
import collections
import os
import re
import subprocess
import sys

repo = sys.argv[1]
files = subprocess.run(["git", "-C", repo, "ls-files", "*.bib", "*.tex", "*.bbl"],
                       capture_output=True, text=True, encoding="utf-8").stdout.split("\n")
files = [f for f in files if f]

CUTS = ("paper", "sections", "manuscript", "tex", "revision-2", "supplement", "arxiv", "src", "latex")


def paper_of(p):
    parts = p.split("/")[:-1]
    for i, x in enumerate(parts):
        if x in CUTS:
            return "/".join(parts[:i])
    return "/".join(parts)


def detex(s):
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\\bysame\b", "(same authors)", s)
    s = re.sub(r"\\doi\s*\{?[^\s}]*\}?\.?", "", s)
    s = re.sub(r"\.\s*URL\s*\.?", ".", s)
    s = s.replace("\\L ", "\u0141").replace("\\L", "\u0141").replace("\\l ", "\u0142").replace("\\i ", "i").replace("\\i", "i")
    s = re.sub(r"\\[()]", "", s)
    s = re.sub(r"\\([_#%&])", r"\1", s)
    s = re.sub(r"\\[`'^\"~=.uvHc]\s?\{?([A-Za-z])\}?", r"\1", s)
    s = re.sub(r"\\(emph|textit|textbf|textsc|textrm|texttt|textsf|mathrm|mathbb|mathcal|em|it|bf|sc|rm|tt|sf|url|href)\b", "", s)
    s = re.sub(r"\\[ ,;!]", " ", s)
    s = re.sub(r"\$", "", s)
    s = re.sub(r"\\newblock|\\penalty0|\\&", " ", s)
    s = re.sub(r"\\[`'^\"~=.uvHc]\{?([A-Za-z])\}?", r"\1", s)
    s = re.sub(r"\\ss\b", "ss", s)
    s = re.sub(r"\\([A-Za-z]+)", r"\1", s)
    s = re.sub(r"[{}]", "", s)
    s = s.replace("~", " ").replace("--", "-")
    return re.sub(r"\s+", " ", s).strip()


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())[:70]


works = {}
cites = collections.defaultdict(set)


INTERNAL = re.compile(r"^(A\d{3}|account\d|Campaign supplemental|Claude B\d|claude-|codex-|Math Brain|Full FEI)|"
                      r"unpublished|recovered manuscript|Repository path|Git blob pin|Source archive|run \\?path|<private-repo>")


def add(k, ent, link, pap):
    # internal run records and research notes are not cited works
    if not k or INTERNAL.search(ent) or "<private-repo>" in link:
        return
    if k not in works or (link and not works[k][1]):
        works[k] = (ent, link)
    cites[k].add(pap)


for f in files:
    try:
        t = open(os.path.join(repo, f), encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    pap = paper_of(f)
    if f.endswith(".bib"):
        for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\s*\}", t, re.S):
            typ, key, body = m.groups()
            if typ.lower() in ("comment", "string", "preamble"):
                continue
            fld = {}
            for fm in re.finditer(r"(\w+)\s*=\s*", body):
                name, j = fm.group(1).lower(), fm.end()
                if j >= len(body):
                    continue
                if body[j] == "{":
                    depth, k2 = 0, j
                    while k2 < len(body):
                        depth += {"{": 1, "}": -1}.get(body[k2], 0)
                        if depth == 0:
                            break
                        k2 += 1
                    val = body[j + 1:k2]
                elif body[j] == '"':
                    k2 = body.find('"', j + 1)
                    val = body[j + 1:k2]
                else:
                    val = re.match(r"[^,\n]*", body[j:]).group(0)
                fld.setdefault(name, detex(val))
            title = fld.get("title", "")
            if not title:
                continue
            venue = fld.get("journal") or fld.get("booktitle") or fld.get("publisher") or ""
            ent = " ".join(x for x in [fld.get("author", "").replace(" and ", ", "),
                                       "(%s)." % fld["year"] if fld.get("year") else "",
                                       title.rstrip(".") + ".", venue] if x).strip()
            link = ("https://doi.org/" + fld["doi"]) if fld.get("doi") else \
                   ("https://arxiv.org/abs/" + fld["eprint"]) if fld.get("eprint") else fld.get("url", "")
            add(norm(title), ent, link, pap)
    elif "\\bibitem" in t:
        for m in re.finditer(r"\\bibitem(?:\[[^\]]*\])?\{[^}]*\}(.*?)(?=\\bibitem|\\end\{thebibliography\})", t, re.S):
            raw = m.group(1)
            urls = re.findall(r"\\(?:url|href)\{([^}]+)\}", raw)
            doi = re.search(r"(10\.\d{4,9}/[^\s},\\]+)", raw)
            arx = re.search(r"arXiv[: ]*(?:abs/)?(\d{4}\.\d{4,5})", raw)
            ent = detex(re.sub(r"\\(url|href)\{[^}]*\}(\{[^}]*\})?", "", raw)).strip(" .,")
            if len(ent) < 15:
                continue
            link = ("https://doi.org/" + doi.group(1).rstrip(".")) if doi else \
                   ("https://arxiv.org/abs/" + arx.group(1)) if arx else (urls[0] if urls else "")
            # key on the part after the author list (first ". " or ", " followed by a title-ish run)
            tail = re.split(r"\.\s|,\s(?=[A-Z][a-z])", ent, maxsplit=1)
            add(norm(tail[-1]) or norm(ent), ent[:400], link, pap)

papers = sorted({p for s in cites.values() for p in s})
print("files", len(files), "works", len(works), "citing folders", len(papers))
print("with link", sum(1 for v in works.values() if v[1]))
if "--write" in sys.argv:
    out = ["# Works cited by the papers in this repository", "",
           "Every work cited in a bibliography (a `.bib` file or a `thebibliography` list) of a paper or manuscript in this "
           "repository, merged across papers. Each entry gives a DOI, arXiv or web link when the source gave one, and the "
           "folders whose papers cite it. Only bibliographic data is listed; the cited works are not copied here.", "",
           "%d works, cited from %d folders. Regenerate with `python tools/cited_works.py . --write`." % (len(works), len(papers)), ""]
    for k in sorted(works, key=lambda k: works[k][0].lower()):
        ent, link = works[k]
        line = "- " + ent.replace("|", "/") + (" <%s>" % link if link else "")
        ws = sorted(cites[k])
        line += " Cited in " + ", ".join("`%s`" % w for w in ws[:3]) + (" and %d more" % (len(ws) - 3) if len(ws) > 3 else "") + "."
        out.append(line)
    open(os.path.join(repo, "docs", "cited-works.md"), "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    print("wrote docs/cited-works.md")
