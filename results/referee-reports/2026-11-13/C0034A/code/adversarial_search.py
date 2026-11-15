"""Search real/complex orthogonal decompositions by optimizing Farkas functionals.

The transportation matrix depends only on ranks. Each rational dual vector y
satisfies M^T y >= 0 exactly. We minimize b(Q).y over a Cayley chart of O(n)
or U(n), then evaluate the full min-L1-violation LP at the resulting point.
No numerical negative value alone is a counterexample.
"""
from exact_transport import *
from scipy.optimize import minimize


def float_rhs(Q,groups,states):
    return np.concatenate([abs(np.linalg.det(Q[np.array(ss)][:,:,list(cols)]))**2 for cols,ss in zip(groups,states)])

def cayley(parameters,n,is_complex):
    S=np.zeros((n,n),dtype=complex if is_complex else float);at=0
    for i in range(n):
        for j in range(i):
            S[i,j]=parameters[at];S[j,i]=-parameters[at];at+=1
    if is_complex:
        for i in range(n):
            for j in range(i+1):
                S[i,j]+=1j*parameters[at]
                if i!=j:S[j,i]+=1j*parameters[at]
                at+=1
    assert at==len(parameters)
    return np.linalg.solve(np.eye(n)+S,np.eye(n)-S)

def exact_dual(y,As,Bs,Cs,pairs):
    yy=[F(float(x)).limit_denominator(10**6) for x in y]
    ia={A:i for i,A in enumerate(As)};ib={B:i+len(As) for i,B in enumerate(Bs)}
    ic={C:i+len(As)+len(Bs) for i,C in enumerate(Cs)}
    # Enlarge each union coordinate to repair every rationalized inequality.
    for A,B in pairs:
        k=ic[tuple(sorted(A+B))]
        yy[k]=max(yy[k],-yy[ia[A]]-yy[ib[B]])
    assert all(yy[ia[A]]+yy[ib[B]]+yy[ic[tuple(sorted(A+B))]]>=0 for A,B in pairs)
    return yy

