"""Write protocol artifacts and verify local persistence, without external publication."""
from pathlib import Path
import json,hashlib,copy
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
BASE=AGENT.parents[1]
SHARED=Path('math-open-problems/reports/fei-2026-10-11')
NOW=datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def dump(p,obj):write(p,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def sha(b):return hashlib.sha256(b).hexdigest()
def receipt(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())}
protocol=read(SHARED/'EXECUTION_PROTOCOL.json')
source=BASE/'agents/A039/runs/20261023T032407Z-account03-A039-projection-under-restrictions'
peer=read(source/'CLAIMS.json')[0]
assert peer['statement_sha256']=='cb3710e60592cb05b2fcce92557492aaff1201687e45b651fb574401a8a04f40'
assert sha(peer['exact_statement'].encode('utf-8'))==peer['statement_sha256']
main=read(ROOT/'out/CHECK.json');audit=read(ROOT/'out/AUDIT.json');pilot=read(ROOT/'out/PILOT.json')
assert all(v['status']=='PASS' for v in (main,audit,pilot))
assert main['checks']==25378 and audit['checks']==14203
assert main['local_nodes']==2105 and audit['prime_log_equalities']==144
total=main['checks']+audit['checks']
review=copy.deepcopy(peer)
review['review_records'].append({'reviewer':'A040','verdict':'HOLDS_AT_COMPLETE_STATED_SCOPE_WITHOUT_SOURCE_REPAIR','reviewed_at':NOW,'repair_supplied':False,'source':str(ROOT/'REVIEW_A039.md'),'method':'Independent spectator-sector proof, own Fraction/FWHT reference transport, separate direct character sums and144 exact prime-log equalities. Full source/paired-surplus derivation reconstructed analytically.'})
review['status']='INDEPENDENT_REVIEW_HOLDS_BY_A040_LOCAL_RECORD'
statement=('For disjoint finite uniform Boolean v(V),u(U), epsilon=+/-1, G=epsilon on x0 and vu on x1, let q_v,q_u have the same support and empty masses as their actual spectra, with zero/zero likelihood1. Start the complete normalized coherent lift R=P_G*(q_v/p_v)*(q_u/p_u), and define comparison B=P_G*(q_v/p_v). For ANY finite adaptive physical stopping tree querying only V and making no intermediate reset, same actual coherent-kernel transport preserves R_h=B_h*(q_u/p_u), including equal own outcome normalizers for R and B. At any selected terminal leaves reset only v_h to a matched-empty same-support reference q_h_new, keeping q_u fixed. The COMPLETE signed change is exactly sum pi_h[D(p_vh||q_h_new)/2-D(P_h||B_h)]. For a signed width-w>=2 point v and four-fifths matched-empty targets (exact laws for constants/characters), this is at most Var(v)*log2(5/4)/2<1/8, for arbitrary factor stopping. Consequently in the ORIGINAL seven-eighths point-tensor priority source F_h of A039@1, after b, arbitrary fresh-data prefix, selected a exposure with BOTH children actually reset to five-sixths factor lifts, one may run such an arbitrary finite one-chosen-factor stopping tree on any subset of those already reset children and make the four-fifths factor-only final resets. Keeping both prior/source costs, every complementary/full terminal, all signed query credits and any supplied old0<=omega<=1/4, the SAME account S-[A0+e+sigma1+sigma2]_+-omega>11/16, with sigma2<1/16. No query of another factor before that final reset, repeated-reset cumulative bound, unpriced old-reference conversion, arbitrary-core supplier price or universal FEI constant is asserted.')
claim={'claim_id':'A040-COHERENT-FIXED-SPECTATOR-STOPPING-RESET','version':1,'exact_statement':statement,'hypotheses':['Uniform physical cube; bit entropy and KL; actual Boolean signs and independent queried/spectator blocks.','Local entry laws normalized, same support and empty masses as actual factor spectra; fair kernel extension at source-zero rows.','Only the chosen V block is queried until its declared final reset; arbitrary finite adaptive orders and stopping, with every complementary leaf retained.','Root application uses exactly the ORIGINAL seven-eighths correlated supplier, then actually exercised five-sixths first reset; old omega is supplied and charged once.','No relabelled fresh owner, repeated variance allowance, omitted terminal reference, spectator refresh or free old-source conversion.'],'statement_sha256':sha(statement.encode('utf-8')),'contributors':['A040'],'proof_source':[str(ROOT/'PROOF.md'),str(ROOT/'code/check.py'),str(ROOT/'code/audit.py'),str(ROOT/'out/CHECK.json'),str(ROOT/'out/AUDIT.json')],'proof_dependencies':[{'claim_id':peer['claim_id'],'version':peer['version'],'statement_sha256':peer['statement_sha256'],'status':'FULL_STATED_SOURCE_RECONSTRUCTED_AND_INDEPENDENTLY_HOLDS_BY_A040','scope':'Original paid source/first reset and paired-surplus interface; all required inputs reconstructed in PROOF sections4-5.'}],'review_records':[{'reviewer':'A040','kind':'author analytic proof plus separate exact implementation','verdict':'PASS; external independent review pending','exact_checks':total}],'status':'AUTHOR_PROVED_EXACT_CERTIFICATES_EXTERNAL_REVIEW_PENDING','supersedes':[],'refutes':['Every inherited comparison B_h has the same spectator likelihood-group masses as the physical P_h. Exact witness: G_+(point2*point2), query first V bit=0; likelihood1 group P=5/8 but B=3871/6016.'],'first_unproved_line':'None inside stated local/root scope. Universal gap: paid arbitrary-core initial supplier; history gap: second-block query before the factor reset or amortized multiple conversions from the same diminished owner.','next_consumers':['A039','A036','A037','A046','A050','A088','A092','A094','A096','A097','B08','B20']}
dump(ROOT/'CLAIMS.json',[review,claim])
next_action='Price one interposed SECOND-block physical query BEFORE the chosen-factor final reset, carrying SAME original source, first reset, old quarter, actual inherited Q and both complete terminal bills; A039/A050 supply and A088/A094 independently review.'
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B08','packet_id':'A040','gap_id':'G-R-MISMATCH','attempt_id':'A040-stage8-fixed-spectator-arbitrary-stopping','method':'Independent source review; complete spectral-sector invariance; finite conditional variance; signed same-owner identity; exact rational certificates and independent prime-log reconstruction.','mathematical_delta':'A039 one-query theorem independently HOLDS; one chosen factor now permits arbitrary finite adaptive data stopping before its factor-only final reset at SAME global sigma2<1/16 and SAME >11/16 remaining. General Boolean local KL identity is proved under matched-empty factor hypotheses. False auxiliary marginal-equality assertion explicitly refuted.','deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_ANALYTIC_LEMMA_PROVED; FULL_FEI_OPEN; NEW_EXTERNAL_REVIEW_PENDING','claim_versions_used':[peer['claim_id']+'@'+str(peer['version'])],'claims_created_or_changed':[peer['claim_id']+'@'+str(peer['version']),claim['claim_id']+'@1'],'source_artifacts':['PROOF.md','REVIEW_A039.md','out/FROZEN_SPEC.json','out/PRE_MAIN_AMENDMENT.json','out/AUDIT_SPEC.json','out/CHECK.json','out/AUDIT.json','out/VALIDATION_REPAIRS.json'],'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Arbitrary-core initial correlated price is unpaid, not supplied by this point-tensor application.','Interposed second-block histories and cumulative repeated reset ownership need new proof.','New A040 theorem awaits external review; remote copying/adoption unverified.','Brain personal-context self-care degraded/unverified; stale notes excluded from mathematics.'],'packet_ids':['A040']}
closure=ROOT/'out/CHECKLIST_CLOSURE.json'
if closure.exists():
    progress['blockers'].append('Shared checklist completion failed: RuntimeError(checklist lock held too long); local research artifacts are complete. No lock repair or retry launched.')
