"""Sequential exact checks of the dimension extension, not a full FPP proof."""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
from datetime import datetime,timezone
import sys,subprocess,json,time,hashlib
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from measure_chord5 import available_memory
jobs=[('certify_scalar_bridge_mass.py','PASS exact scalar'),('certify_renewal_norm.py','PASS exact renewal norm'),('certify_height_renewal_interval.py','PASS outward')]
start=time.monotonic();done=[]
for d in map(int,sys.argv[1:]):
    assert d in (18,19)
    dest=ROOT/'dimension_extension'/f'd{d}'
    for name,marker in jobs:
        if time.monotonic()-start>450:raise SystemExit('Checkpoint retained: rerun only the unfinished dimension.')
        free=available_memory()
        if free is None or free<2*1024**3:raise SystemExit('WAIT: memory admission fails.')
        p=dest/'logs'/('producer_'+name.removesuffix('.py')+'.txt')
        with p.open('w',encoding='utf-8',newline='') as log:
            run=subprocess.run([sys.executable,'-X','utf8',str(dest/'scripts'/name)],stdout=log,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW)
        lines=p.read_text(encoding='utf-8').splitlines()
        assert run.returncode==0 and any(v.startswith(marker) for v in lines),(d,name,run.returncode,lines[-2:])
        done.append(dict(d=d,script=name,producer_exit=run.returncode))
        (ROOT/'logs/renewal_extension_checkpoint.json').write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),done=done),indent=2)+'\n',encoding='utf-8')
        print('PASS producer',d,name,flush=True)
    point=json.loads((dest/'logs/height_bridge_tail_certificate.json').read_text(encoding='utf-8'))
    interval=json.loads((dest/'logs/height_renewal_interval_certificate.json').read_text(encoding='utf-8'))
    assert interval['d']==d and interval['boundary_rows']==330
    get=lambda obj,key:Q(int(obj[key]['n']),int(obj[key]['d']))
    assert get(interval,'rho_upper')<1
    s,z=get(point,'s'),get(point,'z');scale=10**24
    root=Q(isqrt(d*scale**2),scale);assert root*root<=d
    t=(z-1)/(z+1);assert 0<t<1
    loglo=2*sum(t**(2*k+1)/Q(2*k+1) for k in range(50))
    ratio=root*loglo/s;units=(ratio*10**12).__floor__()
    result=dict(at=datetime.now(timezone.utc).isoformat(),d=d,point_sha256=hashlib.sha256((dest/'logs/height_bridge_tail_certificate.json').read_bytes()).hexdigest(),floor_numerator=str(units),floor_denominator=str(10**12),floor_decimal=f'{units//10**12}.{units%10**12:012d}',method='sqrt lower by integer isqrt at scale 10^24; positive 50-term logarithm series; exact downward decimal floor',scope='Exact floor of sqrt(d)log(z)/s; its FPP interpretation is not independently checked.')
    (dest/'logs/diagonal_ratio_floor.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    files=[p for p in dest.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='delivery_manifest.json']
    manifest=dict(at=datetime.now(timezone.utc).isoformat(),d=d,runs=[v for v in done if v['d']==d],hashes={p.relative_to(dest).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)},scope='Exact/outward encoded-operator checks only; full FPP proof and novelty await independent review.')
    (dest/'logs/delivery_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print('PASS finite encoded contraction d',d,'rho',str(get(interval,'rho_upper')),'ratio floor',result['floor_decimal'],flush=True)
