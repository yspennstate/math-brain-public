from pathlib import Path
import json,time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
import numpy as np
from check_signmap import root_a
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter()
cert=json.loads((ROOT/'out'/'THRESHOLD_CERTIFICATE.json').read_text());pc=sum(cert['decimal_display_only'])/2
def hv(x):
    x=np.clip(x,1e-300,1-1e-16)
    return -x*np.log2(x)-(1-x)*np.log2(1-x)
v=(np.arange(400)+.5)/400;p,q=np.meshgrid(v,v)
r=4*q*(1-q);t=p*r
F=2*hv(t)-p*hv(r)
for m in [(1-2*p*q)**2,4*p*(1-p)*q*q,p*p*r,p*(1-p)*r]:
    F+=np.where(m>0,m*np.log2(np.maximum(m,1e-300)),0)
fig,ax=plt.subplots(figsize=(7.6,6.6))
fig.subplots_adjust(left=.11,right=.98,top=.92,bottom=.15)
ax.imshow(F>0,origin='lower',extent=[0,1,0,1],cmap=ListedColormap(['#b4d7e8','#f0b18b']),aspect='equal',interpolation='nearest')
ax.axhline(.5,color='black',lw=1.2)
pp=np.linspace(.5+1e-5,1,300);ax.plot(pp,1/(2*pp),color='black',lw=1.2)
for high in [False,True]:
    ps=np.linspace(pc+1e-5,.5-1e-5,120) if not high else np.linspace(.5+1e-5,1-pc-1e-5,120)
    lows=[];highs=[]
    for val in ps:
        theta=np.arcsin(np.sqrt(val));s=theta if not high else np.pi/2-theta;a=root_a(s)
        if not high:lows.append((1-np.tan(s-a)/np.tan(theta))/2);highs.append((1-np.tan(a)/np.tan(theta))/2)
        else:lows.append((1+np.tan(a)/np.tan(theta))/2);highs.append((1+np.tan(s-a)/np.tan(theta))/2)
    ax.plot(ps,lows,color='black',lw=1.2);ax.plot(ps,highs,color='black',lw=1.2)
ax.scatter([pc,1-pc],[1/(2*(1+np.sqrt(1-pc))),1/(2*np.sqrt(1-pc))],s=22,color='black',zorder=4)
ax.set(xlim=(0,1),ylim=(0,1),xlabel='p = Pr(X = 1)',ylabel='q = Pr(Y = 1)',title='Biased AND: exact sign regions of J_X − M_X')
ax.text(.69,.48,'q = 1/2',fontsize=10,ha='center',va='top')
ax.text(.78,.72,'q = 1/(2p)',fontsize=10,rotation=-27)
ax.legend(handles=[Patch(facecolor='#f0b18b',label='J_X > M_X: tax-free bound fails'),Patch(facecolor='#b4d7e8',label='J_X < M_X'),plt.Line2D([],[],color='black',label='J_X = M_X')],loc='upper right',fontsize=8)
fig.text(.5,.025,'Analytic classification: PROOF.md. Curve positions and shading are numerical illustrations.',ha='center',fontsize=8)
fig.savefig(ROOT/'out'/'SIGN_MAP.png',dpi=170,bbox_inches='tight')
fig.savefig(ROOT/'out'/'SIGN_MAP.svg',bbox_inches='tight')
plt.close(fig)
(ROOT/'out'/'PLOT_RECEIPT.json').write_text(json.dumps({'runtime_seconds':time.perf_counter()-start,'proof_status':'illustration only; continuum theorem in PROOF.md','outputs':['SIGN_MAP.png','SIGN_MAP.svg']},indent=2),encoding='utf-8')
print('Saved standalone sign-map PNG and SVG.',flush=True)
