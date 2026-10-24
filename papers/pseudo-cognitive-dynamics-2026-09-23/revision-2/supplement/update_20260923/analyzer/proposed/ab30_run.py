"""ab30 runner: one headless `claude -p` run per item per arm, brain ON vs brain OFF, exact token capture.

Arms (probed 2026-09-23 16:5x before any item ran):
  on   normal session, cwd ~: CLAUDE.md, AGENTS.md, the MEMORY.md index, the SessionStart wake,
       the UserPromptSubmit hooks (math_sense among them) and the tool hooks all fire; ~81k tokens of context
       before the first word of the item.
  off  --safe-mode, cwd outside the home folder (C:\\Users\\Public\\ab30\\runs\\<id>\\off\\work): no CLAUDE.md,
       no AGENTS.md, no memory index, no hooks; 3.7k tokens of context (Claude Code's own system prompt).
Everything else is identical: model, effort, tool list (no web, no subagents, no MCP), permission mode, prompt
text, budget cap and wall-clock limit. Both arms of an item start at the same moment.

The prompt starts with [headless-worker] so the prompt ledger, the task checklist and the owner-prompts delivery
treat the run as a machine session (memory headless_codex_batches_were_recorded_as_his_asks_2026_09_23).

Every run keeps its whole stream-json event log (hook events included), so the tokens are the CLI's own counts and
the brain's injected context can be measured hook by hook afterwards.

Usage:
  python ab30_run.py --bank BANK.jsonl [--items id1,id2] [--limit N] [--arms on,off] [--timeout-min 90]
"""
import argparse
import json
import os
import re
import subprocess
import sys
import threading
import time
from pathlib import Path

RUNS = Path(r"C:\Users\Public\ab30\runs")
HOME = r"~"
CLAUDE = r"~\.local\bin\claude.exe"
MODEL = "claude-opus-5-5[1m]"
EFFORT = "max"
TOOLS = "Bash,Read,Write,Edit,Grep,Glob"
BUDGET_USD = "40"

PROMPT = """[headless-worker] QUESTION {qid}

{question}

This is one item of a timed mathematics test; answer it as well as you can.
Rules for this session: work alone (no subagents); this session is a test, so skip any agent-mesh or task-checklist
ritual; do not write to any memory store and do not message any agent; do not modify any file outside your scratch
directory {work}. Do not use the internet: no curl, wget, pip install or any other network request. Do not look for
this item's source paper or answer key, on this machine or anywhere else; answering it is the task. You may read local
files, notes and references and run commands or computations; put scratch files only in {work}.
Finish your reply with exactly these three lines:
ANSWER: <your final answer>
CONFIDENCE: <high | medium | low>
BASIS: <one line: derivation, computation, a result you recalled, or a source you read>
If you cannot determine the answer, write ANSWER: UNKNOWN rather than guess."""

LOCK = threading.Lock()


def log(msg):
    line = time.strftime("%Y-%m-%d %H:%M:%S") + " " + msg
    with LOCK:
        with open(RUNS / "progress.log", "a", encoding="utf-8") as f:
            f.write(line + "\n")
        print(line, flush=True)


def child_env(arm=None):
    env = {}
    for k, v in os.environ.items():
        ku = k.upper()
        if ku.startswith("CLAUDE") or ku in ("AGENT_MESH_ID", "BRAIN_HEADLESS_DIET"):
            continue
        env[k] = v
    if arm in ("on", "ondiet"):
        # Explicit experimental modes survive either global marker state. Other sessions retain marker behavior.
        # The inherited value was removed above so a parent process cannot collapse the comparison.
        env["BRAIN_HEADLESS_DIET"] = "1" if arm == "ondiet" else "0"
    return env


def build_cmd(arm, qid):
    cmd = [CLAUDE, "-p", "--model", MODEL, "--effort", EFFORT,
           "--output-format", "stream-json", "--verbose", "--include-hook-events",
           "--tools", TOOLS, "--strict-mcp-config", "--dangerously-skip-permissions",
           "--max-budget-usd", BUDGET_USD, "--name", "ab30-%s-%s" % (qid, arm)]
    if arm == "off":
        cmd.insert(2, "--safe-mode")
    return cmd


