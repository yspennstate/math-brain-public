from exact import *
import exact as eng

def sub(a,b):return combine((1,a),(-1,b))
def kl(p,q):return sub(ce(p,q),entropy(p))
def lower_nat(expr,rhs):
    if not expr:check(rhs==0)
    else:check(bounds(expr)[0]*ln2[0]>=rhs)

controller=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1]
bb=[1-x*x for x in controller]
aa=[F(x,16) for x in walsh(controller)]; bh=[F(x,16) for x in walsh(bb)]
beta=sum(x*x for x in bh);check(beta==F(3,8))
def coherent(h,R,sigma):
    mu=F(sum(h),len(h));return [(a+sigma*mu*b)**2 if T==0 else b*b*R[T] for a,b in zip(aa,bh) for T in range(len(R))]
def wrapped(h,sigma):return [a+sigma*b*x for a,b in zip(controller,bb) for x in h]

rows=0; eligible=0; exact_edges=0; positive_rows=0; fixed=0
for truth in range(256):
    v=[1 if truth>>z&1 else -1 for z in range(8)]
    amps=[F(x,8) for x in walsh(v)];p=[x*x for x in amps];a0=1-p[0]
    if not a0:continue
    for j in range(3):
        if amps[1<<j] or any(amps[T]*amps[T|(1<<j)] for T in range(8) if not T&(1<<j)):continue
        eligible+=1
        pc=[spectrum(restrict(v,j,s)) for s in (0,1)];pb=marginal(p,j)
        check(pc[0]==pc[1]==pb);check(not erased(p,j));exact_edges+=1
        # Exact-match inheritance is checked in both actual outcomes.
        check(all(not sub(ce(child,pb),entropy(child)) for child in pc))
        for theta in [F(0),F(1,4),F(1,2),F(3,4)]:
            R=[p[0] if T==0 else ((1-theta)*p[T]+theta*a0/6 if T!=1<<j else F(0)) for T in range(8)]
            check(sum(R)==1 and R[0]==p[0] and not R[1<<j])
            rb=marginal(R,j)
            delta=sum(abs(x-y) for x,y in zip(pb[1:],rb[1:]))/(2*a0)
            W=sum((p[T]+p[T|(1<<j)])*(p[T|(1<<j)]/(p[T]+p[T|(1<<j)])-R[T|(1<<j)]/(R[T]+R[T|(1<<j)]))**2 for T in range(8) if not T&(1<<j) and p[T]+p[T|(1<<j)])
            eta=delta*delta+W/a0
            check((not eta)==(R==p))
            occ=sub(kl(p,R),kl(pb,rb));lower_nat(occ,2*W)
            bins=[[T for T in range(1,4) if (pb[T]>rb[T])==flag] for flag in [True,False]]
            cal=[p[0]]+[F(0)]*3
            for block in bins:
                mass=sum(pb[T] for T in block);ref=sum(rb[T] for T in block)
                if mass:check(ref>0)
                for T in block:cal[T]=mass*rb[T]/ref if ref else F(0)
            check(sum(cal)==1)
            refund=sub(ce(pb,rb),ce(pb,cal));lower_nat(refund,2*a0*delta*delta)
            for strength in [eta/(1+eta)]+([F(1,64)] if eta>=F(1,63) else []):
                if strength==F(1,64):fixed+=1
                for target in [[F(0),F(1,3),F(1,3),F(1,3)],[F(0),F(1),F(0),F(0)]]:
                    new=[p[0]]+[(1-strength)*cal[T]+strength*a0*target[T] for T in range(1,4)]
                    tax=sub(ce(pb,new),ce(pb,cal))
                    inc=combine((-beta,occ),(-beta,refund),(beta,tax))
                    if eta:check(bounds(inc)[1]*ln2[0]<=-beta*a0*eta);positive_rows+=1
                    else:check(not inc)
                    rows+=1
            check(time.perf_counter()-start<55)

# Full seven-bit wrapper witnesses: no factored CE assumption in this audit.
witnesses=[]
parity=[-1 if z.bit_count()%2 else 1 for z in range(8)]
for mask in [6,3,7]:
    R=[F(0)]*8;R[7]+=F(1,2);R[mask]+=F(1,2)
    for sigma in [-1,1]:
        v=wrapped(parity,sigma);Q=coherent(parity,R,sigma);P=spectrum(v)
        check(sum(Q)==1)
        check(coherent(parity,spectrum(parity),sigma)==P)
        children,ps,r,B,rho=query(v,Q,0)
        check(not B)
        seed_child=restrict(parity,0,0);pseed=spectrum(seed_child)
        cal=pseed
        new=[F(0)]*4;new[3]=F(63,64);new[1]=F(1,64)
        Qcal=coherent(seed_child,cal,sigma);Qnew=coherent(seed_child,new,sigma)
        check(ps[0]==ps[1]==spectrum(wrapped(seed_child,sigma)))
        calibration=sub(ce(ps[0],r),ce(ps[0],Qcal))
        tax=sub(ce(ps[0],Qnew),ce(ps[0],Qcal))
        inc=combine((1,B),(F(1,2),ce(ps[0],Qnew)),(F(1,2),ce(ps[1],Qnew)),(-1,ce(P,Q)))
        check(not combine((1,inc),(1,rho),(1,calibration),(-1,tax)))
        check(not sub(tax,combine((beta,logq(F(64,63))))))
        if mask!=7:check(bounds(inc)[1]<-F(93,256))
        else:check(not rho and not calibration and positive(inc))
        witnesses.append({'reference_masks':[7,mask],'sigma':sigma,'full_transaction':display(inc),'occupancy_refund':display(rho),'calibration_refund':display(calibration),'new_reset_cost':display(tax)})
        check(time.perf_counter()-start<55)

out={'status':'PASS','assertions':eng.assertions,'all_boolean_tables':256,'isospectral_edges':eligible,'exact_match_edges':exact_edges,'profile_transactions':rows,'positive_eta_transactions':positive_rows,'fixed_strength_references':fixed,'witnesses':witnesses,'elapsed_seconds':time.perf_counter()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'helper_sha256':hashlib.sha256(Path(eng.__file__).read_bytes()).hexdigest(),'proof_scope':'A004 full statement independently reconstructed from statement only; global fixed-rate chaining conditional on supplied coherent reference; exact-match isospectral queries admit no-reset deferral'}
(run/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps(out,indent=2))
