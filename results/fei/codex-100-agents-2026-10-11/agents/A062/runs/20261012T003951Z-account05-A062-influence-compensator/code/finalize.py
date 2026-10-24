from pathlib import Path
import hashlib,json

run=Path(__file__).resolve().parents[1]
agent=run.parents[1]
root=Path(r'~\brain_workers\FEI100_20261011')
registry=Path(r'~\mop_fei100\reports\fei-2026-10-11')
protocol=json.loads((registry/'EXECUTION_PROTOCOL.json').read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,value): (run/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
sources=[(root/'BOARD.md','stage-start board snapshot 2026-10-12 00:39 UTC'),
 (root/'claude/B13/STREAM_NOTES.md','v2 target, prior-interface review and Q* convention'),
 (registry/'EXECUTION_PROTOCOL.json','revision 2026-10-11-execution-v2, full text'),
 (agent/'runs/20261011T220423Z-account05-A062-influence-compensator/CLAIMS.json','prior A062 v1 interface'),
 (agent/'runs/20261011T220423Z-account05-A062-influence-compensator/FAIR_TREE_INFLUENCE_PROCESS.tex','finite budgets used without re-derivation'),
 (root/'agents/A064/LEARNED.md','frontier and sign/no-go distinctions'),
 (root/'agents/A089/LEARNED.md','empty-core coefficient shifts in all control fibers'),
 (root/'agents/A064/runs/20261011T224431Z-account05-A064-global-debt-potential/GLOBAL_DEBT_POTENTIAL.tex','complete source; positive reserve bound not used as premise'),
 (root/'agents/A064/runs/20261011T224431Z-account05-A064-global-debt-potential/POTENTIAL_OBSTRUCTION_TESTS.md','physical-minority no-go independently reconstructed'),
 (root/'agents/A064/runs/20261011T224431Z-account05-A064-global-debt-potential/CLAIMS.json','v1 scope and dependency pins'),
 (root/'claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich/code/b05_trees.py','actual selector-first query order and Bellman recursion'),
 (Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents\sources\ERASURE_REDUCTION.md'),'section 2 uniform singleton JS bound, read in prior stage'),
 (registry/'runs/B05/20261011T193057Z-account01-B05-rare-restrictions/REPORT.md','section 4 analytic packet asymptotic, read in prior stage')]
write('out/SOURCES.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':scope} for p,scope in sources])
consumers=['A064','A065','A087','A094','A097','A099','B13','B20']
statement=('For every even k>=4, r>=2k, and C>=6, let F be the canonical quadratic bent k-bit function and its zero-vertex point flip, activated by r fresh point controls and selected by a fair physical selector. On the complete selector-controls-adjacent-data-pairs tree with irrelevant inputs skipped and constant leaves, the minimal nonnegative reserve Q*_v=[D_v-C Inf_v+average Q*_children]_+ vanishes at every control node and even point-edited paired-data entry. Odd edited data states have Q*<=2. For physical minority mu(g)=min(P[g=-1],P[g=+1]), every node obeys Q*_v<=4mu(g_v)log2(1/mu(g_v)); at the root Q*=[D_selector-C 2^{-(r+k)}]_+<4*2^{-k}mu(F)log2(1/mu(F))<=mu(F)log2(1/mu(F))/4 and Q*<=2^{1-k}I(F). At r=2k and fixed finite C, Q*/I(F) is asymptotic to (2/5)2^{-k}. In particular the C=6 reserve certificate gives H(F)<=(6+2^{1-k})I(F)<=49I(F)/8. Pointwise credit domination is not a local drift assertion for the rarity function, which remains false on these selector roots for fixed coefficients.')
hyp=['Actual Boolean signs on uniform finite cubes; entropy in bits; ordinary total influence',
 'Canonical b_k=(-1)^(x1*x2+...+x_{k-1}*x_k), flipped only at zero; k even >=4',
 'r fresh point controls with r>=2k; independent fair physical selector',
 'Complete fresh-input order selector then controls then adjacent data pairs; skip irrelevant coordinates; zero constant leaves',
 'Physical output minority, not spectral minority-fiber mass; psi(0)=0',
 'Fixed finite C>=6 for the stated asymptotic; larger finite C allowed for inequalities']
