# -*- coding: utf-8 -*-
"""pw1k: one thousand paper-writing rules, P0001..P1000 (an agent, 12 Nov 2026).

Written at the author's request.

Beside pw_core.py / pw_hooks.py (W01..W50, an agent); nothing of theirs is imported or changed.
Tables: pw1k_terms.py (word clusters, math-notation clusters), pw1k_rules.py (text rules, detectors, event lines).

  python pw1k.py lint <file.tex|folder> [--chapter terms] [--max 60]   every finding, with line numbers
  python pw1k.py notation <file.tex> [--write out.tex]                  notation and terminology table: build, check
  python pw1k.py hook [--codex]                                         hook entry (payload on stdin); warns, never blocks
  python pw1k.py list [--md FILE]                                       the thousand rules
  python pw1k.py selftest
"""
import bisect, io, json, os, re, sys, time, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
STATE_DIR = os.path.join(HERE, "state")
FIRES = os.path.join(HERE, "pw1k_fires.jsonl")
MAX_OUT, COOL_S, TOP = 1200, 2700, 5
HOOK_S = 6.0       # seconds the hook spends on one file; the heavier rules run first
MAX_DOC = 400000  # bytes; a larger file is data pasted into a paper, and the hook leaves it to the command line
SELF = "python ~/.claude/dreaming/paper_writing_hooks/pw1k.py"

# ---------------------------------------------------------------- loading
_ACC = {"'": "\u0301", "`": "\u0300", "^": "\u0302", '"': "\u0308", "~": "\u0303", "=": "\u0304", ".": "\u0307",
        "H": "\u030b", "c": "\u0327", "v": "\u030c", "u": "\u0306", "k": "\u0328", "r": "\u030a"}
_ACC1 = re.compile(r"""\{?\\(['`^"~=.])\s*\{?\\?([A-Za-z])\}?\}?""")
_ACC2 = re.compile(r"\{?\\([Hcvukr])(?:\s*\{\\?([A-Za-z])\}|\s+([A-Za-z])(?![A-Za-z]))\}?")
_SPEC = {r"\o": "\u00f8", r"\O": "\u00d8", r"\l": "\u0142", r"\L": "\u0141", r"\ss": "\u00df", r"\aa": "\u00e5",
         r"\ae": "\u00e6", r"\i": "i"}
_SPEC_RX = re.compile(r"\{?\\(o|O|l|L|ss|aa|ae)(?![A-Za-z])\s?\}?")
_COMMENT = re.compile(r"(?<!\\)%.*$")
_INPUT = re.compile(r"\\(?:input|include|subfile)\{([^}]+)\}")


def _acc(m):
    letter = m.group(2) or (m.group(3) if m.lastindex and m.lastindex >= 3 else None)
    return unicodedata.normalize("NFC", letter + _ACC[m.group(1)])


def norm_line(s):
    if "\\" not in s:
        return s
    s = _ACC1.sub(_acc, s)
    s = _ACC2.sub(_acc, s)
    return _SPEC_RX.sub(lambda m: _SPEC["\\" + m.group(1)], s)


def load_lines(path, seen=None, depth=0):
    seen = seen if seen is not None else set()
    ap = os.path.abspath(path)
    if ap in seen or depth > 6 or not os.path.isfile(ap):
        return []
    seen.add(ap)
    out = []
    with io.open(ap, encoding="utf-8", errors="replace") as f:
        for n, line in enumerate(f, 1):
            line = _COMMENT.sub("", line.rstrip("\r\n"))
            m = _INPUT.search(line)
            if m:
                sub = m.group(1).strip()
                cand = os.path.join(os.path.dirname(ap), sub if sub.endswith(".tex") else sub + ".tex")
                got = load_lines(cand, seen, depth + 1)
                if got:
                    out.extend(got)
                    continue
            out.append((norm_line(line), os.path.basename(ap), n))
    return out


# ---------------------------------------------------------------- the document
_MATH = re.compile(
    r"\\begin\{(equation|align|gather|multline|eqnarray|displaymath|flalign|alignat|math)(\*?)\}.*?\\end\{\1\2\}"
    r"|(?<!\\)\\\[.*?(?<!\\)\\\]|(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\\\(.*?(?<!\\)\\\)|(?<!\\)\$.*?(?<!\\)\$", re.S)
_VERB = re.compile(r"\\begin\{(verbatim|lstlisting|minted|comment)\}.*?\\end\{\1\}", re.S)
_ARGCMD = re.compile(
    r"\\(?:(cite[a-zA-Z]*)|(ref|eqref|[cC]ref|autoref|pageref)|label|bibitem|url|href|includegraphics|input|include"
    r"|bibliography|bibliographystyle|usepackage|documentclass|hypersetup|email|address|thanks|begin|end|vspace"
    r"|hspace|setcounter|newtheorem|numberwithin|theoremstyle|pagestyle|subjclass|keywords|date)\*?"
    r"(?:\[[^\]\n]*\])*(?:\{[^{}\n]*\})+")
_CMD = re.compile(r"\\[A-Za-z@]+\*?")
_ESC = re.compile(r"\\(.)")
_THM_DEFAULT = {"theorem": "theorem", "thm": "theorem", "lemma": "lemma", "lem": "lemma", "proposition": "proposition",
                "prop": "proposition", "corollary": "corollary", "cor": "corollary", "definition": "definition",
                "defn": "definition", "defi": "definition", "conjecture": "conjecture", "conj": "conjecture",
                "claim": "claim", "remark": "remark", "rem": "remark", "example": "example",
                "assumption": "assumption", "fact": "fact", "observation": "observation", "question": "question",
                "problem": "problem"}
_STATEMENT = {"theorem", "lemma", "proposition", "corollary", "conjecture", "claim", "definition", "assumption", "fact"}
_EQENV = {"equation", "align", "gather", "multline", "eqnarray", "flalign", "alignat"}


def _blank(s):
    return re.sub(r"[^\n]", " ", s)


