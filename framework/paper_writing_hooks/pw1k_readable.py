"""Readability rules for pw1k: a paper a person can read, follow and enjoy.

Twenty rules keep a paper readable: every symbol and term defined before use, every claim cited, the main
derivations written out step by step, and a table of symbols at the end. Five more rules are derived from each.

READ holds 20 core rules (C01..C20) and five rules derived from each (C01a..C01e, ...), 120 in all. Each is either a
regular expression on one scope of the document (kind "rx", the same scopes as pw1k_rules.RX) or a detector in this
module (kind "fn"). pw1k.rules() appends them after the event lines, so the ids of the older rules never move; their
ids are P1102 onward, chapter "readable". pw1k_readable_selftest.py holds a firing fixture for every rule and a clean
paper on which none of them fires.

Absence rules (no history paragraph, no example, no plain-words sentence) run only on a whole paper: not a .bib file,
not a fragment without \\begin{document}, not a research statement or cover letter, and at least 600 words of text.
"""
import re

import pw1k_detect as D

_isbib, _envs, _bibitems, _refs, _lst, _names = D._isbib, D._envs, D._bibitems, D._refs, D._lst, D._names


def _E():
    return D._eng()


def _words(t):
    return len(re.findall(r"[A-Za-z]{2,}", t))


def _paper(doc, words=600):
    if _isbib(doc) or "\\begin{document}" not in doc.raw:
        return False
    try:
        if _E().application_doc(doc):
            return False
    except Exception:
        pass
    c = doc._cache.get("rd_words")
    if c is None:
        c = doc._cache["rd_words"] = _words(doc.prose[doc.d0:doc.b0])
    return c >= words


def _tops(doc, app=False):
    return [s for s in doc.secs if s["lvl"] == 0 and (app or not s["app"])]


def _sec_end(doc, s):
    for t in doc.secs:
        if t["off"] > s["off"] and t["lvl"] <= s["lvl"]:
            return t["off"]
    return doc.b0 if s["off"] < doc.b0 else len(doc.raw)


def _next_head(doc, s):
    for t in doc.secs:
        if t["off"] > s["off"]:
            return t["off"]
    return doc.b0 if s["off"] < doc.b0 else len(doc.raw)


def _intro(doc):
    t = _tops(doc)
    if not t:
        return None
    return (t[0]["off"], t[1]["off"] if len(t) > 1 else doc.b0)


def _kind_envs(doc, kinds):
    return [e for e in doc.envs if doc.thm.get(e[0]) in kinds]


_THMS = {"theorem", "proposition", "corollary"}
_STMTS = {"theorem", "lemma", "proposition", "corollary", "claim", "conjecture"}
_PROOFS = lambda doc: [e for e in doc.envs if e[0] == "proof"]
_JUST = re.compile(r"\\(?:text|intertext|shortintertext|tag|eqref|overset|stackrel|underset|ref|cref)\b")
_JUSTP = re.compile(r"\b(?:by|since|using|because|follows|from|where|first|second|third|last|final|step|line)\b", re.I)


def _disp(doc):
    return [(a, b) for a, b, d in doc.mspans if d and doc.d0 <= a < doc.b0]


def _sentence_after(doc, off, n=600):
    return doc.prose[off:off + n]


def _inner_prose(doc, e):
    t = doc.prose[e[3]:e[4]]
    return re.sub(r"^\s*\[[^\]\n]*\]", "", t)


def _occ(doc):
    """{symbol name: [offsets]} over the formulas, for the symbols pw1k counts as real."""
    c = doc._cache.get("rd_occ")
    if c is not None:
        return c
    real = set(n for o, n, k, kk in _real(doc))
    out = {}
    for name, off in _names(doc.math):
        if name in real:
            out.setdefault(name, []).append(off)
    doc._cache["rd_occ"] = out
    return out


def _real(doc):
    c = doc._cache.get("rd_real")
    if c is None:
        try:
            c = D._real_symbols(doc)
        except Exception:
            c = []
        doc._cache["rd_real"] = c
    return c


def _in(spans, off):
    return any(a <= off < b for a, b in spans)


def _top_index(doc, off):
    t = _tops(doc, app=True)
    k = -1
    for i, s in enumerate(t):
        if s["off"] <= off:
            k = i
    return k


# ======================================================================== C01 the table of symbols at the end
_NOTA_T = re.compile(r"notation|symbols|nomenclature|glossary", re.I)


def rd_nota_not_last(doc):
    if not _paper(doc):
        return None
    n = doc.notation_section()
    if not n:
        return None
    later = [s for s in doc.secs if s["lvl"] == 0 and n[0] < s["off"] < doc.b0]
    if later:
        return (later[0]["off"], "'%s' comes after it" % D._clean(later[0]["title"])[:50])
    return None


def rd_nota_in_body(doc):
    if not _paper(doc) or doc.notation_section():
        return None
    for s in doc.secs:
        if not s["app"] and _NOTA_T.search(s["title"]) and re.search(r"table|list|index|summary|^\s*(?:notation|symbols)\s*$",
                                                                     s["title"], re.I):
            return (s["off"], "'%s' is in the body" % D._clean(s["title"])[:50])
    return None


def rd_nota_not_pointed(doc):
    if not _paper(doc):
        return None
    n = doc.notation_section()
    if not n:
        return None
    s = next(x for x in doc.secs if x["off"] == n[0])
    if s["label"] and s["label"] in _refs(doc):
        return None
    if re.search(r"(?:table|list|index) of (?:symbols|notation)|symbols? (?:are|is) (?:listed|collected|gathered)",
                 doc.prose[doc.d0:n[0]], re.I):
        return None
    return (n[0], "no sentence before it sends the reader there")


def rd_nota_no_label(doc):
    if not _paper(doc):
        return None
    n = doc.notation_section()
    if not n:
        return None
    s = next(x for x in doc.secs if x["off"] == n[0])
    return None if s["label"] else (n[0], "")


def rd_nota_twice(doc):
    if not _paper(doc):
        return None
    hs = [s for s in doc.secs if re.search(r"\b(?:notation|symbols|nomenclature|glossary)\b", s["title"], re.I)
          and re.search(r"table|list|index|summary|glossary|nomenclature|^\s*(?:notation|symbols)\s*$", s["title"], re.I)]
    if len(hs) >= 2:
        return (hs[1]["off"], "%s and %s" % (doc.line(hs[0]["off"]), doc.line(hs[1]["off"])))
    return None


def rd_nota_no_header(doc):
    if not _paper(doc):
        return None
    n = doc.notation_section()
    if not n:
        return None
    t = doc.raw[n[0]:n[1]]
    m = re.search(r"\\begin\{(?:tabular|longtable|tabularx)\*?\}(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})+", t)
    if not m:
        return (n[0], "the symbols are not set as a table")
    head = re.split(r"\\\\", t[m.end():], maxsplit=1)[0]
    if re.search(r"symbol|notation|meaning|description|defined|where|first", head, re.I):
        return None
    return (n[0] + m.start(), "the first row is not a header (Symbol & Meaning & Where defined)")


# ======================================================================== C02 everything defined
def rd_def_no_emph(doc):
    if not _paper(doc):
        return None
    bad = [e for e in _kind_envs(doc, {"definition"})
           if not re.search(r"\\(?:emph|textit|textbf|textsl|defn|term|index)\b|\{\\(?:em|it|bf)\b", doc.raw[e[3]:e[4]])]
    if not bad:
        return None
    return (bad[0][1], "%d definition(s) do not mark the word being defined, first at %s" % (len(bad), doc.line(bad[0][1])))


# ======================================================================== C03 definitions easy to look up
def rd_defs_unlabelled(doc):
    if not _paper(doc):
        return None
    ds = _kind_envs(doc, {"definition"})
    bad = [e for e in ds if "\\label{" not in doc.raw[e[3]:e[4]]]
    if len(ds) >= 3 and len(bad) >= 2:
        return (bad[0][1], "%d of %d definitions carry no \\label, so nothing can point back to them" % (len(bad), len(ds)))
    return None


def rd_remark_defines(doc):
    if not _paper(doc):
        return None
    for e in _kind_envs(doc, {"remark", "example", "observation"}):
        m = re.search(r"\bwe (?:call|define|say that|write)\b|\bis (?:called|said to be)\b|\bwill be called\b", doc.prose[e[3]:e[4]], re.I)
        if m:
            return (e[3] + m.start(), "a remark at %s defines something; give it a numbered Definition" % doc.line(e[1]))
    return None


# ======================================================================== C04 / C05 derivations and steps explained
def rd_display_chain(doc):
    if not _paper(doc):
        return None
    ds = _disp(doc)
    run, best = 1, None
    for (a1, b1), (a2, b2) in zip(ds, ds[1:]):
        if _words(doc.prose[b1:a2]) < 3:
            run += 1
            if run >= 3 and best is None:
                best = (a2, run)
        else:
            run = 1
    if best:
        return (best[0], "three or more displays in a row with almost no words between them, at %s" % doc.line(best[0]))
    return None


def _aligns(doc):
    return [e for e in doc.envs if e[0] in ("align", "eqnarray", "alignat", "flalign", "split", "aligned")
            and doc.d0 <= e[1] < doc.b0]


