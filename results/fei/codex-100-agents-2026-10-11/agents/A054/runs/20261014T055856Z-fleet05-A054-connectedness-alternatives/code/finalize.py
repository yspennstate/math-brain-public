from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):(ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
c=json.loads((ROOT/'out/EXACT_CHECK.json').read_text());pilot=json.loads((ROOT/'out/PILOT.json').read_text())
assert c['status']==pilot['status']=='PASS' and c['block_cases']==1574 and c['assertions']==31859
previous=AGENT/'runs/20261014T025808Z-fleet05-A054-connectedness-alternatives'
workers=AGENT.parent
source=workers/'A053/runs/20261014T052310Z-fleet05-A053-near-tensor-perturbations'
statement=('For every indicator g on a finite uniform physical cube with actual connected components g_k, every nonempty proper r-coordinate block A, and retained coordinate Y, define m_ky=E_A g_k, W_A=sum_k E_Y m_ky log2(1/m_ky), Q_A=E_Y m_y log2(1/m_y), and Omega_A=E_Y m_y H((m_ky/m_y)_k). '
'Then W_A=Q_A+Omega_A=p[r-H(X_A|Y,L,g=1)] and E_A(g)>=W_A/2, with no component-projection separation hypothesis. '
'The original-label raw component excess satisfies Delta_root=X_A+Z_A<=Gamma_A+Z_A with Z_A=E_actual_child Delta_child and Gamma_A=[rp+(2/ln2)E_A(g)-sum_k Lambda_A(g_k)]_+; Z_A is never discarded. '
'For the actual sign f=1-2g, W_A>=rp/2 implies L_A(f)<=C I_A(f), C=4+2/ln2+4/(e ln2)<37/4. Thus physical-descendant ratio-critical sources in this class have H/I<=C, and least-essential-dimension K-violations at K>=C are excluded with all actual child reserves retained. '
'For every such minimal violation and every proper block at K>a=2/ln2+4/(e ln2), H(X_A|Y,L,g=1)>=r[1-2/(K-a)]+(D_K+S_A)/(2p(K-a)). '
'At essential dimension n>=2 this forces sum_k(p_k/p)log2|U_k|>=(n-1)[1-2/(K-a)]+(D_K+S_A)/(2p(K-a)) for any n-1 cut; in particular at K>=C both sign level sets contain a component larger than2^((n-1)/2). Universal paid-block admission is not asserted.')
hyp=['Finite uniform physical cubes; actual Boolean signs and indicators; Fourier and Shannon entropy in bits',
 'Components are actual connected components in the physical cube; their original labels are retained after restricting queried coordinates',
 'Block is proper and nonempty; p>0 where conditional laws or ratios are used; zero fibers contribute zero',
 'Payment condition is W_A>=r p/2; overlapping projections and connected support are allowed',
 'Criticality conclusions use actual physical descendants; minimal fixed-K violation means least essential dimension among all Boolean K-violations',
 'The terminal component excess is signed and is retained in the exact ledger; no uncontrolled terminal is certified or discarded']
dependency=dict(claim_id='A054-RAW-SIGN-BLOCK-TREE-TRANSFER',version=1,acceptance='AUTHOR_PROVED_SOURCE_COMPLETE_PENDING_INDEPENDENT_REVIEW',source=str(previous/'RAW_SIGN_TRANSFER.md'),used_scope='Universal block transfer (5), raw row logarithmic Sobolev normalization; not the old disjoint-projection hypothesis')
claim=dict(claim_id='A054-OVERLAP-FIBER-PAYMENT-GIANT-COMPONENT',version=1,exact_statement=statement,hypotheses=hyp,
 statement_sha256=hashlib.sha256(json.dumps(dict(statement=statement,hypotheses=hyp),sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 contributors=['fleet05/A054'],proof_source=dict(path=str(ROOT/'OVERLAP_PAYMENT.md'),sha256=sha(ROOT/'OVERLAP_PAYMENT.md'),locator='sections1--5; equations(1)--(13)'),
 proof_dependencies=[dependency],review_records=[],status='AUTHOR_PROVED_EXACT_VALIDATION_PASS_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],first_unproved_line=None,
 next_consumers=['A051','A052','A053','A055','claude/B11','A090','A094','B20'])
save('CLAIMS.json',[claim])
report=f'''# exact target, quantifiers, hypotheses and units

A054/B11 stage {ROOT.name}: pay actual proper-block entropy when
component projections overlap, without deleting the original-label
terminal cross term. All cubes finite and uniform, f=1-2g actual
Boolean, entropy bits, I_A(f)=4E_A(g). The paid class now requires
within-component queried-fiber entropy at most half the block width;
it requires neither disjoint projections nor a density lower bound.
Derive a necessary giant-component condition for hypothetical minimal
high-threshold witnesses. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read own STATUS and previous RAW_SIGN_TRANSFER.md, mathematical helper
and finalize source; read current BOARD B11 rows and later header
(06:02UTC); full board refreshed at06:12UTC (truncated middle
sections separately retrieved), and unchanged complete B11 STREAM_NOTESv2 from Oct11.
The lead's original Brain45/interface direction is already completed;
the new live gap is actual signed payment and terminal reserve.
Read complete EXECUTION_PROTOCOL revision2026-10-11-execution-v2.
Earlier campaign/paper background is not presented as newly read.
New source consumed: A053 stage5 REPORT, CLAIMS,
PACKING_CRITICAL_EXCLUSION.md sections1--4 and checker opening.
REVIEW_A053.md independently reconstructs the complete bundled analytic
statement, including its pair/refund constants and critical exclusion,
without repair. Source finite census is not adopted. Exact source paths,
current byte hashes and revisions are in SOURCE_MANIFEST.json.

# complete derivation or exact first unsupported line

OVERLAP_PAYMENT.md is the complete new proof with the exact prior
transfer dependency stated. Physical component labels give the
identity W_A=Q_A+Omega_A=p[r-H(X_A|Y,L,g=1)]. Fiberwise edge
isoperimetry and exact boundary additivity give E_A(g)>=W_A/2.
Projection overlap adds a nonnegative physical label-entropy credit;
it does not license erasing spectral terminal excess. For every block,
Delta_root=X_A+Z_A<=Gamma_A+Z_A, where original component labels
survive in actual children. Z_A may be nonzero and has no asserted
universal sign or free bound. The terminal-inclusive interface
P_A(K) is explicitly expressed using Delta_root-Z_A, the component
block drops and the exact sign/raw scalar correction; it equals
L_A(f)-K I_A(f), with no virtual component treated as a descendant.

The universal raw/sign transfer and raw row upper bound imply
P_A(K)<=4rp+(a-K)I_A, a=2/ln2+4/(e ln2). When W_A>=rp/2,
I_A>=rp, so L_A<=C I_A at C=4+a<37/4 (same C as last stage,
rigorously <9.008342). This extends prior projection admission to
overlap and also admits connected supports with full projections but
sparse actual fibers. The original-label terminal cross term is paid
only as part of the actual child ledger; root-only component entropy
payment is not claimed.

For every minimal K-violation, actual S_A=-E_child D_K>=0 and
D_K+S_A=L_A-K I_A. Thus 2(K-a)W_A+D_K+S_A<=4rp for K>a.
The conditional entropy lower bound (12) and weighted component-size
bound (13) follow. At K>=C, each sign level set must have a component
larger than2^((n-1)/2); the weighted geometric mean condition is
stronger. Replacing f by -f preserves every physical deficit, so the
conclusion applies independently to both level sets. This excludes
minimal witnesses with uniformly small components, irrespective of
component shape, placement, density or overlapping projections.

First unsupported line: a uniformly paid proper block for the
remaining hypothetical witnesses with giant components in BOTH sign
sets and high within-component conditional fiber entropy on every
proper block. Conditional entropy alone does not supply that choice;
actual signed phase/refund and child reserves remain a possible route.
No universal FEI constant or criticality-preserving reduction is claimed.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json saved before validation. Helper mathcore.py copied
from the previous run; the new checker separately constructs retained-Y
physical fibers, original labels in queried-X child truth tables,
integer Walsh spectra and direct physical edge energy. The final v2
domain is all278 labeled indicators n<=3 and all1568 proper nonempty
cuts, plus six explicitly frozen fixtures: identical overlapping
projections at n8, connected full queried projection at n4, two
overlapping paths at n5, Brain45 and Brain44 original data separators,
and a full-overlap zero-influence n4 control. No symmetry quotient or
automatic dimension growth. Counts measure block cases, not distinct
root functions or critical roots.

    python -X utf8 runs\\{ROOT.name}\\code\\check_overlap.py --pilot
    python -X utf8 runs\\{ROOT.name}\\code\\check_overlap.py

Final pilot: {pilot['assertions']} exact checks,35 block cases,
{pilot['seconds']:.6f}s. Final full: {c['assertions']} exact checks,
{c['block_cases']} block cases,883 paid cases,147 overlapping cases,
{c['seconds']:.6f}s. All PASS. Fraction and canonical prime-log
vectors verify identities; range-reduced32-term atanh with explicit
tail and outward112-bit dyadic intervals decide signs. The rational
relaxation37/4 is proved analytically, not a floating entropy check.
Class fixtures are not called critical and no violating root is found.

The n5 fixture has component paths {{0,4,12,13,15}} and
{{3,19,27,26,24}}, A=bits0,1, p=5/16. Exact
Q=9/16-(3/16)log2 3<p while
W=5/8-(3/16)log2 3>p=rp/2, Omega=1/16.
The old projection credit also fails its threshold. The decisive
integer signs are3^3>2^4 and3^3<2^5. The terminal cross term is
-3/4+(9/32)log2 3, retained exactly; sign drop is
5/2-(9/16)log2 3, I_A=3/4. The n4 connected fixture
{{0,1,5,7,14,15}} has full queried projection, hence zero old
projection credit, but W=rp/2 and is paid. These examples establish
strict class enlargement, not numerical evidence for universal admission.

V1 pilot/full passed667/31846 assertions; summaries and full fixture output are preserved as
*_V1.json. A useful explicit label-credit fixture then replaced the n4
edge control, and v2 specification was frozen BEFORE the new pilot/full.
No family search or hidden automatic parameter change occurred.
All jobs estimated140MB, below300MB; actual peak unmeasured, so no
memok-gated allocation was required. Runtime caps55/180sec respected;
one mathematical job at a time, no GPU or background process.

# proof dependencies and changed downstream conclusions

Only proof dependency is A054-RAW-SIGN-BLOCK-TREE-TRANSFER@1 at its
universal transfer/raw log-Sobolev scope; author-proved and source-complete,
independent review pending. No dependency on its restrictive disjoint
projection consequence. New edge isoperimetry, label chain rule,
boundary additivity, terminal cross ledger and actual child deficit
arguments are proved locally. A053 analytic review is independent,
not a premise for the new component result and not a registry write.

Changed conclusion: affordable projection cuts do not need separation,
and stronger actual fiber information can pay connected full projections
or overlap where the old projection information is insufficient.
Minimal K>=C witnesses must have giant components in BOTH sign sets;
the quantitative weighted geometric mean and child reserve are retained.
This is a paid-query exclusion with actual descendants, not unrestricted
FEI(C) for an unclosed small-component class. The unrestricted component
ratio/entropy pruning refutations remain valid and are not reopened.

# one next mathematical action and independent reviewer

Next: use the forced large within-component conditional entropy to
select a signed pair/block on a hypothetical two-sided giant-component
critical witness, comparing its complete phase/refund cost with the
actual D_K+S_A bank. One physical influence owner must pay it. A052/A055
are the immediate consumers; A090/A094 should reconstruct the label
chain rule, exact boundary additivity, terminal-ledger cancellation and
two-sign giant-component threshold. No outgoing messages are sent.

# actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and byte-identical PACKET_DELTA saved in the
requested run alongside OVERLAP_PAYMENT, REVIEW_A053, code, frozen
specification and exact outputs. Rolling STATUS, WORKLOG and LEARNED
updated only under A054. out/RECEIPTS checks exact protocol fields,
byte lengths, hashes and the20MB ceiling; no large artifact generated.
Independent review of the new theorem, shared adoption and supervisor
mirrors are pending and not inferred from local persistence.

# Universal bridge

This stage advances B11 critical block selection feeding C019 stopping-
tree payment by removing projection separation and adding the exact
within-component fiber/label credit at the same C<37/4. It pays the
combined actual terminal interface on that larger class and forces BOTH
sign level sets of any remaining minimal high-K witness to have giant
components, with a weighted entropy lower bound retaining every child
reserve. Universal proper-block selection for those remaining giant
components is still unsupported. NEXT targets their actual signed
phase/refund bank because selecting a uniformly paid query would
contradict every minimal FEI witness; another small-component census
would only repeat a now closed admission class.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=ROOT.name,stream='B11',packet_id='A054',gap_id='FEI-B11-A054-INITIAL',attempt_id='A054-component-fiber-overlap-4',
 method='Physical component-label chain rule, fiberwise edge isoperimetry and raw/sign transfer with original-label terminal cross ledger',
 mathematical_delta='Projection separation removed; stronger within-component fiber credit pays actual sign blocks at C<37/4; every remaining minimal K>=C witness has giant components in both sign level sets and a quantitative weighted component-size reserve.',
 deliverable_status='COMPLETE_SAVED_LOCAL',mathematical_status='OVERLAP_CLASS_PAYMENT_AND_CRITICAL_STRUCTURE_PROVED_FULL_FEI_OPEN',
 claim_versions_used=[dependency],claims_created_or_changed=[dict(claim_id=claim['claim_id'],version=1)],
 source_artifacts=['REPORT.md','OVERLAP_PAYMENT.md','REVIEW_A053.md','out/EXACT_CHECK.json','out/FIXTURES.json'],next_consumers=claim['next_consumers'],
 next_action='Select a signed pair/block using forced within-component conditional entropy on two-sided giant-component critical sources, keeping D_K+S_A and one influence owner; A090/A094 independent review.',
 stagnant_substantive_attempts=0,blockers=['Uniform affordable proper-block selection for two-sided giant-component critical sources remains open','Prior transfer/new theorem independent review and shared/remote adoption pending'],packet_ids=['A054'])
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
save('out/REVIEW_RECORDS.json',[dict(claim_id='A053-PACKED-POINT-SURGERY-PAID-SINGLETON',version=1,reviewer='fleet05/A054',verdict='ACCEPT_AT_STATED_ANALYTIC_SCOPE',source='REVIEW_A053.md',repair=False,source_census_adopted=False,registry_adoption='PENDING')])
protocolpath=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
sources=[protocolpath,Path('~/brain_workers/FEI100_20261011/BOARD.md'),Path('~/brain_workers/FEI100_20261011/claude/B11/STREAM_NOTES.md')]
sources += [previous/x for x in ['RAW_SIGN_TRANSFER.md','CLAIMS.json','code/mathcore.py','code/finalize.py']]
sources += [source/x for x in ['REPORT.md','CLAIMS.json','PACKING_CRITICAL_EXCLUSION.md','code/check_packing.py']]
save('out/SOURCE_MANIFEST.json',[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in sources])
(AGENT/'STATUS.md').write_text('STATE: A054 overlapping/connected fiber payment proved at C<37/4; minimal high-K witnesses need giant components in BOTH sign sets;31,859 exact checks PASS; A053 packed-surgery chain reviewed; FEI OPEN.\nNEXT: A052/A055 select an actual signed block on two-sided giant-component critical sources using the conditional-entropy and D+S bank; A090/A094 review.\n',encoding='utf-8')
marker='2026-10-14 / '+ROOT.name
work=f'\n{marker}: Consumed live B11 updates and independently reconstructed complete A053 packed-point-surgery singleton/pair/refund exclusion without repair. Proved W=Q+Omega=p[r-H(X|Y,L,U)] and EA>=W/2, removed projection separation, retained signed terminal cross term, paid actual critical blocks at C<37/4. Derived quantitative weighted component-size necessity and giant component in BOTH sign sets of every minimal K>=C witness. V1 census passed; frozen v2 label-decisive fixture passed {c["assertions"]} assertions/{c["seconds"]:.6f}s,1574 cuts. Universal giant-component selection remains open; artifacts/schema saved.\n'
learn=f'\n{marker}: Actual connected-component fiber information W_A=sum_k E_Y m_ky log2(1/m_ky)=Q_A+pH(L|Y,U) satisfies EA(g)>=W_A/2 because actual component boundary energies add. Thus W_A>=rp/2 pays L_A(1-2g)<=C IA at C=4+2/ln2+4/(e ln2)<37/4, without disjoint projections and at arbitrary rarity, including connected full-projection sparse-fiber supports. Root component excess Delta=X_A+E_child Delta_child retains original labels and signed terminal excess; label entropy does NOT separately bound that excess. Minimal K-violator obeys 2(K-a)W+D+S<=4rp, a=C-4. At K>=C both sign sets contain components >2^((n-1)/2); weighted component geometric mean has the stronger explicit reserve. A five-bit two-path example has Q<p but W>p, Omega=1/16, demonstrating decisive label credit. Full FEI still needs actual block selection for two-sided giant-component witnesses.\n'
for name,text in [('WORKLOG.md',work),('LEARNED.md',learn)]:
 p=AGENT/name
 if marker not in p.read_text(encoding='utf-8'):
  with p.open('a',encoding='utf-8') as f:f.write(text)
protocol=json.loads(protocolpath.read_text());req=protocol['required_per_run']
assert set(claim)==set(req['claim_fields'])
keys=set(req['progress_fields']);keys.remove('packet_ids (one primary ID, for compatibility)');keys.add('packet_ids')
assert set(progress)==keys and (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert all('# '+field in report for field in req['report_fields'])
files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='RECEIPTS.json']+[AGENT/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20_000_000 for p in files)
save('out/RECEIPTS.json',[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(files)])
print(json.dumps(dict(status='SAVED_AND_SCHEMA_CHECKED',assertions=c['assertions'],receipts=len(files),full_fei='OPEN'),indent=2))
