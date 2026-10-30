SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B10, 2026-09-24T07:52:28Z.
attacking: the diffuse near-coloop two-sheet survivor after the newest fleet02/B10 hyperbolic-Fresnel identity; retain the mixed `(xi,q)` phase and quantify exactly what smoothing it buys before the final `V^2` Fresnel step.

# fleet01/B10 — mixed-phase collapse to a one-dimensional dynamic Fresnel amplitude

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: rank-three coupled case  
Status: `NEW_PHASE_RETAINING_L2_THEOREM / PARTNER_RESULT_APPLIED / NEW_ONE_DIMENSIONAL_BARRIER / FULL_EXACT_RANK3_OPEN / FULL_QFORM_OPEN`.

## 1. Exact target and live source boundary

The owner target is unchanged: for arbitrary independent real source coordinates with probability densities bounded by one, and a real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential-supremum bound for the density of the quadratic form, or give an admissible counterexample. No moment, support, log-concavity, Gaussian, post-rotation-independence, or compactness hypothesis is used below.

Fresh control and the live correction corpus were read before this report. In particular, the following failures are respected: law-uniform pointwise quadratic van-der-Corput decay is false for fragmented cap-one laws; bounded finite-dimensional projection densities do not by themselves control the indefinite quadratic pushforward; conditional projection caps cannot be substituted for independence; and the full absolute hyperbolic-Fresnel receiver below is known to lose a logarithm.

The designated partner result actually consumed is the newest completed `fleet02/B10` report