def _brace_end(s, i):
    """s[i] == '{': index after the matching '}' (or len)."""
    d = 0
    for j in range(i, len(s)):
        c = s[j]
        if c == "{" and (j == 0 or s[j - 1] != "\\"):
            d += 1
        elif c == "}" and s[j - 1] != "\\":
            d -= 1
            if d == 0:
                return j + 1
    return len(s)


class Doc(object):
    def __init__(self, path=None, text=None, name="text.tex"):
        if path:
            L = load_lines(path)
            name = os.path.basename(path)
        else:
            L = [(norm_line(_COMMENT.sub("", l)), name, n) for n, l in enumerate(text.split("\n"), 1)]
        self.name, self.path = name, path
        self.multi = len(set(f for _, f, _ in L)) > 1
        self.orig = [(f, n) for _, f, n in L]
        raw = "\n".join(t for t, _, _ in L)
        raw = _VERB.sub(lambda m: _blank(m.group(0)), raw)
        self.raw = raw
        self.starts = [0]
        for t, _, _ in L:
            self.starts.append(self.starts[-1] + len(t) + 1)
        pr, ma, last = [], [], 0
        self.mspans = []
        for m in _MATH.finditer(raw):
            a, b = m.span()
            g = m.group(0)
            self.mspans.append((a, b, not g.startswith(("$", "\\(")) or g.startswith("$$")))
            pr.append(raw[last:a]); ma.append(_blank(raw[last:a]))
            pr.append("\x01" + _blank(g[1:])); ma.append(g)
            last = b
        pr.append(raw[last:]); ma.append(_blank(raw[last:]))
        self.math = "".join(ma)
        p = "".join(pr)
        p = _ARGCMD.sub(lambda m: ("\x02" if m.group(1) in ("cite", "citep", "parencite", "autocite", "citealp") else
                                   "\x05" if m.group(1) else "\x03" if m.group(2) else " ") + _blank(m.group(0)[1:]), p)
        p = _CMD.sub(lambda m: " " * len(m.group(0)), p)
        p = _ESC.sub(lambda m: " " + (m.group(1) if m.group(1) in "%&$#_" else " "), p)
        self.prose = re.sub(r"[{}~]", " ", p)
        self._mstarts = [a for a, _, _ in self.mspans]
        self._regions()
        self._cache = {}

    # ---- geometry
    def line(self, off):
        i = max(0, min(bisect.bisect_right(self.starts, off) - 1, len(self.orig) - 1))
        f, n = self.orig[i]
        return ("%s:%d" % (f, n)) if self.multi else ("l.%d" % n)

    def lineno(self, off):
        return max(0, min(bisect.bisect_right(self.starts, off) - 1, len(self.orig) - 1))

    def mspan_at(self, off):
        i = bisect.bisect_right(self._mstarts, off) - 1
        if i >= 0 and self.mspans[i][0] <= off < self.mspans[i][1]:
            return self.mspans[i]
        return None

    def _regions(self):
        raw = self.raw
        m = re.search(r"\\begin\{document\}", raw)
        self.d0 = m.end() if m else 0
        m = re.search(r"\\end\{document\}", raw)
        self.d1 = m.start() if m else len(raw)
        m = re.search(r"\\begin\{thebibliography\}|\\bibliography\{|\\printbibliography", raw)
        self.b0 = m.start() if m and m.start() > self.d0 else self.d1
        m = re.search(r"\\appendix\b", raw)
        self.app0 = m.start() if m else None
        m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", raw, re.S)
        self.abstract = (m.start(1), m.end(1)) if m else None
        m = re.search(r"\\title\s*(?:\[[^\]]*\])?\s*\{", raw)
        self.title = (m.end(), _brace_end(raw, m.end() - 1) - 1) if m else None
        self.thm = dict(_THM_DEFAULT)
        for m in re.finditer(r"\\newtheorem\*?\{(\w+)\}(?:\[\w+\])?\{([^}]+)\}", raw):
            self.thm[m.group(1)] = m.group(2).strip().split()[0].lower()
        self.envs, stack = [], []
        for m in re.finditer(r"\\(begin|end)\{([A-Za-z]+)\*?\}", raw):
            if m.group(1) == "begin":
                stack.append((m.group(2), m.start(), m.end()))
            else:
                for k in range(len(stack) - 1, -1, -1):
                    if stack[k][0] == m.group(2):
                        self.envs.append((m.group(2), stack[k][1], m.end(), stack[k][2], m.start()))
                        del stack[k:]
                        break
        self.envs.sort(key=lambda e: e[1])
        self.caps = [(m.end(), _brace_end(raw, m.end() - 1) - 1) for m in re.finditer(r"\\caption\s*(?:\[[^\]]*\])?\s*\{", raw)]
        self.secs, c, app = [], [0, 0, 0], False
        for m in re.finditer(r"\\(section|subsection|subsubsection)(\*?)\s*(?:\[[^\]]*\])?\s*\{", raw):
            if not (self.d0 <= m.start() < self.b0 or m.start() >= self.b0):
                continue
            lvl = ("section", "subsection", "subsubsection").index(m.group(1))
            e = _brace_end(raw, m.end() - 1)
            app = self.app0 is not None and m.start() > self.app0
            num = ""
            if not m.group(2):
                if app and lvl == 0 and not getattr(self, "_appreset", False):
                    c = [0, 0, 0]
                    self._appreset = True
                c[lvl] += 1
                for k in range(lvl + 1, 3):
                    c[k] = 0
                head = chr(64 + c[0]) if app else str(c[0])
                num = ".".join([head] + [str(x) for x in c[1:lvl + 1]])
            lab = re.match(r"\s*\\label\{([^}]+)\}", raw[e:e + 120])
            self.secs.append({"off": m.start(), "lvl": lvl, "title": raw[m.end():e - 1], "num": num,
                              "label": lab.group(1) if lab else None, "tend": e, "app": app})
        self.labels = {}
        for m in re.finditer(r"\\label\{([^}]+)\}", raw):
            self.labels.setdefault(m.group(1), m.start())
        if self.name.lower().endswith(".bib"):
            self.d0 = self.d1 = self.b0 = 0

    def sec_at(self, off):
        best = None
        for s in self.secs:
            if s["off"] <= off:
                best = s
            else:
                break
        return best

    def top_sec_at(self, off):
        best = None
        for s in self.secs:
            if s["off"] <= off and s["lvl"] == 0:
                best = s
        return best

    def env_kind_at(self, off):
        """innermost theorem-like / equation / float environment at off, else section or appendix."""
        best = None
        for name, a, b, _, _ in self.envs:
            if a <= off < b and (name in self.thm or name in _EQENV or name in ("figure", "table")):
                if best is None or a >= best[1]:
                    best = (name, a)
        if best:
            n = best[0]
            return self.thm.get(n) or ("equation" if n in _EQENV else n)
        s = self.sec_at(off)
        return "appendix" if (s and s["app"]) else "section"

    def env_label_at(self, off):
        best = None
        for name, a, b, ia, ib in self.envs:
            if a <= off < b and (name in self.thm or name in _EQENV):
                if best is None or a >= best[1]:
                    best = (name, a, b)
        if not best:
            return None
        m = re.search(r"\\label\{([^}]+)\}", self.raw[best[1]:best[2]])
        if not m:
            return None
        kind = self.thm.get(best[0]) or "equation"
        return kind, m.group(1)

    # ---- scopes: same offsets as raw, everything outside the scope blanked
    def scope(self, k):
        if k in self._cache:
            return self._cache[k]
        base = self.math if k == "M" else self.prose if k.islower() else self.raw
        body = [(self.d0, self.b0)]
        if self.abstract and self.abstract[0] < self.d0:
            body.append(self.abstract)
        key = k.lower()
        if key in ("p", "r", "m"):
            spans = body
        elif key == "a":
            spans = [self.abstract] if self.abstract else []
        elif key == "t":
            spans = [self.title] if self.title else []
        elif key == "s":
            spans = [(ia, ib) for n, a, b, ia, ib in self.envs if self.thm.get(n) in _STATEMENT]
        elif key == "f":
            spans = [(ia, ib) for n, a, b, ia, ib in self.envs if n == "proof"]
        elif key == "c":
            spans = self.caps
        elif key == "i":
            tops = [s for s in self.secs if s["lvl"] == 0]
            spans = [(tops[0]["off"], tops[1]["off"] if len(tops) > 1 else self.b0)] if tops else []
        elif key == "h":
            spans = [(s["tend"] - len(s["title"]) - 1, s["tend"] - 1) for s in self.secs]
        elif key == "b":
            spans = [(self.b0, len(base))]
        elif key == "h2":
            spans = []
        elif key == "w":
            spans = [(0, len(base))]
        else:
            spans = [(0, self.d0)] if key == "e" else body
        out, last = [], 0
        for a, b in sorted(spans):
            if a < last:
                continue
            out.append(_blank(base[last:a])); out.append(base[a:b]); last = b
        out.append(_blank(base[last:]))
        self._cache[k] = "".join(out)
        return self._cache[k]

    # ---- symbols
    def symbols(self):
        if "sym" in self._cache:
            return self._cache["sym"]
        m = re.sub(r"\\(?:text|mathrm|operatorname|textrm|textit|textbf|mbox|label|tag|ref|eqref|cite|begin|end|intertext"
                   r"|mathit|textup|textnormal)\*?\{[^{}]*\}", lambda x: _blank(x.group(0)), self.scope("M"))
        macros = set(re.findall(r"\\(?:re)?newcommand\*?\{?(\\[A-Za-z]+)\}?\s*\{", self.raw[:self.d0]))
        macros |= set(re.findall(r"\\def(\\[A-Za-z]+)\s*\{", self.raw[:self.d0]))
        ops = set("\\" + x for x in re.findall(r"\\DeclareMathOperator\*?\{\\([A-Za-z]+)\}", self.raw[:self.d0]))
        S = {}
        nota = self.notation_section()

        def add(name, off):
            if self.abstract and self.abstract[0] <= off < self.abstract[1]:
                return
            if nota and nota[0] <= off < nota[1]:
                S.setdefault(name, [None, 0, 0])[2] += 1
                return
            e = S.setdefault(name, [None, 0, 0])
            if e[0] is None:
                e[0] = off
            e[1] += 1

        for t in _TOK.finditer(m):
            if t.group(1):
                add("\\%s{%s}" % (t.group(1), t.group(2)), t.start())
            elif t.group(3):
                add("\\%s{%s}" % (t.group(3), t.group(4)), t.start())
            elif t.group(5):
                c = t.group(5)
                if c in _GREEK or (c in macros and c not in ops):
                    add(c, t.start())
            else:
                for j, ch in enumerate(t.group(6)):
                    add(ch, t.start(6) + j)
        self._cache["sym"] = S
        return S

    def notation_section(self):
        for i, s in enumerate(self.secs):
            if re.search(r"notation|symbols|terminology|glossary|nomenclature|conventions", s["title"], re.I) and \
                    re.search(r"index|list|table|summary|glossary|nomenclature|notation and|and notation|^notation$|"
                              r"^symbols$|terminology", s["title"].strip(), re.I) and s["app"]:
                end = self.b0 if s["off"] < self.b0 else len(self.raw)
                for t in self.secs[i + 1:]:
                    if t["lvl"] <= s["lvl"]:
                        end = t["off"]
                        break
                return (s["off"], end)
        return None

    def sentence(self, a, b):
        p = self.prose
        lo = max(0, a - 500)
        cut = [m.end() for m in re.finditer(r"[.!?]\s+(?=[A-Z\x01])|\n\s*\n", p[lo:a])]
        s0 = lo + (cut[-1] if cut else 0)
        m = re.search(r"[.!?](?=\s+[A-Z\x01]|\s*$)|\n\s*\n", p[b:b + 400])
        s1 = b + (m.start() if m else min(400, len(p) - b))
        return s0, s1

    def defined_near(self, name, off):
        sp = self.mspan_at(off)
        if not sp:
            return True
        a, b, _ = sp
        after = self.raw[off:b]
        tok = _TOK.match(after)
        rest = after[tok.end():] if tok else after[1:]
        if _INTRO_MATH.match(rest):
            return True
        if _BOUND.search(self.raw[max(a, off - 40):off]):
            return True
        s0, s1 = self.sentence(a, b)
        return bool(_CUE.search(self.prose[s0:s1]))

    def meaning_guess(self, off):
        sp = self.mspan_at(off)
        if not sp:
            return ""
        a, b, _ = sp
        s0, s1 = self.sentence(a, b)
        after = self.prose[b:s1]
        m = re.match(r"\s*(?:be|denotes?|is|are|stands? for|for)\s+((?:the|an?)\s+[^.;:\x01\x02\x03]{3,80})", after)
        if not m:
            m = re.match(r"\s+((?:the|an?)\s+[^.;:,\x01\x02\x03]{3,80})", after)
        if m:
            return re.sub(r"\s+", " ", m.group(1)).strip(" ,")
        m = re.search(r"\b((?:the|an?)\s+(?:[A-Za-z\-]+\s+){1,4})$", self.prose[s0:a])
        return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""

    def terms(self):
        """Terms introduced with emphasis: (term, offset)."""
        if "terms" in self._cache:
            return self._cache["terms"]
        out, r = [], self.scope("R")
        rx = re.compile(r"(?:\bcall(?:ed)?(?:\s+it)?|\bsay that[^.]{0,80}?\bis|\btermed|\bknown as|\brefer(?:red)? to[^.]{0,40}?\bas"
                        r"|\bdefine[sd]?|\bis said to be|\bwe say[^.]{0,80}?\b(?:is|are|has))\s+(?:the\s+|an?\s+)?"
                        r"\\(?:emph|textit|textbf|textsl)\{([^{}$\\]{2,60})\}", re.I)
        for m in rx.finditer(r):
            out.append((re.sub(r"\s+", " ", m.group(1)).strip().lower(), m.start(1)))
        for n, a, b, ia, ib in self.envs:
            if self.thm.get(n) == "definition":
                for m in re.finditer(r"\\(?:emph|textit|textbf)\{([^{}$\\]{2,60})\}", r[ia:ib]):
                    out.append((re.sub(r"\s+", " ", m.group(1)).strip().lower(), ia + m.start(1)))
        out = sorted(set(out), key=lambda x: x[1])
        self._cache["terms"] = out
        return out


