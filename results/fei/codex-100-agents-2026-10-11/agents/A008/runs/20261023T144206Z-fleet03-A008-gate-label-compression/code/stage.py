from pathlib import Path
from fractions import Fraction as F
import json, hashlib, time, sys
from datetime import datetime, timezone
R=Path(__file__).resolve().parents[1]; H=R.parents[1]
S=H.parent/'A007/runs/20261023T140735Z-fleet03-A007-root-normalization'
P=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,v): p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
for d in ['code','out']: (R/d).mkdir(parents=True,exist_ok=True)
spec={'helper_version':'A008-oriented-extraction-v1','helper_sha256':sha(Path(__file__)),'family':'All labelled nonconstant Boolean cores with signed clauses a_v OR y_v,l; private groups per false point','domain':'pilot: s=1,2 L=1; full: s=1,2,3 L=1 plus s=1,2 L=2; scalar s=1..128, delta=2^-d,d=0..8','case_count':{'pilot':16,'full_boolean':286,'scalar':1152},'symmetry':'None; all labelled truth tables','arithmetic':'Integer Walsh, Fraction squared masses and physical edge influence; exact algebraic log identity, no numerical log signs','memory_estimate_mb':60,'max_runtime_seconds':55,'automatic_escalation':False}
save(R/'SPEC.json',spec)
proof='''# Orientation-aware finite arbitrary-core extraction

Uniform physical cubes, costs in bits. This is a finite strengthening of A007's source-reference reduction, not full FEI.

For every nonconstant sign Boolean g on s>=1 bits and 0<delta<=1, choose h in {g,-g} with false density q<=1/2. The squared Fourier spectrum, variance and influence of h equal those of g. Let A be the least integer with 2^A>=8s/delta and put L=2A, epsilon=2^-L. For each false core point v, form L signed clauses a_v(z) OR y_v,l with distinct positive private bits, where a_v is false exactly at v. The sign of their conjunction is F_L. The representation, orientation and core event are fixed before any spectral set.

Each displayed clause is an irredundant prime implicate: setting core=v and just its selected private bit false isolates the clause. Removing the private literal fails at v with all private bits true. Removing a core literal fails at the neighboring core point with that literal flipped and with all other relevant private groups true. This proves minimality without claiming completeness of the prime table.

An independent reconstruction of A007: F_L=h+2 sum_{v:h(v)=-1} 1_v AND(y_v). Hence E_y F_L=(1-epsilon)h+epsilon. Every nonempty core coefficient is (1-epsilon) hhat(B). A private-supported coefficient is zero if it meets two groups; otherwise, for each nonempty subset of one group and each core subset, its magnitude is 2^(1-s)epsilon. The entire private spectral mass is 4q epsilon(1-epsilon), its entropy exactly that mass times (2s+2L-2). The finitely many core probabilities converge to those of h, and the displayed private entropy tends to zero. Thus H(F_L)->H(g) without dimension-dependent continuity assumptions.

Direct physical edges give

 I(F_L)=(1-epsilon)^2 I(g)+2q epsilon[s(1-epsilon)+L].

Indeed a core edge crossing true/false disagrees with probability 1-epsilon, while a false/false edge uses TWO DISTINCT private groups and disagrees with probability 2epsilon(1-epsilon). Its total false/false oriented incidence is sq-I(g)/2. Private edges contribute 2qL epsilon. This is the physical influence, not an independent-copy surrogate.

For any fixed normalized or subprobability nonempty reference R covering F_L's spectrum, define Z=sum_{B nonempty core}R(B,empty), and r(B)=R(B,empty)/Z. The sign orientation changes no target probability. The COMPLETE equality is

 C_g(r)=C_core(F_L;R)/(1-epsilon)^2+Var(g) log2 Z.

Coverage gives 0<Z<=1. The negative normalizer is retained in the equality before using C_core<=C_total and log Z<=0. A decoder for r conditions the supplied finite alphabet on its fixed core-only event and outputs that core subset; every original branch, gate name, attachment, local-mask choice and final allocation is already included in the supplied R mass. No new free label, output-dependent prior or history reset is assumed. Its logarithmic rate is the normalized finite-alphabet rate; integral prefix overhead is not silently omitted.

Poincare gives I(g)>=Var(g)=4q(1-q)>=2q. Therefore a supplied complete nonempty cost C_total(F_L;R)<=K I(F_L), K>=0, yields

 C_g(r)<=K[1+epsilon(s+L)/(1-epsilon)^2]I(g).

The denominator is essential; omitting it is an invalid finite extraction. Here A>=3, epsilon<=1/64 and (1-epsilon)^-2<2. Put x=8s/delta. For x>=8, ceil(log2 x)<=x (on each dyadic interval the least integer exponent is <= its lower endpoint). Thus A<=8s/delta. Since delta<=1,

 epsilon<=delta^2/(64s^2),
 2epsilon(s+2A)<=delta^2/(32s)+delta/(2s)
                    <=17delta/(32s)<=delta.

Consequently C_g(r)<=(1+delta)K I(g). This is FINITE, with L=2ceil(log2(8s/delta)), reducing A007's exhibited 4s+4 choice to logarithmic per-clause private multiplicity for fixed accuracy, while preserving the full conditioning refund. It does not shrink the exponential number of false core points, price R, or prove a universal core supplier.

Independent A007 whole-claim review: the prime-clause witnesses, all spectrum sectors, exact influence, entropy limit, normalizer equality, finite 2K bound at L=4s+4, and same-constant FEI equivalence all hold as stated. For its finite bound, 5s+4<=2^(3s+2) starts at s=1 and propagates by multiplying the right side by eight; each nonconstant core has at least one changing edge, so I(g)>=2^(1-s). No substantive repair to A007 is required. Its all-positive PRIVATE literals must not be confused with all-positive CORE literals. A008's earlier obstruction is not a premise of this review.

First unsupported universal line: supply the original fixed reference R for arbitrary signed cores with complete cost<=K I(F_L) from one physical influence account. The orientation and shorter finite lift do not pay that source. Full FEI remains OPEN.
'''
(R/'PROOF_AND_REVIEW.md').write_text(proof,encoding='utf-8')
def walsh(a):
    a=list(a); step=1
    while step<len(a):
        for b in range(0,len(a),2*step):
            for j in range(b,b+step):
                x,y=a[j],a[j+step];a[j],a[j+step]=x+y,x-y
        step*=2
    return a
