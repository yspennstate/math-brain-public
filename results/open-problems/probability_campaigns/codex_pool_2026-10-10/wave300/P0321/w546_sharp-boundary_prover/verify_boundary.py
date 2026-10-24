"""Independent deterministic quadrature checks; no numerical result is a Gibbs proof."""
from __future__ import annotations

import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"

import json
import math
from pathlib import Path
import time

root = Path(__file__).resolve().parent
gate = json.loads((root / "COMPUTE_GATE.json").read_text(encoding="utf-8-sig"))
wall_start, cpu_start = time.monotonic(), time.process_time()
from scipy.integrate import quad
from scipy.special import j0, j1, jv, ndtr


def budget() -> None:
    if time.process_time() - cpu_start > gate["max_cpu_seconds"]:
        raise RuntimeError("CPU gate exceeded")
    if time.monotonic() - wall_start > gate["max_wall_seconds"]:
        raise RuntimeError("Wall gate exceeded")
    import ctypes
    from ctypes import wintypes
    class Counters(ctypes.Structure):
        _fields_ = [("cb",wintypes.DWORD),("PageFaultCount",wintypes.DWORD)] + [(n,ctypes.c_size_t) for n in ("PeakWorkingSetSize","WorkingSetSize","QuotaPeakPagedPoolUsage","QuotaPagedPoolUsage","QuotaPeakNonPagedPoolUsage","QuotaNonPagedPoolUsage","PagefileUsage","PeakPagefileUsage")]
    pc=Counters(); pc.cb=ctypes.sizeof(pc)
    kernel=ctypes.WinDLL("kernel32"); kernel.GetCurrentProcess.restype=wintypes.HANDLE
    psapi=ctypes.WinDLL("psapi"); psapi.GetProcessMemoryInfo.argtypes=[wintypes.HANDLE,ctypes.POINTER(Counters),wintypes.DWORD]
    if psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(),ctypes.byref(pc),pc.cb) and pc.WorkingSetSize > gate["max_resident_megabytes"]*1024**2:
        raise RuntimeError("Resident-memory gate exceeded")


def integrate(func, upper: float) -> float:
    # Segments avoid hiding oscillatory errors in one large interval.
    out = 0.0
    at = 0.0
    while at < upper:
        stop = min(upper, at+4)
        out += quad(func, at, stop, epsabs=2e-12, epsrel=2e-12, limit=80)[0]
        at = stop
    return out


def critical_f(z: float) -> float:
    return integrate(lambda t: (1-j0(t))/t if t>1e-4 else t/4-t**3/64+t**5/2304, z)


beta, mu, cutoff = 1.0, 1.0, 1.0
rows = []
max_angle_error = max_projection_error = 0.0
for r in (0.3, 1.0, 4.0, 12.0, 64.0, 256.0):
    budget()
    # Independent angular+radial integral of (half curl)^2 Q. Q_T contraction
    # is evaluated using vector projector coordinates, not the Bessel formula.
    def radial(k: float) -> float:
        if k == 0: return 0.0
        def angular(phi: float) -> float:
            kx, ky = k*math.cos(phi), k*math.sin(phi)
            tx, ty = -ky, kx
            pl_contract = (tx*kx+ty*ky)**2/k**2
            pt_contract = tx*tx+ty*ty-pl_contract
            return (1-math.cos(kx*r))*pt_contract/(4*beta*mu*k*k)
        return k*quad(angular,0,2*math.pi,epsabs=1e-11,epsrel=1e-11,limit=700)[0]/(2*math.pi)**2
    direct = quad(radial,0,cutoff,epsabs=2e-11,epsrel=2e-11,limit=700)[0]
    cov0=cutoff**2/(16*math.pi*beta*mu)
    covr=cutoff*j1(cutoff*r)/(8*math.pi*beta*mu*r)
    angle_log_exact=36*(cov0-covr)
    angle_log_direct=36*direct
    max_angle_error=max(max_angle_error,abs(angle_log_direct-angle_log_exact))
    # Independent angular identity for a non-aligned reciprocal vector.
    alpha=0.37
    t=r
    direct_proj=quad(lambda phi: math.sin(phi-alpha)**2*math.cos(t*math.cos(phi)),0,2*math.pi,epsabs=1e-10,epsrel=1e-10,limit=700)[0]
    exact_proj=math.pi*(j0(t)+math.cos(2*alpha)*jv(2,t))
    max_projection_error=max(max_projection_error,abs(direct_proj-exact_proj))
    rows.append({"r":r,"C6_elastic":math.exp(-angle_log_exact),"negative_log_C6_direct":angle_log_direct,"negative_log_C6_exact":angle_log_exact,"F_critical":critical_f(r)})

budget()
stiffness=144/math.pi
eta6=18/(math.pi*stiffness)
f64,f256=critical_f(64),critical_f(256)
measured_eta=eta6*(f256-f64)/math.log(256/64)
alpha=0.37
def ft(z: float) -> float:
    c=math.cos(2*alpha)
    return integrate(lambda t: (1-j0(t)-c*jv(2,t))/t if t>1e-4 else t*(1/4-c/8)+t**3*(-1/64+c/96), z)
positional_eta=1/(4*math.pi*beta*mu)
measured_positional_eta=positional_eta*(ft(256)-ft(64))/math.log(4)

budget()
# Independent check of randomized-rounding variance via the direct mixture PMF:
# integrate P(q=n*h | V=v) over v, rather than using total-variance formula.
h=2*math.pi/6
quantized=[]
for gaussian_variance in (0.1,1.0,10.0):
    sigma=math.sqrt(gaussian_variance)
    bound=math.ceil(10*sigma/h)+2
    mean=second=mass=0.0
    for n in range(-bound,bound+1):
        p=quad(lambda offset: (ndtr(((n+1)*h-offset)/sigma)-ndtr((n*h-offset)/sigma))/h,0,h,epsabs=2e-13,epsrel=2e-13)[0]
        mass+=p; mean+=n*h*p; second+=(n*h)**2*p
    variance=second-mean**2
    quantized.append({"gaussian_variance":gaussian_variance,"quantized_variance_direct":variance,"added_variance":variance-gaussian_variance,"upper_added_bound":h*h/4,"mass":mass,"mean":mean})
    assert abs(mass-1)<2e-12 and abs(mean)<2e-12
    assert gaussian_variance-2e-12<=variance<=gaussian_variance+h*h/4+2e-12
    budget()

assert max_angle_error<1e-8
assert max_projection_error<1e-8
assert abs(measured_eta-eta6)<8e-4
assert abs(measured_positional_eta-positional_eta)<8e-4
plateau=math.exp(-9*cutoff*cutoff/(4*math.pi*beta*mu))
assert abs(rows[-1]["C6_elastic"]-plateau)<4e-4
result={"status":"PASS","claim_scope":"auxiliary Gaussian formulas and quantized-field variance; no microscopic Gibbs proof","command":"python -X utf8 verify_boundary.py","gate":gate,"cpu_seconds":time.process_time()-cpu_start,"wall_seconds":time.monotonic()-wall_start,"rows":rows,"elastic_plateau":plateau,"angular_log_formula_max_absolute_error":max_angle_error,"projector_angular_identity_max_absolute_error":max_projection_error,"critical_eta6_exact":eta6,"critical_eta6_measured_64_to_256":measured_eta,"positional_eta_exact":positional_eta,"positional_eta_measured_64_to_256":measured_positional_eta,"quantized_variance_rows":quantized,"formal_proof_receipt":None}
(root/"VERIFICATION.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k not in ("gate","rows","quantized_variance_rows")},indent=2))
