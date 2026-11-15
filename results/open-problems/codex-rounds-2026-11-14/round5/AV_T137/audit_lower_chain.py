"""Small reproducible source checks; does not parse or execute Lean."""
from pathlib import Path
import hashlib
import json
import os
import re

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'sources'


def tokens_without_comments(text):
    # None of the compared definition blocks contains string literals.
    chunks = re.split(r'(/-|-/|--[^\n]*)', text)
    depth, kept = 0, []
    for chunk in chunks:
        if chunk == '/-':
            depth += 1
        elif chunk == '-/' and depth:
            depth -= 1
        elif not depth and not chunk.startswith('--'):
            kept.append(chunk)
    assert depth == 0
    return re.findall(r'\S+', ''.join(kept))


def definitions(path):
    text = path.read_text()
    text = text[text.index('abbrev Spin := Bool'):]
    text = text.split('\nend DilutedSpinGlass', 1)[0]
    text = text.split('\ntheorem mezard_parisi', 1)[0]
    return tokens_without_comments(text)


def theorem_header(path):
    text = path.read_text()
    text = text[text.index('theorem mezard_parisi'):].split(':= by', 1)[0]
    return tokens_without_comments(text)


def first_theorem(path):
    text = path.read_text()
    return re.search(r'\\begin\{theorem\}[\s\S]*?\\end\{theorem\}', text).group()


def main():
    print('Process nice:', os.getpriority(os.PRIO_PROCESS, 0))
    a = definitions(SRC / 'Model.lean')
    b = definitions(SRC / 'Comparator-DilutedSpin.lean')
    assert a == b
    assert theorem_header(SRC / 'Main.lean') == theorem_header(SRC / 'Comparator-DilutedSpin.lean')
    print('Earlier result holds: definition tokens match:', len(a))
    print('Earlier result holds: theorem headers match')

    pairs = [('diluted-model-current.tex', 'diluted-model.tex'),
             ('invariant-current.tex', 'invariant-introduction.tex'),
             ('tensor-current.tex', 'tensor-introduction.tex')]
    for fresh, old in pairs:
        assert first_theorem(SRC / fresh) == first_theorem(SRC / old)
        print('Exact main theorem unchanged:', fresh)

    locations = [
        ('ExactVariationalLower.lean', 'admissible_trial_lower'),
        ('SymmetricTrialLower.lean', 'symmetric_trial_lower'),
        ('BoundedCavityLower.lean', 'bounded_symmetric_trial_lower'),
        ('FullRegularSelection.lean', 'full_regular_covariance_selection'),
        ('CavityProxy.lean', 'cavityProxy_comparison_tendsto'),
        ('IncrementCavityProxy.lean', 'increment_cavityProxy_bound'),
        ('UpperInsertion.lean', 'poissonInsertionOn_comparison_tendsto_ae'),
        ('AveragedEnergyRoot.lean', 'randomInsertionOn_comparison_tendsto'),
        ('RandomInsertion.lean', 'randomInsertion_comparison_tendsto'),
    ]
    for file, name in locations:
        lines = (SRC / file).read_text().splitlines()
        found = [i for i, line in enumerate(lines, 1)
                 if re.match(r'(?:lemma|theorem)\s+' + re.escape(name) + r'\b', line)]
        assert len(found) == 1, (file, name, found)
        print(f'Declaration: {file}:{found[0]} {name}')

    manifest = json.loads((SRC / 'fresh-opens.json').read_text())
    for record in manifest:
        record['sha256'] = hashlib.sha256((SRC / record['file']).read_bytes()).hexdigest()
    (ROOT / 'source_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Fresh opened files hashed:', len(manifest))
    print('These are text checks, not a Lean build or proof-correctness test.')


if __name__ == '__main__':
    main()
