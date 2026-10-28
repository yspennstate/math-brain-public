from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]
run=ROOT.name; stamp=datetime.now(timezone.utc).isoformat()
def save(name,obj): (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def rawclaim(c): return hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
agents=AGENT.parent
srcs=[('A059','20261026T223551Z-account04-A059-decomposition-depth'),('A060','20261027T011815Z-account04-A060-composition-sharpness')]
claims=[]
for agent,runid in srcs:
    p=agents/agent/'runs'/runid/'CLAIMS.json'
    c=json.loads(p.read_text(encoding='utf-8'))[0]
    assert rawclaim(c)==c['statement_sha256']
    c['review_records'].append(dict(reviewer='A091',verdict='ACCEPT_NEW_TRANSACTION_AT_WRITTEN_SCOPE' if agent=='A059' else 'ACCEPT_EXACT_TERMINAL_LAW',source=str(ROOT/'PROOF.md'),method='independent algebra, direct-character spectra, all804 local controls and6912 outcome-adaptive policies; A091 original source contribution disclosed'))
    c['status']='SCOPED_A091_INDEPENDENT_ACCEPTANCE; SOURCE_CONTRIBUTION_DISCLOSED' if agent=='A059' else 'INDEPENDENTLY_RECONSTRUCTED_BY_A091_AT_STATED_SCOPE'
    claims.append(c)
def newclaim(cid,statement,hypotheses,dependencies,gap,refs):
    return dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hypotheses,statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A091'],proof_source=dict(path=str(ROOT/'PROOF.md'),sha256=sha(ROOT/'PROOF.md'),validation=refs),proof_dependencies=dependencies,review_records=[dict(reviewer='A091',verdict='AUTHOR_PROOF_AND_EXACT_CONTROLS; NOT_EXTERNAL_REVIEW')],status='PROOF_WITH_EXACT_CERTIFICATE; INDEPENDENT_REVIEW_PENDING',supersedes=[],refutes=[],first_unproved_line=gap,next_consumers=['A057','A059','A060','A087','A094','B19','B20'])
claims.append(newclaim('A091-ACTUAL-FEE-ADAPTIVE-CONTINUATION',
    'For every finite uniform Boolean core in the coherent expected-resource interface with SAME unspent original rate A=9/2, at any actual core query let D be full core entropy decrement, p coordinate influence, I total influence and J=I-p. If J>0, q_star=min(1,(AI-D)/(AJ)) is the largest answer-independent continuation probability whose pending potential AtI has nonnegative local release. Every fresh independent dyadic q<=q_star gives a paid finite stopping policy preserving old costs and both full terminals; q_star=1 iff D<=Ap. At the ideal real-coin boundary the discarded future influence obeys A*E[tI; forced stops]=sum_node w*t*(D-Ap)_+, with explicit nonnegative correction for dyadic rounding. J=0 has constant children and no division. This is not a payment of forced-stop terminal entropy.',
    ['finite uniform physical cubes, Boolean sign outputs, entropy bits','coherent source/exterior escrow retained exactly; rate allocated before use','fresh independent dyadic continuation chosen before the core answer; all killed siblings kept','expected-resource innovations allowed; no pathwise subtraction-only claim'],
    ['A059-EXACT-EXCESS-ESCROW-AND-CORE-OWNER-OBSTRUCTION@2','universal singleton D<=29I/13 independently reconstructed from A060','physical influence conservation'],
    'Pay complete arbitrary-core forced-stop and cap entropy from a sufficiently large dimension-independent ORIGINAL rate; fixed9/2 is obstructed by the next certificate.',
    ['out/main.json','out/ADVERSARY.json']))
claims.append(newclaim('A091-FIXED-NINE-HALVES-FULL-CORE-PAYMENT-OBSTRUCTION',
    'Let g0(x)=x and g_(d+1)=NAND(g_d(X),g_d(Y)) on independent disjoint copies, NAND negative exactly at(+1,+1). The32-bit depth5 seed has I=98620389/67108864 and certified H-(9/2)I>1/10. Let G=z times2048 independent seed copies with one untouched fair tag. In the four-bit paired-bent all-one-point wrapper F=b-C+C*G (c=1/16), full dimension65541, H(F)-[E0+7+(9/32)(2048*I(g5)+1)]>883/160, where E0 is the exact bounded coherent wrapper profile. Thus complete universal terminal payment from this fixed original9/2 core owner plus original exterior7 is impossible even granting E0 free. This refutes that fixed-budget extension, not FEI or A059 partial stopping.',
    ['uniform physical inputs and disjoint seed copies','exact sign NAND convention and actual bent-point wrapper','all full terminal entropy retained; any old nonnegative debit remains booked','rational interval entropy certificate, no high-dimensional truth-table extrapolation'],
    ['exact biased-output disjoint NAND Fourier composition derived in PROOF Section5','direct disjoint product additivity','balanced core coherent wrapper identity independently checked'],
    'Find a sufficiently large finite ORIGINAL all-core rate and a useful terminal-decaying continuation; no claim that every larger rate fails.',
    ['out/SEED_CERTIFICATE.json','out/TENSOR_CERTIFICATE.json']))
claims[-1]['refutes']=['Universal full-terminal payment from the fixed original9/2 core source plus bounded wrapper/exterior credit']
save('CLAIMS.json',claims)
next_action='A059/A060/A087 independently audit adaptive liquidation and certified NAND source obstruction; replace impossible universal fixed9/2 full payment by a sufficiently large ORIGINAL rate and necessary entropy-decaying arbitrary-core policy, with old debits and both full terminals retained.'
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=run,stream='B19',packet_id='A091',gap_id='G-LOWSEL-COLLISION',attempt_id='A091-stage22-actual-fee-and-fixed-source-obstruction',method='independent transaction/full-terminal review; direct-character and butterfly spectra; rational interval composition certificate and tensor budget obstruction',mathematical_delta='A059 new two-ticket transactions and A060 full-terminal law accepted at scope; actual-fee adaptive continuation proved; actual32-bit NAND seed and65541-bit wrapper rigorously obstruct universal complete payment from fixed original9/2, excess>883/160. FEI OPEN.',deliverable_status='COMPLETE',mathematical_status='SCOPED_REVIEW_ACCEPTANCE_AND_NEW_EXACT_OBSTRUCTION; FULL_FEI_OPEN',claim_versions_used=[c['claim_id']+'@'+str(c['version']) for c in claims[:2]]+['A059-EXACT-EXCESS-ESCROW-AND-CORE-OWNER-OBSTRUCTION@2','A091-ONESHOT-ORIGINAL-CORE-INFLUENCE-PAYMENT@1'],claims_created_or_changed=[c['claim_id']+'@'+str(c['version']) for c in claims],source_artifacts=[str(ROOT/p) for p in ['PROOF.md','SPEC.json','SEED_SPEC.json','out/SOURCES.json','out/main.json','out/ADVERSARY.json','out/SEED_CERTIFICATE.json','out/TENSOR_CERTIFICATE.json']],next_consumers=['A057','A059','A060','A087','A094','B19','B20'],next_action=next_action,stagnant_substantive_attempts=0,blockers=['Arbitrary-core complete original source/terminal entropy payment remains unpaid.','Fixed9/2 universal full-payment target now rigorously impossible; larger rate not refuted.','Lean RUNTIME_UNVERIFIED timeout; no formal theorem certificate.'],packet_ids=['A091'])
save('PROGRESS.json',progress); save('PACKET_DELTA.json',progress)
main=json.loads((ROOT/'out/main.json').read_text(encoding='utf-8')); adv=json.loads((ROOT/'out/ADVERSARY.json').read_text(encoding='utf-8'))
report=f'''# A091 composition referee stage22

## exact target, quantifiers, hypotheses and units

Independently audit A059 prepaid two-ticket/geometric theorem v1 and A060 stopped full-terminal law v1, then advance the universal original-source payment gap. Finite uniform physical cubes, Boolean signs, entropy bits, arbitrary Boolean output biases. One actual reused core is retained, not independent copies of a shared physical block. Expected-resource scope includes branch transfers, all old costs, current coherent profile and BOTH full terminals. Full FEI OPEN.

## sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2, current BOARD B09/B12/B19/B20 entries, B19 lead v2 and own stage21 STATUS/LEARNED/REPORT/ONESHOT_PROOF. Direct load-bearing sources: A059 run20261026T223551Z PROOF Sections1--4 and CLAIMS@1; A060 run20261027T011815Z PROOF Sections1--5 and CLAIMS@1. Both exact statement hashes independently match. out/SOURCES.json records38 source pins, including campaign navigation, registries, plan, supplement and four paper-version text files; paper composition/pivotal locator refresh is in out/PAPER_LOCATORS.json. Earlier accepted baseline is reused, with no new literature or priority assertion. A091 supplied the older original9/2 source, so its review accepts the NEW A059 transactions at scope, not its own dependency as an independent full-chain referee.

## complete derivation or exact first unsupported line

PROOF Sections1--3 reconstruct universal singleton D<=29I/13, split9/2=2(29/13)+1/26, both paid tickets, fresh independent geometric transactions, and the exact complete-terminal law E0+(r-S_r)/8. A059 and A060 hold at their written scopes; fixed-q depth alone leaves terminal/root entropy tending to one.

Section4 replaces uniform compulsory killing by the actual-fee maximum q*=min(1,(AI-D)/(A(I-p))) at A=9/2. All dyadic q<=q* are paid, exact-zero remaining influence is handled separately, and q*=1 iff D<=Ap. The ideal boundary liquidates exactly local excess (D-Ap)+ in discarded influence; dyadic rounding has an explicit extra term. This repairs deterministic continuation on tagged AND2 products without inventing a new source, while preserving stopped-child entropy.

Section5 supplies a sharper obstruction to the inherited NEXT. The actual32-variable complete NAND seed has certified H-(9/2)I>1/10. Its2048-copy tagged four-bit wrapper has65541 physical variables and complete entropy exceeding original exterior7 plus core9/2 influence, EVEN granting E0 free, by>883/160. Therefore universal complete payment at this FIXED rate is impossible; no continuation rearrangement can make all full terminals vanish within that budget. A sufficiently large dimension-independent rate is not refuted. The first unpaid line is original all-core payment/necessary entropy decay at such a larger rate; full FEI remains OPEN.

## executed validation with domain, arithmetic, commands and outputs

SPEC.json and SEED_SPEC.json frozen before their searches, out/TENSOR_SPEC.json before the tensor calculation. Main command: python -B -X utf8 code/check.py main. PASS: {main['assertions']} exact assertions on all278 signs n0..3,804 coordinate cases, complete fixed-order stopped trees, direct physical wrapper spectra and a fixed9-bit genuine-tag forced-stop witness. No symmetry reduction. Main measured{main['seconds']:.3f}s. Pilot2731 assertions on38 signs/84 edges passed. Separate code/adversary.py PASS: {adv['scalar_assertions']} rational scalar assertions and6912 outcome-adaptive two-query policies/{adv['two_query_assertions']} exact terminal/ticket assertions; measured{adv['seconds']:.3f}s. The algorithms independently compare direct character sums and butterfly spectra, exact edge and spectral influences, full terminal entropy and original account conservation.

code/seed.py is numerical discovery ONLY over22 frozen formula states. code/seed_certificate.py certifies the SAME states with96-bit outward dyadic intervals,36-term rational atanh and geometric tail; direct actual truth tables check depths0..3. The first strict seed is depth5; margin>1/10 uses rational comparison. code/tensor_certificate.py applies exact disjoint identities at N2048; it does not enumerate65541-bit truth tables. Its complete entropy gap>883/160 is rationally certified. Scripts are saved and command-independent hashes are recorded; no floating sign is used as proof.

Estimated main100MB and seed120MB; no >300MB search, GPU, detached job, new worker or automatic dimension escalation. Fresh memok before Lean exited0 (9.3GB physical/17.3GB commit free). Named Lean scalar target a091_feasible_continuation, exact submitted source hash4d0d5983cbb19999023ac8bebec4c3cb3a2971b7b7a54db90ef8e20e9cef0ee5, timed out after54.319s: RUNTIME_UNVERIFIED, no target kind/axioms verified. This is not a formal certificate or a mathematical refutation. The initial progress description called this an admission hold; the actual receipt corrects it to a runtime timeout. No retry or load shedding. Lean receipt is preserved as produced; its UTF16LE PowerShell serialization is normalized with provenance for readback.

## proof dependencies and changed downstream conclusions

Dependencies: finite Parseval, physical influence conservation, exact entropy erasure plus amplitude-pair JS bound, cube edge isoperimetry, elementary concavity, and the previously audited coherent exterior interface. New adaptive proof is an author result pending external review. New fixed-rate obstruction is an exact finite Boolean composition certificate pending independent reconstruction. A059's partial theorem survives. The previous demand to complete ALL arbitrary core entropy from the SAME9/2 owner must change rate; the new obstruction prevents spending further stages trying to prove an impossible payment interface. No claim of a FEI counterfamily.

## one next mathematical action and independent reviewer

{next_action} A094 supplies a disinterested full-chain challenge; A091 recuses from independent acceptance of its own new proofs. The next all-core source must survive the explicit NAND tensor certificate before its continuation/terminal assembly is pursued.

## actual persistence receipts or precise save blocker

Four protocol files, proof, frozen specs, code and exact outputs saved only inside this A091 run; STATUS two lines and dated WORKLOG/LEARNED updated. out/PERSISTENCE.json checks exact protocol fields, imported/new statement hashes, compatibility equality, file-size limits and saved byte hashes. Supervisor copy, registry adoption, external review and mirror verification NOT_OBSERVED. No Git, mail, external message, trading access, other-agent edit or brain research write. Required wake/checklist hooks ran; wake warned stale personal-context sources, disclosed before reliance. Only this session's bounded commands were launched, and no unrelated running work was stopped.

## Universal bridge

C019/C024 advance by independent acceptance of the new two-ticket/full-terminal results, a paid actual-fee continuation with exact influence-liquidation cost, and a rigorous correction of the universal supplier target: fixed original9/2 cannot pay all terminals, with an actual finite Boolean gap>883/160. What remains is a sufficiently large dimension-independent ORIGINAL core rate and useful necessary continuation paying complete terminal entropy. Reviewing this obstruction and changing the source rate is the shortest route toward full FEI because it removes an impossible universal payment demand while retaining every old debit and full terminal law; further closure of an already affordable tensor control cannot supply the missing all-core owner.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: Stage22 saved: A059 new tickets/A060 terminal law scoped HOLDS; adaptive actual-fee rule; certified NAND tensor disproves universal original9/2 full payment by>883/160; FEI OPEN.\nNEXT: '+next_action+'\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write(f'\n{stamp} {ROOT.name}: independent new-ticket/full-terminal review; main20543 + scalar11101 + two-policy13824 exact assertions PASS;32-bit NAND seed H-4.5I>1/10 and65541-bit wrapper full-budget gap>883/160 certified. Actual-fee adaptive continuation paid; fixed9/2 universal terminal target impossible. Lean runtime timeout UNVERIFIED; no formal claim. All run outputs saved; FEI OPEN.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f: f.write(f'\n{stamp} Stage22: Actual-fee continuation q*=min(1,(AI-D)/(A(I-p))) maximizes feasible answer-independent survival for pendingAtI; q*=1 iff D<=Ap. For ideal boundary A times forced-stop influence equals sum actual overruns(D-Ap)+; dyadic rounding adds explicit nonnegative correction; this is not terminal entropy payment. A0592-ticket refinement holds only if split before first use. Complete NAND depth5 on32 bits has I98620389/67108864 and certifiedH-9I/2>1/10;2048-copy tagged four-bit wrapper exceeds original9/2 core+7 exterior EVEN freeE0 by>883/160. Universal full-terminal9/2 source target is impossible; larger ORIGINAL rate remains open. Lean scalar timed out, no certification.\n')
# Preserve original tool receipt, whose shell redirection used UTF16LE.
lp=ROOT/'out/LEAN_RECEIPT.json'
if lp.exists():
    raw=lp.read_bytes(); text=raw.decode('utf-16') if raw.startswith(b'\xff\xfe') else raw.decode('utf-8-sig')
    receipt=json.loads(text); save('out/LEAN_NORMALIZED.json',dict(original_sha256=sha(lp),original_encoding='UTF16LE BOM' if raw.startswith(b'\xff\xfe') else 'UTF8',receipt=receipt))
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
pf=set(protocol['progress_fields']); pf.remove('packet_ids (one primary ID, for compatibility)'); pf.add('packet_ids')
assert set(progress)==pf
for c in claims:
    assert set(c)==set(protocol['claim_fields'])
    assert rawclaim(c)==c['statement_sha256']
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for field in protocol['report_fields']: assert '## '+field in report
assert report.rstrip().split('## ')[-1].startswith('Universal bridge')
records=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE.json':
        assert p.stat().st_size<20_000_000
        records.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p)))
save('out/PERSISTENCE.json',dict(status='PASS',saved_at=stamp,claim_count=len(claims),progress_exact_fields=True,claim_exact_fields=True,statement_hashes=True,compatibility_equal=True,rolling_status_two_lines=True,files=records,rolling=[dict(path=str(AGENT/n),sha256=sha(AGENT/n)) for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],publication='NOT_OBSERVED'))
print(json.dumps(dict(status='PASS',claim_count=len(claims),files=len(records),run=str(ROOT))))
