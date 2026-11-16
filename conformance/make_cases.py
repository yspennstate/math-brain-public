#!/usr/bin/env python3
"""Write the reference cases that verify_install.py replays.

Every case is drawn from the public export in export/population/ and every expected output is what the public
tools printed on a reference install built from a fresh clone. Nothing here comes from a private store.

    python conformance/make_cases.py --out conformance/cases [--seed 1115] [--search 600] [--fragment 200]
                                     [--negative 50] [--walk 150] [--hook 100] [--nav 40]

Kinds of case
  search    the words of a card's title as one query; checks the hits, and records whether the card itself came back
  fragment  eight content words from the middle of a card's text (a harder, reworded query)
  negative  a question the store cannot answer; the reference says whether WEAK MATCH printed
  walk      --id <card>: the card's own text and its link targets
  hook      one UserPromptSubmit event through math_sense.py: served or silent, and which cards
  nav       a question to the repository's own navigation brain
Each case is written with what was printed (ids, titles, scores, flags), the seconds it took and the tool version.
"""
import argparse
import hashlib
import json
import os
import random
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import _runner as R  # noqa: E402

POP = os.path.join(R.ROOT, "export", "population")
STOP = set("""a an the of and or in on for to with by is are be as at from that this these those which its it into than
then there their such any all each every some not no if when where we let suppose show prove holds hold given over under
between both also only one two three let's above below one's has have had was were will can may must should would""".split())

NEGATIVE = [
    "banana bread recipe with walnuts and brown butter", "how to change the oil in a 2014 pickup truck",
    "best hiking trails near the coast in autumn", "kubernetes pod eviction policy under memory pressure",
    "symptoms of vitamin d deficiency in adults", "history of the byzantine silk trade",
    "how to tune a classical guitar by ear", "train timetable from the airport to the city centre",
    "what temperature to roast a chicken", "javascript promise rejection unhandled warning in node",
    "dog breed that sheds the least", "watercolour techniques for painting clouds", "winter tyre pressure guidance",
    "how to write a cover letter for a museum job", "football league standings this weekend",
    "recipe for vegetable curry with coconut milk", "how to repot an orchid", "printer says paper jam but no paper",
    "css flexbox centering a div vertically", "the plot of a famous nineteenth century opera",
    "how to sharpen a kitchen knife on a whetstone", "packing list for a week of camping",
    "learning to swim as an adult", "how do noise cancelling headphones work", "renewing a passport by mail",
    "how to brew pour over coffee", "grammar rules for semicolons", "planting tomatoes in containers",
    "fixing a squeaky door hinge", "how long to boil an egg", "translating a menu from italian",
    "choosing a sleeping bag temperature rating", "how to fold a fitted sheet", "setting up a home wifi mesh",
    "symptoms of a failing car alternator", "make sourdough starter from scratch", "how to clean a cast iron pan",
    "what is a good beginner telescope", "how to remove a red wine stain", "budgeting app for a small household",
    "jazz chord voicings for piano", "cheap flights in the off season", "how to paint a fence",
    "difference between baking soda and baking powder", "basic first aid for a sprained ankle",
    "how to stop a dripping tap", "knitting a scarf for beginners", "ferry routes between greek islands",
    "how to write a haiku", "storing fresh herbs in the fridge",
]

HOOK_NONMATH = [
    "please rename the variable in the login form", "commit the readme change and push it",
    "what time is the meeting tomorrow", "fix the typo in the footer", "make the button blue",
    "summarise yesterday's standup notes", "open the settings page", "thanks, that works",
    "deploy the staging branch", "add a dark mode toggle",
]


def cards(limit_scan=None):
    """Yield (id, title, body, domain) for every node row of the export."""
    with open(os.path.join(POP, "MANIFEST.json"), encoding="utf-8") as fh:
        man = json.load(fh)
    n = 0
    for part in man["parts"]["nodes"]:
        with open(os.path.join(POP, part), encoding="utf-8") as fh:
            for line in fh:
                d = json.loads(line)
                try:
                    meta = json.loads(d.get("metadata_json") or "{}")
                except ValueError:
                    meta = {}
                yield d["id"], d.get("title") or "", d.get("body") or "", meta.get("domain") or ""
                n += 1
                if limit_scan and n >= limit_scan:
                    return


def words(s):
    return [w for w in re.findall(r"[A-Za-z][A-Za-z\-']{2,}", s) if w.lower() not in STOP]


def fragment(body, rng):
    ws = words(re.sub(r"\$[^$]*\$|\\[a-zA-Z]+", " ", body))
    if len(ws) < 14:
        return None
    start = rng.randrange(2, max(3, len(ws) - 9))
    return " ".join(ws[start:start + 8])


