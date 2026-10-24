"""math_subagent_receipt.py - what a research subagent actually received from the math hook (29 Sep 2026, claude-825b1305;
finding MB-I01 of the interactive review MB-IMPROVEMENT-20260929-155540, job R70).

math_subagent_adapter.py records a decision: whether it asked the harness to append the math store's cards to a child's
task. A decision is not a receipt. This file records the evidence that comes after it, joined to the adapter's row by the
tool call's id, in ~/.claude/brain_graph/live/math_subagent_receipts.jsonl (append-only; ids and flags, never text):

    harness_applied  the prompt the harness reports it launched the child with carries the row's delivery mark; from the
                     PostToolUse event of the same call, null when that event names no prompt
    frame_seen       the child's first message carries the math hook's frame at all: false is what a held or shadow
                     child must show, true what a served one must
    child_received   the child's first message carries this row's delivery mark
    block_complete   every claim id of a served block reached the child's first message (null when nothing was sent)
    block_exact      the text after the frame in the child's first message has the sha256 prefix the adapter recorded for
                     the block: ids surviving while a hypothesis is lost reads false here (the 1000-page report's
                     D12-T04, to the brain dot's specification of 30 Sep); null for a row with no recorded digest, or
                     when the frame is not in the message
    source_opened    one of the child's tool calls names a claim id the block carried (for a held or shadow child: a
                     claim the block would have carried, which the child found by itself)
    cited_in_answer  the child's last message names such a claim id. A child can use a card without citing it, so false
                     here means "not cited", never "not used"; decided only once the child has finished
    outcome_graded   never set here: only a graded test can say whether the answer was better

A stage without evidence stays null - unknown, neither a failure nor a success - and none of these is ever a benefit.
The child's transcript is found through its meta file, <parent transcript folder>/subagents/agent-<id>.meta.json, which
names the tool call's id, so the join does not depend on what the PostToolUse event carries.

    python math_subagent_receipt.py                          PostToolUse hook: stdin is the event; also resolves a few
                                                             pending rows
    python math_subagent_receipt.py --sweep [--days N] [--dry-run]    resolve every row whose child is on disk
"""
import glob
import hashlib
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import math_subagent_adapter as msa  # noqa: E402

PROJECTS = os.environ.get("MATHBRAIN_SUBAGENT_PROJECTS") or os.path.join(os.path.expanduser("~"), ".claude", "projects")
SETTLE_S = 60.0           # a child's last message is final once it ended its turn and the file has been still this long
HOOK_SWEEP_ROWS = 5
HOOK_SWEEP_S = 1.5


def _text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(str(x.get("text") or "") for x in content if isinstance(x, dict) and x.get("type") == "text")
    return ""


def read_child(path):
    """{first, tools, last, finished}: the child's first message, its tool calls' inputs, its last words, and whether it
    has ended its turn and the transcript has settled."""
    first, tools, last, ended = None, [], "", False
    # a line that cannot be read before the first user message leaves the first message unknown: the next readable
    # user line may be a tool's answer, and reading it as the first would call a delivered block missing (30 Sep)
    first_uncertain = False
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                o = json.loads(line)
            except ValueError:
                if first is None and line.strip():
                    first_uncertain = True
                continue
            msg = o.get("message") if isinstance(o.get("message"), dict) else {}
            content = msg.get("content")
            if o.get("type") == "user":
                if first is None:
                    first = _text(content)
                else:
                    ended = False           # a tool's answer or a continued task came after its last turn: still going
            elif o.get("type") == "assistant":
                if isinstance(content, list):
                    for x in content:
                        if isinstance(x, dict) and x.get("type") == "tool_use":
                            tools.append(json.dumps(x.get("input"), ensure_ascii=False))
                said = _text(content)
                if said.strip():
                    last = said
                ended = msg.get("stop_reason") in ("end_turn", "stop_sequence")
    settled = (time.time() - os.path.getmtime(path)) >= SETTLE_S
    return {"first": None if first_uncertain else first, "tools": "\n".join(tools), "last": last,
            "finished": ended and settled, "first_uncertain": first_uncertain}


