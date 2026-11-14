# -*- coding: utf-8 -*-
"""Core of the paper-writing hooks W01..W50 (an agent, 12 Nov 2026).

His words, 12 Nov 2026 05:59, after Probability Theory and Related Fields declined a paper of his with the opinion that
it "does not appear to have undergone a thorough editing process": "i want 50 hoosk intorudeced for paper writting to
make sure tha tthis doe snot happening again, more editing, more auditing, less self introspeciton, it is werid, better
writting, i want more hoosk and relfexes to make sure that the papers we are wirtting are publishable as is".

Two kinds of hook (the table is pw_hooks.py):
  text hooks   read the LaTeX that is being written, compiled or pushed and fire only on something found in it; the
               line is printed with its number. No finding, no output.
  event hooks  one line each at a moment that matters (a paper is started, compiled, pushed, uploaded, submitted, or a
               referee report arrives); at most once per session per cool-down.
A call is sorted into CHANNELS:
  draft     a Write/Edit of a .tex or .bib                      -> text hooks on the text being written
  compile   pdflatex / xelatex / lualatex / latexmk / tectonic  -> text hooks on the file, event hooks
  publish   a paper pushed to GitHub, or an upload to Zenodo or ResearchGate
  submit    arXiv or a journal's submission site, or a prompt that asks to submit
  start     a prompt that asks for a paper to be written, or a new file with \\documentclass
  reject    a prompt about a rejection or a referee report
Hooks warn, never block. Fires go to fires.jsonl. The same checks run by hand: paper_lint.py <file.tex or folder>.
"""
import bisect
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STATE_DIR = os.path.join(HERE, "state")
FIRES = os.path.join(HERE, "fires.jsonl")
OWN_LIST = os.path.join(HERE, "own_papers.txt")
OWN_INDEX = os.path.join(HERE, "own_index.json")
MAX_OUT = 9000          # the harness hands the model at most 10,000 characters of one hook's output
MAX_TEX = 5000000       # a longer paper is read up to here and the output says so; a file is never skipped for size
TEXT_ON = ("draft", "compile", "publish", "submit")
# The referee's reasons (PTRF, 11 Nov 2026) were all of this kind: what the introduction says is new, in which words,
# against which earlier paper. These print right after the MUST findings and count at the push gate (W49).
INTRO_GROUP = ("W16", "W17", "W19", "W21", "W08", "W09", "W11", "W12")
MUST_TAG = "MUST: "      # a finding of a "should" hook that is a MUST in this place starts with this
# What may stand between two words of a phrase: white space, a tie, a thin space, an emphasis command, a brace or a
# comma. "The present~paper does not" and "\emph{re-derived}, line by line" are the same words as the plain phrase.
WS = r"(?:[\s~]|\\[,;]|\\(?:emph|textit|textsl|textbf|text)\{|[{},])+"
FOOT = re.compile(r"\\footnote\{(?:[^{}]|\{[^{}]*\})*\}")
ACK = re.compile(r"acknowledg|funding|thanks", re.I)

# ---------------------------------------------------------------- LaTeX reading
COMMENT = re.compile(r"(?<!\\)%.*")
MATH = re.compile(
    r"\$\$.*?\$\$|(?<!\\)\$(?:[^$\n]|\n(?!\s*\n)){0,700}?(?<!\\)\$|\\\[.*?\\\]|\\\(.*?\\\)|"
    r"\\begin\{(equation|align|gather|multline|eqnarray|displaymath|flalign|alignat|math)\*?\}.*?\\end\{\1\*?\}", re.S)
BIBENV = re.compile(r"\\begin\{thebibliography\}.*?\\end\{thebibliography\}", re.S)
SECTION = re.compile(r"\\(section|subsection|subsubsection)\*?\s*(?:\[[^\]]*\])?\{((?:[^{}]|\{[^{}]*\})*)\}")
ABBR = re.compile(r"\b(?:e\.g|i\.e|cf|et al|resp|Eq|Eqs|Fig|Figs|Thm|Sec|Lem|Prop|Cor|Def|vs|viz|a\.s|a\.e|w\.r\.t|i\.i\.d|"
                  r"p|pp|no|vol|ed|eds|St|Dr|Prof)\.|(?<=\d)\.(?=\d)|\b[A-Z]\.(?=\s[A-Z])")
DECL = re.compile(r"declar|acknowledg|generative|use of ai|ai use|funding|statement on", re.I)
CMD = re.compile(r"\\[a-zA-Z@]+\*?(?:\[[^\]]*\])?")
# A sentence ends at . ? ! followed by white space and then a capital, a command, a bracket or the end. A full stop
# inside a word (thm.main, notes.tex, w.h.p.) ends nothing.
SENT = re.compile(r"(?:[^.?!]|[.?!]+(?![\"')}\]]*(?:\s+[A-Z\\(\[`]|\s*$)))+(?:[.?!]+[\"')}\]]*)?")


def _keep_lines(m):
    return " M " + "\n" * m.group(0).count("\n")


def _blank(m):
    return "\n" * m.group(0).count("\n")


def plain(s):
    """Text of a LaTeX fragment with commands and braces removed (cites kept as the word CITE)."""
    s = re.sub(r"\\(?:cite\w*|citep|citet)\*?(?:\[[^\]]*\])*\{[^}]*\}", " CITE ", s)
    s = re.sub(r"\\(?:label|ref|eqref|cref|Cref|autoref|pageref)\{[^}]*\}", " R ", s)
    s = CMD.sub(" ", s)
    s = s.replace("{", "").replace("}", "").replace("~", " ").replace("\x01", ".")
    return re.sub(r"\s+", " ", s).strip()


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", plain(s).lower()).strip()


