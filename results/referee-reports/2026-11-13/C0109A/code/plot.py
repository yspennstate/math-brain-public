import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(ROOT/'data'/'mpl_config')
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
results=json.loads((ROOT/'data'/'fits.json').read_text())
fig,axes=plt.subplots(1,2,figsize=(10,4),layout='constrained')
for item in results:
 for ax,metric,label in zip(axes,['dK','radial_discrepancy'],['Orthant Kolmogorov distance','Centered-disc discrepancy']):
  ax.loglog(item['sizes'],item[metric]['medians'],'o-',label=f"ε={item['eps']:g}")
  ax.set(xlabel='Matrix size n',ylabel='Median distance (3 matrices)',title=label)
  ax.grid(alpha=.2,which='both')
axes[0].legend()
fig.suptitle('Exactly finite (2+ε) moment: finite-size evidence')
fig.savefig(ROOT/'data'/'convergence.svg')