_GREEK = set("\\" + g for g in (
    "alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa varkappa lambda mu nu xi pi varpi "
    "rho varrho sigma varsigma tau upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi "
    "Psi Omega ell hbar aleph beth nabla wp").split())
_TOK = re.compile(
    r"\\(mathcal|mathbb|mathbf|mathfrak|mathscr|mathsf|bm|boldsymbol|mathbbm|mathds)\s*\{?\s*(\\[A-Za-z]+|[A-Za-z0-9])\s*\}?"
    r"|\\(hat|tilde|bar|overline|widehat|widetilde|vec|check|underline)\s*\{?\s*(\\[A-Za-z]+|[A-Za-z])\s*\}?"
    r"|(\\[A-Za-z]+)"
    r"|(?<![A-Za-z\\])([A-Za-z]{1,2})(?![A-Za-z])")
_INTRO_MATH = re.compile(
    r"\s*(?:[_^]\{[^{}]*\}|[_^]\\?[A-Za-z0-9]+|\([^()]*\)|'|\s|\\[,;!]|\}|\{)*\s*"
    r"(?:=|:=|\\coloneqq|\\triangleq|\\equiv|\\in(?![A-Za-z])|\\colon|:|\\geq?(?![A-Za-z])|\\leq?(?![A-Za-z])|>|<"
    r"|\\to(?![A-Za-z])|\\sim|\\subset|\\neq|\\approx|\\mapsto|\\rightarrow|\\ll(?![A-Za-z])|\\gg(?![A-Za-z])"
    r"|\\geqslant|\\leqslant|,\s*[A-Za-z\\][^,]{0,24}\\in(?![A-Za-z]))")
