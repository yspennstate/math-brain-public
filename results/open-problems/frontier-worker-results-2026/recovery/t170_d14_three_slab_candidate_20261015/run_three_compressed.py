from pathlib import Path
from datetime import datetime
from fractions import Fraction as F
import subprocess,json,hashlib,sys
H=Path(__file__).resolve().parent;d=int(sys.argv[1]);C=int(sys.argv[2]);stem=f'T170_THREE_COMPRESSED_d{d}_C{C}';bp=H/(stem+'_BASE.json');ip=H/(stem+'_INPUT.txt');rp=H/(stem+'_RECEIPT.json')
assert not bp.exists() and not rp.exists(),'Read saved result before replay'
p=subprocess.run([str(H/'t170_three_compressed.exe'),str(d),str(C),str(bp)],capture_output=True,text=True,timeout=65,creationflags=subprocess.CREATE_NO_WINDOW|subprocess.BELOW_NORMAL_PRIORITY_CLASS);assert p.returncode==0,p.stdout+p.stderr;print(p.stdout.strip(),flush=True)
v=json.loads(bp.read_bytes());assert len(v['base_bias'])==C*C
ip.write_text(f'{d} {C} {v["alpha0_units"]}\n'+'\n'.join(map(str,v['base_bias']))+'\n',encoding='utf-8')
p=subprocess.run([str(H/'check_three_compressed.exe'),str(ip)],capture_output=True,text=True,timeout=65,creationflags=subprocess.CREATE_NO_WINDOW|subprocess.BELOW_NORMAL_PRIORITY_CLASS);assert p.returncode==0,p.stdout+p.stderr
r=json.loads(p.stdout);axis=F(r['alpha_units'],r['scale']);row=next(x for x in json.loads(Path('~/brain_workers/w685/T170/logs/chord5_exact_certificates.json').read_bytes())['rows'] if x['d']==d)['lower'];floor=F(int(row['n']),int(row['d']))
r.update(at=datetime.now().astimezone().isoformat(),axis=str(axis),axis_float=float(axis),margin=float(floor-axis),gain_estimate=v['gain_estimate'],sweeps=v['sweeps'],last_change=v['last_change'],files_sha256={n:hashlib.sha256((H/n).read_bytes()).hexdigest() for n in ['t170_three_compressed.cpp','check_three_compressed.cpp',bp.name,ip.name,Path(__file__).name]})
rp.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r))
