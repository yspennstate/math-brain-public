"""Search a small brain: one markdown record per file, with the frontmatter of framework/docs/MEMORY_CONVENTIONS.md.

    python recall.py "wording one" --or "wording two" --or "wording three"
    python recall.py --id some_record_slug

Prints whole records with their slugs, best first. Each wording is scored on its own and a record keeps its best
score, so a second or third wording can find what the first one missed. A record marked superseded is pushed down
and printed with the slug that replaced it. When the best score is low the output says WEAK MATCH: reword, or
treat the store as not having the answer.

Standard library only. Point it at another folder with --dir or the BRAIN_MEM_DIR variable.
"""
import argparse
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WORD = re.compile(r"[a-z0-9]+")
STOP = set("a an and are as at be by for from has have in is it its of on or that the this to was were what when "
           "which who why with does did do how".split())


def fold(w):
    # a plural and its singular are one word here ("refunds", "refund"); nothing heavier than that
    if len(w) > 3 and w.endswith("s") and not w.endswith("ss") and not w.endswith("us"):
        return w[:-1]
    return w


def words(text):
    return [fold(w) for w in WORD.findall(text.lower()) if w not in STOP]


def load(folder):
    recs = {}
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md") or name.isupper() or name.startswith("MEMORY") or name.startswith("MISTAKES"):
            continue
        with open(os.path.join(folder, name), encoding="utf-8") as fh:
            text = fh.read().replace("\r\n", "\n")  # a Windows checkout may carry CRLF
        meta, body = {}, text
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        if m:
            body = m.group(2)
            for line in m.group(1).splitlines():
                k, _, v = line.strip().partition(":")
                if v.strip():
                    meta[k.strip()] = v.strip()
        slug = meta.get("name", name[:-3])
        recs[slug] = dict(meta=meta, body=body.strip(), text=text, terms=words(meta.get("description", "") + " " + body))
    return recs


def bm25(recs, query, k1=1.4, b=0.75):
    n = len(recs)
    avg = sum(len(r["terms"]) for r in recs.values()) / max(n, 1)
    df = {}
    for r in recs.values():
        for t in set(r["terms"]):
            df[t] = df.get(t, 0) + 1
    out = {}
    for slug, r in recs.items():
        tf, s = {}, 0.0
        for t in r["terms"]:
            tf[t] = tf.get(t, 0) + 1
        for t in set(words(query)):
            if t in tf:
                idf = math.log(1 + (n - df[t] + 0.5) / (df[t] + 0.5))
                s += idf * tf[t] * (k1 + 1) / (tf[t] + k1 * (1 - b + b * len(r["terms"]) / avg))
        out[slug] = s
    return out


def show(slug, r):
    m = r["meta"]
    head = "== %s  [%s%s]" % (slug, m.get("type", "?"), ", " + m["status"] if "status" in m else "")
    if m.get("superseded_by"):
        head += "  SUPERSEDED by %s" % m["superseded_by"]
    print(head)
    print(r["body"])
    print()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?")
    ap.add_argument("--or", dest="more", action="append", default=[], help="another wording of the same question")
    ap.add_argument("--id", nargs="+", help="print these records whole")
    ap.add_argument("--dir", default=os.environ.get("BRAIN_MEM_DIR", os.path.join(HERE, "memory")))
    ap.add_argument("-n", type=int, default=4)
    a = ap.parse_args()
    recs = load(a.dir)
    if a.id:
        for s in a.id:
            hits = [k for k in recs if k == s or k.startswith(s)]
            if not hits:
                print("no record %s" % s)
            for k in hits:
                show(k, recs[k])
        return 0
    if not a.query:
        ap.error("give a question, or --id")
    best = {}
    for q in [a.query] + a.more:
        for slug, s in bm25(recs, q).items():
            best[slug] = max(best.get(slug, 0.0), s)
    for slug, r in recs.items():
        if r["meta"].get("superseded_by") or r["meta"].get("status") == "superseded":
            best[slug] *= 0.5
    ranked = sorted((s, k) for k, s in best.items() if s > 0)[::-1][: a.n]
    # BM25 scores shrink with the store (idf is a log of its size), so a fixed cut alone calls every hit in a
    # new ten-record store weak. A top record that holds at least half the words of one wording is not weak.
    cover = 0.0
    if ranked:
        top = set(recs[ranked[0][1]]["terms"])
        for q in [a.query] + a.more:
            qt = set(words(q))
            if qt:
                cover = max(cover, len(qt & top) / len(qt))
    if not ranked or (ranked[0][0] < 3.0 and cover < 0.5):
        print("WEAK MATCH: nothing here fits the question well. Reword it, or answer that the store does not have it.\n")
    for s, k in ranked:
        print("(score %.1f)" % s)
        show(k, recs[k])
    return 0


if __name__ == "__main__":
    sys.exit(main())
