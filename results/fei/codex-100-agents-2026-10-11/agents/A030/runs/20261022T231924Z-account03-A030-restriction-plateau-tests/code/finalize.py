"""Persist this stage and verify its local protocol artifacts; no shared writes."""
from pathlib import Path
import json, hashlib, datetime

ROOT = Path(__file__).resolve().parents[3]
RUN = Path(__file__).resolve().parents[1]
def read(p):
    return json.loads(p.read_text(encoding='utf-8'))
def put(p, x):
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

pilot = read(RUN/'out/PILOT.json')
main = read(RUN/'out/VALIDATION.json')
history = read(RUN/'out/HISTORY.json')
assert all(x['status']=='PASS' for x in [pilot,main,history])
assert main['checks']==86 and history['checks']==55
statement = (
 'For the actual Boolean family F_r in PROOF.md, for all even r>=4, with '
 'epsilon=2^-r, means (1/2,0,-1/2), three-cut weights (5/16,3/16,5/16), '
 'R=sum_j(1-m_j^2)phi(q_j), queried influence d=epsilon/2, and '
 'E=Delta_s H(F_r)-sum_j w_j Delta_s H(1-2C_j)-Delta_s R, '
 'E/d=r/4+3/(4 ln 2)-7/4+o(1), while the actual source-spectrum JS release '
 'Delta_s J/d=3/4+O(epsilon). Under the one original cut policy s then '
 'the r controller bits, every least nonnegative C=1 cut reserve has zero '
 'unused root slack. Hence no fixed finite K,A>=0 bounds E by Kd+A Delta_s J '
 'plus that unused weighted cut slack. The node is reached with probability '
 '1/4 by two actual DATA tag exposures from an equal-mean predecessor, '
 'with the same harmonic cut bank and both children retained. This refutes '
 'only that local unequal-mean payment upgrade: H(F_r)/I(F_r)<=16.'
)
claim = dict(
 claim_id='A030-THREE-STATE-BOOLEAN-CUT-RESERVE', version=3,
 exact_statement=statement,
 hypotheses=['Uniform cube; normalized Walsh spectrum; base-2 entropy.',
 'Canonical even-dimensional bent controller and disjoint private point-defect, majority, negative point-defect cores as defined in PROOF.md.',
 'All three original cuts, their actual physical children, fixed-policy Bellman continuations, rarity and complete source/structural terminal costs retained.',
 'Unused slack is for C=1, not an assertion for arbitrary cut-bank coefficient.'],
 statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 contributors=['A030'], proof_source=['PROOF.md','code/check.py','code/history.py','out/VALIDATION.json','out/HISTORY.json'],
 proof_dependencies=[{'claim':'A030-THREE-STATE-BOOLEAN-CUT-RESERVE@2','use':'Definitions and equal-mean boundary only; no unequal-mean payment assumed.'},
 {'claim':'A029-FINITE-LABEL-SIGNED-CHILD-ACCOUNT@1','use':'Exact T+J+Lstr decomposition reconstructed here; its universal spending claim is not enlarged.'}],
 review_records=[{'reviewer':'A030','kind':'Author analytic proof and two exact Fourier implementations; not independent external acceptance.',
 'results':'Pilot 62 checks; main 86 checks; seven-node history 55 checks. All PASS.'}],
 status='AUTHOR_PROOF_EXACT_CHECKED_INDEPENDENT_REVIEW_PENDING_NOT_LEAN_CERTIFIED',
 supersedes=['A030-THREE-STATE-BOOLEAN-CUT-RESERVE@2 (cumulative refinement; its equal-mean theorem remains valid at its original scope)'],
 refutes=['Proposed fixed-local-price unequal-mean extension: E<=K Inf_s(F)+A Delta_s J+original unused C=1 cut slack, uniformly in controller dimension.'],
 first_unproved_line=None, next_consumers=['B06 Claude lead','A028','A029','A087','A094','B20'])
put(RUN/'CLAIMS.json',[claim])

