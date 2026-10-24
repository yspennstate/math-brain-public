from pathlib import Path
import hashlib,json,datetime
RUN=Path(__file__).resolve().parents[1]; HOME=RUN.parents[1]; ROOT=HOME.parents[1]
OLD=HOME/'runs/20261014T035704Z-account05-A021-rare-core-asymptotics'
def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
protocol_path=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8'))
sources=[protocol_path,ROOT/'BOARD.md',ROOT/'claude/B05/STREAM_NOTES.md',OLD/'REPORT.md',OLD/'DERIVATION.md',OLD/'CLAIMS.json',OLD/'code/check.py',
 ROOT/'agents/A023/runs/20261014T051414Z-account05-A023-amortized-rarity-budget/REPORT.md',
 ROOT/'agents/A025/runs/20261014T062819Z-account05-A025-rare-event-counterfamily/REPORT.md',
 ROOT/'agents/A025/runs/20261014T062819Z-account05-A025-rare-event-counterfamily/PROOF.md',
 ROOT/'agents/A028/runs/20261014T051435Z-account05-A028-stopping-tree-payment/REPORT.md',
 ROOT/'agents/A028/runs/20261014T051435Z-account05-A028-stopping-tree-payment/DERIVATION.md',
 ROOT/'agents/A028/runs/20261014T051435Z-account05-A028-stopping-tree-payment/CLAIMS.json',
 ROOT/'agents/A029/runs/20261014T055200Z-account05-A029-child-deficit-transport/REPORT.md']
dump(RUN/'out/source_inventory.json',[dict(path=str(p),sha256=sha(p)) for p in sources])
prior=json.loads((OLD/'CLAIMS.json').read_text(encoding='utf-8'))[0]
extension=('Version2 retains the preceding flat-reference expansion at exactly its stated scope and adds: for ANY Boolean seed b on m>=1 bits, distinct vertex flips u,v and the same independent balancing sign and nested point blocks, H(f)-sum pi_j H(gj)<=Rstar+(11/2+3/ln(2))*IC<Rstar+10*IC. No Fourier flatness, coefficient sign, mean or support assumption is required for this upper payment. The prior lower bound Rstar<=D is not extended to arbitrary seeds. Supplied terminal certificates H(gj)<=Cj I(gj) imply H(f)<=max(10,max_j Cj+2)*I(f). More generally, for any finite physical controller on independent uniform controls and arbitrary cores on one data cube, with row marginal q_T=E x_T^2, variance v_T=q_T-(E x_T)^2, V=sum v_T>0, actual control influence IC and raw nonempty-control entropy Hplus, H(f)-E H(g_L)<=Hplus+V log2(max_T(v_T)/V)+V/ln(2)+2IC/ln(2). If V=0 the decrement is zero. This row-profile bound does not assert a mixed-data-query drift estimate or FEI.')
statement=prior['exact_statement']+'\n'+extension
hyp=['Uniform physical cubes, Boolean signs, Shannon Fourier entropy bits and ordinary total influence.',
 'The retained asymptotic expansion and coefficient-one lower bound have the prior even-m>=4 bent-reference hypotheses.',
 'The new upper payment allows every Boolean seed on m>=1 bits and distinct u,v; balancing sign, two point blocks and seed coordinates are disjoint, widths r,s positive integers.',
 'The general row-profile inequality needs only a finite label map on independent uniform controls and arbitrary Boolean cores on the shared independent data cube; zero rows have zero contribution.',
 'No lower bound Rstar<=D for arbitrary seeds, universal child certificate, all-depth reserve payment or mixed-query release-only rule is claimed.']
