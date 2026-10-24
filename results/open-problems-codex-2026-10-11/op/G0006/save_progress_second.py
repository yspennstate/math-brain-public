from pathlib import Path
p=Path('SECOND_ATTEMPT.md')
with p.open('a',encoding='utf8') as f:f.write('''

## Progress saved: buffered block certificate

A buffer is needed if the wired finite-volume calculation is to approximate an infinite-volume crossing law. For block side L define C_z=Lz+[0,L-1]^d, M_z=Lz+[-L,2L-1]^d, and D_z=Lz+[-2L,3L-1]^d. Run the finite contact process on D_z with all exterior vertices permanently infected. Let b_L(lambda) be its stationary probability of an occupied path, entirely in M_z, from C_z to the inner vertex boundary of M_z.

Candidate theorem now being checked: b_L(lambda)<(2d-1)^(-5^d) implies nonpercolation of nu_lambda. Disjoint D_z boxes are independent after coloring z by its coordinate residues modulo 5; this number of colors does not grow with L. Continuity of this finite stationary probability implies that a strict certificate at lambda_c would imply a gap.

A further reduction looks possible in dimension two: the original gap should be equivalent to existence of such a finite certificate at lambda_c. For necessity, choose a rate strictly between lambda_c and a supercritical nonpercolating rate, apply van den Berg's exponential cluster-size theorem, and control the buffered wired-law discrepancy by finite propagation plus exponential temporal convergence. This implication must be written fully before it is called proved.

The earlier 3-by-3 calculation in compute_wired.py is the UNBUFFERED diagnostic, not the 5-by-5 L=1 buffered law. It gives crossing probability 0.204892335 at lambda=1/4 and 0.393353517 at lambda=0.4; these are floating-point results only. They fail the unbuffered certificate. No stationary buffered probability has yet been certified.
''')
