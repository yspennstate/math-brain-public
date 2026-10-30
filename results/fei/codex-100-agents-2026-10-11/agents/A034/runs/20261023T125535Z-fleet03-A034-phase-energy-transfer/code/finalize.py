from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
modes=['rows','controls','M2','M4a','M4b','M4c','direct']
results=[json.loads((R/'out'/f'{m}.json').read_text(encoding='utf8')) for m in modes]
assert all(x['status']=='PASS' and x['seconds']<55 for x in results)
assert results[0]['rows']==3834 and results[2]['states']==5097
assert sum(x['states'] for x in results[3:6])==8019 and results[-1]['states']==81
total=sum(x['assertions'] for x in results);maxsec=max(x['seconds'] for x in results)
cid='A034-AFFINE-PLANE-HEREDITARY-PHASE';version=3;cv=cid+'@3'
statement=('Let u be a signed sum of disjoint affine physical Y-cell indicators with intrinsic quadratic F2 phases, no complete cover required. Put mu=||u||_2^2, alpha=min nonzero component mass and R=mu/alpha. Then mu H(P_u)<=(log2(R)+1+log2(e)) E(u), and its complete row bill mu log2(1/mu)+mu H(P_u)<=(log2(R)+3+log2(e)) E(u). In particular FOUR equal-mass components have full coefficient5+log2(e)<13/2 independent of codimension or completion. For a Boolean F=sum_t 1_Ct (-1)^qt chi_{L(y)+J_t}(x), where the at most M affine phase cells partition independent uniform Y, have max codimension k, quadratic phases, arbitrary constant offsets J_t and a COMMON affine label map L of arbitrary rank, EVERY physical X/Y restriction satisfies H(S_Y|S_X)<=(k+log2(M)+1+log2(e)) I_Y and full H(F)<=(k+log2(M)+3+log2(e)) I_Y. Eight phase cells give full coefficient13+log2(e)<29/2 independently of carrier rank or number of frequency labels. At L=0 the stronger previous coefficient k+3+log2(e) is retained. Fresh Boolean data tensor factors have F2 degree<=k+2<=M+1; degree9 is sharp for eight cells. Arbitrary spectral correlations and optional integer X-degree bound d>=1 are allowed. Equal masses alone are NOT restriction-stable: actual Boolean row family A={s=0,u=0}, B={s=1,v=0} acquires ratio2^r after u=0.')
claim={'claim_id':cid,'version':version,'exact_statement':statement,
 'hypotheses':['Uniform independent physical X,Y cubes; bits entropy and original physical influence','Local rows: disjoint affine cells, unit quadratic signs; alpha>0; arbitrary proper union permitted','Stable class: complete affine phase partition of max codim k with <=M nonempty cells, common affine carrier L, constant label offsets','Constants depend on phase complexity or local mass ratio, not dimension, carrier rank or an actually satisfied optional integer X-degree cap'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
 'contributors':['A034; A033 bounded F2-degree minimum-weight mechanism credited and reconstructed'],
 'proof_source':'PROOF.md sections1-5','proof_dependencies':[],'review_records':[],
 'status':'AUTHOR_PROOF_EXACT_VALIDATION_PENDING_INDEPENDENT_REVIEW',
 'supersedes':['A034-AFFINE-PLANE-HEREDITARY-PHASE@2'],'refutes':[],
 'first_unproved_line':'Proper FOUR-cell rows of unbounded mass disparity without a bounded-complexity common-carrier source still have an unbounded log2(mu/alpha_min) loss. No absolute rate is proved for them. Equal-mass row payment alone is not hereditary. Full FEI and universal source/erasure/history conversion remain open.',
 'next_consumers':['A033','A079','A088','A094']}
dump(R/'CLAIMS.json',[claim])
artifacts=['PROOF.md','FROZEN_SPEC.json','code/check.py','code/finalize.py']+[f'out/{m}.json' for m in modes]+['out/source_receipts.json','out/protocol_validation.json','out/artifact_receipts.json']
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B07','packet_id':'A034','gap_id':'G-PHASE-COND','attempt_id':'A034-mass-relative-carrier-v3',
 'method':'Strengthen existing candidate: retain row mass in ternary derivative-gap entropy calculation; balance removes absolute codimension. Add common affine label carrier with exact row fiber mass ratio R<=M2^k. Reconstruct restriction closure, tensor guard and complete SAME-IY ledger.',
 'mathematical_delta':f'Closes equal-mass proper FOUR-cell rows without bounded-size completion at full coefficient5+log2(e)<6.5. Proves concrete restriction-stable common-carrier enlargement with arbitrary rank and unbounded nonempty X labels: eight PHASE cells have full coefficient13+log2(e)<14.5. Old constant-label rate<11.5 remains available. Exact family disproves automatic hereditary equal-mass admission. {total} exact assertions PASS.',
 'deliverable_status':'COMPLETE_LOCAL_PROOF_AND_EXACT_CERTIFICATES',
 'mathematical_status':'EXISTING_RESTRICTED_CANDIDATE_STRENGTHENED_PENDING_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':['A034-AFFINE-PLANE-HEREDITARY-PHASE@2 as prior source/gap locator; proof rederived self-contained','A033 bounded F2-degree mechanism credited, minimum-weight argument reconstructed'],
 'claims_created_or_changed':[cv],'source_artifacts':artifacts,
 'next_consumers':['A033','A079','A088','A094'],
 'next_action':'A079/A033 reconstruct mu-relative influence gap and common-carrier row intersections; A088/A094 audit all physical restrictions, tensor guard and full original influence ledger. Then remove log2(mu/alpha_min) from the COMPLETE bill of unequal proper FOUR-cell rows with no two-cell coarsening and no bounded-complexity carrier certificate.',
 'stagnant_substantive_attempts':0,
 'blockers':['Independent proof review and supervisor mirror verification pending','Unequal proper FOUR-cell mass-disparity loss remains; full FEI OPEN','Brain self-care degraded/unverified: stale personal owner/state/dream notes; not mathematical dependencies'],
 'packet_ids':['A034']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
sources=[Path('BOARD.md'),Path('claude/B07/STREAM_NOTES.md'),Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),A/'runs/20261023T105619Z-fleet03-A034-phase-energy-transfer/PROOF.md',A/'runs/20261023T105619Z-fleet03-A034-phase-energy-transfer/code/check.py']
dump(R/'out/source_receipts.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
descriptions={'rows':'3834 certified equal-mass rows, nY0..3, <=4 singleton/line pieces','controls':'16 exact restriction-instability parameters; point defect, nonBoolean, tensor controls','M2':'5097 states; two phase cells, common carrier ranks0..4','M4a':'2673 four-phase-cell states; first X bit free','M4b':'2673 four-phase-cell states; first X bit fixed0','M4c':'2673 four-phase-cell states; first X bit fixed1','direct':'All81 X restrictions, independent full Boolean Walsh coefficients and original IY'}
table='\n'.join(f'| {x["mode"]} | {descriptions[x["mode"]]} | {x["assertions"]} | {x["seconds"]:.3f} |' for x in results)
report=f'''# A034 stage20: balanced proper fibers and a stable affine carrier

## Exact target, quantifiers, hypotheses and units

Advance G-PHASE-COND for actual Boolean signs on disjoint independent uniform physical X,Y cubes, entropy bits and original physical I_Y. Retain full H(S_Y|S_X), arbitrary spectral correlations and optional integer occupied-label X-degree cap d>=1. Version3 strengthens the EXISTING candidate rather than opening another broad pending candidate. Local signed quadratic affine rows need not cover Y and need no bounded-size affine completion. If mu is row mass and alpha its smallest component mass, their FULL conditional bill is <=(log2(mu/alpha)+1+log2(e)) E; adding row mass entropy costs only2E on the SAME account. Four equal-size cells therefore have full coefficient5+log2(e)<6.5 independently of codimension.

The concrete stable class allows a COMMON affine label map L(y), arbitrary rank, added to cellwise offsets J_t on a complete partition into at most M quadratic-phase affine cells, max codimension k. Every physical restriction has full coefficient k+log2(M)+3+log2(e), and conditional coefficient two less. Eight PHASE cells have full coefficient13+log2(e)<14.5 regardless of number of X labels. The stronger constant-label stage19 rate<11.5 is retained when L=0. Zero-energy states satisfy non-strict entropy inequalities.

## Sources actually read, revisions and theorem locators

BOARD.md supervisor12:58 UTC, B07 STREAM_NOTES.md v2 (2026-10-11 23:45), own STATUS.md; stage19 proof/checked helper retained and reused as a pinned definition library. The complete protocol is read for exact schema validation. Earlier papers/campaign baseline were consumed in prior stages; no unseen paper theorem is imported. B07 requires nonBoolean and vacuous-embedding guards; both addressed below. Board still lists A034 v2 as pending review. Source hashes are at receipt time in out/source_receipts.json. User deadline14:49 UTC supersedes old campaign metadata. Current sources, rather than stale personal brain notes, support this work.

## Complete derivation or exact first unsupported line

PROOF.md supplies every step. For a row u=a-2b, support and negative bits have F2 degrees<=K,K+2, where alpha=2^-K. A nonzero support derivative costs >=alpha/2 after the factor1/4; if the support derivative vanishes identically, row influence equals the weight of the negative-bit derivative and has the SAME lower bound. Crucially retain mu in mu h2(p_i/mu)<=p_i log2(e mu/p_i). This replaces the old absolute codimension loss with log2(mu/alpha). The exact support edge-isoperimetry induction pays mass entropy with2E(u). No spectral independence or component-energy comparison is used.

For a common carrier of rank r, every nonempty label fiber has mass2^-r. Intersecting a phase cell adds at most k equations, so the smallest row piece has mass>=2^(-(r+k)). At most M pieces each have mass<=2^-r, hence mu/alpha<=M2^k. Summing COMPLETE row bills gives EXACT full H(F), and sum E(u_J)=I_Y(F), verified independently by full-F Walsh coefficients. All old debts are in this terminal bill; this is not a reusable query reserve.

Physical X restrictions project the common carrier and offsets, adding only affine cell phases. Physical Y restrictions retain the affine phase partition and do not increase codimension. Thus the common-carrier class is hereditary. A fresh Boolean data tensor factor has F2 phase degree<=k+2<=M+1; degree9 is sharp for eight phase cells, degree10 excluded. The three-bit point defect is admitted. The normalized nonBoolean psi_(2^15) has H=15,I=1 and violates the eight-phase-cell coefficient<14.5; unit-phase admission fails there.

Equal-size rows alone are NOT hereditary: disjoint A={{s=0,u=0}}, B={{s=1,v=0}} have equal mass2^(-(r+1)), but restricting u=0 leaves masses1/2 and2^(-(r+1)). This is realized by an actual Boolean degree-one-address completion. Its ratio2^r disproves the unrestricted stability claim, not FEI. The first unpaid line is removing the unbounded log2(mu/alpha) loss for unequal proper FOUR-cell rows with no two-piece coarsening or bounded-complexity common-carrier source.

## Executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes searches and fixes all domains; before running M4 its SAME8019 states were partitioned into three runtime groups by first X state. Each job was under55 seconds and estimated70MB; no >300MB job/Lean compiler/GPU/detached work was launched, and no memok admission was needed. Commands: `python -B -X utf8 code/check.py MODE`, sequential fixed modes. Definitions from the stage19 helper are loaded without executing its modes; each output records that dependency's SHA256.

| Mode | Exact domain | Assertions | Seconds |
|---|---|---:|---:|
{table}

All {total:,} exact assertions PASS; max measured job time{maxsec:.3f}s. Integer Walsh transforms, physical squared differences, exact Fraction identities, ANF degrees and rational entropy/log intervals are used. The interval bound sums14 positive atanh terms with a geometric remainder; dyadic logs are exact. Canonical singleton/line certificates prove the row domain, rather than treating floating spectra as proof. All X restrictions are covered; the M2 Y domain fixes at most1 coordinate and M4 at most2, explicitly NOT an exhaustive high-dimensional restriction claim. The all-restriction theorem is analytic. Direct full-F checks use all81 X restrictions of the four-phase fixture. The two-phase rank4 fixture has32 nonempty frequency rows despite only TWO phase cells, exceeding the old8-total-cell class.

## Proof dependencies and changed downstream conclusions

No external proof dependency: ternary encoding, polynomial minimum weight, row mass payment, common-fiber rank counting, exact entropy ledger, restriction closure and tensor guard are reconstructed. A033's bounded-degree mechanism is credited. Version3 supersedes the previous candidate's main scope and retains its sharper L=0 subcase. It adds a codimension-free balanced proper-row payment and a concrete stable enlargement with arbitrarily many address labels. It does not turn equal-mass admission into a hereditary rule. Full FEI remains OPEN; exact checks and author proof do not substitute for independent review.

## One next mathematical action and independent reviewer

A079/A033 reconstruct the negative-bit gap with retained row mass and common-carrier fiber intersection bounds. A088/A094 audit restriction closure, full SAME-IY ledger, zero states and degree guard. Next mathematical action: remove log2(mu/alpha_min) from the COMPLETE entropy bill of unequal proper FOUR-cell rows without two-piece coarsening or a bounded-complexity carrier certificate, by charging scale-dependent terms to actual signed physical energy. No messages were sent and no peer/source tree modified.

## Actual persistence receipts or precise save blocker

Proof, frozen spec, code, seven PASS outputs and four protocol files saved in this A034 run. Rolling STATUS is two lines, and WORKLOG/LEARNED append this stage. out/protocol_validation.json checks exact field sets and byte-identical PROGRESS/PACKET_DELTA; out/artifact_receipts.json supplies SHA256 and sizes for every completed run file except itself. Each file<20MB. Independent acceptance, supervisor copying/mirror/public release remain unverified. No mathematical job remains running. Brain self-care is degraded/unverified: owner-model99.4h, state-of-mind84.0h, dream34.7h at wake; guidance relying on those notes remains affected, not the self-contained proof.

## Universal bridge

G-PHASE-COND advances by paying arbitrary-codimension equal-mass proper FOUR-cell rows without bounded affine completion at full coefficient5+log2(e)<6.5, and by adding a concrete all-restriction common-affine-carrier class whose phase complexity, not address-label count or carrier rank, controls the full entropy rate. This retains BOTH the full conditional spectrum and SAME physical influence ownership; no universal C018/C019 conversion follows. The exact remaining loss is log2(mu/alpha_min) for unbalanced proper four-cell fibers. NEXT attacks that mass-disparity loss directly, the shortest extension of the same row interface toward arbitrary-core phase sources, rather than changing to an unrelated isolated class.
'''
(R/'REPORT.md').write_text(report,encoding='utf8')
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
cf=set(protocol['required_per_run']['claim_fields']);pf={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(claim)==cf and set(progress)==pf
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
dump(R/'out/protocol_validation.json',{'status':'PASS','exact_claim_fields':True,'exact_progress_fields':True,'packet_delta_identical':True,'all_outputs_PASS':True,'total_assertions':total})
(A/'STATUS.md').write_text(f'STATE: A034 stage20 v3 saved: proper equal-mass FOUR-cell rows paid codimension-free full rate<6.5; stable common affine carrier has arbitrary rank/label count and fixed phase rate;{total} exact assertions PASS; review pending; FEI OPEN.\nNEXT: A079/A033/A088/A094 review mu-relative row gap, carrier fiber ratio and SAME-IY full ledger; remove log(mu/alpha_min) for unequal proper FOUR-cell rows without bounded-complexity completion/carrier.\n',encoding='utf8')
log=f'\n2026-10-23 stage20 ({R.name}): Saved v3 existing-candidate proof: retain mu in entropy gap to get local complete rate log2(mu/alpha_min)+3+log2(e), paying four equal-mass cells at coefficient<6.5 regardless of codimension. Exact actual-Boolean restriction family disproves automatic mass-balance closure. Added concrete common affine label carrier on bounded phase partition; R<=M2^k gives full rate k+logM+3+loge independent of carrier rank or number of labels, stable under all physical restrictions. Tensor guard degree<=M+1 retained. {total} exact assertions PASS in fixed jobs; source/schema/hash receipts saved, review/mirror pending, no jobs remain. Next unpaid: unbalanced proper FOUR-cell log-mass-ratio loss.\n'
learn=f'\n2026-10-23 stage20 AUTHOR PROOF (review pending): Disjoint affine quadratic rows of smallest cell mass alpha have nonzero influences>=alpha/2. Retaining row mass yields mu H(Pu)<=(log2(mu/alpha)+1+log2(e))E and complete bill with +2E. Equal-size s-cell rows therefore have codimension-free rate log2(s)+3+loge; s4 gives<6.5. Balance alone is not hereditary: equal A=(s0,u0),B=(s1,v0) acquire ratio2^r after u0. Concrete stable enlargement: F phase-partitioned into M affine quadratic cells of max codim k, label L(y)+J_t with COMMON affine L; rank-r fibers have mass2^-r, row intersections>=2^(-(r+k)), so mu/alpha<=M2^k and full rate k+logM+3+loge. Common carrier survives all physical restrictions and does not relax tensor guard degree<=k+2<=M+1. Two phase cells can support2^(r+1) nonempty frequency labels, so fixed-phase complexity is stronger than bounded total cells. Remaining universal loss is unbounded mass disparity in proper four-cell rows, not absolute codimension for balanced rows. {total} exact assertions PASS; no independent acceptance claimed.\n'
for name,entry in [('WORKLOG.md',log),('LEARNED.md',learn)]:
 p=A/name;existing=p.read_text(encoding='utf8')
 if '2026-10-23 stage20' not in existing:
  with p.open('a',encoding='utf8') as f:f.write(entry)
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='artifact_receipts.json':
  assert p.stat().st_size<20*1024*1024
  receipts.append({'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size})
dump(R/'out/artifact_receipts.json',receipts)
print(json.dumps({'status':'PASS','claim':cv,'assertions':total,'max_job_seconds':maxsec,'artifacts':len(receipts)+1,'independent_review':'PENDING','full_FEI':'OPEN'}))
