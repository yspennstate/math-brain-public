# fleet01/B01 — quarter-Riesz splice and ridge-threshold collapse

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T160919Z-b01-qform-auto11d`  
**Assignment:** Oscillatory replacement  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Exact target and correction discipline

The full target remains: for every dimension, every independent real coordinates with probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has an essentially bounded density with one universal finite constant, or give a valid counterexample. Continuity is a separate desired conclusion.

The live correction `QFORM-POINTWISE-DECAY-FALSE` is retained. A cap-one scalar density can be placed on phase-aligned fragmented support so that `|E exp(isX^2)|` is arbitrarily close to one at a prescribed large frequency. Nothing below uses a law-uniform pointwise scalar Fresnel bound. The mechanism is instead a weighted, integrated Fourier estimate for a **Schur critical-value variable**.

## 2. Source-pinned dependencies actually used

1. **Physical indefinite two-pivot quarter-kernel.** fleet03/B19, canonical report
   `yspennstate/math-open-problems@0e6d1715955458010d43193cab3dafc293c0e28c`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260922T154500Z-fleet03-B19-QFORM-r13/REPORT.md`.
   For a physical pivot block
   `B0=[[a,c],[c,-b]]`, `a,b>=m>0`, `Delta=ab+c^2`, with exact outside Schur complement `S`, the conditional mixture satisfies

   `p_Q(x) <= 2 Delta^(-1/4) m^(-1/4) E |x-kappa(Z)|^(-1/4)`,  `kappa(Z)=Z^T S Z`.

   In its proof-assembly branch one also has `m=7/8`, `Delta>=49/64`, and, if no physical Schur diagonal pays, an original-coordinate cut with `s_1(S[I,J])>27/2240`.

2. **Free-regularizer ridge characteristic envelope.** Interactive report
   `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, path
   `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.
   For an original-coordinate cross block `R`, ridge scale `gamma>0`, `q in [1,2]`,

   `K_gamma=RR^T(gamma^2 I+RR^T)^(-1)`, `theta=tr K_gamma`, `D=det(I+RR^T/gamma^2)`,

   and `max_i (K_gamma)_ii <= q/2`, its Section 5 proves the pointwise envelope

   `|phi_kappa(t)| <= D^(-1/(4q)) [L_q/(2 gamma |t|)]^(theta/(2q))`,

   where `L_q=pi e sqrt(2/q)`. Importantly this envelope is proved before the report imposes its stronger ordinary-Fourier condition `theta>2q`.

