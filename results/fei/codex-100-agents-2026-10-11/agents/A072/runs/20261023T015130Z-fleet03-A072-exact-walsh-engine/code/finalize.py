from pathlib import Path
from fractions import Fraction as F
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1];BASE=AGENT.parents[1]
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def claimhash(s,h):return hashlib.sha256(json.dumps({'exact_statement':s,'hypotheses':h},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest()

v=load(RUN/'out/VALIDATION.json');data=load(RUN/'out/HULL_CASES.json');scalar=load(RUN/'out/SCALAR_VALIDATION.json');integers=load(RUN/'out/INTEGER_VALIDATION.json');lean=load(RUN/'out/LEAN_RECEIPT.json')
assert len(v['orbits'])==2 and v['financial_policies']==6
assert all(x['verdict']=='SAME_INHERITED_CREDIT_SUFFICES_FOR_ALL_POLICIES' and x['gap']==[0,0] for x in v['orbits'])
assert len(data['query_rows'])==70 and len(data['financial_policies'])==6
assert sum(x['labelled_restrictions'] for x in v['coverage'])==1458
assert sum(x['labelled_query_rows'] for x in v['coverage'])==2916
assert scalar['allocation_cases']==636 and scalar['hull_cases']==512 and integers['compressed_full_profiles']==24
Q=1<<192;A=v['orbits'][0]['initial_credit'];assert F(A[0],Q)>F(2857328,10**8) and F(A[1],Q)<F(2857329,10**8)

source=BASE/'agents/A071/runs/20261023T003633Z-fleet03-A071-search-space-design'
sourceclaim=next(c for c in load(source/'CLAIMS.json') if c['claim_id']=='A071-INHERITED-SUBSIDY-NO-RENEWAL')
sourcecopy=json.loads(json.dumps(sourceclaim));source_declared=sourcecopy['statement_sha256']
statement_only=hashlib.sha256(sourcecopy['exact_statement'].encode('utf-8')).hexdigest();canonical=claimhash(sourcecopy['exact_statement'],sourcecopy['hypotheses'])
save(RUN/'out/HASH_CONVENTION.json',{'local_convention':'sha256 canonical UTF8 JSON {exact_statement,hypotheses}, sorted keys, compact separators','source_declared':source_declared,'source_statement_only':statement_only,'source_canonical_payload':canonical,'source_claims_bytes':digest(source/'CLAIMS.json'),'source_statement_and_hypotheses_copied_unchanged':True})
assert source_declared in [statement_only,canonical]
sourcecopy['statement_sha256']=canonical
sourcecopy['review_records'].append({'reviewer':'A072','decision':'ACCEPT_UNCHANGED','independent':True,'source_declared_statement_sha256':source_declared,'canonical_statement_and_hypotheses_sha256':canonical,'artifact':'PROOF.md source inherited-credit reconstruction; out/VALIDATION.json source_review','scope':'General finite-weight optimizer proof and all source boundaries; seven independent full profiles, nine adaptive rows and actual original credit/debit labels; AND symmetry covers ten next-query alternatives.'})
sourcecopy['status']='INDEPENDENTLY_ACCEPTED_BY_A072_UNCHANGED'

statement=('On a finite uniform physical-query DAG, with full slack S=K I-H, stop allowed, conserved nonnegative inherited credit a, nonnegative total booked debit D=S+a and arbitrary signed debit labels, '
 'the exact minimum initial credit supporting every adaptive allowed-query/stopping policy with zero new transfer flow is R(v)=max((-S(v))_+,max_i mean R(child_i)). '
 'Redistributing credit as R(child)+(a-mean R(child)) and transporting debit labels by a mean-one kernel preserves all labels and zero residuals. '
 'For F_plus=J(-1,+1,g,g,g,g), g negative{0,1,2} in six bits, h negative{0,1,2,4,8,16,32,6,17,40}, J(x)=-h(x xor1), K=4, '
 'and all queries/stops within ANY ONE chosen remaining core, R(root)=-S(F_plus) exactly, in(2857328/100000000,2857329/100000000). '
 'Hence every actual source F_plus leaf with nonnegative booked debit and its existing a=D-S(F_plus) supports this continuation without a new donor draw. '
 'The two core orbits, all1458 labelled restrictions,2916 query rows,24 compressed profiles and six explicit financial policies are certified. '
 'This excludes interleaving queries between different remaining cores and proves no unrestricted FEI bound.')
hypotheses=['full Fourier entropy in bits, uniform physical cube, original K=4 in the Boolean application','both complete physical children retained, even when the queried inner core becomes constant','credit is nonnegative and may be redistributed with conserved conditional mean; all outside donor balances/outgoing flows fixed','total booked debit nonnegative and zero residual S+a=D; individual ancestor/query debit labels may be signed','allowed queries in the Boolean application remain in one chosen core; other full cores unchanged','positive and zero denominator cases in label transport handled separately; stopping allowed at every state']
cid='A072-OTHER-CORE-STOPPING-CREDIT-HULL'
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':claimhash(statement,hypotheses),'contributors':['A072'],
 'proof_source':['PROOF.md','code/credit_hull.py','out/HULL_CASES.json','out/VALIDATION.json','out/SCALAR_VALIDATION.json','out/INTEGER_SECTORS.json','out/FLAT12_WALSH.json'],
 'proof_dependencies':['A071-INHERITED-SUBSIDY-NO-RENEWAL@1 independently accepted unchanged here, explicit inherited credit convention','integer character orthogonality, physical pivotal edge identity and occupied-block entropy chain rule, independently reconstructed','finite Bellman induction and finite conditional-mean conservation; no universal child-positivity assumption'],
 'review_records':[{'reviewer':'A072 separate constructions','decision':'INTERNAL_EXACT_CERTIFICATE_AND_PROOF_RECONSTRUCTION','independent':False},{'reviewer':'A074/A092','decision':'PENDING','independent':True}],
 'status':'AUTHOR_PROOF_AND_EXACT_FINITE_CERTIFICATES_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Replacing the conserved future credit by only current negative-part slack, on four actual intermediate Boolean profiles; no source theorem is attributed this proposed stronger rule.'],
 'first_unproved_line':'The full physical stopping-credit hull admits a dimension-independent R_4(f)<=L I(f), or a second remaining-core continuation fits the actual diminished inherited account; neither follows from the one-core certificate.',
 'next_consumers':['A071','A074','A075','A089','A092']}