_BOUND = re.compile(r"\\(?:forall|exists|sum|prod|int|max|min|sup|inf|bigcup|bigcap|lim|limsup|liminf|bigoplus|bigotimes)"
                    r"(?![A-Za-z])[^$]{0,36}$")
_CUE = re.compile(
    r"\b(?:let|denot(?:e|es|ed|ing)|defin(?:e|es|ed|ing)|write|writing|set|put|where|fix|fixed|given|for (?:any|every|each|"
    r"all|some|an?|fixed|integers?|real|positive)|consider|suppose|assume|assuming|take|choose|pick|call(?:ed)?|be (?:an?|the)|"
    r"is (?:an?|the)|are the|stands? for|there (?:exists?|is|are)|whose|with|some|any|every|each|such that|satisf\w+|"
    r"constants?|functions?|parameters?|sequences?|integers?|numbers?|sets?|spaces?|measures?|operators?|matri(?:x|ces)|"
    r"vectors?|variables?|process(?:es)?|chains?|graphs?|trees?|maps?|kernels?|weights?|times?)\b", re.I)
_DUMMY = set("ijklmnxyztsde")

# ---------------------------------------------------------------- rules
_RULES = None
_KW = {"T": (9, "two words for one thing"), "S": (7, "two spellings of one word"), "N": (6, "one name spelled two ways"),
       "A": (5, "abbreviation and long form both in use"), "B": (4, "British and American spelling mixed"),
       "P": (5, "two forms of one expression"), "F": (9, "two words for one thing"),   # F: judged only in a finance or chain paper
       "M": (6, "two notations for one thing"), "R": (5, "two LaTeX forms for one thing")}


