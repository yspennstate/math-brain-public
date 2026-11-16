# verdict_read.py: where does the narrator pass a verdict on what the page has just shown?
#
# One question put to a reader. A pattern cannot find this fault, because it lies between a sentence and the
# paragraph before it (R9); a reader asked for nothing else finds it (R10).
# The list is a list of candidates and not of faults: on the two test texts
# between one in six and two in three of the listed sentences were ones blind readers had put among a chapter's
# weakest, and one listed sentence was the one four readers ranked first of twelve to keep. Put the listed
# sentences to line_read.py, which asks keep or cut with controls, before cutting anything.
#
#   python -I -X utf8 verdict_read.py make <text.md> --out <dir> [--runs 2]
#   python -I -X utf8 verdict_read.py collect <dir> [--min 2] [--skip <file>] [--targets <file>] [--sets 1]
#
# make writes <dir>/packets/V01..: CHAPTER.md, PROMPT.md, GO (one folder per reader) and keeps a copy of the
#   text as <dir>/TEXT.md. Put each reader's JUDGEMENT.json in <dir>/judged/<Vnn>/.
# collect matches the listed sentences to the narrated sentences of the text and prints, in the order of the
#   text, how many runs list each and what the first run says had already shown it.
#   --min: runs that must list a sentence for it to be offered (default: every run).
#   --skip: a file of phrases, one per line; a sentence holding one is printed but not offered.
#   --targets: write the offered sentences, one per line as they stand in the text, for line_read.py make.
#   --sets N: split the offered sentences into N files (<file>.1 ..), alternating down the text, so that each
#   line_read packet carries a spread of the chapter and no more marks than a reader can rank.
import argparse
import glob
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reader_checks as rc

PROMPT = """You are an experienced fiction editor. In this folder is CHAPTER.md, a chapter of a novel. Read it whole, from
the first line to the last, before you answer.

Look for one thing only. In some places a narrator, after a scene or a paragraph has shown something, adds a
sentence that rates it, sums it up, says what it meant, or tells the reader how to take it: the narrator's verdict
on his own material. Three examples of the kind, from no particular book: "It was the happiest afternoon of that
year." set after the afternoon has been shown; "That was the whole trouble with us." set after a quarrel; "I have
been grateful for it ever since." A sentence in which the narrator speaks of the book or of the telling counts too.

Do not list a sentence only because it is abstract, or general, or weak in some other way, and do not list
speech. List a sentence only if what it says had already been shown by the paragraph or the scene before it, so
that the chapter would lose nothing but the verdict if the sentence went.

List every such sentence, quoted exactly and whole, in the order they appear, and for each give one line naming
what before it had already shown the thing. Do not pad the list and do not trim it: a chapter may hold three such
sentences or thirty.

Write the result to JUDGEMENT.json in this folder, shaped as
{"verdicts": [{"sentence": "...", "already_shown_by": "..."}]}
and write a short REPORT.md beside it. Do not use the network, do not look outside this folder, and do not change
CHAPTER.md.
"""


def norm(t):
    return re.sub(r"[^a-z0-9 ]", "", re.sub(r"\s+", " ", t.lower().replace("’", "'").replace("*", ""))).strip()


def told(par):
    return " ".join(par.replace("“", '"').replace("”", '"').split('"')[0::2])


def sents(text):
    out, seen = [], set()
    for par in text.split("\n"):
        if par.strip() and not par.startswith("#"):
            for s in rc.sentences(told(par)):
                s = s.strip()
                if len(s.split()) >= 3 and norm(s) not in seen:
                    seen.add(norm(s))
                    out.append(s)
    return out


def hit(s, quotes):
    # A quote counts for the sentence it starts in, and for a later sentence it runs on into. A short sentence
    # is not matched by a longer quote that only ends with the same words.
    ns = norm(s)
    a = ns[:40]
    if len(ns) < 12:
        return False
    for q in quotes:
        if len(q) < 12:
            continue
        if q.startswith(a) or ns.startswith(q[:40]) or (len(q) >= 40 and q[:40] in ns):
            return True
        if (len(a) == 40 and a in q) or (len(ns.split()) >= 6 and ns in q):
            return True
    return False


def make(a):
    text = io.open(a.text, encoding="utf-8").read().replace("\r\n", "\n")
    os.makedirs(a.out, exist_ok=True)
    io.open(os.path.join(a.out, "TEXT.md"), "w", encoding="utf-8", newline="\n").write(text)
    for k in range(1, a.runs + 1):
        d = os.path.join(a.out, "packets", "V%02d" % k)
        os.makedirs(d, exist_ok=True)
        for name, body in (("CHAPTER.md", text), ("PROMPT.md", PROMPT), ("GO", "go\n")):
            io.open(os.path.join(d, name), "w", encoding="utf-8", newline="\n").write(body)
    print("%d packets under %s/packets (%d words)" % (a.runs, a.out, len(text.split())))


def collect(a):
    text = io.open(os.path.join(a.dir, "TEXT.md"), encoding="utf-8").read()
    runs = []
    for f in sorted(glob.glob(os.path.join(a.dir, "judged", "*", "JUDGEMENT.json"))):
        try:
            j = json.loads(io.open(f, encoding="utf-8-sig").read())
        except Exception as e:
            print("unreadable:", f, e)
            continue
        v = [x if isinstance(x, dict) else {"sentence": str(x)} for x in (j.get("verdicts") or [])]
        runs.append([(norm(x.get("sentence", "")), x.get("already_shown_by", "")) for x in v])
    if not runs:
        sys.exit("no JUDGEMENT.json under %s/judged/*/" % a.dir)
    need = a.min or len(runs)
    skip = [x.strip() for x in io.open(a.skip, encoding="utf-8").read().split("\n") if x.strip()] if a.skip else []
    ss = sents(text)
    offered, listed = [], 0
    for s in ss:
        n = sum(hit(s, [q for q, _ in r]) for r in runs)
        if not n:
            continue
        listed += 1
        why = next((w for r in runs for q, w in r if hit(s, [q])), "")
        held = any(x in s for x in skip)
        once = text.count(s) == 1
        tag = "skip" if held else ("offer" if n >= need and once else ("not verbatim" if n >= need else ""))
        if tag == "offer":
            offered.append(s)
        print("%d/%d %-12s %s\n      shown by: %s" % (n, len(runs), tag, s[:160], why[:160]))
    print("runs %d (they list %s) | narrated sentences %d | listed by any run %d | offered (listed by %d or more, "
          "not skipped, found once in the text) %d" % (len(runs), ", ".join(str(len(r)) for r in runs), len(ss),
                                                        listed, need, len(offered)))
    if a.targets:
        k = max(1, a.sets)
        for i in range(k):
            name = a.targets if k == 1 else "%s.%d" % (a.targets, i + 1)
            part = offered[i::k]
            io.open(name, "w", encoding="utf-8", newline="\n").write("\n".join(part) + "\n")
            print("wrote %d sentences to %s" % (len(part), name))


ap = argparse.ArgumentParser(description="the narrator's verdict, put to a reader as one question")
sub = ap.add_subparsers(dest="cmd", required=True)
m = sub.add_parser("make")
m.add_argument("text")
m.add_argument("--out", required=True)
m.add_argument("--runs", type=int, default=2)
c = sub.add_parser("collect")
c.add_argument("dir")
c.add_argument("--min", type=int, default=0)
c.add_argument("--skip")
c.add_argument("--targets")
c.add_argument("--sets", type=int, default=1)
a = ap.parse_args()
make(a) if a.cmd == "make" else collect(a)