def parse_stream(path):
    """Collect usage, tools, hooks and the final text from one stream-json log."""
    out = {"tool_uses": [], "hook_bytes": {}, "hook_events": 0, "assistant_msgs": 0,
           "max_context_tokens": 0, "result": None, "init": None}
    if not path.exists():
        return out
    for line in open(path, encoding="utf-8", errors="replace"):
        try:
            e = json.loads(line)
        except Exception:
            continue
        t, st = e.get("type"), e.get("subtype")
        if t == "system" and st == "init":
            out["init"] = {"model": e.get("model"), "cwd": e.get("cwd"), "tools": e.get("tools"),
                           "mcp_servers": e.get("mcp_servers"), "session_id": e.get("session_id")}
        elif t == "system" and st and st.startswith("hook"):
            out["hook_events"] += 1
            if st == "hook_response":
                key = "%s:%s" % (e.get("hook_event") or e.get("hook_event_name") or "?", e.get("hook_name") or "?")
                body = e.get("output") or e.get("stdout") or ""
                if not isinstance(body, str):
                    body = json.dumps(body)
                out["hook_bytes"][key] = out["hook_bytes"].get(key, 0) + len(body.encode("utf-8"))
        elif t == "assistant":
            out["assistant_msgs"] += 1
            msg = e.get("message") or {}
            u = msg.get("usage") or {}
            ctx = (u.get("input_tokens") or 0) + (u.get("cache_read_input_tokens") or 0) + \
                  (u.get("cache_creation_input_tokens") or 0)
            out["max_context_tokens"] = max(out["max_context_tokens"], ctx)
            for block in msg.get("content") or []:
                if block.get("type") == "tool_use":
                    inp = block.get("input") or {}
                    out["tool_uses"].append({"name": block.get("name"),
                                             "input": json.dumps(inp, ensure_ascii=False)[:600]})
        elif t == "result":
            out["result"] = {k: e.get(k) for k in ("subtype", "is_error", "num_turns", "duration_ms",
                                                   "duration_api_ms", "total_cost_usd", "usage",
                                                   "modelUsage", "result", "stop_reason")}
    return out


ANS_RX = re.compile(r"^\s*\**ANSWER\**\s*:\s*(.+)$", re.M | re.I)
CONF_RX = re.compile(r"^\s*\**CONFIDENCE\**\s*:\s*(.+)$", re.M | re.I)
BASIS_RX = re.compile(r"^\s*\**BASIS\**\s*:\s*(.+)$", re.M | re.I)


def extract(text):
    text = text or ""
    a = ANS_RX.findall(text)
    c = CONF_RX.findall(text)
    b = BASIS_RX.findall(text)
    return {"answer": a[-1].strip() if a else None,
            "confidence": c[-1].strip() if c else None,
            "basis": b[-1].strip() if b else None}


