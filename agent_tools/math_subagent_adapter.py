"""math_subagent_adapter.py - the math store's cards reach research subagents too (29 Sep 2026, job R70; scheduled
audits fleet04/B14 r7, fleet01/B14 r83 and fleet02/B05; the interactive review MB-IMPROVEMENT-20260929-155540,
findings MB-I01 to MB-I03).

The math hook runs on prompt events, and a subagent's task never is one: the parent writes it into an Agent tool call,
and the child starts with that text as its first message. In the week to 29 Sep, 868 Agent calls went out and 113 of
them carried a mathematical task; none received a card (the 24 Sep count was 0 of 41 research subagents).

This is a PreToolUse hook on Agent|Task, run by the dispatcher. It hands the child's task to math_sense.py exactly as a
prompt event would, under a session id of the child's own, and when the hook answers it appends the block to the
child's task through the tool's updatedInput. It makes no permission decision: Claude Code 2.1.284 applies updatedInput
without one, in bypass and in manual mode (probed 29 Sep with a one-hook headless session). A child the hook does not
answer gets its task untouched, and so does every child when anything here fails.

    MATHBRAIN_SUBAGENT_ADAPTER   off | shadow | serve (default since 30 Sep 2026)
        shadow  every eligible child runs through the hook in shadow (MATHBRAIN_SHADOW=1: nothing recorded as served)
                and nothing is appended; the ledger shows what would have been served and what it cost in time
        serve   a child is held back with probability MATHBRAIN_SUBAGENT_HOLD (0.2) and run in shadow; the rest are
                run normally and served. The draw is a hash of the parent session's id, the description and the task:
                a call repeated from the same session keeps its arm, and a reworded description, a changed task or
                another session draws afresh. That cluster, not the call, is the unit of assignment, so repeated calls
                are not independent samples; --summary counts invocations and clusters apart (MB-I03)
    ledger  ~/.claude/brain_graph/live/math_subagent_serves.jsonl: one row per eligible Agent call; ids and digests
            only, never the task text. A row is the adapter's decision, made before any child exists:
            injection_requested says it asked the harness to append the block. `delivered`, the field's only name
            until 29 Sep, is kept with the same value and never meant that a child received anything (MB-I01): what
            the harness applied and what the child received are math_subagent_receipt.py's rows, joined by the call id
    faults  a row that cannot be written is a known outcome, not a silent one (MB-I02). The card is withheld - the
            child runs with its task untouched, so no card goes out that the ledger cannot account for - and the
            fault's category, never text, goes to ~/.claude/dreaming/logs/math_subagent_faults.jsonl, or to stderr
            when that fails too

The child's session id is uuid-shaped and derived from the parent's id and the task, so the hook's logs count the
child as its own session and never as the parent. When the harness gives the tool call's id (tool_use_id, the same id
its PostToolUse event carries), the child's session id takes it too and the ledger row records it: two calls of one task
are two sessions and two rows a later event can be joined to, while the arm still comes from the cluster alone
(fleet01/B05 r91, B05-R70-SUBAGENT-LEDGER-NO-TOOLUSE-JOIN-42). A math hook that exits with an error is never served,
whatever it printed (fleet01/B14 r91, B14-R91-R70-NONZERO-HOOK-EXIT-STILL-INJECTS). The frame that opens a served
block carries the row's delivery id, "(delivery <id>)", so the child's own transcript can show that it got this block.

    python math_subagent_adapter.py --summary [--since HOURS]    invocations, clusters and receipt stages per arm
"""
import errno
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
MATH_SENSE = os.environ.get("MATHBRAIN_SUBAGENT_HOOK") or os.path.join(HERE, "math_sense.py")   # tests point it at a stand-in
LEDGER = os.environ.get("MATHBRAIN_SUBAGENT_LEDGER") or os.path.join(
    os.path.expanduser("~"), ".claude", "brain_graph", "live", "math_subagent_serves.jsonl")
RECEIPTS = os.environ.get("MATHBRAIN_SUBAGENT_RECEIPTS") or os.path.join(os.path.dirname(LEDGER),
                                                                         "math_subagent_receipts.jsonl")
