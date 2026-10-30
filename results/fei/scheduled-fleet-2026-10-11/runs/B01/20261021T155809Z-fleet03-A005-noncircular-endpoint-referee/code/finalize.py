from pathlib import Path
import json, hashlib, datetime
r = Path(__file__).resolve().parents[1]
own = r.parents[1]
def save(n, o):
    (r/n).write_text(json.dumps(o, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
check = json.loads((r/'out/CHECK.json').read_text(encoding='utf-8'))
assert check['status'] == 'PASS'
lean = json.loads((r/'out/LEAN.json').read_text(encoding='utf-8'))
ls = lean.get('result', lean).get('status', 'UNKNOWN')
statement = 'For every finite uniform Boolean sign f, let R_c be the spectral Bregman remainder of k(t)=-t^2 log2(t^2)+3t^2/ln2 for the edit to constant c=+1 or -1, with continuous zero terms. Writing mu=E f, R_c=H+4/ln2+c(2mu log2(mu^2)-4mu/ln2). Thus R_++R_-=2H+8/ln2 and R_min=H+a(abs(mu)), where a(u)=4(1-u+u ln u)/ln2 and 0<=a(abs(mu))<=4I^2/ln2. Every nonconstant Boolean seed embeds into actual Boolean functions F_t with I(F_t)->0, mean->1 and R_min(F_t)/I(F_t)->H(seed)/I(seed). If C_star=sup_all H/I in the extended reals and M(eps)=sup_{0<I<=eps}R_min/I, then C_star<=M(eps)<=C_star+4eps/ln2 and lim_{eps down to0}M(eps)=C_star. A uniform small-influence bound R_min<=KI implies full FEI at the SAME K. No exact fixed-eps converse or critical-witness admission is asserted.'
claim = {
    'claim_id': 'A005-WHOLE-SIGN-REFUND-SAME-CONSTANT-HARDNESS', 'version': 1,
    'exact_statement': statement,
    'hypotheses': [
        'Actual Boolean signs on finite uniform cubes, normalized real Walsh coefficients, entropy bits',
        'Zero terms continuous; convexity only needed on [-1,1]',
        'Ratios use I>0; constants have R_min=H=0',
        'Fixed seed nonconstant; disjoint tensor, fresh balancing literal, ceil(sqrt(t)) fair point controls',
        'No finite maximality, minimal dimension or actual child certification assumed or concluded'],
    'statement_sha256': hashlib.sha256(statement.encode('utf-8')).hexdigest(),
    'contributors': ['fleet03/A005'],
    'proof_source': ['DERIVATION.md Sections1--4', 'code/check.py', 'out/CHECK.json'],
    'proof_dependencies': ['Parseval, elementary log inequality and explicit finite activation spectrum; no unproved FEI estimate'],
    'review_records': [], 'status': 'AUTHOR_PROOF_EXACT_FINITE_CHECKED_PENDING_INDEPENDENT_REVIEW',
    'supersedes': [], 'refutes': [], 'first_unproved_line': None,
    'next_consumers': ['A051', 'A052', 'A055', 'A002', 'A090', 'A094', 'B20']}
save('CLAIMS.json', [claim])
save('SCOPE_VERDICTS.json', {
    'A052_section4': {'verdict': 'HOLDS_FOR_WHOLE_SIGN_SPECIALIZATION_ONLY',
                     'reconstruction': 'Direct Fourier expansion and physical whole-sign edit identity at K=0,3,6 on every n<=3 Boolean sign',
                     'excluded': 'No acceptance of full flow equivalence, arbitrary-edit theorem, critical selection or pair payment'},
    'refund_shortcut': {'verdict': 'SAME_CONSTANT_FEI_HARD',
                       'scope': 'No registered theorem refuted; arbitrary seeds not claimed critical'}})
next_action = 'A052/A051 derive a proper physical-pair comparison from finite maximality and the SAME unused D+S reserve, without assuming O(I) whole-sign refund payment; A055/A094 review this endpoint obstruction and full terminals.'
p = {
    'protocol_revision': '2026-10-11-execution-v2', 'run_id': r.name,
    'stream': 'B01', 'packet_id': 'A005', 'gap_id': 'G-R-SELECT',
    'attempt_id': 'A005-whole-sign-refund-audit-1',
    'method': 'Scoped independent Bregman replay; exact entropy identity; rare seed admission',
    'mathematical_delta': 'R_min=H+a(abs(mu)),0<=a<=4I^2/ln2; the small-I limiting optimal constant equals full FEI constant. Proper critical pair transfer remains unpaid.',
    'deliverable_status': 'COMPLETE_LOCAL',
    'mathematical_status': 'SCOPED_AUTHOR_PROOF_REVIEW_PENDING_FULL_FEI_OPEN',
    'claim_versions_used': ['A052 Section4 curvature identity, scoped whole-sign replay only'],
    'claims_created_or_changed': [claim['claim_id']+'@1'],
    'source_artifacts': ['DERIVATION.md', 'SCOPE_VERDICTS.json', 'out/SOURCE_MANIFEST.json', 'out/FROZEN_SPEC.json', 'code/check.py', 'out/PILOT.json', 'out/CHECK.json', 'out/LEAN.json'],
    'next_consumers': ['A051', 'A052', 'A055', 'A090', 'A094', 'B20'],
    'next_action': next_action, 'stagnant_substantive_attempts': 0,
    'blockers': ['Universal proper-pair payment from finite maximality is unproved; complete terminals remain', 'Independent review and remote mirrors unverified'],
    'packet_ids': ['A005']}
save('PROGRESS.json', p)
save('PACKET_DELTA.json', p)
report = """# exact target, quantifiers, hypotheses and units

A005/B01 current stage: audit whole-sign curvature refunds as a universal payment resource for every actual Boolean sign on every finite uniform cube. Entropy is in bits; ln is natural. CLAIMS.json states the exact theorem. Full FEI remains OPEN. The current owner deadline, 23 October2026 14:49UTC, supersedes the historical21October deadline in the read-only protocol.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL2026-10-11-execution-v2 read fully; README, CURRENT_STATUS, registry/packet entries and B01 next action inspected. BOARD21October15:51UTC, B01 STREAM_NOTESv1, own STATUS/LEARNED and latest saved REPORT/CLAIMS read. New source: A052 20261014T124751Z REPORT and MONOCHROMATIC_FLOW_PROOF Sections1--5, especially Section4. A055 20261014T064016Z and A002 20261014T100104Z REPORTs supply scope warnings. Supplement campaign/claims/counterexamples/seed/mapping texts and sources inventory inspected; relevant scope/composition excerpts in all four supplied paper versions and campaign-plan A005 acceptance text revisited. This is not a new full-paper audit. Supplied PDF text extractions require cp1252; a failed strict UTF8 read was repaired by explicit decoding without modifying source bytes. Source hashes: out/SOURCE_MANIFEST.json. One read-only two-wording math recall returned background, no matching refund theorem or proof dependency. No internet premise used.

# complete derivation or exact first unsupported line

DERIVATION.md proves R_c=H+4/ln2+c(2mu log2(mu^2)-4mu/ln2), including zero coefficients and constants. Thus Rsum=2H+8/ln2 and R_min=H+4(1-u+u ln u)/ln2,u=abs(mu). Elementary log inequalities and Var<=I bound the correction by4I^2/ln2. A balanced t-copy seed activated by ceil(sqrt(t)) fair controls has explicit entropy/influence formulas, I tending to0, and R_min/I tending to the seed H/I. This proves SAME-K hardness. M(eps) lies between C_star and C_star+4eps/ln2, including the infinite case. No exact fixed-eps converse or critical-witness admission is asserted. First unsupported universal line: derive proper physical-pair payment from actual finite maximality and the SAME unused child reserve, retaining complete terminal entropy. Assuming O(I) whole-sign refund payment already imports full FEI.

# executed validation with domain, arithmetic, commands and outputs

Frozen spec out/FROZEN_SPEC.json precedes searches. Commands from A005: python -X utf8 runs/20261021T155809Z-fleet03-A005-noncircular-endpoint-referee/code/check.py --pilot, then without --pilot. Pilot22 labelled tables/380 assertions/0.0524s PASS. Full278 labelled tables n=0..3 and68 fixed activation fixtures (all14 nonconstant two-bit seeds, point3, majority3, parity3; t=1,2;k=1,2):5788 exact assertions/4.2107s PASS. Integer FWHT independently checked by direct characters; physical edge influence, Fraction prime-log identities, symbolic reciprocal ln2, and40-term atanh rational outward bounds. Both full-sign deficit identities checked at K=0,3,6. Constants, empty edits, zero coefficients, mu=0 and noncritical roots included. No symmetry quotient, dimension escalation, GPU or detached work. Estimated RAM80MB, peak unmeasured;55s cap. Lean scalar-check attempt: LEAN_STATUS. No formal certification claimed; out/LEAN.json records the exact outcome. Two finalizer-generation attempts failed at Python quoting before writing anything; code/finalize.py replaces them. These operational failures do not affect the unchanged mathematical checker or its saved outputs.

# proof dependencies and changed downstream conclusions

A052 Section4 receives scoped HOLDS for the whole-sign identity only, by an independent direct expansion. Full flow equivalence and critical selection are not accepted by that replay. The scoped theorem has an author proof and exact finite validation, pending independent review. No universal FEI constant improves. The payment interface now has a concrete circularity guard: even the smaller whole-sign refund retains arbitrary-seed hardness at the SAME constant in the rare regime. Complete terminals and actual witness eligibility remain required.

# one next mathematical action and independent reviewer

NEXT_ACTION

# actual persistence receipts or precise save blocker

All four protocol files, derivation, scoped verdict, frozen spec, code and exact outputs saved under A005. code/finalize.py checks protocol field sets, byte-identical PROGRESS/PACKET_DELTA and20MB cap. out/PERSISTENCE_RECEIPT.json hashes every run artifact except itself plus the three rolling files. Local persistence only: independent review, registry adoption, supervisor copy and remote mirror remain unverified. No local save blocker.

## Universal bridge

C019 stopping-tree payment through B11 critical curvature and physical-pair selection: this stage evaluates the whole-sign refund exactly and proves its smaller rare-regime endpoint has the full FEI limiting optimal constant, with explicit error4eps/ln2. It rules out interpreting a whole-sign refund bound as an independently funded resource. No universal constant gain is claimed. What remains is a proper-pair comparison from finite maximality spending one SAME unused D+S bank and retaining all terminals. NEXT targets that universal unpaid implication; another qualitative critical-class admission leaves this entropy obligation unchanged.
""".replace('LEAN_STATUS', ls).replace('NEXT_ACTION', next_action)
(r/'REPORT.md').write_text(report, encoding='utf-8')
f = json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
assert set(claim) == set(f['claim_fields'])
ex = set(f['progress_fields'])
ex.remove('packet_ids (one primary ID, for compatibility)')
ex.add('packet_ids')
assert set(p) == ex
for h in f['report_fields']:
    assert '# '+h in report
assert (r/'PROGRESS.json').read_bytes() == (r/'PACKET_DELTA.json').read_bytes()
(own/'STATUS.md').write_text('STATE: A005 stage complete: exact whole-sign refund; smaller-refund rare endpoint SAME-K FEI-hard;5788 exact checks PASS; review pending; FEI OPEN.\nNEXT: A052/A051 derive proper-pair payment from finite maximality and SAME unused D+S bank; A055/A094 review refund circularity guard and full terminals.\n', encoding='utf-8')
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
with (own/'WORKLOG.md').open('a', encoding='utf-8', newline='') as z:
    z.write('\n'+now+' '+r.name+': Rsum=2H+8/ln2; Rmin=H+a(abs(mu)),0<=a<=4I^2/ln2. Scoped A052 whole-sign identity HOLDS. Rare balanced tensor admission gives SAME-K hardness. Pilot380/full5788 exact assertions PASS. Lean '+ls+', no formal claim. Proper critical payment remains OPEN.\n')
with (own/'LEARNED.md').open('a', encoding='utf-8', newline='') as z:
    z.write('\n'+now+' Whole-sign refunds: R_c=H+4/ln2+c(2mu log2(mu^2)-4mu/ln2); sum minus8/ln2 equals2H. Rmin=H+4(1-u+u ln u)/ln2,u=abs(mu), correction in[0,4I^2/ln2]. Optimal small-I endpoint tends to full FEI optimal constant, including infinity. Uniform Rmin<=KI near I=0 implies SAME-K FEI; FEI(K) gives only K+4eps/ln2 at fixed eps. No seed admitted into genuine minimal witnesses. Whole-sign refund payment cannot be assumed as a fresh resource.\n')
receipts = []
for q in sorted(r.rglob('*')):
    if q.is_file() and q.name != 'PERSISTENCE_RECEIPT.json':
        assert q.stat().st_size < 20_000_000
        receipts.append({'path': str(q.relative_to(r)), 'bytes': q.stat().st_size, 'sha256': sha(q)})
for name in ['STATUS.md', 'WORKLOG.md', 'LEARNED.md']:
    q = own/name
    receipts.append({'path': str(q), 'bytes': q.stat().st_size, 'sha256': sha(q)})
save('out/PERSISTENCE_RECEIPT.json', {'status': 'LOCAL_VERIFIED', 'at_utc': now, 'files': receipts, 'remote_copy': 'UNVERIFIED', 'independent_review': 'PENDING'})
print(json.dumps({'status': 'LOCAL_COMPLETE', 'files_hashed': len(receipts), 'schema': 'PASS', 'exact_assertions': check['exact_assertions'], 'lean_status': ls}))
