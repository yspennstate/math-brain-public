"""Controls for instinct_prime._refill_after_backoff (28 Sep, an agent).

The cap takes the top MAX_FIRE ranked reflexes before the session backoff runs, so a reflex the backoff then silences
used to keep its slot empty while the next ranked reflexes stayed held by the cap. These controls pin the refill:

  1. a backed-off slot-holder is replaced by the next ranked reflex that is not in its own backoff
  2. a candidate that is itself in backoff is passed over, and ends up recorded 'backoff', not 'cap'
  3. a candidate the precision gate silences is passed over
  4. after a mention/prose filter (drop_act), an 'act' reflex is passed over unless it is never-mentioned
  5. nothing to refill: the list comes back unchanged
  6. INSTINCT_REFILL_BACKOFF=0 turns it off
  7. a malformed ranked list fails open (the fired list unchanged)
  8. the negative arm: without the refill, the scenario of control 1 shows one reflex where two were due

    python test_refill_after_backoff.py [PATH_TO_instinct_prime.py]   (default: the one beside this file)
"""
import importlib.util
import json
import os
import sys
import tempfile
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.abspath(sys.argv.pop(1)) if len(sys.argv) > 1 and sys.argv[1].endswith(".py") else \
    os.path.join(HERE, "instinct_prime.py")


def load():
    spec = importlib.util.spec_from_file_location("ip_under_test", TARGET)
    m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.dirname(TARGET))
    spec.loader.exec_module(m)
    return m


