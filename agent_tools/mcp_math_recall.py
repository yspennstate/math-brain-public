# -*- coding: utf-8 -*-
"""A stdio MCP server with one tool, math_recall, that serves math_recall.py to an agent.

An agent that has this tool needs no shell to use the store: the tool runs math_recall.py (the copy beside this file)
exactly as an agent would from a shell and returns its text. Set MATHBRAIN_STORE and MATHBRAIN_BUILD_SRC as for the
other tools. Protocol: newline-delimited JSON-RPC 2.0 on stdin and stdout (initialize, tools/list, tools/call, ping).

    MATHBRAIN_RECALL_TIMEOUT   seconds before a call gives up (default 300)
    MATHBRAIN_RECALL_LOG       if set, one JSON line per call (the arguments, the length of the answer, error or not)
"""
import json
import os
import subprocess
import sys

RECALL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "math_recall.py")
TIMEOUT_S = int(os.environ.get("MATHBRAIN_RECALL_TIMEOUT", "300"))
NO_WINDOW = 0x08000000 if os.name == "nt" else 0

TOOL = {
    "name": "math_recall",
    "description": (
        "Search the math brain's store of theorems, proofs, open problems, attempts and results. Give two or three "
        "wordings of what you are looking for (the object, the theorem or method by name, the author) - they are "
        "searched together. Or pass ids (from an earlier result) to read those cards whole with every link. "
        "Stop when a card answers; a WEAK MATCH line means reword."),
    "inputSchema": {
        "type": "object",
        "properties": {
            "wordings": {"type": "array", "items": {"type": "string"},
                         "description": "one to three wordings of the search"},
            "ids": {"type": "array", "items": {"type": "string"},
                    "description": "card ids (or their printed prefixes) to read whole"},
        },
    },
}


def run_recall(args):
    ids = [str(x) for x in (args.get("ids") or []) if str(x).strip()]
    words = [str(x) for x in (args.get("wordings") or []) if str(x).strip()][:3]
    if ids:
        cmd = [sys.executable, "-X", "utf8", RECALL, "--id"] + ids[:6]
    elif words:
        cmd = [sys.executable, "-X", "utf8", RECALL, words[0]]
        for w in words[1:]:
            cmd += ["--or", w]
    else:
        return "Give wordings or ids.", True
    try:
        p = subprocess.run(cmd, capture_output=True, timeout=TIMEOUT_S, creationflags=NO_WINDOW,
                           stdin=subprocess.DEVNULL)
        out = p.stdout.decode("utf-8", "replace")
        if p.returncode != 0 and not out.strip():
            return "recall failed: " + p.stderr.decode("utf-8", "replace")[-800:], True
        return out[:40000], False
    except subprocess.TimeoutExpired:
        return "recall timed out after %d s; try fewer or different wordings" % TIMEOUT_S, True


def reply(mid, result=None, error=None):
    msg = {"jsonrpc": "2.0", "id": mid}
    if error is not None:
        msg["error"] = error
    else:
        msg["result"] = result
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()


def main():
    log = os.environ.get("MATHBRAIN_RECALL_LOG")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except ValueError:
            continue
        mid, method = req.get("id"), req.get("method", "")
        if method == "initialize":
            ver = (req.get("params") or {}).get("protocolVersion", "2024-11-05")
            reply(mid, {"protocolVersion": ver, "capabilities": {"tools": {}},
                        "serverInfo": {"name": "mathbrain", "version": "1.0"}})
        elif method == "tools/list":
            reply(mid, {"tools": [TOOL]})
        elif method == "tools/call":
            params = req.get("params") or {}
            if params.get("name") != "math_recall":
                reply(mid, error={"code": -32602, "message": "unknown tool"})
                continue
            text, is_err = run_recall(params.get("arguments") or {})
            if log:
                try:
                    with open(log, "a", encoding="utf-8") as f:
                        f.write(json.dumps({"args": params.get("arguments"), "chars": len(text), "err": is_err}) + "\n")
                except OSError:
                    pass
            reply(mid, {"content": [{"type": "text", "text": text}], "isError": is_err})
        elif method == "ping":
            reply(mid, {})
        elif mid is not None:
            reply(mid, error={"code": -32601, "message": "method not found"})


if __name__ == "__main__":
    main()
