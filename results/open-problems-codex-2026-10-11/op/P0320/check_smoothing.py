import json, math
from pathlib import Path
from scipy.integrate import quad

def averaged(d,s,r):
    norm=math.gamma(d/2)/(math.sqrt(math.pi)*math.gamma((d-1)/2))
    def radial(t):
        angular=quad(lambda th: (r*r+t*t+2*r*t*math.cos(th))**(-s/2)*math.sin(th)**(d-2),0,math.pi,epsabs=1e-12,epsrel=1e-12)[0]
        return d*norm*t**(d-1)*angular
    return quad(radial,0,1,epsabs=1e-12,epsrel=1e-12)[0]

rows=[]
for d,s in [(2,.5),(2,1.),(3,1.5),(3,2.),(4,2.5),(4,3.)]:
    expected=s*(s+2-d)/(2*(d+2))
    for r in [math.sqrt(8),5.,10.,20.,40.]:
        error=averaged(d,s,r)-r**(-s)
        assert error>0
        rows.append(dict(d=d,s=s,r=r,error=error,scaled_error=error*r**(s+2),asymptotic=expected))
    r=math.sqrt(8); err=averaged(d,s,r)-r**(-s)
    c0=d/(d-s)
    for mass in [0,1,10,100,1000]:
        rows.append(dict(d=d,s=s,mass=mass,both_mimicry_costs=c0-4**(-s)+mass*err))
Path('smoothing_checks.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
print('Positive smoothing error verified for 30 quadratures; asymptotic ratios:')
for row in rows:
    if row.get('r')==40.: print(row['d'],row['s'],row['scaled_error']/row['asymptotic'])
print('No numerical gas simulation or inference about rigidity is made.')
