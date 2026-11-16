#!/usr/bin/env python3
"""Write annotated transcripts of the brain at work into conformance/logs/.

Each log is one real call of a public tool on the public store, printed exactly as an agent would see it, with a
header (the command, the seconds it took) and a few lines under it saying what to look for. They show how the
pieces talk to each other: a search and the words that matched, two wordings fused by rank, a walk along links,
spreading through links with --depth 2, the WEAK MATCH hint, and the prompt hook serving a block or staying silent
with its reason. Compare your own output with them when a check fails.

    python conformance/make_logs.py [--out conformance/logs] [--n 200]
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import _runner as R  # noqa: E402

NOTES = {
    "search": "Each hit names its id, kind and score; 'matched' lists the query words found, (title) marks a title "
              "phrase. The last line of a hit says how many links it has and the --id call that reads it whole.",
    "multi": "Two or three wordings in one call are searched separately and fused by rank: 'found by wording 1 (rank "
             "2), 2 (rank 1)' shows where each wording put the card. This is the recommended way to ask.",
    "walk": "--id prints one card whole and every link: the kind (proves, cites, generalizes ...), the direction, the "
            "other card's short id and title and the link's stated reason. Step to a linked card with --id <short id>.",
    "spread": "--depth 2 lets activation spread along links from the word matches; a 'found by spreading' line names "
              "the card it came from and the links it travelled. A CAUTION line means a negative link (a counterexample "
              "or failure) brought the card in. Spreading reorders leads; it does not prove relevance.",
    "weak": "WEAK MATCH is printed when the best score is below the level where an answering card usually appears, "
            "and 'No card contains' names query words absent from the store. Reword, or accept the store has nothing.",
    "hook_served": "The prompt hook read a UserPromptSubmit event on stdin and printed one JSON object whose "
                   "hookSpecificOutput.additionalContext is the block the agent sees before it answers. Claude Code and "
                   "Codex both accept this shape.",
    "hook_silent": "The hook printed nothing, which is correct for prompts that are not mathematics or that the store "
                   "cannot answer. The reason it gave itself is in the 'silence reason' line (from its harness log).",
    "nav": "The repository's own navigation brain: cards for files, folders and README sections, joined by links.",
}

MULTI = [
    ("spectral gap relaxation time mixing time", "absolute spectral gap reversible Markov chain"),
    ("percolation critical probability square lattice", "Kesten theorem p_c = 1/2 bond percolation"),
    ("Fourier entropy influence conjecture", "entropy of the Fourier spectrum bounded by total influence"),
    ("cutoff phenomenon random walk", "abrupt convergence to stationarity total variation"),
    ("uniform spanning tree loop-erased random walk", "Wilson's algorithm"),
    ("Erdos-Renyi giant component threshold", "random graph G(n,p) emergence of the giant"),
    ("first passage percolation time constant", "shape theorem for passage times"),
    ("branching process extinction probability", "Galton-Watson survival generating function"),
    ("hypercontractivity Bonami inequality", "noise operator L2 to Lq bound boolean cube"),
    ("Ising model phase transition", "spontaneous magnetization critical temperature"),
    ("concentration of measure Lipschitz functions", "Talagrand convex distance inequality"),
    ("self-avoiding walk connective constant", "number of self-avoiding walks growth rate"),
    ("random matrix semicircle law", "Wigner matrix empirical spectral distribution"),
    ("coupling from the past", "perfect simulation Propp Wilson"),
    ("isoperimetric inequality hypercube", "Harper vertex boundary Hamming ball"),
]


def write_log(path, title, cmd, out, sec, note, extra=""):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# %s\n# command: %s\n# seconds: %.2f\n#\n# what to look for: %s\n%s#\n" % (title, cmd, sec, note,
                                                                                           extra))
        fh.write(out if out.endswith("\n") else out + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(HERE, "logs"))
    ap.add_argument("--cases", default=os.path.join(HERE, "cases"))
    a = ap.parse_args(argv)
    R.prepare_env()
    os.makedirs(a.out, exist_ok=True)
    index = []

    def load(kind):
        p = os.path.join(a.cases, kind + ".jsonl")
        return [json.loads(x) for x in open(p, encoding="utf-8")] if os.path.exists(p) else []

    kinds = {"search": "search", "search_reworded": "search", "two_wordings": "multi", "spreading": "spread",
             "walk": "walk", "off_topic": "weak", "hook_served": "hook_served", "hook_silent": "hook_silent",
             "nav": "nav"}

    def reuse(i):
        # A run stopped part way (the hook logs take minutes each on a slow machine) restarts where it left off:
        # a log already written in full is indexed from its header instead of being run again.
        for f in sorted(os.listdir(a.out)):
            if not f.startswith("%03d_" % i) or not f.endswith(".txt"):
                continue
            lines = open(os.path.join(a.out, f), encoding="utf-8").read().splitlines()
            body = [x for x in lines if not x.startswith("#")]
            if not body or not lines[0].startswith("# ") or not lines[2].startswith("# seconds: "):
                return False
            index.append({"log": f, "kind": kinds[f[4:-4]], "title": lines[0][2:],
                          "seconds": float(lines[2].split(": ", 1)[1])})
            return True
        return False

    def emit(name, kind, title, cmd, out, sec, extra=""):
        path = os.path.join(a.out, name + ".txt")
        write_log(path, title, cmd, out, sec, NOTES[kind], extra)
        index.append({"log": name + ".txt", "kind": kind, "title": title, "seconds": sec})
        print(name, flush=True)

    n = 0
    for c in load("search")[:50]:
        if reuse(n + 1):
            n += 1
            continue
        rc, out, err, sec = R.recall(c["argv"])
        n += 1
        emit("%03d_search" % n, "search", "search: %s" % c["argv"][0], "math_recall.py %s" % json.dumps(c["argv"][0]),
             out, sec)
    for c in load("fragment")[:20]:
        if reuse(n + 1):
            n += 1
            continue
        rc, out, err, sec = R.recall(c["argv"])
        n += 1
        emit("%03d_search_reworded" % n, "search", "reworded search: %s" % c["argv"][0],
             "math_recall.py %s" % json.dumps(c["argv"][0]), out, sec)
    for q1, q2 in MULTI:
        if reuse(n + 1):
            n += 1
            continue
        rc, out, err, sec = R.recall([q1, "--or", q2])
        n += 1
        emit("%03d_two_wordings" % n, "multi", "two wordings: %s | %s" % (q1, q2),
             "math_recall.py %s --or %s" % (json.dumps(q1), json.dumps(q2)), out, sec)
    for q1, q2 in MULTI[:15]:
        if reuse(n + 1):
            n += 1
            continue
        rc, out, err, sec = R.recall([q1, "--depth", "2", "--limit", "6"])
        n += 1
        emit("%03d_spreading" % n, "spread", "spreading through links: %s" % q1,
             "math_recall.py %s --depth 2 --limit 6" % json.dumps(q1), out, sec)
    for c in load("walk")[:40]:
        if reuse(n + 1):
            n += 1
            continue
        rc, out, err, sec = R.recall(c["argv"])
        n += 1
        emit("%03d_walk" % n, "walk", "walk from %s" % c["argv"][1][:20], "math_recall.py --id %s" % c["argv"][1],
             out, sec)
    for c in load("negative")[:15]:
        if reuse(n + 1):
            n += 1
            continue
        rc, out, err, sec = R.recall(c["argv"])
        n += 1
        emit("%03d_off_topic" % n, "weak", "off-topic question: %s" % c["argv"][0],
             "math_recall.py %s" % json.dumps(c["argv"][0]), out, sec)
    for c in load("hook")[:35] + [h for h in load("hook") if h["case"].startswith("hook-n")][:5]:
        if reuse(n + 1):
            n += 1
            continue
        rc, out, err, sec, reasons = R.hook_with_reason(c["prompt"], c["session_id"] + "-log")
        n += 1
        served = bool(out.strip())
        event = json.dumps({"hook_event_name": "UserPromptSubmit", "session_id": c["session_id"] + "-log",
                            "prompt": c["prompt"]}, ensure_ascii=False)
        extra = "# stdin event: %s\n# silence reason: %s\n" % (event, "; ".join(reasons) if reasons else "(none)")
        body = out
        if served:
            try:
                d = json.loads(out.strip().splitlines()[-1])
                body = ("--- raw stdout (one JSON object) ---\n%s\n--- additionalContext as the agent reads it ---\n%s"
                        % (out.strip(), d["hookSpecificOutput"]["additionalContext"]))
            except Exception:
                pass
        emit("%03d_hook_%s" % (n, "served" if served else "silent"), "hook_served" if served else "hook_silent",
             "prompt hook: %s" % c["prompt"][:90], "math_sense.py < event.json", body or "(no output)\n", sec, extra)
    for c in load("nav")[:20]:
        if reuse(n + 1):
            n += 1
            continue
        rc, out, err, sec = R.nav(c["argv"])
        n += 1
        emit("%03d_nav" % n, "nav", "navigation: %s" % c["argv"][0], "navigation/nav_query.py %s"
             % json.dumps(c["argv"][0]), out, sec)
    with open(os.path.join(a.out, "INDEX.jsonl"), "w", encoding="utf-8", newline="\n") as fh:
        for r in index:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("logs written:", len(index))


if __name__ == "__main__":
    sys.exit(main())
