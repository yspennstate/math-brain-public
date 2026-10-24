from pathlib import Path
import json,hashlib,copy
run=Path(__file__).resolve().parents[1];agent=run.parents[1];team=agent.parents[1]
campaign=Path(r'~\mop_fei100\reports\fei-2026-10-11')
protocol=json.loads((campaign/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
keys=protocol['required_per_run']
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(c):return sha(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode())
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
lead=team/'claude/B14/runs/20261011T224500Z-claude-B14-granularity-neutralization'
s68=team/'agents/A068/runs/20261012T022241Z-account05-A068-antichain-beyond-one-order'
b68=team/'agents/A068/runs/20261011T222313Z-account05-A068-antichain-beyond-one-order'
s69=team/'agents/A069/runs/20261012T043929Z-account05-A069-geometric-transfer'
s67=team/'agents/A067/runs/20261012T004014Z-account05-A067-hypercontractive-refinement'
s88=team/'agents/A088/runs/20261011T223053Z-account05-A088-booleanity-referee'
oldrun=agent/'runs/20261011T230551Z-account05-A070-analytic-route-referee'
def review(verdict,source,extras=None):
    r={'reviewer':'account05/A070','verdict':verdict,'proof_source':str(run/'DERIVATION.md'),'method':'Independent analytic reconstruction and own exact code; no author implementation imported','reviewer_conflict':False,'source_path':str(source),'source_sha256':sha(source.read_bytes()),'shared_registry_adoption':'PENDING_B20'}
    if extras:r.update(extras)
    return r
rawlead=json.loads((lead/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0]
old={k:copy.deepcopy(rawlead[k]) for k in keys['claim_fields']}
oldhash=old['statement_sha256'];old['statement_sha256']=canonical(old)
old['review_records'].append(review('GAP_AT_STATED_BOUNDARY',lead/'CLAIMS.json',{'original_statement_sha256':oldhash,'source_validation_field':rawlead.get('validation'),'exact_objections':['n=1,N=2 eps_raw=(sqrt(2)+1)/2>1; h2(eps_raw) undefined; caveat already in A067 stage2','n=0,N=1 constant seed edited to a character; its matching anchor has zero top coefficient'],'accepted_scope':'Rank-one coefficient update, influence/L1 bounds, and fixed-seed asymptotic consequences; full stated global version not accepted'}))
old['status']='GAP_AT_STATED_BOUNDARY_LOCAL_REVIEW_PENDING_B20'
old['first_unproved_line']='Clause (c) inserts eps_raw>1 into h2 at n=1,N=2; clause (a) every-anchor top support fails at n=0,N=1.'
corrected={
 'claim_id':old['claim_id'],'version':2,
 'exact_statement':'For every Boolean sign f on n>=0 uniform bits, every integer N>n with N>=2 and every input x0, put delta=2^-N and g_N=f(x_1,...,x_n)(1-2*1{x=x0}). Then ghat_N(S)=fhat(S)1{S subset [n]}-2delta f(x0)chi_S(x0); every coefficient is nonzero, so every character anchor has top coefficient nonzero and d=N on all sets. U(g_N)=N Var(g_N)-I(g_N), each physical coordinate influence changes by at most 2delta, and ||p(g_N)-p(f)||_1<=4delta(2^(n/2)+1). Put eta=min(2delta(2^(n/2)+1),1-2^-N). Then |H(g_N)-H(f)|<=h2(eta)+eta log2(2^N-1). For every fixed nonconstant seed, H and I converge to seed values and U/I diverges. For any nonnegative support weight psi with max_s psi(s,N)=o(2^N), its edited expectation on nonempty atoms minus sum_nonempty fhat(S)^2 psi(|S|,N) tends to zero. FEI with a fixed constant on this corrected padded-edited class implies FEI with the same constant on every Boolean seed; constants are handled separately.',
 'hypotheses':['Uniform probability measure; Boolean outputs in {-1,1}; entropy in bits','n>=0, N>n, N>=2; seed fixed in every limiting statement','d_g(S)=max degree of a supported superset; U sums over nonempty positive Fourier masses','The entropy-continuity cap uses monotonicity below 1-1/2^N and the global N-bit entropy bound above it','The support-weight statement requires nonnegative psi and max_s psi(s,N)=o(2^N)'],
 'statement_sha256':'','contributors':['Claude B14 lead: original valid asymptotic theorem','account05/A070: boundary/domain repair; recused from independent acceptance','account05/A067: earlier identification of eps-domain caveat'],
 'proof_source':str(run/'DERIVATION.md')+' Section 1','proof_dependencies':[],'review_records':[],
 'status':'REPAIRED_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[{'claim_id':old['claim_id'],'version':1,'scope':'Corrects only small-dimension anchor and entropy-domain scope; asymptotic mechanism unchanged'}],
 'refutes':[],'first_unproved_line':None,'next_consumers':['A067','A088','A094','B14','B20']}
corrected['statement_sha256']=canonical(corrected)
c69=json.loads((s69/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0]
assert canonical(c69)==c69['statement_sha256']
c69['review_records'].append(review('ACCEPT_AT_STATED_SCOPE',s69/'CLAIMS.json',{'no_mathematical_repair':True,'validation':'360 addressing edits and 4608 proper-subcube fixtures; direct character sums and physical edge probabilities','dependency':'A069-STABLE-HIERARCHY-EDIT-PAYMENT v1 accepted by A070 in stage1; not reopened'}))
c69['status']='INDEPENDENTLY_ACCEPTED_LOCAL_RECEIPT_PENDING_B20'
c68={
 'claim_id':'A070-REVIEW-A068-REPORTED-CYCLIC-EDIT-REFERENCE','version':1,
 'exact_statement':'For every odd q>=5, let F_q(x,z)=MAJ_q(x_i*(-1)^(u_i*u_(i+1))) on q distinct private data bits and q cyclic uniform control bits. Pad to any N>=2q and flip any one input to obtain G. Let R0 be the normalized data-level rank/affine-quadratic-fiber reference of the accepted A068 base theorem, extended by zero on padding frequencies, delta=2^-N, and R_delta=(1-delta)R0+delta U_N. Then R_delta is normalized with full support, H(G)<=Gamma_delta(G)<=C_reg I_x(G)+2I_z(G)-(287/1920)I_x(F_q), where C_reg=log2(4+e)+2log2(e*pi), I_x(F_q)=q binom(q-1,(q-1)/2)/2^(q-1), and I_z includes padding. For fixed q under padding and a one-point edit, Gamma_delta(G) tends to Gamma0(F_q). This accepts the exact theorem stated in A068 stage2 REPORT.md, with its named accepted base-rank dependency; it does not establish absent author package/full-validation receipts.',
 'hypotheses':['Independent uniform physical bits; actual Boolean signs; entropy and expected reference cost in bits','Odd q>=5; q private data labels; controls are the specified cyclic quadratic signs; one edit at any input','Complete R0 base reference and its C001 rank-cost estimate at the source accepted by A088','Uniform fallback prior is delta=2^-N and is fixed before observing the Fourier set','Local review ID is not an upstream registered A068 claim ID; source report theorem is the reviewed artifact'],
 'statement_sha256':'','contributors':['account05/A068 original report theorem'],
 'proof_source':{'source_report':str(s68/'REPORT.md'),'source_report_sha256':sha((s68/'REPORT.md').read_bytes()),'source_locators':'target theorem and Sections 1-4','independent_reconstruction':str(run/'DERIVATION.md')+' Section 2','review_id_mapping':'Local source-bound review ID; B20 upstream mapping pending'},
 'proof_dependencies':[{'claim_id':'A068-QUADRATIC-CONTEXT-RANK-REFERENCE','version':1,'statement_sha256':'23b8038c7a0da79a4d10c3dd9f897646ea2f5b155814c6c112b2a4efa208f181','acceptance':'A088 AUDIT.md lines 73-79, accepted at source-bound C001 scope','source':str(b68/'CLAIMS.json')},{'claim_id':'C001','version':'supplement 2026-10-11 / accepted recovered regular-rank source','source_sha256':'5d87f625fbadad4aa9841416712b8193a869fa9dffcb4e9c200d2f39a62e6a10','acceptance':'Inherited explicit accepted baseline, not a new full-paper proof audit'}],
 'review_records':[review('ACCEPT_REPORTED_THEOREM_AT_STATED_SCOPE',s68/'REPORT.md',{'no_mathematical_repair':True,'implementation':'16 selected edits independently certified complete reference costs; all-q proof reconstructed separately','package_completion':'Source CLAIMS/PROGRESS/PACKET_DELTA and full validation output absent at read cutoff'})],
 'status':'INDEPENDENTLY_ACCEPTED_SOURCE_THEOREM_UPSTREAM_ID_AND_PACKAGE_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A068','A088','A094','B14','B20']}
c68['statement_sha256']=canonical(c68)
cross={
 'claim_id':'A070-TWO-EDIT-PROJECTION-CROSS-LEDGER','version':1,
 'exact_statement':'For any fixed singleton-leaf partition tree with internal cells C_v and child arities b_v, put L(S)=1+sum_v b_v*1{S meets C_v} and <u,v>_L=sum_S uhat(S)vhat(S)L(S). For arbitrary real u,v, <u,v>_L=(1+sum_v b_v)E[uv]-sum_v b_v E[(E[u|C_v^c])(E[v|C_v^c])]. For distinct one-point Boolean edits e_x=-2g(x)1{X=x}, e_y=-2g(y)1{X=y}, the cross is -4g(x)g(y)2^(-2N)sum_v b_v*2^(N-|C_v|)*1{x,y agree outside C_v}. It can be positive despite disjoint physical edit supports: the two-bit x1 seed with edits (+,+),(-,+) gives cross=1/2, individual energies 5/2 and combined energy 6. Moreover for any Boolean core h on a nonempty Y, let g=x1*h(Y), Z={x1,x2}, and join the binary Z tree and any binary Y tree under a binary root. Disjoint proper subcube edits D1={x1=+,x2=+},D2={x1=-,x2=+} have cross=(1+(Eh)^2)/2>=1/2. Their final sign is f=-x1*x2*h, with Gamma(f)=Gamma(g)=5+E_(S_h)W_Y, H(f)=H(g)=H(h), and I(f)=I(g)+1. Thus no finite physical-intersection-density-only bound controls the signed or absolute edit cross; the exact source/edit rebate and retained-core cost cannot be discarded.',
 'hypotheses':['Uniform finite cubes; code lengths/energies in bits; partition tree fixed before observing frequency sample','General projection identity requires only real u,v; Boolean signs are required for the physical edit witnesses and influence statements','Proper-subcube family keeps Y nonempty and arbitrary Boolean h; W_Y is the whole Y subtree mask bill, not assumed paid','Sequential overlapping flips have final difference e1+e2-2e12; union-once edits instead have e1+e2-e12','This is an exact transport/refutation interface, not a universal Gamma<=K I theorem'],
 'statement_sha256':'','contributors':['account05/A070'],
 'proof_source':str(run/'DERIVATION.md')+' Section 4','proof_dependencies':[],'review_records':[],
 'status':'AUTHOR_PROVED_EXACT_CERTIFICATES_PASSED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Hypothetical universal <e1,e2>_L<=K P(D1 intersection D2) or absolute-value variant; no registered A069 theorem asserted this'],
 'first_unproved_line':None,'next_consumers':['A069','A067','A088','A094','B05','B13','B14','B20']}
cross['statement_sha256']=canonical(cross)
claims=[old,corrected,c68,c69,cross]
write(run/'CLAIMS.json',claims)
progress={
 'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B14','packet_id':'A070','gap_id':'G-A070-STABLE-COMPLETE-ANALYTIC-CODE','attempt_id':'A070-stage2-independent-reference-and-cross-ledger',
 'method':'Three referee controls: normalized real spectra, Boolean pad-and-flip, independent direct-character/edge/interval implementation; corrected lead boundary and exact signed cell-projection cross ledger',
 'mathematical_delta':'A069 stage2 v1 accepted; A068 reported full-support cyclic repair accepted at exact baseline scope with packaging caveat; lead v1 boundary gap pinned and v2 repaired; proper-subcube positive cross despite zero physical overlap; arbitrary retained-core reference cost transports exactly on the witness family',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_PENDING_SUPERVISOR_COPY','mathematical_status':'SCOPED_REVIEW_AND_REPAIR_COMPLETE_CROSS_LEDGER_PROVED_UNREVIEWED_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':old['claim_id'],'version':1,'original_statement_sha256':oldhash,'acceptance':'GAP at boundary; valid portions reconstructed independently'},{'claim_id':'A068-QUADRATIC-CONTEXT-RANK-REFERENCE','version':1,'acceptance':'A088 source-bound accepted C001/rank dependency'},{'claim_id':'A069-STABLE-HIERARCHY-EDIT-PAYMENT','version':1,'acceptance':'A070 stage1 independent acceptance; baseline not reopened'},{'claim_id':c69['claim_id'],'version':1,'acceptance':'A070 independent ACCEPT_AT_STATED_SCOPE in this run'}],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],
 'source_artifacts':['REPORT.md','DERIVATION.md','ANALYTIC_SCOPE_AUDIT.md','FROZEN_SPEC.json','FROZEN_OVERLAP_WITNESS.json','RELAXATION_CONTROL_RESULTS.json','out/CONTROL_CHECK.json','out/CYCLIC_CHECK.json','out/PROPER_SUBCUBE_WITNESS.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':['A067','A068','A069','A088','A094','B14','B20'],
 'next_action':'Pay one first-exposure-owned cell-projection cross charge for two overlapping-control subcube edits, including the sequential intersection correction and both retained terminal cores; do not repeat edited-addressing code construction',
 'stagnant_substantive_attempts':0,
 'blockers':[{'scope':'A068 source package adoption only','reason':'Required source claim/progress and declared full-validation files absent at read cutoff; local mathematical review supplies an independent proof/certificate but does not assert author packaging completion'},{'scope':'historical cyclic-law replay, unrelated proof dependency','reason':'Stage1 Addendum 11.51 source not recovered; no repeated recall in this stage'}],
 'packet_ids':['A070']}
write(run/'PROGRESS.json',progress);write(run/'PACKET_DELTA.json',progress)
control=json.loads((run/'out/CONTROL_CHECK.json').read_text());cyclic=json.loads((run/'out/CYCLIC_CHECK.json').read_text());proper=json.loads((run/'out/PROPER_SUBCUBE_WITNESS.json').read_text())
write(run/'RELAXATION_CONTROL_RESULTS.json',{'actual_Boolean_refutations':{'zero_dimensional_anchor':control['boundary_counterexamples'],'positive_disjoint_point_cross':control['positive_disjoint_cross_witnesses'],'proper_subcube_cross_with_nonconstant_cores':proper},'normalized_real_diagnostic':{'singleton':'H=log2 n, E_spec=1, fourth moment=3-2/n; Boolean arithmetic hypothesis fails','A068_cyclic_linear_base':'H=log2 q+2, E_x=E_z=1; fourth moment=3-2/q; regular Boolean base essential','theorem_refuted_by_nonBoolean_control':False},'pad_flip_verdicts':{'lead_v1':'boundary repair required; asymptotic content holds','lead_v2':'repaired proof complete; A070 contributor recused from acceptance','A068':'paid full-support repaired code stable, conditional on exact accepted base-rank dependency','A069':'all-set hierarchy paid and stable at declared family scope'},'independent_execution':{'author_code_imported':False,'assertions':control['exact_assertions']+cyclic['exact_assertions']+proper['exact_assertions'],'target_or_certificate_cases':sum(control['counts'].values())+cyclic['cases']+proper['cases'],'control_seconds':control['seconds'],'cyclic_seconds':cyclic['seconds'],'failed_pilot_counted':False},'cyclic_law_replay':'NOT_RECOVERED_NOT_REPLAYED_NOT_USED'})
sourcefiles=[campaign/'EXECUTION_PROTOCOL.json',team/'BOARD.md',team/'claude/B14/STREAM_NOTES.md',agent/'STATUS.md',agent/'LEARNED.md',oldrun/'REPORT.md',oldrun/'CLAIMS.json',oldrun/'DERIVATION.md',lead/'REPORT.md',lead/'CLAIMS.json',s68/'REPORT.md',s68/'out/pilot_v2.json',s68/'out/PROOF_CHECKPOINT.md',b68/'CLAIMS.json',b68/'REPORT.md',s69/'REPORT.md',s69/'DERIVATION.md',s69/'CLAIMS.json',s67/'REPORT.md',s88/'AUDIT.md']
manifest=[]
for p in sourcefiles:
    raw=p.read_bytes();raw.decode('utf-8-sig')
    manifest.append({'path':str(p),'bytes':len(raw),'sha256':sha(raw),'read_scope':'Protocol/board/current direction or exact target/dependency locators recorded in REPORT.md'})
write(run/'out/SOURCE_MANIFEST.json',manifest)
write(run/'out/SOURCE_PACKAGE_BOUNDARY.json',{'A068_source_folder':str(s68),'read_cutoff_absences':['CLAIMS.json','PROGRESS.json','PACKET_DELTA.json','out/validation.json','out/SUMMARY.json'],'finalization_actual_exists':{n:(s68/n).exists() for n in ['CLAIMS.json','PROGRESS.json','PACKET_DELTA.json','out/validation.json','out/SUMMARY.json']},'mathematical_verdict':'Report theorem independently reconstructed at scope','adoption_verdict':'Upstream ID/package mapping pending B20; no other-agent file modified'})
(run/'out/LEAD_NOTES_READ_SNAPSHOT.md').write_bytes((team/'claude/B14/STREAM_NOTES.md').read_bytes())
(run/'out/START_STATUS_READ_SNAPSHOT.md').write_bytes((agent/'STATUS.md').read_bytes())
assert all(set(c)==set(keys['claim_fields']) for c in claims)
assert all(canonical(c)==c['statement_sha256'] for c in claims)
assert set(progress)=={k.split(' (',1)[0] for k in keys['progress_fields']}
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
report=(run/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+h in report for h in keys['report_fields'])
assert report.splitlines()[-1].startswith('Universal bridge:')
write(run/'out/SCHEMA_CHECK.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,'descriptor_normalization':'packet_ids (one primary ID, for compatibility) -> packet_ids','report_fields_present':True,'statement_hashes_canonical':True,'source_lead_original_statement_hash_preserved_in_review':True,'compatibility_copy_bytes_identical':True,'claim_count':len(claims),'new_broad_FEI_candidate_opened':False,'authored_repair_independently_accepted_by_A070':False})
(agent/'STATUS.md').write_text('STATE: A070 stage2 complete: A069 v1 and A068 report theorem accepted at scope; lead boundary repaired; positive disjoint-edit cross and exact core-preserving transport proved; 93,346 checks PASS; FEI OPEN.\nNEXT: A088/A094 review lead v2/cross ledger; pay first-exposure-owned projected-core cross terms for overlapping controls with intersection correction and both terminal costs retained.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('2026-10-13T21:26:02Z stage2: Read updated BOARD, B14 v2 and saved status. Retired duplicate addressing-code construction after consuming A069 stage2. Independently accepted A069 aligned-edit v1 and A068 reported cyclic full-support repair at scope; source A068 package lacked claim/progress/full-validation files at cutoff. Reconfirmed A067 eps>1 caveat, added n=0,N=1 anchored counterexample, and supplied corrected lead v2 with explicit entropy cap; contributor recused. Proved signed cell-projection cross ledger, certified disjoint proper-subcube positive cross=1/2 with y/-y cores, and derived arbitrary-core Gamma(f)=Gamma(g) transport. Independent standard-library checks passed 93,346 assertions in 12,805 cases; cyclic initial serialization failure repaired by outward 2^-80 interval rounding, no failed-run results counted. Files/schemas saved locally; full FEI and universal cross/terminal payment open.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n## Stage 2 durable interfaces\n\n- Lead neutralization needs N>=2 for every-anchor full support when n=0 is allowed. Original n=1,N=2 eps_raw=(sqrt(2)+1)/2 exceeds the h2 domain (already flagged by A067). Set eta=min(eps_raw,1-2^-N); use h2(eta)+eta log2(2^N-1), invoking the global N-bit entropy bound when the cap is active. Corrected v2 retains all fixed-seed asymptotics; A070 contributes and cannot independently accept it.\n- A068 reported cyclic repair R_delta=(1-delta)R0+delta U_N pays every tail atom; complete cost <=C_reg I_x+2I_z-(287/1920)J for odd q>=5. Independent direct-block/whole-table/rational-interval replay accepts the theorem at its explicit accepted-rank baseline scope, not author package completion.\n- A069 aligned addressing/subcube v1 independently accepted. Its complete hierarchy already closes A070 stage1 addressing reference NEXT: 16I for N rho<=1/8 and 25I for every one-point edit. Do not duplicate that solved obligation.\n- For hierarchy L=1+sum b_C 1{S meets C}, weighted cross equals (1+sum b)Euv-sum b E[(E[u|C^c])(E[v|C^c])]. Physical disjointness only kills Euv and does not kill projected products.\n- Proper-subcube family: g=x1*h(Y), Z={x1,x2}, disjoint edits D1=(x1+,x2+),D2=(x1-,x2+) yield cross=(1+(Eh)^2)/2 >=1/2. Final f=-x1*x2*h has Gamma(f)=Gamma(g)=5+E_h W_Y, H(f)=H(g)=H(h), I(f)=I(g)+1. Source/edit rebate exactly cancels the difference-energy bill; the full core cost remains unpaid unless already certified.\n- Sequential overlapping flips require e1+e2-2e12 before energy expansion; union-once editing requires e1+e2-e12. Keep the operation and projection costs explicit.\n')
receipts=[]
for p in list(run.rglob('*'))+[agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md']:
    if not p.is_file() or p.name=='PERSISTENCE.json':continue
    raw=p.read_bytes();assert len(raw)<20_000_000
    receipts.append({'path':str(p),'bytes':len(raw),'sha256':sha(raw)})
write(run/'out/PERSISTENCE.json',{'status':'LOCALLY_SAVED','supervisor_copy_verified':False,'mirror_verified':False,'B20_adoption_verified':False,'files':receipts})
print(json.dumps({'status':'PASS','claims':len(claims),'exact_assertions':93346,'cases':12805,'files_receipted':len(receipts),'run':str(run)}))