def rd_align_silent(doc):
    if not _paper(doc):
        return None
    for e in _aligns(doc):
        t = doc.raw[e[3]:e[4]]
        rows = len(re.findall(r"\\\\", t)) + 1
        if rows >= 5 and not _JUST.search(t) and not _JUSTP.search(doc.prose[e[2]:e[2] + 300]):
            return (e[1], "%d lines at %s and not one word on where a line comes from" % (rows, doc.line(e[1])))
    return None


def rd_ineq_chain_silent(doc):
    if not _paper(doc):
        return None
    for e in _aligns(doc):
        t = doc.raw[e[3]:e[4]]
        rel = len(re.findall(r"&\s*(?:\\le(?:q|qslant)?|\\ge(?:q|qslant)?|<|>|\\lesssim|\\gtrsim|\\ll|\\gg)(?![a-z])", t))
        if rel >= 2 and not _JUST.search(t) and not _JUSTP.search(doc.prose[e[2]:e[2] + 300]):
            return (e[1], "a chain of %d inequalities at %s; say why each step holds" % (rel + 1, doc.line(e[1])))
    return None


def rd_proof_all_math(doc):
    if not _paper(doc):
        return None
    for e in _PROOFS(doc):
        if e[4] - e[3] < 300:
            continue
        inner = doc.prose[e[3]:e[4]]
        nd = sum(1 for a, b in _disp(doc) if e[3] <= a < e[4])
        if nd >= 2 and _words(inner) < 15:
            return (e[1], "the proof at %s is %d displays and %d words" % (doc.line(e[1]), nd, _words(inner)))
    return None


def rd_proof_opens_similar(doc):
    if not _paper(doc):
        return None
    for e in _PROOFS(doc):
        t = _inner_prose(doc, e).lstrip()
        if re.match(r"(?:Similar(?:ly)?|Analogous(?:ly)?|The same (?:argument|proof|reasoning)|As in the proof of|This is (?:similar|analogous)|"
                    r"Same as|Repeat the|Follow the proof)\b", t):
            return (e[3], "the proof at %s begins by sending the reader to another proof; write out what changes" % doc.line(e[1]))
    return None


# ======================================================================== C06 / C07 history and citations
def rd_intro_few_cites(doc):
    if not _paper(doc):
        return None
    it = _intro(doc)
    if not it or len(_bibitems(doc)) < 5 and "\\bibliography{" not in doc.raw:
        return None
    p = doc.prose[it[0]:it[1]]
    if _words(p) < 150:
        return None
    n = p.count("\x02") + p.count("\x05")
    if n < 3:
        return (it[0], "the introduction cites %d work(s); tell the history of the problem with its citations" % n)
    return None


def _cite_keys(doc):
    keys = []
    for m in re.finditer(r"\\(?:no)?cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}", doc.raw):
        keys += [(k.strip(), m.start()) for k in m.group(1).split(",") if k.strip()]
    return keys


def _thebib(doc):
    return [b for b in _bibitems(doc)] if not _isbib(doc) and "\\begin{thebibliography}" in doc.raw else []


def rd_cite_missing(doc):
    B = _thebib(doc)
    if not B:
        return None
    have = set(k for _, k, _ in B)
    bad = [(o, k) for k, o in _cite_keys(doc) if k not in have and k != "*"]
    return (bad[0][0], "cited and not in the bibliography: " + _lst(sorted(set(k for _, k in bad)), 4)) if bad else None


def rd_bib_uncited(doc):
    B = _thebib(doc)
    if not B or re.search(r"\\nocite\{\*\}", doc.raw):
        return None
    used = set(k for k, _ in _cite_keys(doc))
    bad = [(o, k) for o, k, _ in B if k not in used]
    return (bad[0][0], "in the bibliography and never cited: " + _lst([k for _, k in bad], 4)) if bad else None


def rd_bib_duplicate(doc):
    B = _thebib(doc)
    seen, dup = {}, []
    for o, k, t in B:
        m = re.search(r"\\(?:emph|textit|textsl)\{([^{}]{10,200})\}|``([^']{10,200})''", t)
        if not m:
            continue
        vol = re.search(r"\d+", t[m.end():m.end() + 60])  # the emph may be a journal (28 Nov): add the volume
        pages = re.search(r"\d+\s*(?:-{1,3}|[–—]|\\textendash\s*)\s*\d+", t[m.end():])  # same journal and volume, different pages: two papers; '416--429' and '416–429' are one range (28 Nov)
        key = (re.sub(r"[^a-z0-9]", "", (m.group(1) or m.group(2)).lower()) + "|" + (vol.group(0) if vol else "")
               + "|" + (re.sub(r"\D+", "-", pages.group(0)) if pages else ""))
        if key in seen:
            dup.append((o, "%s and %s" % (seen[key], k)))
        seen.setdefault(key, k)
    return (dup[0][0], _lst([d[1] for d in dup], 3)) if dup else None


def rd_bib_arxiv_noid(doc):
    bad = [(o, k) for o, k, t in _thebib(doc) if re.search(r"arxiv", t, re.I) and not re.search(r"\d{4}\.\d{4,5}|[a-z\-]+/\d{7}", t)]
    return (bad[0][0], _lst([k for _, k in bad], 4)) if bad else None


def rd_bib_toappear_noid(doc):
    bad = [(o, k) for o, k, t in _thebib(doc)
           if re.search(r"\bto appear\b|\bin preparation\b|\bpreprint\b|\bsubmitted\b|\bforthcoming\b", t, re.I)
           and not re.search(r"\d{4}\.\d{4,5}|doi|https?:|\\url|\\href", t, re.I)]
    return (bad[0][0], _lst([k for _, k in bad], 4)) if bad else None


# ======================================================================== C08 accessible to a person
_PLAIN = re.compile(r"\b(?:in words|in other words|roughly|informally|that is|this says|this means|put differently|intuitively|"
                    r"in plain terms|the point is|loosely|says that|asserts that|means that|the content of|the meaning of|"
                    r"in short|that is to say)\b", re.I)


def _intro_thms(doc):
    it = _intro(doc)
    if not it:
        return []
    return [e for e in _kind_envs(doc, _THMS) if it[0] <= e[1] < it[1]]


def rd_thm_no_plain_words(doc):
    if not _paper(doc):
        return None
    ts = _intro_thms(doc)
    if not ts:
        return None
    e = ts[0]
    if _PLAIN.search(doc.prose[e[2]:e[2] + 500]) or _PLAIN.search(doc.prose[max(0, e[1] - 400):e[1]]):
        return None
    return (e[2], "no sentence next to the first theorem (%s) says in plain words what it means" % doc.line(e[1]))


def rd_no_informal_anywhere(doc):
    if not _paper(doc):
        return None
    if len(_kind_envs(doc, _STMTS)) < 3:
        return None
    if re.search(r"\b(?:informally|intuitively|roughly|the idea|heuristic\w*|in words|in other words|the intuition)\b",
                 doc.prose[doc.d0:doc.b0], re.I):
        return None
    return (doc.d0, "%d statements and not one informal explanation of why they hold" % len(_kind_envs(doc, _STMTS)))


def rd_sentence_long(doc):
    if not _paper(doc):
        return None
    p = doc.prose
    disp = _disp(doc)
    for m in re.finditer(r"[^.!?]{300,}?[.!?](?=\s)", p[doc.d0:doc.b0]):
        a, b = doc.d0 + m.start(), doc.d0 + m.end()
        if any(a <= x < b for x, y in disp) or doc.env_kind_at(a) in _STMTS | {"definition"}:
            continue
        n = _words(m.group(0)) + m.group(0).count("\x01")
        if n > 70:
            return (doc.d0 + m.start(), "a sentence of %d words at %s; split it" % (n, doc.line(doc.d0 + m.start())))
    return None


# ======================================================================== C09 examples
_EXW = re.compile(r"\b(?:example|for instance|for example|e\.g\.|consider|instance|illustrat\w*|special case|in particular)\b", re.I)


def _has_example_env(doc):
    return any(doc.thm.get(e[0]) == "example" for e in doc.envs)


def rd_defs_no_example(doc):
    if not _paper(doc):
        return None
    bad = []
    for e in _kind_envs(doc, {"definition"}):
        after = doc.prose[e[2]:e[2] + 1500]
        nxt = [x for x in doc.envs if x[1] >= e[2] and doc.thm.get(x[0]) == "example" and x[1] < e[2] + 1500]
        if not _EXW.search(after) and not nxt:
            bad.append(e)
    if len(bad) >= 2:
        return (bad[0][1], "%d definitions are not followed by an example, first at %s" % (len(bad), doc.line(bad[0][1])))
    return None


def rd_no_examples_at_all(doc):
    if not _paper(doc):
        return None
    if len(_kind_envs(doc, _STMTS | {"definition"})) < 3 or _has_example_env(doc):
        return None
    if re.search(r"\bfor (?:example|instance)\b", doc.prose[doc.d0:doc.b0], re.I):
        return None
    return (doc.d0, "no example anywhere in the paper")


