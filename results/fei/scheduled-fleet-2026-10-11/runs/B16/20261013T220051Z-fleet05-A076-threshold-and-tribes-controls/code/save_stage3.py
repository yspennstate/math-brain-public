"""Persist A076 stage 3; no computation search or writes outside A076."""
from pathlib import Path
import json, hashlib, datetime
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]
PREV=AGENT/'runs'/'20261011T233829Z-fleet05-A076-threshold-and-tribes-controls'
def write(name,obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
validation=json.loads((ROOT/'out/VALIDATION.json').read_text(encoding='utf-8'))
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8-sig'))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
# Reuse the audited elementary arithmetic routines without executing enumeration.
ns={"__file__":str(ROOT/'code/check_shifted.py')}
exec((ROOT/'code/check_shifted.py').read_text(encoding='utf-8').split('records=[];')[0],ns)
F=ns['F'];corr=ns['D'](F(-3,4),F(1,4));lo,hi=ns['bounds'](corr)
assert hi<0
write('out/SIGNED_ROW_CERTIFICATE.json',dict(core='G=+1 only on (+++), -1 elsewhere',
     n=3,truth_table_mask=254,queried_coordinate=0,mu='-3/4',singleton='1/4',influence='1/4',
     exact_log_expression=ns['encoded'](corr) if 'encoded' in ns else [[str(x),str(c)] for x,c in sorted(corr.items())],
     correction_interval=dict(lower_exact=str(lo),upper_exact=str(hi)),
     conclusion='D<0: treating the shifted row as a nonnegative gate bank loses actual credit',
     sharp_upper_witness=dict(core='G=y_i',mu=0,singleton=1,influence=1,D=1)))
old=json.loads((PREV/'CLAIMS.json').read_text(encoding='utf-8'))
claims=[]
extensions=[
 ' Stage-3 extension: Let W_+=(1+x)/2+(1-x)G/2 and W_-=-(1-x)/2+(1+x)G/2 for any Boolean core G on disjoint uniform inputs. With mu=E G,a=Ghat({i}),d=Inf_i(G),Phi(p,q)=(p+q)h2(q/(p+q)), the exact data erasure is B_i(W_+)=B_i(W_-)=B_i(G)/2+D(mu,a), where D=[Phi((1+mu)^2,a^2)+Phi((1-mu)^2,a^2)]/4-Phi(mu^2,a^2)/2. It satisfies -|mu a|<=D<=|a|<=d; the upper coefficient 1 is sharp at G=y_i. Inf_i(W)=d/2. H(W)=H(G)/2+R(mu), with R=1-mu^2+phi((1+mu)^2/4)+phi((1-mu)^2/4)-phi(mu^2)/2. B_x(W)=Phi((1+mu)^2,(1-mu)^2)/4+(1-mu^2)/2<=1-mu^2<=4Inf_x(W).',
 ' Stage-3 extension: For every finite adaptive partial physical core tree T lifted to either one-control wrapper with x unqueried, B_T(W)=B_T(G)/2+D_T, |D_T|<=Pi_I(G)=I(G)-E I(G_leaf), and Pi_I(W)=Pi_I(G)/2. The terminal entropy is exactly E H(W_leaf)=E H(G_leaf)/2+E R(mu_leaf). Querying x at every leaf adds erasure at most 4Inf_x(W_root), giving B_(T;x)(W)<=B_T(G)/2+Pi_I(G)+4Inf_x(W_root). The signed correction may be negative: the three-bit point core G=+1 only at (+++) gives D(-3/4,1/4)<0 by a rational interval certificate. These results pay the shifted-empty-row correction alone; inherited core erasure and arbitrary terminal entropy remain unpriced. No conclusion of full FEI or a universal shared-coordinate ownership rule is claimed.'
]
for c,ext in zip(old,extensions):
    c['version']=3;c['exact_statement']+=ext
    c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
    c['proof_source']['stage3']=str(ROOT/'SHIFTED_ROW_PROOF.md')
    c['proof_source']['stage3_validation']=str(ROOT/'out/VALIDATION.json')
    c['proof_source']['stage3_locator']='sections 1-3, equations (1)-(8)'
    c['supersedes']=[c['claim_id']+'@2']
    c['hypotheses'].append('Stage-3 arbitrary biased Boolean core on independent uniform signs; fresh single control; core-only adaptive prefix, any stopping leaves, optional terminal control query; bits.')
    c['proof_dependencies'].append(c['claim_id']+'@2')
    c['next_consumers']=['A057','A078','A077','A092','A088','B16','B12','B06','B20']
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    claims.append(c)
write('CLAIMS.json',claims)
sources=[protocol_path,
 Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),
 Path(r'~\brain_workers\FEI100_20261011\claude\B16\STREAM_NOTES.md'),
 Path(r'~\brain_workers\FEI100_20261011\agents\A057\runs\20261012T003930Z-fleet05-A057-coherent-restriction-remainder\PROOF.md'),
 Path(r'~\brain_workers\FEI100_20261011\agents\A057\runs\20261011T220314Z-fleet05-A057-coherent-restriction-remainder\COHERENT_REMAINDER_PAYMENT.tex'),
 PREV/'CLAIMS.json',PREV/'code/check_mixed.py',PREV/'code/save_stage2.py']