def child_evidence(row, child):
    """The child-side stages of an adapter row, from what read_child found."""
    ids = list(row.get("ids") or [])
    sent = bool(row.get("injection_requested", row.get("delivered")))
    first = child.get("first")
    ev = {k: None for k in ("frame_seen", "child_received", "block_complete", "block_exact", "source_opened",
                            "cited_in_answer", "exact_basis")}
    if first is None:
        return ev
    ev["frame_seen"] = msa.FRAME_TEXT in first
    ev["child_received"] = msa.mark(row.get("delivery", "")) in first
    if sent and ids:
        ev["block_complete"] = all(i in first for i in ids)
    # RECEIPT CONTRACT 2 (30 Sep, with the brain dot's review of PR 188). The received block is everything after the
    # one frame to the end of the first message (the strict suffix rule, unchanged). A frame that occurs more than once
    # cannot say where the block starts, so the check stays unknown rather than taking the first. A row that carries
    # the full digest and byte count (contract 2) is compared on both, exactly; a row from before carries only a
    # 16-character prefix, compared as such and named "prefix", never "full"; a malformed expectation decides nothing.
    # The expectation always comes from the sender's ledger, never from the received text.
    want = str(row.get("block") or "")
    full = str(row.get("block_sha256") or "")
    size = row.get("block_bytes")
    marker = msa.frame(row.get("delivery", ""))
    if sent and (want or full) and marker in first:
        if first.count(marker) != 1:
            ev["exact_basis"] = "ambiguous_frame"
        else:
            got = first.split(marker, 1)[1].encode("utf-8")
            if row.get("receipt_contract") or full:
                if re.fullmatch(r"[0-9a-f]{64}", full) and isinstance(size, int) and not isinstance(size, bool):
                    ev["block_exact"] = hashlib.sha256(got).hexdigest() == full and len(got) == size
                    ev["exact_basis"] = "full"
                else:
                    ev["exact_basis"] = "malformed_expectation"
            elif re.fullmatch(r"[0-9a-f]{16}", want):
                ev["block_exact"] = hashlib.sha256(got).hexdigest()[:16] == want
                ev["exact_basis"] = "prefix"
            else:
                ev["exact_basis"] = "malformed_expectation"
    if ids:
        opened = any(i in child["tools"] for i in ids)
        ev["source_opened"] = True if opened else (False if child["finished"] else None)
        ev["cited_in_answer"] = any(i in child["last"] for i in ids) if child["finished"] else None
    return ev


class Children:
    """tool call id -> the child's transcript, through the meta files under each parent's subagents folder."""

    def __init__(self, projects=PROJECTS):
        self.projects = projects
        self.by_parent = {}

    def find(self, parent, tool_use_id):
        if not parent or not tool_use_id:
            return None
        if parent not in self.by_parent:
            found = {}
            for meta in glob.glob(os.path.join(glob.escape(self.projects), "*", glob.escape(parent), "subagents",
                                               "agent-*.meta.json")):
                try:
                    with open(meta, encoding="utf-8") as fh:
                        tid = json.load(fh).get("toolUseId")
                except (OSError, ValueError, AttributeError):
                    continue
                if tid:
                    found[tid] = meta[:-len(".meta.json")] + ".jsonl"
            self.by_parent[parent] = found
        path = self.by_parent[parent].get(tool_use_id)
        return path if path and os.path.exists(path) else None


def settled(row, state):
    """Nothing more to learn for this row: every stage its evidence can decide is decided."""
    need = ["frame_seen", "child_received"]
    if row.get("ids"):
        need += ["source_opened", "cited_in_answer"]
        if row.get("injection_requested", row.get("delivered")):
            need.append("block_complete")
            if row.get("block"):
                need.append("block_exact")
    return all(state.get(k) is not None for k in need)