FAULTS = os.environ.get("MATHBRAIN_SUBAGENT_FAULTS") or os.path.join(HERE, "logs", "math_subagent_faults.jsonl")
# SERVE BY DEFAULT (30 Sep 2026, claude-825b1305, the owner's 14:09 order to get relevant knowledge to agents as fast as
# possible). Shadow saw 273 tasks, all film or helper work the math gate rightly refused, so it measured nothing. Replayed
# in shadow, the 24 research-subagent tasks of 22-24 Sep (FEI, QFORM; 41 subagents that got no card then) would get a
# block on 20, mostly on their subject: the LTF-FEI task gets the proven 14.22 bound, the monotone task the failed routes.
# A fifth of tasks stay held back as the control (MATHBRAIN_SUBAGENT_HOLD). MATHBRAIN_SUBAGENT_ADAPTER=shadow rolls back.
MODE = os.environ.get("MATHBRAIN_SUBAGENT_ADAPTER", "serve").strip().lower()
try:
    HOLD = min(1.0, max(0.0, float(os.environ.get("MATHBRAIN_SUBAGENT_HOLD", "0.2"))))
except ValueError:
    HOLD = 0.2
HOOK_BUDGET_S = 10.0      # the math hook's own budget; the dispatcher kills a PreToolUse hook at 15 s
KILL_S = 12.5
MIN_TASK_CHARS = 40
CLAIM_ID = re.compile(r"\bclaim_[0-9a-f]{16,64}\b")
# the block opens with its own "leads, not verdicts" line; the frame marks where the task ends and names the delivery
FRAME_TEXT = "The math hook attached these cards from the math store to your task"
NEWLINE = b"\r\n" if os.name == "nt" else b"\n"      # what the text-mode writer before 29 Sep put in the ledger
CREATE_NO_WINDOW = 0x08000000
STAGES = ("harness_applied", "frame_seen", "child_received", "block_complete", "block_exact", "source_opened",
          "cited_in_answer")


# kept with the stages when receipts are merged, not a stage itself: how block_exact was decided (receipt contract 2,
# 30 Sep) - full, prefix, ambiguous_frame or malformed_expectation
RECEIPT_NOTES = ("exact_basis",)


def mark(delivery):
    return "(delivery %s)" % delivery


def frame(delivery):
    return "\n\n---\n%s %s:\n" % (FRAME_TEXT, mark(delivery))


def child_identity(parent, description, task, invocation=""):
    """(key, child session id, draw in [0, 1)). The key and the draw come from the parent's session id, the description
    and the task - the cluster that keeps its arm however often it is sent; the session id also takes the tool call's
    id when there is one."""
    h = hashlib.sha256(("%s\n%s\n%s" % (parent, description, task)).encode("utf-8", "replace")).hexdigest()
    s = hashlib.sha256(("%s\n%s" % (h, invocation)).encode("utf-8", "replace")).hexdigest() if invocation else h
    child = "%s-%s-4%s-8%s-%s" % (s[:8], s[8:12], s[13:16], s[17:20], s[20:32])
    return h[:16], child, int(h[32:40], 16) / float(0x100000000)


def arm_for(mode, draw, hold=HOLD):
    if mode == "serve":
        return "held" if draw < hold else "served"
    return "shadow"


def run_math_hook(task, child, shadow, timeout=KILL_S, script=MATH_SENSE):
    """(block, seconds, error): the math hook's answer to the child's task, as a prompt event would get it."""
    payload = {"hook_event_name": "UserPromptSubmit", "prompt": task, "session_id": child}
    env = dict(os.environ)
    env["MATHBRAIN_TIME_BUDGET_S"] = str(HOOK_BUDGET_S)
    env["MATHBRAIN_SHADOW"] = "1" if shadow else "0"
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, "-s", script], input=json.dumps(payload).encode("utf-8"),
                           capture_output=True, timeout=timeout, env=env,
                           creationflags=CREATE_NO_WINDOW if os.name == "nt" else 0)
    except subprocess.TimeoutExpired:
        return "", time.time() - t0, "timeout"
    except OSError as exc:
        return "", time.time() - t0, "oserror:%s" % type(exc).__name__
    if r.returncode != 0:
        # an error exit is not an answer, even when what the hook printed before it failed parses
        return "", time.time() - t0, "rc%d" % r.returncode
    out = r.stdout.decode("utf-8", "replace").strip()
    if not out:
        return "", time.time() - t0, ""
    try:
        block = json.loads(out[out.find("{"):]).get("hookSpecificOutput", {}).get("additionalContext") or ""
    except ValueError:
        return "", time.time() - t0, "bad_json"
    return str(block), time.time() - t0, ""


