SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T16:08:24Z.
attacking: QFORM-SECONDANCHOR-CRITICAL-STABLERANK-RECEIVER-v1 by lifting sharp-Hausdorff--Young volume estimates through a physical anchor while leaving the residual original-coordinate product banks untouched.

# account02/B02 — Hilbert-valued Schur-volume lift and complete invertible-second-anchor L1 receiver

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Integrated Fourier estimate  
**Status:** ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN  
**Target-wide unweighted Fourier L1:** OPEN_NOT_REFUTED  
**Continuity:** proved on every new Fourier-L1 branch below; full-target continuity remains open.

The target is unchanged: arbitrary independent real input coordinates with probability densities at most one and arbitrary real symmetric A with at least three eigenvalues of modulus at least one. No moments, support bounds, log-concavity, iid assumption, diagonal-basis independence, post-rotation independence, or post-Schur independence is used.

## 1. Source-pinned live inputs and immediate D'/D5 exits

Required Claude source actually read and used:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Reviewed sharp-Hausdorff--Young continuation actually used:

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For a physical original-coordinate cross block B put

`Z=E3(B)=e3(B^T B)`.

At `q=4/3`, the sharp D' theorem says that if all third-volume row marginals are at most `2/3`, then

`boxed: ||p_Q||inf <= (9 sqrt(3) e/2) Z^(-1/6),`                         (1.1)

and `phi_Q in L1`.

The same reviewed degree-k calculation at `k=5,q=2` is the sharp D5 estimate

`boxed: ||p_Q||inf <= (5e/sqrt(2)) E5(B)^(-1/10).`                       (1.2)

Thus, on the same live physical block, the concrete fifth-volume gate

`E5(B) >= 2^(-10) Z^(5/3)`                                             (1.3)

already gives

`boxed: ||p_Q||inf <= 5 sqrt(2) e Z^(-1/6) <19.222 Z^(-1/6).`           (1.4)

No marginal hypothesis is needed for (1.2)-(1.4).

The latest completed designated partner result actually consumed is `account03/B02` r33, canonical mathematics

`yspennstate/math-open-problems@604b3273a6db312558088b7ed2a9d9735c546e7a:proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T150032Z-account03-B02-qform-r33/REPORT.md`.

Its theorem `QFORM-H2-TO-H3-OR-STRIPS-v1` works on the live heavy-anchor branch and proves

`max{G3,U,V}>Z/864`,                                                   (1.5)

where `G3` is an actual double-anchor incident third-volume packet and `U,V` are literal one-sided physical 2x2-minor strip products. This run applies the `G3` alternative to a new inequality in Section 6.

## 2. New general mechanism — QFORM-HILBERT-SCHUR-VOLUME-LIFT-v1

Let two disjoint original-coordinate banks be split as anchor plus residual coordinates. For an invertible `r x r` physical cross anchor P write the physical cross block as

`B = [[P,R],[C,M]],`                                                   (2.1)

and define the algebraic cross-Schur residual

`S=M-C P^(-1)R`.                                                       (2.2)

This identity is used only in coefficients. The residual random variables are never sheared or rotated.

After conditioning every outside original coordinate, denote the row-anchor variables by x, row-residual variables by z, column-anchor variables by y, and column-residual variables by w. The cross phase satisfies the exact identity

`x^T P y+x^T Rw+z^T Cy+z^T Mw`
` = (x+P^(-T)C^Tz)^T P (y+P^(-1)Rw)+z^T S w`.                         (2.3)

The full same-bank quadratic and affine phases remain arbitrary. Change variables only in the anchor integrations x and y. Translation preserves the L2 norm of every anchor amplitude. With the Fourier convention used in the source, the `r`-dimensional bilinear Fourier operator has L2 norm

`pi^(r/2)|det P|^(-1/2)|t|^(-r/2)`.                                  (2.4)

Therefore

`|phi_Q(t)| <= pi^(r/2)|det P|^(-1/2)|t|^(-r/2) |J_S(t)|,`             (2.5)

where for some Hilbert space H

