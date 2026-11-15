"""Reproduce computations serially, with a per-child wall limit and RSS measurement.

Only this supervisor and one computation run at a time. This also records the
observed maximum resident memory. No external file is written by this script.
"""
import json, os, platform, resource, subprocess, sys, time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
ENV=os.environ.copy()
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:
    ENV[key]='1'
ENV['PYTHONDONTWRITEBYTECODE']='1'

def limits():
    try:os.nice(10)
    except OSError:pass

def main():
    tasks=[('environment_probe.py','environment_results.txt'),
           ('gamma_audit.py','gamma_summary.json'),
           ('precision_audit.py','precision_stdout.json'),
           ('stopping_audit.py','stopping_stdout.json'),
           ('ratio_search.py','ratio_search_stdout.json'),
           ('finalist_audit.py','finalist_stdout.json'),
           ('rational_certificates.py','rational_stdout.json')]
    runs=[]
    for program,output in tasks:
        start=time.monotonic()
        with open(ROOT/output,'w') as f:
            result=subprocess.run([sys.executable,program],cwd=ROOT,env=ENV,stdout=f,
                                  stderr=subprocess.PIPE,text=True,timeout=245,preexec_fn=limits)
        rss=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        if platform.system()!='Darwin':rss*=1024
        record={'program':program,'command':f'python3 {program} > {output}',
                'returncode':result.returncode,'seconds':time.monotonic()-start,
                'cumulative_child_peak_rss_bytes':rss,'stderr':result.stderr}
        runs.append(record)
        print(json.dumps(record),flush=True)
        if result.returncode:raise RuntimeError(program+' failed')
        assert rss<1024**3,'RSS limit exceeded'
    out={'runs':runs,'memory_note':'RLIMIT_DATA unavailable in this environment; actual child RSS measured and checked below 1 GiB','max_child_rss_bytes':max(r['cumulative_child_peak_rss_bytes'] for r in runs),
         'max_concurrent_python_processes':2,'max_run_seconds':max(r['seconds'] for r in runs)}
    with open(ROOT/'run_manifest.json','w') as f:json.dump(out,f,indent=2)

if __name__=='__main__':main()
