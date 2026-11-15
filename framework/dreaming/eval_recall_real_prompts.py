#!/usr/bin/env python3
"""eval_recall_real_prompts.py - the SHIPPED recall path, on real owner prompts.

Why this file exists (2026-09-14). eval_prompt_recall_fullstack.py answers a different question: it
reimplements the blend from the seeder, the spread and the semantic lane so it can sweep the blend
weights. That makes it blind to anything inside `brain.recall()` itself - a rerank added there changes
nothing in its output, and an unchanged number from a blind instrument reads exactly like "no harm
done". It is not evidence on that axis (gate_incomplete_is_not_a_pass_2026_07_16).

This one calls `brain.recall()`, the function the CLI and the hooks call, over the same real
prompt-to-reads episodes: what the author actually typed, scored against what that session actually
went on to read. It is independent of the 56-question owner-voice bank, so a rerank tuned on that
bank can be falsified here.

    python eval_recall_real_prompts.py [--n N] [--k 8] [--served | --resident] [--deadline-s S] [--order-seed N]

Scores hit@k and MRR over the episodes' read sets. Set BRAIN_RECALL_* dials to compare arms; hold the
index generation with `bm25.py freeze` so both arms see one corpus.
"""
from __future__ import annotations

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eval_prompt_recall_fullstack import episodes   # noqa: E402
from eval_brain_recall_fresh import recall as cli_recall  # the CLI path, exactly as the bank scores it


def _inproc_recall():
    """brain.recall() called in this one process, the call brain.py's CLI makes after parsing (2026-10-03).

    The CLI path starts a fresh `brain.py recall` per episode. On this box a process start stalls for 20-35 s in a
    busy window, so the 66 episodes passed the gate's 900 s cap on 6 of the 8 nights to 3 Oct (rc 124, no number at
    all); on calm nights they took 259-403 s. Same function, same arguments, same output parsing; `--cli` keeps the
    old path, and `--check-cli N` compares the two on the first N episodes, slug for slug."""
    import contextlib
    import io
    import re
    import brain  # noqa: E402  (the module the CLI runs)

    def rec(q, k=8):
        q = re.sub(r"^[\-\*>\s]+", "", q)      # what brain.main() does to a query before recall()
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            brain.recall(q, 8)
        out = buf.getvalue()
        slugs = re.findall(r"^\s*\d\.\d\d\s+\[[^\]]*\]\s+(\S+)", out, re.M)
        return slugs[:k], out
    return rec


def _resident_recall():
    """The recall server's own warm state, built in this process (2026-11-10).

    brain.recall() called bare re-reads the embeddings, the graph, the superseded list and the folder listing on
    every call: 7-14 s a query on this box (profiled 10 Nov 07:2x, 139 episodes), so the pass ended rc 124 at the
    gate's 900 s cap on 23 of the last 25 nights and gave no number. Callers do not get that path any more: since
    3 Nov `brain.py recall` is answered by brain_recall_server.py, which keeps that state between calls and drops
    it when the files under it change. This builds the same Brain object here and sends each prompt through its
    call(), the function the server runs for a client, so the number is the one a caller's recall gives."""
    import re
    import brain_recall_server as S

    B = S.Brain()
    env = {k: os.environ[k] for k in S.PER_CALL_ENV if k in os.environ}
    cwd = os.getcwd()

    def rec(q, k=8):
        r = B.call(["recall", q], env, cwd)
        out = r.get("out") or ""
        slugs = re.findall(r"^\s*\d\.\d\d\s+\[[^\]]*\]\s+(\S+)", out, re.M)
        return slugs[:k], out
    return rec


def _served_recall(stats):
    """Each prompt sent to the live recall server through brain_recall_client, as `brain.py recall` sends it
    (2026-11-10). The resident state built in THIS process did not make the pass fit: 30 episodes took 223 s under
    the gate at 07:3x on 10 Nov, because a call is about 2.3 s of CPU and this process waits for a core like every
    other; the live server runs AboveNormal and answered its last 400 callers in 1.6 s median. An episode the server
    does not answer (no server, busy, code changed) is answered by the resident state here; the summary says how
    many went each way. BRAIN_RECALL_LOG=0 unless the caller set it, as every test bank does, so the server does not
    file these as a session's searches."""
    import contextlib
    import io as _io
    import re
    import brain_recall_client as C

    os.environ.setdefault("BRAIN_RECALL_LOG", "0")
    fallback = []

    def rec(q, k=8):
        buf, err = _io.StringIO(), _io.StringIO()
        try:
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
                rc = C.run(["recall", q])
        except Exception:
            rc = None
        if rc is None:
            if not fallback:
                fallback.append(_resident_recall())
            stats["fallback"] = stats.get("fallback", 0) + 1
            return fallback[0](q, k)
        stats["served"] = stats.get("served", 0) + 1
        out = buf.getvalue()
        slugs = re.findall(r"^\s*\d\.\d\d\s+\[[^\]]*\]\s+(\S+)", out, re.M)
        return slugs[:k], out
    return rec


