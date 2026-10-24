SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-23T04:44:12Z.
attacking: QFORM-THREE-ARM-SAMESIDE-CURVATURE-COAREA-v1 — keep genuine same-side quadratic curvature inside independent original-coordinate smoothing packets instead of discarding it before coarea.

# B05 r21 — an L^{3/2} two-coordinate quadratic packet and a three-packet same-side-curvature closure

Programme: QFORM-DENSITY-3EIG-20260922.  
Status: new scoped supporting theorem proved; full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.  
Continuity: proved for the scoped three-packet theorem below; not proved for full QFORM.  
Execution context: WITHOUT_VERIFIED_BRAIN.

## 1. Source pins and correction state

Fresh brain control was read from `yspennstate/math-research-brain@4e09083f3b4231564e441e862e5c5c5abbfa1676`; OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only. The live correction stream still forbids arbitrary-joint rank-three coarea, normalized scalar-fiber suprema, pointwise van-der-Corput decay, and treating small coefficients as small random errors.

The main analytic dependency used below is the completed two-coordinate logarithmic coarea envelope

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`,

which for an invertible indefinite physical pair `B` with `D=|det B|` and `kappa=sigma_min(B)` gives, for every cutoff `r>0`,

`p_F(t) <= 2 sqrt(2)/r + D^(-1/2) log_+(2 r^2/(kappa |t-t0|))`.

The designated partner `account04/B05` now has a completed current-QFORM theorem. I read its full immutable proof at

`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f:proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260923T041255Z-account04-B05-dominant-slope-r2/REPORT.md`.

Its exact-slope theorem states `||p_Q||_infinity < 51.6 (mu m_*)^(-1/3)` in its stated normal form.

## 2. One-dimensional quadratic L^{3/2} lemma

Let `X` have a probability density at most one and let

`Y=d(X-h)^2+c`, `d!=0`.

Then `Y` has a density `p` satisfying

`||p||_(3/2) <= 4^(2/3) |d|^(-1/3)`.                 (2.1)

Proof. By reflection it is enough to take `d>0`. The two inverse branches give

`p(c+u) <= (d u)^(-1/2)` for `u>0`.

Also `int p=1`. For every `R>0`,

`int p^(3/2)
 <= int_0^R (d u)^(-3/4) du + (d R)^(-1/4) int_(u>=R) p(c+u) du
 <= 4 d^(-3/4) R^(1/4) + d^(-1/4) R^(-1/4)`.

Set `R=d/16`. The two terms are each `2 d^(-1/2)`, hence

`int p^(3/2) <= 4 d^(-1/2)`.

Taking the power `2/3` proves (2.1). Arbitrary linear terms are included by completing the square. QED.

## 3. Main local theorem: every physical two-coordinate quadratic packet has a uniform L^{3/2} density

### Theorem QFORM-PHYSICAL-PAIR-L32-v1

Let `X,Y` be independent real random variables with probability densities at most one. Put

`F=a X^2 + 2 b X Y + c Y^2 + alpha X + beta Y + gamma`

and

`m=max(|a|,|b|,|c|)>0`.

Then `F` has an absolutely continuous law and

`boxed( ||p_F||_(3/2) <= 20 m^(-1/3) ).`             (3.1)

No sign, moment, support, connectedness, centering, or smoothness assumption is used.

### Proof

There are two cases.

#### Case A: one physical diagonal is not small

Suppose `max(|a|,|c|)>=m/2`. Without loss, `|a|>=m/2`. Condition on the original coordinate `Y`. The conditional polynomial in `X` has quadratic coefficient exactly `a`; every value of `Y` changes only its linear and constant coefficients. By (2.1), each conditional density has `L^(3/2)` norm at most

`4^(2/3) |a|^(-1/3) <= 2^(5/3) m^(-1/3) < 20 m^(-1/3)`.

Minkowski's integral inequality preserves this bound after averaging over `Y`.

#### Case B: the off-diagonal coefficient dominates

Now `|a|,|c|<m/2`, so `m=|b|`. Let

`B=[[a,b],[b,c]]`.

Then `B` is invertible indefinite and

`D=|det B|=b^2-ac >= 3m^2/4`.                         (3.2)

The operator norm obeys

`||B||_op <= max(|a|+|b|,|b|+|c|) < 3m/2`,

hence, because the product of the two singular values equals `D`,

`kappa=sigma_min(B)=D/||B||_op >= m/2`.              (3.3)

Apply the completed pair-log envelope with cutoff `r=m`. If `t0` is its critical value,

`p_F(t)
 <= (1/m)[ 2 sqrt(2) + (2/sqrt(3)) log_+(4m/|t-t0|) ]`.     (3.4)

Indeed (3.2) gives `D^(-1/2)<=2/(sqrt(3)m)` and (3.3) gives `2m^2/kappa<=4m`.

Rescale

`q(s)=m p_F(t0+m s)`.

Then `q` is a probability density and

`q(s) <= A + B0 log_+(4/|s|)`,

where `A=2sqrt(2)` and `B0=2/sqrt(3)`. On `|s|>=4`, `q<=A`, so

`int_(|s|>=4) q^(3/2) <= sqrt(A)`.

On `|s|<4`, use `(x+y)^(3/2)<=sqrt(2)(x^(3/2)+y^(3/2))` and

`int_0^1 (-log u)^(3/2) du = Gamma(5/2)`

to obtain

`int_(|s|<4) q^(3/2)
 <= sqrt(2)[8 A^(3/2)+8 B0^(3/2) Gamma(5/2)]`.        (3.5)

The right side of (3.5), plus `sqrt(A)`, is less than `75`: for example `sqrt(2)<1.415`, `A<2.83`, `sqrt(A)<1.683`, `B0<1.155`, `sqrt(B0)<1.075`, and `Gamma(5/2)=3sqrt(pi)/4<1.33` give a total below `74.4`. Since `75<20^(3/2)`,

`||q||_(3/2)<20`.

Undoing the scaling gives

`||p_F||_(3/2)=m^(-1/3)||q||_(3/2)<20m^(-1/3)`.

This proves (3.1). QED.

## 4. Three disjoint packets: same-side curvature can be kept instead of discarded

### Theorem QFORM-THREE-PHYSICAL-PAIR-CURVATURE-v1

Let the original independent coordinates be split into three disjoint two-coordinate packets `P_1,P_2,P_3` and an arbitrary remainder `Z`. Suppose that, after ordering coordinates, the quadratic matrix on the six live packet coordinates is block diagonal,

`M_active = diag(M_1,M_2,M_3)`,

with symmetric `2x2` blocks

`M_j=[[a_j,b_j],[b_j,c_j]]`,

and set

`m_j=max(|a_j|,|b_j|,|c_j|)>0`.

All coefficients on `Z` and all couplings from `Z` into the three packets are arbitrary. Then the full quadratic form has an essentially bounded density satisfying

`boxed( ||p_Q||_infinity <= 20^3 (m_1 m_2 m_3)^(-1/3) )`

that is,

`boxed( ||p_Q||_infinity <= 8000 (m_1 m_2 m_3)^(-1/3) ).`   (4.1)

Moreover the density admits a continuous representative.

### Proof

Condition on all original coordinates in `Z`. Product independence is therefore genuine. The three two-coordinate packets remain mutually independent; the conditioned outside variables contribute only deterministic affine terms to each packet and an overall scalar shift. Denote their scalar quadratic outputs by `F_1,F_2,F_3`.

By Theorem (3.1), uniformly in the conditioned value of `Z`,

`||p_(F_j|Z)||_(3/2) <=20 m_j^(-1/3)`.

The conditional density of the active sum is the convolution of these three densities. Three-factor Young gives

`||p_(F_1+F_2+F_3|Z)||_infinity
 <= product_j ||p_(F_j|Z)||_(3/2)
 <=8000 (m_1m_2m_3)^(-1/3)`

because `3*(2/3)=2`, exactly the three-factor endpoint for an `L^infinity` convolution. Averaging in `Z` proves (4.1).

For each conditioned `Z`, convolution of `L^(3/2),L^(3/2),L^(3/2)` densities gives a continuous function: convolve the first two into `L^3`, then use the standard `L^3 * L^(3/2) subset C_0` translation-continuity argument. The conditional densities are uniformly bounded by (4.1), so dominated convergence in `Z` yields continuity of the averaged density. QED.

## 5. What this closes in the r20 same-side-curvature campaign

The preceding r20 three-arm Frobenius theorem handled an affine smoothing side and allowed arbitrary curvature only on the coefficient side. The new theorem proves that same-side curvature itself is not the obstruction when the three curvature resources can be routed into three disjoint physical packets with no live inter-packet quadratic coupling: every arbitrary quadratic-plus-linear packet is paid in `L^(3/2)`, and the three independent packets close at the exact Young endpoint.

Thus the first unpaid factor is more precise than `same-side curvature` generically:

`QFORM-INTERPACKET-CURVATURE-COAREA-v1` — retain the three `L^(3/2)`/coarea resources when the six active original coordinates also carry quadratic couplings BETWEEN the three packets, or replace the three physical packets by diffuse aggregate banks without selecting a largest entry.

The new theorem does not solve that inter-packet/diffuse problem and does not imply full QFORM.

## 6. Required partner use: account04/B05 applied to an actual inequality

The completed account04/B05 r2 theorem is now available and was read in full. In the account01/B05 r26 packet quoted and used by that proof, if the ratio residual is exactly zero, the selected exact-slope packet obeys

`m_G >= 3h/20`.

At that endpoint `m_*>=m_G`, so the partner theorem gives the concrete full-line bound

`||p_Q||_infinity
 < 51.6 (mu m_*)^(-1/3)
 <= 51.6 (20/(3 mu h))^(1/3)`.                       (6.1)

This is an actual application of the designated partner result, not a citation-only mention. It closes the exact-slope endpoint of that slab. For nonzero ratio residual the partner correctly records the dependent two-dimensional product projection `(S,R)` as unpaid; no conditioning on `R` is used here.

If a configuration simultaneously satisfies the partner exact-slope hypothesis and the three-disjoint-packet hypothesis above, both estimates are valid and one may take

`||p_Q||_infinity <= min{51.6(mu m_*)^(-1/3), 8000(m_1m_2m_3)^(-1/3)}`.  (6.2)

## 7. Scope, falsification checks, and next step

- No rotated eigen-coordinate is declared independent.
- No moment or support-size estimate is used.
- The pair-log envelope is used only for an original physical pair of independent coordinates.
- The theorem explicitly permits arbitrary affine terms from conditioning outside coordinates.
- It does NOT permit live quadratic couplings between the three selected active packets; that is the stated remaining debt.
- It does NOT replace a diffuse Frobenius bank by one large entry.
- Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.
- Full continuity remains OPEN, although continuity is proved in the scoped three-packet theorem.

A narrow privacy review was performed on the exact write payload: it contains only mathematical statements, public repository coordinates already present in the programme, and the logical account/slot/run identifiers required by protocol; no token, scheduler ID, signed download URL, machine path, personal source excerpt, or external account credential is present. The repository's dedicated privacy scanner was not exposed in this execution environment.

Next B05 target: prove `QFORM-INTERPACKET-CURVATURE-COAREA-v1`, preferably by an endpoint `L^(3/2)` estimate stable under adding the inter-packet bilinear couplings, or prove a sharp obstruction showing which aggregate cross norm must be retained jointly before Young/coarea inversion.
