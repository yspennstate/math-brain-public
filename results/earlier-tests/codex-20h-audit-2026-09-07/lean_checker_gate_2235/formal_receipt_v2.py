"""Reviewed-source receipt requiring a theorem declaration and allowed axioms."""
import re
from formal_receipt import classify as classify_axioms


def classify(returncode, output, **kwargs):
    result = classify_axioms(returncode, output, **kwargs)
    result['target_kind'] = 'UNVERIFIED'
    if not result['formal_target_verified']:
        return result
    target = re.escape(result['target'])
    kinds = re.findall(r'^TARGET_KIND ' + target + r': theorem=(true|false)\s*$', output, re.M)
    if len(kinds) != 1:
        result.update(status='TARGET_KIND_MISSING_OR_AMBIGUOUS', formal_target_verified=False)
    elif kinds[0] != 'true':
        result.update(status='TARGET_KIND_UNSUPPORTED', formal_target_verified=False,
                      target_kind='not_theorem')
    else:
        result['target_kind'] = 'theorem'
    return result
