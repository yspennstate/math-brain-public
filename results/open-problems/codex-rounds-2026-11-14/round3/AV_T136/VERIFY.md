# T136 verification — 15 November 2026

The earlier literature verdict survives independent rechecking: **PARTIAL-CLAIMED**, covering fixed finite inverse temperatures \(\beta>1\), with ground-state fluctuations outside the three candidates. A new analytic check establishes a bare-system supporting lemma, not the claimed fluctuation theorems.

The exact theorem blocks below were extracted from freshly opened repository sources and saved locally. The repository's opened LICENSE is Apache-2.0; its text is saved in sources/LICENSE-openai-math. Author of all three candidates: **OpenAI**. These are unrefereed claims; no conclusion about the correctness of their full proofs is made.

## Candidate 1: The low-temperature Sherrington–Kirkpatrick free-energy limiting law

Date: September 24, 2026. Opened the actual [introduction](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/01-introduction.tex), [Section 4](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/04-reduction.tex), and [foundations](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/02-foundations.tex). Local filenames appear in sources/INDEX.md.

Theorem 1.1, exactly:

```tex
\begin{theorem}[Limiting law]\label{thm:main}
For every fixed real $\beta>1$, there is a nondegenerate Borel probability measure $\nu_\beta$ such that
\[
 X_n(\beta)\ \Longrightarrow\ \nu_\beta
 \qquad\text{as }n\to\infty\text{ through all integers}.
\]
The measure $\nu_\beta$ has mean zero, variance one, and a finite exponential moment in a neighborhood of the origin. It is the unique probability measure with the moments specified in Proposition~\ref{def:law} below.
\end{theorem}
```

Its definitions are \(F_n=\log Z_n\), \(s_n^2=\operatorname{Var}(F_n)\), and \(X_n=(F_n-\mathbb EF_n)/s_n\), with exactly our \(n^{-1/2}\sum_{i<j}g_{ij}\sigma_i\sigma_j\), independent standard Gaussian couplings, Ising spins, and no field.

Theorem 1.2, exactly:

```tex
\begin{theorem}[Moment convergence at the fluctuation scale]\label{thm:moments}
For each fixed $\beta>1$, there are real numbers $a_k=a_k(\beta)$, $k\ge1$, with the following property. For every integer $k\ge1$, there are constants $c_k>0$ and $C_k<\infty$ such that
\begin{equation}\label{eq:moment-rate}
 \big|\mathbb E Y_n^k-a_k\big|\le C_k n^{-c_k},\qquad n\ge2.
\end{equation}
There are also constants $c>0$ and $C<\infty$, depending on $\beta$, for which
\begin{equation}\label{eq:exponential-moments}
 \sup_{n\ge2}\mathbb E e^{c|Y_n|}\le C.
\end{equation}
The limits satisfy $a_1=0$ and $0<a_2<\infty$.
\end{theorem}
```

Here \(F_n^c=F_n-n\log2+\zeta_n\), with independent \(\zeta_n\sim N(0,\beta^2/2)\), and \(Y_n=n^{-1/6}(F_n^c-\mathbb EF_n^c)\). Consequently its second-moment assertion claims
\[
 n^{-1/3}\operatorname{Var}(F_n)
 =\mathbb E Y_n^2-\frac{\beta^2}{2n^{1/3}}
 \longrightarrow a_2(\beta)\in(0,\infty).
\]
Thus the claimed standard deviation is asymptotic to \(\sqrt{a_2(\beta)}n^{1/6}\), rather than merely having this exponent.

The exact moment specification (Proposition 1.3) is included because the limiting law is not named:

```tex
\begin{proposition}[Moment specification]\label{def:law}
Fix $\beta>1$ and let $C=\sum_{l=2}^{\infty}l^{-2}$. For an integer $k\ge1$, draw an integer $J\ge2$ with
\[
 \mathbb P(J=l)=\frac{l^{-2}}C.
\]
Conditional on $J$, draw $k+1$ independent copies $F_J^{c,0},\ldots,F_J^{c,k}$ of the completed free energy in \eqref{eq:completed-free-energy}. Set
\[
 t=\log J,
 \qquad P_k=\prod_{i=1}^k J^{-1/6}(F_J^{c,0}-F_J^{c,i}).
\]
Conditional averaging over the independent comparison copies gives
$\mathbb E[P_k\mid J=l]=\mathbb E Y_l^k$.
The constants in Theorem~\ref{thm:moments} satisfy
\begin{equation}\label{eq:law-moments}
 a_k=C\sum_{h=0}^{\infty}
 \mathbb E\!\left[P_k\left(\frac{t^h}{h!}
       -\mathbf1_{\{h\ge1\}}\frac{t^{h-1}}{(h-1)!}\right)\right],
\end{equation}
where the second term is absent for $h=0$. Each expectation is taken before the series is summed. The series of these scalar expectations is absolutely convergent. We have $a_2>0$, and the law in Theorem~\ref{thm:main} is uniquely determined by
\[
 \int z^k\,\nu_\beta(dz)=\frac{a_k}{a_2^{k/2}},\qquad k\ge1.
\]
\end{proposition}
```

| Our statement | Comparison |
| --- | --- |
| Ising SK, iid standard Gaussian couplings, zero field | Exact match. |
| \(N^{-1/2}\sum_{i<j}g_{ij}\sigma_i\sigma_j\) | Exact normalization; only the size letter changes. |
| Dimension or range | Complete-graph mean-field model, no spatial dimension parameter; all integer sizes in the limit. |
| Each fixed \(\beta>1\) | Every finite real \(\beta>1\); constants may depend on it. No uniformity at \(\beta=\infty\). |
| \(\log Z_N(\beta)\) | Exact unnormalized logarithmic partition function, centered by its exact disorder expectation. |
| Order and limiting law | Claims a positive variance equivalent and full-sequence convergence after exact variance standardization. The law is specified through a convergent series of finite-system moments, without a named-distribution identification or explicit prefactor formula. |
| \(\max_\sigma H_N(\sigma)\) | Not included. Neither a zero-temperature fluctuation exponent nor a ground-state limiting law is claimed. |

## Candidate 2: The low-temperature Sherrington–Kirkpatrick fluctuation scale

Date: September 24, 2026. Opened the actual [introduction](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026/build/sections/introduction.tex). Main theorem, exactly:

```tex
\begin{theorem}\label{thm:main}
For every fixed $1<\beta<\infty$,
\[
 \sd(F_n)=n^{1/6+o(1)},\qquad \Var(F_n)=n^{1/3+o(1)}.
\]
More explicitly, for every $\eta>0$ there is $n_0(\beta,\eta)$ such that
\[
 n^{1/6-\eta}\le\sd(F_n)\le n^{1/6+\eta}
 \qquad(n\ge n_0(\beta,\eta)).
\]
Moreover, for every $\eta>0$,
\[
 \mathbb P\!\left(n^{1/6-\eta}\le|F_n-\mathbb EF_n|
                         \le n^{1/6+\eta}\right)\longrightarrow1.
\]
\end{theorem}
```

This paper includes \(\beta\) in its Hamiltonian and uses the probability spin sum \(2^{-n}\sum_\sigma e^{\beta H_n^{\rm ours}(\sigma)}\). Therefore its \(F_n=\log Z_n^{\rm ours}(\beta)-n\log2\); centered fluctuations and variance are exactly unchanged. The model, Gaussian law, zero field and every fixed finite \(\beta>1\) agree with ours. The theorem claims the exponent with arbitrary power slack, and typical centered absolute magnitude with that slack; it does not give two-sided constant multiples of \(n^{1/6}\), an asymptotic variance prefactor, or a limiting law. It expressly excludes temperature-uniform conclusions at 1 or infinity.

## Candidate 3: Full support of the zero-temperature Sherrington–Kirkpatrick order parameter

