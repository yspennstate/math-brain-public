"""Persist this stage and its interrupted predecessor; writes only inside A043."""
from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]; OUT=ROOT/'out'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
P=json.loads(protocol.read_text(encoding='utf-8-sig'))
fields=P['required_per_run']; CF=fields['claim_fields']; PF=[s.split(' (')[0] for s in fields['progress_fields']]
HEAD=fields['report_fields']; stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
old=AGENT/'runs'/'20261022T210449Z-account03-A043-prime-gate-decomposition'
stage5=AGENT/'runs'/'20261014T052009Z-account05-A043-prime-gate-decomposition'
base=AGENT.parents[1]
sources=[protocol,base/'BOARD.md',base/'claude'/'B09'/'STREAM_NOTES.md',AGENT/'STATUS.md',old/'PROOF.md',old/'CLAIMS.json',stage5/'PROOF.md',ROOT/'PROOF.md',ROOT/'code'/'check_payment.py']
save(OUT/'source_receipts.json',{'captured_utc':stamp,'sources':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources],
 'reading_scope':'Current stage read updated BOARD/B09/STATUS, protocol, stage17 proof and helper, relevant stage5 ledger; campaign baseline and papers carried from previously documented source-complete stage17. No new external literature claim.'})
checks=json.loads((OUT/'checks.json').read_text(encoding='utf-8'))
assert checks['status']=='PASS' and checks['case_count']==52 and checks['assertions']==3935
statement=('For the actual Boolean sign f=-1+2z+2xy-2z[ax+(1-a)y] at interior product probabilities (alpha,e,d,q), let Delta=I-Var, T be the total triple Fourier mass, E the natural corrected nonempty entropy, S=4Delta-2T-E_single, and G=E_ge2-ln(4)Delta. For 0<d<=e<1, G/T<=2sqrt(q)+2sqrt(alpha)+2d/[e(1-e)]+2sqrt(e)/(1-e). Thus whenever 0<alpha,q,e<=1/16 and 0<d<=e/16, G<=5T/3 and (4+ln4)Delta-E>=S+T/3>=T/3. The swapped collar alpha->1-alpha, e<->d also satisfies this. Every nonnegative polynomial reserve S_m from the retained-slack hierarchy satisfies S_m+2T-G>=T/3 on those collars. In particular the old all-fixed-order obstruction path (t,t^2,t^4,t), 0<t<=1/16, is paid directly. This is a collar theorem only; at fair biases G/T=4ln2>2, so reserve-free G<=2T is not universal.')
cid='A043-PRIME56067-ACTUAL-CHARGE-COLLAR'
claim=dict(zip(CF,[cid,1,statement,
 ['Actual Boolean sign and full biased orthonormal spectrum; independent interior probabilities; natural entropy units','d<=e only for the displayed asymmetric K bound; explicit collar or its exact swapped symmetry for the 5/3 bound','Original joint packet ownership and original Delta; no truncated conditional reference'],
 hashlib.sha256(statement.encode('utf-8')).hexdigest(),['A043'],['PROOF.md','code/check_payment.py','out/frozen_spec.json','out/checks.json'],
 [{'source':str(stage5/'PROOF.md'),'sha256':sha(stage5/'PROOF.md'),'scope':'original 56067 polynomial and exact G ledger, reconstructed explicitly in current proof'},
  {'source':str(old/'PROOF.md'),'sha256':sha(old/'PROOF.md'),'scope':'reserve S>=S_m>=0 and all-fixed-m corner obstruction; S>=0 reconstructed in current proof'}],
 [],'PROVED_AUTHOR_PENDING_INDEPENDENT_REVIEW',[],[],
 'No gap in the stated collar derivation; first unsupported extension is G<=S+2T for every remaining interior four-bias law, and then a uniform bound on all prime gates.',
 ['A042','A044','A091','B09 lead']]))
