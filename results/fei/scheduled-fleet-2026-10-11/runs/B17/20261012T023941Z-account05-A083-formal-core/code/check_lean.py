from pathlib import Path
import subprocess, os, json, time, ctypes
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(exist_ok=True)
project=Path(r'~\lean_verify')
exe=Path(r'~\.elan\toolchains\leanprover--lean4---v4.33.1\bin\lean.exe')
env=os.environ.copy()
paths=[project/'.lake/build/lib/lean']+[p/'.lake/build/lib/lean' for p in (project/'.lake/packages').iterdir() if p.is_dir()]
env['LEAN_PATH']=';'.join(str(p) for p in paths)
spec={'helper_version':'check_lean.py v1','family':'all ordered fields; arbitrary real or rational interval endpoints','domain':'c>0, a<=x<=b, c<=y<=d','case_count':'two universally quantified theorems','symmetry':'none','arithmetic':'Lean kernel ordered-field proof','memory_estimate_MB':250,'memory_hard_cap_MB':1400,'maximum_runtime_seconds':60,'imports':['Mathlib.Algebra.Order.Field.Basic']}
spec['helper_version']='check_lean.py JS v1'
spec['family']='central-binomial even power-series coefficient products, all indices n>=1'
spec['memory_estimate_MB']=550
spec['domain']='all natural n>=1; no finite cutoff'
spec['case_count']='six universal coefficient, factorial and finite partial-sum theorems'
spec['arithmetic']='Lean core Nat and Rat proofs'
spec['imports']=['Init.Data.Rat.Lemmas']
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
class BASIC(ctypes.Structure):
    _fields_=[('PerProcessUserTimeLimit',ctypes.c_int64),('PerJobUserTimeLimit',ctypes.c_int64),('LimitFlags',ctypes.c_uint32),('MinimumWorkingSetSize',ctypes.c_size_t),('MaximumWorkingSetSize',ctypes.c_size_t),('ActiveProcessLimit',ctypes.c_uint32),('Affinity',ctypes.c_size_t),('PriorityClass',ctypes.c_uint32),('SchedulingClass',ctypes.c_uint32)]
class IO(ctypes.Structure):
    _fields_=[(n,ctypes.c_uint64) for n in ['ReadOperationCount','WriteOperationCount','OtherOperationCount','ReadTransferCount','WriteTransferCount','OtherTransferCount']]
class EXT(ctypes.Structure):
    _fields_=[('BasicLimitInformation',BASIC),('IoInfo',IO),('ProcessMemoryLimit',ctypes.c_size_t),('JobMemoryLimit',ctypes.c_size_t),('PeakProcessMemoryUsed',ctypes.c_size_t),('PeakJobMemoryUsed',ctypes.c_size_t)]
k=ctypes.windll.kernel32
k.CreateJobObjectW.restype=ctypes.c_void_p
k.SetInformationJobObject.argtypes=[ctypes.c_void_p,ctypes.c_int,ctypes.c_void_p,ctypes.c_uint32]
k.AssignProcessToJobObject.argtypes=[ctypes.c_void_p,ctypes.c_void_p]
k.TerminateJobObject.argtypes=[ctypes.c_void_p,ctypes.c_uint32]
k.QueryInformationJobObject.argtypes=[ctypes.c_void_p,ctypes.c_int,ctypes.c_void_p,ctypes.c_uint32,ctypes.c_void_p]
job=k.CreateJobObjectW(None,None); limits=EXT(); limits.BasicLimitInformation.LimitFlags=0x2100; limits.ProcessMemoryLimit=1400*2**20
assert k.SetInformationJobObject(job,9,ctypes.byref(limits),ctypes.sizeof(limits))
cmd=[str(exe),str(R/'code/JSCoefficients.lean')]; start=time.perf_counter()
with (R/'out/LEAN_CHECK.txt').open('w',encoding='utf-8') as out:
    p=subprocess.Popen(cmd,cwd=R,env=env,stdout=out,stderr=subprocess.STDOUT)
    assert k.AssignProcessToJobObject(job,int(p._handle))
    try: rc=p.wait(timeout=60)
    except subprocess.TimeoutExpired:
        k.TerminateJobObject(job,124); p.wait(); rc=124
usage=EXT(); k.QueryInformationJobObject(job,9,ctypes.byref(usage),ctypes.sizeof(usage),None)
result={'exit_code':rc,'seconds':time.perf_counter()-start,'peak_commit_bytes':usage.PeakProcessMemoryUsed,'command':cmd,'lean_version':subprocess.check_output([str(exe),'--version'],text=True).strip(),'LEAN_PATH':env['LEAN_PATH'],'status':'PASS' if rc==0 else 'FAILED'}
(R/'out/LEAN_RESULT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result)); print((R/'out/LEAN_CHECK.txt').read_text(encoding='utf-8'))
raise SystemExit(rc)
