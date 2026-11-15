"""Plot independent empirical CDFs, keeping the plotting cache local."""
import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.environ.update(MPLCONFIGDIR=str(ROOT/"data"/".mpl"), XDG_CACHE_HOME=str(ROOT/"data"/".cache"),
                  OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import csv
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rows=list(csv.DictReader((ROOT/"data/samples.csv").open()))
sizes=sorted(set(int(r["n"]) for r in rows))
fig,axes=plt.subplots(2,len(sizes),figsize=(14,6),sharex=True,sharey=True)
t=np.linspace(0,5,400)
for i,ensemble in enumerate(("GOE","Rademacher")):
    for k,n in enumerate(sizes):
        ax=axes[i,k]
        for region,color in (("lower","#1f77b4"),("bulk","#e07010"),("upper","#22864b")):
            a=np.sort([float(r["scaled_min"]) for r in rows if r["ensemble"]==ensemble and int(r["n"])==n and r["index"]==region])
            ax.step(np.r_[0,a],np.r_[0,np.arange(1,len(a)+1)/len(a)],where="post",label=region,color=color,lw=1)
        ax.plot(t,1-np.exp(-math.sqrt(2/math.pi)*t),"k--",label="exponential",lw=1.4)
        ax.set_title(f"{ensemble}, n={n}")
        ax.set_xlim(0,5); ax.set_ylim(0,1); ax.grid(alpha=.15)
        if i==1: ax.set_xlabel(r"$n^{3/2}\min_k|v_j(k)|$")
        if k==0: ax.set_ylabel("empirical CDF")
axes[0,0].legend(fontsize=8)
fig.tight_layout()
fig.savefig(ROOT/"data/referee_cdfs.svg")
print("saved data/referee_cdfs.svg")
