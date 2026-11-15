"""test_math_vouch_seal.py - a block the vouch route opens goes out only if it still leads with the card the word and meaning
channels agreed on (29 Sep 2026, an agent; scheduled audit account01/B08 auto11,
B08-R19-VOUCH-FINAL-IDENTITY-NOT-SEALED-079).

    python test_math_vouch_seal.py [MATH_SENSE.py] [--old OLD_MATH_SENSE.py]

The real hook, in shadow mode, on a frozen store snapshot and a frozen copy of the claim vectors (campaign mb10d s0929r77);
skipped when they are not on this machine. Each case loads a fresh copy of the hook.
 V0  a plain question the vouch route serves: its agreed first card leads the block, as before (VOUCH-NORMAL)
 V1  the session already holds the agreed card, so session dedup removes it and the next card would lead: silent, with
     vouch_identity_lost (VOUCH-DEDUP-SEAL)
 V2  the agreed card is too long for the block, so the budget drops it and the next card would lead: silent, with
     vouch_identity_lost (VOUCH-BUDGET-SEAL)
 V3  a question the gate admits, with its first card removed the same way: served with the next card first, since only the
     vouch route has an agreement to keep
With --old, the hook before this change serves the second card in V1 and V2 (the defect B08 found).
"""
import contextlib
import importlib.machinery
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]
MS = os.path.abspath(ARGS[0]) if ARGS and not ARGS[0].startswith("--") else os.path.join(HERE, "math_sense.py")
OLD = os.path.abspath(ARGS[ARGS.index("--old") + 1]) if "--old" in ARGS else None
MB = r"~/math-brain-build/local/mb10d"
STORE = MB + "/s0929r77/brain.sqlite3"
VECS = MB + "/vectors/claim_embeddings_live_20260929b.npz"
VOUCHED = ("When testing one fully specified distribution against another at a fixed significance level, why does "
           "rejecting based on a likelihood ratio threshold give the test with the greatest power among all tests of that "
           "size?")          # plain bank v1, question 32 (its card is the Neyman-Pearson lemma)
ADMITTED = ("If a function between topological spaces is continuous and its domain is compact, must the image of that "
            "domain also be compact?")
fails, ran = [], []


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def run(hook, prompt, dedup_first=False, inflate_first=False, tag="v"):
    """(served, emitted ids, silence notes) of one prompt through a fresh copy of hook."""
    os.environ.update(MATHBRAIN_TIME_BUDGET_S="300", MATHBRAIN_INTEGRITY_GRACE_S="60", PYTHONIOENCODING="utf-8",
                      MATHBRAIN_USE_LOG="0", MATHBRAIN_SHADOW="1", MATH_BRAIN_CLAIM_VECS=VECS, MATHBRAIN_STORE=STORE)
    if os.path.dirname(hook) not in sys.path:
        sys.path.insert(0, os.path.dirname(hook))
    name = "vouch_seal_%s_%d" % (tag, len(ran))
    loader = importlib.machinery.SourceFileLoader(name, hook)      # a backup named .bak_* is still Python source
    spec = importlib.util.spec_from_file_location(name, hook, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    notes = []
    m._silence_note = lambda data, note, **kw: notes.append(note)
    if dedup_first:
        # the session has already been shown the first card of the pool: the dedup guard reports it
        real = m._already_injected
        first = {}

        def already(sess, ids, record=True):
            ids = list(ids)
            if not record:
                first.setdefault("id", ids[0] if ids else None)
                return {first["id"]} & set(ids)
            return real(sess, ids, record=record)
        m._already_injected = already
    if inflate_first:
        real_block = m._assemble_note_block

        def block(header, pieces, budget):
            if pieces and not getattr(block, "done", False):
                block.done = True
                pieces[0] = (pieces[0][0], pieces[0][1] + " " * (budget + 1))    # the first card no longer fits
            return real_block(header, pieces, budget)
        m._assemble_note_block = block
    sys.stdin = io.StringIO(json.dumps({"prompt": prompt, "session_id": "vouchseal-%s-%04d" % (tag, len(ran))}))
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        try:
            m.main()
        except SystemExit:
            pass
    text = out.getvalue()
    body = json.loads(text)["hookSpecificOutput"]["additionalContext"] if text.strip() else ""
    return bool(body), re.findall(r"\((claim_[0-9a-f]+)\s*\|", body), notes


def main():
    if not (os.path.exists(STORE) and os.path.exists(VECS)):
        print("SKIP - the frozen store snapshot or vectors are not on this machine (%s)" % MB)
        return 0
    served, ids, notes = run(MS, VOUCHED, tag="v0")
    agreed = ids[0] if ids else None
    check(served and len(ids) >= 2 and "vouch_route" in notes and "vouch_identity_lost" not in notes,
          "V0 the vouch route serves its agreed card first: %d cards, first %s, notes %r"
          % (len(ids), (agreed or "")[:22], notes))
    served, ids, notes = run(MS, VOUCHED, dedup_first=True, tag="v1")
    check(not served and "vouch_identity_lost" in notes,
          "V1 dedup removes the agreed card: served %s, notes %r" % (served, notes))
    served, ids, notes = run(MS, VOUCHED, inflate_first=True, tag="v2")
    check(not served and "vouch_identity_lost" in notes,
          "V2 the budget drops the agreed card: served %s, notes %r" % (served, notes))
    served0, ids0, notes0 = run(MS, ADMITTED, tag="v3a")
    served, ids, notes = run(MS, ADMITTED, dedup_first=True, tag="v3b")
    check(served0 and served and len(ids0) >= 2 and ids and ids[0] == ids0[1] and "vouch_route" not in notes0 + notes,
          "V3 a gate-admitted question is not sealed: first card %s, then %s after dedup (the second before)"
          % ((ids0 or [""])[0][:22], (ids or [""])[0][:22]))
    if OLD:
        served, ids, notes = run(OLD, VOUCHED, dedup_first=True, tag="n1")
        check(served and ids and ids[0] != agreed,
              "N1 the hook before this change serves another card first after dedup: %s (agreed %s)"
              % ((ids or [""])[0][:22], (agreed or "")[:22]))
        served, ids, notes = run(OLD, VOUCHED, inflate_first=True, tag="n2")
        check(served and ids and ids[0] != agreed,
              "N2 the hook before this change serves another card first when the agreed one does not fit: %s"
              % (ids or [""])[0][:22])
    print("%s - %d controls, %d failed" % ("FAIL" if fails else "PASS", len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
