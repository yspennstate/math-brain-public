"""Independent exact-series and growth-tree checks. Standard library only.

The formal-series calculation does not use the tree-growth formula.
The separate tree calculation does not differentiate the power means.
Neither is a Lean elaboration or a proof of the full theorem.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json
import os
import re
import shutil

ROOT = Path(__file__).resolve().parent
PREV = Path('~/codex_op_1114r5/briefs/AV_T137')
ORDER = 6


def add(a, b):
    return [x+y for x, y in zip(a, b)]


def scale(a, c):
    return [x*c for x in a]


def mul(a, b):
    return [sum((a[j]*b[n-j] for j in range(n+1)), Q(0))
            for n in range(ORDER+1)]


def exponential(a):
    assert a[0] == 0
    out = [Q(1)] + [Q(0)]*ORDER
    for n in range(1, ORDER+1):
        out[n] = sum((j*a[j]*out[n-j] for j in range(1, n+1)), Q(0))/n
    return out


def logarithm(a):
    assert a[0] == 1
    u = a.copy()
    u[0] = 0
    power = [Q(1)] + [Q(0)]*ORDER
    out = [Q(0)]*(ORDER+1)
    for k in range(1, ORDER+1):
        power = mul(power, u)
        out = add(out, scale(power, Q((-1)**(k+1), k)))
    return out


def probability(prefix):
    # Conditional nonuniform kernels, including nontrivial prefix dependence.
    return Q(1 + (len(prefix)+sum((i+1)*x for i, x in enumerate(prefix))) % 4, 5)


def leaf_value(prefix):
    return Q((sum((i+2)*(2*x-1) for i, x in enumerate(prefix)) % 17)-8, 8)


def direct_series(depth, exponents, prefix=()):
    if len(prefix) == depth:
        f = leaf_value(prefix)
        return [Q(0)] + [Q((-1)**(n+1), n)*f**n for n in range(1, ORDER+1)]
    j = len(prefix)
    m = exponents[j+1]
    p = probability(prefix)
    a = exponential(scale(direct_series(depth, exponents, prefix+(0,)), m))
    b = exponential(scale(direct_series(depth, exponents, prefix+(1,)), m))
    return scale(logarithm(add(scale(a, 1-p), scale(b, p))), 1/m)


@lru_cache(None)
def single(depth):
    return None if depth == 0 else (single(depth-1),)


@lru_cache(None)
def leaves(tree):
    return 1 if tree is None else sum(leaves(child) for child in tree)


def growth(tree, exponents, depth, j=0):
    if tree is None:
        return
    gamma = exponents[j]-len(tree)*exponents[j+1]
    yield (single(depth-j-1),)+tree, -gamma
    for i, child in enumerate(tree):
        for new_child, weight in growth(child, exponents, depth, j+1):
            yield tree[:i]+(new_child,)+tree[i+1:], weight


@lru_cache(None)
def moment(tree, prefix=()):
    if tree is None:
        return leaf_value(prefix)
    p = probability(prefix)
    out = Q(1)
    for child in tree:
        out *= (1-p)*moment(child, prefix+(0,)) + p*moment(child, prefix+(1,))
    return out


def compare_series(depth, exponents):
    series = direct_series(depth, exponents)
    law = {single(depth): Q(1)}
    for k in range(ORDER):
        assert sum(law.values()) == 1
        assert all(weight >= 0 for weight in law.values())
        assert all(leaves(tree) == k+1 for tree in law)
        coefficient = Q((-1)**k, k+1)*sum(
            (weight*moment(tree) for tree, weight in law.items()), Q(0))
        assert coefficient == series[k+1], (depth, exponents, k, coefficient, series[k+1])
        assert abs(coefficient) <= Q(1, k+1)
        print(f'depth={depth} exponents={exponents[1:]} order={k+1} '
              f'coefficient={coefficient} trees={len(law)} MATCH')
        if k+1 < ORDER:
            new_law = defaultdict(Q)
            for tree, prob in law.items():
                steps = list(growth(tree, exponents, depth))
                assert sum(weight for _, weight in steps) == leaves(tree)
                for grown, weight in steps:
                    new_law[grown] += prob*weight/leaves(tree)
            law = {tree: weight for tree, weight in new_law.items() if weight}


def preserve_record():
    src = ROOT / 'sources'
    manifest_path = ROOT / 'source_manifest.json'
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        for record in manifest:
            assert hashlib.sha256((src/record['file']).read_bytes()).hexdigest() == record['sha256']
    else:
        manifest = [{'file': p.name,
                 'url': 'https://github.com/openai/math/blob/main/lean/OAI/Probability/DilutedSpin/'+p.name,
                 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                for p in sorted(src.glob('*.lean'))]
        manifest_path.write_text(json.dumps(manifest, indent=2)+'\n')
    for path in (PREV / 'sources').iterdir():
        target = src / path.name
        if path.is_file() and not target.exists():
            shutil.copyfile(path, target)
    target = ROOT / 'VERIFY.md'
    if not target.exists():
        target.write_text('> Inherited round-5 verification record. Its historical opens '
                          'belong to earlier sessions; the round-6 continuation is appended below.\n\n'
                          + (PREV / 'VERIFY.md').read_text())
    return len(manifest)


def independent_prior_check():
    # Character-stream removal of comments, independent of prior tokenization.
    def clean(s):
        output, i, nesting = [], 0, 0
        while i < len(s):
            if s[i:i+2] == '/-':
                nesting += 1
                i += 2
            elif nesting and s[i:i+2] == '-/':
                nesting -= 1
                i += 2
            elif nesting:
                i += 1
            elif s[i:i+2] == '--':
                end = s.find('\n', i)
                i = len(s) if end < 0 else end
            else:
                output.append(s[i])
                i += 1
        assert nesting == 0
        return re.sub(r'\s+', ' ', ''.join(output)).strip()
    def block(name):
        s = (PREV/'sources'/name).read_text()
        s = s[s.index('abbrev Spin := Bool'):]
        return clean(s.split('\nend DilutedSpinGlass')[0].split('\ntheorem mezard_parisi')[0])
    assert block('Model.lean') == block('Comparator-DilutedSpin.lean')
    current = (ROOT/'sources'/'RandomInsertion.lean').read_text()
    old = (PREV/'sources'/'RandomInsertion.lean').read_text()
    assert current == old
    print('Earlier definition equality: MATCH; fresh RandomInsertion.lean: unchanged')


def check_preprints():
    manifest = []
    specs = [
        ('diluted-r6.tex', 'diluted-model-current.tex',
         'The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/model.tex'),
        ('invariant-r6.tex', 'invariant-current.tex',
         'All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/build/invariant-sk.tex'),
        ('tensor-r6.tex', 'tensor-current.tex',
         'Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/build/sections/01-introduction.tex'),
    ]
    for fresh, old, path in specs:
        a, b = [(ROOT/'sources'/name).read_text() for name in (fresh, old)]
        theorem = r'\\begin\{theorem\}[\s\S]*?\\end\{theorem\}'
        assert re.search(theorem, a).group() == re.search(theorem, b).group()
        print('Fresh exact main theorem: MATCH', fresh)
        manifest.append({'file': fresh,
                         'url': 'https://github.com/openai/math/blob/main/preprints/'+path,
                         'sha256': hashlib.sha256((ROOT/'sources'/fresh).read_bytes()).hexdigest()})
    (ROOT/'preprint_manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')


def check_pattern_bound():
    checks = 0
    for b in (1, 2, 3):
        patterns = list(product((-1, 1), repeat=b))
        laws = []
        for z in range(3):
            weights = [Q(1+(i*i+z*i+2*z) % 7) for i in range(len(patterns))]
            laws.append([w/sum(weights) for w in weights])
        root = (Q(1, 5), Q(3, 10), Q(1, 2))
        mean = [sum((root[z]*laws[z][i] for z in range(3)), Q(0))
                for i in range(len(patterns))]
        deviation = Q(0)
        for mask in range(1, 2**b):
            chars = []
            for pattern in patterns:
                c = 1
                for j in range(b):
                    if mask & (1 << j):
                        c *= pattern[j]
                chars.append(c)
            moments = [sum((p*c for p, c in zip(law, chars)), Q(0)) for law in laws]
            average = sum((w*m for w, m in zip(root, moments)), Q(0))
            deviation += sum((w*abs(m-average) for w, m in zip(root, moments)), Q(0))
        for a in (0, 1, 2, 3):
            distance = Q(0)
            for indices in product(range(len(patterns)), repeat=a):
                mixed = Q(0)
                for z in range(3):
                    p = root[z]
                    for i in indices:
                        p *= laws[z][i]
                    mixed += p
                independent = Q(1)
                for i in indices:
                    independent *= mean[i]
                distance += abs(mixed-independent)
            assert distance <= a*deviation
            if a <= 1:
                assert distance == 0
            checks += 1
    print(f'Exact mixed-pattern absolute-mass checks: {checks} passed (b=1..3, a=0..3).')


def main():
    print('OMP_NUM_THREADS:', os.environ.get('OMP_NUM_THREADS'))
    print('Process nice:', os.getpriority(os.PRIO_PROCESS, 0))
    independent_prior_check()
    count = preserve_record()
    print('Fresh opened Lean files hashed:', count)
    check_preprints()
    for depth in (1, 2, 3):
        compare_series(depth, tuple(Q(j, depth) for j in range(depth+1)))
    # Equal exponents remove an intermediate level; small exponent catches divisions.
    compare_series(2, (Q(0), Q(1), Q(1)))
    compare_series(2, (Q(0), Q(1, 97), Q(1)))
    print('All 30 exact coefficient comparisons passed through order 6.')
    check_pattern_bound()
    print('Finite checks support PROOF.md; no Lean build or full-formula certification.')


if __name__ == '__main__':
    main()
