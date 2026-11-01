# -*- coding: utf-8 -*-
"""After wave_target_reader.py: write the FIX/DROP list for the integrator (claude-4a88bc43 maps each claim to its landed
logical_name and lands the correction or retirement), a count table, and the argument list for the push of
claude_labels/ beside the wave's results in math-open-problems (claude-322bc92e, 10 Oct 2026)."""
import collections
import glob
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
L = os.path.join(HERE, "claude_labels")
DEST = "probability_campaigns/codex_pool_2026-10-10/claude_labels"


def main():
    rows = [json.loads(l) for l in io.open(os.path.join(L, "LABELS.jsonl"), encoding="utf-8") if l.strip()]
    # two reader copies can both read the target where they meet: keep the last row per (target, claim)
    rows = list({(r["target"], str(r["claim_id"])): r for r in rows}.values())
    fixdrop = [r for r in rows if str(r.get("verdict")).upper() in ("FIX", "DROP")]
    with io.open(os.path.join(L, "FIX_DROP_FOR_INTEGRATOR.jsonl"), "w", encoding="utf-8", newline="\n") as fh:
        for r in fixdrop:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    by_t = collections.defaultdict(collections.Counter)
    for r in rows:
        by_t[r["target"]][r["claude_label"]] += 1
    labels = ["PROVED", "PARTIAL", "COUNTEREXAMPLE", "DRAFT", "UNREAD"]
    lines = ["# Cross-family labels on the 300-worker wave (sealed Claude, 10 Oct 2026)", "",
             "One read per target over every claim its workers labelled proved, independently checked or counterexample. "
             "Labels: PROVED (complete proof of exactly the claim), PARTIAL (a weaker statement proved), COUNTEREXAMPLE, "
             "DRAFT (not established). Per-claim rows in LABELS.jsonl; FIX and DROP rows in FIX_DROP_FOR_INTEGRATOR.jsonl.",
             "", "| target | " + " | ".join(labels) + " |", "|---" * (len(labels) + 1) + "|"]
    for t in sorted(by_t):
        lines.append("| %s | %s |" % (t, " | ".join(str(by_t[t][x]) for x in labels)))
    tot = collections.Counter(r["claude_label"] for r in rows)
    lines.append("| all | %s |" % " | ".join(str(tot[x]) for x in labels))
    lines += ["", "FIX: %d, DROP: %d, of %d claims." % (sum(1 for r in fixdrop if str(r["verdict"]).upper() == "FIX"),
                                                       sum(1 for r in fixdrop if str(r["verdict"]).upper() == "DROP"), len(rows))]
    unread_t = collections.Counter(r["target"] for r in rows if r["claude_label"] == "UNREAD")
    lines += ["", "How far to trust these labels: each read covered every strong claim of one target at once (about 40 claims, "
              "up to 400 KB of attempts), so a label is a first sorting by a second model family, not a line-by-line proof "
              "check. The claims are mostly lemma-sized steps and special cases; PROVED means the step's proof held up in that "
              "read, never that a big open problem was solved; counterexamples are mostly to proposed routes. UNREAD (%d: %s) "
              "are claims with no label: two first reads were killed in flight, and by the re-read most of those workers' "
              "files had moved to GitHub (probability_campaigns/codex_pool_2026-10-10/), where a later pass can read them."
              % (tot["UNREAD"], ", ".join("%s %d" % kv for kv in unread_t.most_common()))]
    io.open(os.path.join(L, "SUMMARY.md"), "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    pairs = []
    for f in sorted(glob.glob(os.path.join(L, "*"))):
        n = os.path.basename(f)
        if n.endswith(".response.json"):
            continue        # the CLI's response records stay here (session records do not go to GitHub)
        pairs.append("%s/%s=%s" % (DEST, n, f.replace("\\", "/")))
    io.open(os.path.join(L, "push_args.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(pairs) + "\n")
    print("\n".join(lines[-4:]))
    print("push pairs:", len(pairs))


if __name__ == "__main__":
    main()
