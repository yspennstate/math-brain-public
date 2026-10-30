import json,hashlib,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HOME=ROOT.parents[1]
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
CTX=Path(r'~\brain_workers\FEI100_20261011\context')
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 pilot=json.loads((ROOT/'out'/'edge_pilot.json').read_text())
 independent=json.loads((ROOT/'out'/'independent_check.json').read_text())
 assert independent['status']=='PASS' and independent['cases']==32906
 source_files=[BASE/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
 source_files += [SUP/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
 source_files += sorted((SUP/'sources').glob('*'))
 source_files += sorted(CTX.glob('*.txt'))
 source_files += sorted((BASE/'runs').rglob('REPORT.md'))
 source_files += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md')]
 receipts=[]
 for p in source_files:
  if p.is_file():
   content=p.read_text(encoding='utf-8',errors='replace')
   receipts.append({'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size,'lines':len(content.splitlines()),'access':'full text loaded; mathematical dependence confined to locators in REPORT.md'})
 save(ROOT/'out'/'source_receipts.json',{'at':NOW,'sources':receipts,'missing_lead_notes':str(Path(r'~\brain_workers\FEI100_20261011\claude\B06\STREAM_NOTES.md'))})
 definitions=[
  ('A026-AFFINE4-GOOD-COORDINATE',
   'Every nonconstant uniform-cube Boolean sign function with nonzero Fourier support of affine F2 dimension at most four, and every disjoint product of such factors, has a relevant physical coordinate i with B_i <= (7/2) I_i. This class is closed under physical restrictions and satisfies H <= (7/2+2/ln 2) I.',
   ['Uniform finite cube; Boolean sign outputs; bit entropy; factors use disjoint physical variable sets; each factor support has affine F2 dimension <=4.'],
   'GOOD_COORDINATE_TARGET.tex; code/edge_pilot.py; code/independent_check.py; out/edge_pilot.json; out/independent_check.json',
   ['Recovered exact physical decrement and influence identities: ERASURE_REDUCTION.md sections 1-4; reconstructed in GOOD_COORDINATE_TARGET.tex.'],[],['A003','A087','A094','A027','A061','A096']),
  ('A026-AMPLITUDE-K4-THRESHOLD-NOGO',
   'For f=+1 exactly at Hamming weights >=24 on 32 uniform sign bits, every coordinate has edge amplitude proxy A_i=2 sum_T |fhat(T) fhat(T+i)| with A_i/I_i=2220940451/536870912>4. Thus existential proxy selection with K=4 is false. No true-erasure violation or unbounded-ratio family is claimed.',
   ['Uniform 32-bit cube; coordinate signs identified with 0/1 bits; threshold is Hamming weight >=24; proxy A_i is not child Hellinger affinity.'],
   'code/symmetric_pilot.py; code/independent_check.py; out/symmetric_pilot.json; out/independent_check.json',
   [],['Existential edge-amplitude proxy A_i<=4 I_i for every Boolean function.'],['A003','A087','A094','A046','A075','A096'])
 ]
 claims=[]
 for cid,statement,hyp,proof,deps,refutes,consumers in definitions:
  hashed=json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode('utf-8')
  claims.append({'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(hashed).hexdigest(),'contributors':['A026'],'proof_source':proof,'proof_dependencies':deps,'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':refutes,'first_unproved_line':None,'next_consumers':consumers})
 save(ROOT/'CLAIMS.json',claims)
 progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B06','packet_id':'A026','gap_id':'G-R-SELECT','attempt_id':'A026-stage1-amplitude-affine4','method':'Exact finite edge-amplitude coordinate certificate; affine-support zero-cost physical reductions; hereditary disjoint tensor closure; symmetric threshold stress.',
 'mathematical_delta':'Certified K=7/2 good-coordinate erasure for affine Fourier dimension <=4 and disjoint products. All 32906 sign-normalized tables through n=4 checked independently. Exact symmetric threshold witness refutes proxy K=4. Universal selection remains open.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'RESTRICTED_CLASS_PROVED_LOCALLY; UNIVERSAL_G-R-SELECT_OPEN; INDEPENDENT_REVIEW_PENDING',
 'claim_versions_used':['Recovered ERASURE_REDUCTION.md sections 1-4; source hashes in out/source_receipts.json','Recovered ISOSPECTRAL_SPLICING_CURATED.md sections 2-3; used for exact rebate and zero-cost scope'],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':1} for c in claims],
 'source_artifacts':['REPORT.md','GOOD_COORDINATE_TARGET.tex','SELECTION_SCOPE.md','FROZEN_SPEC.json','REPRODUCTION_SPEC.json','SYMMETRIC_SPEC.json','out/source_receipts.json','code/edge_pilot.py','code/independent_check.py','code/symmetric_pilot.py','out/edge_pilot.json','out/independent_check.json','out/gray_selections.bin','out/symmetric_pilot.json'],
 'next_consumers':['A003','A087','A094','A027','A061','A096'],
 'next_action':'Analyze the symmetric threshold amplitude proxy asymptotically at t=n/2+c sqrt(n), from exact binomial Walsh sums, to decide whether it is an overly strong universal selector; A087/A094 review the affine4 selection certificate.',
 'stagnant_substantive_attempts':0,'blockers':['B06 STREAM_NOTES.md absent at stage start; not a mathematical block','External independent review and supervisor mirror not performed by A026'],'packet_ids':['A026']}
 save(ROOT/'PROGRESS.json',progress);save(ROOT/'PACKET_DELTA.json',progress)
 report={
 'exact target, quantifiers, hypotheses and units':
 'Universal target: one finite K such that every nonconstant Boolean sign function on every finite uniform cube has some relevant physical i with B_i=H(S_i|S_-i)<=K I_i. H is in bits and I_i=Pr[f(x)!=f(x^i)]. The universal target stays OPEN. Locally closed target: affine Fourier support dimension <=4, and arbitrary disjoint products of these factors, with K=7/2 and H<=(7/2+2/ln2)I. This is an existential coordinate theorem with a hereditary structural hypothesis; no all-coordinate theorem is asserted. Amplitude A_i here means 2 sum|parent adjacent coefficients|, not the Hellinger affinity denoted A_i in the recovered source.',
 'sources actually read, revisions and theorem locators':
 'Protocol 2026-10-11-execution-v2 was read in full. Campaign state, registries, packet index, stream next actions, plan A026 contract and restriction identities were loaded/read. Supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and sources were loaded; mathematical inputs: ERASURE_REDUCTION sections 1-4 and 6; ISOSPECTRAL_SPLICING_CURATED sections 2-3; ROUTE_MAP sections 2.1,2.2 and recovered mechanism floors; ERASURE_RIGIDITY sections 1-2. Earlier B05 and B19 reports supply accepted all-coordinate no-go scope, not a premise of the new restricted lemma; B09 remains unreviewed and unused. Four paper text versions were loaded and located; threshold 38-page introduction/Theorems A-B and section 7, identities (67)-(70), Corollaries 7.2-7.4 were inspected for existing class/composition scope; percolation 30-page introduction/Theorems 1.1-1.2 were inspected and are not proof dependencies. Earlier paper versions were scanned for restriction/composition locators, not substituted for current results. Hash/byte receipts for all loaded source files are in out/source_receipts.json. BOARD snapshot at 21:38 UTC was read at stage start. B06 STREAM_NOTES.md was absent. No priority claim is made.',
 'complete derivation or exact first unsupported line':
 'Full restricted derivation is GOOD_COORDINATE_TARGET.tex. Binary entropy <=2 sqrt(p(1-p)) yields B_i<=A_i. Two exact exhaustive implementations prove selectable A_i/I_i<=7/2 through four variables. If support lies in c+V and relevant e_i is outside V, adjacent Fourier supports are disjoint, B_i=JS=Delta_iH=0. Otherwise all relevant unit vectors lie in V, so at most dim(V)<=4 variables are relevant. Projection under physical restriction preserves the affine-dimension hypothesis. Disjoint independent spectra preserve individual B_i and I_i. Exact decrement and influence identities then telescope/induct with 7/2+2/ln2. The mismatch minority law and KL rebate are retained explicitly; they vanish at zero-cost splits. First unsupported universal line: when Fourier affine dimension is unbounded and no zero-erasure coordinate is available, there exists i with true B_i/I_i bounded by a universal constant. Neither finite enumeration nor affine-dimension reduction proves that line. Recovered bounds already exclude universal K=4 for true erasure. Our different proxy K=4 is also false: symmetric n=32,t=24 gives exact ratio 2220940451/536870912 at every coordinate. No implication about actual erasure on this witness, proxy divergence, or FEI failure is asserted.',
 'executed validation with domain, arithmetic, commands and outputs':
 f'Frozen specs precede their searches. Commands, from the A026 folder: python -X utf8 runs/{ROOT.name}/code/edge_pilot.py; python -X utf8 runs/{ROOT.name}/code/symmetric_pilot.py; python -X utf8 runs/{ROOT.name}/code/independent_check.py. Butterfly Walsh pilot: {pilot["assertions"]} integer Parseval checks, elapsed {pilot["elapsed_seconds"]:.6f}s. Gray-update independent reproduction: PASS on {independent["cases"]} cases, elapsed {independent["elapsed_seconds"]:.6f}s. Domains n=1,2,3,4, counts 2,8,128,32768 modulo global output sign; max minimum proxy ratios exactly 0,2,3,7/2. Independently verifies all integer selection inequalities 4 sum|products|<=7 sum squares with positive denominator. All nonconstant cases total 32902. Symmetric pilot: 19 thresholds at the frozen n=8,16,32,64 and offsets; integer binomial Walsh sums, exact Fraction ratios; polynomial-coefficient construction independently verifies n=32,t=24. No floating entropy assertions. Display decimals are not used as proof. Estimated memory 20 MB, no >300 MB job; no GPU and no automatic dimension increase. Initial frozen count 33034 was a bookkeeping addition error; the original file is preserved and corrected to actual 32906 in REPRODUCTION_SPEC without altering domain. Exact proxy maximum sharpness witness is the point defect; true-erasure sharpness is not claimed.',
 'proof dependencies and changed downstream conclusions':
 'Only recovered exact entropy decrement, JS upper bound, influence conservation, tensor independence, and elementary affine-support projection are used; decrement/mismatch identities are also reconstructed in the proof. No unreviewed campaign candidate is used. Downstream A003 can add a proper hereditary class to its implication map; A027/A061 can use the zero-cost rank reduction and finite terminal certificate. A046/A075 should distinguish the stronger amplitude-proxy failure from true erasure. Full FEI and G-R-SELECT remain OPEN. No shared indices changed. There are two locally complete unreviewed claims; subsequent stage should prioritize review/repair or narrowly diagnose the current proxy before opening broad candidates.',
 'one next mathematical action and independent reviewer':
 'Analyze symmetric thresholds t=n/2+c sqrt(n) using exact binomial Walsh formula and controlled asymptotics to test whether the amplitude proxy can have an unbounded minimum ratio; do not increase dimension automatically. Independent packet reviewers A087 and A094 should reconstruct the affine4 proof and replay the Gray-code certificate. They have not reviewed this run yet.',
 'actual persistence receipts or precise save blocker':
 f'Local run persisted at {ROOT}; rolling files STATUS.md, WORKLOG.md, LEARNED.md saved in A026 only. All JSON field sets validated against protocol by save_stage.py. Packet delta is byte-for-byte equal to PROGRESS.json. Persistence manifest out/persistence_receipts.json gives paths, sizes, SHA256 and generation commands. Independent selection binary SHA256={independent["selection_bytes_sha256"]}. No source trees, shared indices, brain databases, other agent folders, git, or external applications were modified. Supervisor copy/mirror and independent review have not occurred and are not inferred from local save.'}
 (ROOT/'REPORT.md').write_text('# A026 stage 1 — good-coordinate erasure\n\n'+'\n\n'.join('## '+k+'\n\n'+v for k,v in report.items())+'\n',encoding='utf-8')
 (HOME/'STATUS.md').write_text('STATE: A026 stage 1 saved; affine Fourier dimension <=4 and disjoint products have checked K=7/2 selection; two claims await review; full FEI OPEN.\nNEXT: A087/A094 review certificate; analyze symmetric-threshold amplitude proxy before extending universal selection.\n',encoding='utf-8')
 with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:
  f.write(f'\n{NOW}: Stage {ROOT.name}. Read campaign protocol/state/board; B06 lead notes missing. Frozen integer Walsh pilot and independent Gray replay checked 32906 sign-normalized functions through n=4, selectable amplitude K=7/2. Proved hereditary affine-support-dimension <=4 extension and disjoint product closure using zero-cost physical queries. Symmetric threshold n=32,t=24 exactly refutes proxy K=4. Universal erasure selection remains open. Saved two locally complete claims, review pending. No external writes.\n')
 (HOME/'LEARNED.md').write_text('''# Durable facts from A026 stage 1

- For adjacent parent Fourier coefficients, B_i <= A_i := 2 sum_T |a_T a_(T+i)| by h2(p)<=2 sqrt(p(1-p)). This A_i differs from child Hellinger affinity.
- Exact complete enumeration through n=4, modulo global output sign, yields max_f min_relevant_i A_i/I_i equal to 0,2,3,7/2 at n=1,2,3,4. Two independent integer implementations agree; point defect attains the last three proxy maxima. This does not identify sharp true B_i constants.
- If nonzero Fourier support lies in affine c+V and e_i is outside V, adjacent support pairs do not coexist, so B_i=JS=Delta_iH=0. If all relevant e_i belong to V, their number is <=dim(V). Physical restriction projects support and never increases its affine dimension.
- Therefore affine Fourier dimension <=4, and arbitrary disjoint products of such factors, have a relevant B_i <=(7/2)I_i at every nonconstant restriction and H <=(7/2+2/ln2)I. Locally proved and checked; external independent review pending. Existing bounded-gate/parity FEI results mean no priority claim should be inferred.
- Symmetric threshold f=+1 at weights>=24 on n=32 has A_i/I_i=2220940451/536870912>4 for every i. The n=64,t=40 exact proxy ratio is 10293444163950323579/2305843009213693952. These are proxy failures only, not actual erasure failures or FEI disproofs.
- Universal existence of finite K for some B_i/I_i remains FEI-equivalent and open. All-coordinate rare-split obstructions do not refute it. Root-only zero erasure does not certify a terminal class: heredity must be proved and all descendants accounted for.
- Preserve mismatch credit M[log(1/M)-D2(nu||q)+1/ln2]. Zero isospectral steps have M=0 and exact zero entropy decrement. Do not replace them by marginal entropy.
''',encoding='utf-8')
 protocol=json.loads((BASE/'EXECUTION_PROTOCOL.json').read_text())
 # The protocol's final list entry is a field name followed by explanatory text.
 # User explicitly requires the actual JSON key packet_ids, not that annotation.
 expected_progress={k.split(' (',1)[0] for k in protocol['required_per_run']['progress_fields']}
 assert set(progress)==expected_progress
 assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
 assert set(report)==set(protocol['required_per_run']['report_fields'])
 assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
 manifest=[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='persistence_receipts.json']
 assert all(r['bytes']<20*1024*1024 for r in manifest)
 save(ROOT/'out'/'persistence_receipts.json',{'at':NOW,'files':manifest,'schema_check':'PASS exact report/claim field sets; progress packet_ids annotation normalized as expressly required by user','regenerate':'python -X utf8 code/edge_pilot.py; python -X utf8 code/symmetric_pilot.py; python -X utf8 code/independent_check.py; python -X utf8 code/save_stage.py (from run directory; separate commands)','scope':'Local save only; no supervisor mirror receipt'})
 print(json.dumps({'schema_check':'PASS','files':len(manifest),'claims':len(claims),'run':str(ROOT),'source_receipts':len(receipts)},indent=2))
if __name__=='__main__':main()