save(RUN/'CLAIMS.json',[sourcecopy,claim])

proof=(RUN/'PROOF.md').read_text(encoding='utf-8')
proof=proof.replace('Four explicit first/last-active-coordinate financial policies','Six explicit financial policies (four first/last-active-coordinate policies from zero-debit source leaves and two from the actual earlier positive-debit source leaf)')
proof=proof.replace('# Checks that could fail','The compressed full-Walsh check writes each occupied-sector coefficient as c_T times the product of nonempty inner coefficients. If d_j is the gcd of the nonempty integer inner Walsh numerators and N_j its truth-table length, every full integer Walsh coefficient in sector T is a multiple of N c_T product_(j in T)(d_j/N_j). Every such base is checked integral; constant-core occupied sectors are exactly zero. Exact sector Parseval gives the full integer square sum N^2, and composing the checked inner and outer inverses proves sign-valued full inversion. Independent outer pivotal probabilities times direct inner edges give integral full edge counts for every physical coordinate. The actual boundary with paired core3=-1 ignores core5 pointwise and reduces to12 relevant physical bits: all4096 integer Walsh entries, full integer Parseval, inverse and12 direct edge counts are explicitly checked and saved. Dummy padding only multiplies Walsh numerators by its truth-table size and does not alter entropy or influence.\n\n# Checks that could fail')
proof=proof.replace('The added a-r is redistributed preexisting credit, not new donor income.','The added a-r is redistributed preexisting credit, not new donor income. If the credit has several nonnegative owner labels summing to a>0, use the separate mean-one kernel a_child/a to conserve each credit label; when a=0 all such labels vanish. The actual source here has one already spent original credit owner.')
(RUN/'PROOF.md').write_text(proof,encoding='utf-8')

progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B15','packet_id':'A072','gap_id':'C019-INHERITED-COMPONENT-ELIGIBILITY','attempt_id':'A072-stage18-other-core-credit-hull-v1',
 'method':'Exact inherited-credit Bellman hull, all adaptive one-core restrictions, two independent spectrum constructions, integer sector certificate and flat12-bit Walsh verification.',
 'mathematical_delta':'A071 inherited-subsidy theorem independently accepted unchanged. One additional non-flat core, of either physical outer type, can be revealed/stopped in every adaptive way using SAME existing subsidy; exact minimum equals -S(F_plus), new donor flow0. Covers source leaves with zero or positive booked debit.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'CONDITIONAL_ALL_POLICY_ACCOUNT_PROOF_AND_EXACT_FINITE_CERTIFICATE; FULL_FEI_OPEN',
 'claim_versions_used':['A071-INHERITED-SUBSIDY-NO-RENEWAL@1 independently accepted here','A089-SIGNED-TERMINAL-COMMON-KERNEL-REPAIR@1 accepted by A071, explicit source account only','A072-SATURATED-DONOR-OPTIMALITY@1 accepted by A074, context'],
 'claims_created_or_changed':['A071-INHERITED-SUBSIDY-NO-RENEWAL@1 local independent review',cid+'@1'],
 'source_artifacts':['PROOF.md','FROZEN_SPEC.json','SCALAR_SPEC.json','INTEGER_SPEC.json','out/VALIDATION.json','out/HULL_CASES.json','out/SCALAR_VALIDATION.json','out/INTEGER_VALIDATION.json','out/FLAT12_WALSH.json','out/HASH_CONVENTION.json','out/SOURCE_RECEIPTS.json','out/INSTANT_CREDIT_OBSTRUCTION.json'],
 'next_consumers':['A071','A074','A075','A089','A092'],
 'next_action':'Expose a SECOND remaining core in one saved terminal carrying the actual redistributed credit and signed old labels; compute the joint two-core hull or derive a signed-row invariant. Keep original donor outgoing A and all stopped siblings/parked2tau fixed. A074/A092 independently review current all-policy criterion and integer certificates.',
 'stagnant_substantive_attempts':0,'blockers':['No dimension-independent bound on the full stopping-credit hull; this bound is equivalent to full FEI.','Independent review of new theorem and remote persistence unverified.','Lean supporting-identity status is limited to the saved admission receipt; full Bellman theorem not Lean-certified.'],'packet_ids':['A072']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)

