"""Reads only grep-selected mathematical cards and reports their exact statements."""
from pathlib import Path
import json
import subprocess
import time
root = Path(__file__).resolve().parent
p = root / 'brain_target_matches.jsonl'
started = time.perf_counter()
pattern = r'"title"\s*:\s*"[^"]*(?:potts|mean.?field)|C0048'
proc = subprocess.run(['rg','-i','-m','12',pattern,
    '~/math-brain-build/export/population/nodes.jsonl'],
    capture_output=True, text=True, encoding='utf-8')
elapsed = time.perf_counter()-started
if proc.returncode not in (0,1):
    raise RuntimeError(proc.stderr)
p.write_text(proc.stdout,encoding='utf-8')
rows=[]
if p.exists():
    for line in p.read_text(encoding='utf-8-sig').splitlines():
        if not line.strip():
            continue
        rows.append(json.loads(line))
(root/'brain_target_nodes.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(root/'measurement_grep.json').write_text(json.dumps({'command_argv':proc.args,
    'exit_code':proc.returncode,'seconds':elapsed,'selected_cards':len(rows),
    'is_recall_engine_benchmark':False,
    'limitation':'Targeted grep of a dated export, not production ranked recall.'},indent=2),encoding='utf-8')
print('grep_selected_cards',len(rows),'seconds',elapsed)
for row in rows:
    print(json.dumps(row,ensure_ascii=False)[:3500])
