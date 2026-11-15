"""test_math_pool_adjacency_reset.py - the math hook's pool adjacency does not carry from one prompt to the next in one
process (28 Sep 2026, an agent; scheduled audit account02/B11 auto37, B11-R31-POOL-ADJ-FALLBACK-STATE-LEAK-01).

    python test_math_pool_adjacency_reset.py [MATH_SENSE.py] [--old OLD_MATH_SENSE.py]

 P1 a prefiltered prompt leaves its pool's links (A-B linked); the per-prompt reset clears them, and A-B is then
    linked in no way a fresh process would not see
 P2 main() calls the reset first, and the full-store branch clears the links itself
 P3 after the reset the module's state equals a freshly loaded module's (vouch route, agreed card, semantic top, links)
With --old, the module before this change must keep A-B linked after main()'s own reset (the leak B11 found).
"""
import importlib.machinery
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]
MS = os.path.abspath(ARGS[0]) if ARGS and not ARGS[0].startswith("--") else os.path.join(HERE, "math_sense.py")
OLD = os.path.abspath(ARGS[ARGS.index("--old") + 1]) if "--old" in ARGS else None
sys.path.insert(0, HERE)
fails, ran = [], []


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def load(path, name):
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    return m


class E:
    def __init__(self, a, b, kind="depends_on"):
        self.source_id, self.target_id, self.kind = a, b, kind


def state(m):
    return (bool(m._VOUCH.get("route")), dict(m._COV_AGREED), dict(m._SEMTOP), {k: sorted(v) for k, v in m._POOL_ADJ.items()})


def main():
    m = load(MS, "ms_under_test")
    fresh = state(load(MS, "ms_fresh"))
    m._set_pool_adjacency([E("A", "B"), E("B", "C")])
    linked_before = m._linked_to("A", "B")
    m._VOUCH["route"] = True
    m._COV_AGREED["prefilter"] = "A"
    m._reset_per_prompt_state()
    check(linked_before and not m._linked_to("A", "B") and m._POOL_ADJ == {},
          "P1 a prefiltered prompt's links (A-B linked %s) are gone after the reset (linked %s)" % (
              linked_before, m._linked_to("A", "B")))
    src = open(MS, encoding="utf-8").read()
    body = src.split("def main():", 1)[1][:400]
    main_src = src.split("def main():", 1)[1]
    fallback = main_src.split("edges = list(store.iter_edges())", 1)[1][:200] if "edges = list(store.iter_edges())" in main_src else ""
    check("_reset_per_prompt_state()" in body and "_set_pool_adjacency(())" in fallback,
          "P2 main() resets first and the full-store branch clears the links itself")
    check(state(m) == fresh, "P3 after the reset the state equals a fresh module's: %s" % (state(m) == fresh,))
    if OLD:
        o = load(OLD, "ms_old")
        o._set_pool_adjacency([E("A", "B")])
        # the old main() reset, run by hand: the three per-prompt fields it cleared, and nothing else
        o._VOUCH["route"] = False
        o._COV_AGREED.clear()
        o._SEMTOP.clear()
        check(o._linked_to("A", "B"), "N1 the module before this change keeps A-B linked after its per-prompt reset (the "
                                      "leak B11 found; the check can fail): %s" % o._linked_to("A", "B"))
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
