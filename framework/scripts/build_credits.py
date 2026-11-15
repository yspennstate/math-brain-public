"""build_credits.py <tree> <out.md> <out.tsv> [surname to leave out ...]
Credits index for the public math brain: who our papers and results build on.
Sources, per paper folder under papers/public: .bib author fields, else \\bibitem author segments.
Per result folder under results/open-problems: the README's Credits / What is known / Prior work section.
Output: a people index (surname, number of our papers citing them, which) and a per-result credit list."""
import collections, io, os, re, sys

tree, out_md, out_tsv = sys.argv[1:4]
SELF = set(a.lower() for a in sys.argv[4:])  # the papers' own authors: self-citations are left out
PAP = os.path.join(tree, "papers", "public")
RES = os.path.join(tree, "results", "open-problems")

def read(p):
    try:
        return io.open(p, encoding="utf-8", errors="replace").read()
    except Exception:
        return ""

LATEX = [(r"\\[\"']\{?(\w)\}?", r"\1"), (r"\\[`^~=.uvHckr]\{?(\w)\}?", r"\1"), (r"\{\\(\w)\}", r"\1"),
         (r"\\ss\b", "ss"), (r"\\o\b", "o"), (r"\\l\b", "l"), (r"[{}~]", " ")]

def clean(s):
    for a, b in LATEX:
        s = re.sub(a, b, s)
    return re.sub(r"\s+", " ", s).strip()

def surnames(authors):
    """authors: 'A. B. Smith and C. Jones' or 'Smith, A. and Jones, C.' -> ['Smith', 'Jones']"""
    out = []
    a = clean(authors)
    a = re.sub(r"\bet al\.?", "", a)
    parts = re.split(r"\s+and\s+|;|&", a)
    for p in parts:
        p = p.strip(" ,.")
        if not p:
            continue
        if "," in p:  # 'Smith, A.' or a comma list 'A. Smith, B. Jones'
            bits = [b.strip() for b in p.split(",") if b.strip()]
            if len(bits) == 2 and re.fullmatch(r"([A-Z]\.\s?-?)+|[A-Z][a-z]+(\s[A-Z]\.)*", bits[1]) and not re.search(r"\.", bits[0]):
                out.append(bits[0].split()[-1])
                continue
            for b in bits:
                w = [t for t in b.split() if not re.fullmatch(r"[A-Z]\.(-?[A-Z]\.)*", t)]
                if w:
                    out.append(w[-1])
            continue
        w = [t for t in p.split() if not re.fullmatch(r"[A-Z]\.(-?[A-Z]\.)*", t)]
        if w:
            out.append(w[-1])
    good = []
    for s in out:
        s = s.strip(".,:;()")
        if re.fullmatch(r"[A-Z][A-Za-z'\-]{1,30}", s) and s.lower() not in STOP and s.lower() not in SELF and not re.fullmatch(r"[IVXLC]+", s):
            good.append(s)
    return good

STOP = set("""the and of in on for with a an to journal ann math probab theory relat fields phys rev lett proc
vol press university springer arxiv preprint comm commun ams soc trans electron j stat statist inst ser
lecture notes surveys annals mathematical studies new york berlin cambridge oxford princeton editor eds ed
in: available online acm ieee siam community programs science software wiley elsevier society institute
team project contributors developers group foundation library""".split())

def bib_authors(txt):
    for m in re.finditer(r"author\s*=\s*[{\"](.+?)[}\"]\s*,\s*\n", txt, re.S | re.I):
        yield m.group(1)

def bibitem_authors(txt):
    for m in re.finditer(r"\\bibitem(?:\[[^\]]*\])?\{[^}]*\}(.*?)(?=\\bibitem|\\end\{thebibliography\})", txt, re.S):
        e = m.group(1).strip()
        cut = re.split(r",\s*(?:\\emph|\\textit|\{\\it|\\textsl|``|\")|\.\s*(?:\\emph|\\textit|\{\\it)|\\newblock", e, maxsplit=1)[0]
        if len(cut) < 200:
            yield cut

people = collections.defaultdict(set)
paper_refs = {}
for d in sorted(os.listdir(PAP)) if os.path.isdir(PAP) else []:
    root = os.path.join(PAP, d)
    if not os.path.isdir(root):
        continue
    bibs, texs = [], []
    for dp, _, fs in os.walk(root):
        for f in fs:
            if f.endswith(".bib"):
                bibs.append(os.path.join(dp, f))
            elif f.endswith(".tex"):
                texs.append(os.path.join(dp, f))
    names, n = set(), 0
    for b in bibs:
        for a in bib_authors(read(b)):
            n += 1
            names.update(surnames(a))
    if not n:
        for t in texs:
            for a in bibitem_authors(read(t)):
                n += 1
                names.update(surnames(a))
    paper_refs[d] = n
    for s in names:
        people[s].add(d)

SEC = re.compile(r"^#+\s*(credits?|acknowledg\w*|what is known|prior work|known results|builds on|references|source question|the question|the problem and where it comes from|what the outside source asks|the sources|what is new( here)?)\b.*$", re.I | re.M)
results = []
for d in sorted(os.listdir(RES)) if os.path.isdir(RES) else []:
    if "intake" in d:  # problem catalogues, not results
        continue
    t = read(os.path.join(RES, d, "README.md"))
    if not t:
        continue
    title = (re.search(r"^#\s+(.+)$", t, re.M) or [None, d])[1]
    secs = []
    for m in SEC.finditer(t):
        body = t[m.end():]
        nxt = re.search(r"^#+\s", body, re.M)
        body = body[: nxt.start()] if nxt else body
        secs.append(re.sub(r"\s+", " ", body).strip())
    if secs:
        txt = " ".join(secs)
        sent = re.split(r"(?<=[.;])\s+(?=[A-Z])", txt)
        results.append((d, title.strip(), " ".join(sent[:3])[:700]))

ranked = sorted(people.items(), key=lambda kv: (-len(kv[1]), kv[0]))
with io.open(out_tsv, "w", encoding="utf-8", newline="") as f:
    f.write("surname\tpapers\tfolders\n")
    for s, ds in ranked:
        f.write("%s\t%d\t%s\n" % (s, len(ds), ",".join(sorted(ds))))
with io.open(out_md, "w", encoding="utf-8", newline="") as f:
    np = sum(1 for v in paper_refs.values() if v)
    f.write("# Credits\n\n")
    f.write("Every result here rests on other people's mathematics. This index lists the authors our public papers cite and the\n"
            "prior work each open-problem result names in its own README. It is built mechanically by `build_credits.py` from\n"
            "the papers' bibliographies (%d papers with a reference list, %d references in all) and from the result READMEs, so\n"
            "it shows who is cited, not how much each contribution mattered; the papers' introductions and acknowledgment\n"
            "sections say that. Surnames are merged across first names, so two authors with one surname share a row; the\n"
            "papers' own authors are left out.\n\n"
            % (np, sum(paper_refs.values())))
    f.write("## Authors cited by three or more of our papers\n\n| author | papers |\n|---|---|\n")
    for s, ds in ranked:
        if len(ds) >= 3:
            f.write("| %s | %d |\n" % (s, len(ds)))
    f.write("\nThe full list, with the papers citing each author, is `CREDITS_AUTHORS.tsv`.\n\n")
    f.write("## Prior work named by each open-problem result\n\n")
    for d, title, txt in results:
        f.write("- `%s` (%s): %s\n" % (d, title, txt))
print("papers", len(paper_refs), "with refs", sum(1 for v in paper_refs.values() if v), "refs", sum(paper_refs.values()),
      "authors", len(people), "results with credit sections", len(results))
