from pathlib import Path
from datetime import datetime,timezone
import json,hashlib

run=Path(__file__).resolve().parents[1]; agent=run.parents[1]
old=agent/'runs'/'20261011T214703Z-fleet05-A076-threshold-and-tribes-controls'
root=agent.parents[1]
protocol_root=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
lead=root/'claude'/'B16'
now=datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,v):(run/name).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
validation=json.loads((run/'out'/'VALIDATION.json').read_text(encoding='utf-8'))

sources=[]
def source(p,scope):sources.append(dict(path=str(p),sha256=sha(p),read_scope=scope))
source(root/'BOARD.md','Read updated 23:39 UTC board at stage start, including all native stream summaries; tool display of combined read was truncated')
source(lead/'STREAM_NOTES.md','Complete v2 23:25Z read: assigned majority-of-tribes Lambda/true-B/leaf comparison; old K>=4 dominated by spectator comparison; no repeated Q/I search')
source(agent/'LEARNED.md','Stage-start facts read separately; this hash fingerprints mutable rolling content immediately before final packaging')
source(agent/'STATUS.md','Stage-start status read separately; this hash fingerprints mutable rolling content immediately before final packaging')
source(lead/'runs'/'20261011T225600Z-claude-B16-retained-kl-sandwich'/'CLAIMS.json','Read retained-KL proof and majority evidence; not used as an accepted universal upper bound')
source(lead/'runs'/'20261011T225600Z-claude-B16-retained-kl-sandwich'/'code'/'b16_sandwich.py','Read majority Krawtchouk implementation and scalar Lambda definitions; new checker independently implemented')
source(supp/'sources'/'LOG_ALLOCATION_CURATED.md','Complete mathematical sections 2-6; Lambda definition section 5 and valid local majorant (1)')
source(supp/'sources'/'ISOSPECTRAL_SPLICING_CURATED.md','Complete mathematical sections 2-9; erasure fiber (2.6), exact decrement (2.8), profile formulas (3.3)-(3.4), exact-zero guard section 4')
source(old/'STRUCTURED_CONTROLS.tex','Reused exact tribes spectrum/entropy/influence, independently rederived product spectrum this stage')
source(old/'CLAIMS.json','Previous two author-proved unreviewed claim versions; extended as v2 verification/repair bundles rather than opening another broad candidate')
source(root/'context'/'threshold_paper_38pp.txt','Previously read Theorem A/C_reg<8.937; this stage uses only symmetric-threshold leaf specialization with rational constant 9, not formula closure')
source(protocol_root/'EXECUTION_PROTOCOL.json','Protocol revision 2026-10-11-execution-v2 carried forward; schema reloaded for exact field verification')
save('SOURCE_MANIFEST.json',dict(saved_at_utc=now,sources=sources,hash_policy='Hashes are save-time readback fingerprints; mutable board/notes/rolling paths need not retain the stage-start bytes.',source_status='Lead proof reviewed for definitions; no pending lead theorem needed for the new lower bound or transport identities'))