assert set(claim)==set(CF)
save(ROOT/'CLAIMS.json',[claim])
progress={
 'protocol_revision':P['revision'],'run_id':ROOT.name,'stream':'B09','packet_id':'A043',
 'gap_id':'B09-PRIME56067-ACTUAL-G-PAYMENT','attempt_id':'actual-charge-collar-v1',
 'method':'Repair the failed fixed-truncation sufficient condition by bounding the actual merged G; analytic continuum bound plus exact physical vertex reconstruction and outward rational logarithms.',
 'mathematical_delta':'Full four-dimensional interior collar alpha,q,e<=1/16,d<=e/16 and swapped collar: actual G<=5T/3, hence sharp residual>=S+T/3; pays entire previously obstructing path for 0<t<=1/16 without spending any truncation tail.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'COLLAR_AUTHOR_PROOF_REVIEW_PENDING; ALL_BIAS_SHARP_PAYMENT_AND_FULL_FEI_OPEN',
 'claim_versions_used':['A043-RETAINED-SLACK-POLYNOMIAL-HIERARCHY@1','Stage5 prime56067 exact G ledger; source hashes in source_receipts.json'],
 'claims_created_or_changed':[cid+'@1'],'source_artifacts':['PROOF.md','REPORT.md','CLAIMS.json','code/check_payment.py','code/finalize.py','out/frozen_spec.json','out/checks.json','out/source_receipts.json'],
 'next_consumers':['A042','A044','A091','B09 lead'],
 'next_action':'Review the direct collar payment, then pay actual G using S at the complementary q->1 joint endpoint; preserve the same merged ledger and original Delta. Do not resume fixed-order S_m>=4T.',
 'stagnant_substantive_attempts':0,
 'blockers':['Independent review pending; no Lean formalization claimed','Sharp all-interior 56067 payment and uniform all-prime endpoint remain open','Personal-context brain self-care degraded: model 89h and state-of-mind 73.6h stale; current campaign sources used instead'],
 'packet_ids':['A043']}
