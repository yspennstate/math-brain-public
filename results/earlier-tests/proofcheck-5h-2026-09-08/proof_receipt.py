"""Truthful Lean receipt classification for explicitly reviewed source.

This is not a sandbox. Lean metaprograms can print arbitrary output; a matching
reviewed-source hash must represent a real review of code, imports and macros.
The receipt does not establish fidelity to an informal mathematical statement.
"""
import hashlib
import re

STANDARD_AXIOMS = frozenset({'propext', 'Classical.choice', 'Quot.sound'})
TARGET_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']*)*")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def validate_target(target):
    if not isinstance(target, str) or not TARGET_RE.fullmatch(target):
        raise ValueError('Use a simple, fully qualified Lean declaration name')
    return target


def target_commands(target):
    validate_target(target)
    # Environment lookup distinguishes a theorem from a definition or axiom.
    return ('\nopen Lean Elab Command in\nrun_cmd do\n'
            f'  let ci ← getConstInfo ``{target}\n'
            '  let isTheorem : Bool := match ci with | .thmInfo _ => true | _ => false\n'
            f'  logInfo m!"TARGET_KIND {target}: theorem={{toString isTheorem}}"\n'
            f'#print axioms {target}\n')


def classify(returncode, output, *, source_sha256, reviewed_sha256=None,
             target=None, evidence_integrity=True, timed_out=False):
    output = '\n'.join(output.splitlines())
    if target is not None:
        validate_target(target)
    if not re.fullmatch(r'[0-9a-f]{64}', source_sha256):
        raise ValueError('Source SHA256 required')
    if type(evidence_integrity) is not bool or type(timed_out) is not bool:
        raise ValueError('Integrity and timeout must be explicit booleans')
    result = dict(status=None, formal_target_verified=False, target=target,
                  source_sha256=source_sha256, source_review_assertion=reviewed_sha256,
                  target_kind='UNVERIFIED', axioms=None,
                  allowed_axioms=sorted(STANDARD_AXIOMS),
                  translation_fidelity='UNVERIFIED',
                  mathematical_falsity_established=False,
                  threat_model='Explicitly reviewed source and trusted compiler/dependencies; not a sandbox')
    if not evidence_integrity:
        result['status'] = 'EVIDENCE_DRIFT_OR_MISSING'
    elif timed_out or returncode is None:
        result['status'] = 'RUNTIME_UNVERIFIED'
    elif returncode != 0:
        result['status'] = 'COMPILE_FAILED'
    elif target is None:
        result['status'] = 'COMPILED_NO_NAMED_TARGET'
    elif reviewed_sha256 is None:
        result['status'] = 'COMPILED_SOURCE_UNREVIEWED'
    elif reviewed_sha256 != source_sha256:
        result['status'] = 'SOURCE_REVIEW_MISMATCH'
    else:
        name = re.escape(target)
        kinds = re.findall(r'^TARGET_KIND ' + name + r': theorem=(true|false)$', output, re.M)
        empty = re.findall(r"^'" + name + r"' does not depend on any axioms$", output, re.M)
        lists = re.findall(r"^'" + name + r"' depends on axioms:\s*\[([^\]\r\n]*)\]$", output, re.M)
        if len(kinds) != 1:
            result['status'] = 'TARGET_KIND_MISSING_OR_AMBIGUOUS'
        elif kinds[0] != 'true':
            result.update(status='TARGET_NOT_THEOREM', target_kind='not_theorem')
        elif len(empty) + len(lists) != 1:
            result.update(status='TARGET_AXIOMS_MISSING_OR_AMBIGUOUS', target_kind='theorem')
        else:
            axioms = [] if empty else [s.strip() for s in lists[0].split(',')]
            # Empty/malformed list entries are not permission to drop evidence.
            if lists and (not axioms or any(not TARGET_RE.fullmatch(s) for s in axioms)):
                result.update(status='MALFORMED_AXIOM_RECEIPT', target_kind='theorem')
                return result
            result.update(target_kind='theorem', axioms=axioms)
            if 'sorryAx' in axioms:
                result['status'] = 'ADMITTED_TARGET'
            elif not set(axioms) <= STANDARD_AXIOMS:
                result['status'] = 'UNAPPROVED_AXIOMS'
            else:
                result.update(status='FORMAL_TARGET_VERIFIED', formal_target_verified=True)
    return result


def exit_code(receipt):
    if receipt['formal_target_verified']:
        return 0
    if receipt['status'] in {'COMPILE_FAILED', 'ADMITTED_TARGET', 'UNAPPROVED_AXIOMS', 'TARGET_NOT_THEOREM'}:
        return 1
    if receipt['status'] in {'RUNTIME_UNVERIFIED', 'EVIDENCE_DRIFT_OR_MISSING', 'SOURCE_REVIEW_MISMATCH'}:
        return 2
    return 3
