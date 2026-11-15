"""Merge the mirror's journal hubs into the live ones by item, keeping each file's order.
usage: memory_hub_merge.py <live.md> <origin.md> [--apply]  (backup to ~/.claude/brain_graph/memory_sync_backups_<date>)

An item is a top-level line plus its indented continuation lines. An origin-only item goes in after the item that
precedes it in origin; a checkbox [x] in origin over the same item [ ] here takes origin's version (resolved on the
other machine). memory_twoway_sync.py imports merge_items() for OPEN_QUESTIONS / PREDICTIONS / STATE_OF_MIND / MISTAKES.
"""
import datetime, difflib, os, re, shutil, sys

PRED = re.compile(r"^- \[([ x])\] (p\d+) \|")
CHK = re.compile(r"^(\s*- \[)([ x])\] (.*)$")


def _items(L):
    out = []
    for x in L:
        if out and x.strip() and x[:1] in (" ", "\t") and out[-1][0].strip():
            out[-1][1].append(x)
        else:
            out.append([x, []])
    return out


def _similar(x, y):
    return x.strip() in y or difflib.SequenceMatcher(None, x, y).ratio() >= 0.6


def merge_items(lv, og):
    """lv, og: lists of lines (no CR). Returns (out lines, added lines, origin lines not kept, replaced)."""
    LI, OI = _items(lv), _items(og)
    lset, oset = set(lv), set(og)
    live_only = [x for x in lv if x.strip() and x not in oset]
    first_idx = {}
    for i, (f, _) in enumerate(LI):
        if f.strip():
            first_idx.setdefault(f, i)
    adds_after, conts_add, replaced = {}, {}, []
    prev = -1
    for f, conts in OI:
        if not f.strip():
            continue
        if f in first_idx:
            i = first_idx[f]
            for c in conts:
                if c.strip() and c not in lset and not any(_similar(c, y) for y in live_only):
                    conts_add.setdefault(i, []).append(c)
            prev = i
            continue
        hit = next((y for y in live_only if _similar(f, y)), None)
        if hit is not None:
            mo, ml = CHK.match(f), CHK.match(hit)
            if hit in first_idx:
                i = first_idx[hit]
                same_item = mo and ml and (mo.group(3) == ml.group(3) or (
                    PRED.match(f) and PRED.match(hit) and PRED.match(f).group(2) == PRED.match(hit).group(2)))
                if same_item and mo.group(2) == "x" and ml.group(2) == " ":
                    LI[i][0] = f
                    replaced.append(f[:90])
                    for c in conts:
                        if c.strip() and c not in lset:
                            conts_add.setdefault(i, []).append(c)
                prev = i
            continue
        adds_after.setdefault(prev, []).append([f, [c for c in conts if c not in lset]])
    out = []
    for f, conts in adds_after.get(-1, []):
        out += [f] + conts
    for i, (f, conts) in enumerate(LI):
        out += [f] + conts + conts_add.get(i, [])
        for g, gc in adds_after.get(i, []):
            out += [g] + gc
    added = [x for x in out if x not in lset and x.strip()]
    so = set(out)
    lost = [x for x in og if x.strip() and x not in so]
    return out, added, lost, replaced


def main():
    live_p, orig_p = sys.argv[1], sys.argv[2]
    raw = open(live_p, "rb").read()
    crlf = b"\r\n" in raw
    lv = raw.decode("utf-8", "replace").replace("\r", "").split("\n")
    og = open(orig_p, "rb").read().decode("utf-8", "replace").replace("\r", "").split("\n")
    out, added, lost, replaced = merge_items(lv, og)
    print("%s: live %d -> %d lines; added %d (replaced %d); mirror lines not kept %d" % (
        os.path.basename(live_p), len(lv), len(out), len(added), len(replaced), len(lost)))
    for x in added:
        print("  + " + x[:150])
    for x in lost:
        print("  - " + x[:150])
    if "--apply" in sys.argv:
        bk = os.path.expanduser(r"~\.claude\brain_graph\memory_sync_backups_" + datetime.date.today().strftime("%Y%m%d"))
        os.makedirs(bk, exist_ok=True)
        shutil.copy2(live_p, os.path.join(bk, os.path.basename(live_p) + ".prehub"))
        t = "\n".join(out)
        if crlf:
            t = t.replace("\n", "\r\n")
        open(live_p + ".hubtmp", "w", encoding="utf-8", newline="").write(t)
        os.replace(live_p + ".hubtmp", live_p)
        print("applied")


if __name__ == "__main__":
    main()
