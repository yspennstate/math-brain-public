# account04/B15 — continuous-output extremal envelope

**Run:** `20260922T152333Z-b15-qform-continuous-envelope-r3`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
**Assignment:** Absolute continuity and regularity  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_TARGET_LEVEL_REGULARITY_REDUCTION`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope

The full conjecture remains open. The target class consists of laws
\[
\mu_{A,f}=\operatorname{law}(X^TAX)
\]
where the coordinates of \(X\) are independent, \(0\le f_i\le1\), \(\int f_i=1\), and the real symmetric matrix \(A\) has at least three eigenvalues of modulus at least one. No support, moment, sign, or diagonal-coordinate hypothesis is imposed.

This report proves that the optimal universal \(L^\infty\) constant is already determined exactly by the subclass whose quadratic outputs have continuous \(C_0\) densities. Thus continuity is harmless for the *extremal constant*, even though continuity of the density for every original rough-input instance remains a separate open assertion.

## 2. Partner result used

The completed account01/B15 theorem is used in its exact form:

- repository/commit: `yspennstate/math-open-problems@5e161df12dcfebf0d13eb7efeaef5c478bf09455`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account01/B15/20260922T150652Z-account01-B15-qform-r11/REPORT.md`.

It proves that the optimal interval constant for the full class equals the optimal constant after restricting every marginal to \(C_c^\infty(\mathbb R)\), still with \(0\le f_i\le1\) and mass one. Its proof uses account02/B15's exact Choquet representation and cap-preserving smooth approximation of measure-one indicator extremes. It also proves that every output in this smooth subclass has a density in \(C_0(\mathbb R)\).

## 3. Three extremal constants

For a target law \(\mu\), put
\[
\mathcal M(\mu)=\sup_I\frac{\mu(I)}{|I|},
\]
where the supremum is over bounded nondegenerate intervals. If \(\mu=p\,dt\), then \(\mathcal M(\mu)=\|p\|_\infty\). Define, with values in \([0,\infty]\),
\[
C_{\rm all}=\sup_{\text{all target instances}}\mathcal M(\mu),
\]
\[
C_{C_0}=\sup_{\substack{\text{target instances}\\ \mu=p\,dt,\ p\in C_0(\mathbb R)}}\|p\|_\infty,
\qquad
C_{\rm sm}=\sup_{\substack{\text{target instances}\\ f_i\in C_c^\infty,\ 0\le f_i\le1}}\|p\|_\infty.
\]

### Theorem 3.1 — exact continuous-output envelope

\[
\boxed{C_{\rm all}=C_{C_0}=C_{\rm sm}.}
\]

The equality includes the value \(+\infty\).

### Proof

The smooth-output theorem from account01/B15 gives
\[
C_{\rm sm}\le C_{C_0}\le C_{\rm all}.
\]
Conversely, the exact partner reduction says that, for every finite \(C\), the inequalities
\[
\mu(I)\le C|I|
\]
for all smooth target instances and all intervals imply the same inequalities for every target instance, with no change in \(C\). Therefore \(C_{\rm all}\le C_{\rm sm}\).

If \(C_{\rm all}=+\infty\), take any \(L<C_{\rm all}\) and select a target instance and interval \(I\) with \(\mu(I)>L|I|\). The partner's total-variation approximation supplies a smooth target law \(\mu_k\) with
\[
\|\mu_k-\mu\|_{\rm TV}<\mu(I)-L|I|.
\]
Then \(\mu_k(I)>L|I|\), and its density belongs to \(C_0\). Letting \(L\to\infty\) proves equality also in the infinite case. \(\square\)

### Corollary 3.2 — counterexample preservation

If a proposed finite universal constant \(C\) fails anywhere in the full target class, it already fails for an instance with compactly supported smooth cap-one marginals and a continuous \(C_0\) output density.