_FIN = re.compile(r"\b(?:sharpe|drawdown|portfolio|backtest|trading strateg|hedg(?:e|ed|ing)|option premium|bitcoin|blockchain|"
                  r"transaction output|leveraged (?:fund|etf))", re.I)
_SUF = r"(?:e|ed|es|ing|ation|ations|er|ers|able)"
_GLOSS_CUE = (r"\b(?:writ(?:e|ing)|denot\w+|means?|meaning|notation|stands? for|where|defin\w+|convention|that is|i\.e\.|"
              r"called|understood|abbreviat\w+|shorthand|symbol)\b")


def _one(v, star, noplural, plus):
    body = r"\s+".join(re.escape(w).replace("_", r"(?:--?|–|\s)\s*") for w in v.split(" "))
    if plus:
        return body + _SUF
    if star:
        return body + r"[a-z]*"
    if not noplural and v[-1:].isalpha():
        if v.endswith("y") and len(v) > 3 and v[-2] not in "aeiou":
            return body[:-1] + r"(?:y|ies)"
        return body + r"(?:e?s)?"
    return body


def _vname(v):
    return v.lstrip("=").rstrip("*!+").split(";")[0].replace("_", "-")


def _variant_rx(v, math=False):
    """Variant grammar: ';' separates alternatives counted as one variant, '=' prefix case-sensitive, '!' no plural,
    '*' any word ending, '+' verb/noun endings of an -ize/-ise stem, '_' a dash or space between two names."""
    cs = v.startswith("=")
    v = v.lstrip("=")
    if math:
        alts = []
        for a in v.split(";"):
            b = re.escape(a)
            if a[:1].isalpha():
                b = r"(?<![A-Za-z\\])" + b
            if a[-1:].isalpha():
                b += r"(?![A-Za-z])"
            alts.append(b)
        return re.compile("|".join(alts))
    star, noplural, plus = v.endswith("*"), v.endswith("!"), v.endswith("+")
    v = v.rstrip("*!+")
    body = "|".join(_one(a, star, noplural, plus) for a in v.split(";"))
    return re.compile(r"(?<![A-Za-z0-9\-])(?:" + body + r")(?![A-Za-z0-9\-])", 0 if cs else re.I)


def rules():
    """The thousand rules, ids fixed by table order: word clusters, math clusters, text rules, detectors, event lines."""
    global _RULES
    if _RULES is not None:
        return _RULES
    import pw1k_terms as T
    import pw1k_rules as Rm
    out = []

    def add(kind, chapter, **kw):
        kw.update(id="P%04d" % (len(out) + 1), kind=kind, chapter=chapter)
        out.append(kw)

    for line in T.TERMS:
        body, _, hint = line.partition("#")
        f = [x.strip() for x in body.split("|")]
        add("cluster", "terms", k=f[0], variants=f[1:], hint=hint.strip(), w=_KW[f[0]][0])
    for line in T.MATH:
        body, _, hint = line.partition("#")
        f = [x.strip() for x in body.split("|")]
        add("cluster", "notation", k=f[0], variants=f[1:], hint=hint.strip(), w=_KW[f[0]][0])
    for g in Rm.GLOSS:
        rx, cue, text = g[:3]
        add("gloss", "notation", rx=rx, cue=cue, text=text, w=4, defrx=g[3] if len(g) > 3 else None)
    chapter = "misc"
    for r in Rm.RX:
        if r[0] == "#":
            chapter = r[1]
            continue
        m = re.match(r"([A-Za-z])(\d*)$", r[0])
        add("rx", chapter, scope=m.group(1), minc=int(m.group(2) or 1), rx=r[1], text=r[2], w=r[3] if len(r) > 3 else 3)
    for name, chapter, text, w in Rm.FN:
        add("fn", chapter, fn=name, text=text, w=w)
    for ch, text in Rm.EVENTS:
        add("event", "events", channel=ch, text=text, w=1)
    _RULES = out
    return out


def _compile(r):
    if "c" in r:
        return r["c"]
    if r["kind"] == "cluster":
        math = r["k"] in ("M", "R")
        vs = sorted(r["variants"], key=lambda v: -len(v))
        r["c"] = [(_vname(v), _variant_rx(v, math)) for v in vs]
        low = [a.lower() for v in vs for a in v.lstrip("=").rstrip("*!+").split(";")]
        r["overlap"] = any(a != b and b in a for a in low for b in low)
        r["pf"] = [[re.split(r"[ _]", a.lower())[0] for a in v.lstrip("=").rstrip("*!+").split(";")] for v in vs]
    else:
        rx = _prose_ws(r["rx"]) if r["scope"].islower() and r["scope"] not in ("h", "t") else r["rx"]
        r["c"] = re.compile(rx, re.I if r["scope"].islower() else 0)
    return r["c"]


_WS1 = r"(?:[ \t]+\n?|\n)[ \t]*"  # one or more blanks holding at most one line break: never a paragraph break


def _prose_ws(rx):
    """A literal space in a prose rule matches a run of blanks with at most one line break. Prose keeps the source's line breaks and
    blanks commands to spaces, so 'see below' is often 'see\\nbelow' or 'see   below' there (12 Nov: the
    ising paper's '(see\\nbelow)' passed P0813). Spaces inside a character class are left alone."""
    out, i, n, cls, groups = [], 0, len(rx), False, []
    while i < n:
        c = rx[i]
        if c == "\\" and i + 1 < n:
            out.append(rx[i:i + 2]); i += 2; continue
        if cls:
            cls = c != "]"
            out.append(c); i += 1; continue
        if c == "(":
            groups.append(rx[i:i + 4] in ("(?<=", "(?<!"))
        elif c == ")" and groups:
            groups.pop()
        if c == " " and any(groups):
            out.append(r"\s"); i += 1; continue
        if c == "[":
            out.append(c); i += 1; cls = True
            if i < n and rx[i] == "^":
                out.append("^"); i += 1
            if i < n and rx[i] == "]":
                out.append("]"); i += 1
            continue
        if c == " ":
            j = i
            while j < n and rx[j] == " ":
                j += 1
            if j < n and rx[j] in "?*+{":
                out.append(_WS1 * (j - i > 1) + r"\s")
            else:
                out.append(_WS1)
            i = j
            continue
        out.append(c); i += 1
    return "".join(out)


