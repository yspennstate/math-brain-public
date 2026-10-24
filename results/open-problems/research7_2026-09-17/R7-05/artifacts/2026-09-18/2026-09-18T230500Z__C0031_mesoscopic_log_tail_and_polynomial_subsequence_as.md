Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# C0031 — mesoscopic lower-log control, a polynomial-subsequence a.s. theorem, and a smoothing no-go

Date: 2026-09-18 UTC  
Worker: `R7-05 Sharp Inequality Research`  
Canonical target: `C0031`, Bordenave–Chafaï heavy-tailed circular law, general almost-sure upgrade  
Methods: **B6 / B18 / B25**

## 1. Scope and notation

Let

\[
A_n(z)=n^{-1/\alpha}X_n-zI,
\qquad 0<\alpha<2,
\]

in the survey normalization of Bordenave–Chafaï, *Around the circular law*, Theorem 6.2.  Everything below inherits the source's exact heavy-tail hypotheses; if one works in an equivalent stable-domain normalization with a slowly varying factor, the same argument is written with that source normalization.

Write the singular values in decreasing order

\[
s_1(A_n(z))\ge\cdots\ge s_n(A_n(z))\ge0,
\]

and define the empirical singular-value CDF

\[
F_{n,z}(t)
:=\frac1n\#\{j:s_j(A_n(z))\le t\}.
\]

The previous R7-05 run proved the exact regularization-defect identity

\[
R_{n,\eta}(z)
=\int_0^\infty
F_{n,z}(t)\frac{\eta^2}{t(t^2+\eta^2)}\,dt.
\tag{1.1}
\]

For \(\eta=e^{-J}\), the genuinely dangerous part \(0<t\le\eta\) is

\[
R^{\rm low}_{n,e^{-J}}(z)
=
\int_J^\infty
\frac{F_{n,z}(e^{-u})}{1+e^{-2(u-J)}}\,du,
\tag{1.2}
\]

hence

\[
\frac12\int_J^\infty F_{n,z}(e^{-u})\,du
\le R^{\rm low}_{n,e^{-J}}(z)
\le \int_J^\infty F_{n,z}(e^{-u})\,du.
\tag{1.3}
\]

The present run attacks this integrated count directly rather than asking first for a full-sequence summable bound on the single smallest singular value.

## 2. B18 — exact dyadic form of the lower-log defect

Because \(u\mapsto F_{n,z}(e^{-u})\) is nonincreasing, for integer \(J\ge0\),

\[
\sum_{m\ge J+1}F_{n,z}(e^{-m})
\le
\int_J^\infty F_{n,z}(e^{-u})\,du
\le
\sum_{m\ge J}F_{n,z}(e^{-m}).
\tag{2.1}
\]

Thus, up to one dyadic-log bin and the factor 2 in (1.3), the entire lower-log problem is equivalent to the tail of

\[
Q_n(z;J):=\sum_{m\ge J}F_{n,z}(e^{-m}).
\tag{2.2}
\]

This is useful because a count estimate for all small singular values can be summed before one ever singles out \(s_n\).

## 3. Source inputs used, with no new hypothesis

Two estimates already occur in the Bordenave–Chafaï/Bordenave–Caputo–Chafaï proof chain.

### 3.1 Intermediate singular values

The source's heavy-tail lower-tail argument provides constants

\[
\gamma\in(0,1),\quad C<\infty,
\]

and good events \(\mathcal G_n(z)\) with

\[
\mathbb P(\mathcal G_n(z)^c)\le C e^{-n^\delta}
\tag{3.1}
\]

for some \(\delta>0\), such that for every integer

\[
i\ge n^{1-\gamma}
\]

one has, in the notation of the source,

\[
\mathbb E\!\left[s_{n-i}(A_n(z))^{-2}\mid\mathcal G_n(z)\right]
\le C\left(\frac ni\right)^\beta,
\qquad
\beta:=1+\frac2\alpha.
\tag{3.2}
\]

The survey states this as Lemma 6.5; the exponentially small exceptional event is explicit in the detailed Bordenave–Caputo–Chafaï argument from which the survey lemma is taken.  The 2018 appendix correction to the conditional-variance lemma does not change the form of the source estimate being used here.

### 3.2 Concentration of the empirical singular law

For a matrix with independent rows/columns, the source bounded-variation concentration lemma gives, for a CDF test function and every \(u>0\),

\[
\mathbb P\left(
F_{n,z}(t)>\mathbb EF_{n,z}(t)+u
\right)
\le 2e^{-cnu^2}
\tag{3.3}
\]

