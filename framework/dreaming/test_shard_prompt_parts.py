"""test_shard_prompt_parts.py - a month past PART_CAP is published as day-bounded parts, losslessly.

    python test_shard_prompt_parts.py [--module SHARD_PROMPT_ARCHIVE.py] [--old OLD_SHARD_PROMPT_ARCHIVE.py]

Every case runs main() on a temporary ledger and archive, with PART_CAP set small.
 S1 a month over the cap becomes parts that break only at day boundaries; every part is under the cap
    unless it holds one day; LOSSLESS, and --check reads it back clean
 S2 later days added: the parts already closed keep their exact bytes
 S3 a month published as one file before it outgrew the cap: the old file is removed once the parts hold every line
 S4 a leftover undated shard is removed when the ledger has no undated line
 S5 --union-existing on a month in parts: the new line goes to the last part, no whole-month file appears
 S6 a month under the cap keeps its single file name
With --old, the module before this change must fail S1 (the check can fail).
"""
import contextlib
import importlib.machinery
import importlib.util
import io
import json
import os
import shutil
import sys
import tempfile

if __name__ == "__main__" and ("-h" in sys.argv[1:] or "--help" in sys.argv[1:]):
    print(__doc__)
    sys.exit(0)

HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.abspath(sys.argv[sys.argv.index("--module") + 1]) if "--module" in sys.argv else os.path.join(HERE, "shard_prompt_archive.py")
OLD = os.path.abspath(sys.argv[sys.argv.index("--old") + 1]) if "--old" in sys.argv else None
CAP = 4000


def load(path, name):
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    return m


def rec(day, k, pad=200):
    return json.dumps({"ts": "%sT10:%02d:00" % (day, k % 60), "prompt": "p%d %s" % (k, "x" * pad)})


def days(month, first, last, per_day):
    out, k = [], 0
    for d in range(first, last + 1):
        for _ in range(per_day):
            out.append(rec("%s-%02d" % (month, d), k))
            k += 1
    return out


def files(arch):
    return {n: io.open(os.path.join(arch, n), encoding="utf-8").read() for n in sorted(os.listdir(arch))}


def run(m, tmp, lines, *argv):
    live = os.path.join(tmp, "PROMPTS.jsonl")
    with io.open(live, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    m.LIVE = live
    m.ARCHIVE = os.path.join(tmp, "archive")
    if hasattr(m, "PART_CAP"):
        m.PART_CAP = CAP
    old_argv, buf = sys.argv, io.StringIO()
    sys.argv = ["shard_prompt_archive.py"] + list(argv)
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(io.StringIO()):
            rc = m.main()
    finally:
        sys.argv = old_argv
    return rc, buf.getvalue()


def day_of(line):
    return json.loads(line)["ts"][:10]


def cases(m, base):
    r = {}
    # S1
    t = tempfile.mkdtemp(dir=base)
    oct_ = days("2026-10", 1, 20, 3)
    rc, out = run(m, t, oct_)
    got = files(os.path.join(t, "archive"))
    parts = [n for n in got if n.startswith("PROMPTS_2026-10.p")]
    ok = rc == 0 and "LOSSLESS       : True" in out and len(parts) >= 3 and "PROMPTS_2026-10.jsonl" not in got
    seen_days = []
    for n in parts:
        ls = [l for l in got[n].split("\n") if l]
        ds = sorted({day_of(l) for l in ls})
        seen_days.append(ds)
        ok = ok and (len(got[n].encode("utf-8")) <= CAP or len(ds) == 1)
    flat = [d for ds in seen_days for d in ds]
    ok = ok and len(flat) == len(set(flat)) and flat == sorted(flat)          # no day split across two parts
    rc2, out2 = run(m, t, oct_, "--check")
    ok = ok and rc2 == 0 and "invented=0" in out2
    r["S1"] = (ok, "S1 %d parts, day-bounded, under the cap, lossless, --check clean" % len(parts))
    # S2
    before = files(os.path.join(t, "archive"))
    rc, out = run(m, t, oct_ + days("2026-10", 21, 28, 3)[:0] + [rec("2026-10-%02d" % d, 900 + d * 5 + i)
                                                                     for d in range(21, 29) for i in range(3)])
    after = files(os.path.join(t, "archive"))
    closed = sorted(n for n in before if n.startswith("PROMPTS_2026-10.p"))[:-1]
    r["S2"] = (rc == 0 and closed and all(after.get(n) == before[n] for n in closed),
               "S2 %d closed parts unchanged after later days" % len(closed))
    # S3
    t = tempfile.mkdtemp(dir=base)
    small = days("2026-09", 1, 3, 2)
    run(m, t, small)
    had_one = "PROMPTS_2026-09.jsonl" in files(os.path.join(t, "archive"))
    rc, out = run(m, t, small + days("2026-09", 4, 25, 3))
    got = files(os.path.join(t, "archive"))
    r["S3"] = (had_one and rc == 0 and "PROMPTS_2026-09.jsonl" not in got and any(n.startswith("PROMPTS_2026-09.p") for n in got)
               and "LOSSLESS       : True" in out, "S3 the month's old single file is gone once its parts hold every line")
    # S4
    t = tempfile.mkdtemp(dir=base)
    run(m, t, small + ["not json at all"])
    had_undated = "PROMPTS_UNDATED.jsonl" in files(os.path.join(t, "archive"))
    rc, out = run(m, t, small)
    r["S4"] = (had_undated and rc == 0 and "PROMPTS_UNDATED.jsonl" not in files(os.path.join(t, "archive"))
               and "LOSSLESS       : True" in out, "S4 the leftover undated shard is removed")
    # S5
    t = tempfile.mkdtemp(dir=base)
    run(m, t, oct_)
    arch = os.path.join(t, "archive")
    last = sorted(n for n in files(arch) if n.startswith("PROMPTS_2026-10.p"))[-1:]
    extra = rec("2026-10-29", 4242)
    rc, out = run(m, t, [extra], "--union-existing")
    got = files(arch)
    r["S5"] = (bool(last) and rc == 0 and "PROMPTS_2026-10.jsonl" not in got and extra in got.get(last[0], "")
               and "LOSSLESS       : True" in out, "S5 union mode adds to the last part %s" % (last[0] if last else "-"))
    # S6
    t = tempfile.mkdtemp(dir=base)
    rc, out = run(m, t, days("2026-08", 1, 2, 2))
    got = files(os.path.join(t, "archive"))
    r["S6"] = (rc == 0 and list(got) == ["PROMPTS_2026-08.jsonl"], "S6 a small month keeps one file: %s" % list(got))
    return r


def main():
    base = tempfile.mkdtemp(prefix="shardparts_")
    try:
        fails = []
        r = cases(load(MOD, "spa_under_test"), base)
        for k in sorted(r):
            ok, what = r[k]
            print(("PASS  " if ok else "FAIL  ") + what)
            if not ok:
                fails.append(k)
        if OLD:
            ro = cases(load(OLD, "spa_old"), base)
            ok = not ro["S1"][0]
            print(("PASS  " if ok else "FAIL  ") + "control: the module before parts fails S1 (%s)" % ro["S1"][1])
            if not ok:
                fails.append("control")
        print("ALL PASS" if not fails else "FAILED: " + " ".join(fails))
        return 1 if fails else 0
    finally:
        shutil.rmtree(base, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
