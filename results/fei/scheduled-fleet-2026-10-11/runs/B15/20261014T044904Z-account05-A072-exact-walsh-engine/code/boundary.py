import json,sys,time,math
from fractions import Fraction as F
from functools import lru_cache
import audit as u
R=u.R;B=u.B;ck=u.ck
g=tuple(-1 if x in (0,1,2) else 1 for x in range(64))
def plus(*intervals):return tuple(sum(x[k] for x in intervals) for k in (0,1))
def times(x,c):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def entropy(cert):return u.a.ent(cert['spectrum'])
def child(i,side):
    return tuple(g[(x&((1<<i)-1))|(side<<i)|((x>>i)<<(i+1))] for x in range(32))
@lru_cache(None)
def outer(name,p):
    t=u.H if name=='h' else u.J;c=list(map(F,t));v=[4*z*(1-z) for z in p]
    for j in range(6):
        for s in range(64):
            if not s>>j&1:
                a,b=c[s],c[s|(1<<j)];c[s]=(1-p[j])*a+p[j]*b;c[s|(1<<j)]=b-a
    masses=[c[S]**2*math.prod(p[j]*(1-p[j]) for j in range(6) if S>>j&1) for S in range(64)]
    ck(sum(masses)==1)
    for x in range(64):
        ck(sum((c[S]*math.prod(F((x>>j)&1)-p[j] for j in range(6) if S>>j&1) for S in range(64)),F(0))==t[x])
    qs=[]
    for j in range(6):
        q=sum((math.prod(p[l] if x>>l&1 else 1-p[l] for l in range(6) if l!=j) for x in range(64) if not x>>j&1 and t[x]!=t[x|(1<<j)]),F(0))
        ck(sum((masses[S] for S in range(64) if S>>j&1),F(0))==v[j]*q);qs.append(q)
    C=u.a.e.subtract(u.a.ent(masses),plus(*(times(u.a.ent((1-vj,vj)),q) for vj,q in zip(v,qs))))
    return {'biases':p,'masses':masses,'q':qs,'C':C,'coefficients':c}
def direct_boundary(name,j,i,p):
    t=u.H if name=='h' else u.J;total=F(0)
    for x in range(32):
        a,b=child(i,0)[x],child(i,1)[x]
        for z in range(32):
            other=(z&((1<<j)-1))|((z>>j)<<(j+1))
            y0=other|((a<0)<<j);y1=other|((b<0)<<j)
            if t[y0]!=t[y1]:total+=p**z.bit_count()*(1-p)**(5-z.bit_count())/32
    return total
def run(pilot):
    start=time.perf_counter();cap=55 if pilot else 120
    base=B.uniform_certificate(g);p=F(3,64);Hg=entropy(base);Ig=sum(base['influences'])
    children={(i,s):B.uniform_certificate(child(i,s)) for i in (0,2) for s in (0,1)}
    rows=[]
    for name in ('h','J'):
        B.uniform_certificate(u.H if name=='h' else u.J)
        root=outer(name,(p,)*6);q=root['q'];C=root['C'];rootH=plus(times(Hg,sum(q)),C);rootI=sum(q)*Ig
        for j,i in ([(0,2)] if pilot else [(0,0),(0,2),(1,0),(1,2)]):
            sub=[];Hs=[];Is=[]
            for side in (0,1):
                cg=children[i,side];pc=F(sum(z<0 for z in child(i,side)),32);pv=list((p,)*6);pv[j]=pc
                bc=outer(name,tuple(pv));sub.append(bc)
                Hs.append(plus(times(entropy(cg),bc['q'][j]),times(Hg,sum(bc['q'][l] for l in range(6) if l!=j)),bc['C']))
                Is.append(bc['q'][j]*sum(cg['influences'])+sum(bc['q'][l]*Ig for l in range(6) if l!=j))
            for l in range(6):ck((sub[0]['q'][l]+sub[1]['q'][l])/2==q[l])
            ck(sub[0]['q'][j]==sub[1]['q'][j]==q[j])
            di=base['influences'][i];edge=direct_boundary(name,j,i,p)
            ck(edge==q[j]*di==rootI-(Is[0]+Is[1])/2)
            deltaC=u.a.e.subtract(C,times(plus(sub[0]['C'],sub[1]['C']),F(1,2)))
            deltaG=u.a.e.subtract(Hg,times(plus(entropy(children[i,0]),entropy(children[i,1])),F(1,2)))
            deltaF=u.a.e.subtract(rootH,times(plus(*Hs),F(1,2)))
            diagnostic=u.a.e.subtract(deltaF,plus(times(deltaG,q[j]),deltaC));ck(diagnostic[0]<=0<=diagnostic[1])
            sign='POSITIVE' if deltaC[0]>0 else ('NEGATIVE' if deltaC[1]<0 else 'UNRESOLVED_OR_ZERO')
            row={'gate':name,'block':j,'inner_coordinate':i,'parent_p':p,'child_p':[b['biases'][j] for b in sub],
                 'core_walsh':base['walsh'],'child_walsh':[children[i,s]['walsh'] for s in (0,1)],
                 'physical_influence':edge,'parent_C':C,'child_C':[b['C'] for b in sub],'delta_C_bounds':deltaC,'delta_C_sign':sign,
                 'delta_H_g_bounds':deltaG,'delta_H_F_bounds':deltaF,'identity_interval_diagnostic':diagnostic,
                 'full_query_excess_at_K4':u.a.e.subtract(deltaF,(4*edge,4*edge)),
                 'normalized_curvature_delta_C_over_Inf':[z/edge for z in deltaC],
                 'parent_outer':root,'child_outers':sub}
            rows.append(row);u.dump('boundary_case_'+name+'_'+str(j)+'_'+str(i)+'.json',row)
            ck(time.perf_counter()-start<cap)
    result={'passed':True,'queries':len(rows),'assertions':u.checks,'runtime_seconds':time.perf_counter()-start,'curvature_signs':{s:sum(r['delta_C_sign']==s for r in rows) for s in ['POSITIVE','NEGATIVE','UNRESOLVED_OR_ZERO']},'note':'Complete starting and child entropy retained. No universal payment conclusion.'}
    u.dump('boundary_pilot.json' if pilot else 'boundary_validation.json',result);print(json.dumps(result))
if __name__=='__main__':run('--pilot' in sys.argv)