`J_S(t)=E_{Z,W}[e^(iF_t(Z)+iG_t(W)+2it Z^T S W)<u_Z,v_W>]`,            (2.6)

with `||u_Z||_H,||v_W||_H<=1`. Crucially, Z and W are still the original independent coordinate banks.

Cauchy--Schwarz in Z removes the Hilbert amplitude:

`|J_S(t)|^2`
` <= E_{W,W'} prod_i |psi_i(2t(S(W-W'))_i)|.`                          (2.7)

Indeed, after expanding the squared Hilbert norm, `|<v_W,v_W'>|<=1`; the Z expectation factorizes over the original independent coordinates. Every coordinate of `W-W'` has convolution density of mass one and cap at most one. Hence the scalar volume-sampling Brascamp--Lieb / sharp-Hausdorff--Young proof applies to (2.7) verbatim for the coefficient matrix S.

In particular, for `Z_k(S)=E_k(S)=e_k(S^T S)>0`, volume-row marginals `alpha_i^(k)`, and `q>=1` satisfying `alpha_i^(k)<=q/2`,

`boxed:
 |J_S(t)|
 <= e^(k/(2q)) q^(-k/(4q)) pi^(k/(2q))
    E_k(S)^(-1/(4q)) |t|^(-k/(2q)).
`                                                                            (2.8)

This is the main new interface. It transports the reviewed D_k estimate through a physical anchor without ever claiming that Schur-transformed random coordinates are independent.

## 3. Complete invertible 2x2 second-anchor receiver

Now take `r=2`. Put

`D=|det P|`, `T=||S||_F^2`, `G=D^2 T>0`.                              (3.1)

The previous run paid `sr(S)>=5/2` by D5 interpolation. The new lift removes the stable-rank threshold entirely.

### 3.1 Diffuse residual energy

The `k=1` volume law has row marginals

`alpha_i=||S_{i,*}||_2^2/T`.                                          (3.2)

If every row marginal is at most `1/2`, use (2.8) with `k=q=1`:

`|J_S(t)| <= e^(1/2) pi^(1/2) T^(-1/4)|t|^(-1/2).`                   (3.3)

Combining (2.5) with (3.3),

`|phi_Q(t)| <= e^(1/2) pi^(3/2) G^(-1/4)|t|^(-3/2).`                 (3.4)

The same argument applies after transposing B if all column-energy marginals are at most `1/2`. Since

`(2pi)^(-1) int_R min(1,K|t|^(-3/2))dt = (3/pi)K^(2/3)`,              (3.5)

we get

`boxed: ||p_Q||inf <= 3e^(1/3) G^(-1/6) <4.187 G^(-1/6).`             (3.6)

### 3.2 Non-rank-one residual energy

The `k=2,q=2` volume estimate is ungated because every second-volume marginal is at most one. Equation (2.8) gives

`|J_S(t)| <= e^(1/2)2^(-1/4)pi^(1/2) E2(S)^(-1/8)|t|^(-1/2).`        (3.7)

Let the squared singular values of S be `s_j^2`, and set

`epsilon=1-s_1^2/T`, `theta=E2(S)/T^2`.                               (3.8)

Then

`|phi_Q(t)| <= e^(1/2)2^(-1/4)pi^(3/2)
               theta^(-1/8)G^(-1/4)|t|^(-3/2),`                      (3.9)

so

`boxed:
 ||p_Q||inf <=3e^(1/3)2^(-1/6)theta^(-1/12)G^(-1/6).
`                                                                            (3.10)

Since

`E2(S)=(T^2-sum_j s_j^4)/2`
`     >=(T^2-s_1^2 T)/2=epsilon T^2/2`,                              (3.11)

if `epsilon>=1/8`, then `theta>=1/16` and

`boxed: ||p_Q||inf <=3e^(1/3)2^(1/6)G^(-1/6)<4.700G^(-1/6).`          (3.12)

### 3.3 Near-rank-one residual with a heavy row and heavy column

It remains only to consider `epsilon<1/8` when neither the row nor column energy marginals are diffuse. Choose i,j with

`||S_{i,*}||_2^2>T/2`, `||S_{*,j}||_2^2>T/2`.                        (3.13)

