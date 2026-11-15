import json,subprocess,time
from pathlib import Path
for n in range(1,25):
 path=Path(f'census_cert_{n:02d}.json')
 if path.exists() and 'B_le_2.18I_integer_certificate' in path.read_text():continue
 row=json.loads(subprocess.check_output(['./census_cert',str(n)],text=True))
 path.write_text(json.dumps(row,indent=2)+'\n')
 print(n,row['coarse_upper_max'],row['cpu_seconds'],flush=True)
