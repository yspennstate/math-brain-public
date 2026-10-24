#!/usr/bin/env python3
"""Regenerate actual-input certificates with the recorded deterministic seed."""
from verify_remainder import generate_certificates
if __name__ == '__main__':
    result=generate_certificates()
    print('Actual physical inputs recorded:',len(result['physical_inputs_hex']))
    print('Final exact search record:',result['search'][-1])
