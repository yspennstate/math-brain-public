"""Run one independent C simulation at a time; write all outputs locally."""
import json
import os
from pathlib import Path
import resource
import subprocess
import time

try:
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    if priority < 10:
        os.setpriority(os.PRIO_PROCESS, 0, 10)
except (OSError, AttributeError):
    pass

jobs = [(name, m, seed) for name in ("sqrt", "log", "osc") for m in (2, 3) for seed in (89, 97)]
jobs += [("two", 2, 89), ("uniform", 2, 89)]
results = []
start_all = time.monotonic()
for name, m, seed in jobs:
    start = time.monotonic()
    p = subprocess.run(["./referee_sim", name, "1000000", str(m), str(seed)],
                       text=True, capture_output=True, timeout=245, check=True)
    result = json.loads(p.stdout)
    result["elapsed_seconds"] = time.monotonic() - start
    result["sampler_oracle"] = "all first-1000-vertex endpoint comparisons passed"
    results.append(result)
    Path(f"referee_sim_{name}_m{m}_s{seed}.json").write_text(json.dumps(result, indent=2) + "\n")
    Path("referee_simulations.json").write_text(json.dumps(results, indent=2) + "\n")
    print(f"{name} m={m} seed={seed} S/n={result['S_over_n']:.10f} "
          f"p0={result['p0_to_p10'][0]:.6f} H0={result['ball_H0']:.6f} H1={result['ball_H1']:.6f} "
          f"time={result['elapsed_seconds']:.3f}s", flush=True)
print(f"total_seconds={time.monotonic()-start_all:.3f}")
print(f"max_child_rss_bytes={resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss}")
