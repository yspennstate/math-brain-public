SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B12, 2026-09-22T18:18:10Z.
attacking: scalar-Q_rest conditioning under one arbitrary extra eigenvalue; test the proposed uniform conditional core-density cap on an exact four-coordinate product source.

# QFORM-SCALAR-CONDITIONING-SUP-FALSE-v1

Status: rigorous counterexample to a proposed proof interface; FULL QFORM remains OPEN. This is not a counterexample to the quadratic-form bounded-density conjecture.

Let `X_1,...,X_4` be iid Uniform[0,1], `z=(1,1,1,1)^T/2`, `P=I_4-z z^T=I_4-J_4/4`, and for any real `tau != 0` let

`A_tau=P+tau z z^T=I_4-(1-tau)J_4/4`.

Then `spec(A_tau)={1,1,1,tau}`. Hence `A_tau` is in the exact target class for every tau; for `0<|tau|<1` the three unit eigenvalues are the unique large core. Write `Q=Q_3+Q_rest` with `Q_3=X^T P X` and `Q_rest=tau(z^T X)^2`.

Put `Z=z^T X=(sum_i X_i)/2`. Fix `s in (3/2,2)` and set `r=2(2-s) in (0,1)`. With `U_i=1-X_i`, conditioning on `Z=s` is conditioning on `sum_i U_i=r`. For `r<1` the upper bounds `U_i<=1` are automatic. The change of variables `(U_1,U_2,U_3,U_4)->(U_1,U_2,U_3,R=sum U_i)` has Jacobian one, so given `R=r`, `(U_1,U_2,U_3)` is uniform on `D_r={u_j>=0, sum_{j<=3}u_j<=r}` with density `6/r^3`. Thus `U=rV` with V uniform on the standard 3-simplex.

Since `P1=0`,

`Q_3=||PX||^2=||PU||^2=r^2(sum_i V_i^2-1/4)`.

On the simplex `1/4<=sum_i V_i^2<=1`, so the complete conditional law is supported in `[0,3r^2/4]`. Set `b=tau s^2`. Because `Z>=0`, conditioning on `Q_rest=b` is the same as conditioning on `Z=s` at these levels. Therefore any conditional density version obeys

`||p_{Q_3|Q_rest=b}||_infinity >= 4/(3r^2)=1/[3(2-s)^2]`.

As `s->2-` (equivalently `b->4tau` through the support), this diverges. If a conditional density failed to exist at some level, the proposed bounded-density interface would fail even more strongly; here coarea on the simplex gives a density away from the single quadratic critical point. Hence

`sup_b ||p_{Q_3|Q_rest=b}||_infinity = infinity`.

This rigorously refutes the revision-2026-09-22.11 worst-fiber scalar-conditioning bridge, already in dimension four with a cap-one product source and one additional eigenvalue.

The construction is NOT a QFORM counterexample. For the physical principal block on coordinates 1,2,3,

`B_tau=I_3-(1-tau)J_3/4`,

whose eigenvalues are `{1,1,(1+3tau)/4}`. The completed designated-partner fleet03/B12 theorem at `yspennstate/math-open-problems@b3c543b40dfaef13468466fa82625303a7719af8:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md` gives a full-ambient density cap `C_*/L` whenever a physical 3x3 block has two same-sign eigenvalues of magnitude at least L, with arbitrary third eigenvalue. Taking L=1 yields

`||p_{X^T A_tau X}||_infinity <= C_*=24.183038289961516...`

for every real tau. Thus the full law is uniformly stable under an arbitrary fourth eigenvalue of either sign and any magnitude even though the scalar-conditioned core cap is infinite.

The valid identity `p_Q(y)=E[p_{Q_3|Q_rest}(y-Q_rest)]` is not the problem; the invalid step is replacing this average by the worst conditional fiber. Extreme Q_rest levels collapse the product source onto simplices of diameter O(r), making the conditional Q_3 density O(r^-2), while their Q_rest weights simultaneously vanish. Any viable scalar-conditioning proof must retain that compensating level weight inside an averaged fractional-trace/kernel functional.

