"""The reflex primary show-or-hold trial (owner, 6 Oct 2026 13:3x local time): controls, both ways, in a sandbox.
Run: python test_primary_ab.py"""
import importlib.util
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ip_primary_ab_test", os.path.join(HERE, "instinct_prime.py"))
ip = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ip)

LIVE = os.path.join(HERE, "instinct_primary_ab.tsv")
live_size = os.path.getsize(LIVE) if os.path.exists(LIVE) else -1
tmp = tempfile.mkdtemp()
ip.REFILL_LOG = os.path.join(tmp, "refills.tsv")      # the primary log follows REFILL_LOG's directory
ip.PRIMARY_AB_LOG = None
SANDBOX = os.path.join(tmp, "instinct_primary_ab.tsv")
os.environ.pop("INSTINCT_PRIMARY_AB", None)
PLAIN, OTHER = "a_plain_reflex_for_the_test", "another_plain_reflex_for_the_test"
ip._ELIGIBLE[0] = {PLAIN, OTHER, "a_scheduled_task_made_by_schtasks_will_not_start_on_battery", "secrets_in_git",
                   "owner_law_brain_data_is_never_deleted", "windowless"}

fails = 0


def check(cond, what):
    global fails
    print(("PASS  " if cond else "FAIL  ") + what)
    fails += 0 if cond else 1


sessions = ["test-primary-%04d" % i for i in range(400)]
arms = [ip._primary_arm(s, PLAIN) for s in sessions]
held = arms.count("held")
check(70 <= held <= 130 and arms.count("shown") == 400 - held, "about one in four held (%d of 400)" % held)
check(all(ip._primary_arm(s, PLAIN) == a for s, a in zip(sessions, arms)), "the arm is fixed for a (session, reflex)")
pairs = set((ip._primary_arm(s, PLAIN), ip._primary_arm(s, OTHER)) for s in sessions)
check(("held", "shown") in pairs and ("shown", "held") in pairs, "two reflexes in one session get independent arms")

for rid in ("owner_law_brain_data_is_never_deleted", "secrets_in_git", "windowless", "the_trading_box_runs_no_research",
            "a_push_to_vanilla_brain_is_one_a_day"):
    check(all(ip._primary_arm(s, rid) == "open" for s in sessions), "never held, never logged: " + rid)
check(all(ip._primary_arm(s, "a_scheduled_task_made_by_schtasks_will_not_start_on_battery") != "open" for s in sessions),
      "a schedule reflex is in the trial (the 'edu' substring no longer excludes it)")
check(all(ip._primary_arm(s, r) == "open" for s in sessions for r in ip.REFILL_AB), "the refill trial's four stay open")
check(ip._primary_arm("", PLAIN) == "open", "no session: open")
check(all(ip._primary_arm(s, "a_reflex_not_on_the_list") == "open" for s in sessions),
      "a reflex not on the frozen allowlist is never held")
live = ip.PRIMARY_ELIGIBLE
check(os.path.exists(live) and "owner_law_brain_data_is_never_deleted" not in open(live, encoding="utf-8").read(),
      "the live allowlist exists and holds none of his laws")
os.environ["INSTINCT_PRIMARY_AB"] = "0"
check(all(ip._primary_arm(s, PLAIN) == "open" for s in sessions), "INSTINCT_PRIMARY_AB=0 shows all")
os.environ.pop("INSTINCT_PRIMARY_AB", None)

# the split keeps every reflex, logs only trial reflexes, in both arms, and writes to the sandbox
rows_expected = 0
ok_split = True
for s in sessions[:40]:
    fired = [{"id": PLAIN, "charge": "0.5"}, {"id": "secrets_in_git", "charge": "0.5"}]   # the gate reads the live charge
    shown, held_l = ip._primary_ab(s, fired)
    ok_split &= (len(shown) + len(held_l) == 2 and any(it["id"] == "secrets_in_git" for it in shown)
                 and all(it["id"] == PLAIN for it in held_l))
    rows_expected += 1
check(ok_split, "the split keeps both reflexes; a never-hold reflex is always shown")
rows = open(SANDBOX, encoding="utf-8").read().splitlines() if os.path.exists(SANDBOX) else []
check(len(rows) == rows_expected and all(r.split("\t")[2] == PLAIN for r in rows),
      "one row per trial reflex per call, none for the never-hold one (%d rows)" % len(rows))
arms_logged = set(r.split("\t")[3] for r in rows)
check(arms_logged <= {"held", "shown"} and len(arms_logged) == 2, "both arms are logged: %s" % sorted(arms_logged))
# Round 4 (dot D7CB6565's source review): both defect paths, in a sandbox backoff directory, with forced arms.
ip.STATE_DIR = os.path.join(tmp, "state")
os.makedirs(ip.STATE_DIR, exist_ok=True)
real_arm = ip._primary_arm
ip._ELIGIBLE[0] = {"refill_only_reflex", "held_one"}
item = lambda rid: {"id": rid, "mode": "fire", "charge": "0.5", "gut": "g", "sting": "s"}