assert set(progress)==set(PF)
save(ROOT/'PROGRESS.json',progress);(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
texts=[
 'Prove the actual-charge collar in PROOF.md for all stated real interior product biases. Natural corrected entropy units; actual prime56067; positive triple mass T. This is a repair of the existing sharp-payment route under the stream review cap, not a new broad FEI candidate.',
 'Execution protocol revision '+P['revision']+' read in full this session; updated BOARD, B09 STREAM_NOTES v2, and A043 STATUS read at the start. Stage17 PROOF.md: reserve identity and fixed-m obstruction. Stage5 PROOF.md: Exact pair-normalization ledger. Current proof reconstructs that ledger. Byte hashes and reading scope in out/source_receipts.json; baseline campaign files/papers were read in the prior source-complete stage, not freshly claimed as reread here.',
 'Complete analytic derivation is in PROOF.md: logarithm derivative inequality gives A(t)<=sqrt(t) and h(t)<=2t^(3/2)(1-t); division of the ORIGINAL G ledger by T gives K; collar arithmetic gives K<=5/3. Boolean derivative reserve S>=0 yields residual>=T/3. First unsupported line: G<=S+2T on all remaining four-bias laws; the uniform all-prime bridge is further open. No finite sample supplies that extension.',
 'Command: python -X utf8 '+str(ROOT/'code'/'check_payment.py')+'. Frozen specification saved before calculation, 52 laws, no dimension increase or symmetry omission, Fraction vertex sums and outward 20-term atanh intervals, 40 MB estimate, 55-second cap. PASS: 3935 exact assertions; observed runtime '+str(checks['runtime_seconds'])+' seconds. All 10 proper blocks have >2 cofactor rows, verifying genuine primality. Both collars and the thin path pass. Fair-law negative control certifies G>2T, while the actual sharp residual remains positive. Spectrum/ledger interval overlap is consistency evidence; the exact symbolic identity is proved analytically. No floating-point sign certificate and no formal Lean result are claimed. No job exceeded 300 MB or needed memory admission.',
 'Dependencies are hash-bound in CLAIMS.json. The nonnegative reserve and original merged spectrum are used, without additional constituent deficit credit. The previous all-fixed-m obstruction is preserved; its region is now paid through G directly. This strengthens the route from an asymptotic positive residual to an explicit multidimensional continuum collar. Universal approximation remains valid; universal sharp payment is not inferred. Independent review is pending, not accepted by status alone.',
 progress['next_action']+' Requested independent reviewers/consumers: A042 or A091; no review performed or message sent by this stage. A044 can inspect original-owner preservation. No other agent folder was modified.',
 'All four protocol files, PROOF.md, both helper sources and exact output saved inside this run. out/schema_validation.json validates field sets and packet-copy identity; out/persistence_receipts.json lists SHA256 and byte counts for all other stage files. The interrupted 02:35 stage has a separate honest handoff package. Rolling STATUS has exactly two lines; WORKLOG and LEARNED are appended. No git, brain write, messaging, detached process or external mutation. No mirror/publication receipt is claimed.'
]
report='# A043 actual-charge corner payment\n\n'+'\n\n'.join('## '+h+'\n\n'+t for h,t in zip(HEAD,texts))
report+='\n\n**Universal bridge**: B09 lead\'s all-product-bias prime-gate endpoint advances by an explicit four-dimensional collar with G<=5T/3 and at least T/3 sharp residual, including the full thin path 0<t<=1/16 that defeats every fixed-order S_m>=4T shortcut. This pays actual whole-set charge from its original triple owners and leaves S intact. Sharp payment elsewhere and a dimension-independent bound on all primes remain unproved. The shortest next step is the complementary q->1 endpoint in this SAME G/S ledger, followed by review and reuse of the packet estimate; another finite grid or stronger fixed-order surrogate would not remove the known universal obstruction.\n'
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
# Earlier requested stage was interrupted by the owner's next stage before a run was saved.
PREV=AGENT/'runs'/'20261023T023500Z-account03-A043-prime-gate-decomposition'
PREV.mkdir(exist_ok=True);(PREV/'code').mkdir(exist_ok=True);(PREV/'out').mkdir(exist_ok=True)
prior=dict(progress);prior.update(run_id=PREV.name,attempt_id='handoff-to-024327',method='Read and resume prior stage; interrupted by next owner stage instruction before mathematical artifact creation.',mathematical_delta='No separate mathematical result; analytic continuation and all certificates saved in '+ROOT.name,mathematical_status='HANDED_OFF; FULL_FEI_OPEN',claims_created_or_changed=[],source_artifacts=['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json'],next_action='Consume the completed 02:43 continuation package at '+str(ROOT))
save(PREV/'PROGRESS.json',prior);(PREV/'PACKET_DELTA.json').write_bytes((PREV/'PROGRESS.json').read_bytes());save(PREV/'CLAIMS.json',[])
pt=['Resume the actual G payment on prime56067.','BOARD, B09 notes, STATUS and protocol read; sources inherited by the 02:43 continuation.','No separate closed claim; work continued in '+ROOT.name+'.','No search executed in this interrupted run. All executed certificates are in the continuation.','No new dependency or downstream theorem in this run.','Read the completed continuation; A042/A091 independent review pending.','Four protocol files saved; code/out directories intentionally empty.']
(PREV/'REPORT.md').write_text('# A043 interrupted-stage handoff\n\n'+'\n\n'.join('## '+h+'\n\n'+t for h,t in zip(HEAD,pt))+'\n\n**Universal bridge**: No separate movement is claimed in this interrupted stage. The all-product-bias prime-gate endpoint is continued in '+ROOT.name+'; its explicit actual-charge collar and exact remaining gap are recorded there.\n',encoding='utf-8')
status='STATE: 02:43 stage complete locally: actual prime56067 G<=5T/3 on explicit 4D collar; sharp residual>=T/3;52 laws/3935 exact checks PASS;independent review pending;FEI OPEN.\nNEXT: A042/A091 review collar payment; pay complementary q->1 endpoint with SAME original G/S/Delta ledger; no fixed-order S_m>=4T retry.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
for name,text in [
 ('WORKLOG.md','2026-10-23 02:43 UTC stage: resumed 02:35 work; repaired fixed-truncation route using actual G. Proved K upper envelope and collar G<=5T/3 with residual>=S+T/3; swapped law included. Ran 52 frozen exact fixtures/3935 assertions in '+str(checks['runtime_seconds'])+'s, including direct primality and fair G>2T control. All-bias/universal FEI open; independent review pending; no formal claim. Saved full package and prior interrupted handoff.'),
 ('LEARNED.md','2026-10-23: In actual prime56067, for d<=e, G/T<=2sqrt(q)+2sqrt(alpha)+2d/[e(1-e)]+2sqrt(e)/(1-e). Hence alpha,q,e<=1/16,d<=e/16 gives G<=5T/3 and sharp residual>=S+T/3. Swap e,d and alpha,1-alpha for second collar. Entire t,t^2,t^4,t path with t<=1/16 is paid without any S_m>=4T condition, despite that condition failing at every fixed m. At fair law G/T=4ln2>2, so reserve-free payment cannot be extended globally. Author proof pending independent review; preserve actual packet owners.')]:
 with (AGENT/name).open('ab') as f:f.write(('\n'+text+'\n').encode('utf-8'))
validation={'status':'PASS','claim_fields_exact':set(claim)==set(CF),'progress_fields_exact':set(progress)==set(PF),'packet_delta_byte_identical':(ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes(),'report_fields_present':all('## '+h in report for h in HEAD),'status_two_lines':len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2,'checks_pass':checks['status']=='PASS'}
assert all(v for k,v in validation.items() if k!='status');save(OUT/'schema_validation.json',validation)
manifest=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='persistence_receipts.json':
  assert p.stat().st_size<20_000_000
  manifest.append({'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
save(OUT/'persistence_receipts.json',{'captured_utc':stamp,'files':manifest,'scope':'local persistence only; no mirror or publication claim'})
assert all(sha(ROOT/x['path'])==x['sha256'] for x in manifest)
print(json.dumps({'status':'PASS','saved_run':ROOT.name,'prior_handoff':PREV.name,'manifest_files':len(manifest),'schema_validation':validation}))
