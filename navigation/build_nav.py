"""Build the navigation brain (cards.jsonl, edges.jsonl, MANIFEST.json) for the public math brain repo.

Schema: SCHEMA.md beside this file (draft 1). Standard library only; files are read as bytes and parsed
(ast for Python docstrings and names), never executed.

usage: build_nav.py <file list> <checkout dir> <commit> <out dir>
  file list    one tracked path per line (git ls-tree -r --name-only <commit>)
  checkout dir a checkout of exactly <commit> (HEAD is checked)
"""
import ast, hashlib, io, json, os, re, subprocess, sys, time
from collections import Counter, defaultdict

CONCEPTS = {
    "dreaming": r"\bdream(s|ing)?\b",
    "recall": r"\brecall\b",
    "compaction": r"\bcompaction(s)?\b",
    "hooks": r"\bhooks?\b",
    "skills": r"\bskills?\b",
    "agents": r"\bagents?\b|\bagentic\b|\bagency\b",
    "math store": r"\bmath store\b|\bstore\b",
    "cards": r"\bcards?\b",
    "edges": r"\bedges?\b|\blinks?\b",
    "tests": r"\btests?\b|\bbenchmarks?\b|\bprobes?\b",
    "open problems": r"\bopen problems?\b|\bconjectures?\b",
    "export": r"\bexport(s|ed)?\b",
    "retrieval": r"\bretrieval\b|\bbm25\b|\bembedding(s)?\b",
    "formal verification": r"\blean\b|\bformal\b",
    "privacy": r"\bprivate\b|\bprivacy\b",
    "evaluation": r"\bevaluation\b|\bablation\b",
}
CONCEPT_RX = {k: re.compile(v, re.I) for k, v in CONCEPTS.items()}
ENTRY = {"README.md", "AGENTS_GUIDE.md", "TESTS.md", "docs/README.md", "agent_tools/README.md",
         "docs/brain-in-an-afternoon.md", "docs/architecture.md"}
SECTION_FILES = re.compile(r"(^|/)(README[^/]*\.md|AGENTS_GUIDE\.md|TESTS\.md)$", re.I)
TEXT_EXT = {"md", "py", "txt", "json", "jsonl", "toml", "yaml", "yml", "cfg", "ini", "sh", "ps1", "lean", "tex",
            "csv", "tsv", "rst", "(none)", "gitignore", "gitattributes", "js", "ts", "html", "css", "bib"}
MAX_READ = 2_000_000
AGENT_ID = re.compile(r"\b(?:claude|codex)-[0-9a-f]{8}(?:-[A-Za-z0-9]+)*\b")
TASK_ID = re.compile(r"\bT-\d{8}-\d{3}\b")
MARKET_WORD = re.compile(r"\btrading\b", re.I)


def cid(kind, path, anchor=""):
    key = kind + ":" + path + ("#" + anchor if anchor else "")
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]


def ext_of(p):
    b = p.rsplit("/", 1)[-1]
    if b.startswith(".") and b.count(".") == 1:
        return b[1:].lower()
    return b.rsplit(".", 1)[-1].lower() if "." in b else "(none)"


def slug(h):
    s = re.sub(r"[^\w\- ]", "", h.lower()).strip()
    return re.sub(r"[\s]+", "-", s)


def clip(s, n=300):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 3].rsplit(" ", 1)[0] + "..."


