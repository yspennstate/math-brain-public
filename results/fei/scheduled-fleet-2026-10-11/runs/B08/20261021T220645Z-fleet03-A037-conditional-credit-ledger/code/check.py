from exact import *
import sys
import exact

def h(t): return ent([t,1-t])
def half(a): return scale(a,F(1,2))
def point_H(m):
    d=F(2,2**m)
    return add(ent([(1-d)**2]),scale(log(1/d),2*(2*d-d*d)))

def scalar(m):
    d=F(2,2**m)
    beta=2*d*(1-d)
    phi=lambda t: sub(h(t),half(h(2*t)))
    q0=(1-d)**2+d*d
    t=(1-d)**(m-1)/(2*q0)
    O=kl([F(1,2)]*2,[t,1-t])
    J=phi(beta)
    G=scale(phi(d),m-1)
    reset=sub(add(O,J),G)
    D=sub(add(h(d),half(point_H(m-1))),point_H(m))
    if m==2: ck(reset[0]<=0<=reset[1])
    else: ck(reset[1]<0)
    if m>=5: ck(D[0]>0 and sub(h(d),D)[0]>0)
    if m>=6:
        ck(reset[1] <= -2*d*S)
        alpha=2*t-1
        ck(abs(alpha)<=F(16,15)*(m-1)*d<=F(1,6))
        ck(F(64,75)*(m-1)**2*d<=F(2,3))
        ck(J[1] <= F(9,4)*d*S)
        ck(O[1] <= F(2,3)*d*S)
    return {'m':m,'d':str(d),'reset':encode(reset),'initial_excess':encode(D),'reset_display':diag(reset),'initial_excess_display':diag(D)}

def actual(n):
    # bit order x,a,b,z0,... ; x=0 selects the character (-1)^a.
    N=n+3
    tab=[(-1 if t&2 else 1) if not t&1 else (-1 if t&4 and t>>3==0 else 1) for t in range(1<<N)]
    P,d,H,TC,S4=info(tab)
    Q=prodlaw(d)
    coords=list(range(N))
    first,E,O,zero=step(tab,Q,coords,1)
    ck(O[0]<=0<=O[1])
    dd=F(1,2**(n+1));m=n+2
    ck(d==[F(1,2),F(1,2)]+[dd]*(n+1))
    Hm=point_H(m)
    ck(sub(H,add(iv(2),half(point_H(m-1))))[0]<=0<=sub(H,add(iv(2),half(point_H(m-1))))[1])
    D=sub(add(h(dd),half(point_H(m-1))),Hm)
    ck(D[1]<h(dd)[0])
    if n>=3: ck(D[0]>0)
    else: ck(D[1]<0)
    debit=(max(0,D[0]),max(0,D[1]))
    ck(h(dd)[1]<F(3,5)*S)
    # Bank allocated once: prior global 1/4 plus actual initial excess D.
    # All booking is carried by the x-twisted a=1 lineage, not reassigned.
    booking=add(iv(F(1,2)),scale(debit,2))
    envelope=add(iv(F(1,2)),scale(h(dd),2))
    ck(envelope[1]<F(17,10)*S)
    leaves=[];root_tc=TC
    first_tc=sm(half(info(t)[3]) for t,q,c in first)
    first_kl=sm(half(kl(law(t),q)) for t,q,c in first)
    measured_D=sub(add(O,first_tc),TC)
    diff=sub(measured_D,D);ck(diff[0]<=0<=diff[1])
    initial_sigma=sub(first_tc,first_kl)
    for a,(t,q,c) in enumerate(first):
        p,ds,hh,tc,bank=info(t)
        ck(kl(p,prodlaw(ds))==tc or sub(kl(p,prodlaw(ds)),tc)[0]<=0<=sub(kl(p,prodlaw(ds)),tc)[1])
        ck(sub(hh,Hm)[0]<=0<=sub(hh,Hm)[1])
        ck(sum(ds)==(m*dd if a==0 else 1+(m-2)*dd))
        if a: ck(bank[0]>=2*S)
        # The conversion is EXERCISED: replace q by the actual product here.
        leaves.append((t,prodlaw(ds),c,F(1,2),a))
    levels=[]
    for depth in range(n+1):
        out=[];net=(0,0);hterm=(0,0);iterm=F(0);bankterm=(0,0);terminals=[]
        for t,q,c,w,a in leaves:
            p,ds,hh,tc,bank=info(t)
            hterm=add(hterm,scale(hh,w));iterm+=w*sum(ds)
            bankterm=add(bankterm,scale(bank,w))
            terminals.append({"a":a,"reach":str(w),"coords":c,"H":encode(hh),"I":str(sum(ds)),"TC_equals_current_reference_KL":encode(tc),"S4":encode(bank),"original_booking":encode(booking if a else (0,0)),"remaining_S4":encode(sub(bank,booking) if a else bank)})
            if a:
                ck(bank[0]>=2*S)
                ck(sub(bank,envelope)[0]>F(3,10)*S)
            else: ck(bank[0]>=0)
            if depth==n:continue
            # Only original private z bits are queried. Inactive branches stop.
            if len(set(t))==1 or all(t[j]==t[j^(1<<c.index(0))] * -1 for j in range(len(t))):
                out.append((t,q,c,w,a));continue
            query=3+depth
            kids,e,o,z=step(t,q,c,query)
            child_tc=(0,0)
            for tt,qq,cc in kids:
                pp,dds,hhh,tcc,bb=info(tt)
                child_tc=add(child_tc,half(tcc))
                # Exercise this reset as well. No canonical/root balance restarts.
                out.append((tt,prodlaw(dds),cc,w/2,a))
            sig=sub(add(o,child_tc),sub(tc,e))
            ck(sig[1]<0)
            net=add(net,scale(sub(add(o,child_tc),tc),w))
        if depth<n: ck(net[1]<=0 or net[0]<=0<=net[1])
        levels.append({'depth':depth,'leaf_count':len(leaves),'H':encode(hterm),'I':str(iterm),'S4':encode(bankterm),'next_net_liability':encode(net),'terminals':terminals})
        leaves=out
    return {'n':n,'original_root_A':encode(TC),'first_erasure':encode(E),'first_outcome_KL':encode(O),'first_pre_reset_KL':encode(first_kl),'first_exercised_reset':encode(initial_sigma),'initial_excess':encode(D),'initial_excess_display':diag(D),'prior_global_debit':'1/4','initial_original_twist_bank_lower_bound':'1','remaining_global_twist_bank_lower_bound':'3/20','levels':levels}

pilot='--pilot' in sys.argv
scalars=[scalar(m) for m in ([2,3,4,5,6] if pilot else range(2,21))]
arrays=[actual(n) for n in ([2] if pilot else [2,3,4,5,6])]
ck(log(2)[0]>F(2,3)*S)
ck(h(F(1,8))[1]<F(3,5)*S)
summary={'status':'PASS','assertions':exact.COUNT,'runtime_seconds':time.monotonic()-START,'pilot':pilot,'scalar':scalars,'actual_roots':arrays,'arithmetic':'Fraction and rigorous fixed-point log intervals; decimals diagnostic only'}
(BASE/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:summary[k] for k in ['status','assertions','runtime_seconds','pilot']}))