class Refill(unittest.TestCase):
    def setUp(self):
        self.ip = load()
        self.tmp = tempfile.mkdtemp()
        self.ip.STATE_DIR = self.tmp
        self.ip.REFILL_LOG = os.path.join(self.tmp, "refills.tsv")
        self.sess = "test-session-0001"
        self.ip._SUPPRESSED[:] = []
        self._gate = self.ip._gated_by_precision
        self.ip._gated_by_precision = lambda it, prec=None: False
        os.environ.pop("INSTINCT_REFILL_BACKOFF", None)

    def tearDown(self):
        self.ip._gated_by_precision = self._gate
        os.environ.pop("INSTINCT_REFILL_BACKOFF", None)

    def backed_off(self, *rids):
        st = {self.sess + "|" + r: [time.time(), 1] for r in rids}
        with open(os.path.join(self.tmp, self.sess + ".json"), "w", encoding="utf-8") as f:
            json.dump(st, f)

    def scenario(self, ranked, backed=()):
        """The hook's state after the cap and before the backoff: the top MAX_FIRE shown, the rest held by the cap."""
        self.backed_off(*backed)
        items = [{"id": r} for r in ranked]
        self.ip._LAST_RANKED[:] = items
        top = items[:self.ip.MAX_FIRE]
        for it in items[self.ip.MAX_FIRE:]:
            self.ip._suppress(it["id"], "cap")
        fired = self.ip._dedup(self.sess, [dict(it) for it in top])
        return fired

    def ids(self, fired):
        return [it["id"] for it in fired]

    def test_1_backed_off_slot_is_refilled(self):
        fired = self.scenario(["B", "A", "C", "D"], backed=("A",))
        self.assertEqual(self.ids(fired), ["B"])
        out = self.ip._refill_after_backoff(self.sess, fired)
        self.assertEqual(self.ids(out), ["B", "C"])
        self.assertNotIn(("C", "cap"), self.ip._SUPPRESSED)
        self.assertIn(("D", "cap"), self.ip._SUPPRESSED)
        with open(os.path.join(self.tmp, self.sess + ".json"), encoding="utf-8") as f:
            self.assertIn(self.sess + "|C", json.load(f))
        with open(self.ip.REFILL_LOG, encoding="utf-8") as f:
            self.assertEqual(f.read().split("\t")[2], "C")

    def test_2_candidate_in_backoff_is_passed_over(self):
        fired = self.scenario(["B", "A", "C", "D"], backed=("A", "C"))
        out = self.ip._refill_after_backoff(self.sess, fired)
        self.assertEqual(self.ids(out), ["B", "D"])
        self.assertNotIn(("C", "cap"), self.ip._SUPPRESSED)
        self.assertIn(("C", "backoff"), self.ip._SUPPRESSED)

    def test_3_precision_gated_candidate_is_passed_over(self):
        fired = self.scenario(["B", "A", "C", "D"], backed=("A",))
        self.ip._gated_by_precision = lambda it, prec=None: it.get("id") == "C"
        out = self.ip._refill_after_backoff(self.sess, fired)
        self.assertEqual(self.ids(out), ["B", "D"])

    def test_4_act_candidate_skipped_after_a_mention_filter(self):
        fired = self.scenario(["B", "A", "C", "D"], backed=("A",))
        stub = type(sys)("habituation_filter")
        stub.danger_surface = lambda rid: "act" if rid == "C" else "claim"
        sys.modules["habituation_filter"] = stub
        try:
            out = self.ip._refill_after_backoff(self.sess, fired, drop_act=True)
        finally:
            sys.modules.pop("habituation_filter", None)
        self.assertEqual(self.ids(out), ["B", "D"])

    def test_5_nothing_to_refill(self):
        fired = self.scenario(["B", "A"], backed=("A",))
        out = self.ip._refill_after_backoff(self.sess, fired)
        self.assertEqual(self.ids(out), ["B"])

    def test_6_switch_off(self):
        fired = self.scenario(["B", "A", "C"], backed=("A",))
        os.environ["INSTINCT_REFILL_BACKOFF"] = "0"
        out = self.ip._refill_after_backoff(self.sess, fired)
        self.assertEqual(self.ids(out), ["B"])

    def test_7_fails_open(self):
        fired = self.scenario(["B", "A", "C"], backed=("A",))
        self.ip._LAST_RANKED[:] = [None, 42]
        out = self.ip._refill_after_backoff(self.sess, fired)
        self.assertEqual(self.ids(out), ["B"])

    def test_8_negative_arm_without_the_refill(self):
        fired = self.scenario(["B", "A", "C", "D"], backed=("A",))
        self.assertEqual(len(fired), 1)           # what the hook showed before 28 Sep: one where two were due
        self.assertIn(("C", "cap"), self.ip._SUPPRESSED)

    # --- the refill A/B (registered 28 Sep 03:39): four reflexes shown or held per (session, reflex) ---
    AB = "mesh_claim_never_chained_with_mutate"

    def session_for(self, rid, arm):
        for i in range(10000):
            s = "ab-session-%d" % i
            if self.ip._refill_arm(s, rid) == arm:
                return s
        self.fail("no session maps to %s" % arm)

    def log_rows(self):
        with open(self.ip.REFILL_LOG, encoding="utf-8") as f:
            return [l.rstrip("\n").split("\t") for l in f if l.strip()]

    def test_9_held_arm_is_not_shown_and_is_logged(self):
        self.sess = self.session_for(self.AB, "held")
        fired = self.scenario(["B", "A", self.AB, "D"], backed=("A",))
        out = self.ip._refill_after_backoff(self.sess, fired)
        self.assertEqual(self.ids(out), ["B", "D"])                   # the next candidate takes the slot
        self.assertIn([self.AB, "held"], [[r[2], r[4]] for r in self.log_rows()])
        with open(os.path.join(self.tmp, self.sess + ".json"), encoding="utf-8") as f:
            self.assertNotIn(self.sess + "|" + self.AB, json.load(f))  # not entered in the backoff
        self.assertIn((self.AB, "ab_held"), self.ip._SUPPRESSED)
        self.assertNotIn((self.AB, "cap"), self.ip._SUPPRESSED)

    def test_10_shown_arm_is_shown_and_logged(self):
        self.sess = self.session_for(self.AB, "shown")
        fired = self.scenario(["B", "A", self.AB, "D"], backed=("A",))
        out = self.ip._refill_after_backoff(self.sess, fired)
        self.assertEqual(self.ids(out), ["B", self.AB])
        self.assertIn([self.AB, "shown"], [[r[2], r[4]] for r in self.log_rows()])

    def test_11_other_reflexes_are_open(self):
        fired = self.scenario(["B", "A", "C", "D"], backed=("A",))
        self.ip._refill_after_backoff(self.sess, fired)
        self.assertEqual([[r[2], r[4]] for r in self.log_rows()], [["C", "open"]])

    def test_12_switch_shows_every_refill(self):
        self.sess = self.session_for(self.AB, "held")
        os.environ["INSTINCT_REFILL_AB"] = "0"
        try:
            fired = self.scenario(["B", "A", self.AB, "D"], backed=("A",))
            out = self.ip._refill_after_backoff(self.sess, fired)
        finally:
            os.environ.pop("INSTINCT_REFILL_AB", None)
        self.assertEqual(self.ids(out), ["B", self.AB])
        self.assertIn([self.AB, "open"], [[r[2], r[4]] for r in self.log_rows()])

    def test_13_held_in_backoff_is_not_an_event(self):
        self.sess = self.session_for(self.AB, "held")
        fired = self.scenario(["B", "A", self.AB, "D"], backed=("A", self.AB))
        out = self.ip._refill_after_backoff(self.sess, fired)
        self.assertEqual(self.ids(out), ["B", "D"])
        rows = self.log_rows() if os.path.exists(self.ip.REFILL_LOG) else []
        self.assertNotIn(self.AB, [r[2] for r in rows])               # cut the same way as a shown arm
        self.assertIn((self.AB, "backoff"), self.ip._SUPPRESSED)
        # not an A/B opportunity: never 'ab_held', and its 'cap' is gone (29 Sep, account01/B04, B04-F203)
        self.assertNotIn((self.AB, "ab_held"), self.ip._SUPPRESSED)
        self.assertNotIn((self.AB, "cap"), self.ip._SUPPRESSED)

    def test_15_refill_row_carries_the_call_time_and_opportunity(self):
        fired = self.scenario(["B", "A", "C", "D"], backed=("A",))
        self.ip._refill_after_backoff(self.sess, fired)
        row = self.log_rows()[0]
        self.assertEqual(len(row), 6)
        self.assertEqual(row[0], self.ip._T0_S)
        self.assertEqual(row[5], self.ip.opportunity_id(self.ip._CALL_ID, "C"))

    def test_16_two_calls_have_two_ids(self):
        other = load()
        self.assertNotEqual(other._CALL_ID, self.ip._CALL_ID)
        self.assertNotEqual(other.opportunity_id(other._CALL_ID, "C"), self.ip.opportunity_id(self.ip._CALL_ID, "C"))

    def test_17_fire_row_joins_its_refill(self):
        self.ip.FIRELOG = os.path.join(self.tmp, "fires.tsv")
        data = {"session_id": "0123abcd-0000-4000-8000-000000000000", "tool_name": "Bash",
                "tool_input": {"command": "echo hi"}}
        self.assertTrue(self.ip._log_fires("PreToolUse", data, [{"id": "C", "_via": "regex"}]))
        with open(self.ip.FIRELOG, encoding="utf-8") as f:
            row = f.readline().rstrip("\n").split("\t")
        self.assertEqual(row[0], self.ip._T0_S)
        self.assertEqual(self.ip.opportunity_id(row[7], row[3]), self.ip.opportunity_id(self.ip._CALL_ID, "C"))

    def test_14_assignment_is_fixed_and_balanced(self):
        for rid in self.ip.REFILL_AB:
            arms = [self.ip._refill_arm("s%d" % i, rid) for i in range(4000)]
            share = arms.count("held") / 4000.0
            self.assertTrue(0.45 < share < 0.55, (rid, share))
            self.assertEqual(arms[:50], [self.ip._refill_arm("s%d" % i, rid) for i in range(50)])
        self.assertEqual(self.ip._refill_arm("s1", "windowless"), "open")


if __name__ == "__main__":
    print("testing", TARGET)
    unittest.main(verbosity=1)
