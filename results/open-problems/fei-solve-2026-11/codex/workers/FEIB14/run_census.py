import subprocess, json, os, time
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
if os.getpriority(os.PRIO_PROCESS,0)<10:os.nice(10-os.getpriority(os.PRIO_PROCESS,0))
subprocess.run(['cc','-O3','witness.c','-o','witness'],check=True)
subprocess.run(['cc','-O3','-DLIBRARY','-dynamiclib','witness.c','-o','witness.dylib'],check=True)
for n in range(1,6):
    with open(f'census{n}.json','w') as out,open(f'census{n}.log','w') as err:
        subprocess.run(['./witness',str(n),f'../FEIB12/npn{n}.bin'],stdout=out,stderr=err,check=True)
    print(open(f'census{n}.json').read(),flush=True)
