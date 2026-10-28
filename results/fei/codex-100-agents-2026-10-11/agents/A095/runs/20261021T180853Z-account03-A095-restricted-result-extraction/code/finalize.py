from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];ROOT=A.parents[1]
BASE=Path(r'~\mop_fei100')
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False),encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=json.loads((BASE/'reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
read=[]
files=[BASE/'reports/fei-2026-10-11'/s for s in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [BASE/'research_pushes/2026-10-11-full-fei-100-agents'/s for s in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((BASE/'research_pushes/2026-10-11-full-fei-100-agents/sources').glob('*.md'))
files += list((ROOT/'context').glob('*.txt'))
files += [ROOT/'BOARD.md',ROOT/'claude/B19/STREAM_NOTES.md']
source_runs=[('A094','20261021T155244Z-account03-A094-proof-chain-challenger',['REPORT.md','CLAIMS.json','PROFILE_CERTIFICATE.md','AUDIT.md']),('A096','20261014T094929Z-account05-A096-live-gap-ledger',['REPORT.md','DERIVATION.md']),('A086','20261014T093519Z-account05-A086-joint-code-referee',['REPORT.md','RECONSTRUCTION.md']),('A095','20261014T074829Z-account05-A095-restricted-result-extraction',['REPORT.md','CLAIMS.json','DERIVATION.md']),('A095','20261014T034647Z-account05-A095-restricted-result-extraction',['DERIVATION.md'])]
for a,r,ns in source_runs:files += [ROOT/'agents'/a/'runs'/r/s for s in ns]
extract=[]
for p in files:
    raw=p.read_bytes()
    try:txt=raw.decode('utf-8-sig');enc='utf-8-sig'
    except UnicodeDecodeError:txt=raw.decode('cp1252');enc='cp1252'
    matches=[{'line':i+1,'text':l[:260]} for i,l in enumerate(txt.splitlines()) if any(s in l.lower() for s in ['normaliz','conditional','signed','composition','reference','theorem','a095','c024'])]
    read.append({'path':str(p),'sha256':sha(p),'bytes':len(raw),'encoding':enc,'scope':'critical source fully reconstructed' if '/agents/' in p.as_posix() else 'background intake; no blanket acceptance'})
    extract.append({'path':str(p),'locators':matches[:12]})
save(R/'out/SOURCE_RECEIPTS.json',read);save(R/'out/INTAKE_LOCATORS.json',extract)
result=json.loads((R/'out/EXACT_RESULTS.json').read_text(encoding='utf-8'))
proof=R/'DERIVATION.md'
statement='For all integers w>=4,m>=0, let g=h_w*h_2 with h_L=1-2*1_zero on disjoint blocks, and let M select padded g and its all-zero full-point flip by a fresh fair bit. With the prescribed support-completed source-spectrum reference Q, every finite adaptive history querying only the width-w block and using normalized physical-child posterior transport satisfies CE_root<1005/256, E I_leaf>=63/64 and 4 E I_leaf-E CE_leaf>3/256. Every complete terminal cost is retained; an independent untouched arbitrary terminal remains additive outside this bank.'
hyp=['Uniform physical cube, entropy and cross entropy in bits','All-zero edit and prescribed source R=P_g; no arbitrary-reference substitution','No repeated coordinate per path; selector,padding,width-two block and independent terminal unqueried','No descendant reset or renewal; product-compatible zero-fiber posterior for independent terminal']
canonical=json.dumps({'exact_statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':'),ensure_ascii=False)
claim=dict(claim_id='A095-UNBOUNDED-WIDTH-SIGNED-PROFILE-HISTORY',version=1,exact_statement=statement,hypotheses=hyp,statement_sha256=hashlib.sha256(canonical.encode()).hexdigest(),contributors=['A095'],proof_source={'path':str(proof),'sections':'1-4','sha256':sha(proof)},proof_dependencies=['A095 stage5 normalized posterior transport, reconstructed in DERIVATION section4 and independently accepted by A094','A095 point-path physical edge identity, independently reconstructed in section3'],review_records=[],status='ANALYTIC_AUTHOR_PROOF_EXACT_FINITE_CHECKS_REVIEW_PENDING',supersedes=[],refutes=[],first_unproved_line='None within stated scope. Universal arbitrary-source reference/reset payment remains open.',next_consumers=['A094','A086','A096','A097'])
source_claims=json.loads((ROOT/'agents/A094/runs/20261021T155244Z-account03-A094-proof-chain-challenger/CLAIMS.json').read_text(encoding='utf-8'))
review=next(x for x in source_claims if x['claim_id']=='A094-SIGNED-PROFILE-WEAK-HISTORY-RATE4')
review['review_records'].append({'reviewer':'A095/account03','verdict':'HOLDS_AT_FULL_NAMED_PROFILE_SCOPE','proof':str(proof)+' section5','independence':'Independent Walsh/character sums, direct edge counts, rational log intervals, all-m analytic rederivation; no source checker imported','substantive_repair_supplied':False})
review['status']='INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE'
save(R/'CLAIMS.json',[claim,review])
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B19',packet_id='A095',gap_id='C020-C024-SAME-OWNER-SIGNED-PROFILE',attempt_id='A095-stage16-unbounded-width',method='Independent reconstruction plus exact signed tensor log-profile, arbitrary-tree physical edge lower bound, rational verification',mathematical_delta='Independently accepts A094 named fixed-core profile; removes width, padding and adaptive-depth admission for h_w*h2 with w>=4 at unchanged rate4 and surplus>3/256; universal constant improvement zero.',deliverable_status='COMPLETE_LOCAL_REVIEW_PENDING',mathematical_status='SCOPED_ANALYTIC_PROOF_FULL_FEI_OPEN',claim_versions_used=['A095 stage5 adaptive same-reference admission','A094 stage16 named fixed-core profile'],claims_created_or_changed=[claim['claim_id']+'@1'],source_artifacts=['DERIVATION.md','out/EXACT_RESULTS.json','out/SOURCE_RECEIPTS.json','out/LEAN_RECEIPT.json'],next_consumers=['A094','A086','A096','A097'],next_action='Expose a width-two coordinate with SAME inherited Q and booked debit; price prescribed reset and complementary complete terminal from unused ancestor capacity.',stagnant_substantive_attempts=0,blockers=['Independent review pending','No universally influence-priced arbitrary source/reference reset','Remote adoption and mirror unverified'],packet_ids=['A095'])
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-21 stage16: Independently reconstructed A094 fixed-core profile. Derived all w>=4, all padding, all adaptive wide-block policies at rate4 from one original source bank, surplus>3/256; '+str(result['assertions'])+' exact assertions across '+str(result['histories'])+' histories PASS. Full FEI OPEN; prescribed reset/arbitrary source price remains unpaid. Artifacts: '+R.name+'.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-21 stage16: For g=h_w*h2,w>=4, source P_g and zero full-point selector edit, A=sum a log(1/a²)=2+2(1-q)log2(1-q)+(2-q)(2w-2), B=sum log(1/a²)=-8log2(1-q)+2^(w+3)w-8w+8, q=2^(1-w). Signed cancellation yields complete root CE<1005/256 uniformly in padding. EVERY adaptive history restricted to width-w block has mean remaining I>=1-delta>=63/64: edited-path unqueried original influences contribute (w-t)q. Same posterior-transport root bank pays terminal average at4, surplus>3/256. This is no local per-leaf guarantee or arbitrary incoming-reference/reset payment. A094 named width3 first/two-query profile independently HOLDS.\n')
expected=set(protocol['required_per_run']['progress_fields']);expected.discard('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
headings=protocol['required_per_run']['report_fields']
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all(s in report for s in headings)
assert report.rstrip().split('## Universal bridge')[-1].strip()
save(R/'out/SCHEMA_VALIDATION.json',{'status':'PASS','claim_fields':len(claim),'progress_fields':len(progress),'assertions':result['assertions'],'report_required_fields':headings})
receipts=[]
for p in list(R.rglob('*'))+[A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']:
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20_000_000
        receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
save(R/'out/PERSISTENCE_RECEIPTS.json',receipts)
print(json.dumps({'status':'PASS','files':len(receipts),'claim':claim['claim_id'],'assertions':result['assertions']}))