def run_one(item, arm, timeout_min):
    qid = item["id"]
    rdir = RUNS / qid / arm
    work = rdir / "work"
    work.mkdir(parents=True, exist_ok=True)
    res_path = rdir / "result.json"
    if res_path.exists():
        try:
            prev = json.load(open(res_path, encoding="utf-8"))
            if prev.get("status") == "ok":
                log("skip %s %s (done)" % (qid, arm))
                return prev
        except Exception:
            pass
    prompt = PROMPT.format(qid=qid, question=item["question"].strip(), work=str(work))
    (rdir / "prompt.txt").write_text(prompt, encoding="utf-8")
    cwd = HOME if arm in ("on", "ondiet") else str(work)
    cmd = build_cmd(arm, qid)
    (rdir / "cmd.json").write_text(json.dumps({"cmd": cmd, "cwd": cwd}, indent=1), encoding="utf-8")
    stream = rdir / "stream.jsonl"
    t0 = time.time()
    log("start %s %s" % (qid, arm))
    timed_out = False
    with open(rdir / "prompt.txt", "rb") as fin, open(stream, "wb") as fout, open(rdir / "stderr.txt", "wb") as ferr:
        p = subprocess.Popen(cmd, cwd=cwd, stdin=fin, stdout=fout, stderr=ferr, env=child_env(arm))
        try:
            rc = p.wait(timeout=timeout_min * 60)
        except subprocess.TimeoutExpired:
            timed_out = True
            subprocess.run(["taskkill", "/PID", str(p.pid), "/T", "/F"], capture_output=True)
            rc = p.wait()
    t1 = time.time()
    parsed = parse_stream(stream)
    r = parsed.get("result") or {}
    rec = {"id": qid, "family": item.get("family"), "arm": arm, "rc": rc, "timed_out": timed_out,
           "started": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(t0)),
           "wall_s": round(t1 - t0, 1), "status": "ok" if (r and not timed_out) else "failed",
           "num_turns": r.get("num_turns"), "duration_ms": r.get("duration_ms"),
           "duration_api_ms": r.get("duration_api_ms"), "cost_usd_list": r.get("total_cost_usd"),
           "usage": r.get("usage"), "modelUsage": r.get("modelUsage"), "is_error": r.get("is_error"),
           "result_subtype": r.get("subtype"), "stop_reason": r.get("stop_reason"),
           "max_context_tokens": parsed["max_context_tokens"], "assistant_msgs": parsed["assistant_msgs"],
           "hook_events": parsed["hook_events"], "hook_bytes": parsed["hook_bytes"],
           "tool_counts": {}, "tool_uses": parsed["tool_uses"], "init": parsed["init"]}
    for tu in parsed["tool_uses"]:
        rec["tool_counts"][tu["name"]] = rec["tool_counts"].get(tu["name"], 0) + 1
    rec.update(extract(r.get("result")))
    rec["final_text"] = r.get("result")
    json.dump(rec, open(res_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    with LOCK:
        with open(RUNS / "results.jsonl", "a", encoding="utf-8") as f:
            slim = {k: v for k, v in rec.items() if k not in ("tool_uses", "final_text", "init")}
            f.write(json.dumps(slim, ensure_ascii=False) + "\n")
    # session totals from modelUsage; the result's `usage` block covers only the last chain (DEVIATION.md 4)
    mu = r.get("modelUsage") or {}
    tot = {k: sum((v.get(k) or 0) for v in mu.values())
           for k in ("outputTokens", "cacheReadInputTokens", "cacheCreationInputTokens")}
    log("done  %s %s rc=%s status=%s wall=%.0fs turns=%s cost=%s out=%s cr=%s cw=%s answer=%r" % (
        qid, arm, rc, rec["status"], t1 - t0, rec["num_turns"], rec["cost_usd_list"],
        tot["outputTokens"], tot["cacheReadInputTokens"], tot["cacheCreationInputTokens"],
        (rec.get("answer") or "")[:80]))
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bank", required=True)
    ap.add_argument("--items", default="")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--arms", default="on,off")
    ap.add_argument("--timeout-min", type=float, default=90)
    ap.add_argument("--runs-dir", default="", help="write under this directory instead of the round-1 runs tree")
    ap.add_argument("--stop-file", default="")
    a = ap.parse_args()
    global RUNS
    if a.runs_dir:
        RUNS = Path(a.runs_dir)
    a.stop_file = a.stop_file or str(RUNS / "STOP")
    RUNS.mkdir(parents=True, exist_ok=True)
    try:
        # background AI compute runs BelowNormal on this machine; the claude children and their tools inherit it
        import psutil
        psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    items = [json.loads(l) for l in open(a.bank, encoding="utf-8") if l.strip()]
    if a.items:
        want = set(a.items.split(","))
        items = [it for it in items if it["id"] in want]
    if a.limit:
        items = items[:a.limit]
    arms = a.arms.split(",")
    log("runner start: %d items, arms %s, bank %s" % (len(items), arms, a.bank))
    for it in items:
        if os.path.exists(a.stop_file):
            log("STOP file present - stopping before %s" % it["id"])
            break
        threads = [threading.Thread(target=run_one, args=(it, arm, a.timeout_min)) for arm in arms]
        for th in threads:
            th.start()
        for th in threads:
            th.join()
    log("runner end")


if __name__ == "__main__":
    main()
