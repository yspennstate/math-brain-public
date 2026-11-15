#!/usr/bin/env python3
"""prompt_class_tool.py - the mechanical half of the prompt-class pass (SWS section P).

Why it exists (2026-11-12): the pass went dark from 2026-10-21 to 2026-11-12. By November a day held 3,000-5,000
ledger rows, nearly all of them loop re-fires and headless-worker prompts; the words he actually typed were 15-120
unique texts a day. "Read yesterday's unclassified lines" had become unreadable, so the pass was skipped. This tool
does everything that needs no judgement and leaves the model only the unique texts he typed.

  count [N]                    per-day table for the last N days (default 14): rows, classified, owner rows, owner classified
  heads DAY [DAY ...]          write heads_<day>.txt (numbered unique unclassified owner texts with no repeat_of, cut to
                               420 chars) and heads_<day>.json (number -> sha1) into the work dir; a text is listed once
                               across the days asked for, under the first day given
  build OUT DAY [DAY ...]      join verdicts_<day>.txt ("<number> <class> <0|1 correction> [owner|automation]") to
                               heads_<day>.json, add the mechanical verdicts, write the sidecar OUT
  mech OUT                     the mechanical verdicts alone

Mechanical verdicts (never a judgement about the user's words):
  A  a text since --since whose every ledger row has origin automation            -> automation
  B  an unclassified owner row whose text already carries a class in the ledger   -> that class (the commonest)
Then: python apply_prompt_classes.py OUT   (the only writer of the ledger), and re-run `count`.

Options: --dir WORKDIR (default ~/.claude/dreaming/prompt_class_work), --since YYYY-MM-DD (default 2026-10-20),
--rater NAME. Practice follows the 13 Oct sidecar: scope all, so a loop's re-fires carry the class of the order he
typed and stay his in the prompt layers; a machine-written prompt stamped owner gets class automation AND origin
automation on its verdict line. Classify the newest day first. Boundary rules for the classes: dream_prompt_sws.md,
section P.
"""
import sys, os, io, json, re, hashlib, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import prompt_archive as pa

TAX = pa.TAXONOMY + ["automation"]


def key(text):
    # the same hash apply_prompt_classes.py recomputes
    return hashlib.sha1(re.sub(r"\s+", " ", (text or "").lower()).encode("utf-8", "replace")).hexdigest()


def rows():
    out = []
    with io.open(pa.LEDGER, encoding="utf-8", errors="replace") as f:
        for ln in f.read().split("\n"):      # "\n" only: a record may hold U+2028 (see apply_prompt_classes.py)
            if ln.strip():
                try:
                    out.append(json.loads(ln))
                except Exception:
                    pass
    return out


def opt(argv, name, default):
    if name in argv:
        i = argv.index(name)
        val = argv[i + 1]
        del argv[i:i + 2]
        return val
    return default


def cmd_count(n):
    tot, cls, own, owncls = (collections.Counter() for _ in range(4))
    for r in rows():
        d = str(r.get("ts") or "")[:10]
        tot[d] += 1
        has = bool(r.get("class_model"))
        cls[d] += has
        if (r.get("origin") or "owner") == "owner":
            own[d] += 1
            owncls[d] += has
    print("day         rows  classified  owner  owner_classified")
    for d in sorted(x for x in tot if len(x) == 10)[-n:]:
        print("%s %6d %8d %8d %8d%s" % (d, tot[d], cls[d], own[d], owncls[d], "" if owncls[d] >= own[d] else "   <- open"))
    dark = [d for d in tot if len(d) == 10 and own[d] and not owncls[d]]
    print("days with owner rows and none classified: %d%s" % (len(dark), (" (%s .. %s)" % (min(dark), max(dark))) if dark else ""))