def strip_md(s):
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[`*>]", "", s)
    # underscores are emphasis only at a word edge; inside a name (AGENTS_GUIDE.md) they stay
    s = re.sub(r"(?<![A-Za-z0-9])_+|_+(?![A-Za-z0-9])", "", s)
    return s


def md_parse(text):
    """title, first paragraph, list of (level, heading), links"""
    title, paras, heads, cur, in_code = "", [], [], [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if m:
            heads.append((len(m.group(1)), strip_md(m.group(2)).strip()))
            if not title:
                title = heads[-1][1]
            if cur and len(paras) < 2:
                paras.append(" ".join(cur))
            cur = []
            continue
        if line.strip():
            if len(paras) < 2 and not line.lstrip().startswith(("|", "<!--")):
                cur.append(line.strip())
        elif cur and len(paras) < 2:
            paras.append(" ".join(cur))
            cur = []
    if cur and len(paras) < 2:
        paras.append(" ".join(cur))
    para = paras[0] if paras else ""
    # a short first line with no sentence end is a subtitle: carry the next paragraph with it
    if len(paras) > 1 and len(para) < 80 and not para.rstrip().endswith((".", ":", "!", "?")):
        para = para + " - " + paras[1]
    links = re.findall(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", text)
    return title, clip(strip_md(para)), heads, links


def md_sections(text):
    """(heading, first paragraph under it) for ## and ### headings"""
    out, cur_h, buf, in_code = [], None, [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^(#{2,3})\s+(.*?)\s*#*\s*$", line)
        if m:
            if cur_h:
                out.append((cur_h, buf))
            cur_h, buf = strip_md(m.group(2)).strip(), []
            continue
        if cur_h is not None:
            buf.append(line)
    if cur_h:
        out.append((cur_h, buf))
    res = []
    for h, lines in out:
        para, cur = "", []
        for l in lines:
            if l.strip() and not l.lstrip().startswith(("|", "```", "<!--", "#")):
                cur.append(l.strip())
            elif cur:
                break
        res.append((h, clip(strip_md(" ".join(cur)))))
    return res


def py_parse(text):
    try:
        tree = ast.parse(text)
    except (SyntaxError, ValueError):
        return "", "", []
    doc = ast.get_docstring(tree) or ""
    names = [n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
             and not n.name.startswith("_")]
    first = doc.strip().splitlines()[0].strip() if doc.strip() else ""
    paras = re.split(r"\n\s*\n", doc.strip()) if doc.strip() else [""]
    return first, clip(paras[0]), names


def concepts_in(s):
    return [k for k, rx in CONCEPT_RX.items() if rx.search(s)]


def main():
    flist, src, commit, out = sys.argv[1:5]
    head = subprocess.run(["git", "-C", src, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    if head != commit:
        sys.exit("checkout is at %s, not %s" % (head, commit))
    files = [l.rstrip("\n") for l in io.open(flist, encoding="utf-8") if l.strip()]
    # the map's own data files are left out: a card for cards.jsonl would describe the previous build
    own = {"navigation/cards.jsonl", "navigation/edges.jsonl", "navigation/MANIFEST.json"}
    core = sorted(f for f in files if not f.startswith(("results/", "papers/")) and f not in own)
    cards, edges, missing = {}, set(), []
    file_ids = {f: cid("file", f) for f in core}

    def dir_card(d, summary="", count=None):
        i = cid("dir", d)
        if i not in cards:
            cards[i] = dict(id=i, kind="dir", path=d, anchor="", title=d.rstrip("/").rsplit("/", 1)[-1] or d,
                            summary=summary, ext="", lines=0, keywords=[], entry=False)
        elif summary and not cards[i]["summary"]:
            cards[i]["summary"] = summary
        return i

    def parent_dir(p):
        q = p.rstrip("/")
        return q.rsplit("/", 1)[0] + "/" if "/" in q else ""

    def ensure_dirs(p):
        d = parent_dir(p)
        child = None
        while d:
            di = dir_card(d)
            if child:
                edges.add((child, di, "in_dir", ""))
            child, d = di, parent_dir(d)

    # summary cards for the two big trees: the top dir and each second-level dir, with counts only
    for big in ("results/", "papers/"):
        sub = Counter()
        for f in files:
            if f.startswith(big):
                parts = f.split("/")
                sub[big + parts[1] + "/" if len(parts) > 2 else big] += 1
        total = sum(sub.values())
        bi = dir_card(big, "%d tracked files in %d subdirectories; reached through this card and the indexes, "
                           "not carded file by file." % (total, len([s for s in sub if s != big])))
        cards[bi]["lines"] = 0
        for s, n in sorted(sub.items()):
            if s == big:
                continue
            si = dir_card(s, "%d tracked files." % n)
            exts = Counter(ext_of(f) for f in files if f.startswith(s))
            cards[si]["keywords"] = [e for e, _ in exts.most_common(4)]
            edges.add((si, bi, "in_dir", ""))

    readme_of_dir = {}
    md_links = []
    for f in core:
        p = os.path.join(src, f)
        e = ext_of(f)
        title, summary, kws, lines, heads = f.rsplit("/", 1)[-1], "", [], 0, []
        text = None
        if not os.path.isfile(p):
            missing.append(f)
        elif e in TEXT_EXT and os.path.getsize(p) <= MAX_READ:
            raw = open(p, "rb").read()
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                text = None
            if text is not None and "\x00" in text:
                text = None
            if text is not None:
                lines = text.count("\n") + (0 if text.endswith("\n") or not text else 1)
        if text is not None and e == "md":
            t, summary, heads, links = md_parse(text)
            title = t or title
            kws = [h for _, h in heads[1:13]]
            md_links.append((f, links))
            if SECTION_FILES.search(f):
                for h, para in md_sections(text):
                    a = slug(h)
                    si = cid("readme_section", f, a)
                    if si in cards:
                        continue
                    cards[si] = dict(id=si, kind="readme_section", path=f, anchor=a, title=h, summary=para,
                                     ext="md", lines=0, keywords=concepts_in(h + " " + para)[:12], entry=False)
                    edges.add((si, file_ids[f], "in_dir", ""))
            if f.rsplit("/", 1)[-1].lower().startswith("readme"):
                readme_of_dir[parent_dir(f)] = f
        elif text is not None and e == "py":
            t, summary, names = py_parse(text)
            title = t or title
            kws = names[:12]
        elif text is not None and e in ("txt", "toml", "cfg", "ini", "sh", "lean", "tex", "rst"):
            first = next((l.strip() for l in text.splitlines() if l.strip()), "")
            summary = clip(first.lstrip("#-% ").strip())
        cons = concepts_in(" ".join([f, title, summary] + [h for _, h in heads]))
        kw = []
        for k in list(kws) + cons:
            if k and k not in kw:
                kw.append(k)
        fi = file_ids[f]
        cards[fi] = dict(id=fi, kind="file", path=f, anchor="", title=clip(title, 160), summary=summary, ext=e,
                         lines=lines, keywords=kw[:12], entry=f in ENTRY)
        d = parent_dir(f)
        if d:
            edges.add((fi, dir_card(d), "in_dir", ""))
            ensure_dirs(f)
        for c in cons:
            ci = cid("concept", c)
            cards.setdefault(ci, dict(id=ci, kind="concept", path="", anchor="", title=c, summary="", ext="",
                                      lines=0, keywords=[c], entry=False))
            edges.add((fi, ci, "mentions", c))

    tracked = set(files)
    tracked_dirs = {c["path"] for c in cards.values() if c["kind"] == "dir"}
    for f, links in md_links:
        base = parent_dir(f)
        for text_, href in links:
            if re.match(r"^[a-z]+:", href) or href.startswith("#"):
                continue
            target = href.split("#", 1)[0]
            if not target:
                continue
            norm = os.path.normpath(os.path.join(base, target)).replace("\\", "/")
            if norm.startswith(".."):
                continue
            if norm in file_ids:
                dst = file_ids[norm]
            elif norm + "/" in tracked_dirs or norm.rstrip("/") + "/" in tracked_dirs:
                dst = cid("dir", norm.rstrip("/") + "/")
            else:
                continue
            note = clip(strip_md(text_), 120)
            edges.add((file_ids[f], dst, "links_to", note))
            if norm.endswith(".py") or norm.rstrip("/") + "/" in tracked_dirs:
                edges.add((file_ids[f], dst, "documents", ""))
    for d, f in readme_of_dir.items():
        if not d:
            continue  # the root README documents the whole repo; it is an entry card, not a dir edge
        edges.add((file_ids[f], cid("dir", d), "documents", ""))

    ids = set(cards)
    bad = [e for e in edges if e[0] not in ids or e[1] not in ids]
    if bad:
        sys.exit("dangling edges: %d, first %r" % (len(bad), bad[0]))
    # summaries for concept cards: how many files mention them (counts, not prose)
    men = Counter(e[1] for e in edges if e[2] == "mentions")
    for c in cards.values():
        if c["kind"] == "concept":
            c["summary"] = "Named in the title, headings or summary of %d core files." % men[c["id"]]

    # card text is copied from files; drop working labels a reader has no use for (agent and task ids)
    # and the one word the public label rule refuses, wherever a file's own prose carried them
    def scrub(s):
        s = AGENT_ID.sub("an agent", s)
        s = TASK_ID.sub("a task", s)
        return MARKET_WORD.sub(lambda m: "Market" if m.group(0)[0].isupper() else "market", s)
    for c in cards.values():
        for k in ("title", "summary"):
            c[k] = scrub(c[k])
        c["keywords"] = [scrub(str(x)) for x in c["keywords"]]
    edges = [(a, b, r, scrub(n)) for a, b, r, n in edges]

    os.makedirs(out, exist_ok=True)
    order = {"file": 0, "readme_section": 1, "dir": 2, "concept": 3}
    cl = sorted(cards.values(), key=lambda c: (order[c["kind"]], c["path"], c["anchor"]))
    el = sorted(edges, key=lambda e: (e[2], e[0], e[1], e[3]))
    cb = "".join(json.dumps(c, ensure_ascii=False, sort_keys=False) + "\n" for c in cl).encode("utf-8")
    eb = "".join(json.dumps(dict(src=a, dst=b, rel=r, note=n), ensure_ascii=False) + "\n"
                 for a, b, r, n in el).encode("utf-8")
    open(os.path.join(out, "cards.jsonl"), "wb").write(cb)
    open(os.path.join(out, "edges.jsonl"), "wb").write(eb)
    man = dict(repo="yspennstate/math-brain-public", commit=commit, schema="SCHEMA.md draft 1",
               built_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               tracked_files=len(files), core_files=len(core), missing_in_checkout=len(missing),
               cards=len(cl), cards_by_kind=dict(Counter(c["kind"] for c in cl)),
               edges=len(el), edges_by_rel=dict(Counter(e[2] for e in el)),
               sha256={"cards.jsonl": hashlib.sha256(cb).hexdigest(),
                       "edges.jsonl": hashlib.sha256(eb).hexdigest()})
    io.open(os.path.join(out, "MANIFEST.json"), "w", encoding="utf-8").write(json.dumps(man, indent=1) + "\n")
    print(json.dumps(man, indent=1))
    if missing:
        print("missing in checkout (first 10):", missing[:10])


if __name__ == "__main__":
    main()
