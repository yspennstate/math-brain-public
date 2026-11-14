# -*- coding: utf-8 -*-
"""Detectors for pw1k.py (author an agent, 12 Nov 2026).

Each fn_* takes the engine's Doc and returns (offset, detail) or None.  The message printed is the rule's text from
pw1k_rules.FN, a colon, and the detail.  A detector that is unsure returns None: these lines are shown to an agent in
the middle of its work, and a wrong line costs more than a missed one.
"""
import os
import re
import sys

DUMMY = set("ijklmnxyztsde")
STMT = {"theorem", "lemma", "proposition", "corollary"}
STMT_ALL = STMT | {"conjecture", "claim", "definition", "assumption", "fact"}


def _eng():
    m = sys.modules.get("pw1k")
    if m is None or not hasattr(m, "_TOK"):
        m = sys.modules.get("__main__")
        if m is None or not hasattr(m, "_TOK"):
            import pw1k as m
    return m


def _isbib(doc):
    return doc.name.lower().endswith(".bib")


def _names(s):
    E, out = _eng(), []
    for t in E._TOK.finditer(s):
        if t.group(1):
            out.append(("\\%s{%s}" % (t.group(1), t.group(2)), t.start()))
        elif t.group(3):
            out.append(("\\%s{%s}" % (t.group(3), t.group(4)), t.start()))
        elif t.group(5):
            out.append((t.group(5), t.start()))
        else:
            for j, ch in enumerate(t.group(6)):
                out.append((ch, t.start(6) + j))
    return out


def _refs(doc):
    c = doc._cache.get("refs")
    if c is None:
        c = set()
        for m in re.finditer(r"\\(?:eq|c|C|auto|page|name|v)?ref\*?\{([^}]*)\}|\\(?:cref|Cref)range\{([^}]*)\}\{([^}]*)\}", doc.raw):
            for g in m.groups():
                if g:
                    c.update(x.strip() for x in g.split(","))
        doc._cache["refs"] = c
    return c


def _envs(doc, kinds):
    return [e for e in doc.envs if doc.thm.get(e[0]) in kinds]


