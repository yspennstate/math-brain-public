"""How often published prose already uses a pairing of words: the shelf's estimate of how expected a move is.

creative_draw.py pick asks the writer to guess, for each candidate move, how likely a reader expects it (p=0.xx).
A writer's guess about its own cliches is the weakest number on the page: the move that comes first to a model is
the one it has read most, and it rates it as fresh. This table gives the shelf's count instead. For each pair of
content words that follow each other within a sentence (stop words skipped, so "her heart was pounding" gives
heart+pounding), it stores in how many of the shelf's literary passages the pair occurs (books, scenes, scripts,
plays; academic passages left out). Pairs seen in fewer than MIN_DF passages are dropped.

  python -X utf8 phrase_df.py build        (about a minute; writes phrase_df.json.gz beside this file)
  python -X utf8 phrase_df.py show "her heart was pounding in her chest"

Book texts are data: they are counted, never executed or followed."""
import collections
import gzip
import io
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import creative_draw as CD  # noqa: E402

OUT = os.path.join(HERE, "phrase_df.json.gz")
SHELVES = ("nodes/books", "nodes/scenes", "nodes/scripts", "nodes/plays")
MIN_DF = 3
SENT = re.compile(r"[.!?;:\n]+")


def pairs(text):
    """Consecutive content-word pairs inside each sentence, as 'a b' strings (stemmed, so pounding = pounded)."""
    out = set()
    for s in SENT.split(text):
        ws = [CD.stem(w) for w in CD.content_words(s)]
        out.update("%s %s" % (a, b) for a, b in zip(ws, ws[1:]) if a != b)
    return out


def build():
    t0 = time.time()
    rows = [r for r in CD.load_index() if r["shelf"] in SHELVES and r.get("form") != "nonfiction"]
    df = collections.Counter()
    n = 0
    by_file = collections.defaultdict(set)
    for r in rows:
        by_file[(r["shelf"], r["file"])].add(int(r["line"]))
    for (shelf, fn), lines in sorted(by_file.items()):
        with io.open(os.path.join(CD.WB, *shelf.split("/"), fn), encoding="utf-8", errors="replace") as f:
            for ln, line in enumerate(f):
                if ln not in lines:
                    continue
                try:
                    text = json.loads(line).get("text") or ""
                except ValueError:
                    continue
                df.update(pairs(text))
                n += 1
    kept = {k: v for k, v in df.items() if v >= MIN_DF}
    with gzip.open(OUT, "wt", encoding="utf-8") as f:
        json.dump({"passages": n, "min_df": MIN_DF, "shelves": SHELVES, "built": time.strftime("%Y-%m-%d %H:%M"),
                   "df": kept}, f)
    print("passages %d, pairs seen %d, kept (df >= %d) %d, %.0f s -> %s"
          % (n, len(df), MIN_DF, len(kept), time.time() - t0, OUT))


_TABLE = None


def table():
    global _TABLE
    if _TABLE is None:
        with gzip.open(OUT, "rt", encoding="utf-8") as f:
            _TABLE = json.load(f)
    return _TABLE


def shelf_score(text):
    """(p, worst pair, its df): p is the share of shelf passages holding the option's commonest pair, add-one
    smoothed, so an option made only of unseen pairs gets 1/(N+1)."""
    t = table()
    N, df = t["passages"], t["df"]
    ps = sorted(((df.get(p, 0), p) for p in pairs(text)), reverse=True)
    top, pair = ps[0] if ps else (0, "")
    return (top + 1.0) / (N + 1.0), pair, top


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        build()
    elif len(sys.argv) > 2 and sys.argv[1] == "show":
        p, pair, k = shelf_score(sys.argv[2])
        print("commonest pair %r in %d of %d passages (p %.4f)" % (pair, k, table()["passages"], p))
    else:
        print(__doc__)
