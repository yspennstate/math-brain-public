Frozen before execution: FROZEN_SPEC.json; equality follow-up frozen in ZERO_RESOLUTION_SPEC.json.
One Python process, serial loops, no worker pool, no GPU, no automatic dimension increase. Each computational job has a 55-second elapsed-time cap checked after bounded batches. Expected peak RAM <=100 MB for grid, <=30 MB for equality resolution; no >300 MB job was started. RAM was estimated, not measured. CPU is a single serial execution lane, with no promise of exclusive hardware.
Pilot: 768 cases in 0.191381 s (<60 s).
Full grid: 20736 cases in 22.158842 s.
Equality resolution: 600 cases in 0.411915 s.
Command startup/tool latency is distinct from the computational runtimes recorded by perf_counter. The timeout can overrun by one bias-vector batch; measured full job remained below 55 seconds. No heavy job or memok gate was needed for this bounded low-memory search.
