# Independent review: geometric-amplitude KL compression

**Verdict:** PASS for the mathematical compression theorems and their stated hypotheses. No proof of unrestricted FEI is supplied or implied.

**Reviewed source:** `fei_proof_20260922/rigidity/REPORT.md`, including its fixed-width theorem, appended linear level-adaptive variant, arbitrary-bias extension, and exact-support entropy corollary. The source's local signed-valuation and near-bent reports were also read for context. This review independently checks the displayed proofs; it does not certify bibliographic priority or every mathematical claim in the external source reports.

## 1. Boundary-safe reference law

The maximum-entropy law \(Q_r\) exists because the finite feasible polytope contains \(P\), and it is unique by strict concavity of entropy. Its invariance under coordinate permutations preserving the exact marginal classes is sufficient: no assumption about finite exponential-family parameters is necessary.

If \(Q_r(S)=0<P(S)\), the feasible mixture \((1-\delta)Q_r+\delta P\) gains a positive term of order \(\delta\log(1/\delta)\) at at least one previously zero atom. Changes at the finitely many positive atoms are \(O(\delta)\). This contradicts entropy maximality. Thus every \(P\)-positive atom has \(Q_r\)-positive probability.

The class permutation group acts transitively on each occupancy-vector fibre, so \(Q_r\) is constant there. It remains constant on any subset selected by a magnitude bin. Consequently its conditional law is uniform in each occupied bin fibre. This argument covers \(r_i=0\), \(r_i=1\), and \(\sum_i r_i=1\).

The single ZERO cell may have positive \(Q_r\) mass and must remain in the pushforward. Its \(P\) mass is zero, so it contributes no conditional KL loss. The report handles this correctly.

## 2. Fixed-width constant and exact binning

For weights \(w_i\in[1,R]\) with uniform-reference mean \(s\), convexity gives
\[
\mathbb E[w\ln w]\le a(s-1),\qquad a=\frac{R\ln R}{R-1}.
\]
Hence
\[
D(\pi\Vert U)\le a(1-1/s)-\ln s.
\]
The derivative is \((a-s)/s^2\), and \(1<a<R\). The maximum is therefore \(a-1-\ln a\). Endpoint weights with proportions approaching \((a-1)/(R-1)\) establish the asserted supremum over finite lists.

For \(X=\ln w\) and \(F(t)=\ln\mathbb E e^{tX}\),
\[
F'(1)-F(1)=\int_0^1tF''(t)\,dt.
\]
Since \(F''\) is a variance on an interval of length \(\ln R\), it is at most \((\ln R)^2/4\). This proves the second bound \((\ln R)^2/(8\ln2)\) in bits. With \(R=2^{2/q}\), it becomes \(\ln2/(2q^2)\).

The exact bin formula
\[
\lfloor q\log_2|A|\rfloor=\operatorname{bitlength}(|A|^q)-1
\]
is valid for every positive integer \(|A|\) and positive integer \(q\). Half-open logarithmic intervals give amplitude ratio strictly below \(2^{1/q}\); using the closed upper bound \(R\) in the lemma is safe.

Singletons are retained individually. Thus the loss is bounded by
\[
\kappa_qP(|S|\ge2)\le \kappa_q\sum_S(|S|-1)P(S)
=\kappa_q(I-1).
\]
The refinement by the original signed-valuation statistic can only reduce this loss. It does not establish a bound on the original unrefined loss. The report makes that distinction.

## 3. Linear level-adaptive variant

At level \(k\ge2\), let \(d=k-1\). The identity
\[
\left\lfloor\frac{\lfloor x\rfloor}{d}\right\rfloor
=\left\lfloor\frac{x}{d}\right\rfloor
\]
holds for an integer \(d>0\). Applied to \(x=\log_2|A|^{2q}\), it validates the displayed exact integer-division implementation.

