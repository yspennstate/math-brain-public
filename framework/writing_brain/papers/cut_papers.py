"""Cut the modern paper shelf into the moves a paper has to make.

Reads $PAPER_SHELF_DATA/meta.jsonl and src/<id>.tex (harvest_arxiv.py) and writes
writing_brain/papers/shelf/papers_NNN.jsonl, one passage per line, in the fields of nodes/academic plus where it
came from (arxiv, journal_ref, doi, licence). Every paper is CC BY, CC BY-SA or CC0 and refereed.

The moves (role):
  abstract           the abstract
  intro_opening      the first paragraph of the introduction: how the problem is put to a reader
  contribution       the paragraph that says what this paper proves ("In this paper", "Our main result")
  result_stated      a theorem or proposition with the sentence that leads into it
  proof_entered      the first sentences of a proof
  definition         a term introduced
  idea_given         the heuristic or the idea of a proof, said in words
  prior_work         a paragraph that places the paper among others (three or more citations)
  open_question      a question, conjecture or direction left open
  section_opening    the first paragraph of a later section

  python -I -X utf8 cut_papers.py [--out shelf/papers_001.jsonl] [--new]   (--new: only papers no other shelf file holds)
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.environ.get("PAPER_SHELF_DATA", "writing_brain_data/papers")  # raw harvest: meta.jsonl, src/
CAP = {"abstract": 1, "intro_opening": 1, "contribution": 1, "result_stated": 2, "proof_entered": 2, "definition": 1,
       "idea_given": 1, "prior_work": 1, "open_question": 1, "section_opening": 2}


def clean(t):
    t = re.sub(r"(?<!\\)%.*", "", t)
    t = re.sub(r"\\(label|index|vspace|hspace|medskip|bigskip|smallskip|noindent|newline|linebreak)\*?(\{[^{}]*\})?", " ", t)
    t = re.sub(r"\\(cite[tp]?|citep|citet|cites)(\[[^\]]*\])*\{[^{}]*\}", "[cite]", t)
    t = re.sub(r"\\(eqref)\{[^{}]*\}", "(eq)", t)
    t = re.sub(r"\\(c?ref|Cref|autoref)\{[^{}]*\}", "(ref)", t)
    for _ in range(2):
        t = re.sub(r"\\(emph|textit|textbf|textrm|textsf|text|mbox|textsc)\{([^{}]*)\}", r"\2", t)
    t = re.sub(r"\\begin\{(equation|align|eqnarray|multline|gather)\*?\}", "$$", t)
    t = re.sub(r"\\end\{(equation|align|eqnarray|multline|gather)\*?\}", "$$", t)
    t = re.sub(r"\\\[(.*?)\\\]", r"$$\1$$", t, flags=re.S)
    t = re.sub(r"\\\((.*?)\\\)", r"$\1$", t, flags=re.S)
    t = re.sub(r"\\footnote\{[^{}]*(\{[^{}]*\}[^{}]*)*\}", "", t)
    t = re.sub(r"\\smash\{(\$[^$]*\$)\}", r"\1", t)
    t = re.sub(r"\{\\(it|em|bf|sl|rm|sc|tt) ([^{}]*)\}", r"\2", t)
    t = re.sub(r"\\(it|em|bf|sl|rm|sc|tt)\b ?", "", t)
    t = re.sub(r"\\(begin|end)\{(itemize|enumerate|description|center|quote)\}", " ", t)
    t = re.sub(r"\\item(\[[^\]]*\])?", " -", t)
    t = t.replace("~", " ").replace("``", '"').replace("''", '"')
    return re.sub(r"\s+", " ", t).strip()


CMD = re.compile(r"\\[a-zA-Z]{2,}")


def latex_left(t):
    """A command outside the maths (a private macro, an environment the cleaner does not know): the passage
    would show a writer source code, so it is left off the shelf."""
    t = re.sub(r"\$\$.*?\$\$", " ", t, flags=re.S)
    return bool(CMD.search(re.sub(r"\$[^$]*\$", " ", t)))


def words(t):
    return len(re.sub(r"\$[^$]*\$", " x ", t).split())


def paras(block):
    return [p for p in (clean(x) for x in re.split(r"\n\s*\n", block)) if words(p) >= 25 and not p.startswith("\\")]


def sentences(t, n):
    s = re.split(r"(?<=[.!?])\s+(?=[A-Z\\$])", t)
    return " ".join(s[:n])


def cut(tex):
    out = []
    body = tex.split("\\begin{document}", 1)[-1].split("\\end{document}")[0]
    body = re.split(r"\\(bibliography|begin\{thebibliography\})", body)[0]
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", body, re.S)
    if m:
        out.append(("abstract", clean(m.group(1))))
    secs = re.split(r"\\section\*?\{([^{}]*)\}", body)
    names, texts = secs[1::2], secs[2::2]
    for i, (nm, tx) in enumerate(zip(names, texts)):
        ps = paras(re.split(r"\\subsection", tx)[0])
        if not ps:
            continue
        if i == 0 or re.search(r"introduction", nm, re.I):
            out.append(("intro_opening", ps[0]))
            for p in ps[1:]:
                if re.search(r"\b(In this (paper|note|article|work)|Our main (result|theorem|contribution)|We prove|We show|The main result)", p):
                    out.append(("contribution", p)); break
        else:
            out.append(("section_opening", ps[0]))
        for p in ps:
            if len(re.findall(r"\[cite\]", p)) >= 3:
                out.append(("prior_work", p))
            if re.search(r"\b(open (problem|question)|we conjecture|remains open|it would be interesting|natural question)", p, re.I):
                out.append(("open_question", p))
            if re.search(r"\b(heuristic|intuition|the idea (of|behind) the proof|roughly speaking|strategy of the proof|key idea)", p, re.I):
                out.append(("idea_given", p))
    for m in re.finditer(r"\\begin\{(theorem|thm|proposition|prop|maintheorem)\*?\}", body):
        end = body.find("\\end{" + m.group(1), m.end())
        if end < 0 or end - m.end() > 4000:
            continue
        stmt = re.sub(r"^\s*\[[^\]]*\]", "", body[m.end():end])
        # the lead-in: the paragraph just before the statement, if it is prose
        before = re.split(r"\n\s*\n", body[max(0, m.start() - 1500):m.start()])[-1]
        lead = clean(before)
        lead = lead if 6 <= words(lead) <= 120 and not lead.startswith("\\") else ""
        out.append(("result_stated", (lead + " " if lead else "") + "Theorem. " + clean(stmt)))
    for m in re.finditer(r"\\begin\{proof\}(\[[^\]]*\])?(.*?)\\end\{proof\}", body, re.S):
        out.append(("proof_entered", sentences(clean(m.group(2)), 3)))
    for m in re.finditer(r"\\begin\{(definition|defn|defi)\*?\}(\[[^\]]*\])?(.*?)\\end\{\1\*?\}", body, re.S):
        out.append(("definition", clean(m.group(3))))
    return out


def main():
    a = sys.argv[1:]
    dst = a[a.index("--out") + 1] if "--out" in a else os.path.join(HERE, "shelf", "papers_001.jsonl")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    meta = {}
    for line in open(os.path.join(DATA, "meta.jsonl"), encoding="utf-8"):
        r = json.loads(line); meta[r["id"]] = r
    # --new: cut only papers no shelf file holds yet, so a harvest adds a new shelf file and the old ones stay as they are
    shelved = set()
    if "--new" in a:
        import glob
        for fp in glob.glob(os.path.join(HERE, "shelf", "*.jsonl")):
            if os.path.abspath(fp) == os.path.abspath(dst):
                continue
            for line in open(fp, encoding="utf-8"):
                shelved.add(json.loads(line)["work"])
    n = papers = 0
    roles = {}
    with open(dst, "w", encoding="utf-8") as f:
        for fn in sorted(os.listdir(os.path.join(DATA, "src"))):
            if not fn.endswith(".tex"):
                continue
            aid = fn[:-4]
            if "W-AX-" + aid in shelved:
                continue
            r = meta.get(aid) or meta.get(aid.replace("_", "/"))
            if not r:
                continue
            tex = open(os.path.join(DATA, "src", fn), encoding="utf-8", errors="replace").read()
            got = {}
            for role, text in cut(tex):
                w = words(text)
                if w < 20 or w > 320 or got.get(role, 0) >= CAP[role] or latex_left(text):
                    continue
                got[role] = got.get(role, 0) + 1
                au = r["authors"][0] + (" et al." if len(r["authors"]) > 1 else "") if r["authors"] else ""
                row = {"work": "W-AX-" + aid, "title": r["title"], "author": au, "id": f"P-AX{aid}-{role}-{got[role]}",
                       "kind": "passage", "role": role, "form": "paper", "year": r["year"], "words": w, "text": text,
                       "arxiv": r["id"], "journal_ref": r["journal_ref"], "doi": r["doi"], "license": r["license"],
                       "cats": r["cats"]}
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
                n += 1; roles[role] = roles.get(role, 0) + 1
            papers += 1 if got else 0
    print(json.dumps({"papers": papers, "passages": n, "roles": roles}))


if __name__ == "__main__":
    main()
