"""Summarize independent simulator outputs, with fixed theoretical references."""
import glob
import math
import numpy as np
from scipy.stats import kstest, kurtosis

c=math.pi**2/6
groups={}
print(f'Exact references: c={c:.12f}; zeta(4)={math.pi**4/90:.12f}')
for path in sorted(glob.glob('cycles*_t*.csv')):
    a=np.genfromtxt(path,delimiter=',',names=True,dtype=None,encoding=None)
    L=int(a['V'][0]);T=a['T'][0];R=len(a)
    groups.setdefault((L,T),[]).append(a)
    M=a['M'];Z=M/math.sqrt(L);q=a['Q']/L
    variance=Z.var(ddof=1)
    sevar=np.sqrt(np.mean((Z-Z.mean())**4)-variance**2)/math.sqrt(R)
    meanse=Z.std(ddof=1)/math.sqrt(R)
    D,p=kstest(Z,'norm',args=(0,math.sqrt(c)))
    u=np.tanh(a['logcharge']/L)
    cf=np.mean(np.cos(Z))
    cfexact=(math.pi/math.sqrt(L)/math.sinh(math.pi/math.sqrt(L)))**(L/2)
    print(f'{path}: L={L} T={T:g} R={R}')
    print(f'  mean Z={Z.mean():.6f} +/- {meanse:.6f}; Var Z={variance:.6f} +/- {sevar:.6f}; '
          f'excess={kurtosis(Z,bias=False):.5f}; exact terminal excess={2.4/L:.5f}')
    print(f'  mean Q/L={q.mean():.6f} +/- {q.std(ddof=1)/math.sqrt(R):.6f}; '
          f'Var Q/L={q.var(ddof=1):.6f}; terminal reference={math.pi**4/(90*L):.6f}')
    print(f'  estimated future E[(M_inf-M_T)^2]/L={c-a["optional"].mean()/L:.8f}; '
          f'RMS(logcharge-M)={np.sqrt(np.mean((a["logcharge"]-M)**2)):.7f}')
    print(f'  shape RMS={np.sqrt(np.mean(a["shape_rms"]**2)):.7f}; '
          f'vertex RMS={np.sqrt(np.mean(a["vertex_rms"]**2)):.7f}; '
          f'RMS(altmean-u_logs)={np.sqrt(np.mean((a["altmean"]-u)**2)):.7f}')
    valid=abs(a['altmean'])<1
    projection_charge=L*np.arctanh(a['altmean'][valid])
    print(f'  independent count-projection check: valid {valid.sum()}/{R}; '
          f'RMS(L*atanh(altmean)-M)={np.sqrt(np.mean((projection_charge-M[valid])**2)):.7f}')
    print(f'  normal KS D={D:.6f}, p={p:.5g}; E cos(Z)={cf:.7f}, exact-terminal={cfexact:.7f}')
    if L==4:
        print(f'  Var((X0+X2)/4)={a["p"].var(ddof=1):.7f}; '
              f'Var((1+tanh(M/4))/2)={((1+np.tanh(M/4))/2).var(ddof=1):.7f}; '
              f'exact terminal={math.pi**2/32-.25:.7f}')

for (L,T),arrays in sorted(groups.items()):
    if len(arrays)<2: continue
    a=np.concatenate(arrays);R=len(a);Z=a['M']/math.sqrt(L);q=a['Q']/L
    error=a['logcharge']-a['M'];v=Z.var(ddof=1)
    se=np.sqrt(np.mean((Z-Z.mean())**4)-v*v)/math.sqrt(R)
    r2=error*error
    se_rms=r2.std(ddof=1)/math.sqrt(R)/(2*np.sqrt(r2.mean()))
    print(f'POOLED L={L} T={T:g}: R={R}, meanZ={Z.mean():.7f}, VarZ={v:.7f} +/- {se:.7f}, '
          f'mean Q/L={q.mean():.7f} +/- {q.std(ddof=1)/math.sqrt(R):.7f}, '
          f'RMS log-M={np.sqrt(r2.mean()):.7f} (delta-method SE {se_rms:.7f}), '
          f'abs-error quantiles 50/90/99/100%={np.quantile(abs(error),[.5,.9,.99,1])}, '
          f'shape RMS={np.sqrt(np.mean(a["shape_rms"]**2)):.7f}')

for path in sorted(glob.glob('smallgraph*.csv')):
    a=np.genfromtxt(path,delimiter=',',names=True,dtype=None,encoding=None)
    R=len(a);M=a['M'];mm=M*M
    print(f'{path}: R={R}, mean M={M.mean():.7f} +/- {M.std(ddof=1)/math.sqrt(R):.7f}; '
          f'mean M^2={mm.mean():.7f} +/- {mm.std(ddof=1)/math.sqrt(R):.7f}; '
          f'mean Q={a["Q"].mean():.7f} +/- {a["Q"].std(ddof=1)/math.sqrt(R):.7f}; '
          f'mean optional={a["optional"].mean():.7f}')

for path in sorted(glob.glob('line*.csv')):
    a=np.genfromtxt(path,delimiter=',',names=True,dtype=None,encoding=None)
    print(path)
    for T in sorted(set(a['T'])):
        b=a[a['T']==T];q=b['Q'];rate=b['qrate']
        print(f'  T={T:g}, replicas={len(b)}, q(T)={q.mean():.7f} +/- {q.std(ddof=1)/math.sqrt(len(b)):.7f}, '
              f'mean integrand={rate.mean():.9g}, exact c-q_est={c-q.mean():.7f}, '
              f'count-based expected tail estimate={c-b["optional"].mean():.7f}')
        corrected=q+c-b['optional']
        print(f'    tail-corrected mean={corrected.mean():.7f} +/- {corrected.std(ddof=1)/math.sqrt(len(b)):.7f}')

for path in sorted(glob.glob('synchronous*.csv')):
    a=np.genfromtxt(path,delimiter=',',names=True,dtype=None,encoding=None)
    Z=a['Z'];R=len(a);var=Z.var(ddof=1)
    sevar=np.sqrt(np.mean((Z-Z.mean())**4)-var**2)/math.sqrt(R)
    print(f'{path}: R={R}, Var Z={var:.7f} +/- {sevar:.7f}, '
          f'Var p={a["p"].var(ddof=1):.7f}')
