from pathlib import Path
import json,hashlib
RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1]
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def put(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pilot,main,rows=[rd(RUN/('out/'+n+'.json')) for n in ['PILOT','VALIDATION','ROWS']]
assert all(x['status']=='PASS' for x in [pilot,main,rows])
assert main['physical_continuation_nodes']==40 and rows['cases']==9280
statement=('Version4 retains A030@3 at its declared scope and adds the following. For any finite-label Boolean selector F(y,x)=g_L(y)(x), with independent uniform control and data cubes and arbitrary shared-data Boolean sources, let c_j=hat(1_{L=j}), b_j=hat(g_j), P(U,t)=(sum_j c_j(U)b_j(t))^2 and Qinc(U,t)=sum_j c_j(U)^2 b_j(t)^2. Qinc is a normalized support-positive reference with the same data marginal as P. The exact conditional-profile conversion cost C=D(P||Qinc) is at most sum_t q(t) log2(k_t), where k_t counts nonzero source amplitudes at t, and hence at most log2(number of sources). The latter bound is sharp for uniform address labels and identical sources. For the even-r>=4 tagged rare-label bent family of PROOF.md, after actual tag outcomes (+,-) of root reach1/4, this conversion has 0<C<3*2^-r/8=(3/4)Inf_s(F). The SAME original U=4I_root, with old debit1/4, pays the two-tag entropy path, the selected conversion, all other full terminals, and every subsequent finite adaptive physical no-reset continuation with the CURRENT reference, leaving more than765/512 unused root units. The exact source references have inherited Z=0, so the conversion is paid from original admission surplus, not Z or cut slack. No universal initial admission or full-FEI theorem is asserted.')
claim=dict(claim_id='A030-THREE-STATE-BOOLEAN-CUT-RESERVE',version=4,exact_statement=statement,
 hypotheses=['Uniform finite product cube; normalized Walsh coefficients and base2 entropy/KL.',
 'All source/control phases retained when computing the true Boolean spectrum; Qinc retains mass on zero-true rows.',
 'For quantitative payment: exact canonical bent rare-label controller, independent tagged point-defect/majority/tagged point-defect sources; even r>=4.',
 'One selected (+,-) tag-history conversion; physical reach1/4, old debit1/4, original U=4I_root; both physical children and all source terminals retained.',
 'After conversion inherit CURRENT reference through actual phase channels with its own branch normalizers; no further free reset.'],
 statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A030'],
 proof_source=['PROOF.md sections1-5','code/check.py','code/rows.py','out/VALIDATION.json','out/ROWS.json'],
 proof_dependencies=[{'claim':'A030-THREE-STATE-BOOLEAN-CUT-RESERVE@3','scope':'Actual family and previous local obstruction retained; new admission proof independently derived here.'},
 {'claim':'A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@7','scope':'Physical reference transport interface only; reconstructed directly in PROOF.md section4.'},
 {'claim':'A029-FINITE-LABEL-SIGNED-CHILD-ACCOUNT@2','scope':'Exact conditional-profile bill and inherited-Z distinction only; its special eligibility example is not used.'}],
 review_records=[{'reviewer':'A030','kind':'Author analytic proof plus exact sector/physical-reference checker and separate helper-free integer character-sum reconstruction.','result':'Pilot69/main668 assertions PASS; independent-representation9280 finite cases/152322 integer assertions PASS; not external independent acceptance.'}],
 status='AUTHOR_PROOF_EXACT_CHECKED_EXTERNAL_REVIEW_PENDING_NOT_LEAN_CERTIFIED',
 supersedes=[{'claim_id':'A030-THREE-STATE-BOOLEAN-CUT-RESERVE','version':3,'reason':'Cumulative addition: a specified incoherent-profile conversion and same original quota payment; previous local obstruction remains valid.'}],
 refutes=[{'statement':'A changed conditional profile may be reset free whenever supplied source references are exact.','witness':'Exact source references give W=Z=0 but selected tagged node has C>0.'},
 {'statement':'Delete off-true mass from Qinc without retaining normalization and the actual reference.','witness':'2816 of9280 frozen actual shared-source cases have Qinc>0 at a zero P row.'}],
 first_unproved_line=None,next_consumers=['B06 Claude lead','A028','A029','A056','A087','A094','A097','B20'])
put(RUN/'CLAIMS.json',[claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=RUN.name,stream='B06',packet_id='A030',
 gap_id='C019-C024-UNEQUAL-MEAN-STRUCTURAL-CONVERSION',attempt_id='A030-incoherent-profile-original-quota',
 method='Universal exact incoherent-reference normalization and row-overlap Cauchy bound; chi-square refinement; analytic original-quota admission; exact physical channel continuation and helper-free integer shared-source certificates.',
 mathematical_delta='Paid one genuine coherent-to-incoherent profile conversion on the previous bent obstruction from SAME original4I account, not zero cut slack/Z: C<(3/4)Inf_s, old debit1/4 retained, root reserve>765/512 for all even r>=4 and every later adaptive no-reset physical tree. Generic finite-label conversion costs at most log(label count), sharply. Universal initial admission remains unpaid.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACTS_VERIFIED',mathematical_status='SCOPED_CONVERSION_AND_ALL_R_QUOTA_PAYMENT_PROVED_BY_AUTHOR; EXTERNAL_REVIEW_PENDING; FULL_FEI_OPEN',
 claim_versions_used=['A030-THREE-STATE-BOOLEAN-CUT-RESERVE@3','A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@7','A029-FINITE-LABEL-SIGNED-CHILD-ACCOUNT@2'],
 claims_created_or_changed=['A030-THREE-STATE-BOOLEAN-CUT-RESERVE@4'],
 source_artifacts=['PROOF.md','out/FROZEN_SPEC.json','out/ROW_SPEC.json','out/PILOT.json','out/VALIDATION.json','out/ROWS.json','out/SOURCE_RECEIPTS.json','out/PERSISTENCE.json'],
 next_consumers=claim['next_consumers'],
 next_action='Price a second prescribed nonempty-profile conversion AFTER one real mixed query using the CURRENT incoherent reference and already-debited original4I account; retain first cost, actual phase refunds, old1/4 and both full terminals. Seek generic admission suppliers separately rather than call log-label cost FEI.',
 stagnant_substantive_attempts=0,
 blockers=['Universal influence-priced full source/structural admission remains unproved; one-label case already contains arbitrary source FEI.','External review and Lean certification pending.','No remote mirror verification; supervisor owns copying.'],packet_ids=['A030'])
put(RUN/'PROGRESS.json',progress);put(RUN/'PACKET_DELTA.json',progress)
report='''# A030: a paid profile conversion after the plateau

## exact target, quantifiers, hypotheses and units

Move the C019/C024 structural conversion left open by A030@3. For arbitrary finite-label Boolean selectors on independent uniform control/data cubes, the normalized incoherent reference Qinc(U,t)=sum_j hat(C_j)(U)^2 hat(g_j)(t)^2 shares the true data marginal. Its exact conditional-profile conversion bill is at most sum_t q(t)log2(k_t)<=log2(number of sources), where k_t counts the nonzero source amplitudes at that data row. The log-label bound is sharp. All logarithms are base2.

For EVERY even r>=4 in the actual tagged bent rare-label family, the selected (+,-) two-tag history has reach1/4 and conversion cost 0<C<3*2^-r/8=(3/4)Inf_s(F). The SAME original quota U=4I_root pays this conversion, the full entropy path and every later finite adaptive no-reset physical stopping tree, with old debit1/4 and both full terminal CE bills, leaving MORE than765/512 unused root units. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read the current BOARD.md (04:04 UTC23 October), B06 STREAM_NOTES.md v2, own STATUS.md and previous stage's proof/code. Read machine-wide AGENTS.md and protocol required fields; this packet's explicit ownership and compute limits govern local writes. New mathematical dependencies consumed: A028's20261023T023055Z run, out/DERIVATION.md and claim version7; A029's20261023T032111Z run, DERIVATION.md sections1-7 and CLAIMS.json version2. Exact statements are identified in CLAIMS.json and source hashes in out/SOURCE_RECEIPTS.json. A028's prescribed true-profile transport and A029's actual conditional-profile bill were reconstructed here, without adopting universal suppliers or enlarging their special-family eligibility.

One read-only math-store query returned the prior warning that a bad specified coordinate does not refute existential selection, and the sharp logarithmic coordinate bound. Neither is used as an external theorem. No new literature or paper version is asserted. Previously consumed campaign baselines are not represented as newly reread this stage. The initial attempt to read A028/DERIVATION.md failed because its derivation is under out/; the correct file was then read.

## complete derivation or exact first unsupported line

PROOF.md supplies the complete author derivation. Orthogonality of the indicator partition proves normalization and common data marginal of Qinc; rowwise Cauchy supplies the universal log-overlap bound. Identical Boolean sources with uniform address labels attain the log-label cost, showing the bill cannot be discarded. For the actual three-private-source obstruction, only the vacuum data row can interfere. A chi-square calculation retains the rare scale: c_2 has no s Fourier membership, and the squared c_0 mass on those rows is exactly2^-r/4. Thus C<=2^-r/(4 ln2)<3*2^-r/8.

At the original balanced tagged root, all source entropies2 are retained. Disjoint nonempty private spectra give H_root<=r+5. Exact edges give I_root=r/4+(r+1)2^-r/2+2-pi1/2>=r/4+27/16. Consequently4I_root-H_root>=7/4. Paying the prior1/4 and the actual root-reach-weighted reset cost<3/512 leaves>765/512. Every subsequent query transports the CURRENT changed reference using actual phases and its own reference outcome masses. KL erasure and outcome refunds are retained; data processing pays every finite adaptive continuation without reset.

This does not contradict the previous local obstruction E/Inf_s~r/4: E is the old cut/rarity conversion bill, whereas C is a different specified reference transaction with an explicitly identified original owner. The exact source-reference choice has W=Z=0, so C>0 cannot be charged to inherited Z; it is charged solely to original admission surplus. No cut bank, descendant4I quota or frontier JS is renewed. The first unsupported universal line is a full influence-priced source/structural admission for arbitrary inputs; log-label calibration by itself cannot provide it. A second reset must also retain the first debit and current profile.

## executed validation with domain, arithmetic, commands and outputs

The specs out/FROZEN_SPEC.json and out/ROW_SPEC.json were saved BEFORE their respective jobs. All jobs were below100MB expected memory; no job exceeding300MB was attempted. The pilot took0.132 seconds and passed69 assertions. The main took6.889 seconds and passed668 assertions: sector checks r=4,6,8, all four tag outcomes, r=4 direct full Boolean spectrum/physical edges, all12 one-coordinate continuations and four complete depth-three policies (40 physical query nodes total). The pilot also includes r=2 as a finite boundary control, outside the all-r>=4 theorem. The first pilot preceded the chi-square refinement and passed65 checks; adding that bound explains the increase to69, and the final saved pilot matches the main code hash.

Normalized Walsh coefficients, references and channel probabilities use exact Fractions. Entropy/KL are canonical rational prime-log expressions, with rigorous rational logarithm enclosures for signs. At r=4, 0.010755593<C<0.010755594; at r=8, 0.000701821<C<0.000701822. Floating-point times are diagnostics only. The separate helper-free integer character-sum reconstruction exhausts4096 two-label/shared-two-bit-source cases and5184 three-label/shared-one-bit-source cases:9280 total,152322 exact assertions, PASS in2.299 seconds. It independently reconstructs actual full Boolean Fourier numerators, normalization, common marginal and row-overlap dominance, retaining zero-probability labels. Exactly2816 cases require off-true reference mass.

Commands from this run are `python -X utf8 code/check.py --pilot`, `python -X utf8 code/check.py`, and `python -X utf8 code/rows.py`. Results are out/PILOT.json, out/VALIDATION.json and out/ROWS.json. The all-dimensional claims come from the analytic proof, not finite extrapolation. No Lean certification or independent external acceptance is claimed.

## proof dependencies and changed downstream conclusions

A030-THREE-STATE-BOOLEAN-CUT-RESERVE@4 cumulatively retains@3. A028@7/A029@2 are used only for their reconstructed reference interface and exact accounting distinction. The new general conversion lemma needs only finite Fourier orthogonality, Cauchy and elementary KL inequalities. The selected all-r supplier is proved explicitly here, rather than assumed from their special fixtures. The original zero cut slack remains zero and the old local failure remains true. Downstream consumers can now use a specified incoherent-profile target with a cost and a real owner on this obstruction; they cannot discard terminal structural CE or claim a generic FEI supplier.

## one next mathematical action and independent reviewer

Price a SECOND prescribed nonempty-profile conversion after one actual mixed query, inheriting the CURRENT incoherent reference and retaining the first reset debit, original old1/4, actual erasure/outcome refunds and both full terminal costs. Use the remaining original4I quota; do not reopen a descendant bank. A087/A094 should independently reconstruct the full proof; A028/A029/A056 are immediate consumers of the finite-label conversion interface. These are locally recorded handoffs, not messages or reviews obtained. The universal initial-admission obligation remains explicit.

## actual persistence receipts or precise save blocker

All four protocol files, PROOF.md, specs, scripts and exact outputs are saved in this requested run. out/FINAL_CHECK.json records schema, hash, output-PASS, compatibility-copy and size checks; out/PERSISTENCE.json lists local byte/SHA256 receipts, including the rolling files. STATUS.md is current and WORKLOG.md/LEARNED.md are appended. Only A030-owned paths were modified. Remote upload, supervisor adoption, external review and mirror verification are not claimed. Brain self-care remains degraded/unverified: stale owner-model/state-of-mind sources affect personal-context reliability and were not relied on mathematically. No running work was killed, suspended or throttled; these bounded jobs completed.

## Universal bridge

This stage moves C019 stopping-tree payment and C024 history transfer by paying one genuine coherent conditional-profile conversion on the prior plateau obstruction from ONE explicitly supplied original4I account, with cost<(3/4)Inf_s, old debit retained and reserve>765/512 through every later no-reset mixed tree. The universal row-overlap conversion bound supplies a reusable interface, while arbitrary-input initial admission remains unpaid. The next second conversion with the current reference is the shortest useful continuation because it tests whether the same diminished ancestor owner survives a real profile change, rather than restating a restriction-class FEI result or retrying the analytically excluded local cut bill.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(OWN/'STATUS.md').write_text('STATE: A030 stage complete: universal incoherent-profile KL<=log labels; bent reset C<(3/4)Inf_s paid SAME original4I after old1/4, reserve>765/512; exact69+668+152322 checks PASS; external review pending; FEI OPEN.\nNEXT: Pay second prescribed profile conversion after actual mixed query using CURRENT changed reference and SAME diminished original quota; retain first cost/refunds/both terminals; A087/A094 review, A028/A029 consume.\n',encoding='utf-8')
date='2026-10-23 stage20261023T041014Z'
for name,body in [('WORKLOG.md','Consumed A028@7/A029@2 and proved a concrete incoherent-profile conversion. Generic normalized Qinc shares true data marginal and costs at most log label count, sharply. For the prior even-r bent obstruction, chi-square gives C<3*2^-r/8; original4I admission minus old1/4 pays reset and every later no-reset physical tree with reserve>765/512. Exact final pilot69/main668 and independent integer9280 cases/152322 assertions PASS. Source Z=0: original admission surplus is the actual owner. External review pending, FEI open.'),('LEARNED.md','For any finite-label selector, Qinc(U,t)=sum_j Chat_j(U)^2 ghat_j(t)^2 is normalized, support-positive and shares the actual data marginal. Conditional-profile KL is <=sum_t q(t)log2(number of nonzero source amplitudes at t), sharp log labels for identical shared sources. In the tagged bent rare-label family, only two vacuum sources interfere; the no-s c0 squared mass=2^-r/4 yields C<3*2^-r/8. A bad cut residual E/Inf~r/4 does not imply this different calibration cost is expensive. Here exact source references give Z=0, so pay positive C from original admission surplus4I-H>=7/4, never from fictitious Z or renewed cut slack. After old1/4 and reach1/4 conversion reserve>765/512 survives arbitrary CURRENT-reference physical no-reset trees. Full terminal structural CE and the generic initial-admission gap remain.')]:
 with (OWN/name).open('a',encoding='utf-8') as f:f.write('\n## '+date+'\n'+body+'\n')
base=OWN.parents[1]
sources=[base/'BOARD.md',base/'claude/B06/STREAM_NOTES.md',base/'agents/A028/runs/20261023T023055Z-fleet03-A028-stopping-tree-payment/out/DERIVATION.md',base/'agents/A029/runs/20261023T032111Z-fleet03-A029-child-deficit-transport/DERIVATION.md',base/'agents/A029/runs/20261023T032111Z-fleet03-A029-child-deficit-transport/CLAIMS.json',Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
put(RUN/'out/SOURCE_RECEIPTS.json',{'note':'Current local byte hashes at finalization; shared board is mutable, not a claimed immutable earlier snapshot.','files':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources]})
protocol=rd(sources[-1])['required_per_run']
assert set(progress)=={k.split(' (')[0] for k in protocol['progress_fields']}
assert set(claim)==set(protocol['claim_fields'])
assert rd(RUN/'PROGRESS.json')==rd(RUN/'PACKET_DELTA.json')
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
assert all('## '+field in report for field in protocol['report_fields'])
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert pilot['code_sha256']==main['code_sha256']==sha(RUN/'code/check.py')
assert rows['code_sha256']==sha(RUN/'code/rows.py')
assert all(p.stat().st_size<20*1024*1024 for p in RUN.rglob('*') if p.is_file())
put(RUN/'out/FINAL_CHECK.json',{'status':'PASS','protocol_exact_keys':True,'statement_sha256':claim['statement_sha256'],'progress_delta_identical':True,'all_report_fields':True,'code_hashes_match_outputs':True,'status_two_lines':True,'all_files_under20MB':True,'pilot_checks':pilot['checks'],'main_checks':main['checks'],'independent_integer_checks':rows['checks'],'independent_integer_cases':rows['cases'],'full_fei':'OPEN','external_review':'PENDING'})
files=[p for p in RUN.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name!='PERSISTENCE.json']
put(RUN/'out/PERSISTENCE.json',{'scope':'Local only; manifest excludes itself and transient caches. No remote adoption claimed.','files':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)],'rolling_files':[{'path':str(OWN/n),'bytes':(OWN/n).stat().st_size,'sha256':sha(OWN/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'status':'PASS','run':RUN.name,'claim':'A030-THREE-STATE-BOOLEAN-CUT-RESERVE@4','checks':[pilot['checks'],main['checks'],rows['checks']],'statement_sha256':claim['statement_sha256'],'files':len(files)},indent=2))
