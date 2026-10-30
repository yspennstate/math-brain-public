from pathlib import Path
import json,hashlib,datetime,shutil
run=Path(__file__).resolve().parents[1]; agent=run.parents[1]
team=agent.parents[1]; campaign=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def write(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(b): return hashlib.sha256(b).hexdigest()
def sh(c): return digest(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode())
protocol=json.loads((campaign/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
claims=[]; used=[]
imports=[('A066','20261011T214539Z-fleet05-A066-semigroup-dissipation'),('A067','20261011T220539Z-fleet05-A067-hypercontractive-refinement'),('A069','20261011T224507Z-fleet05-A069-geometric-transfer')]
for who,folder in imports:
    source=team/'agents'/who/'runs'/folder
    for c in json.loads((source/'CLAIMS.json').read_text(encoding='utf-8-sig')):
        if c['claim_id'] in [x['claim_id'] for x in claims]: continue
        original_hash=c['statement_sha256']; convention='protocol statement+hypotheses canonical JSON'
        if sh(c)!=original_hash:
            assert digest(c['exact_statement'].encode())==original_hash
            convention='legacy statement-only SHA256, verified exactly'
            c['statement_sha256']=sh(c)
        c['review_records'].append({'reviewer':'fleet05/A070','verdict':'ACCEPT_AT_STATED_SCOPE','method':'Independent finite-sum/finite-difference/occupancy reconstruction, exact Walsh and edge validation of finite inputs; no mathematical repair or coauthorship','proof_source':str(run/'DERIVATION.md'),'reviewer_conflict':False,'shared_registry_adoption':'PENDING_B20','original_statement_sha256':original_hash,'original_hash_convention':convention,'local_hash_convention':'protocol statement+hypotheses canonical JSON; identical statement and hypotheses'})
        c['status']='INDEPENDENTLY_ACCEPTED_LOCAL_RECEIPT_PENDING_B20'
        claims.append(c); used.append({'claim_id':c['claim_id'],'version':c['version'],'acceptance':'A070 independent reconstruction at scope','original_statement_sha256':original_hash,'local_protocol_statement_sha256':c['statement_sha256']})
new={
 'claim_id':'A070-HYBRID-SCOPE-AND-THREE-REFERENCE-NOGO','version':1,
 'exact_statement':'For any finite probability law p, atom costs a_s>=log2(1/p_s) and nonnegative Kraft lengths l_s, let m be the mass where l_s<a_s. Then H(p)<=sum_s p_s min(a_s,l_s)+m log2(1/m)<=sum_s p_s min(a_s,l_s)+h2(m). For every integer a>=8, pad the Boolean addressing function with a address and 2^a private data coordinates to N=a+2^a+2 bits and flip its all-plus input, obtaining F_a. Put c_arith(S)=2(N-1) on nonempty S and infinity on empty S, c_inf(S)=log2(e)+sum_i_in_S log2(I(F_a)/Inf_i(F_a)), and c_level(S)=-log2(r_|S|)+log2 binom(N,|S|) for any probability prior r on levels. Then E_{p_Fa} min(c_arith,c_inf,c_level)/I(F_a)>=log2(a/2)/40, while H(F_a)/I(F_a)->4. The same lower bound holds for min(c_arith,c_mix), where c_mix is the length of any fixed subprobability prior mixture of the influence and level code laws. Thus no universal O(I) expected-cost bound exists for these three references; no queue-code or FEI claim is refuted.',
 'hypotheses':['Uniform finite sign cubes for F_a; abstract partition inequality requires only a probability law','Entropy and code lengths in bits; infinities allowed where code probability is zero','Addressing uses distinct private data variables and two dummy coordinates; edit at all plus','Level prior is normalized; code-mixture weights are fixed across atoms and sum at most one','Empty atom has an explicit code or separate charge; Boolean arithmetic not applied to empty'],
 'statement_sha256':'','contributors':['fleet05/A070 independent reconstruction','Claude B14 lead: prior statement of hybrid and point-defected-addressing mechanism'],
 'proof_source':str(run/'DERIVATION.md'),'proof_dependencies':[],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Universal expected-cost O(I) payment of granularity plus only level and influence code references'],
 'first_unproved_line':None,'next_consumers':['A067','A088','A094','B14','B20']}
new['statement_sha256']=sh(new); claims.append(new)
write(run/'CLAIMS.json',claims)
gap='G-A070-STABLE-COMPLETE-ANALYTIC-CODE'
progress={
 'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B14','packet_id':'A070','gap_id':gap,'attempt_id':'A070-stage1-independent-scope-reconstruction',
 'method':'Normalized singleton and bounded-L4 relaxation controls; exact Boolean point-flip stability; independent heat/granularity/occupancy proof reconstruction; Kraft hybrid and explicit addressing lower bound',
 'mathematical_delta':'Five imported v1 claims independently accepted at scope; hybrid partition bound reconstructed; three-reference expected-cost/I >= log2(a/2)/40 on actual Boolean point-flipped addressing; full FEI OPEN; original cyclic certificate not recovered',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_PENDING_SUPERVISOR_COPY',
 'mathematical_status':'SCOPED_REVIEWS_ACCEPTED_LOCAL_HYBRID_NOGO_PROVED_UNREVIEWED_FULL_FEI_OPEN_CYCLIC_REPLAY_GAP',
 'claim_versions_used':used,'claims_created_or_changed':[{'claim_id':x['claim_id'],'version':x['version'],'change':'local independent review' if x is not new else 'proof-complete independent reconstruction pending review'} for x in claims],
 'source_artifacts':['REPORT.md','DERIVATION.md','ANALYTIC_SCOPE_AUDIT.md','RELAXATION_CONTROL_RESULTS.json','FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':['A066','A067','A069','A088','A094','B14','B20'],
 'next_action':'Prove complete full-support fixed-prior queue-reference cost on point-flipped addressing, paying new tail atoms; separately recover Addendum 11.51 original cyclic law for source-bound replay',
 'stagnant_substantive_attempts':0,
 'blockers':[{'scope':'cyclic certificate replay only','reason':'Full Addendum 11.51 not in packaged twelve source notes; both read-only recall queries returned unrelated hits; Boolean hybrid proof has no dependency on this missing source'}],
 'packet_ids':['A070']}
write(run/'PROGRESS.json',progress); write(run/'PACKET_DELTA.json',progress)
controls={
 'singleton':{'domain':'normalized real; not Boolean','H_bits':'log2 n','spectral_degree':'1','L4_fourth_moment':'3-2/n','dyadic_amplitude_subfamily':'n=4^m','phase_impossibility':'two-coordinate signed convolution has magnitude 2/n for every phase choice','Boolean_theorem_refuted':False},
 'A066':{'identity':'ACCEPT_AT_SCOPE','Boolean_input':'none in identity; even Walsh numerator in dimension-specific endpoint bound','singleton_payment':'FAILS_OUTSIDE_BOOLEAN_DOMAIN','perturbation':'STABLE','universal_integrated_payment':'OPEN_FEI_EQUIVALENT'},
 'A067':{'local_theorem':'ACCEPT_AT_SCOPE','Boolean_input':'integer-valued 2^(|S|-1)D_S f','singleton_arithmetic':'HYPOTHESIS_FAILS','perturbation':'U=N Var-I diverges','raw_and_all_anchor_nogos':'ACCEPT_AT_SCOPE'},
 'hybrid':{'partition_inequality':'PROVED_WITH_BRANCH_AND_EMPTY_CHARGES','Boolean_input':'arithmetic bound validity only','three_reference_payment':'REFUTED_WITH_ACTUAL_BOOLEAN_FAMILY','lower_bound':'cost/I>=log2(a/2)/40 for a>=8','queue_augmented_payment':'NOT_REFUTED_NOT_PROVED'},
 'A068':{'review_scope':'STRUCTURAL_SCOPE_ONLY_NOT_FULL_ACCEPTANCE','Boolean_input':'regular ternary pivotal antichain and quadratic sign phase','perturbation':'GENERIC_EDIT_NOT_PROVED_TO_STAY_IN_CLASS'},
 'A069':{'claim':'ACCEPT_AT_SCOPE_FULL_V1','decoder_Boolean_input':'none','payment_Boolean_input':'paid recursive-majority occupancy and physical edit influence comparison','perturbation':'STABLE','constants':[12,25]},
 'cyclic':{'status':'SOURCE_NOT_RECOVERED_NO_REPLAY_CLAIM','plan_locators':[273,'302-308'],'limitation':'Generic probability-law identities/codes add no admission excluding known non-Boolean cyclic laws'},
 'exact_validation':json.loads((run/'out/CHECK.json').read_text(encoding='utf-8'))}
write(run/'RELAXATION_CONTROL_RESULTS.json',controls)
sources=json.loads((agent/'source_read_receipts.json').read_text(encoding='utf-8'))
paths=[Path(x['path']) for x in sources]
paths += [campaign/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json']]
paths += [team/'BOARD.md',team/'claude/B14/STREAM_NOTES.md']
for who,folder in imports:
    paths += list((team/'agents'/who/'runs'/folder).glob('DERIVATION.md'))
    paths += list((team/'agents'/who/'runs'/folder).glob('REPORT.md'))
    paths += list((team/'agents'/who/'runs'/folder).glob('CLAIMS.json'))
paths += list((team/'agents/A068/runs').rglob('REPORT.md'))
manifest=[]
for p in dict.fromkeys(paths):
    raw=p.read_bytes()
    try: raw.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: raw.decode('cp1252'); enc='cp1252'
    manifest.append({'path':str(p),'bytes':len(raw),'sha256':digest(raw),'decoded_encoding':enc,'scope':'Background full-load and targeted consultation; actual proof scope is recorded in REPORT.md'})
write(run/'out/SOURCE_MANIFEST.json',manifest)
write(run/'out/BRAIN_RECALL_RECEIPT.json',{'queries':[{'command':'python -X utf8 ~\\.claude\\dreaming\\brain.py recall "FEI cyclic label law Addendum 11.51 fixed atom cap prefix non Boolean"','exit_code':0,'outcome':'No relevant cyclic certificate; eight hits mostly unrelated or older FEI statements'},{'command':'PYTHONPATH=src; python -X utf8 -m math_brain.cli recall local/population/brain.sqlite3 "FEI cyclic signed lifetime Addendum 11.51 atom cap" --limit 5','workdir':'~\\math-brain-build','exit_code':0,'hit_titles':['rooted nae connector compatibility 38e','more finite low corank endpoints do not bridge','Cyclic Group','Ray-Chaudhuri-Wilson Theorem','A deterministic unit normal can have a Rademacher atom'],'outcome':'No original Addendum 11.51 recovered'}],'brain_mutation':False})
shutil.copy2(agent/'read_sources.py',run/'code/read_sources.py')
fields=protocol['required_per_run']
assert all(set(c)==set(fields['claim_fields']) for c in claims)
progress_keys={x.split(' (',1)[0] for x in fields['progress_fields']}
assert set(progress)==progress_keys
assert all(sh(c)==c['statement_sha256'] for c in claims)
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
report=(run/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+h in report for h in fields['report_fields'])
assert '**Universal bridge:**' in report.splitlines()[-1]
write(run/'out/SCHEMA_CHECK.json',{'status':'PASS','claim_count':len(claims),'independently_reviewed':5,'new_pending':1,'claim_fields_exact':True,'progress_fields_exact':True,'progress_field_descriptor_normalization':'packet_ids (one primary ID, for compatibility) is the canonical packet_ids key per protocol compatibility.run_delta','report_fields_present':True,'compatibility_bytes_identical':True,'statement_hashes_checked':True})
(agent/'STATUS.md').write_text('STATE: A070 local scope audit complete: five v1 claims independently accepted; hybrid addressing no-go proved; 31,381 exact checks PASS; full FEI OPEN; cyclic replay source missing.\nNEXT: A088/A094 review hybrid; prove full-support fixed-prior queue payment on point-flipped addressing with tail cost; recover cyclic Addendum 11.51 separately.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('2026-10-12: Completed independent A066/A067/A069 reconstructions and exact two-control audit. Check.py PASS: 31,381 exact assertions, 299 target cases plus three addressing-base transforms, 29.43s. Hybrid/three-reference addressing lower bound proved analytically for every a>=8; five existing v1 claims accepted locally without repair. Both read-only Brain recalls failed to recover cyclic Addendum 11.51; replay not claimed. Required schemas, hashes and local persistence checked; copying/adoption pending.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('- A069 complete v1 independently reconstructed: Gamma(g_d)<=6I(g_d)-3; edits satisfy Gamma(f)<=12I(f)-6+48N rho-16rho. Thus constants 12 for N rho<=1/8 and 25 for every one-point edit follow without a new assumption.\n')
files=list(run.rglob('*'))+[agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md']
receipts=[]
for p in files:
    if not p.is_file() or p.name=='PERSISTENCE.json':continue
    raw=p.read_bytes(); assert len(raw)<20_000_000
    receipts.append({'path':str(p),'bytes':len(raw),'sha256':digest(raw)})
write(run/'out/PERSISTENCE.json',{'status':'LOCALLY_SAVED','supervisor_copy_verified':False,'brain_or_github_mirror_verified':False,'files':receipts})
print(json.dumps({'status':'PASS','claims':len(claims),'reviews':5,'files_receipted':len(receipts),'run':str(run)}))
