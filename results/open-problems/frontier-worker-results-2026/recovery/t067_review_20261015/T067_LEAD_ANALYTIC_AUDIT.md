# Lead audit of T067-PIECEWISE-D0-001 v1

Subject: w682/proofs/T067-PIECEWISE-D0-001_v1.md, SHA256
`9a8a26b8c0631b4549f29bdc7ee231130a080a680408394bb75e0a8c16986226`.
Reviewer: codex-term-362ebe34. Scope: mathematical composition and independently
rebuilt finite gate. Result: PASS as a lead review using the pinned previously
audited supporting lemmas below. This does not replace the outstanding w683
review, establish publication priority, or solve all degrees of T067.

The claim is nonreconstruction for the symmetric three-state ferromagnetic
broadcast process on the regular d-ary tree, for every integer d>=156 and
0<lambda<=1/sqrt(d), including equality. The finite gate and the analytic
composition both matter; a numerical sample or a small-s expansion alone would
not prove this assertion.

## A. Calibrated comparison and retained cubic term

I rederived the expansion with a=3p-1, A=||a||^2, M=EA=9x,
U=EA^2 and T=E sum(a_i^3). With P=I-11'/3 the actual branch log-likelihood
is P log(1+lambda a). Conditional on root 1 the density tilt is 1+lambda a_1.
The matching Gaussian has covariance (lambda^2 M/2)P and conditional mean
lambda^2 M(1/3,-1/6,-1/6). Its equal-norm mean vectors give likelihood ratios
exp(g_i). Both experiments are calibrated. Independent replacement branches
are independent conditional on the root; unconditional branch independence is
not used. The radial moments have the same tilted and unconditional means by
permutation symmetry.

The third-order contribution is retained, not bounded by its absolute value.
Writing the resulting softmax polynomial as ell_i gives

    ell_i = -p_i(p_j-p_k)^2/2 + 3 p_1 p_2 p_3 (1-3p_i)/2,
    sum p_i ell_i = -e2(e2-9e3),
    e2-9e3 = sum_cyclic p_k(p_i-p_j)^2 >= 0.

This is an averaged calibrated sign. A pointwise assertion ell_1<=0 would be
false and is not needed. I reconstructed the softmax derivatives algebraically
without importing solver code in audit_t067_symbolic.py. All identities pass;
the exact receipt is T067_SYMBOLIC_RECEIPT.json. The pinned cubic-fusion lemma
supplies T>=0 along the depth recursion and at its limiting fixed point.

I also checked the Taylor constants against the displayed bounds. The log
remainder follows from the integral remainder for t>-1; one must not use an
alternating power series outside its convergence disk. The ternary identities
sum a_i^4=A^2/2, ||Pa^2||^2=A^2/6, Pa^3=Aa/2 and
Pa^4=(A/2)Pa^2+(sum a_i^3)a/3 give the stated remainder bounds.
For 0<lambda<=L<=1/10 the resulting comparison is

    x_next - g3(d lambda^2 x) <= d lambda^4 [CU(L) U + CM(L) M^2].

I checked the mean, covariance, mixed-cubic and fourth-order contributions
separately. In particular the Gaussian fourth moment is
lambda^4[2M^2+(2/3)lambda^2 M^3+lambda^4 M^4/36]; M<=6 gives the stated
factor 2+4L^2+L^4. The softmax fourth derivative bound 3/5 gives Taylor
coefficient 1/40. No unreviewed small-gap theorem is used here.

## B. Gaussian normalization, curvature and quadrature

Summing the comparison Gaussians gives mean (3s,-3s/2,-3s/2) and covariance
(9s/2)P. A two-dimensional orthogonal representation yields

    g3(s)+1/3 = E [1+2 exp(-9s/2-3 sqrt(3s) Z1/2)
                           cosh(3 sqrt(s) Z2/2)]^(-1).

The projected spatial Hessian bound is 1/5, hence the Hessian norm in Z is
at most 9s/10. For bin masses w_i, conditional means m_i and unnormalised
variances D_i, conditional Taylor expansion cancels the linear term. With
P0=sum w_i and D0=sum D_i, the interior error is <=9s P0 D0/10.
The entire omitted square tail has probability 1-P0^2 and integrand at most 1.
Both error terms are included in my independent endpoint program.

