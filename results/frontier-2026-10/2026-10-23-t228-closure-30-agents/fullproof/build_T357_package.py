"""Assemble the accepted proof without modifying its reviewed components."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parent
WORK = ROOT.parent
SYNTHESIS_SHA = '7b773eba4446340893bd8e67a1397ba06b154bf79b9f89a348e68c1a93282d51'
MODULES = [
    ('A', 'Random-feature dynamics and matrix hypotheses', 'b03_gaussian_dynamics.md'),
    ('B', 'Explicit finite-time state evolution', 'b01_GD_state_evolution_check.md'),
    ('C', 'Total variation and exact calibration', 'b04_calibration_transfer.md'),
    ('D', 'Uniform-time GD and stopping rules', 'b02_uniform_time_GD.md'),
    ('E', 'Signed overconfidence and the common regime', 'b06_gaussian_overconfidence.md'),
]
REVIEWS = [
    'b01_final_T357_review.md', 'b02_final_T357_review.md',
    'b02_gaussian_calibration_audit.md', 'b04_state_evolution_audit.md',
    'b05_RF_universality_audit.md', 'b05_uniform_time_audit.md',
    'b06_scope_and_mathematics.md',
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record(name):
    p = ROOT / name
    return {'path': name, 'sha256': sha(p), 'bytes': p.stat().st_size}


def main():
    synthesis = ROOT / 'T357_THEOREM_AND_SYNTHESIS.md'
    assert sha(synthesis) == SYNTHESIS_SHA
    refs = ROOT / 'references'
    refs.mkdir(exist_ok=True)
    for name in ['source_registry_rows.json', 'ORIGINAL_PROBLEM_SCOPE_AUDIT.md',
                 'T357_gaussian_first_step_attempt.md',
                 'T357_gaussian_first_step_independent_review.md']:
        shutil.copyfile(WORK / 'followup' / name, refs / name)
    combined = synthesis.read_text()
    combined += '\n\n---\n\n# Complete detailed proof modules\n\n'
    combined += ('The following modules are reproduced in full. Each module states its own local '
                 'dependencies; the synthesis above proves their composition and closes the '
                 'cross-module inputs. Equation numbers restart within each module. Published '
                 'spectral and AMP theorems are explicitly identified and their application '
                 'hypotheses are checked.\n')
    for letter, title, name in MODULES:
        combined += f'\n\n---\n\n# Appendix {letter}: {title}\n\n'
        combined += f'Source module: `{name}`. SHA-256: `{sha(ROOT / name)}`.\n\n'
        combined += (ROOT / name).read_text()
    combined_path = ROOT / 'T357_GAUSSIAN_COMPLETE_PROOF.md'
    combined_path.write_text(combined)
    acceptance = {
        'problem_id': 'T357', 'list': 'TOP200_DL',
        'status': 'complete internally reviewed mathematical answer in the explicitly permitted Gaussian random-feature regime',
        'published_open_problem_novelty_certified': False,
        'external_peer_review': False, 'formal_proof_assistant_verification': False,
        'central_registry_modified': False,
        'synthesis': record(synthesis.name),
        'complete_proof': record(combined_path.name),
        'proof_modules': [record(x[2]) for x in MODULES],
        'independent_reviews': [record(x) for x in REVIEWS],
        'quantifiers': {
            'finite_time': 'Every fixed finite horizon; every fixed positive finite alpha, gamma and c; finite beta >= 0.',
            'uniform_time': 'Explicit alpha/gamma > C_star(beta,gamma) and fixed 0 < c < gamma/(2 Lambda); all positive times and MLE.',
            'overconfidence': 'Positive beta; riskoptimal first-step scale; average confidence minus accuracy, not pointwise at every score.',
            'common_regime': 'Synthesis equation (16) gives a nonempty open weak-teacher regime in which the same fixed scale satisfies all conclusions.'
        },
        'verification': {
            'analytic': 'Independent derivations and adversarial assumption/normalization/scope checks; see pinned reviews.',
            'numeric': 'Two regimes, five iterations, dimensions 250/500/1000 and twelve network draws each; independent QMC scrambles.',
            'numeric_is_proof': False,
            'finite_network_A_Q': 'Asymptotically equivalent covariance proxies.'
        }
    }
    (ROOT / 'ACCEPTANCE.json').write_text(json.dumps(acceptance, indent=2)+'\n')
    files = sorted(p for p in ROOT.rglob('*') if p.is_file() and
                   '__pycache__' not in p.parts and p.name not in ['MANIFEST.json', 'SAVE_RECEIPTS.json'])
    manifest = {'algorithm': 'sha256', 'excluded': ['MANIFEST.json (self)', 'SAVE_RECEIPTS.json (written after immutable-commit verification)', '__pycache__'],
                'files': [{'path': str(p.relative_to(ROOT)), 'sha256': sha(p), 'bytes': p.stat().st_size} for p in files]}
    (ROOT / 'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
    delivery = WORK / 'deliverables'
    delivery.mkdir(exist_ok=True)
    shutil.copyfile(combined_path, delivery / combined_path.name)
    print(json.dumps({'files':len(files),'proof_bytes':combined_path.stat().st_size,'proof_sha256':sha(combined_path)}))


if __name__ == '__main__':
    main()