progress=dict(
 protocol_revision='2026-10-11-execution-v2', run_id=RUN.name, stream='B06', packet_id='A030',
 gap_id='C019-C024-UNEQUAL-MEAN-STRUCTURAL-CONVERSION', attempt_id='A030-rare-label-bent-structural-obstruction',
 method='Analytic finite-difference proof, exact rational prime-log certificates, separate recursive full Boolean Fourier history reconstruction.',
 mathematical_delta='Closed the failure of fixed local unequal-mean cut/rarity/JS pricing: E/Inf_s grows r/4, genuine JS/Inf_s tends 3/4, and original C=1 cut unused slack is exactly zero. Two DATA tag exposures reach the obstruction from the equal-mean paid slice without renewing the bank.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACTS_VERIFIED',
 mathematical_status='SCOPED_LOCAL_PAYMENT_OBSTRUCTION_PROVED_BY_AUTHOR; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 claim_versions_used=['A030-THREE-STATE-BOOLEAN-CUT-RESERVE@2','A029-FINITE-LABEL-SIGNED-CHILD-ACCOUNT@1'],
 claims_created_or_changed=['A030-THREE-STATE-BOOLEAN-CUT-RESERVE@3'],
 source_artifacts=['PROOF.md','out/FROZEN_SPEC.json','out/HISTORY_SPEC.json','out/PILOT.json','out/VALIDATION.json','out/HISTORY.json','out/SOURCE_RECEIPTS.json','out/PERSISTENCE.json'],
 next_consumers=claim['next_consumers'],
 next_action='Reconstruct a single signed ancestor structural-row account for the tagged bent example, retaining every DATA debit/refund, cut continuation, frontier J and both source terminals; determine whether the old unused owner pays the divergent coherent conversion.',
 stagnant_substantive_attempts=0,
 blockers=['No universal structural-to-cut/history payment proved.', 'Independent external mathematical review and Lean certification not obtained.', 'Remote mirror verification belongs to supervisor and is not claimed.'],
 packet_ids=['A030'])
put(RUN/'PROGRESS.json',progress)
put(RUN/'PACKET_DELTA.json',progress)

