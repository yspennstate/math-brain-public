# line_read.py: would a blind reader cut these sentences? A keep-or-cut reading of one text with marked controls.
#
# A reader who is shown two copies of a text that differ in a few sentences finds the sentences and votes once
# for the set. This tool gives a count for each sentence instead. The sentences in question (targets) are marked
# in one copy of the text together with as many control sentences, picked by a fixed rule and not by eye, and
# each reader says keep, cut or either for every mark and ranks them. The controls show whether the readers cut
# whatever is marked.
#
#   python -I -X utf8 line_read.py make <text.md> <targets.txt> --out <dir> [--runs 4]
#                                       [--avoid <file>] [--faulted <file>]
#   python -I -X utf8 line_read.py score <dir>
#
# targets.txt: one target per line, exactly as it stands in the text (two adjacent sentences on one line are one
#   mark). Each must occur exactly once.
# --avoid: a file of phrases, one per line; a paragraph holding any of them gives no control (lines that must
#   not be controls, lines changed in the last pass).
# --faulted: a file of sentences readers have already faulted; none of them becomes a control.
# make writes <dir>/packets/R01..: CHAPTER.md, PROMPT.md, GO (one folder per reader) and <dir>/key.json.
# key.json says which marks are targets. Keep it off any machine a reader runs on and out of any repository.
# Register the rules below before a reader runs. Put each reader's JUDGEMENT.json in <dir>/judged/<Rnn>/.
#
# Rules score applies (with T targets and R readers there are T*R votes on each side):
#   - "either" is not a cut;
#   - controls cut in half their votes or more: a cutting reading, no line-by-line finding;
#   - otherwise the readers single out the targets if cut votes on targets exceed cut votes on controls by a
#     third of T*R or more;
#   - a sentence the readers would cut: cut by three quarters of the readers or more; would keep likewise;
#     anything else is split.
# First use: a keep-or-cut read of a draft chapter with marked controls, 16 Nov 2026.
import argparse
import glob
import io
import json
import os
import re
import sys

PROMPT = """You are an experienced fiction editor and a demanding reader of literary novels. In this folder is CHAPTER.md.
Read it whole, from the first line to the last, before you answer anything. You are not told who wrote it, and
you should not guess.

%(n)d places in it are marked like this: [[7: the sentence]]. A mark may hold a pair of sentences. The double
brackets and the numbers are not part of the text. The editor before you marked them for a second opinion: for
each one, would the text be better with it cut, or is it better kept? Some of them were marked at random, so do
not assume that a marked sentence is weak. Nothing else may change: the choice is the sentence as it stands, or
the text without it and nothing in its place.

DO THIS
1. For each mark say keep, cut or either (either means the text is no better and no worse without it), and give
   one line of reason that says what the sentence does, or fails to do, where it stands.
2. For each say how sure you are: sure or leaning.
3. Rank all %(n)d from the one the text most needs (first) to the one it would gain most by losing (last).
4. In three sentences say what kind of sentence you found yourself cutting and what kind keeping.

Write the result to JUDGEMENT.json in this folder, shaped as
{"sentences": {"1": {"verdict": "keep or cut or either", "sure": "sure or leaning", "why": "..."}, "2": {...}},
 "rank_need_first": [the %(n)d numbers in order], "pattern": "..."}
with every number under "sentences", and write a short REPORT.md beside it. Do not use the network, do not look
outside this folder, and do not change CHAPTER.md.
"""


def norm(s):
    return re.sub(r"\s+", " ", s.replace("*", "").lower()).strip()


def sentences(p):
    return [x for x in re.split(r"(?<=[.!?])\s+", p.strip()) if x]


def lines_of(path):
    if not path:
        return []
    return [x.strip() for x in io.open(path, encoding="utf-8").read().replace("\r\n", "\n").split("\n") if x.strip()]


