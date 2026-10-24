"""Check a disclosed hook output against the treatment commitments, or check the commitment files against each other.

    python verify_disclosure.py ROUND ID ARM SEQ OUTPUT_FILE        one disclosed output: exit 0 when it is the committed one
    python verify_disclosure.py --files [COMMITMENTS EVENTS]        the two files checked against each other, run by run

A disclosed output is the exact text of one hook response's "output" field, saved as UTF-8 with no added newline. It
matches when its sha256 equals the output_sha256 committed for (ROUND, ID, ARM, SEQ) in TREATMENT_EVENTS.jsonl, its
length equals that event's output_bytes, and the event list of that run rebuilds to both roots committed in
TREATMENT_COMMITMENTS.jsonl (so no event was dropped, reordered or resized in the list).

Two roots are committed per run. events_root_sha256 is sha256 over one line per hook response,
"seq<TAB>hook_name<TAB>sha256(output)<LF>". events_root_v2_sha256 adds the byte count, "seq<TAB>hook_name<TAB>bytes<TAB>
sha256(output)<LF>". The first root left each event's output_bytes free: bytes could move between two responses of one
hook while the root and the per-hook totals both still matched (scheduled audit account02/B19,
B19-R37-AB30-PER-EVENT-SIZE-METADATA-UNBOUND-20260928). The v2 roots were added on 28 Sep by rerunning
tools/ab30_treatment_commitments.py on the same private streams: every earlier field of all 177 rows came out
byte-identical, the events file too, and the v2 root of each run equals the one this file's events rebuild.

--files checks, for every run: it has both roots, each 64 lowercase hex digits; the events rebuild both; their number
equals its hook_responses; their positions are exactly 0..n-1; their output bytes, summed by hook name, equal its
hook_output_bytes; every run with events has a commitment row; and no run and no (run, seq) appears twice. Until 28 Sep a
row without a root was skipped instead of failed, and a repeated run key was silently collapsed by the dict (scheduled
audit account01/B19, B19-R37-AB30-MISSING-EVENT-ROOT-PASSES-VERIFIER-20260928). A root alone cannot show an event list
is complete, because the same tool wrote both; the count and the byte totals were read from the stream in the same
pass, so a list that lost a row after that pass fails here (account02/B19, B19-R37-AB30-EVENT-COMPLETENESS-VERIFIER-GAP).
Completeness against the stream itself needs the stream, which is private; stream_sha256 binds it for whoever holds it.

--files also checks each row's own fields (28 Sep, account01/B19 R44, B19-R44-AB30-SELF-DECLARED-STREAM-MISMATCH-PASSES-
FILES-VERIFIER-20260928; until then a row could say its stream disagreed with its counted row and still pass):
 schema     stream_sha256 and hook_context_sha256 are 64 lowercase hex digits; stream_bytes a positive integer;
            hook_responses and every hook_output_bytes value non-negative integers; a run with no hook responses commits
            the empty context (sha256 of nothing) and a run with responses does not; matches_row holds booleans under
            exactly the keys the generator writes for the run's counted row: hook_bytes always, num_turns and
            duration_ms when the counted row (the last row of the run in roundN/results.jsonl beside this file) carries
            them - so a disagreeing key cannot be dropped to make the rest read true
 declared   status is "committed" and every matches_row value is true: a row that declares its stream disagrees fails
 hook bytes the one match a reader can redo from public files: the counted row's hook_bytes, summed by hook name, equal
            the commitment's non-zero hook_output_bytes (the generator's own rule)
Without the round files beside it, matches_row is checked against the generator's key set only, and the output says so.
The values of stream_sha256, stream_bytes and hook_context_sha256 bind private streams, so here they are checked for form
only and reported as UNVERIFIED_PRIVATE; the holder recomputes them from the streams (tools/ab30_private_holder_check.py,
receipt PRIVATE_HOLDER_RECEIPT_2026-09-28.json beside this file).
"""
import hashlib
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HEX64 = re.compile(r"^[0-9a-f]{64}$")
EMPTY = hashlib.sha256(b"").hexdigest()
MATCH_KEYS = {"duration_ms", "hook_bytes", "num_turns"}
DUP_MEMBERS = []     # (file, line, member) for every JSON object read that names a member twice (B17-R44 ... -013)


def strict_loads(text, fname, lineno):
    """json.loads, recording any object that names a member twice. Python's own loader keeps the last value silently, so
    a row could carry a second, hidden value under a name the checks read (28 Sep, account03/B17 r67,
    B17-R44-DUPLICATE-JSON-MEMBER-SMUGGLING-013); such a file fails as duplicate_json_member before any other check."""
    def pairs(ps):
        seen = set()
        for k, _v in ps:
            if k in seen:
                DUP_MEMBERS.append((fname, lineno, k))
            seen.add(k)
        return dict(ps)
    return json.loads(text, object_pairs_hook=pairs)


