"""Sequential reproduction of search data or the final mathematical audits."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import argparse,subprocess,sys
root=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['audit','searches']);args=parser.parse_args()
def run(name):
 print(name,flush=True)
 with (root/(name.removesuffix('.py')+'_run.log')).open('w') as out:
  subprocess.run([sys.executable,name],cwd=root,stdout=out,stderr=subprocess.STDOUT,check=True)
if args.mode=='searches':
 for name in ('explore3.py','star_probe.py','ranktwo_probe.py','commuting_search.py','wedge_probe.py','decomposable_search.py','submodular_probe.py','submod_boundary.py'):run(name)
else:
 subprocess.run(['clang++','-O3','-std=c++17','-shared','-fPIC','dpp.cpp','-o','libdpp.dylib'],cwd=root,check=True)
 for name in ('verify_mp.py','verify_certificates.py','interval3.py','wedge_interval.py'):run(name)
 subprocess.run([sys.executable,'make_tables.py'],cwd=root,check=True)
