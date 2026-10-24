"""Protocol metadata and local receipts; saved-certificate checks only."""
import copy,json,hashlib
from pathlib import Path
from fractions import Fraction as Q
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1];TEAM=ROOT.parents[1]
PREV=ROOT/'runs/20261013T223305Z-account05-A023-amortized-rarity-budget'
P=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
SRC21=TEAM/'agents/A021/runs/20261014T011316Z-account05-A021-rare-core-asymptotics'
SRC25=TEAM/'agents/A025/runs/20261014T002956Z-account05-A025-rare-event-counterfamily'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def receipt(p):
    raw=p.read_bytes();return {'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
protocol=read(P);validation=read(RUN/'out/validation.json')
assert validation['status']=='PASS' and validation['cases']==1039 and validation['checks']==34734
rows=read(RUN/'out/results.json');signs=read(RUN/'out/sign_certificates.json')
assert len(rows)==1039 and len(signs)==386
assert len((RUN/'out/rows.jsonl').read_text(encoding='utf-8').splitlines())==1039
for row in rows:
    alpha=Q(1,1<<row['s']);gamma=Q(row['gamma']);IS=Q(row['selector_I']);IT=Q(row['terminal_I']);R=Q(row['boundary_reserve'])
    assert IS==2*row['s']*alpha*gamma and R<=2*IT and Q(row['minority_mass_sum'])<=IS
for item in signs:
    if item.get('exact_zero'):assert item['sign']==0 and not item['vector']
    else:
        lo,hi=Q(item['lower']),Q(item['upper']);assert lo<=hi
        assert lo>0 if item['sign']==1 else hi<0

consumers=['A021','A025','A027','A028','A029','A064','A087','A094','B05','B20']
old=next(c for c in read(PREV/'CLAIMS.json') if c['claim_id'].startswith('A023-OVERLAP'))
claim=copy.deepcopy(old)
claim.update(version=3,proof_source=str(RUN/'PROOF.md'),review_records=[],
    status='PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',next_consumers=consumers,
    supersedes=[{'claim_id':old['claim_id'],'version':2}],
    proof_dependencies=[{'claim_id':old['claim_id'],'version':2,'source':str(PREV/'REPORT.md'),
        'status':'Single-separator entropy/face scope independently accepted by A021; bundled earlier/KL portions remain pending',
        'role':'Preserve earlier scope only; whole shared-data point-block theorem is independently derived.'}])
claim['exact_statement'] += (
    ' Additional whole-block theorem: for EVERY Boolean G,H on the same uniform data cube, '
    's>=1 fresh point controls, alpha=2^-s, gamma=P(G!=H), F=G+A_s(H-G), '
    'query controls to resolution and stop at actual G or H. Let I_S=2s alpha gamma, '
    'I_T=(1-alpha)I(G)+alpha I(H), H_T=(1-alpha)H(G)+alpha H(H), '
    'R=2alpha(1-alpha)I(GH). Then I(F)=I_S+I_T, R<=2I_T, and '
    'E_B<=2(1-2alpha)I_S+4alpha gamma(1-alpha)[log2(1/gamma)+1/ln2], '
    'with gamma=0 interpreted continuously. H(F)-H_T<=(11/2)I_S+R; '
    'genuine retained minority/KL debt<= (5/2)I_S+R; adding3mu/ln2 gives<=7I_S+R. '
    'Strict scalar-rate slack holds when I_S>0. Each physical data coordinate reserves '
    'at most2alpha times its inactive-terminal influence and2(1-alpha) times its '
    'active-terminal influence, marked once for the whole block and never reissued '
    'at selector descendants. If H(G)<=C_G I(G), H(H)<=C_H I(H), then '
    'H(F)<=max(11/2,C_G+2alpha,C_H+2(1-alpha))I(F). For any bent sign '
    'on even m>=4 bits and its actual one-vertex flip, both multiplied by one '
    'shared independent balancing sign z, the switched family has H<(11/2)I, '
    'retained J+terminal<=4I and full sufficient KL ledger<7I, uniformly in m,s. '
    'Fresh width-t point activation of that balanced family has H<6I and '
    'I=2^-t[I(F)+t]->0 for fixed m,s as t grows. No bound on arbitrary '
    'localized bad-face credit or repeatedly renewed nested terminal reserves is asserted.')
claim['hypotheses']=old['hypotheses']+[
    'Additional whole-block subtheorem allows arbitrary shared-data branches and biases; it requires only fresh independent point controls and complete terminal entropy.',
    'Gamma is the original unthinned branch disagreement throughout each selector block; capacities are marked once and not renewed across failed histories or nested blocks.',
    'Explicit unconditional whole-block family uses two balanced bent/edit branches on the same data cube; activation controls are fresh.'
]
canonical=json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':'))
claim['statement_sha256']=hashlib.sha256(canonical.encode()).hexdigest()
reviewed=copy.deepcopy(read(SRC21/'CLAIMS.json')[0])
reviewed['review_records'].append({'reviewer':'A023','source':str(RUN/'REVIEW_A021.md'),
    'verdict':'HOLDS_UPPER_PRICE_AND_K6_K7_SUFFICIENT_CRITERIA_ONLY',
    'scope':'All-dimensional relative-bias upper point-switch inequality and strict sufficient contrast criteria, reconstructed with separate constant/nonconstant rows.',
    'excluded':'Lower supremum asymptotics, entire overlap application, source computations and whole bundled claim acceptance.',
    'repair_supplied':False})