with an absolute \(c>0\).  No finite second moment is needed for this concentration step.

### 3.3 The single-smallest-singular-value floor

The weak invertibility input used by the source says that for every fixed \(z\), after normalization there is some finite \(B=B(z,\alpha)>0\) such that

\[
\mathbb P\bigl(s_n(A_n(z))<n^{-B}\bigr)
\le C\sqrt{\frac{\log n}{n}}.
\tag{3.4}
\]

The right side is the familiar nonsummable obstruction identified immediately after Theorem 6.2.

The first two inputs will already give an all-\(n\) almost-sure theorem down to a polynomial singular-value scale.  The third will only be used afterward, on sparse deterministic subsequences where it becomes summable.

## 4. B25 — turn the source inverse-square estimate into a counting estimate

Set

\[
\kappa:=\frac{2}{\beta}=\frac{2\alpha}{\alpha+2}.
\tag{4.1}
\]

For \(t>0\), let

\[
N_n(t):=nF_{n,z}(t)=\#\{j:s_j(A_n(z))\le t\}.
\]

For an integer \(r\ge n^{1-\gamma}\), the event \(N_n(t)\ge r+1\) implies

\[
s_{n-r}(A_n(z))\le t.
\]

Consequently, by (3.2) and Markov,

\[
\mathbb P\bigl(N_n(t)\ge r+1\mid\mathcal G_n(z)\bigr)
\le
C t^2\left(\frac nr\right)^\beta.
\tag{4.2}
\]

Now use the exact tail-sum identity

\[
\mathbb E[N_n(t)\mid\mathcal G_n]
=
\sum_{r=0}^{n-1}
\mathbb P(N_n(t)\ge r+1\mid\mathcal G_n).
\tag{4.3}
\]

Choose

\[
q=t^\kappa,
\qquad r_0=\lceil nq\rceil.
\]

Provided \(q\ge n^{-\gamma}\), i.e.

\[
t\ge n^{-c_*},
\qquad
c_*:=\frac{\gamma}{\kappa}
=\frac{\gamma(\alpha+2)}{2\alpha},
\tag{4.4}
\]

we may apply (4.2) for every \(r\ge r_0\).  Splitting (4.3) at \(r_0\) gives

\[
\begin{aligned}
\frac1n\mathbb E[N_n(t)\mid\mathcal G_n]
&\le q+
\frac Cn t^2 n^\beta
\sum_{r\ge r_0}r^{-\beta}\\
&\le q+C t^2q^{1-\beta}.
\end{aligned}
\tag{4.5}
\]

Since \(q=t^{2/\beta}\),

\[
t^2q^{1-\beta}
=t^{2+(2/\beta)(1-\beta)}
=t^{2/\beta}=t^\kappa.
\]

Therefore

\[
\boxed{
\mathbb E[F_{n,z}(t)\mid\mathcal G_n(z)]
\le C_1t^\kappa,
\qquad n^{-c_*}\le t\le1.
}
\tag{4.6}
\]

Removing the conditioning using \(0\le F_{n,z}\le1\) and (3.1),

\[
\boxed{
\mathbb EF_{n,z}(t)
\le C_1t^\kappa+C_2e^{-n^\delta},
\qquad n^{-c_*}\le t\le1.
}
\tag{4.7}
\]

This is the key aggregate estimate.  It is strictly different from a least-singular-value estimate: it says that the *expected fraction* of singular values below \(t\) has a power law throughout the mesoscopic range where the source's intermediate-singular-value lemma applies.

## 5. Almost-sure mesoscopic lower-log uniform integrability

Let

\[
M_n:=\lfloor c_*\log n\rfloor.
\tag{5.1}
\]

For every integer \(m\le M_n\), one has \(e^{-m}\ge n^{-c_*}\), so (4.7) applies.  Choose

\[
u_n=A\sqrt{\frac{\log n}{n}}
\tag{5.2}
\]

with \(A\) large enough that (3.3) is at most \(2n^{-6}\) at each one of the \(O(\log n)\) thresholds \(t=e^{-m}\).  The union bound over \(m\le M_n\) is summable in \(n\).  Borel–Cantelli therefore gives an event of probability one on which, for all sufficiently large \(n\), simultaneously for all integer \(0\le m\le M_n\),

\[
F_{n,z}(e^{-m})
\le
C_1e^{-\kappa m}+C_2e^{-n^\delta}+u_n.
\tag{5.3}
\]

For every fixed integer \(J\), sum (5.3) from \(J\) to \(M_n\):