checks=0
def ck(v):
    global checks
    checks+=1
    assert v, checks
def case(s,table,L):
    M=1<<s; g=[1 if table>>x&1 else -1 for x in range(M)]
    false=[x for x in range(M) if g[x]<0]; idx={v:i for i,v in enumerate(false)}
    n=s+L*len(false); N=1<<n; eps=F(1,1<<L); q=F(len(false),M)
    vals=[]
    for x in range(N):
        z=x&(M-1)
        direct=1 if g[z]>0 or (x>>(s+L*idx[z]))&((1<<L)-1)==(1<<L)-1 else -1
        clause=all(z!=v or (x>>(s+L*j+l))&1 for j,v in enumerate(false) for l in range(L))
        ck(direct==2*clause-1);vals.append(direct)
    gw=walsh(g); fw=walsh(vals)
    Ig=F(sum(k.bit_count()*x*x for k,x in enumerate(gw)),M*M)
    If=F(sum(k.bit_count()*x*x for k,x in enumerate(fw)),N*N)
    edges=sum(vals[x]!=vals[x^(1<<j)] for x in range(N) for j in range(n))
    ck(If==F(edges,N));ck(If==(1-eps)**2*Ig+2*q*eps*(s*(1-eps)+L))
    private_mass=F(0)
    for b,x in enumerate(fw):
        core=b&(M-1); pm=b>>s
        if not pm:
            expected=(1-eps)*F(gw[core],M)+(eps if core==0 else 0)
            ck(F(x,N)==expected)
        else:
            groups=[j for j in range(len(false)) if (pm>>(L*j))&((1<<L)-1)]
            expected=F(0)
            if len(groups)==1:
                j=groups[0];sgn=-1 if ((core&false[j]).bit_count()+pm.bit_count())%2 else 1
                expected=sgn*F(2,M)*eps
            ck(F(x,N)==expected);private_mass+=F(x*x,N*N)
    ck(private_mass==4*q*eps*(1-eps));ck(sum(F(x*x,N*N) for x in fw)==1)
    # Two fixed full references; test every extracted mass, not an author helper.
    for skew in [False,True]:
        total=sum((b+1 if skew else 1) for b in range(1,N))
        z=F(sum((b+1 if skew else 1) for b in range(1,M)),total)
        ck(0<z<=1)
        for b in range(1,M):
            rr=F(b+1 if skew else 1,total)
            rc=rr/z
            ck(rc==F(b+1 if skew else 1,sum(k+1 if skew else 1 for k in range(1,M))))
            ck(F(fw[b]**2,N*N)==(1-eps)**2*F(gw[b]**2,M*M))
    return n
