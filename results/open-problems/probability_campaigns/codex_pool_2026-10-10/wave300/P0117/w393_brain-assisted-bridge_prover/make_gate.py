from pathlib import Path
import json
import time

now = time.time()
gate = dict(created_unix=now, expires_unix=now + 600, cpu_seconds=8,
            max_box_radius=3, max_vertices=49, deterministic_cases=8,
            processes=1, gpu=False, network=False, outputs='w393 only')
(Path(__file__).resolve().parent / 'COMPUTE_GATE.json').write_text(json.dumps(gate, indent=2), encoding='utf-8')
print(json.dumps(gate))
