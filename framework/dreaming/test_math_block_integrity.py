"""A served math card counts only when it arrives whole: a claim id and a trust tag (29 Sep 2026; fixed 30 Sep).

    python test_math_block_integrity.py [--old DIR]

The auditor showed a hook that exits 0 with valid JSON whose cards had lost their id and trust lines: the hook-path
evaluator scored the header's title as a theorem hit, the health check passed eleven such blocks, and the gate's
production probe looked only for the marker. T01-T08 are the auditor's proposed checks, against the parser
(math_block_parse), the evaluator (eval_math_hookpath), the health check (math_sense_healthcheck) and the gate's
production probe (math_brain_regression_gate.production_math_block). --old DIR runs the same malformed cases through
the consumers as they were before the fix (copies of the four files in DIR) and shows them passing (the finding).
"""
import contextlib
import importlib.util
import io
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import math_block_parse as P  # noqa: E402

FAILS = []
ID1, ID2, ID3 = ("claim_" + c * 64 for c in "abc")
HEAD = "[math-brain] leads, not verdicts - check each result's hypotheses against the step that uses it.\n"
CARD1 = ("- Hoeffding's inequality [theorem]: For independent X_i in [a_i, b_i], P(S - ES >= t) <= exp(-2t^2 / sum (b_i - a_i)^2).\n"
         "    (" + ID1 + " | theorem +proof; draft; unreviewed; unverified)\n")
CARD2 = ("- Tight family of measures [definition]: A family of probability measures on a metric space is tight if ...\n"
         "    (" + ID2 + " | definition lead; draft; unreviewed; unverified)\n")
CARD3 = ("- Sylow theorems [theorem]: Let G be a finite group of order p^a m with p prime not dividing m ...\n"
         "    (" + ID3 + " | EXCERPT, incomplete; theorem +proof; draft; unreviewed; unverified)\n")
BLOCK = HEAD + CARD1 + CARD2 + CARD3
OLD_FORMAT = (HEAD + "- Hoeffding's inequality [theorem, score 21.4]: For independent X_i in [a_i, b_i] ...\n"
              "    (source-id: " + ID1 + ")\n    (hint: SOURCE EXCERPT: incomplete statement; unverified)\n")
HEADER_ONLY = HEAD + "".join(c.split("\n")[0] + "\n" for c in (CARD1, CARD2, CARD3))
NO_HINT = BLOCK.replace(" | theorem +proof; draft; unreviewed; unverified", "")
OLD_NO_HINT = OLD_FORMAT.replace("    (hint: SOURCE EXCERPT: incomplete statement; unverified)\n", "")
BULLET = HEAD + "- see the theorem [Hoeffding]: in the appendix for details\n"


def check(name, ok, detail=""):
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (": " + str(detail)[:300]) if detail else ""))
    if not ok:
        FAILS.append(name)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


FAKE = r'''
import json, os, sys
prompt = json.loads(sys.stdin.read() or "{}").get("prompt", "")
blocks = json.loads(open(os.environ["FAKE_BLOCKS"], encoding="utf-8").read())
silent = set(blocks["silent_prompts"])
block = "" if prompt in silent else blocks[os.environ.get("FAKE_MODE", "whole")]
if block:
    sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": block}}))
'''


def fake_hook(tmp, health):
    """A zero-exit hook that serves one of the fixture blocks to every must-speak prompt and nothing to the rest."""
    whole = BLOCK + "- Turan's theorem [theorem]: ex(n, K_{r+1}) is attained by the Turan graph.\n    (claim_" + "d" * 64 + \
        " | theorem +proof; draft; unreviewed; unverified)\n"
    header = HEAD + "".join(line + "\n" for line in whole.split("\n") if line.startswith("- "))
    data = {"whole": whole, "header_only": header, "silent_prompts": [p for _, p in health.MUST_STAY_SILENT]}
    with open(os.path.join(tmp, "blocks.json"), "w", encoding="utf-8") as fh:
        json.dump(data, fh)
    path = os.path.join(tmp, "fake_hook.py")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(FAKE)
    return path


