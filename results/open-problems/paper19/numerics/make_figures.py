"""
Generate publication figures for paper19. Non-interactive (Agg); writes PDFs to this folder.
Run: python make_figures.py
  fig_base.pdf  : (1/m) log M_m -> -h(2)/d_F  (real -log4, complex -log4/2), N=2m-1.
  fig_gumbel.pdf: standardized log M_m vs the reflected (min) Gumbel -- QQ plot + histogram.
"""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from itertools import combinations
from math import log, sqrt, pi
from scipy import stats

rng = np.random.default_rng(20260628)
def rg(s): return rng.standard_normal(s)
def cg(s): return (rng.standard_normal(s)+1j*rng.standard_normal(s))/np.sqrt(2)

def logMm(m,N,gen):
    subs=[list(S) for S in combinations(range(N),m)]
    A=gen((N,m))
    return log(min(np.linalg.svd(A[S],compute_uv=False)[-1] for S in subs))

# ---- Figure 1: base convergence ----
ms=list(range(4,9)); target_r=-log(4); target_c=-log(4)/2
mean_r=[]; mean_c=[]
for m in ms:
    N=2*m-1; tr=300
    r=np.array([logMm(m,N,rg) for _ in range(tr)])/m
    c=np.array([logMm(m,N,cg) for _ in range(tr)])/m
    mean_r.append(r.mean()); mean_c.append(c.mean())
fig,ax=plt.subplots(figsize=(5.2,3.4))
ax.plot(ms,mean_r,"o-",label=r"real,  $(1/m)\log M_m$")
ax.plot(ms,mean_c,"s-",label=r"complex,  $(1/m)\log M_m$")
ax.axhline(target_r,ls="--",color="C0",alpha=.7,label=r"$-\log 4$")
ax.axhline(target_c,ls="--",color="C1",alpha=.7,label=r"$-\frac{1}{2}\log 4$")
ax.set_xlabel(r"$m$"); ax.set_ylabel(r"$(1/m)\log M_m$")
ax.set_title(r"Extremal base at $N=2m-1$ ($\gamma=2$)"); ax.legend(fontsize=8); ax.grid(alpha=.3)
fig.tight_layout(); fig.savefig("fig_base.pdf"); plt.close(fig)
print("wrote fig_base.pdf; real means", [f"{v:.3f}" for v in mean_r])

# ---- Figure 2: Gumbel shape (real, m=7) ----
m=7; N=2*m-1; tr=4000
Y=np.array([logMm(m,N,rg) for _ in range(tr)])
Ys=(Y-Y.mean())/Y.std()
# reflected (min) Gumbel: if W ~ standard max-Gumbel, the min version is -W; standardize.
# standard max-Gumbel mean=euler_gamma, std=pi/sqrt6. min-Gumbel standardized = (euler_gamma - W')/(pi/sqrt6)... use scipy gumbel_l (left-skewed = min).
gum=stats.gumbel_l  # left/min Gumbel
fig,(a1,a2)=plt.subplots(1,2,figsize=(8.4,3.4))
# QQ
q=np.linspace(.5/tr,1-.5/tr,tr)
ax_th=gum.ppf(q); ax_th=(ax_th-ax_th.mean())/ax_th.std()
a1.plot(ax_th,np.sort(Ys),".",ms=3,alpha=.5)
lim=[min(ax_th.min(),Ys.min()),max(ax_th.max(),Ys.max())]
a1.plot(lim,lim,"k--",lw=1)
a1.set_xlabel("standard min-Gumbel quantiles"); a1.set_ylabel(r"standardized $\log M_m$")
a1.set_title(f"QQ plot (real, m={m})"); a1.grid(alpha=.3)
# histogram vs density
xs=np.linspace(Ys.min(),Ys.max(),200)
g0=gum(); sd=g0.std(); mu=g0.mean()
a2.hist(Ys,bins=40,density=True,alpha=.5,label="empirical")
a2.plot(xs, gum.pdf(xs*sd+mu)*sd,"r-",lw=1.5,label="min-Gumbel")
a2.plot(xs, stats.norm.pdf(xs),"g:",lw=1.2,label="Gaussian")
a2.set_xlabel(r"standardized $\log M_m$"); a2.set_title(f"shape (skew={stats.skew(Y):+.2f})")
a2.legend(fontsize=8); a2.grid(alpha=.3)
fig.tight_layout(); fig.savefig("fig_gumbel.pdf"); plt.close(fig)
ks=stats.kstest(Ys,lambda z: gum.cdf(z*sd+mu))
print(f"wrote fig_gumbel.pdf; m={m} skew={stats.skew(Y):+.3f} KS-to-Gumbel stat={ks.statistic:.3f} p={ks.pvalue:.3f}")
print("DONE.")
