"""Before writing a part of a paper, see how refereed papers made the same move; after, see where yours stands.

  python -I -X utf8 paper_moves.py show <move> "<what you are about to write>" [--k 3]
      three passages from the paper shelf that make this move on the nearest subject, each with its source
  python -I -X utf8 paper_moves.py check <move> <your paragraph file>
      your paragraph's measures beside the shelf's for the same move (median and middle half): words, sentence
      length, words before the first full stop, citations, displayed formulas, "we" per hundred words, and the
      share of sentences that open on the object rather than on "We" / "In this" / "It is"
  python -I -X utf8 paper_moves.py moves
      the moves and how many passages the shelf holds of each

Moves: abstract intro_opening contribution result_stated proof_entered definition idea_given prior_work
open_question section_opening. The shelf is papers/shelf/*.jsonl (cut_papers.py): refereed arXiv papers under
CC BY, CC BY-SA or CC0, in probability, combinatorics, statistics and machine learning. A shelf passage is shown
to learn the move from, never to copy: name the source if a phrase of it is used.
"""
import glob, json, math, os, re, statistics, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
TOK = re.compile(r"[a-z][a-z-]+")
STOP = set("the of and a an to in is are for on that this with by as we be it at from or which can our its these their there then than this those such also has have not but if all any each one two".split())


def load():
    rows = []
    for fp in sorted(glob.glob(os.path.join(HERE, "shelf", "*.jsonl"))):
        with open(fp, encoding="utf-8") as f:
            rows += [json.loads(l) for l in f]
    return rows


def toks(t):
    return [w for w in TOK.findall(re.sub(r"\$[^$]*\$", " ", t.lower())) if w not in STOP]


def bm25(rows, q, k1=1.4, b=0.75):
    docs = [toks(r["title"] + " " + r["text"]) for r in rows]
    N = len(docs) or 1
    df = Counter(w for d in docs for w in set(d))
    avg = sum(map(len, docs)) / N if N else 1
    qs = toks(q)
    out = []
    for r, d in zip(rows, docs):
        tf = Counter(d)
        s = sum(math.log(1 + (N - df[w] + .5) / (df[w] + .5)) * tf[w] * (k1 + 1) / (tf[w] + k1 * (1 - b + b * len(d) / avg))
                for w in qs if w in tf)
        out.append((s, r))
    return sorted(out, key=lambda x: -x[0])


def measures(t):
    plain = re.sub(r"\$\$.*?\$\$", " FORMULA. ", t)
    plain = re.sub(r"\$[^$]*\$", "x", plain)
    sents = [s for s in re.split(r"(?<=[.!?])\s+", plain) if len(s.split()) >= 3]
    w = len(plain.split()) or 1
    opens = sum(1 for s in sents if not re.match(r"(We|In this|It is|There (is|are)|This (paper|note))\b", s))
    return {"words": w,
            "sentence length": round(w / max(1, len(sents)), 1),
            "first sentence": len(sents[0].split()) if sents else 0,
            "citations": t.count("[cite]"),
            "displayed formulas": t.count("$$") // 2,
            "we per 100 words": round(100 * len(re.findall(r"\b[Ww]e\b|\bour\b", plain)) / w, 1),
            "share opening on the object": round(opens / max(1, len(sents)), 2)}


# House rule for our papers: say what existed before, what is new, and how the new relates to the old, crediting the
# mathematicians by name. A credit sentence ties a paper's own work to a cited earlier one.
REL = {
    "extends / generalizes / improves": r"extend(s|ed|ing)?|generali[sz](e|es|ed|ing)|improv(e|es|ed|ing) (on|upon)|refine[sd]?|strengthen(s|ed)?|sharpen(s|ed)?",
    "follows / builds on / adapts": r"build(s|ing)? on|built on|follow(s|ing)? (the|closely|an?)|based on (the|an?) (idea|method|approach|argument|technique)s?|inspired by|adapt(s|ed|ing)? (the|an?)|borrow(s|ed)?",
    "differs from": r"in contrast (to|with)|unlike|differs? from|instead of",
    "answers / recovers": r"answer(s|ing)? (a |the )?question|conjectured|settl(e|es|ed)|recover(s|ing)?|confirm(s|ed)?",
    "names the origin": r"((was|were) )?(first )?(introduced|proved|shown|obtained|established|studied|initiated) by|(was|were) (first )?(introduced|proved|shown|obtained|established|studied) in|due to",
}
REL_ANY = re.compile(r"\b(" + "|".join(REL.values()) + r")\b", re.I)
OWN = re.compile(r"\b(we|our|this paper|the present paper|this note|this work|this article)\b", re.I)
NAMED = re.compile(r"[A-Z][a-z]+(?:[- ](?:and|&|--|-)?\s?[A-Z][a-z]+)*(?: et al\.)?,? \[cite\]|[A-Z][a-z]+'s? (?:theorem|method|argument|approach|result|conjecture|inequality|bound)")


