"""rem_arm_order.py - which login should tonight's REM pass try first?

    python rem_arm_order.py            one arm per line for run_dream.ps1, lines starting with # are the reasons
    python rem_arm_order.py --selftest

Until 10 Nov 2026 the dream tried its arms in one fixed order: the main login on Fable, the main login on Opus, then
the pool. Of 37 REM results since 20 Oct, 15 were "You've hit your weekly limit": the dream learned that the main
login was spent by failing on it, and on three nights every Claude login was spent. This asks the pool for a live
usage reading of the main login (the one the open terminals use) and of the pool accounts before anything is
launched, and puts a login that has usage first. Codex comes last, or first when every Claude login reads spent.

Arms: a bare model runs on the main login; "pool:<model>" runs on the pool account with the most room;
"codex:<model>" runs rem_codex_arm.py. Exit 0 with arms printed; exit 3 when no reading could be had (the caller
keeps its fixed order).
"""
import importlib.util
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
try:
    # The dream starts this with `python -s`, which hides the user site, and psutil lives only there. Without it
    # the pool's usage governor raised on import and answered "governor unavailable" (allowed) for every account,
    # so a pool account at its weekly limit could still be picked (found 10 Nov 2026).
    import _usersite  # noqa: F401
except Exception:
    pass
POOL =os.path.join(os.path.expanduser("~"), "claude_pool", "claude_pool.py")
# Keep these equal to run_dream.ps1's fixed `$models = @(...)` line (the selftest checks it). From 10 to 14 Nov they
# still named Fable 5.1 and Opus 5 while run_dream.ps1 had moved to 5.2 and 5.5, and since this helper's order
# replaces the fixed one whenever it answers, every dream of those days ran on the older models.
FABLE = "claude-fable-5-2[1m]"
OPUS = "claude-opus-5-5[1m]"
RUN_DREAM = os.path.join(HERE, "run_dream.ps1")


def fixed_models():
    """The model ids in run_dream.ps1's fixed order, or None when the line is not found."""
    import re
    try:
        text = open(RUN_DREAM, encoding="utf-8", errors="replace").read()
    except OSError:
        return None
    m = re.search(r"^\s*\$models\s*=\s*@\(([^)]*)\)", text, re.M)
    return re.findall(r"'([^']+)'", m.group(1)) if m else None
CODEX = "codex:gpt-6.1-sol"
MAIN_TTL = 600


def spent(rec):
    """True when a reading exists and says the login is refused; None when there is no reading."""
    if not rec or not rec.get("ok"):
        return None
    return rec.get("status") == "rejected"


def order(main_rec, pool_name, have_pool, have_codex):
    """(arms, reason)."""
    main_spent = spent(main_rec)
    pool_arms = ["pool:" + FABLE, "pool:" + OPUS] if have_pool else []
    if main_spent is None:
        arms = [FABLE, OPUS] + pool_arms[1:]
        why = "no usage reading for the main login; fixed order"
    elif not main_spent:
        arms = [FABLE, OPUS] + pool_arms[1:]
        why = "the main login has usage (7d %s); it goes first" % pct(main_rec.get("u7"))
    elif pool_name:
        arms = pool_arms + [FABLE]
        why = "the main login is at its limit; pool account %s has room and goes first" % pool_name
    else:
        arms = [FABLE, OPUS] + pool_arms[1:]
        why = "every Claude login reads spent"
        if have_codex:
            arms = [CODEX] + arms
            why += "; Codex goes first"
    if have_codex and CODEX not in arms:
        arms.append(CODEX)
    return arms, why


def pct(u):
    return "?" if u is None else "%d%% used" % round(100 * float(u))


def load_pool():
    spec = importlib.util.spec_from_file_location("claude_pool", POOL)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read_usage():
    """(main_rec, pool_name, have_pool, notes)."""
    notes = []
    if not os.path.exists(POOL):
        return None, None, False, ["no claude_pool on this machine"]
    cp = load_pool()
    state = cp._read_json(cp._paths()["state"], {})
    main_rec = (state.get("probes", {}) or {}).get("main") or {}
    if time.time() - main_rec.get("at", 0) > MAIN_TTL:
        main_rec = cp.probe("main")
        cp._store_probes({"main": main_rec})
    notes.append("main: %s" % ("no reading (%s)" % str(main_rec.get("error"))[:120] if not main_rec.get("ok") else
                               "%s, 7d %s" % (main_rec.get("status"), pct(main_rec.get("u7")))))
    names = cp.signed_in()
    pool_name = None
    if names:
        pool_name, why = cp.pick_account("fail", record=False)
        notes.append("pool: %s (%s)" % (pool_name or "none free", str(why)[:160]))
        gov = governor_state(cp, names)
        if gov:
            notes.append(gov)
    else:
        notes.append("pool: no account signed in")
    return main_rec, pool_name, bool(names), notes


