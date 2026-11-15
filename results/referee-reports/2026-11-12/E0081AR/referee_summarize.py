"""Recheck reported means, finite analytic bounds and resource records."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,sqrt,exp,log,lgamma
import csv,json
root=Path('referee_results')
def mass(n,b):
    if abs(b)>n or (n+b)%2:return 0.
    k=(n+b)//2
    return exp(lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)-n*log(2))
def rec(s):return F(comb(s-1,(s-1)//2),2**s)
rows=[]
for b in csv.DictReader(root.joinpath('blocks.csv').open()):
    n=int(b['n']);a=int(b['a']);L=n//2
    ev=1+sum((rec(s) for s in range(1,L+1)),F(0))
    ev2=1+sum((rec(s) for s in range(1,2*L+1)),F(0))
    pot=1+sum((rec(s)**2 for s in range(1,L+1)),F(0))
    d=1.
    for s in range(1,L+1):
        peak=max(1,int(sqrt(s+1)-1));peak+=(s-peak)%2
        if peak*(peak+2)<s:peak+=2
        d+=peak/s*mass(s,peak)
    en=(L+1)*a/n*mass(n,a)
    lower=en/d;upper=mass(n-L,(n-L)%2)*float(ev2/pot)
    # These are statistical comparisons, not exact proofs.
    rows.append(dict(n=n,a=a,EN_theory=en,EN_sample=float(b['EN']),EN_z=(float(b['EN'])-en)/float(b['se_N']),G_theory=float(pot),G_sample=float(b['G_sample']),EV_theory=float(ev),EV_sample=float(b['EV']),ER_sample=float(b['ER']),ER_upper=float(ev2/pot),q_sample=float(b['q']),q_lower=lower,q_upper=upper))
claim=list(csv.DictReader(Path('claim_files/data/monte_carlo.csv').open()))
comparisons=[]
for row in csv.DictReader(root.joinpath('waiting.csv').open()):
    same=next((c for c in claim if c['n']==row['n'] and c['a']==row['a']),None)
    if same:
        z=(float(row['mean_end'])-float(same['mean']))/sqrt(float(row['se'])**2+float(same['se'])**2)
        comparisons.append(dict(n=int(row['n']),a=int(row['a']),combined_z=z))
summary=dict(blocks=rows,submission_comparisons=comparisons)
root.joinpath('summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
