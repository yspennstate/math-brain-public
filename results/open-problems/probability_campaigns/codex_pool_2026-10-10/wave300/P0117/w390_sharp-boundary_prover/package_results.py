"""Build local DRAFT files. Submission is explicit and checks the w390 inbox path."""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w390')
TARGET = 'math:probability.core:open-problem-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--submit', action='store_true')
    args = parser.parse_args()
    proof = (ROOT / 'PROOF.md').read_text(encoding='utf-8')
    constants = ('Choose 0<=l<h<infinity with p_l=P(t_e<=l)>0 and p_h=P(t_e>=h)>0; '
                 'K=1+4l/(h-l), C=2K log(1/p_h)+(K+4)log(1/p_l). Logs are natural. ')
    source = {'source_id': 'owner-probability-campaign:w390:P0117:2026-10-10',
              'url': 'urn:owner-own-work:w390:P0117:thin-tube:2026-10-10',
              'revision': 'author-proof-v1-pending-independent-review-w392',
              'license': 'owner-own-work; DRAFT, author-proved special case, not independently reviewed',
              'excerpt': None}
    common = ['Undirected nearest-neighbor Z^2', 'iid finite nonnegative nonconstant edge weights',
              'Geodesics minimize in the full ambient lattice', 'Injective rays and bigeodesics',
              'Independent mathematical review pending; no novelty claim']
    def entry(key, name, kind, title, statement, proof_text, assumptions):
        return {'key': key, 'namespace': 'probability.fpp', 'logical_name': name,
                'kind': kind, 'title': title, 'statement': statement, 'proof_text': proof_text,
                'assumptions': assumptions, 'domain': 'probability theory', 'source': source.copy()}
    def section(start, end):
        return proof.split(start, 1)[1].split(end, 1)[0].strip()
    prefix = 'DRAFT: author-proved special case; independent review pending. '
    entries = [
        entry('slab', 'ambient-fpp-cheap-bypass-excludes-confined-slab-crossing', 'lemma',
              'Cheap bypass excludes an FPP crossing confined to a strip',
              prefix + 'Fix integer columns A and A+m and a strip |y-y0|<=w. For 0<=l<h, suppose all m(2w+1) '
              'horizontal edges inside this strip between the columns cost at least h, while the m edges in '
              'row y0+w+1 and the vertical connectors at the two columns from y0-w to y0+w+1 cost at most l. '
              'If m(h-l)>(4w+2)l, no ambient-lattice finite geodesic joining the two columns stays in the strip.',
              section('## Lemma 1:', '## Lemma 2:'), common + ['w>=0 integer', 'm>=1 integer', 'Nonnegative edge costs']),
        entry('trap', 'iid-fpp-slab-trap-probability-and-disjoint-supports', 'lemma',
              'Probability and independent supports of the FPP strip trap',
              prefix + constants + 'For integer w>=0, let m=floor((4w+2)l/(h-l))+1. The event with m(2w+1) '
              'high horizontal edges in the strip and m+4w+2 low bypass and connector edges has probability '
              'q_w=p_h^(m(2w+1))*p_l^(m+4w+2)>=exp(-C(w+1)^2). Copies spaced by m+1 columns have disjoint '
              'required edge supports and hence independent events.',
              section('## Lemma 2:', '## Theorem 3:'), common + [constants]),
        entry('tube', 'nonconstant-iid-fpp-no-eventual-logarithmically-thin-tube-ray', 'theorem',
              'Geodesic rays cannot eventually stay in sufficiently thin logarithmic tubes',
              prefix + constants + 'For every fixed deterministic nondecreasing integer width w(n)>=0 '
              'with limsup w(n)/sqrt(log n)<1/sqrt(C), and each fixed integer y0, almost surely no injective '
              'ambient-lattice geodesic ray has a tail in {(x,y): |y-y0|<=w(|x|)}. This requires neither '
              'continuity nor moments. It does not exclude unrestricted bigeodesics.',
              section('## Theorem 3:', '## Corollary 4:'), common + [constants, 'Deterministic width and center']),
        entry('transversal', 'iid-fpp-simultaneous-logarithmic-transversal-ray-lower-bound', 'theorem',
              'A simultaneous logarithmic transversal lower bound for FPP geodesic rays',
              prefix + constants + 'Almost surely every injective ambient-lattice geodesic ray (x_j,y_j), '
              'simultaneously for every integer center y0, satisfies limsup_j |y_j-y0|/sqrt(log(2+|x_j|)) '
              '>=1/sqrt(C). Therefore no bigeodesic has a tail eventually in a fixed finite-width horizontal '
              'or vertical strip. The coefficient and scale are not claimed optimal.',
              section('## Corollary 4:', '## Boundary and scope'), common + [constants]),
        entry('constant', 'constant-iid-fpp-horizontal-bigeodesic-hypothesis-boundary', 'lemma',
              'Constant-law boundary of the FPP strip exclusion',
              prefix + 'If every nearest-neighbor edge of Z^2 has a fixed weight a>=0, the path ((j,0)) '
              'indexed by all integers is a bigeodesic in the full lattice. Thus nonconstancy is necessary '
              'for fixed-strip exclusion. This law is atomic and is not a counterexample to the nonatomic '
              'P0117 target.',
              'A finite horizontal segment has L1-minimal length. With constant a>0 its cost is a times '
              'that length, so it minimizes among all paths. With a=0 all finite path costs tie at zero.',
              ['Undirected nearest-neighbor Z^2', 'Constant iid edge law at a>=0', 'Independent review pending']),
        entry('scope', 'p0117-thin-tube-proof-unrestricted-wandering-gap', 'concept',
              'The remaining unrestricted-wandering gap in the P0117 tube route',
              'DRAFT concept: the standard P0117 target excludes every bigeodesic for nonatomic iid finite '
              'nonnegative weights on Z^2, commonly with E[min(X1,X2,X3,X4)^2]<infinity. Explicit independent '
              'slab traps exclude confined rays in tubes of width below a sufficient multiple of sqrt(log n). '
              'An unrestricted candidate may wander outside every such tube. No bridge forcing confinement '
              'is proved, so the tube result cannot be promoted to the full target. Current openness and '
              'novelty are UNKNOWN; a September 2026 primary manuscript already claims the standard full result.',
              None, ['Author analysis only', 'No assertion that the target remains open', 'No full-target proof claim'])
    ]
    relations = [
        {'from_key': 'trap', 'to_key': 'slab', 'kind': 'depends_on', 'rationale': 'The trap statement counts the strip, bypass and connector edges explicitly defined in the slab lemma.'},
        {'from_key': 'tube', 'to_key': 'slab', 'kind': 'depends_on', 'rationale': 'A ray confined to the tube must cross a trapped slab; the slab lemma excludes that ambient geodesic crossing.'},
        {'from_key': 'tube', 'to_key': 'trap', 'kind': 'depends_on', 'rationale': 'The dyadic argument uses q_w>=exp(-C(w+1)^2) and disjoint slab supports to obtain summable no-trap probabilities.'},
        {'from_key': 'transversal', 'to_key': 'tube', 'kind': 'depends_on', 'rationale': 'A transversal limsup below 1/sqrt(C) forces eventual confinement in one rational-coefficient tube excluded by the tube theorem.'},
        {'from_key': 'constant', 'to_key': 'tube', 'kind': 'semantic_association', 'rationale': 'The constant-law horizontal bigeodesic shows why the tube theorem must assume a nonconstant weight law; it does not refute the theorem as stated.'},
        {'from_key': 'scope', 'to_key': 'tube', 'kind': 'cites', 'rationale': 'The scope concept identifies the limitation of the tube theorem: only eventually confined rays are excluded.'},
        {'from_key': 'scope', 'to_existing_logical': TARGET, 'kind': 'semantic_association', 'rationale': 'The existing P0117 card asks about bi-infinite geodesics for nondegenerate continuous iid planar laws. The scope concept records why thin-tube exclusion alone does not answer it.'}
    ]
    bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w390',
              'bundle_slug': 'p0117-quantitative-thin-tube-boundary-w390-001',
              'entries': entries, 'relations': relations}
    folder = ROOT / 'bundles'
    folder.mkdir(exist_ok=True)
    body = json.dumps(bundle, ensure_ascii=False, indent=2) + '\n'
    local = folder / 'bundle_001.json'
    local.write_text(body, encoding='utf-8')
    metrics = {'prepared_entries': len(entries), 'prepared_relations': len(relations),
               'proved_special_case_entries_pending_review': sum(e['kind'] != 'concept' for e in entries),
               'unproved_or_scope_concepts': sum(e['kind'] == 'concept' for e in entries),
               'live_store_changes_by_w390': 0,
               'source_target_nodes_found_before': len(json.loads((ROOT/'reports/store_target_baseline.json').read_text(encoding='utf-8')))}
    (ROOT / 'reports' / 'bundle_metrics.json').write_text(json.dumps(metrics, indent=2), encoding='utf-8')
    submission = {'prepared': True, 'submitted': False, 'reviewed': False, 'ingested': False,
                  'retrievable': False, 'local_bundle': local.as_posix(), 'reviewer': 'w392',
                  'at_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
    # A new-file unified diff names the exact proposed shared path. No live code is patched.
    patches = ROOT / 'patches'
    patches.mkdir(exist_ok=True)
    target_header = '~/math-brain-inbox/w390/bundle_001.json'
    diff = ''.join(difflib.unified_diff([], body.splitlines(keepends=True),
                    fromfile='a/' + target_header, tofile='b/' + target_header))
    (patches / '01_p0117_thin_tube_bundle.diff').write_text(diff, encoding='utf-8')
    if args.submit:
        destination = INBOX / 'bundle_001.json'
        resolved_root = INBOX.resolve()
        if destination.resolve().parent != resolved_root:
            raise RuntimeError('Inbox destination escaped the explicitly authorized w390 directory.')
        INBOX.mkdir(exist_ok=True)
        if destination.exists():
            if destination.read_text(encoding='utf-8') != body:
                raise RuntimeError('Existing shared bundle differs; no overwrite authorized.')
        else:
            partial = destination.with_suffix('.part')
            if partial.exists():
                raise RuntimeError('Existing partial bundle preserved; choose a new output name.')
            if partial.resolve().parent != resolved_root:
                raise RuntimeError('Partial destination escaped the w390 inbox.')
            partial.write_text(body, encoding='utf-8')
            partial.rename(destination)
        submission.update(submitted=True, submitted_path=destination.as_posix(),
                          submitted_at_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    (ROOT / 'SUBMISSION_STATUS.json').write_text(json.dumps(submission, indent=2), encoding='utf-8')
    print(json.dumps({'metrics': metrics, 'submission': submission}, indent=2))


if __name__ == '__main__':
    main()