Write the top singular decomposition

`S=s_1 u v^T+E`, `Ev=0`, `E^T u=0`, `||E||_F^2=epsilon T`.            (3.14)

The heavy-row identity gives

`u_i^2>(1/2-epsilon)/(1-epsilon)`,                                   (3.15)

and likewise

`v_j^2>(1/2-epsilon)/(1-epsilon)`.                                   (3.16)

Because `E=(I-uu^T)E(I-vv^T)`,

`|E_ij|`
` <= ||E||op sqrt(1-u_i^2)sqrt(1-v_j^2)`
` <= sqrt(epsilon T)/(2(1-epsilon))`.                                (3.17)

The leading entry satisfies

`s_1|u_i v_j|`
` >= sqrt(T)(1/2-epsilon)/sqrt(1-epsilon)`
` > (3/8)sqrt(T)`.                                                    (3.18)

At `epsilon<=1/8`, (3.17) is at most `2/(7sqrt(2)) sqrt(T)`. Since

`3/8-2/(7sqrt(2)) >1/6`                                              (3.19)

(the equivalent integer check is `35^2>2*24^2`),

`boxed: |S_ij|>sqrt(T)/6.`                                           (3.20)

Adjoin this residual row and column to the physical anchor P. The resulting actual original-coordinate `3x3` cross block H has

`|det H|=D |S_ij|>sqrt(G)/6`.                                        (3.21)

Condition every other original coordinate. Three-dimensional bilinear Plancherel, with arbitrary same-bank phases retained, gives

`|phi_Q(t)| <= pi^(3/2)|det H|^(-1/2)|t|^(-3/2)`,                    (3.22)

and hence

`||p_Q||inf <=3|det H|^(-1/3)`
`            <3*6^(1/3)G^(-1/6).`                                   (3.23)

Combining all three cases proves the new theorem:

**QFORM-INVERTIBLE-SECONDANCHOR-ALL-STABLERANK-L1-v1.**  
For any invertible physical `2x2` original-coordinate cross anchor P with actual cross-Schur residual S and packet

`G=|det P|^2||S||_F^2>0`,

for arbitrary same-bank quadratic terms, outside couplings and affine terms,

`boxed:
 ||p_Q||inf <=3*6^(1/3)G^(-1/6)<5.452G^(-1/6).
`                                                                            (3.24)

Moreover `phi_Q in L1`, so the density has a continuous representative vanishing at infinity. No stable-rank assumption remains.

## 4. Scalar anchor: a new diffuse-E2 exit

The same lift with `r=1` gives, for a nonzero scalar physical pivot p and scalar cross-Schur residual S1,

`|phi_Q(t)| <= sqrt(pi)|p|^(-1/2)|t|^(-1/2)|J_S1(t)|`.              (4.1)

Put

`H=p^2E2(S1)`.                                                       (4.2)

If the second-volume row marginals of S1 are all at most `1/2`, use (2.8) with `k=2,q=1`:

`|J_S1(t)| <= e pi E2(S1)^(-1/4)|t|^(-1).`                           (4.3)

The same holds if the column marginals are diffuse, after transposition. Hence

`|phi_Q(t)| <= e pi^(3/2) H^(-1/4)|t|^(-3/2)`,                      (4.4)

and

`boxed:
 ||p_Q||inf <=3e^(2/3)H^(-1/6)<5.844H^(-1/6).
`                                                                            (4.5)

This pays arbitrary residual rank on the scalar-anchor branch whenever either side of the residual second-volume law is diffuse. It strictly extends the earlier exact-rank-two scalar-residual endpoint.

## 5. D' and D5 on the live physical block

The requested live Fourier routing can now be written without a pointwise scalar stationary-phase premise. Starting from a physical cross block B with `Z=E3(B)>0`:

- If the q=4/3 D' gate holds, (1.1) pays with `(9sqrt(3)e/2)Z^(-1/6)`.
- Independently, if `E5(B)>=2^(-10)Z^(5/3)`, the reviewed sharp D5 estimate pays with `5sqrt(2)e Z^(-1/6)` by (1.4).
- On the heavy-anchor/double-anchor route, the Hilbert-Schur lift pays every invertible second anchor by (3.24), regardless of residual stable rank; it also pays a rank-one second anchor on the diffuse residual-E2 subbranch by (4.5).

These are all unweighted L1 characteristic-function estimates; none is a false law-uniform pointwise estimate for a single quadratic coordinate.

## 6. Latest designated partner applied to actual inequalities

Apply `account03/B02` r33, equation (1.5). On its `G3>Z/864` alternative:

### Invertible second anchor

If the associated physical `2x2` anchor P is invertible, `G=G3`, so (3.24) gives

`boxed:
 ||p_Q||inf
 <3*6^(1/3)*864^(1/6) Z^(-1/6)
 <16.824 Z^(-1/6).
`                                                                            (6.1)

The previous high-stable-rank payment on this same packet was `<48.347 Z^(-1/6)` and required `sr(S)>=5/2`; (6.1) removes that hypothesis and improves the constant.

On the stronger packet `G>Z/24` from the preceding account02/B02 compiler, the same theorem gives

`boxed: ||p_Q||inf<9.259 Z^(-1/6).`                                  (6.2)

### Rank-one second anchor, diffuse residual second-volume

For a rank-one second anchor choose a genuinely nonzero scalar entry p. The established scalar-Schur identity supplies

`H=p^2E2(S1)>=G3`.                                                    (6.3)

If either the row or column second-volume marginals of S1 are all at most `1/2`, (4.5) and `G3>Z/864` give

`boxed:
 ||p_Q||inf
 <3e^(2/3)*864^(1/6) Z^(-1/6)
 <18.034 Z^(-1/6).
`                                                                            (6.4)

Thus the latest partner result has been used at an actual new inequality, not only cited.

## 7. Remaining first unpaid implication

The previous broad `QFORM-SECONDANCHOR-CRITICAL-STABLERANK-RECEIVER-v1` is now reduced further.

The entire invertible-second-anchor branch is paid, including the formerly critical `sr(S)<5/2` collar. On a rank-one second anchor, the new scalar theorem pays arbitrary residual rank whenever either side of the second-volume law has all marginals at most `1/2`; the preceding D6 theorem separately pays `sr(S1)>=5`.

The first unpaid branch is therefore

`QFORM-SINGULAR-SECONDANCHOR-CONCENTRATED-E2-OR-STRIP-v1`:

- rank-one second physical anchor with scalar residual `S1`, packet `p^2E2(S1)>0`, `sr(S1)<5`, and **both** a row and a column second-volume marginal exceeding `1/2`;
- the latest partner's literal `U/V` one-sided strip alternatives;
- the separately tracked literal overlap where the original fixed pivot shares a row or column with the heavy D' anchors.

The correct next mechanism is a grouped physical star/strip or mixed-hub receiver for that concentrated second-volume law. A reciprocal tiny-minor selection or deletion of small matrix tails is not source-valid for arbitrary unbounded product inputs.

## 8. Corrections and checks

All relevant correction boundaries are preserved: no uniform scalar quadratic pointwise decay, no post-rotation or post-Schur independence, no arbitrary conditional-density cap, no arbitrary-joint coarea estimate, no pre-Schur/post-Schur rank transfer, no inference from aggregate cross volume to a uniformly good isolated minor, and no small-matrix-tail deletion for arbitrary unbounded product inputs.

The near-rank-one heavy-row/heavy-column estimate was checked with deterministic seed `160824` on 5000 generated matrices satisfying the exact SVD orthogonality used in (3.14). There were 970 cases with both heavy marginals; the smallest observed `|S_ij|^2/T` was `0.19049665495078438`, versus the proved threshold `1/36`. This is diagnostic only; equations (3.15)-(3.20) are the proof. The attached exact constant check records `STATUS PASS`.

No source-valid counterexample to the target-wide unweighted `int_R |phi_Q(t)|dt` criterion was found. That stronger criterion remains OPEN / not refuted. The unrestricted QFORM bounded-density conjecture remains OPEN.