def run_gloss(r, doc):
    c = r.get("c")
    if c is None:
        c = r["c"] = (re.compile(r["rx"]), re.compile(r["cue"] or _GLOSS_CUE, re.I))
    ms = list(c[0].finditer(doc.scope("M")))
    if not ms:
        return None
    if r.get("defrx") and re.search(r["defrx"], doc.raw):
        return None   # the sign is introduced as a named object (a potential, a set), not an order symbol
    for m in ms[:15]:
        sp = doc.mspan_at(m.start())
        s0, s1 = doc.sentence(sp[0], sp[1]) if sp else (m.start(), m.end())
        if c[1].search(doc.prose[s0:s1]):
            return None
    return (ms[0].start(), r["text"] + (" (%dx)" % len(ms) if len(ms) > 1 else ""))


def run_cluster(r, doc):
    k = r["k"]
    text = doc.scope("M") if k == "M" else doc.scope("R") if k == "R" else doc.scope("p")
    if k == "F":
        fin = doc._cache.get("fin")
        if fin is None:
            fin = doc._cache["fin"] = len(_FIN.findall(text)) >= 3
        if not fin:
            return None
        k = "T"
    cs = _compile(r)
    if k not in ("M", "R"):
        low = doc._cache.get("low")
        if low is None:
            low = doc._cache["low"] = text.lower()
        if sum(1 for toks in r["pf"] if any(t in low for t in toks)) < 2:
            return None
    got = []
    for v, rx in cs:
        ms = list(rx.finditer(text))
        if ms:
            got.append((v, len(ms), ms[0].start()))
            if r.get("overlap"):
                text = rx.sub(lambda m: " " * len(m.group(0)), text)
    if len(got) < 2:
        return None
    if k == "A":
        longs = sorted(got, key=lambda g: -len(g[0]))
        if longs[0][1] < 3:
            return None
    got.sort(key=lambda g: -g[1])
    parts = ", ".join("'%s' (%dx, first %s)" % (v, n, doc.line(o)) for v, n, o in got[:4])
    tail = r["hint"] or {"T": "Keep one. If they are different things, define both where the second first appears.",
                         "S": "Keep one spelling.", "N": "Keep one spelling of the name.",
                         "A": "Define the abbreviation once, then use only it, or drop it.",
                         "B": "Keep one convention.", "M": "Keep one.", "R": "Keep one.", "P": "Keep one form."}[k]
    minor = min(got, key=lambda g: g[1])
    return (minor[2], "%s: %s. %s" % (_KW[k][1], parts, tail))


def run_rx(r, doc):
    ms = list(_compile(r).finditer(doc.scope(r["scope"])))
    if len(ms) < r["minc"]:
        return None
    n = len(ms)
    return (ms[0].start(), r["text"] + (" (%dx)" % n if n > 1 else ""))


_APP_DOC = re.compile(r"\b(?:research|teaching|diversity|mentoring)\s+statement\b|\bstatement of (?:teaching|research)|"
                      r"\bcover letter\b|\bDear (?:Members|Hiring|Search|Selection|Committee|Professor|Dr)\b", re.I)
_APP_PATH = re.compile(r"statement|cover[_-]?letter|(?:^|/)cl[_\d.]", re.I)
# Rules about the shape of a journal paper. A research or teaching statement or a cover letter has no roadmap, notation
# appendix, keywords, funding paragraph or theorem in its introduction, and it is about future and ongoing work (24 Nov:
# P1021, P1026, P1000 fired on the 10-page mathematics research statement). Line-level rules still run on it.
_APP_SKIP_FN = {"fn_roadmap", "fn_intro_no_statement", "fn_notation_table_missing", "fn_numbered_definition",
                "fn_ack_position", "fn_msc_missing", "fn_funding_complete", "fn_data_availability"}
_APP_SKIP_TEXT = ("The text calls itself preliminary", "Three or more deferrals to future work",
                  "A companion or forthcoming paper with no", "The source names where the paper is unde")


def application_doc(doc):
    """True for a research, teaching or diversity statement or a cover letter (same test as pw_hooks.application_doc).
    A file with an abstract is always a paper."""
    if doc.abstract:
        return False
    where = (doc.path or doc.name or "").replace("\\", "/")
    return bool(_APP_PATH.search(where) or _APP_DOC.search(doc.raw[:doc.d0 + 4000]))


def lint(doc, chapter=None, budget=None):
    """[(weight, offset, rule id, chapter, message)] sorted by weight then position.
    With a budget in seconds the heavier rules run first and the rest are left out once the time is spent;
    lint.left_out then holds how many rules did not run."""
    import pw1k_detect as D
    out = []
    todo = rules()
    if application_doc(doc):
        todo = [r for r in todo if r.get("fn") not in _APP_SKIP_FN and not str(r.get("text", "")).startswith(_APP_SKIP_TEXT)]
    lint.left_out = 0
    t0 = time.time()
    if budget:
        todo = sorted(todo, key=lambda r: -r["w"])
    for i, r in enumerate(todo):
        if chapter and r["chapter"] != chapter:
            continue
        if budget and i % 20 == 0 and time.time() - t0 > budget:
            lint.left_out = len(todo) - i
            break
        try:
            if r["kind"] == "cluster":
                h = run_cluster(r, doc)
            elif r["kind"] == "rx":
                h = run_rx(r, doc)
            elif r["kind"] == "gloss":
                h = run_gloss(r, doc)
            elif r["kind"] == "fn":
                h = getattr(D, r["fn"])(doc)
                if h:
                    h = (h[0], r["text"] + ": " + h[1] if h[1] else r["text"])
            else:
                continue
        except Exception as e:  # a broken rule must not silence the others
            h = None
            if os.environ.get("PW1K_DEBUG"):
                sys.stderr.write("%s: %r\n" % (r["id"], e))
        if h:
            out.append((r["w"], h[0], r["id"], r["chapter"], h[1]))
    out.sort(key=lambda x: (-x[0], x[1]))
    return out


