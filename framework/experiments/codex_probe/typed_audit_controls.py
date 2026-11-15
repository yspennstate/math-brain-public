"""typed_audit_controls.py <work dir> <real rollout of probe STDIN1>: controls both ways for codex_typed_audit.py.

  P1  a made-up rollout whose worker TYPES 'python tool.py --help' into an open shell (tool.py exists, unapproved):
      the audit must refuse that line (exit 4, one refusal) and pass the harmless line beside it.
  N1  the same made-up rollout with the same command run as its own exec_command (hooked by Codex itself): the audit
      must report no typed refusal (exit 0); it checks typed lines only.
  N2  the real rollout of probe STDIN1 (four harmless typed lines): exit 0, and it must have READ four typed lines.
  P2  a typed text built at run time (not a literal): the audit must say it could not read it.
  B1  the guard file swapped for one that never answers 'deny' (a guard-less run): P1's rollout then passes, which
      shows the refusal in P1 comes from the guard and not from the audit's own text matching.
Nothing typed is ever run; tool.py is only hashed by the guard."""
import io
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
AUDIT = os.path.join(HERE, "codex_typed_audit.py")
work, real = sys.argv[1], sys.argv[2]
cw = os.path.join(work, "syn_cwd")
os.makedirs(cw, exist_ok=True)
io.open(os.path.join(cw, "tool.py"), "w", encoding="utf-8").write("print('ran')\n")
io.open(os.path.join(work, "guard_silent.py"), "w", encoding="utf-8").write("import sys\nsys.stdin.read()\n")


def rollout(name, inputs):
    p = os.path.join(work, name)
    with io.open(p, "w", encoding="utf-8") as fh:
        fh.write(json.dumps({"type": "session_meta", "payload": {"id": "syn-" + name, "cwd": cw, "cli_version": "0.160.0"}}) + "\n")
        for s in inputs:
            fh.write(json.dumps({"type": "response_item", "payload": {"type": "custom_tool_call", "name": "exec", "input": s}}) + "\n")
    return p


def run(args):
    r = subprocess.run([sys.executable, "-B", AUDIT] + args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=600,
                       creationflags=0x08000000 if os.name == "nt" else 0)
    return r.returncode, r.stdout.decode("utf-8", "replace")


typed_bad = "text(await tools.write_stdin({session_id:1,chars:'python tool.py --help\\r',yield_time_ms:1000}));"
typed_ok = "text(await tools.write_stdin({session_id:1,chars:'python -c \"print(\\'B1\\')\"\\r',yield_time_ms:1000}));"
poll = "text(await tools.write_stdin({session_id:1,chars:'',yield_time_ms:1000}));"
own_bad = "text(await tools.exec_command({cmd:'python tool.py --help',yield_time_ms:1000}));"
built = "const c = 'python tool.py --he' + 'lp\\r'; text(await tools.write_stdin({session_id:1,chars:c,yield_time_ms:1000}));"
ok = True


def check(tag, good, rc, out):
    global ok
    ok = ok and good
    print("%s %s (exit %d)" % (tag, "PASS" if good else "FAIL", rc))
    for ln in out.strip().split("\n")[:6]:
        print("      " + ln[:230])


rc, out = run([rollout("p1.jsonl", [typed_ok, poll, typed_bad])])
check("P1 typed --help on an unapproved script is refused, the harmless line is not", rc == 4 and "refused: 1" in out and "typed 2" in out and "polls 1" in out, rc, out)
rc, out = run([rollout("n1.jsonl", [typed_ok, poll, own_bad])])
check("N1 the same command as its own process is not a typed refusal", rc == 0 and "refused: 0" in out and "own commands 1" in out, rc, out)
rc, out = run([real])
check("N2 the real probe rollout: four typed lines read, none refused", rc == 0 and "typed 4" in out and "refused: 0" in out, rc, out)
rc, out = run([rollout("p2.jsonl", [built])])
check("P2 a typed text built at run time is reported as not read", "NOT READ: 1" in out and "typed but not a literal 1" in out, rc, out)
rc, out = run([os.path.join(work, "p1.jsonl"), "--guard", os.path.join(work, "guard_silent.py")])
check("B1 with a guard that never refuses, P1's rollout passes", rc == 0 and "refused: 0" in out and "typed 2" in out, rc, out)
print("ALL PASS" if ok else "SOME FAILED")
sys.exit(0 if ok else 1)
