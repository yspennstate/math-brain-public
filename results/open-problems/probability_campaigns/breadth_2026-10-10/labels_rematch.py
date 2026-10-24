# -*- coding: utf-8 -*-
"""Recover labels the first pass missed only because the reader keyed claims its own way (claude-322bc92e, 10 Oct 2026).
The per-target answers sometimes prefix a claim id with the target and worker ("C0023-w420-L0" for claim "L0" of w420);
an exact lookup called those UNREAD. This re-parses claude_labels/<target>.md (no new reads) and appends a row for every
UNREAD claim whose label is found under a key that is the id itself, ends with "-<id>", or names its worker and id."""
import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
L = os.path.join(HERE, "claude_labels")


def answer(t):
    p = os.path.join(L, "%s.md" % t)
    if not os.path.exists(p):
        return {}
    m = re.search(r"\{.*\}", io.open(p, encoding="utf-8").read(), re.S)
    try:
        return json.loads(m.group(0)) if m else {}
    except ValueError:
        return {}


def main():
    rows = [json.loads(l) for l in io.open(os.path.join(L, "LABELS.jsonl"), encoding="utf-8") if l.strip()]
    last = {(r["target"], str(r["claim_id"])): r for r in rows}
    cache, found, still = {}, 0, 0
    out = []
    for (t, cid), r in last.items():
        if r["claude_label"] != "UNREAD":
            continue
        lab = cache.setdefault(t, answer(t))
        w = str(r.get("worker") or "")
        hit = lab.get(cid)
        if not hit:
            keys = [k for k in lab if k.endswith("-" + cid) or k.endswith("_" + cid) or k.endswith(":" + cid)]
            keys = [k for k in keys if w in k] or keys
            if len(keys) == 1:
                hit = lab[keys[0]]
        if not hit:
            keys = [k for k in lab if w and w in k and cid in k]
            if len(keys) == 1:
                hit = lab[keys[0]]
        if hit and isinstance(hit, dict) and hit.get("label"):
            found += 1
            out.append(dict(r, claude_label=hit.get("label"), verdict=hit.get("verdict"),
                            line_checked=hit.get("line_checked"), note=hit.get("note"), rematched=True))
        else:
            still += 1
    with io.open(os.path.join(L, "LABELS.jsonl"), "a", encoding="utf-8", newline="\n") as fh:
        for r in out:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("rematched %d, still unread %d" % (found, still))


if __name__ == "__main__":
    main()