write('SOURCE_MANIFEST.json',dict(captured_at=now,hash_scope='save-time bytes, not a retroactive stage-start snapshot',
 sources=[dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in sources],
 scopes=dict(board='Stage-start full board plus B08-B13 and B16-B20 targeted reads; board dated 2026-10-13 21:55 UTC',
             lead='B16 v2 remains dated 2026-10-11 23:25Z; previous directed control target completed at stage2',
             A057='Complete stage2 proof and stage1 TeX; generic split and scalar envelope are credited, not reopened')))
progress=dict(protocol_revision=protocol['revision'],run_id=ROOT.name,stream='B16',packet_id='A076',
 gap_id='FEI-B16-A076-INITIAL',attempt_id='A076-stage3-shifted-empty-row',
 method='Exact Fourier row reconstruction after one majority restriction; sharp scalar entropy envelope and adaptive influence telescope; exhaustive small-core rational certification',
 mathematical_delta='Pays actual signed shifted-empty-row correction by one core influence, sharp at a literal; any adaptive partial core tree pays correction <=2 consumed wrapper influence. Gives exact inherited-erasure and terminal-potential formulas and a negative-credit witness.',
 deliverable_status='COMPLETE_LOCAL_PENDING_INDEPENDENT_REVIEW',
 mathematical_status='SHIFTED_ROW_INTERFACE_AUTHOR_PROVED; C018_C019_UNIVERSAL_PAYMENT_OPEN; FULL_FEI_OPEN',
 claim_versions_used=['A076-STRUCTURED-SPECTRA@2','A076-TRIBES-PAYMENT-DISCRIMINATION@2','A057 stage2 PROOF.md sections1-2 (credited scalar/split source; reconstructed here)'],
 claims_created_or_changed=[c['claim_id']+'@3' for c in claims],
 source_artifacts=['SHIFTED_ROW_PROOF.md','SOURCE_MANIFEST.json','code/check_shifted.py','code/save_stage3.py','out/FROZEN_SPEC.json','out/VALIDATION.json','out/EXACT_TREE_LEDGERS.json','out/SIGNED_ROW_CERTIFICATE.json'],
 next_consumers=['A057','A078','A077','A092','A088','B16','B12','B06','B20'],
 next_action='Derive a source-bound signed-row collision formula for two priority activation events sharing one physical coordinate; preserve both inherited core bills and determine one exclusive influence reserve. A092/A088 independently reconstruct the present sharp shift and terminal formulas.',
 stagnant_substantive_attempts=0,
 blockers=['Inherited arbitrary-core erasure/terminal entropy unpaid; shared-coordinate ownership not proved','Independent review, supervisor adoption and mirror verification not observed'],packet_ids=['A076'])
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
report=f'''# A076 stage 3: shifted empty-row transport

## exact target, quantifiers, hypotheses and units

Close the previous NEXT: after one physical outer query in Maj3(x1,x2,G), transport actual data erasure through its OR/AND children with arbitrary biased Boolean G. Original coordinates are independent uniform signs; entropies are bits. The all-dimensional proof covers every finite core-only adaptive restriction prefix and any stopping leaves, with the outer control unqueried until an optional terminal query. It proves sharp D<=Inf_i(G), the two-sided signed bound, and exact terminal entropy. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

BOARD.md dated 2026-10-13 21:55 UTC, unchanged B16 STREAM_NOTES.md v2 dated 2026-10-11 23:25Z, own STATUS/LEARNED, complete execution protocol v2, and prior stage2 claims/helper/packaging were read. Targeted board reads covered the composition, posterior and stopping-tree streams. A057 stage2 PROOF.md (sections 1-4 and unsupported bridge) and stage1 COHERENT_REMAINDER_PAYMENT.tex were read in full. SOURCE_MANIFEST.json gives actual save-time hashes and read scopes.

General biased composition transport is already established locally by A056/A057 and reviewed by other agents; this stage does not restart that calculus or the completed majority/tribes scalar obstruction. A057 section 2 provides the scalar Phi envelope, reconstructed in the proof. No threshold-paper leaf theorem or external pending sandwich is used for this arbitrary-core extension.

## complete derivation or exact first unsupported line

SHIFTED_ROW_PROOF.md sections 1-3, equations (1)-(8), contain the full proof. Nonempty residual-core rows contribute exactly half their original erasure. Only the empty residual-core row shifts. Its signed correction D is bounded above by |a| and below by -|mu a| using Phi(u^2,v^2)<=2|uv| and the Boolean physical derivative |a|<=Inf_i(G). The upper coefficient is exactly attained by a one-bit core. Summing over any adaptive prefix uses the consumed influence telescope once: |D_T|<=I(G)-E I(G_leaf), which is twice the corresponding consumed wrapper influence.

The optional terminal x query costs <=4 of the original x influence, reserved separately from the prefix. The proof retains the inherited half-core erasure. Its exact Fourier entropy potential R(mu) retains the full arbitrary-core terminal entropy before and after the outer query. A three-bit point core gives a rigorously negative D, so unsigned gate pricing can discard actual credit.

The first unsupported universal line remains a finite dimension-independent payment of inherited core erasure plus retained arbitrary-core terminal entropy for a universal selection policy, or a common exclusive reserve for two cores sharing physical coordinates. The new transport does not pay those quantities and does not prove FEI.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was written before enumeration. It freezes every Boolean core on 0..3 bits: 278 cores, both OR/AND wrappers (556), 1,608 data splits and 2,224 trees. Policies select largest or smallest current physical influence, ties by current coordinate, with either complete core revelation or stopping at constants/at most one core bit, followed by terminal x queries. No symmetry reduction, larger dimension, or heavy job was used; memory estimate 100 MB.

Command: `python -X utf8 runs\\{ROOT.name}\\code\\check_shifted.py`.

Result: **{validation['exact_assertions']:,} exact assertions PASS**, helper runtime **{validation['elapsed_seconds']:.3f} seconds**, below the 60-second pilot limit. Integer FWHT/Fraction arithmetic checks actual spectra and pivotal influences. Logarithmic equality is checked by converting rational coefficients to integer exponents and verifying an exact rational product equals one, independently of numerical evaluation. Inequalities use outward 70-bit dyadic intervals from 24-term rational atanh series with proved tail 2*z^(2N+1)/((2N+1)*(1-z^2)); boundary equalities receive exact product checks. The full correction, suffix and terminal expressions are in out/EXACT_TREE_LEDGERS.json. out/SIGNED_ROW_CERTIFICATE.json gives exact negative bounds for D(-3/4,1/4). The analytic proof, not the finite enumeration, closes all dimensions.

## proof dependencies and changed downstream conclusions

The two existing A076 bundles extend to v3; no third broad unreviewed candidate is opened. Previous claims remain recorded verbatim, with the narrow shifted-row and adaptive transport extension appended. The new proof is elementary and independent of the prior all-width scalar obstruction, generic FEI class bounds and pending universal claims. A057's known general split/envelope is explicitly credited.

A078/A077 can now replace the one-remaining-control scalar surrogate by a sharp actual signed-row correction through biased descendants. A057/B12 receive the sharp one-control specialization and nonnegative-bank caveat; B06/B20 receive the exact partial-tree inherited/terminal interface. Author proof and exact computational verification are complete locally; independent review, mirror receipt and downstream adoption have not been observed.

## one next mathematical action and independent reviewer

Compute the first signed-row collision for two priority activation events sharing one physical coordinate, retaining both inherited core bills, and test whether the correction admits one exclusive influence reserve. This is the earliest place the fresh-control proof loses its two disjoint Fourier copies. Independent reviewers: A092 primary, A088 alternate, specifically equations (1)-(8), sharpness, exact physical-child entropy and the separate control reserve.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and matching PACKET_DELTA.json are saved under this run, together with source-complete proof, frozen spec, scripts, exact log ledgers and rational certificates. out/PERSISTENCE.json records hashes and byte counts. Protocol fields are checked mechanically by code/save_stage3.py; rolling STATUS.md, WORKLOG.md and LEARNED.md are updated. Save time is {now}; no continuous execution or stage-date clock reset is claimed. Every file is below 20 MB. Supervisor mirror/adoption is not locally verified.

## Universal bridge

C018/C019 moves by closing the one-remaining-control shifted-empty-row interface: its sharp positive correction costs at most one queried core influence, or two consumed wrapper influences, for every adaptive partial prefix; the optional terminal control charge costs at most four of its separately reserved influence. The inherited half-core erasure and exact arbitrary-core terminal entropy remain unpaid, so there is no universal constant improvement or FEI closure. NEXT targets the first shared-coordinate signed collision and exclusive reserve because the board identifies overlapping-control ownership as the live universal bottleneck; it tests the transport mechanism where it first fails instead of producing another threshold or tribes class estimate.
'''
for heading in protocol['required_per_run']['report_fields']:assert '## '+heading in report
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A076 stage 3 saved: sharp shifted-row D<=core influence; arbitrary adaptive prefix correction <=2 consumed wrapper influence; 47,681 exact assertions PASS; review pending, FEI OPEN.\nNEXT: A092/A088 review signed transport/terminal potential; derive first shared-coordinate two-core collision with one exclusive influence reserve and both inherited core bills retained.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n## {now} (requested stage 2026-10-13 22:00 UTC)\nRead board/B16 notes and A057 proofs; avoided duplicating general composition calculus. Proved sharp signed shifted-empty-row correction |D|<=Inf_i(G), adaptive nonreuse, exact terminal potential, and terminal control erasure<=4 reserved x influence. Exhausted 278 cores/556 wrappers, 1,608 data splits and 2,224 adaptive trees: 47,681 exact assertions, {validation["elapsed_seconds"]:.3f}s, no heavy job. Negative correction on three-bit point core rigorously certified. Extended both existing bundles to v3; inherited arbitrary-core erasure/terminal entropy and shared-coordinate ownership remain open.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage3 durable fact (bits): OR/AND fresh-control wrapper has B_i(W)=B_i(G)/2+D(mu,a), D=[Phi((1+mu)^2,a^2)+Phi((1-mu)^2,a^2)]/4-Phi(mu^2,a^2)/2. The sharp upper bound D<=|a|<=Inf_i(G), lower bound D>=-|mu a|, survives arbitrary biased core restrictions. Any adaptive partial core tree pays |sum wD|<=consumed core influence, i.e. twice consumed wrapper influence; inherited B/2 is still unpaid. B_x(W)<=1-mu^2<=4Inf_x(W), with x influence a separate terminal reserve. H(W)=H(G)/2+R(mu); retain exact E R(mu_leaf) and E H(G_leaf)/2 rather than inventing a threshold leaf certificate. Three-bit point core mu=-3/4,a=1/4 gives D<0; unsigned banks lose credit. General composition split/envelope already belongs to A056/A057; new scope is sharp signed one-control transport and adaptive nonreuse. Next live obstruction: two cores sharing a physical coordinate, requiring one common reserve.\n')
paths=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']
for p in paths:assert p.stat().st_size<20*1024*1024
write('out/PERSISTENCE.json',dict(saved_at=now,scope='local writes verified, no mirror or independent review implied',
 artifacts=[dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in paths],
 rolling=[dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']]))
print(json.dumps(dict(saved=True,run=str(ROOT),exact_assertions=validation['exact_assertions'],
                     correction_upper_diagnostic=float(hi),files=len(paths)+1,schema='PASS')))