def state(sess):
    p = os.path.join(ip.STATE_DIR, sess + ".json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}


# P1-2: an eligible reflex that arrives ONLY through the refill, with its arm forced to held
ip._primary_arm = lambda s, r: "held" if r == "refill_only_reflex" else real_arm(s, r)
ip._SUPPRESSED[:] = []
ip._LAST_RANKED[:] = [item("refill_only_reflex")]
ip._DEFER_BACKOFF[0] = True
shown2, held2 = ip._split_and_render("sessR", [], False)
check(not any(i["id"] == "refill_only_reflex" for i in shown2) and any(i["id"] == "refill_only_reflex" for i in held2),
      "a reflex added by the refill goes through the primary split: held, not shown")
rows = open(SANDBOX, encoding="utf-8").read().splitlines()
check(any(r.split("\t")[1:4:2] == ["sessR", "held"] and r.split("\t")[2] == "refill_only_reflex" for r in rows),
      "the refilled reflex has a held assignment row")
ip._discard_backoff()

# P1-1: one eligible reflex, no refill candidates, each arm forced; the held arm renders nothing
ip._LAST_RANKED[:] = []
for arm_forced, sess in (("held", "sessH"), ("shown", "sessS")):
    ip._primary_arm = lambda s, r, a=arm_forced: a if r == "held_one" else real_arm(s, r)
    ip._DEFER_BACKOFF[0] = True
    shown3, held3 = ip._split_and_render(sess, [item("held_one")], False)
    if arm_forced == "held":
        check(not shown3 and len(held3) == 1, "forced held: nothing to render, one held")
        ip._settle_backoff_when_silent(held3)          # the silent branch of main
    else:
        check(len(shown3) == 1 and not held3, "forced shown: one to render")
        ip._commit_backoff()                           # main commits after the output
    check((sess + "|held_one") in state(sess), "%s arm: the reflex entered the backoff" % arm_forced)
    ip._DEFER_BACKOFF[0] = False
    check(ip._dedup(sess, [item("held_one")]) == [], "%s arm: a repeat inside the window is suppressed" % arm_forced)
# negative control: the old silent branch (discard) leaves no backoff, so the test above can fail
ip._primary_arm = lambda s, r: "held" if r == "held_one" else real_arm(s, r)
ip._DEFER_BACKOFF[0] = True
_s, held4 = ip._split_and_render("sessOld", [item("held_one")], False)
ip._discard_backoff()
check(("sessOld|held_one") not in state("sessOld"), "negative control: the old discard left no backoff")
ip._primary_arm = real_arm

# P1-4: the live charge and the route are part of the gate
check(not ip._primary_item_eligible(dict(item("held_one"), charge="1.0")), "a listed id with charge raised to 1.0 is shown")
check(not ip._primary_item_eligible(dict(item("held_one"), _via="graph")), "a listed id fired by the graph route is shown")
check(not ip._primary_item_eligible(dict(item("held_one"), _via="ff")), "a listed id fired by forward-feed is shown")
check(ip._primary_item_eligible(item("held_one")), "a listed id at charge 0.5 by its own trigger is eligible")
ip._primary_arm = lambda s, r: "held"
sh5, he5 = ip._primary_ab("sessG", [dict(item("held_one"), _via="graph")])
check(len(sh5) == 1 and not he5, "a graph-route fire of a listed id is never held even when its arm says held")
ip._primary_arm = real_arm

# round 6, C: a held-only call whose backoff write fails reports the failure, as the shown path does
real_wb = ip._write_backoff
ip._write_backoff = lambda *a, **k: False
ip._primary_arm = lambda s, r: "held" if r == "held_one" else real_arm(s, r)
ip._DEFER_BACKOFF[0] = True
_s6, held6 = ip._split_and_render("sessFail", [item("held_one")], False)
check(ip._settle_backoff_when_silent(held6) == ["backoff"], "C: a failed held-only backoff write is returned as a failure")
ip._write_backoff, ip._primary_arm = real_wb, real_arm
src = open(ip.__file__, encoding="utf-8").read()
check("_sf = _settle_backoff_when_silent(_held_primary)" in src and "_note_emit_failure(_sf," in src,
      "C: main records that failure")

now_size = os.path.getsize(LIVE) if os.path.exists(LIVE) else -1
check(now_size == live_size, "the live instinct_primary_ab.tsv was not written by this test")

print(("PASS" if not fails else "FAIL") + " - primary A/B controls, %d failed" % fails)
sys.exit(1 if fails else 0)
