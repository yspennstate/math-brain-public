import json,hashlib,time,datetime,shutil
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]; A=R.parents[1]; ROOT=A.parents[1]
(R/'out').mkdir(parents=True,exist_ok=True)
def read(p): return p.read_text(encoding='utf-8')
def save(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
protocol_path=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(read(protocol_path))
oldrun=A/'runs/20261023T121547Z-account03-A003-minimal-target-formulation'
claim=json.loads(read(oldrun/'CLAIMS.json'))[0]
# Frozen before any enumeration; independent direct sums, no FWHT imports.
spec={'helper':'code/close.py v1','family':'every Boolean core n=0,1,2, disjoint parity lifts L=2,3','domain':'44 lifts; all 348 complete unwrapping terminals; fixed block order','symmetry':'none','arithmetic':'direct integer character sums, Fraction spectra, physical edge influences; no logarithmic approximations','memory_estimate_mb':50,'max_runtime_seconds':55,'pilot':'entire bounded domain, below60s; no enlargement'}
save(R/'out/FROZEN_SPEC.json',spec)
start=time.monotonic(); checks=0; lifts=0; terminals=0
def ck(b):
 global checks
 checks+=1; assert b
 if time.monotonic()-start>55: raise RuntimeError('frozen55s exceeded')
def law(t):
 return sorted(F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t))**2,len(t)**2) for s in range(len(t)) if sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)))
def influences(t):
 return [F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(len(t).bit_length()-1)]
for n in range(3):
 for mask in range(1<<(1<<n)):
  g=[1-2*((mask>>x)&1) for x in range(1<<n)]; p=law(g); al=influences(g)
  for L in (2,3):
   lifts+=1
   t=[g[sum((((x>>(j*L))&((1<<L)-1)).bit_count()%2)<<j for j in range(n))] for x in range(1<<(n*L))]
   ck(law(t)==p); ck(influences(t)==[al[j] for j in range(n) for _ in range(L)])
   for z in range(1<<(n*(L-1))):
    theta=[((z>>(j*(L-1)))&((1<<(L-1))-1)).bit_count()%2 for j in range(n)]
    leaf=[g[y^sum(theta[j]<<j for j in range(n))] for y in range(1<<n)]
    ck(law(leaf)==p); ck(influences(leaf)==al)
    # Exact cancellation of the common symbolic H term, K=1,4,25.
    for K in (1,4,25): ck(K*L*sum(al)-K*(L-1)*sum(al)==K*sum(influences(leaf)))
    terminals+=1
save(R/'out/DIRECT_AUDIT.json',{'status':'PASS','assertions':checks,'lifts':lifts,'terminals':terminals,'elapsed_seconds':time.monotonic()-start,'scope':'Independent AUTHOR representation and small-domain corroboration, not an independent-agent review or new all-dimensional theorem.'})
# Consume the source-bound independent review, not the board label alone.
matches=[]
for pth in sorted((ROOT/'agents/A004/runs').glob('*/CLAIMS.json'),reverse=True):
 rows=json.loads(read(pth))
 for row in rows:
  if row['claim_id']==claim['claim_id'] and row['statement_sha256']==claim['statement_sha256']:
   reviews=[v for v in row['review_records'] if 'A004' in str(v) and ('HOLDS' in str(v) or 'HOLD' in str(v))]
   if reviews: matches.append((pth,row,reviews)); break
 if matches: break
assert matches, 'No matching independent A004 review: do not mark accepted'
source,row,reviews=matches[0]
claim['review_records']+=reviews; claim['status']='INDEPENDENTLY_ACCEPTED_BY_A004_AT_STATED_SCOPE'
# Preserve exact statement/version/hash; proof points to immutable original source.
claim['proof_source']=[str(oldrun/p) for p in claim['proof_source']]
save(R/'CLAIMS.json',[claim])
save(R/'out/REVIEW_RECEIPT.json',{'source':str(source),'source_sha256':sha(source),'claim_id':claim['claim_id'],'version':claim['version'],'statement_sha256':claim['statement_sha256'],'review_records':reviews,'scope':'A004 source review consumed without changing theorem; no new theorem claimed'})
for name in ['DERIVATION.md','IMPLICATIONS_BASELINE.md']:
 shutil.copyfile(oldrun/name,R/name)
