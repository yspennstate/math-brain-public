"""Compare my replays (run_d*.json) with worker R's frozen artifacts, depth by depth and mass by mass."""
import json, hashlib
A = r"(local file)"
pairs = {76: ("run_d76_5-43.json", "balanced_bp_fast_d76_N96_5-43.json"),
         79: ("run_d79_31-272.json", "balanced_bp_fast_d79_N96_31-272.json"),
         83: ("run_d83_35-313.json", "balanced_bp_fast_d83_N96_35-313.json"),
         88: ("run_d88_37-339.json", "balanced_bp_fast_d88_N96_37-339.json"),
         90: ("run_d90_529999-5000000.json", "balanced_bp_fast_d90_N96_529999-5000000.json")}
res = {}
for d, (mine, theirs) in pairs.items():
    try:
        m = json.load(open(mine))
    except FileNotFoundError:
        res[d] = "no replay yet"; continue
    raw = open(A + theirs, "rb").read()
    t = json.loads(raw)
    depth_ok = [r["x"] == tr["second_moment_upper"] and r["nodes"] == [int(v) for v in tr["node_rounding_masses"]]
                for r, tr in zip(m["rows"], t["rows"])]
    tm = {tuple(sorted(k, reverse=True)): int(v) for k, v in zip(t["orbit_keys"], t["final_integer_masses"])}
    mm = {tuple(k): v for k, v in zip(m["orbit_keys"], m["masses"])}
    done = len(m["rows"]) == len(t["rows"])
    res[d] = {"artifact_sha256": hashlib.sha256(raw).hexdigest(), "depths_replayed": len(m["rows"]),
              "depths_in_artifact": len(t["rows"]), "every_depth_signal_and_node_mass_equal": all(depth_ok),
              "final_x_mine": m["rows"][-1]["x"], "final_x_artifact": t["rows"][-1]["second_moment_upper"],
              "final_masses_equal": (mm == tm) if done else "replay not finished",
              "eta": m["eta"], "artifact_eta": t["eta"]}
print(json.dumps(res, indent=1))
json.dump(res, open("compare.json", "w"), indent=1)
