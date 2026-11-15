from common import log
import os
os.environ['MPLCONFIGDIR']=os.path.abspath('.matplotlib')
os.environ['XDG_CACHE_HOME']=os.path.abspath('.cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np,json,math
M=np.load('moments.npz')['moments'];mc=np.genfromtxt('mc_1000000.csv',delimiter=',',names=True)
fig,axes=plt.subplots(1,3,figsize=(12,3.5),layout='constrained')
for k,name in enumerate(('S','C','QC')):
    ax=axes[k];p=np.load(f'pmf/{name}/200.npy')
    with open(f'pmf/{name}/offsets.json') as f:off=json.load(f)[200]
    mu,v=M[200,k,:2];z=(np.arange(off,off+len(p))-mu)/math.sqrt(v)
    bins=np.linspace(-3.5,6,96);mass=np.histogram(z,bins=bins,weights=p)[0]/np.diff(bins)
    ax.stairs(mass,bins,label='Exact recursion, n=200',color='#356d99')
    x=mc[name];z=(x-np.mean(x))/np.std(x)
    ax.hist(z,bins=bins,density=True,histtype='step',label='Monte Carlo, n=1,000,000',color='#af603c',lw=1.2)
    zz=np.linspace(-3.5,6,400);ax.plot(zz,np.exp(-zz*zz/2)/math.sqrt(2*math.pi),'--',color='0.4',label='Standard normal')
    ax.set(title=name,xlabel='Centered index / standard deviation',xlim=(-3.5,6),ylim=(0,.6))
axes[0].set_ylabel('Probability density');axes[0].legend(fontsize=7)
fig.savefig('laws.png',dpi=180);fig.savefig('laws.pdf');plt.close(fig)
fig,axes=plt.subplots(1,3,figsize=(12,3.5),layout='constrained')
constants=json.load(open('constants.json'));n=np.arange(20,len(M));L=np.log(n)
axes[0].plot(n,M[n,0,1]/(n**2*L**2),label='S');axes[0].plot(n,M[n,1,1]/(n**2*L**2),label='C')
axes[0].axhline(float(constants['kappa_S_C']),ls='--',color='0.4',label='Proved limit');axes[0].set(title='Variance / (n² log² n)',xlabel='n');axes[0].legend()
axes[1].plot(n,M[n,2,1]/(n.astype(float)**4*L**2));axes[1].axhline(2/11,ls='--',color='0.4');axes[1].set(title='QC variance / (n⁴ log² n)',xlabel='n')
for k,name in enumerate(('S','C','QC')):axes[2].plot(n,M[n,k,2]/M[n,k,1]**1.5,label=name)
axes[2].axhline(float(constants['S_skewness']),ls=':',color='0.4');axes[2].axhline(float(constants['QC_skewness']),ls='--',color='0.4');axes[2].set(title='Standardized third moment',xlabel='n');axes[2].legend()
fig.savefig('trends.png',dpi=180);fig.savefig('trends.pdf');plt.close(fig)
log('Saved laws.png/pdf and trends.png/pdf; exact n=200 PMFs and independent n=10^6 simulations compared on common standardized axes.')
