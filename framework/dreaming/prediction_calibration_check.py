#!/usr/bin/env python3
"""prediction_calibration_check.py - tell a bet what its own track record is.

WHY. Measured 2026-08-17 over 140 scored bets in PREDICTIONS.md, the brain's overconfidence is not
general. It is concentrated in OWNER-scope bets BELOW p=0.70:

    scope    band          n   stated  actual     gap
    owner    <0.50         7    0.429   0.000   -0.429
    owner    0.50-0.60    20    0.528   0.400   -0.128
    owner    0.60-0.70    11    0.618   0.364   -0.255
    owner    >=0.70       12    0.717   0.750   +0.033
    infra    0.50-0.60    22    0.536   0.545   +0.009
    infra    0.60-0.70    14    0.607   0.500   -0.107
    infra    >=0.70       13    0.758   0.769   +0.012
    result   all bands    37    0.541   0.514   -0.027

When the brain is CONFIDENT about the author it is right. When it HEDGES about him it is close to
fantasising, and seven sub-0.50 owner bets went 0 for 7.

WHY A LINTER AND NOT A PLACEMENT HOOK. There is no code path that writes a bet. foresight.py only
READS the ledger; dream.py only mentions it inside a prompt telling the dreaming model to edit the
file; the scripts that have actually appended bets are one-off dream scratch files. The author is a
MODEL following prose, so the two things that can work are (a) this linter, run over open bets, and
(b) putting the table above into the instructions the bet-writer reads. A placement-time guard has
no host to live in.

FIRE WHEN   scope is owner and p < 0.70          (every sub-band measured at gap <= -0.128)
DO NOT FIRE scope is owner and p >= 0.70          (measured +0.033, the best-calibrated cell)
DO NOT FIRE scope is infra at any band            (overall +0.009)
DO NOT FIRE scope is result at any band           (overall -0.027, inside noise for n=37)
DO NOT FIRE a cell with fewer than MIN_N resolved bets - an unmeasured cell gets UNKNOWN, never a
            warning invented from a neighbouring cell.

Recomputes the table from the live ledger every run rather than trusting the constants above, so it
cannot keep warning from a record that has since changed. Usage:
    python prediction_calibration_check.py                 lint the OPEN bets
    python prediction_calibration_check.py --table         print the current calibration table
    python prediction_calibration_check.py --selftest      controls
Read-only.
"""
from __future__ import annotations

import io
import os
import re
import sys
from collections import defaultdict

LEDGER = os.path.join(os.path.expanduser("~"), ".claude", "projects", os.environ.get("BRAIN_SLUG", "default"),
                      "memory", "PREDICTIONS.md")

# BOTH resolution vocabularies. The ledger uses outcome:hit and also "RESOLVED HIT"; reading only
# the first silently drops entries, which is how a calibration loses part of its own denominator.
VALID = re.compile(r"\boutcome:\s*(hit|miss|void)\b", re.I)
ALT = re.compile(r"\bRESOLVED\s+(HIT|MISS|VOID|YES|NO)\b", re.I)
P_RE = re.compile(r"\bp:\s*([0-9.]+)")
P_EQ_RE = re.compile(r"^- \[[ xX]\]\s*p=([0-9.]+)")          # "- [x] p=0.7 [infra] ..." (no bet id)
SCOPE_RE = re.compile(r"\bscope:\s*([A-Za-z_]+)")
SCOPE_BR_RE = re.compile(r"^- \[[ xX]\]\s*p=[0-9.]+\s*\[([A-Za-z_]+)\]")
ID_RE = re.compile(r"- \[[ xX]\]\s*(p[A-Za-z0-9_-]+)")       # p52, pL1, pRW3, p17x-sws0819; not "p=0.7"
# A resolution written apart from its bet (13 Nov fix, an agent): "- [x] p228 RESOLVED MISS ...",
# "- [x] p209 resolved YES ...", "- p226 -> MISS (p=0.60) ...". Before the fix these bets read as
# RESOLVED BUT UNSCOREABLE, and so did outcomes on the indented lines under a bet; 20 bets fell out.
SEP_RES_RE = re.compile(r"^\s*-\s*(?:\[[xX]\]\s*)?(p[A-Za-z0-9_-]+)[^|]*?(?:\bRESOLVED\s+|->\s*)"
                        r"(HIT|MISS|VOID|YES|NO)\b", re.I)
_NORM = {"yes": "hit", "no": "miss"}


def _outcome(text):
    m = VALID.search(text) or ALT.search(text)
    if not m:
        return None
    lab = m.group(1).lower()
    return _NORM.get(lab, lab)

BANDS = [(0.0, 0.50, "<0.50"), (0.50, 0.60, "0.50-0.60"),
         (0.60, 0.70, "0.60-0.70"), (0.70, 1.01, ">=0.70")]