board=ROOT/'BOARD.md'; lead=ROOT/'claude/B01/STREAM_NOTES.md'
save(R/'out/SOURCES.json',[{'path':str(p),'sha256':sha(p)} for p in [protocol_path,board,lead,A/'STATUS.md',source,oldrun/'CLAIMS.json',oldrun/'DERIVATION.md']])
target='''# Final minimal target comparison

All information is in bits; c=2/ln2. Every assertion below quantifies over all finite uniform Boolean cubes unless a source/terminal class is explicitly specified. No local reset theorem supplies initial O(I) admission.

| Route | Paid implication | First unpaid all-dimensional line |
|---|---|---|
| C018 total erasure | B<=K I => a good coordinate => FEI(K+c); FEI(C)=>B<=C I | Prove an actual Boolean structural bound B<=lambda H+K I with lambda<1, giving FEI((K+c)/(1-lambda)) |
| Good coordinate, weak regime | If max Inf<tau admits B_i<=(lambda H/I+K)Inf_i, FEI constant is max(log2(e/tau)+c,(K+c)/(1-lambda)) | At tau=1/4, require Inf_i>=I/(2d) AND B_i<=4Inf_i on every weak-coordinate function; this fixed structural lemma implies FEI(4+c) |
| Signed Booleanity | L_i=sum_T p(T+i)log2(1+p(T)/p(T+i)); L_i<=B_i<=L_i+Inf_i/ln2; some L_i<=KInf_i =>FEI(K+3/ln2) | Obtain L_i<=4Inf_i from the full signed convolution constraints, not just an arbitrary probability law; implies FEI(4+3/ln2) |
| Whole-set witness | The full posterior-residual bound R*<=K I implies FEI(2+K_ref+K), K_ref=3+2log2(3)+log2(6e) | Pay the FIXED baseline witness residual with its original gate/selector/normalizer and complete reference costs; changing the admissible family changes the target |
| C019/C024 deferral | Exact matched zero-erasure queries cost zero entropy, preserving ORIGINAL K L I-H | Re-expressing capacity at CURRENT core influence is not free: endpoint residual is K I-H, exactly FEI(K) |

These constants and route interfaces are the established baseline, not new theorems this stage. There is no canonical least stronger lemma among inequivalent structural hypotheses. The fixed numerical coordinate/signed/witness targets are reviewable sufficient statements. A mere unspecified influence-priced full-reference supplier is FEI-equivalent, since CE>=H and Q=P realizes equality.

The complete checked previous theorem is DERIVATION.md, now independently accepted by A004 at unchanged scope. Its key distinction is: sum erasure + full terminal CE remains H(core), whereas an additional K-times-queried-influence earmark leaves K I(current)-H(core). Both accounts are valid when declared; they cannot be silently exchanged. Maj3 with L2,K1 retains original entropy surplus1 but has endpoint influence residual-1/2. This is a fixed-rate heredity obstruction, never a FEI disproof.

Next substantive target: supply a noncircular Boolean mechanism for one displayed coordinate/signed/witness inequality or a well-founded decreasing original-source construction. Stop treating optional exact-match resets, paid padding, or relabeling current influence as universal progress. Full FEI remains OPEN.
'''
(R/'MINIMAL_TARGET.md').write_text(target,encoding='utf-8')
v=json.loads(read(R/'out/DIRECT_AUDIT.json'))
report=f'''# A003 final stage: source-bound acceptance and explicit remaining targets

## exact target, quantifiers, hypotheses and units

Consume independent review of A003-MATCHED-DEFERRAL-INFLUENCE-COMPRESSION@1, preserve its exact version/hash, reproduce a bounded domain with a different representation, and save the final fixed-constant route comparison. No new universal theorem is claimed. All spectra include empty mass and references are complete; units bits. Full FEI OPEN.

## sources actually read, revisions and theorem locators

Read BOARD2026-10-23 14:39UTC, B01 STREAM_NOTES v1, own STATUS, complete execution protocol revision2026-10-11-execution-v2, own preceding DERIVATION/CLAIMS/baseline, and matching A004 CLAIMS at {source}. Source hashes bind these files. A004 review is consumed only for the matching A003 exact statement; other board claims are routing context, not independently accepted premises. Earlier campaign/paper intake is inherited; no new external-paper theorem is used. Fresh wake warns owner-model101.1h/state85.7h/dream36.4h stale; personal context is degraded/unverified and not a proof premise.

## complete derivation or exact first unsupported line

The all-dimensional proof is copied unchanged as DERIVATION.md: parity-expanded exact matched spectra remain identical probability multisets; legal block queries have zero erasure/occupancy/calibration costs; influence is sum of remaining block sizes times core-coordinate influences. Original entropy capacity remains K L I-H. Explicitly earmarking K times queried influence instead leaves K J_frontier-H, ending K I-H. Every core has an unconditionally cheaply admitted matched lift using H<=n and I>=2^(1-n); compression to SAME-K core scale is therefore exactly FEI(K). A004 independently accepts this theorem at unchanged scope; review receipt and statement hash are saved. This is acceptance consumed, not a newly renamed result.

MINIMAL_TARGET.md gives the final implication table and each first unpaid line. The weak-coordinate fixed target requires an actual high-average-influence good coordinate, the signed target must use the full convolution equations, and the witness target must pay its fixed whole-set posterior residual with normalizers. An unspecified O(I) reference supplier or quotient endpoint inequality is FEI-equivalent, not an independent structural proof. No unsupported universal supplier is inserted. First unsupported line remains an all-dimensional Boolean structural inequality or a well-founded influence-priced ORIGINAL core-source mechanism.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec was written before enumeration. A different AUTHOR implementation uses direct character sums and physical edge counts, without FWHT/importing prior checker code: every core n0..2, L2,3,44 lifts and all complete unwrapping terminals, no symmetry reduction or automatic enlargement. Exact Fraction spectra/influences verify entropy probability multisets, each physical influence and endpoint tariff cancellation at K1,4,25. PASS {v['assertions']} assertions on {v['terminals']} terminals in {v['elapsed_seconds']:.3f}s, below55s. Entropy equality is exact distribution equality; no floating log sign. This is a bounded reproduction, not independent-agent review; the latter is A004's separately saved source review. Prior stage's1828004 checks are not counted as new.

Command python -X utf8 <run>/code/close.py. Estimated memory50MB; no >300MB job, GPU, detached job, new dimension or compiler. Shared work is left untouched. The governor is reported alive with stale heartbeat; inspect-only policy, no blind restart. No machine-health freshness is inferred from stale state.

## proof dependencies and changed downstream conclusions

Unchanged A003-MATCHED-DEFERRAL-INFLUENCE-COMPRESSION@1 is now independently accepted by A004 at its stated scope; review records preserve the original statement SHA256. No fresh broad candidate or new FEI constant. Prior stage19 acceptance remains unchanged. The final route comparison uses established baseline implications; it does not close any universal leaf or declare FEI false. Acceptance is local source-bound evidence, not supervisor adoption or remote persistence.

## one next mathematical action and independent reviewer

After campaign close, resume only with a concrete Boolean structural payment for one fixed target in MINIMAL_TARGET.md, or a strictly decreasing source-price construction retaining the same old owner and both terminals. A090/A094 can audit this final interface; A004 acceptance already covers the exact previous theorem. This is a saved handoff, not a sent message. No more optional reset cycles or padding admissions are needed to expose the universal gap.

## actual persistence receipts or precise save blocker

Four protocol files, unchanged derivation/baseline, final route table, frozen spec, direct checker output, source-bound review receipt and source/artifact hashes saved only in this A003 run. Rolling STATUS/WORKLOG/LEARNED updated. Schema/readback verifies fields, exact statement hash, delta byte identity and size<20MB. Mirrors and supervisor collection remain unverified. No git/mail/shared-source/brain-store mutation or deletion. Brain self-care remains degraded/unverified, affecting owner-context freshness. The explicit owner deadline2026-10-23 14:49UTC overrides archived protocol dates; no broad search is launched in this final window.

**Universal bridge:** C019/C024 gains independent acceptance of the exact deferral-versus-current-influence separation, plus a direct exact small-domain reproduction; no universal constant improves. C018/C020/signed targets retain their explicit fixed-constant first unpaid inequalities in MINIMAL_TARGET.md. What remains is a noncircular all-dimensional Boolean payment or a well-founded ORIGINAL core-source supplier. NEXT is shortest because the local transaction and nullspace accounting are already closed at scope; another optional conversion or isolated padded class would not price arbitrary cores.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B01','packet_id':'A003','gap_id':'UNIVERSAL-CORE-SOURCE-PRICE','attempt_id':'A003-stage21-final-review-consumption','method':'Consume matching independent review; different direct-character/physical-edge reproduction; explicit fixed-constant target handoff','mathematical_delta':'Prior exact deferral-compression theorem independently accepted by A004; universal inequalities remain explicit and open; no new theorem claimed.','deliverable_status':'COMPLETE_LOCAL_VERIFIED','mathematical_status':'SCOPED_THEOREM_INDEPENDENTLY_ACCEPTED; FULL_FEI_OPEN','claim_versions_used':[claim['claim_id']+'@1'],'claims_created_or_changed':[claim['claim_id']+'@1 review status only'],'source_artifacts':['out/SOURCES.json','out/REVIEW_RECEIPT.json','out/DIRECT_AUDIT.json','MINIMAL_TARGET.md'],'next_consumers':['A090','A094','B01 lead','B20'],'next_action':'Prove a fixed Boolean structural inequality or well-founded decreasing ORIGINAL source-price construction; no optional exact-match reset.','stagnant_substantive_attempts':0,'blockers':['Universal core source/structural inequality open','Remote mirrors unverified','Owner-context freshness degraded/unverified'],'packet_ids':['A003']}
save(R/'PROGRESS.json',progress); (R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
(A/'STATUS.md').write_text(f'STATE: A003 stage21 saved: stage20 compression theorem independently accepted by A004 unchanged;{checks} new direct exact checks PASS;final route targets explicit;full FEI OPEN.\nNEXT: Noncircular fixed Boolean erasure/signed/witness payment or well-founded decreasing ORIGINAL core-source construction; no optional reset/padding loop; supervisor collects final run.\n',encoding='utf-8')
for name,line in [('WORKLOG.md',f'\n2026-10-23 final stage21: consumed matching A004 independent acceptance of stage20, preserved statement/version; direct character/physical-edge reproduction {checks} assertions PASS. Saved final constants and first unpaid inequalities. No new universal theorem/constant; full FEI OPEN.\n'),('LEARNED.md','\nFinal campaign interface: stage20 exact deferral/current-influence separation independently accepted by A004 unchanged. Free entropy deferral is not current-influence compression. Final remaining targets must use Boolean structure or a well-founded original-source supplier; optional exact-match conversion, inflation by padding, and an unspecified O(I) supplier do not close FEI.\n')]:
 p=A/name; p.write_text(read(p)+line,encoding='utf-8')
req=protocol['required_per_run']; assert set(claim)==set(req['claim_fields']); assert set(progress)=={s.split(' (')[0] for s in req['progress_fields']}
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all(h in report for h in req['report_fields']); assert len(read(A/'STATUS.md').splitlines())==2
receipts=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='RECEIPTS.json':
  assert p.stat().st_size<20_000_000; receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(R/'out/RECEIPTS.json',{'status':'PASS','files':receipts,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'remote':'UNVERIFIED'})
for x in json.loads(read(R/'out/RECEIPTS.json'))['files']: assert sha(R/x['path'])==x['sha256']
print(json.dumps({'status':'PASS','assertions':checks,'lifts':lifts,'terminals':terminals,'review_source':str(source),'claim_status':claim['status'],'full_FEI':'OPEN','files':len(receipts)}))
print(read(A/'STATUS.md'))