save(RUN/'CLAIMS.json',[reviewed,claim])
save(RUN/'out/CONSUMED_REVIEW.json',{'claim_id':old['claim_id'],'version':2,
    'source':str(SRC21/'REVIEW_A023.md'),'source_statement_sha256':old['statement_sha256'],
    'verdict':'HOLDS_SINGLE_SEPARATOR_ENTROPY_FACE_SUBTHEOREM_ONLY',
    'excluded':'Earlier biased-core and full KL scope; whole version2 remains pending'})

sources=[P,TEAM/'BOARD.md',TEAM/'claude/B05/STREAM_NOTES.md',
    SRC21/'REPORT.md',SRC21/'DERIVATION.md',SRC21/'CLAIMS.json',SRC21/'REVIEW_A023.md',
    SRC25/'REPORT.md',SRC25/'PROOF.md',PREV/'REPORT.md',PREV/'CLAIMS.json',PREV/'code/check_separator.py']
sources+=sorted((TEAM/'agents/A028/runs').glob('20261013*/REPORT.md'))
save(RUN/'out/source_receipts.json',{'scope':'Exact local source bytes; BOARD and A028 report read scope stated in REPORT, not blanket theorem audit',
    'files':[receipt(p) for p in sources]})
report_path=RUN/'REPORT.md';report=report_path.read_text(encoding='utf-8')
oldsentence='Final counts/runtime are in out/validation.json and inserted into progress metadata directly from executed output.'
report=report.replace(oldsentence,
    'Final PASS: 1,039 cases, 34,734 exact assertions, 386 saved sign certificates, '+str(validation['elapsed_seconds'])+' seconds observed compute time. Counts/runtime are saved in out/validation.json.')
report_path.write_text(report,encoding='utf-8')
artifacts=['REPORT.md','PROOF.md','REVIEW_A021.md','code/check_block.py','code/finalize.py',
    'out/FROZEN_SPEC.json','out/SPEC_UPDATE.json','out/INITIAL_ATTEMPT.json','out/rows.jsonl',
    'out/results.json','out/sign_certificates.json','out/constant_certificates.json','out/validation.json',
    'out/CONSUMED_REVIEW.json','out/source_receipts.json']