MIN_N = 8          # below this a cell is UNKNOWN, not a verdict
GAP_WARN = -0.10   # stated minus actual worse than this is worth saying out loud


def band_of(p):
    for lo, hi, name in BANDS:
        if lo <= p < hi:
            return name
    return "?"


def parse(path=LEDGER, lines=None):
    """Return (scored, open_bets, unscoreable).

    A bet is its checkbox line plus the indented lines under it. Its outcome is the one on the
    checkbox line; else the last one on its indented lines; else a resolution line written
    elsewhere in the ledger under the same bet id. A checked line with no stated p whose id is
    a bet's id is that bet's resolution, not a bet of its own.
    """
    if lines is None:
        lines = io.open(path, encoding="utf-8", errors="replace").read().splitlines()
    # 1. group each checkbox bullet with its indented continuation lines
    entries, cur = [], None
    for line in lines:
        if line.startswith("- ["):
            cur = [line, []]
            entries.append(cur)
        elif cur is not None and line[:1] in (" ", "\t") and line.strip():
            cur[1].append(line)
        elif line.strip():
            cur = None                           # a heading or paragraph ends the bet
    # 2. resolutions written apart from the bet, keyed by bet id (first one wins)
    sep = {}
    for line in lines:
        m = SEP_RES_RE.match(line)
        if m and not P_RE.search(line):
            lab = m.group(2).lower()
            sep.setdefault(m.group(1), _NORM.get(lab, lab))
    bet_ids = set()
    for head, _ in entries:
        mid = ID_RE.match(head)
        if mid and (P_RE.search(head) or P_EQ_RE.match(head)):
            bet_ids.add(mid.group(1))
    scored, open_bets, unscoreable = [], [], []
    for head, cont in entries:
        checked = head.startswith("- [x]") or head.startswith("- [X]")
        mp = P_RE.search(head) or P_EQ_RE.match(head)
        ms = SCOPE_RE.search(head) or SCOPE_BR_RE.match(head)
        mid = ID_RE.match(head)
        rec = {"id": mid.group(1) if mid else "?",
               "p": float(mp.group(1)) if mp else None,
               "scope": (ms.group(1).lower() if ms else "UNKNOWN")}
        if rec["p"] is None and rec["id"] in bet_ids:
            continue                             # the resolution line of a bet counted elsewhere
        lab = _outcome(head)
        if lab is None:
            for c in reversed(cont):
                lab = _outcome(c)
                if lab:
                    break
        if lab is None and checked:
            lab = sep.get(rec["id"])
        if checked:
            if lab in ("hit", "miss") and rec["p"] is not None:
                scored.append((rec, 1 if lab == "hit" else 0))
            elif lab == "void":
                pass
            else:
                unscoreable.append(rec)          # resolved but not machine-readable
        elif rec["p"] is not None:
            open_bets.append(rec)
    return scored, open_bets, unscoreable


def table(scored):
    cells = defaultdict(list)
    for rec, y in scored:
        cells[(rec["scope"], band_of(rec["p"]))].append((rec["p"], y))
    out = {}
    for key, v in cells.items():
        mp = sum(p for p, _ in v) / len(v)
        hr = sum(y for _, y in v) / len(v)
        out[key] = {"n": len(v), "stated": mp, "actual": hr, "gap": hr - mp}
    return out


def verdict(cell):
    if cell is None or cell["n"] < MIN_N:
        return "UNKNOWN", ("no measured track record for this scope and confidence band "
                           "(fewer than %d resolved bets) - not a warning, an absence" % MIN_N)
    if cell["gap"] <= GAP_WARN:
        return "OVERCONFIDENT", ("this cell states %.3f and lands %.3f over %d resolved bets "
                                 "(gap %+.3f)" % (cell["stated"], cell["actual"],
                                                  cell["n"], cell["gap"]))
    return "OK", ("stated %.3f against %.3f over %d resolved bets (gap %+.3f)"
                  % (cell["stated"], cell["actual"], cell["n"], cell["gap"]))


def main():
    args = sys.argv[1:]
    if "--selftest" in args:
        return selftest()
    scored, open_bets, unscoreable = parse()
    t = table(scored)

    if "--table" in args:
        print("%-10s %-11s %5s %8s %8s %8s" % ("scope", "band", "n", "stated", "actual", "gap"))
        for (sc, bd), c in sorted(t.items()):
            print("%-10s %-11s %5d %8.3f %8.3f %+8.3f" % (sc, bd, c["n"], c["stated"],
                                                          c["actual"], c["gap"]))
        return 0

    print("scored bets %d | open bets %d | RESOLVED BUT UNSCOREABLE %d"
          % (len(scored), len(open_bets), len(unscoreable)))
    if unscoreable:
        print("  UNKNOWN outcomes (excluded from every calibration, kept visible here): %s"
              % ", ".join(r["id"] for r in unscoreable))
    print()
    warned = 0
    for rec in sorted(open_bets, key=lambda r: r["id"]):
        v, why = verdict(t.get((rec["scope"], band_of(rec["p"]))))
        if v == "OK":
            continue
        warned += 1
        print("  %-6s scope=%-7s p=%.2f  %s" % (rec["id"], rec["scope"], rec["p"], v))
        print("         %s" % why)
    if not warned:
        print("  no open bet sits in a cell measured as overconfident.")
    return 0