oldclaims=json.loads((old/'CLAIMS.json').read_text(encoding='utf-8'))
transport='For every even m>=2, alpha=binom(m,m/2)/2^m, and every Boolean core G on disjoint uniform inputs (not necessarily balanced), F=Maj_(m+1)(x_1,...,x_m,G(y))=g(x)+c(x)G(y), where g=sign(sum x), g=0 on ties, c=1_{sum x=0}. The g and c Fourier supports have odd and even x-cardinality. Fhat(X,Y)=ghat(X)1_{Y=empty}+chat(X)Ghat(Y); H(F)=H(Maj_(m+1))+alpha H(G), I(F)=alpha(m+I(G)), and at every data split (B_i,M_i,Q_i,JS_i)(F)=alpha*(B_i,M_i,Q_i,JS_i)(G). If G is balanced, all x erasures vanish and B(F)=alpha B(G). For m=2, H=2+H(G)/2,I=1+I(G)/2,B(F)=B(G)/2+(1+mu^2)h2(mu^2/(1+mu^2)),mu=E G, and both children at every data split have kappa=3/4. For m=2 tribes q=2^-w,b=1-q,beta=2q*b^(t-1), the exact y-first Lambda is (beta/2)sum_(j=0..t-1,u=1..w)log2(1+(3/4)*2^(u-1)*b^-(t-j-1)); symmetric-threshold stopping subtracts (beta/2)log2(7/4), has E Ileaf=1+beta/2 and E Hleaf=2.'
obstruction='For even w>=16,t=2^w,G=uniform disjoint tribes(w,t),F=Maj3(x1,x2,G), and any fixed interleaving of the two x queries with the contiguous block-by-block y order, both constant-only and symmetric-threshold stopping trees satisfy Lambda_T/I(F)>=w/64, including after exact-zero-erasure skipping. The y-first tree has Lambda_T/I(F)=w/2+O(1), also with the same symmetric leaf certificate. At the identical trees, B_T+9 E Ileaf<=14 I(F), because H(G)<=5 I(G) and H(F)<=5 I(F). The lower bound counts actual queried influence; no physical spectator tensor is present since F is monotone and all inputs are relevant. These refute only a universal scalar Lambda payment for the specified schedules/leaf class, not arbitrary adaptive y orders, LOG_ALLOCATION local bound, C019 or FEI. Finally, for fixed even m, the supremum of B/I over central-majority compositions with arbitrary balanced cores equals the unrestricted supremum: cores G=z product_(a=1..k)h_a have H(G)=kH(h),I(G)=1+kI(h),B(G)=kB(h), giving B(F)/I(F)->B(h)/I(h) and H(F)/I(F)->H(h)/I(h).'

claims=[]
for index,extension in [(0,transport),(1,obstruction)]:
    oldc=oldclaims[index]; statement=oldc['exact_statement']+' Stage-2 extension: '+extension
    deps=[oldc['claim_id']+'@1'] if index==0 else ['A076-STRUCTURED-SPECTRA@2','threshold_paper_38pp Theorem A, symmetric-threshold specialization C_reg<9']
    refutes=list(oldc['refutes'])
    if index==1:refutes.append('There exists finite K such that for every even w>=16 one of x-first, y-first or alternating-x-y schedules with symmetric-threshold leaves pays Lambda_T+9 E Ileaf<=K I(Maj3(x1,x2,Tribes_(w,2^w))), even after exact-zero-erasure skipping.')
    claims.append(dict(claim_id=oldc['claim_id'],version=2,exact_statement=statement,
      hypotheses=oldc['hypotheses']+['Stage-2 original inputs all independent uniform physical signs; m even; core block disjoint from x','For divergence: w even>=16,t=2^w; y queries contiguous within successive tribes; no arbitrary adaptive-y-order conclusion','Lambda is LOG_ALLOCATION section 5 exact j log2(1+kappa_min/(2j)); all terminal influence retained'],
      statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A076'],
      proof_source=dict(stage1=str(old/'STRUCTURED_CONTROLS.tex'),stage2=str(run/'MIXED_TREE_PROOF.md'),summary=str(run/'STRUCTURED_CONTROLS.tex'),validation=str(run/'out'/'VALIDATION.json'),locator='(1)-(8b)' if index==0 else '(9)-(17)'),
      proof_dependencies=deps,review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[oldc['claim_id']+'@1'],refutes=refutes,first_unproved_line=None,next_consumers=['A077','A078','A092','A088','B16','B06','B20']))
save('CLAIMS.json',claims)

