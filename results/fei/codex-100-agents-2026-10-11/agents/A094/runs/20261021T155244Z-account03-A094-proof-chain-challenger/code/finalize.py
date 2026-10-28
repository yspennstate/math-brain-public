from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1]; OWN=RUN.parents[1]
BASE=Path(r'~\brain_workers\FEI100_20261011')
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(name,obj):
    (RUN/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
g=[(1-2*(x&7==0))*(1-2*(x>>3==0)) for x in range(32)]
a=[F(sum(g[x]*(-1)**((x&t).bit_count()) for x in range(32)),32) for t in range(32)]
assert Counter(a)=={F(3,8):1,F(-3,8):3,F(-1,8):7,F(1,8):21}
# Formal coefficients (constant, coefficient of log2(3)).
ell=[(F(6),F(-2) if abs(x)==F(3,8) else F(0)) for x in a]
cc=tuple(sum(x*x*y[j] for x,y in zip(a,ell)) for j in [0,1])
aa=tuple(sum(x*y[j] for x,y in zip(a,ell)) for j in [0,1])
bb=tuple(sum(y[j] for y in ell) for j in [0,1])
assert cc==(F(6),F(-9,8));assert aa==(F(6),F(3,2));assert bb==(F(192),F(-8))
assert 3**2>2**3
assert F(2,3)+F(2,81)>F(2,3) # first two positive atanh terms for ln2
small=json.loads((RUN/'out/SMALL_RESULTS.json').read_text(encoding='utf-8'))
critical=json.loads((RUN/'out/CRITICAL_RESULTS.json').read_text(encoding='utf-8'))
pilot=json.loads((RUN/'out/PILOT_RESULTS.json').read_text(encoding='utf-8'))
classified=[]
for row in critical['rows']:
    m=row['m'];d=F(1,2**(m+5)); Iroot=F(7,4)+d*(m-4)
    rootmargin=[F(x) for x in row['root_rate6_margin_interval']]
    rootce=[6*Iroot-rootmargin[1],6*Iroot-rootmargin[0]]
    rate4=[F(x)-2*F(row['remaining_I']) for x in row['rate6_terminal_margin_interval']]
    assert rootce[1]<F(301,64);assert rate4[0]>F(3,64)
    classified.append({'m':m,'history':row['policy'],'coarse_admission':row['coarse_admission'],
                       'root_CE_interval':[str(x) for x in rootce],
                       'terminal_rate4_margin_interval':[str(x) for x in rate4]})
save('out/PROFILE_CERTIFICATE.json',{'status':'PASS','coefficient_method':'direct integer character sums, independent of FWHT checker',
    'coefficient_counts':{str(k):v for k,v in Counter(a).items()},'source_cost_formal':list(map(str,cc)),
    'signed_linear_profile_formal':list(map(str,aa)),'quadratic_profile_formal':list(map(str,bb)),
    'all_padding_root_CE_upper':'301/64','all_padding_terminal_I_lower':'19/16',
    'all_padding_rate4_terminal_surplus_lower':'3/64','finite_crosschecks':classified,
    'histories_outside_coarse_admission':sum(not r['coarse_admission'] for r in classified)})
lean=json.loads((RUN/'out/LEAN_RECEIPT.json').read_text(encoding='utf-8')) if (RUN/'out/LEAN_RECEIPT.json').exists() else {'result':{'status':'NOT_RUN'}}
save('out/EXACT_RESULTS.json',{'status':'PASS','histories':small['histories']+critical['histories'],
    'assertions':small['assertions']+critical['assertions'],'pilot_assertions_not_added_twice':pilot['assertions'],
    'small_seconds':small['seconds'],'critical_seconds':critical['seconds'],'lean_status':lean['result']['status'],
    'scope':'Small domain exact physical path and reference likelihood identities; pilot and critical information intervals. All-m result uses separate analytic proof, not finite extrapolation.'})
src=[BASE/'BOARD.md',BASE/'claude/B19/STREAM_NOTES.md',
    BASE/'agents/A086/runs/20261014T093519Z-account05-A086-joint-code-referee/REPORT.md',
    BASE/'agents/A086/runs/20261014T093519Z-account05-A086-joint-code-referee/RECONSTRUCTION.md',
    BASE/'agents/A086/runs/20261014T093519Z-account05-A086-joint-code-referee/CLAIMS.json',
    BASE/'agents/A011/runs/20261014T074949Z-account05-A011-representation-existence/GENERAL_ENVELOPE.md',
    BASE/'agents/A095/runs/20261014T074829Z-account05-A095-restricted-result-extraction/REPORT.md',
    BASE/'agents/A095/runs/20261014T074829Z-account05-A095-restricted-result-extraction/DERIVATION.md',
    BASE/'agents/A095/runs/20261014T074829Z-account05-A095-restricted-result-extraction/CLAIMS.json',
    BASE/'agents/A095/runs/20261014T034647Z-account05-A095-restricted-result-extraction/DERIVATION.md',
    BASE/'agents/A094/runs/20261014T061347Z-account05-A094-proof-chain-challenger/REPORT.md']
campaign=Path(r'math-open-problems/reports\fei-2026-10-11')
src +=[campaign/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
supp=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
src +=[supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
# Read the source notes as read-only intake; no theorem from them is blanket accepted.
src +=list((supp/'sources').glob('*.md'))+list((BASE/'context').glob('*.txt'))
receipts=[]
for p in src:
    data=p.read_bytes()
    encoding='cp1252' if p.suffix=='.txt' else 'utf-8'
    text=data.decode(encoding)
    receipts.append({'path':str(p),'sha256':sha(p),'bytes':len(data),'encoding':encoding,
                     'scope':'source chain read' if 'DERIVATION' in p.name or 'RECONSTRUCTION' in p.name else 'campaign/context intake; not blanket proof acceptance'})
save('out/SOURCE_RECEIPTS.json',receipts)
statement1='For every Boolean core g on k>=1 bits with prescribed normalized finite-cost reference R positive on its true Fourier support, every m>=0 and edited full vertex, carry the A095 support-completed reference through any finite adaptive tree querying only original core coordinates. The exact point-path debit is Pi_M=Pi_g+delta(t_a-2j_a), and E I_leaf=I(g)-Pi_g+delta[k+m+1-t_a-2j_rem]. With K>=4,K>K0>=0,c<=K0 I(g), nonconstant g and beta=Pi_g/I(g), the admission 2^-m[(5/4)K0+kK+(3-K)/2]<=K-K0-K beta implies E CE_leaf<=K E I_leaf for the same inherited references. Complete independent terminal CE and KL remain additive. Constant cores use a separate point-defect argument. This is a scoped independent reconstruction of A095 support-completion/history clauses, not acceptance of its other rank, collision or activation clauses.'
statement2='For every integer m>=0, let g=(1-2 AND_3)(1-2 AND_2) on five disjoint core bits, append m dummies, flip the all-zero full vertex under a fresh fair selector, and use the A095 support-completed reference with source R=P_g. After either the first width-three coordinate query, or that query followed by a second width-three coordinate query only on its zero branch, the same incoming root CE is at most301/64 and average remaining physical influence at least19/16. Therefore the complete inherited mean leaf cost obeys 4 E I_leaf-E CE_leaf>=3/64, without padding admission, a reset, rate inflation or bank renewal. Any independent prescribed terminal retains its full additive CE and KL outside the core bank. This fixed-core all-padding statement does not assert universal FEI.'
def claim(cid,statement,status,proof,dependencies,reviews):
    return {'claim_id':cid,'version':1,'exact_statement':statement,
        'hypotheses':['finite uniform Boolean cubes; ideal bits; actual physical restrictions and original reaches',
                      'prescribed complete normalized references positive on true support; zero-fiber reference mass retained',
                      'independent terminal coordinates unqueried with product-compatible posteriors; no bank renewal'],
        'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A094/account03; source history and support-completion attributed to A095'],
        'proof_source':str(RUN/proof),'proof_dependencies':dependencies,'review_records':reviews,'status':status,
        'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A086','A095','A097','A039','A096','B19','B20']}
claims=[claim('A094-SCOPED-ADAPTIVE-HISTORY-ADMISSION-AUDIT',statement1,'INDEPENDENTLY_RECONSTRUCTED_AT_EXPLICIT_SCOPE',
    'AUDIT.md',[{'claim_id':'A095-RANK-KL-EQUIVALENCE','version':5,'scope':'support-completed root and finite original-core-query history clauses only'}],
    [{'reviewer':'A094/account03','verdict':'HOLDS_AT_SUPPORT_COMPLETION_AND_FINITE_HISTORY_SCOPE','substantive_repair_supplied':False,
      'independence':'new character/edge/reference implementation; generic reference transport originated in an earlier A094 dependency and is reconstructed rather than counted as new independent review'}]),
    claim('A094-SIGNED-PROFILE-WEAK-HISTORY-RATE4',statement2,'AUTHOR_PROOF_WITH_EXACT_CERTIFICATE_REVIEW_PENDING',
    'PROFILE_CERTIFICATE.md',[{'claim_id':'A094-SCOPED-ADAPTIVE-HISTORY-ADMISSION-AUDIT','version':1,'scope':'actual support-completed reference, physical path debit, nonnegative release and terminal product'}],[])]
save('CLAIMS.json',claims)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B19','packet_id':'A094',
    'gap_id':'C024-SAME-INCOMING-REFERENCE-FIXED-RATE-BANK','attempt_id':'A094-stage16-signed-profile-history',
    'method':'Full dependency reconstruction; independent exact physical history and likelihood audit; signed old-sector coefficient proof',
    'mathematical_delta':'Scoped A095 all-core adaptive history independently reconstructed. For h3*h2 first/two weak core queries, signed profile pays SAME incoming root and full inherited terminals at rate4 for every padding m>=0, surplus>=3/64. Universal constant improvement zero.',
    'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_HISTORY_HOLDS; NEW_NARROW_PROOF_REVIEW_PENDING; FULL_FEI_OPEN',
    'claim_versions_used':[{'claim_id':'A095-RANK-KL-EQUIVALENCE','version':5,'scope':'support completion and finite core-query history'},
                           {'claim_id':'A011-POINT-EDIT-GENERAL-ENVELOPE-ONE-USE-HISTORY','version':1,'scope':'general envelope reconstructed via A086; no repeated-rate inference'}],
    'claims_created_or_changed':[x['claim_id'] for x in claims],
    'source_artifacts':['out/SOURCE_RECEIPTS.json','AUDIT.md','PROFILE_CERTIFICATE.md','out/EXACT_RESULTS.json','out/PROFILE_CERTIFICATE.json','out/LEAN_RECEIPT.json'],
    'next_consumers':['A086','A095','A097','A039','B19','B20'],
    'next_action':'A086/A095 independently review signed profile rate4 theorem; replace its fixed-core signed log profile by an influence-controlled arbitrary-core profile through the next inherited query, retaining complete terminals and original bank.',
    'stagnant_substantive_attempts':0,'blockers':['No universal influence-priced supplied source or fixed-rate arbitrary-core signed profile; external adoption/mirror not verified; checklist working update encountered lock timeout'],
    'packet_ids':['A094']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
status='STATE: Stage16 saved: A095 scoped history HOLDS; same-reference h3*h2 weak histories paid at rate4 for ALL padding m>=0, surplus>=3/64;812 histories/93651 exact checks PASS; full FEI OPEN.\nNEXT: A086/A095 review signed-profile proof; pay arbitrary inherited positive profile from SAME unused original bank with both terminal references and erased edges retained.\n'
(OWN/'STATUS.md').write_text(status,encoding='utf-8')
for name,entry in [('WORKLOG.md',f'\n{NOW} — Stage16: reconstructed A086 general envelope and complete A095 support/history dependency. Main800 and critical12 histories passed93651 assertions; pilot16/352 is a subset, not added twice. Direct coefficient profile proves all-padding rate4 weak-history payment with surplus3/64. Lean tail status: {lean["result"]["status"]}. No shared-source changes, external writes, GPU or detached jobs.\n'),
                   ('LEARNED.md','\nStage16 durable facts: timestamp-only .final files are not proof artifacts; use substantive preserved runs. For h3*h2 at zero, coefficient counts are 1(+3/8),3(-3/8),7(-1/8),21(+1/8); signed log profile sum a ell=6+(3/2)log2(3)>0. The negative linear edit term pays both weak histories at rate4 for every dummy padding m, original CE<=301/64 and remaining mean I>=19/16. This removes the coarse padding/rate increase only for this profile, not for arbitrary cores. Keep signed source costs: the granularity envelope loses this cancellation.\n')]:
    with (OWN/name).open('a',encoding='utf-8') as f:f.write(entry)
print(json.dumps({'saved':True,'histories':812,'assertions':93651,'lean':lean['result']['status']}))