def selftest():
    """Controls on fixed fixtures (the live ledger drifts: the first version asserted that the live
    owner cells were overconfident, and it failed once they recalibrated - a test of the data,
    not of the code)."""
    def cell_bets(scope, p, n, hits):
        return [({"id": "f", "p": p, "scope": scope}, 1 if i < hits else 0) for i in range(n)]
    scored = (cell_bets("owner", 0.65, 20, 9) + cell_bets("owner", 0.55, 20, 8)
              + cell_bets("owner", 0.75, 20, 15) + cell_bets("infra", 0.55, 20, 10)
              + cell_bets("infra", 0.75, 20, 16) + cell_bets("result", 0.55, 5, 0))
    t = table(scored)
    fails = []

    print("PARSER CONTROLS - outcomes written apart from the bet line:")
    fx = ["- [x] p1 | scope:owner | p:0.6 | by:x | bet | outcome:hit | on:x",
          "- [x] p2 | scope:infra | p:0.7 | by:x | bet",
          "  - interim note, NOT resolving",
          "  - outcome: miss (SWS): measured",
          "- [x] p3 | scope:result | p:0.5 | by:x | bet",
          "## REM",
          "- [x] p3 RESOLVED HIT 09-21: the bet said ...",
          "- [x] p4 | scope:owner | p:0.55 | by:x | bet",
          "- p4 -> MISS (p=0.55). his lines ...",
          "- [x] p=0.7 [infra] by:x bet | outcome:hit | on:x",
          "- [x] p5 | scope:owner | p:0.6 | by:x | bet with no outcome anywhere",
          "- [x] p6 | scope:owner | p:0.6 | by:x | bet",
          "",
          "Paragraph text that is not under the bet: outcome: hit",
          "- [ ] p7 | scope:owner | p:0.6 | by:x | open bet"]
    s, o, u = parse(lines=fx)
    got = {(r["id"], r["scope"]): y for r, y in s}
    want = {("p1", "owner"): 1, ("p2", "infra"): 0, ("p3", "result"): 1, ("p4", "owner"): 0,
            ("?", "infra"): 1}
    for k, v in sorted(want.items()):
        ok = got.get(k) == v
        if not ok:
            fails.append("parse %s" % (k,))
        print("  %-5s %-34s -> %s" % ("PASS" if ok else "FAIL", "%s scored %s" % (k[0], v), got.get(k)))
    ok = sorted(r["id"] for r in u) == ["p5", "p6"] and [r["id"] for r in o] == ["p7"] and len(s) == 5
    if not ok:
        fails.append("parse unscoreable/open")
    print("  %-5s %-34s -> unscoreable %s, open %s, scored %d" % (
        "PASS" if ok else "FAIL", "p5,p6 unscoreable; p7 open", [r["id"] for r in u],
        [r["id"] for r in o], len(s)))
    print()

    def show(label, key, expect):
        cell = t.get(key)
        v, why = verdict(cell)
        ok = (v == expect)
        if not ok:
            fails.append(label)
        print("  %-5s %-34s -> %-14s (%s)" % ("PASS" if ok else "FAIL", label, v, why[:70]))

    print("POSITIVE CONTROL - must fire:")
    show("owner p=0.65", ("owner", "0.60-0.70"), "OVERCONFIDENT")
    show("owner p=0.55", ("owner", "0.50-0.60"), "OVERCONFIDENT")
    print()
    print("NEGATIVE CONTROLS - must stay silent:")
    show("owner p=0.75 (best cell)", ("owner", ">=0.70"), "OK")
    show("infra p=0.55", ("infra", "0.50-0.60"), "OK")
    show("infra p=0.75", ("infra", ">=0.70"), "OK")
    print()
    print("UNKNOWN CONTROL - an unmeasured cell must not invent a verdict:")
    show("scope=nonsense p=0.55", ("nonsense", "0.50-0.60"), "UNKNOWN")
    show("result p=0.55, n=5 < MIN_N", ("result", "0.50-0.60"), "UNKNOWN")
    print()
    ls, lo, lu = parse()
    print("LIVE LEDGER (reported, not tested): scored %d, open %d, unscoreable %d"
          % (len(ls), len(lo), len(lu)))
    print()
    if fails:
        print("SELFTEST FAILED: %s" % ", ".join(fails))
        return 1
    print("SELFTEST PASSED - fires on the measured cells, silent on the calibrated ones, UNKNOWN")
    print("where there is no record.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