def execute(pilot):
    global checks
    checks=0;t=time.perf_counter(); count=0;maxn=0
    domains=[(s,1) for s in ([1,2] if pilot else [1,2,3])]
    if not pilot:domains += [(1,2),(2,2)]
    for s,L in domains:
        for table in range(1,(1<<(1<<s))-1):
            maxn=max(maxn,case(s,table,L));count+=1
    scalar=0
    if not pilot:
        for s in range(1,129):
            for d in range(9):
                delta=F(1,1<<d);x=8*s/delta;A=0
                while 1<<A<x:A+=1
                L=2*A;eps=F(1,1<<L)
                ck(A>=3);ck(A<=x);ck(eps*(s+L)/(1-eps)**2<=delta)
                scalar+=1
    out={'status':'PASS','boolean_cases':count,'scalar_cases':scalar,'checks':checks,'max_n':maxn,'elapsed_seconds':time.perf_counter()-t,'helper_sha256':sha(Path(__file__))}
    assert out['elapsed_seconds']<55
    save(R/'out'/('pilot.json' if pilot else 'full.json'),out)
    return out
pilot=execute(True);full=execute(False)
protocol=load(P);fields=protocol['required_per_run']
source=next(c for c in load(S/'CLAIMS.json') if c['claim_id']=='A007-SIGNED-CORE-PRIVATE-CLAUSE-UNIVERSALITY-AND-NORMALIZATION')
source['review_records'].append({'reviewer':'A008','verdict':'HOLDS_FULL_STATED_SCOPE','independent':True,'evidence':['PROOF_AND_REVIEW.md','out/full.json'],'scope':'Independent signed clause, physical-edge and exact full-spectrum reconstruction; no repair supplied; finite source normalization and all-parameter entropy limit reviewed.'})
statement='For every nonconstant Boolean g on s>=1 uniform bits, every 0<delta<=1 and K>=0, choose h in {g,-g} with false density q<=1/2 and form A007 signed-core positive-private clauses with L=2ceil(log2(8s/delta)) private bits per false core point. Any fixed normalized or subprobability nonempty reference R covering F_L and having complete nonempty cross-entropy <=K I(F_L) induces a normalized nonempty core reference r with C_g(r)<=(1+delta)K I(g). The exact extraction is C_g(r)=C_core(F_L;R)/(1-2^-L)^2+Var(g)log2 Z, with Z its original core-sector mass. No source supplier, history reset or FEI theorem is asserted.'
hyp=['Uniform physical cube, signed core literals, disjoint relevant positive private variables.','All references, orientation and represented core event fixed before the spectral set; costs in bits.','The supplied-reference bound is a hypothesis, not proved for arbitrary cores.']
cid='A008-ORIENTED-LOGARITHMIC-FINITE-CORE-EXTRACTION'
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest(),'contributors':['A008'],'proof_source':['PROOF_AND_REVIEW.md','code/stage.py','out/full.json'],'proof_dependencies':[{'claim_id':source['claim_id'],'version':source['version'],'statement_sha256':source['statement_sha256'],'acceptance':'Independent A008 reconstruction in this run'},'Poincare I(g)>=Var(g), directly from degree-weighted Fourier Parseval.'],'review_records':[],'status':'PROVED_LOCALLY_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':'No gap in stated conditional extraction. Universal source reference for arbitrary signed cores is unpaid.','next_consumers':['A007','A015','A086','A094','B02']}
claims=[source,claim]
for c in claims: assert set(c)==set(fields['claim_fields'])
save(R/'CLAIMS.json',claims)
next_action='A007/A015 independently reconstruct the oriented finite extraction; price the ORIGINAL arbitrary signed-core reference with all labels, signed fusion and conditioning refund from ONE physical influence account.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B02','packet_id':'A008','gap_id':'C020-PI-J-COMPLETE-FIXED-REFERENCE-NAME-RANK-PAYMENT','attempt_id':R.name,'method':'Full independent A007 universality review; sign-oriented Poincare finite extraction; actual clause truth tables, integer Walsh and physical edges.','mathematical_delta':'Accepted complete A007 arbitrary-core universality/normalization claim; improved explicit finite per-clause lift from 4s+4 to logarithmic multiplicity with arbitrarily small multiplicative source-cost loss 1+delta.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'CONDITIONAL_EXTRACTION_PROVED_LOCALLY_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':source['claim_id'],'version':source['version'],'statement_sha256':source['statement_sha256']}],'claims_created_or_changed':[{'claim_id':source['claim_id'],'version':source['version'],'change':'A008 independent whole-claim acceptance'},{'claim_id':cid,'version':1,'change':'new finite extraction corollary'}],'source_artifacts':['PROOF_AND_REVIEW.md','SPEC.json','code/stage.py','out/pilot.json','out/full.json','out/SOURCE_RECEIPTS.json'],'next_consumers':['A007','A015','A086','A094','B02'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Original arbitrary-core supplier remains unproved.','New finite extraction needs independent review.','Brain self-care degraded/unverified: personal model101.2h, state-of-mind85.8h and latest dream36.5h stale.','Checklist service lock held too long during initial working/previous-stage done attempt; no seen mark made.'],'packet_ids':['A008']}
assert set(progress)=={x.split(' (')[0] for x in fields['progress_fields']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
receipts=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in [S/'CORE_EMBEDDING.md',S/'CLAIMS.json',P]]
save(R/'out/SOURCE_RECEIPTS.json',receipts)
bodies=[statement+'\n\n'+' '.join(hyp)+' Full FEI remains OPEN.',
 'Read current BOARD.md (2026-10-23 14:39 UTC), B02 STREAM_NOTES.md v2, own STATUS.md and machine AGENTS.md. Complete mathematical source read: A007 run20261023T140735Z CORE_EMBEDDING.md, exact universality claim and full REPORT. A010 latest full REPORT read as context only; no independent acceptance of its new bundle is claimed. Prior campaign/paper/protocol baseline reads inherited; field contract freshly loaded. out/SOURCE_RECEIPTS.json pins immutable mathematical source bytes. The old shared-core extension was already done by A006, so it was not duplicated. No new literature-priority assertion.',
 'PROOF_AND_REVIEW.md contains the full reconstruction and new proof. Choose sign so q<=1/2, hence 2q<=I(g) by Poincare. Retain the exact Var(g)log Z conditioning refund and the denominator (1-epsilon)^2. The additional source-cost ratio is <=epsilon(s+L)/(1-epsilon)^2. For A=ceil(log2(8s/delta)), L=2A, A>=3 and A<=8s/delta, this is <=2epsilon(s+2A)<=17delta/(32s)<=delta. This proves the finite (1+delta) transfer. It does not pay the source R. First unsupported universal line: an original fixed reference paid by physical influence for arbitrary signed cores, including all branches and fusion. No adaptive-history reset follows.',
 'Frozen SPEC.json saved before executing the helper. Command: python -X utf8 code/stage.py. It executes a bounded pilot, saves its output, then the fixed full domain and persistence. Pilot: '+str(pilot)+'. Nonpilot: '+str(full)+'. All 286 actual labelled nonconstant core/lift cases: s<=3,L=1 plus s<=2,L=2; no symmetry quotient. Every literal CNF truth input is compared with its independent conditional form, complete signed coefficients are checked against integer Walsh, physical edges independently recover influence, and full private mass plus two reference normalization profiles are checked. Scalar finite bound checked at 1152 exact rational (s,delta) pairs; the all-parameter claim is proved analytically, not inferred from this finite range. No floating mathematical sign or source helper import. Entropy limit and cost identity are analytic equalities; no numerical entropy certificate claimed. Estimate60MB, runtime limit55s, max dimension10, no escalation, GPU, detached worker or >300MB job. Wake/reading overhead crossed the nominal 14:49 campaign deadline; only this already-derived proof certification and final persistence were completed afterward. No new open-ended search was started.',
 'The complete A007 claim is independently accepted without repair, including prime/irredundant (not complete prime-table) scope, exact full private sector, physical influence, entropy limit, signed normalizer and finite 2K transfer. The new conditional corollary is locally proved and independently unreviewed. The older A008 common-anchor theorem has independent acceptance reported in A006/A010/A015 board updates; no new imported review record was fabricated. Full signed cores are FEI-universal; all-positive core clauses have not been proved universal by this reduction. No source/shared index was modified.',
 next_action,
 'Four protocol files, proof, frozen spec and exact outputs saved only inside A008; schemas and identical PROGRESS/PACKET_DELTA verified with packet_ids=[A008]. STATUS.md has two lines; WORKLOG.md and LEARNED.md appended. out/PERSISTENCE.json pins sizes and hashes with readback; all files<20MB. No remote mirror or downstream adoption receipt is claimed. Checklist T-20261023-551 working and T-20261023-432 closure attempts encountered a shared service lock; record closure only if the final retry succeeds. Brain self-care is degraded/unverified: personal-model, state-of-mind and dream freshness remain affected; they supply no mathematical premise. No shared work was stopped, restarted or load-shed. No research computation is left running.' ]
