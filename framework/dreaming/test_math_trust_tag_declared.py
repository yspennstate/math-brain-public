"""The card's trust tag names a revision's declared status apart from its authenticated one (account02/B11,
B11-R79-OVERLAY-STATUS-CANNOT-APPEND-01, T9; 30 Sep 2026).

    python test_math_trust_tag_declared.py [MATH_SENSE_BEFORE_THE_FIX.py]

Since 30 Sep a Math Brain revision can declare any status and still be appended: the stored claim starts unverified
and the node carries the declaration as declared_status. The closing word of the tag stays the authenticated status,
so a declared 'verified' is shown as a declaration, not a verification, and a declared retraction is not served as a
plain 'unverified'. D1-D7 check the tag; N1 runs the hook before the change and shows the retraction silent.
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from math_block_parse import delivery_problem, iter_cards  # noqa: E402

FAILS = []
BASE = {"claim_kind": "theorem", "proof_text": "a proof", "draft": "fixture"}


def check(name, ok, detail=""):
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (": " + str(detail)[:240]) if detail else ""))
    if not ok:
        FAILS.append(name)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ms = load(os.path.join(HERE, "math_sense.py"), "ms_declared")
    plain = ms._trust_tag(dict(BASE))
    check("D1 a node with no declared status is tagged exactly as before",
          plain == "theorem +proof; draft; unreviewed; unverified", plain)
    tag = ms._trust_tag(dict(BASE, declared_status="retracted"))
    check("D2 a declared retraction is named, and the closing word stays the authenticated one",
          "declared retracted" in tag and tag.endswith("; unverified"), tag)
    tag = ms._trust_tag(dict(BASE, declared_status="verified"))
    check("D3 a declared 'verified' reads as a declaration beside 'unverified', never as a verification",
          "declared verified" in tag and tag.endswith("; unverified"), tag)
    tag = ms._trust_tag(dict(BASE, declared_status="gap_found"))
    check("D4 an underscore status is written in words", "declared gap found" in tag, tag)
    check("D5 a declared 'unverified' adds nothing", ms._trust_tag(dict(BASE, declared_status="unverified")) == plain)
    check("D6 a declared status that is not a string is ignored",
          ms._trust_tag(dict(BASE, declared_status=["verified"])) == plain)
    tag = ms._trust_tag(dict(BASE, declared_status="refuted"),
                        read={"when": "2026-09-30", "passed": False, "human": False})
    block = ("[math-brain] leads, not verdicts.\n- A theorem [theorem]: text\n    (claim_" + "c" * 64 + " | " + tag
             + ")\n")
    check("D7 a card carrying a declared status and a recorded read is still read whole by the shared parser",
          delivery_problem(block) == "" and "declared refuted" in list(iter_cards(block))[0].hint
          and tag.endswith("GAP FOUND; unverified"), tag)
    if len(sys.argv) > 1:
        old = load(sys.argv[1], "ms_before")
        tag = old._trust_tag(dict(BASE, declared_status="retracted"))
        check("N1 the hook before the change serves a declared retraction as a plain 'unverified' (the finding)",
              "retracted" not in tag and tag.endswith("unverified"), tag)
    print("%d failed" % len(FAILS))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
