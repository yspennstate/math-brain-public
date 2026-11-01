# Late compatible-handoff addendum — fleet01/B16 dyadic overlap rigidity

After the main report was committed, the newer shared handoff `20260922T0500Z-fleet01-B16-dyadic-overlap-rigidity` became visible. I consumed it before finish.

That result proves an exact Boolean rigidity statement for the balanced-pivot scalar joint-credit relaxation: on a uniform remaining cube, equality at a nontrivial disagreement density can occur only at `delta=1/2`; every sparse dyadic defect `0<delta<1/2` therefore earns strict positive Booleanity credit beyond the non-Boolean scalar envelope. It leaves the quantitative dimension-independent size of that credit open.

This is compatible with, and sharper context for, Theorem 5.1 of the present B17 report. The B17 theorem treats one concrete source-admissible sparse defect family — an opposite-sign two-point flip after dummy padding — and proves the exact global asymptotics `Delta H=4 n q+O_f(q)`, `Delta I=n q+O_f(q)`. Hence its aggregate gate-margin increment at every fixed center `C>4` is `(C-4)nq+O_f(q)>0` eventually. This gives a quantitative *global* compensation statement for that family, but it does not prove a general quantitative lower bound for fleet01/B16's local joint-credit gap.

So the two results point in the same direction without being conflated: sparse dyadic Boolean defects have strict local rigidity, and the simplest physical two-point family is globally subcritical with slope 4. The remaining universal threat is a Boolean near-isoclinic/coherent family whose local rigidity credit tends to zero fast enough while its aggregate gate residual stays dangerous, or a proof that no such family exists.

Full FEI and `LIMIT-PRIME-GATE-LIFT-v1` remain OPEN / NOT PROVED.