def rd_thm_no_special_case(doc):
    if not _paper(doc):
        return None
    ts = [e for e in _kind_envs(doc, _THMS) if doc.d0 <= e[1] < doc.b0]
    if not ts:
        return None
    e = ts[0]
    if re.search(r"\b(?:in particular|special case|for example|for instance|example|e\.g\.|simplest case|when \x01 ?=)", doc.prose[e[2]:e[2] + 3000], re.I):
        return None
    if any(doc.thm.get(x[0]) in ("example", "corollary") and e[2] <= x[1] < e[2] + 3000 for x in doc.envs):
        return None
    return (e[2], "no special case or example follows the first theorem (%s)" % doc.line(e[1]))


_OBJ = re.compile(r"\b(?:graph|tree|curve|polygon|region|lattice|path|cycle|vert(?:ex|ices)|triangle|polytope|surface|knot|tiling|"
                  r"configuration|cube|simplex|hexagon|square)s?\b", re.I)


def rd_no_figure(doc):
    if not _paper(doc):
        return None
    if re.search(r"\\begin\{(?:figure|tikzpicture)|\\includegraphics", doc.raw):
        return None
    n = len(_OBJ.findall(doc.prose[doc.d0:doc.b0]))
    if n >= 25:
        return (doc.d0, "the text names geometric or combinatorial objects %d times and shows no picture of one" % n)
    return None


def rd_hypotheses_untested(doc):
    if not _paper(doc):
        return None
    if len(_kind_envs(doc, _THMS)) < 3:
        return None
    if re.search(r"\bnecessary\b|\bcannot be (?:dropped|removed|omitted|weakened|relaxed)|\bsharp\b|\boptimal\b|best possible|"
                 r"counter-?example|\bfails\b|\bneeded\b|\bessential\b", doc.prose[doc.d0:doc.b0], re.I):
        return None
    return (doc.d0, "nothing says whether the hypotheses are needed")


def rd_def_conditions_no_example(doc):
    if not _paper(doc):
        return None
    for e in _kind_envs(doc, {"definition"}):
        t = doc.raw[e[3]:e[4]]
        n = len(re.findall(r"\\item\b|\((?:i|ii|iii|iv|v|vi|a|b|c|d|1|2|3|4)\)", t))
        if n >= 3 and not _EXW.search(doc.prose[e[2]:e[2] + 1500]):
            return (e[1], "a definition with %d conditions at %s and no example of an object that meets them" % (n, doc.line(e[1])))
    return None


# ======================================================================== C10 sections open with words
def _first_block(doc, a, b):
    starts = [x[1] for x in doc.envs if a <= x[1] < b and (x[0] in doc.thm or x[0] == "proof")]
    starts += [x for x, y in _disp(doc) if a <= x < b]
    return min(starts) if starts else None


def rd_section_opens_cold(doc):
    if not _paper(doc):
        return None
    for s in _tops(doc):
        end = _next_head(doc, s)
        f = _first_block(doc, s["tend"], end)
        if f is not None and _words(doc.prose[s["tend"]:f]) < 10:
            return (s["off"], "Section '%s' opens with a statement or a formula; open with a sentence on what the section does"
                    % D._clean(s["title"])[:40])
    return None


def rd_subsection_opens_cold(doc):
    if not _paper(doc):
        return None
    for s in doc.secs:
        if s["lvl"] == 0 or s["app"]:
            continue
        f = _first_block(doc, s["tend"], _next_head(doc, s))
        if f is not None and _words(doc.prose[s["tend"]:f]) < 6:
            return (s["off"], "'%s' opens with a statement or a formula" % D._clean(s["title"])[:40])
    return None


def rd_heading_then_heading(doc):
    if not _paper(doc):
        return None
    for s, t in zip(doc.secs, doc.secs[1:]):
        if t["lvl"] > s["lvl"] and _words(doc.prose[s["tend"]:t["off"]]) < 10:
            return (t["off"], "'%s' is followed at once by '%s'; say what the section contains first"
                    % (D._clean(s["title"])[:30], D._clean(t["title"])[:30]))
    return None


def rd_long_proof_no_close(doc):
    if not _paper(doc):
        return None
    for e in _PROOFS(doc):
        if e[4] - e[3] < 2500:
            continue
        if not re.search(r"\b(?:complete|completes|proves|proved|as claimed|as required|as desired|concludes|we are done|done|establish\w*|"
                         r"finish\w*|gives|yields|follows|(?<!\bto\s)shows?|(?<!\bbe\s)shown|is the (?:theorem|lemma|claim|proposition|corollary|statement))\b",
                         doc.prose[max(e[3], e[4] - 400):e[4]], re.I):  # 'Steps 1-4 show ..., which is the theorem' closes it (28 Nov)
            return (e[4], "the long proof at %s stops without a sentence saying what has now been shown" % doc.line(e[1]))
    return None


_CONC = re.compile(r"conclu|discussion|open (?:problems|questions)|questions|remarks|outlook|final|further|future|problems", re.I)


def rd_no_conclusion(doc):
    if not _paper(doc):
        return None
    t = _tops(doc)
    if len(t) < 5 or any(_CONC.search(s["title"]) for s in t[1:]):
        return None
    return (t[-1]["off"], "%d sections and none that says what was found and what is still open" % len(t))


def rd_subsection_thin(doc):
    if not _paper(doc):
        return None
    for s in doc.secs:
        if s["lvl"] == 0 or s["app"]:
            continue
        n = _words(doc.prose[s["tend"]:_next_head(doc, s)])
        if n < 40:
            return (s["off"], "'%s' has %d words; merge it or say more" % (D._clean(s["title"])[:40], n))
    return None


# ======================================================================== C11 what the result means
def rd_intro_no_contribution(doc):
    if not _paper(doc):
        return None
    it = _intro(doc)
    if not it or _words(doc.prose[it[0]:it[1]]) < 150:
        return None
    if re.search(r"\bour (?:main )?(?:results?|contributions?|theorems?)\b|\bwe (?:prove|show|establish|determine|construct|give|obtain|"
                 r"compute|find|disprove|classify|characteri[sz]e|answer|resolve|settle)\b|\bmain (?:result|theorem)\b",
                 doc.prose[it[0]:it[1]], re.I):
        return None
    return (it[0], "the introduction never says in a sentence what this paper proves")


def rd_intro_nothing_new(doc):
    if not _paper(doc):
        return None
    it = _intro(doc)
    if not it or _words(doc.prose[it[0]:it[1]]) < 150:
        return None
    if re.search(r"\b(?:new|first|improv\w*|extend\w*|generali[sz]\w*|answer\w*|resolv\w*|settl\w*|strengthen\w*|sharpen\w*|"
                 r"refin\w*|complet\w*|unif\w*|simplif\w*)\b", doc.prose[it[0]:it[1]], re.I):
        return None
    return (it[0], "the introduction does not say what is new against the earlier work")


def rd_intro_thm_no_pointer(doc):
    if not _paper(doc):
        return None
    for e in _intro_thms(doc):
        lab = re.search(r"\\label\{([^}]+)\}", doc.raw[e[3]:e[4]])
        after = doc.prose[e[2]:e[2] + 600]
        if "\x03" in after or re.search(r"\bprov(?:ed|en|e)\b|\bproof\b", after, re.I):
            continue
        if lab and re.search(r"\\begin\{proof\}\[[^\]]*\\(?:ref|cref)\{" + re.escape(lab.group(1)) + r"\}", doc.raw):
            continue
        return (e[2], "the theorem at %s is stated with no word on where it is proved" % doc.line(e[1]))
    return None


def rd_no_open_questions(doc):
    if not _paper(doc):
        return None
    t = _tops(doc)
    cs = [s for s in t[1:] if _CONC.search(s["title"])]
    if len(t) < 4 or not cs:
        return None
    s = cs[-1]
    if re.search(r"\bopen\b|\bquestions?\b|\bconjectur\w*|\bremains?\b|\bunknown\b|\bfuture\b|\bproblems?\b|\bnot known\b",
                 doc.prose[s["tend"]:_sec_end(doc, s)], re.I):
        return None
    return (s["off"], "the closing section names no open question")


# ======================================================================== C12 symbols used far from where they were defined
def rd_symbol_far_no_reminder(doc):
    if not _paper(doc):
        return None
    tops = _tops(doc, app=True)
    if len(tops) < 4:
        return None
    bad = []
    macros = set(re.findall(r"\\(?:re)?newcommand\*?\{?(\\[A-Za-z]+)\}?|\\def(\\[A-Za-z]+)|\\DeclareMathOperator\*?\{(\\[A-Za-z]+)\}",
                            doc.raw[:doc.d0]))
    macros = set(x for t in macros for x in t if x)
    for name, offs in _occ(doc).items():
        # a bare Latin letter (c, C, N, T) is reused with a local meaning all the time, and a preamble macro is notation, not a
        # quantity: what a reader loses track of is a named constant or parameter (\sigma, \kappa_0, \mathcal{A})
        if (len(name) == 1 and name.isascii()) or name in macros:
            continue
        f = offs[0]
        fi = _top_index(doc, f)
        for o in offs[1:]:
            if not (doc.d0 <= o < doc.b0):
                continue
            if _top_index(doc, o) >= fi + 3:
                w = doc.prose[max(0, o - 250):o + 250]
                if not re.search(r"\brecall\w*\b|\bdefined in\b|\bas in\b|\bas before\b|\x03|\bthe (?:same|notation)\b", w, re.I):
                    bad.append((o, "%s (defined %s, used %s)" % (name, doc.line(f), doc.line(o))))
                break
    if len(bad) >= 3:
        bad.sort()
        return (bad[0][0], _lst([b[1] for b in bad], 3) + "; remind the reader what they mean")
    return None


