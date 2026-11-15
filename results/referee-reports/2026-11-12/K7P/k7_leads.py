"""Exact audits of proposed proof shortcuts and a diagonal obstruction family."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
import json,time,resource,random
from fractions import Fraction as Q
from q1_core import exact,lump,solve,serialize
from q2_families import k5,clone
from q2_search import partitions,correction,random_w,log

start=time.monotonic();out={};counts=0;rng=random.Random(70017)
def put(key,data):
    if key in out:return
    out[key]=serialize(data)
    with open('k7_leads_results.json','w') as f:json.dump(out,f,indent=2)
    log('Exact lead audit: '+key+'; details saved in k7_leads_results.json.')

family=[]
for t in (2,10,1000):
    w=k5(Q(t));x=exact(w);z=exact(lump(w,[[0],[1],[2,3]]))
    W=x['W'];S=Q(t*t+2*t+2);aa=W/Q(t*t)*(1-S/W)**2
    assert z['F'][0][0]-x['F'][0][0]==aa
    assert x['t']==max(x['F'][0])
    for shape in ('triple','pairs'):
        if shape=='triple':
            v=clone(w,3,2);bs=[[0],[1],[2,3,4]]
        else:
            v=clone(clone(w,2,2),3,2);bs=[[0],[1],[2,3],[4,5]]
        xx=exact(v);zz=exact(lump(v,bs))
        assert xx['t']==x['t'] and zz['t']==z['t']
        assert xx['F'][0][0]==x['F'][0][0] and zz['F'][0][0]==z['F'][0][0]
        family.append(dict(t=t,shape=shape,w=v,partition=bs,T=xx['t'],a=aa,a_over_T=aa/xx['t']))
        for n in (6,7,8):
            padded=clone(v,0,n-len(v)+1)
            pp=bs+[[a] for a in range(len(v),n)]
            px=exact(padded);pz=exact(lump(padded,pp))
            assert px['t']==x['t'] and pz['t']==z['t']
            assert pz['F'][0][0]-px['F'][0][0]==aa
            family.append(dict(t=t,shape=shape,n=n,w=padded,partition=pp,T=px['t'],a=aa,a_over_T=aa/px['t']))
put('diagonal_family',family)

# A second, irrelevant pair shows why adding the intermediate row maxima is too weak.
w=k5(Q(10))
for _ in range(2):
    old=len(w);w=[row+[Q(0)] for row in w]+[[Q(0)]*(old+1)]
    w[3][old]=w[old][3]=Q(1,10**6)
bs1=[[0],[1],[2,3],[4],[5]];bs=[[0],[1],[2,3],[4,5]]
x=exact(w);z1=exact(lump(w,bs1));z=exact(lump(w,bs))
ti=max(x['F'][0]);tj=max(x['F'][1]);sum1=max(z1['F'][0])+max(z1['F'][1])
assert sum1>ti+tj+x['t']
put('intermediate_row_sum_exceeds_proposed_budget',dict(w=w,partition=bs,T=x['t'],ti=ti,tj=tj,row_sum_after_first=sum1,budget=ti+tj+x['t'],Fhat=z['F'][0][1]))

for n in (6,7,8):
    for trial in range(12):
        w=random_w(n,rng);x=exact(w);F=x['F'];ti=list(map(max,F));T=x['t']
        for bs in partitions(n,n-2):
            h=correction(F,bs);ss=[(k,b[0]) for k,b in enumerate(bs) if len(b)==1]
            dif=[(a,b[0]) for b in bs for a in b[1:]]
            V=[[F[i][a]-F[i][b] for a,b in dif] for i in range(n)]
            S=[[V[a][k]-V[b][k] for k in range(2)] for a,b in dif]
            for k,i in ss:
                for l,j in ss:
                    if i>=j:continue
                    ai=h[k][k]-F[i][i];aj=h[l][l]-F[j][j];cross=h[k][l]-F[i][j]
                    if cross>0 and ai*aj>(3*T-F[i][j])**2:
                        put('cauchy_schwarz_bound_exceeds_3T',dict(w=w,partition=bs,i=i,j=j,T=T,Fij=F[i][j],Fhat=h[k][l],ai=ai,aj=aj,cross=cross,positive_square_gap=ai*aj-(3*T-F[i][j])**2))
                    if ai and cross>0:
                        lam=cross/ai
                        vi=solve(S,[-v for v in V[i]]);vj=solve(S,[-v for v in V[j]])
                        qi=[sum(a*b for a,b in zip(v,vi)) for v in V]
                        qj=[sum(a*b for a,b in zip(v,vj)) for v in V]
                        gamma=[a-lam*b for a,b in zip(qj,qi)]
                        psij=[ti[j]-F[j][a]-gamma[a] for a in range(n)]
                        if min(psij)<0:
                            put('removing_orthogonal_boundary_part_loses_nonnegativity',dict(w=w,partition=bs,i=i,j=j,T=T,lambda_=lam,gamma=gamma,modified_phi_j=psij))
                        # Verify gamma is energy orthogonal to Qphi_i via its value at i.
                        assert gamma[i]==0
                    counts+=1
        if time.monotonic()-start>170:break
    if time.monotonic()-start>170:break
log(f'Lead audit complete: {counts} singleton-pair tests, {time.monotonic()-start:.3f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes.')
print('ALL LEAD CHECKS PASSED',list(out),flush=True)