Date: September 27, 2026. Opened the actual [main source](https://github.com/openai/math/blob/main/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/build/main.tex). Main theorem, exactly:

```tex
\begin{theorem}[Full support at zero temperature]\label{thm:full-support}
If $\gamma\in\mathcal U$ minimizes $\mathcal P$, then
\[
 \supp\mu_\gamma=[0,1).
\]
In particular $\gamma(b)>\gamma(a)$ whenever $0\leq a<b<1$.
For the solution of~\eqref{eq:model-diffusion},
\begin{equation}\label{eq:main-consistency}
 \E[u_\gamma(t,X_t)^2]=t,\qquad
 \E[\Phi_{\gamma,xx}(t,X_t)^2]=1,
 \qquad 0\leq t<1.
\end{equation}
\end{theorem}
```

The finite-system Hamiltonian matches ours. However, \(\gamma\) minimizes the deterministic zero-temperature Parisi functional, and \(\mu_\gamma([0,t])=\gamma(t)\); the theorem concerns its support and diffusion consistency. It gives no sample-to-sample fluctuation order or limiting law for the finite-system maximum. Its scope for our requested quantities is NOT-THIS.

For clarity, writing \(M_n=\max_\sigma H_n(\sigma)\), the elementary inequality
\[
 0\le\beta^{-1}\log Z_n(\beta)-M_n\le n\log2/\beta
\]
also bounds the absolute difference of the centered variables by \(n\log2/\beta\). To make this bound negligible at scale \(n^{1/6}\) requires \(\beta_n/n^{5/6}\to\infty\). The first two candidates concern fixed \(\beta\) and give no such growing-temperature control. This explains a gap in what they imply, not a necessary condition for every possible zero-temperature argument.

## Independent recheck of the earlier result

The earlier folder was read without modification: REPORT.md, LOG.md, VERIFY.md, source snapshots and spot-check-arithmetic.txt. There is no earlier PROOF.md or computation script. Fresh quotations and normalization identities agree with its central conclusion.

The completion constant was also rederived two ways. If \(q=n^{-1}\sum_i\sigma_i\tau_i\), then
\[
 \operatorname{Cov}(\beta H_n(\sigma),\beta H_n(\tau))
 =\frac{\beta^2}{2}(nq^2-1).
\]
Adding independent spin-constant noise of variance \(\beta^2/2\) gives exactly \(n\beta^2q^2/2\). Independently, the ordered-matrix model
\[
 \frac{\beta}{\sqrt{2n}}\sum_{i,j}G_{ij}\sigma_i\sigma_j
\]
has off-diagonal couplings \((G_{ij}+G_{ji})/\sqrt2\), which are independent standard Gaussians, and spin-constant diagonal part \(\beta(2n)^{-1/2}\sum_iG_{ii}\), of variance \(\beta^2/2\). Thus the two normalization conventions really do differ only by the stated independent noise and deterministic shift.

The exact-arithmetic audit enumerates every pair of spin configurations at \(n=2,3,4\), checking both covariance formulas. It also rechecks the earlier three smoothing exponents and stencil order 23. These are finite algebra checks, not evidence of the asymptotic SK law.

## Follow-ups opened in this session

The literature refresh was limited to the requested brief search. No later settlement of the whole row, specific refutation, referee report, or expert verification of the limiting-law proof surfaced. This records the search outcome, not an assertion that none exists.

| Opened source | What it establishes about scope |
| --- | --- |
| P. M. Aronow and Patrick Lopatto, [Lower and Upper Bounds for Glauber Dynamics from Typical States of the Low-Temperature Sherrington–Kirkpatrick Model](https://hexagonmath.org/2610.00402v1), October 20, 2026; [actual PDF](https://hexagonmath.org/pdf/2610.00402v1), abstract, Section 1.4 and final discussion | Reports formalizing the exponent theorem and its positive-Laplace input. Distinguishes this from the prefactor and limiting-law claims, which it does not use. This is hexagon:2610.00402v1, not an arXiv identifier. |
| [fluctuations-palomar README](https://github.com/pmaronow/fluctuations-palomar/blob/main/README.md) | Advertises exponent results; excludes the positive variance prefactor and limit law. Historical protected verification is scoped to a named revision; fresh protected replay of the strengthened mean-bias interface remains pending. These are repository reports, not replayed here. |
| Yan Ru Pei, [Upper deviations of the Sherrington-Kirkpatrick free energy: the fifth-order law and the onset of constrained Parisi measures](https://arxiv.org/abs/2610.06480), submitted October 5, revised November 11, 2026 (v3); [actual HTML](https://arxiv.org/html/2610.06480v3), especially Section 10.2 | Studies upper large deviations with system size tending to infinity first. Explains the missing finite-size control at shrinking deviations and missing zero-temperature uniformity; it does not settle our central ground-state fluctuation problem. |
| OpenAI [EventuallyNatPos.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/SKFluctuations/EventuallyNatPos.lean) | The exported deduction takes an explicit PositiveLaplaceWindow hypothesis. It is conditional code for the exponent statement, not the prefactor or limiting law. |
| OpenAI [lean/docs/281.md](https://github.com/openai/math/blob/main/lean/docs/281.md) | Documents the support and ground-state-value formalization. These concern different assertions from the ground-state fluctuation problem. |

The earlier worker's broader exposition and manifest searches are documented in its VERIFY.md. They were read as prior evidence; they are not presented as fresh opens. No Lean build, kernel replay or independent statement-equivalence check was run.

Search queries and cache failures are recorded in LOG.md. No arXiv version of either fluctuation candidate was found in this refresh.

## Recommended replacement for “where it stands”

OpenAI's unrefereed *The low-temperature Sherrington–Kirkpatrick free-energy limiting law* (September 24, 2026), together with *The low-temperature Sherrington–Kirkpatrick fluctuation scale* (September 24, 2026), claims a positive variance equivalent of order \(N^{1/3}\) and a moment-characterized limiting law for exactly centered and standardized \(\log Z_N(\beta)\) at every fixed finite \(\beta>1\). P. M. Aronow and Patrick Lopatto subsequently report formalizing the exponent result, but the stronger variance-prefactor and limiting-law claims are not independently verified here. The ground-state fluctuation order and limiting law remain open on the evidence checked; *Full support of the zero-temperature Sherrington–Kirkpatrick order parameter* (September 27, 2026) concerns a different quantity.

## Spot check

The earlier worker left the stopped pressure-increment estimate unresolved. Its Section 4 reduction uses an augmentation lemma to turn variance bounds into uniform exponential moments. The new check isolates that analytic ingredient at bare endpoints, where no hierarchical transition kernels are present.

[PROOF.md](PROOF.md) proves directly that, for every finite Gaussian zero-field SK system, adding independent Exp(rate \(a\)) noise to completed or uncompleted log Z gives a log-concave density whenever \(0<a\le1\). The proof uses an exact spin-gauge identity to preserve the law of log Z under a pinned density, then applies the log-concave marginal theorem to a joint density on the convex epigraph of log Z. Gaussian completion is checked independently by convolution.

Conditional on \(V=\sup_n\operatorname{Var}(Y_n)<\infty\), this yields the explicit bound
\[
 \sup_n\mathbb E e^{t_0|Y_n|}\le\tfrac32\,3^{1/4},
 \qquad t_0=\frac{\log3}{8\sqrt{V+4}}.
\]
The added noise contributes variance four, checked both from its rate and from the distribution of its scaled version. The scalar tail bound is derived from Chebyshev and concavity of the logarithm of the survival function, rather than imported without constants.

An adversarial \(n=2\) calculation shows that unaugmented log Z itself need not have a log-concave density, so omitting the independent noise would invalidate this argument. Rates zero and greater than one, biased spin priors, and nonzero fields are not silently included.

This check finds no obstruction in the bare augmentation step. It neither proves the augmentation claim along all hierarchical physical paths nor supplies the stopped increment or its signed overlap estimates. The stronger SK claims therefore retain the status recorded above.

