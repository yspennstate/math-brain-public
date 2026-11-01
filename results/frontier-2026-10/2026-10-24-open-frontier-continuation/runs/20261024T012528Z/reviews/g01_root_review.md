# Independent review: phase uniqueness, reflected selector, and relay audit

**Verdict.** PHASE_UNIQUENESS.md proves its stated at-most-one result for a *shared prescribed support/sign phase* and square-summable endpoint marks. REFLECTION_SELECTOR.md correctly gives the reflected-integral path for a prescribed continuous normal forcing after a nonnegative, positive-support entrance. agents/g02_audit.md correctly extends the normal-path argument through grazing and one-sided release, conditional on the same support sector. None of these selects the marked initial entrance or proves global phase validity. I checked the proofs against the exact changing-weight projected recursion and reran code/release_check.py; its four lines agree with outputs/release_check.txt.

## Phase uniqueness

For one endpoint with common boundary/support assignment, the normal difference obeys
\[
\Delta q_b'=a(\theta-\widetilde\theta)
 + z\,\Delta r_b\,\widetilde\theta+\rho z\,\Delta r_p,\qquad
a=z r_b\le0.
\]
Monotonicity of the Heaviside graph makes the first term dissipative whenever \(\Delta q_b\ne0\). On the equality set \(\{\Delta q_b=0\}\), the derivative of the absolutely continuous difference is zero almost everywhere. Hence the claimed \(|z|(1+\rho)\int\|\Delta r\|_\infty\) bound is valid. The tangential elimination and the identity \(\rho(1+\rho)+(1-\rho^2)=1+\rho\) give the same support-coordinate bound. Multiplying the ReLU difference by \(|z_i|\), summing with \(\sum z_i^2<\infty\), and applying Gronwall proves equal residuals and all endpoint paths. The increment series is uniformly absolutely convergent as asserted.

One wording refinement: the proof's phrase “at equality of q's the upper derivative is bounded by the forcing difference” should be read as an **almost-everywhere zero-set derivative** statement, not a pointwise Dini-derivative assertion. The latter can fail when the two gate fractions differ at a single equality time, but it has no effect on the integral comparison. Uniqueness of fractions is correctly excluded where their coefficient vanishes.

## Reflected selector

For \(a<0,c\ge0,q_0\ge0\), the running-minimum regulator \(k=\max(0,-\min w)\) is absolutely continuous because \(w\) is Lipschitz. It is nondecreasing and grows only on \(q=w+k=0\). On the positive set, \(k'=0\) almost everywhere and \(q'=c+a\), so \(\theta=1\). On the zero set, \(q'=0\) almost everywhere and \(k'=-g\ge0\), whence \(g=c+a\le0\) and \(\theta=-c/a\in[0,1]\). Graph monotonicity with \(a<0\) proves uniqueness. The \(q_p\) reconstruction follows from the exact cancellation \(q_p-\rho q_b\), and with \(0<\rho<1\), \(q_b(0)=0\), \(q_p(0)>0\), \(z r_p\ge0\), it indeed preserves positive support. The quadratic transversal-release expansion is correct; mere contact \(g=0\) does not imply release.

For standalone precision, the reflection note should state its intended \(0<\rho<1\) when it introduces the two-input corollary. It is implicit from this run's problem, and this is editorial rather than a defect in the result under the run assumptions.

## Separate check of agents/g02_audit.md

Its exact finite-grid identities retain \(z_n\); the \(y-\rho x\) cancellation has no slow-variation premise. The nonnegative-drift strip remains invariant at grazing even though capture from a fixed distance may no longer have a uniform bound. Its comparison estimate for the relay with \(a\le0\) is valid a.e. by the same zero-set derivative argument. The compactness proof for Euler paths is sufficient: bounded held coefficients give equi-Lipschitz paths, weak-star gates, and correct graph membership away from the limiting zero set; \(L^1\) convergence of coefficients passes the product to the limit. The comparison estimate then removes subsequence ambiguity. The \(d<0\) release uses the integrated on-side drift, and the \(\lceil D/c_0\rceil+1\) off-step bound from a trapped strip is correct.

The countable coupled comparison in agents/g02_audit.md uses a harmless \(\sqrt2\) Euclidean-norm factor where PHASE_UNIQUENESS.md uses the sharper infinity norm. Both require *the same* support assignment and \(z_i r_{b_i}\le0\) for both candidate residual paths. These conditions can cease at a later sector event; the estimate does not concatenate phases or settle the original marked entrance. The changing-\(z_n\) product-rule term in actual output is correctly retained as a caveat; agents/g01_sliding.md bounds it explicitly by \(O(L^2/a^2)\) on a fixed physical horizon.

I corrected agents/g01_sliding.md to distinguish margin loss from \(A=c+d\downarrow0\): when one inward drift merely reaches zero, \(A\) can stay positive and an already trapped strip can persist. Only uniform capture from a fixed off-face distance is lost automatically.