progress=dict(protocol_revision=protocol['revision'],run_id=RUN.name,stream='B05',packet_id='A023',
    gap_id='G-R-MISMATCH-FIRST-REVELATION',attempt_id='A023-4-whole-point-block',
    method='Consume already-closed multi-bit overlap; independent upper-price review; exact geometric sum and once-owned terminal-coordinate boundary reserve for arbitrary shared-data point switches',
    mathematical_delta='A021 upper-price/K6/K7 criterion independently HOLDS at stated scope. Whole shared-data point-block prefix pays logarithm once: H-H_T<=(11/2)I_S+2alpha(1-alpha)I(GH), reserve<=2I_T; full bent/edit family H<5.5I and rare activation H<6I with I->0. 1039 cases,34734 exact assertions,386 sign certificates PASS.',
    deliverable_status='COMPLETE_LOCAL_ARTIFACT',
    mathematical_status='SCOPED_WHOLE_BLOCK_PAYMENT_PROVED; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
    claim_versions_used=claim['proof_dependencies'],
    claims_created_or_changed=[{'claim_id':reviewed['claim_id'],'version':1,'change':'Partial independent review record only'},
        {'claim_id':claim['claim_id'],'version':3}],
    source_artifacts=artifacts,next_consumers=consumers,
    next_action='For two nested point selectors sharing actual core coordinates, subtract the first block reserve from conditional terminal capacities and prove remaining-capacity payment or give an exact deficit; retain both source disagreements and every terminal entropy.',
    stagnant_substantive_attempts=0,
    blockers=['No nonreusing terminal-capacity rule for nested shared-data point blocks.',
        'Actual entropy payment does not establish general localized bad-face payment or arbitrary terminal FEI.',
        'New whole-block theorem awaits independent reconstruction; remote adoption unverified.'],packet_ids=['A023'])
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
fields=set(protocol['required_per_run']['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids')
assert set(progress)==fields
for item in read(RUN/'CLAIMS.json'):
    assert set(item)==set(protocol['required_per_run']['claim_fields'])
    canon=json.dumps({'statement':item['exact_statement'],'hypotheses':item['hypotheses']},sort_keys=True,separators=(',',':'))
    assert hashlib.sha256(canon.encode()).hexdigest()==item['statement_sha256']
for title in protocol['required_per_run']['report_fields']:assert '\n# '+title+'\n' in '\n'+report
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()

(ROOT/'STATUS.md').write_text(
    'STATE: A023 stage4 complete: arbitrary shared-data point-block entropy/KL paid from one marked terminal reserve; H<5.5I on bent/edit branches, rare activation H<6I; 34734 exact checks PASS; A021 upper-price scoped HOLDS; new review pending; FEI OPEN.\n'
    'NEXT: Track remaining physical terminal capacity through two nested point selectors sharing core data; A021/A025/A087/A094 review geometric cancellation, reserve fractions and full terminal bounds.\n',encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-14 02:22 UTC stage '+RUN.name+': Read new B05/A021/A025 results; former multi-bit overlap NEXT already done, so consumed their contrast obstruction rather than duplicating it. Independently reconstructed A021 upper price/K6/K7 sufficient criteria, partial review only. Summed whole shared-data point-block erasure exactly; geometric cancellation leaves one logarithmic coefficient4alpha gamma(1-alpha), paid by R=2alpha(1-alpha)I(GH) with named physical terminal capacities. H-H_T<=5.5I_S+R; retained/full KL paid; balanced bent/edit branches have H<5.5I, fresh rare activation H<6I with I->0. Initial frozen pilot hit60-second cap after small pairs; fixed-domain memoized exact rerun passed1039 cases/34734 assertions/386 certificates in16.2711313s. Extended existing claim v3. Nested capacity ownership and localized odd-face payment remain explicitly unproved. Required files and rolling records saved locally.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-14: For arbitrary G,H sharing a data cube and one fresh point block alpha=2^-s, original gamma=P(G!=H) stays fixed through all live histories. Sum of actual erasure costs is <=2(1-2alpha)I_S+4alpha gamma(1-alpha)[log2(1/gamma)+c]. Thus rarity width does not multiply the logarithmic excess: geometric residual-row cancellation is essential. Reserve R=2alpha(1-alpha)I(GH) spends at most2alpha of inactive terminal-coordinate influence and2(1-alpha) of active terminal influence, once for the WHOLE block; all failed histories aggregate to one G account. H-H_T<=5.5I_S+R; genuine J<=2.5I_S+R; full allowance<7I_S+R. Both balanced arbitrary bent/edit branches have H/I<2, giving full H<5.5I; fresh activation gives H<6I at vanishing influence. This does NOT control general Q_bad and does NOT renew terminal slack at nested blocks. A025 already refuted unfiltered per-layer face reservation; A021 already closed all-width three-event overlap at K7. Their precise scopes must be consumed instead of repeated.\n')
allfiles=[p for p in RUN.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20*1024*1024 for p in allfiles)
save(RUN/'out/artifact_check.json',{'status':'PASS','cases_checked':1039,'sign_endpoints_checked':386,
    'protocol_fields':'PASS','statement_hashes':'PASS','report_headings':'PASS',
    'compatibility_copy_identical':True,'file_size_limit':'PASS','rolling_status_lines':2,
    'scope':'Local persistence only; new theorem review and remote adoption pending'})
save(RUN/'out/artifact_receipts.json',{'scope':'Local bytes only; no independent review/remote mirror/downstream use receipt',
    'files':[receipt(p) for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='artifact_receipts.json'],
    'rolling':[receipt(ROOT/p) for p in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'status':'PASS','claim_version':3,'cases':1039,'checks':34734,
    'protocol':'PASS','persistence':'SAVED','review':'PENDING_NEW_THEOREM'}))
