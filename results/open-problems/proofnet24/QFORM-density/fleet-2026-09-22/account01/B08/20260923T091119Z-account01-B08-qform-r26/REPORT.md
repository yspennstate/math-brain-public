SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T09:11:19.846031Z.
attacking: enlarge the genuinely diffuse spectral-window branch by spending ridge leverage with q>1, then route the next leverage layer through the completed account02/B08 physical-core theorem.

# account01/B08 r26 — q>1 ridge window and a wider diffuse/core interface

Programme `QFORM-DENSITY-3EIG-20260922`; OWNER CONTROL revision `2026-09-22.15`. Status: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / DESIGNATED_PARTNER_APPLIED / FULL_TARGET_OPEN**. Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted conjecture remains OPEN, and continuity for the unrestricted target remains OPEN. Everything below uses ORIGINAL independent coordinates. No moment, Gaussian, log-concave, compact-support, connected-support, post-rotation independence, pointwise law-uniform stationary-phase, arbitrary-joint coarea, conditional fiber-height moment, or random-smallness consequence of a small matrix tail is used.

## 1. Source-pinned inputs

Fresh control was read on `yspennstate/math-research-brain` current `main`; OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only. The live correction inbox was reread before publication.

The analytic input is the completed supporting ridge theorem

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For an ORIGINAL-coordinate cross block `B`, `gamma>0`,

`K=B B^T(gamma^2 I+B B^T)^(-1)`, `theta=tr K`.

If `1<=q<=2`, `max_i K_ii<=q/2`, and `theta>2q`, the FULL ambient quadratic form has a continuous `C_0` density and

`||p_Q||_infinity <= sqrt(e)/(sqrt(2q) gamma) * theta/(theta-2q)`.   (1.1)

The same source proves the perturbation estimate: if `B=B_0+F`, `||F||<=eta`, and the projection onto `range(B_0)` has diagonal at most `ell`, then

`max_i K_ii <= (sqrt(ell)+eta/gamma)^2`.                           (1.2)

The designated partner actually applied below is account02/B08 r23,

`yspennstate/math-open-problems@ab1940d32f6f758e7a355c128916a523e5519537`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T064247Z-account02-B08-qform-diffuse-r23/REPORT.md`.

Its theorem `QFORM-DIFFUSE-POST-2/3-CORE-ROUTER-v1` says that `Z_3=e_3(B^T B)>=zeta^6` implies either a continuous `C_0` density `<987/zeta`, a physical star `>zeta`, or one of the explicit S/R1/E2/BICORE product-preserving survivors recorded in Section 4 below.

## 2. Parametric q>1 spectral-window theorem

Let `0<kappa<1`. Let `P` be the spectral projection of the full symmetric matrix `A` onto **all** eigenspaces with `|lambda(A)|>=kappa`, and put

`delta=max_i P_ii`,
`g=1/2-delta-sqrt(2 delta)`.                                      (2.1)

Assume `g>kappa`. Let `r>0` and `1<=q<3/2` obey

`3/(1+r^2)>2q`,                                                   (2.2)

`( sqrt(delta/g) + kappa/[r(g-kappa)] )^2 < q/2`.                (2.3)

### Theorem 2.1 — `QFORM-SPECTRAL-WINDOW-QGT1-v1`

Under the original target hypothesis (at least three eigenvalues of `A` have modulus at least one), conditions (2.1)-(2.3) imply that for every independent cap-one product input the law of `Q=X^T A X` has a continuous density vanishing at infinity, with

`||p_Q||_infinity
 < sqrt(e)/(sqrt(2q) r(g-kappa))
    * [3/(1+r^2)]/[3/(1+r^2)-2q].`                              (2.4)

All eigenvalues below `kappa` may be nonzero, arbitrarily numerous, of either sign and arbitrarily oriented.

### Proof

Write `A=A_H+E`, where `A_H=U Lambda U^T` is the spectral truncation to `P`. Thus `U^T U=I`, every row `u_i` has `||u_i||^2=P_ii<=delta`, `Lambda` is invertible, `s_3(Lambda)>=1`, and `||E||<kappa`.

By the two-part Marcus-Spielman-Srivastava frame partition there is a physical partition `I union J` such that, with

`G_I=U_I^T U_I`, `G_J=U_J^T U_J`,

one has

`G_I,G_J >= g I`.                                                (2.5)

Indeed each part has Gram upper bound `(1/sqrt(2)+sqrt(delta))^2 I`, and the two Grams sum to `I`.

Put `B=A[I,J]`, `B_0=(A_H)[I,J]=U_I Lambda U_J^T`, and `F=E[I,J]`. Whiten the restricted frames. The nonzero singular values of `B_0` are those of

`G_I^(1/2) Lambda G_J^(1/2)`.

Hence `s_3(B_0)>=g s_3(Lambda)>=g`; since `||F||<kappa`,

`s_3(B)>sigma:=g-kappa`.                                        (2.6)

Also `range(B_0)=range(U_I)` and its physical projection diagonal satisfies

`(P_range(B_0))_ii=u_i^T G_I^(-1)u_i<=delta/g`.                 (2.7)

Set `gamma=r sigma`. By (1.2) and (2.3), `max_i K_ii<q/2`. By (2.6), the first three ridge eigenvalues each exceed `1/(1+r^2)`, so

`theta>3/(1+r^2)>2q`.                                           (2.8)

Apply (1.1). Since `theta/(theta-2q)` decreases for `theta>2q`, (2.4) follows. No spectral tail was dropped probabilistically. QED.

## 3. Concrete enlarged diffuse branch: leverage 0.059

Take

`delta=59/1000`, `kappa=1/1000`, `q=4/3`, `r=27/100`.             (3.1)

Then

`g=441/1000-sqrt(59/500)=0.0974887192536466...`,
`sigma=g-1/1000=0.0964887192536466...`.                          (3.2)

The ridge gate can be certified with rational slack. Since

`(0.34352)^2-59/500 =117/19531250>0`,

we have `g>0.09748`, hence `sigma>0.09648`. Therefore

`delta/g <59/97.48 <0.778^2`,

and

`kappa/(r sigma)<0.0384`.

Thus

`sqrt(delta/g)+kappa/(r sigma)<0.8164`,

while

`0.8164^2=0.66650896<2/3=q/2`.                                  (3.3)

Furthermore

`3/(1+r^2)=30000/10729=2.79615994...>8/3=2q`.                  (3.4)

Consequently:

### Corollary 3.1 — `QFORM-SPECTRAL1000-LEVERAGE059-v1`

If `P=P_{|A|>=1/1000}` satisfies

`max_i P_ii <=0.059`,                                           (3.5)

then the full target form has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <837.`                                 (3.6)

