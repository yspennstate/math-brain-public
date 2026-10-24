from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1]; O=R.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def dump(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
cert=json.loads((R/'out/nogo.json').read_text(encoding='utf-8'))
assert cert['status']=='PASS' and len(cert['cases'])==6
assert any(4 in r['certified_positive_local_debt_rates'] for r in cert['cases'])
claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'));c=claims[0]
c['exact_statement']+=' Corollary: for every fixed finite C>=0 and every fixed such mask with beta>0, no seed-independent finite controller reserve bounds all protected-tag stopped signed costs. Explicit Boolean seeds are tensor powers of bent/one-point-flip selector functions f_m with even m>=max(2,C+6); they satisfy H<=3I while their displayed seed-selector-only stopping costs diverge linearly in the tensor order. For the fixed A079 mask the complete outer functions also satisfy H<=3I. This refutes an all-history fixed-controller-reserve shortcut, not FEI or a selected-history theorem with a seed-dependent unused bank.'
c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
c['proof_source']['additional_proof']={'path':str(R/'NO_GO.md'),'sha256':sha(R/'NO_GO.md')}
c['proof_source']['certificates'].append('out/nogo.json')
dump(R/'CLAIMS.json',claims)
p=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))
p['mathematical_delta']+=' Stronger actual-Boolean corollary: for EVERY finite C, bent/point-flip selector tensor seeds give divergent stopped signed cost against any fixed controller-only reserve although all seed and fixed-A079 outer ratios obey H/I<=3. The missing seed reserve cannot be replaced by a constant even on a proved FEI-bounded family.'
p['mathematical_status']='AUTHOR_PROOF_WITH_EXACT_CERTIFICATES; ALL_HISTORY_FIXED_RESERVE_NOGO; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING'
p['source_artifacts']+=['NO_GO.md','FROZEN_NOGO.json','code/nogo.py','out/nogo.json']
p['blockers']=[x for x in p['blockers'] if not x.startswith('Formal status:')]
p['blockers'].append('Formal status: SETUP_UNVERIFIED resource gate; wrapper explicitly started no compiler process')
p['next_action']='Choose a seed-dependent stopping/reference rule, or expose the protected tag ONCE at a selected inherited cut; retain BOTH A_s +/- B_s h_t terminal spectra and fund signed empty-frequency interference from the SAME unused seed/structural bank. Never ask a seed-independent controller reserve to pay every seed history. A032/A079/A088/A094 review the separation and all-C Boolean no-go.'
dump(R/'PROGRESS.json',p);dump(R/'PACKET_DELTA.json',p)
text=(R/'REPORT.md').read_text(encoding='utf-8')
add='''
The continuation NO_GO.md sharpens the obstruction on ACTUAL Boolean functions. For every finite C choose even m>=max(2,C+6), a quadratic bent g on m bits, its one-origin flip h, and selector seed f=(g,h). With delta=2^-m, the midpoint conditional spectrum has chi-square divergence4/(2^m-1) from uniform. Jensen's entropy bound gives Delta_z H(f)-C Inf_z(f)>delta*(m-C-4/ln2)>0, while exact physical energy gives I(f)=m/2+(m+1)delta and H(f)<=3I(f). Tensor t copies and query only their selector bits, then stop with BOTH complete g/h terminals retained. Stopped debt is t times the positive displayed debt, while H/I stays<=3. Every fixed controller with beta>0 multiplies that debt by beta; no finite seed-independent controller reserve can cover it. For the displayed A079 mask even the complete outer functions satisfy H<=3I. This does not refute FEI or a selected-history theorem retaining a genuinely unused seed-dependent bank. The bent/flip local seed is prior work; the all-interleaving fixed-reserve consequence is the application recorded here.

'''
text=text.replace('# executed validation with domain, arithmetic, commands and outputs\n',add+'# executed validation with domain, arithmetic, commands and outputs\n')
extra=f'''FROZEN_NOGO.json precedes code/nogo.py. Six explicit even dimensions2,4,6,8,10,12 and twelve symbolic checks at rates2,4: PASS,{cert['exact_assertions']} exact assertions in{cert['seconds']:.6f}s. Direct integer Walsh/physical-edge checks verify flat bent magnitudes, the origin-flip transform, midpoint second/fourth moments, chi-square4/(N-1), every data/selector influence and H-upper/I<=3. All-dimensional and all-tensor quantifiers follow from NO_GO.md's explicit two-bit tensor proof and finite-depth selector tree, NOT from the six-dimensional check. Memory estimate40MB, runtime limit20s, no automatic dimension increase. ln2>2/3 follows from its positive convergent atanh series; no floating-point sign is used.

'''
text=text.replace('A small core Lean theorem',extra+'A small core Lean theorem')
text=text.replace('Actual wrapper status: Wrapper exit: 2.','Actual wrapper status: SETUP_UNVERIFIED, resource gate (hung window or under5500MB free), no new compiler process. The wrapper exit was2.')
text=text.replace(p.get('next_action','__NO_MATCH__'),'__NO_MATCH__') if False else text
before=text.split('# Universal bridge\n')[0]
bridge='''# Universal bridge

This stage moves B07's full-Booleanity/nonproduct target toward C019/C024 by proving the exact protected-tag interleaving price U_C+beta V_C and an all-C actual-Boolean obstruction to replacing beta V_C by one fixed controller reserve. The counterfamily has H/I<=3, so the failed line is stronger than FEI and cannot be treated as its helper. Universal FEI payment gained is zero; the concrete gain is a closed false route plus its exact surviving seed debt. NEXT must select and pay a seed-dependent history or one actual tag collision, retaining both complete terminals, the incoming reference and SAME unused seed/structural owner. That is the shortest continuation because all protected interleavings are now priced exactly and universal seed-independent payment is rigorously ruled out.
'''
text=before+bridge
oldnext='Expose the protected balancing tag once after an inherited mixed controller/seed history; price empty-frequency interference in BOTH complete spectra A_s +/- B_s h_t using the SAME unused structural/seed reserve and a specified incoming reference. A088/A094 independently reconstruct separation and beta conservation; A032/A079 review the source specialization.'
text=text.replace(oldnext,p['next_action'])
write(R/'REPORT.md',text)
write(O/'STATUS.md','STATE: Exact U+beta V separation; EVERY finite-C fixed-controller all-history reserve refuted by actual Boolean H/I<=3 tensor seeds; exact certificates PASS; FEI OPEN.\nNEXT: A032/A079/A088/A094 review; select a seed-dependent history or pay one tag collision with BOTH terminals, incoming reference and SAME unused seed/structural owner.\n')
now=datetime.now(timezone.utc).isoformat()
with (O/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{now} - Same stage continuation: strengthened the exact interleaving identity to an all-C actual-Boolean fixed-controller-reserve no-go. Reconstructed prior bent/point-flip local seed, derived chi-square4/(N-1), positive selector debt at even m>=C+6, exact tensor amplification with complete terminal spectra, and H/I<=3 for seeds and fixed A079 outer family. Six frozen dimension checks: {cert["exact_assertions"]} exact assertions PASS. This is a route refutation, not FEI disproof. Lean wrapper explicitly held on resource admission and started no compiler; no retry. Final next action now requires selected/seed-dependent payment.\n')
with (O/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{now} - ALL-C all-history fixed-controller-bank no-go: for even m>=max(2,C+6), g=quadratic bent, h=g with origin flipped, f=(g,h), delta=2^-m. Midpoint normalized spectrum has chi-square4/(2^m-1); hence Delta_z H(f)-C delta>delta*(m-C-4/ln2)>0 using ln2>2/3. Exact I(f)=m/2+(m+1)delta and H(f)<=3I(f). Tensor copies and query only each selector, STOP with all g/h terminals: cost grows linearly while H/I<=3. Any fixed outer mask with beta>0 scales the cost by beta. A079 fixed-mask outer family also has H/I<=3. Thus a controller-only constant cannot pay EVERY seed history, even on a proved FEI-bounded family; retain beta V_C(h) or choose a paid seed-dependent history. Prior bent/flip local example credited to ERASURE_RIGIDITY/B05; no priority claim for it. Proof:NO_GO.md;6 frozen dimensions exact PASS.\n')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((O/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
proto=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))['required_per_run']
assert set(p)=={x.split(' (')[0] for x in proto['progress_fields']}
assert set(c)==set(proto['claim_fields'])
assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
assert all(q.stat().st_size<20*1024*1024 for q in R.rglob('*') if q.is_file())
receipt={'finalized_at':now,'protocol_keys':'PASS','statement_sha256':'PASS','progress_delta_identical':True,'validation':json.loads((R/'out/interleaving.json').read_text(encoding='utf-8')),'nogo_validation':cert,'boundary_status':'PASS','formal_status':'SETUP_UNVERIFIED resource hold; no compiler started','local_only':True,'artifacts':[{'path':str(q.relative_to(R)),'sha256':sha(q),'bytes':q.stat().st_size} for q in R.rglob('*') if q.is_file() and q.name!='PERSISTENCE_RECEIPT.json']}
dump(R/'out/PERSISTENCE_RECEIPT.json',receipt)
print(json.dumps({'status':'PASS','protocol_keys':'PASS','all_C_nogo':True,'nogo_exact_assertions':cert['exact_assertions'],'files':len(receipt['artifacts']),'full_FEI':'OPEN'}))
