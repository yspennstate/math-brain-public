# account02/B07 MOC4 — higher-order saturation and corrected mixed-Schur discriminant

Run: `20260922T083437Z-b07-d9295a20`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Candidate: **`MOC4-MSQR-HIGHER-ORDER-SATURATION-v1`**  
Parent target: **OPEN / NOT PROVED / NOT DISPROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh authority and scope


The scheduler surface was inspected only for account02. The current managed B01-B20 set has 20 enabled tasks, each on an hourly rule, with current collective/FEI role prompts and quiet task delivery flags. No missing managed slot, duplicate current slot, disabled current slot, or cadence defect was observed, so there is no B20 deficit to report and B07 made no scheduler mutation.

The canonical same-hour B07 login already existed when this invocation started, so it was not overwritten. A unique immutable start record for this invocation was created separately.

## 2. Source-bound state consumed

The latest complete campaign-lead source recovered is account03/B07 run `20260922T074824Z-account03-B07-MOC4-r13`, report `MOC4-MSQR-CROSS-BLOCK-ANNIHILATION-v1` / `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`. Its key inputs used here are:

1. at a true-unitary support global maximum the full support Hessian is negative semidefinite;
2. a kernel vector of a principal mixed-Schur pair block is therefore a kernel vector of the full Hessian;
3. for `A=-D^2F>=0`, split as `A=[[P,B],[B^T,C]]`, with cubic covector `ell=(u,v)`, generalized Schur complement `S=C-B^TP^+B`, and corrected residual `r=v-B^TP^+u`, one has

   `q + 3 u^T P^+u + 3 r^T S^+r <= 0`;

4. the first general unpaid MSQR implication is to turn the structured determinant/same-unitary equations into enough cross-split payment to violate that gate, or show that the residual-zero exceptional system is target-safe.

The latest complete named-partner source recovered is account03/B08 run `20260922T072320Z-account03-B08-MOC4-r12`, `MOC4-GENERIC-FACET-LADDER-v1`. It gives a dense exact true-unitary/simple-spectrum point within about `3.81e-5` of a unique exposed target facet, but an exact genuine pair move still raises the same support functional. I use it as a guardrail: small support gap is not evidence for the stationary branch; all elementary pair stationarity/global-maximality gates must precede the higher-order analysis below.

A second OTHER-account source used directly is account03/B20 run `20260922T071802Z-account03-B20-MOC4-r12`, `MOC4-MIXED-SCHUR-TRUST-COLLAPSE-v1`. In a genuine complementary `SU(2)xSU(2)` product orbit it proves that, on the mixed-Schur boundary, the exact same-pair global trust-region condition collapses to the same pair Lyapunov-Schmidt reserve. Thus another same-pair optimization cannot close MSQR; the new information must be cross-split or higher-order.

The latest complete own canonical report visible in the current B07 scientific root is `20260922T073613Z-b07-2e219625`, `MOC4-MIXED-SCHUR-FULL-LS-CROSS-RESERVE-v1`. It proves the full Lyapunov-Schmidt gate and the quantitative cross-residual estimate

`||r||^2 <= (4 Delta/3) sum_{sigma in W} g_sigma`,

where `Delta=-(q+3u^TP^+u)` is pair-only quartic slack. The current canonical B07 directory exposes no later completed own science folder, so no later unsurfaced state is assumed.

## 3. Compact conditional end-to-end route

The current proof tree can be stated compactly as follows.

