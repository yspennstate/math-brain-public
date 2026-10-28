import argparse,hashlib,itertools,json,math,runpy,time
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
H=runpy.run_path(str(A/'runs/20261023T110145Z-account03-A015-minterm-barrier-analysis/code/check.py'))
START=time.monotonic(); checks=0
def ck(x):
    global checks
    assert x;checks+=1
    if time.monotonic()-START>55:raise RuntimeError('frozen55s runtime cap')
def profile(s):
    m=s//2;delta=F(1,1<<s);mu=[];Ip=F(0);rows=[]
    for k in range(s+1):
        b=math.comb(s-k,m+1) if k<=m else 0
        value=2*delta**b-1;mu.append(value)
        private=2*s*b*delta**b if b else F(0)
        ck(value==1 if not b else -1<=value<=-1+2*delta)
        ck(private<=2*s*delta)
        Ip+=F(math.comb(s,k),1<<s)*private
        rows.append({'s':s,'k':k,'false_anchors':b,'mean':str(value),'private_influence':str(private)})
    avg=sum(F(math.comb(s,k),1<<s)*mu[k] for k in range(s+1))
    N=sum(F(math.comb(s,k),1<<s)*mu[k]**2 for k in range(s+1))-avg**2
    # Adjacent core restrictions are nested because the function is monotone.
    Iz=s*sum(F(math.comb(s-1,k),1<<(s-1))*(mu[k+1]-mu[k])/2 for k in range(s))
    Ih=F(s*math.comb(2*m,m),1<<(2*m))
    ck(N>=1-3*delta and N>=F(5,8));ck(Ip<=s*delta);ck(Iz<=Ih+s*delta);ck(Ip+Iz<=2*Ih)
    return rows,{'s':s,'N':str(N),'I_private':str(Ip),'I_core':str(Iz),'I_total':str(Ip+Iz),'I_majority':str(Ih)}
def main():
    p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true');pilot=p.parse_args().pilot
    rows=[];summaries=[]
    for s in ([3,5] if pilot else [3,5,7,9]):
        rr,ss=profile(s);rows+=rr;summaries.append(ss)
    anchors=[sum(1<<i for i in T) for T in itertools.combinations(range(3),2)]
    clauses=[(anchor,1<<(3+3*j+l)) for j,anchor in enumerate(anchors) for l in range(3)]
    vals=[1 if all((x&a) or (x&B) for a,B in clauses) else -1 for x in range(1<<12)]
    coeff=H['fw'](vals);N=sum(coeff[b]**2 for b in range(1,8));Iz=sum(coeff[b]**2*(b&7).bit_count() for b in range(len(coeff)))
    Ip=sum(coeff[b]**2*(b>>3).bit_count() for b in range(len(coeff)))
    ck(N==F(summaries[0]['N']));ck(Iz==F(summaries[0]['I_core']));ck(Ip==F(summaries[0]['I_private']));ck(Iz+Ip==H['inf'](vals))
    # All individual physical edges, including the nine distinct private bits.
    for i in range(12):
        direct=F(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals))),len(vals))
        spectral=sum(coeff[b]**2 for b in range(len(coeff)) if b>>i&1)
        ck(direct==spectral)
    for m in range(1,5 if pilot else 129):
        s=2*m+1;delta=F(1,1<<s);central=F(math.comb(2*m,m),1<<(2*m))
        ck(2*s*delta<=1);ck(1-3*delta>=F(5,8));ck(central**2*(m+1)<=1)
        ck(2*((1<<s)-1)>=1<<s)
    out={'status':'PASS','pilot':pilot,'assertions':checks,'physical_functions':1,'physical_truth_points':len(vals),'profile_rows':len(rows),'scalar_m':4 if pilot else 128,'profiles':summaries,'rows':rows,'elapsed_seconds':round(time.monotonic()-START,4),'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (R/'out'/('barrier_pilot.json' if pilot else 'barrier.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ['profiles','rows']},indent=2))
if __name__=='__main__':main()