def make(a):
    text = io.open(a.text, encoding="utf-8").read().replace("\r\n", "\n")
    targets = lines_of(a.targets)
    avoid = lines_of(a.avoid)
    blob = norm(" ".join(lines_of(a.faulted)))
    for s in targets:
        if text.count(s) != 1:
            sys.exit("target must occur exactly once (found %d): %s" % (text.count(s), s[:80]))
    paras = text.split("\n\n")
    tpar = [i for s in targets for i, p in enumerate(paras) if s in p]

    def control(i, used):
        p = paras[i]
        if not p or p[0] in '"#*>(-' or '"' in p or "“" in p or "\n" in p.strip():
            return None
        if any(x in p for x in avoid) or any(abs(i - j) <= 2 for j in tpar + used):
            return None
        ss = sentences(p)
        if len(ss) < 3:
            return None
        last = ss[-1]
        if not 6 <= len(last.split()) <= 30 or text.count(last) != 1 or (blob and norm(last)[:30] in blob):
            return None
        return last

    picks, used = [], []
    for i0 in tpar:
        for i in list(range(i0 - 3, -1, -1)) + list(range(i0 + 3, len(paras))):
            last = control(i, used)
            if last:
                picks.append(last)
                used.append(i)
                break
        else:
            sys.exit("no control found for the target in paragraph %d" % (i0 + 1))
    items = sorted([(text.index(s), "target", s) for s in targets] + [(text.index(s), "control", s) for s in picks])
    marked, key = text, {}
    for n, (_, role, s) in enumerate(items, 1):
        marked = marked.replace(s, "[[%d: %s]]" % (n, s))
        key[str(n)] = {"role": role, "sentence": s}
        print("%2d %-7s %s" % (n, role, s[:120]))
    if marked.count("[[") != len(items):
        sys.exit("marks in the text: %d, expected %d" % (marked.count("[["), len(items)))
    for k in range(1, a.runs + 1):
        d = os.path.join(a.out, "packets", "R%02d" % k)
        os.makedirs(d, exist_ok=True)
        for name, body in (("CHAPTER.md", marked), ("PROMPT.md", PROMPT % {"n": len(items)}), ("GO", "go\n")):
            io.open(os.path.join(d, name), "w", encoding="utf-8", newline="\n").write(body)
    io.open(os.path.join(a.out, "key.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps({"text": os.path.basename(a.text), "key": key}, indent=1, ensure_ascii=False))
    print("%d packets under %s/packets; key.json beside them stays local" % (a.runs, a.out))
    print("control rule: for each target, the nearest earlier paragraph of narration (no speech, 3+ sentences), 3+ "
          "paragraphs from any mark, last sentence 6-30 words, not in --faulted, no --avoid phrase; its last sentence.")


def score(a):
    key = json.load(io.open(os.path.join(a.dir, "key.json"), encoding="utf-8"))["key"]
    js = []
    for f in sorted(glob.glob(os.path.join(a.dir, "judged", "*", "JUDGEMENT.json"))):
        try:
            js.append(json.loads(io.open(f, encoding="utf-8-sig").read()))
        except Exception as e:
            print("unreadable:", f, e)
    R = len(js)
    if not R:
        sys.exit("no JUDGEMENT.json under %s/judged/*/" % a.dir)
    tot = {"target": 0, "control": 0}
    cnt = {"target": 0, "control": 0}
    rank = {"target": [], "control": []}
    for n in sorted(key, key=int):
        role = "control" if key[n]["role"] == "control" else "target"
        vs, rk = [], []
        for j in js:
            sd = j.get("sentences") if isinstance(j.get("sentences"), dict) else {}
            s = sd.get(n) or {}
            v = str(s.get("verdict", "?")).strip().lower()
            v = next((k for k in ("keep", "cut", "either") if v.startswith(k)), "?")
            vs.append(v + ("" if str(s.get("sure", "")).lower().startswith("sure") else "~"))
            order = [str(x) for x in (j.get("rank_need_first") or [])]
            if n in order:
                rk.append(order.index(n) + 1)
        cuts = sum(v.startswith("cut") for v in vs)
        keeps = sum(v.startswith("keep") for v in vs)
        tot[role] += cuts
        cnt[role] += R
        rank[role] += rk
        call = "readers would cut" if cuts >= 0.75 * R else ("readers would keep" if keeps >= 0.75 * R else "split")
        print("%2s %-7s %-24s ranks %-14s %-18s %s" % (n, role, " ".join(vs), " ".join(map(str, rk)), call,
                                                    key[n]["sentence"][:70]))
    H, C = tot["target"], tot["control"]
    print("readers %d | cut votes on targets %d of %d, on controls %d of %d (~ = leaning)" % (R, H, cnt["target"], C, cnt["control"]))
    if cnt["control"] and C >= 0.5 * cnt["control"]:
        print("A CUTTING READING: the controls were cut in half their votes or more; report no line-by-line finding.")
    elif H - C >= cnt["target"] / 3.0:
        print("The readers single out the targets (difference %d, bar %.1f)." % (H - C, cnt["target"] / 3.0))
    else:
        print("The readers do not single out the targets (difference %d, bar %.1f)." % (H - C, cnt["target"] / 3.0))
    for r in ("target", "control"):
        if rank[r]:
            print("mean rank of %ss: %.2f (1 = most needed)" % (r, sum(rank[r]) / len(rank[r])))


ap = argparse.ArgumentParser(description="keep-or-cut reading of marked sentences with controls")
sub = ap.add_subparsers(dest="cmd", required=True)
m = sub.add_parser("make")
m.add_argument("text")
m.add_argument("targets")
m.add_argument("--out", required=True)
m.add_argument("--runs", type=int, default=4)
m.add_argument("--avoid")
m.add_argument("--faulted")
s = sub.add_parser("score")
s.add_argument("dir")
a = ap.parse_args()
make(a) if a.cmd == "make" else score(a)