def credit_sentences(rows):
    out = []
    for r in rows:
        if r["role"] not in ("prior_work", "intro_opening", "contribution", "abstract"):
            continue
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", r["text"]):
            if "[cite]" in s and REL_ANY.search(s) and 8 <= len(s.split()) <= 70:
                kind = next(k for k, p in REL.items() if re.search(r"\b(" + p + r")\b", s, re.I))
                # a sentence that only names where a tool came from ("due to Nelson [cite]") credits without "we";
                # the other kinds must be about this paper's own work
                if kind != "names the origin" and not OWN.search(s):
                    continue
                out.append({"text": s, "kind": kind, "named": bool(NAMED.search(s)), "row": r})
    return out


def credit(a):
    rows = load()
    cs = credit_sentences(rows)
    if a[1] == "show":
        q, k = a[2], int(a[a.index("--k") + 1]) if "--k" in a else 6
        named = sum(c["named"] for c in cs)
        print(f"credit: sentences where a refereed paper ties its own work to a cited earlier one ({len(cs)} on the "
              f"shelf; {named} name the author as well as citing)\n")
        pseudo = [dict(c["row"], text=c["text"], _c=c) for c in cs]
        seen = set()
        for s, r in bm25(pseudo, q):
            if r["work"] in seen:
                continue
            seen.add(r["work"])
            print(f"- [{r['_c']['kind']}] {r['text']}\n  ({r['author']}, \"{r['title']}\", {r['journal_ref']}; arXiv {r['arxiv']})\n")
            if len(seen) >= k:
                break
    elif a[1] == "check":
        text = open(a[2], encoding="utf-8").read()
        if re.search(r"\\(cite|\[|begin\{|ref\{|emph)", text):
            sys.path.insert(0, HERE)
            from cut_papers import clean
            text = clean(text)
        mine = credit_sentences([{"role": "intro_opening", "text": text, "work": "yours"}])
        per = Counter(c["row"]["work"] for c in cs)
        works = len({r["work"] for r in rows if r["role"] in ("prior_work", "contribution")})
        print(f"credit check: {len(mine)} sentence(s) in your text tie your work to a cited earlier one; "
              f"{sum(c['named'] for c in mine)} name the author.")
        print(f"  shelf: {len(per)} of {works} papers with a contribution or prior-work passage have at least one such "
              f"sentence there; {sum(c['named'] for c in cs)} of {len(cs)} name the author.")
        for c in mine:
            print(f"  [{c['kind']}{', named' if c['named'] else ', cite only'}] {c['text'][:220]}")
        if not mine:
            print("  none found: say once, in a sentence with a citation, whose result or method yours extends, follows "
                  "or departs from, and name them. See: paper_moves.py credit show \"<your subject>\"")


def main():
    a = sys.argv[1:]
    if a and a[0] == "credit" and len(a) >= 3:
        credit(a); return
    if not a or a[0] == "moves":
        c = Counter(r["role"] for r in load())
        papers = len({r["work"] for r in load()})
        print(f"paper shelf: {papers} papers")
        for k, v in c.most_common():
            print(f"  {k:16s} {v}")
        return
    cmd, move = a[0], a[1]
    rows = [r for r in load() if r["role"] == move]
    if not rows:
        print(f"no passages for move '{move}'; run: paper_moves.py moves"); return
    if cmd == "show":
        k = int(a[a.index("--k") + 1]) if "--k" in a else 3
        seen = set()
        print(f"{move}: how refereed papers on the nearest subject made this move ({len(rows)} on the shelf)\n")
        for s, r in bm25(rows, a[2]):
            if r["work"] in seen:
                continue
            seen.add(r["work"])
            print(f"- {r['author']}, \"{r['title']}\" ({r['year']}), {r['journal_ref']}; arXiv {r['arxiv']}, licence {r['license'].split('/')[-3:-1]}")
            print("  " + r["text"][:1400] + ("..." if len(r["text"]) > 1400 else "") + "\n")
            if len(seen) >= k:
                break
    elif cmd == "check":
        text = open(a[2], encoding="utf-8").read()
        # 15 Nov: a paragraph pasted from a .tex read 0 citations and 0 displayed formulas, because the shelf is
        # stored after cut_papers.clean ([cite], $$...$$). Clean raw LaTeX the same way before measuring it.
        if re.search(r"\\(cite|\[|begin\{|ref\{|emph)", text):
            sys.path.insert(0, HERE)
            from cut_papers import clean
            text = clean(text)
        mine = measures(text)
        shelf = [measures(r["text"]) for r in rows]
        print(f"{move}: your paragraph against {len(shelf)} on the shelf (median, middle half)")
        for key, v in mine.items():
            xs = sorted(m[key] for m in shelf)
            q1, med, q3 = xs[len(xs) // 4], statistics.median(xs), xs[3 * len(xs) // 4]
            flag = "  <- outside the middle half" if v < q1 or v > q3 else ""
            print(f"  {key:30s} yours {v:>6}   shelf {med:>6} ({q1} to {q3}){flag}")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
