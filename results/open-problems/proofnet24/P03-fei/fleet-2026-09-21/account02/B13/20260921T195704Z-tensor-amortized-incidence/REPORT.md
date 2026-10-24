TASK: B13 ACCOUNT: account02 RUN: 2026-09-21T19:57:04.392245Z — tensor-amortized layer-incidence no-shortcut and primitive-core localization

MODEL: GPT-5.6 Sol (self-report)
REQUESTED EFFORT: maximum actually supported
CONFIGURED / KNOWN REASONING LEVEL: UNKNOWN / NOT_EXPOSED
PROVIDER REASONING USAGE: null / NOT_EXPOSED
EXECUTION: WITHOUT_VERIFIED_BRAIN

# Status

**Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

This run follows the live `FEI-FULL-PROOF-PROGRESS-2026-09-21-174421Z` continuation and the later joint order. The stale provisional benchmark row for B13 is not used. No publication-priority claim is made.

The main new result is a tensor-amortization theorem for B13's exact layer-incidence residual. It shows that the global harmonic-Riesz target proposed in the newest B17 handoff is not an easier residual theorem: under tensor powers that residual recovers the entire original Fourier entropy up to only logarithmic overhead. Consequently a global bound

    R_inc(f) <= C (I(f)-tau(f))

for every Boolean f would itself imply full FEI with the **same** constant C, not merely with the previously displayed paid coefficient plus C. In particular the optimal global harmonic-Riesz constant is at least the true FEI constant and hence is already forced above the current explicit lower-bound scale.

This is a no-shortcut theorem and a quantifier correction, not a full FEI bound. It redirects the Riesz/layer-incidence mechanism to the minimum-dimensional tensor-primitive centered cores supplied by the current interactive reduction, where tensor amplification is excluded by construction.

# 1. Fresh inputs and nonduplication

The exact own input is `20260921T192906Z-harmonic-layer-incidence/REPORT.md`. For a Boolean f, let

    mu(S)=fhat(S)^2,  K=|S|,  I=E K,  tau=Pr(K>0),

and, on K>0, mark M uniformly in S. Put

    r_i = Pr(K>0,M=i),

and let Q_i be the law of S conditional on M=i, with L_i=K-1. The previous B13 report proved the exact decomposition

    H(f)
      = h_2(tau)
        + tau H(M | K>0)
        + sum_i r_i H(L_i)
        + R_inc(f),                                      (1.1)

where

    R_inc(f)
      = tau [ H(S | K,K>0) - H(M | K,K>0) ].             (1.2)

It also paid the first three terms dimension-independently but left `R_inc` open.

The newest B17 report `20260921T194732Z-harmonic-riesz-curvature/REPORT.md` identifies Q_i as the normalized squared spectrum of

    u_i = D_i L^{-1/2} f,

and proves the exact curvature bank

    sum_{i != k} ||D_k D_i L^{-1/2}f||_2^2 = I-tau.      (1.3)

It proposes testing a universal harmonic-Riesz inequality

    (HR_C)  R_inc(f) <= C_R (I-tau).                     (1.4)

The account04/B18 handoff `20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md` is also consumed here. Its genuine Boolean mixed-derivative identity

    kappa_ik=kappa_ki=p_ik+4 o_ik

and column conservation show that physical derivative rows from one Boolean source have a real integrability bank; this is not reproduced or weakened below.

The newest interactive account02 continuation `20260921T192650Z-joint-fei-subcube-peeling/REPORT.md` proves a paid peeling theorem for one exact/near constant-sign subcube derivative and preserves the minimum-dimensional centered primitive-core reduction. The present result is complementary: it identifies which **global tensor quantifier** must be removed before (1.4) can plausibly be a simpler local target.

# 2. Required comparison with the last THREE completed substantive own reports

The last three completed substantive account02/B13 reports are:

1. `20260921T192906Z-harmonic-layer-incidence`: refuted row-local `H(Q_i)<=A+B kappa_i`, then paid cardinality entropy and isolated `R_inc`.
2. `20260921T185920Z-harmonic-marker-payment`: introduced inverse-size harmonic rows, paid empty/nonempty plus root-marker entropy using the actual ternary Boolean derivative, and left a row-local Palm entropy.
3. `20260921T180326Z-sign-stability-defect`: proved the exact sign-defect decomposition and dimension-free transfer from a low-defect signed derivative Palm row to its unsigned support row; terminal-to-prefix information remained unpaid.

## FULL-PROBLEM CHANGE

**Before:** the best own reduction was

    H(f) <= 6.416127927200970... I(f) + R_inc(f),

and B17's newest candidate was to prove the global residual payment (1.4).

