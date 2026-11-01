"""Check the landing record: every landed package starts from the hook the previous one left, and print the bank counts."""
import json, os

D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "landings.json"), encoding="utf-8"))
landed = [r for r in D["landings"] if r["landed"]]
live = {}
breaks = 0
for r in landed:
    for f in r["files"]:
        prev = live.get(f["file"])
        if prev is not None and prev != f["sha256_before"]:
            breaks += 1
            print("candidate %d: %s starts from %s, the previous landing left %s" % (r["candidate"], f["file"], f["sha256_before"], prev))
        live[f["file"]] = f["sha256_after"]
print("%d landings; packages starting from a hook no earlier package left: %d" % (len(landed), breaks))
for r in landed:
    b = r["bank218"]
    print("%3d  %-34s %s" % (r["candidate"], r["when"],
                             "unnamed %s  named %s  unanswerable %s" % (b["unnamed"], b["named"], b["unanswerable"]) if b
                             else "no 218-prompt run" + (" (" + r["bank218_note"].split(";")[0] + ")" if r["bank218_note"] else "")))