def rd_where_many_symbols(doc):
    if not _paper(doc):
        return None
    for a, b in _disp(doc):
        m = re.match(r"[\s,.]*where\b([^.]{0,500})", doc.prose[b:b + 520], re.I)
        if m and m.group(1).count("\x01") >= 4:
            return (b, "a 'where' clause after the display at %s defines %d symbols at once; introduce them before the display"
                    % (doc.line(a), m.group(1).count("\x01")))
    return None


# ======================================================================== C13 notation set up before it is used
def rd_no_prelims(doc):
    if not _paper(doc):
        return None
    t = _tops(doc)
    if len(t) < 4 or len(_real(doc)) < 15:
        return None
    if any(re.search(r"prelim|notation|set-?up|setting|background|definitions|framework|basic|conventions|model",
                     s["title"], re.I) for s in t[:3]):
        return None
    return (t[1]["off"] if len(t) > 1 else t[0]["off"],
            "%d symbols and no section near the front that sets them up" % len(_real(doc)))


def rd_naturals_unstated(doc):
    if not _paper(doc):
        return None
    m = re.search(r"\\mathbb\s*\{?\s*N\s*\}?(?!_)", doc.math)
    if not m:
        return None
    if re.search(r"(?:positive|non-?negative|nonnegative) integers|\\mathbb\s*\{?N\}?\s*(?:=|:=)\s*\\\{\s*[01]|\\mathbb\s*\{?N\}?_0|"
                 r"includ\w* (?:0|zero|\$0\$)|contain\w* (?:0|zero|\$0\$)|start\w* (?:at|from|with) (?:0|1|zero|one|\$[01]\$)",
                 doc.raw, re.I):  # a bare {1,2,...} elsewhere (an example set) no longer counts as saying where N starts
        return None
    return (m.start(), "the natural numbers are used and the text never says whether they start at 0 or at 1")


def rd_log_ln_both(doc):
    if not _paper(doc):
        return None
    a, b = re.search(r"\\log(?![a-zA-Z])", doc.math), re.search(r"\\ln(?![a-zA-Z])", doc.math)
    if a and b:
        return (max(a.start(), b.start()), "both \\log and \\ln; use one, and say the base")
    return None


def rd_asymp_unstated(doc):
    if not _paper(doc):
        return None
    m = re.search(r"\\(?:lesssim|gtrsim|asymp|ll|gg)(?![a-zA-Z])", doc.math)
    if not m:
        return None
    nota = doc.notation_section()
    # explained anywhere counts: next to any use of any of the signs, in the table of symbols, or in a notation section
    for u in re.finditer(r"\\(?:lesssim|gtrsim|asymp|ll|gg)(?![a-zA-Z])", doc.raw):
        if nota and nota[0] <= u.start() < nota[1]:
            return None
        w = doc.raw[max(0, u.start() - 300):u.start() + 300]
        if re.search(r"\bmeans?\b|\bwe write\b|\bdenotes?\b|\bstands? for\b|\bto mean\b|\bshorthand\b|\bindicates?\b|\bif and only if\b|"
                     r"\babsolute constants?\b|\bimplicit constants?\b", w, re.I):
            return None
    return (m.start(), "%s is used and never explained (up to which constant?)" % m.group(0))


def rd_subset_both(doc):
    if not _paper(doc):
        return None
    a, b = re.search(r"\\subset(?![a-zA-Z])", doc.math), re.search(r"\\subseteq(?![a-zA-Z])", doc.math)
    if a and b:
        return (max(a.start(), b.start()), "both \\subset and \\subseteq; a reader cannot tell whether \\subset is strict")
    return None


def rd_variant_letters(doc):
    if not _paper(doc):
        return None
    for x in ("epsilon", "phi", "theta", "rho", "sigma", "pi"):
        a, b = re.search(r"\\%s(?![a-zA-Z])" % x, doc.math), re.search(r"\\var%s(?![a-zA-Z])" % x, doc.math)
        if a and b:
            return (max(a.start(), b.start()), "both \\%s and \\var%s" % (x, x))
    return None


# ======================================================================== C14 long proofs a person can follow
_IDEA = re.compile(r"\b(?:idea|strategy|outline|plan|overview|sketch|roadmap|we (?:first|begin|start)|the proof (?:proceeds|has|is divided|consists|goes)|"
                   r"in (?:two|three|four|five) steps|first we)\b", re.I)


def rd_long_proof_no_idea(doc):
    if not _paper(doc):
        return None
    for e in _PROOFS(doc):
        if e[4] - e[3] < 3000:
            continue
        if _IDEA.search(doc.prose[max(0, e[1] - 800):e[1]]) or _IDEA.search(doc.prose[e[3]:e[3] + 600]):
            continue
        return (e[1], "a proof of %d lines at %s with no sentence first on how it goes" % (doc.lineno(e[4]) - doc.lineno(e[3]), doc.line(e[1])))
    return None


def rd_proof_huge_no_lemma(doc):
    if not _paper(doc):
        return None
    for e in _PROOFS(doc):
        if e[4] - e[3] < 8000:
            continue
        if re.search(r"\b(?:Lemma|Claim|Proposition)s? \x03|\\begin\{(?:claim|lemma)", doc.prose[e[3]:e[4]] + doc.raw[e[3]:e[4]]):
            continue
        return (e[1], "a proof of %d characters at %s that rests on no lemma; move self-contained parts into lemmas" % (e[4] - e[3], doc.line(e[1])))
    return None


def rd_proof_nested(doc):
    if not _paper(doc):
        return None
    ps = _PROOFS(doc)
    for p in ps:
        for q in ps:
            if p is not q and p[3] <= q[1] and q[2] <= p[4]:
                return (q[1], "a proof inside a proof at %s; state the inner fact as a lemma" % doc.line(q[1]))
    return None


def rd_proof_far_from_statement(doc):
    if not _paper(doc):
        return None
    st = sorted(_kind_envs(doc, _STMTS), key=lambda e: e[2])
    for p in _PROOFS(doc):
        if re.match(r"\s*\[", doc.raw[p[3]:p[3] + 40]):
            continue
        before = [e for e in st if e[2] <= p[1]]
        if before and p[1] - before[-1][2] > 1500:
            return (p[1], "the proof at %s starts %d lines after the last statement and does not say what it proves"
                    % (doc.line(p[1]), doc.lineno(p[1]) - doc.lineno(before[-1][2])))
    return None


def rd_cases_unannounced(doc):
    if not _paper(doc):
        return None
    for e in _PROOFS(doc):
        t = doc.prose[e[3]:e[4]]
        n = len(set(re.findall(r"\bCase (\d+|[IVX]+)\b", t)))
        if n >= 4 and not re.search(r"\b(?:two|three|four|five|six|seven|\d+) cases\b|\bdistinguish\b|\bsplit\w* into\b|\baccording to whether\b",
                                    t, re.I):
            return (e[3], "%d cases at %s and no sentence first that lists them" % (n, doc.line(e[1])))
    return None


# ======================================================================== C15 the abstract
def _abs(doc):
    if not doc.abstract:
        return None
    return doc.prose[doc.abstract[0]:doc.abstract[1]]


def rd_abstract_opens_let(doc):
    a = _abs(doc)
    if a is None or not _paper(doc, 300):
        return None
    if re.match(r"\s*(?:Let|Suppose|Assume|Fix|Given|Consider)\b", a):
        return (doc.abstract[0], "the abstract opens with a hypothesis; open with what was found, in words")
    return None


def rd_abstract_short(doc):
    a = _abs(doc)
    if a is None or not _paper(doc, 300):
        return None
    n = _words(a)
    return (doc.abstract[0], "%d words; say what was proved and why it matters" % n) if 0 < n < 40 else None


def rd_abstract_first_long(doc):
    a = _abs(doc)
    if a is None or not _paper(doc, 300):
        return None
    m = re.match(r"\s*([^.!?]*[.!?])", a)
    if m and _words(m.group(1)) + m.group(1).count("\x01") > 45:
        return (doc.abstract[0], "the first sentence has %d words" % (_words(m.group(1)) + m.group(1).count("\x01")))
    return None


def rd_abstract_no_result(doc):
    a = _abs(doc)
    if a is None or not _paper(doc, 300) or _words(a) < 20:
        return None
    if re.search(r"\bwe (?:prove|show|establish|determine|give|construct|compute|find|obtain|classify|characteri[sz]e|answer|resolve|"
                 r"disprove|settle|derive|improve|extend|exhibit)\b|\b(?:is|are) (?:proved|shown|determined|established|computed|found)\b|"
                 r"\b(?:proves|shows|establishes|determines|gives|answers)\b", a, re.I):
        return None
    return (doc.abstract[0], "the abstract never says what was found")


