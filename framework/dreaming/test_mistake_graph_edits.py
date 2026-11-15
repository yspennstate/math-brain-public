# mg_edit_controls.py [LIVE_MISTAKE_GRAPH_PY]: controls for the in-place-edit handling of the recurrence watch.
# Uses temp files only; reads the live MISTAKES.md once (read-only) to prove the ids did not move.
import importlib.util, io, json, os, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mistake_graph as mg

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  " + str(detail)) if detail and not ok else ""))
    if not ok:
        FAILS.append(name)


def snap(gen, all_ids, singles, overrides=()):
    return {"schema": mg.SNAPSHOT_SCHEMA, "observed_at_ns": gen, "all_ids": sorted(all_ids),
            "singletons": sorted(singles), "override_reflexes": sorted(overrides), "seen_ids": sorted(all_ids)}


def run(tmp, payload, **kw):
    out = io.StringIO()
    seen = {}

    def renderer(prior, status):
        seen["prior"] = prior
        seen["status"] = status
        return "verdict\n"

    res = mg._watch_snapshot_transaction(payload, path=os.path.join(tmp, "snap.json"), renderer=renderer, stream=out,
                                         status_path=os.path.join(tmp, "status.json"), **kw)
    return res, seen


def status(tmp):
    return json.load(open(os.path.join(tmp, "status.json"), encoding="utf-8"))


def stored(tmp):
    return json.load(open(os.path.join(tmp, "snap.json"), encoding="utf-8"))


A, A2, B, C, D, E = "c_aaaaaaaaaa", "c_aaaaaaaa22", "c_bbbbbbbbbb", "c_cccccccccc", "c_dddddddddd", "c_eeeeeeeeee"

# 1. the stem
long_entry = "- **2026-08-12 morning (a bold family)** 'quote' -> wrong: " + "an old mistake told at length. " * 8
check("stem: a note added past the head keeps the stem",
      mg._stem(long_entry) == mg._stem(long_entry + " (18 Oct 2026, agent: now covered - some_reflex)"))
check("stem: whitespace reflow keeps the stem", mg._stem(long_entry) == mg._stem(long_entry.replace(" ", "\n  ", 3)))
check("stem: a different head is a different stem", mg._stem(long_entry) != mg._stem("- **2026-08-13" + long_entry[14:]))

# 2. the map
recs = [{"id": A2, "stem": "s_one"}, {"id": B, "stem": "s_two"}, {"id": C, "stem": "s_twin"}, {"id": D, "stem": "s_twin"}]
m = mg.edited_in_place_map({A: "s_one", B: "s_two", E: "s_twin", "c_gone000000": "s_nowhere"}, recs)
check("map: an edited entry maps old id to new id", m.get(A) == A2, m)
check("map: an unchanged id is not mapped", B not in m, m)
check("map: a stem shared by two current entries maps nothing", E not in m, m)
check("map: a stem that is gone maps nothing", "c_gone000000" not in m, m)

# 3. an annotated entry passes the guard and is not a new correction
with tempfile.TemporaryDirectory() as tmp:
    run(tmp, snap(100, [A, B, C], [A]))
    applied = {}
    (prev, st), seen = run(tmp, snap(200, [A2, B, C, D], [A2, D]), edited_in_place={A: A2}, edits_applied=applied)
    s = status(tmp)
    check("edit: published without --allow-removals", st == "published", st)
    check("edit: the pair is reported back", applied == {A: A2}, applied)
    check("edit: only the really new entry counts as new", s["signals"]["new_corrections"] == 1, s)
    check("edit: no one-off became recurring", s["signals"]["became_recurring"] == 0, s)
    check("edit: the renderer sees the entry under its new id",
          A2 in seen["prior"]["all_ids"] and A not in seen["prior"]["all_ids"], seen["prior"])
    now = stored(tmp)
    check("edit: the stored snapshot holds today's ids", now["all_ids"] == sorted([A2, B, C, D]), now["all_ids"])
    check("edit: the old id stays in the seen history", A in now["seen_ids"] and A2 in now["seen_ids"], now["seen_ids"])

# 4. the same observation without the map is refused as before
with tempfile.TemporaryDirectory() as tmp:
    run(tmp, snap(100, [A, B, C], [A]))
    try:
        run(tmp, snap(200, [A2, B, C, D], [A2, D]))
        check("no map: refused as before", False, "published")
    except mg.SnapshotStateError as exc:
        check("no map: refused as before", "removes 1 correction id" in str(exc), exc)
    check("no map: prior preserved", stored(tmp)["all_ids"] == sorted([A, B, C]))

