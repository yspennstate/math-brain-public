# -*- coding: utf-8 -*-
"""Second pass over the wave claims the per-target reads left UNREAD (claude-322bc92e, 10 Oct 2026): one sealed Claude
read per target with only those claims and their workers' attempts (shorter packets, ids listed up front), rows appended
to claude_labels/LABELS.jsonl (labels_finish.py keeps the last row per claim)."""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
L = os.path.join(HERE, "claude_labels")
sys.path.insert(0, HERE)
sys.path.insert(0, "~/pd_work/pilot_pair")
import claude_reader_s11 as R  # noqa: E402
import wave_target_reader as W  # noqa: E402  (its ASK and claim filter)


REPO = "~/math-open-problems"
WAVE = "probability_campaigns/codex_pool_2026-10-10/wave300"
_INDEX = {}


def read_file(target, worker, name):
    """The worker's file here, or - once it has moved to GitHub and been deleted (10 Oct) - the copy in the campaign repo's
    origin/master, read with git show (no download)."""
    import subprocess
    p = "~/brain_workers/%s/%s" % (worker, name)
    if os.path.exists(p):
        return io.open(p, encoding="utf-8", errors="replace").read()
    if not _INDEX:
        out = subprocess.run(["git", "-C", REPO, "ls-tree", "-r", "--name-only", "origin/master", WAVE],
                             capture_output=True, text=True).stdout.splitlines()
        for f in out:
            parts = f.split("/")
            if len(parts) >= 5:
                _INDEX.setdefault((parts[-3], parts[-2].split("_")[0], parts[-1]), f)
    f = _INDEX.get((target, worker, name))
    if not f:
        return None
    r = subprocess.run(["git", "-C", REPO, "show", "origin/master:" + f], capture_output=True)
    return r.stdout.decode("utf-8", errors="replace") if r.returncode == 0 else None


def main():
    rows = [json.loads(l) for l in io.open(os.path.join(L, "LABELS.jsonl"), encoding="utf-8") if l.strip()]
    last = {(r["target"], str(r["claim_id"])): r for r in rows}
    unread = {}
    for r in last.values():
        if r["claude_label"] == "UNREAD":
            unread.setdefault(r["target"], set()).add(str(r["claim_id"]))
    print("targets with unread claims:", {t: len(v) for t, v in unread.items()})
    for t, ids in sorted(unread.items()):
        ws = sorted({r["worker"] for r in last.values() if r["target"] == t and str(r["claim_id"]) in ids})
        claims, parts = [], []
        for w in ws:
            mine = []
            for line in (read_file(t, w, "CLAIMS.jsonl") or "").splitlines():
                try:
                    c = json.loads(line)
                except ValueError:
                    continue
                cid = str(c.get("claim_id") or c.get("id") or "")
                if cid in ids:
                    c["_worker"] = w
                    c["claim_id"] = cid
                    mine.append(c)
            if not mine:
                continue
            claims += mine
            att = (read_file(t, w, "ATTEMPT.md") or "(no ATTEMPT.md)")[:20000]
            parts.append("=== WORKER %s: claims ===\n%s\n=== WORKER %s: ATTEMPT.md (first 20k chars) ===\n%s" % (
                w, "\n".join(json.dumps(c, ensure_ascii=False)[:5000] for c in mine), w, att))
        if not claims:
            continue
        head = "Use exactly these claim ids as the JSON keys: %s\n\n" % ", ".join(c["claim_id"] for c in claims)
        R.OUT = L
        j = R.call(W.ASK + "\n\nOPEN PROBLEM " + t + "\n\n" + head + "\n\n".join(parts)[:250000], timeout=1800)
        res = str(j.get("result") or "")
        io.open(os.path.join(L, "%s.pass2.md" % t), "w", encoding="utf-8", newline="\n").write(
            "# %s second pass on %d unread claims (served %s)\n\n%s\n" % (t, len(claims),
                                                                          sorted((j.get("modelUsage") or {}).keys()), res))
        m = re.search(r"\{.*\}", res, re.S)
        try:
            lab = json.loads(m.group(0)) if m else {}
        except ValueError:
            lab = {}
        with io.open(os.path.join(L, "LABELS.jsonl"), "a", encoding="utf-8", newline="\n") as fh:
            for c in claims:
                v = lab.get(c["claim_id"]) or {}
                fh.write(json.dumps({"target": t, "worker": c["_worker"], "claim_id": c["claim_id"],
                                     "worker_label": c.get("status"), "claude_label": v.get("label") or "UNREAD",
                                     "verdict": v.get("verdict"), "line_checked": v.get("line_checked"),
                                     "note": v.get("note"), "pass": 2}, ensure_ascii=False) + "\n")
        print(t, "read", len(claims), "labelled", sum(1 for c in claims if lab.get(c["claim_id"])), flush=True)


if __name__ == "__main__":
    main()