def tex_files(path):
    if os.path.isdir(path):
        got = []
        for d, _, fs in os.walk(path):
            if ".git" in d:
                continue
            for f in fs:
                if f.endswith(".tex"):
                    p = os.path.join(d, f)
                    try:
                        if "\\begin{document}" in io.open(p, encoding="utf-8", errors="replace").read():
                            got.append(p)
                    except OSError:
                        pass
        return got
    return [path]


def cmd_lint(args):
    chapter = args[args.index("--chapter") + 1] if "--chapter" in args else None
    mx = int(args[args.index("--max") + 1]) if "--max" in args else 80
    rc = 0
    for p in tex_files(args[0]):
        if os.path.getsize(p) > MAX_DOC and "--big" not in args:
            print("%s: %d bytes, skipped (add --big to lint it)" % (p, os.path.getsize(p)))
            continue
        doc = Doc(path=p)
        F = lint(doc, chapter)
        by = {}
        for f in F:
            by[f[3]] = by.get(f[3], 0) + 1
        print("%s: %d findings (%s)" % (p, len(F), ", ".join("%s %d" % kv for kv in sorted(by.items(), key=lambda kv: -kv[1]))))
        for w, off, rid, ch, msg in F[:mx]:
            print("  %s [%s] %s %s" % (rid, ch, doc.line(off), msg))
        if len(F) > mx:
            print("  ... %d more (--max N)" % (len(F) - mx))
        rc = rc or (1 if F else 0)
    return rc


# ---------------------------------------------------------------- notation and terminology table
def notation_rows(doc):
    S = doc.symbols()
    rows = []
    for name, (off, n, _) in S.items():
        if off is None:
            continue
        if len(name) == 1 and name in _DUMMY and n < 6:
            continue
        s = doc.sec_at(off)
        el = doc.env_label_at(off)
        if el and el[0] != "equation":
            where = "%s~\\ref{%s}" % (el[0].capitalize(), el[1])
        elif el:
            where = "\\eqref{%s}" % el[1]
        elif s and s["label"]:
            where = "%s~\\ref{%s}" % ("Appendix" if s["app"] else "Section", s["label"])
        elif s and s["num"]:
            where = "%s %s" % ("Appendix" if s["app"] else "Section", s["num"])
        else:
            where = "p.~\\pageref{}"
        rows.append((off, name, doc.meaning_guess(off), where, n, doc.defined_near(name, off)))
    rows.sort()
    return rows