save('CONTROL_DISCRIMINATION.json',dict(target='C019 logarithmic stopping-tree surrogate, lead-directed majority-of-tribes',formula='Lambda_T=sum w_v j_v log2(1+kappa_min,v/(2j_v))',parameters='F=Maj3(x1,x2,Tribes_(w,2^w)), even w>=16',orders=['x-first','y-first','alternating-x-y','every fixed shuffle preserving the contiguous block-by-block y order'],stopping='constant-only or symmetric-threshold leaves; exact B=0 queries may be skipped for charging',rigorous_results=dict(Lambda_over_I_lower_bound='w/64',y_first_Lambda_over_I='w/2+O(1)',true_erasure_plus_9_leafI_over_I_upper_bound=14),terminal_certification='Only H(leaf)<9 I(leaf) for symmetric thresholds, no formula theorem',arbitrary_core_guard='Central-majority/balanced-arbitrary-core B/I supremum is exactly the universal erasure supremum; preserve B(core).',finite_certificates='out/VALIDATION.json and out/EXACT_LOG_LEDGERS.json',scope_exclusions=['every adaptive y order','arbitrary certified leaf classes','refutation of the valid one-step majorant','C019 or FEI disproof'],next_target='exact shifted empty-core erasure row after one x restriction, retaining core erasure and terminal entropy'))

progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=run.name,stream='B16',packet_id='A076',gap_id='FEI-B16-A076-INITIAL',attempt_id='A076-controls-stage2-majority-tribes',method='Lead-directed verification extension: parity-separated mixed spectrum, exact arbitrary-core erasure transport, rational interval tree ledgers, and all-width analytic good-node lower bound',mathematical_delta='Exact Lambda/true-B/terminal comparison closes the mixed control: every canonical fixed shuffle pays Lambda/I>=w/64 while the same true-erasure-plus-symmetric-leaf bill is <=14I; y-first exact leading ratio w/2+O(1). Central-majority balanced-core admission preserves universal B/I supremum.',deliverable_status='COMPLETE_LOCAL_PENDING_INDEPENDENT_REVIEW',mathematical_status='LEAD_CONTROL_OBSTRUCTION_AUTHOR_PROVED; C018_ADMISSION_EQUIVALENCE_AUTHOR_PROVED; FULL_FEI_OPEN',claim_versions_used=['A076-STRUCTURED-SPECTRA@1','A076-STRUCTURED-SPECTRA@2','threshold_paper_38pp Theorem A: symmetric leaves C_reg<9'],claims_created_or_changed=[c['claim_id']+'@2' for c in claims],source_artifacts=['MIXED_TREE_PROOF.md','STRUCTURED_CONTROLS.tex','CONTROL_DISCRIMINATION.json','SOURCE_MANIFEST.json','code/check_mixed.py','out/FROZEN_SPEC.json','out/FORMULA_EXTENSION_SPEC.json','out/VALIDATION.json','out/EXACT_LOG_LEDGERS.json'],next_consumers=['A077','A078','A092','A088','B16','B06','B20'],next_action='A092/A088 independently reconstruct the uniform kappa>=7/16 and good-prefix weighted influence; then derive the exact shifted-empty-core row correction after one x restriction with a hereditary retained-profile payment, preserving arbitrary-core B and terminal entropy.',stagnant_substantive_attempts=0,blockers=['Independent review and supervisor mirror/adoption not yet observed','Universal retained-profile erasure/terminal payment remains unsupported; no claim about adaptive y permutations'],packet_ids=['A076'])
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)