def violation(M,b):
    d=linprog(b,A_ub=-M.T,b_ub=np.zeros(M.shape[1]),bounds=(-1,1),method='highs-ds',
              options={'threads':1,'parallel':False,'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    assert d.success
    # By LP duality, -d.fun is the min L1 residual over x>=0.
    return float(-d.fun),d

def positive_control():
    n=3;As,Bs,Cs,pairs,inds,M=transport_structure(n,1,1)
    a={A:F(A==(0,)) for A in As};b={B:F(B==(1,)) for B in Bs};c={C:F(C==(0,2)) for C in Cs}
    rhs=[a[A] for A in As]+[b[B] for B in Bs]+[c[C] for C in Cs]
    # alpha_0=beta_1=-1; gamma_01=2, gamma_02=gamma_12=1.
    y=[F(-1),F(0),F(0),F(0),F(-1),F(0),F(2),F(1),F(1)]
    slacks=[sum((y[i] for i in ii),F(0)) for ii in inds]
    dot=sum((v*w for v,w in zip(rhs,y)),F(0))
    assert min(slacks)>=0 and dot==-1
    v,_=violation(M,np.array(list(map(float,rhs))))
    assert v>0.5
    record={'description':'Deliberately mismatched union law, not an orthogonal-decomposition counterexample',
            'n':n,'As':As,'Bs':Bs,'Cs':Cs,'rhs':list(map(str,rhs)),
            'dual':list(map(str,y)),'M_transpose_y':list(map(str,slacks)),'rhs_dot_y':str(dot),
            'min_L1_violation_float':v}
    dump(ROOT/'data/positive_control_farkas.json',record)
    return record

def run():
    start=time.monotonic();control=positive_control();records=[]
    rng=np.random.default_rng(340013)
    for n,p,q in [(6,2,2),(7,2,2)]:
        As,Bs,Cs,pairs,inds,M=transport_structure(n,p,q)
        states=[As,Bs,Cs];groups=[list(range(p)),list(range(p,p+q)),list(range(p+q))]
        for is_complex in [False,True]:
            for trial in range(8):
                dim=n*n if is_complex else n*(n-1)//2
                initial=rng.normal(size=dim)*0.45
                base=cayley(initial,n,is_complex)
                b0=float_rhs(base,groups,states)
                v0,_=violation(M,b0)
                dual=None
                for perturb in [0.5,2,8,24]:
                    cost=b0+perturb*rng.normal(size=len(b0))/len(b0)
                    lp=linprog(cost,A_ub=-M.T,b_ub=np.zeros(M.shape[1]),bounds=(-1,1),method='highs-ds',
                               options={'threads':1,'parallel':False})
                    assert lp.success
                    candidate=exact_dual(lp.x,As,Bs,Cs,pairs)
                    yf=np.array(list(map(float,candidate)))
                    if max(M.T@yf)>1e-6:dual=candidate;break
                assert dual is not None
                yf=np.array(list(map(float,dual)))
                evaluations=0
                def objective(parameters):
                    nonlocal evaluations
                    evaluations+=1
                    return float(float_rhs(cayley(parameters,n,is_complex)@base,groups,states)@yf)
                optimum=minimize(objective,np.zeros(dim),method='L-BFGS-B',bounds=[(-2,2)]*dim,
                                 options={'maxiter':60,'maxfun':6000,'ftol':1e-13,'gtol':1e-8})
                final=cayley(optimum.x,n,is_complex)@base
                bf=float_rhs(final,groups,states)
                vf,full_dual=violation(M,bf)
                m=len(bf);nv=M.shape[1]
                phase1=linprog(np.r_[np.zeros(nv),np.ones(2*m)],
                               A_eq=np.c_[M,np.eye(m),-np.eye(m)],b_eq=bf,bounds=(0,None),
                               method='highs-ds',options={'threads':1,'parallel':False,
                               'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
                assert phase1.success
                primal_residual=float(np.sum(abs(M@phase1.x[:nv]-bf)))
                orth_error=float(np.max(abs(final.conj().T@final-np.eye(n))))
                record={'n':n,'p':p,'q':q,'field':'complex' if is_complex else 'real','trial':trial,
                        'dual_exact':list(map(str,dual)),
                        'initial_functional':float(b0@yf),'optimized_functional':float(bf@yf),
                        'initial_min_L1_violation_raw':v0,'final_min_L1_violation_raw':vf,
                        'final_primal_L1_residual':primal_residual,
                        'final_primal_min_coordinate':float(min(phase1.x[:nv])),
                        'phaseI_primal_dual_gap_raw':float(phase1.fun+full_dual.fun),
                        'optimizer_success':bool(optimum.success),'optimizer_message':str(optimum.message),
                        'iterations':int(optimum.nit),'function_evaluations':evaluations,'orthogonality_error':orth_error,
                        'final_Q_real':final.real.tolist(),'final_Q_imag':final.imag.tolist()}
                records.append(record)
                summary={'seed':340013,'runs':len(records),'total_objective_evaluations':sum(r['function_evaluations'] for r in records),
                         'max_min_L1_violation_raw':max(r['final_min_L1_violation_raw'] for r in records),
                         'max_primal_L1_residual':max(r['final_primal_L1_residual'] for r in records),
                         'min_fixed_dual_functional':min(r['optimized_functional'] for r in records),
                         'elapsed_seconds':time.monotonic()-start,'records':records,
                         'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                         'nice':os.getpriority(os.PRIO_PROCESS,0),'threads':1}
                dump(ROOT/'data/adversarial_results.json',summary)
                print(n,record['field'],trial,'dual',record['optimized_functional'],'violation',vf,'evals',evaluations,flush=True)
                if vf>1e-7:
                    # Save the candidate and stop for exact rational conversion.
                    # An exact Farkas certificate for an orthogonal rational
                    # instance must be constructed before any counterexample claim.
                    raise RuntimeError('Candidate violation saved: exact conversion required')
    print('DONE',len(records),time.monotonic()-start,flush=True)
if __name__=='__main__':run()