claim=dict(claim_id=prior['claim_id'],version=2,exact_statement=statement,hypotheses=hyp,statement_sha256=hashlib.sha256(json.dumps(dict(statement=statement,hypotheses=hyp),sort_keys=True,separators=(',',':')).encode()).hexdigest(),contributors=['A021'],proof_source=['DERIVATION.md','code/check.py','out/validation.json',str(OLD/'DERIVATION.md')],proof_dependencies=[dict(claim_id=prior['claim_id'],version=1,statement_sha256=prior['statement_sha256'],scope='Retained flat expansion only; prior local proof, independent review pending'),dict(claim_id='A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT',version=5,statement_sha256='66a08477db58867a640a8dc7202d62a73c1f8d766491eaf3a2cd26e896317b7d',scope='Mixture entropy/log-Sobolev subclause only; independently reconstructed in REVIEW_A028.md and current proof')],review_records=[],status='PROVED_LOCALLY_REVIEW_PENDING',supersedes=[dict(claim_id=prior['claim_id'],version=1,reason='Same coherent refund mechanism completed for arbitrary seed upper payments; old asymptotics retained at original scope')],refutes=[],first_unproved_line=None,next_consumers=['A023','A025','A028','A029','A087','B05','B20'])
dump(RUN/'CLAIMS.json',[claim])
progress=dict(protocol_revision=protocol['revision'],run_id=RUN.name,stream='B05',packet_id='A021',gap_id='G-R-SELECT',attempt_id='A021-stage6-flatness-free-signed-variance-refund',method='Consume A025 conserved-bank mixed-data no-go and A028 physical-cube mixture entropy; independently reconstruct scalar log-Sobolev via even coefficients; replace pointwise curvature by a signed marginal-row Jensen refund and delocalized point-edit variance',mathematical_delta='The existing three-core one-owner refund now holds for EVERY Boolean seed, including zero and unequal-amplitude Fourier rows, with control price10 and original terminal weights. A universal signed row-profile inequality isolates the exact unpaid quantity. This pays the selected control continuation on A025 non-flat obstruction family without claiming its data query is paid by release.',deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='ARBITRARY_SEED_TWO_EDIT_PAYMENT_AND_GENERAL_ROW_PROFILE_BOUND_PROVED_LOCALLY; SCOPED_A028_JS_RECONSTRUCTION_HOLDS; NEW_REVIEW_PENDING; FULL_FEI_OPEN',claim_versions_used=claim['proof_dependencies'],claims_created_or_changed=[dict(claim_id=claim['claim_id'],version=2)],source_artifacts=['REPORT.md','DERIVATION.md','REVIEW_A028.md','SEARCH_SPEC.json','code/check.py','code/finalize.py','out/validation.json','out/pilot.json','out/rows.jsonl','out/pilot_rows.jsonl','out/source_inventory.json'],next_consumers=claim['next_consumers'],next_action='A029/A023 review the signed row-profile refund and non-flat control continuation. At one A025 x-query retain its SAME positive remaining Rstar and both child bills, and pay only the signed parent residual from genuinely unused certified terminal surplus; no bank renewal.',stagnant_substantive_attempts=0,blockers=['No universal price for the general Hplus plus signed row-profile term against one terminal reserve.','Mixed-data-query excess cannot be bounded by queried influence and released reserve alone, by A025.','New theorem independent acceptance, shared adoption and mirror verification unobserved.'],packet_ids=['A021'])
dump(RUN/'PROGRESS.json',progress); dump(RUN/'PACKET_DELTA.json',progress)
report='''# exact target, quantifiers, hypotheses and units

Finish the existing coherent two-edit refund by removing the flat Fourier reference hypothesis. Uniform cubes, Boolean signs, Fourier entropy in bits and ordinary influence. For ANY seed on m>=1 data bits, balance it by fresh z and form its two distinct vertex flips. Select the three actual cores by two independent nested point blocks of arbitrary positive widths r,s. Original pi=(1-a,a(1-t),at) terminal weights are retained. The precise all-parameter theorem and a general row-profile inequality are proved in DERIVATION.md. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

BOARD.md supervisor07:47UTC, especially B05/B06 and neighboring history-payment entries; B05 lead v2 read fully, own STATUS and prior completed run035704. The board display truncated unrelated entries; no complete board-wide audit is asserted. Execution protocol v2 is retained and machine checked. New source reports read: A023 run051414, A025 run062819, A028 run051435, A029 run055200. Additionally read full A025 PROOF.md and A028 DERIVATION.md/CLAIMS.json. Main locators are A028 Section2 (physical-cube mixture entropy) and A025's exact zero-row data-query obstruction. Paths and hashes are in out/source_inventory.json. No fresh literature/brain/web premise or external write is used.

# complete derivation or exact first unsupported line

For the declared ANY-seed family, with IC the actual removed control influence and Rstar=2sum pi_i*pi_j I(gi*gj),

    H(f)-sum pi_j H(gj)<=Rstar+(11/2+3/ln2) IC<Rstar+10 IC.

The actual nonempty-control entropy remains2mV+L, independent of the seed. The new proof replaces common-amplitude curvature by v_T<=2delta V, where v_T is the control variance of the actual Fourier amplitude. The empty-control entropy difference is bounded ABOVE by V(1-m+1/ln2), using the marginal q_T and Jensen. This supplies the signed dimension-growing refund even if the base coefficient vanishes. The separately reconstructed mixture entropy is at most2IC/ln2. The exact edge correction, V<=IC and L<=4IC give the stated constant. No arbitrary-seed LOWER bound on the decrement is asserted.

More generally, for ANY finite physical controller and shared-data cores, the complete control bill is at most Hplus+V log2(max v_T/V)+V/ln2+2IC/ln2, with zero-variance case handled exactly. This is a proved universal profile inequality; comparing that joint quantity to one owned terminal reserve remains open.

A025's non-flat obstruction is an instance with an extra dummy seed bit and point edits conditional on that bit. The new theorem pays its control-first bill and both conditioned control continuations from their actual banks. It does NOT pay the prior data query or spend its unreleased bank. Exact first unsupported line: fund the signed data-query residual using one genuinely unused terminal surplus under the SAME incoming bank and both physical child bills, or prove the joint profile quantity has universal payment. Local release-only payment is already false.

# executed validation with domain, arithmetic, commands and outputs

SEARCH_SPEC.json frozen first. Commands: python -X utf8 runs/20261014T075029Z-account05-A021-rare-core-asymptotics/code/check.py --pilot, then the same without --pilot. Pilot96 cases PASS in0.077492seconds. Full2432 cases PASS in1.638531seconds: all16 two-bit seeds/all6 edit pairs/r,s=1,2 (384 full Walsh reconstructions), and all256 three-bit seeds/u=0,v=1 or3/r,s=1,2 (2048 additional compressed cases). This is the exact declared subset, not a symmetry claim for all three-bit edit pairs. Included1216 cases with zero seed coefficients and1024 with unequal nonzero magnitudes. Max direct dimension7/table128.

All Walsh transforms and influence/variance identities use integers and Fraction; logarithm bounds use the pinned own prior28-term atanh helper with proved tail and192-bit outward rounding. Every final margin and signed refund sign is interval-certified. Direct coefficient multisets and physical influence/terminal decomposition are checked exactly. Rows are immediately flushed. An initial file-open failed because out/ had not yet been created; no mathematical search ran, and creating the directory fixed it. No mathematical assertion failed. Frozen150MB estimate is below the memok threshold; no heavy job, automatic dimension escalation or surviving process. The analytic theorem covers every dimension and width independently of finite checks.

# proof dependencies and changed downstream conclusions

Same existing claim is narrowly extended to version2; prior flat asymptotics remain at original hypotheses. No new broad universal candidate is opened. A028@5 mixture entropy subclause is independently reconstructed by a different scalar proof and accepted ONLY at that scope in REVIEW_A028.md; bundled reference/history clauses are excluded. The new theorem itself follows from the exact spectra, entropy tangent and physical-cube mixture inequality. The old theorem's coefficient-one necessity remains applicable to the larger family.

A023's high-contrast NEXT is closed at a uniform control rate10 and extended beyond bent seeds. A025/A029 can use the non-flat control continuation under one symmetric reserve with supplied terminal certificates. H(gj)<=Cj I(gj) implies full H(f)<=max(10,max Cj+2)I(f); the child costs are not silently free. A025's bad data query, nonrenewal obstruction and conserved-bank identities survive unchanged. This is a concrete extension of the existing history mechanism, rather than another class census. New independent review remains pending.

# one next mathematical action and independent reviewer

At A025's actual x-query, retain the root bank's remaining conditional capacities and the now-certified control continuation. Bound its signed residual from a fixed, explicitly unused fraction of the actual terminal surplus, keeping both siblings and no renewed reference. For arbitrary cores, test the general joint profile term rather than separately paying its canceling pieces. Independent reviewer A029 should reconstruct the row variance, weighted Jensen and edge correction; A023 should check the stopping/terminal substitution, with A028 checking the finite-label mixture extension.

# actual persistence receipts or precise save blocker

All four protocol files, proof, scoped review, frozen spec, code, immediate case outputs and source receipts are saved locally. out/ARTIFACTS.json records local artifact hashes; out/FINAL_CHECK.json records schema/hash/file checks. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated. The prior035704 run is also complete and preserved. No external messages, shared indices, Git, mirrors, independent acceptance or downstream adoption are asserted.

## Universal bridge

This moves C024 history transfer toward C019 by removing the flat-reference restriction from the first two-edit symmetric-reserve refund: every seed, including zero and unequal Fourier rows, has a complete control bill paid by ONE Rstar plus10 IC with original terminals. The universal row-profile inequality identifies the exact signed term that enabled that refund. What remains is its payment for arbitrary core changes and the mixed-data-query residual from genuinely unused child surplus; bank release alone is insufficient. NEXT carries the same bank into that concrete residual, the shortest route toward universal FEI because it targets the unpaid history step rather than enlarging an already-certified finite class.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(HOME/'STATUS.md').write_text('STATE: A021 stage6 saved: ANY-seed two-point-edit three-core control bill<=Rstar+10IC; universal signed row-profile refund proved;2432 exact cases/384 Walsh reconstructions PASS; full FEI OPEN.\nNEXT: A029/A023 review; pay A025 mixed x-query signed residual using SAME remaining bank, certified non-flat control continuation and one unused actual terminal surplus; no bank renewal.\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as out: out.write('\n'+now+' | Stage6 '+RUN.name+': read07:47 board/B05 notes/status; consumed A025 bad data-query family and A028 physical-cube mixture theorem. Removed all seed-flatness assumptions from existing two-edit upper refund: D<=Rstar+(11/2+3c)IC<Rstar+10IC. New universal row-profile inequality retains coherent marginal refund; no release-only data payment claimed. Independent A028 JS reconstruction via even scalar coefficients HOLDS at that scope only. Exact pilot96/full2432 cases,384 actual Walsh reconstructions,1216 zero-row and1024 unequal-amplitude cases PASS in0.077492/1.638531s; initial missing-out-directory access error corrected before any search. No heavy job or external writes.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as out: out.write('\nStage6 flatness-free refund: same two distinct point edits to ANY Boolean seed on m>=1 bits give D<=Rstar+(11/2+3c)IC<Rstar+10IC, all positive widths. DO NOT extend the old lower bound Rstar<=D to non-flat seeds. For each data Fourier row q=E x_j^2 and v=q-(E x_j)^2. Point edits ensure v_T<=2delta V even on zero seed rows; tangent entropy plus weighted Jensen refunds at least(m-1-c)V from nonempty entropy2mV+L. Mixture entropy J<=2cIC follows from physical-cube scalar entropy and tensorization; A028@5 accepted at this subclause only. Universally D<=Hplus+V log2(max v/V)+cV+2cIC (V=0 gives0), with one common profile: separately bounding canceling terms loses the refund. A025 data-query no-go family is a two-edit seed with one dummy bit, so its control-first/conditional control continuations are paid while its obstructed parent data query remains unpaid. Conditional full FEI transfer is max(10,max child rates+2); no free terminal certificate or renewed reserve.\n')
claims=json.loads((RUN/'CLAIMS.json').read_text(encoding='utf-8'))
assert all(set(x)==set(protocol['required_per_run']['claim_fields']) for x in claims)
fields=set(protocol['required_per_run']['progress_fields']); fields.remove('packet_ids (one primary ID, for compatibility)'); fields.add('packet_ids')
assert set(progress)==fields and (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert all(h in report for h in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n\n')[-1].startswith('This moves C024')
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
validation=json.loads((RUN/'out/validation.json').read_text(encoding='utf-8'))
assert validation['cases']==2432 and validation['direct_fixtures']==384 and validation['result']=='PASS'
for p in RUN.rglob('*'):
    if p.is_file(): assert p.stat().st_size<20_000_000
dump(RUN/'out/FINAL_CHECK.json',dict(result='PASS',claim_statement_sha256=claim['statement_sha256'],schema='exact protocol field sets',progress_copy='byte identical',rows=validation['cases'],review='pending',mirror='unverified'))
dump(RUN/'out/ARTIFACTS.json',[dict(path=str(p.relative_to(RUN)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='ARTIFACTS.json'])
print(json.dumps(dict(result='PASS',run=RUN.name,claim_version=2,claim_sha256=claim['statement_sha256'])))
if __name__=='__main__': pass
