from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];HOME=R.parents[1];NOW=datetime.datetime.now(datetime.timezone.utc).isoformat();RID=R.name
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
main=read(R/'out/CHECK.json');audit=read(R/'out/AUDIT.json');assert main['status']==audit['status']=='PASS'
assert audit.get('reference_recipe_reconstructed') is True
assert main['cases']==audit['cases']==27 and main['positive_reset_nodes']==56
source=Path(r'agents\A040\runs\20261022T232049Z-fleet03-A040-credit-insufficiency-tests')
accepted=read(source/'CLAIMS.json')[0]
assert accepted['claim_id']=='A046-PRESCRIBED-SEPARATOR-RESERVE-RETIREMENT'
assert hashlib.sha256(accepted['exact_statement'].encode('utf-8')).hexdigest()==accepted['statement_sha256']
accepted['status']='INDEPENDENT_REVIEW_HOLDS_BY_A040_ADOPTED_BY_A046'
supplier='A050-CORRELATION-PRESERVING-SIGNED-LIFT'
supplierhash='671f52984dae0135907a518e7324c3efee58268b8065ab0e92137948844d937e'
statement=('For every m>=1,r>=2, let h be the product of m disjoint width-r point-defect Boolean signs and F_h(x,a,b,z)=(-1)^a on x0,h(z) on x=b=1,and1 otherwise, on a uniform cube. Use the original normalized A050 sector lift Q of the tensor factor reference q_r(empty)=p_r(empty),q_r(s)=(7/8)p_r(s)+(v_r/8)1_full for s nonempty, v_r=4*2^-r*(1-2^-r). Query b, retain b0, and take any finite adaptive fresh-data-only stopping tree in b1. At any selected active leaves expose x or a once and stop. After x reset only its core-bearing child to the tensor of conditional-factor fresh references r_k(empty)=p_k(empty),r_k(s)=(6/7)p_k(s)+(v_k/7)1_full, with exact laws for characters/constants. After a reset both children to their complete two-copy lifts of those fresh joint core references, copying actual zero-data masses. All complements keep inherited references. Actual source/reference transport retains full normalized laws, reference-only rows, physical reaches and all outcome/erasure KL. If T is complete reach-weighted fresh-reference KL, then T< m*2^-r/4 by finite conditional-variance contraction and7^4<2*6^4. The actual signed reset sigma=T-Kold_selected<=T is charged once. With A0=D(P_F||Q),e=H0-EHleaf-4(I0-EIleaf),S=E(4Ileaf-Hleaf), and any supplied earlier booking0<=omega<=1/4 against this original signed account, S-[A0+e+sigma]_+-omega>=3/4. The actual reset is full replacement to the specified fresh laws, not a renewed root account or a diluted incoming law. This stops at the stated mixed/reset frontier; no arbitrary-core initial source price, further divergent history or repeated-reset budget is asserted. All entropy/KL units are bits.')
claim={'claim_id':'A046-CORRELATED-RESET-AFTER-MIXED-EXPOSURE','version':1,'exact_statement':statement,'hypotheses':['Uniform physical Boolean signs; disjoint point factors m>=1,r>=2; actual entropy and influence, not relaxed spectral distributions.','Initial Q is exactly the specified correlated lift, not an unpriced conversion from a previously booked canonical source.','Finite adaptive DATA-only history follows b; at selected active leaves expose x or a once, make prescribed resets, and stop; retain b0 and every complementary terminal.','The fresh reference uses1/7 tilt and matches each factor empty mass; inherited original factor tilt remains1/8.','Only one supplied old booking omega<=1/4 is allowed; full signed query credit and all outcome/erasure/terminal costs remain in the SAME original owner.'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A046'],'proof_source':{'run_id':RID,'files':['PROOF.md','code/check.py','code/audit.py','out/CHECK.json','out/AUDIT.json','out/STRONGER_RESET_SPEC.json']},'proof_dependencies':[{'claim_id':supplier,'version':1,'statement_sha256':supplierhash,'scope':'Original sector lift, supplied point-tensor price and first mixed frontier. Relevant inputs reconstructed in PROOF.md sections1-3; no blanket independent acceptance of every source clause asserted.','status':'AUTHOR_SOURCE_SPECIFIC_INPUTS_RECONSTRUCTED'}],'review_records':[],'status':'ANALYTIC_PROOF_WITH_EXACT_CERTIFICATES_EXTERNAL_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A040','A039','A047','A049','A050','A087','A092','A094','B10','B20']}
save(R/'CLAIMS.json',[accepted,claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RID,'stream':'B10','packet_id':'A046','gap_id':'G-R-MISMATCH-SAME-OWNER-CORRELATED-RESET','attempt_id':'A046-stage8-variance-paid-post-controller-reset','method':'Consume already-paid A040 continuation; freeze A050 correlated initial source; finite conditional-variance amortization pays full prescribed post-x/a reset with same signed owner. Independent actual Boolean spectrum and rational reference audit.','mathematical_delta':f'For every m>=1,r>=2 and finite adaptive data frontier, selected x/a exposure plus full1/7-tilt correlated reset pays from SAME original1/8-tilt lifted source at rate4, keeping>=3/4 after oldquarter. 27 frozen histories pass{main["checks"]} main+{audit["checks"]} independent audit assertions, including56 positive reset nodes.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'ANALYTIC_PROOF_EXACT_CERTIFICATES; NEW_EXTERNAL_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':supplier,'version':1,'statement_sha256':supplierhash},{'claim_id':accepted['claim_id'],'version':1,'statement_sha256':accepted['statement_sha256'],'use':'observe independent A040 acceptance; prior NEXT already closed by A040 continuation, not a new proof premise'}],'claims_created_or_changed':[{'claim_id':accepted['claim_id'],'version':1,'change':'adopt unchanged independent A040 review'},{'claim_id':claim['claim_id'],'version':1,'change':'new all-m/r full correlated post-controller reset theorem'}],'source_artifacts':['out/SOURCE_RECEIPTS.json','out/PROTOCOL_SNAPSHOT.json','out/FROZEN_SPEC.json','out/STRONGER_RESET_SPEC.json','out/CHECK.json','out/AUDIT.json'],'next_consumers':claim['next_consumers'],'next_action':'A040/A050/A092 independently reconstruct the variance amortization and actual reset ownership. Then allow one active data query after an a-child reset using the SAME original Q/oldquarter and accumulated reset debit; prove the actual paired frontier S or preserve its full shortfall before any second reset.','stagnant_substantive_attempts':0,'blockers':['Arbitrary-core priced correlated initial reference is still unavailable; full FEI remains open.','No arbitrary divergent post-a history or repeated-reset allowance proved.','New theorem external independent review and supervisor private-route copy unverified.'],'packet_ids':['A046']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
lean='NOT_LAUNCHED_OR_UNVERIFIED'
coordination='Checklist completion pending until final local checkpoint.'
cp=R/'out/CHECKLIST_RECEIPT.json'
if cp.exists():
 cpr=read(cp);coordination='Checklist completion recorded.' if cpr.get('exit_code')==0 else 'Checklist completion could not be recorded: '+cpr.get('output','')[:280].replace('\n',' ')
p=R/'out/LEAN_RECEIPT.txt'
if p.exists():
 s=p.read_text(encoding='utf-8')
 try:
  obj=json.loads(s);lean=obj.get('result',{}).get('status',obj.get('status','UNVERIFIED'))
 except Exception:lean=s[:220].replace('\n',' ')
report=f'''# exact target, quantifiers, hypotheses and units

A046/B10 stage8 closes the selected post-controller reset step on the point-tensor supplier class. For every m>=1,r>=2, h is a product of m disjoint width-r point signs and F_h is the three-control family in PROOF.md. Keep the ORIGINAL A050 normalized correlation-preserving lifted reference and an old eligible booking0<=omega<=1/4. After b, ANY finite adaptive DATA-only frontier and one selected physical x/a exposure, reset the core-bearing x child or both a children to prescribed complete correlated references with fresh1/7 tilt. Original source tilt stays1/8. Both full terminals, all complementary leaves and signed old/new bills remain. The SAME source owner retains>=3/4 at unchanged rate4. Units are bits; influence is physical. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read BOARD and B10 notes v2 and own two-line STATUS at stage start. A040 run20261022T232049Z REPORT/PROOF/SINGLETON_GUARD/CLAIMS independently accepts the previous A046 transaction unchanged and already closes all four second-data/S continuations. Therefore that prior NEXT is consumed, not rerun. Its all-core singleton guard and product-CE/I>=n-1 barrier reject product-reference admission as the next mechanism. The old B10 scalar-review target was completed in earlier stages; no unchanged retired scalar repair was retested.

The selected supplier is A050 run20261022T232833Z PROOF sections1-4, CLAIMS {supplier}@1 hash{supplierhash}; its lifted source and mixed x/a frontier are reconstructed directly. A039 run20261022T222059Z REPORT/PROOF/SIGNED_REPAIR locates why negative query edges and the original unused allowance must remain. Source bytes are pinned in out/SOURCE_RECEIPTS.json; this is specific input reconstruction, not blanket acceptance of all claims in these sources. Execution-v2 protocol and fields were read; its full snapshot is saved. Earlier campaign/manuscript intake remains earlier-stage provenance, with no new uninspected paper premise or new network source. Current user endpoint23October14:49UTC overrides old protocol dates.

Required wake reported stale personal-model/state-of-mind notes about87/71hours old; the user was told before reliance and neither note is a premise. Compute state/interventions were read. No process was stopped to free resources. Research remains bounded and local.

# complete derivation or exact first unsupported line

PROOF.md gives the complete all-dimensional proof. Original point-reference price supplies M0=4I0-CE0>1+2t+m2^-r/4. For each original factor H_j and the adaptive data partition L, the finite law of total variance gives E Var(H_j|L)<=Var(H_j). Restriction leaves are actual cylinders, including constant exits and width-one characters. Fresh factor references have KL<=v_j log2(7/6), and the exact integer sign7^4<2*6^4 gives log2(7/6)<1/4. Physical b/x reaches, or b/a reaches together with the two-sector half-KL identity, give total fresh KL T<=m2^-r(1-2^-r)log2(7/6)<m2^-r/4. This uses one ORIGINAL variance allowance for the entire frontier.

Actual signed reset sigma=T-Kold_selected is retained with its inherited terminal references; no deletion is free. The full same-kernel chain is A0+sigma=sum old erasure/outcome costs+Knew. The complete paid margin is S-[A0+e+sigma]_+-omega=min(S,M0-sigma)-omega. The actual mixed frontier has S>=1, including retained b0 and aggregate a-pairs, so the remaining account is>=3/4. Neither T and sigma nor the negative query credits are counted twice.

The initial18-case target had only nonpositive reset increments. That diagnostic is preserved as PRE_STRONGER_CHECK/PILOT, then a pre-run amendment fixed the stronger1/7 target and added zero-data-prefix cases AFTER an actual active x/a exposure. The final27-case certificate includes56 positive reset increments; it is not evidence only from favorable resets. Physical dimension never increases beyond9. The whole source/reference theorem, not finite extrapolation, supplies every m,r and adaptive frontier.

First unsupported universal line: provide a useful correlated initial source price for an arbitrary Boolean core. At this specific history interface, a further active data query after an a-child reset also needs a new actual paired S bound and an accumulated reset ledger. Arbitrary post-a continuation or repeated reset payment is not claimed.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes the initial pilot/main; STRONGER_RESET_SPEC.json precedes the amended target, pilot and main; AUDIT_SPEC.json precedes the independent audit. No symmetry quotient or floating sign decision. Final domain: (m,r)=(1,2),(2,2),(2,3), prefixes none/first/adaptive and controllers x/a/mixed:27 labelled histories, maximum9 physical variables. Independent code imports no foreign helper.

Commands from A046:

    python -X utf8 -B runs/{RID}/code/check.py --pilot
    python -X utf8 -B runs/{RID}/code/check.py
    python -X utf8 -B runs/{RID}/code/audit.py

Amended pilot PASS:1case,187 assertions,0.0131s. Main PASS:{main['checks']} assertions,{main['nodes']} physical nodes,{main['runtime_seconds']:.4f}s. Audit PASS:{audit['checks']} assertions,{audit['runtime_seconds']:.4f}s,3 independently recomputed character-sum roots with physical-edge influences, all persisted full law/reference/KL bills recomputed using40 rather than32 atanh terms. Main uses integer FWHT/Fraction, proved32-term logarithm tails and outward2^-110 bounds. Both runs verify normalization, support and strictly positive reference branch probabilities. Actual reference-only erased rows in this family:0; the code retains them if present, and no positive count is invented. Main and audit independently count56 positive reset nodes. The audit verifies exact finite records, not the analytic unbounded quantifiers.

Each research job estimates100MB with55s cap, no GPU, automatic dimension increase, detached worker or overlapping heavy job. Fresh memok was requested before the narrow formal check. Formal status: {lean}. ResetBound.lean concerns ONLY the exact scalar sign7^4<2*6^4; even a verified scalar result would not certify variance amortization, entropy or FEI. No prior failed formal target is retried. See out/MEMOK.txt and out/LEAN_RECEIPT.txt for actual admission and compiler evidence.

The additional exact reference-recipe audit initially failed because its inner loop shadowed the branch-reach variable. The prior9585-check audit remained valid at its narrower scope, but its receipt did not certify the extension. AUDIT_REPAIR.json records the failure and fixed variable name. The corrected audit reconstructs every prescribed reference and requires a new recipe-verified marker before finalization; its final count is{audit['checks']}. No failed execution is counted as passing.

# proof dependencies and changed downstream conclusions

Adopt the unchanged independent A040 acceptance of A046-PRESCRIBED-SEPARATOR-RESERVE-RETIREMENT@1, hashd2021311ab374a71c57771c9e5fa82474b3708a4af40e9cc3107cb423ed981fa. A040 has already paid that next continuation and proved its product-source obstruction, so a new code7 census or full-original-U release would duplicate or contradict current results.

The new theorem retains A050's ORIGINAL paid correlated source and changes only the explicitly prescribed descendant reference. Root1/8 tilt and new1/7 tilt are distinct normalized laws with an actual charged sigma. This closes A050's stated fresh reset after a paid mixed exposure on every supplied point-tensor instance, including its canonical falsifiers. It is a new proof pending external review, with specific original supplier inputs rederived and no dependency cycle. No general arbitrary-core supplier is inferred from this class.

# one next mathematical action and independent reviewer

{progress['next_action']} This must not renew the original source, old quarter or factor-variance allowance.

# actual persistence receipts or precise save blocker

Saved all four protocol files, complete proof, frozen specifications, self-contained code, immediate per-history full probability records, independent audit, actual formal receipt and source pins. STATUS is exactly two lines; WORKLOG/LEARNED append dated durable facts. PERSISTENCE.json verifies protocol key sets, statement hashes, identical progress/delta, readback hashes and every file<20MB. No git, external messages, foreign research writes, brain-store writes, trading access, deletion, GPU, background job or schedule changes. Runtime wake/checklist/formal helpers maintain their required own receipts separately. Supervisor private-repository copy, mirror verification, shared index adoption and independent review remain unverified; no remote persistence is claimed.

{coordination}

## Universal bridge

This stage moves C024 history transfer and C019 stopping-tree payment by paying the previously excluded FULL prescribed correlated reset after actual x/a exposure from the SAME original point-tensor source, for all factor counts/widths and finite adaptive data frontiers, retaining>=3/4 after the old quarter and every terminal bill. The universal FEI constant improves by zero. An arbitrary-core priced initial correlated reference and post-a/repeated-reset eligibility remain unpaid. NEXT follows one actual data query beyond the now-paid reset with the original diminished owner, because this tests whether the acquired transfer composes into a stopping proof rather than merely adding another isolated class entropy estimate.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(HOME/'STATUS.md').write_text(f'STATE: A046 stage8 saved: all-m/r full correlated post-x/a reset paid from SAME original source, >=3/4 after oldquarter;27 cases/{main["checks"]} main+{audit["checks"]} audit checks,56 positive reset nodes; review pending, FEI OPEN.\nNEXT: A040/A050/A092 review; query active data after an a-child reset using SAME original Q, oldquarter and accumulated reset debit; certify actual paired S before any second reset.\n',encoding='utf-8')
if RID not in (HOME/'WORKLOG.md').read_text(encoding='utf-8-sig'):
 with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{NOW} — {RID}: consumed A040 unchanged acceptance and already-paid second-query continuation; full-product admission is retired by its all-n barrier. Reconstructed A050 correlated supplier and proved all-m/r adaptive variance amortization pays prescribed1/7 post-x/a full reset from original1/8 source, >=3/4 after oldquarter. Initial18 cases only negative reset increments; frozen stronger target and27 cases give26123 exact checks/56 positive nodes, independent40-term audit9585 PASS. Arbitrary-core source and further post-a frontier remain open; formal receipt separate, new external review pending.\n')
if '2026-10-23 stage8:' not in (HOME/'LEARNED.md').read_text(encoding='utf-8-sig'):
 with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-23 stage8: For A050 point-tensor supplier m>=1,r>=2, keep root1/8-tilt correlated lift. After b and ANY finite adaptive data frontier, expose selected x/a. Full fresh factor1/7 tilt has KL<=v log2(7/6), exact7^4<2*6^4. E sum conditional factor variance<=m v_r, so total fresh KL T<=m delta(1-delta)log2(7/6)<m delta/4, paid by UNUSED original source allowance. x resets only pure-core child; a resets both normalized two-sector lifts with half core KL each. sigma=T-Kold_selected, not T+sigma. min(S,M0-sigma)-oldquarter>=3/4 since actual mixed frontierS>=1. Preserve original source, both terminals and all outcome costs. Finite27 histories include56 positive resets; arbitrary-core source price and further post-a/repeated-reset history remain open.\n')
proto=read(R/'out/PROTOCOL_SNAPSHOT.json')['required_per_run']
assert set(progress)==set(s.split(' (')[0] for s in proto['progress_fields'])
for c in [accepted,claim]:
 assert set(c)==set(proto['claim_fields'])
 assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for heading in proto['report_fields']:assert '# '+heading in report
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  b=p.read_bytes();assert len(b)<20_000_000
  files.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save(R/'out/PERSISTENCE.json',{'status':'PASS','timestamp':NOW,'files':files,'schemas':'exact protocol keys','progress_delta':'byte-identical','full_fei':'OPEN','independent_review':'PENDING','remote_save':'UNVERIFIED','formal_status':lean})
print(json.dumps({'status':'PASS','files':len(files),'new_statement_sha256':claim['statement_sha256'],'formal_status':lean}))