Using the exact constants in (2.4) gives `836.8302445...`; the slightly weaker `837` is recorded. This nearly doubles the earlier clean `1/32` spectral-window leverage range while still allowing an arbitrary dense nonseparable spectrum below `1/1000`.

There is also a mechanism threshold. Let `kappa->0` and `r->0`. Feasibility reduces to `delta/g<3/4`, equivalently, with `x=sqrt(2delta)`,

`7x^2+6x-3<0`.

Thus the limiting leverage threshold of this two-part/q-ridge mechanism is

`delta_*=(39-6sqrt(30))/98=0.06261884234...`.                   (3.7)

For every fixed `delta<delta_*`, sufficiently small positive `kappa` and suitable `q<3/2,r>0` make Theorem 2.1 apply. This is a statement about this proof mechanism, not a proof of the full conjecture.

## 4. Designated partner applied one leverage layer farther

Take instead the slightly larger physical leverage threshold

`delta=1/16`, `kappa=1/1000`.                                   (4.1)

The same MSS construction gives

`g=(7-4sqrt(2))/16=0.0839466094067262...`,
`sigma=g-0.001=0.0829466094067262...`.                           (4.2)

The resulting **actual full** physical cross block has `s_3(B)>sigma`; hence

`Z_3=e_3(B^T B)>sigma^6`.                                       (4.3)

Apply account02/B08 r23 at the actual scale `zeta=sigma`. One obtains one of:

1. a continuous `C_0` density
   `boxed: ||p_Q||_infinity<987/sigma=11899.221...`;             (4.4)
2. a physical cross star `>sigma=0.0829466...`;                 (4.5)
3. an S branch of three disjoint original-coordinate linear banks with coefficient-norm product
   `>0.0526286782826 sigma^3 =3.00344e-5`;                      (4.6)
4. an R1 core with `G>0.0372140952985 sigma=0.00308678...` and `dist_F(N,{rank<=1})<G/2`; (4.7)
5. an E2 core with
   `E_2(N)>1.70226e-11` and matched four-bank reserve `>1.06392e-12`; (4.8)
6. a BICORE row and column star each `>0.000840116`.             (4.9)

This is an actual use of the designated partner theorem, not a restatement. It pushes a structured source-valid interface to the leverage `1/16` layer even though the convenient `kappa=1/1000` q-ridge payment above is only asserted through `0.059`.

## 5. Complementary high-leverage certificate and remaining debt

Corollary 3.1 gives an immediate basis-invariant dichotomy at the fixed spectral window `1/1000`:

- either `max_i P_ii<=0.059` and the form is continuously paid by `<837`, or
- some physical coordinate satisfies `P_ii>0.059`.

In the latter case

`||A e_i||_2^2=e_i^T A^2 e_i >=10^-6 P_ii>5.9e-8`,             (5.1)

so

`||A e_i||_2>sqrt(59)/(10000 sqrt(10))=0.000242899...`.         (5.2)

Thus the remaining global work can be concentrated on a quantitatively high spectral-leverage physical coordinate, rather than the fully diffuse regime.

The first unpaid B08 implication is now `QFORM-WINDOW059-HIGHLEVERAGE-RECEIVER-v1`: use the physical coordinate guaranteed by (5.1)-(5.2), together with the wider `1/16` partner S/R1/E2/BICORE router when available, to force one of the already-paid localized scalar/pair/hub/grouped-square branches while retaining every low-spectrum coupling. A large `||Ae_i||` alone is not yet a density theorem, because same-bank curvature can obstruct naive one-hub absorption.

The full conjecture remains OPEN. Continuity is proved on the paid ridge and partner-paid branches only.
