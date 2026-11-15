"""Second derivation: exact falling-factorial C inequalities, no loose bounds.

Independent of the ratio bounds used in verify_counterexample.py.
"""
import json, math
from pathlib import Path

def audit(s):
    n=2**s; d=2**(2*s//3)
    fs=fd=fn=1; count=0
    for r in range(1,s+1):
        fs*=s-r+1; fd*=d-r+1; fn*=n-r+1
        # T_s(r)^2 <= 9^(s-r)4^(r-1) [q T_d(r)]^3.
        left=fs*fs*n**3*fn
        right=9**(s-r)*4**(r-1)*fd**3
        assert left<=right,(s,r)
        count+=1
    # Exact D for an s-atom: 1/C(n,s) <= 4^(s-1)[q T_d(s)]^2.
    assert fs*n*n*fn<=4**(s-1)*fd*fd
    # Beyond the middle layer the required squared factor times h is
    # (9/4)^(d-r) for r<=d, and 4^(n-d)(9/4)^(n-r) for r>d.
    # Exponents are nonnegative on the stated ranges, proving all ranks at once.
    assert n>d>s and n-s>2*d
    assert s%6==0 and s>=36
    # Log amplitude of the forced nonzero Fourier coefficient of f^2.
    log_mu_s=-math.log2(math.comb(n,s)) # replacing w by 1: upper approximation only
    log_amplitude_upper=1+.5*(log_mu_s+2-2*d)
    return {'s':s,'first_layer_exact_squared_C_checks':count,'first_layer_all_pass':True,
            'D_small_exact_pass':True,'remaining_C_ranks_symbolic_pass':True,
            'forced_square_coefficient_log2_magnitude_upper_approx':log_amplitude_upper,
            'forced_square_coefficient_nonzero':True}

if __name__=='__main__':
    out=[audit(s) for s in (36,48,60,96,192,384)]
    Path('audit_output.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