def governor_state(cp, names):
    """One line when the pool's usage governor does not answer here, '' when it does (or the pool has none)."""
    if not hasattr(cp, "governor_allows"):
        return ""
    try:
        ok, why = cp.governor_allows(names[0], None)
    except Exception as exc:
        return "governor: RAISED (%s) - the pool pick was not checked against the usage governor" % str(exc)[:100]
    if str(why).strip().lower() == "governor unavailable":
        return "governor: UNAVAILABLE in this interpreter - the pool pick was not checked against the usage governor"
    return ""


def selftest():
    fails = []
    n = [0]

    def check(name, cond, detail=""):
        n[0] += 1
        if not cond:
            fails.append(name + (" :: " + str(detail)[:200] if detail else ""))
        print(("ok   " if cond else "FAIL ") + name)

    ok = {"ok": True, "status": "allowed", "u7": 0.4}
    warn = {"ok": True, "status": "allowed_warning", "u7": 0.93}
    out = {"ok": True, "status": "rejected", "u7": 1}
    none = {"ok": False, "error": "the probe timed out"}
    a, w = order(ok, "claude2", True, True)
    check("main with usage goes first, Codex last", a[0] == FABLE and a[-1] == CODEX, a)
    a, w = order(warn, "claude2", True, True)
    check("a warning is still usage", a[0] == FABLE, a)
    a, w = order(out, "claude2", True, True)
    check("main spent and a pool account free: the pool goes first on Fable", a[0] == "pool:" + FABLE, a)
    check("  and the main login is still in the list in case the reading was wrong", FABLE in a, a)
    check("  and Codex is last", a[-1] == CODEX, a)
    a, w = order(out, None, True, True)
    check("every Claude login spent: Codex goes first", a[0] == CODEX, a)
    check("  and the Claude arms stay behind it", a[1:3] == [FABLE, OPUS], a)
    a, w = order(out, None, True, False)
    check("every Claude login spent and no Codex arm: the fixed order", a == [FABLE, OPUS, "pool:" + OPUS], a)
    a, w = order(none, "claude2", True, True)
    check("no reading: the fixed order with Codex last", a == [FABLE, OPUS, "pool:" + OPUS, CODEX], a)
    a, w = order({}, None, False, False)
    check("no pool, no Codex, no reading: the two main arms", a == [FABLE, OPUS], a)
    for case in ((ok, "claude2"), (out, "claude2"), (out, None), (none, None)):
        a, w = order(case[0], case[1], True, True)
        check("no arm is listed twice (%s, %s)" % (case[0].get("status"), case[1]), len(a) == len(set(a)), a)
    check("spent() is None without a reading", spent(none) is None and spent({}) is None)
    fm = fixed_models()
    check("the arms name the same models as run_dream.ps1's fixed order", fm is None or fm == [FABLE, OPUS], fm)

    class _Pool:
        def __init__(self, answer):
            self.answer = answer

        def governor_allows(self, name, fleet=None):
            if isinstance(self.answer, Exception):
                raise self.answer
            return self.answer

    check("a governor that answers leaves no note", governor_state(_Pool((False, "at its weekly limit")), ["a"]) == "")
    check("a governor that fails open is named", "UNAVAILABLE" in governor_state(_Pool((True, "governor unavailable")), ["a"]))
    check("a governor that raises is named", "RAISED" in governor_state(_Pool(RuntimeError("x")), ["a"]))
    check("a pool without a governor leaves no note", governor_state(object(), ["a"]) == "")
    usersite = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Python",
                            "Python%d%d" % sys.version_info[:2], "site-packages")
    if os.path.isdir(os.path.join(usersite, "psutil")):
        try:
            import psutil  # noqa: F401
            seen = True
        except Exception:
            seen = False
        check("psutil imports in this interpreter, also under python -s (the pool's governor needs it)", seen)
    if os.path.exists(POOL):
        try:
            cp = load_pool()
            names = cp.signed_in()
            live = governor_state(cp, names) if names else ""
        except Exception as exc:
            live = "could not load the pool: " + str(exc)[:120]
        check("the live pool's governor answers here", live == "", live)
    print("%s: %d checks, %d failed" % ("PASS" if not fails else "FAIL", n[0], len(fails)))
    for f in fails:
        print("  " + f)
    return 1 if fails else 0


def main():
    if sys.argv[1:] == ["--selftest"]:
        return selftest()
    have_codex = (os.path.exists(os.path.join(HERE, "rem_codex_arm.py"))
                  and os.path.exists(os.path.expandvars(r"%APPDATA%\npm\codex.cmd")))
    try:
        main_rec, pool_name, have_pool, notes = read_usage()
    except Exception as exc:
        print("# usage reading failed: " + str(exc)[:200])
        return 3
    for line in notes:
        print("# " + line)
    if main_rec is None:
        return 3
    arms, why = order(main_rec, pool_name, have_pool, have_codex)
    print("# " + why)
    for a in arms:
        print(a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
