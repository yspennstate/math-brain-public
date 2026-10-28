# B03 decoupled-time report: aggregate cross-minors before reciprocal payment

Run: `20260922T225606Z-account03-B03-QFORM-r21`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: **Decoupled time integral**  
Status: **SUPPORTING THEOREM PROVED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and mechanism change

The owner target is unchanged: for independent real coordinates with densities at most one and any real symmetric `A` with at least three eigenvalues of magnitude at least one, prove a universal essential-density bound for `Q=X^T A X`, or give a valid counterexample. Continuity is tracked separately.

This run changes the B03 mechanism from paying a reciprocal cost for one physical pair (r20b) to **aggregating every k-by-k minor of one residual original-coordinate cross block before inversion**. The aggregation is the elementary symmetric polynomial

`E_k(B):=e_k(BB^T)=sum_{|I|=|J|=k} det(B[I,J])^2`.

The new result is useful already for `k=3`, where it strictly strengthens B03 r17: it replaces a lower bound on three individual cross singular values by the total third-order determinant-bank mass `E_3`, and improves the explicit constant from `17.426` to `9.841` in the equal-singular-value comparison.

The proof keeps independence only in the original coordinates. It does not use the false law-uniform pointwise quadratic-phase decay, false conditional sum/difference cap, arbitrary-joint coarea, or single-Schur extraction claims.

## 2. Source theorem consumed

Use the complete regularized-determinant theorem

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

at

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

For any quadratic form `R(W)` in independent original coordinates with cap-one densities, any disjoint original-coordinate sets `I,J`, and cross block `B=S[I,J]` of its quadratic coefficient matrix, that theorem proves, with no leverage hypothesis at `q=2`,

`|eta_R(t)| <= det(I + c t^2 BB^T)^(-1/8)`,              (2.1)

where

`c=4/(pi^2 e^2)`.                                         (2.2)

Its proof is itself an independent-copy/Cauchy--Schwarz argument. The relevant difference variables remain generated from pairs of original independent coordinates; no independence between a coordinate sum and difference is introduced. Arbitrary self-quadratic phases and outside couplings are retained.

## 3. Determinant-bank identity

Let `s_1^2,...,s_m^2` be the eigenvalues of `BB^T`, with zeros included. For each integer `k>=1`,

`E_k(B)=e_k(BB^T)`.

By the principal-minor formula for `e_k` followed by Cauchy--Binet,

`E_k(B)`
` = sum_{|I0|=k} det((BB^T)[I0,I0])`
` = sum_{|I0|=|J0|=k} det(B[I0,J0])^2`.                    (3.1)

Also

`det(I+c t^2 BB^T)`
` = sum_{j>=0} c^j t^(2j) E_j(B)`
` >= 1 + c^k E_k(B) t^(2k)`.                              (3.2)

Therefore (2.1) implies

`|eta_R(t)| <= (1+a |t|^(2k))^(-1/8)`,                    (3.3)

where

`a=c^k E_k(B)`.                                           (3.4)

The important point is that (3.1) aggregates the entire physical determinant bank before any reciprocal power is paid.

## 4. Main theorem: aggregate half-Riesz transducer

### Theorem `QFORM-PIVOT-EK-AGGREGATE-HALF-RIESZ-v1`

Let `Z` be one original coordinate and `W` the remaining original coordinates. Suppose `A_ZZ=d!=0`. Completing the physical scalar square gives

`Q=d (Z+h(W))^2 + R(W)`.                                  (4.1)

Assume the Schur residual `R` has disjoint original-coordinate sets `I,J` whose cross block `B` satisfies `E_k(B)>0` for some integer `k>=3`. Then `Q` has an essentially bounded density and

`||p_Q||_infinity`
` <= C_k |d|^(-1/2) E_k(B)^(-1/(4k))`,                    (4.2)

where

`C_k = [sqrt(e)/(2k)]`
`      BETA(1/(4k),(k-2)/(8k))`.                          (4.3)

Consequently every interval `L` satisfies

`P(Q in L) <= C_k |d|^(-1/2) E_k(B)^(-1/(4k)) |L|`.       (4.4)

The estimate is homogeneous: under `A -> rho A`, `d -> rho d` and `E_k -> rho^(2k)E_k`, so the right side scales by `|rho|^(-1)` exactly as a density should.

### Proof

For fixed `W=w`, the map in the original coordinate `z` is a translated square. Since `f_Z<=1`, its conditional output density obeys

`p_{Q|W=w}(y) <= |d|^(-1/2)|y-R(w)|^(-1/2)`.             (4.5)

Indeed there are at most two roots, each with derivative magnitude `2 sqrt(|d| |y-R(w)|)`.

Average (4.5):

`p_Q(y) <= |d|^(-1/2) E |y-R|^(-1/2)`.                   (4.6)

For `k>=3`, (3.3) makes the half-Riesz Fourier integral absolutely convergent. With the convention `eta_R(t)=E exp(itR)`, Gaussian regularization of the classical transform of `|x|^(-1/2)` gives

`E|y-R|^(-1/2)`
` <= (2pi)^(-1/2) int_R |t|^(-1/2)|eta_R(t)| dt.          (4.7)

Insert (3.3). For `a>0`, the substitution `u=a t^(2k)` gives

`int_R |t|^(-1/2)(1+a|t|^(2k))^(-1/8) dt`
` = (1/k) a^(-1/(4k))`
`   BETA(1/(4k),1/8-1/(4k)).                              (4.8)

The beta integral is finite exactly when `k>2`. Since

`a^(-1/(4k))=c^(-1/4)E_k^(-1/(4k))`
`             =sqrt(pi e/2) E_k^(-1/(4k))`,               (4.9)