class Doc(object):
    def __init__(self, tex, path="", fragment=None, lmap=None, doc_only=False):
        self.path = path.replace("\\", "/")
        self.cut = len(tex) > MAX_TEX      # only the first MAX_TEX characters are read
        self.lmap = lmap                   # with \input files inlined: (file, line) of each line of this text
        self.doc_only = doc_only           # the paper around an edit: whole-paper checks only
        self.unresolved = None             # \input files that could not be found (None: not expanded)
        self.files = 1
        self.raw = tex[:MAX_TEX]
        self.nc = "\n".join(COMMENT.sub("", ln) for ln in self.raw.split("\n"))
        self.whole = "\\begin{document}" in self.nc if fragment is None else not fragment
        prose = MATH.sub(_keep_lines, self.nc)
        self.bib = [(m.start(), m.end()) for m in BIBENV.finditer(prose)]
        prose = BIBENV.sub(_blank, prose)
        if self.whole and "\\begin{document}" in prose:        # the preamble is not prose
            cut = prose.index("\\begin{document}")
            prose = "\n" * prose[:cut].count("\n") + prose[cut:]
        self.prose = prose
        # the same text, same length, with footnotes blanked: a footnote between subject and verb hides nothing
        self.flat = FOOT.sub(lambda m: "".join(c if c == "\n" else " " for c in m.group(0)), prose)
        self.lines = prose.split("\n")
        self._starts = [0]
        for ln in self.lines[:-1]:
            self._starts.append(self._starts[-1] + len(ln) + 1)
        self._sent = None
        self._secs = None
        self.words = len(re.findall(r"[A-Za-z]{2,}", plain(prose)))

    def line_of(self, pos):
        return bisect.bisect_right(self._starts, pos)

    def src(self, ln):
        """(file, line) in the source of line ln of this text."""
        if self.lmap and 1 <= ln <= len(self.lmap):
            return self.lmap[ln - 1]
        return self.path, ln

    def nc_line(self, pos):
        """Line of an offset into self.nc (the source without comments, math not masked)."""
        return self.nc.count("\n", 0, pos) + 1

    def title(self):
        m = re.search(r"\\title\s*(?:\[[^\]]*\])?\{((?:[^{}]|\{[^{}]*\})*)\}", self.nc)
        return plain(m.group(1)) if m else ""

    def sections(self):
        """[(level, title, start, end, line)] over the prose; end is the next heading of any level."""
        if self._secs is None:
            ms = list(SECTION.finditer(self.prose))
            lev = {"section": 1, "subsection": 2, "subsubsection": 3}
            out = []
            for i, m in enumerate(ms):
                end = ms[i + 1].start() if i + 1 < len(ms) else len(self.prose)
                out.append((lev[m.group(1)], plain(m.group(2)), m.end(), end, self.line_of(m.start())))
            self._secs = out
        return self._secs

    def decl_lines(self):
        """Line numbers inside an acknowledgment / declaration section, where the process may be named."""
        s = set()
        for lv, title, a, b, ln in self.sections():
            if DECL.search(title):
                s.update(range(ln, self.line_of(b) + 1))
        for m in re.finditer(r"\\begin\{(acknowledg\w*|ack|funding)\}.*?\\end\{\1\}", self.prose, re.S):
            s.update(range(self.line_of(m.start()), self.line_of(m.end()) + 1))
        for m in re.finditer(r"\\(?:paragraph|subsection|section)\*?\{[^}]*(?:" + DECL.pattern + r")[^}]*\}", self.prose,
                             re.I):
            ln = self.line_of(m.start())
            s.update(range(ln, ln + 12))
        return s

    def ack_lines(self):
        """Line numbers inside an acknowledgment or funding section only. Thanking a person there for a correction is
        ordinary; an AI declaration is not exempt from the rules on manuscript history and narrated checking."""
        s = set()
        for lv, title, a, b, ln in self.sections():
            if ACK.search(title) and not re.search(r"declar|generative|\bai\b", title, re.I):
                s.update(range(ln, self.line_of(b) + 1))
        for m in re.finditer(r"\\begin\{(acknowledg\w*|ack|funding)\}.*?\\end\{\1\}", self.prose, re.S):
            s.update(range(self.line_of(m.start()), self.line_of(m.end()) + 1))
        for m in re.finditer(r"\\(?:paragraph|subsection|section)\*?\{[^}]*(?:acknowledg|funding)[^}]*\}", self.prose, re.I):
            ln = self.line_of(m.start())
            s.update(range(ln, ln + 12))
        return s

    def intro(self):
        """(start, end) of the introduction: up to the second \\section, else the first fifth."""
        tops = [x for x in self.sections() if x[0] == 1]
        a = self.prose.find("\\begin{document}")
        a = 0 if a < 0 else a
        if len(tops) >= 2:
            return a, tops[1][2]
        return a, a + max(2000, (len(self.prose) - a) // 5)

    def sentences(self):
        """[(line, raw sentence)] of the prose; abbreviations and decimals do not end a sentence."""
        if self._sent is None:
            out = []
            body = ABBR.sub(lambda m: m.group(0).replace(".", "\x01"), self.prose)
            for para in re.finditer(r"(?:[^\n]|\n(?!\s*\n))+", body):
                for m in SENT.finditer(para.group(0)):
                    t = m.group(0).strip()
                    if len(t) > 3:
                        out.append((self.line_of(para.start() + m.start() + len(m.group(0)) - len(m.group(0).lstrip())),
                                    t.replace("\x01", ".")))
            self._sent = out
        return self._sent


def excerpt(s, n=110):
    s = re.sub(r"\s+", " ", s.replace("\x01", ".")).strip()
    return s if len(s) <= n else s[: n - 3] + "..."


_RX = {}
_CLASS = re.compile(r"(\[(?:\\.|[^\]\\])*\])")


def _compiled(pat, flags):
    """The pattern with each space widened to WS; inside a character class a space becomes white space or a tie."""
    key = (pat, flags)
    if key not in _RX:
        parts = _CLASS.split(pat)
        _RX[key] = re.compile("".join(p.replace(" ", r"\s~") if i % 2 else p.replace(" ", WS)
                                      for i, p in enumerate(parts)), flags)
    return _RX[key]


def line_hits(doc, pat, skip=None, flags=re.I):
    """One finding per line. A space in the pattern matches any run of white space, so a phrase that the source wraps
    over two lines is still found."""
    rx = _compiled(pat, flags)
    out, seen = [], set()
    for src in ((doc.prose,) if doc.flat == doc.prose else (doc.prose, doc.flat)):
        for m in rx.finditer(src):
            i = doc.line_of(m.start())
            if i in seen or (skip and i in skip):
                continue
            seen.add(i)
            out.append((i, excerpt(doc.prose[max(0, m.start() - 45): m.end() + 55])))
    return sorted(out)


# ---------------------------------------------------------------- his own earlier papers (overlap index)
def own_sources():
    out = []
    try:
        with open(OWN_LIST, encoding="utf-8") as f:
            pats = [ln.strip() for ln in f if ln.strip() and not ln.lstrip().startswith("#")]
    except OSError:
        pats = []
    for pt in pats:
        for fp in glob.glob(os.path.expanduser(pt), recursive=True)[:400]:
            if fp.lower().endswith(".tex"):
                out.append(fp.replace("\\", "/"))
    return sorted(set(out))


FUND = re.compile(r"grant agreement|supported by|funded by|funding from|research council|science foundation|"
                  r"\bERC\b|\bNSF\b|\bISF\b|\bBSF\b|gratefully|is grateful|are grateful|\bthanks?\b|acknowledg", re.I)


def sent_keys(doc, minwords=9):
    """[(line, sentence, key)] of the sentences long enough to compare. The funding and acknowledgment paragraph is
    left out: every paper of his carries the same one, and it is not reprinted mathematics."""
    out = []
    skip = doc.decl_lines()
    for ln, s in doc.sentences():
        if ln in skip or FUND.search(s):
            continue
        k = norm(s)
        real = [w for w in k.split() if w not in ("m", "r", "cite") and not w.isdigit()]   # masked math is not a word
        if len(real) >= minwords and len(real) >= 0.75 * len(k.split()) and \
                not k.startswith(("let ", "assume ", "suppose ", "then ", "proof ")):
            out.append((ln, s, hashlib.md5(k.encode("utf-8")).hexdigest()[:16]))
    return out


# A statement or a proof is mostly formulas, and masked formulas leave two or three sentences to compare: one reprinted
# lemma passed the sentence check. So theorem, lemma, proposition, corollary, claim and proof environments are also
# compared as units with the mathematics kept: the unit's tokens, in runs of five, against the units of his earlier papers.
UNIT = re.compile(r"\\begin\{(theorem|thm|lemma|lem|proposition|prop|corollary|cor|claim|proof)\*?\}"
                  r"(\s*\[(?:[^\[\]]|\[[^\]]*\])*\])?(.*?)\\end\{\1\*?\}", re.S)
TOK = re.compile(r"\\[a-zA-Z]+|[A-Za-z]+|\d+|[^\sA-Za-z\d]")
TOK_DROP = frozenset("\\left \\right \\big \\Big \\bigg \\Bigg \\bigl \\bigr \\Bigl \\Bigr \\biggl \\biggr \\displaystyle "
                     "\\quad \\qquad \\nonumber \\notag \\emph \\textit \\textbf \\text \\mathrm \\begin \\end \\qedhere "
                     "\\ { } $ & ~ , . ; : ! ( ) [ ]".split())
UNIT_NAME = {"thm": "theorem", "lem": "lemma", "prop": "proposition", "cor": "corollary"}
UNIT_MIN = 8             # sampled runs a unit needs before it is compared (about thirty tokens)
UNIT_SHARE = 0.8


def unit_list(doc):
    """[(line, environment, label, [keys])]: each theorem-like environment and proof with its sampled five-token runs."""
    out = []
    for m in UNIT.finditer(doc.nc):
        opt = m.group(2) or ""
        if "\\cite" in opt:                       # a quoted theorem of someone else, given with its source
            continue
        lab = re.search(r"\\label\{([^}]*)\}", m.group(3))
        body = re.sub(r"\\label\{[^}]*\}|\\(?:ref|eqref|cref|Cref|autoref)\{[^}]*\}", " ", m.group(3))
        toks = [t.lower() if t[0] != "\\" else t for t in TOK.findall(body) if t not in TOK_DROP]
        keys = []
        for i in range(len(toks) - 4):
            h = hashlib.md5(" ".join(toks[i:i + 5]).encode("utf-8")).hexdigest()[:10]
            if int(h[:6], 16) % 3 == 0:
                keys.append(h)
        if len(keys) >= UNIT_MIN:
            env = m.group(1).lower()
            out.append((doc.nc_line(m.start()), UNIT_NAME.get(env, env), lab.group(1) if lab else "", keys))
    return out


def unit_matches(units, lookup, share=UNIT_SHARE):
    """For each unit, the earlier unit that holds at least `share` of its runs: [(unit, earlier unit id, runs found)].
    lookup(key) -> the ids of the earlier units that hold the run."""
    out = []
    for u in units:
        votes = {}
        for k in u[3]:
            for e in set(lookup(k)):
                votes[e] = votes.get(e, 0) + 1
        if votes:
            e, c = max(votes.items(), key=lambda x: x[1])
            if c >= share * len(u[3]):
                out.append((u, e, c))
    return out


def build_own_index():
    idx = {"v": 2, "built": time.strftime("%Y-%m-%dT%H:%M:%S"), "sources": [], "keys": {}, "units": [], "runs": {}}
    for i, fp in enumerate(own_sources()):
        d = _read_doc(fp)
        if d is None or not d.whole:
            continue
        idx["sources"].append({"path": fp, "title": norm(d.title())})
        n = len(idx["sources"]) - 1
        for ln, s, k in sent_keys(d):
            got = idx["keys"].setdefault(k, [])
            if n not in got and len(got) < 4:
                got.append(n)
        for ln, env, lab, keys in unit_list(d):
            f, n2 = d.src(ln)
            idx["units"].append([n, n2, env, lab])
            u = len(idx["units"]) - 1
            for k in keys:
                got = idx["runs"].setdefault(k, [])
                if len(got) < 4 and u not in got:
                    got.append(u)
    tmp = OWN_INDEX + ".%d.tmp" % os.getpid()
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(idx, f)
    os.replace(tmp, OWN_INDEX)
    return idx


def load_own_index():
    try:
        with open(OWN_INDEX, encoding="utf-8") as f:
            return json.load(f)
    except Exception:  # noqa: BLE001
        return {"sources": [], "keys": {}}


# ---------------------------------------------------------------- a paper kept in several files
INPUT = re.compile(r"\\(?:input|include|subfile|subfileinclude)\s*\{([^{}]+)\}|"
                   r"\\(?:import|subimport|includefrom|inputfrom)\*?\s*\{([^{}]*)\}\s*\{([^{}]+)\}")


def _key(p):
    return os.path.normcase(os.path.abspath(p))


def expand(path, override=None, _depth=0, _seen=None, _root=None, _stat=None):
    """The file with \\input, \\include, \\subfile and \\import inlined, five levels deep:
    ([(file, line, text)], {"files", "missing", "chars"}); (None, stat) when the file cannot be read.
    override = {normalised path: text} stands in for files as they will be after the edit that is being judged."""
    path = path.replace("\\", "/")
    seen = set() if _seen is None else _seen
    stat = {"files": 0, "missing": 0, "chars": 0} if _stat is None else _stat
    root = _root or os.path.dirname(path)
    key = _key(path)
    if override and key in override:
        text = override[key]
    else:
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                text = f.read(MAX_TEX + 1)
        except OSError:
            return None, stat
    seen.add(key)
    stat["files"] += 1
    if _depth and "\\begin{document}" in text:          # a \subfile carries its own preamble: keep its body
        a = text.index("\\begin{document}") + len("\\begin{document}")
        b = text.find("\\end{document}", a)
        text = "\n" * text[:a].count("\n") + text[a: b if b >= 0 else len(text)]
    out = []
    for i, ln in enumerate(text.split("\n"), 1):
        m = None
        if "\\i" in ln or "\\s" in ln:
            code = COMMENT.sub("", ln)
            m = INPUT.search(code)
        if m is None or _depth >= 5 or stat["chars"] > MAX_TEX:
            out.append((path, i, ln))
            stat["chars"] += len(ln) + 1
            continue
        name = (m.group(1) or m.group(3)).strip()
        sub = (m.group(2) or "").strip()
        child = None
        for base in (os.path.join(root, sub), os.path.join(os.path.dirname(path), sub)):
            for nm in (name, name + ".tex"):
                c = os.path.join(base, nm)
                if (override and _key(c) in override) or os.path.isfile(c):
                    child = c
                    break
            if child:
                break
        got = None
        if child and child.lower().endswith(".tex") and _key(child) not in seen:
            got, _ = expand(child, override, _depth + 1, seen, root, stat)
        if got is None:
            if child is None and "#" not in name and os.path.splitext(name)[1].lower() in ("", ".tex"):
                stat["missing"] += 1
            out.append((path, i, ln))
            stat["chars"] += len(ln) + 1
            continue
        pre, post = code[:m.start()], code[m.end():]
        if pre.strip():
            out.append((path, i, pre))
        out += got
        if post.strip():
            out.append((path, i, post))
    return out, stat


# ---------------------------------------------------------------- channels
PAPERISH = re.compile(r"\.tex\b|\.pdf\b|\.bib\b|\bpapers?\b|preprint|manuscript|open[-_ ]?problems|_paper\b|paper_|"
                      r"arxiv|zenodo|researchgate", re.I)
QARG = r"(\"[^\"]+\"|'[^']+'|[^\s;&|)]+)"
GIT_PUB = re.compile(r"\bgit\s+(?:-[cC]\s+(?:\"[^\"]+\"|'[^']+'|\S+)\s+)*push\b|"
                     r"\bgh\s+(?:release\s+(?:create|upload)|repo\s+create)\b|"
                     r"\bgh\s+api\b[^;|&]{0,200}/contents/|push_paths\.sh", re.I)
GIT_C = re.compile(r"\bgit\s+(?:-c\s+\S+\s+)*-C\s+" + QARG)
GIT_ADD = re.compile(r"\bgit\s+(?:-[cC]\s+(?:\"[^\"]+\"|'[^']+'|\S+)\s+)*(add|commit)\b(.*)", re.I | re.S)
COMMIT_MSG = re.compile(r"\s-(?:m|-message)[ =]+(\"(?:[^\"\\]|\\.)*\"|'[^']*')", re.S)
BUNDLE = re.compile(r"\b(?:tar|zip|7z|Compress-Archive)\b[^;&|\n]*\.tex\b", re.I)
RUNS = r"(?:curl|wget|Invoke-WebRequest|Invoke-RestMethod|iwr|irm|requests\.\w+|(?:py|python)\S*\s+(?:-\S+\s+)*\S*)"
ZEN_ACT = re.compile(RUNS + r"[^;|&\n]{0,300}zenodo|zenodo\.org/api", re.I)
# a read of a record is not a publication: something has to be sent
ZEN_WRITE = re.compile(r"-X\s*(?:POST|PUT|PATCH)|--data\b|--data-\w+|\s-d\s|\s-F\s|--form\b|--upload-file|\s-T\s|"
                       r"requests\.(?:post|put)|actions/publish|-Method\s+(?:Post|Put)|"
                       r"\w*(?:upload|publish|new_?version|deposit)\w*\.py", re.I)
PRE = r"^\(?\s*(?:timeout\s+\S+\s+|time\s+|nice\s+(?:-n\s*\S+\s+)?|\w+=\S+\s+)*\"?(?:\S*[/\\])?"
LATEX = re.compile(PRE + r"(pdflatex|xelatex|lualatex|latexmk|tectonic)(?:\.exe)?\"?(?=\s|$)(.*)", re.I | re.S)
MAKE = re.compile(PRE + r"make(?:\.exe)?(?=\s|$)", re.I)
HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1[^\n]*\n(.*?)\n\s*\2\b", re.S)
SEG = re.compile(r"&&|\|\||[;|\n]")
DIRCMD = re.compile(r"^\(?\s*(?:cd|pushd|chdir|Push-Location|Set-Location|sl)\s+(?:-(?:Path|LiteralPath)\s+)?" + QARG + r"\s*$",
                    re.I)
# a .tex written through the shell: redirection, tee, Set-Content, sed -i, open(..., "w")
TEX_OUT = [re.compile(p, re.I) for p in (
    r">>?\s*(\"[^\"]+\.tex\"|'[^']+\.tex'|[^\s;|'\"()<>]+\.tex)(?=[\s;|)]|$)",
    r"\btee\s+(?:-a\s+)?(\"[^\"]+\.tex\"|'[^']+\.tex'|[^\s;|'\"()]+\.tex)\b",
    r"\b(?:Set-Content|Add-Content|Out-File)\b[^;|\n]*?[\s'\"]((?:[A-Za-z]:)?[^\s;|'\"()]+\.tex)\b",
    r"\bsed\s+-i\S*\s[^;|\n]*?\s(\"[^\"]+\.tex\"|'[^']+\.tex'|[^\s;|'\"()]+\.tex)(?=[\s;|)]|$)",
    r"open\(\s*r?['\"]([^'\"]+\.tex)['\"]\s*,\s*['\"][wa]")]
ABOUT = re.compile(r"brain\.py\s+(?:remember|recall|dream-about|node)|fleet_board\.py|checklist(?:_hook)?\.py|"
                   r"agent_mesh\.py|send_\w*mail\w*\.py|\bmail\.py|math_recall\.py|problem_recall\.py|mail_find\.py|"
                   r"citation_hooks[/\\]|paper_writing_hooks[/\\]|paper_lint\.py|paper_audit\.py", re.I)
UPLOADISH = re.compile(r"upload|deposit|/new\b|submit|publish|add new|add-new|create", re.I)
SUBMIT_SITE = re.compile(r"arxiv\.org/(?:submit|user)|editorialmanager\.com|submission\.springernature\.com|"
                         r"manuscriptcentral\.com|ems\.press/[^\"]{0,40}submi|msp\.org/[^\"]{0,40}submi|"
                         r"mc\.manuscriptcentral|peerreview|scholarone|easychair\.org|openreview\.net/[^\"]{0,40}submi", re.I)
P_SKIP = ("This session is being continued from a previous conversation", "Stop hook feedback:", "Loop tick",
          "<task-notification>")
P_LOOP = ("/loop", "fire this every", "fire thsi every", "fire this evey")
P_START = re.compile(r"\b(?:write|writ+ing|draft\w*|rewrit\w+|revis\w+|prepar\w+|finish\w*|polish\w*|edit\w*)\b.{0,70}"
                     r"\b(?:papers?|preprints?|manuscripts?|articles?|write-?ups?)\b|"
                     r"\b(?:papers?|preprints?|manuscripts?)\b.{0,40}\b(?:rewrit\w+|revis\w+|writ+en|polish\w*)\b", re.I)
P_SUBMIT = re.compile(r"\b(?:submit|sumbit|resubmit)\w*\b.{0,90}\b(?:journal|arxiv|annals|ptrf|transactions|papers?|"
                      r"manuscripts?|preprints?)\b|\b(?:papers?|manuscripts?)\b.{0,50}\b(?:submit|sumbit)\w*", re.I)
P_REJECT = re.compile(r"\b(?:reject\w*|regect\w*|rejction|referee\w*|reviewer'?s?|decision letter|desk[- ]reject\w*|"
                      r"declin\w+)\b", re.I)
P_REJ_WHAT = re.compile(r"papers?|journals?|publication|submission|manuscripts?|preprints?|referee|editor", re.I)


def _win(p):
    p = os.path.expanduser(p.strip("\"'"))
    if re.match(r"^/[a-zA-Z]/", p):
        p = p[1].upper() + ":" + p[2:]
    return p


def _str(x):
    if x is None:
        return ""
    if isinstance(x, str):
        return x
    try:
        return json.dumps(x, ensure_ascii=False)
    except Exception:  # noqa: BLE001
        return str(x)


def _main_tex(d, cap=3, subs=("", "paper", "papers", "tex")):
    """The .tex files in a folder (or its paper/ papers/ subfolder) that start a document. Top level only."""
    out = []
    for base in [os.path.join(d, s) if s else d for s in subs]:
        try:
            names = sorted(os.listdir(base))
        except OSError:
            continue
        for n in names[:300]:
            if n.lower().endswith(".tex"):
                fp = os.path.join(base, n)
                try:
                    with open(fp, encoding="utf-8", errors="replace") as fh:
                        if "\\documentclass" in fh.read(6000):
                            out.append(fp.replace("\\", "/"))
                except OSError:
                    pass
            if len(out) >= cap:
                return out
    return out


def _read_doc(fp, override=None, **kw):
    """The paper that starts at fp, with its \\input files inlined. None only when fp cannot be read."""
    got, stat = expand(fp, override)
    if got is None:
        return None
    d = Doc("\n".join(t for _, _, t in got), fp, lmap=[(f, n) for f, n, _ in got] if stat["files"] > 1 else None, **kw)
    d.unresolved = stat["missing"]
    d.files = stat["files"]
    return d


def paper_sha(fp):
    """sha256 of the paper as it is read (its \\input files inlined): what an audit record is tied to. "" when unreadable."""
    got, _ = expand(fp)
    if got is None:
        return ""
    return hashlib.sha256("\n".join(t for _, _, t in got).encode("utf-8", "replace")).hexdigest()


def find_main(fp, override=None):
    """The file that starts the document a fragment belongs to: a .tex with \\documentclass, in the fragment's folder
    or one of the two above it, whose \\input tree reaches the fragment."""
    key = _key(fp)
    if not override and key in _FOUND:
        return _FOUND[key]
    d = os.path.dirname(os.path.abspath(fp))
    got = None
    for _ in range(3):
        for m in _main_tex(d, 8, ("",)):
            if _key(m) == key:
                continue
            seen = None if override else _MEMBERS.get(_key(m))
            if seen is None:                       # one read of a main file's \input tree serves every file in it
                seen = set()
                expand(m, override, 0, seen)
                if not override:
                    _MEMBERS[_key(m)] = seen
            if key in seen:
                got = m
                break
        up = os.path.dirname(d)
        if got or up == d:
            break
        d = up
    if not override:
        _FOUND[key] = got
    return got


_MEMBERS, _FOUND = {}, {}                          # per process: a hook run is one process


def _after_edit(fp, ti):
    """The file's text as it will stand after this Edit or MultiEdit; None when that cannot be worked out."""
    try:
        if os.path.getsize(fp) > MAX_TEX:
            return None
        with open(fp, encoding="utf-8", errors="replace") as f:
            t = f.read()
    except OSError:
        return None
    for e in [ti] + [e for e in ti.get("edits") or [] if isinstance(e, dict)]:
        old, new = e.get("old_string"), e.get("new_string")
        if not isinstance(old, str) or not isinstance(new, str) or not old:
            continue
        if old not in t:
            return None
        t = t.replace(old, new) if e.get("replace_all") else t.replace(old, new, 1)
    return t


def _paper_around(fp, new_text):
    """The whole paper as it will stand once fp holds new_text, for the whole-paper checks; None when fp is not part
    of a paper that can be found."""
    ov = {_key(fp): new_text}
    main = fp if "\\begin{document}" in new_text else find_main(fp, ov)
    if not main:
        return None
    return _read_doc(main, ov, doc_only=True)


def _ours(fp):
    """A file of the hooks themselves (their tests hold every banned sentence)."""
    k = _key(fp).replace("\\", "/")
    return k.startswith(_key(HERE).replace("\\", "/") + "/") or "/citation_hooks/" in k or \
        "/dreaming/paper_writing_hooks/" in k


def _git(d, *args):
    """stdout of one quick git call in d; None when git fails or is slow."""
    try:
        r = subprocess.run(["git", "-C", d] + list(args), capture_output=True, timeout=6,
                           creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else None
    except Exception:  # noqa: BLE001
        return None


def _outgoing(d, added):
    """The papers a push from d sends out: main .tex files among the files that differ from the upstream branch, plus
    what `git add <path>` / `git commit -a` in the same command is about to add. [] when d is no git repository."""
    top = (_git(d, "rev-parse", "--show-toplevel") or "").strip()
    if not top:
        if not os.path.exists(os.path.join(d, ".git")):
            return []
        # a repository git could not answer for in time: the papers one folder down that were touched last
        found = []
        try:
            subs = [os.path.join(d, n) for n in sorted(os.listdir(d))[:400]]
        except OSError:
            subs = []
        for s in subs:
            if os.path.isdir(s) and not os.path.basename(s).startswith("."):
                found += _main_tex(s, 1, ("", "paper"))
        found.sort(key=lambda f: -os.path.getmtime(f))
        return found[:3]
    names = set()
    out = _git(d, "diff", "--name-only", "@{u}..HEAD")
    if out is None:
        out = _git(d, "diff", "--name-only", "HEAD~1..HEAD")
    names.update((out or "").split("\n"))
    names.update((_git(d, "diff", "--name-only", "--cached") or "").split("\n"))
    for here, spec in added[:6]:
        names.update((_git(here, "diff", "--name-only", "--", spec) or "").split("\n"))
        names.update((_git(here, "ls-files", "-o", "--exclude-standard", "--full-name", "--", spec) or "").split("\n"))
    mains, seen = [], set()
    for n in sorted(x.strip() for x in names if x.strip().lower().endswith((".tex", ".bbl", ".bib", ".pdf")))[:60]:
        fp = os.path.join(top, n)
        if n.lower().endswith(".tex") and os.path.isfile(fp):
            try:
                with open(fp, encoding="utf-8", errors="replace") as fh:
                    cand = [fp] if "\\documentclass" in fh.read(6000) else [find_main(fp)]
            except OSError:
                cand = []
        else:
            cand = _main_tex(os.path.dirname(fp), 1, ("",))
        for m in cand:
            if m and _key(m) not in seen and not _ours(m):
                seen.add(_key(m))
                mains.append(m.replace("\\", "/"))
    return mains


def _patch(patch, cwd, ch, ctx):
    """Codex apply_patch: every .tex or .bib file in the patch, each with its own added lines."""
    parts = re.split(r"^\*\*\* (Add|Update) File: (.+?)\s*$", patch, flags=re.M)
    first = ""
    for i in range(1, len(parts) - 2 + 1, 3):
        kind, name, body = parts[i], parts[i + 1].strip(), parts[i + 2]
        if not name.lower().endswith((".tex", ".bib")):
            continue
        fp = _win(name).replace("\\", "/")
        if not os.path.isabs(fp):
            fp = os.path.join(cwd, fp).replace("\\", "/")
        if _ours(fp):
            continue
        text = "\n".join(ln[1:] for ln in body.split("\n") if ln.startswith("+") and not ln.startswith("+++"))
        whole = kind.lower() == "add" and "\\documentclass" in text[:6000]
        ch.add("draft")
        ctx["docs"].append(Doc(text, fp, fragment=not whole))
        if not first:
            first = fp
            ctx["dir"] = os.path.dirname(fp)
        if whole:
            ch.add("start")
            ctx["new"] = True
    return ch, first or patch[:200], ctx


def _add_doc(ctx, fp, **kw):
    if any(_key(d.path) == _key(fp) for d in ctx["docs"]):
        return True
    doc = _read_doc(fp, **kw) if os.path.isfile(fp) else None
    if doc:
        ctx["docs"].append(doc)
    return bool(doc)


_HIDE = {ord(";"): 1, ord("|"): 2, ord("&"): 3, ord("\n"): 4}
_SHOW = {1: ";", 2: "|", 3: "&", 4: "\n"}


def _shell(p, ti, ch, ctx):
    """A shell command, read one segment at a time: the folder it runs in (cd, pushd, Set-Location, git -C), a compile,
    a push or an upload, an archive of the source, a .tex written by redirection or sed."""
    command = ti.get("command") or ti.get("cmd") or ti.get("script") or ti.get("x") or ""
    if isinstance(command, (list, tuple)):         # Codex: ["bash", "-lc", "<the command>"] or an argv
        command = [str(x) for x in command]
        command = command[-1] if len(command) >= 3 and command[1].startswith(("-", "/")) else " ".join(command)
    command = str(command)
    d = str(ti.get("workdir") or ti.get("cwd") or p.get("cwd") or os.getcwd())
    if "*** Begin Patch" in command:
        return _patch(command, d, ch, ctx)
    bare = HEREDOC.sub(" ", command)
    # a commit message may hold ; | & itself (the chained message is the one W56 is for): keep it in one segment
    bare = COMMIT_MSG.sub(lambda m: m.group(0).translate(_HIDE), bare)
    pushes, added = [], []
    for seg in SEG.split(bare):
        seg = seg.strip()
        if not seg:
            continue
        m = DIRCMD.match(seg)
        if m:
            nd = _win(m.group(1))
            d = nd if os.path.isabs(nd) else os.path.join(d, nd)
            continue
        if ABOUT.search(seg):                      # a mesh, checklist, brain or mail command that mentions a paper
            continue
        here = d
        m = GIT_C.search(seg)
        if m:
            nd = _win(m.group(1))
            here = nd if os.path.isabs(nd) else os.path.join(d, nd)
        m = LATEX.match(seg)
        if m:
            ch.add("compile")
            ctx["dir"] = here
            toks = [t.strip("\"')") for t in m.group(2).split() if not t.startswith("-")]
            cand = [t for t in toks if t.lower().endswith(".tex")] or toks[-1:]
            ok = False
            for t in cand[:2]:
                fp = _win(t)
                if not fp.lower().endswith(".tex"):
                    fp += ".tex"
                if not os.path.isabs(fp):
                    fp = os.path.join(here, fp)
                ok = _add_doc(ctx, fp) or ok
            if not ok:
                for f in _main_tex(here, 1):
                    _add_doc(ctx, f)
            continue
        if MAKE.match(seg):
            mains = _main_tex(here, 1)
            if mains:
                ch.add("compile")
                ctx["dir"] = here
                _add_doc(ctx, mains[0])
            continue
        m = GIT_ADD.search(seg)
        if m:
            rest = COMMIT_MSG.sub(" ", m.group(2))
            if m.group(1).lower() == "add" or re.search(r"\s-\w*a|\s--all\b", rest):
                specs = [t.strip("\"'") for t in rest.split() if not t.startswith("-")] or ["."]
                added += [(here, s) for s in specs[:4]]
            mm = COMMIT_MSG.search(m.group(2)) if m.group(1).lower() == "commit" else None
            if mm and (_main_tex(here, 1) or PAPERISH.search(os.path.basename(here.replace("\\", "/").rstrip("/")))):
                ch.add("commit")
                ctx["commit_msg"] = mm.group(1)[1:-1].translate(_SHOW)
                ctx["dir"] = here
        if GIT_PUB.search(seg):
            pushes.append((here, seg))
        if BUNDLE.search(seg):                     # the arXiv upload bundle
            ch.add("publish")
            ctx["dir"] = here
            ok = False
            for t in re.findall(r"[^\s\"']+\.tex\b", seg)[:3]:
                fp = _win(t)
                ok = _add_doc(ctx, fp if os.path.isabs(fp) else os.path.join(here, fp)) or ok
            if not ok:
                for f in _main_tex(here, 1):
                    _add_doc(ctx, f)
        if ZEN_ACT.search(seg) and ZEN_WRITE.search(seg):
            ch.add("publish")
    for here, seg in pushes:
        if "push_paths.sh" in seg:                 # the files are named on the line, relative to the repository
            toks = [t.strip("\"'") for t in seg.split()]
            repo = next((t for t in toks if os.path.isdir(_win(t))), here)
            mains = []
            for t in toks:
                if t.lower().endswith(".tex"):
                    for base in ("", _win(repo), here):
                        fp = os.path.join(base, _win(t)) if base else _win(t)
                        if os.path.isfile(fp):
                            mains.append(fp if "\\documentclass" in _head(fp) else find_main(fp) or fp)
                            break
        else:
            mains = _outgoing(here, added) or _main_tex(here)
        name = os.path.basename(here.replace("\\", "/").rstrip("/"))
        if mains or (re.search(r"\.tex\b|\.pdf\b", bare, re.I) and
                     (PAPERISH.search(name) or re.search(r"\.tex\b|\bpapers?/|preprint|manuscript", bare, re.I))):
            ch.add("publish")
            ctx["dir"] = here
            for f in mains[:3]:
                if not _ours(f):
                    _add_doc(ctx, f)
            if len(mains) > 3:
                ctx["more"] = [os.path.basename(os.path.dirname(f)) + "/" + os.path.basename(f) for f in mains[3:]]
    # LaTeX written through the shell: the text is in the command (a heredoc body, a sed script, a string)
    for rx in TEX_OUT:
        m = rx.search(command)
        if not m:
            continue
        fp = _win(m.group(1))
        if not os.path.isabs(fp):
            fp = os.path.join(d, fp)
        if _ours(fp):
            break
        text = "\n\n".join(h.group(3) for h in HEREDOC.finditer(command)) or command
        ch.add("draft")
        ctx["dir"] = ctx["dir"] or os.path.dirname(fp)
        ctx["docs"].append(Doc(text, fp.replace("\\", "/"), fragment=True))
        break
    ctx["dir"] = ctx["dir"] or d
    return ch, command[:200], ctx


def _head(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read(6000)
    except OSError:
        return ""


def channels(p):
    """-> (set of channels, short text for the log, ctx) with ctx = {"docs": [Doc], "dir": str, "new": bool}."""
    ev = str(p.get("hook_event_name") or "")
    tool = str(p.get("tool_name") or "")
    ti = p.get("tool_input") or {}
    if not isinstance(ti, dict):
        ti = {"x": _str(ti)}
    ch = set()
    ctx = {"docs": [], "dir": "", "new": False}
    if not tool and ev not in ("PreToolUse",):
        t = str(p.get("prompt") or "")
        tl = t.lstrip()
        if tl.startswith(P_SKIP) or tl.lower().startswith(P_LOOP):
            return ch, "", ctx
        if len(t) < 4000:
            if P_REJECT.search(t) and P_REJ_WHAT.search(t):
                ch.add("reject")
            if P_SUBMIT.search(t):
                ch.add("submit")
            if P_START.search(t):
                ch.add("start")
        return ch, t[:200], ctx
    if tool in ("Bash", "PowerShell", "shell_command", "exec_command", "shell", "local_shell", "container.exec"):
        return _shell(p, ti, ch, ctx)
    if tool.startswith("mcp__claude-in-chrome__") or tool.startswith("mcp__Claude_Browser__"):
        blob = json.dumps(ti, ensure_ascii=False).lower()
        if ("zenodo.org" in blob or "researchgate.net" in blob) and UPLOADISH.search(blob):
            ch.add("publish")
        if SUBMIT_SITE.search(blob):
            ch.add("submit")
        return ch, blob[:200], ctx
    if tool == "apply_patch":                      # Codex: the file names and the added lines are inside the patch
        patch = "\n".join(str(x) for v in ti.values() for x in (v if isinstance(v, (list, tuple)) else [v])
                          if isinstance(x, str))
        return _patch(patch, str(p.get("cwd") or os.getcwd()), ch, ctx)
    if tool in ("Write", "Edit", "MultiEdit"):
        fp = str(ti.get("file_path") or ti.get("path") or "").replace("\\", "/")
        low = fp.lower()
        if _ours(fp):
            return ch, fp, ctx
        if os.path.basename(low) in ("readme.md", "readme.txt", "readme", "readme.rst"):
            # the README of a paper's repository is read by the same people as the paper: the line checks apply
            dd = os.path.dirname(fp)
            if not (_main_tex(dd, 1) or _main_tex(os.path.dirname(dd), 1, ("",))):
                return ch, fp, ctx
            body = str(ti.get("content") or ti.get("new_string") or "")
            for e in ti.get("edits") or []:
                if isinstance(e, dict):
                    body += "\n\n" + str(e.get("new_string") or "")
            ch.add("draft")
            ctx["dir"] = dd
            ctx["docs"] = [Doc(body, fp, fragment=True)]
            return ch, fp, ctx
        if not low.endswith((".tex", ".bib")):
            return ch, fp, ctx
        ch.add("draft")
        ctx["dir"] = os.path.dirname(fp)
        if tool == "Write":
            body = new_text = str(ti.get("content") or "")
            ctx["docs"] = [Doc(body, fp)]
            if "\\documentclass" in body[:6000] and not os.path.exists(fp):
                ch.add("start")
                ctx["new"] = True
        else:
            body = str(ti.get("new_string") or "")
            for e in ti.get("edits") or []:
                if isinstance(e, dict):
                    body += "\n\n" + str(e.get("new_string") or "")
            body += str(ti.get("patch") or "")
            ctx["docs"] = [Doc(body, fp, fragment=True)]
            new_text = _after_edit(fp, ti)
        # The text being written gets the line checks. The whole-paper checks (labels before their definition, one
        # object under several names, the comparison with earlier work, reprinted lemmas) need the paper around it:
        # the file as it will stand, inside the main file that \input's it.
        if low.endswith(".tex") and new_text is not None:
            try:
                around = _paper_around(fp, new_text)
            except Exception:  # noqa: BLE001
                around = None
            if around is not None and around.whole:
                if ctx["docs"][0].whole and around.files == 1:
                    pass                                   # a Write of a one-file paper: already read whole
                elif ctx["docs"][0].whole:
                    around.doc_only = False
                    ctx["docs"] = [around]                 # a Write of the main file of a paper in several files
                else:
                    ctx["docs"].append(around)
        return ch, fp, ctx
    return ch, "", ctx


# ---------------------------------------------------------------- decide and render
def scan(h, docs):
    """Findings of one text hook over the documents: [(path, line, excerpt)]."""
    out = []
    for d in docs:
        if h["kind"] == "doc" and not d.whole:
            continue
        if d.doc_only and h["kind"] != "doc":
            continue
        if d.path.lower().endswith(".bib") and not h.get("bib"):
            continue
        try:
            if h.get("fn"):
                got = h["fn"](d)
            else:
                skip = d.decl_lines() if h.get("skip_decl") else d.ack_lines() if h.get("skip_ack") else None
                got = line_hits(d, h["pat"], skip)
        except Exception as e:  # noqa: BLE001
            # a check that could not run is a finding, not a pass: the count at the gate must not come out lower
            sys.stderr.write("[paper-writing hooks] %s failed on %s: %s\n" % (h["id"], d.path, e))
            out.append((d.path, 0, "%sthis check could not run (%s: %s): read the file for it by hand"
                        % (MUST_TAG, type(e).__name__, excerpt(str(e), 60))))
            continue
        if len(got) >= h.get("min", 1):
            for ln, ex in got:
                if d.lmap and ln:                          # a line of an \input file: name the file, give its line
                    f, ln = d.src(ln)
                    if _key(f) != _key(d.path):
                        tag = os.path.basename(f) + ": "
                        ex = MUST_TAG + tag + ex[len(MUST_TAG):] if ex.startswith(MUST_TAG) else tag + ex
                out.append((d.path, ln, ex))
    return out


def must_n(h, found):
    """How many of a hook's findings are MUST: all of them for a MUST hook, the tagged ones otherwise."""
    return len(found) if h.get("must") else sum(1 for x in found if str(x[-1]).startswith(MUST_TAG))


def rank(h, found):
    """Print order: MUST, then the introduction group, then the rest."""
    return 0 if must_n(h, found) else 1 if h["id"] in INTRO_GROUP else 2


def decide(p, hooks, now=None, state=None, pre=None):
    now = time.time() if now is None else now
    state = {} if state is None else state
    ch, text, ctx = pre or channels(p)
    if not ch:
        return [], ch, text, ctx
    out = []
    leaving = bool(ch.intersection(("publish", "submit")))
    paper = "+".join(sorted(os.path.basename(os.path.dirname(d.path)) + "/" + os.path.basename(d.path)
                            for d in ctx["docs"] if d.path))[:200] or ctx.get("dir") or ""
    for h in hooks:
        if h["kind"] == "event":
            if not ch.intersection(h["on"]):
                continue
            ev = None
            chk = h.get("check")
            if chk is not None:
                try:
                    ev = chk(ch, p, ctx)
                except Exception as e:  # noqa: BLE001
                    ev = "this check could not run (%s): do it by hand" % type(e).__name__
                if not ev:
                    continue
            # one line per paper, not per session: the second paper pushed in a session gets its own gate. A hook
            # with a check speaks for as long as what it checks stands.
            key = h["id"] + "|" + paper
            cool = 0 if chk is not None and leaving else h.get("cool", 3600)
            found = [("", 0, ev)] if isinstance(ev, str) else []
        else:
            if not ctx["docs"] or not ch.intersection(TEXT_ON):
                continue
            found = scan(h, ctx["docs"])
            if not found:
                continue
            # the cool-down is on the finding, not on the hook: a new sentence is always reported, an old one is not
            # repeated for ten minutes; when the paper is leaving, everything is shown
            cool = h.get("cool", 600)
            fresh = []
            for f in found:
                k = "%s|%s|%s" % (h["id"], os.path.basename(f[0]) or "frag",
                                  hashlib.md5(str(f[2]).encode("utf-8", "replace")).hexdigest()[:10])
                last = state.get(k)
                if leaving or not (isinstance(last, (int, float)) and now - last < cool):
                    fresh.append(f)
                state[k] = now if k not in state or f in fresh else state[k]
            if fresh:
                out.append((h, fresh))
            continue
        last = state.get(key)
        if isinstance(last, (int, float)) and now - last < cool:
            continue
        state[key] = now
        out.append((h, found))
    return out, ch, text, ctx


def render(fired, ch, ctx, total):
    text = [(h, f) for h, f in fired if h["kind"] != "event"]
    events = [(h, f) for h, f in fired if h["kind"] == "event"]
    names = sorted(set(os.path.basename(d.path) for d in ctx["docs"] if d.path))
    lines = ["[paper-writing hooks] %d of the %d fired on %s%s (his 12 Nov order after a journal declined a paper as not "
             "thoroughly edited: a paper leaves here publishable as is)."
             % (len(fired), total, "+".join(sorted(ch)), (" - " + ", ".join(names)) if names else "")]
    gates = [(h, f) for h, f in events if h.get("check") is not None]      # first, so a cut never removes them
    events = [(h, f) for h, f in events if h.get("check") is None]
    for h, found in gates:
        lines.append("  [%s | %s] %s NOW: %s" % (h["id"], h["title"], h["rule"], found[0][2] if found else ""))
    if ctx.get("more"):
        lines.append("  this push also carries %d more paper(s) that were not read here: %s; run paper_lint.py on each"
                     % (len(ctx["more"]), ", ".join(ctx["more"][:6])))
    if text or ch.intersection(("publish", "submit")):
        lines.append("  These checks know a list of wordings. A paper they pass has none of the listed wordings; it has "
                     "not been read. The reading is the audit (W43).")
    if text:
        lines.append("FOUND IN THE TEXT (each is a line of the file, not a reminder; fix it, or say in your report why it "
                     "stands):")
        text.sort(key=lambda x: (rank(*x), x[0]["id"]))
        for h, found in text[:14]:
            found = sorted(found, key=lambda x: 0 if str(x[2]).startswith(MUST_TAG) else 1)
            ex = "; ".join("l.%d \"%s\"" % (ln, e) if ln else e for _, ln, e in found[:2])
            more = "" if len(found) <= 2 else " (+%d more)" % (len(found) - 2)
            kind = "MUST" if must_n(h, found) else "introduction" if h["id"] in INTRO_GROUP else "should"
            lines.append("  [%s %s | %s] %s%s -- %s" % (h["id"], kind, h["title"], ex, more, h["rule"]))
        for d in ctx["docs"]:
            if d.cut:
                lines.append("  %s is longer than %d characters: only that much of it was read" % (
                    os.path.basename(d.path), MAX_TEX))
            if d.unresolved:
                lines.append("  %s: %d \\input file(s) were not found, so part of the paper was not read" % (
                    os.path.basename(d.path), d.unresolved))
        if len(text) > 14:
            lines.append("  ... and %d more hooks with findings: %s" % (len(text) - 14, ", ".join(h["id"] for h, _ in text[14:])))
        if names:
            lines.append("  every finding with its line: python ~/.claude/dreaming/paper_writing_hooks/"
                         "paper_lint.py \"%s\"" % ctx["docs"][0].path)
    for h, found in events:
        ev = found[0][2] if found else ""
        lines.append("  [%s | %s] %s%s" % (h["id"], h["title"], h["rule"], (" NOW: " + ev) if ev else ""))
    out = "\n".join(lines)
    if len(out) > MAX_OUT:
        out = out[: MAX_OUT - 80] + "\n  ... cut; run paper_lint.py on the file for the rest"
    return out


def _state_path(session):
    return os.path.join(STATE_DIR, re.sub(r"[^\w.-]", "_", session)[:80] + ".json")


def _load_state(session):
    try:
        with open(_state_path(session), encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except Exception:  # noqa: BLE001
        return {}


def _save_state(session, d):
    try:
        os.makedirs(STATE_DIR, exist_ok=True)
        path = _state_path(session)
        tmp = path + ".%d.tmp" % os.getpid()
        old = time.time() - 2 * 86400
        d = {k: v for k, v in d.items() if not isinstance(v, (int, float)) or v > old}
        try:
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(d, f)
            os.replace(tmp, path)
        finally:
            if os.path.exists(tmp):
                os.remove(tmp)
    except Exception:  # noqa: BLE001
        pass


def run_payload(raw, hooks_loader):
    try:
        p = json.loads(raw or "{}")
    except Exception:  # noqa: BLE001
        return "", {}
    if not isinstance(p, dict):
        return "", {}
    pre = channels(p)
    if not pre[0]:
        return "", p
    session = str(p.get("session_id") or p.get("sessionId") or "unknown")
    hooks = hooks_loader()
    st = _load_state(session)
    fired, ch, text, ctx = decide(p, hooks, state=st, pre=pre)
    if not fired:
        return "", p
    _save_state(session, st)
    try:
        with open(FIRES, "a", encoding="utf-8") as f:
            f.write(json.dumps({"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "session": session, "channels": sorted(ch),
                                "ids": [h["id"] for h, _ in fired], "n": [len(x) for _, x in fired],
                                "text": text[:160]}, ensure_ascii=False) + "\n")
    except Exception:  # noqa: BLE001
        pass
    return render(fired, ch, ctx, len(hooks)), p