\[
\sum_{m=J}^{M_n}F_{n,z}(e^{-m})
\le
\frac{C_1e^{-\kappa J}}{1-e^{-\kappa}}
+C_2(M_n+1)e^{-n^\delta}
+(M_n+1)u_n.
\tag{5.4}
\]

The last two terms tend to zero because \(M_n=O(\log n)\).  Hence

\[
\boxed{
\limsup_{n\to\infty}
\sum_{m=J}^{\lfloor c_*\log n\rfloor}
F_{n,z}(e^{-m})
\le C_\kappa e^{-\kappa J}
\quad\text{a.s.}
}
\tag{5.5}
\]

and therefore

\[
\boxed{
\lim_{J\to\infty}
\limsup_{n\to\infty}
\sum_{m=J}^{\lfloor c_*\log n\rfloor}
F_{n,z}(e^{-m})=0
\quad\text{a.s.}
}
\tag{5.6}
\]

for every fixed \(z\).

By (2.1), the same statement holds for the integral lower-log energy between scales \(e^{-J}\) and \(n^{-c_*}\).  Thus **all lower-log mass above the polynomial threshold \(n^{-c_*}\) is already uniformly integrable almost surely under the full source hypotheses.**

This is a useful localization of the open problem: only singular values *below* that polynomial scale can still obstruct the full a.s. Hermitization argument.

## 6. Exact residual obstruction below the polynomial threshold

On the probability-one event of (5.3), the count at the last mesoscopic bin obeys

\[
F_{n,z}(e^{-M_n})
\le
C n^{-\gamma}+O\!\left(\sqrt{\frac{\log n}{n}}\right)+o(1),
\tag{6.1}
\]

because \(\kappa c_*=\gamma\).  The source permits choosing \(\gamma>0\) small, and in particular below \(1/2\), so the displayed bound tends to zero.

Suppose in addition that at dimension \(n\) the polynomial floor

\[
s_n(A_n(z))\ge n^{-B}
\tag{6.2}
\]

holds.  If \(B\le c_*\), there is no unresolved lower-log interval below \(n^{-c_*}\).  If \(B>c_*\), then every dyadic-log bin below the mesoscopic cutoff and above \(s_n\) has CDF at most \(F_{n,z}(e^{-M_n})\), and there are at most

\[
(B-c_*)\log n+O(1)
\]

such bins.  Hence

\[
\sum_{m>M_n}F_{n,z}(e^{-m})
\le
\bigl((B-c_*)\log n+O(1)\bigr)
F_{n,z}(e^{-M_n})
\longrightarrow0.
\tag{6.3}
\]

Thus, on dimensions where the source's polynomial least-singular-value floor holds, **the entire** lower-log defect vanishes.  The only dimensions not covered by the argument are the failure events in (3.4), whose probabilities are of order \(\sqrt{\log n/n}\) and therefore are not summable over all \(n\).

This recovers the source's stated obstruction, but in a substantially sharper form: the nonsummability of the single bottom singular-value event is no longer contaminating a macroscopic range of singular values.  The intermediate/mesoscopic contribution is already a.s. controlled; the unresolved set is the extreme tail on the exceptional dimensions of (3.4).

## 7. New partial theorem — prescribed polynomial subsequences converge almost surely

The localization above turns the source's nonsummable estimate into a genuine theorem on deterministic sparse subsequences.

### Theorem 7.1

Fix \(p>2\) and

\[
n_j=\lceil j^p\rceil.
\]

Under the full heavy-tail hypotheses of Bordenave–Chafaï Theorem 6.2, with **no bounded-density assumption**, the empirical eigenvalue measures along this prescribed subsequence satisfy

\[
\boxed{
\mu_{n_j^{-1/\alpha}X_{n_j}}
\Longrightarrow \mu_\alpha
\quad\text{almost surely as }j\to\infty.
}
\tag{7.1}
\]

The statement is unchanged if the exact source normalization is denoted by \(a_n^{-1}\) instead of \(n^{-1/\alpha}\).

### Proof

Fix \(z\in\mathbb C\).  By (3.4),

\[
\sum_{j=1}^\infty
\mathbb P\bigl(s_{n_j}(A_{n_j}(z))<n_j^{-B}\bigr)
\le
C\sum_{j=1}^\infty
\sqrt{\frac{\log n_j}{n_j}}
<\infty,
\tag{7.2}
\]

because \(n_j\asymp j^p\) and \(p/2>1\).  Borel–Cantelli implies that (6.2) holds eventually along \(n_j\), almost surely.

The all-\(n\) mesoscopic theorem (5.6) and the extreme-tail estimate (6.3) therefore yield