report=f'''# A076 stage 2 — majority-of-tribes Lambda obstruction and exact erasure transport

## exact target, quantifiers, hypotheses and units

The B16 lead assigned F=Maj(x_1,...,x_(n-1),Tribes_(w,t)(y)), with exact Lambda_T and true B_v on y-first, x-first and interleaved orders, all physical influence included, and leaves certified only by symmetry. This stage closes that control test at the stated schedule scope. All original inputs are independent uniform signs; all logarithms and entropies are bits. Exact analytic results apply to m=n-1 even for transport and to m=2, even w>=16,t=2^w for divergence.

The result is **Lambda_T/I(F)>=w/64** for every fixed shuffle of the two x queries with contiguous block-by-block y queries, including the three requested schedules. The same trees have **B_T+9 E I(leaf)<=14 I(F)** with symmetric-threshold leaves. For y-first, the exact leading scalar ratio is w/2+O(1). Full FEI remains OPEN; these are author-proved verification extensions awaiting independent review.

## sources actually read, revisions and theorem locators

Read the updated BOARD.md (23:39 UTC) and complete B16 STREAM_NOTES.md v2 (23:25Z) at the stage start, plus my STATUS.md and LEARNED.md. The lead's CLAIMS.json and threshold-code implementation were read. LOG_ALLOCATION_CURATED sections 2-6 supply the precise Lambda definition and valid local majorant; ISOSPECTRAL_SPLICING_CURATED sections 2-9 supply the exact erasure/decrement/profile definitions. Stage-1 STRUCTURED_CONTROLS.tex supplies the tribes product formula; it is rechecked by the new full truth-table implementation. SOURCE_MANIFEST.json pins hashes and read scopes.

The symmetric-threshold leaf certificate is the supplied 38-page threshold paper's Theorem A specialization, C_reg<8.937<9. No read-once formula theorem or arbitrary-core leaf certificate pays this tree. The lead correctly notes that stage-1 whole-block K>=4 constants are dominated by spectator-tensored known high-ratio controls; they are retained as valid calibrations, not repeated as a new frontier. No Q/I disproof search is repeated.

## complete derivation or exact first unsupported line

MIXED_TREE_PROOF.md contains the complete derivation, with a TeX summary in STRUCTURED_CONTROLS.tex. Its (1)-(5) give the central-majority arbitrary-core spectrum and exact data-erasure transport, including nonbalanced and empty spectral sectors. At data splits of majority3 the actual child kappa is exactly 3/4. Equations (8a)-(8b) give the exact full y-first Lambda sum and symmetric terminal H/I.

The all-width proof (9)-(14) counts the first half of the first quarter of the tribes. Their exact weighted pivotal mass is beta/2 per position, independent of query interleaving. Both child core means are bounded and their nonconstant coefficients are small, giving actual kappa_min>=7/16 through zero, one or two remaining x bits. Each good logarithm is at least w/4. Good nodes are neither symmetric leaves nor exact-zero-erasure nodes; monotonicity excludes a nonconstant disjoint spectator product. This proves w/64 without extrapolating any finite sweep. The exact y-first expansion yields w/2+O(1) with remainder bounded by 8/(3w ln2) before influence normalization.

The exact tribes entropy proves H(F)<=5I(F). True decrement B+JS and JS>=0 imply B_T+E Hleaf<=H(F); replacing leaf entropy by the same 9 Ileaf gives the 14I bill. Thus the scalar route loses an unbounded width factor even though true erasure and the admitted terminal cost stay paid.

The arbitrary-core guard (17) proves that the optimal universal erasure ratio is unchanged inside central-majority compositions with arbitrary balanced cores: use a fresh literal times k disjoint copies of any seed. Therefore a transport that discards core B or H is circular. The exact first unsupported universal line remains a hereditary retained-profile selection/stopping rule paying the actual erasure and terminal entropy by nonreused physical influence. This stage does not cover arbitrary adaptive permutations of y or a larger leaf class.

## executed validation with domain, arithmetic, commands and outputs

Before running, out/FROZEN_SPEC.json froze 14 mixed-family truth tables with m in {{2,4}}, w,t in 1..3, m+wt<=8, three orders and two stopping modes: **84 tree cases**. It also froze every Boolean core on k=0..3, m in {{2,4}}: **556 transport cases**. Before the follow-up equality check, out/FORMULA_EXTENSION_SPEC.json froze only the y-first closed-form extension on the same small domain.

Command: `python -X utf8 runs\\{run.name}\\code\\check_mixed.py`.

Final output: **{validation['exact_assertions']:,} exact assertions passed**, helper runtime **{validation['elapsed_seconds']:.3f} seconds**. The independent implementation uses integer FWHT and Fraction spectra, physical-edge influence, actual maximum-coefficient child defects, canonical exact B/Q/Lambda log-expression ledgers and exact leaf influence. The complete closed y-first Lambda expression and terminal H/I are matched against separately enumerated trees. Complete and stopped influence telescopes are exact.

Logarithms use 24-term rational atanh series after reduction to [1,2], proved tail 2*z^(2N+1)/((2N+1)*(1-z^2)), and outward dyadic rounding to 70 bits. Signed interval division uses all four corners. The resulting exact rational intervals are in out/VALIDATION.json, with full expressions in out/EXACT_LOG_LEDGERS.json. A numerical near-zero/interval-straddling check is diagnostic only; exact spectrum identities and analytic JS nonnegativity supply the zero/sign facts. No floating-point search establishes an all-width theorem. Estimated memory is 80 MB; no >300 MB job or automatic dimension escalation was used.

## proof dependencies and changed downstream conclusions

The two previous unreviewed A076 claim bundles are extended as v2 verification/repair results, rather than opening another broad candidate after the cap. The exact tribes spectrum and elementary Walsh/parity algebra supply the core proofs. The local Lambda definition is reused, but neither the pending retained-KL sandwich nor the lead's majority-divergence evidence is assumed as a proved dependency. The only external upper bound used is the symmetric-threshold leaf certificate <9 I.

B16/A077 receive an exact mixed-family counterexample to canonical-schedule scalar Lambda payment, beyond the lead's majority numerical warning. A078 receives the exact central-core B/M/Q/JS scaling and the defect-versus-profile gap it must repair. B06/B20 receive an explicit terminal-inclusive comparison and an arbitrary-core C018 admission guard. Independent review, adoption and downstream use have not yet been observed.

## one next mathematical action and independent reviewer

A092 (alternate A088) should reconstruct the kappa>=7/16 bound, the exact beta/2 prefix mass and the symmetric-stopping guard. The next mathematical step is the exact erasure correction in the shifted empty-core row after one x restriction (an OR/AND of the remaining x literal and arbitrary G), retaining B(G), actual descendant probabilities and terminal entropy. A profile-dependent payment must beat the scalar Lambda at these same noncentral nodes without assuming a certificate for the unknown arbitrary core.

## actual persistence receipts or precise save blocker

All four required protocol files, the proof, TeX summary, discrimination ledger, source pins, frozen specs, exact code and interval/log-expression outputs are saved in this assigned A076 run. STATUS.md, WORKLOG.md and LEARNED.md are updated only in A076. out/PERSISTENCE_RECEIPTS.json gives hashes and sizes after schema/readback checks. No git operation, external message, other-agent write, shared-index mutation, upload or mirror verification is claimed. All files are below 20 MB.

## Universal bridge

This stage moves **C019 stopping-tree payment** by decisively rejecting the lead's scalar child-defect bill on all three requested mixed-family orders: its terminal-inclusive cost grows at least w/64 times total influence (y-first w/2+O(1)), while the identical true-erasure/symmetric-leaf bill is at most 14I. It also supplies an exact **C018** admission guard: central-majority balanced-core compositions retain the unrestricted B/I supremum, so omitting core erasure cannot close FEI. What remains is a hereditary, nonreusing retained-profile payment through the shifted empty-core row and its terminal entropy for arbitrary cores. NEXT targets that first noncentral physical child because it is the shortest unresolved transport interface on a family that preserves full FEI difficulty; another isolated threshold/tribes constant would neither repair the divergent bill nor pay the universal core.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: A076 stage 2 complete locally: canonical majority-of-tribes Lambda/I>=w/64 (y-first w/2+O(1)); same true B+9 leafI<=14I; 53,949 exact checks; FEI OPEN, review pending.\nNEXT: A092/A088 verify kappa/prefix/stopping proof; derive shifted-empty-core erasure transport after one x restriction, retaining arbitrary core B and terminal entropy for C019/C018.\n',encoding='utf-8')
if not (agent/'WORKLOG.md').exists() or 'Stage 2 majority-of-tribes' not in (agent/'WORKLOG.md').read_text(encoding='utf-8'):
    with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} — Stage 2 majority-of-tribes: consumed B16 v2 lead direction and new board. Replaced isolated constant tests by actual Lambda/true-B/terminal comparison. Proved arbitrary-core central-majority spectrum/erasure scaling, exact y-first Lambda sum, w/64 all-width lower bound for canonical shuffles (survives symmetry/zero-erasure guards), and true bill <=14I with only symmetric-threshold leaves. All 556 core cases and 84 tree ledgers passed 53,949 exact assertions and rational log intervals. Saved two v2 bundles; universal profile transport and external review remain open.\n')
learned=agent/'LEARNED.md'
if 'Stage 2: retained-profile transport' not in learned.read_text(encoding='utf-8'):
    with learned.open('a',encoding='utf-8') as f:f.write('''

