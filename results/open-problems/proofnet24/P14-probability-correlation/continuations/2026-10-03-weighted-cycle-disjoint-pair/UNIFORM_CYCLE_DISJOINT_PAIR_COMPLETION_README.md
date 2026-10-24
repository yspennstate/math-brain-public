# Completion record: disjoint marked pair over a uniform cycle

This completed Chebyshev proof is retained as an elementary independent
route.  The later `weighted_cycle_apex_real_rooted_proof.md` supersedes it
in scope by allowing arbitrary rim activities and arbitrary profiles.

The full proof is `uniform_cycle_apex_real_rooted_proof.md`.  Its key exact
identity is

```text
D_n(s)/Z_Cn = [r_+^n+r_-^n-2p^n]/(1-p^n),
r_+ + r_- = 1+p+(1-p)s,   r_+ r_- = p,
p=lambda/(1+lambda).
```

Equivalently, the zeros solve `T_n(x)=p^(n/2)`.  They are all negative;
for positive lambda they are distinct.  This supplies the Stieltjes factors
required by the already audited arbitrary-backbone four-core identity and
proves marked-pair negative correlation at every activity.

Run the author checker with:

```text
python3 uniform_cycle_apex_real_rooted_exact.py
```

It independently builds the literal cycle/apex forest partition, the cyclic
gap formula, and the Lucas recurrence in 40 exact cases (`3<=n<=10`, five
rational activity regimes).  It also enumerates six whole graphs with the
four new vertices and verifies the exact Rayleigh difference against the
derivative formula.  All checks exited zero on 3 October 2026.

The independent audit and checker are separate files in this directory.
Read the source/scope record before using the result.  This is a cyclic
restricted theorem, not a solution of the general forest conjecture.
