"""Rebuild all certificate dependencies sequentially, checking producer exits."""
from pathlib import Path
import subprocess,sys,json,hashlib,time
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
jobs=[('build_height_renewal.py','DONE states'),('certify_height_tail.py','PASS scalar tail'),
      ('certify_scalar_bridge_mass.py','PASS exact scalar'),('certify_renewal_norm.py','PASS exact renewal norm'),
      ('validate_height_renewal_words.py','PASS full-coordinate'),('validate_height_cut_boundaries.py','PASS height-cut'),
      ('certify_height_renewal_interval.py','PASS outward'),('compute_renewal_mu_floor.py','PASS exact diagonal')]
start=time.monotonic();runs=[]
for name,required in jobs:
    dest=ROOT/'logs'/('clean_renewal_'+name.removesuffix('.py')+'.txt')
    with dest.open('w',encoding='utf-8',newline='') as log:
        result=subprocess.run([sys.executable,'-X','utf8',str(ROOT/'scripts'/name)],stdout=log,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW)
    lines=dest.read_text(encoding='utf-8').splitlines()
    if result.returncode or not any(line.startswith(required) for line in lines):
        print(name,'FAILED producer exit',result.returncode,'\n'.join(lines[-6:]),flush=True)
        raise SystemExit(1)
    runs.append({'script':name,'producer_exit':result.returncode,'required_marker':required})
    print(lines[-1],flush=True)
files=['proofs/unique_height_renewal.md','proofs/scalar_bridge_mass.md','proofs/renewal_boundary_norm.md',
       'scripts/height_renewal_graph.json','scripts/height_profiles.py','scripts/measure_chord5.py',
       'scripts/certify_bounds.py','scripts/hybrid2_certificate_parameters.json',
       'logs/height_renewal_measure_K21.json','logs/height_bridge_tail_certificate.json',
       'logs/scalar_bridge_mass_certificate.json','logs/height_renewal_norm_certificate.json',
       'logs/height_renewal_word_validation.json','logs/height_cut_boundary_validation.json',
       'logs/height_renewal_interval_certificate.json','logs/height_renewal_mu_floor.json']
files += ['scripts/'+name for name,marker in jobs]
files += ['scripts/run_height_renewal_certificate.py']
manifest=dict(at=datetime.now(timezone.utc).isoformat(),producer_runs=runs,seconds=time.monotonic()-start,
              hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in files},
              scope='from-scratch computational checks; full FPP proof and novelty await independent review')
(ROOT/'logs/height_renewal_delivery_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print('PASS clean renewal certificate pipeline; full mathematical proof remains unaudited.',flush=True)
