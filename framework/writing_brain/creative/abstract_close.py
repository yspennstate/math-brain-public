"""Sentences that may sum a scene up: narration with an abstract noun and no concrete one.

Nouns are classed by the lexicographer file of their first noun sense in Open English WordNet 2025 (concrete:
animal, artifact, body, food, object, person, plant, substance; abstract: act, attribute, cognition, event,
feeling, motive, phenomenon, process, relation, state). A word that can also be a verb or adjective counts as a
noun only after a determiner. Speech in double quotes is left out; sentences under three words are skipped.

Function words that WordNet also lists as nouns (he, it, at, or ...) are never counted. A noun whose first sense is
a phenomenon but which also has a concrete sense (snow, wind, rain, smoke, heat, cloud: 53 words) counts as concrete;
tested before it went in, it lost none of 70 flagged weak sentences and took 32 of 729 flags off draft2, 31 of them
weather lines (bench/abstract_close_weather.py).

Against blind readers' weak sentences in three readings of chapter one, the flag held 22 of 76 against about 12
percent of all sentences (bench/abstract_close_vs_readers.md). On published prose the same rule, fixed before the
counts, marked readers' weakest sentences 1.39 times as often as the rest (72 of 279 against 51.8 expected over 14
excerpts, each counted once, p 0.0016), and 1.25 times on the one reading it was not tuned on. It is not a length
signal: flagged sentences run shorter than the rest, and with length held fixed the odds ratio was 2.42 on the readings
the rules were checked against and 1.65 on the two it was not (p 0.087; bench/abstract_close_length*.py). As a hint
it is weak: 26 of 238 flags (11 pct) fell on a reader's weak sentence where the base rate was 6 pct, and 13 of 126
(10 pct) against 8 pct on the held-out readings. It points at sentences to read beside the
paragraph before them; it does not judge them. Under each flagged sentence it lists the concrete nouns already on
the page nearby (its own paragraph and the one before, nearest first): the things a rewrite can lean on, or the
sign that the paragraph already said it. A flag in the last two paragraphs is marked as the close: published chapter
endings flag about 21 percent, draft2's last 15 sentences 10 percent (bench/abstract_close_endings.py), so there a
summing-up line is the published habit, not a fault to cut on sight.

    python -P -X utf8 abstract_close.py <file>        list the flagged sentences
    python -P -X utf8 abstract_close.py --build       rebuild data/noun_kinds_v2.json.gz from the OEWN XML
    python -P -X utf8 abstract_close.py --selftest
"""
import gzip
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "data", "noun_kinds_v2.json.gz")  # v2: phenomenon nouns with a concrete sense count as concrete
XML = os.environ.get("OEWN_XML", "english-wordnet-2025.xml.gz")  # Open English WordNet 2025 release
CONC = {5, 6, 8, 13, 17, 18, 20, 27}
ABST = {4, 7, 9, 11, 12, 16, 19, 22, 24, 26}
DET = {"the", "a", "an", "his", "her", "my", "our", "their", "its", "this", "that", "these", "those", "your",
       "no", "every"}
# Function words WordNet also lists as nouns (he = helium, it = information technology, at = astatine, or = operating
# room): never counted.
STOP = set("i me my he him his she her it its we us our you your they them their one ones a an the this that these those "
           "who what which there here then now so as at by in on of to up out off do did does is was be am are been had has "
           "have will would can could may might must shall should not no all any some each every both either other another "
           "such same own more most much many few less least just only also too very but and or if because while when where "
           "how why yet still ever never again once mr mrs".split())
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "turn"))
try:
    import reader_checks as _rc
    sentences = _rc.sentences
except Exception:  # the turn/ checks are not on this machine: a plain splitter
    def sentences(t):
        return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if s.strip()]

_KINDS = None


def build():
    first, other, physical = {}, set(), set()
    lemma = pos = None
    for line in gzip.open(XML, "rt", encoding="utf-8"):
        if "<Lemma " in line:
            m = re.search(r'writtenForm="([^"]+)" partOfSpeech="(\w)"', line)
            lemma, pos = (m.group(1).lower(), m.group(2)) if m else (None, None)
            if lemma and pos != "n":
                other.add(lemma)
        elif "<Sense " in line and lemma and pos == "n":
            m = re.search(r"__1\.(\d\d)\.", line)
            if m:
                first.setdefault(lemma, int(m.group(1)))
                if int(m.group(1)) in CONC:
                    physical.add(lemma)
    # "c" concrete, "a" abstract, "o" any other noun; upper case = also a verb or adjective
    kinds = {}
    for w, f in first.items():
        k = "c" if f in CONC or (f == 19 and w in physical) else "a" if f in ABST else "o"
        if " " not in w:
            kinds[w] = k.upper() if w in other else k
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    with gzip.open(CACHE, "wt", encoding="utf-8") as f:
        json.dump(kinds, f, separators=(",", ":"), sort_keys=True)
    return kinds


def kinds():
    global _KINDS
    if _KINDS is None:
        if os.path.exists(CACHE):
            with gzip.open(CACHE, "rt", encoding="utf-8") as f:
                _KINDS = json.load(f)
        else:
            _KINDS = build()
    return _KINDS


def counts(s):
    K, a, c = kinds(), 0, 0
    w = re.findall(r"[a-z']+", s.lower())
    for i, x in enumerate(w):
        if x in STOP:
            continue
        k = K.get(x)
        if k is None and x.endswith("s"):
            k = K.get(x[:-1])
        if k is None:
            continue
        if k.isupper() and not (i and w[i - 1] in DET):
            continue
        a += k.lower() == "a"
        c += k.lower() == "c"
    return a, c