def run_health(path, hook, tmp, mode):
    os.environ["MATH_SENSE_HOOK"] = hook
    os.environ["FAKE_BLOCKS"] = os.path.join(tmp, "blocks.json")
    os.environ["FAKE_MODE"] = mode
    try:
        mod = load(path, "health_%s_%d" % (mode, len(FAILS)))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = mod.main()
        return rc, buf.getvalue()
    finally:
        for k in ("MATH_SENSE_HOOK", "FAKE_BLOCKS", "FAKE_MODE"):
            os.environ.pop(k, None)


def evaluator_row(mod, block, stems=("hoeffding",)):
    """What the evaluator makes of a zero-exit hook serving this block."""
    mod._call = lambda prompt, e: (json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
                                                                      "additionalContext": block}}) if block else "", 0, "")
    r = mod.ask("q", {})
    r.update({"kind": "answerable", "key": "k", "area": "a", "form": "q_content", "prompt_chars": 1})
    r["hit"] = mod.stem_hit(r["titles"], list(stems))
    r["rank1"] = bool(r["titles"]) and mod.stem_hit(r["titles"][:1], list(stems))
    return r


def dispatcher_out(math_block, after="[verify] Before you call a claim proved ...\n- note [x]: y\n"):
    ctx = "[unconscious] a reflex line\n" + math_block + after
    return json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": ctx}})