# ======================================================================== C16 headings
def rd_intro_not_first(doc):
    if not _paper(doc):
        return None
    t = _tops(doc)
    if len(t) < 4 or re.search(r"intro|overview|background|motivation", t[0]["title"], re.I):
        return None
    return (t[0]["off"], "the first section is '%s'; a reader expects an introduction" % D._clean(t[0]["title"])[:40])


def rd_heading_caps(doc):
    if not _paper(doc):
        return None
    for s in doc.secs:
        t = re.sub(r"\$[^$]*\$|\\[A-Za-z]+", "", s["title"])
        letters = re.sub(r"[^A-Za-z]", "", t)
        if len(letters) >= 6 and letters.isupper() and len(t.split()) >= 2:
            return (s["off"], "'%s' is set in capitals" % D._clean(s["title"])[:40])
    return None


# ======================================================================== C17 tables and figures
def rd_intro_results_no_table(doc):
    if not _paper(doc):
        return None
    ts = _intro_thms(doc)
    it = _intro(doc)
    if len(ts) < 4 or re.search(r"\\begin\{tabular", doc.raw[it[0]:it[1]]):
        return None
    return (ts[0][1], "%d results stated in the introduction; add a table that lists them with where each is proved" % len(ts))


def rd_caption_mostly_math(doc):
    for a, b in doc.caps:
        t = doc.raw[a:b]
        if len(t.strip()) < 10:
            continue
        m = sum(len(x) for x in re.findall(r"\$[^$]*\$", t))
        if m > 0.6 * len(t.strip()):
            return (a, "a caption that is mostly formula at %s; say in words what is shown" % doc.line(a))
    return None


def rd_table_wide(doc):
    for m in re.finditer(r"\\begin\{(?:tabular|tabularx|longtable)\*?\}(?:\{[^{}]*\})?\{((?:[^{}]|\{[^{}]*\})*)\}", doc.raw):
        spec = re.sub(r"\{[^{}]*\}", "", m.group(1))
        n = len(re.findall(r"[lcrpXmb]", spec))
        if n >= 9:
            return (m.start(), "a table of %d columns at %s; split it or turn it" % (n, doc.line(m.start())))
    return None


def rd_table_digits(doc):
    for e in doc.envs:
        if e[0] not in ("tabular", "tabularx", "longtable"):
            continue
        n = len(re.findall(r"\d\.\d{7,}", doc.raw[e[3]:e[4]]))
        if n >= 5:
            return (e[1], "%d entries with seven or more decimals at %s; round to what the reader needs" % (n, doc.line(e[1])))
    return None


# ======================================================================== C18 finding one's way
_LAYOUT = {"\\frac", "\\dfrac", "\\tfrac", "\\left", "\\right", "\\bigl", "\\bigr", "\\Bigl", "\\Bigr", "\\biggl",
           "\\biggr", "\\overline", "\\mathrm", "\\mathbf", "\\operatorname", "\\label", "\\quad", "\\qquad", "\\text"}


def _symbols(tex):
    return {t for t in re.findall(r"\\[a-zA-Z]+|[a-zA-Z]", re.sub(r"\\label\{[^}]*\}", "", tex)) if t not in _LAYOUT}


