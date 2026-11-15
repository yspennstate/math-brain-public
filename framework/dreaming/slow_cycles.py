"""slow_cycles.py - the two-day study of the cycles this laptop goes through (owner, 2026-09-15 14:3x:
"spend the next 2 days on this problem, studying the cycles that the computer goes through, and make things more efficient").

Reads ~/.claude/compute/slow_history.jsonl (one row per slow_probe.py run, every 10 min) and writes
~/.claude/compute/slow_cycles_report.md: what tripped, when, which processes were on top at those minutes,
the hour-of-day profile of every signal, and the minute-of-hour profile (to see the scheduled-task pile-ups at :00, :05,
:15 ...). Run by hand:  python -X utf8 slow_cycles.py [--hours 48]   or by the SlowCyclesReport6h task.
"""
import json, os, sys, time, collections

HIST = r"~\.claude\compute\slow_history.jsonl"
OUT = r"~\.claude\compute\slow_cycles_report.md"
SIGNALS = ["open_ms_scanned", "open_ms_excluded", "msmpeng_pct", "ps_start_wall_s", "ps_start_cpu_s", "cmd_start_ms",
           "cores_pinned", "core_avg", "cores_busy_sum", "commit_pct", "ram_free_gb", "disk_free_gb", "orphan_fragments",
           "disk_read_mb_s", "disk_write_mb_s"]


def load(hours):
    rows = []
    cutoff = time.time() - hours * 3600
    try:
        for line in open(HIST, encoding="utf-8"):
            try:
                r = json.loads(line)
            except Exception:
                continue
            if r.get("at_epoch", 0) >= cutoff:
                rows.append(r)
    except FileNotFoundError:
        pass
    return rows


def med(xs):
    xs = sorted(x for x in xs if isinstance(x, (int, float)))
    return None if not xs else xs[len(xs) // 2]


def fmt(x):
    return "-" if x is None else ("%.2f" % x if isinstance(x, float) else str(x))


def main():
    hours = 48
    if "--hours" in sys.argv:
        hours = float(sys.argv[sys.argv.index("--hours") + 1])
    rows = load(hours)
    L = []
    L.append("# Laptop slowness cycles - last %g h, %d probe runs (written %s)" % (hours, len(rows), time.strftime("%Y-%m-%d %H:%M")))
    if not rows:
        L.append("no history yet - slow_probe.py appends one row per run to slow_history.jsonl")
        open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n"); return
    # 1. verdict frequency
    vc = collections.Counter(v for r in rows for v in r.get("verdict", []))
    L.append("\n## What tripped, how often")
    for v, n in vc.most_common():
        L.append("- %-28s %3d of %d runs (%.0f pct)" % (v, n, len(rows), 100.0 * n / len(rows)))
    if not vc:
        L.append("- nothing tripped")
    # 2. timeline of tripped runs with their top consumers
    L.append("\n## Tripped runs (time, verdict, top consumers by cores, counts)")
    for r in rows:
        if r.get("verdict"):
            top = ", ".join("%s %.1f" % (t["name"].replace(".exe", ""), t["cores"]) for t in r.get("top", [])[:5])
            c = r.get("counts", {})
            L.append("- %s  %s  | %s  | procs %s ps %s py %s ffmpeg %s" % (r["at"][11:16], ",".join(r["verdict"]), top,
                     c.get("procs"), c.get("powershell"), c.get("python"), c.get("ffmpeg")))
    # 3. hour-of-day profile (median per hour) for each signal
    L.append("\n## Hour-of-day profile (median per hour)")
    byh = collections.defaultdict(list)
    for r in rows:
        byh[r["at"][11:13]].append(r)
    L.append("hour | runs | " + " | ".join(s.replace("_", " ") for s in SIGNALS))
    L.append("|".join(["---"] * (len(SIGNALS) + 2)))
    for h in sorted(byh):
        rs = byh[h]
        L.append("%s | %d | " % (h, len(rs)) + " | ".join(fmt(med([r.get(s) for r in rs])) for s in SIGNALS))
    # 4. minute-of-hour profile (the scheduled-task pile-ups)
    L.append("\n## Minute-of-hour profile (median cores busy, powershell count, python count) - task pile-ups show here")
    bym = collections.defaultdict(list)
    for r in rows:
        bym[int(r["at"][14:16]) // 5 * 5].append(r)
    for m in sorted(bym):
        rs = bym[m]
        L.append("- :%02d-%02d  runs %2d  cores %s  powershell %s  python %s  ps_start %s s  open %s ms" % (
            m, m + 4, len(rs), fmt(med([r.get("cores_busy_sum") for r in rs])), fmt(med([r.get("counts", {}).get("powershell") for r in rs])),
            fmt(med([r.get("counts", {}).get("python") for r in rs])), fmt(med([r.get("ps_start_wall_s") for r in rs])),
            fmt(med([r.get("open_ms_scanned") for r in rs]))))
    # 5. who is on top overall
    L.append("\n## Processes most often in the top 3 by CPU rate")
    tc = collections.Counter()
    for r in rows:
        for t in r.get("top", [])[:3]:
            tc[t["name"]] += 1
    for nm, n in tc.most_common(12):
        L.append("- %-22s %d runs" % (nm, n))
    # 6. core steering effect: E-core avg vs agent cores when available
    L.append("\n## Core steering")
    cs = [r.get("core_steer") for r in rows if r.get("core_steer")]
    L.append("- probe saw core_steer states: %s" % dict(collections.Counter(cs)))
    L.append("\nSignals and the fixes they point at: memory the_slow_laptop_was_the_on_access_scanner_2026_09_15; hook slow_sense.py.")
    open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
    if "--print" in sys.argv:
        print("\n".join(L))


if __name__ == "__main__":
    main()
