"""Build reviewable, unpromoted C0029 concepts. Does not access or write a store."""
import difflib
import json
from pathlib import Path

folder = Path(__file__).resolve().parent
source = {'source_id': 'owner-probability300-w574-20261010:gaussian-radius-bridge',
          'url': (folder / 'ATTEMPT.md').as_uri(),
          'revision': 'author-derived-2026-10-10-referee-pending',
          'license': 'owner-own-work', 'excerpt': None}

def entry(key, name, kind, title, statement, assumptions):
    return {'key': key, 'namespace': 'probability.random-matrices',
            'logical_name': name, 'kind': kind, 'title': title,
            'statement': statement, 'proof_text': None, 'assumptions': assumptions,
            'domain': 'real Gaussian small-ball probabilities and random-matrix proof auditing',
            'source': dict(source)}

entries = [
    entry('gaussian-radius', 'independent-gaussian-random-radius-small-ball-function', 'definition',
          'Independent Gaussian random-radius small-ball function',
          'For a standard real Gaussian Z and a nonnegative random variable R finite almost surely and independent of Z, define h(t)=P(|Z|<=tR) for t>0. This construction includes deterministic R. Independence is part of the definition used in the rescaling bridge.',
          ['Z is standard real Gaussian', 'R>=0 is finite almost surely', 'Z and R are independent']),
    entry('signed-rescaling', 'gaussian-random-radius-rescaling-positive-remainder-draft', 'concept',
          'Gaussian small-ball probability: independent random radius rescaling, third moment and spectral cutoff',
          'DRAFT, author-derived proof awaiting independent referee: Let Z be standard real Gaussian, independent of R>=0 finite almost surely, and h(t)=P(|Z|<=tR). For 0<t<=t0, h(t)>=(t/t0)h(t0), strictly when t<t0 and P(R>0)>0. If E[R^3]<infinity, then 0<=h(t)-(t/t0)h(t0)<=sqrt(2/pi)*t*(t0^2-t^2)*E[R^3]/6. A spectral cutoff can bound this moment; conditional finiteness alone cannot. This bridge retains a positive error and does not prove the exact-coefficient Spielman-Teng conjecture.',
          ['Z is standard real Gaussian', 'R>=0 is finite almost surely and independent of Z',
           '0<t<=t0', 'The quantitative upper remainder requires E[R^3]<infinity']),
    entry('refuted-upper-route', 'gaussian-concavity-does-not-give-zero-error-upper-rescaling', 'concept',
          'Refuted route: Gaussian concavity gives no zero-error upper rescaling to smaller thresholds',
          'DRAFT refuted inference, awaiting independent referee: For independent standard real Gaussian Z and R>=0 finite almost surely, let h(t)=P(|Z|<=tR). The universal claim h(t)<=(t/t0)h(t0) for 0<t<t0 is false. With R=1, h(t)/t=sqrt(2/pi)*integral_0^1 exp(-t^2 u^2/2) du strictly decreases in t. Thus the proposed upper inequality is strictly reversed. A published approximate rescaling lemma with a positive remainder is not refuted by this counterexample.',
          ['Z is standard real Gaussian', 'R=1', '0<t<t0']),
    entry('moment-obstruction', 'gaussian-row-radius-conditional-third-moment-not-integrable', 'concept',
          'Gaussian spectral-radius moment obstruction: conditional third moments need not be integrable',
          'DRAFT counterexample, awaiting independent referee: Let A,B,W be independent standard real Gaussians, S=sqrt(A^2+B^2), and R=|W|/(sqrt(2)*S), defined arbitrarily when S=0. Then E[R^3|A,B] is finite almost surely, but E[R^3]=infinity. S has density s exp(-s^2/2) on s>0, so E[S^(-3)] diverges at zero. This is the untruncated n=2 one-row Gaussian spectral radius, and refutes averaging conditional finiteness into an unconditional cubic rescaling bound. It is not a Bernoulli matrix counterexample.',
          ['A,B,W are independent standard real Gaussians', 'Conditional finiteness is asserted almost surely'])
]
relations = [
    {'from_key': 'signed-rescaling', 'to_key': 'gaussian-radius', 'kind': 'depends_on',
     'rationale': 'The rescaling statement uses precisely the independent Gaussian-radius function and its conditioning hypotheses.'},
    {'from_key': 'signed-rescaling', 'to_key': 'refuted-upper-route', 'kind': 'refutes',
     'rationale': 'With R=1 and 0<t<t0 the derived inequality is strict in the opposite direction to the proposed zero-error upper inequality.'},
    {'from_key': 'moment-obstruction', 'to_key': 'signed-rescaling', 'kind': 'semantic_association',
     'rationale': 'The example fails the finite unconditional third-moment premise of the quantitative part; it does not refute the theorem with that premise retained.'},
    {'from_key': 'signed-rescaling',
     'to_existing_logical': 'math:probability.random-matrices:open-problem-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr',
     'kind': 'semantic_association',
     'rationale': 'C0029 needs a coefficient-one uniform tail; the Gaussian replacement/rescaling route retains a positive error and independence/moment hypotheses. This association is a proof-gap warning, not a proves edge.'}
]
bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w574',
          'bundle_slug': 'c0029-gaussian-radius-rescaling-obstructions-w574-20261010',
          'entries': entries, 'relations': relations}
text = json.dumps(bundle, ensure_ascii=False, indent=2) + '\n'
(folder / 'bundle_001.json').write_text(text, encoding='utf-8')
(folder / 'patches').mkdir(exist_ok=True)
target = '~/math-brain-inbox/w574/bundle_001.json'
patch = ''.join(difflib.unified_diff([], text.splitlines(keepends=True),
                                  fromfile='a/'+target, tofile='b/'+target))
(folder / 'patches/01_c0029_gaussian_radius_bundle.diff').write_text(patch, encoding='utf-8')
print(json.dumps({'entries': len(entries), 'relations': len(relations),
                  'local_draft': str(folder / 'bundle_001.json'),
                  'inbox_target': target, 'published': False}))
