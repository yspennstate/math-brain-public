"""Controls for the sub-query refill rule (MATHBRAIN_SUBQ_REFILL): an emptied block is refilled only by a sub-query
that names something the store holds.

 Q1 the rule is read in _main_body with default "src"
 Q2 src: an empty block is NOT refilled from quoted phrases the store has no title for
 Q3 src: an empty block IS refilled from quoted store titles
 Q4 src: a non-empty block keeps its quoted-phrase sub-queries
 Q5 "0" never refills an empty block; "1" refills from anything; "arg" only on argument-shaped prompts

    python test_subq_refill.py      (under a second; ALL PASS at the end)
Runs the hook's own statements, cut from _main_body, against stubs.
"""
import ast
import io
import os
import sys
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = io.open(os.path.join(HERE, "math_sense.py"), encoding="utf-8").read().replace("\r\n", "\n")
LINES = SRC.split("\n")
results = []


def check(ok, what):
    results.append(bool(ok))
    print(("PASS  " if ok else "FAIL  ") + what)


def piece(pred):
    for fn in ast.parse(SRC).body:
        if isinstance(fn, ast.FunctionDef) and fn.name == "_main_body":
            for node in ast.walk(fn):
                if isinstance(node, ast.stmt) and pred(node):
                    return textwrap.dedent("\n".join(LINES[node.lineno - 1:node.end_lineno]))
    return ""


MODE = piece(lambda n: isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "_subq_mode")
REFILL = piece(lambda n: isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "_subq_refill")
REFUSE = piece(lambda n: isinstance(n, ast.If) and "_subq_mode" in ast.dump(n.test) and "_subq_quoted" in ast.dump(n.test))
check(bool(MODE and REFILL and REFUSE), "Q1 the refill rule is in _main_body")


def run(mode, chosen, quoted, covered, argshape=False):
    """Returns (stage runs at all, sub-queries left after the refusal)."""
    os.environ.pop("MATHBRAIN_SUBQ_REFILL", None)
    if mode is not None:
        os.environ["MATHBRAIN_SUBQ_REFILL"] = mode
    g = {"os": os, "prompt": "p", "_argument_shape": (lambda p: 1 if argshape else None)}
    exec(MODE + "\n" + REFILL, g)
    runs = bool(chosen) or g["_subq_refill"]
    g.update(chosen=chosen, subs=["a", "b"], _subq_quoted=quoted, _covered_titles=covered)
    exec(REFUSE, g)
    return runs, g["subs"]


try:
    if MODE and REFILL and REFUSE:
        check(run(None, [], True, []) == (True, []), "Q2 src: no refill from absent quoted phrases")
        check(run(None, [], True, ["T1"]) == (True, ["a", "b"]), "Q3 src: refill from quoted store titles")
        check(run(None, ["c"], True, []) == (True, ["a", "b"]), "Q4 src: a non-empty block keeps its sub-queries")
        check(run("0", [], False, [])[0] is False and run("1", [], True, [])[1] == ["a", "b"]
              and run("arg", [], False, [])[0] is False and run("arg", [], False, [], argshape=True)[0] is True,
              "Q5 0 / 1 / arg modes")
finally:
    os.environ.pop("MATHBRAIN_SUBQ_REFILL", None)
print("ALL PASS" if all(results) and len(results) == 5 else "FAILED %d of %d" % (5 - results.count(True), 5))
sys.exit(0 if all(results) and len(results) == 5 else 1)
