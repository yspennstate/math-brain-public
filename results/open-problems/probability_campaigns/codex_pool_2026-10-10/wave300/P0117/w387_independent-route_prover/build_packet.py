"""Build local claim/review drafts; never integrates or writes a live store."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
attempt = (ROOT / 'ATTEMPT.md').read_text(encoding='utf-8')


def section(start, stop):
    return attempt.split(start, 1)[1].split(stop, 1)[0].strip()


def source(label):
    return {
        'source_id': 'owner-own-work:w387:P0117:' + label,
        'url': 'urn:owner-own-work:probability:P0117:w387:' + label,
        'revision': 'draft-2026-10-10',
        'license': 'owner-own-work (campaign lemma; independent review pending)',
        'excerpt': None,
    }


common = {
    'status': 'proved special case',
    'independent_reviewer': 'w389 (pending)',
    'novelty_claim': False,
    'formal_check': 'None. Exact finite controls are not a formal theorem receipt.',
}

bound_statement = (
    'For iid finite nonnegative nondegenerate edge weights on nearest-neighbor Z^2, choose '
    'finite 0<=a<b with q=P(t<=a)>0 and p=P(t>=b)>0. Let integer L>=2 satisfy '
    'L(b-a)>2a, R=2(L+1), D=1+2R(R+1), eta=p^L q^(L+2). Every deterministic '
    'simple N-edge path gamma has P(gamma is a full-lattice geodesic) <= '
    '(1-eta)^ceil(floor(N/L)/D).'
)
dictionary_statement = (
    'For iid finite nonnegative nondegenerate weights on nearest-neighbor Z^2, choose finite '
    '0<=a<b with q=P(t<=a)>0 and p=P(t>=b)>0, integer L>=2 with L(b-a)>2a, '
    'R=2(L+1), D=1+2R(R+1), and eta=p^L q^(L+2). For any deterministic finite '
    'dictionary P_N of simple N-edge paths, P(some member is a geodesic) <= '
    '|P_N|(1-eta)^ceil(floor(N/L)/D). Thus if these products tend to zero, almost surely '
    'there is no geodesic ray starting at a specified vertex whose N-edge prefix belongs '
    'to P_N for every N. In particular subexponential dictionary cardinality suffices. '
    'The result excludes bigeodesics only when one of their tails is covered by such dictionaries.'
)
square_statement = (
    'For iid Uniform[1,2] weights on nearest-neighbor Z^2, the full-lattice geodesic between '
    '(0,0) and (1,1) is almost surely the cheaper of the two two-edge square routes A,B. '
    'For fixed A, the event both A edges >=7/4 and both B edges <=5/4 has probability '
    '1/256. For the minimizing route R, the event both R edges >=7/4 and both other '
    'square-route edges <=5/4 is impossible, also conditional on R=A or R=B. '
    'A fixed-route iid shortcut probability therefore need not survive weight-dependent route selection.'
)

records = [
    dict(common, id='w387-P0117-C02', type='finite-cylinder reduction',
         statement='For finite nonnegative deterministic weights on Z^2, let A_n(v) denote existence of a centered simple 2n-edge path through v that is shortest in the induced l1-ball B_n(v). Then A_(n+1)(v) is contained in A_n(v), each is a finite-cylinder event, and their intersection is exactly existence of a full-lattice bigeodesic through v. For random weights P(bigeodesic through v)=lim_n P(A_n(v)).',
         assumptions=['nearest-neighbor Z^2', 'finite nonnegative weights', 'simple centered paths'],
         source=dict(source('L1'), proof_file=str(ROOT / 'ATTEMPT.md'), proof_section='L1'),
         proof=section('## L1:', '## L2:'), remaining_gap='No gap in this reduction is claimed internally; obtaining limit zero is G1. Related compactness lemma already held by w388; supporting only, omitted from landing bundle.'),
    dict(common, id='w387-P0117-C03', type='prescribed infinite path exclusion',
         statement='For iid finite nonnegative nondegenerate weights on Z^2, every prescribed infinite simple path has probability zero of being a geodesic. Every countable prescribed family, or path sampled independently of the weights, is excluded.',
         assumptions=['iid finite nonnegative nondegenerate weights', 'path geometry prescribed independently of the edge weights'],
         source=dict(source('L2'), proof_file=str(ROOT / 'ATTEMPT.md'), proof_section='L2'),
         proof=section('## L2:', '## L3:'), remaining_gap='Does not exclude weight-dependent paths; G1 remains.'),
    dict(common, id='w387-P0117-C04', type='selection counterexample',
         statement=square_statement, assumptions=['iid Uniform[1,2] weights', 'actual full-lattice diagonal-endpoint geodesic selected from these same weights'],
         source=dict(source('L3'), proof_file=str(ROOT / 'ATTEMPT.md'), proof_section='L3'),
         proof=section('## L3:', '## L4:'), remaining_gap='None for this counterexample; it refutes only the specified probability transfer, not the target theorem.'),
    dict(common, id='w387-P0117-C05', type='uniform finite-path bound and dictionary exclusion',
         statement=bound_statement + ' ' + dictionary_statement,
         assumptions=['iid finite nonnegative nondegenerate weights on nearest-neighbor Z^2', 'deterministic simple candidate paths; trials chosen before weights are seen', 'p,q>0; L>=2; L(b-a)>2a'],
         source=dict(source('L4'), proof_file=str(ROOT / 'ATTEMPT.md'), proof_section='L4'),
         proof=section('## L4:', '## Single hardest'),
         remaining_gap='For the unrestricted target, no candidate dictionary below the shortcut entropy rate or valid conditional resampling substitute has been derived.'),
    {'id': 'w387-P0117-G1', 'status': 'conjecture', 'type': 'single hardest remaining proof obligation',
     'statement': 'Derive exclusion uniform over every weight-selected bigeodesic candidate through a fixed vertex: prove lim_n P(A_n(0))=0, e.g. with a deterministic candidate cover whose entropy lies below the C05 rate, or a conditional resampling law which remains valid after selection.',
     'assumptions': ['nonatomic iid finite nonnegative planar weights; moment-restricted version additionally E[min(t1,t2,t3,t4)^2]<infinity'],
     'source': dict(source('G1'), proof_file=str(ROOT / 'ATTEMPT.md')),
     'proof': None, 'counterexample_to_naive_step': 'C04', 'independent_reviewer': 'w389 (pending)',
     'remaining_gap': 'The obligation itself is unproved; no full target theorem established.', 'novelty_claim': False},
]

claims_path = ROOT / 'CLAIMS.jsonl'
existing = [json.loads(line) for line in claims_path.read_text(encoding='utf-8').splitlines() if line.strip()]
ids = {row['id'] for row in existing}
with claims_path.open('a', encoding='utf-8', newline='\n') as handle:
    for row in records:
        if row['id'] not in ids:
            handle.write(json.dumps(row, ensure_ascii=False) + '\n')
            handle.flush()


def entry(key, logical_name, title, statement, label):
    return {
        'key': key, 'namespace': 'probability.fpp', 'logical_name': logical_name,
        'kind': 'concept', 'title': title + ' (draft)',
        'statement': 'DRAFT; independent mathematical review pending. ' + statement,
        'proof_text': None,
        'assumptions': ['Not a proof of the unrestricted no-bigeodesics conjecture; see the exact hypotheses in the statement.'],
        'domain': 'probability theory; first-passage percolation', 'source': source(label),
    }

bundle = {
    'spec': 'mathbrain-draft-v1', 'author_agent': 'w387', 'bundle_slug': 'p0117-prescribed-path-shortcuts-w387-001',
    'entries': [
        entry('fixed-path-bound', 'prescribed-fpp-path-exponential-shortcut-bound', 'Prescribed FPP path exponential shortcut bound', bound_statement, 'L4'),
        entry('dictionary-bound', 'fpp-geodesic-exclusion-from-small-deterministic-dictionaries', 'FPP geodesic exclusion from small deterministic dictionaries', dictionary_statement, 'L4-dictionary'),
        entry('selected-square', 'fpp-square-selection-annihilates-iid-shortcut-pattern', 'FPP square selection annihilates an iid shortcut pattern', square_statement, 'L3'),
        entry('invalid-transfer', 'invalid-iid-shortcut-probability-transfer-after-path-selection', 'Invalid iid shortcut transfer after path selection',
              'REFUTED INFERENCE: a shortcut event with positive iid probability for each prescribed path retains that probability after selecting a minimizing path from the same edge weights. The Uniform[1,2] square example gives a fixed-route pattern probability 1/256 and selected-route probability zero. A derived conditional law, independent selection, or valid deterministic dictionary bound is required.', 'L3-obstruction'),
    ],
    'relations': [
        {'from_key': 'dictionary-bound', 'to_key': 'fixed-path-bound', 'kind': 'depends_on', 'rationale': 'The dictionary statement applies the exact C05 bound to each prescribed member and uses a union bound; no cross-path independence is assumed.'},
        {'from_key': 'selected-square', 'to_key': 'invalid-transfer', 'kind': 'refutes', 'rationale': 'The endpoints are exact: the inference demands retaining a positive shortcut-pattern probability; the actual selected-square pattern probability is zero.'},
    ],
}
(ROOT / 'DRAFT_BUNDLE.json').write_text(json.dumps(bundle, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

hook = {
    'id': 'selected-path-w387-01', 'area': 'math', 'event': 'PostToolUse',
    'cue': 'A shortcut/resampling proof treats edges along a path selected from the same weights as retaining their original independent law without a derived conditional law.',
    'fire_when': 'After choosing the cheaper square route from iid weights, multiply its original fixed-route high/low shortcut probability.',
    'silent_when': 'Candidate geometry is fixed independently of weights and trial supports are disjoint, or a posterior coupling/filtration explicitly derives the selected-path conditional law.',
    'text': 'A path chosen from the same weights can erase a fixed-path shortcut probability. Name the selection sigma-field and derive the conditional law, or use a valid deterministic candidate cover. Disjoint supports before selection alone do not preserve iid weights afterward.',
    'evidence': 'proof_steps_need_derived_joint_structure_2026_09_09; ~/brain_workers/w387/ATTEMPT.md L3 (Uniform[1,2], fixed 1/256 versus selected 0)',
    'proposer': 'w387',
}
assert len(hook['text']) <= 300
(ROOT / 'HOOK_PROPOSAL.jsonl').write_text(json.dumps(hook, ensure_ascii=False) + '\n', encoding='utf-8')
patches = ROOT / 'patches'
patches.mkdir(exist_ok=True)
hook_line = json.dumps(hook, ensure_ascii=False)
patch = '--- a/~/primary_directive/hooks1000/proposals/math-w387.jsonl\n+++ b/~/primary_directive/hooks1000/proposals/math-w387.jsonl\n@@ -0,0 +1 @@\n+' + hook_line + '\n'
(patches / '01_selected_path_hook.diff').write_text(patch, encoding='utf-8')
print(json.dumps({'claim_rows': len(existing) + sum(r['id'] not in ids for r in records), 'draft_entries': len(bundle['entries']), 'hook_characters': len(hook['text'])}))