report=f'''# exact target, quantifiers, hypotheses and units

The SAME inherited credit pays every adaptive reveal/stopping policy within one additional remaining core of the negative F_plus terminal. Both core types have exact minimum credit R=-S(F_plus), strictly between2857328/10^8 and2857329/10^8 bits. No fresh donor flow is required. This is an author proof plus exact finite certificates, pending independent review; full FEI remains OPEN.

Use g negative on{{0,1,2}} in six bits; h negative on{{0,1,2,4,8,16,32,6,17,40}}; J(x)=-h(x xor1); F_plus=J(-1,+1,g,g,g,g). Keep K=4, all uniform physical inputs and all other complete cores. A071's last-query stopped source leaves have credit -S(F_plus), debit0 and original reaches1/1024 or1/2048. Its earlier stopped leaves have positive debit D and actual credit D-S(F_plus); they also satisfy the new criterion. The latter case is explicitly tested using the real early source leaf at reach1/128. Original donor expenditure, donor booked balance, other source terminals and parked2tau stay fixed.

# sources actually read, revisions and theorem locators

BOARD2026-10-23 01:52 UTC, B15 leadv2, own STATUS and prior stage17, A07420261022T225155Z review, A08920261022T225420Z report, and A07120261023T003633Z report/claims/adaptive/subsidy source were read. A074 accepts the prior A072 optimizer unchanged. A089 refutes the proposed child-positivity extension; it is not revived here. The old lead's f5/f6 engine task is already closed, so protocol dispatch consumes this new signed-account dependency. The current owner deadline supersedes older protocol dates. Campaign/paper intake remains prior background, with no new literature theorem as a premise.

A071-INHERITED-SUBSIDY-NO-RENEWAL@1 is independently ACCEPTED unchanged. PROOF.md reconstructs its general finite-weight optimum max(0,N-A), including zero denominators. Seven full source profiles and all nine adaptive rows are independently rebuilt; AND symmetry covers its ten labelled next alternatives. Its raw statement/hypotheses and source byte hashes are pinned; HASH_CONVENTION.json records the source digest and canonical local statement-plus-hypotheses digest. Source code is read, never executed in another agent's folder. All imported helpers are pinned local copies of A072's preceding run. No brain card is a mathematical premise.

# complete derivation or exact first unsupported line

For S=K I-H, supplied credit a>=0 and nonnegative total debit D=S+a, define R(v)=max((-S(v))_+,max_allowed-query mean R(child)). This is the exact minimum credit supporting every allowed adaptive stopping policy with zero new flow. Necessity follows from the stop option and conserved mean child credit. For sufficiency allocate a_child=R(child)+(a-mean R(child)), d_child=S(child)+a_child. Child credits/debits are nonnegative, mean credit stays a, and mean debit is D+e by physical influence telescoping. Signed debit labels use d_child/T when T>0; T=0 forces both debits0 and permits kernel1. Each original credit owner is separately conserved. All residuals remain0. PROOF.md supplies every boundary and the finite induction.

The hull also equals the maximum expected negative terminal slack over allowed stopping policies, giving an attaining lower-bound policy. For ALL physical coordinates on ALL Boolean functions, R_K(f)<=L I(f) is equivalent to FEI(K+L): stop immediately for one direction; apply terminal FEI and E I_terminal<=I_root for the other. This identifies the universal unpaid bill rather than solving it. The actual finite calculation restricts queries to ONE chosen remaining core; no interleaving with a second core is covered.

The fixed outer table has two physical core orbits{{2,4}} and{{3,5}}, checked literally. Each queried core reduces by pointwise dummy deletion to twelve profiles. All3^6 labelled restrictions and every remaining-coordinate query are checked against this reduction. The exact root log profiles satisfy R=-S symbolically, not by interval tolerance. Therefore any source stopped F_plus leaf with D>=0 has enough already supplied a=D-S for all such policies, including its nonzero old labels. The other full terminal entropies remain present even when the queried core becomes constant.

Four intermediate Boolean profiles strictly require more future credit than their current negative slack: exact attaining stopping policies and excesses are in INSTANT_CREDIT_OBSTRUCTION.json. The actual inherited allocation funds these requirements; a greedy reset to current deficit would erase required credit.

First unsupported universal line: derive a dimension-independent bound on the full physical stopping-credit hull, or pay the next SECOND-core query using the actual conditional credit and old labels left in the saved terminal. A new incoming subsidy cannot be named after the original donor has already paid it.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC, its recorded financial amendment, SCALAR_SPEC and INTEGER_SPEC precede their jobs. The full domain has1458 labelled restrictions and2916 labelled query rows, represented by24 full profiles and70 query rows; no unjustified affine quotient or automatic dimension increase occurs. Six actual financial policy trees include four zero-debit source cases and two positive-debit source cases. They retain original coordinate labels, both full outcomes, all signed old/new labels and true reach weights; conditional mean conservation composes by finite iterated expectation.

Final credit_hull.py runs in{v['runtime_seconds']:.3f}s with{v['exact_checks']} recorded checks and{v['engine_checks']} pinned-engine checks;29 distinct full states have independent spectrum reconstructions. The636 scalar allocation cases exercise all source optimizer regimes with independent attaining-witness enumeration. Another512 need assignments compare the hull with all4608 explicit two-bit adaptive stopping-policy payoffs. boundary.py records{scalar['exact_checks']} checks in{scalar['runtime_seconds']:.3f}s. These account cases are not Boolean counterexamples and do not replace the algebraic continuum proof.

integer_certificate.py checks all24 full spectra in compressed integer form and a literal12-bit boundary with4096 integer Walsh entries. Each sector coefficient is the outer centered coefficient times inner nonempty coefficients; gcd bases certify integrality of every full Walsh numerator without materializing the24-bit array. Sector Parseval, composed sign inversion and independent full edge counts are exact. The flat boundary additionally checks full integer Parseval, inverse and12 direct coordinate edge counts before entropy comparison. It records{integers['integer_checks']} checks in{integers['runtime_seconds']:.3f}s. Exact masses/physical influences agree between the centered-Taylor and separate product-moment paths. Strict signs use Fraction/integer arithmetic and192-bit outward atanh bounds; no floating sign or equality tolerance is used.

Commands from A072 use python -B -X utf8 runs/{RUN.name}/code/: credit_hull.py --pilot, credit_hull.py, boundary.py, integer_certificate.py, finalize.py. The v1 first full outputs are retained under FIRST_*; v1.1 adds actual positive-debit source-label transport. Each certificate job is estimated<=120MB and bounded55s; the separately admitted supporting Lean attempt returns RUNTIME_UNVERIFIED after122.8s, with translation fidelity also unverified. No expected>300MB certificate job, GPU, detached worker or new worker is used. The possible Lean compiler job is separately gated by memok.py and lean_check.py admission. Its exact result is in LEAN_RECEIPT.json; the first PowerShell input replaced a Unicode type by?, corrected to ASCII Real and preserved in LEAN_FIRST_RECEIPT.json. No full Bellman or FEI theorem is labelled Lean-checked. Compute snapshots are status ok, with low shared RAM/disk noted; no running work is stopped or throttled.

# proof dependencies and changed downstream conclusions

The source inherited-credit optimizer is independently accepted unchanged at its exact scope. The new result extends its all-adaptive AND-core continuation to a further non-flat three-point core, of either outer type, with zero new donor flow. Exact elementary character orthogonality, pivotal edges, occupied-mask entropy and finite Bellman induction are reconstructed. The source theorem is not used to assume arbitrary child positivity. The new general conditional account theorem and finite Boolean application await A074/A092 review; no universal FEI constant changes.

# one next mathematical action and independent reviewer

Query a SECOND remaining core in one saved full terminal using its actual redistributed credit, signed booked labels and true reach. A joint two-core hull or a signed component-row invariant must pay it without renewing the original donor or dropping stopped full functions. A074/A092 independently review the all-policy quantifier, actual early positive-debit account, dummy/orbit reductions, integer sectors and flat boundary; A071/A089 consume the same-credit extension. Repeating first-row or fixed-order searches would miss the unpaid history-dependent bill.

# actual persistence receipts or precise save blocker

The four protocol files, PROOF.md, frozen specs/amendments, local code, exact certificates, source-review receipts and hash convention are saved inside this A072 run. STATUS has exactly two lines; WORKLOG and LEARNED append the result. MANIFEST binds saved bytes/hashes; SCHEMA_VALIDATION checks exact protocol field sets and identical PROGRESS/PACKET_DELTA. Each file is below20MB. Supervisor copy, remote mirror, brain ingestion and independent acceptance of the new theorem are unverified. No git, mail, messaging, other-agent write, deletion or trading access occurs. Brain self-care remains degraded/unverified: owner-model/state-of-mind notes are88.3/72.9 hours stale; these personal notes are not used as evidence.

# Universal bridge

This stage moves C019 stopping-tree payment through every adaptive reveal/stopping policy in one additional non-flat core of either type, after the source AND core has already been exposed, at exactly zero new funding and with every original donor expenditure and old label retained. The sharp supplied-credit threshold is the negative-slack stopping hull; a dimension-independent bound on the FULL hull is precisely the unpaid FEI bridge. NEXT exposes a second remaining core with the actual conditional account, so it attacks the missing history-sensitive admission mechanism rather than another isolated root class bound.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A072 stage18 saved: SAME credit pays ALL adaptive one-other-core reveals/stops in both types;24 profiles/1458 restrictions/2916 rows;integer+flat12 PASS;FEI OPEN.\nNEXT: Query SECOND remaining core with actual inherited credit/old labels and spent original donor; joint hull or signed-row bound; A074/A092 review,A071/A089 consume.\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
notes={
'WORKLOG.md':f'\n{now} stage18 ({RUN.name}): independently accepted A071 inherited-subsidy theorem unchanged (7 profiles/9 rows); exact Bellman hull for both OTHER-core types equals original -S(F_plus), no new flow for all adaptive queries/stops in one chosen core. 24 profiles,1458 restrictions,2916 rows,6 financial policies incl actual nonzero old debit PASS. {v["exact_checks"]}+{v["engine_checks"]} hull checks;636 scalar cases,512 exhaustive policy cases;24 integer spectrum sectors plus flat12-bit4096-entry Walsh,1558 checks PASS. All artifacts local; universal full hull and second-core continuation remain open.\n',
'LEARNED.md':'\n2026-10-23 stage18: With inherited nonnegative credit a, booked total D=S+a>=0 and conserved conditional credit, the exact all-policy zero-new-flow threshold is R=max((-S)_+,max_query mean R_child). Allocate a_child=R_child+(a-mean R_child), debit=S_child+a_child; all signed debit labels use a mean-one kernel, with T=0 handled separately. Full physical R_K<=L I is equivalent to FEI(K+L), not a new universal estimate. For actual F_plus=J(-1,+1,g^4), both outer core orbits have R=-S(F_plus) in(0.02857328,0.02857329): every adaptive reveal/stop within ANY ONE remaining core needs no new donor flow. This also covers earlier source F_plus leaves with NONZERO D and existing a=D-S; only the LAST source failure has debit0. All other source donor balances and parked2tau remain fixed. 12 canonical inner shapes per orbit cover all labelled restrictions by exact dummy deletion. Compressed integer Walsh integrality follows from N*c_T*product(gcd nonempty inner Walsh/N_j); flat paired-minus boundary has12 relevant bits and checks all4096 integer coefficients. No interleaving with a second remaining core has been certified.\n'}
for name,text in notes.items():
    p=AGENT/name;old=p.read_text(encoding='utf-8');marker=RUN.name if name=='WORKLOG.md' else '2026-10-23 stage18:'
    if marker not in old:p.write_text(old+text,encoding='utf-8')

receipt_paths=[BASE/'BOARD.md',BASE/'claude/B15/STREAM_NOTES.md',source/'REPORT.md',source/'CLAIMS.json',source/'out/ADAPTIVE.json',source/'out/SEVEN_PROFILES.json',BASE/'agents/A074/runs/20261022T225155Z-fleet03-A074-independent-reproducer/REPORT.md',BASE/'agents/A089/runs/20261022T225420Z-fleet03-A089-repair-specialist/REPORT.md']
protocol_path=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json');receipt_paths.append(protocol_path)
save(RUN/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)} for p in receipt_paths])
protocol=load(protocol_path);pf=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']];cf=protocol['required_per_run']['claim_fields']
assert set(progress)==set(pf)
for c in [claim,sourcecopy]:assert set(c)==set(cf)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(p.stat().st_size<20*1024*1024 for p in RUN.rglob('*') if p.is_file())
save(RUN/'out/SCHEMA_VALIDATION.json',{'exact_progress_fields':True,'exact_claim_fields':True,'packet_delta_identical':True,'source_statement_and_hypotheses_unchanged':True,'labelled_restrictions':1458,'labelled_query_rows':2916,'compressed_rows':70,'financial_policies':6,'all_files_under_20MB':True,'status_lines':2,'full_fei':'OPEN'})
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='MANIFEST.json']
save(RUN/'out/MANIFEST.json',[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files])
print(json.dumps({'saved':RUN.name,'files':len(files),'source_theorem':'ACCEPT_UNCHANGED','new_theorem':'REVIEW_PENDING','hull_checks':v['exact_checks'],'integer_checks':integers['integer_checks'],'schema':'PASS','full_fei':'OPEN'}))