**After:** no universal FEI constant has been proved. Instead, (1.4) is proved to be full-FEI-strength under tensor amplification: if (1.4) holds globally with constant C_R, then

    H(f) <= C_R I(f)

for every Boolean f. Therefore a global proof of (1.4) cannot be advertised as merely paying a smaller leftover after a 6.416... base charge. Its best possible constant is at least the actual FEI constant.

## MECHANISM CHANGE

The preceding two own runs both tried to simplify the harmonic residual locally (first by row mean, then by cardinality splitting). This run changes mechanism completely: use **disjoint Boolean tensor powers as an adversarial compiler** for the residual theorem itself. The resulting logarithmic-overhead identity detects whether a proposed residual inequality is genuinely weaker than FEI before further local optimization is attempted.

The correct next quantifier is therefore not "all Boolean f" for (1.4), but the minimum-dimensional centered tensor-primitive critical cores supplied by the interactive reduction.

# 3. Universal logarithmic overhead around R_inc

### Theorem 3.1 — layer incidence already contains all but O(log n) entropy

For every Boolean f on n>=1 relevant coordinates,

    0 <= H(f)-R_inc(f) <= 1 + 2 log_2 n.                 (3.1)

### Proof

Use the exact decomposition (1.1). The empty/nonempty flag contributes at most one bit:

    0 <= h_2(tau) <= 1.

The marker M has at most n possible values, so

    tau H(M|K>0) <= log_2 n.

For every i, L_i=K-1 takes values in {0,...,n-1}, hence H(L_i)<=log_2 n. Since sum_i r_i=tau<=1,

    sum_i r_i H(L_i) <= log_2 n.

All three terms are nonnegative. Substitution in (1.1) gives (3.1). QED.

This uses the exact B13 decomposition, not a sign-free sufficiency claim. The statement is deliberately dimension-dependent and is not FEI.

# 4. PROVED: tensor powers amortize R_inc to the full FEI ratio

Let f be a nonconstant Boolean function on d relevant coordinates and put

    H_0=H(f), I_0=I(f)>0.

For m>=1 form the disjoint Boolean tensor power

    F_m(x^(1),...,x^(m)) = product_{a=1}^m f(x^(a)).

Its Fourier spectral law is the product of m independent copies of mu, so exactly

    H(F_m)=m H_0,   I(F_m)=m I_0.                       (4.1)

Let tau_m be its nonempty spectral mass.

### Theorem 4.1 — tensor-amortized incidence theorem

For every m,

    m H_0 - 1 - 2 log_2(md)
        <= R_inc(F_m)
        <= m H_0.                                       (4.2)

Consequently

    lim_{m->infinity}
      R_inc(F_m)/(I(F_m)-tau_m)
      = H_0/I_0.                                        (4.3)

### Proof

Apply Theorem 3.1 to F_m, whose ambient relevant dimension is md, and use (4.1). This gives (4.2).

For the limit, tau_m<=1, so

    I(F_m)-tau_m = m I_0 + O(1).

The upper bound in (4.2) gives

    R_inc(F_m)/(mI_0-tau_m)
      <= mH_0/(mI_0-tau_m) -> H_0/I_0.

For all sufficiently large m the lower numerator in (4.2) is positive; because mI_0-tau_m <= mI_0,

    R_inc(F_m)/(mI_0-tau_m)
      >= H_0/I_0
         - [1+2 log_2(md)]/(m I_0),

which has the same limit. QED.

No isolated non-Boolean probability law appears: every F_m is a genuine Boolean tensor product of f.

# 5. Consequences for the B17 harmonic-Riesz target

### Corollary 5.1 — global HR_C implies full FEI with the SAME constant

Assume a finite C satisfies

    R_inc(g) <= C [I(g)-tau(g)]                         (5.1)

for every Boolean g. Then every Boolean f satisfies

    H(f) <= C I(f).                                     (5.2)

### Proof

Apply (5.1) to F_m and combine with (4.2):

    mH_0
      <= 1+2log_2(md)+C(mI_0-tau_m)
      <= 1+2log_2(md)+CmI_0.

Divide by m and let m tend to infinity. QED.

Thus the B17 harmonic-Riesz inequality is a valid sufficient target, but **globally it is already a full-FEI theorem in disguise**. The earlier route `H<=6.416...I+R_inc` is still correct; tensor amplification simply shows that if R_inc itself has a global `(I-tau)` bound, the 6.416... overhead washes out and one gets the sharper same-C theorem.

### Corollary 5.2 — sharp lower constraint on any global HR constant

Let

    C_FEI^* = sup_f H(f)/I(f),
    C_HR^*  = sup_{g:I(g)>tau(g)} R_inc(g)/(I(g)-tau(g)).

