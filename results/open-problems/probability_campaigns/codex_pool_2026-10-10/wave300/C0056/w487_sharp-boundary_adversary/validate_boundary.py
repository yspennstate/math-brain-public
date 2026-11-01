"""Small, freshly gated independent quadrature and exact torus checks."""
import ctypes
import json
import math
import shutil
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

folder=Path(__file__).resolve().parent
started=time.perf_counter()

class Memory(ctypes.Structure):
    _fields_=[("length",ctypes.c_ulong),("load",ctypes.c_ulong)]+[(n,ctypes.c_ulonglong) for n in
        ("total_phys","avail_phys","total_page","avail_page","total_virtual","avail_virtual","avail_extended")]

memory=Memory(); memory.length=ctypes.sizeof(memory)
if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory)):
    raise RuntimeError("Fresh memory gate could not be read")
gate={"timestamp_utc":datetime.now(timezone.utc).isoformat(),"available_ram_bytes":memory.avail_phys,
      "free_disk_bytes":shutil.disk_usage(folder).free,"limits":{"ram_min_bytes":256*1024**2,
      "disk_min_bytes":64*1024**2,"kernel_evaluations_max":4096,"wall_seconds_max":5},
      "gpu":False,"subprocesses":False}
gate["pass"]=memory.avail_phys>=gate["limits"]["ram_min_bytes"] and gate["free_disk_bytes"]>=gate["limits"]["disk_min_bytes"]
(folder/"COMPUTE_GATE.json").write_text(json.dumps(gate,indent=2)+"\n",encoding="utf-8")
if not gate["pass"]:
    print(json.dumps({"status":"SKIPPED_FRESH_RESOURCE_GATE","gate":gate})); raise SystemExit(0)

evals=0
def quadrature_second(lam,a,b,n=128):
    # Independently integrate the conditional density in the angle coordinate.
    # This avoids resolving a narrowing peak with a growing integration grid.
    global evals
    lo=math.atan((-lam-a)/b); hi=math.atan((lam-a)/b); step=(hi-lo)/n
    total=0.0
    for j in range(n+1):
        if time.perf_counter()-started>5: raise RuntimeError("Five-second compute gate exceeded")
        weight=1 if j in (0,n) else 4 if j%2 else 2
        total+=weight*math.cos(lo+j*step)**2
        evals+=1
    return total*step/(6*lam*b)

rows=[]
for lam in (1.0,0.3):
    for eta in (0.1,0.01,0.001,0.0001):
        first=math.atan(lam/eta)/lam
        second=1/(2*(lam*lam+eta*eta))+math.atan(lam/eta)/(2*lam*eta)
        independent=quadrature_second(lam,0.0,eta)
        error=abs(independent-second)/second
        if error>1e-8: raise AssertionError((lam,eta,error))
        rows.append({"lambda":lam,"eta":eta,"first_moment":first,"second_moment":second,
          "eta_times_second":eta*second,"quadrature_relative_error":error})
schur=[]
for a,b in ((0.0,0.5),(0.4,0.1),(0.4,0.001),(2.0,0.01)):
    measured=quadrature_second(1.0,a,b)
    upper=math.pi/(4*b)
    lower=1/(4*b) if abs(a)<=0.5 and b<=0.5 else None
    if measured>upper*(1+1e-8) or (lower is not None and measured<lower*(1-1e-8)):
        raise AssertionError((a,b,measured,lower,upper))
    schur.append({"a":a,"B":b,"conditional_second_moment":measured,"lower":lower,"upper":upper})

# Exact algebraic arithmetic: energy=(integer_a+integer_b*sqrt(5))/2 for L=5.
torus=[]
for L,coordinate in ((3,[(4,0),(-2,0),(-2,0)]),(5,[(4,0),(-1,1),(-1,-1),(-1,-1),(-1,1)])):
    energies=Counter((x[0]+y[0]+z[0],x[1]+y[1]+z[1]) for x in coordinate for y in coordinate for z in coordinate)
    bulk={key:n for key,n in energies.items() if -1<(key[0]+key[1]*math.sqrt(5))/2<1}
    M=sum(bulk.values()); D=len(bulk)
    if M>1 and (M-D)*2<M: raise AssertionError("Bulk zero-spacing bound failed")
    torus.append({"odd_L":L,"N":L**3,"distinct_full_energies":len(energies),"bulk_interval":[-1,1],
                  "bulk_M":M,"bulk_D":D,"bulk_zero_spacings":M-D,"bulk_zero_fraction":(M-D)/(M-1) if M>1 else None})

result={"status":"PASS","moment_rows":rows,"schur_rows":schur,"free_torus_rows":torus,
        "kernel_evaluations":evals,"seconds":time.perf_counter()-started,
        "max_quadrature_relative_error":max(row["quadrature_relative_error"] for row in rows),
        "scope":"Numerical/formula smoke check only; not an independent or formal proof."}
if evals>4096: raise RuntimeError("Kernel-evaluation gate exceeded")
(folder/"MEASUREMENTS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result))
