from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
def read(p):return p.read_text(encoding='utf-8')
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(b):return hashlib.sha256(b).hexdigest()
results={m:json.loads(read(RUN/'out'/f'{m}.json')) for m in ['rows','scales','carrier','audit','symbolic','carrier_short']}
assert all(x['status']=='PASS' for x in results.values())
assert all(results[m]['helper_sha256']==sha((RUN/'code/check.py').read_bytes()) for m in ['rows','scales','carrier','audit'])
assert results['symbolic']['helper_sha256']==sha((RUN/'code/symbolic.py').read_bytes())
total=sum(v['assertions'] for v in results.values())
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
statement=('For every integer s>=1 and every ternary row u on a finite uniform physical cube that is a signed sum of at most s disjoint affine-cell indicators with intrinsic quadratic phases, '
           'B(u)=sum_T uhat(T)^2 log2(1/uhat(T)^2) <= K_s E(u), where K_s=2s[log2(s)+(s-1)log2(64s^2)+3+log2(e)]. '
           'No bound on codimension, cell mass ratios, or spectral correlations is assumed. Thus any Boolean F(x,y) partitioned into at most M affine physical Y cells with a quadratic phase and an arbitrary CELL-DEPENDENT affine X-label map on each cell satisfies H(F)<=K_M I_Y(F) and H(S_Y|S_X)<=K_M I_Y(F), under every mixed physical restriction. '
           'The complete source class also has H(F)<=2^(M+1)I_Y and H(S_Y|S_X)<=2^M I_Y by the elementary bounded-phase/active-Y argument, so its better full rate is min(K_M,2^(M+1)). '
           'The optional integer X-degree bound d>=1 is retained when present. Fixed-M admission excludes fresh Boolean data tensor factors of F2 phase degree above M+1. Proper FOUR-cell rows have K_4=280+8log2(e)<292; complete four-phase-cell sources also have full rate32.')
claim=dict(claim_id='A034-AFFINE-PLANE-HEREDITARY-PHASE',version=4,exact_statement=statement,
           hypotheses=['independent uniform disjoint physical X,Y cubes','actual Boolean sign F','disjoint affine physical row cells','intrinsic quadratic phase on each cell','at most s pieces per row; at most M source phase cells for the hereditary corollary','all logarithms base two'],
           statement_sha256=sha(statement.encode('utf-8')),contributors=['A034'],proof_source='PROOF.md sections 1-5',
           proof_dependencies=[],review_records=[],status='AUTHOR_PROOF_REVIEW_PENDING',supersedes=['A034-AFFINE-PLANE-HEREDITARY-PHASE@3'],refutes=[],
           first_unproved_line='No influence-priced bounded-piece decomposition of an arbitrary Boolean core; no bound independent of s. Independent reconstruction pending.',
           next_consumers=['A079','A033','A088','A094','B07','B20'])