dump(ROOT/'PROGRESS.json',progress);write(ROOT/'PACKET_DELTA.json',(ROOT/'PROGRESS.json').read_text(encoding='utf-8'))
reviewtext=f'''# Independent A040 review: HOLDS

Source: {source}. Claim {peer['claim_id']}@{peer['version']}, exact statement SHA256 {peer['statement_sha256']}. The statement is retained unchanged in CLAIMS.json; no source repair was supplied. This verdict covers its entire declared one-query and same-original-source scope, not an arbitrary FEI reference.

PROOF sections1-4 reconstruct the full likelihood/normalizer identity and the original seven-eighths source, five-sixths first reset, signed paired surplus and old-quarter payment. In one query the source identity's positive outcome term remains essential. Sector invariance shows R and comparison B have equal own outcome normalizers; the negative erasure term plus positive outcome term is exactly minus the mean inherited comparison KL. This also gives a stronger stopping-tree extension, claimed separately with A040 as contributor; it is not a repair required for source acceptance.

Independent tests: {main['checks']} primary exact assertions on2105 ordered local histories/24 full root policies; {audit['checks']} separate assertions on1104 local histories,144 exact prime-log identities and154 saved terminal laws including37 constants. The second implementation imports no author/peer helper and uses direct character sums. Ten complete root-policy reset nodes have rigorously positive second reset charge. Finite tests corroborate; the unbounded quantifiers follow from the explicit finite-tree sector/variance proof.

The failed auxiliary assertion P_h and B_h share spectator marginals belongs to A040's initial pilot and was removed without changing the reviewed source statement. Exact witness P=5/8 and B=3871/6016 appears in VALIDATION_REPAIRS and PILOT. Neither the failed assertion nor a failed run is counted as passing evidence. Full FEI, arbitrary-core admission and post-reset cumulative bills remain open.
'''
write(ROOT/'REVIEW_A039.md',reviewtext)
report=f'''# exact target, quantifiers, hypotheses and units

A040/B08 stage8 consumes the now-paid A039 coherent a-child interface instead of repeating the retired census or product-reference barrier. The target is ANY finite adaptive stopping tree within ONE chosen point factor after the first actually exercised reset. Keep the SAME ORIGINAL seven-eighths correlated source, first five-sixths reset, old omega<=1/4, both a outcomes, all complementary/full terminals and all signed query credit. Prove sigma2<1/16 and remaining>11/16 without a per-depth budget. A general Boolean local KL identity is proved under matched-empty same-support factor hypotheses. Uniform physical bits encode the uniform sign cube; all entropy/KL units are bits. Full FEI OPEN.

# sources actually read, revisions and theorem locators

Current BOARD header2026-10-23 04:15UTC and B08 section, B08 STREAM_NOTES v2(Oct11), own STATUS and previous stage7 arithmetic/proof frontier. Full execution protocol revision {protocol['revision']} remains the schema baseline; current user campaign endpoint2026-10-23 14:49UTC supersedes its legacy date. Machine-wide AGENTS was consulted; this resumed stage uses the earlier complete campaign/registry/plan/supplement and four context-paper intake as prior-stage baseline, with no new paper premise or literature-priority claim. No brain/personal note is a theorem premise.

Primary pinned source: A03920261023T032407Z REPORT/PROOF/CLAIMS, especially PROOF1-4 and claim@1 hash{peer['statement_sha256']}. Also consulted A05020261022T232833Z PROOF1-5 and A04620261023T002101Z REPORT/PROOF/CLAIMS to consume the correlated-source supplier and current history exclusions. An initial dynamic-latest A050 read hit a newly created incomplete next run; it failed and was replaced by the explicitly pinned completed source. This is recorded in SOURCE_READ_REPAIR. No conclusion rests on the missing file. Byte source receipts are local identities, not mirror/acceptance receipts.

the owner was told at stage start that brain self-care is degraded/unverified: owner-model and state-of-mind sources were90.3/74.9hours old. Those personal-context notes were not used for mathematics. The signed project-contract hook also reports stale/unresolved state; this stage performs only reversible owned research-file writes, with no publication or irreversible action.

# complete derivation or exact first unsupported line

PROOF.md contains the complete proof. For G_epsilon(vu), put R=P*l_v*s_u and B=P*l_v. A query inside v has a coherent kernel independent of the nonempty spectator frequency. Because q_u(empty)=p_u(empty), R and B have exactly equal reference-outcome normalizers, and the entire stopping tree preserves R_h=B_h*s_u. Consequently D(P_h||R_h)=D(P_h||B_h)+D(p_u||q_u)/2. Subtracting the full fresh law gives the exact reset identity sigma=sum_selected pi_h[D(p_vh||q_new)/2-D(P_h||B_h)]. This retains all positive outcome-normalizer corrections inside the final comparison KL. B is an analytic comparison, not a new physical reset or new bank.

For a signed point factor the fresh term is <=Var(v_h)log2(5/4)/2. Finite stopping-partition variance contraction and Var(point_w)<=3/4 give sigma<1/8 locally, by exact5^3<2*4^3. Eligible a-child reaches total<=1/2, so sigma2<1/16 globally. The separately reconstructed original price and first actual reset give M0-sigma1>1. Both a outcomes' bias contributions cancel under their arbitrary respective stopping trees, so actual COMPLETE S>=1. Thus S-[A0+e+sigma1+sigma2]_+-omega>11/16 for the SAME supplied old omega<=1/4. The previous11/16 number is unchanged because the new invariant removes dependence on query count; only the allowed history scope increases.

The first unsupported universal line is a useful paid correlated initial price for an arbitrary Boolean core. Locally, switching to another factor BEFORE this final reset breaks fixed-spectator invariance. After a completed matched-empty reset relabelling a new block is structurally allowed, but the sum of later actual reset bills is not paid by this theorem. No arbitrary earlier debit, repeated fresh allowance or unpriced incoming conversion is approved.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs precede every executed domain. From this run:

    python -X utf8 -B code/check.py --pilot
    python -X utf8 -B code/check.py
    python -X utf8 -B code/audit.py

Final pilot PASS:171 assertions,13 local histories/one full root policy,{pilot['runtime_seconds']:.6f}s. Main PASS:25378 assertions,2105 ordered local histories and24 complete root policies,{main['runtime_seconds']:.6f}s. Local widths2,3 x constant/point2/character1/point2*character1 spectators x both epsilon/core signs, plus width4/point2 positive signs; all ordered restriction prefixes, no quotient. Root(m,r)=(1,2),(2,2),(1,3), prefix none/one, final policies zero-length/one query/stop-at-zero/full chosen-factor exposure. Physical dimension<=7; domains never auto-raised. Ten actual second-reset nodes are rigorously positive. Every final probability/reference law is stored, including complementary constant terminals.

Main arithmetic: exact integer FWHT/Fraction transport, exact likelihood/normalizer equalities; rigorous36-term positive atanh logarithms with geometric tail and outward2^-120 rounding. Independent audit PASS:14203 assertions,1104 direct-character local histories,144 EXACT prime-log identities,154 complete terminal spectra including37 constants,{audit['runtime_seconds']:.6f}s; imports no primary/foreign helper. Combined final exact count39581 excludes pilot and both failed drafts. The analytic finite-tree argument proves all-width/all-history scope independently of these finite cases.

VALIDATION_REPAIRS preserves the rejected initial auxiliary marginal-equality assertion (exact P group5/8 versus B3871/6016), its corrected proportional-sector invariant, and a subsequent missing fmt serializer error after the pilot arithmetic. Both are repaired; no failed run is counted. The pre-main helper hash is frozen after the final PASS pilot; audit source has its own pre-execution hash. No floating sign or interval-overlap equality is accepted.

All jobs estimated100MB with55s runtime cap, below the300MB memok trigger. No heavy search, GPU, compiler, new worker, detached process, automatic dimension increase or deletion. No Lean attempt or formal verification is claimed. Compute state read near finalization showed1770MB free and5458MB live commit headroom; this is a later snapshot than earlier advisory figures, not an unexplained revision. No work was stopped or throttled to free resources.

# proof dependencies and changed downstream conclusions

The unchanged A039 claim@1 independently HOLDS at its full stated scope without source repair; the local review record is copied into CLAIMS. Its root/first-reset inputs are rederived here rather than accepted through an opaque dependency. The new A040 theorem is author-proved, with separate arithmetic corroboration; external peer acceptance remains pending. No A046 new theorem, arbitrary-core supplier, general FEI or dependency cycle is assumed. No universal FEI constant improves. A039/A036/A037/A046/A050 can now consume a whole chosen-factor stopping tree without issuing a per-query normalization allowance.

# one next mathematical action and independent reviewer

{next_action} This consumes the current history bottleneck; it does not repeat the already refuted product-reference admission or an unchanged class entropy calculation. A092 should challenge full-terminal/source ownership; A039/A050 should compare the exact supplier and retained first reset. No messages were sent, and named consumption/review is not claimed to have happened.

# actual persistence receipts or precise save blocker

The four required protocol files, full proof/review, frozen specs, both self-contained checkers, immediate outputs, exact pilot counterexample and validation repairs are saved inside this assigned run. Rolling STATUS has two lines; dated WORKLOG/LEARNED are appended. Finalization reads back exact protocol key sets and statement hashes, byte-identical progress/delta, PASS outputs and source/helper pins, then records local file hashes/bytes with every artifact<20MB. Supervisor private-copy, brain ingestion, remote mirror, registry adoption, downstream use and new-claim external review remain unverified. No git, mail, peer messages, other-agent research writes or brain-store changes were made. Nothing launched by this stage remains running after verification.

## Universal bridge

This advances C024 history transfer and C019 stopping-tree payment from one coherent post-reset data query to ANY finite adaptive stopping tree inside one chosen factor, with the SAME original source, first reset, old quarter, full terminals and unchanged>11/16 margin. The local fixed-spectator identity is general Boolean, but its terminal price and arbitrary-core initial supplier remain unpaid; the universal FEI constant improves by zero. NEXT exposes a second block before the final reset while preserving this diminished owner, because removing that remaining history-separation hypothesis is the shortest direct test of composition toward a universal stopping proof rather than another isolated tensor entropy result.
'''
if closure.exists():
    report=report.replace('\n## Universal bridge\n','\nRuntime checklist status: the required working acknowledgment exited0, but the completion acknowledgment exited1 with RuntimeError("checklist lock held too long"). The blocker is the shared checklist lock, not research persistence. All three command sessions were polled to exit; nothing remains running. No shared-lock repair or repeated status job was launched. See out/CHECKLIST_CLOSURE.json.\n\n## Universal bridge\n')