multiplying (4.8) by `(2pi)^(-1/2)` gives precisely (4.3). Combining (4.6)--(4.9) proves (4.2)--(4.4). QED.

## 5. The first closing order is exactly k=3

For `k=2`, the right side of (4.8) has the endpoint parameter

`1/8-1/(4k)=0`,

so the integral diverges logarithmically. Thus this direct regularized-determinant plus half-Riesz mechanism closes **exactly starting at third-order cross-minor mass**. This is a mechanism threshold, not a rank-two counterexample to QFORM.

At `k=3`,

`C_3 = [sqrt(e)/6] BETA(1/12,1/24)`
`    = 9.8406558649220185...`.                             (5.1)

Hence

`boxed: ||p_Q||_infinity <= 9.841 |d|^(-1/2) E_3(B)^(-1/12)`. (5.2)

Equivalently,

`||p_Q||_infinity <= 9.841 [|d|^6 E_3(B)]^(-1/12)`.       (5.3)

If `B` has three singular values at least `sigma`, then `E_3(B)>=sigma^6`, so

`||p_Q||_infinity <= 9.841 |d|^(-1/2)sigma^(-1/2)`.       (5.4)

B03 r17 obtained the same homogeneity with constant `17.4254229...` under that stronger three-individual-singular-values hypothesis. Thus (5.2) both aggregates and improves that branch.

## 6. Pure independent-copy L2/collision consequence

The same determinant bank gives a direct result for the assigned `|phi|^2` mechanism. Squaring (3.3),

`|eta_R(t)|^2 <= (1+a|t|^(2k))^(-1/4)`.                  (6.1)

For `k>=3`, Plancherel therefore gives an `L^2` density for `R` and

`||p_R||_2^2`
` <= [e/(4k)] BETA(1/(2k),(k-2)/(4k))`
`       E_k(B)^(-1/(2k)).`                                (6.2)

Proof: the exact beta integral is

`int_R (1+a|t|^(2k))^(-1/4)dt`
` = (1/k)a^(-1/(2k)) BETA(1/(2k),1/4-1/(2k)),`            (6.3)

then use `a=c^kE_k`, `c^(-1/2)=pi e/2`, and the Plancherel factor `1/(2pi)`.

At `k=3`,

`||p_R||_2^2`
` <= [e/12] BETA(1/6,1/12) E_3(B)^(-1/6)`
` = 3.9992289169513335... E_3(B)^(-1/6).`                 (6.4)

This is a genuine independent-copy collision certificate: if `R'` is an independent copy, then its difference density at zero is `||p_R||_2^2`.

## 7. Designated partner account04/B03 applied to an actual inequality

The designated partner handoff is


canonical mathematics `yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`.

Its advertised `QFORM-COLLISION-L2-COMPILER-v1` remains false as previously corrected: the stated Cauchy--Schwarz step loses a time weight and the coefficient homogeneity is wrong. That claim is not revived.

The completed handoff also contains the valid collision implication

`P(|Y-Y'|<=epsilon) <= 2 epsilon ||p_Y||_2^2`.            (7.1)

Applying (7.1) to the new aggregate bound (6.2) gives the actual partner-consumed inequality

`P(|R-R'|<=epsilon)`
` <= [e/(2k)] BETA(1/(2k),(k-2)/(4k))`
`      E_k(B)^(-1/(2k)) epsilon`.                          (7.2)

At `k=3`,

`boxed: P(|R-R'|<=epsilon)`
` <= 7.998457833902667 E_3(B)^(-1/6) epsilon`.             (7.3)

Thus the partner's valid collision step is used on a new determinant-bank `L^2` certificate, while its refuted compiler stays excluded.

## 8. Relation to the full target

This result pays an analytically important aggregate branch. It no longer requires selecting one third-order physical minor and paying its reciprocal; all third-order minors of one residual cross cut contribute through the positive sum `E_3(B)`.

The unrestricted three-large-eigenvalue conjecture is **not** closed. The remaining structural implication is:

> From the bare hypothesis that `A` has at least three eigenvalues of magnitude at least one, prove an exhaustive product-preserving alternative that either enters an already-paid diffuse/ridge/hyperbolic/localized branch or produces a nonzero original-coordinate scalar pivot `d` and a Schur-residual original-coordinate cut `B` with a dimension-free lower bound on the homogeneous aggregate certificate `|d|^6 E_3(B)`.

Known corrections rule out simply asserting one good local triple, one good Schur rank-two block, or one rank-three cross cut. The new theorem is useful precisely because it asks for a **bank total** rather than one determinant atom.

Continuity is **not proved** by the present square-pivot argument; only essential boundedness and linear interval scaling are claimed.

## 9. Numerical/algebraic verification

A checker accompanies this report. It verifies:

1. the Cauchy--Binet identity `E_k(B)=sum det(B[I,J])^2` on random matrices;
2. the beta constants in (5.1), (6.4), and (7.3);
3. the scalar homogeneity of (4.2);
4. that the `k=2` beta endpoint diverges and `k=3` is finite.

The checker is finite verification only; the analytic proof above is the mathematical result.

## 10. Source/control record

Start control read: `yspennstate/math-research-brain@0de937a66fc7877561f4a9946f6272e0dc8d0e24`, owner revision `2026-09-22.15`. Pre-publication main refresh observed `38c01bd0633aa4ae280f6f8461ba65a5a8f1bf25`, still QFORM-only. Live corrections consumed include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, the arbitrary-joint coarea correction, and the conditional projection positive-moment correction.

Repository transport was authenticated, but no separate native learned-memory receiver was verified; status remains `WITHOUT_VERIFIED_BRAIN`.
