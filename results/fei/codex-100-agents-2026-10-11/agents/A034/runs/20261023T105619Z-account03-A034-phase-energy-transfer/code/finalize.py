from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def dump(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
results=[json.loads((R/'out'/f'{mode}.json').read_text(encoding='utf8')) for mode in ('ternary','fixture7','fixture9','masses','direct')]
assert all(r['status']=='PASS' and r['seconds']<55 for r in results)
total=sum(r['assertions'] for r in results)
assert total==1187798
claim_id='A034-AFFINE-PLANE-HEREDITARY-PHASE';cid=claim_id+'@2'
statement=('For independent uniform physical X,Y cubes, let C_t be a complete partition of Y into affine cells of maximum codimension k, with quadratic F2 cell phases q_t and arbitrary possibly repeated X-frequency labels J_t. The Boolean F=sum_t chi_Jt 1_Ct (-1)^qt and every physical X/Y restriction satisfy H(S_Y|S_X)<=(k+1+log2(e)) I_Y(F) and H(F)<=(k+3+log2(e)) I_Y(F). A partition into at most m cells has k<=m-1, hence full coefficient m+2+log2(e)<m+7/2. In particular arbitrary eight-cell partitions have full coefficient10+log2(e)<23/2, covering intermediate proper nonaffine four-cell collisions with no two-piece coarsening. Four-cell partitions have full coefficient6+log2(e)<15/2. Every fresh Boolean tensor factor in the fixed-k class has F2 degree<=k+2; for at most m cells the bound m+1 is sharp. The theorem retains full conditional entropy, arbitrary spectral correlations and any optional integer X-degree bound d>=1, and uses only original physical I_Y.')
claim={
 'claim_id':claim_id,'version':2,'exact_statement':statement,
 'hypotheses':['Independent uniform physical X,Y cubes; entropy in bits; original physical influence','Complete disjoint affine partition of Y with maximum cell codimension k; intrinsic quadratic cell phases','Arbitrary X-frequency labels, repetitions allowed; optional integer occupied-label degree cap d>=1','Constants depend on k or the cell-count bound, and not on dimension or d'],
 'statement_sha256':hashlib.sha256(statement.encode('utf8')).hexdigest(),
 'contributors':['A034; bounded F2-degree influence-gap mechanism credited to A033; version2 uses ternary support/negative-bit encoding and reconstructs every proof step'],
 'proof_source':'PROOF.md sections1-6','proof_dependencies':[],
 'review_records':[], 'status':'AUTHOR_PROOF_EXACT_VALIDATION_PENDING_INDEPENDENT_REVIEW',
 'supersedes':['A034-AFFINE-PLANE-HEREDITARY-PHASE@1 main rate24 and four-label representation; old sharper rank-specific subcases remain valid'],
 'refutes':[],
 'first_unproved_line':'No codimension-independent complete row entropy/energy payment is proved for four arbitrary signed affine quadratic cells on a proper nonaffine support without a bounded-size affine completion. Replacing the absolute derivative gap by a dimension-free signed structural payment is open. Full FEI and history/reference conversion remain open.',
 'next_consumers':['A033','A079','A088','A094']}
dump(R/'CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B07','packet_id':'A034','gap_id':'G-PHASE-COND',
 'attempt_id':'A034-ternary-affine-collision-v2',
 'method':'Repair/strengthen the existing hereditary phase candidate using support bit a and negative bit b, row identity u=a-2b, F2 derivative minimum weight, entropy subadditivity and exact mass-isoperimetry ledger; no component-energy comparison',
 'mathematical_delta':'Closes proper nonaffine noncoarsenable four-cell fibers in ANY complete eight-cell affine partition at all physical restriction states, with full coefficient10+log2(e)<11.5 and conditional coefficient8+log2(e)<9.5. Extends to arbitrary fixed maximum codimension k and arbitrary labels; improves the former four-cell full rate24 to6+log2(e)<7.5. Sharp degree9 tensor guard for eight cells; arbitrary tensors excluded. 1187798 exact assertions PASS.',
 'deliverable_status':'COMPLETE_LOCAL_PROOF_AND_EXACT_CERTIFICATES',
 'mathematical_status':'EXISTING_RESTRICTED_CANDIDATE_STRENGTHENED_PENDING_INDEPENDENT_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':['A034-AFFINE-PLANE-HEREDITARY-PHASE@1 as gap locator only; new proof self-contained','A033 bounded F2-degree mechanism reconstructed rather than assumed'],
 'claims_created_or_changed':[cid],
 'source_artifacts':['PROOF.md','FROZEN_SPEC.json','code/check.py','code/finalize.py']+[f'out/{r["mode"]}.json' for r in results]+['out/source_receipts.json','out/artifact_receipts.json','out/protocol_validation.json'],
 'next_consumers':['A033','A079','A088','A094'],
 'next_action':'A079/A033 independently reconstruct the support/negative-bit influence gap and full entropy ledger; A088/A094 audit same original influence, zero-energy states and tensor guard. Then obtain a codimension-free complete-row bound for FOUR signed quadratic affine cells without bounded-size completion, replacing the absolute influence cutoff with a cancellation-sensitive payment.',
 'stagnant_substantive_attempts':0,
 'blockers':['Independent review pending; no claim of independent acceptance','Four-cell payment without bounded-size affine completion and full FEI remain open','Supervisor mirror/publication not verified','Brain self-care degraded: stale owner model, state-of-mind and dream; current mathematics uses campaign sources'],
 'packet_ids':['A034']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
sources=[
 Path('BOARD.md'),
 Path('claude/B07/STREAM_NOTES.md'),
 Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),
 A/'runs/20261023T032301Z-account03-A034-phase-energy-transfer/PROOF.md',
 A/'runs/20261023T032301Z-account03-A034-phase-energy-transfer/CLAIMS.json',
 A/'runs/20261023T032301Z-account03-A034-phase-energy-transfer/PROGRESS.json']
dump(R/'out/source_receipts.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
report=f'''# A034 stage19: proper four-cell fibers paid by ternary phase encoding

## Exact target, quantifiers, hypotheses and units

Advance G-PHASE-COND on actual Boolean signs on disjoint independent uniform physical X,Y cubes, retaining FULL H(S_Y|S_X), entropy bits and original physical I_Y. Repair/strengthen the existing candidate to version2; no third broad candidate is opened while two earlier author proofs await independent review. For ANY complete affine partition with maximum cell codimension k and quadratic cell phases, with ANY repeated X-frequency labels, prove Hcond<=(k+1+log2(e)) I_Y and full H<=(k+3+log2(e)) I_Y at every mixed physical restriction. Optional integer X-degree d>=1 is retained and absent from the constant. At most m cells imply k<=m-1. Thus EIGHT cells have full coefficient10+log2(e)<23/2; FOUR have6+log2(e)<15/2, improving old24. Rational-rate inequalities use <=, including zero-energy states.

## Sources actually read, revisions and theorem locators

Current BOARD.md supervisor10:53 UTC, B07 STREAM_NOTES.md v2 (2026-10-11 23:45), own STATUS.md, full execution protocol revision2026-10-11-execution-v2, and stage18 PROOF.md sections1-6/first unsupported line plus its claims/progress/check helper. The earlier required papers and campaign baseline remain previously consumed sources; this proof imports no unquoted theorem from them. Machine-wide rules were consulted; task-specific read-only/no-git/output scope prevails. Board reveals no independent acceptance of A034 stage18. Source hashes are in out/source_receipts.json. Current user campaign deadline14:49 UTC supersedes older protocol dates.

## Complete derivation or exact first unsupported line

Complete self-contained proof is PROOF.md. A collided row u in {{0,+1,-1}} has support bit a and negative bit b, with INTEGER identity u=a-2b. Disjoint affine supports imply deg_F2 a<=k, deg_F2 b<=k+2. On a coordinate with nonzero support derivative, the boundary has weight>=2^(-(k-1)) and row influence>=2^(-(k+1)). If the support derivative vanishes identically, row influence is exactly the weight of the negative-bit derivative, whose degree<=k+1 gives the SAME gap. This avoids the false comparison between component energy and collided energy.

Shannon subadditivity bounds mu H(P_u) by sum_i mu h2(p_i/mu); the gap and h2(t)<=t log2(e/t) pay this by (k+1+log2(e)) E(u). The exact support edge-isoperimetry induction gives mu log2(1/mu)<=2E(1_support)<=2E(u). These two payments share one coefficient on the SAME original row energy. Summing complete row bills gives exact full H(F), and summing row energies gives exact I_Y(F). No spectral independence, omitted terminal, or fresh per-query budget appears.

Restrictions preserve the cell representation and never increase codimension. A dyadic mass merge induction proves k<=m-1. Fixing old inputs bounds every admitted fresh Boolean tensor factor's F2 degree by k+2, or m+1. Nested eight-cell quadratic gluing admits the degree9 monomial; degree10 is excluded. The three-bit defect passes, while normalized non-Boolean psi_N fails every fixed-k rate for large N and violates the unit-phase hypotheses.

The genuinely new collision witness has proper row masses85/128 and43/128. Both numerators have binary popcount4, so neither support can be represented by two disjoint affine cells. Their eight-cell complete source now pays every restriction. The first unsupported line is a codimension-independent bound for a proper FOUR-cell signed quadratic row without a bounded-size affine completion. The absolute gap still depends on k; arbitrary singleton partitions would require k=n. Removing this dependence generally would imply full FEI. No universal erasure/history/reference conversion is claimed.

## Executed validation with domain, arithmetic, commands and outputs

Before execution FROZEN_SPEC.json fixed dimensions, counts, arithmetic, memory80MB and per-job55-second cap. No >300MB job or compiler was started, so memok admission was unnecessary. Commands are `python -B -X utf8 code/check.py MODE` from this run directory (MODE below). No dimension escalation or detached work.

| MODE | Exact domain | Assertions | Seconds |
|---|---|---:|---:|
'''+''.join(f'| {r["mode"]} | '+{'ternary':'All 6654 ternary rows on nY=0..3','fixture7':'ALL59049 mixed restrictions of actual Boolean nX3/nY7 eight-cell fixture','fixture9':'4401 states: all27 X restrictions times163 Y restrictions fixing at most2 of9 coordinates','masses':'Dyadic profiles through8 cells, degree9 guard, direct proper-support character sums','direct':'Independent full-F Walsh decomposition at all27 X restrictions;8 gap-sharp rows k0..7'}[r['mode']]+f' | {r["assertions"]} | {r["seconds"]:.3f} |\n' for r in results)+f'''

All {total:,} assertions PASS. Integer Walsh transforms, physical difference sums, exact Fraction comparisons and ANF degree calculations are used. Entropies have rational upper intervals from14 positive atanh terms with a proved geometric remainder; dyadic logs are exact. Physical and Fourier I_Y agree. The direct full-F lane checks each Walsh coefficient against row assembly, including label collisions, so the complete ledger is independently verified rather than inferred from a marginal test. Finite tests support, and do not replace, the all-dimensional proof. Max observed job time {max(r['seconds'] for r in results):.3f}s. Output receipts are JSON, each under20MB.

## Proof dependencies and changed downstream conclusions

Version2 has no external proof dependency: polynomial weight, row encoding, dyadic cover, restriction closure, entropy chain rule and mass payment are proved here. It strengthens A034-AFFINE-PLANE-HEREDITARY-PHASE@1 and replaces its missing rank-three intermediate fiber step when the source has eight cells. Old sharper rank-specific subcases remain valid. No withdrawal of the old two-cell theorem is required, but the new proof needs neither it nor a false component-energy comparison. The general class has a changed guard: fixed eight-cell degree<=9, while the smaller four-cell guard remains degree<=5. Full FEI OPEN; author proof awaits independent reconstruction, not accepted merely by these checks.

## One next mathematical action and independent reviewer

A079/A033: reconstruct the negative-bit support-invariant case and normalization of the full entropy ledger. A088/A094: audit zero energy, same original influence, arbitrary X labels, restriction closure and tensor guard. Next mathematical action: bound the COMPLETE bill of a proper signed FOUR-cell quadratic row independently of its cell codimensions when no bounded-size affine completion exists; replace the absolute minimum-influence cutoff by a signed geometric entropy payment. This is a source-bound handoff, with no message sent or other-agent file modified.

## Actual persistence receipts or precise save blocker

PROOF.md, frozen spec, code, all five PASS outputs, four protocol files and rolling STATUS/WORKLOG/LEARNED saved locally in A034. out/protocol_validation.json checks exact schema fields and byte-identical PACKET_DELTA/PROGRESS. out/artifact_receipts.json records sizes/SHA256 of completed run artifacts excluding itself. Supervisor copying, independent review, downstream acceptance and public release are unverified. No mathematical job remains running. Brain self-care remains degraded/unverified: owner model97.4h, state-of-mind82.0h and dream32.7h at wake; those stale personal notes are not proof dependencies.

## Universal bridge

G-PHASE-COND advances from four labels with rate24 to ANY eight-cell affine partition with full coefficient10+log2(e)<11.5 through ALL physical restrictions, paying the previously unpaid proper nonaffine noncoarsenable four-cell fibers from the SAME original I_Y and retaining full H(S_Y|S_X). The general maximum-codimension-k payment exposes the remaining loss precisely at the absolute derivative cutoff2^(-(k+1)). Full universal C018 erasure/C019 history conversion is not obtained. The shortest next route is to remove that codimension loss for proper four-cell rows without bounded completion; this directly addresses the phase-payment obstruction needed by arbitrary-core sources, rather than opening another unrelated class.
'''
(R/'REPORT.md').write_text(report,encoding='utf8')
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
cf=set(protocol['required_per_run']['claim_fields']);pf={f.split(' (')[0] for f in protocol['required_per_run']['progress_fields']}
assert set(claim)==cf and set(progress)==pf
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert (R/'REPORT.md').read_text(encoding='utf8').rstrip().split('## Universal bridge\n\n')[-1].startswith('G-PHASE-COND')
dump(R/'out/protocol_validation.json',{'status':'PASS','claim_fields':sorted(cf),'progress_fields':sorted(pf),'identical_packet_delta':True,'assertions':total,'all_outputs_PASS':True})
(A/'STATUS.md').write_text('STATE: A034 stage19 v2 proof/checks saved: ANY eight-cell affine partition, ALL physical restrictions, full rate10+log2(e)<11.5; genuine proper FOUR-cell fibers paid;1187798 exact assertions PASS; review pending; FEI OPEN.\nNEXT: A079/A033/A088/A094 review ternary support/negative-bit gap and full SAME-IY ledger; remove codimension loss for proper FOUR-cell rows without bounded-size affine completion.\n',encoding='utf8')
with (A/'WORKLOG.md').open('a',encoding='utf8') as f:f.write('\n2026-10-23 stage19 ('+R.name+'): Read board10:53/B07/own status. Repaired existing candidate to v2: u=a-2b with degrees k,k+2 gives nonzero row influence>=2^(-(k+1)); complete bill<=(k+3+log2(e))E. Complete m-cell partition has k<=m-1; all eight-cell restriction histories paid at coefficient<11.5, including proper noncoarsenable four-cell row masses85/128,43/128. Four-cell full rate improves24 to<7.5. Fixed-eight tensor guard degree9 sharp. 1187798 exact assertions PASS across five fixed jobs, each<55s. Self-contained proof and protocol files saved; independent review/mirror pending; no jobs remain. First gap: codimension-free four-cell payment without bounded-size completion. Brain stale personal context explicitly reported.\n')
with (A/'LEARNED.md').open('a',encoding='utf8') as f:f.write('\n2026-10-23 stage19 durable lemma (AUTHOR PROOF, review pending): A ternary row u=a-2b with support bit a, negative bit b, deg_F2(a)<=k and deg_F2(b)<=k+2 has every nonzero coordinate energy>=2^(-(k+1)). If support derivative nonzero use boundary weight and factor1/4; if support invariant use EXACT negative-bit derivative, not an arbitrary extension phase. Hence mu H(Pu)<=(k+1+log2(e))E and complete row bill<=(k+3+log2(e))E after support isoperimetry. Any complete affine quadratic-cell partition of max codimk and arbitrary frequency labels satisfies the SAME full IY theorem under all physical restrictions. At most m cells imply k<=m-1 by merging dyadic masses. Eight-cell source pays previously unpaid proper FOUR-cell fibers at full coefficient10+log2(e)<11.5; arbitrary labels allowed. Fixedm tensor guard degree<=m+1 sharp (nested tests+last quadratic). Generic row-energy comparison is still false; this mechanism avoids it. 6654 ternary rows,59049 full mixed restrictions,4401 quadratic states,27 independent full-F Walsh checks and guards total1187798 exact assertions PASS. Remaining universal loss is codim dependence, not a missing four-label rank case.\n')
art=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='artifact_receipts.json':
  assert p.stat().st_size<20*1024*1024
  art.append({'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size})
dump(R/'out/artifact_receipts.json',art)
print(json.dumps({'status':'PASS','assertions':total,'artifacts':len(art)+1,'claim':cid,'running_jobs':0,'review':'PENDING','full_FEI':'OPEN'}))
