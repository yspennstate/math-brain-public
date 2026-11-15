import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(ROOT/'referee_data/matplotlib')
os.environ['XDG_CACHE_HOME']=str(ROOT/'referee_data/cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json
g=np.genfromtxt(ROOT/'referee_data/grid.csv',delimiter=',',names=True)
s=json.loads((ROOT/'referee_data/summary.json').read_text())
fig,ax=plt.subplots(figsize=(7,4))
ax.semilogx(g['r'],g['exponent'],label='Independent stationary density',color='#254b73')
ax.axhline(0,color='black',lw=.7)
for r,lo,hi in [(.1,.18,.25),(5,-.071355633951,-.009745897257),(20,.070309824390,.084999667350)]:
    ax.plot([r,r],[lo,hi],color='#ba5428',lw=3)
ax.plot([],[],color='#ba5428',lw=3,label='Rigorous bounds (0.1: lower bound + universal upper bound)')
ax.set(xlabel='Actual flip rate r',ylabel='Top Lyapunov exponent',xlim=(.001,1000))
ax.legend(fontsize=7,loc='lower left')
fig.tight_layout()
for ext in ('png','pdf'):fig.savefig(ROOT/f'referee_data/independent_curve.{ext}',dpi=170)
