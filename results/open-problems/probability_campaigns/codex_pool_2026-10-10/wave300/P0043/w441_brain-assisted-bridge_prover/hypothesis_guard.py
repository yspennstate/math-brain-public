"""A proposed offline applicability check; it infers no mathematical hypotheses."""

def check(required, established):
    """A hypothesis must be explicitly True, not merely absent or truthy."""
    missing = [name for name in required if established.get(name) is not True]
    return {
        'applicable': not missing,
        'false_hypotheses': [name for name in missing if established.get(name) is False],
        'unknown_hypotheses': [name for name in missing if established.get(name) is not False],
        'note': 'This only checks supplied hypotheses; it is not a mathematical verifier.'
    }
