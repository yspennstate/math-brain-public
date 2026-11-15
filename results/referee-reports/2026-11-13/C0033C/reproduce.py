"""Sequential reproduction, without worker pools. Targets the macOS workspace."""
import os,subprocess,sys,json,hashlib,platform
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
ROOT=Path(__file__).resolve().parent

def main():
    os.chdir(ROOT)
    subprocess.run(['clang++','-O3','-std=c++17','-dynamiclib','dpp.cpp','-o','libdpp.dylib'],check=True)
    for script,log in [('probe_scalar.py','scalar_run.log'),('ranktwo_search.py','ranktwo_run.log'),('interval_audit.py','interval_run.log'),('certify_ranktwo.py','certify_run.log'),('structural_audit.py','structural_run.log')]:
        print(script,flush=True)
        with open(log,'w') as out:subprocess.run([sys.executable,script],stdout=out,stderr=subprocess.STDOUT,check=True)
    subprocess.run([sys.executable,'make_tables.py'],check=True)
    import numpy,scipy,sympy,mpmath
    inherited={}
    for name in ('dpp.py','dpp.cpp'):
        local=(ROOT/name).read_bytes();prior=(ROOT.parent/'C0033B'/name).read_bytes();assert local==prior
        inherited[name]=hashlib.sha256(local).hexdigest()
    files={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.rglob('*')) if p.is_file() and (p.suffix in ('.py','.cpp','.json','.npz') or p.name=='REPORT.md') and '__pycache__' not in str(p) and p.name!='artifact_manifest.json'}
    out=dict(python=platform.python_version(),platform=platform.platform(),packages={m.__name__:m.__version__ for m in (numpy,scipy,sympy,mpmath)},inherited_verbatim_sha256=inherited,numerical_threads=1,worker_pools=0,priority=os.getpriority(os.PRIO_PROCESS,0),sha256=files)
    Path('artifact_manifest.json').write_text(json.dumps(out,indent=2)+'\n')
    print('All certificates passed; tables and manifest regenerated.',flush=True)
if __name__=='__main__':main()