def manifest_digest():
    with open(os.path.join(POP, "MANIFEST.json"), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:16]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(HERE, "cases"))
    ap.add_argument("--seed", type=int, default=1115)
    ap.add_argument("--search", type=int, default=600)
    ap.add_argument("--fragment", type=int, default=200)
    ap.add_argument("--negative", type=int, default=50)
    ap.add_argument("--walk", type=int, default=150)
    ap.add_argument("--hook", type=int, default=100)
    ap.add_argument("--nav", type=int, default=40)
    ap.add_argument("--only", default="", help="comma list of kinds to (re)write")
    a = ap.parse_args(argv)
    R.prepare_env()
    os.makedirs(a.out, exist_ok=True)
    rng = random.Random(a.seed)
    only = set(x for x in a.only.split(",") if x)

    pool = []
    for cid, title, body, dom in cards():
        if len(title) < 12 or len(title) > 160 or title.lower().startswith(("attempt on", "attempt record")):
            continue
        if len(words(title)) < 2:
            continue
        pool.append((cid, title, body, dom))
    rng.shuffle(pool)
    print("pool of titled cards:", len(pool), flush=True)
    meta = {"export_manifest_sha16": manifest_digest(), "seed": a.seed, "made": time.strftime("%Y-%m-%d %H:%M:%S"),
            "python": sys.version.split()[0], "platform": sys.platform}

    def write(kind, rows):
        if only and kind not in only:
            return
        path = os.path.join(a.out, kind + ".jsonl")
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            for r in rows():
                r.update({"kind": kind, "ref": meta})
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
                fh.flush()
        print("wrote", path, flush=True)

    def search_rows():
        for i, (cid, title, body, dom) in enumerate(pool[:a.search]):
            q = " ".join(words(title)[:10])
            rc, out, err, sec = R.recall([q])
            p = R.parse_search(out)
            yield {"case": "search-%04d" % i, "argv": [q], "target": cid, "domain": dom, "rc": rc,
                   "expect": p, "target_rank": (p["ids"].index(cid) + 1) if cid in p["ids"] else None,
                   "seconds": sec}

    def fragment_rows():
        k = 0
        for cid, title, body, dom in pool[a.search:]:
            if k >= a.fragment:
                break
            q = fragment(body, rng)
            if not q:
                continue
            rc, out, err, sec = R.recall([q])
            p = R.parse_search(out)
            yield {"case": "fragment-%04d" % k, "argv": [q], "target": cid, "domain": dom, "rc": rc, "expect": p,
                   "target_rank": (p["ids"].index(cid) + 1) if cid in p["ids"] else None, "seconds": sec}
            k += 1

    def negative_rows():
        for i, q in enumerate(NEGATIVE[:a.negative]):
            rc, out, err, sec = R.recall([q])
            yield {"case": "negative-%04d" % i, "argv": [q], "rc": rc, "expect": R.parse_search(out), "seconds": sec}

    def walk_rows():
        base = a.search + a.fragment + 50
        for i, (cid, title, body, dom) in enumerate(pool[base:base + a.walk]):
            rc, out, err, sec = R.recall(["--id", cid])
            yield {"case": "walk-%04d" % i, "argv": ["--id", cid], "rc": rc, "expect": R.parse_walk(out),
                   "seconds": sec}

    def hook_rows():
        base = a.search + a.fragment + 50 + a.walk
        n_math = a.hook - len(HOOK_NONMATH)
        for i, (cid, title, body, dom) in enumerate(pool[base:base + n_math]):
            frag = fragment(body, rng) or ""
            prompt = "I am working on this: %s (%s). What is known, and what should I check first?" % (title, frag)
            rc, out, err, sec, why = R.hook_with_reason(prompt, "conformance-%04d" % i)
            yield {"case": "hook-%04d" % i, "prompt": prompt, "session_id": "conformance-%04d" % i,
                   "target": cid, "rc": rc, "expect": R.parse_hook(out), "silence": why, "seconds": sec}
        for j, prompt in enumerate(HOOK_NONMATH):
            rc, out, err, sec, why = R.hook_with_reason(prompt, "conformance-n%02d" % j)
            yield {"case": "hook-n%02d" % j, "prompt": prompt, "session_id": "conformance-n%02d" % j,
                   "rc": rc, "expect": R.parse_hook(out), "silence": why, "seconds": sec}

    def nav_rows():
        qs = ["dreaming", "how do I import the store", "recall workflow", "prompt hook for codex",
              "packet importer for new cards", "MCP server", "link strength", "fast recall prebuild",
              "navigation cards", "evaluation protocol", "challenge bank", "privacy settings", "export the store",
              "attempt ledger", "cited works", "formal verification with lean", "benchmark", "field brain starter",
              "spreading activation", "weak match", "superseded cards", "recall server", "card types",
              "how to add cards", "math_sense hook", "nightly dream", "agents guide", "tests", "brain switch",
              "frontier digest", "query embedding", "property order", "subagent adapter", "runtime paths",
              "server safety", "recall keeper", "math walk", "math note", "claim vectors", "prefilter"]
        for i, q in enumerate(qs[:a.nav]):
            rc, out, err, sec = R.nav([q])
            yield {"case": "nav-%04d" % i, "argv": [q], "rc": rc, "expect": R.parse_nav(out),
                   "out_sha16": hashlib.sha256(out.encode("utf-8")).hexdigest()[:16], "seconds": sec}

    write("negative", negative_rows)
    write("walk", walk_rows)
    write("search", search_rows)
    write("fragment", fragment_rows)
    write("hook", hook_rows)
    write("nav", nav_rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
