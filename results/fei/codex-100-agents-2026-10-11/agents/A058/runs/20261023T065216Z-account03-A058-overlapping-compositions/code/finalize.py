from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from functools import lru_cache
from math import lcm
import json,hashlib,time

R=Path(__file__).resolve().parents[1]; Aroot=R.parents[1]
P=Aroot/'runs/20261023T024748Z-account03-A058-overlapping-compositions'
started=time.perf_counter()
def dump(name,obj): (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
@lru_cache(None)
def factors(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def add(*pairs):
    v=defaultdict(Q)
    for scale,u in pairs:
        for p,c in u.items():v[p]+=scale*c
    return {p:c for p,c in v.items() if c}
@lru_cache(None)
def entropy(tt):
    v=defaultdict(Q);N=len(tt)
    for t in range(N):
        a=Q(sum(y*(-1 if (x&t).bit_count()%2 else 1) for x,y in enumerate(tt)),N)
        p=a*a
        if not p:continue
        for prime,c in factors(p.denominator).items():v[prime]+=p*c
        for prime,c in factors(p.numerator).items():v[prime]-=p*c
    return {p:c for p,c in v.items() if c}
def influence(tt):
    n=(len(tt)-1).bit_length()
    return Q(sum(tt[x]!=tt[x^(1<<i)] for x in range(len(tt)) for i in range(n)),len(tt))
def ge(v):
    d=lcm(*(c.denominator for c in v.values())) if v else 1
    pos=neg=1
    for p,c in v.items():
        n=int(c*d)
        assert abs(n)<1000000
        if n>0:pos*=p**n
        elif n<0:neg*=p**(-n)
    return pos>=neg
def chain(a,b,k):return tuple(a[x&3] if x>>2==(1<<k)-1 else b[x&3] for x in range(4<<k))
tables=[tuple(-1 if m>>x&1 else 1 for x in range(4)) for m in range(16)]
cases=checks=0;witness=None
for k in [1,2,3]:
    alpha=Q(1,1<<k)
    for ai,a in enumerate(tables):
        for bi,b in enumerate(tables):
            f=chain(a,b,k);g=chain(a,b,k-1)
            eouter=tuple(y*b[x&3] for x,y in enumerate(g))
            delta=Q(sum(x!=y for x,y in zip(a,b)),4)
            Ie=influence(tuple(x*y for x,y in zip(a,b)))
            J=Q(sum(x!=b[i&3] for i,x in enumerate(g)),len(g))
            B=4*J+influence(eouter)
            assert B==2*alpha*Ie+4*alpha*(k+1)*delta;checks+=1
            D=add((Q(1),entropy(f)),(-alpha,entropy(a)),(-(1-alpha),entropy(b)))
            assert ge(D);assert ge(add((Q(3)*B,{2:Q(1)}),(Q(-1),D)));checks+=2
            assert influence(f)==alpha*influence(a)+(1-alpha)*influence(b)+2*k*alpha*delta;checks+=1
            if k==2 and ai==0 and bi==10:
                old=add((Q(1),entropy(f)),(Q(-1,2),entropy(g)),(Q(-1,2),entropy(b)))
                inner=add((Q(1,2),entropy(g)),(Q(-1,4),entropy(a)),(Q(-1,4),entropy(b)))
                assert ge(old) and old and ge(inner) and inner
                deficit=add((Q(1),old),(Q(1),inner),(-B,{2:Q(1)}))
                assert ge(deficit) and deficit and 2**16>3**9
                witness={'B':str(B),'old_outer_debit':{str(p):str(c) for p,c in old.items()},'reached_inner_debit':{str(p):str(c) for p,c in inner.items()},'deficit':{str(p):str(c) for p,c in deficit.items()},'integer_sign':'2^16>3^9'}
            cases+=1;assert time.perf_counter()-started<60
ind={'status':'PASS','cases':cases,'assertions':checks,'method':'actual full truth tables, direct character sums and Fraction prime-log forms; signs from exact integer products; actual outer product influence','witness':witness,'elapsed_seconds':time.perf_counter()-started,'independent_agent_review':False}
dump('out/INDEPENDENT_VALIDATION.json',ind)

protocolpath=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocolpath.read_text(encoding='utf-8-sig'))
statement='For arbitrary Boolean A,B on the same finite uniform data cube, k>=1 fresh fair selectors, alpha=2^-k, and F_k equal to A only when all selectors are1 and B otherwise, let delta=Pr(A!=B), E=I(AB), D_k=H(F_k)-alpha H(A)-(1-alpha)H(B), and B_k=2alpha E+4alpha(k+1)delta. Then 0<=D_k<=3 B_k. B_k is exactly the v7 outermost-selector ticket 4Inf_outer(F_k)+I(F_(k-1)B). ONE original allocation 3B_root pays every signed coherent debit along any adaptive physical stopping tree, retaining all complete inherited core decrements and actual terminals; no descendant ticket is renewed. Price1 is false already at k2,A=1,B=x: D_2=4-(9/8)log2(3)>B_2=2, after a positive outer debit. The same family has D_k/B_k tending to2, so any all-depth multiplier is at least2. Price2 remains open. If H(A)<=C I(A) and H(B)<=C I(B), then H(F_k)<=max(C+6,9)I(F_k), uniformly in k. Arbitrary branching source ownership and full FEI remain open.'
claim=json.loads((P/'CLAIMS.json').read_text(encoding='utf-8'))[0]
claim.update(version=8,exact_statement=statement,statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),hypotheses=['finite uniform cubes; entropy in bits; Boolean A,B arbitrary overlapping data','k fresh fair selectors, independent of data; point activation all1','ONE original allocation3B, fixed before actual signed debits','both inherited branch bills and every actual terminal retained; old debit not reset','conditional FEI transfer assumes both complete cores satisfy the specified C'],proof_source=['PROOF.md','LOG_CERTIFICATE.md','code/exact_chain.js','code/finalize.py','out/EXACT_VALIDATION.json','out/INDEPENDENT_VALIDATION.json'],proof_dependencies=['v7 single-selector source for k1; reconstructed proof in previous run','exact coherent Fourier posterior; entropy tensorization on an input indicator; scalar Taylor upper bound','no numerical or external unreviewed assertion used to bridge dimensions'],review_records=[{'reviewer':'A091','status':'PENDING; primary; no external message sent'},{'reviewer':'A090','status':'PENDING; alternate; no external message sent'}],status='AUTHOR_PROOF_AND_EXACT_CERTIFICATES; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',supersedes=['A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER@7 (extends; v7 statements preserved)'],refutes=['Exploratory price1 claim: original outer B_root alone funds all subsequent nested coherent selector costs; false on explicit3-bit A=1,B=x,k2'],first_unproved_line='Price2 is unproved. No allocation of genuinely new costs from arbitrary two-surviving-branch mux structures to the SAME already diminished source, with inherited cores and old debit retained.',next_consumers=['A091','A090','A057','A059','A060','B12','B20'])
assert set(claim)==set(protocol['required_per_run']['claim_fields']);dump('CLAIMS.json',[claim])
progress=json.loads((P/'PROGRESS.json').read_text(encoding='utf-8'))
progress.update(run_id=R.name,attempt_id='substantive-stage8-rare-chain-original-source',method='coherent row posterior + indicator entropy tensorization + scalar weighted-JS Taylor estimate; exact original-source accounting',mathematical_delta='Closed all-depth rare-switch repair for arbitrary overlapping A,B: ONE original3B funds every stopped coherent ledger; no renewed bank. Actual positive-old-debit price1 obstruction; necessary multiplier>=2, price2 unproved. Conditional branch FEI transfer max(C+6,9), independent of chain length.',deliverable_status='COMPLETE_LOCAL; review and supervisor adoption unverified',mathematical_status='author-proved dimension-independent original-source lemma; finite exact certificates; full FEI OPEN',claim_versions_used=['A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER@7'],claims_created_or_changed=['A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER@8'],source_artifacts=['PROOF.md','LOG_CERTIFICATE.md','FROZEN_SPEC.json','INDEPENDENT_SPEC.json','code/exact_chain.js','code/finalize.py','out/EXACT_VALIDATION.json','out/INDEPENDENT_VALIDATION.json','out/SOURCE_RECEIPTS.json'],next_consumers=['A091','A090','A057','A059','A060','B12','B20'],next_action='Expose a SECOND surviving activation branch after actual nonzero coherent debit; price only its new row cost from SAME original3B slack or original physical-edge owner, retain both full cores and all old debit. Do not merely optimize3 to2.',stagnant_substantive_attempts=0,blockers=['independent review pending','second-surviving-branch source ownership unpaid','arbitrary inherited core FEI unpaid','brain wake degraded: personal model/state notes stale; not proof premises'],packet_ids=['A058'])
fields=set(protocol['required_per_run']['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids');assert set(progress)==fields
dump('PROGRESS.json',progress);dump('PACKET_DELTA.json',progress)

sections={
'exact target, quantifiers, hypotheses and units':'All finite uniform cubes, arbitrary Boolean A,B sharing the same data, k>=1 fresh fair selector bits, entropy in bits. F_k chooses A only on the all1 selector point, otherwise B. The exact original v7 outer ticket is B_k=2alpha I(AB)+4alpha(k+1)Pr(A!=B), alpha=2^-k. PROOF.md proves full coherent overhead D_k<=3B_k, uniformly in k and both data functions. The original allocation is made ONCE and retains all inherited core bills and actual terminals. Full FEI is OPEN.',
'sources actually read, revisions and theorem locators':'Current STATUS.md, BOARD.md B12 A056-A060 and referee/source-frontier entries, B12 STREAM_NOTES.md v2 (2026-10-11 23:30 UTC), complete EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2, and previous v7 PROOF.md. Read-only math recall used two wordings and returned prior coordinate-deficit/bent-splice guards; none is a proof dependency. Earlier campaign/paper orientation is inherited from previous stages, not claimed as a fresh source audit. User campaign extension governs stale protocol end date. A059 rare-switch bank warning is respected: no whole-subformula bank per level.',
'complete derivation or exact first unsupported line':'PROOF.md gives exact selector-row amplitudes and coherent posterior (1), exact outer source (2), a proved scalar weighted-JS inequality (3), input-indicator entropy payment (4), and the all-depth original3B bound (5). Nonnegative D reserves telescope through arbitrary adaptive selector/data histories, with full inherited signed core terms and both actual terminals retained. A three-bit Boolean witness proves price1 fails AFTER an actual positive outer debit; the same explicit family forces any all-depth price>=2. Price2 passed the finite domain but is NOT proved. The first universal unsupported step is funding a SECOND surviving branch after old debit from the same original physical owner; fresh descendant-ticket sums remain ruled out by v7 complete quadratics.',
'executed validation with domain, arithmetic, commands and outputs':'FROZEN_SPEC.json was written before execution and the arithmetic specification updated before search began. code/exact_chain.js computational body ran in functions.exec V8: ALL16^2 ordered two-data-bit branch pairs, k1..12,3072 cases with no symmetry reduction.9216 certified comparisons:3072 nonnegative-D checks,3072 original3B checks,3072 exploratory2B checks; no failure for3B or2B. Price1 fails on2400 cases. Runtime0.475s. The exact counterexample has D=(1024 log2(2)-288 log2(3))/256, B=512/256. Prime-log intervals use64 rational atanh terms at scale2^160, with proved tail and rounding bounds in LOG_CERTIFICATE.md; undecided signs could return INCOMPLETE and none did. No floating sign, dimension escalation or job above300MB. Independent source code runs as python -X utf8 code/finalize.py: full actual truth tables for ALL branch pairs,k1..3 (768 cases), direct character sums, exact Fraction entropy maps and integer-product signs; source influence computed from the ACTUAL outer branch product. out/INDEPENDENT_VALIDATION.json records3072 assertions and the actual old-debit ledger. This is another implementation by A058, not independent-agent review. Memory estimates under100MB main and30MB independent are estimates, not measurements.',
'proof dependencies and changed downstream conclusions':'This is an extension of the existing umbrella claim, respecting the stream review cap. It converts the v7 nested-source obstruction into a repaired ONE-original-account theorem at unbounded depth for arbitrary overlapping cores along the rare-switch mechanism. Price1 is explicitly refuted and must not be inferred from v7. Price3 has a checked analytic derivation; necessary price>=2 is an actual Boolean asymptotic. Both complete inherited branch FEI bounds remain hypotheses: if both have C, the composite has max(C+6,9), independent of k. This is not payment of arbitrary inherited core entropy, and source3 cannot be renewed inside another independent hierarchy.',
'one next mathematical action and independent reviewer':'A091 primary, A090 alternate; review PENDING. Next expose an actual SECOND surviving activation branch after nonzero debit, keeping the SAME unused original owner and both complete terminal bills; price only new coherent row cost or produce its exact failure. Optimizing3 to2 is secondary because it does not remove the universal ownership bottleneck.',
'actual persistence receipts or precise save blocker':'All research writes are inside this immutable A058 run and rolling files. REPORT, CLAIMS, PROGRESS, PACKET_DELTA, proof, exact code/specs/output, source hashes and a byte manifest are saved locally. CLAIMS statement SHA256 and exact protocol fields are checked against the actual protocol; PACKET_DELTA equals PROGRESS with packet_ids=[A058]. STATUS has exactly two lines; dated WORKLOG/LEARNED entries are appended. Supervisor remote copy and independent adoption are unverified; no git or brain write was performed. Task checklist T-20261023-267 is the current ask. Brain self-care is degraded: model-of-owner/state notes stale; these are not proof premises. No other agents or running work were stopped.'}
report='# A058 stage8: one original source through an arbitrary rare-switch depth\n\n'+''.join('## '+title+'\n\n'+sections[title]+'\n\n' for title in protocol['required_per_run']['report_fields'])
report+='Did: saved all-depth original-source proof, exact positive-old-debit failure and finite certificates. Stopped: own finite checks ended normally; no running work killed. Left running: no owned research jobs.\n\n## Universal bridge\n\nC019 stopping-tree payment advances from a one-mux supplied reserve to an arbitrary-length rare-switch chain with genuinely arbitrary overlapping Boolean cores: three times the SAME original outer ticket pays all stopped coherent costs, with old debits, both complete inherited core bills and true terminal entropies retained. A price-one continuation is exactly false and any all-depth multiplier must be at least two. The remaining universal gap is a second surviving branch or a general branching decomposition with shared physical energy owned once; arbitrary inherited-core FEI remains unpaid. NEXT targets that second surviving branch with the original diminished account because it tests the missing ownership mechanism directly, rather than collecting another fixed-depth case or tuning the constant.\n'
(R/'REPORT.md').write_text(report,encoding='utf-8')
status='STATE: A058 stage8 saved: arbitrary shared cores/ALL rare-switch depths paid SAME original3B; price1 false after old debit, necessary price>=2;9216+3072 exact checks PASS; review pending, FEI OPEN.\nNEXT: A091/A090 review v8; expose SECOND surviving branch after nonzero debit using SAME diminished original source, both full cores/terminals retained; no renewed ticket or constant-only detour.\n'
(Aroot/'STATUS.md').write_text(status,encoding='utf-8')
for name,entry in [('WORKLOG.md','v8 proves D_k<=3B_k for arbitrary shared Boolean A,B and all point-selector depths; full stopping ledger from ONE original account. Price1 fails k2 after actual positive outer debit; necessary multiplier>=2 asymptotically.3072 frozen pairs/depth cases9216 exact comparisons PASS; independent768 full truth tables3072 assertions PASS. Price2 finite evidence only; next second surviving branch with old debit.'),('LEARNED.md','Rare-switch original source: alpha=2^-k,delta=Pr(A!=B),E=I(AB), B=2alpha E+4alpha(k+1)delta is EXACT outermost v7 ticket. Full overhead D=H(F)-alpha HA-(1-alpha)HB satisfies0<=D<=3B for arbitrary shared cores/all k. Proof: coherent row entropy plus weighted-JS Taylor bound and indicator entropy tensorization. ONE original account telescopes all adaptive stops; no renewal after debit. A1,Bx gives D_2=4-(9/8)log2(3)>B_2=2 after positive first debit; D_k/B_k->2. Price2 not proved. Branch FEI transfer max(C+6,9), independent of depth. The second surviving branch and arbitrary inherited core source remain unpaid.')]:
    p=Aroot/name;old=p.read_text(encoding='utf-8') if p.exists() else ''
    if R.name not in old:
        with p.open('a',encoding='utf-8') as f:f.write('\n2026-10-23 | '+R.name+' | '+entry+'\n')
paths=[protocolpath,Path(r'BOARD.md'),Path(r'claude\B12\STREAM_NOTES.md'),P/'PROOF.md',P/'CLAIMS.json',P/'PROGRESS.json']
dump('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'bytes at finalize; mutable board may change'} for p in paths])
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
assert len((Aroot/'STATUS.md').read_text().splitlines())==2
manifest=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name not in ['MANIFEST.json','FINALIZE.json']:
        data=p.read_bytes();assert len(data)<20_000_000
        manifest.append({'path':str(p.relative_to(R)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
dump('out/MANIFEST.json',manifest)
result={'status':'PASS','manifest_files':len(manifest),'statement_sha256':claim['statement_sha256'],'independent_validation':ind,'protocol_fields':'PASS','remote_copy':'UNVERIFIED','independent_review':'PENDING','full_FEI':'OPEN'}
dump('out/FINALIZE.json',result);print(json.dumps(result))