def flagged(s):
    a, c = counts(s)
    return a >= 1 and c == 0


def things(s):
    """The concrete nouns of s, in order, each once (the same noun test as counts)."""
    K, out = kinds(), []
    w = re.findall(r"[a-z']+", s.lower())
    for i, x in enumerate(w):
        if x in STOP:
            continue
        k, base = K.get(x), x
        if k is None and x.endswith("s"):
            k, base = K.get(x[:-1]), x[:-1]
        if k is None or k.lower() != "c" or (k.isupper() and not (i and w[i - 1] in DET)):
            continue
        if base not in out:
            out.append(base)
    return out


def at_hand(pars, p, s, n=4):
    """Things the writer already put on the page near a flagged sentence: the concrete nouns of its own paragraph
    and the one before, nearest first, none of them in the sentence itself. A summing-up line can often be
    rewritten around one of them, or cut because one of them already said it."""
    near = told(pars[p - 1])
    cut = near.find(s)
    before = near[:cut] if cut >= 0 else near
    after = near[cut + len(s):] if cut >= 0 else ""
    pool = things(before)[::-1] + things(after) + (things(told(pars[p - 2]))[::-1] if p >= 2 else [])
    own = set(things(s))
    out = []
    for t in pool:
        if t not in own and t not in out:
            out.append(t)
    return out[:n]


def told(par):
    return " ".join(par.replace("\u201c", '"').replace("\u201d", '"').split('"')[0::2])


def paragraphs(text):
    return [par for par in text.split("\n") if par.strip() and not par.lstrip().startswith("#")]


def scan(text):
    """[(paragraph number, sentence)] for every flagged narrated sentence, and the number of sentences read."""
    out, n, p = [], 0, 0
    for par in paragraphs(text):
        p += 1
        for s in sentences(told(par)):
            if len(re.findall(r"[A-Za-z']+", s)) < 3:
                continue
            n += 1
            if flagged(s):
                out.append((p, s.strip()))
    return out, n


def report(text, limit=12):
    hits, n = scan(text)
    if not n:
        return []
    lines = ["SUMMING UP? %d of %d narrated sentences have an abstract noun and no concrete one (chapter one runs about 12%%,"
             " published fiction 13%% mid-scene to 21%% at a chapter's end, the middle half of 252 openings by authors born 1880-1945"
             " 12-20%%). About one flag in ten fell on a sentence a blind reader called weak (11 pct on the"
             " readings the rules were checked against, 10 pct on two they were not), against one sentence in"
             " fifteen overall: most flags mark sentences readers passed, so do not cut on sight. Read each beside"
             " the paragraph before it: if that paragraph already showed it, cut it or put a thing in it." % (len(hits), n)]
    if n >= 40 and len(hits) > 0.2 * n:
        lines.append("  (over a fifth flagged: the whole register is abstract here, and on such pages the flag did not"
                     " find the judges' faults more often than other sentences; skim, do not work through the list)")
    pars = paragraphs(text)
    close = len(pars) - 1  # the last two paragraphs are the close
    for p, s in hits[:limit]:
        lines.append("  par %d: %s" % (p, s[:160]))
        if p >= close and len(pars) >= 6:
            lines.append("      at the close: published chapters sum up here about one sentence in five (our draft one"
                         " in ten); keep it if it earns its place")
        near = at_hand(pars, p, s)
        if near:
            lines.append("      on the page near it: " + ", ".join(near))
    if len(hits) > limit:
        lines.append("  ... %d more: python -P -X utf8 abstract_close.py <file>" % (len(hits) - limit))
    return lines


def selftest():
    ok = True
    for s, want in (("Familiarity is a strange kind of death.", True),
                    ("He put the cup on the table by the door.", False),
                    ("Consciousness arrived as panic first.", True),
                    ("Grief sat in the kitchen with its coat on.", False)):
        got = flagged(s)
        ok &= got == want
        print(("PASS " if got == want else "FAIL ") + "%r -> %s" % (s, got))
    hits, n = scan('"Death is near," he said. The rail was cold under my hand.\n\nKindness is a kind of patience.')
    good = n == 2 and len(hits) == 1 and hits[0][0] == 2
    ok &= good
    print(("PASS " if good else "FAIL ") + "speech left out, paragraphs counted (%d read, %s)" % (n, hits))
    text = '"Death is near," he said. The rail was cold under my hand.\n\nKindness is a kind of patience.'
    near = at_hand(paragraphs(text), 2, "Kindness is a kind of patience.") if good else None
    good = near == ["hand", "rail"]
    ok &= good
    print(("PASS " if good else "FAIL ") + "things at hand from the paragraph before, nearest first (%s)" % near)
    body = "\n\n".join(["The rail was cold under my hand."] * 6 + ["Kindness is a kind of patience."])
    rep = report(body)
    good = any("at the close" in l for l in rep) and not any("at the close" in l for l in report(text))
    ok &= good
    print(("PASS " if good else "FAIL ") + "a flag in the last two paragraphs carries the closing note")
    print("ALL PASS" if ok else "SOME FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    if sys.argv[1:] == ["--build"]:
        print(len(build()), "nouns classed ->", CACHE)
    elif sys.argv[1:] == ["--selftest"]:
        sys.exit(selftest())
    elif len(sys.argv) == 2:
        with io.open(sys.argv[1], encoding="utf-8", errors="replace") as f:
            print("\n".join(report(f.read(), limit=10 ** 6)))
    else:
        print(__doc__)
        sys.exit(2)