A bin has squared-weight ratio below \(2^{d/q}\). If \(\pi\) is obtained by normalizing such weights, then \(m\pi_i\le \max w/\min w\), so
\[
D_2(\pi\Vert U)\le d/q.
\]
Summing the exact conditional KL decomposition gives
\[
0\le K_{\rm occ}-K_q^{\rm lin}\le (I-1)/q.
\]
No assumption about the number of coefficients is used in this loss bound.

For equal influences, occupancy is just the cardinality \(k\). Since \(|A|\le2^n\), level \(k\) has at most \(\lfloor2qn/(k-1)\rfloor+1\) possible bins. Including at most \(n\) singleton cells and one ZERO cell gives
\[
\#\text{cells}\le 2qnH_{n-1}+2n.
\]
This is correct, including \(n=1\) with \(H_0=0\).

Minor presentation refinements were communicated and are now implemented in the final report: use \(0<\varepsilon\le1\) when stating the \(O(n\log n/\varepsilon)\) accuracy tradeoff, and use \(\log(n+1)\) or explicitly \(n\ge2\) in an asymptotic expression intended to cover the whole stated domain. These were notation refinements; the exact inequality already covered all \(n\ge1\).

## 4. Stress-family distinction independently checked

Fixed-width bins are lossless when all nonzero non-singleton amplitudes are powers of two, because distinct powers occupy distinct bins for integral \(q\). In a one-point suspension the exceptional amplitude is a singleton and all remaining nonzero magnitudes are equal, so both variants are lossless.

The wider linear bins need not be lossless on recursive majority. An independent exact support recursion for depth-three ternary majority gives level-seven amplitudes \(2^{-7}\) and \(2^{-9}\). In dimension \(27\), the corresponding integer Walsh amplitudes are \(2^{20}\) and \(2^{18}\). At \(q=1\), both squared-amplitude bins are
\[
\lfloor40/6\rfloor=\lfloor36/6\rfloor=6.
\]
They therefore create positive within-cell loss. The report now states this distinction explicitly and retains only the proved additive bound for that variant.

## 5. Arbitrary product biases and constants

For an interior product measure and a nonconstant Boolean function, \(v>0\) and the nonempty normalized spectral law is \(P(S)=\widehat f_p(S)^2/v\). Then
\[
\sum_S(|S|-1)P(S)=(\widetilde I-v)/v.
\]
Multiplying the conditional KL estimate by \(v\) proves both biased extensions exactly. The proof requires no dyadic lattice. Real-amplitude bin endpoints and the finite nonzero amplitude dynamic range are handled correctly.

The uniform integer cell count does not extend automatically to arbitrary biases. The report explicitly refrains from that claim. The \(v=0\) case is handled by defining the unnormalized reserve/loss as zero without forming \(P\).

## 6. Exact-support entropy corollary

If \(P\) is supported on \(F\cup R\), \(R\subseteq A\), with nonempty \(F\), entropy subadditivity and concavity give
\[
H(P)\le |A|h_2(t),\qquad I=|F|+|A|t.
\]
The derivative of \(h_2(t)/t\) is \(\ln(1-t)/(t^2\ln2)<0\), so the displayed bound for \(t\ge a\) follows. The TV hypothesis bounds the expectation of the normalized cardinality in \([0,1]\), giving \(t\ge1/2-\varepsilon\). The \(a=1/32\) constant is \(5+31\log_2(32/31)<6.5\), as stated.

This is an exact-support result. Leakage outside that support is not covered.

## 7. Material limits

The partition depends on the source spectrum and its exact marginal classes. Its small range in the equal-influence case does not give a polynomial-time procedure for constructing that range or computing its probabilities. For many distinct influence classes, occupancy may retain the full Fourier label.

The report supplies a rigorously priced compression error. A lower bound on the retained reserve sufficient to pay the FEI deficit is still missing. No universal FEI constant, template-recovery theorem, or full proof is established.

**Review conclusion:** no unresolved mathematical gap found in the compression statements actually proved.