def _arg(name, default=None, cast=str):
    return cast(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default


def main():
    if any(a in ("-h", "--help") for a in sys.argv[1:]):
        print(__doc__)
        return 0
    # 10 Nov 2026: the number must not depend on who runs the bank. recall() gives display slot 5 to a past-session
    # segment and holds back one the CALLER'S session was shown in the last hour. Run from an agent's shell, the bank
    # ran under that agent's session id: its second pass within the hour lost the segment row on most prompts (25 of
    # 30 lists differed from the resident path's; with the id unset, 12 of 12 identical), and its rows went into the
    # live segment monitor under that id, holding segments back from the agent's own real recalls for an hour. The
    # nightly task has no session. So: no session here either, and the monitor rows go to a log of their own.
    for _k in ("CLAUDE_CODE_SESSION_ID", "CODEX_THREAD_ID"):
        os.environ.pop(_k, None)
    os.environ.setdefault("BRAIN_SEGMENT_SLOT_LOG", os.path.join(
        os.path.expanduser("~"), ".claude", "brain_graph", "logs", "segment_slot_eval.jsonl"))
    k = int(sys.argv[sys.argv.index("--k") + 1]) if "--k" in sys.argv else 8
    eps = episodes()
    if "--n" in sys.argv:
        eps = eps[: int(sys.argv[sys.argv.index("--n") + 1])]
    if len(eps) < 20:
        print("too few episodes (%d) - re-run as the archive grows" % len(eps))
        return 2
    if "--check-cli" in sys.argv:
        m = int(sys.argv[sys.argv.index("--check-cli") + 1])
        rec = _inproc_recall()
        same = 0
        for _sess, prompt, _reads in eps[:m]:
            a, _ = rec(prompt, k)
            b, _ = cli_recall(prompt, k)
            same += a == b
            if a != b:
                print("DIFFERS: %r\n  inproc %s\n  cli    %s" % (prompt[:80], a, b))
        print("check-cli: %d of %d episodes identical" % (same, m))
        return 0 if same == m else 1
    if "--check-resident" in sys.argv:
        # the bare path first, for every episode, and only then the resident state: building it memoizes functions
        # on modules both paths share, so a bare call made afterwards would no longer be the bare path
        m = int(sys.argv[sys.argv.index("--check-resident") + 1])
        bare = _inproc_recall()
        a_all = [bare(p, k)[0] for _s, p, _r in eps[:m]]
        res = _resident_recall()
        same = 0
        for (_sess, prompt, _reads), a in zip(eps[:m], a_all):
            b, _ = res(prompt, k)
            same += a == b
            if a != b:
                print("DIFFERS: %r\n  bare     %s\n  resident %s" % (prompt[:80], a, b))
        print("check-resident: %d of %d episodes identical" % (same, m))
        return 0 if same == m else 1
    resident = "--resident" in sys.argv and "--cli" not in sys.argv
    served = "--served" in sys.argv and "--cli" not in sys.argv and not resident
    stats = {}
    t0 = time.time()
    recall_fn = cli_recall if "--cli" in sys.argv else (
        _served_recall(stats) if served else (_resident_recall() if resident else _inproc_recall()))
    # --deadline-s: stop asking when the budget is spent and report the episodes asked, in a fixed shuffled order so
    # the sample is the same one every night and not the oldest episodes first. With no deadline every episode is
    # asked in file order, as before.
    deadline = _arg("--deadline-s", None, float)
    seed = _arg("--order-seed", 20260914, int)
    total = len(eps)
    if deadline:
        import random
        random.Random(seed).shuffle(eps)
    hit = 0
    rr = 0.0
    n = 0
    for _sess, prompt, reads in eps:
        if deadline and n >= 20 and time.time() - t0 > deadline:
            break
        try:
            slugs, _raw = recall_fn(prompt, k)
        except Exception:
            slugs = []
        n += 1
        rank = next((i + 1 for i, s in enumerate(slugs) if s in reads), None)
        if rank:
            hit += 1
            rr += 1.0 / rank
    print("eval_recall_real_prompts: %d episodes through brain.recall(n=%d) %s, dials "
          "QCOVER=%s NAME_COVERAGE=%s NOTE_DEMOTE=%s"
          % (n, k, "via the CLI, one process each" if "--cli" in sys.argv else
             ("through the live recall server (%d served, %d answered here)"
              % (stats.get("served", 0), stats.get("fallback", 0)) if served else
              ("in one process, resident state" if resident else "in one process")),
             os.environ.get("BRAIN_RECALL_QCOVER", "0"),
             os.environ.get("BRAIN_RECALL_NAME_COVERAGE", "1"),
             os.environ.get("BRAIN_RECALL_NOTE_DEMOTE", "1")))
    print("  hit@%d %d/%d = %.3f     MRR %.4f     (%.0fs)" % (k, hit, n, hit / float(n), rr / n, time.time() - t0))
    if n < total:
        print("  partial: asked %d of %d (deadline %ds, order seed %d)" % (n, total, deadline, seed))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
