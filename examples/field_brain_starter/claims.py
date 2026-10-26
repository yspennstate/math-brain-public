"""Let several agents share one brain without overwriting each other's work.

    python claims.py claim  --agent ana --resource record:the_q2_pricing_date --purpose "correct the ship date"
    python claims.py list
    python claims.py release --agent ana --resource record:the_q2_pricing_date
    python claims.py selftest

An agent claims what it is about to change, does the work, and releases it. A second agent asking for the same
resource is refused with exit code 3 and told who holds it, until the first releases or the claim expires (default
30 minutes, so a crashed agent does not block anyone for long). A claim is a promise between agents that read this
tool before they write; it locks no file.

Name resources so that two agents who mean the same thing type the same string: record:<slug> for one record,
topic:<word> for a piece of work that touches several records ("topic:pricing"), index for memory/MEMORY.md.
new_record.py takes its own short lock on the index, so writing records never needs a claim.

The claims live in claims/, one small JSON file per resource, written with an exclusive create so two agents racing
for the same free resource cannot both win. No server, no daemon, standard library only; the folder can sit on a
shared drive. framework/mesh/ is the full version (heartbeats, mailboxes, handoffs) for many agents working all day.
"""
import argparse
import hashlib
import json
import os
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
HELD = 3  # exit code when someone else holds the resource


def path_for(folder, resource):
    safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in resource)[:60]
    return os.path.join(folder, "%s_%s.json" % (safe, hashlib.sha1(resource.encode()).hexdigest()[:8]))


def read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def live(c, now=None):
    return c is not None and c.get("expires", 0) > (now or time.time())


def claim(folder, agent, resource, purpose="", minutes=30):
    """Return (True, claim) when the agent now holds the resource, (False, holder) when someone else does."""
    os.makedirs(folder, exist_ok=True)
    p = path_for(folder, resource)
    now = time.time()
    mine = {"resource": resource, "agent": agent, "purpose": purpose, "since": now, "expires": now + minutes * 60}
    for _ in range(3):
        try:
            fd = os.open(p, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            held = read(p)
            if held and held.get("agent") == agent:  # renewing your own claim
                mine["since"] = held.get("since", now)
                tmp = p + ".%d.tmp" % os.getpid()
                with open(tmp, "w", encoding="utf-8") as fh:
                    json.dump(mine, fh)
                os.replace(tmp, p)
                return True, mine
            if live(held, now):
                return False, held
            # Expired or unreadable: clear it and race for it again, but only if it is still the file we judged; another
            # agent may have cleared it and claimed afresh in the meantime.
            if read(p) == held:
                try:
                    os.remove(p)
                except FileNotFoundError:
                    pass
            continue
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(mine, fh)
        return True, mine
    return False, read(p) or {"agent": "unknown", "resource": resource}


def release(folder, agent, resource):
    p = path_for(folder, resource)
    held = read(p)
    if held is None:
        return True, "not held"
    if held.get("agent") != agent and live(held):
        return False, "held by %s" % held.get("agent")
    os.remove(p)
    return True, "released"


def listing(folder):
    if not os.path.isdir(folder):
        return []
    out = [read(os.path.join(folder, n)) for n in sorted(os.listdir(folder)) if n.endswith(".json")]
    return [c for c in out if live(c)]


def describe(c):
    left = max(0, int((c["expires"] - time.time()) / 60))
    return "%s  held by %s for %d more min%s" % (c["resource"], c["agent"], left,
                                                 ("  (" + c["purpose"] + ")") if c.get("purpose") else "")


def selftest():
    folder = tempfile.mkdtemp(prefix="claims_")
    checks = []
    ok, _ = claim(folder, "ana", "topic:pricing", "move the ship date")
    checks.append(("first agent gets a free resource", ok))
    ok, holder = claim(folder, "ben", "topic:pricing")
    checks.append(("second agent is refused and told who holds it", not ok and holder["agent"] == "ana"))
    ok, _ = claim(folder, "ben", "record:refund_rule")
    checks.append(("a different resource is free", ok))
    ok, _ = release(folder, "ben", "topic:pricing")
    checks.append(("an agent cannot release another's claim", not ok))
    ok, _ = claim(folder, "ana", "topic:pricing")
    checks.append(("the holder can renew", ok))
    release(folder, "ana", "topic:pricing")
    ok, _ = claim(folder, "ben", "topic:pricing")
    checks.append(("after release the second agent gets it", ok))
    claim(folder, "cat", "topic:old", minutes=0)
    ok, _ = claim(folder, "dan", "topic:old")
    checks.append(("an expired claim is taken over", ok))
    checks.append(("list shows only live claims", sorted(c["resource"] for c in listing(folder))
                   == ["record:refund_rule", "topic:old", "topic:pricing"]))
    for label, passed in checks:
        print("%-48s %s" % (label, "ok" if passed else "FAILED"))
    for n in os.listdir(folder):
        os.remove(os.path.join(folder, n))
    os.rmdir(folder)
    return 0 if all(p for _, p in checks) else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("action", choices=("claim", "release", "list", "selftest"))
    ap.add_argument("--agent", default=os.environ.get("BRAIN_AGENT"))
    ap.add_argument("--resource")
    ap.add_argument("--purpose", default="")
    ap.add_argument("--minutes", type=float, default=30)
    ap.add_argument("--dir", default=os.environ.get("BRAIN_CLAIMS_DIR", os.path.join(HERE, "claims")))
    a = ap.parse_args()
    if a.action == "selftest":
        return selftest()
    if a.action == "list":
        held = listing(a.dir)
        print("\n".join(describe(c) for c in held) if held else "no live claims")
        return 0
    if not (a.agent and a.resource):
        ap.error("%s needs --agent (or BRAIN_AGENT) and --resource" % a.action)
    if a.action == "claim":
        ok, c = claim(a.dir, a.agent, a.resource, a.purpose, a.minutes)
        print(("claimed " if ok else "REFUSED ") + describe(c))
        return 0 if ok else HELD
    ok, msg = release(a.dir, a.agent, a.resource)
    print(msg)
    return 0 if ok else HELD


if __name__ == "__main__":
    sys.exit(main())
