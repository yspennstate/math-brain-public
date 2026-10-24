from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];now=datetime.datetime.now(datetime.timezone.utc).isoformat()
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
jobs=[json.loads(p.read_text(encoding='utf-8')) for p in sorted((R/'out').glob('CHECK_*.json'))]
for name in ['ADVERSARIAL_RESULTS.json','TRANSPORT_RESULTS.json']:
 p=R/'out'/name
 if p.exists():jobs.append(json.loads(p.read_text(encoding='utf-8')))
assert len(jobs)==7 and all(j['status']=='PASS' for j in jobs)
total=sum(j['exact_assertions'] for j in jobs);runtime=sum(j['seconds'] for j in jobs)
totals={'status':'PASS','exact_assertions':total,'completed_jobs':len(jobs),'seconds':runtime,'jobs':jobs,'formal_status':'RUNTIME_UNVERIFIED; Lean timeout; no theorem certificate claimed'}
(R/'out/VALIDATION_TOTALS.json').write_text(json.dumps(totals,indent=2),encoding='utf-8')
formal={'status':'RUNTIME_UNVERIFIED','formal_target_verified':False,'target':'a011_same_bank','source_sha256':'ec1bd5deb48407d534c5f93985e14f1777ab9a795029656967354dd6bc1c4332','compiler_sha256':'af49bacfabaa1fea71332ca0feae0fa1a60912219d5902291adc79f905bffb8d','mathlib_manifest_sha256':'e53681b8d817947e44c51838f367219138162d03880ce23a449c8fec5139c784','timeout_seconds':55,'observed_seconds':56.986,'compiler_output':'','mathematical_falsity_established':False,'source_and_generated_receipt_directory':'out/lean/0a004229ec7f458e93c01036dcbebc3e','axioms_verified':False,'rung':'analytic proof with exact finite checks; NOT Lean-checked'}
(R/'out/FORMAL_RESULT.json').write_text(json.dumps(formal,indent=2),encoding='utf-8')
statement=('For every nonconstant Boolean source g on a>=1 uniform bits, b>=1 independent padded data bits, r>=1 fresh point controls, every edited point, and every source subprobability R of mass s<=1 positive on P_g support with finite complete cost c<=C0 I_g (C0>=0), put n=a+b,p=2^-r,t=2^-n,F=g-2g(y*)1_(controls=x*)1_(data=y*,padding=z*) and K=4C0+15. Start with the original general-envelope floor (Rpad+6pt U_n)/(1+6pt) lifted by the true conditional selector kernel. Query any ell=1..b padded bits, in any adaptive order on the unique branch matching the edit, stopping all other branches at g and its ORIGINAL source reference R. Prescribe the same envelope on the surviving branch using original R and beta_ell=6p2^ell t, not a newly certified descendant source. The complete signed reset ledger L_ell=CE_root+sum_(j<ell)2^-j[avg D(child||fresh_child)-D(parent||current)] equals sum reach DeltaH+sum_leaves reach CE_fresh and H(F)+sum_leaves reach D_fresh, including all subprobability normalizers and both terminals. It obeys L_ell<=(1+2^-ell)c+2pt[15(n+r-ell)+ell(n+r+8)-ell(ell-1)/2]<=(3/2)c+(41/4)I_g. The physical erased-edge term is E<=p2^-b I_g<=I_g/4 and I(F)>=3I_g/4, so K I(F)-L_ell>=((3/2)C0+1)I_g>0. Hence every prescribed fresh reset is paid from the SAME unused root remainder K I(F)-CE_root, with this displayed final margin, without a renewed source bank or rate inflation. An independent arbitrary Boolean terminal with prescribed finite-cost subprobability reference adds exactly its complete cost and divergence and multiplies model masses. Every terminal is nonconstant. No query that changes the source core and no full FEI theorem is asserted; integer rounding is separate.')
claim={k:None for k in protocol['required_per_run']['claim_fields']}
claim.update(claim_id='A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK',version=1,exact_statement=statement,hypotheses=['Uniform Boolean cube; nonconstant g; arbitrary a-bit ambient source, no full-coordinate-dependence hypothesis','b>=1 source-independent padding bits and r>=1 independent point controls; query only padding on the unique edited branch','Supplied subprobability s in (0,1], finite inherited cost c<=C0 Ig; off-source zeros allowed; source reference retained, not renewed','Complete fresh terminal reference costs and signed reset divergences include their actual masses; original reaches; one unused root bank','Any previously booked additional debit must fit the displayed remaining margin; cannot be silently refunded','Optional arbitrary independent terminal keeps its whole cost/debt; ideal bits, one separate global rounding convention'],statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A011/account03'],proof_source={'derivation':str(R/'DERIVATION.md'),'validation':str(R/'out/VALIDATION_TOTALS.json'),'formal_attempt':str(R/'out/FORMAL_RESULT.json')},proof_dependencies=[{'claim_id':'A011-POINT-EDIT-GENERAL-ENVELOPE-ONE-USE-HISTORY','version':1,'statement_sha256':'91c986da02a99e02cf9b7782914f38e4a57725107589c8bddbdc83444aef1fb4','scope_used':'ONLY arbitrary-core CE<=2c+15(C+E+J) floor and its complete mass; re-read analytic proof; author-proved, independent review pending','source':str(A/'runs/20261014T074949Z-account05-A011-representation-existence/GENERAL_ENVELOPE.md')}],review_records=[],status='AUTHOR_PROVED_NARROW_REFINEMENT_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],first_unproved_line='Pay prescribed descendant references after a genuinely source-dependent data query from the SAME original unused bank, preserving changed source amplitude profiles and both full terminals.',next_consumers=['A086','A094','A097','A096','A028','A029','B03','B20'])
(R/'CLAIMS.json').write_text(json.dumps([claim],indent=2),encoding='utf-8')
progress={k:None for k in protocol['required_per_run']['progress_fields'] if k!='packet_ids (one primary ID, for compatibility)'}
progress.update(protocol_revision=protocol['revision'],run_id=R.name,stream='B03',packet_id='A011',gap_id='G-J-COST-INHERITED-REFERENCE-SOURCE-BANK',attempt_id='A011-stage17-padding-fresh-reset',method='Refine existing envelope interface: original-reach source-copy contraction, elementary query JS bound, minimum cube edge boundary and exact signed reset telescoping',mathematical_delta=f'ANY nonconstant Boolean source with >=1 padding bit: ALL adaptive active-padding prefixes with prescribed fresh floors paid at SAME K=4C0+15, margin>=((3/2)C0+1)Ig; source coefficient falls to1+2^-ell; full masses/terminals retained; {total} exact checks PASS. Source-dependent query still OPEN.',deliverable_status='COMPLETE_LOCAL_PENDING_SUPERVISOR_ADOPTION',mathematical_status='ANALYTIC_PROOF_WITH_EXACT_FINITE_CHECKS; NEW_INDEPENDENT_REVIEW_PENDING; LEAN_RUNTIME_UNVERIFIED; FULL_FEI_OPEN',claim_versions_used=claim['proof_dependencies'],claims_created_or_changed=[{'claim_id':claim['claim_id'],'version':1,'change':'narrow paid-reset refinement of existing arbitrary-core envelope, no new broad universal candidate'}],source_artifacts=['REPORT.md','DERIVATION.md','CLAIMS.json','FROZEN_SPEC.json','ADVERSARIAL_SPEC.json','TRANSPORT_SPEC.json','FORMAL_SPEC.json','code/check.py','code/adversary.py','code/transport.py','code/Bank.lean','out/VALIDATION_TOTALS.json','out/SOURCE_RECEIPTS.json','out/FORMAL_RESULT.json'],next_consumers=claim['next_consumers'],next_action='After all padding is exposed, query one genuine source-data bit, construct the two full prescribed descendants from actual inherited source references and fund the signed reset from SAME residual bank; A086/A094 review this padded-prefix proof.',stagnant_substantive_attempts=0,blockers=['Source-dependent restrictions change source core and spectrum; repeated original source copies no longer justify inequality(2).','New independent review and integration pending.','Lean55second attempt timed out; no kernel certificate or axiom acceptance obtained.'],packet_ids=['A011'])
data=json.dumps(progress,indent=2)
for name in ['PROGRESS.json','PACKET_DELTA.json']:(R/name).write_text(data,encoding='utf-8')
report=f'''# A011: same original bank pays fresh floors along all padded-bit prefixes

## exact target, quantifiers, hypotheses and units

For every nonconstant Boolean g on a>=1 bits, any b>=1 independent padded data bits and r>=1 fresh point controls, supply a finite-cost source subprobability R with c<=C0 I(g), C0>=0. Query ell=1..b padded bits only along the branch containing the edit, retaining the original source model on stopped siblings and prescribing fresh general-envelope floors on surviving descendants. Prove that the complete reset ledger stays paid at the ORIGINAL K=4C0+15. Units are bits and ordinary uniform-cube influence; ideal CE with separate integer rounding. This is a quantitative repair of the existing envelope interface; full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Execution protocol fei-execution-protocol/2 (revision {protocol['revision']}), BOARD snapshot2026-10-21 18:26UTC, B03 STREAM_NOTES v2, own six substantive earlier reports and rolling files. Later account05 folders mostly contain no REPORT.md; their existence is not counted as completed research. Required campaign registries, supplemental sources and all four supplied paper texts were loaded for source receipts, with text encoding recorded (one source required explicit cp1252 fallback). Their read-only byte hashes are in out/SOURCE_RECEIPTS.json. The current owner's campaign end2026-10-23 overrides the old protocol endpoint; no schedules were changed.

The proof uses ONLY the arbitrary-core bound and mass statement in own stage6 GENERAL_ENVELOPE.md, with exact dependency hash in CLAIMS.json. Its full algebra was re-read. A097 stage5 DERIVATION distinguishes its negative-AND-cell three-component mixture from arbitrary source amplitudes. BOARD's A094/A095 paid special-core histories and A096 no-reset histories establish overlap boundaries: this result pays PRESCRIBED FRESH FLOORS for ANY nonconstant padded core. No novelty claim is made for FEI on a class, for no-reset telescoping, or for the minimum edge boundary. No external literature premise or new internet claim is used.

## complete derivation or exact first unsupported line

DERIVATION.md gives the complete proof. Original reaches make total leaf CE at most (1+2^-ell)c+30pt(n+r-ell). Query entropy decrements obey Delta<=h2(d)+4d/ln2 by a direct scalar log/chi-square estimate; summing actual d_j=2p2^j t adds the displayed quadratic prefix cost. Nonconstant g has I_g>=2a2^-a by the cube's minimum edge boundary. The rational sequence (q²+15q+7)/2^q decreases for q=b+r>=2, giving the complete ledger

    L_ell <= (3/2)c+(41/4)I_g.

All erased edges remain: E<=p2^-b I_g<=I_g/4, so I(F)>=3I_g/4. Consequently at the SAME original K=4C0+15,

    K I(F)-L_ell >= ((3/2)C0+1)I_g >0.

The reset charge is the signed change in average COMPLETE descendant divergence, so L_ell equals incoming CE plus all reset charges. It is paid from the same root remainder K I(F)-CE_root, with the displayed margin retained. Missing masses of fresh and inherited references differ and remain in their divergences. Both terminals are nonconstant. Optional independent terminals keep all CE, KL and reference mass. A previously booked additional debit is covered only up to the displayed remaining margin.

The first unsupported line is a query that changes the SOURCE core itself. The repeated original-reference copy in inequality(2) then ceases to describe the descendants. This theorem does not grant fresh influence-paid source certificates or a universal recursive FEI rate.

## executed validation with domain, arithmetic, commands and outputs

All search specifications preceded execution. FROZEN_SPEC freezes every labelled nonconstant1/2-bit core and16declared3-bit labels, b1..3,r1..2, ell1..b, three prescribed source models(P,P/2,uniform active), and no symmetry quotient on core truth tables. Commands from A011, with this run's code prefix:

    python -X utf8 code/check.py pilot
    python -X utf8 code/check.py 0
    python -X utf8 code/check.py 1
    python -X utf8 code/check.py 2
    python -X utf8 code/check.py 3
    python -X utf8 code/adversary.py
    python -X utf8 code/transport.py

The five main jobs cover32labelled cores,192actual roots,576root-reference cases and1152prefix-reference cases. Integer Walsh transforms, separately enumerated physical edges, Fraction probabilities, exact likelihood identities and outward32-term atanh log intervals check the complete ledger and rational margin. No floating sign is credited. The adversary independently enumerates16small cube boundaries, checks two constant-source exclusions,127polynomial boundary values and64arbitrary independent terminal/reference cases. Transport reconstructs12actual queries/24inherited models, checks Z0+Z1=2M, each child massM and the exact likelihood factor Z_b/M before fresh reset. Every job PASS: **{total:,} exact assertions**, total observed helper time{runtime:.6f}seconds, max cube dimension8, each job under55seconds; memory estimate100MB, peak unmeasured. No GPU, background job or automatic dimension increase.

A formal bank/algebra source is saved as code/Bank.lean. Fresh memok exited0 before the Lean attempt (physical15.1GB and commit25.7GB free). lean_check.py --file code/Bank.lean --target a011_same_bank --timeout55 --json reached RUNTIME_UNVERIFIED after56.986seconds, without compiler output. Source/compiler/manifest hashes and local generated inputs are preserved. This is **an analytic proof with exact finite checks, not a Lean-checked theorem**; a timeout is not a refutation or certificate. The memory ceiling for that timed-out formal attempt was not measured. No independent acceptance is inferred.

Initial intake stopped on a non-UTF8 source. It was repaired with an explicitly recorded cp1252 source fallback and re-run; no source file changed. The first typed derivation used the sharper standard JS comparison. Before verification it was replaced by the weaker fully elementary bound above; all published constants and finite checks use the final41/4 bound. These were analytic refinements, not failed certified claims. The voice checker was run on the technical derivation; its flagged terms are mathematical subjects, not narration. No private voice material enters the mathematics.

## proof dependencies and changed downstream conclusions

The prior arbitrary-core envelope@1, hash91c986da02a99e02cf9b7782914f38e4a57725107589c8bddbdc83444aef1fb4, remains author-proved pending independent review. Its construction is used, not the prior special bent/AND fixture. The new proof gives a narrow repair under the candidate cap: arbitrary source plus fresh padded-prefix resets, rather than a new broad FEI candidate. Full all-dimensional scope follows the analytic proof, not finite extrapolation. A086/A094 are requested independent reviewers through this source-bound run; no outgoing message or acceptance is presumed. A097/A096/A028/A029 may consume the new fixed-rate reset margin while keeping source-changing queries open.

## one next mathematical action and independent reviewer

After the last padded query, expose ONE genuinely source-dependent data coordinate on the surviving nonconstant child. Construct its two complete descendant models from actual inherited source references and price their fresh floor changes against the SAME remaining ancestor margin, with complementary terminal and booked debits retained. A086 primary independent reviewer; A094 alternate. This attacks the precise premise used in inequality(2), rather than repeating a scalar local-query obstruction.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, DERIVATION.md, all specs/checkers and exact output receipts are saved only under A011. STATUS.md has exactly two lines; WORKLOG.md is appended and LEARNED.md retains the theorem and limitation. code/finalize.py checks exact protocol key sets, statement SHA256, completed-job totals, file size caps and the Universal bridge ending, then emits out/PERSISTENCE_RECEIPTS.json. Local persistence is distinct from independent review, shared index adoption, supervisor copying or mirror verification. None of those later steps is claimed.

## Universal bridge

This stage advances C024 history transfer and C020/C019 paid whole-set/stopping-tree cost from a no-reset inherited ledger or a special nonflat fixture to ALL active padded-bit prefixes of ANY nonconstant Boolean core with PRESCRIBED FRESH FLOORS at the SAME original K=4C0+15, leaving at least((3/2)C0+1)I_g in the one ancestor account. It removes the extra inherited-cost renewal on every source-independent query, retaining full terminal models, normalizers and erased edges. A genuinely source-changing query is still unpaid; no universal FEI constant or conjecture status changes. NEXT tests exactly that lost original-source-copy premise with the remaining same bank, the shortest continuation toward full FEI rather than another isolated class bound.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text(f'STATE: A011 stage17 saved: ANY nonconstant padded core, ALL active-padding prefixes with fresh floors paid at SAME K=4C0+15; margin>=(3C0/2+1)Ig; {total:,} exact checks PASS; independent review pending; FEI OPEN.\nNEXT: Expose one SOURCE-dependent bit after padding, retain original source references, both full terminals and booked debits, fund prescribed fresh reset from SAME remaining ancestor bank; A086/A094 review.\n',encoding='utf-8')
entry=f'\n## {now} — stage17/account03\nProved the narrow arbitrary-core padding reset refinement: full fresh-floor ledger through every active padded prefix remains paid at original K4C0+15 with margin(3C0/2+1)Ig. {total} exact assertions passed across seven bounded jobs. Lean55second attempt timed out, no formal certificate. Full FEI and genuinely source-changing query payment remain open. Run: {R.name}.\n'
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(entry)
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write('''
## Stage17: arbitrary source, all padded-prefix fresh resets (review pending)

