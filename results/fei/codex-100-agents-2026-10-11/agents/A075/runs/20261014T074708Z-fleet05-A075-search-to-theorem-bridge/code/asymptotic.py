from block_reveal import *
def trim(a):
    while len(a)>1 and not a[-1]:a.pop()
    return a
def plus(a,b):
    out=[Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return trim(out)
def times(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)
def mul(a,c):return trim([x*c for x in a])
def ev(a,p):return sum((x*p**i for i,x in enumerate(a)),Q(0))
def masspolys(endpoint=None):
    means=[[1,-2] for j in range(6)];vars=[[0,4,-4] for j in range(6)]
    if endpoint is not None:means[0]=[1 if endpoint==0 else -1];vars[0]=[0]
    out=[]
    for T in range(64):
        c=[Q(0)];v=[Q(1)]
        for U,w in enumerate(W):
            if U&T!=T:continue
            z=[Q(w,64)]
            for j in range(6):
                if (U^T)>>j&1:z=times(z,means[j])
            c=plus(c,z)
        for j in range(6):
            if T>>j&1:v=times(v,vars[j])
        out.append(times(v,times(c,c)))
    total=[Q(0)]
    for z in out:total=plus(total,z)
    ar.ck(total==[Q(1)])
    return out
def pivotpolys(endpoint=None):
    out=[]
    for j in range(6):
        q=[Q(0)]
        for x in range(64):
            if x>>j&1 or J[x]==J[x^(1<<j)]:continue
            term=[Q(1)]
            for l in range(6):
                if l==j:continue
                if l==0 and endpoint is not None:
                    term=mul(term,Q(((x>>l)&1)==endpoint))
                else:term=times(term,[0,1] if x>>l&1 else [1,-1])
            q=plus(q,term)
        out.append(q)
    return out
# coefficient triple: rational combination of logs of positive integers, log2 p coefficient, log2(e) coefficient
def zero():return ({},Q(0),Q(0))
def aadd(x,y,c=Q(1)):return ar.add(x[0],y[0],c),x[1]+c*y[1],x[2]+c*y[2]
def ascale(x,c):return ar.scale(x[0],c),x[1]*c,x[2]*c
def coeff(loga=Q(0),a=Q(1),logp=Q(0),loge=Q(0)):return ar.scale(logq(a),loga),logp,loge
def entseries(masses):
    out=[zero() for i in range(3)]
    for z in masses:
        z=[Q(c) for c in z]
        if not any(z):continue
        r=next(i for i,x in enumerate(z) if x);a=z[r];ar.ck(a>0)
        b=z[r+1] if r+1<len(z) else Q(0);c=z[r+2] if r+2<len(z) else Q(0)
        if r==0:
            out[0]=aadd(out[0],coeff(-a,a))
            out[1]=aadd(out[1],coeff(-b,a,loge=-b))
            out[2]=aadd(out[2],coeff(-c,a,loge=-c-b*b/(2*a)))
        elif r==1:
            out[1]=aadd(out[1],coeff(-a,a,-a))
            out[2]=aadd(out[2],coeff(-b,a,-b,-b))
        elif r==2:out[2]=aadd(out[2],coeff(-a,a,-2*a))
    return out
def boundtriple(x):
    ar.ck(all(isinstance(c,Q) for c in [x[1],x[2]]))
    ar.ck(x[1]==0)
    lo,hi=ar.enclose(x[0]);l,u=Q(1)/ar.LN2[1],Q(1)/ar.LN2[0]
    lo+=x[2]*(l if x[2]>=0 else u);hi+=x[2]*(u if x[2]>=0 else l)
    return {'log_form':ar.forms(x[0]),'log_p_coefficient':str(x[1]),'log_e_coefficient':str(x[2]),'lower':str(lo),'upper':str(hi),'display':[float(lo),float(hi)]}
def main():
    start=time.perf_counter();polys=[masspolys(x) for x in [None,0,1]]
    es=[entseries(z) for z in polys]
    # q0 polynomial, exact other-five pivot law
    q=[Q(0)]
    for x in range(64):
        if x&1 or J[x]==J[x^1]:continue
        term=[Q(1)]
        for j in range(1,6):term=times(term,[0,1] if x>>j&1 else [1,-1])
        q=plus(q,term)
    v=[[0,4,-4],[1,-4,4]];hs=entseries(v)
    delta=[]
    for i in range(3):
        z=aadd(es[0][i],es[1][i],Q(-1))
        if i:z=aadd(aadd(z,es[1][i-1]),es[2][i-1],Q(-1))
        for j in range(min(i,len(q)-1)+1):z=aadd(z,hs[i-j],-q[j])
        delta.append(z)
    ar.ck(delta[0]==zero() and delta[1]==zero() and delta[2][1]==0)
    # S4(g_n)/p -> 6 log2 3 - 8/3 - 4 log2 e
    corelim=({3:Q(6),2:Q(-8,3)},Q(0),Q(-4))
    ar.ck(q[0]==0)
    banklim=ascale(corelim,q[1]);excesslim=aadd(delta[2],banklim,Q(-1))
    bounds=[boundtriple(x) for x in [corelim,delta[2],banklim,excesslim]]
    ar.ck(Q(bounds[3]['lower'])>0)
    qminus=[Q(0)]
    for z in pivotpolys(1)[1:]:qminus=plus(qminus,z)
    Cminus=[]
    for i in range(3):
        z=es[2][i]
        for j in range(min(i,len(qminus)-1)+1):z=aadd(z,hs[i-j],-qminus[j])
        Cminus.append(z)
    ar.ck(Cminus[0]==zero() and Cminus[1]==zero() and Cminus[2][1]==0 and qminus[0]==0)
    minuslim=aadd(ascale(corelim,qminus[1]),Cminus[2],Q(-1))
    mb=boundtriple(minuslim);ar.ck(Q(mb['upper'])<0)
    # Independent polynomial evaluation matches direct rational endpoint masses.
    for p in [Q(3,64),Q(3,128),Q(1,1000)]:
        for j,end in enumerate([None,0,1]):
            ps=[p]*6
            if end is not None:ps[0]=Q(end)
            _,qs,masses=outer(ps)
            ar.ck([ev(z,p) for z in polys[j]]==masses);ar.ck(ev(q,p)==qs[0])
    out={'q0_polynomial':[str(x) for x in q],'minus_endpoint_other_pivot_sum_polynomial':[str(x) for x in qminus],'core_S4_over_p_limit':bounds[0],'block_delta_C_over_p2_limit':bounds[1],'selected_bank_over_p2_limit':bounds[2],'signed_full_block_excess_over_p2_limit':bounds[3],'minus_endpoint_C_over_p2_limit':boundtriple(Cminus[2]),'minus_endpoint_full_S4_over_p2_limit':mb,'constant_and_linear_and_p2logp_cancel_exactly':True,'remainder':'O(p^3(1+abs(log2 p))) for outer quantities; S4(g_n)=p*core_limit+O(p^2*n), hence excess and minus-endpoint full S4 have p^2*their limits+O(p^3*n), p=3*2^-n. Coefficients rational, fixed finite polynomials, analytic Taylor log at their positive leading coefficients.','scope':'Positive excess and negative full minus-endpoint S4 for all sufficiently large integer n, with no claimed explicit all-tail cutoff. Exact n6 finite certificate is a separate witness.','polynomial_masses':[[[str(c) for c in z] for z in row] for row in polys],'checks':ar.checks,'runtime_seconds':time.perf_counter()-start}
    assert out['runtime_seconds']<55
    (ROOT/'out/ASYMPTOTIC.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['polynomial_masses']}))
if __name__=='__main__':main()
