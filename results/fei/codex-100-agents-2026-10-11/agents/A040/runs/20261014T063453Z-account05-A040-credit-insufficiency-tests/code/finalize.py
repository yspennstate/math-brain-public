from pathlib import Path
import json,hashlib,copy,datetime
ROOT=Path(__file__).resolve().parents[1];HOME=ROOT.parents[1];AGENTS=HOME.parent;CAMP=AGENTS.parent
SOURCE=AGENTS/'A046/runs/20261014T041928Z-account05-A046-current-candidate-intake'
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=read(PROTOCOL);source=read(ROOT/'out/SOURCE.json');biased=read(ROOT/'out/BIASED.json');inter=read(ROOT/'out/INTERLEAVED.json');rational=read(ROOT/'out/RATIONAL_SUMMARY.json')
assert all(x['status']=='PASS' for x in [source,biased,inter,rational])
total=sum(x['checks']+x['helper_checks'] for x in [source,biased,inter])+rational['total_checks'];assert total==30000
assert source['nodes']==4 and biased['nodes']==32 and inter['parents']==8 and inter['child_occurrences']==48
original=next(x for x in read(SOURCE/'CLAIMS.json') if x['claim_id']=='A046-SEPARATOR-LAYER-CUTOFF-RESERVE' and x['version']==2)
assert original['statement_sha256']=='bd27ee5a2c778775819779bfeceee08d76d1f3f64f9e9667a7dc13e941bf547f'
review=copy.deepcopy(original)
review['review_records'].append({'reviewer':'A040','verdict':'HOLDS','source':str(ROOT/'REVIEW_A046_V2.md'),'scope':'Full exact balanced-core v2 claim: rare-row constant/nonconstant moments and strict 1781/480 bound; all-width actual prefix Q_bad<=5I via the filtered reserve; full pi H(g) and conditional terminal-rate corollary.',
'excluded':'No acceptance of arbitrary data-query payment, biased descendant union payment, prescribed reference/reset conversion or universal FEI. A040 bias continuation is separate from this source review.',
'repair_supplied':False,'source_claims_sha256':sha(SOURCE/'CLAIMS.json'),'validation':'Independent physical Walsh/edge representation plus exact rational moment/reserve checks; analytic all-width reconstruction in REVIEW_A046_V2.md.'})
review['status']='INDEPENDENT_REVIEW_HOLDS'
statement='Let W,U,V be compatible point events on disjoint uniform blocks of positive widths L,R,T, S a disjoint j-bit point event, and g any independent Boolean sign with a=1-Eg in [0,2]. Put eta=2^-(L+R+T),q=2^-R,r=2^-T,e=q+r-qr-eta,F=1+[WUV+S((U OR V)-WUV)](g-1). If e<=1/8, every live S query with positive influence has B_i/Inf_i<10063/2520<4; zero-influence cases have zero erasure. This holds without balance and under every adaptive history querying only core-data and S coordinates with W,U,V unexposed. The actual S-query strict-K4 bad-face bill is zero along these histories. For alpha=2^-j,JB=(L+R+T)eta,JC=R q(1-r)+T r(1-q),JD=JB+JC,pi=eta+alpha e, the next-S face price is c_j=alpha[a(JD+(j-1)e)+e I(g)]. At any core query i with physical child cores g0,g1 it obeys c_j(F)-[c_j(F|i=0)+c_j(F|i=1)]/2=alpha e Inf_i(g)<=Inf_i(F)=pi Inf_i(g), with residual difference eta Inf_i(g). No data-query entropy, later biased union descendant, terminal entropy or prescribed-reference/reset payment is asserted.'
hyp=['Actual uniform Boolean cube and bit entropy; no core balance assumption.',
'Disjoint fresh point blocks with compatible literals and e<=1/8; min(R,T)>=4 is sufficient.',
'Conditional history reveals only S or core-data bits while W,U,V remain entirely unexposed; stop counting S queries after S failure.',
'Face cost is actual I(child product)/2; data-query influence and both terminal laws retain their original physical weights. Face contraction is not an additional independent budget.']
digest=hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
own={'claim_id':'A040-BIASED-RARE-SEPARATOR-CORE-QUERY','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest,'contributors':['A040'],
'proof_source':{'run_id':ROOT.name,'files':['BIAS_EXTENSION.md','code/check.py','out/BIASED.json','out/INTERLEAVED.json','out/MOMENTS.json','out/RATIONAL_SUMMARY.json']},
'proof_dependencies':[{'claim_id':original['claim_id'],'version':2,'statement_sha256':original['statement_sha256'],'scope':'Balanced rare-row method supplies source interface; arbitrary-bias moments and tighter constants independently derived in BIAS_EXTENSION.md. No universal core bound is used.','status':'INDEPENDENTLY_REVIEWED_BY_A040'}],
'review_records':[],'status':'NARROW_EXISTING_INTERFACE_CONTINUATION_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A046','A024','A023','A087','A092','B08','B20']}
for c in [review,own]:assert set(c)==set(protocol['required_per_run']['claim_fields'])
save(ROOT/'CLAIMS.json',[review,own])
sources=[PROTOCOL,CAMP/'BOARD.md',CAMP/'claude/B08/STREAM_NOTES.md',SOURCE/'REPORT.md',SOURCE/'PROOF.md',SOURCE/'CLAIMS.json',AGENTS/'A024/runs/20261014T055140Z-account05-A024-biased-child-stability/REPORT.md',AGENTS/'A098/runs/20261014T054007Z-account05-A098-resource-reallocation/REPORT.md',HOME/'runs/20261014T033148Z-account05-A040-credit-insufficiency-tests/REVIEW_A046.md',HOME/'runs/20261014T033148Z-account05-A040-credit-insufficiency-tests/ENVELOPE_OBSTRUCTION.md',HOME/'runs/20261014T033148Z-account05-A040-credit-insufficiency-tests/code/arithmetic.py']
save(ROOT/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'read_scope':'Protocol all; relevant board/routing and report/proof/claim scopes described in REPORT; own prior proof/helper provenance.'} for p in sources])
report='''# exact target, quantifiers, hypotheses and units

A040/B08 stage 5, run 20261014T063453Z-account05-A040-credit-insufficiency-tests. Independently review A046-SEPARATOR-LAYER-CUTOFF-RESERVE@2, the actual strict-K4 controller-prefix payment for F=1+[WUV OR S(U OR V)](g-1), arbitrary positive point-block widths and independent BALANCED core g. All inputs are uniform physical bits, entropy/logs are bits and influence is flip probability. The declared prefix stops at a constant or the actual core, retaining pi H(g).

Verdict: **HOLDS without repair at full exact v2 claim scope**. The actual prefix bill is <=5I, and is zero for min(R,T)>=4, despite the old envelope's logarithmic price. A separate narrow continuation derives arbitrary-BIASED core moments and proves every live separator query has B/d<10063/2520<4 when e<=1/8. This survives core-data reveals while W,U,V stay unexposed. It does not pay the data query itself or its references. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read BOARD 2026-10-14 06:34 UTC, B08 lead notes v2, own STATUS and execution protocol 2026-10-11-execution-v2 in full. B08's old minimum-census instruction remains superseded by the A098 source-bound review assignment. A098 stage-5 REPORT explicitly assigns A040 the v2 review and A046 the full first-core-query ownership target. This run finishes that review and hands back a narrow conditional-moment lemma; it does not run a competing general data-payment search.

Read A046 stage-5 REPORT, PROOF and CLAIMS, statement digest bd27ee5a2c778775819779bfeceee08d76d1f3f64f9e9667a7dc13e941bf547f. Read A024 stage-5 REPORT's separate lifted-controller obstruction and partial balanced rare-row acceptance; it does not establish the arbitrary-bias bound here. Own prior A040 v1 review and old-envelope obstruction are preserved and consumed. A040-owned arithmetic was copied into this run; no A046/A024 author helper was executed or imported. SOURCE_RECEIPTS records paths and bytes; hashes are not theorem verdicts. No new paper, web fact or brain-write premise.

# complete derivation or exact first unsupported line

REVIEW_A046_V2.md independently reconstructs every exact source clause. Separating the FULL constant Fourier row gives exact exceptional masses q_star,b_star. Compatible nested events force eta<=8e^2/25, allowing a uniform balanced bound B/d<1781/480 for e<=1/8. Hence all wide-block separator charges are deleted. The remaining widths have at most five cutoff layers, and the physical suffix-face reserve gives Q_bad<=5I_other+2I_sep+5I_terminal<=5I. All balanced descendants and terminal pi H(g) retain their original scope. This closes the previous width gap in the ACTUAL K4 prefix price, while the old V/I~log(width) envelope obstruction stays valid.

BIAS_EXTENSION.md gives the additional conditional calculation. Let a=1-Eg in [0,2], G=1+WUV(g-1), H=1+(U OR V)(g-1), Delta=Hhat-Ghat, rho=2^{-(j-1)}, d=rho a e/2. On nonempty data labels,

    sum Ghat^2=2a eta-a^2 eta^2,
    sum Ghat Delta=-a^2 eta e,
    sum Delta^2=2a e-a^2 e^2.

The full constant row is u0=1-a eta-d,v0=d, and

    q_star=2a eta-a^2 eta^2-rho a^2 eta e+rho^2(a e-a^2e^2/2),
    b_star=rho^2 a e(2-a e)/4.

Binary remainder/log-sum plus eta<=8e^2/25 give a rare-row bound uniform in a. Exact estimates c<13/9, euler<87/32, (87/56)^20<2^13 and sqrt2<10/7 yield

    B/d<2+13/20+26/63+67/72=10063/2520<4.

The strict margin is 17/2520. Zero-influence cases have zero erasure. Every conditional core after a data query has a new a in [0,2] but the same unexposed control geometry, so its separator bill remains zero. This also applies along arbitrary adaptive S/core-data histories while W,U,V remain unexposed.

The corresponding physical accounts are bias-scaled on the control side only. With alpha=2^-j, JB=(L+R+T)eta,JC=R q(1-r)+T r(1-q),JD=JB+JC,pi=eta+alpha e,

    I(F)=a[j alpha e+(1-alpha)JB+alpha JC]+pi I(g),
    c_j=alpha[a(JD+(j-1)e)+e I(g)].

At an actual core query i, original physical child weights give

    c_j(parent)-avg c_j(children)=alpha e Inf_i(g)
       <=pi Inf_i(g)=Inf_i(F).

The remaining difference is eta Inf_i(g). This face contraction is an identity, not a second spendable credit. Both child entropy increments and terminal spectra are recorded explicitly. The previously proved positive-KL/terminal Theta(1/k) insufficiency remains a warning against deleting these bills; it is not recounted as new work.

First unsupported universal line: pay the actual core-data erasure/JS and prescribed reference/reset change from a genuinely UNUSED inherited child/core bank, retaining both complete terminal laws. Later biased union/controller reveals may leave the rare unexposed geometry. No bound for those residuals follows from separator zero-badness or (6) in BIAS_EXTENSION.md.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC preceded jobs. ACCOUNT_ADDENDUM preceded the additional influence/face-contraction checks on the SAME frozen interleaved domain. Estimated memory160 MB, largest truth table14 bits; peak not measured. No >300 MB job or memok trigger. Jobs were sequential, below55 seconds, with no dimension increase or background process.

Pilot: first balanced source node,16 audit+2 helper assertions,1.729618 seconds,PASS. Main physical tests: four balanced source nodes (60+8 assertions,6.932633 seconds); all16 labeled two-bit cores at j=1,2, 32 biased nodes (460+64 assertions,28.432375 seconds); eight three-bit parent nodes and every physical core-coordinate/both-child restriction,48 child occurrences (1192+80 assertions,34.024737 seconds). The parents are Maj3,parity3,a one-point defect and its negative, at j=1,2. All physical controls use L=1,R=T=4. Total92 physical node occurrences, without a symmetry quotient. The helper caches identical spectra but occurrence counts are explicit.

The physical checker derives constant/nonconstant moments from integer Walsh amplitudes, checks exact erasure-vector equality against the full spectrum, compares spectral influences to direct flips, and certifies strict bounds by rational log intervals. The interleaved test preserves actual parent/child functions, checks bias-scaled influence accounts, exact face prices/contraction, exact entropy decrement B+JS and complete child terminal entropies. No assumption of flat core spectra is used.

Formal rational tests:4200 moment rows j=1..8,L=1..3,R,T=4..8 independently,a in {0,1/64,1/8,1/2,1,3/2,2};1296 source-reserve cases s=1..6,L=1..3,R,T=1..6,formal I(g) in {1,5/2};4536 exact reserve drifts;8 exact scalar certificates. These are algebraic controls, not extra Boolean spectra. Rational job28,136 assertions,0.626783 seconds,PASS. Total final nonpilot assertions:30,000. The separate analytic proof covers every bias and dimension; finite cases do not establish continuum claims.

Commands from A040:

    python -X utf8 runs/20261014T063453Z-account05-A040-credit-insufficiency-tests/code/check.py source pilot
    python -X utf8 runs/20261014T063453Z-account05-A040-credit-insufficiency-tests/code/check.py source
    python -X utf8 runs/20261014T063453Z-account05-A040-credit-insufficiency-tests/code/check.py biased
    python -X utf8 runs/20261014T063453Z-account05-A040-credit-insufficiency-tests/code/check.py interleaved
    python -X utf8 runs/20261014T063453Z-account05-A040-credit-insufficiency-tests/code/check.py rational
    python -X utf8 runs/20261014T063453Z-account05-A040-credit-insufficiency-tests/code/finalize.py

Fraction edge/moment identities and prime-log vectors decide equalities. Fixed24-term atanh enclosures with proved tails and outward endpoints certify signs. No floating entropy decision, random sampling, GPU, author helper, automatic precision or dimension escalation. Completed cases are saved immediately. No job failed or required continuation.

# proof dependencies and changed downstream conclusions

CLAIMS preserves A046@2's exact statement,hypotheses,author and hash, appending a full independent HOLDS record without repair. Its accepted v1 dependency is acyclic and unchanged. A040's arbitrary-bias continuation is a separate narrow refinement of this existing interface, author-proved pending independent review; it is not a repair to the accepted balanced source or a new broad universal candidate.

A046/A024/A023 can now consume the exact biased moments and first-data-query face contraction. In the rare unexposed-controller regime, balance loss itself does not recreate a bad separator debit or require any W reserve. Data-query entropy/reference payment and later biased controller admission remain open, so no inherited bank may be reassigned automatically. The old envelope obstruction is not withdrawn; its costly eligible rows have been correctly filtered.

# one next mathematical action and independent reviewer

Hand the biased moments and contraction to A046's existing first-core-query payment lane. Consume its next actual data-query erasure/reference residual, compare it with genuinely remaining child surplus, and retain both original child terminal laws; do not renew the deleted separator budget. A046/A087 should independently check the 10063/2520 constant and adaptive-history scope; A092 should challenge any claimed reference refund. A024 can consume the exact bias-scaled face account. No tool message was sent.

# actual persistence receipts or precise save blocker

Saved: four protocol files, REVIEW_A046_V2,BIAS_EXTENSION,independent code,frozen spec/addendum,immediate exact outputs,source receipts,schema readback and artifact hashes. STATUS has exactly two lines; WORKLOG and LEARNED append this stage. PROGRESS/PACKET_DELTA are byte-identical; every file is below20 MB. No local blocker. Supervisor copies, shared adoption, mirrors, independent review of the biased continuation and downstream use remain unverified.

## Universal bridge

This stage moves C019 stopping-tree payment and its C024 history interface by independently closing A046 v2's actual Q_bad<=5I theorem and proving that rare-block separator zero-badness survives arbitrary core bias and S/core-data histories, with strict rate10063/2520<4 and exact owned face contraction. The universal FEI constant improves by zero. What remains is actual data-query entropy/reference payment and later-controller/terminal admission from unused inherited surplus. NEXT consumes A046's distinct data-payment calculation using the now-fixed conditional moments, the shortest route toward full FEI because balance loss is removed as a separator obstruction while the true unpaid residual stays explicit.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B08','packet_id':'A040','gap_id':'C019-C024-FIRST-CORE-DATA-QUERY-OWNER','attempt_id':'A040-stage5-v2-review-biased-rare-row',
'method':'Independent constant/nonconstant Walsh-row reconstruction, exact scalar certificate, biased first-core-query face contraction and terminal-preserving physical audit.',
'mathematical_delta':'Full A046@2 independently HOLDS, no repair. For e<=1/8 arbitrary biased core has separator B/d<10063/2520<4 under all S/core-data histories with WUV unexposed; exact next-face contraction=alpha e Inf_i(g)<=Inf_i(F). Data-query/reference payment remains open.',
'deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'SOURCE_V2_REVIEW_HOLDS; NARROW_BIASED_CONTINUATION_PROVED_REVIEW_PENDING; FULL_FEI_OPEN',
'claim_versions_used':[{'claim_id':original['claim_id'],'version':2,'statement_sha256':original['statement_sha256'],'status':'INDEPENDENT_REVIEW_HOLDS'}],
'claims_created_or_changed':[{'claim_id':original['claim_id'],'version':2,'change':'Local full independent HOLDS appended; original source unchanged'},{'claim_id':own['claim_id'],'version':1,'change':'Narrow arbitrary-bias rare-row and physical core-query continuation'}],
'source_artifacts':[str(p) for p in sources]+[str(ROOT/'BIAS_EXTENSION.md'),str(ROOT/'REVIEW_A046_V2.md'),str(ROOT/'out/INTERLEAVED.json'),str(ROOT/'out/RATIONAL_SUMMARY.json')],
'next_consumers':['A046','A024','A023','A087','A092','B08','B20'],
'next_action':'Consume A046 actual first-core-query entropy/reference residual with these biased moments; pay from genuinely unused inherited child surplus, retaining both original terminal laws and not recreating separator W.',
'stagnant_substantive_attempts':0,'blockers':['No local save blocker. Actual data-query entropy/reference payment and later biased-controller/terminal admission remain mathematical gaps.'],'packet_ids':['A040']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save(ROOT/'PROGRESS.json',progress);(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
(HOME/'STATUS.md').write_text('STATE: A040 stage 5 complete: A046 v2 full claim independently HOLDS; arbitrary-bias rare separator B/d<10063/2520 and exact first-core-query face contraction proved;30,000 exact assertions PASS;FEI OPEN.\nNEXT: A046/A087 review biased continuation; consume actual core-data entropy/reference debit from one unused inherited child bank, preserving both terminal laws and never renewing the zero separator reserve.\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n## '+now+' — stage 20261014T063453Z\nConsumed A046@2 actual bad-prefix theorem and A098 review dispatch. Independently HOLDS without repair. Derived arbitrary-bias moments (a=1-Eg), strict rare-row rate10063/2520<4 for e<=1/8, adaptive S/core-only-history zero separator bill with WUV unexposed, exact face contraction alpha e Inf_i(g)<=pi Inf_i(g) across a core query. Frozen92 physical node occurrences,4200 formal moment rows,1296 reserve cases/4536 drifts;30000 final assertions PASS. New narrow continuation pending independent review; actual data-query entropy/reference costs remain open. No foreign writes or refreshed separator bank.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n## Stage 5: arbitrary-bias rare rows survive core-data exposure\nA046 v2 full exact claim independently HOLDS. For a=1-Eg arbitrary[0,2], nonconstant moments are 2a eta-a^2eta^2,-a^2eta e,2a e-a^2e^2. With rho=2^-(j-1),d=rho a e/2, qstar=2a eta-a^2eta^2-rho a^2eta e+rho^2(ae-a^2e^2/2),bstar=rho^2ae(2-ae)/4. eta<=8e^2/25 and e<=1/8 imply B/d<2+13/20+26/63+67/72=10063/2520<4, even biased conditional cores. Under only S/core-data queries while WUV unexposed, S-query bad bill stays0. Actual I(F)=a J(A)+pi I(g); next-S face c_j=alpha[a(JD+(j-1)e)+eI(g)]. Across core query i, c_parent-avg c_child=alpha e Inf_i(g)<=pi Inf_i(g)=Inf_i(F), with residual eta Inf_i(g). This is not another budget; actual data-query erasure/reference costs and later biased union descendants remain unpaid. Exact constants: ln2>842/1215>9/13,euler<65/24+1/100<87/32,87^20<2^13*56^20,sqrt2<10/7.\n')
assert len((HOME/'STATUS.md').read_text().splitlines())==2
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
for field in protocol['required_per_run']['report_fields']:assert '# '+field in report
save(ROOT/'out/SCHEMA_CHECK.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,'packet_delta_byte_identical':True,'report_fields_present':True,'status_two_lines':True,'physical_node_occurrences':92,'formal_moment_rows':4200,'formal_reserve_cases':1296,'final_assertions':30000,'source_v2_review':'HOLDS_NO_REPAIR','new_biased_claim_review_pending':True,'mirror_verified':False})
files=[p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='ARTIFACT_RECEIPTS.json']
assert all(p.stat().st_size<20*1024*1024 for p in ROOT.rglob('*') if p.is_file())
save(ROOT/'out/ARTIFACT_RECEIPTS.json',[{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(files)]+[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in [HOME/'STATUS.md',HOME/'WORKLOG.md',HOME/'LEARNED.md']])
print(json.dumps({'status':'SAVED_SCHEMA_PASS','source_v2_review':'HOLDS_NO_REPAIR','new_rate':'10063/2520<4','final_assertions':30000,'artifact_receipts':len(files)+3,'new_statement_sha256':digest}))