For signal curvature the generator is (9/2)D_w+(9/4)Delta_P,
||w||^2=2/3. The required mixed derivatives give

    |g3''| <= 27/10 + 135/8 + 243/20 = 1269/40 < 32.

The mixed fourth bound follows by polarizing the diagonal fourth bound in
orthogonal directions; it is not an unsupported inference about arbitrary
tensor entries. Consequently the correct upper interpolant on [a,b] is the
upper endpoint chord plus 16(s-a)(b-s). Its sign is essential: subtracting
that parabola would reverse the enclosure.

I rebuilt all 86 endpoints s_i=10/(100-i), i=0,...,85, with 180-bit Arb,
192 signed bins of width 1/16 on [-6,6], and no imports from the worker's
quadrature or gate. This differs from the author's mixed coarse/refined table
and symmetry pairing. Each independently computed upper bound is at most its
corresponding submitted bound. Source and all endpoint SHA256 values are
pinned in T067_OWN_ENDPOINT_MAP.json. Arbitrary-precision interval arithmetic
remains a software trust premise; this is not a formal kernel proof.

## C. Exact gate

With the original L=16013/200000 and D=156, I checked all 85 interval
inequalities by exact rational quadratic minimization at endpoints and every
interior stationary point, splitting at 2/15 where needed. This is a different
gate from the author's Bernstein calculation. The rebuilt endpoint table
gives a minimum gap approximately 0.00008689917825785154; the exact rational
is in T067_OWN_FINITE_GATE_RECEIPT.json. The earlier gate using submitted
endpoints also passed, with the smaller minimum approximately 0.00000284263.

An additional general-L cutoff check uses a tighter rational upper enclosure
for 1/sqrt(D). It still passes D=156 and fails this frozen certificate at
D=155 (minimum about -0.00000746214). T067_CUTOFF_SCAN.json preserves both
exact results. A failed sufficient inequality is not evidence of
reconstruction. Do not repeatedly refine this same table without a new
measured reason: the all-fine table has already tested that route.

## D. From the gate to nonreconstruction

The limiting posterior law exists by the decreasing-information/reverse
martingale construction. At fixed finite d, likelihood denominators stay
positive since lambda<1; thus the Bayesian recursion is continuous on the
compact posterior simplex and the limit is a fixed point. The pinned
ternary two-experiment estimate, applied branch by branch at lambda=1/sqrt(d),
gives U<=U/d+5(d-1)M^2/d, hence U<=5M^2. Blackwell domination of intermediate
prefixes justifies using M_j<=M. The elementary A<=6 also gives U<=6M.
Therefore U<=81 min(5x^2,2x/3), M^2=81x^2. The exact gate excludes all
fixed points x in [1/10,2/3]; the pinned uniform-local lemma excludes
0<x<=1/10 for d>=100. Equality d lambda^2=1 is included in this argument.
Total variation then tends to zero from the posterior second moment.

For smaller positive lambda, the relevant garbling replaces an observation
with an independent unconditional observation with probability 1-lambda/eta,
eta=1/sqrt(d), without revealing the replacement flag. Its posterior map is
p -> u+(lambda/eta)(p-u). This root-independent channel tensorizes
conditional on the root and proves the needed Blackwell comparison at every
finite depth. It does not require unconditional branch independence.

## Dependencies and audit-status limitation

The eight supporting proof hashes are pinned in
w682/checks/piecewise156_submission.json and checked against current bytes in
T067_LEAD_REVIEW_RECEIPT.json. The main analytic uses the derivative,
cubic-fusion, ternary-moment, uniform-local and fixed-point lemmas with their
existing exact-version reviews. Rescale and Gaussian quadrature have also
been rederived above; this audit does not rely on a blanket metadata claim
that every dependency has two saved reviews. I found old reviewer PASS
records for RESCALE and GAUSSIAN-QUAD but no separate w683 rows under those
exact claim IDs. The proof introduction's blanket two-review wording should
be corrected or those missing receipts supplied. This is an audit-status
qualification, not a mathematical gap in the explicit arguments above.

No global frontier promotion is made by this note. The remaining admission
step is the outstanding exact-version independent review and reconciliation
of the supporting audit metadata. The full q=3 problem at every degree, and
priority relative to literature, remain outside this conclusion.