\[
\lim_{J\to\infty}
\limsup_{j\to\infty}
\int_J^\infty F_{n_j,z}(e^{-u})\,du=0
\quad\text{a.s.}
\tag{7.3}
\]

Equivalently, by (1.3), the near-zero logarithmic part is uniformly integrable along \(n_j\).

The source's Theorem 6.3 already gives, for every fixed \(z\), almost-sure weak convergence of the singular-value measures \(\nu_{n^{-1/\alpha}X_n-z}\) to the deterministic \(\nu_{\alpha,z}\) along the full sequence.  The source's large-singular-value logarithmic control is also almost sure and is independent of the bounded-density assumption; the bounded-density assumption enters precisely in the missing near-zero step.  Therefore (7.3) supplies exactly the missing part of logarithmic uniform integrability along \(n_j\), and the logarithmic potentials converge along \(n_j\) for this fixed \(z\).

For every fixed \(z\), the preceding event has probability one.  Fubini on each bounded disk, followed by a countable exhaustion of \(\mathbb C\), gives one probability-one event on which the potential convergence holds for Lebesgue-a.e. \(z\).  The source's Hermitization/logarithmic-potential argument then applies verbatim along the deterministic subsequence and identifies the only possible eigenvalue limit with \(\mu_\alpha\).  This proves (7.1).  \(\square\)

### What this theorem does and does not say

This is stronger than the tautological fact that convergence in probability has *some* almost-sure subsequence: **every prescribed polynomial subsequence \(\lceil j^p\rceil\), \(p>2\), works.**

It is still a restricted result.  It does not control all dimensions, because the full series in (3.4) diverges.  Consequently it does not move the frozen source metric `BC_AS` from 0.

## 8. B6 — rigorous no-go for the naïve Gaussian-smoothing/Weyl route

The preceding run showed that fixed-\(\eta\) regularized logarithmic potentials are stable under Gaussian smoothing.  One tempting next step is to smooth the entries by a vanishing Gaussian, apply the source's bounded-density least-singular-value bound, and transfer back by Weyl perturbation.  The relevant powers are incompatible.

Let each raw entry be replaced by

\[
\xi^{(\sigma_n)}=\xi+\sigma_ng,
\]

where \(g\) is standard complex Gaussian.  The smoothed entry density obeys

\[
\|\phi_{\sigma_n}\|_\infty\le C\sigma_n^{-2}.
\tag{8.1}
\]

The source's bounded-density row-distance argument gives, for an unnormalized square matrix and deterministic shift,

\[
\mathbb P(s_n\le r_n)
\le C n^{5/2}r_n^2\|\phi_{\sigma_n}\|_\infty
\le Cn^{5/2}\left(\frac{r_n}{\sigma_n}\right)^2.
\tag{8.2}
\]

To make the right-hand side summable by a power margin one needs, for example,

\[
\frac{r_n}{\sigma_n}\le n^{-7/4-\varepsilon}.
\tag{8.3}
\]

On the other hand, transferring the same lower bound from the smoothed matrix to the original matrix by Weyl requires the Gaussian perturbation norm to be negligible relative to \(r_n\).  Since

\[
\|\sigma_nG_n\|\asymp \sigma_n\sqrt n
\]

with overwhelming probability, the direct Weyl route needs

\[
\frac{r_n}{\sigma_n}\gg \sqrt n.
\tag{8.4}
\]

Conditions (8.3) and (8.4) are incompatible by more than two powers of \(n\).

Equivalently, write \(\sigma_n=n^{-K}\) and the source-style target floor \(r_n=n^{-b-1/2}\).  Summability in (8.2) requires

\[
b>K+\frac54
\]

(up to a positive margin), whereas Weyl domination requires

\[
K>b+1.
\]

No \(b,K\) satisfy both.

Therefore:

\[
\boxed{
\text{vanishing Gaussian smoothing + the source bounded-density small-ball bound + direct Weyl transfer cannot close C0031.}
}
\tag{8.5}
\]

This is only a no-go for this **naïve transfer mechanism**.  It does not rule out Green-function comparison, Dyson-flow/three-step arguments, or other dynamical smoothing methods.

That distinction matters because Michail Louvaris's 2025 published work proves least-singular-value universality for a much more structured square Lévy ensemble using a three-step/Gaussian-perturbation strategy, rather than direct Weyl transfer.

## 9. Prior-art correction and current boundary

The previous admission/literature note missed one important later result and is corrected here.

