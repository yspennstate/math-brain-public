# Checks — fleet01/B09 — 20260924T001451Z

These are deterministic/symbolic-numeric regressions for the supporting theorems in `REPORT.md`; they are not evidence for the unrestricted conjecture by themselves.

## 1. Constants

`3*2^(2/3) = 4.762203155904598`.

For the eight-leaf target family with `a=8`, `M=1`, `S=1/sqrt(2)`, `b=1`,

`3*2^(2/3) * (1/sqrt(2))^(2/3) * 8^(-1/3)
 = (3/2)2^(1/3)
 = 1.8898815748423097`.

For `|sigma|<=1`, the smaller absolute star-block eigenvalue is minimized at `|sigma|=1` and equals

`(sqrt(17)-1)/2 = 1.5615528128088303 > 1`.

For the same family, `Omega_(2,H)=896`, and the packet-only estimate is

`6*896^(-1/6)=1.9324128441272834`,

consistent with but slightly weaker than the direct `1.889881...` receiver.

## 2. Invariant identity `g^T adj(B)g=(Jg)^T B(Jg)`

For a fixed-seed symmetric test matrix

`B=[[0.89806201,-0.08513388],[-0.08513388,0.34781958]]`

and

`g=(-0.82161107,0.02033065)`,

we obtained

`kappa_g=g^T adj(B)g=0.23232084622500596`,

while

`(Jg)^T B(Jg)/||g||^2 = 0.34394561781427574`

and

`kappa_g/||g||^2 = 0.34394561781427574`,

as required by equation (2.5).

## 3. Cross-minor identity

With the same `B,g` and a fixed-seed five-vector `r`, form

`A=[[B,g r^T],[r g^T,0]]`.

For every ordered pair `i!=j`, direct determinants satisfy

`det A[H union {i}, H union {j}] = -kappa_g r_i r_j`

with maximum absolute discrepancy

`1.1102230246251565e-16`.

Summing the ordered pair squares gives

`direct Omega_(2,H)=1.0653065263720105`,

versus

`kappa_g^2[(sum r_i^2)^2-sum r_i^4]=1.0653065263720103`,

absolute discrepancy `2.220446049250313e-16`.

## 4. Proof-scope audit

The new bathtub step uses the density cap of the independent scalar `W` only after fixing `v`; an arbitrary `H(v)` is therefore a target translation and causes no conditional-density assumption. No claim is made for `H` depending on the same leaf variables as `W`. The hub rotation/shear is used only for integration; independence of the transformed hub coordinates is never asserted. The final small-ball estimate is linear in interval length and does not square a probability.