FAULT_NAMES = {errno.ENOSPC: "no_space", errno.EISDIR: "not_a_file", errno.EACCES: "permission",
               errno.EPERM: "permission", errno.ENOENT: "missing", errno.EROFS: "read_only"}


def _fault(stage, exc, path=None):
    code = getattr(exc, "errno", None)
    if path is not None and os.path.isdir(path):
        name = "not_a_file"       # Windows reports a folder opened as a file as a permission error
    else:
        name = FAULT_NAMES.get(code) or (errno.errorcode.get(code, "oserror") if code else "oserror")
    return "%s:%s" % (stage, name)


def append_line(row, path):
    """(ok, fault): one JSON line appended in a single write. A failure comes back as a bounded category, never as text
    from the row. A line that an interrupted append left unterminated is closed first, so it cannot swallow this row."""
    try:
        line = json.dumps(row, separators=(",", ":")).encode("utf-8") + NEWLINE
    except (TypeError, ValueError):
        return False, "serialize"
    try:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    except OSError as exc:
        return False, _fault("folder", exc)
    try:
        fd = os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT | getattr(os, "O_BINARY", 0), 0o644)
    except OSError as exc:
        return False, _fault("open", exc, path)
    try:
        try:
            size = os.fstat(fd).st_size
            if size:
                with open(path, "rb") as fh:
                    fh.seek(size - 1)
                    if fh.read(1) != b"\n":
                        line = NEWLINE + line
        except OSError:
            pass
        if os.write(fd, line) != len(line):
            return False, "write:short"
        return True, ""
    except OSError as exc:
        return False, _fault("write", exc)
    finally:
        try:
            os.close(fd)
        except OSError:
            pass


def ledger_row(row, path=None):
    return append_line(row, path or LEDGER)


def record_fault(row, path=None):
    """Put a fault where it can be counted; stderr when even that fails. Returns whether the fault log took it."""
    ok, fault = append_line(row, path or FAULTS)
    if not ok:
        try:
            sys.stderr.write("math_subagent_adapter: the ledger and the fault log both failed (%s; %s); the card was "
                             "withheld\n" % (row.get("fault"), fault))
        except Exception:
            pass
    return ok


def decide(data, mode=MODE, runner=run_math_hook, ledger=ledger_row, faults=record_fault):
    """The hook's JSON answer (a dict) or None. Never raises. `ledger` returns (ok, fault); anything else is a fault."""
    try:
        if mode not in ("shadow", "serve") or data.get("tool_name") not in ("Agent", "Task"):
            return None
        inp = data.get("tool_input")
        if not isinstance(inp, dict) or not isinstance(inp.get("prompt"), str):
            return None
        task = inp["prompt"]
        if len(task.strip()) < MIN_TASK_CHARS:
            return None
        parent = str(data.get("session_id") or "")
        invocation = str(data.get("tool_use_id") or "")[:128]
        key, child, draw = child_identity(parent, str(inp.get("description") or ""), task, invocation)
        arm = arm_for(mode, draw)
        block, seconds, error = runner(task, child, shadow=(arm != "served"))
        delivery = uuid.uuid4().hex[:16]
        row = {"t": round(time.time(), 1), "delivery": delivery, "parent": parent[:64], "child": child,
               "tool_use_id": invocation[:64],
               "key": key, "type": str(inp.get("subagent_type") or ""), "model": str(inp.get("model") or ""),
               "mode": mode, "arm": arm, "answered": bool(block), "chars": len(block),
               "block": hashlib.sha256(block.encode("utf-8")).hexdigest()[:16] if block else "",
               # receipt contract 2 (30 Sep): the full digest and the UTF-8 byte count of what was served, so a receipt
               # can check the received bytes exactly; "block" stays for rows and readers from before
               "block_sha256": hashlib.sha256(block.encode("utf-8")).hexdigest() if block else "",
               "block_bytes": len(block.encode("utf-8")) if block else 0, "receipt_contract": 2,
               "ids": sorted(set(CLAIM_ID.findall(block)))[:12], "seconds": round(seconds, 2), "error": error}
        requested = bool(block) and arm == "served"
        row["injection_requested"] = requested
        row["delivered"] = requested      # the same decision under its name until 29 Sep; never a receipt (MB-I01)
        status = ledger(row)
        ok, fault = status if isinstance(status, tuple) and len(status) == 2 else (False, "ledger:no_status")
        if not ok:
            faults({"t": row["t"], "delivery": delivery, "tool_use_id": row["tool_use_id"], "key": key, "mode": mode,
                    "arm": arm, "stage": "ledger", "fault": str(fault)[:64], "injection_requested": requested,
                    "withheld": requested})
            return None
        if not requested:
            return None
        new = dict(inp)
        new["prompt"] = task + frame(delivery) + block
        return {"hookSpecificOutput": {"hookEventName": "PreToolUse", "updatedInput": new}}
    except Exception:
        return None