def sweep(ledger=None, receipts=None, projects=PROJECTS, days=None, limit=None, budget_s=None, dry_run=False):
    """Resolve the child-side stages of adapter rows whose child is on disk; append a row only when a stage changed.
    Returns the rows it appended (or would append, with dry_run)."""
    t0 = time.time()
    rows = msa.read_rows(ledger or msa.LEDGER)
    if days:
        cut = time.time() - float(days) * 86400.0
        rows = [r for r in rows if float(r.get("t") or 0) >= cut]
    state = msa.merged_receipts(receipts)
    kids = Children(projects)
    out = []
    for row in reversed(rows):                 # newest first: a bounded sweep serves the calls just made
        if limit is not None and len(out) >= limit:
            break
        if budget_s is not None and time.time() - t0 > budget_s:
            break
        d = row.get("delivery")
        have = state.get(d, {})
        if not d or settled(row, have):
            continue
        path = kids.find(row.get("parent"), row.get("tool_use_id"))
        if not path:
            continue
        try:
            ev = child_evidence(row, read_child(path))
        except OSError:
            continue
        new = {k: v for k, v in ev.items() if v is not None and have.get(k) != v}
        if not new:
            continue
        rec = {"t": round(time.time(), 1), "source": "sweep", "delivery": d, "tool_use_id": row.get("tool_use_id", ""),
               "arm": row.get("arm", ""), "agent_id": os.path.basename(path)[len("agent-"):-len(".jsonl")][:40]}
        rec.update(new)
        if not dry_run:
            ok, _ = msa.append_line(rec, receipts or msa.RECEIPTS)
            if not ok:
                break
        state.setdefault(d, {}).update(new)
        out.append(rec)
    return out


def find_row(tool_use_id, ledger=None):
    found = None
    for r in msa.read_rows(ledger or msa.LEDGER):
        if r.get("tool_use_id") == tool_use_id:
            found = r
    return found


def post(data, ledger=None, receipts=None, projects=PROJECTS):
    """PostToolUse on an Agent call the adapter saw: what the harness reports it launched. Returns the row it wrote."""
    if data.get("tool_name") not in ("Agent", "Task"):
        return None
    tid = str(data.get("tool_use_id") or "")
    row = find_row(tid, ledger) if tid else None
    if row is None:
        return None
    resp = data.get("tool_response")
    resp = resp if isinstance(resp, dict) else {}
    prompt = resp.get("prompt")
    rec = {"t": round(time.time(), 1), "source": "post", "delivery": row.get("delivery", ""), "tool_use_id": tid,
           "arm": row.get("arm", ""), "agent_id": str(resp.get("agentId") or "")[:40],
           "status": str(resp.get("status") or "")[:24],
           "harness_applied": (msa.mark(row.get("delivery", "")) in prompt) if isinstance(prompt, str) else None,
           "harness_frame": (msa.FRAME_TEXT in prompt) if isinstance(prompt, str) else None}
    ok, _ = msa.append_line(rec, receipts or msa.RECEIPTS)
    return rec if ok else None


def main():
    try:
        raw = sys.stdin.buffer.read().decode("utf-8", "replace")
        data = json.loads(raw[raw.find("{"):]) if "{" in raw else {}
    except Exception:
        return 0
    try:
        if isinstance(data, dict):
            post(data)
        sweep(days=3, limit=HOOK_SWEEP_ROWS, budget_s=HOOK_SWEEP_S)
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if "-h" in a or "--help" in a:
        print(__doc__)
        raise SystemExit(0)
    if "--sweep" in a:
        got = sweep(days=float(a[a.index("--days") + 1]) if "--days" in a else None, dry_run="--dry-run" in a)
        for r in got:
            print(json.dumps(r))
        print("%s %d row(s)" % ("would record" if "--dry-run" in a else "recorded", len(got)))
        raise SystemExit(0)
    sys.exit(main())