# 5. a real removal is still refused, with a map that does not cover it and with maps that must not be believed
with tempfile.TemporaryDirectory() as tmp:
    run(tmp, snap(100, [A, B, C], [A]))
    for label, emap in (("a removal beside an edit", {A: A2}),          # C is gone for real
                        ("a map onto an id the prior already had", {C: B}),
                        ("a map onto an id that is not here today", {C: E})):
        try:
            run(tmp, snap(200, [A2, B] if A in emap else [A, B], [], ), edited_in_place=emap)
            check("removal: refused - " + label, False, "published")
        except mg.SnapshotStateError as exc:
            check("removal: refused - " + label, "removes 1 correction id" in str(exc), exc)
    try:
        run(tmp, snap(200, [B, C, D], [D]), edited_in_place={A: D, "c_other00000": D})
        check("removal: one new id claimed by one old id only is accepted", True)
    except mg.SnapshotStateError as exc:
        check("removal: one new id claimed by one old id only is accepted", False, exc)

with tempfile.TemporaryDirectory() as tmp:
    run(tmp, snap(100, [A, B, C], [A]))
    try:
        run(tmp, snap(200, [C, D], [D]), edited_in_place={A: D, B: D})
        check("removal: two old ids claiming one new id are both refused", False, "published")
    except mg.SnapshotStateError as exc:
        check("removal: two old ids claiming one new id are both refused", "removes 2 correction id" in str(exc), exc)

# 6. an edited one-off that now sits in a family is reported as recurring
with tempfile.TemporaryDirectory() as tmp:
    run(tmp, snap(100, [A, B, C], [A]))
    run(tmp, snap(200, [A2, B, C], []), edited_in_place={A: A2})
    s = status(tmp)
    check("recurring: an edited one-off that joined a family is counted",
          s["signals"]["became_recurring"] == 1 and s["state"] == "actionable", s)

# 7. --allow-removals still works, and a stale observation is never translated
with tempfile.TemporaryDirectory() as tmp:
    run(tmp, snap(100, [A, B, C], [A]))
    (prev, st), _ = run(tmp, snap(200, [B, C], []), allow_removals=True)
    check("allow-removals: still publishes", st == "published", st)
    applied = {}
    (prev, st), _ = run(tmp, snap(150, [A2, B, C], []), edited_in_place={A: A2}, edits_applied=applied)
    check("stale: not translated", st == "stale" and applied == {}, (st, applied))

# 8. the sidecar
with tempfile.TemporaryDirectory() as tmp:
    p = os.path.join(tmp, "stems.json")
    check("stems: a missing file reads as empty", mg.load_stems(p) == {})
    open(p, "w").write("{not json")
    check("stems: a corrupt file reads as empty", mg.load_stems(p) == {})
    open(p, "w").write(json.dumps({"schema": "something/else", "stems": {A: "s_x"}}))
    check("stems: another schema reads as empty", mg.load_stems(p) == {})
    open(p, "w").write(json.dumps([1, 2]))
    check("stems: a list reads as empty", mg.load_stems(p) == {})
    ok = mg.save_stems([{"id": A, "stem": "s_one"}], {}, 1, path=p)
    ok2 = mg.save_stems([{"id": A2, "stem": "s_one"}, {"id": B, "stem": "s_two"}], mg.load_stems(p), 2, path=p)
    got = mg.load_stems(p)
    check("stems: round trip, old ids kept", ok and ok2 and got == {A: "s_one", A2: "s_one", B: "s_two"}, got)
    raw = open(p, "rb").read()
    check("stems: ASCII, one line, schema named", raw.endswith(b"\n") and raw.count(b"\n") == 1
          and json.loads(raw)["schema"] == mg.STEMS_SCHEMA)

# 9. the ids did not move: the patched parser and the live one agree on the real file
live_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(mg.DR, "mistake_graph.py")
spec = importlib.util.spec_from_file_location("mg_live", live_path)
live = importlib.util.module_from_spec(spec)
sys.path.insert(0, os.path.dirname(live_path))
spec.loader.exec_module(live)
raw = open(mg.MISTAKES, encoding="utf-8", errors="replace").read()
r_new = mg.parse_corrections(mg.load_reflex_ids(), raw=raw)[0]
r_old = live.parse_corrections(live.load_reflex_ids(), raw=raw)[0]
check("ids: same ids in the same order on the real MISTAKES.md (%d)" % len(r_new),
      [r["id"] for r in r_new] == [r["id"] for r in r_old])
strip = lambda r: {k: v for k, v in r.items() if k != "stem"}
check("ids: every other field unchanged", [strip(r) for r in r_new] == [strip(r) for r in r_old])
stems = [r["stem"] for r in r_new]
check("stems: every record has one", all(s.startswith("s_") and len(s) == 14 for s in stems))
print("     %d records, %d distinct stems (%d records share a stem with another)" % (
    len(stems), len(set(stems)), sum(1 for s in stems if stems.count(s) > 1)))

print("\n%d failed" % len(FAILS) if FAILS else "\nALL PASS")
sys.exit(1 if FAILS else 0)
