from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];OWN=ROOT.parents[1]
REPORTS=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
TEAM=Path(r'~\brain_workers\FEI100_20261011')
def save(name,obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(b):return hashlib.sha256(b).hexdigest()
def txt(p):
    b=p.read_bytes()
    try:return b.decode('utf-8')
    except UnicodeDecodeError:return b.decode('cp1252')
sources=[REPORTS/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']]
sources += [SUP/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','baseline/current-threshold-paper.tex','supporting/shared_data_delta_independent_audit.md']]
sources += list((SUP/'sources').glob('*.md'))
sources += list((TEAM/'context').glob('*.txt'))
sources += list((REPORTS/'runs').rglob('REPORT.md'))
sources += [REPORTS/'source_material/reductions/paper/biased.tex',TEAM/'BOARD.md']
A056=TEAM/'agents/A056/runs/20261011T214407Z-fleet05-A056-balanced-composition'
sources += [A056/'REPORT.md',A056/'CLAIMS.json']
receipts=[];excerpts=[]
for p in sources:
    b=p.read_bytes();s=txt(p)
    receipts.append({'path':str(p),'bytes':len(b),'sha256':sha(b)})
    lines=s.splitlines()
    if p.name=='biased.tex':selected=lines
    elif p.name=='threshold_paper_38pp.txt':selected=lines[1340:1422]+lines[1948:2610]
    elif p.suffix=='.txt':selected=lines[:110]
    elif p==A056/'REPORT.md':selected=lines
    elif p.name=='REPORT.md':selected=lines[:75]
    else:selected=lines[:45]
    excerpts.append('\nSOURCE '+str(p)+'\n'+'\n'.join(selected))
save('out/SOURCE_RECEIPTS.json',{'sources':receipts,'absent':[str(TEAM/'claude/B19/STREAM_NOTES.md')],'receipt_scope':'Byte hashes; theorem-level reading/audit scope is stated in REPORT.md, not inferred from this manifest.'})
(ROOT/'out/SOURCE_EXCERPTS.txt').write_text('\n'.join(excerpts),encoding='utf-8')
original=json.loads((A056/'CLAIMS.json').read_text(encoding='utf-8'))
claims=[]
for c in original:
    # Preserve author identity and exact statement version; supply an independent review record only.
    c['review_records']=[{'reviewer':'fleet05/A091','verdict':'ACCEPT_AT_STATED_SCOPE','source':str(ROOT/'REPORT.md'),'method':'Independent rational centered-bit moment transform on three physical product laws; direct coefficient and formal prime-log identity checks; explicit physical-restriction witness. No A056 code reused.','reviewed_statement_sha256':c['statement_sha256'],'full_fei_status':'OPEN'}]
    c['status']='INDEPENDENTLY_REVIEWED_ACCEPTED_AT_STATED_SCOPE'
    claims.append(c)
statement='Child-ledger-only additivity of physical/spectral restriction quantities M_A=H(S_A|S_B) and J_A=I(Z;S_B) under arbitrary disjoint outer substitution is false: sign AND of two fresh uniform literal children has M_{first bit}=J_{first bit}=1 bit, while each standalone literal has M=J=0 for the aligned full/empty reveal. Additivity remains valid for aligned disjoint tensor products; a general outer-gate substitution requires a separate residual/cocycle.'
hyp=['Boolean signs','independent uniform physical inputs','ordinary spectral Shannon entropy in bits','M,J defined by the actual physical-child/spectral experiment']
claims.append({'claim_id':'A091-NONTENSOR-LEDGER-SCOPE','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':sha(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()),'contributors':['fleet05/A091'],'proof_source':{'path':str(ROOT/'REPORT.md'),'code':str(ROOT/'code/endpoints.py'),'output':str(ROOT/'out/endpoints.json')},'proof_dependencies':[],'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Child-ledger-only additive extension to arbitrary outer gate substitution; B09 Section 5 broad wording requires a specified residual'],'first_unproved_line':None,'next_consumers':['A043','A044','A056','A058','A090','B09','B12','B20']})
save('CLAIMS.json',claims)
scope={'review_verdicts':[{'source_claim':'A056-DISJOINT-COMPOSITION','version':1,'verdict':'ACCEPT_AT_STATED_SCOPE'},{'source_claim':'A056-PHYSICAL-RESTRICTION-SCOPE','version':1,'verdict':'ACCEPT_AT_STATED_SCOPE'},{'source':'threshold manuscript Prop 7.1/Cor 7.2','verdict':'CLOSURE_DERIVATION_ACCEPTED; leaf/gate estimates cited premises'},{'source':'threshold manuscript Prop 8.6/Cor 8.7-8.8','verdict':'CLOSURE_DERIVATION_ACCEPTED; regular-leaf estimate cited premise'},{'source':'B09 Section 5','verdict':'NARROW_TENSOR_ADDITIVITY; endpoint necessity requires separate proof'}],
 'disjoint_substitution':{'physical_inputs':'independent product laws','child_blocks':'pairwise disjoint','induced_probabilities':'q_i=(1+E f_i)/2, exact at every node/restriction','weights':'I_i^nu(g)/(1-(E f_i)^2), after removing zero-variance children','invariant':'corrected Hplus <= C (I-Var)','gate_admission':[{'gate':'symmetric threshold','input_biases':'all product biases, deterministic coordinates deleted','constant':'80+460/ln2','premise':'Theorem 6.6'},{'gate':'parity','input_biases':'all product biases','constant':'2/ln2','premise':'Lemma 7.5'},{'gate':'weighted LTF/regular','input_biases':'uniform; all nonconstant child outputs balanced','constant':'4 C_reg','premise':'Theorem A + D_char<=4(I-Var)'},{'gate':'fixed arbitrary gate basis','input_biases':'only those covered by separate all-bias gate theorem','constant':'maximum of separately established constants'}]},
 'shared_data':{'physical_inputs':'fresh uniform selector independent of common uniform branch data','overlap':'arbitrary data overlap admitted, including Fourier support overlap','correlation':'neighbor correlations zero is sufficient; actual I_sel>=c*a suffices','constant':'max(4,C) or max(2/c,C); recursive regular leaves C_reg','forbidden_inference':'current selector reuse without a new identity, arbitrary biased selectors via the uniform formula, uncharged low-energy collision term'},
 'terminals':{'constant':'H=I=delta=0; freeze/remove before division','biased_literal':'corrected Hplus=delta=0; raw H=h2(4p(1-p)) is not zero','uniform_balanced_I_equal_1':'signed dictator, H=0; do not divide by I-1','zero_current_selector_energy':'all branches identical; use branch directly','spectral_erasure_zero':'not an entropy terminal; bent splice and parity embeddings retain entropy'},
 'open':['all-arity weighted threshold product-bias Hplus estimate','all-bias prime-gate payment','signed collision payment at I_sel/a ->0','controlled current-selector reuse','B09 endpoint-tax necessary lower bound'], 'full_fei':'OPEN'}
save('COMPOSITION_SCOPE.json',scope)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B19','packet_id':'A091','gap_id':'FEI-B19-A091-INITIAL','attempt_id':'A091-composition-audit-1','method':'Independent coefficient factorization, rational moment transform, formal prime-log entropy checks, exact shared-data signed collision law, rigorous rational constants and original weighted-obstruction reconstruction','mathematical_delta':'Accepted A056 v1 disjoint composition and physical restriction scope; independently checked conditional shared-data closure and constants; narrowed B09 additive ledger scope to tensors; replayed bent splice and three weighted physical-payment obstructions. Full FEI remains open.','deliverable_status':'COMPLETE_LOCAL_PENDING_SUPERVISOR_COPY','mathematical_status':'AUDIT_COMPLETE_AT_STATED_SCOPE_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':'A056-DISJOINT-COMPOSITION','version':1},{'claim_id':'A056-PHYSICAL-RESTRICTION-SCOPE','version':1},{'source':'baseline/current-threshold-paper.tex','locators':'Prop 7.1, Cor 7.2, Prop 8.6, Cor 8.7-8.8; Theorem A and 6.6 conditional terminal premises'}],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],'source_artifacts':['REPORT.md','CLAIMS.json','COMPOSITION_REVIEW.md','COMPOSITION_SCOPE.json','out/SOURCE_RECEIPTS.json','out/SOURCE_EXCERPTS.txt','out/checks-law0.json','out/checks-law1.json','out/checks-law2.json','out/constants.json','out/controls.json','out/endpoints.json'],'next_consumers':['A019','A041','A043','A044','A045','A056','A057','A058','A090','A085','B20'],'next_action':'Review a new source-complete prime-gate or low-energy collision theorem when supplied; A058 should derive a paid signed collision ledger at I_sel/a tending to zero. Independent review of this audit: A090 or A085.','stagnant_substantive_attempts':0,'blockers':['B19 lead notes absent','No source-complete new A043 prime theorem or A058 overlap theorem found at initial intake; only their conditional interfaces audited','Remote copy/mirror/adoption pending supervisor, not a local-save blocker'],'packet_ids':['A091']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
(ROOT/'COMPOSITION_REVIEW.md').write_bytes((ROOT/'REPORT.md').read_bytes())
(OWN/'STATUS.md').write_text('STATE: A091 composition audit complete locally: A056 v1 accepted at scope, closure/constants checked, B09 tensor-only ledger guard saved; full FEI OPEN.\nNEXT: A090/A085 review audit; consume a source-complete prime-gate or low-energy/reused-selector theorem and test its complete bias/collision payment.\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-12: Completed independent composition review: 12,288 disjoint compositions, 512 shared selectors, 88,030 exact assertions; 3 bent splices, 9 weighted conditional-law tables, 6 rational-interval control rows, 3 endpoint fixtures. C_reg and all cited closure constants enclosed rationally. Initial combined main timed out at watchdog; batched unchanged domain passed. Initial controls took 61.155 seconds (1.155-second spec overrun); rational-mesh optimization reran the same domain in 0.817 seconds. B09 broad additivity requires tensor-only scope. All results saved locally; no external persistence/adoption claimed.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nA056 v1 accepted by independent rational centered-bit implementation: raw entropy H(F)=H_nu(g)+sum_i I_i(g)/v_i[H(f_i)-h2(v_i)], and corrected Hplus/deficit cocycles. Recenter after physical restriction; output conditioning does not imply a product cylinder.\nPhysical conditional TC(Q) is distinct from spectral M_A. Weighted event X0 OR AND_m has divergent TC/credit helper ratios while its actual corrected Hplus/delta tends to 2.\nB09 restriction ledgers M,J add for aligned disjoint products, not child-ledger-only arbitrary gate substitution: uniform AND of literals has M=J=1 although literal ledgers vanish.\nDo not call spectral-erasure-zero, rare activation, arbitrary signed shared leaves, or arbitrary prime arity an FEI-certified terminal.\n')
# Validate exact protocol field sets, then receipts, without rewriting any shared index.
protocol=json.loads((REPORTS/'EXECUTION_PROTOCOL.json').read_text())['required_per_run']
# Protocol annotates packet_ids in its human-readable field list; actual JSON key is packet_ids.
assert set(progress)==set(k.split(' (')[0] for k in protocol['progress_fields'])
for c in claims:assert set(c)==set(protocol['claim_fields'])
assert json.loads((ROOT/'PROGRESS.json').read_text())==json.loads((ROOT/'PACKET_DELTA.json').read_text())
assert len((OWN/'STATUS.md').read_text().splitlines())==2
for n in ['checks-law0.json','checks-law1.json','checks-law2.json','constants.json','controls.json','endpoints.json']:assert json.loads((ROOT/'out'/n).read_text())['status']=='PASS'
files=[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='RECEIPTS.json']
assert all(f['bytes']<20_000_000 for f in files)
save('out/RECEIPTS.json',{'local_only':True,'remote_copy':'PENDING_SUPERVISOR','files':files,'schema_validation':'PASS'})
print(json.dumps({'status':'PASS','files':len(files),'claims':len(claims),'progress_fields':len(progress),'main_exact_assertions':88030,'local_run':str(ROOT)}))