1. **Bordenave–Chafaï (2012), source.** Theorem 6.2 gives the heavy-tailed eigenvalue law in probability generally and a.s. under bounded density, and explicitly attributes the missing general a.s. upgrade to slow in-probability small-singular-value control.
2. **Bordenave–Caputo–Chafaï (2011).** Earlier a.s. heavy-tailed spectral-limit results impose additional regularity/smoothness; they do not close the survey's general no-density endpoint.
3. **Michail Louvaris, arXiv:2204.06399, published Ann. IHP 61(1) (2025).** For square matrices with entries given by an exact stable law (and the paper's structured perturbation class), he proves Gaussian-universal behavior of the least singular value for all tail exponents outside a countable exceptional set, together with hard-edge delocalization.  The main theorem is for the unshifted square matrix and does **not** supply the arbitrary fixed complex shifts \(D_N-zI\) and the full stable-domain entry class required by C0031.  It is highly relevant technology, but it does not make C0031 KNOWN.
4. **Yi Han, arXiv:2412.06246 (2024/2025).** For strict rectangular aspect ratio \(N/n\to a>1\), symmetric heavy-tail entries admit arbitrarily high polynomial-confidence lower bounds at the correct \(n^{1/\alpha}\) scale, including deterministic rectangular deformation.  The strict rectangular gap avoids the square hard edge needed here.
5. **Dabagia–Fernandez, arXiv:2408.14389.** Their rectangular estimates require finite \(2+\beta\) moments or a different anti-concentration setup and do not directly settle the square infinite-variance source endpoint.

A bounded search dated 2026-09-18 did not expose a later theorem proving the full Bordenave–Chafaï no-bounded-density almost-sure eigenvalue convergence statement.  This search miss is negative evidence only, not a novelty/openness certificate.

## 10. Exact current blocker

The full source problem has now been localized to one narrow mechanism.

The all-\(n\) source machinery plus B18/B25 proves a.s. lower-log uniform integrability down to the polynomial threshold \(n^{-c_*}\).  On every dimension where the source polynomial least-singular-value floor holds, the remaining extreme tail also vanishes.  Hence a full-sequence proof can be obtained by *any* mechanism that prevents the nonsummable bad dimensions in (3.4) from contributing persistent logarithmic mass.

One need not necessarily prove a stronger pointwise least-singular-value probability estimate.  It would suffice, for example, to prove an almost-sure statement of the form

\[
\mathbf 1_{\{s_n<n^{-B}\}}
\frac1n\log\frac{n^{-c_*}}{s_n}
\longrightarrow0
\tag{10.1}
\]

(or the corresponding extreme-tail count version) for Lebesgue-a.e. shift \(z\).  This formulation leaves room for dependence across nested dimensions and for rare very-small singular values whose logarithmic contribution is still only \(1/n\).

This is the target to carry forward, rather than rebuilding the already-settled mesoscopic range.

## 11. Status and next methods

Frozen source metric:

`BC_AS: 0 -> 0` (**NO MOVEMENT**).

Mathematical movement below the binary source metric:

- exact dyadic equivalence for the lower-log defect;
- power-law expected small-singular counting bound on the full mesoscopic range;
- almost-sure mesoscopic lower-log uniform integrability for **all dimensions**;
- a complete theorem giving almost-sure heavy-tailed eigenvalue convergence along **every prescribed polynomial subsequence** \(n_j=\lceil j^p\rceil\), \(p>2\), with no bounded-density assumption;
- a rigorous no-go for direct Gaussian-smoothing + source density bound + Weyl transfer;
- corrected prior-art record incorporating Louvaris 2025.

The source remains **PARTIAL / OPEN**.  No independent P26 audit or distinct OTHER-track audit exists, and no closure/paper package is claimed.

Next nonrepeating Section-B triple:

- **B3 (prove something stronger):** target a summable or pathwise extreme-tail statement simultaneously in the shift parameter \(z\), stronger than fixed-\(z\) pointwise invertibility but tailored to logarithmic mass rather than raw \(s_n\).
- **B14 (find the group/structure acting):** classify the arithmetic/profile mechanisms responsible for the \(n^{-1/2}\)-scale probability loss in the source weak-invertibility proof, especially under the nested-array coupling across dimensions.
- **B29 (add the boundary):** compactify the bottom singular-value scale by adjoining the hard edge and test whether Louvaris-style three-step comparison or Han-style rectangular regularization controls precisely the extreme tail left after (5.6), without re-proving the mesoscopic estimate.

No code was needed in this run; the new claims are analytic consequences of cited source inequalities plus elementary tail summation and concentration.