def main():
    tmp = tempfile.mkdtemp(prefix="mbi_")
    ev = load(os.path.join(HERE, "eval_math_hookpath.py"), "emh_integrity")
    gate = load(os.path.join(HERE, "math_brain_regression_gate.py"), "gate_integrity")
    health_path = os.path.join(HERE, "math_sense_healthcheck.py")
    health = load(health_path, "health_lists")
    hook = fake_hook(tmp, health)

    # T01 whole cards, both formats, through every consumer
    cards = list(P.iter_cards(BLOCK))
    check("T01a three whole cards parse with id, title, kind, text and tag",
          [c.node_id for c in cards] == [ID1, ID2, ID3] and all(P.card_is_complete(c) and c.title and c.kind and c.text
                                                               for c in cards) and P.delivery_problem(BLOCK) == "")
    check("T01b the old format with its hint line is whole", P.delivery_problem(OLD_FORMAT) == "")
    r = evaluator_row(ev, BLOCK)
    check("T01c the evaluator scores a whole block: valid, a hit at rank 1", ev.valid(r) and r["hit"] and r["rank1"], r)
    rc, out = run_health(health_path, hook, tmp, "whole")
    check("T01d the health check passes when every must-speak block is whole", rc == 0, out[-300:])
    check("T01e the gate's production probe reads a whole block as served",
          gate.production_math_block(dispatcher_out(BLOCK)) == (True, ""))

    # T02 truncated before the id line; T06 the health check on eleven header-only blocks
    r = evaluator_row(ev, HEADER_ONLY)
    check("T02a header-only cards: the row is invalid, not a hit, and the titles are kept for the record",
          not ev.valid(r) and r.get("invalid") == P.INCOMPLETE_CARD and not r["hit"] and r["titles"] == []
          and r.get("incomplete_titles"), r)
    s, lines = ev.summarize([r, evaluator_row(ev, BLOCK)], {}, "bank.json")
    check("T02b the summary keeps the broken row out of the rates and counts it by reason",
          s["q_content"]["n"] == 1 and s["q_content"]["not_scored"] == 1 and s["invalid"] == 1
          and s["invalid_reasons"] == {P.INCOMPLETE_CARD: 1}, s)
    rc, out = run_health(health_path, hook, tmp, "header_only")
    check("T06 the health check fails when the must-speak blocks are header-only",
          rc == 1 and "SPOKE but the block is broken (incomplete math card)" in out, out[-300:])
    check("T02c the gate's production probe breaches on header-only cards",
          gate.production_math_block(dispatcher_out(HEADER_ONLY)) == (False, P.INCOMPLETE_CARD))

    # T03 id kept, tag lost, both formats
    check("T03a new format with the id but no tag is incomplete", P.delivery_problem(NO_HINT) == P.INCOMPLETE_CARD)
    check("T03b old format with the source-id but no hint line is incomplete",
          P.delivery_problem(OLD_NO_HINT) == P.INCOMPLETE_CARD)
    check("T03c the evaluator does not score a card without its tag", not ev.valid(evaluator_row(ev, NO_HINT)))

    # T04 an ordinary bullet with the card shape and no id line is never a hit
    r = evaluator_row(ev, BULLET, stems=("hoeffding", "see the theorem"))
    check("T04 a card-shaped bullet without an id line is not a served card", not ev.valid(r) and not r["hit"], r)

    # T05 every byte boundary of a three-card block
    bad, whole_prefix = [], [0]
    for k in range(len(BLOCK) + 1):
        cut = BLOCK[:k]
        prob = P.delivery_problem(cut)
        got = [c.node_id for c in P.iter_cards(cut)]
        complete_before = [i for i, end in ((ID1, len(HEAD + CARD1)), (ID2, len(HEAD + CARD1 + CARD2)),
                                            (ID3, len(BLOCK))) if k >= end - 1]
        if prob == "":
            # a clean read: only cards whose id line arrived whole, and never a card cut short
            if any(g is None for g in got) or [g for g in got] != complete_before[:len(got)] or len(got) > len(complete_before):
                bad.append((k, got, complete_before))
        r = evaluator_row(ev, cut)
        hit_ids = r["ids"] if ev.valid(r) else []
        if ev.valid(r) and cut.strip() and r["titles"] and len(hit_ids) != len(r["titles"]):
            bad.append((k, "title without id", r))
    check("T05 across all %d cut points, a cut leaves only whole preceding cards or an invalid row, never an added hit"
          % (len(BLOCK) + 1), not bad, bad[:3])

    # T07 crash, timeout and bad JSON keep their own reasons (the 30 Sep child-exit fix)
    ev._call = lambda prompt, e: ("", 7, "")
    r7 = ev.ask("q", {})
    ev._call = lambda prompt, e: ("Traceback: not JSON", 0, "")
    rj = ev.ask("q", {})
    check("T07 a nonzero exit and output that is not the hook's JSON stay distinct invalid reasons",
          r7.get("invalid") == "hook exited 7" and rj.get("invalid") == "hook output is not the hook's JSON", (r7, rj))

    # T08 a whole but irrelevant card is a relevance miss, not a delivery failure
    r = evaluator_row(ev, HEAD + CARD2, stems=("hoeffding",))
    check("T08 a whole card on the wrong topic is a valid row that misses", ev.valid(r) and not r["hit"], r)

    # the dispatcher context: the math section ends at the next hook's tag, and keeps its own omitted-notes line
    tail = "[math-brain: 1 note(s) omitted whole for the context budget.]\n"
    check("S1 the block's own '[math-brain: N note(s) omitted]' line stays inside the section",
          gate.production_math_block(dispatcher_out(BLOCK + tail)) == (True, ""))
    cut_note = HEAD + CARD1 + CARD2.split("\n")[0] + "\n  ... [math_sense.py: 812 more chars, in the file above]\n"
    check("S2 the dispatcher's own cut leaving a header without its id line is a breach",
          gate.production_math_block(dispatcher_out(cut_note)) == (False, P.INCOMPLETE_CARD))
    check("S3 no marker, or output that is not JSON, is named",
          gate.production_math_block(dispatcher_out("", after="")) == (False, "no [math-brain] block")
          and gate.production_math_block("not json")[0] is False)

    if "--old" in sys.argv:
        old = sys.argv[sys.argv.index("--old") + 1]
        sys.path.insert(0, old)
        for name in ("math_block_parse",):
            sys.modules.pop(name, None)
        oev = load(os.path.join(old, "eval_math_hookpath.py"), "emh_old")
        r = evaluator_row(oev, HEADER_ONLY)
        check("N1 the evaluator before the fix scores header-only cards as a valid theorem hit with no id (the finding)",
              oev.valid(r) and r["hit"] and r["ids"] == [], r)
        rc, out = run_health(os.path.join(old, "math_sense_healthcheck.py"), hook, tmp, "header_only")
        check("N2 the health check before the fix passes eleven header-only blocks (the finding)", rc == 0, out[-200:])
        pout = dispatcher_out(HEADER_ONLY)
        check("N3 the gate's old production test ('[math-brain]' in the output) calls header-only served (the finding)",
              "[math-brain]" in pout and "production_math_block" not in open(
                  os.path.join(old, "math_brain_regression_gate.py"), encoding="utf-8").read())
    print("%d failed" % len(FAILS))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