1. The inherited exact pair-symmetrized/common-lift argument covers repeated spectra; determinant derivatives used here are polynomial and therefore remain valid when `det(A+B)=0`.
2. A strict counterexample can therefore be reduced to a simple-spectrum positive-gap true-unitary global support maximizer, subject to the campaign's strict elementary pair gates.
3. The lead splits the remaining zero-free generic maximizer into `MSQR` (some complementary Spin(4) pair Hessian is singular on its mixed-Schur boundary) and `NDI` (all such pair blocks are negative definite), plus the separately tracked zero-face branch.
4. On `MSQR`, same-pair trust gives no extra information beyond pair Lyapunov-Schmidt. The full Hessian adds the nonnegative cross reserve `r^TS^+r`.
5. This run treats the most rigid residual leaf, exact pair-LS saturation `Delta=0`. In that leaf the full cross-reserve theorem already forces `r=0`, hence the *full* quartic kernel gate also saturates. The new result below then forces an exact fifth-order identity and a new sixth-order positive-reserve inequality.
6. Closing the positive-slack MSQR leaf, this exact-saturation leaf, NDI, and the known zero-face obligation would exclude every positive support gap and hence prove the desired 24-vertex convex-hull inclusion by support separation.

No step below claims those remaining branches are closed.

## 4. Structured meaning of the cross residual: a corrected mixed-Schur discriminant gradient

Work in fixed real local coordinates on the genuine unitary manifold at a support global maximizer. For one complementary pair split write the negative pair Hessian in the standard mixed-Schur form

`P_pair = [[alpha I_2, -N],[-N^T, beta I_2]] >= 0`,

with `alpha,beta>0`. Assume for this paragraph that the top singular value of `N` is simple and

`sigma_1(N)=sqrt(alpha beta)`.

Let `p,q` be corresponding unit left/right singular vectors and set

`z=(sqrt(beta) p, sqrt(alpha) q)`.

Then `P_pair z=0`. Define the scalar mixed-Schur discriminant

`kappa = alpha beta - sigma_1(N)^2`.

Let `Y` be any true-unitary tangent coordinate and let

`ell(Y)=D^3F(0)[z,z,Y]`.

### Theorem 4.1 — discriminant-gradient identity

At the mixed-Schur point,

`ell(Y) = - d kappa(Y)`.

**Proof.** In the fixed tangent basis, `P_pair=-D^2F|_pair`, so differentiating the pair Hessian in direction `Y` gives

`ell(Y) = - z^T (d P_pair[Y]) z`.

Direct substitution of `z` gives

`z^T(dP_pair[Y])z
 = beta d alpha[Y] + alpha d beta[Y]
   - 2 sqrt(alpha beta) p^T(dN[Y])q`.

For a simple singular value, `d sigma_1[Y]=p^T(dN[Y])q`. The displayed expression is therefore exactly

`d(alpha beta-sigma_1^2)[Y]=d kappa[Y]`.

This proves the identity. No determinant inverse appears. `QED`

Now split the full negative Hessian as

`A=[[P,B],[B^T,C]]>=0`

between the four-real-dimensional pair space and its orthogonal complement, and split the cubic covector as `ell=(u,v)`. For a complement vector `w` define its Hessian-corrected lift

`Yhat(w)=(-P^+ B w, w)`.

Then the lead/own cross residual satisfies the exact identity

`r(w)=(v-B^TP^+u)·w = ell(Yhat(w)) = -d kappa(Yhat(w)).`    (DG)

Thus the abstract Schur residual is not a free quantity: on the simple mixed branch it is precisely the differential of the mixed-Schur discriminant after the quadratic pair response has been eliminated.

In particular, at exact pair-LS saturation the prior full-Hessian gate forces `r=0`, so `kappa` is stationary in *every* Hessian-corrected transverse direction. This is a concrete same-unitary condition to insert into the determinant/exterior-square formulas.

The simple-singular-value assumption is only needed for the differentiable formula for `sigma_1`. The higher-order theorem below does not require it and therefore also applies to multiple Hessian kernels once a full kernel direction is chosen.

## 5. New higher-order saturation theorem

Let `F:R^n->R` be `C^6` near `0` and have a local maximum at `0`. Put

`A=-D^2F(0)>=0`.

Let `0!=z in ker A`. Set

`ell(w)=D^3F(0)[z,z,w]`,

`q=D^4F(0)[z,z,z,z]`.

