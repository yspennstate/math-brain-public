#!/usr/bin/env python3
"""Build the locally retained research-only Blossom V with 64-bit integral costs."""
import os,subprocess
from pathlib import Path
assert os.getpriority(os.PRIO_PROCESS,0)>=10
v=Path('code/vendor/blossom5-v2.05.src')
p=v/'PerfectMatching.h'
s=p.read_text().replace('typedef int REAL;', 'typedef long long REAL;').replace('(INT_MAX/2)','(LLONG_MAX/4)')
s=s.replace('int* edges, int* weights, PerfectMatching* pm','int* edges, PerfectMatching::REAL* weights, PerfectMatching* pm')
p.write_text(s)
p=v/'misc.cpp'
s=p.read_text().replace('int* edges, int* weights, PerfectMatching* pm','int* edges, PerfectMatching::REAL* weights, PerfectMatching* pm')
p.write_text(s)
p=v/'MinCost/instances.inc'
s=p.read_text()
if 'template class DualMinCost<long long>;' not in s:
 p.write_text(s+'\ntemplate class DualMinCost<long long>;\n')
files=[str(v/f) for f in ['PMduals.cpp','PMexpand.cpp','PMinit.cpp','PMinterface.cpp','PMmain.cpp','PMrepair.cpp','PMshrink.cpp','misc.cpp','MinCost/MinCost.cpp']]
cmd=['clang++','-O2','-std=c++11','-fPIC','-shared','-Wno-deprecated-declarations','-Wno-writable-strings','-I'+str(v),'code/matching_wrapper.cpp',*files,'-o','code/libmatching.dylib']
print(' '.join(cmd),flush=True)
subprocess.run(cmd,check=True)
