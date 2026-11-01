"""Classify trusted-source Lean target evidence without overclaiming translation."""
import re

STANDARD_AXIOMS = frozenset({'propext', 'Classical.choice', 'Quot.sound'})


def classify(returncode, output, *, target, timed_out=False, source_reviewed=False,
             translation_reviewed=False, allowed_axioms=STANDARD_AXIOMS):
    if type(source_reviewed) is not bool or type(translation_reviewed) is not bool:
        raise ValueError('Review assertions must be explicit booleans')
    if not set(allowed_axioms) <= STANDARD_AXIOMS:
        raise ValueError('Custom axioms cannot be approved as an unconditional proof certificate')
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_'.]*", target):
        raise ValueError('An explicit simple Lean declaration name is required')
    result = {'status': None, 'formal_target_verified': False, 'target': target,
              'source_reviewed': bool(source_reviewed),
              'translation_reviewed': bool(translation_reviewed), 'axioms': None,
              'allowed_axioms': sorted(allowed_axioms),
              'mathematical_falsity_established': False}
    if timed_out or returncode is None:
        result['status'] = 'RUNTIME_UNVERIFIED'
    elif returncode != 0:
        result['status'] = 'COMPILE_FAILED'
    elif not source_reviewed:
        result['status'] = 'COMPILED_SOURCE_UNREVIEWED'
    else:
        name = re.escape(target)
        empty = re.findall(r"^'"+name+r"' does not depend on any axioms\s*$", output, re.M)
        lists = re.findall(r"^'"+name+r"' depends on axioms:\s*\[([^\]]*)\]", output, re.M)
        if len(empty) + len(lists) != 1:
            result['status'] = 'TARGET_EVIDENCE_MISSING_OR_AMBIGUOUS'
            return result
        axioms = [] if empty else [x.strip() for x in lists[0].split(',') if x.strip()]
        result['axioms'] = axioms
        if 'sorryAx' in axioms:
            result['status'] = 'ADMITTED_TARGET'
        elif not set(axioms) <= set(allowed_axioms):
            result['status'] = 'UNAPPROVED_AXIOMS'
        else:
            result['formal_target_verified'] = True
            result['status'] = 'FORMAL_TARGET_VERIFIED'
    return result