def load(commitments=None, events_path=None):
    commitments = commitments or os.path.join(HERE, "TREATMENT_COMMITMENTS.jsonl")
    events_path = events_path or os.path.join(HERE, "TREATMENT_EVENTS.jsonl")
    runs, dup_runs = {}, []
    for n, l in enumerate(io.open(commitments, encoding="utf-8"), 1):
        if l.strip():
            r = strict_loads(l, os.path.basename(commitments), n)
            k = (r["round"], r["id"], r["arm"])
            if k in runs:
                dup_runs.append(k)
            runs[k] = r
    events, dup_events, seen = {}, [], set()
    for n, l in enumerate(io.open(events_path, encoding="utf-8"), 1):
        if l.strip():
            e = strict_loads(l, os.path.basename(events_path), n)
            k = (e["round"], e["id"], e["arm"])
            if (k, e["seq"]) in seen:
                dup_events.append((k, e["seq"]))
            seen.add((k, e["seq"]))
            events.setdefault(k, []).append(e)
    return runs, events, dup_runs, dup_events


def counted_rows(folder):
    """The counted row of each run as the generator reads it: the last row of each (id, arm) in roundN/results.jsonl."""
    out = {}
    for rnd in sorted(os.listdir(folder)):
        p = os.path.join(folder, rnd, "results.jsonl")
        if rnd.startswith("round") and os.path.isfile(p):
            for n, l in enumerate(io.open(p, encoding="utf-8"), 1):
                if l.strip():
                    r = strict_loads(l, rnd + "/results.jsonl", n)
                    out[(rnd, r["id"], r["arm"])] = r
    return out


def root_of(evs):
    h = hashlib.sha256()
    for e in sorted(evs, key=lambda e: e["seq"]):
        h.update(("%d\t%s\t%s\n" % (e["seq"], e["hook_name"], e["output_sha256"])).encode("utf-8"))
    return h.hexdigest()


def root_v2(evs):
    h = hashlib.sha256()
    for e in sorted(evs, key=lambda e: e["seq"]):
        h.update(("%d\t%s\t%d\t%s\n" % (e["seq"], e["hook_name"], e["output_bytes"], e["output_sha256"])).encode("utf-8"))
    return h.hexdigest()


def well_formed(v):
    return isinstance(v, str) and bool(HEX64.match(v))


def whole(v, positive=False):
    return isinstance(v, int) and not isinstance(v, bool) and (v > 0 if positive else v >= 0)


def expected_match_keys(row):
    """The keys ab30_treatment_commitments.py writes into matches_row for this counted row."""
    keys = {f for f in ("num_turns", "duration_ms") if row.get(f) is not None}
    hb = row.get("hook_bytes")
    if (isinstance(hb, dict) and hb) or hb in ({}, None, 0):
        keys.add("hook_bytes")
    return keys


def hook_bytes_agree(row, run):
    """The generator's hook_bytes match, redone from public files; None when the row's hook_bytes has another shape."""
    hb = row.get("hook_bytes")
    got = {k: v for k, v in (run.get("hook_output_bytes") or {}).items() if v}
    if isinstance(hb, dict) and hb:
        want = {}
        for k, v in hb.items():
            name = k.split(":", 1)[1] if ":" in k else k
            want[name] = want.get(name, 0) + int(v or 0)
        return {k: v for k, v in want.items() if v} == got
    if hb in ({}, None, 0):
        return not got
    return None


def schema_errors(r, row=None):
    """The fields a reader can check without the private stream (B19-R44); [] when all hold."""
    bad = []
    for f in ("stream_sha256", "hook_context_sha256"):
        if not well_formed(r.get(f)):
            bad.append(f)
    if not whole(r.get("stream_bytes"), positive=True):
        bad.append("stream_bytes")
    if not whole(r.get("hook_responses")):
        bad.append("hook_responses")
    hob = r.get("hook_output_bytes")
    if not isinstance(hob, dict) or not all(whole(v) for v in hob.values()):
        bad.append("hook_output_bytes")
    if whole(r.get("hook_responses")) and well_formed(r.get("hook_context_sha256")) and \
            (r["hook_responses"] == 0) != (r["hook_context_sha256"] == EMPTY):
        bad.append("hook_context_sha256 vs hook_responses")
    mr = r.get("matches_row")
    want = expected_match_keys(row) if row is not None else None
    if not isinstance(mr, dict) or not mr or not all(isinstance(v, bool) for v in mr.values()) \
            or not set(mr) <= MATCH_KEYS or (want is not None and set(mr) != want) \
            or (want is None and "hook_bytes" not in mr):
        bad.append("matches_row keys")
    return bad


def declares_disagreement(r):
    mr = r.get("matches_row")
    return r.get("status") != "committed" or (isinstance(mr, dict) and not all(v is True for v in mr.values()))


