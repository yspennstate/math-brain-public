"""Persist protocol bundle after exact checks; writes only the A063 tree."""
import hashlib
import json
from pathlib import Path
from datetime import datetime,timezone

run = Path(__file__).resolve().parent.parent
agent = run.parent.parent
run_id = run.name
def readjson(name):
    return json.loads((run/name).read_text(encoding='utf-8'))
def save(path,text):
    with path.open('w',encoding='utf-8',newline='\n') as f:
        f.write(text)
def dump(path,obj):
    save(path,json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

pilot,main,audit = [readjson('out/'+name+'.json') for name in ('pilot','main','independent')]
prefix_pilot,prefix = [readjson('out/'+name+'.json') for name in ('prefix_pilot','prefix_main')]
boundary = readjson('out/cone_boundary.json')
for result in (pilot,main,audit,prefix_pilot,prefix,boundary):
    assert result['status'] == 'PASS'
assert pilot['elapsed_seconds'] < 60 and prefix_pilot['elapsed_seconds'] < 60
assert main['elapsed_seconds'] < 300 and audit['elapsed_seconds'] < 300 and prefix['elapsed_seconds'] < 300
assert main['cases'] == 2198 and audit['cases'] == 1099 and prefix['roots'] == 76
assert main['script_sha256'] == pilot['script_sha256'] == sha(run/'code/quadratic_audit.py')
assert audit['script_sha256'] == sha(run/'code/independent_gauss.py')
assert prefix['script_sha256'] == prefix_pilot['script_sha256'] == sha(run/'code/prefix_audit.py')
assert boundary['script_sha256'] == sha(run/'code/cone_boundary.py') and boundary['elapsed_seconds'] < 60

claim_id = 'A063-QUADRATIC-ORIGINAL-RANK-OWNER-OPTIONAL-RESETS'
statement = (
    'For every Boolean quadratic phase over F2 with alternating matrix rank r and m nonzero rows, '
    'start with its actual full-product Fourier reference and use the actual physical-query kernel '
    'extended fairly on every zero-source row. For every adaptive coordinate policy, stopping cut, '
    'and optional full-product-reset schedule, references remain convex mixtures of uniforms on '
    'affine superspaces containing the current actual spectrum. Reference outcomes are fair. '
    'When r>=2, cumulative gross positive actual reset price is at most r/2-1 on every physical path. '
    'The SAME original bank S=4I funds initial source KL m-r once, all gross reset debits, the full '
    'root entropy reservation (therefore full terminal entropy), and an old debit omega<=S/4, '
    'with residual at least one at every cut. Via the source chain this also pays all reached '
    'erasure losses and terminal KL. When r=0, those costs vanish and residual>=3S/4. '
    'For each k>=1, q=z0*(z1+...+z_(k+1))+sum_(j=2)^(k+1) yj*zj is bent on 2k+2 bits; '
    'querying all y bits first requires exactly k extra reference/outcome units beyond initial KL=0, '
    'with no E/O refund, and I=k+1. This sharpens the rank reserve, not the complete bank constant.'
)
claim = {
    'claim_id':claim_id,'version':1,'exact_statement':statement,
    'hypotheses':['uniform cube, base-two entropy/KL','quadratic Boolean phase; arbitrary affine and constant terms',
                  'original actual full-marginal product reference','actual kernel with fair zero-source extension',
                  'adaptive physical queries and arbitrary optional actual product resets',
                  'old debit is relative to the SAME original S=4I; no descendant source admission',
                  'sharp extra reference reserve excludes separately supplied entropy/outside reserves'],
    'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
    'contributors':['A063'],'proof_source':['PROOF.md sections 1-4','PROOF_PREFIX.md sections 1-3'],
    'proof_dependencies':[],
    'review_records':[{'reviewer':'A063','kind':'author exact computational verification, not independent agent acceptance',
                       'artifacts':['out/main.json','out/independent.json','out/prefix_main.json'],
                       'scope':'truth-table Walsh and separate Gauss implementation for local formulas; rational full-history optional-reset audit; general analytic proofs in accompanying files'}],
    'status':'PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
    'first_unproved_line':None,'next_consumers':['A061','A064','A065','A087','A094','B13 lead']
}
dump(run/'CLAIMS.json',[claim])

next_action = ('Pay inherited product-admission gaps and weighted cone repair for a selector between '
               'quadratic phases from the SAME unused original influence bank, then retain an ordinary '
               'data prefix with O/E/K and all old debits. CONE_BOUNDARY.md already refutes literal '
               'unweighted-cone invariance at one selector. Do not renew the child rank owner. '
               'A087/A094 independently review the quadratic history theorem.')
sources = ['PROOF.md','PROOF_PREFIX.md','CONE_BOUNDARY.md','SEARCH_SPEC.json','out/PREFIX_SPEC.json',
           'code/quadratic_audit.py','code/independent_gauss.py','code/prefix_audit.py','code/cone_boundary.py','code/finalize.py',
           'out/pilot.json','out/main.json','out/independent.json','out/prefix_pilot.json','out/prefix_main.json','out/cone_boundary.json',
           'out/BOARD_SNAPSHOT.txt','out/A061_READ.txt','out/A064_READ.txt','out/A065_READ.txt']
progress = {
    'protocol_revision':'2026-10-11-execution-v2','run_id':run_id,'stream':'B13','packet_id':'A063',
    'gap_id':'G-R-MISMATCH','attempt_id':'A063-original-rank-owner-affine-reference-cone-v1',
    'method':'consume A061 ordinary-prefix and A065 zero-source coupling objections; derive hereditary affine-reference cone and a single original matrix-rank owner; exact full-policy rational audits',
    'mathematical_delta':'Quadratic phases: optional ordinary prefixes and arbitrary adaptive actual product resets paid from SAME original 4I bank including initial KL, full terminal H/K and old relative quarter; residual>=1 for r>0. Gross reserve r/2-1 sharp at bent-star prefixes. No arbitrary supplied reference admission needed in this class. Universal FEI remains OPEN.',
    'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ORIGINAL_OWNER_AND_REFERENCE_CONE_THEOREM; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
    'claim_versions_used':[], 'claims_created_or_changed':[claim_id+'@1'], 'source_artifacts':sources,
    'next_consumers':['A061','A064','A065','A087','A094','B13 lead'], 'next_action':next_action,
    'stagnant_substantive_attempts':0,
    'blockers':['Universal restriction-stable eligible reference cone and nonlocal O(I) owner not established',
                'Independent agent reconstruction/acceptance pending; independent code covers local algebra, not full analytic prefix proof',
                'Brain self-care degraded/unverified: stale personal model, state-of-mind and dream; earlier document-integrity alerts not cleared here',
                'Compute-governor heartbeat observed stale; used only small bounded jobs with frozen <=150MB estimates',
                'Remote supervisor adoption unverified; user forbids git and assigns mirror work to supervisor'],
    'packet_ids':['A063']
}
dump(run/'PROGRESS.json',progress)
dump(run/'PACKET_DELTA.json',progress)

report = f'''# exact target, quantifiers, hypotheses and units

For every uniform-cube quadratic Boolean phase, construct ONE original eligible reference/influence account for every adaptive physical-query history, ordinary prefix, optional actual product reset and stopping cut. All entropy/KL quantities are in bits. Use the source-induced kernel on positive-source rows and its FAIR extension on every zero-source row. The root reference is the actual full product. No new source owner is issued. Full FEI remains OPEN; this is a scoped hereditary-reference mechanism, not another claimed general conjecture.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2, including all required fields; current BOARD snapshot at stage start (12:27 UTC update), B13 STREAM_NOTES.md v2; own STATUS.md and previous 20261023T065336Z payment/obstruction proofs. Consumed A061 run 20261023T113614Z ordinary-prefix guarded-reserve proof, A064 run 20261023T105821Z all-pair fixed-product half-bit theorem, and A065 run 20261023T112150Z global-zero-source tensor-coupling obstruction. Complete copied source text is in out/A061_READ.txt, A064_READ.txt and A065_READ.txt; the board is out/BOARD_SNAPSHOT.txt. These motivate the target and are not proof dependencies of the new theorem. No web source or unverified brain card is used as mathematical evidence.

# complete derivation or exact first unsupported line

PROOF.md derives the actual affine spectral law (including its nontrivial affine shift), H=r, TC=m-r, influence, full normalized query algebra and sharp bent-star lower bound. PROOF_PREFIX.md proves the additional reference cone: mixtures of uniform affine superspaces containing the actual support. A rank drop transports each uniform component into an explicit hyperplane mixture; rank-preserving queries project the mixture. Thus actual reference outcomes remain fair, and each ordinary loss E is between zero and one, with E=0 at rank drops. Newly isolated queries are charged; they are NOT assumed free. Over any interval between resets the actual signed endpoint price is <= the number of rank drops in that interval. The last rank drop cannot receive a positive bill. Hence cumulative GROSS positive reset price <=r/2-1 pathwise, even with adaptive optional resets.

Initial KL m-r is purchased ONCE. One original S=4I bank pays that admission, every gross reset charge, H_root (therefore full terminal H), and an old RELATIVE debit omega<=S/4, retaining >=1 when r>0. The exact source chain retains all reached-node E and terminal K. The r=0 endpoint is explicit. Sharp family q=z0 sum(z_j)+sum y_j z_j has I=k+1, zero initial KL, and prescribed-prefix pending reference cost exactly k before any E/O refund. This sharpness is for the extra reference/outcome reserve; no optimality of complete bank 4I is claimed.

First unsupported universal line: an analogous stable eligible reference cone and original nonlocal O(I) owner exist for arbitrary Boolean functions. Affine support, equal-coset splitting and binary alternating rank have only been proved here for quadratic phases. CONE_BOUNDARY.md explicitly checks that the inherited dense-child reference of the earlier dense/sparse selector family is nonuniform on full actual support, so literal affine-cone invariance already fails. Dense cone repair has nonpositive price, while the sparse reference is already in the cone yet has a positive n-2 product-admission gap. The earlier local J/B/marginal-drift obstruction remains in force; cone membership cannot renew initial admission. No full FEI claim is made.

# executed validation with domain, arithmetic, commands and outputs

Frozen SEARCH_SPEC.json and out/PREFIX_SPEC.json precede their jobs. No automatic dimension growth or symmetry omission: the main local audit explicitly enumerates all 2,198 quadratic truth tables n=0..4, all linear/constant terms, both physical outcomes and every query. It performs {main['transactions_including_sharp']} transactions and {main['assertions']} assertions; PASS, {main['elapsed_seconds']} seconds. It retains {main['positive_reference_only_rows_retained']} positive reference-only row occurrences. Sharp full controller trees k=1..4 (n=4,6,8,10) retain all branches and their full H/K. Pilot: 150 truth tables, 420 transactions, {pilot['elapsed_seconds']} seconds, PASS.

Separate Gauss/kernel implementation uses no Walsh transform: 1,099 phase classes, {audit['queries']} queries, {audit['assertions']} assertions; PASS, {audit['elapsed_seconds']} seconds. It independently checks local normalization and rank costs, and sharp prefixes k=1..3. It is an independent implementation by the same author, not independent agent acceptance.

The optional-prefix audit covers all 76 alternating-matrix roots n=0..4 and ALL coordinate orders, physical outcomes, stopping cuts, and reset/retain choices through memoized recursion; it checks {prefix['query_states']} query states with {prefix['assertions']} direct assertions, {prefix['helper_assertions']} helper assertions; PASS, {prefix['elapsed_seconds']} seconds. Linear/constant reduction is justified by exact spectral-translation covariance of the kernel, reference and zero-source extension. Gross price is checked by EXACT rational exponentiation, so nonintegral KL values need no floating-point logarithms. Prefix pilot: {prefix_pilot['elapsed_seconds']} seconds, PASS. This prefix implementation reuses the truth-table law helper; independent human reconstruction of the all-dimensional prefix proof remains pending.

Commands, from this run directory:
`python -X utf8 -B code/quadratic_audit.py --pilot --out out/pilot.json`
`python -X utf8 -B code/quadratic_audit.py --out out/main.json`
`python -X utf8 -B code/independent_gauss.py`
`python -X utf8 -B code/prefix_audit.py --pilot`
`python -X utf8 -B code/prefix_audit.py`
`python -X utf8 -B code/cone_boundary.py`
`python -X utf8 -B code/finalize.py`

The selector-cone boundary is independently reconstructed from raw Walsh transforms at data dimensions 4,6,8: {boundary['assertions']} exact assertions, PASS in {boundary['elapsed_seconds']} seconds, pilot {boundary['pilot_seconds']} seconds. Its frozen domain, arithmetic, memory and runtime are in the code header written before execution. All probabilities, normalization and tested inequalities are exact integer/Fraction arithmetic. Only reported elapsed times are floating point. Estimated Python memory <=150MB; no >300MB job, GPU or detached work. Compute telemetry was stale, so no large admission was attempted. One malformed patch request was rejected before mutation; corrected patch subsequently saved the intended files. No mathematical failure was hidden.

# proof dependencies and changed downstream conclusions

The proof is self-contained apart from elementary finite Fourier inversion and binary linear algebra, both derived at the needed points. No pending external claim is an axiom. This answers A061's ordinary-prefix challenge WITHIN the quadratic hereditary class, and handles the zero-source rows highlighted by A065. A064's protected-query half-bit theorem is not invoked beyond its scope. The new reserve covers all query orders, purchases initial source KL from the original influence bank, and leaves the old relative quarter booked. It does not upgrade these conclusions outside the affine spectral cone. The stream's broad unreviewed universal candidates are not multiplied; this is a scoped continuation and test of the original-owner mechanism.

# one next mathematical action and independent reviewer

{next_action}

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json are saved here, with code/out, exact results, proof texts and frozen specs. out/BUNDLE_MANIFEST.json pins every listed local artifact by SHA256. The finalizer checks exact protocol field sets, statement digest and all executable/result digests. STATUS.md has two lines; WORKLOG.md is appended with this stage; LEARNED.md records the invariant and its boundary. All writes stay inside A063. No git, brain write, external message or shared-index mutation occurred. Supervisor remote adoption and independent review remain unverified. No computation is left running by completion.

Brain self-care remains degraded/unverified: stale personal model, state-of-mind and dream context, plus earlier attached-document integrity alerts not cleared here. Those sources do not support this mathematical claim.

Universal bridge: C019 stopping-tree payment and C024 history transfer move from a separately admitted reference/local-payment failure to an explicit hereditary reference cone with ONE original 4I bank paying source admission, arbitrary ordinary prefixes and optional actual resets, full terminal H/K and old relative quarter, with positive margin for every nonaffine quadratic phase. The sharp k/(k+1) pending-cost family forces a nonlocal budget rather than a local revelation price. Literal cone invariance already fails at one quadratic selector, where cone repair and product admission have different signs and must be separated. What remains is an original influence-funded owner paying inherited admission gaps and weighted cone repair beyond quadratic spectra. Auditing that debit across a selector with an ordinary data prefix is the shortest next step because it directly extends the existing obstruction while preserving the new history account, rather than merely proving another classwise FEI bound.
'''
save(run/'REPORT.md',report)

status = ('STATE: Quadratic phases: SAME original 4I bank pays initial KL, arbitrary ordinary prefixes/optional resets, full H/K and old relative quarter; residual>=1 for r>0; sharp extra reserve r/2-1; exact audits PASS; review pending; FEI OPEN.\n'
          'NEXT: A087/A094 review rank/cone history proof. Literal cone fails at one cubic selector; pay inherited product-admission gaps and weighted cone repair from SAME unused original influence owner, with O/E/K/full H/old debits. General FEI OPEN.\n')
save(agent/'STATUS.md',status)
marker = '20261023T123929Z'
entry = (f'\n[{datetime.now(timezone.utc).isoformat()}] {marker}: Consumed A061 prefix/A065 coupling objections; proved quadratic affine-superspace reference cone and pathwise gross reset bound r/2-1 for arbitrary adaptive optional resets. Original 4I funds source KL, full H/K and old relative quarter, residual>=1 for r>0. Bent-star prefix is sharp for extra reference reserve. Local exact main 2198 functions/{main["transactions_including_sharp"]} queries PASS; independent Gauss {audit["queries"]} queries PASS; full optional histories 76 roots/{prefix["query_states"]} query states PASS. General Boolean cone/owner and independent agent review OPEN. Saved full local bundle; remote supervisor adoption unverified.\n')
learned = ('\n'+marker+': Quadratic phases have uniform affine spectrum of dimension r (NOT necessarily ell+im A), TC=m-r. Actual full products admit source KL from original 2I. Fair-zero-row coherent references remain mixtures of uniform affine superspaces CONTAINING the actual spectrum, even without resets: rank-drop transport is an explicit average of containing/excluding hyperplanes. Outcomes are fair; ordinary E<=1, rank-drop E=0. Newly isolated queries may release E and must be charged. Between resets, signed cost <= rank drops; final drop cannot cost positively, so all adaptive gross reset charges <=r/2-1. SAME original 4I pays admission, gross resets, root H and old relative quarter with residual>=1 (r>0). Bent-star extension q=z0 sum(zj)+sum yj zj starts bent/product, and querying k controls costs exactly k=I-1 before E/O refunds. This lower bound concerns reference/outcome reserve only, not complete-bank optimality. General nonaffine-spectral support does not inherit the cone; universal FEI remains open.\n')
learned += ('Boundary of this cone: a selector between dense full-rank and sparse rank-two quadratics '
            'has actual predicted dense reference 4/N^2 on four sparse atoms and (N+4)/N^2 elsewhere. '
            'It leaves the containing-superspace cone, but its product repair costs nonpositively. '
            'The sparse predicted reference equals its source and ALREADY lies in the cone, yet its '
            'product admission costs n-2. Cone membership alone does not authorize a renewed rank '
            'owner or source admission; price that inherited gap from the SAME original account.\n')
for name,text in [('WORKLOG.md',entry),('LEARNED.md',learned)]:
    path = agent/name
    old = path.read_text(encoding='utf-8') if path.exists() else ''
    if marker not in old:
        save(path,old+text)

protocol = json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
expected_progress = {('packet_ids' if x.startswith('packet_ids ') else x) for x in protocol['progress_fields']}
assert set(progress) == expected_progress
assert set(claim) == set(protocol['claim_fields'])
assert [line[2:] for line in report.splitlines() if line.startswith('# ')] == protocol['report_fields']
assert (run/'PACKET_DELTA.json').read_bytes() == (run/'PROGRESS.json').read_bytes()
assert len((agent/'STATUS.md').read_text(encoding='utf-8').splitlines()) == 2
assert claim['statement_sha256'] == hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
allpaths = [run/p for p in sources]+[run/p for p in ('REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json')]
manifest = {'saved_at_utc':datetime.now(timezone.utc).isoformat(),'protocol_validation':'PASS',
            'independent_agent_review':'PENDING','remote_mirror':'UNVERIFIED_SUPERVISOR_HANDOFF',
            'artifacts':[{'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in allpaths]}
assert all(p.stat().st_size < 20_000_000 for p in allpaths)
dump(run/'out/BUNDLE_MANIFEST.json',manifest)
print(json.dumps({'status':'PASS','protocol_fields':'EXACT','files_hashed':len(allpaths),'run_id':run_id,
                  'claim':claim_id+'@1','remote':'SUPERVISOR_PENDING','independent_agent_review':'PENDING'}))