def _clean(t):
    t = re.sub(r"\$[^$]*\$", " ", t)
    t = re.sub(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?", " ", t)
    return re.sub(r"\s+", " ", re.sub(r"[{}~]", " ", t)).strip()


def _body(doc):
    return doc.scope("p")


def _count(rx, text, flags=re.I):
    return len(re.findall(rx, text, flags))


def _first(rx, text, flags=re.I):
    m = re.search(rx, text, flags)
    return m.start() if m else None


def _bibitems(doc):
    c = doc._cache.get("bibitems")
    if c is not None:
        return c
    raw, out = doc.raw, []
    if _isbib(doc):
        ms = list(re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", raw))
        for i, m in enumerate(ms):
            if m.group(1).lower() in ("comment", "string", "preamble"):
                continue
            end = ms[i + 1].start() if i + 1 < len(ms) else len(raw)
            out.append((m.start(), m.group(2), raw[m.end():end]))
    else:
        ms = list(re.finditer(r"\\bibitem\s*(?:\[[^\]]*\])?\s*\{([^}]+)\}", raw))
        ms = [m for m in ms if m.start() >= doc.b0]
        for i, m in enumerate(ms):
            if i + 1 < len(ms):
                end = ms[i + 1].start()
            else:
                end = raw.find("\\end{thebibliography}", m.end())
                end = len(raw) if end < 0 else end
            out.append((m.start(), m.group(1), raw[m.end():end]))
    doc._cache["bibitems"] = out
    return out


def _back(doc, title_rx):
    """(start, end) of a back-matter unit whose heading matches title_rx, else None."""
    raw = doc.raw
    m = re.search(r"\\(?:section|subsection|subsubsection|paragraph)\*?\s*\{\s*(?:" + title_rx + r")[^}]*\}", raw, re.I)
    if not m:
        return None
    n = re.search(r"\\(?:section|subsection|paragraph|appendix|bibliography|printbibliography)\b|\\begin\{thebibliography\}"
                  r"|\\end\{document\}", raw[m.end():])
    return (m.start(), m.end() + (n.start() if n else len(raw) - m.end()))


def _lst(xs, k=4):
    xs = list(xs)
    return ", ".join(xs[:k]) + (" and %d more" % (len(xs) - k) if len(xs) > k else "")


# ---------------------------------------------------------------- terms
_HEAD = re.compile(r"\b(?:the|an?|this|that|each|every|our|its|any|some|same|given|fixed)\s+(?:[a-z][a-z\-]+\s+){0,2}?"
                   r"([a-z][a-z\-]{2,})\s+$", re.I)
_STOPW = set("the a an this that these those of in on at by to is are be was has have its our their it as or and for with "
             "which whose where".split())
_ONESYM = re.compile(r"^\\?[A-Za-z]+(?:\{[A-Za-z]+\})?(?:_(?:[A-Za-z0-9]|\{[A-Za-z0-9,]+\}))?$")
_GENERIC = set("""integer number constant parameter value index point element variable function map mapping set sequence family
collection matrix vector operator space graph real natural prime quantity term factor sum product exponent case
following above below same case cases where when that with for and from into onto over under such fixed given some any all
every each both either between let if then also only note recall since because hence thus whenever while random positive
negative nonnegative finite infinite large small first second third last next previous new old other another certain
corresponding respective associated resulting arbitrary general particular unique limit bound inequality identity
equation expression formula condition assumption hypothesis property statement claim event probability expectation
symbol letter notation scalar tuple pair triple subset interval rate order size length dimension degree level step time""".split())


def fn_object_names(doc):
    if _isbib(doc):
        return None
    P, groups = doc.prose, {}
    for a, b, disp in doc.mspans:
        if disp or b - a > 26 or not (doc.d0 <= a < doc.b0):
            continue
        body = doc.raw[a:b].strip("$").replace("\\(", "").replace("\\)", "").strip()
        key = re.sub(r"\s+", "", re.sub(r"[_^](?:\{[^{}]*\}|\\[A-Za-z]+|.)", "", body))
        if not key or len(key) > 14 or re.search(r"[=<>+,(|]|\\(?:le|ge|in|to|sim|approx|ne|cdot|times)(?![A-Za-z])", key):
            continue
        m = _HEAD.search(P[max(0, a - 70):a])
        if not m:
            continue
        noun = m.group(1).lower()
        if len(noun) > 4 and noun.endswith("s") and not noun.endswith("ss"):
            noun = noun[:-1]
        if noun in _GENERIC or noun in _STOPW or noun.endswith("ly"):
            continue
        groups.setdefault(key, {}).setdefault(noun, []).append(a)
    hits = []
    for key, d in groups.items():
        if sum(1 for v in d.values() if len(v) >= 2) >= 2:
            hits.append((len(d), sum(len(v) for v in d.values()), key, d))
    if not hits:
        return None
    hits.sort(reverse=True)
    _, _, key, d = hits[0]
    parts = sorted(d.items(), key=lambda kv: (-len(kv[1]), kv[1][0]))
    det = "$%s$ is %s" % (key, ", ".join("'%s' (%dx, %s)" % (n, len(v), doc.line(v[0])) for n, v in parts[:4]))
    if len(hits) > 1:
        det += "; also " + _lst(["$%s$" % h[2] for h in hits[1:]], 3)
    return (parts[1][1][0], det)


def fn_hyphen_compound_mixed(doc):
    if _isbib(doc):
        return None
    P = _body(doc).lower()
    words, first = {}, {}
    for m in re.finditer(r"[a-z]+(?:-[a-z]+)*", P):
        w = m.group(0)
        words[w] = words.get(w, 0) + 1
        first.setdefault(w, m.start())
    hits = []
    for w, n1 in words.items():
        parts = w.split("-")
        if len(parts) != 2 or len(parts[0]) < 3 or len(parts[1]) < 3:
            continue
        closed = parts[0] + parts[1]
        n2 = words.get(closed, 0) + words.get(closed + "s", 0)
        if n2:
            hits.append((first[w], "'%s' (%dx) and '%s' (%dx)" % (w, n1, closed, n2)))
    hits.sort()
    if not hits:
        return None
    return (hits[0][0], _lst([h[1] for h in hits], 3))


def fn_capital_mixed(doc):
    if _isbib(doc):
        return None
    P = _body(doc)
    seen, hits = set(), []
    for m in re.finditer(r"(?<=[a-z,] )([A-Z][a-z]{2,}(?: (?:of |in |for |and )?[A-Z][a-z]{2,}){1,3})\b", P):
        ph = m.group(1)
        if ph in seen:
            continue
        seen.add(ph)
        low = ph.lower()
        n = len(re.findall(r"(?<![A-Za-z])%s(?![A-Za-z])" % re.escape(low), P))
        if n:
            hits.append((m.start(), "'%s' and '%s' (%dx)" % (ph, low, n)))
    if not hits:
        return None
    return (hits[0][0], _lst([h[1] for h in hits], 3))


_ACR_OK = set("""AI US UK EU USA PDF URL DOI ISBN ISSN ORCID MSC NSF ERC ISF GPU CPU RAM QED OK TV ID LLC NY MIT IBM AMS SIAM IEEE ACM
NYSE ETF VIX SPY SPX OPRA NBBO USD EUR ILS GBP UTC GMT ET EST PM AM BC AD HTML
JSON CSV API SDK OS PC III VII VIII XII XIII XIV ICML ICLR COLT STOC FOCS SODA NIPS JMLR PNAS CNRS ETH UCLA MSRI IAS IHES
OEIS LMFDB arXiv AND OR NOT XOR NAND NOR XNOR""".split())


def _acronyms(doc):
    c = doc._cache.get("acr")
    if c is None:
        P = _body(doc)
        c = {}
        for m in re.finditer(r"(?<![A-Za-z0-9\-])([A-Z]{2,6})(s?)(?![A-Za-z0-9])", P):
            a = m.group(1)
            if a in _ACR_OK or re.match(r"^[IVXLC]+$", a):
                continue
            e = c.setdefault(a, {"uses": [], "defs": []})
            e["uses"].append(m.start())
            if P[max(0, m.start() - 1):m.start()] == "(" and re.search(r"[a-z]\s*$", P[max(0, m.start() - 4):m.start() - 1]):
                e["defs"].append(m.start())
        doc._cache["acr"] = c
    return c


def fn_acronym_undefined(doc):
    if _isbib(doc):
        return None
    P = _body(doc)
    bad = []
    for a, e in _acronyms(doc).items():
        if len(e["uses"]) >= 2 and not e["defs"]:
            if re.search(r"%s\s+(?:stands for|denotes|is short for|abbreviates|for short)|\(\s*%s\s*,|henceforth\s+%s" % (a, a, a), P):
                continue
            bad.append((e["uses"][0], "%s (%dx, first %s)" % (a, len(e["uses"]), doc.line(e["uses"][0]))))
    if not bad:
        return None
    bad.sort()
    return (bad[0][0], _lst([b[1] for b in bad], 4))


def fn_acronym_redefined(doc):
    if _isbib(doc):
        return None
    bad = [(e["defs"][1], "%s at %s and again at %s" % (a, doc.line(e["defs"][0]), doc.line(e["defs"][1])))
           for a, e in _acronyms(doc).items() if len(e["defs"]) >= 2]
    if not bad:
        return None
    bad.sort()
    return (bad[0][0], _lst([b[1] for b in bad], 3))


def fn_abbrev_once(doc):
    if _isbib(doc):
        return None
    bad = [(e["defs"][0], "%s (%s)" % (a, doc.line(e["defs"][0])))
           for a, e in _acronyms(doc).items() if len(e["defs"]) == 1 and len(e["uses"]) <= 2]
    if not bad:
        return None
    bad.sort()
    return (bad[0][0], _lst([b[1] for b in bad], 4) + "; write the words instead")


def fn_term_defined_twice(doc):
    if _isbib(doc):
        return None
    first, bad = {}, []
    for t, off in doc.terms():
        if t in first and off - first[t] > 400:
            bad.append((off, "'%s' at %s and again at %s" % (t, doc.line(first[t]), doc.line(off))))
        first.setdefault(t, off)
    if not bad:
        return None
    return (bad[0][0], _lst([b[1] for b in bad], 3))


def fn_term_used_before_defined(doc):
    if _isbib(doc):
        return None
    P = _body(doc).lower()
    tops = [s for s in doc.secs if s["lvl"] == 0]
    start = tops[1]["off"] if len(tops) > 1 else doc.d0
    bad, seen = [], set()
    for t, off in doc.terms():
        if t in seen or len(t) < 7 or off < start:
            continue
        seen.add(t)
        m = re.search(r"(?<![a-z\-])%s(?![a-z\-])" % re.escape(t), P[start:off - 300] if off - 300 > start else "")
        if m:
            bad.append((start + m.start(), "'%s' is used at %s and introduced at %s" % (t, doc.line(start + m.start()), doc.line(off))))
    if not bad:
        return None
    bad.sort()
    return (bad[0][0], _lst([b[1] for b in bad], 3))


def fn_definition_style(doc):
    if _isbib(doc):
        return None
    R = doc.scope("R")
    cue = r"(?:\bcall(?:ed)?(?:\s+it)?|\btermed|\bis said to be|\bsay that[^.]{0,80}?\bis|\bknown as)\s+(?:the\s+|an?\s+)?"
    it = len(re.findall(cue + r"\\(?:emph|textit|textsl)\{", R))
    bf = len(re.findall(cue + r"\\textbf\{", R))
    qu = len(re.findall(cue + r"``", R))
    for n, a, b, ia, ib in doc.envs:
        if doc.thm.get(n) == "definition":
            it += len(re.findall(r"\\(?:emph|textit)\{", R[ia:ib]))
            bf += len(re.findall(r"\\textbf\{", R[ia:ib]))
    used = [(k, v) for k, v in (("italic", it), ("bold", bf), ("quotes", qu)) if v]
    if len(used) < 2 or it + bf + qu < 3:
        return None
    off = _first(cue + r"(?:\\textbf\{|``)", R) or doc.d0
    return (off, ", ".join("%s %dx" % kv for kv in used))


# ---------------------------------------------------------------- notation
_STD = {"\\pi", "\\ell", "\\infty", "\\partial", "\\nabla", "O", "o", "\\mathbb{R}", "\\mathbb{N}", "\\mathbb{Z}", "\\mathbb{Q}",
        "\\mathbb{C}", "\\mathbb{E}", "\\mathbb{P}", "\\R", "\\N", "\\Z", "\\Q", "\\C", "\\E", "\\P", "\\varepsilon", "\\epsilon",
        "\\delta"}


def _real_symbols(doc, minc=2):
    S = doc.symbols()
    return [(o, n, c, k) for n, (o, c, k) in S.items()
            if o is not None and c >= minc and not (len(n) == 1 and n in DUMMY) and n not in _STD]


def fn_symbol_undefined(doc):
    if _isbib(doc):
        return None
    bad = []
    for o, n, c, k in sorted(_real_symbols(doc)):
        if not (doc.d0 <= o < doc.b0):
            continue
        if not doc.defined_near(n, o):
            bad.append((o, "%s (%s)" % (n, doc.line(o))))
    if not bad:
        return None
    return (bad[0][0], _lst([b[1] for b in bad], 5))


def fn_notation_table_missing(doc):
    if _isbib(doc) or doc.notation_section() or not re.search(r"\\begin\{document\}", doc.raw):
        return None
    big = _real_symbols(doc)
    if len(big) < 15:
        return None
    return (doc.app0 or doc.b0, "%d symbols are in use; draft the table with `python pw1k.py notation FILE --write notation.tex`"
            % len(big))


def fn_notation_table_check(doc):
    nota = None if _isbib(doc) else doc.notation_section()
    if not nota:
        return None
    S = doc.symbols()
    text = doc.raw[nota[0]:nota[1]]
    listed, nopointer, late = set(), 0, []
    for row in re.split(r"\\\\", text):
        if "&" not in row:
            continue
        cell = row.split("&")[0]
        m = re.search(r"\$([^$]+)\$|\\\(([^)]*)\\\)", cell)
        if not m:
            continue
        names = [n for n, _ in _names(m.group(1) or m.group(2))]
        name = next((n for n in names if n in S), names[0] if names else None)
        if not name:
            continue
        listed.add(name)
        labs = re.findall(r"\\(?:eq|c|C|auto|page)?ref\{([^}]+)\}", row)
        if not labs:
            nopointer += 1
            continue
        first = S.get(name, [None])[0]
        loff = doc.labels.get(labs[0].split(",")[0].strip())
        if first is None or loff is None:
            continue
        ustart = None
        for s in doc.secs:
            if s["label"] == labs[0]:
                ustart = s["off"]
        if ustart is None:
            inner = [a for nme, a, b, ia, ib in doc.envs if a <= loff < b and (nme in doc.thm or nme in _eng()._EQENV)]
            ustart = max(inner) if inner else loff - 300
        if first < ustart - 5:
            late.append("%s is used at %s, before the place the table names" % (name, doc.line(first)))
    unused = sorted(n for n in listed if S.get(n, [None])[0] is None)
    missing = [n for o, n, c, k in sorted(_real_symbols(doc, 3)) if k == 0 and n not in listed]
    parts = []
    if missing:
        parts.append("used and not listed: " + _lst(missing, 6))
    if unused:
        parts.append("listed and never used: " + _lst(unused, 4))
    if late:
        parts.append(_lst(late, 2))
    if nopointer:
        parts.append("%d rows give no place of first appearance" % nopointer)
    if not parts:
        return None
    return (nota[0], "; ".join(parts[:3]))


def fn_symbol_two_meanings(doc):
    if _isbib(doc):
        return None
    P, intro = doc.prose, {}
    for a, b, disp in doc.mspans:
        if disp or b - a > 22 or not (doc.d0 <= a < doc.b0):
            continue
        if not re.search(r"\b(?:let|denote by|write)\s+$", P[max(0, a - 14):a], re.I):
            continue
        m = re.match(r"\s+(?:be|denote)\s+(?:the|an?)\s+([a-z\-]+(?:\s+[a-z\-]+)?)", P[b:b + 60])
        if not m:
            continue
        key = re.sub(r"\s+", "", doc.raw[a:b].strip("$"))
        if (len(key) == 1 and key in DUMMY) or not _ONESYM.match(key):
            continue
        ws = [w for w in m.group(1).lower().split() if w not in _STOPW]
        if ws:
            intro.setdefault(key, []).append((a, " ".join(ws)))
    bad = []
    for key, L in intro.items():
        nouns = set(n.split()[-1] for _, n in L)
        if len(L) >= 2 and len(nouns) >= 2 and not (nouns & _GENERIC) and not (set(L[0][1].split()) & set(L[1][1].split())):
            bad.append((L[1][0], "$%s$ is '%s' at %s and '%s' at %s" % (key, L[0][1], doc.line(L[0][0]), L[1][1], doc.line(L[1][0]))))
    if not bad:
        return None
    bad.sort()
    return (bad[0][0], _lst([b[1] for b in bad], 2))


def fn_macro_bypass(doc):
    if _isbib(doc) or not doc.d0:
        return None
    pre, body, bad = doc.raw[:doc.d0], doc.raw[doc.d0:doc.b0], []
    for m in re.finditer(r"\\(?:re)?newcommand\*?\{?(\\[A-Za-z]+)\}?\s*\{(\\(?:mathbb|mathcal|mathbf|mathfrak|mathrm|operatorname"
                         r"|mathscr|mathsf)\{[A-Za-z]+\})\}", pre):
        n = body.count(m.group(2))
        if n:
            bad.append((doc.d0 + body.find(m.group(2)), "%s is defined as %s, and %s is also typed %dx" % (m.group(1), m.group(2), m.group(2), n)))
    for m in re.finditer(r"\\DeclareMathOperator\*?\{(\\[A-Za-z]+)\}\{([A-Za-z]+)\}", pre):
        k = re.search(r"\\(?:operatorname|mathrm|text)\{%s\}" % re.escape(m.group(2)), body)
        if k:
            bad.append((doc.d0 + k.start(), "%s is declared, and %s is also typed" % (m.group(1), k.group(0))))
    if not bad:
        return None
    bad.sort()
    return (bad[0][0], _lst([b[1] for b in bad], 3))


_FONT_PAIRS = [("mathbf", "bm"), ("mathbf", "boldsymbol"), ("bm", "boldsymbol"), ("mathcal", "mathscr"), ("mathbb", "mathbbm"),
               ("mathbb", "mathds"), ("hat", "widehat"), ("tilde", "widetilde"), ("bar", "overline")]


def fn_font_mix(doc):
    if _isbib(doc):
        return None
    S, bad = doc.symbols(), []
    for n, (o, c, k) in S.items():
        m = re.match(r"\\([a-z]+)\{(.+)\}$", n)
        if not m or o is None:
            continue
        for x, y in _FONT_PAIRS:
            if m.group(1) == x:
                other = "\\%s{%s}" % (y, m.group(2))
                if other in S and S[other][0] is not None:
                    bad.append((max(o, S[other][0]), "%s (%dx) and %s (%dx)" % (n, c, other, S[other][1])))
    if not bad:
        return None
    bad.sort()
    return (bad[0][0], _lst([b[1] for b in bad], 3))


def fn_symbol_once(doc):
    if _isbib(doc):
        return None
    once = sorted((o, n) for n, (o, c, k) in doc.symbols().items()
                  if o is not None and c == 1 and len(n) > 1 and n not in _STD and doc.d0 <= o < doc.b0)
    if len(once) < 5:
        return None
    return (once[0][0], _lst(["%s (%s)" % (n, doc.line(o)) for o, n in once], 5))


def fn_index_clash(doc):
    if _isbib(doc):
        return None
    M, P = doc.scope("M"), doc.prose
    idx = {}
    for m in re.finditer(r"\\(?:sum|prod|bigcup|bigcap|bigoplus)\s*_\s*\{?\s*([A-Za-z])\s*(?:=|\\in|\\ge|\\le|<|>|\}|:)", M):
        idx.setdefault(m.group(1), []).append(m.start())
    bad = []
    for a, b, disp in doc.mspans:
        if disp or b - a > 14 or not (doc.d0 <= a < doc.b0):
            continue
        if not re.search(r"\b(?:fix|fixed|let|given)\s+$", P[max(0, a - 8):a], re.I):
            continue
        m = re.match(r"\$\s*([A-Za-z])\s*(?:\$|\\ge|\\le|>|<|\\in)", doc.raw[a:b])
        if not m or m.group(1) not in idx:
            continue
        top = doc.top_sec_at(a)
        same = [o for o in idx[m.group(1)] if o > a and doc.top_sec_at(o) is top]
        if len(same) >= 1 and re.match(r"\s+(?:be|denote)\s+(?:the|an?)\b", P[b:b + 30]):
            bad.append((same[0], "$%s$ is fixed at %s and is a running index at %s" % (m.group(1), doc.line(a), doc.line(same[0]))))
    if not bad:
        return None
    bad.sort()
    return (bad[0][0], bad[0][1])


def fn_const_names(doc):
    if _isbib(doc):
        return None
    S, P = doc.symbols(), _body(doc)
    nC = S.get("C", [None, 0, 0])[1]
    nc = S.get("c", [None, 0, 0])[1]
    if nC < 6 and not (nC >= 3 and nc >= 3):
        return None
    if re.search(r"line to line|may (?:change|vary|differ)|generic constant|whose value|not necessarily the same|from one (?:line|occurrence)"
                 r"|(?:absolute|universal|numerical) constants?|constants?[^.]{0,60}\bdepend", P, re.I):
        return None
    return (S["C"][0], "C appears %d times%s" % (nC, (", c %d times" % nc) if nc else ""))


_TRAIL = re.compile(r"(?:\s+|\\label\{[^}]*\}|\\nonumber|\\notag|\\qedhere|\\tag\{[^}]*\}|\\end\{(?:aligned|split|gathered|cases|array|alignedat)\}"
                    r"|\\\]|\$\$|\\end\{(?:equation|align|gather|multline|eqnarray|flalign|alignat|displaymath)\*?\})$")


def fn_display_punct(doc):
    if _isbib(doc):
        return None
    tot, bad = 0, []
    for a, b, disp in doc.mspans:
        if not disp or not (doc.d0 <= a < doc.b0):
            continue
        tot += 1
        t = doc.raw[a:b]
        while True:
            m = _TRAIL.search(t)
            if not m or m.start() == len(t):
                break
            t = t[:m.start()]
        t = re.sub(r"(?:\\[,;!: ]|\\quad|\\qquad|\s)+$", "", t)
        if t.endswith("\\right.") or not t or t[-1] not in ".,;:":
            nxt = doc.raw[b:b + 80].lstrip(" \t")
            if re.match(r"(?:\n\s*)?(?:[A-Z]|\\end\{proof\}|\\section|\\subsection|\\begin\{(?:theorem|lemma|proof|remark|proposition|corollary)|\n\s*\n)", nxt):
                bad.append(a)
    if len(bad) < 3:
        return None
    return (bad[0], "%d of %d displays end a sentence with no period (first %s)" % (len(bad), tot, doc.line(bad[0])))


def fn_eq_numbers(doc):
    if _isbib(doc):
        return None
    refs, tot, bad = _refs(doc), 0, []
    for n, a, b, ia, ib in doc.envs:
        if n != "equation" or doc.raw[a:ia].endswith("*}") or not (doc.d0 <= a < doc.b0):
            continue
        tot += 1
        m = re.search(r"\\label\{([^}]+)\}", doc.raw[ia:ib])
        if not m or m.group(1) not in refs:
            bad.append(a)
    if len(bad) < 5 or 2 * len(bad) < tot:
        return None
    return (bad[0], "%d of %d numbered equations are never cited" % (len(bad), tot))


# ---------------------------------------------------------------- references and latex setup
_WORD = {"theorem": "theorem", "thm": "theorem", "lemma": "lemma", "lem": "lemma", "proposition": "proposition", "prop": "proposition",
         "corollary": "corollary", "cor": "corollary", "definition": "definition", "def": "definition", "remark": "remark",
         "conjecture": "conjecture", "claim": "claim", "assumption": "assumption", "example": "example", "section": "section",
         "sec": "section", "subsection": "section", "appendix": "appendix", "figure": "figure", "fig": "figure", "table": "table",
         "tab": "table", "equation": "equation", "eq": "equation", "algorithm": "algorithm"}


def fn_ref_kind(doc):
    if _isbib(doc):
        return None
    bad = []
    for m in re.finditer(r"\b([A-Z][a-z]+)\.?[~\s]+\(?\\(?:eq)?ref\{([^}]+)\}", doc.raw[doc.d0:]):
        w = m.group(1).lower()
        if w.endswith("ies"):
            w = w[:-3] + "y"
        elif w.endswith("s") and w[:-1] in _WORD:
            w = w[:-1]
        word = _WORD.get(w)
        if not word:
            continue
        loff = doc.labels.get(m.group(2).strip())
        if loff is None:
            continue
        kind = doc.env_kind_at(loff)
        if kind == word or {kind, word} <= {"section", "appendix"}:
            continue
        if word in ("figure", "table", "algorithm", "example") and kind in ("section", "appendix"):
            continue      # an environment the engine does not track
        if kind in ("section", "appendix") and word not in ("section", "appendix"):
            # a label right after \begin{...} of an untracked environment, or a loose label
            env = re.search(r"\\begin\{([A-Za-z]+)\*?\}[^\\]{0,80}$", doc.raw[max(0, loff - 120):loff])
            if not env or doc.thm.get(env.group(1)) == word:
                continue
        bad.append((doc.d0 + m.start(), "'%s~\\ref{%s}' points at %s %s (%s)" % (
            m.group(1), m.group(2), "an" if kind[0] in "aeiou" else "a", kind, doc.line(doc.d0 + m.start()))))
    if not bad:
        return None
    return (bad[0][0], bad[0][1] + ("; %d more of the kind" % (len(bad) - 1) if len(bad) > 1 else ""))


def fn_env_prints_other_kind(doc):
    if _isbib(doc):
        return None
    E, bad = _eng(), []
    for m in re.finditer(r"\\newtheorem\*?\{(\w+)\}(?:\[\w+\])?\{([^}]+)\}", doc.raw[:doc.d0 or len(doc.raw)]):
        want = E._THM_DEFAULT.get(m.group(1).lower())
        got = m.group(2).strip().split()[0].lower() if m.group(2).strip() else ""
        if want and got and got != want and not (got.startswith(want[:4])):
            bad.append((m.start(), "\\begin{%s} prints '%s'" % (m.group(1), m.group(2).strip())))
    if not bad:
        return None
    return (bad[0][0], _lst([b[1] for b in bad], 3))


def fn_theorem_counters(doc):
    if _isbib(doc):
        return None
    own = []
    for m in re.finditer(r"\\newtheorem\{(\w+)\}(\[\w+\])?\{([^}]+)\}", doc.raw[:doc.d0 or len(doc.raw)]):
        if not m.group(2) and m.group(3).strip().split()[0].lower() in STMT:
            own.append((m.start(), m.group(3).strip()))
    if len(own) < 2:
        return None
    return (own[1][0], _lst([o[1] for o in own], 4) + " each have their own counter; share one (\\newtheorem{lemma}[theorem]{Lemma})")


def fn_label_duplicate(doc):
    if _isbib(doc):
        return None
    seen, bad = {}, []
    for m in re.finditer(r"\\label\{([^}]+)\}", doc.raw):
        if m.group(1) in seen:
            bad.append((m.start(), "%s at %s and %s" % (m.group(1), doc.line(seen[m.group(1)]), doc.line(m.start()))))
        seen.setdefault(m.group(1), m.start())
    if not bad:
        return None
    return (bad[0][0], _lst([b[1] for b in bad], 3))


def fn_label_unreferenced(doc):
    if _isbib(doc):
        return None
    refs, bad = _refs(doc), []
    for lab, off in sorted(doc.labels.items(), key=lambda kv: kv[1]):
        if lab in refs or not (doc.d0 <= off):
            continue
        kind = doc.env_kind_at(off)
        if kind in STMT or kind in ("figure", "table"):
            bad.append((off, "%s (%s, %s)" % (lab, kind, doc.line(off))))
    if len(bad) < 3:
        return None
    return (bad[0][0], _lst([b[1] for b in bad], 4))


def fn_macro_unused(doc):
    if _isbib(doc) or not doc.d0:
        return None
    bad = []
    for m in re.finditer(r"\\(?:(?:re)?newcommand\*?\{?|DeclareMathOperator\*?\{)(\\[A-Za-z]+)\}?", doc.raw[:doc.d0]):
        n = len(re.findall(re.escape(m.group(1)) + r"(?![A-Za-z])", doc.raw))
        if n <= 1:
            bad.append((m.start(), m.group(1)))
    if len(bad) < 3:
        return None
    return (bad[0][0], _lst([b[1] for b in bad], 6))


def fn_pkg_twice(doc):
    if _isbib(doc) or not doc.d0:
        return None
    seen, bad = set(), []
    for m in re.finditer(r"\\usepackage\s*(?:\[[^\]]*\])?\s*\{([^}]+)\}", doc.raw[:doc.d0]):
        for p in m.group(1).split(","):
            p = p.strip()
            if p in seen:
                bad.append((m.start(), p))
            seen.add(p)
    if not bad:
        return None
    return (bad[0][0], _lst([b[1] for b in bad], 4))


def fn_thm_unused(doc):
    if _isbib(doc) or not doc.d0:
        return None
    bad = []
    for m in re.finditer(r"\\newtheorem\*?\{(\w+)\}", doc.raw[:doc.d0]):
        if ("\\begin{%s}" % m.group(1)) not in doc.raw:
            bad.append((m.start(), m.group(1)))
    if len(bad) < 2:
        return None
    return (bad[0][0], _lst([b[1] for b in bad], 6))


def _log(doc):
    if not doc.path:
        return None
    p = os.path.splitext(doc.path)[0] + ".log"
    try:
        if os.path.getmtime(p) + 2 < os.path.getmtime(doc.path):
            return None
        return open(p, "r", errors="replace").read()
    except Exception:
        return None


def fn_log_overfull(doc):
    log = _log(doc)
    if not log:
        return None
    w = [float(x) for x in re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\)", log)]
    w = [x for x in w if x > 5]
    if not w:
        return None
    return (0, "%d lines, the widest %.0fpt (see the .log)" % (len(w), max(w)))


def fn_log_multiply(doc):
    log = _log(doc)
    if not log:
        return None
    a = len(re.findall(r"multiply[- ]defined", log))
    b = len(re.findall(r"Missing character", log))
    if not a and not b:
        return None
    return (0, ", ".join(x for x in ("%d multiply defined" % a if a else "", "%d missing characters" % b if b else "") if x))


# ---------------------------------------------------------------- structure
def fn_numbered_definition(doc):
    if _isbib(doc):
        return None
    defs = [e for e in doc.envs if doc.thm.get(e[0]) == "definition"]
    inline = [(off, t) for t, off in doc.terms() if not any(a <= off < b for _, a, b, _, _ in defs) and doc.d0 <= off < doc.b0]
    if (not defs and len(inline) >= 2) or len(inline) >= 6:
        return (inline[0][0], "%d terms are defined in running text (%s)%s" % (
            len(inline), _lst(["'%s' %s" % (t, doc.line(o)) for o, t in inline], 3),
            " and the paper has no Definition environment" if not defs else ""))
    return None


def fn_roadmap(doc):
    if _isbib(doc):
        return None
    tops = [s for s in doc.secs if s["lvl"] == 0 and not s["app"] and s["num"]]
    if len(tops) < 4:
        return None
    P = doc.prose
    m = re.search(r"organi[sz]ed as follows|structure of (?:the|this) (?:paper|article)|outline of (?:the|this) paper"
                  r"|the (?:rest|remainder) of (?:the|this) (?:paper|article)|plan of the paper", P[doc.d0:doc.b0], re.I)
    if not m:
        if len(tops) >= 6:
            return (tops[0]["off"], "%d sections and no map of the paper in the introduction" % len(tops))
        return None
    a = doc.d0 + m.start()
    seg = P[a:a + 1400]
    end = re.search(r"\n\s*\n", seg)
    seg = seg[:end.start()] if end else seg
    n = len(re.findall(r"\bSections?\s+\x03|\bAppendi(?:x|ces)\s+\x03", seg))
    listed = any(nm in ("itemize", "enumerate", "description", "tabular", "table", "tikzpicture") and (a - 200 <= ea <= a + 600)
                 for nm, ea, eb, _, _ in doc.envs)
    if n >= 4 and not listed:
        return (a, "the map is one run of sentences over %d sections (%s); set it as a table: section, what it proves, what it uses"
                % (n, doc.line(a)))
    return None


def fn_ack_position(doc):
    if _isbib(doc):
        return None
    u = _back(doc, r"Acknowledge?ments?|Funding|Acknowledge?ments? and funding")
    if not u:
        return None
    if doc.app0 is not None and u[0] > doc.app0:
        return (u[0], "they come after the appendix (%s); move them before \\appendix" % doc.line(u[0]))
    if doc.b0 < doc.d1 and u[0] > doc.b0:
        return (u[0], "they come after the references (%s)" % doc.line(u[0]))
    return None


def fn_one_subsection(doc):
    if _isbib(doc):
        return None
    bad, cur, n = [], None, 0
    for s in doc.secs + [{"lvl": 0, "off": None, "title": ""}]:
        if s["lvl"] == 0:
            if cur is not None and n == 1:
                bad.append((cur["off"], "'%s'" % _clean(cur["title"])[:50]))
            cur, n = s, 0
        elif s["lvl"] == 1:
            n += 1
    if not bad:
        return None
    return (bad[0][0], _lst([b[1] for b in bad], 3))


def _case(title):
    w = [x for x in _clean(title).split() if re.match(r"[A-Za-z]", x)]
    if len(w) < 3:
        return None
    rest = [x for x in w[1:] if len(x) > 3]
    if not rest:
        return None
    cap = sum(1 for x in rest if x[0].isupper())
    if cap >= 0.7 * len(rest):
        return "title"
    if cap == 0:
        return "sentence"
    return None


def fn_heading_case_mixed(doc):
    if _isbib(doc):
        return None
    t = [(s["off"], _case(s["title"]), _clean(s["title"])) for s in doc.secs if s["lvl"] <= 1]
    ti = [x for x in t if x[1] == "title"]
    se = [x for x in t if x[1] == "sentence"]
    if not ti or not se or len(ti) + len(se) < 4:
        return None
    minority = ti if len(ti) <= len(se) else se
    return (minority[0][0], "%d headings in title case ('%s') and %d in sentence case ('%s')" % (
        len(ti), ti[0][2][:40], len(se), se[0][2][:40]))


def fn_heading_duplicate(doc):
    if _isbib(doc):
        return None
    seen, bad = {}, []
    for s in doc.secs:
        k = _clean(s["title"]).lower()
        if len(k) < 4:
            continue
        if k in seen:
            bad.append((s["off"], "'%s' at %s and %s" % (k[:50], doc.line(seen[k]), doc.line(s["off"]))))
        seen.setdefault(k, s["off"])
    if not bad:
        return None
    return (bad[0][0], _lst([b[1] for b in bad], 2))


def fn_intro_no_statement(doc):
    if _isbib(doc):
        return None
    tops = [s for s in doc.secs if s["lvl"] == 0]
    if len(tops) < 3 or not _envs(doc, {"theorem", "proposition"}):
        return None
    a, b = tops[0]["off"], tops[1]["off"]
    if any(a <= e[1] < b for e in _envs(doc, STMT | {"conjecture"})):
        return None
    if re.search(r"\b(?:Theorems?|Propositions?|Corollar(?:y|ies))\s+\x03", doc.prose[a:b]):
        return None
    return (a, "the first theorem is at %s" % doc.line(_envs(doc, {"theorem", "proposition"})[0][1]))


def fn_appendix_unreferenced(doc):
    if _isbib(doc) or doc.app0 is None:
        return None
    apps = [s for s in doc.secs if s["lvl"] == 0 and s["app"] and s["off"] < doc.b0 or (s["lvl"] == 0 and s["app"])]
    main_refs = set()
    for m in re.finditer(r"\\(?:eq|c|C|auto)?ref\{([^}]*)\}", doc.raw[doc.d0:doc.app0]):
        main_refs.update(x.strip() for x in m.group(1).split(","))
    bad = []
    for i, s in enumerate(apps):
        end = apps[i + 1]["off"] if i + 1 < len(apps) else len(doc.raw)
        if re.search(r"notation|symbols|terminology|acknowledg|funding|declaration|data availab", s["title"], re.I):
            continue
        inside = [lab for lab, off in doc.labels.items() if s["off"] <= off < end]
        if not any(lab in main_refs for lab in inside):
            bad.append((s["off"], "Appendix %s ('%s')" % (s["num"], _clean(s["title"])[:40])))
    if not bad:
        return None
    return (bad[0][0], _lst([b[1] for b in bad], 3))


def fn_short_paragraphs(doc):
    if _isbib(doc):
        return None
    P = _body(doc)
    paras = [p for p in re.split(r"\n\s*\n", P) if len(p.strip()) >= 40]
    short = [p for p in paras if len(p.strip()) < 220 and len(re.findall(r"[.!?](?:\s|$)", p.strip())) <= 1 and "\x01" not in p[:3]]
    if len(short) < 15 or len(short) < 0.5 * len(paras):
        return None
    return (P.find(short[0]), "%d of %d paragraphs are one short sentence" % (len(short), len(paras)))


# ---------------------------------------------------------------- statements and proofs
def fn_proof_long_unstructured(doc):
    if _isbib(doc):
        return None
    bad = []
    for n, a, b, ia, ib in doc.envs:
        if n != "proof" or ib - ia < 6000:
            continue
        t = doc.raw[ia:ib]
        if re.search(r"\b(?:Step|Case|Claim|Part)\s*(?:\d|[IVX]+\b|\(?[a-z]\))|\\paragraph|\\begin\{(?:enumerate|claim|step)\}|\\emph\{(?:Step|Case|Claim)", t):
            continue
        bad.append((a, "%d lines from %s" % (doc.lineno(ib) - doc.lineno(ia), doc.line(a))))
    if not bad:
        return None
    return (bad[0][0], _lst([x[1] for x in bad], 2) + "; mark the steps and say at the start how the proof goes")


def fn_statement_long(doc):
    if _isbib(doc):
        return None
    bad = []
    for n, a, b, ia, ib in _envs(doc, STMT):
        k = len(re.sub(r"\s+", " ", doc.raw[ia:ib]))
        if k > 2200:
            bad.append((a, "%s at %s (%d characters)" % (doc.thm.get(n), doc.line(a), k)))
    if not bad:
        return None
    return (bad[0][0], _lst([x[1] for x in bad], 2))


def fn_statement_unlabelled(doc):
    if _isbib(doc):
        return None
    bad = [(a, "%s at %s" % (doc.thm.get(n), doc.line(a))) for n, a, b, ia, ib in _envs(doc, STMT)
           if "\\label{" not in doc.raw[a:b] and doc.d0 <= a < doc.b0]
    if len(bad) < 2:
        return None
    return (bad[0][0], _lst([x[1] for x in bad], 4))


def fn_proof_names_statement(doc):
    if _isbib(doc):
        return None
    bad = []
    for n, a, b, ia, ib in doc.envs:
        if n != "proof" or not (doc.d0 <= a < doc.b0):
            continue
        if re.match(r"\s*\[", doc.raw[ia:ia + 10]):
            continue
        before = doc.raw[max(0, a - 400):a].rstrip()
        m = re.search(r"\\end\{([A-Za-z]+)\*?\}$", before)
        if m and doc.thm.get(m.group(1)) in STMT_ALL:
            continue
        bad.append((a, doc.line(a)))
    if not bad:
        return None
    return (bad[0][0], "%s; write \\begin{proof}[Proof of Theorem~\\ref{...}]" % _lst([x[1] for x in bad], 4))


def fn_proof_ends_display(doc):
    if _isbib(doc):
        return None
    bad = []
    for n, a, b, ia, ib in doc.envs:
        if n != "proof":
            continue
        t = doc.raw[ia:ib].rstrip()
        if re.search(r"(?:\\\]|\$\$|\\end\{(?:equation|align|gather|multline|displaymath)\*?\})$", t) and "\\qedhere" not in t[-400:]:
            bad.append((ib, doc.line(ib)))
    if not bad:
        return None
    return (bad[0][0], "%d (%s); put \\qedhere in the last line of the display" % (len(bad), _lst([x[1] for x in bad], 3)))


# ---------------------------------------------------------------- abstract and title
def fn_abstract_length(doc):
    if _isbib(doc) or not doc.abstract:
        return None
    a, b = doc.abstract
    n = len(re.findall(r"[A-Za-z][A-Za-z'\-]*|\x01", doc.prose[a:b]))
    if n <= 170:
        return None
    return (a, "%d words; aim for under 150" % n)


def fn_title_case(doc):
    if _isbib(doc) or not doc.title:
        return None
    t = _clean(doc.raw[doc.title[0]:doc.title[1]])
    letters = [c for c in t if c.isalpha()]
    if len(letters) < 8:
        return None
    if sum(1 for c in letters if c.isupper()) > 0.7 * len(letters):
        return (doc.title[0], "the title is in capitals: '%s'" % t[:60])
    if t[0].isalpha() and t[0].islower():
        return (doc.title[0], "the title starts in lower case: '%s'" % t[:60])
    return None


def fn_abstract_numbers(doc):
    if _isbib(doc) or not doc.abstract:
        return None
    a, b = doc.abstract
    rest = doc.raw[b:doc.b0] if a >= doc.d0 else doc.raw[doc.d0:doc.b0]
    rest_flat = re.sub(r"[{},\\\s]", "", rest)
    bad = []
    for m in re.finditer(r"(?<![\w.\\{])(\d+\.\d+|\d{1,3}(?:,\d{3})+|\d{2,})(?![\w}])", doc.raw[a:b]):
        num = m.group(1)
        if re.match(r"(?:19|20)\d\d$", num):
            continue
        if num.replace(",", "") not in rest_flat:
            bad.append((a + m.start(), num))
    if not bad:
        return None
    return (bad[0][0], _lst(sorted(set(x[1] for x in bad)), 4))


def fn_abstract_symbols(doc):
    if _isbib(doc) or not doc.abstract:
        return None
    a, b = doc.abstract
    seen, bad = set(), []
    for n, off in _names(doc.math[a:b]):
        if n in seen or (len(n) == 1 and n in DUMMY) or n in _STD or re.match(r"\\[a-z]+$", n) and n not in _eng()._GREEK:
            continue
        seen.add(n)
        if not doc.defined_near(n, a + off):
            bad.append((a + off, n))
    if len(bad) < 2:
        return None
    return (bad[0][0], _lst([x[1] for x in bad], 5))


def fn_msc_missing(doc):
    if _isbib(doc) or not doc.title or not doc.abstract:
        return None
    if re.search(r"\\subjclass|\\keywords|\bMSC\b|Mathematics Subject Classification|Key ?words", doc.raw):
        return None
    return (doc.abstract[1], "add \\subjclass and \\keywords")


# ---------------------------------------------------------------- floats and numbers
def _floats(doc):
    return [e for e in doc.envs if e[0] in ("figure", "table")]


def fn_float_unreferenced(doc):
    if _isbib(doc):
        return None
    refs, bad = _refs(doc), []
    for n, a, b, ia, ib in _floats(doc):
        labs = re.findall(r"\\label\{([^}]+)\}", doc.raw[ia:ib])
        if labs and not any(l in refs for l in labs):
            bad.append((a, "%s %s (%s)" % (n, labs[0], doc.line(a))))
    if not bad:
        return None
    return (bad[0][0], _lst([x[1] for x in bad], 3))


def fn_float_incomplete(doc):
    if _isbib(doc):
        return None
    bad = []
    for n, a, b, ia, ib in _floats(doc):
        t = doc.raw[ia:ib]
        miss = [w for w, k in (("caption", "\\caption"), ("label", "\\label{")) if k not in t]
        if miss:
            bad.append((a, "%s at %s has no %s" % (n, doc.line(a), " and no ".join(miss))))
    if not bad:
        return None
    return (bad[0][0], _lst([x[1] for x in bad], 3))


def _captions(doc):
    return [(a, re.sub(r"\s+", " ", doc.prose[a:b]).strip()) for a, b in doc.caps]


def fn_caption_short(doc):
    if _isbib(doc):
        return None
    bad = [(a, "'%s' (%s)" % (t[:40], doc.line(a))) for a, t in _captions(doc) if len(t.split()) < 6]
    if not bad:
        return None
    return (bad[0][0], _lst([x[1] for x in bad], 3) + "; say what is shown, for which parameters, and what to see")


def fn_caption_period_mixed(doc):
    if _isbib(doc):
        return None
    caps = [(a, t) for a, t in _captions(doc) if t]
    yes = [a for a, t in caps if t.endswith(".")]
    no = [a for a, t in caps if not t.endswith(".")]
    if len(caps) < 3 or not yes or not no:
        return None
    return ((no if len(no) <= len(yes) else yes)[0], "%d with a period, %d without" % (len(yes), len(no)))


def fn_seeds_missing(doc):
    if _isbib(doc):
        return None
    P = _body(doc)
    if _count(r"\bsimulat\w+|\bmonte carlo\b|\brandom(?:ly)? (?:initiali[sz]|sampl|generat)\w+", P) < 3:
        return None
    if re.search(r"\bseeds?\b|\b\d[\d,]*\s+(?:independent\s+)?(?:runs|trials|replications|repetitions|samples|simulations|realizations|"
                 r"realisations|paths|draws)\b|\x01\s+(?:independent\s+)?(?:runs|trials|replications|samples|paths)\b", P, re.I):
        return None
    return (_first(r"\bsimulat\w+|\bmonte carlo\b", P), "say how many runs, and the seeds or how they were drawn")


def _finance(P):
    return _count(r"\bsharpe\b|\bdrawdown|\bportfolio|\bbacktest|\btrading strateg|\bhedg(?:e|ed|ing)\b", P) >= 3


def fn_gross_net(doc):
    if _isbib(doc):
        return None
    P = _body(doc)
    if not _finance(P) or _count(r"\breturns?\b|\bCAGR\b|\bP&L\b|\bprofits?\b|\bannuali[sz]ed\b", P) < 3:
        return None
    if re.search(r"\bgross\b|\bnet of\b|\bnet return|\bafter (?:fees|costs)|\bbefore (?:fees|costs)|\bnet-of", P, re.I):
        return None
    return (_first(r"\breturns?\b|\bCAGR\b", P), "say gross or net of which fees and costs, once, where the first number is given")


def fn_costs_unstated(doc):
    if _isbib(doc):
        return None
    P = _body(doc)
    if _count(r"\bbacktest\w*|\bsimulated trading|\bstrategy returns?|\bhistorical simulation", P) < 2:
        return None
    if re.search(r"\bcommissions?\b|\btransaction costs?\b|\bslippage\b|\bbid[- ]ask\b|\bspreads?\b|\bfills?\b|\bborrow\b|\bfees?\b", P, re.I):
        return None
    return (_first(r"\bbacktest\w*", P), "say at what price orders fill and what is charged (commission, spread, borrow)")


def fn_insample(doc):
    if _isbib(doc):
        return None
    P = _body(doc)
    if not re.search(r"\bbacktest\w*|\bgrid search|\bparameter sweep|\btuned\b|\boptimi[sz]ed (?:the )?(?:hyper)?parameters|\bcalibrat\w+|\bselected the (?:best|parameters)", P, re.I):
        return None
    if not re.search(r"\bsharpe\b|\breturns?\b|\bdrawdown|\baccuracy\b|\btest error|\bperformance\b", P, re.I):
        return None
    if re.search(r"\bin[- ]sample|\bout[- ]of[- ]sample|\bhold[- ]?out|\btest set|\bvalidation\b|\bwalk[- ]forward|\bcross[- ]validat", P, re.I):
        return None
    return (_first(r"\bbacktest\w*|\bgrid search|\bparameter sweep|\btuned\b|\bcalibrat\w+", P),
            "say whether the reported numbers are in-sample, and give an out-of-sample figure if there is one")


# ---------------------------------------------------------------- bibliography
def fn_bib_no_locator(doc):
    items = _bibitems(doc)
    bad = []
    for off, key, t in items:
        if not re.search(r"(?:19|20)\d\d", t):
            bad.append((off, "%s (no year)" % key))
        elif not _isbib(doc) and not re.search(
                r"\d+\s*[(:,]|arXiv|doi|https?:|\\url|[Ii]n preparation|[Pp]reprint|[Ss]ubmitted|[Mm]anuscript|[Tt]o appear|Press|Springer|Wiley|Birkh|AMS|Society|Universit|[Tt]hesis|Verlag|Elsevier|SIAM|"
                r"Publish|Lecture Notes|Proceedings|Conference|Dover|Academic|North-Holland|Hermann|Cambridge|Oxford|Princeton", t):
            bad.append((off, "%s (no journal, publisher or identifier)" % key))
    if not bad:
        return None
    return (bad[0][0], _lst([x[1] for x in bad], 4))


def fn_bib_journal_mixed(doc):
    items = _bibitems(doc)
    ab = [(off, key) for off, key, t in items if re.search(r"\b(?:Ann|J|Trans|Comm|Bull|Adv|Proc|Electron|Probab|Math)\.\s+(?:of\s+)?[A-Z]", t)]
    fu = [(off, key) for off, key, t in items if re.search(r"\b(?:Journal of|Annals of|Transactions of|Communications (?:in|on)|Bulletin of|Advances in|Electronic Journal|Electronic Communications)\b", t)
          and not re.search(r"\b(?:Ann|J|Trans|Comm|Bull|Adv)\.\s", t)]
    if not ab or not fu:
        return None
    minority = fu if len(fu) <= len(ab) else ab
    return (minority[0][0], "%d entries abbreviate the journal (%s) and %d write it out (%s)" % (len(ab), ab[0][1], len(fu), fu[0][1]))


def fn_bib_title_case(doc):
    items = _bibitems(doc)
    ti, se = [], []
    for off, key, t in items:
        m = re.search(r"title\s*=\s*[{\"]+([^}\"]{15,})", t) if _isbib(doc) else None
        if m:
            cand = m.group(1)
        else:
            segs = [s for s in re.split(r"(?<=[a-z0-9}])[.,]\s+|\\newblock|\\emph\{|\\textit\{|``|''", t) if len(s.split()) >= 5]
            cand = max(segs, key=len) if segs else ""
        c = _case(cand) if cand else None
        if c == "title":
            ti.append((off, key))
        elif c == "sentence":
            se.append((off, key))
    if len(ti) < 3 or len(se) < 3:
        return None
    minority = ti if len(ti) <= len(se) else se
    return (minority[0][0], "%d titles capitalise every word (%s) and %d do not (%s)" % (len(ti), ti[0][1], len(se), se[0][1]))


def fn_self_cite_share(doc):
    items = _bibitems(doc)
    if len(items) < 6 or _isbib(doc):
        return None
    m = re.search(r"\\author\s*(?:\[[^\]]*\])?\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", doc.raw)
    if not m:
        return None
    names = set(x.split()[-1] for x in re.split(r"\\and|,|\band\b|\\\\", _clean(m.group(1))) if x.split() and len(x.split()[-1]) > 3)
    if not names:
        return None
    own = [off for off, key, t in items if any(n in t for n in names)]
    if len(own) <= 0.5 * len(items):
        return None
    return (own[0], "%d of %d entries" % (len(own), len(items)))


# ---------------------------------------------------------------- declarations
def fn_funding_complete(doc):
    if _isbib(doc):
        return None
    u = _back(doc, r"Acknowledge?ments?|Funding")
    if not u:
        return None
    t = doc.raw[u[0]:u[1]]
    if not re.search(r"101041711|European Research Council|\bERC\b|Simons", t):
        return None
    miss = [w for w, rx in (("ERC grant 101041711", r"101041711"), ("the Simons Foundation", r"Simons"),
                            ("Google", r"Google")) if not re.search(rx, t)]
    if not miss:
        return None
    return (u[0], "missing " + _lst(miss, 4))


def fn_ai_declaration(doc):
    if _isbib(doc):
        return None
    u = _back(doc, r"(?:Declaration of |Use of |Statement on )?(?:generative )?(?:AI|artificial intelligence)[^}]*|Declaration of generative[^}]*")
    if not u:
        return None
    t = doc.prose[u[0]:u[1]]
    n = len(t.split())
    diary = _count(r"\b(?:first|then|afterwards?|initially|later|subsequently|fixed|corrected|mistakes?|errors?|rounds?|passes|"
                   r"iterations?|sessions?|prompts?|re-?ran|re-?derived|retried|rewrote|earlier (?:draft|version))\b", t)
    if n > 130:
        return (u[0], "%d words; three or four sentences are enough" % n)
    if diary >= 3:
        return (u[0], "%d process words (then, later, corrected, round); say which system did what, once" % diary)
    return None


def fn_data_availability(doc):
    if _isbib(doc):
        return None
    P = _body(doc)
    if _count(r"\bsimulat\w+|\bmonte carlo\b|\bnumerical (?:experiment|check|comput)\w*|\bwe comput\w+|\bcomputed (?:numerically|with|by)|\bscripts?\b", P) < 3:
        return None
    if re.search(r"github|zenodo|repositor|\\url\{|\\href\{|doi\.org/10\.5281|available at", doc.raw, re.I):
        return None
    return (_first(r"\bsimulat\w+|\bmonte carlo\b|\bnumerical\b", P), "give the repository and the commit, in a data and code availability paragraph")