def check_files(runs, events, dup_runs, dup_events, counted=None):
    missing_root = [k for k, r in runs.items() if "events_root_sha256" not in r]
    missing_v2 = [k for k, r in runs.items() if "events_root_v2_sha256" not in r]
    malformed = [k for k, r in runs.items() if ("events_root_sha256" in r and not well_formed(r["events_root_sha256"]))
                 or ("events_root_v2_sha256" in r and not well_formed(r["events_root_v2_sha256"]))]
    bad = [k for k, r in runs.items() if well_formed(r.get("events_root_sha256"))
           and root_of(events.get(k, [])) != r["events_root_sha256"]]
    bad_v2 = [k for k, r in runs.items() if well_formed(r.get("events_root_v2_sha256"))
              and root_v2(events.get(k, [])) != r["events_root_v2_sha256"]]
    missing = [k for k, r in runs.items() if r.get("hook_responses") and k not in events]
    count, seqs, nbytes = [], [], []
    for k, r in runs.items():
        if "hook_responses" not in r:
            continue
        evs = events.get(k, [])
        if len(evs) != r["hook_responses"]:
            count.append(k)
        if sorted(e["seq"] for e in evs) != list(range(len(evs))):
            seqs.append(k)
        per = {}
        for e in evs:
            per[e["hook_name"]] = per.get(e["hook_name"], 0) + e["output_bytes"]
        want = {n: b for n, b in (r.get("hook_output_bytes") or {}).items() if b}
        if {n: b for n, b in per.items() if b} != want:
            nbytes.append(k)
    orphan = [k for k in events if k not in runs]
    counted = counted or {}
    schema = [(k, e) for k, e in ((k, schema_errors(r, counted.get(k) if counted else None)) for k, r in runs.items()) if e]
    declared = [k for k, r in runs.items() if declares_disagreement(r)]
    uncounted = [k for k in runs if counted and k not in counted]
    hb_public = [k for k, r in runs.items() if k in counted and hook_bytes_agree(counted[k], r) is False]
    found = {"missing_root": missing_root, "missing_v2_root": missing_v2, "malformed_root": malformed,
             "root_does_not_rebuild": bad, "v2_root_does_not_rebuild": bad_v2, "run_missing_its_events": missing,
             "count_differs_from_hook_responses": count, "positions_not_0_to_n": seqs, "byte_totals_differ": nbytes,
             "events_with_no_run": orphan, "duplicate_run": dup_runs, "duplicate_event": dup_events,
             "schema": schema, "declares_stream_disagrees": declared, "run_with_no_counted_row": uncounted,
             "public_hook_bytes_disagree": hb_public, "duplicate_json_member": list(DUP_MEMBERS)}
    return found


def main():
    args = sys.argv[1:]
    if args[:1] == ["--files"]:
        runs, events, dup_runs, dup_events = load(*(args[1:3] if len(args) >= 3 else []))
        folder = os.path.dirname(os.path.abspath(args[1])) if len(args) >= 3 else HERE
        counted = counted_rows(folder)
        found = check_files(runs, events, dup_runs, dup_events, counted)
        n = len(runs)
        print("runs %d, event rows %d, roots present %d/%d, v2 roots present %d/%d" % (
            n, sum(len(v) for v in events.values()), n - len(found["missing_root"]), n,
            n - len(found["missing_v2_root"]), n))
        failed = {k: v for k, v in found.items() if v}
        for k, v in found.items():
            print("  %-34s %d%s" % (k, len(v), (" e.g. %s" % (v[0],)) if v else ""))
        print("  counted rows beside the files: %s" % (
            "%d, matches_row keys and the hook-bytes match checked against them" % len(counted) if counted else
            "none found (roundN/results.jsonl): matches_row keys checked against the generator's key set only"))
        print("  stream_sha256, stream_bytes, hook_context_sha256: form checked for %d rows; values UNVERIFIED_PRIVATE "
              "(they bind private streams; the holder's recomputation is PRIVATE_HOLDER_RECEIPT_2026-09-28.json)" % n)
        print("FAIL: " + ", ".join(sorted(failed)) if failed else "PASS")
        return 1 if failed else 0
    rnd, iid, arm, seq, path = args[0], args[1], args[2], int(args[3]), args[4]
    runs, events, dup_runs, dup_events = load()
    key = (rnd, iid, arm)
    evs = events.get(key, [])
    ev = next((e for e in evs if e["seq"] == seq), None)
    if ev is None or key not in runs:
        print("no committed event %s seq %d" % (key, seq))
        return 1
    raw = open(path, "rb").read()
    ok_event = hashlib.sha256(raw).hexdigest() == ev["output_sha256"]
    ok_len = len(raw) == ev["output_bytes"]
    ok_root = well_formed(runs[key].get("events_root_sha256")) and root_of(evs) == runs[key]["events_root_sha256"]
    ok_v2 = well_formed(runs[key].get("events_root_v2_sha256")) and root_v2(evs) == runs[key]["events_root_v2_sha256"]
    ok_once = (key not in dup_runs) and not any(d[0] == key for d in dup_events)
    print("output %s the committed one (%s, %d bytes committed, %d disclosed); the run's event list %s its committed "
          "root and %s its byte-count root%s" % (
              "is" if ok_event else "is NOT", ev["hook_name"], ev["output_bytes"], len(raw),
              "rebuilds to" if ok_root else "does NOT rebuild to", "rebuilds to" if ok_v2 else "does NOT rebuild to",
              "" if ok_once else "; the run or one of its events appears twice"))
    return 0 if ok_event and ok_len and ok_root and ok_v2 and ok_once else 1


if __name__ == "__main__":
    sys.exit(main())