save(RUN/'CLAIMS.json',[claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=RUN.name,stream='B07',packet_id='A034',gap_id='G-PHASE-COND',
              attempt_id='A034-stage21-mass-clusters-v4',method='Group adjacent dyadic cell masses; derivative gap protects group energy; coherent entropy comparison retains full row bill.',
              mathematical_delta='Removes unbounded log(mu/alpha_min) for ANY fixed-s proper quadratic affine row; permits different affine carriers and ranks on source cells while preserving all physical restriction histories.',
              deliverable_status='COMPLETE_LOCAL',mathematical_status='RESTRICTED_AUTHOR_PROOF; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING',
              claim_versions_used=[],claims_created_or_changed=[claim['claim_id']+' v4'],source_artifacts=['PROOF.md','FROZEN_SPEC.json','FROZEN_SYMBOLIC.json','FROZEN_CARRIER_SHORT_BOUND.json','code/check.py','code/symbolic.py','code/carrier_short.py','out/rows.json','out/scales.json','out/carrier.json','out/audit.json','out/symbolic.json','out/carrier_short.json','out/lean_result.json'],
              next_consumers=claim['next_consumers'],next_action='A079/A033 reconstruct grouped-energy and coherent-entropy proof; then remove s-dependence or influence-price an arbitrary-core bounded-piece decomposition.',
              stagnant_substantive_attempts=0,blockers=['Independent review not performed','Lean admission held before compilation: compute status distressed or unknown','No universal control of growing row piece count'],packet_ids=['A034'])
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
table='\n'.join(f"| {m} | {v.get('rows',v.get('states',v.get('cases',len(v.get('fixtures',[])))))} | {v['assertions']} | {v['seconds']:.3f} |" for m,v in results.items())
report=f'''# A034 stage21: remove the unequal-mass loss

## exact target, quantifiers, hypotheses and units

{statement}

The row theorem has no affine-completion hypothesis. This stage strengthens the existing phase-row mechanism, rather than opening an unrelated broad candidate. The old balanced-four-cell coefficient below6.5 remains valid on its sharper domain; the new coefficient below292 covers arbitrary mass disparity. Full FEI is OPEN. Rung: author proof with exact finite certificates, external review pending; NOT Lean-checked.

## sources actually read, revisions and theorem locators

The complete EXECUTION_PROTOCOL.json v2, current BOARD B07/B18/B19/B20 entries, B07 STREAM_NOTES v2, own rolling files and stage20 REPORT/PROOF/code; canonical README/CURRENT_STATUS, claim/obstruction/packet/dispatch registries; supplemental CAMPAIGN, CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and source inventory; campaign plan opening and current owner control. Paper text searches were limited to baseline/affine/shared-data locators across all four text versions. Earlier stages supply the prior full-paper recovery; no unseen paper theorem is used here. Source receipts distinguish actual source files and targeted reads. The proof is self-contained. The brain query returned the existing nonBoolean-control and mass-weighted-entropy gap cards, not the new result. The wake reported stale personal-state/dream notes, which are not mathematical premises. The current direct stage invocation authorizes this continuation beyond the historical campaign endpoint; no schedule or endpoint was changed.

## complete derivation or exact first unsupported line

PROOF.md supplies the derivation. Nonzero derivative energy of a grouped ternary quadratic-cell row is at least half its smallest cell mass. Split sorted masses at ratio64s^2. Within-group mass ratio is at most(64s^2)^(s-1). Across groups, the first nonzero derivative has tail norm at most one quarter its own norm; the reverse triangle and exact tail-energy bound give E(u)>=1/2 sum_g E(v_g). This is a GROUP comparison: the false ungrouped comparison is explicitly rejected by a constant two-cell cover. Physical disjointness makes grouped Fourier laws have the same total norm; Cauchy--Schwarz, Gibbs and mixture entropy give B(u)<=q sum_g B(v_g), keeping BOTH normalized conditional entropy and row-mass entropy. The combined constant is K_s above.

For cell-dependent affine carriers every row has at most M affine intersections, even when ranks and fiber masses differ. Sum complete row bills and use exactly sum_J E(u_J)=I_Y(F). X restrictions project the individual maps and add affine phases; Y restrictions intersect cells and restrict quadratic phases. Every history retains the same M. Fixing all old variables forces any fresh Boolean data tensor factor to have phase degree<=M+1; AND_(M+2) is excluded. The three-bit point defect is admitted; normalized psi_N violates any fixed rate for large N and fails ternary/unit-phase admission. Physical input laws remain uniform product laws.

For COMPLETE sources there is also a simpler small-M bound, credited to the bounded-phase mechanism: global F2 phase degree<=M+1 makes every nonzero Y influence>=2^-M. If N Y coordinates are essential then N<=2^M I_Y; the X spectral marginal is the deterministic label law and has entropy<=N, while the conditional Y entropy is<=N. This gives full rate2^(M+1), or32 atM4. The proper-row rate below292 has weaker hypotheses; the polynomial K_M eventually improves the elementary exponential source bound. Both rates and their hypotheses are retained explicitly.

First unsupported universal line: an arbitrary Boolean core need not have bounded row piece count, and no original-influence-priced bounded-piece decomposition is proved. Taking singleton cells can have M=2^n. The theorem therefore supplies no dimension-independent universal FEI constant.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json, FROZEN_SYMBOLIC.json and FROZEN_CARRIER_SHORT_BOUND.json precede their respective searches. Commands are `python -B -X utf8 code/check.py MODE` for rows/scales/carrier/audit, `python -B -X utf8 code/symbolic.py` and `python -B -X utf8 code/carrier_short.py`. All arithmetic is integer/Fraction, including rational logarithm intervals from16 positive atanh terms with a geometric remainder. Entropy upper intervals are checked against LOWER bounds on the claimed constants; this is not a floating-point sign check. Single-group entropy equality is checked as vector identity. The analytic proof supplies the all-dimensional conclusion.

| Job | States/fixtures | Exact assertions | Seconds |
|---|---:|---:|---:|
{table}

Total: {total:,} exact assertions PASS. The exhaustive row domain is nY0..3 with canonical singleton quadratic cells (6654 ternary rows including zero); it is not all higher-dimensional affine geometry. Eight dense unequal-scale two-cell fixtures use nY8..11. The actual Boolean differing-carrier fixture has nX2,nY4 and all729 physical mixed restrictions, independently checked through full-F integer Walsh coefficients and direct physical differences. The short-bound job checks the SAME729 restrictions for actual global ANF degree<=3, nonzero Y influence>=1/4 and full rate8. The symbolic36-coordinate certificate checks256 signed four-cell rows, with1/2/3/4 mass groups and maximum codimension34, by a second implementation using exact shifted physical intersections. It does not enumerate2^36 points. Runtime per job stays below55 seconds and memory estimate below40MB. No automatic dimension escalation, GPU, remote compute, detached job or large artifact was used.

Fresh memok returned physical free7.7GB and commit free10.4GB before the formal attempt. The subsequent Lean wrapper independently held admission with `SETUP_UNVERIFIED: Compute status is distressed or unknown`, exit2; no compiler certificate resulted. The proposed core theorem formalizes only integer-denominator rounding from9 first<=16 energy and32 summed<=33 first to summed<=2 energy; it does not formalize the Fourier/entropy theorem. Its source and held receipt are saved. No failed formal attempt is counted as mathematical validation.

## proof dependencies and changed downstream conclusions

No externally accepted theorem is assumed: the derivative gap, support isoperimetry, coherent entropy and full ledger are reconstructed. Stage20's explicit unequal-four-cell mass-disparity obstruction is now removed at fixed piece count. Its common-carrier restriction is replaced by arbitrary independent affine carriers on the phase cells; its sharper balanced/common-rank constants remain available. The next gap is growing piece count, not unbounded codimension or mass disparity at fixed count. This is one strengthening of the existing pending candidate, not an acceptance of earlier unreviewed versions.

## one next mathematical action and independent reviewer

A079/A033 should reconstruct the first-nonzero-group reverse triangle and the entropy domination argument without relying on the checker. A088/A094 should challenge physical-restriction closure, tensor guard, empty/constant rows and SAME-IY ownership. No peer has yet reviewed this version and no messages or external writes were sent. After reconstruction, remove piece-count dependence or prove an original-influence-priced bounded-piece decomposition for arbitrary Boolean cores; further balanced-only cases no longer address the frontier.

## actual persistence receipts or precise save blocker

The four protocol artifacts, complete proof, three frozen specifications, code and six PASS outputs are saved inside this run. PROGRESS/PACKET_DELTA match byte-for-byte, with packet_ids=[A034]. out/protocol_validation.json checks exact field sets; out/artifact_receipts.json records SHA256 and sizes. STATUS.md has exactly two lines; WORKLOG and LEARNED append this stage. All files are below20MB. Local persistence is verified; supervisor copying, GitHub/brain mirrors, independent acceptance and public release are not claimed. No brain store, shared tree or other agent folder was modified.

## Universal bridge

G-PHASE-COND advances from a mass-relative conditional estimate to a codimension-free COMPLETE row payment for every fixed number of disjoint quadratic affine pieces, including arbitrary unequal proper FOUR-cell fibers. It also gains a hereditary cell-dependent-affine-carrier class with unbounded labels and unrelated carrier ranks. The precise remaining universal cost is K_s=O(s^2 log s) as the piece count grows; no C018 erasure or C019 stopping bank is funded by merely restating this bound. NEXT targets piece-count-independent signed cancellation or an influence-priced bounded-piece decomposition because that is the remaining obstruction in the same full-entropy interface to arbitrary Boolean cores.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(ROOT/'STATUS.md').write_text('STATE: A034 stage21 v4 saved: ALL unequal fixed-s quadratic affine rows have codimension-free COMPLETE transfer; independent cellwise affine carriers hereditary; '+str(total)+' exact assertions PASS; review pending, Lean held; FEI OPEN.\nNEXT: A079/A033/A088/A094 reconstruct group energy/coherent entropy/SAME-IY closure; remove growing piece-count cost or influence-price an arbitrary-core bounded-piece decomposition.\n',encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' stage21: mass clustering closes unequal proper-four-cell row gap, K4<292; different affine carriers/ranks permitted per phase cell under every physical restriction. '+str(total)+' exact assertions PASS; independent symbolic36-bit1..4-group check included; Lean admission held, independent review pending. Full FEI OPEN.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' stage21 AUTHOR PROOF, review pending: For <=s disjoint affine quadratic ternary pieces, COMPLETE B(u)<=2s[log2s+(s-1)log2(64s^2)+3+loge]E(u), arbitrary mass disparity/codimension/proper support. Cluster adjacent masses at gap>64s^2; group derivative gap alpha_min/2 plus first-active dominance gives Etotal>=half sum Egroup. Coherent entropy Btotal<=#groups sum Bgroup retains row-mass entropy. NEVER compare original component energies: constant covers refute that. Consequently <=M source phase cells may each have their OWN affine label carrier/rank; all mixed physical restrictions pay SAME IY with K_M, guard degree<=M+1. Old balanced rate<6.5 retained; new general FOUR-cell rate<292 is looser on a larger domain. Remaining universal loss is piece-count dependence O(s^2 log s), not mass disparity. '+str(total)+' exact assertions PASS; no Lean/independent acceptance.\n')
protocol=json.loads(read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')))
fields=protocol['required_per_run']
expected={x.split(' (')[0] for x in fields['progress_fields']}
assert set(progress)==expected
assert set(claim)==set(fields['claim_fields'])
assert all(x in report for x in fields['report_fields'])
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len(read(ROOT/'STATUS.md').splitlines())==2
save(RUN/'out/protocol_validation.json',dict(status='PASS',progress_fields=sorted(expected),claim_fields=fields['claim_fields'],report_fields=fields['report_fields'],compatibility_copy_identical=True,total_exact_assertions=total,timestamp=stamp))
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='artifact_receipts.json']
assert all(p.stat().st_size<20_000_000 for p in files)
save(RUN/'out/artifact_receipts.json',[dict(path=str(p.relative_to(RUN)),bytes=p.stat().st_size,sha256=sha(p.read_bytes())) for p in files])
print(json.dumps(dict(status='COMPLETE_LOCAL',assertions=total,files=len(files)+1,claim=claim['claim_id'],full_fei='OPEN')))