`yspennstate/math-open-problems@fe4042fe31234cbe45ed47a6b1546fa70f687b68`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260924T064844Z-fleet02-B10-QFORM-r11/REPORT.md`.

It gives, for the exact near-coloop harmonic survivor

`Q = 2(s H + a Z)L + V^2`,                                         (1.1)

where `s=sqrt(c)`, `a=sqrt(rho)`, `c=1-rho`, `0<rho<1/64`, `H` is one ORIGINAL physical coordinate independent of the full leaf vector, and `(Z,L,V)` are three orthogonal linear forms of the same ORIGINAL independent leaf bank, the exact phase representation

`phi_Q(t)=omega_t/(8*pi^(3/2)*|t|^(3/2)) K_rho(t)`,                 (1.2)

`K_rho(t)=int exp(-i xi q/(2t)-i w^2/(4t))
                 psi_H(s xi) Phi(a xi,q,w) dxi dq dw`,              (1.3)

with `|omega_t|=1` and

`Phi(p,q,w)=E exp(i(pZ+qL+wV))
           =prod_j psi_j(p z_j+q r_j+w y_j)`.                       (1.4)

The partner also proved that the full absolute majorant obtained from (1.3) grows at least like `log(1/rho)` on an admissible fixed-dimensional uniform product source. Thus the mixed phase in `(xi,q)` must be spent before absolute values.

## 2. Phase-retaining collapse

The key observation is that one can spend the entire `(xi,q)` mixed phase exactly, without conditioning on a rotated coordinate and without losing the original hub/leaf independence.

For `t!=0`, define the partial receiver

`B_t(w):=int_R2 exp(-i xi q/(2t))
                 psi_H(s xi) Phi(a xi,q,w) dxi dq`.                 (2.1)

Also define a complex finite measure `nu_t` on the `V` line by

`int eta(v) dnu_t(v)
 := E[ eta(V) exp(i 2 a t ZL) psi_H(2 s t L) ]`                    (2.2)

for bounded Borel `eta`. Since `V` has a density `p_V`, `nu_t` is absolutely continuous; write its density as `g_t`. A regular conditional expectation gives

`g_t(v)=p_V(v) E[exp(i2atZL) psi_H(2stL) | V=v]`                    (2.3)

for almost every `v`, hence immediately

`|g_t(v)| <= p_V(v)`.                                               (2.4)

### Theorem 2.1 — `QFORM-HYPERBOLIC-MIXED-PHASE-L2-COLLAPSE-v1`

Assume only:

* `H` is independent of `(Z,L,V)`;
* `H,L,V` have one-dimensional density caps `K_H,K_L,K_V` respectively;
* `s>0`;
* no hypothesis at all on the dependence among `Z,L,V`.

Then, for every `t!=0`,

`boxed: B_t(w)=4*pi*|t| * hat(g_t)(w),`                             (2.5)

with Fourier convention `hat g(w)=int exp(iwv)g(v)dv`, and

`boxed: ||g_t||_2^2 <= pi K_H K_L K_V /(s |t|).`                   (2.6)

Consequently

`boxed: ||B_t||_2^2 <= 32*pi^4 (K_H K_L K_V/s) |t|,`               (2.7)

or equivalently

`boxed: ||B_t||_2 <= 4*sqrt(2)*pi^2
        sqrt(K_H K_L K_V/s) |t|^(1/2).`                            (2.8)

The constants are independent of `a=sqrt(rho)`, of the dimension of the leaf bank, of the leaf fragmentation, and of the dependence among `(Z,L,V)`.

### Proof

Insert (1.4) into (2.1), but do not take an absolute value. Fubini is first justified after a standard Gaussian regularisation; the resulting identity then passes to the oscillatory limit. The `q` integral is

`int exp(iq(L-xi/(2t))) dq = 2*pi delta(L-xi/(2t))`.                (2.9)

As a distribution in `xi`,

`delta(L-xi/(2t))=2|t| delta(xi-2tL)`.                             (2.10)

Therefore

`B_t(w)
 =4*pi*|t| E[exp(iwV+i2atZL) psi_H(2stL)]
 =4*pi*|t| hat(g_t)(w)`,                                           (2.11)

which proves (2.5). This is exactly the partner's mixed hyperbolic phase being used rather than discarded.

Next (2.4) gives

`||g_t||_2^2
 <= K_V int |g_t(v)| dv`

but that estimate alone does not gain time. Instead use conditional Jensen in (2.3):

`|g_t(v)|^2
 <= p_V(v)^2 E[|psi_H(2stL)|^2 | V=v]
 <= K_V p_V(v) E[|psi_H(2stL)|^2 | V=v]`.                          (2.12)

Integrating in `v`,

`||g_t||_2^2 <= K_V E |psi_H(2stL)|^2`.                            (2.13)

Since `p_L<=K_L`,

`E |psi_H(2stL)|^2
 <= K_L int_R |psi_H(2stl)|^2 dl
 = K_L/(2s|t|) int_R |psi_H(u)|^2 du`.                             (2.14)

Plancherel and `0<=f_H<=K_H`, `int f_H=1`, give

`int |psi_H(u)|^2 du
 =2*pi int f_H(x)^2 dx
 <=2*pi K_H`.                                                       (2.15)

Combining (2.13)--(2.15) proves (2.6). Finally Plancherel in `w` and (2.5) yield

`||B_t||_2^2
 =(4*pi|t|)^2 2*pi ||g_t||_2^2
 <=32*pi^4 (K_H K_L K_V/s)|t|`,                                   (2.16)

which is (2.7)--(2.8). No rotated independence was used. QED.

## 3. Actual application to the designated fleet02/B10 harmonic family

In the partner's exact target-valid harmonic frame, `H` is an ORIGINAL cap-one coordinate and `L,V` are unit linear projections of an ORIGINAL cap-one product law. Hence the standard one-dimensional product-projection bound gives

`K_H<=1`, `K_L<=sqrt(2)`, `K_V<=sqrt(2)`.                          (3.1)

Also `s=sqrt(c)` with `c>63/64`. Theorem 2.1 therefore gives the actual inequality

`boxed: ||B_t||_2^2 <= 64*pi^4 c^(-1/2) |t|`,                      (3.2)

and

`boxed: ||B_t||_2 <= 8*pi^2 c^(-1/4) |t|^(1/2)
                 < 8*pi^2 (64/63)^(1/4)|t|^(1/2).`                (3.3)

This is the promised application of the completed `fleet02/B10` phase representation to a genuine target inequality. It is endpoint-stable as `rho downarrow 0`.

The comparison with the partner's obstruction is informative: its full absolute three-frequency majorant can grow like `log(1/rho)`, whereas after the `(xi,q)` phase is spent exactly, the resulting `L^2(dw)` norm (3.3) has **no `rho` loss at all**. Thus the hub logarithm is not intrinsic to the first hyperbolic step; it is created by absolutising before the mixed phase has acted.

The same partner report pays the majority/one-sheet side of this signature-(2,1) family by the already completed inequality

`p_Q(x) <= pi*sqrt(2) < 4.443,  x>=0`.                              (3.4)

The remaining density endpoint is therefore still the minority/two-sheet side.

## 4. Exact remaining one-dimensional obstacle

The full receiver (1.3) is now

`K_rho(t)=int exp(-iw^2/(4t)) B_t(w) dw`.                           (4.1)

Equivalently, using (2.5) and the one-dimensional Fresnel identity,

`phi_Q(t)=int exp(itv^2) g_t(v) dv`.                                (4.2)

Thus the three-frequency partner debt has been compressed to one precise question: obtain quadratic cancellation in (4.2) for the **dynamically generated** amplitude `g_t`.

Theorem 2.1 supplies

`||g_t||_1<=1`,
`||g_t||_infinity<=K_V`,
`||g_t||_2^2<=pi K_H K_L K_V/(s|t|)`.                              (4.3)

These norm facts alone cannot close the endpoint. Indeed, for `T>=1`, the artificial complex amplitude

`h_T(v)=T^(-1) 1_[0,T](v) exp(-iT v^2)`                            (4.4)

satisfies

`||h_T||_1=1`, `||h_T||_infinity=T^(-1)<=1`,
`||h_T||_2^2=T^(-1)`,                                              (4.5)

yet

`|int exp(iT v^2) h_T(v) dv|=1`.                                  (4.6)

This is **not** a QFORM counterexample and is not claimed to arise from a product projection. It proves only that the remaining argument must retain more of the source-level structure of (2.3); no interpolation among the three norms in (4.3), and no bare Fresnel `L^2` pairing, can supply the missing decay.

The useful new structural separation is therefore:

1. the dangerous hub `L^1` logarithm has been completely removed by the exact `(xi,q)` phase;
2. all dependence on the longitudinal leakage `a=sqrt(rho)` is now confined to the phase factor `exp(i2atZL)` inside the one-dimensional dynamic amplitude `g_t`;
3. the only remaining endpoint is to show that an amplitude of the special product-projection form (2.3) cannot quadratically anti-phase-align as in (4.4).

## 5. First unpaid implication

The next debt is

`QFORM-DYNAMIC-AMPLITUDE-PROVENANCE-FRESNEL-v1`:

> In the exact near-coloop product-projection law, with `g_t` defined by (2.3), prove enough source-valid cancellation in
> `int exp(itv^2)g_t(v)dv`
> to make the large-frequency characteristic function integrable (or prove the equivalent linear small-ball estimate), uniformly in `rho`. The proof must use the original product-linear provenance of `(Z,L,V)` beyond the norm bounds (4.3).

A valid proof cannot replace `g_t` by an arbitrary complex function satisfying (4.3), cannot take the full three-frequency absolute majorant, cannot invoke support/moment/log-concavity assumptions, and cannot treat `Z,L,V` as independent.

This is a strictly smaller analytic interface than the partner's three-frequency receiver: the hyperbolic mixed phase is already paid and the remaining debt is one-dimensional.

## 6. Status

* New supporting theorem: `QFORM-HYPERBOLIC-MIXED-PHASE-L2-COLLAPSE-v1` — proved above.
* Designated `fleet02/B10` result: applied at the target-valid inequalities (3.2)--(3.3).
* Full exact rank three: **OPEN**.
* Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
* Full-target continuity: **OPEN**. This run makes no new continuity claim.
* Execution/memory: repository transport only; `WITHOUT_VERIFIED_BRAIN`.