3. **Assigned partner fleet02/B01.** r22 canonical report
   `yspennstate/math-open-problems@08e91d2cd50db663646e7c25983c421ccaa78c7c`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260922T150052Z-fleet02-B01-qform-r22/REPORT.md`.
   Its rank-two cross-bank plus transverse-curvature theorem gives the residual density cap

   `M_R <= 1/pi + 4 sqrt(2) pi^(1/3) Delta_2^(-1/2) max(3^(1/4), |a_2|^(-1/4))`.

The ridge extension is a supplied complete supporting derivation but was still awaiting its own full independent review at the source handoff; I do not relabel that provenance.

## 3. Exact quarter-Riesz identity

For `0<alpha<1`, with Fourier convention `hat f(t)=int exp(itx) f(x) dx`,

`int_R exp(-itx) |x|^(-alpha) dx = 2 Gamma(1-alpha) sin(pi alpha/2) |t|^(alpha-1)`.

Therefore, whenever the right-hand side is absolutely integrable against a characteristic function,

`E |x-R|^(-alpha)
 <= c_alpha int_R |t|^(alpha-1) |phi_R(t)| dt`,

where

`c_alpha = Gamma(1-alpha) sin(pi alpha/2)/pi`.

For `alpha=1/4`,

`c_(1/4)=Gamma(3/4) sin(pi/8)/pi
        =0.14927036108294766127...`.

Combining this with the fleet03/B19 conditional inequality gives

`||p_Q||_infinity
 <= 2 c_(1/4) Delta^(-1/4)m^(-1/4)
    int_R |t|^(-3/4)|phi_kappa(t)|dt.`                         (3.1)

Thus an ordinary `L^1` characteristic-function bound is unnecessarily strong here: the physical indefinite pivot pair has already contributed three quarters of the integrability threshold.

## 4. Main theorem — ridge threshold falls from `theta>2q` to `theta>q/2`

### Theorem 4.1 — `QFORM-QUARTER-RIESZ-RIDGE-SPLICE-v1`

In the setup of Section 2(1), let `R=S[I,J]` be any cross block of the exact outside Schur complement on disjoint sets of original outside coordinates. Fix `gamma>0`, `q in [1,2]`, and define

`K_gamma=RR^T(gamma^2 I+RR^T)^(-1)`,
`theta=tr K_gamma`,
`D=det(I+RR^T/gamma^2)`.

Assume

`max_i (K_gamma)_ii <= q/2`,                                      (4.1)

and only

`theta > q/2`.                                                     (4.2)

Then `Q` has an essentially bounded density and

`||p_Q||_infinity
 <= 16 c_(1/4) Delta^(-1/4)m^(-1/4)
    [pi e/(gamma sqrt(2q))]^(1/4)
    D^(-1/(8theta))
    [2theta/(2theta-q)].`                                         (4.3)

No continuity assertion is made by this theorem.

### Proof

The ridge source proves under (4.1), without needing its later `theta>2q` density hypothesis,

`|phi_kappa(t)| <= min(1,(t_0/|t|)^beta)`,

with

`beta=theta/(2q)`,
`t_0=[L_q/(2gamma)]D^(-1/(2theta))`,
`L_q=pi e sqrt(2/q)`.

Because the Riesz weight in (3.1) is `|t|^(-3/4)`, its tail is integrable precisely when `beta>1/4`, which is exactly (4.2). Direct integration gives

`J:=int_R |t|^(-3/4) min(1,(t_0/|t|)^beta) dt`

`=2[ int_0^(t_0) t^(-3/4)dt
    +t_0^beta int_(t_0)^infinity t^(-3/4-beta)dt ]`

`=8 t_0^(1/4) [4beta/(4beta-1)]`

`=8 t_0^(1/4) [2theta/(2theta-q)].`                               (4.4)

Substitute (4.4) into (3.1), and use

`[L_q/(2gamma)]^(1/4)=[pi e/(gamma sqrt(2q))]^(1/4)`

and `t_0^(1/4)=[L_q/(2gamma)]^(1/4)D^(-1/(8theta))`. This is (4.3). QED.

### Interpretation

The ordinary ridge theorem needs effective ridge dimension `theta>2q` because it pays the whole `|t|^{-1}` integrability threshold itself. The physical two-pivot quarter-kernel changes the remaining Fourier weight to `|t|^{-3/4}`, so the residual cross bank needs only one quarter of a Fourier power. The exact threshold becomes `theta>q/2`, a factor-four reduction.

This is an averaged-frequency replacement, not a repaired scalar pointwise van-der-Corput statement.

## 5. Clean diffuse one-direction corollary and application to the B19 residual cut

Take `q=1`. Suppose a residual cross block has largest singular value `sigma>0`, choose

`gamma=sigma/sqrt(3)`,

and suppose its ridge operator at this scale obeys

`max_i (K_gamma)_ii <= 1/2`.                                     (5.1)

Then the top singular direction alone gives

`theta >= sigma^2/(gamma^2+sigma^2)=3/4`.

Ignoring the favorable determinant factor `D^(-1/(8theta))<=1` and using that `2theta/(2theta-1)` decreases for `theta>1/2`, Theorem 4.1 gives

`||p_Q||_infinity
 <= C_diff Delta^(-1/4)m^(-1/4)sigma^(-1/4)`,                    (5.2)

with

`C_diff
 =16 c_(1/4) [pi e sqrt(3)/sqrt(2)]^(1/4) *3
 =12.885085858602194...`.

Now apply the exact fleet03/B19 branch. There `m=7/8`, `Delta>=49/64`, and the forced Schur cross bank has

`sigma=s_1(S[I,J])>27/2240`.

Therefore, whenever that forced bank satisfies the single scale condition (5.1),

`||p_Q||_infinity < 42.984.`                                    (5.3)

So the previously unpaid Schur-cross branch is now closed whenever its fixed nonzero cross direction is **ridge-diffuse at one physical scale**. The remaining obstruction has become a high-ridge-leverage / localized cross direction, not a lack of Fourier decay.

For an exact rank-one residual cross block `R=sigma u v^T`, condition (5.1) at `gamma=sigma/sqrt(3)` is simply `(3/4) max_i u_i^2<=1/2`, i.e.

`max_i u_i^2 <= 2/3`.

Thus every exact rank-one Schur cross direction whose left singular vector has coordinate leverage at most `2/3` is paid by (5.2). Interchanging the two sides gives the analogous right-leverage criterion.

## 6. Assigned partner result applied to an actual new inequality

The fleet02/B01 r22 theorem supplies a bounded density for a residual quadratic form `R0` whenever it contains a three-coordinate rank-two cross bank with nonzero transverse curvature:

`M_R := ||p_(R0)||_infinity
 <= 1/pi + 4 sqrt(2) pi^(1/3) Delta_2^(-1/2)
       max(3^(1/4),|a_2|^(-1/4)).`                              (6.1)

For any probability density `p<=M`, symmetric decreasing rearrangement (or the one-dimensional bathtub principle) gives exactly

`sup_x int |x-y|^(-1/4)p(y)dy
 <= M int_(-1/(2M))^(1/(2M)) |u|^(-1/4)du
 = [2^(9/4)/3] M^(1/4).`                                       (6.2)

Insert (6.2) into the physical pivot inequality from fleet03/B19. This produces the explicit nested `2+3`-gate bound

`||p_Q||_infinity
 <= [2^(13/4)/3] Delta^(-1/4)m^(-1/4) M_R^(1/4),`              (6.3)

where

`2^(13/4)/3 = 3.1712189733405895...`.

Combining (6.1)-(6.3) is a literal application of the assigned fleet02/B01 theorem to a new inequality; no post-rotation independence is introduced. It is useful when the Schur residual's own rank-two/transverse gate is quantitatively controlled.

## 7. What is and is not closed

**Proved in this run:**

- the exact weighted quarter-Riesz splice (3.1);
- the ridge criterion `theta>q/2` with explicit constant (4.3);
- the one-scale diffuse cross-direction corollary (5.2);
- the `<42.984` closure of the fleet03/B19 forced-Schur-cross branch under ridge leverage `<=1/2` at `gamma=s_1/sqrt(3)`;
- the explicit partner-lift inequality (6.3).

**Not proved:** the full three-large-eigenvalue conjecture. In the B19 one-effective-direction residue the first remaining structural/analytic obstruction is now a forced Schur cross bank whose useful singular direction is highly localized at every scale that keeps `theta>q/2`, or a quantitatively near-localized rank-one perturbation. A universal proof still has to show that such a localized endpoint forces one of the already-paid physical diagonal / finite-dimensional pivot / separable / additional-cross-direction branches, or control it directly.

Continuity of the full density is **not** obtained from Theorem 4.1 alone. It proves existence of an essentially bounded density via conditional densities and the Riesz-potential estimate. Additional smoothing would be needed for a continuous representative in this branch.

## 8. Verification

`checks.py` and `check_results.json` in this run directory reproduce:

- `c_(1/4)=0.14927036108294766...`;
- the exact weighted-envelope integral at three test exponents;
- `C_diff=12.885085858602194...`;
- the B19 branch constant `42.983555904027955...`;
- the partner-lift coefficient `3.1712189733405895...`.

The check output ends `STATUS=PASS`. Numerical quadrature is only a check of the closed-form identities; the proof above is analytic.

## 9. Next mathematical attempt

Attack the localized ridge endpoint of the B19 Schur cut. The concrete target is: from `s_1(S[I,J])>27/2240` and ridge leverage `>1/2` at `gamma=s_1/sqrt(3)`, extract a physical outside coordinate carrying a fixed fraction of the cross direction and show that either (i) a physical Schur diagonal is forced above the already-paid threshold, (ii) a second cross direction appears quantitatively, or (iii) the residual reduces to a product-preserving low-dimensional star/hyperbolic form that can be controlled by an endpoint weighted Fourier estimate. This is narrower than the previous generic heavy/diffuse dichotomy.