def cmd_heads(days, work):
    os.makedirs(work, exist_ok=True)
    allrows = rows()
    taken = set()
    for day in days:
        seen = collections.OrderedDict()
        for r in allrows:
            if str(r.get("ts") or "")[:10] != day or r.get("class_model") or r.get("repeat_of"):
                continue
            if (r.get("origin") or "owner") != "owner":
                continue
            k = key(r.get("text", ""))
            if k not in seen and k not in taken:
                seen[k] = r
        taken.update(seen)
        idx = {}
        with io.open(os.path.join(work, "heads_%s.txt" % day), "w", encoding="utf-8", newline="\n") as f:
            for i, (k, r) in enumerate(seen.items(), 1):
                t = re.sub(r"\s+", " ", r.get("text", ""))
                cut = t[:420] + (" ...[%d chars]" % len(t) if len(t) > 420 else "")
                f.write("%d|%s|%s|%s| %s\n" % (i, str(r.get("ts"))[11:16], str(r.get("session") or "")[:8],
                                               r.get("class_provisional") or "", cut))
                idx[str(i)] = k
        with io.open(os.path.join(work, "heads_%s.json" % day), "w", encoding="utf-8", newline="\n") as f:
            json.dump(idx, f)
        print("%s: %d unique owner texts to read -> %s" % (day, len(seen), os.path.join(work, "heads_%s.txt" % day)))


def mechanical(skip, since, rater):
    by = collections.defaultdict(lambda: {"o": collections.Counter(), "c": collections.Counter(), "n": 0})
    for r in rows():
        b = by[key(r.get("text", ""))]
        b["o"][r.get("origin") or ""] += 1
        if r.get("class_model"):
            b["c"][r["class_model"]] += 1
        elif str(r.get("ts") or "")[:10] >= since:
            b["n"] += 1
    out, stat = [], collections.Counter()
    for k, b in by.items():
        if k in skip or not b["n"]:
            continue
        if set(b["o"]) == {"automation"}:
            out.append({"sha1": k, "class_model": "automation", "confidence": 0.9, "correction_present": False,
                        "rater": rater + "_mechA"})
            stat["A texts"] += 1; stat["A rows"] += b["n"]
        elif b["c"] and b["o"].get("owner"):
            out.append({"sha1": k, "class_model": b["c"].most_common(1)[0][0], "confidence": 0.7, "rater": rater + "_mechB"})
            stat["B texts"] += 1; stat["B rows"] += b["n"]
    return out, stat


def cmd_build(out_path, days, work, since, rater):
    read = collections.OrderedDict()
    for day in days:
        idx = json.load(io.open(os.path.join(work, "heads_%s.json" % day), encoding="utf-8"))
        n = 0
        for ln in io.open(os.path.join(work, "verdicts_%s.txt" % day), encoding="utf-8"):
            p = ln.split()
            if not p:
                continue
            if p[1] not in TAX or p[2] not in ("0", "1") or (len(p) > 3 and p[3] not in ("owner", "automation")):
                raise SystemExit("bad verdict line in %s: %r" % (day, ln))
            v = {"sha1": idx[p[0]], "class_model": p[1], "confidence": 0.8, "correction_present": p[2] == "1", "rater": rater}
            if len(p) > 3:
                v["origin"] = p[3]
                v["confidence"] = 0.95
            if v["sha1"] in read:
                if read[v["sha1"]]["class_model"] != p[1]:
                    print("  same text, two verdicts: %s #%s %s (kept %s)" % (day, p[0], p[1], read[v["sha1"]]["class_model"]))
            else:
                read[v["sha1"]] = v
            n += 1
        if n != len(idx):
            raise SystemExit("%s: %d verdicts for %d texts - every listed text needs one" % (day, n, len(idx)))
        print("%s: %d verdicts" % (day, n))
    mech, stat = mechanical(set(read), since, rater)
    with io.open(out_path, "w", encoding="utf-8", newline="\n") as f:
        for v in list(read.values()) + mech:
            f.write(json.dumps(v) + "\n")
    print("sidecar %s: %d lines (%d read, mechanical %s)" % (out_path, len(read) + len(mech), len(read), dict(stat)))
    print("next: python %s %s" % (os.path.join(HERE, "apply_prompt_classes.py"), out_path))


def main():
    argv = sys.argv[1:]
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    work = opt(argv, "--dir", os.path.join(HERE, "prompt_class_work"))
    since = opt(argv, "--since", "2026-10-20")
    rater = opt(argv, "--rater", "prompt_class_tool")
    cmd, rest = argv[0], argv[1:]
    if cmd == "count":
        cmd_count(int(rest[0]) if rest else 14)
    elif cmd == "heads" and rest:
        cmd_heads(rest, work)
    elif cmd == "build" and len(rest) >= 2:
        cmd_build(rest[0], rest[1:], work, since, rater)
    elif cmd == "mech" and rest:
        cmd_build(rest[0], [], work, since, rater)
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
