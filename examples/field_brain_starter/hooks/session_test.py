"""Run one whole session through the five hooks, the way a runtime calls them, and check what each one says.

Each hook has its own --selftest, which calls its functions directly. This test does what Codex or Claude Code does:
it starts every hook as a separate process, writes the event as JSON on its stdin, and reads what it prints. The
session is the ordinary one:

    session start      wake_hook        the index arrives once, and not again on the next prompt
    request            recall_hook      the festival delivery spec is handed over
                       request_hook     the request goes into the ledger (silent the first time)
    tool call          scar_hook        deleting raw footage warns; listing a folder does not
    stop, no record    write_back_hook  a turn that ends on a lesson asks for a record, once per session
    record written     new_record.py    the agent files the lesson
    stop               request_hook     --stop links the new record to the request as produced
    same request       request_hook     the second ask says it was asked before and what it produced

Everything runs on a scratch copy of memory/ with its own state folder and ledger, so the real store is not
touched. Exit 0 when every step behaves, 1 otherwise.

    python3 hooks/session_test.py           # add -v to print what each hook said
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
VERBOSE = "-v" in sys.argv[1:]


def run(script, payload, *args, env=None):
    cmd = [sys.executable, os.path.join(ROOT, script)] + list(args)
    out = subprocess.run(cmd, input=json.dumps(payload).encode("utf-8"), capture_output=True, env=env, timeout=120)
    return out.stdout.decode("utf-8", "replace").strip()


def context(out):
    """The text the model would see: additionalContext from JSON, or the plain text itself."""
    if not out:
        return ""
    try:
        data = json.loads(out)
    except ValueError:
        return out
    return (data.get("hookSpecificOutput") or {}).get("additionalContext") or data.get("reason") or ""


def ledger_events(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def main():
    work = tempfile.mkdtemp(prefix="brain_session_")
    mem = os.path.join(work, "memory")
    shutil.copytree(os.path.join(ROOT, "memory"), mem)
    old = time.time() - 3 * 86400   # the copied records were written days ago, as in a real store
    for name in os.listdir(mem):
        os.utime(os.path.join(mem, name), (old, old))
    ledger = os.path.join(work, "requests.jsonl")
    env = dict(os.environ, BRAIN_MEM_DIR=mem, BRAIN_HOOK_STATE=os.path.join(work, "state"),
               MATH_BRAIN_REQUESTS=ledger, BRAIN_WRITE_BACK="ask", PYTHONIOENCODING="utf-8")
    session = "session-test-%d" % time.time_ns()
    request = "What does the festival need from us for delivery?"
    lesson = ("The festival rejected the first upload. It turned out the delivery spec wants stereo and a"
              " 5.1 mix as separate files, not one file with both.")
    results = []

    def check(step, ok, said):
        results.append(ok)
        print("%s  %s" % ("ok  " if ok else "FAIL", step))
        if VERBOSE or not ok:
            for line in (said or "(nothing)").splitlines()[:8]:
                print("        " + line[:150])

    said = context(run("hooks/wake_hook.py", {"session_id": session, "source": "startup",
                                              "hook_event_name": "SessionStart"}, "--runtime", "claude", env=env))
    check("wake: the index arrives at session start", "reference_delivery_spec_festival" in said, said)
    said = context(run("hooks/wake_hook.py", {"session_id": session, "source": "startup",
                                              "hook_event_name": "SessionStart"}, "--runtime", "claude", env=env))
    check("wake: silent the second time in the same session", said == "", said)

    prompt = {"session_id": session, "prompt": request, "hook_event_name": "UserPromptSubmit"}
    said = context(run("hooks/recall_hook.py", prompt, env=env))
    check("recall: the delivery spec is handed over", "reference_delivery_spec_festival" in said, said)
    said = context(run("hooks/request_hook.py", prompt, env=env))
    asks = [e for e in ledger_events(ledger) if e.get("op") == "ask"]
    check("request: a new request is silent and lands in the ledger", said == "" and len(asks) == 1,
          said or json.dumps(asks))

    def tool(command):
        return {"session_id": session, "tool_name": "Bash", "tool_input": {"command": command},
                "hook_event_name": "PreToolUse"}

    said = context(run("hooks/scar_hook.py", tool("delete the raw camera footage folder to free disk space"), env=env))
    check("scar: deleting raw footage warns", bool(said), said)
    said = context(run("hooks/scar_hook.py", tool("list the files in the current folder"), env=env))
    check("scar: listing a folder is silent", said == "", said)

    stop = {"session_id": session, "last_assistant_message": lesson, "hook_event_name": "Stop"}
    out = run("hooks/write_back_hook.py", stop, env=env)
    blocked = out.startswith("{") and json.loads(out).get("decision") == "block"
    check("write-back: a lesson with no record asks for one, quoting the whole sentence",
          blocked and "5.1 mix as separate files" in context(out), context(out))
    said = context(run("hooks/write_back_hook.py", stop, env=env))
    check("write-back: it asks only once per session", said == "", said)

    subprocess.run([sys.executable, os.path.join(ROOT, "new_record.py"), "feedback",
                    "Festival delivery needs stereo and 5.1 as separate files",
                    "--why", "The first upload had both mixes in one file and was rejected.",
                    "--apply", "Export the two mixes as two files and name each one by its layout.",
                    "--link", "reference_delivery_spec_festival_2026_03_31", "--dir", mem],
                   capture_output=True, env=env, timeout=120)
    run("hooks/request_hook.py", {"session_id": session, "hook_event_name": "Stop"}, "--stop", env=env)
    made = [e for e in ledger_events(ledger) if e.get("op") == "link" and e.get("rel") == "produced"]
    check("request --stop: the new record is linked to the request as produced",
          len(made) == 1 and "stereo" in made[0].get("node", ""), json.dumps(made))

    said = context(run("hooks/request_hook.py", dict(prompt, session_id=session + "-later"), env=env))
    check("request: asked again, it says so and names what the first ask produced",
          "asked 2x" in said and "produced" in said, said)

    shutil.rmtree(work, ignore_errors=True)
    bad = results.count(False)
    print("%d of %d steps behave" % (len(results) - bad, len(results)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
