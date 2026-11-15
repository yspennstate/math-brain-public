from common import log
import glob,json,csv,math
import numpy as np
mom=np.load('moments.npz')['moments'];out=[]
for path in glob.glob('mc_*.csv'):
    d=np.genfromtxt(path,delimiter=',',names=True);n=int(d['n'][0]);R=len(d)
    for k,name in enumerate(('S','C','QC')):
        x=d[name];mu=float(np.mean(x));delta=x-mu;v=float(np.mean(delta**2));m3=float(np.mean(delta**3));m4=float(np.mean(delta**4))
        power=4 if name=='QC' else 2
        row={'file':path,'n':n,'replicates':R,'index':name,'mean':mu,'variance':v,'mean_se':math.sqrt(v/R),'variance_se':math.sqrt((m4-v*v)/R),'variance_scaled':v/(n**power*math.log(n)**2),'skewness':m3/v**1.5,'kurtosis':m4/v**2}
        if n<len(mom):
            row['mean_z']=(mu-float(mom[n,k,0]))/row['mean_se'];row['variance_z']=(v-float(mom[n,k,1]))/row['variance_se']
        out.append(row)
    corr=float(np.corrcoef(d['S'],d['C'])[0,1]);log(f'MC {path}: n={n}, R={R}, corr(S,C)={corr}; '+json.dumps(out[-3:]))
with open('mc_summary.json','w') as f:json.dump(out,f,indent=2)