def cmd_notation(args):
    doc = Doc(path=args[0])
    rows = notation_rows(doc)
    terms = doc.terms()
    L = ["% Draft made by pw1k.py notation from " + doc.name + ". Edit every meaning; delete index letters that need no entry.",
         "\\section{Notation and terminology}\\label{app:notation}",
         "Symbols and terms are listed in the order in which they first appear.", "",
         "\\begin{center}\\begin{tabular}{@{}lp{0.55\\textwidth}l@{}}\\toprule",
         "Symbol & Meaning & First appears \\\\ \\midrule"]
    for off, name, mean, where, n, ok in rows:
        L.append("$%s$ & %s & %s \\\\%s" % (name, mean, where, "" if mean else "   % meaning missing"))
    L += ["\\bottomrule\\end{tabular}\\end{center}", ""]
    if terms:
        L += ["\\begin{center}\\begin{tabular}{@{}lp{0.55\\textwidth}l@{}}\\toprule", "Term & Meaning & First appears \\\\ \\midrule"]
        seen = set()
        for t, off in terms:
            if t in seen:
                continue
            seen.add(t)
            s = doc.sec_at(off)
            el = doc.env_label_at(off)
            where = ("%s~\\ref{%s}" % (el[0].capitalize(), el[1])) if el and el[0] != "equation" else \
                ("Section %s" % s["num"] if s and s["num"] else "")
            L.append("%s & & %s \\\\" % (t, where))
        L += ["\\bottomrule\\end{tabular}\\end{center}"]
    if "--write" in args:
        out = args[args.index("--write") + 1]
        io.open(out, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
        print("wrote %s (%d symbols, %d terms)" % (out, len(rows), len(set(t for t, _ in terms))))
    else:
        print("%s: %d symbols, %d terms introduced with emphasis" % (doc.name, len(rows), len(set(t for t, _ in terms))))
        for off, name, mean, where, n, ok in rows:
            print("  %-22s %4dx  first %-8s %-28s %s%s" % (name, n, doc.line(off), where.replace("~", " "),
                                                         mean[:50], "" if ok else "   <- no definition near first use"))
    import pw1k_detect as D
    for fn in ("fn_notation_table_check", "fn_notation_table_missing"):
        h = getattr(D, fn)(doc)
        if h:
            print("CHECK %s %s" % (doc.line(h[0]), h[1]))
    return 0


# ---------------------------------------------------------------- hook entry
_LATEX = re.compile(r"\b(pdflatex|xelatex|lualatex|latexmk|tectonic)\b")
_PUBLISH = re.compile(r"\bgit\b[^|;&]*\bpush\b|\bgh\s+(release|repo\s+create)|zenodo|researchgate|arxiv", re.I)


def _state(session):
    os.makedirs(STATE_DIR, exist_ok=True)
    p = os.path.join(STATE_DIR, "pw1k_%s.json" % re.sub(r"[^A-Za-z0-9_-]", "", session or "none")[:40])
    try:
        return p, json.load(io.open(p, encoding="utf-8"))
    except Exception:
        return p, {}


def _events(channel, st, now, k):
    ev = [r for r in rules() if r["kind"] == "event" and r["channel"] == channel]
    ev.sort(key=lambda r: st.get(r["id"], 0))
    out = []
    for r in ev[:k]:
        if now - st.get(r["id"], 0) > COOL_S:
            st[r["id"]] = now
            out.append("  %s %s" % (r["id"], r["text"]))
    return out


def hook(raw, codex=False, now=None):
    try:
        p = json.loads(raw) if raw.strip() else {}
    except Exception:
        return ""
    now = now or time.time()
    ti = p.get("tool_input") or {}
    path = ti.get("file_path") or ti.get("path") or ""
    cmd = ti.get("command") or ""
    cwd = p.get("cwd") or os.getcwd()
    if isinstance(cmd, (list, tuple)):
        cmd = "\n".join(str(x) for x in cmd)
    if not path:   # Codex apply_patch: the file name is inside the patch text
        blob = "\n".join(v for v in list(ti.values()) + [cmd] if isinstance(v, str))
        m = re.search(r"^\*\*\* (?:Add|Update) File: (.+?\.(?:tex|bib))\s*$", blob, re.M)
        if m:
            path = m.group(1).strip()
            if not os.path.isabs(path):
                path = os.path.join(cwd, path)
            cmd = ""
    lines, doc, channel = [], None, None
    if path.lower().endswith(".tex"):
        channel = "draft"
        if ti.get("content") and "\\begin{document}" in ti["content"] and p.get("hook_event_name") == "PreToolUse" \
                and len(ti["content"]) <= MAX_DOC:
            doc = Doc(text=ti["content"], name=os.path.basename(path))
        elif os.path.isfile(path) and os.path.getsize(path) <= MAX_DOC:
            head = io.open(path, encoding="utf-8", errors="replace").read()
            if "\\begin{document}" in head:
                doc = Doc(path=path)
    elif path.lower().endswith(".bib"):
        channel = "bib"
    elif cmd and _LATEX.search(cmd):
        channel = "compile"
        m = re.search(r"([^\s\"']+\.tex)\b", cmd)
        cand = os.path.join(cwd, m.group(1)) if m and not os.path.isabs(m.group(1)) else (m.group(1) if m else "")
        if cand and os.path.isfile(cand) and os.path.getsize(cand) <= MAX_DOC:
            doc, path = Doc(path=cand), cand
    elif cmd and _PUBLISH.search(cmd):
        if not any(f.endswith(".tex") for d in (cwd, os.path.join(cwd, "paper")) if os.path.isdir(d) for f in os.listdir(d)) \
                and not re.search(r"paper|zenodo|researchgate|arxiv", cmd, re.I):
            return ""
        channel = "publish"
    if not channel:
        return ""
    sp, st = _state(p.get("session_id") or os.environ.get("CLAUDE_SESSION_ID") or "")
    if doc is not None:
        F = lint(doc, budget=HOOK_S)
        key = lambda f: "%s|%s" % (os.path.basename(path), f[2])
        fresh = [f for f in F if now - st.get(key(f), 0) > COOL_S]
        if fresh:
            nt = sum(1 for f in F if f[3] == "terms")
            nn = sum(1 for f in F if f[3] == "notation")
            lines.append("[paper-1k] %s: %d findings (one word per thing %d, notation %d). First to fix:"
                         % (os.path.basename(path), len(F), nt, nn))
            for f in fresh[:TOP]:
                st[key(f)] = now
                lines.append("  %s %s %s" % (f[2], doc.line(f[1]), f[4][:230]))
            lines.append("  all of them: %s lint \"%s\"   notation table: %s notation \"%s\"" % (SELF, path, SELF, path))
    ev = _events(channel, st, now, 1 if lines else 2)
    if ev and not lines:
        lines.append("[paper-1k] %s:" % {"draft": "writing a paper", "bib": "editing a bibliography", "compile": "compiling a paper",
                                         "publish": "about to post a paper"}[channel])
    lines += ev
    if not lines:
        return ""
    try:
        json.dump(st, io.open(sp, "w", encoding="utf-8"))
        io.open(FIRES, "a", encoding="utf-8").write(json.dumps({"t": int(now), "ch": channel, "f": os.path.basename(path),
                                                               "n": len(lines)}) + "\n")
    except Exception:
        pass
    text = "\n".join(lines)[:MAX_OUT]
    if codex:
        return json.dumps({"hookSpecificOutput": {"hookEventName": p.get("hook_event_name") or "PreToolUse",
                                                  "additionalContext": text}})
    return text


def cmd_list(args):
    R = rules()
    L = ["# pw1k: the thousand paper-writing rules", "",
         "The fault these rules catch most often is one object called by several names.", "", "%d rules. Check a paper: `%s lint <file.tex>`." % (len(R), SELF), ""]
    ch = None
    for r in R:
        if r["chapter"] != ch:
            ch = r["chapter"]
            L += ["", "## %s (%d)" % (ch, sum(1 for x in R if x["chapter"] == ch)), ""]
        if r["kind"] == "cluster":
            L.append("- %s one of: %s" % (r["id"], " / ".join(_vname(v) for v in r["variants"])))
        else:
            L.append("- %s %s" % (r["id"], r["text"]))
    text = "\n".join(L) + "\n"
    if "--md" in args:
        io.open(args[args.index("--md") + 1], "w", encoding="utf-8", newline="\n").write(text)
    by = {}
    for r in R:
        by[r["chapter"]] = by.get(r["chapter"], 0) + 1
    print("%d rules: %s" % (len(R), ", ".join("%s %d" % kv for kv in by.items())))
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 0
    c, a = argv[0], argv[1:]
    if c == "lint":
        return cmd_lint(a)
    if c == "notation":
        return cmd_notation(a)
    if c == "list":
        return cmd_list(a)
    if c == "selftest":
        import pw1k_selftest
        return pw1k_selftest.run()
    if c == "hook":
        try:
            out = hook(sys.stdin.read(), codex="--codex" in a)
            if out:
                sys.stdout.write(out + "\n")
        except Exception as e:
            if os.environ.get("PW1K_DEBUG"):
                raise
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    sys.exit(main(sys.argv[1:]))