## Stage 2: retained-profile transport, 2026-10-11

- Follow B16 v2 direction: stage-1 whole-block K>=4 constants are dominated by spectator-tensored high-ratio cores and should not be reopened as a universal frontier.
- For even m, F=Maj_(m+1)(x,G)=g(x)+c(x)G with odd/even x Fourier supports. H(F)=H(Maj)+alpha H(G),I(F)=alpha(m+I(G)); data-coordinate B/M/Q/JS scale exactly by alpha. Balanced cores have all root x erasures zero and B(F)=alpha B(G). Full empty-core mass is essential.
- For m=2, H(F)=2+H(G)/2,I(F)=1+I(G)/2 and both data-split children have kappa=3/4 regardless of the core. Thus child kappa can fail to reflect the data erasure profile even without a spectator tensor.
- For t=2^w, even w>=16, every fixed shuffle of the two x queries with contiguous block-by-block y queries has Lambda/I>=w/64. This survives stopping at symmetric thresholds and skipping B=0 splits. Good-node kappa>=7/16, weighted pivotal mass beta/2, and nonsymmetry guards are explicit. Do not generalize to adaptive y permutations without proof.
- Exact y-first Lambda=(beta/2)sum_(j,u)log2(1+(3/4)*2^(u-1)*b^-(t-j-1)); symmetric stopping subtracts (beta/2)log2(7/4),EIleaf=1+beta/2,EHleaf=2. For t=2^w, Lambda/I=w/2+O(1).
- Same trees have B_T+9EIleaf<=14I from exact H(F)<=5I and entropy telescoping. The growing bill is the scalar majorant, not FEI or the actual erasure cost.
- Central-majority/balanced-arbitrary-core endpoint retains the universal erasure supremum: G=z times k disjoint seed copies makes B(F)/I(F)->B(seed)/I(seed). Any shortcut erasing the core conditional entropy is FEI-strength/circular.
- NEXT: the first noncentral x-child is OR/AND(x,G); derive its shifted empty-core erasure-row correction with core B and terminal entropy retained. This addresses C019's universal transport rather than another solved family constant.
- Validation: 556 all-core cases, 84 complete/stopped tree cases, 53,949 exact assertions; 24-term rational atanh logarithms with proved tails and 70-bit outward rounding. Interval-straddling zero checks are diagnostic, with analytic identities supplying sign/zero proofs.

Full derivation: runs/20261011T233829Z-fleet05-A076-threshold-and-tribes-controls/MIXED_TREE_PROOF.md. Independent A092/A088 review pending.
''')

required=json.loads((protocol_root/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
for c in claims:assert set(c)==set(required['claim_fields'])
assert set(progress)=={s.split(' (')[0] for s in required['progress_fields']}
assert all(field in report for field in required['report_fields'])
assert json.loads((run/'PACKET_DELTA.json').read_text())==json.loads((run/'PROGRESS.json').read_text())
assert report.rstrip().endswith('nor pay the universal core.')
assert len((agent/'STATUS.md').read_text().splitlines())==2
files=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        files.append(dict(path=str(p.relative_to(run)),size_bytes=p.stat().st_size,sha256=sha(p)))
save('out/PERSISTENCE_RECEIPTS.json',dict(saved_at_utc=now,schema_check='PASS',files=files,rolling_files=[dict(path=str(agent/n),sha256=sha(agent/n)) for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],independent_review='PENDING',external_mirror='NOT_OBSERVED'))
print(json.dumps(dict(run=str(run),saved_at_utc=now,files=len(files),claims='two v2 extensions',schema_check='PASS',exact_assertions=validation['exact_assertions']),indent=2))
