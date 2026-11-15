"""Run the saved finite investigations and audits sequentially at nice 10."""
import os,json,time,subprocess
from pathlib import Path
os.chdir(Path(__file__).resolve().parent)
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
if os.getpriority(os.PRIO_PROCESS,0)<10:os.nice(10-os.getpriority(os.PRIO_PROCESS,0))
jobs=[
 ('census',['python3','run_census.py']),
 ('samples',['python3','experiments.py','general']),
 ('ltf',['python3','experiments.py','ltf']),
 ('monotone',['python3','experiments.py','monotone']),
 ('extrema',['python3','experiments.py','extrema']),
 ('audit',['python3','audit.py']),
 ('composition',['python3','composition.py']),
 ('highprecision',['python3','highprecision.py']),
 ('compile_symmetric',['cc','-O3','symmetric.c','-o','symmetric']),
 ('symmetric',['./symmetric']),
 ('symmetric_audit',['python3','structured.py','symmetric_audit']),
 ('families',['python3','structured.py','families']),
 ('cardinality_dilution',['python3','structured.py','cardinality']),
 ('majority_meets',['python3','structured.py','majority']),
 ('quantized',['python3','quantized.py']),
 ('inherited_audit',['python3','inherited_audit.py']),
 ('large_audit',['python3','run_large_audit.py']),
 ('final_audit',['python3','final_audit.py']),
 ('make_results',['python3','make_results.py'])]
rows=[];start=time.time()
for name,cmd in jobs:
    Path('STATUS.md').write_text(f'# FEIB14 status\nNEXT: finish reproduction unit {name}, then write REPORT.md.\n\nProofs and discoveries are saved in PROOFS.md and LEARNINGS.md. The sequential reproduction validates the final script chain and records resources.\n')
    t=time.time();log=name+'.reproduce.log'
    with open(log,'w') as out:
        if name=='symmetric':
            data=open('symmetric.json','w');err=out
        else:data=out;err=subprocess.STDOUT
        p=subprocess.Popen(cmd,stdout=data,stderr=err)
        pid,status,usage=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status)
        if name=='symmetric':data.close()
    r=dict(unit=name,command=cmd,exit_code=p.returncode,elapsed_seconds=time.time()-t,cpu_seconds=usage.ru_utime+usage.ru_stime,maxrss_bytes=usage.ru_maxrss,log=log)
    rows.append(r);Path('resources.json').write_text(json.dumps(dict(rows=rows,nice=os.getpriority(os.PRIO_PROCESS,0),maximum_simultaneous_units=1,thread_limit=1,elapsed_seconds=time.time()-start),indent=2)+'\n')
    print(name,p.returncode,r['elapsed_seconds'],r['maxrss_bytes'],flush=True)
    if p.returncode:raise SystemExit(p.returncode)
Path('STATUS.md').write_text('# FEIB14 status\nNEXT: audit final deliverable text and write REPORT.md; all reproduction units passed.\n\nGeneral width-DNF, monotone and cheap universal witness targets remain mathematical open questions, identified in PROOFS.md.\n')
print('REPRODUCTION PASS',time.time()-start)