report='\n\n'.join('## '+title+'\n\n'+body for title,body in zip(fields['report_fields'],bodies))
report+='\n\n## Universal bridge\n\nC020 whole-set witness cost moves by independent acceptance of the arbitrary-core universality barrier and by an explicit finite (1+delta)-cost extraction with logarithmic per-clause private multiplicity, retaining the exact signed conditioning refund. The arbitrary ORIGINAL core-sensitive reference is still unpaid; the exponentially large false-core truth table is not compressed by this lemma. NEXT directly attacks that universal supplier with the same physical influence owner, rather than treating another bounded-core family as a solution. Full FEI remains OPEN.\n'
(R/'REPORT.md').write_text(report,encoding='utf-8')
(H/'STATUS.md').write_text('STATE: A008 stage144206: A007 arbitrary-core universality independently HOLDS; oriented logarithmic finite extraction gives (1+delta) source transfer; exact checks PASS; new review pending; FEI OPEN.\nNEXT: A007/A015 review finite extraction; price ORIGINAL arbitrary signed-core fixed reference including all labels/fusion/refund from ONE physical influence account.\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
for filename,body in [('WORKLOG.md','Read fresh board; did not duplicate A006 shared-core result. Independently reconstructed complete A007 signed-core universality. New oriented Poincare argument gives finite (1+delta) extraction with L=2ceil(log2(8s/delta)); denominator and negative normalizer retained. Exact independent validation: '+str(full)+'. Original supplier and full FEI open; new corollary awaits review.'),('LEARNED.md','For any nonconstant Boolean core, sign orientation ensures false density q<=1/2 and 2q<=I. In A007 signed-core/private clause lift, conditioning supplied R to core gives C_g=C_core/(1-epsilon)^2+Var(g)log Z. With L=2ceil(log2(8s/delta)), extra ratio epsilon(s+L)/(1-epsilon)^2<=delta. Thus any supplied K-paid lift reference gives finite (1+delta)K-paid core reference with logarithmic private multiplicity. This neither compresses the false-core table nor pays the original universal source. See '+R.name+'/PROOF_AND_REVIEW.md.')]:
    with (H/filename).open('a',encoding='utf-8') as f:f.write('\n\n'+stamp+' — '+body+'\n')
items=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE.json':
        assert p.stat().st_size<20_000_000
        items.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
for p in [H/'STATUS.md',H/'WORKLOG.md',H/'LEARNED.md']:
    items.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
save(R/'out/PERSISTENCE.json',{'verified_at':stamp,'artifacts':items,'full_fei':'OPEN','full_checks':full['checks']})
for i in items:assert sha(Path(i['path']))==i['sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((H/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
print(json.dumps({'saved':True,'pilot':pilot,'full':full,'verified_artifacts':len(items),'FEI':'OPEN'}))
