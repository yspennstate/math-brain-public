# C0029 referee packet (working)

## w565-C01 — KEEP as an elementary obstruction only

At n≥2, let v=(1,-1,0,…,0)/√2. Its norm is 1. For independent uniform signs R1,R2, the four ordered pairs are equiprobable; (R1-R2)/√2 is zero in (+1,+1) and (-1,-1), so P(⟨R,v⟩=0)=2/4=1/2. Thus a putative universal bound P(|⟨R,v⟩|≤t)≤Kt for every deterministic unit vector fails already at t=0 (and for all 0≤t<√2 if Kt<1/2). This checks w565's exact claim independently. It neither bounds a random normal nor solves the least singular value conjecture. Reviewer: w566, 2026-10-10.

NEXT: Compare the primary statement and later literature, then audit any load-bearing w564 or w565 lemma as soon as it appears.

## w564 L1/L2/L3 — KEEP within their stated scope

Reviewed [ATTEMPT.md](~/brain_workers/w564/ATTEMPT.md), SHA-256 `7861BF36F60FB966A8B9CEEB736801BA0BBAA2D9AFF9BDB96811B01597D2293B` as read. L1 follows from interlacing on d<=r and from the scalar Schur complement on d>r. Inertia handles equality; r=0 returns the exact singularity event. L2 uses the same mixed skeleton for each one-row replacement and telescopes p_0-p_n with sign Q_R-Q_G. No product of conditional probabilities appears. L3: for the Hadamard skeleton, the two-dimensional block of A^T A has trace 2n and determinant S², so its lower eigenvalue is n−√(n²−S²). With r=1/[8(n+1)], every nonzero even S gives eigenvalue ≥2/n>r², whence Q_R=binom(n,n/2)/2^n≥1/(n+1). The Gaussian normal/tangent decomposition gives Q_G≤2r=1/[4(n+1)], leaving the stated ≥3/[4(n+1)] gap. The exact arithmetic control at n=2,4,8,16 produced sign atoms 0.5, 0.375, 0.2734375, 0.196380615234375, respectively; these checks support, but do not replace, the all-n proof.

w564 H: KEEP as an explicitly open exact reformulation. Since p_R=F_n+Σ_kE(Q_R−Q_G), H is equivalent to the coefficient-one bound in the nontrivial ε range. **The signed sum estimate is not proved.** The Hadamard example defeats a pointwise sign shortcut but is too rare by itself to refute the averaged target.

## w565 independent derivation — KEEP as scoped obstructions

Reviewed [INDEPENDENT_DERIVATION.md](~/brain_workers/w565/INDEPENDENT_DERIVATION.md). Its Schur formula independently agrees with L1; it treats t=0, equality, and deficient rank separately. Its n=4 dependence example can be reproduced without simulation: z² has masses 6/16, 8/16, 2/16 at 0,1,4. At t=3/4, the true squared radius equals 9(119−16z²)/880, so z²=0 or 1 passes, giving 14/16=7/8. An independent radius copy admits z²=1 for only 14/16 of radius outcomes, giving 6/16+(8/16)(14/16)=13/16. The 1/16 underestimate invalidates an independence substitution, but ε=t√4=3/2 is outside the nontrivial target range. Its artificial CDF F_n(x)=min(1,(1+(log n)^(-1/16))x) demonstrates that a (1+o(1))x bound alone cannot yield x+exp(-cn); it is not a Bernoulli counterexample.

The w565 exact-check script was not run here: its saved fresh compute gate says BLOCKED. My reproduction above is analytic. w565's claim C01 has a separate KEEP verdict at the top of this packet.

## Archive correction — FIX

`C0029-A001` in the 2026-09-07 intake calls the real Gaussian hard-edge limiting CDF an exact finite-n law. At n=1 and t=1, `python -X utf8 -c "import math; print(math.erf(1/math.sqrt(2)),1-math.exp(-1.5))"` gives 0.6826894921370857 versus 0.7768698398515702, an absolute discrepancy of 0.09418034771448447. Replace the finite-n equality by the finite-n Gaussian CDF F_n and cite Edelman's inequality F_n(t)≤t (Sah–Sahasrabudhe–Sawhney, Theorem 9.4). This correction is a source-level FIX, not a parent proof.

## Own result awaiting next referee

L4 in [ATTEMPT.md](~/brain_workers/w566/ATTEMPT.md) charges the exact orthogonal-skeleton event under iid sign rows by at most 2^(−(n−2)); request w569 to independently audit the conditioning and mixed-Gaussian clause. Do not promote L4 before that check. No served-model identity has been verified for this review; the mathematical verdicts are preliminary for any gate requiring a specified final-review model.

NEXT: w569 checks L4; coordinator reviews the frozen L1/L2/L3/C01 bundle and applies the archive correction. H remains the single hardest unproved estimate.
