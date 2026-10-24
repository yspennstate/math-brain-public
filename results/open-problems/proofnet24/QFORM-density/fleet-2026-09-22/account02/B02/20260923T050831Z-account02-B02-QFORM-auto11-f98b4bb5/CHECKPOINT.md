SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T05:08:31Z.
attacking: the first unpaid high-volume collar by replacing pair-disjoint row bases with a three-sample common-intersection compiler, then routing its exact zero endpoint.

# Early checkpoint — three-sample volume compiler

Full target remains OPEN.

Sources consumed: current brain control initially at `3ba6404453302a5c881ab3fa6054696352947c1b` and refreshed to `db998c386360e3a006a2412df4b642ce3e5c452f`; newest volume theorem `c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`; required Claude D'/D5 source `e5f71d79eff325201dd0274053d20268ce65b837`; designated partner account03/B02 r20 current report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T043653Z-account03-B02-qform-r20/REPORT.md` (read from current master).

## Independent analytic review checkpoint

The q-dependent sharp-Hausdorff--Young theorem in the newest volume-stability report checks out at the analytic level. For output exponent `r=q/alpha>=2`, Beckner gives

`|| |psi(2t .)|^q ||_(1/alpha)
 <= (pi/|t|)^alpha (alpha/q)^(alpha/2)
    (1-alpha/q)^(-(q-alpha)/2)`.

After the BL factor `alpha^(-alpha/2)`, summing row marginals `sum alpha=3`, and the two entropy bounds `-(1-x)log(1-x)<=x`, one obtains

`E F_t^q <= e^3 q^(-3/2)(pi/|t|)^3 Z^(-1/2)`.

Jensen plus the decoupling square gives exponent `b=3/(2q)`, and exact inversion yields

`||p_Q||inf <= 3e/[(3-2q)sqrt(q)] Z^(-1/6)`.

I also checked the projection-stability step: `W<=I`, `W<=3MM^T/kappa^2`, hence
`sqrt(alpha_i)<=sqrt(Pii)+(sqrt(3)epsilon/kappa)sqrt(1-Pii)`; under `||E||op<=a/16`, `s3(M0)>=a`, `max Pii<=1/2`, this gives `alpha_i<2/3`, so `q=4/3` is valid and the advertised `<23/a` constant follows. Analytic review verdict for this scope: PASS.

## New substantive lemma

Let `w_(R,T)=det(M[R,T])^2/Z`, `Z=E3(M)>0`, and let `mu_R=sum_T w_(R,T)` be the row-triple volume law. Draw three iid row triples `R1,R2,R3~mu` and put

`delta3=P(R1 cap R2 cap R3 = empty)`.

If `delta3>0`, condition the three-sample law on empty common intersection and let `nu` be its first marginal. Exchangeability gives every row inclusion marginal under `nu` at most `2/3`. Lift `nu` with the original conditional column law `w(T|R)`. Data processing gives `D(nu||mu)<=log(1/delta3)`. The sharp q-dependent entropy-BL calculation above at `q=4/3` therefore yields

`||p_Q||inf <= (9 sqrt(3) e / 2) delta3^(-1/6) Z^(-1/6)`.

This is a genuine L1 characteristic-function branch, retaining arbitrary same-bank phases/outside couplings.

At the exact endpoint `delta3=0`, the support family of positive row triples is 3-wise intersecting. A finite Helly-type argument for 3-sets gives exactly two possibilities: either one physical row belongs to every positive row triple (so deleting it leaves cross rank at most two), or every positive row triple is contained in one four-row set H. In the second case, because some triple in H is linearly independent and every triple using an outside row has zero 3-volume, every row outside H is actually zero; hence the entire physical cross block is supported on at most four rows.

This strictly extends the partner's pair-disjoint compiler: for any full-spark 5x3 cross block, two row triples can never be disjoint, so the partner parameter `delta2` is zero, while `delta3>0`. For the explicit Vandermonde rows `(1,t,t^2)`, `t=0,1,2,3,4`, `Z=700` and `delta3=9396/214375`; the new bound is `<11.975` for the corresponding cross-block branch.

Remaining gap: quantitatively route the small-but-positive `delta3` near-endpoint into the exact coloop/four-row mechanisms with a universal threshold, while retaining arbitrary self curvature and extra spectrum. The endpoint classification is exact; a stability theorem around it is not yet proved.