claim={'claim_id':'A062-B05-MINIMAL-RESERVE-CREDIT','version':1,'exact_statement':statement,
 'hypotheses':hyp,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['A062; target and Bellman convention from B13 lead; local-rarity obstruction credited to A064; empty-fiber correction credited to A089'],
 'proof_source':{'path':'DERIVATION.md','certificate':'out/CERTIFICATES.json','full_tree_oracle':'out/TREE_ORACLE.json'},
 'proof_dependencies':[{'claim_id':'A062-INFLUENCE-STOPPING-INTERFACE','version':1,
    'scope':'finite same-tree budgets only','review_status':'B13 lead v2 records both prior A062 claims checked and holding'},
   {'source':str(sources[-2][0]),'sha256':sha(sources[-2][0]),'scope':'section 2 singleton JS scalar bound'}],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':[],'first_unproved_line':None,'next_consumers':consumers}
write('CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B13','packet_id':'A062',
 'gap_id':'G-R-MISMATCH','attempt_id':'A062-Qstar-isoperimetric-1',
 'method':'complete Bellman reserve state classification; adjacent-pair ownership; isoperimetric root credit; rational logarithm intervals',
 'mathematical_delta':'All-k canonical B05 selector-first Q* credited at C>=6; control/even reserves zero; root Q*/I<=2^{1-k}, asymptotic (2/5)2^{-k}; physical rarity local-drift no-go preserved.',
 'deliverable_status':'COMPLETE_LOCAL_REVIEW_PENDING','mathematical_status':'SCOPED_LEAD_TARGET_PROVED_LOCAL; UNIVERSAL_C019_AND_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A062-INFLUENCE-STOPPING-INTERFACE','version':1,'scope':'finite budgets'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','DERIVATION.md','REVIEW_NOTE.md','out/CERTIFICATES.json','out/TREE_ORACLE.json','out/SOURCES.json','out/PILOT_FAILURE.md'],
 'next_consumers':consumers,
 'next_action':'Flip b_k at both zero and e_1+e_3; derive the first paired-node ownership correction when both children retain edits under the same physical rule, with exact child reserves and initial influence retained.',
 'stagnant_substantive_attempts':0,
 'blockers':['Independent review and supervisor mirror/adoption pending; Bellman-stable reserve on incompatible edits and arbitrary sources unproved.'],
 'packet_ids':['A062']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
write('out/REVIEW_SCOPE.json',{'reviewer':'A062','source_claim_id':'A064-TERMINAL-CORRECTED-GLOBAL-DEBT','version':1,
 'scope':'physical output minority psi local-drift no-go clause only','verdict':'HOLDS_AT_STATED_SCOPE',
 'proof':'REVIEW_NOTE.md','whole_bundled_claim_accepted':False})
cert=json.loads((run/'out/CERTIFICATES.json').read_text());oracle=json.loads((run/'out/TREE_ORACLE.json').read_text())
assert cert['assertions']==259 and oracle['assertions']==136
assert cert['failures']==oracle['failures']==0
assert cert['runtime_seconds']<60 and oracle['runtime_seconds']<60
required=protocol['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in required['progress_fields']}
assert set(claim)==set(required['claim_fields'])
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
report=(run/'REPORT.md').read_text()
for field in required['report_fields']: assert '## '+field in report
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
assert len((agent/'STATUS.md').read_text().splitlines())==2
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        assert p.stat().st_size<20_000_000
        receipts.append({'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=agent/name
    receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
write('out/RECEIPTS.json',{'run_id':run.name,'local_persistence_verified':True,'schema_checks_passed':True,
 'independent_review':'PENDING','mirror_verified':False,'files':receipts})
print(json.dumps({'schema_checks_passed':True,'exact_assertions':395,'local_claims':1,
 'scope':'all even k>=4,r>=2k,C>=6 on canonical complete selector-first tree','full_fei':'OPEN',
 'receipted_files':len(receipts)},indent=2))