The standard kernel Lyapunov-Schmidt argument gives `ell in range A` and

`q+3 ell^T A^+ ell <= 0`.

Assume now that this quartic gate **saturates exactly**:

`q+3 ell^T A^+ ell = 0`.                                  (QS)

Define the optimizing second-order correction

`y=(1/2) A^+ ell#`,                                       (5.1)

where `ell#` is the Riesz vector of `ell`.

### Theorem 5.1 — forced quintic identity

Under `(QS)`,

`D^5F[z,z,z,z,z]
 +20 D^4F[z,z,z,y]
 +60 D^3F[z,y,y] = 0`.                                    (Q5)

### Proof

Use the curved path

`x(t)=t z+t^2 y+t^3 w`.

Because `Az=0`, `D^3F[z,z,z]=0`, and `(QS)` with (5.1) makes the entire `t^4` coefficient zero. The `t^5` coefficient is

`-<Ay,w> + (1/2)ell(w)
 +(1/2)D^3F[z,y,y]
 +(1/6)D^4F[z,z,z,y]
 +(1/120)D^5F[z,z,z,z,z]`.

By `Ay=(1/2)ell#`, the two terms containing `w` cancel identically. A nonzero remaining coefficient would change sign under `t -> -t`, contradicting local maximality. Multiplication by 120 gives `(Q5)`. `QED`

Define a new covector

`m(w)=D^3F[z,y,w] + (1/6)D^4F[z,z,z,w]`.                  (5.2)

### Theorem 5.2 — sixth-order kernel reserve

The covector `m` annihilates `ker A`, hence `m# in range A`, and

`D^6F[z^6]
 +30 D^5F[z^4,y]
 +180 D^4F[z,z,y,y]
 +120 D^3F[y,y,y]
 +360 m#^T A^+ m# <= 0`.                                  (Q6)

Here `D^6F[z^6]` abbreviates six copies of `z`, etc.

### Proof

With the lower-order saturated coefficients already zero, the `t^6` coefficient of the same path is

`-1/2 <w,Aw> + m(w)
 +1/6 D^3F[y,y,y]
 +1/4 D^4F[z,z,y,y]
 +1/24 D^5F[z,z,z,z,y]
 +1/720 D^6F[z^6].`                                       (5.3)

If `m` were nonzero on `ker A`, choosing a fixed kernel component of `w` with suitable sign and arbitrarily large coefficient would make (5.3) positive, contradicting local maximality for sufficiently small `t`. Therefore `m# in range A`.

Maximizing the `w`-dependent part of (5.3) gives

`(1/2) m#^T A^+m#`.

Local maximality forces the resulting maximum coefficient to be nonpositive. Multiplying by 720 yields `(Q6)`. `QED`

This is strictly higher-order information: it activates only after the full quartic reserve has saturated, and it involves fifth- and sixth-order true-unitary derivatives that do not appear in the pair trust certificate or the lead's quartic cross reserve.

## 6. MOC4 specialization

Let `F=h_eta` be the actual real support functional

`F(U)=Re(conj(eta) det(D_a+U D_b U*))`

in any smooth real chart of the true unitary orbit at a hypothetical positive-gap global maximizer. This function is real analytic because the determinant is polynomial and unitary exponential coordinates are analytic. Therefore all derivatives in Sections 4-5 exist even if `det(D_a+U D_b U*)=0`.

Suppose one mixed-Schur pair block lies on `MSQR` and its pair-only Lyapunov-Schmidt slack is exactly `Delta=0`. The prior full cross-reserve theorem gives

`r^T S^+r <= Delta/3 = 0`.

Since `r in range S`, this forces `r=0`. Consequently the full quartic gate itself is an equality, not merely an inequality. The mixed-Schur pair kernel is already a full-Hessian kernel by the lead's cross-block-annihilation theorem. Hence Theorems 5.1 and 5.2 apply to the **actual full true-unitary support function**:

1. the exact quintic identity `(Q5)` is mandatory;
2. the sixth-order reserve `(Q6)` is mandatory;
3. on the simple mixed singular channel, `(DG)` additionally says the mixed-Schur discriminant is stationary along every Hessian-corrected transverse direction.

Thus an exact-saturation MOC4 candidate must satisfy a new stack of full-tangent polynomial identities, not merely the same-pair sphere trust certificate.

## 7. Exact calibration

`VERIFY_HIGHER_ORDER_SATURATION.py` uses only Python standard-library `Fraction` arithmetic on the exact polynomial

`F(x,y)=-(y-x^2/2)^2-x^6`.

At `(0,0)`,

`A=diag(0,2)`, `z=e_x`, `ell=(0,2)`, `q=-6`,

so

`ell^T A^+ell=2`, `q+3 ell^TA^+ell=0`,

and `y=(0,1/2)`. The exact checker obtains

`quintic_identity=0`,

`m=(0,0)`,

`sextic_gate=-720`,

while direct restriction to the optimizing curve gives

`F(t,t^2/2)=-t^6`.

The captured output is:

```
ell_energy=2
quartic_gate=0
quintic_identity=0
m=(0,0)
sextic_gate=-720
optimized_curve_t6_coefficient=-1
PASS exact higher-order saturation calibration
```

This is an algebraic calibration of the coefficient bookkeeping, not an MOC4 instance and not evidence of target closure.

## 8. Application of the named partner and failure ledger

The account03/B08 r12 generic-facet ladder is applied as follows. Its exact dense simple-spectrum point is very near a unique target facet but admits a genuine pair support-improving move, so it cannot enter the local-maximality hypotheses of Sections 4-6. Any future adversarial search for the new `(DG)/(Q5)/(Q6)` obstruction must first impose all left/right pair stationarity and strictness conditions; otherwise a tiny support gap is a false positive for this mechanism.

What is **not** proved here:

- the positive pair-LS slack branch `Delta>0` is still governed by the lead's cross-reserve-payment obligation;
- the `NDI` branch remains open;
- the separate zero-face support obligation remains open;
- `(DG)` in its singular-value form assumes a simple top singular channel; multiple channels require direct tensor equations rather than differentiating `sigma_1`;
- `(Q5)` and `(Q6)` are necessary conditions at exact full quartic saturation, not by themselves a contradiction.

No arbitrary bistochastic matrix, free compound-minor array, real-only spectral surrogate, or phase-erasing relaxation is used.

## 9. First sharpened missing implication

The exact-saturation leaf is now reduced to the following source-valid structured problem.

### `MOC4-MSQR-SATURATION-Q5Q6-RIGIDITY-v1` — OPEN

At a zero-free, simple-spectrum, positive-gap true-unitary global support maximizer on a mixed-Schur pair boundary with exact pair-LS saturation, substitute the actual determinant/exterior-square derivative formulas into

1. all elementary left/right pair stationarity and strictness conditions;
2. the Hessian-corrected discriminant stationarity `(DG)`;
3. the forced quintic identity `(Q5)`;
4. the sixth-order reserve `(Q6)`;
5. the subgroup/V4 and same-unitary compatibility constraints;

and prove that these equations force the known zero/common-block boundary or target support safety. A strict positive-gap true unitary satisfying this entire system would instead be a legitimate source-valid obstruction to the current proof mechanism.

For the general `MSQR` branch with `Delta>0`, the lead's `MOC4-MSQR-CROSS-RESERVE-PAYMENT-v1` remains the first unpaid implication. This run therefore advances the exact-saturation residual leaf without falsely declaring the whole branch closed.

## 10. Verdict

**ESSENTIAL_STEP_APPLIED.** The cross-Schur residual has been identified with a structured corrected mixed-Schur discriminant gradient, and exact quartic saturation has been pushed one full order further: a compulsory quintic cancellation plus a new sixth-order pseudoinverse reserve. Both are singular-determinant safe and live on the genuine unitary manifold. Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.
