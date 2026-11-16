"""prior_work.py <papers/public tree> <out.md> <out.tsv> [own author surnames...]
For each mirrored paper: the abstract (what the paper claims as new), and the works it leans on most, measured by how
often each bibliography entry is cited in the body text. Everything is taken from the paper's own .tex and .bib files;
nothing is written by hand. Writes LF."""
import io, os, re, sys

root, out_md, out_tsv = sys.argv[1:4]
SELF = re.compile("|".join(re.escape(a) for a in sys.argv[4:]) or "(?!)", re.I)  # the papers' own authors: left out


def read(p):
    p = os.path.abspath(p)
    if os.name == "nt" and len(p) > 250 and not p.startswith("\\\\?\\"):
        p = "\\\\?\\" + p.replace("/", "\\")
    try:
        return io.open(p, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""


def strip_comments(t):
    return re.sub(r"(?<!\\)%[^\n]*", "", t)


def main_tex(d):
    best, score = None, -1
    for dp, dn, fn in os.walk(d):
        for f in fn:
            if not f.endswith(".tex"):
                continue
            p = os.path.join(dp, f)
            t = read(p)
            s = ("\\begin{document}" in t) * 1000000 + ("\\begin{abstract}" in t) * 100000 + len(t)
            if s > score:
                best, score = p, s
    return best


def expand_inputs(path, t, depth=0):
    if depth > 3:
        return t
    base = os.path.dirname(path)

    def rep(m):
        name = m.group(2)
        for cand in (name, name + ".tex"):
            q = os.path.join(base, cand)
            if os.path.isfile(q):
                return expand_inputs(q, strip_comments(read(q)), depth + 1)
        return ""
    return re.sub(r"\\(input|include)\{([^}]+)\}", rep, t)


def clean_text(s):
    """Text outside math: drop font commands, references and braces."""
    s = re.sub(r"\\(emph|textit|textbf|textsc|textrm|texttt|url|href)\{([^}]*)\}", r"\2", s)
    s = re.sub(r"\\(label|ref|eqref|Cref|cref|autoref|vspace|hspace)\*?\{[^}]*\}", "", s)
    s = re.sub(r"\\[vcHukrd]\s*\{\s*\\?([a-zA-Z])\s*\}", r"\1", s)
    s = re.sub(r"\\[vcHukrd] ([a-zA-Z])", r"\1", s)
    s = re.sub(r"\\(ss|ae|AE|oe|OE|o|O|l|L|i|j)\b\s?", lambda m: {"ss": "ss", "ae": "ae", "AE": "AE", "oe": "oe",
               "OE": "OE", "o": "ø", "O": "Ø", "l": "ł", "L": "Ł", "i": "i", "j": "j"}[m.group(1)], s)
    s = re.sub(r"\\(noindent|medskip|smallskip|bigskip|par|newline|newblock|url|em|it|bf|sc)\b", " ", s)
    s = s.replace("\\ ", " ").replace("\\&", "&").replace("{", "").replace("}", "")
    s = re.sub(r"\\['`\"^~]([a-zA-Z])", r"\1", s)
    return s


def clean(s, entry=False):
    s = re.sub(r"\\cite[a-zA-Z]*\*?(\[[^\]]*\])?(\[[^\]]*\])?\{[^}]*\}", "", s)
    s = s.replace("~", " ").replace("\\\\", " ")
    if entry:
        s = clean_text(s)
        s = re.sub(r"\\[a-zA-Z]+", "", s).replace("\\", "")
    else:
        s = re.sub(r"\\\[(.*?)\\\]", lambda m: "$" + m.group(1).strip() + "$", s, flags=re.S)
        s = re.sub(r"\\\((.*?)\\\)", lambda m: "$" + m.group(1).strip() + "$", s, flags=re.S)
        s = re.sub(r"\\begin\{(equation|align|gather|multline)\*?\}(.*?)\\end\{\1\*?\}",
                   lambda m: "$" + m.group(2).replace("&", "").replace("\\\\", " ").strip() + "$", s, flags=re.S)
        s = s.replace("$$", "$")
        parts = s.split("$")
        s = "$".join(clean_text(p) if i % 2 == 0 else p for i, p in enumerate(parts))
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([,.;])", r"\1", s)
    return s


def bib_entries(d, tex):
    ent = {}
    for m in re.finditer(r"\\bibitem(\[[^\]]*\])?\{([^}]+)\}(.*?)(?=\\bibitem|\\end\{thebibliography\})", tex, re.S):
        ent[m.group(2).strip()] = clean(m.group(3), True)[:240]
    for dp, dn, fn in os.walk(d):
        for f in fn:
            if f.endswith(".bib"):
                t = read(os.path.join(dp, f))
                for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", t, re.S):
                    body = m.group(2)
                    au = re.search(r"author\s*=\s*[{\"](.*?)[}\"]\s*,?\s*\n", body, re.S)
                    ti = re.search(r"title\s*=\s*[{\"](.*?)[}\"]\s*,?\s*\n", body, re.S)
                    yr = re.search(r"year\s*=\s*[{\"]?(\d{4})", body)
                    s = "%s, %s (%s)" % (clean(au.group(1), True) if au else "?", clean(ti.group(1), True) if ti else "?",
                                         yr.group(1) if yr else "n.d.")
                    ent.setdefault(m.group(1).strip(), s[:220])
    return ent


rows, tsv = [], ["paper\ttitle\tkey\tcitations\tentry"]
n_abs = n_top = 0
for name in sorted(os.listdir(root), key=str.lower):
    d = os.path.join(root, name)
    if not os.path.isdir(d):
        continue
    p = main_tex(d)
    if not p:
        continue
    tex = expand_inputs(p, strip_comments(read(p)))
    title = name
    m = re.search(r"\\title(\[[^\]]*\])?\{((?:[^{}]|\{[^{}]*\})*)\}", tex)
    if m:
        title = clean(m.group(2))
    ab = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S)
    abstract = clean(ab.group(1)) if ab else ""
    body = tex.split("\\begin{thebibliography}")[0]
    counts = {}
    for c in re.finditer(r"\\cite[a-zA-Z]*\*?(\[[^\]]*\])?(\[[^\]]*\])?\{([^}]+)\}", body):
        for k in c.group(3).split(","):
            k = k.strip()
            if k:
                counts[k] = counts.get(k, 0) + 1
    ent = bib_entries(d, tex)
    top = sorted(((v, k) for k, v in counts.items() if k in ent and not SELF.search(ent[k])), key=lambda x: (-x[0], x[1]))[:4]
    rel = os.path.relpath(p, os.path.dirname(root)).replace("\\", "/")
    rows.append("### %s\n" % title.replace("|", "/"))
    rows.append("Folder: [%s](public/%s) (source `%s`)\n" % (name, name, rel))
    if abstract:
        n_abs += 1
        rows.append("What the paper claims: %s\n" % abstract)
    if top:
        n_top += 1
        rows.append("Most cited in the text:\n")
        for v, k in top:
            rows.append("- %s (cited %d time%s)" % (ent[k], v, "" if v == 1 else "s"))
            tsv.append("%s\t%s\t%s\t%d\t%s" % (name, title.replace("\t", " "), k, v, ent[k].replace("\t", " ")))
        rows.append("")
    rows.append("")

head = ["# Prior work behind each paper", "",
        "For every paper in `public/`, its abstract and the works its text cites most often. The citation counts are a "
        "rough measure of whose results each paper rests on; the introduction and bibliography of each paper give the "
        "full account. This page is generated from the papers' own source files by `prior_work.py` in "
        "`framework/scripts`.", "",
        "%d papers, %d with an abstract found, %d with cited works matched to the bibliography." % (
            sum(1 for r in rows if r.startswith("### ")), n_abs, n_top), ""]
io.open(out_md, "w", encoding="utf-8", newline="\n").write("\n".join(head + rows).rstrip("\n") + "\n")
io.open(out_tsv, "w", encoding="utf-8", newline="\n").write("\n".join(tsv) + "\n")
print("papers", sum(1 for r in rows if r.startswith("### ")), "abstracts", n_abs, "with top cites", n_top, "tsv rows",
      len(tsv) - 1)