Then

    C_HR^* >= C_FEI^*.                                 (5.3)

The current explicit FEI lower-bound record gives

    C_FEI^* > 6.521845710923046575,

so any universal global HR constant must be strictly larger than that number. In particular constants 2, 4, or 6.4161279272... cannot satisfy (5.1) globally.

More constructively, if a finite Boolean f satisfies H_0/I_0>c, then every m obeying

    m(H_0-cI_0) > 1+2log_2(md)                          (5.4)

produces a genuine Boolean F_m that violates `R_inc<=c(I-tau)`. This follows directly from (4.2), since `c(I(F_m)-tau_m) <= cmI_0`.

This is an actual counterexample generator for any proposed global constant below an already realized FEI ratio.

# 6. Explicit calibration: tensor powers of two-bit AND

For the two-bit AND sign table, the squared Fourier spectrum is uniform on F_2^2, so H=2 and I=1. Its m-fold tensor power has uniform squared spectrum on F_2^(2m). Therefore

    tau_m = 1-2^(-2m),

and at fixed K=k the spectral set is uniform on k-subsets while its marked endpoint is uniform on 2m coordinates. Hence exactly

    R_inc(F_m)
      = sum_{k=1}^{2m} [C(2m,k)/2^(2m)]
          [log_2 C(2m,k)-log_2(2m)].                    (6.1)

Thus `R_inc/(I-tau)->2`, matching Theorem 4.1. The executed standard-library checker gives ratios

    m=10:  1.38559467203167
    m=20:  1.63000481605781
    m=50:  1.81606392655107
    m=100: 1.89380932491225
    m=200: 1.93963377329320
    m=500: 1.97195236093846.

The same checker directly verifies (1.1), H/I additivity, and the sandwich (4.2) on AND_2, MAJ_3 and a three-bit one-point defect tensor powers. It records 92 direct checks and ends `PASS`. These numerics are self-checks; Theorems 3.1--4.1 are analytic.

# 7. Corrected target: primitive-core HR, not global HR

The newest interactive centered-critical theorem gives, from any Boolean f, a minimum-dimensional median-character physical-restriction descendant h with

    H(h)/J(h) >= H(f)/I(f),

with I(h)=J(h), and with no nontrivial disjoint-variable multiplicative factorization. The same interactive continuation additionally pays one exact/near constant-sign coordinate-subcube derivative row when its transverse surplus is small. Account04/B18 supplies a true mixed-derivative congestion bank for jointly realized derivative rows.

Theorem 4.1 explains why **global** (5.1) is the wrong simplification: nonprimitive tensor products alone make R_inc asymptotically equal to the entire entropy ratio. A nonduplicative target is therefore:

> Prove a dimension-independent layer-incidence/Riesz-curvature payment only for the minimum-dimensional centered tensor-primitive cores, using the exact subcube-peeling and mixed-curvature exclusions to remove rigid/near-rigid rows.

A bound

    R_inc(h) <= C_prim [I(h)-tau(h)]                    (7.1)

for every such primitive core would, by the existing B13 reduction plus the critical-core theorem, imply

    H(f) <= (6.416127927200970... + C_prim) I(f)

for every Boolean f. Unlike the global HR target, (7.1) excludes the tensor-amplification obstruction proved here. It remains unproved.

This is the precise next B13 interface to B17/B18: identify a genuinely Boolean curvature or signed affine-block inequality that uses primitivity/minimum-dimensional restriction criticality and cannot be reproduced by a disjoint tensor power.

# 8. Sanity / forbidden-route checks

* No global phase/rank/l1 payment is revived.
* No sign-free parity profile is asserted sufficient.
* No lattice-integrality shortcut is used.
* The tensor products are genuine Boolean functions, not relaxed square laws.
* Ordinary original entropy/influence are used in (4.1)--(5.2); no affine change is hidden in the transfer.
* The primitive-core statement is used only as a quantifier reduction; no claim that its listed properties alone prove FEI is made.
* B17's HR target is not claimed false for some finite constant. What is proved is that any such global constant is at least the full FEI constant and that proving it would already prove FEI with the same constant.
* Full FEI remains OPEN.

# 9. Verification and next target

Executed checker: `check_tensor_amortization.py`.
Archived output: `CHECKER_OUTPUT.txt`.
Direct checks: 92, all PASS.

Next mathematical target: on a minimum-dimensional centered primitive core, combine the interactive one-row punctured-cube Shannon peeling with account04/B18 mixed-curvature conservation and B17 harmonic Riesz rows to prove a **primitive-only** incidence payment, or construct a genuine primitive Boolean family refuting that restricted target. Tensor powers must not be used as positive evidence for the primitive-only conjecture.