write(ROOT/'REPORT.md',report)
state='STATE: A040 stage8 saved: A039 coherent reset v1 independently HOLDS; arbitrary chosen-factor stopping retains SAME >11/16;39581 exact checks PASS; new review pending; FEI OPEN.\n'
nextline='NEXT: Price second-block query BEFORE first-factor final reset with SAME original source, exercised sigma1, old quarter and both full terminals; A039/A050 supply, A088/A094 review. No source/variance renewal.\n'
write(AGENT/'STATUS.md',state+nextline)
marker=ROOT.name
for name,entry in [('WORKLOG.md',f'\n{NOW} [{marker}] Independently reconstructed A039@1 HOLDS. Proved arbitrary chosen-factor stopping identity with unchanged sigma2<1/16 and >11/16 old-quarter margin. Main25378+audit14203=39581 exact assertions PASS; audit144 prime-log identities/154 terminal laws. Preserved false auxiliary marginal assertion and missing serializer failures; final domains unchanged. Full FEI and interposed second-block payment remain open.\n'),('LEARNED.md',f'\n{NOW} [{marker}] Fixed-spectator law R=P*l_v*s_u survives ANY physical V-only stopping tree as R_h=B_h*s_u, B=P*l_v carried with its own normalizers. Thus factor-only final reset sigma=E_selected[D(p_vh||q_new)/2-D(P_h||B_h)], retaining spectator and outcome costs. B_h need not have P_h spectator marginal (5/8 vs3871/6016 exact counterexample); proportional nonempty sector suffices. Point stopping variance yields SAME global sigma2<1/16 and SAME >11/16 after original first reset/old quarter. Switching blocks before the reset, repeated-conversion amortization and arbitrary-core admission remain unpaid.\n')]:
    prior=(AGENT/name).read_text(encoding='utf-8')
    if marker not in prior:write(AGENT/name,prior+entry)