report='''# A030: rare-label obstruction after an entropy plateau

## exact target, quantifiers, hypotheses and units

Resolve the unequal-mean extension left open in A030@2, with all original three Boolean cuts and physical children retained. Entropy is in bits. For every even r>=4, the actual bent-controller Boolean family in PROOF.md has queried influence d=2^(-r-1). Its residual after weighted cut entropy and original rarity releases satisfies E/d=r/4+3/(4 ln 2)-7/4+o(1). The genuine source-spectrum JS release satisfies Delta J/d=3/4+O(2^-r). At C=1 all original least cut reserves have zero unused root slack. Thus every fixed finite K,A>=0 eventually fails to pay E by Kd+A Delta J plus that slack. This is a local transaction obstruction; H(F_r)/I(F_r)<=16. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read this stage: BOARD.md (22 October 23:19 update), B06 STREAM_NOTES.md v2, own rolling status/lessons and previous 21 October run; full EXECUTION_PROTOCOL.json v2; A028 20261022T205915Z DERIVATION.md and A029 20261022T221752Z DERIVATION.md/CLAIMS.json. A029-FINITE-LABEL-SIGNED-CHILD-ACCOUNT@1 has statement hash a1dbce965dc96f208072a22f42b49e3e21de81b3c42d5a3f9347ab77eb196463. Its exact T+J+Lstr split, signed DATA JS accounting and nonnegative CONTROL JS release are used at their declared scope. Baseline campaign sources and papers remain the previously read baseline; they were not independently reread or newly used as a theorem this stage. SOURCE_RECEIPTS.json pins available local files and the exact helper. No new literature claim is imported.

## complete derivation or exact first unsupported line

PROOF.md gives the complete author proof. A bent sign controller initially uses labels 1 and 2; one physical selector child changes only z=0 to label 0. Private cores have means (1/2,0,-1/2), are nonconstant and non-flat, and each has entropy 2. The exact private Fourier sector identity and a uniform finite-difference estimate yield the asymptotic with a vanishing error O(2^(-r/2)+r2^-r) after division by influence. Strictly positive raw debts make the positive-part Bellman recursion inactive for the two changing cuts, proving zero unused slack. All cut continuations remain present.

Two fresh sign tags make all source means zero at an ancestor. Their actual DATA exposures reach the obstruction with probability 1/4. The same cut bank is harmonic through both exposures; the first exposure is an exact entropy plateau. The independent recursive finite-history implementation checks all seven nodes, all four frontier histories and both structural/source terminals. The local upgrade is refuted, rather than simply unproved. The first unsupported replacement line is a global payment of the complete coherent structural rows from one original signed ancestor account; JS transport alone does not supply it. No whole-tree or universal FEI conclusion follows.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede their jobs: out/FROZEN_SPEC.json and out/HISTORY_SPEC.json. No large-memory job was started. Arithmetic is exact rational prime-log expressions with rigorous rational atanh-series logarithm enclosures; floating-point diagnostics never decide signs. The pinned helper hash is ddbb50fab85a7ca8176036423eb4a320214213d0511ab90941d7facf019fe739.

The pilot checked r=2,4,6,8 (62 checks, 32 certified signs, PASS, 0.120 seconds). The main checked compact formulas at r=4,8,12,16,20,24; direct controller spectra at r=4,6,8; and the full Boolean F at r=4 (86 checks, 54 certified signs, PASS, 1.421 seconds). These are deliberately frozen finite domains, not an exhaustive Boolean classification. At r=24 the exact enclosure is 5.332020306<E/d<5.332020307; subtracting actual JS still leaves 4.582020252<(E-Delta J)/d<4.582020253. The all-r conclusion comes from the analytic uniform remainder, not extrapolation.

The separate recursive even/odd Fourier implementation checked the full r=4 two-tag history (55 checks, seven nodes, four leaves, target reach 1/4, PASS, 0.415 seconds). Commands are `python -X utf8 code/check.py --pilot`, `python -X utf8 code/check.py`, and `python -X utf8 code/history.py`, from this run directory; exact invocation details are also retained in the frozen specs and scripts. No Lean certification or external independent acceptance is claimed.

## proof dependencies and changed downstream conclusions

A030@2 supplies definitions and the still-valid equal-mean boundary, not an unequal-mean theorem. A029@1 supplies only the exact finite-label account, reconstructed on the actual family. The new obstruction is A030-THREE-STATE-BOOLEAN-CUT-RESERVE@3. It refutes an attempted local extension rather than any accepted universal claim. A029's full structural term must remain in every downstream bill; dropping it in favor of local JS is invalid for this family. The source costs and both physical terminals cannot be erased by restricting to a convenient sign-tag outcome.

## one next mathematical action and independent reviewer

Apply the same single signed ancestor structural-row account to this tagged bent family, explicitly retaining every DATA debit/refund, the original cut continuations, frontier J and both source terminals. Identify the original unused owner of the divergent coherent conversion before seeking a universal inequality. Request source-bound independent reconstruction from A087/A094 through the B06 lead; A028/A029 are the immediate mathematical consumers. These are handoff requests recorded locally, not messages sent or reviews obtained.

## actual persistence receipts or precise save blocker

All stage artifacts are saved under this run, with local SHA-256/byte receipts in out/PERSISTENCE.json. out/FINAL_CHECK.json records protocol-key, statement-hash, compatibility-copy, PASS-output and file-size checks. STATUS.md is current; WORKLOG.md and LEARNED.md are appended. Remote upload, supervisor adoption and mirror verification have not been performed or claimed. No shared source tree was modified. Brain self-care remains degraded/unverified because the owner-model and state-of-mind sources are stale; no mathematical premise depends on those personal-context notes.

## Universal bridge

This stage advances C019 stopping-tree payment and C024 history transfer by closing the failure of a specific local upgrade: even after an actual entropy plateau, a same-bank reachable unequal-mean node has an unbounded residual/influence ratio after genuine local JS and all unused C=1 cut slack. The universal global structural payment remains open. Moving next to the single ancestor structural account is the shortest route here because the local cut/rarity/JS mechanism is now analytically excluded, while this exact family exposes the missing coherent bill with every original continuation and source terminal intact.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')

status = ('STATE: A030 stage complete: rare-label bent family refutes fixed local unequal-mean cut/rarity/JS payment; exact pilot/main/history PASS; author proof saved, external review pending; full FEI OPEN.\n'
 'NEXT: Pay the coherent structural conversion from ONE signed ancestor account on this tagged family, retaining DATA refunds/debits, original cut continuations, frontier J and both source terminals; independent review A087/A094.\n')
(ROOT/'STATUS.md').write_text(status,encoding='utf-8')
stamp='2026-10-23 (stage 20261022T231924Z)'
for name, entry in [
 ('WORKLOG.md',f'\n## {stamp}\nProved a new rare-label bent-controller local obstruction: E/Inf_s=r/4+3/(4 ln2)-7/4+o(1), genuine JS/Inf_s tends 3/4, and all original C=1 cut unused slack is zero. Exact pilot/main/history checks: 62/86/55 PASS. Two DATA tags reach the bad means with probability 1/4 from a balanced ancestor and the first query is an entropy plateau; the same cut bank remains harmonic. Retired the fixed local upgrade and pivoted to a single ancestor structural-row payment. Full FEI open; no external acceptance or Lean certification claimed.\n'),
 ('LEARNED.md',f'\n## {stamp}: rare new labels defeat local curvature pricing\nFor the actual family and definitions in runs/{RUN.name}/PROOF.md, the residual after all three weighted cuts and original rarity release has E/d=r/4+3/(4 ln2)-7/4+o(1), while actual JS release/d tends 3/4 and unused least C=1 cut slack is identically zero. Thus no fixed K,A can pay this transaction by Kd+A Delta J+that slack. Equal-mean cancellation is not hereditary under two real DATA tag exposures, even though the same cut bank is exactly harmonic and the first query preserves entropy. H(F)/I(F)<=16, so this is a route obstruction, not a disproof of FEI. Retain complete Lstr and both terminals in any global replacement.\n')]:
    with (ROOT/name).open('a',encoding='utf-8') as handle:
        handle.write(entry)

base=Path(r'~\brain_workers\FEI100_20261011')
sources=[base/'BOARD.md',base/'claude/B06/STREAM_NOTES.md',
 base/'agents/A028/runs/20261022T205915Z-account03-A028-stopping-tree-payment/DERIVATION.md',
 base/'agents/A029/runs/20261022T221752Z-account03-A029-child-deficit-transport/DERIVATION.md',
 base/'agents/A029/runs/20261022T221752Z-account03-A029-child-deficit-transport/CLAIMS.json',
 Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
put(RUN/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
protocol=read(sources[-1])['required_per_run']
expected_progress=[k.split(' (')[0] for k in protocol['progress_fields']]
assert set(progress)==set(expected_progress)
assert set(claim)==set(protocol['claim_fields'])
assert read(RUN/'PROGRESS.json')==read(RUN/'PACKET_DELTA.json')
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
assert len((ROOT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for field in protocol['report_fields']:
    assert '## '+field in report
files=[p for p in RUN.rglob('*') if p.is_file() and '__pycache__' not in str(p)]
assert all(p.stat().st_size<20*1024*1024 for p in files)
put(RUN/'out/FINAL_CHECK.json',{'status':'PASS','protocol_exact_keys':True,'statement_hash':True,'progress_delta_identical':True,'all_required_report_fields':True,'rolling_status_two_lines':True,'pilot_checks':pilot['checks'],'main_checks':main['checks'],'history_checks':history['checks'],'external_review':'PENDING','full_fei':'OPEN'})
files=[p for p in RUN.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name!='PERSISTENCE.json']
put(RUN/'out/PERSISTENCE.json',{'scope':'Local files only; excludes manifest itself and transient Python caches. No remote adoption claimed.','files':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)],'rolling_files':[{'path':str(ROOT/n),'bytes':(ROOT/n).stat().st_size,'sha256':sha(ROOT/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'status':'PASS','run':str(RUN),'claim':claim['claim_id']+'@3','statement_sha256':claim['statement_sha256'],'checks':[pilot['checks'],main['checks'],history['checks']],'files':len(files)},indent=2))
