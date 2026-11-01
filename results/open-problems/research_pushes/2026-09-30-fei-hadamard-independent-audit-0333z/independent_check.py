#!/usr/bin/env python3
"""Finite independent cross-checks; the all-dimension result is proved in AUDIT.md."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json

HERE = Path(__file__).resolve().parent

def ln_rational_bounds(x, terms=64):
    """Direct atanh series for positive rational x >= 1; no binary float."""
    x = Q(x)
    assert x >= 1
    z = (x-1)/(x+1)
    z2 = z*z
    term = z
    total = Q(0)
    for i in range(terms):
        total += 2*term/(2*i+1)
        term *= z2
    return total, total + 2*term/((2*terms+1)*(1-z2))

def rational_pair(bounds):
    return [{'numerator': str(q.numerator), 'denominator': str(q.denominator)} for q in bounds]

def check_case(w):
    L = len(w)
    signs = list(product((-1,1), repeat=L))
    index = {y:i for i,y in enumerate(signs)}
    H = [[(-1)**((i&j).bit_count()) for j in range(L)] for i in range(L)]
    norm_w2 = sum(a*a for a in w)
    norm_a2 = L*norm_w2
    onehot = 0
    total_influence = {1:Q(0),-1:Q(0)}
    max_l1 = 0
    ties = 0
    for xi in signs:
        a = [sum(H[j][i]*xi[i]*w[i] for i in range(L)) for j in range(L)]
        assert sum(t*t for t in a) == norm_a2
        max_l1 = max(max_l1, sum(abs(t) for t in a))
        onehot += sum(t!=0 for t in a)==1
        z = [sum(a[j]*y[j] for j in range(L)) for y in signs]
        ties += z.count(0)
        assert sum(t*t for t in z) == len(signs)*norm_a2
        assert sum(t**4 for t in z) == len(signs)*(3*norm_a2**2-2*sum(t**4 for t in a))
        for tie in (1,-1):
            f = [1 if t>0 else -1 if t<0 else tie for t in z]
            influences = []
            for j in range(L):
                flip = [index[y[:j]+(-y[j],)+y[j+1:]] for y in signs]
                influences.append(Q(sum(f[i]!=f[flip[i]] for i in range(len(signs))),len(signs)))
                correlation = Q(sum(y[j]*f[i] for i,y in enumerate(signs)),len(signs))
                orientation = (a[j]>0)-(a[j]<0)
                assert correlation == orientation*influences[-1]
            weighted = sum(abs(a[j])*influences[j] for j in range(L))
            assert weighted == Q(sum(abs(t) for t in z),len(signs))
            influence = sum(influences)
            assert 3*max(t*t for t in a)*influence**2 >= norm_a2
            total_influence[tie] += influence/len(signs)
    flat = all(L*t*t==norm_w2 for t in w)
    assert onehot == (2*L if flat else 0)
    assert L*L*norm_w2 <= 3*max_l1**2
    assert max_l1**2 <= L*L*norm_w2
    ln_lo,ln_hi = ln_rational_bounds(4*L)
    for inf in total_influence.values():
        assert 24*inf*inf*ln_lo >= L
    return {'L':L,'w':list(w),'onehot_count':onehot,'sign_layer_inputs':len(signs),
            'ties_across_xi_Y':ties,'expected_influence_tie_plus':str(total_influence[1]),
            'expected_influence_tie_minus':str(total_influence[-1]),
            'max_l1_numerator':max_l1,'normalization_squared':norm_a2}

def main():
    cases = [(1,),(-2,)]
    cases += list(w for w in product(range(-2,3),repeat=2) if any(w))
    cases += list(w for w in product((-1,0,1),repeat=4) if any(w))
    cases += [(1,2,3,4),(1,)*8,(1,0,0,0,0,0,0,0),(1,2,0,-1,0,0,3,-2)]
    results = [check_case(w) for w in cases]
    # Reproduce the pinned artifact's serialization defect, not its proof logic.
    source = HERE/'source'/'verify.py'
    spec = importlib.util.spec_from_file_location('pinned_author_checker',source)
    author = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(author)
    defects = []
    for L in (2,4,8):
        lo,hi = author.ln_interval(Q(4*L))
        exact = (Q(L,24)/hi,Q(L,24)/lo)
        printed = author.encl(exact)
        lower,upper = map(Q.from_float,printed)
        lower_exceeds_true_upper = lower>exact[1]
        upper_below_true_lower = upper<exact[0]
        assert lower_exceeds_true_upper or upper_below_true_lower
        defects.append({'L':L,'serialized':printed,'certified_rational_bounds':rational_pair(exact),
            'lower_exceeds_true_upper':lower_exceeds_true_upper,
            'upper_below_true_lower':upper_below_true_lower})
    final_source = HERE/'final'/'verify.py'
    final_spec = importlib.util.spec_from_file_location('final_author_checker',final_source)
    final_author = importlib.util.module_from_spec(final_spec)
    final_spec.loader.exec_module(final_author)
    final_author.test_enclosures()
    final_encl = final_author.encl
    export_checks = []
    def audited_encl(bounds):
        pair = final_encl(bounds)
        binary_ok = Q.from_float(pair[0])<=bounds[0]<=bounds[1]<=Q.from_float(pair[1])
        decimal_ok = Q(str(pair[0]))<=bounds[0]<=bounds[1]<=Q(str(pair[1]))
        assert binary_ok and decimal_ok
        export_checks.append({'pair':pair,'binary64_enclosure':binary_ok,'exact_decimal_enclosure':decimal_ok})
        return pair
    final_author.encl = audited_encl
    configs = [(2,1,1),(2,2,1),(2,3,1),(2,4,1),(2,2,2),(4,1,1),(4,2,1),(4,3,1),(4,1,2),(8,1,1)]
    final_checks = [final_author.calc(*args) for args in configs]
    saved_final = json.loads((HERE/'final'/'verification.json').read_text())
    assert final_checks == saved_final['checks']
    final_sha = hashlib.sha256(final_source.read_bytes()).hexdigest()
    assert final_sha == saved_final['script_sha256']
    assert len(export_checks)==20
    result = {'status':'ANALYTIC_PASS_EXPORT_REPAIR_VERIFIED','full_classical_FEI':'OPEN',
        'source_commit':'c4d07e6e2280aa54c767512540d143f930154d3c',
        'source_script_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'corrected_commit':'67c4459ae0e8ae85a228c7a5c2629f003910139b',
        'corrected_script_sha256':final_sha,'corrected_export_checks':export_checks,
        'corrected_output_exact_checks_match':True,
        'case_count':len(results),'checked_threshold_inputs_per_tie_convention':sum((1<<len(w))**2 for w in cases),
        'checks':results,'pinned_serialization_defects':defects,
        'scope':'Finite cross-check only. Analytic independent audit in AUDIT.md. No formal certification or novelty claim.'}
    target=HERE/'independent_results.json'
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('checks','pinned_serialization_defects','corrected_export_checks')},indent=2))
    print('Saved exact rational defect witnesses to',target)

if __name__=='__main__':
    main()