for c in (review,claim):
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    assert sha(c['exact_statement'].encode('utf-8'))==c['statement_sha256']
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for heading in protocol['required_per_run']['report_fields']:assert '# '+heading in report
assert len(report.split('## Universal bridge\n')[-1].strip().split('\n\n'))==1
amend=read(ROOT/'out/PRE_MAIN_AMENDMENT.json');audspec=read(ROOT/'out/AUDIT_SPEC.json')
assert amend['check_sha256']==sha((ROOT/'code/check.py').read_bytes())
assert amend['arithmetic_sha256']==sha((ROOT/'code/arithmetic.py').read_bytes())
assert audspec['helper_sha256']==sha((ROOT/'code/audit.py').read_bytes())
sources=[SHARED/'EXECUTION_PROTOCOL.json',BASE/'BOARD.md',BASE/'claude/B08/STREAM_NOTES.md']
sources += [source/n for n in ('REPORT.md','PROOF.md','CLAIMS.json')]
for agent,stamp in [('A050','20261022T232833Z-account03-A050-repair-with-scope'),('A046','20261023T002101Z-account03-A046-current-candidate-intake')]:
    sources += [BASE/'agents'/agent/'runs'/stamp/'PROOF.md']
dump(ROOT/'out/SOURCE_RECEIPTS.json',{'meaning':'Byte identities at finalization; not mirror acceptance or downstream use.','sources':[receipt(p) for p in sources]})
dest=ROOT/'out/PERSISTENCE_RECEIPTS.json';files=sorted(p for p in ROOT.rglob('*') if p.is_file() and p!=dest)
assert all(p.stat().st_size<20*1024*1024 for p in files)
dump(dest,{'status':'PASS','checked_at_utc':NOW,'exact_checks':total,'claim_count':2,'schema':'exact execution-v2 fields','source_review':'A039@1 HOLDS unchanged','new_external_review':'pending','formal_verification':'NOT_ATTEMPTED','full_fei_status':'OPEN','persistence':'local only','mirror_verified':False,'self_receipt_excluded':True,'files':[receipt(p) for p in files],'rolling':[receipt(AGENT/n) for n in ('STATUS.md','WORKLOG.md','LEARNED.md')]})
print(json.dumps({'status':'PASS','exact_checks':total,'local_files':len(files),'max_bytes':max(p.stat().st_size for p in files),'claims':2,'source_review':'HOLDS','full_fei':'OPEN','receipt':str(dest)}))
