#!/usr/bin/env python3
"""Reproduce the old enclosure-export failure without changing old artifacts.

Use exact fractions to distinguish binary64 parsing, exact decimal parsing,
and genuine rational endpoint serialization. This is an artifact audit, not
a mathematical counterexample to any accepted theorem.
"""
from pathlib import Path
from fractions import Fraction as F
import json, hashlib
from independent_check import entropy_interval, entropy_walsh, walsh_direct, plus, minus

ROOT = Path(__file__).resolve().parent

def inspect_export(name, exact, text_pair):
    lo,hi = exact
    binary = tuple(F.from_float(float(x)) for x in text_pair)
    decimal = tuple(F(x) for x in text_pair)
    result = {'field':name, 'old_exported_decimal_endpoints':list(text_pair),
              'recomputed_rational_lower':str(lo), 'recomputed_rational_upper':str(hi)}
    for label,parsed in [('binary64',binary),('exact_decimal',decimal)]:
        contains = parsed[0] <= lo and parsed[1] >= hi
        strictly_below = parsed[1] < lo
        strictly_above = parsed[0] > hi
        assert not contains and (strictly_below or strictly_above)
        result[label] = {'encloses':contains,'strictly_below':strictly_below,
                         'strictly_above':strictly_above,
                         'positive_separation':str(lo-parsed[1] if strictly_below else parsed[0]-hi)}
    return result

def main():
    base_l = entropy_interval([F(3,256)]*3+[F(9,256)]*3+[F(27,256)])
    witness = json.loads((ROOT/'product/witness.json').read_text())
    size = 1 << witness['n']
    negatives = set(witness['negative_f'])
    f = [-1 if x in negatives else 1 for x in range(size)]
    g = [-1]+[1]*(size-1)
    h = [a*b for a,b in zip(f,g)]
    ef,eg,eh = map(lambda x:entropy_walsh(walsh_direct(x)),(f,g,h))
    gap = minus(eh,plus(ef,eg))
    issues = [inspect_export('convolution.tensor_certificate.base_L_interval',base_l,
                            ('1.0772085933443496','1.0772085933443496')),
              inspect_export('product.seven_bit.excess_interval',gap,
                            ('0.1630852002095617','0.1630852002095617'))]
    saved = json.loads((ROOT/'independent_results.json').read_text())
    item = saved['seven_bit_gap']
    assert (F(item['rational_lower']),F(item['rational_upper'])) == gap
    pairs=[]
    def visit(x,path=''):
        if isinstance(x,dict):
            assert not any(k.endswith('_interval') for k in x)
            if 'rational_lower' in x:
                a,b=F(x['rational_lower']),F(x['rational_upper'])
                assert a<=b and 'decimal_summary' in x
                assert isinstance(x['rational_lower'],str) and isinstance(x['rational_upper'],str)
                pairs.append(path)
            for k,v in x.items(): visit(v,path+'.'+k)
        elif isinstance(x,list):
            for i,v in enumerate(x): visit(v,path+f'[{i}]')
    visit(saved)
    out={'artifact_audit_status':'ORIGINAL_FLOAT_INTERVAL_EXPORTS_FAIL',
         'mathematical_proofs_and_internal_exact_assertions':'UNAFFECTED',
         'independent_results_exact_serialization':'PASS',
         'independent_rational_endpoint_objects':pairs,
         'counterexamples':issues,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'serialization_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'artifact_audit_status':out['artifact_audit_status'],
                      'independent_results_exact_serialization':'PASS',
                      'rational_objects_checked':len(pairs)},indent=2))

if __name__=='__main__': main()