More quantitatively, for any target density \(p\) and any \(\eta>0\), there exists a smooth target instance with output density \(p_\eta\in C_0\) such that
\[
\|p_\eta\|_\infty\ge\|p\|_\infty-\eta.
\]
Choose an interval \(I\) with \(\mu(I)/|I|>\|p\|_\infty-\eta/2\), and then take the total-variation approximation error below \(\eta|I|/2\).

Hence both proof and falsification of the universal \(L^\infty\) conjecture may be carried out entirely inside a continuous-output class. This does **not** prove that every original rough-input output density is continuous.

## 4. Explicit continuous-density estimate on the smooth subclass

Let \(r=\operatorname{rank}(A)\ge3\), let \(\Lambda\) be the nonsingular diagonal active matrix, and let \(h\in C_c^\infty(\mathbb R^r)\) be the active density obtained after rotating and integrating the null directions. The Fresnel calculation in account01/B15 gives
\[
|\phi(t)|\le B|t|^{-r/2},\qquad
B=2^{-r}\pi^{-r/2}|\det\Lambda|^{-1/2}\|\widehat h\|_1.
\]
Together with \(|\phi(t)|\le1\),
\[
|\phi(t)|\le\min\{1,B|t|^{-r/2}\}.
\]
Writing \(a=r/2>1\) and \(T=B^{1/a}=B^{2/r}\),
\[
\begin{aligned}
\int_{\mathbb R}|\phi(t)|\,dt
&\le2\left(T+B\int_T^\infty t^{-a}\,dt\right)\\
&=\frac{2r}{r-2}B^{2/r}.
\end{aligned}
\]
Fourier inversion yields the actual inequality
\[
\boxed{
\|p\|_\infty\le
\frac{r}{\pi(r-2)}
\left(
2^{-r}\pi^{-r/2}|\det\Lambda|^{-1/2}\|\widehat h\|_1
\right)^{2/r}.
}
\]
Moreover \(p\in C_0(\mathbb R)\).

This is instance-dependent, not universal: \(\|\widehat h\|_1\) may depend badly on support fragmentation and derivatives. It does not revive the refuted law-uniform pointwise-decay claim. Its role is to give a precise classical-density endpoint for every member of the extremally complete smooth subclass.

## 5. Why rough-input continuity does not follow

Uniform \(L^\infty\) control plus total-variation convergence of continuous densities does not preserve continuity. Let
\[
u=1_{[0,1]}
\]
and let \(\eta_\varepsilon\in C_c^\infty\) be a nonnegative approximate identity. Then
\[
u_\varepsilon=u*\eta_\varepsilon
\]
is a smooth probability density with
\[
0\le u_\varepsilon\le1,\qquad \|u_\varepsilon-u\|_1\to0,
\]
but the limit \(u\) has no continuous representative.

This is not a quadratic-form counterexample. It is a rigorous obstruction to one inference only: the exact smooth-class reduction, even with a common density cap and total-variation convergence, cannot by itself establish continuity of every rough target output. A further target-specific scale-coherence or modulus estimate is necessary.

## 6. Regularity ledger

1. **Absolute continuity:** proved for every nonzero quadratic polynomial of an absolutely continuous vector.
2. **Bounded density for each fixed rank-\(\ge3\) matrix:** proved with a matrix-dependent principal-block constant.
3. **Universal \(L^\infty\) constant:** still open.
4. **Extremal reduction:** the optimal full constant equals the optimal constant over \(C_0\)-output instances, exactly.
5. **Continuity for every rough target input:** still open and not implied by approximation alone.

The first unpaid regularity implication is therefore precise: prove a quadratic/product-specific uniform scale-coherence estimate for rough output densities, or exhibit a valid rough target instance with a discontinuous density. This is separate from the universal constant, whose exact value is already captured by continuous outputs.

## 7. Corrections respected

The proof uses no law-uniform pointwise oscillatory decay, no independence after rotation, no bounded fragment-count reduction, no bounded-diameter localization, and no naive fiber supremum. The live correction ledger through `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1` is compatible with every statement above.

No novelty or publication-priority claim is made. The full quadratic-form conjecture remains **OPEN / NOT PROVED**.