def read_rows(path):
    """The JSON objects of a JSONL file; a torn line (an interrupted append) is skipped, never fatal."""
    rows = []
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except ValueError:
                    continue
                if isinstance(obj, dict):
                    rows.append(obj)
    except OSError:
        pass
    return rows


def merged_receipts(path=None):
    """delivery -> the latest recorded value of each receipt stage (a later row fills or corrects an earlier null)."""
    out = {}
    for r in read_rows(path or RECEIPTS):
        d = r.get("delivery")
        if not d:
            continue
        cur = out.setdefault(d, {})
        for k in STAGES + RECEIPT_NOTES:
            if r.get(k) is not None:
                cur[k] = r[k]
    return out


def summarize(since_hours=None, ledger=None, receipts=None, faults=None):
    """{(mode, arm): counts}: invocations and clusters apart (MB-I03), the decision, and each receipt stage as
    true / false / unknown. Nothing here is a benefit: a graded outcome is a test's to give."""
    rows = read_rows(ledger or LEDGER)
    if since_hours:
        cut = time.time() - float(since_hours) * 3600.0
        rows = [r for r in rows if float(r.get("t") or 0) >= cut]
    rec = merged_receipts(receipts)
    out = {}
    for r in rows:
        g = out.setdefault((str(r.get("mode")), str(r.get("arm"))), {
            "invocations": 0, "clusters": set(), "answered": 0, "injection_requested": 0, "hook_errors": 0,
            "stages": {k: [0, 0, 0] for k in STAGES}})
        g["invocations"] += 1
        g["clusters"].add(r.get("key"))
        g["answered"] += bool(r.get("answered"))
        g["injection_requested"] += bool(r.get("injection_requested", r.get("delivered")))
        g["hook_errors"] += bool(r.get("error"))
        got = rec.get(r.get("delivery"), {})
        for k in STAGES:
            v = got.get(k)
            g["stages"][k][0 if v is True else 1 if v is False else 2] += 1
    for g in out.values():
        g["clusters"] = len(g["clusters"])
    fault_rows = read_rows(faults or FAULTS)
    return out, {"faults": len(fault_rows), "withheld": sum(1 for f in fault_rows if f.get("withheld"))}


def print_summary(since_hours=None):
    groups, faults = summarize(since_hours)
    print("math subagent adapter%s: a cluster is one (parent session, description, task); effects are counted over "
          "clusters, never invocations" % ((" - the last %s h" % since_hours) if since_hours else ""))
    for (mode, arm), g in sorted(groups.items()):
        print("  %s/%s: %d invocations in %d clusters; answered %d, injection requested %d, hook errors %d"
              % (mode, arm, g["invocations"], g["clusters"], g["answered"], g["injection_requested"], g["hook_errors"]))
        print("    " + "; ".join("%s %d/%d/%d" % (k, *g["stages"][k]) for k in STAGES) + "   (true/false/unknown)")
    print("  ledger faults %d, cards withheld for them %d" % (faults["faults"], faults["withheld"]))


def main():
    try:
        raw = sys.stdin.buffer.read().decode("utf-8", "replace")
        data = json.loads(raw[raw.find("{"):]) if "{" in raw else {}
    except Exception:
        return 0
    answer = decide(data if isinstance(data, dict) else {})
    if answer:
        sys.stdout.write(json.dumps(answer))
    return 0


if __name__ == "__main__":
    if "-h" in sys.argv[1:] or "--help" in sys.argv[1:]:
        print(__doc__)
        raise SystemExit(0)
    if "--summary" in sys.argv[1:]:
        a = sys.argv[1:]
        print_summary(float(a[a.index("--since") + 1]) if "--since" in a else None)
        raise SystemExit(0)
    sys.exit(main())
