import subprocess,json
from pathlib import Path
for n in range(1,25):
 p=Path(f'census_interval_{n:02d}.json')
 if p.exists():continue
 row=json.loads(subprocess.check_output(['./census_interval',str(n)],text=True));p.write_text(json.dumps(row,indent=2)+'\n');print(n,row['cpu_seconds'],flush=True)