For ANY nonconstant Boolean g on a>=1 bits, b>=1 padding bits,r>=1 point controls, original source reference c<=C0 Ig, the complete reset ledger after ell=1..b active padded queries with ORIGINAL source R and FRESH prescribed surviving floors obeys Lell<=(1+2^-ell)c+2pt[15(n+r-ell)+ell(n+r+8)-ell(ell-1)/2]<=1.5c+41Ig/4. Minimum cube edge boundary gives Ig>=2a2^-a; E<=p2^-b Ig<=Ig/4. At SAME original K4C0+15, KIroot-Lell>=(1.5C0+1)Ig. No fresh child source certification or rate inflation. Full mass/terminal KL and signed reset debt retained. Constant sources violate the Ig-scaled bound; genuine source-data queries change the source-copy premise and remain OPEN. Extra booked debit must fit the displayed residual margin. 1152prefix/reference cases plus boundary, full independent tensors and actual normalized inheritance checked exactly. Lean attempt timed out: analytic proof, not Lean-certified. No new broad universal candidate opened; this refines stage6's pending envelope.
''')
assert set(progress)=={k if not k.startswith('packet_ids ') else 'packet_ids' for k in protocol['required_per_run']['progress_fields']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert report.rstrip().split('## Universal bridge\n')[-1].strip().count('\n')==0
for field in protocol['required_per_run']['report_fields']:assert f'## {field}' in report
receipts=[]
for p in R.rglob('*'):
 if p.is_file():
  assert p.stat().st_size<20*1024*1024
  receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(R/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps({'saved_utc':now,'files':receipts,'external_mirror_verified':False,'independent_review_accepted':False},indent=2),encoding='utf-8')
print(json.dumps({'status':'SAVED_AND_SCHEMA_CHECKED','exact_assertions':total,'completed_jobs':len(jobs),'files':len(receipts)}))