def _restates(math, body):
    """A formula beside a far reference restates it if it shares at least half the equation's symbols."""
    want = _symbols(body)
    if not want:
        return False
    return len(want & _symbols(math)) >= max(1, (len(want) + 1) // 2)


def rd_eqref_far(doc):
    if not _paper(doc):
        return None
    bad = []
    for m in re.finditer(r"\\eqref\{([^}]+)\}", doc.raw):
        if not (doc.d0 <= m.start() < doc.b0):
            continue
        lo = doc.labels.get(m.group(1).strip())
        if lo is None:
            continue
        if _top_index(doc, m.start()) - _top_index(doc, lo) >= 3:
            if re.search(r"\brecall\w*\b", doc.prose[max(0, m.start() - 200):m.start() + 60], re.I):
                continue
            if any(e[0] in ("tabular", "tabularx", "longtable") and e[3] <= m.start() < e[4] for e in doc.envs):
                continue  # a notation-table row restates the formula beside the reference
            body = next((doc.raw[e[3]:e[4]] for e in doc.envs
                         if e[3] <= lo < e[4] and e[0].rstrip("*") in ("equation", "align", "gather", "multline", "eqnarray")), "")
            after = re.match(r"[\s,:(~]*\$([^$]+)\$", doc.raw[m.end():m.end() + 200])
            w0 = max(0, m.start() - 260)
            if doc.raw[:w0].replace("\\$", "").count("$") % 2:
                w0 = doc.raw.find("$", w0) + 1  # start the window outside a formula
            before = re.search(r"\$([^$]+)\$[^$.;]{0,60}$", doc.raw[w0:m.start()])  # same sentence only
            if any(x and _restates(x.group(1), body) for x in (after, before)):
                continue
            bad.append(m.start())
    if len(bad) >= 3:
        return (bad[0], "%d equations cited from three or more sections back, first at %s; restate them" % (len(bad), doc.line(bad[0])))
    return None


def rd_forward_lemma_in_proof(doc):
    if not _paper(doc):
        return None
    for p in _PROOFS(doc):
        if doc.app0 is not None and p[1] > doc.app0:
            continue
        for m in re.finditer(r"\b(?:Lemma|Proposition|Claim|Theorem|Corollary)s?[~ ]*\\(?:ref|cref)\{([^}]+)\}", doc.raw[p[3]:p[4]]):
            lo = doc.labels.get(m.group(1).strip())
            if lo is not None and lo > p[2] and (doc.app0 is None or lo < doc.app0):
                return (p[3] + m.start(), "the proof at %s uses a result stated later (%s); state it first" % (doc.line(p[1]), doc.line(lo)))
    return None


def rd_no_refs_at_all(doc):
    if not _paper(doc):
        return None
    st = [e for e in _kind_envs(doc, _STMTS) if "\\label{" in doc.raw[e[3]:e[4]]]
    if len(st) >= 4 and not re.search(r"\\(?:ref|eqref|cref|Cref|autoref)\{", doc.raw[doc.d0:doc.b0]):
        return (st[0][1], "%d labelled statements and not one cross-reference" % len(st))
    return None


def rd_proof_location_unsaid(doc):
    if not _paper(doc):
        return None
    for e in _intro_thms(doc):
        if re.match(r"\s*(?:\\begin\{[^}]+\}\s*)?\[[^\]]*\\cite", doc.raw[e[3]:e[4]]):
            continue  # '\begin{theorem}[{\cite{x}}]' quotes a known result: its proof is in the cited work (paper6, 28 Nov)
        # 'Theorem A [Theorem~\ref{thm:main}]': the pointer in the optional argument names the theorem whose proof
        # counts, ahead of any \label inside the body (an equation label there is not the theorem's, 28 Nov)
        lab = re.match(r"\s*(?:\\begin\{[^}]+\}\s*)?\[[^\]]*\\(?:ref|cref|Cref)\{([^}]+)\}", doc.raw[e[3]:e[4]])
        if not lab:
            lab = re.search(r"\\label\{([^}]+)\}", doc.raw[e[3]:e[4]])
        if not lab:
            continue
        L = re.escape(lab.group(1))
        if re.search(r"\\begin\{proof\}\[[^\]]*\\(?:ref|cref|Cref)\{" + L + r"\}", doc.raw):
            continue
        # the numbered statement it points to is followed at once by its proof (28 Nov)
        if re.search(r"\\label\{" + L + r"\}(?:(?!\\begin\{(?:theorem|proposition|corollary|lemma)\*?\})[\s\S]){0,2000}?"
                     r"\\end\{(?:theorem|proposition|corollary|lemma)\*?\}\s*\\begin\{proof\}", doc.raw):  # its OWN end (28 Nov)
            continue
        if re.search(r"\\(?:sub)*section\*?\{[^{}]*\\(?:ref|cref|Cref)\{" + L + r"\}", doc.raw):
            continue
        # a body statement that says it gives the theorem ('Every g satisfies the conclusion of Theorem~\ref{..}') and is
        # followed at once by its proof: the reader finds the proof there (paper13 thm:packet-intro, 28 Nov)
        # one environment at a time (the body may not open another statement), and the reference must say the statement
        # gives the theorem ('conclusion stated in', 'proves'), not just borrow its setting ('In the setting of')
        if any(re.search(r"\b(?:conclusion|stated in|proves|establishes|implies|gives|yields|this is|which is)\b[^.]{0,60}?\\(?:ref|cref|Cref)\{"
                         + L + r"\}", m.group(2)) for m in re.finditer(
                r"\\begin\{(theorem|proposition|corollary)\*?\}((?:(?!\\begin\{(?:theorem|proposition|corollary|lemma)\*?\})"
                r"[\s\S])*?)\\end\{\1\*?\}\s*\\begin\{proof\}", doc.raw)):
            continue
        if re.search(r"\bproof of (?:Theorem|Proposition|Corollary)[~ ]*\\(?:ref|cref)\{" + L + r"\}", doc.raw, re.I):
            continue
        # prose that tells the reader where the proof is: 'Section~\ref{s} proves Theorem~\ref{t}', 'This appendix
        # proves ... \Cref{t}', 'Theorem~\ref{t} follows from Propositions ...' (paper15, paper23, open_problem_0706, 28 Nov).
        # Not accepted: 'This proves Theorem~\ref{t}' or a bare 'Theorem~\ref{t} follows.' at the END of an unheaded
        # proof (the reader learns it too late), nor '..., which is Theorem~\ref{t}' inside a computation.
        if re.search(r"(?:(?:Sections?|Appendix|Appendices)[~ ]*\\(?:ref|cref|Cref)\{[^}]+\}|\b[Tt]his (?:section|appendix))\s+"
                     r"(?:proves?|establish(?:es)?)\b[^.]{0,40}?\\(?:ref|cref|Cref)\{" + L + r"\}", doc.raw) or \
                re.search(r"\\(?:ref|cref|Cref)\{" + L + r"\}\s*(?:then\s+)?(?:follows (?:from|by)|is proved in)\b", doc.raw):
            continue
        return (e[1], "no proof or heading names the theorem at %s, so a reader cannot find its proof" % doc.line(e[1]))
    return None


# ======================================================================== C20 statements that stand alone
def rd_stmt_symbol_from_proof(doc):
    if not _paper(doc):
        return None
    pf = [(e[3], e[4]) for e in _PROOFS(doc)]
    stv = [(e[3], e[4]) for e in _kind_envs(doc, _STMTS)]
    macros = set(re.findall(r"\\(?:re)?newcommand\*?\{?(\\[A-Za-z]+)|\\def(\\[A-Za-z]+)|\\DeclareMathOperator\*?\{(\\[A-Za-z]+)",
                            doc.raw[:doc.d0]))
    macros = set(x for t in macros for x in t if x)
    for name, offs in sorted(_occ(doc).items(), key=lambda kv: kv[1][0]):
        if (len(name) == 1 and name.isascii()) or name in macros:
            continue  # a plain letter reused in a statement is usually a new local object, not the proof's one
        if _in(pf, offs[0]):
            for o in offs[1:]:
                if _in(stv, o):
                    return (o, "%s is first introduced inside a proof (%s) and then used in a statement (%s)"
                            % (name, doc.line(offs[0]), doc.line(o)))
    return None


def rd_stmt_opens_formula(doc):
    if not _paper(doc):
        return None
    for e in _kind_envs(doc, _STMTS | {"definition"}):
        t = _inner_prose(doc, e).lstrip()
        if t.startswith("\x01"):
            return (e[3], "the statement at %s opens with a formula" % doc.line(e[1]))
    return None


def rd_stmt_eqref_into_proof(doc):
    if not _paper(doc):
        return None
    pf = [(e[1], e[2]) for e in _PROOFS(doc)]
    for e in _kind_envs(doc, _STMTS):
        for m in re.finditer(r"\\eqref\{([^}]+)\}", doc.raw[e[3]:e[4]]):
            lo = doc.labels.get(m.group(1).strip())
            if lo is not None and _in(pf, lo):
                return (e[3] + m.start(), "the statement at %s points to an equation inside a proof" % doc.line(e[1]))
    return None


def rd_stmt_many_items(doc):
    if not _paper(doc):
        return None
    for e in _kind_envs(doc, _THMS):
        n = len(re.findall(r"\\item\b", doc.raw[e[3]:e[4]]))
        if n >= 5:
            return (e[1], "a theorem with %d parts at %s; split it into a theorem and corollaries" % (n, doc.line(e[1])))
    return None


# ======================================================================== the table
# (id, kind, spec, text, weight).  kind "rx": spec = (scope[+min count], regex) on pw1k's scopes; kind "fn": spec = detector name.
P = "fn"
READ = [
    # C01 the table of symbols, always at the end
    ("C01", P, "rd_nota_not_last", "The table of symbols is not the last section before the references; keep it at the very end, where a reader looks for it", 5),
    ("C01a", P, "rd_nota_in_body", "The list of symbols sits in the body; move it to an appendix at the end, just before the references", 4),
    ("C01b", P, "rd_nota_not_pointed", "Nothing in the paper sends the reader to the table of symbols; say in the introduction where it is (Appendix~\\ref{...})", 3),
    ("C01c", P, "rd_nota_no_label", "The table of symbols has no \\label, so the introduction cannot point to it", 3),
    ("C01d", P, "rd_nota_twice", "Two sections list notation; keep one table of symbols, at the end", 3),
    ("C01e", P, "rd_nota_no_header", "The table of symbols has no header row; give it columns Symbol, Meaning, Where defined", 3),
    # C02 everything defined
    ("C02", P, "rd_def_no_emph", "A Definition does not mark the word it defines; set the new word in \\emph so the eye finds it", 4),
    ("C02a", "rx", ("R", r"\b(?:is|are) (?:then )?called (?:an? |the )?(?!\\emph|\\textit|\\textbf|\{\\em|\$|\\\()[a-z]"),
     "A term is introduced with 'is called' but not marked; put the new word in \\emph (or a Definition)", 3),
    ("C02b", "rx", ("p", r"\b(?:the )?(?:usual|standard|obvious|customary|common|familiar) notation\b"),
     "'The usual notation' leaves the reader to guess; write the notation out once and list it in the table of symbols", 3),
    ("C02c", "rx", ("p", r"\bwell[- ]known (?:definitions?|notions?|concepts?|facts?|results?|properties)\b(?![^.]{0,150}[\x02\x05\x03])"),
     "A 'well-known' fact with no citation and no statement; state it and cite where it is proved", 3),
    ("C02d", "rx", ("p", r"\b(?:the reader is (?:assumed|expected|supposed) to (?:be familiar|know)|we assume (?:that )?the reader|familiarity with)\b(?![^.]{0,160}[\x02\x05])"),
     "The paper assumes the reader knows something and names no source; cite a textbook or a survey where it can be learned", 3),
    ("C02e", "rx", ("p", r"\bin the sense of (?-i:[A-Z][a-z]+)\b(?![^.]{0,80}[\x02\x05])"),
     "'In the sense of X' with no citation; cite X and say in a clause what that sense is", 3),
    # C03 definitions easy to look up
    ("C03", "rx", ("f", r"\b(?:we (?:now )?(?:call|define)|let us (?:call|define)|will be called|is said to be)\b"),
     "A notion is defined inside a proof, where nobody will look for it; move it to a numbered Definition before the statement", 4),
    ("C03a", P, "rd_defs_unlabelled", "Definitions without a \\label; label every definition so later uses can say 'Definition~\\ref{...}'", 3),
    ("C03b", "rx", ("R", r"\\footnote\{[^{}]{0,300}?\b(?:we call|is called|denotes|we write|we define|stands for)\b"),
     "A definition is hidden in a footnote; give it a sentence or a Definition in the text", 3),
    ("C03c", P, "rd_remark_defines", "A remark defines a term; definitions belong in numbered Definitions, where they can be found again", 3),
    ("C03d", "rx", ("p", r"\b(?:the (?:above|previous|preceding|earlier) definition|(?:as )?defined (?:above|earlier|previously|before))\b(?![^.]{0,60}\x03)"),
     "A definition is recalled by position ('defined above'); point to it: 'Definition~\\ref{...}'", 3),
    ("C03e", "rx", ("p", r"\brecall (?:that|the definition|from)\b(?![^.]{0,160}[\x02\x03\x05])"),
     "'Recall that' with no pointer; say where it was defined or cite it, so the reader can look it up", 3),
    # C04 main derivations explained
    ("C04", P, "rd_display_chain", "Three or more displays in a row with no words between them; say what each line does and why it follows", 4),
    ("C04a", P, "rd_align_silent", "A long aligned derivation with no justification anywhere; mark each step (\\text{by ...}) or explain them after it", 3),
    ("C04b", "rx", ("p", r"\bafter (?:some|a little|a bit of|tedious|lengthy|elementary|routine|simple) (?:algebra|manipulations?|computations?|calculations?|rearrangements?)\b"),
     "'After some algebra' hides the derivation; give the intermediate line, or put the computation in an appendix", 3),
    ("C04c", "rx", ("p", r"\bone (?:easily|readily|immediately|quickly) (?:checks|verifies|sees|obtains|computes|deduces)\b|\b(?:easily|readily) (?:checked|verified|seen)\b"),
     "'One easily checks' asks the reader to do the work; show the check in a line or two", 3),
    ("C04d", P, "rd_proof_all_math", "A proof made only of displays; a reader needs a sentence for each step saying what is done", 3),
    ("C04e", "rx", ("p", r"\b(?:combining|putting together) (?:these|the (?:above|previous|last|two|three)(?: two| three)?) (?:equations|estimates|inequalities|bounds|identities|facts)\b(?![^.]{0,60}\x03)"),
     "'Combining these estimates' without naming them; cite each one by its number", 3),
    # C05 explain the steps
    ("C05", P, "rd_ineq_chain_silent", "A chain of inequalities with no reason for any step; say which fact gives each inequality", 4),
    ("C05a", "rx", ("p", r"\b(?:by|from|using|applying) (?:Lemma|Theorem|Proposition|Corollary|Definition|Claim)\b(?-i:(?! *[\x03A-Z0-9]))"),
     "A result is used by kind with no number ('by Lemma'); give its number", 3),
    ("C05b", P, "rd_proof_opens_similar", "A proof that only says 'similarly'; write out what changes from the other proof", 3),
    ("C05c", "rx", ("f3", r"\b(?:clearly|obviously|trivially|evidently)\b"),
     "'Clearly' or 'obviously' three or more times in the proofs; each one is a step a reader may not see, say why it holds", 3),
    ("C05d", "rx", ("p", r"\bthe rest (?:of the (?:proof|argument) )?(?:is|follows|goes through) (?:similar|similarly|analogous|analogously|standard|routine|easy|the same)\b"),
     "'The rest is similar' leaves the end of the argument out; finish it", 3),
    ("C05e", "rx", ("p", r"\bit (?:suffices|is enough) to (?:show|prove|check|verify)\b(?![^.]{0,200}\b(?:since|because|as|by|indeed|for)\b)"),
     "'It suffices to show' with no reason why it suffices; add the clause that says why", 3),
    # C06 the history, told with citations
    ("C06", P, "rd_intro_few_cites", "The introduction cites fewer than three works; tell the history of the problem, who asked it and what was known, with citations", 5),
    # not a theorem's own title '[Section lemma ...]', not a class adjective ('the Toeplitz problem'), not a textbook
    # result a reader needs no citation for ('Borel--Cantelli lemma', 'Markov's inequality'): 28 Nov corpus read
    # the stop depends on the noun: 'the Toeplitz problem' is a class, 'the Bernoulli conjecture' still needs its source
    ("C06a", "rx", ("i", r"(?<!\[)\b(?!(?:Toeplitz|Hankel|Gaussian|Hermitian|Wigner|Wishart|Rademacher|Bernoulli|Euclidean|Boolean|Lipschitz)"
                         r"\s+(?:problem|question)\b)(?!(?:Cantelli|Schwarz|Markov|Chebyshev|Jensen|Hölder|Holder|Minkowski|Fubini|Tonelli"
                         r"|Fatou|Zorn|Baire|Bayes|Stirling|Taylor)(?:'s|’s)?\s+(?:inequality|lemma|theorem|formula)\b)"
                         r"(?-i:(?!(?:Our|The|This|Main|Each|Every|That|These|Its|In|An?|Key|First|Second|Third|Last|Final|Next|Previous|Section)\b)[A-Z][a-z]+)(?:'s|’s)? (?:conjecture|problem|question|inequality|theorem|lemma)\b(?!\s*~?\s*\x03)(?![^.]{0,400}[\x02\x05])"),  # 'Thus Problem~\ref{..}' is the paper's own (28 Nov)
     "A named problem or theorem in the introduction with no citation; cite where it was posed or proved", 3),
    ("C06b", "rx", ("p", r"\b(?:was|were|has been|have been) (?:first )?(?:posed|asked|raised|introduced|proposed|conjectured|proved|studied|considered|solved) by\b(?![^.]{0,400}[\x02\x05])"),
     "'Was posed by' with no citation; cite the paper where it was posed", 3),
    ("C06c", "rx", ("p", r"\bit is (?:well[- ]known|known|a classical fact|a classical result|folklore) that\b(?![^.]{0,200}[\x02\x05\x03])"),
     "'It is known that' with no citation; cite where it is proved", 3),
    ("C06d", "rx", ("p", r"\bin (?:1[789]\d\d|20[0-2]\d)\b(?![^.]{0,400}[\x02\x05])"),
     "A year is given for an earlier result with no citation; cite the paper", 3),
    ("C06e", "rx", ("p", r"\bthe (?:best|previous(?:ly)?|strongest|current) (?:known )?(?:bound|result|estimate|constant|record)s?\b(?![^.]{0,150}[\x02\x05\x03])"),
     "'The best known bound' with no citation; say whose bound it is", 3),
    # C07 all citations included
    ("C07", P, "rd_cite_missing", "A \\cite key has no entry in the bibliography; the reference prints as '?'", 5),
    ("C07a", P, "rd_bib_uncited", "A bibliography entry is never cited; cite it where it is used or remove it", 3),
    ("C07b", P, "rd_bib_duplicate", "The same work appears twice in the bibliography", 3),
    ("C07c", P, "rd_bib_arxiv_noid", "An arXiv entry with no arXiv number; give the identifier so the reader can find it", 3),
    ("C07d", P, "rd_bib_toappear_noid", "A 'to appear' or 'preprint' entry with no arXiv number, DOI or link; the reader cannot find it", 3),
    ("C07e", "rx", ("B", r"\\bibitem[^\n]*(?:\n(?!\\bibitem)[^\n]*){0,3}?\bet al\.?"),
     "'et al.' in the bibliography; list every author there", 3),
    # C08 accessible to a person
    ("C08", P, "rd_thm_no_plain_words", "The main theorem is not followed by a sentence in plain words saying what it means", 5),
    ("C08a", P, "rd_no_informal_anywhere", "No informal explanation anywhere (the idea, intuitively, in words); give the reader the picture before the details", 4),
    ("C08b", "rx", ("p", r"\([^()\n]{0,200}\([^()\n]{0,200}\)[^()\n]{0,200}\)"),
     "Parentheses inside parentheses in running text; make the inner aside a sentence", 3),
    ("C08c", P, "rd_sentence_long", "A sentence of more than seventy words; a reader loses the thread, split it", 3),
    ("C08d", "rx", ("p4", r"\brespectively\b"),
     "'Respectively' four or more times; each one makes the reader pair lists by position, write the cases out", 3),
    ("C08e", "rx", ("p", r"\bnot (?:un|in|im|non-?)(?:likely|common|usual|important|reasonable|possible|consistent|related|trivial|significant|interesting)\b"),
     "A double negative ('not uncommon'); say it directly", 3),
    # C09 examples
    ("C09", P, "rd_defs_no_example", "Definitions with no example after them; give the simplest object that satisfies each one", 4),
    ("C09a", P, "rd_no_examples_at_all", "The paper has no example at all; one worked example makes the definitions and the theorem concrete", 4),
    ("C09b", P, "rd_thm_no_special_case", "The first theorem is not followed by a special case or an example; show what it says in the simplest case", 3),
    ("C09c", P, "rd_no_figure", "The paper is about objects that can be drawn and has no figure; one picture saves a page of description", 3),
    ("C09d", P, "rd_hypotheses_untested", "Nothing says whether the hypotheses of the theorems are needed; give an example that fails without them, or say it is open", 3),
    ("C09e", P, "rd_def_conditions_no_example", "A definition with three or more conditions and no example; show an object that meets them and one that does not", 3),
    # C10 every section opens with words
    ("C10", P, "rd_section_opens_cold", "A section opens with a statement or a formula; open with a sentence saying what the section does and why", 4),
    ("C10a", P, "rd_subsection_opens_cold", "A subsection opens with a statement or a formula; give it a sentence of purpose first", 3),
    ("C10b", P, "rd_heading_then_heading", "A heading followed at once by a lower heading; say what the section contains before dividing it", 3),
    ("C10c", P, "rd_long_proof_no_close", "A long proof stops without saying what has been shown; end with the sentence that closes the argument", 3),
    ("C10d", P, "rd_no_conclusion", "No closing section; end with what was found, what it means and what is still open", 3),
    ("C10e", P, "rd_subsection_thin", "A subsection of fewer than forty words; merge it or say more", 3),
    # C11 what the result means
    ("C11", P, "rd_intro_no_contribution", "The introduction never says in a sentence what this paper proves; say it early: 'We prove that ...'", 5),
    ("C11a", P, "rd_intro_nothing_new", "The introduction does not say what is new; say how the result compares with what was known", 4),
    ("C11b", P, "rd_intro_thm_no_pointer", "A theorem in the introduction with no word on where it is proved; add 'proved in Section~\\ref{...}'", 3),
    ("C11c", "rx", ("p", r"\b(?:by|from|using|of|in|see) (?:our |the )?main (?:theorem|result)\b(?! *\x03)"),
     "'The main theorem' by name with no number; point to it", 3),
    ("C11d", P, "rd_no_open_questions", "The closing section names no open question; a reader wants to know where the subject goes next", 3),
    ("C11e", "rx", ("p", r"\b(?:is|are|seems|seem) (?:very |quite |particularly |especially )?interesting\b(?![^.]{0,120}\b(?:because|since|as it|as they|for)\b)"),
     "'Interesting' with no reason; say why", 3),
    # C12 symbols that come back later
    ("C12", P, "rd_symbol_far_no_reminder", "Symbols come back many sections after their definition with no reminder; add a few words ('the constant c_0 of (2.3)')", 4),
    ("C12a", "rx", ("p", r"\b(?:by )?(?:a slight |an |slight )?abuse of notation\b|\babusing notation\b"),
     "An abuse of notation; give the second object its own symbol and add it to the table", 3),
    ("C12b", "rx", ("p", r"\b(?:we )?(?:re-?use|redefine|overload) (?:the )?(?:symbol|letter|notation)s?\b"),
     "A letter is reused for a new object; use a new letter, one symbol for one thing", 3),
    ("C12c", "rx", ("p", r"\b(?:to be|will be|is) (?:chosen|fixed|determined|specified) later\b(?![^.]{0,60}\x03)"),
     "A quantity 'to be chosen later' with no pointer; say where it is chosen and list it in the table of symbols", 3),
    ("C12d", "rx", ("p", r"\b(?:may|might|can) (?:change|vary|differ) (?:from line to line|from one (?:line|occurrence) to (?:the )?(?:next|another)|at each (?:occurrence|appearance)|between occurrences)\b"),
     "Constants that change from line to line; where a constant matters, name it (C_1, C_2) so a reader can follow it", 3),
    ("C12e", P, "rd_where_many_symbols", "A 'where' clause defines four or more symbols at once after a display; introduce them before the display, one at a time", 3),
    # C13 notation set up before use
    ("C13", P, "rd_no_prelims", "Many symbols and no section near the front that sets them up; add a short Notation or Preliminaries section", 4),
    ("C13a", P, "rd_naturals_unstated", "The natural numbers are used without saying whether they start at 0 or 1", 3),
    ("C13b", P, "rd_log_ln_both", "Both \\log and \\ln appear; use one and say which base", 3),
    ("C13c", P, "rd_asymp_unstated", "An asymptotic sign (\\lesssim, \\ll, \\asymp) is used and never explained; say what it means and what the constant depends on", 3),
    ("C13d", P, "rd_subset_both", "Both \\subset and \\subseteq appear; say whether \\subset is strict, or use one", 3),
    ("C13e", P, "rd_variant_letters", "Two forms of one Greek letter (\\epsilon and \\varepsilon); a reader takes them for two objects", 3),
    # C14 long proofs a person can follow
    ("C14", P, "rd_long_proof_no_idea", "A long proof with no sentence first on how it goes; give the idea in two or three sentences before the details", 4),
    ("C14a", P, "rd_proof_huge_no_lemma", "A very long proof that rests on no lemma; move self-contained parts into lemmas a reader can check one at a time", 3),
    ("C14b", P, "rd_proof_nested", "A proof inside a proof; state the inner fact as a lemma or a claim", 3),
    ("C14c", P, "rd_proof_far_from_statement", "A proof far from its statement with no header; write \\begin{proof}[Proof of Lemma~\\ref{...}]", 3),
    ("C14d", "rx", ("p", r"\b(?:this|which) (?:completes|finishes|concludes|ends) the proof of (?:the )?(?:claim|lemma|theorem|proposition|corollary)\b(?! *\x03)"),
     "'This completes the proof of the lemma' without saying which; give its number", 3),
    ("C14e", P, "rd_cases_unannounced", "Four or more cases with no sentence first that lists them; say how the cases split before the first one", 3),
    # C15 the abstract
    ("C15", P, "rd_abstract_opens_let", "The abstract opens with a hypothesis ('Let ...'); open with what was found, in words", 4),
    ("C15a", P, "rd_abstract_short", "The abstract is under forty words; say what was proved and why it matters", 3),
    ("C15b", P, "rd_abstract_first_long", "The abstract's first sentence has more than forty-five words", 3),
    ("C15c", P, "rd_abstract_no_result", "The abstract never says what was found ('we prove', 'we show', 'we determine')", 4),
    ("C15d", "rx", ("A", r"\b(?:Theorem|Lemma|Proposition|Corollary|Section|Appendix)s?[~ ]\d"),
     "The abstract refers to a numbered part of the paper; the abstract is read alone", 3),
    ("C15e", "rx", ("a", r"\b(?:perhaps|possibly|seems? to|appears? to|might)\b"),
     "The abstract hedges; state what is proved, and say plainly what is only conjectured", 3),
    # C16 headings that say what is inside
    ("C16", "rx", ("h2", r"(?im)^[ \t]*(?:proofs?|lemmas|some lemmas|technical lemmas|auxiliary (?:results|lemmas)|miscellane\w*|further results|other results|more results|results|computations|calculations)[ \t]*$"),
     "Two or more headings that name nothing ('Proofs', 'Auxiliary results'); name what each section proves", 4),
    ("C16a", P, "rd_intro_not_first", "The paper does not open with an introduction; a reader needs one before the first definition", 3),
    ("C16b", P, "rd_heading_caps", "A heading in capitals; set headings in ordinary case", 3),
    ("C16c", "rx", ("R", r"\\(?:sub)*section\*?\{\s*[a-z]"),
     "A heading that starts with a lower-case letter", 3),
    ("C16d", "rx", ("R", r"\\section\*?\{\s*Appendix(?: [A-Z])?\s*\}"),
     "An appendix headed only 'Appendix'; say what it contains", 3),
    ("C16e", "rx", ("R", r"\\(?:sub)*section\{[^{}$]*\b(?!AI\b)[A-Z]{2,6}s?\b[^{}]*\}"),
     "An abbreviation in a heading; a heading is read before the abbreviation is defined", 3),
    # C17 tables and figures a reader can use
    ("C17", P, "rd_intro_results_no_table", "Four or more results in the introduction and no table of them; a table (result, hypotheses, where proved) helps the reader", 3),
    ("C17a", "rx", ("c", r"\bsee (?:the )?(?:main )?text\b|\bdescribed in the text\b|\bexplained in the text\b"),
     "A caption sends the reader to the text; a caption should say what is shown on its own", 3),
    ("C17b", P, "rd_caption_mostly_math", "A caption that is mostly formula; say in words what the figure or table shows", 3),
    ("C17c", P, "rd_table_wide", "A table of nine or more columns; split it", 3),
    ("C17d", P, "rd_table_digits", "Table entries with seven or more decimals; round to what the reader needs and say the precision", 3),
    ("C17e", "rx", ("R", r"\\caption\*?(?:\[[^\]]*\])?\{\s*[a-z]"),
     "A caption that starts with a lower-case letter", 3),
    # C18 finding one's way
    ("C18", P, "rd_eqref_far", "Equations cited from three or more sections back with no reminder; restate the formula or recall what it says", 4),
    ("C18a", P, "rd_forward_lemma_in_proof", "A proof uses a lemma stated later; state the lemma first, or say it is proved later and that the argument is not circular", 3),
    ("C18b", "rx", ("R", r"\b(?:in|by|from|see|of|to)\s*~?\s*\\ref\{(?!eq)"),  # not 'and': 'Theorems~\ref{a} and~\ref{b}' is right
     "A bare \\ref with no word before it ('by \\ref{x}'); write 'by Lemma~\\ref{x}' so the reader knows what kind of thing it is", 3),
    ("C18c", "rx", ("p", r"\b(?:elsewhere|earlier|later) in (?:this|the) (?:paper|article|text)\b(?![^.]{0,40}\x03)"),
     "'Earlier in the paper' with no pointer; give the section or the statement number", 3),
    ("C18d", P, "rd_no_refs_at_all", "Labelled statements and not one cross-reference; refer to results by number so a reader can turn to them", 3),
    ("C18e", P, "rd_proof_location_unsaid", "A theorem of the introduction whose proof no heading or proof header names; write \\begin{proof}[Proof of Theorem~\\ref{...}]", 3),
    # C19 sentences that read well
    ("C19", "rx", ("p8", r"\bnote that\b"),
     "'Note that' eight or more times; most can go, and the rest can say why the fact matters", 3),
    ("C19a", "rx", ("p5", r"\bwe have that\b"),
     "'We have that' five or more times; write 'we have' or state the fact", 3),
    ("C19b", "rx", ("p6", r"\b(?:very|quite|rather|fairly|extremely|highly)\b"),
     "Intensifiers (very, quite, rather) six or more times; give the number or the reason instead", 3),
    ("C19c", "rx", ("p4", r"(?:[.!?][ \t\n]+)(?:This|These) (?:is|are|shows|show|gives|give|implies|imply|means|yields|proves|follows)\b"),
     "Four or more sentences open with a bare 'This' or 'These'; say what: 'This bound shows'", 3),
    ("C19d", "rx", ("p4", r"\bthe fact that\b"),
     "'The fact that' four or more times; say the fact", 3),
    ("C19e", "rx", ("p", r"\band/or\b"),
     "'And/or'; say which is meant", 3),
    # C20 statements that stand alone
    ("C20", P, "rd_stmt_symbol_from_proof", "A statement uses a symbol first introduced inside an earlier proof; a statement must be readable without the proofs", 4),
    ("C20a", "rx", ("R", r"\\begin\{(?:theorem|thm|lemma|lem|proposition|prop|corollary|cor)\}\[(?![^\]]*\\cite)(?![^\]]*\b(?:Main|Key|Technical|Our|The|Basic|General|Local|Global)\b)[^\]]*\b[A-Z][a-z]+(?:'s|’s|--[A-Z][a-z]+| and [A-Z][a-z]+)? (?:theorem|lemma|inequality|formula|identity|bound|conjecture|criterion)\b[^\]]*\]"),
     "A named theorem from the literature in a header with no citation; put \\cite in the header", 3),
    ("C20b", P, "rd_stmt_opens_formula", "A statement opens with a formula; open with a word ('For every ...')", 3),
    ("C20c", P, "rd_stmt_eqref_into_proof", "A statement points to an equation that lives inside a proof; a statement must stand alone", 3),
    ("C20d", "rx", ("s", r"\bwe (?:have|get|obtain|see)\b"),
     "A statement narrates ('we have'); a statement states", 3),
    ("C20e", P, "rd_stmt_many_items", "A theorem with five or more parts; split it into a theorem and corollaries a reader can cite one by one", 3),
]
