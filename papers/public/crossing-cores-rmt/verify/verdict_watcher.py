"""Poll the sweep's checkpoint and announce the verdict the moment it is
certified, without waiting for the sweep to finish.

Every reduced core with at least four pairs has volume at most 9/20
(Theorem 9.1), so at any moment

    S_done  <=  kappa_8^T  <=  S_done + (9/20) * W_remaining.

The order-sixteen free conditional-positivity test passes as soon as the
LOWER bound alone puts m_16 above the Schur threshold, which happens well
before the sweep completes.  This writes one line per poll to
verdict_watch.log and stops as soon as the verdict is certified either
way (or the sweep finishes).

Run:  python -u verdict_watcher.py [poll_seconds]
"""
import json, os, sys, time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "verdict_watch.log")
CAP = Fr(9, 20)
KNOWN = Fr(29362422, 105)
THRESH = Fr(3863516832738344459, 10908088231950)
TARGET = Fr(687080, 9)

def snapshot():
    with open(os.path.join(HERE, "kappa8_orbits_T.json"), encoding="utf-8") as f:
        meta = json.load(f)
    orbits, wtot = meta["orbits"], meta["n_words"]
    with open(os.path.join(HERE, "kappa8_volumes_T.json"), encoding="utf-8") as f:
        vols = json.load(f)
    S = Fr(0)
    wdone = 0
    for k, v in vols.items():
        s = orbits.get(k)
        if s is None:
            continue
        S += Fr(v) * s
        wdone += s
    return S, wdone, wtot, len(vols), len(orbits)

def say(msg):
    line = f"{time.strftime('%H:%M:%S')}  {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def main():
    poll = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    say("watcher armed")
    while True:
        try:
            S, wdone, wtot, ndone, ntot = snapshot()
        except Exception as e:
            say(f"read failed ({e}); retrying")
            time.sleep(poll)
            continue
        lo, hi = S, S + CAP * (wtot - wdone)
        m_lo, m_hi = KNOWN + lo, KNOWN + hi
        pct = 100.0 * wdone / wtot
        if m_lo >= THRESH:
            say(f"CERTIFIED at {pct:.1f}% coverage: m_16 >= {float(m_lo):.2f} "
                f"exceeds the threshold {float(THRESH):.2f} - the order-16 "
                f"free conditional-positivity test PASSES.")
            break
        if m_hi < THRESH:
            say(f"CERTIFIED at {pct:.1f}% coverage: m_16 <= {float(m_hi):.2f} "
                f"is below {float(THRESH):.2f} - gamma_T is NOT freely "
                f"infinitely divisible.")
            break
        if ndone >= ntot:
            kappa = S
            say(f"sweep complete: kappa_8^T = {kappa}; extension implied "
                f"{TARGET}; {'MATCH' if kappa == TARGET else 'MISMATCH'}")
            break
        need = THRESH - KNOWN - S
        say(f"{ndone}/{ntot} orbits ({pct:.1f}%): kappa_8 in "
            f"[{float(lo):.0f}, {float(hi):.0f}]; needs {float(need):.0f} more "
            f"to certify")
        time.sleep(poll)

if __name__ == "__main__":
    main()
