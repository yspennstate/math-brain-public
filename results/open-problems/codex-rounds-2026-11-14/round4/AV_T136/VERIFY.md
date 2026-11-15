# T136 verification — 15 November 2026

The earlier literature verdict survives independent rechecking: **PARTIAL-CLAIMED**, covering fixed finite inverse temperatures \(\beta>1\), with ground-state fluctuations outside the three candidates. The new check extends the augmentation argument to finite Gaussian hierarchies and their fixed-site weak limits; it does not verify the fluctuation theorems.

The exact theorem blocks below were extracted from freshly opened repository sources and saved locally. The repository's opened LICENSE is Apache-2.0; its text is saved in sources/LICENSE-openai-math. Author of all three candidates: **OpenAI**. These are unrefereed claims; no conclusion about the correctness of their full proofs is made.

## Candidate 1: The low-temperature Sherrington–Kirkpatrick free-energy limiting law

Date: September 24, 2026. Opened the actual [introduction](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/01-introduction.tex), [Section 4](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/04-reduction.tex), and [foundations](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/02-foundations.tex). The fresh snapshots are listed in sources/INDEX.md. This session also opened Section 3, which specifies the physical clocks.

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

## Independent recheck and the new extension

Read both earlier REPORT.md and LOG.md files, round 3's PROOF.md and audit.py, and the original VERIFY.md. The original session has no PROOF.md or scripts. Neither earlier folder was modified.

The round-3 bare-system result holds under independent derivation. Gauge averaging gives E[h(F) exp(L_plus-F)]=E[h(F)]; adjoining independent Exp(rate rho) gives a joint density with exponent -|g|^2/2+L_plus-(1-rho)F-rho*u on u>=F. Its convex coefficients have the required sign for 0<rho<=1. The earlier tail-integral constant (3/2)*3^(1/4) and scaled independent-noise variance four also check independently.

The extension in [PROOF.md](PROOF.md) checks the source's **Augmentation along the physical paths** lemma, Section 4, label red:lem-augmentation. It proves the finite Gaussian hierarchy statement from normalized transitions and spin gauge symmetry, treats zero increments, and checks the physical cutoff in (P3) and (P6). Its remaining initial-continuation coefficient is at least x/2 after adding Exp(rate x/2); under terminal-mass normalization the exponential rate becomes x/(2a). The claim passes to every defining fixed-site weak limit; existence and identification of that limit remain an input of the source's construction. The stopped Lp density bound is derived with uniform constants from log-concavity and the positive Laplace stop. No stopped increment estimate, variance asymptotic, or limiting-law proof follows from this check alone.

## Follow-ups actually opened in this continuation

The initial search was limited to five minutes. No later settlement of the complete row, arXiv version of the two candidates, refutation, error report, referee report or expert verification of their complete proofs surfaced. This is a search result, not a claim of exhaustive absence.

| Opened primary source | Scope found |
| --- | --- |
| P. M. Aronow and Patrick Lopatto, [Lower and Upper Bounds for Glauber Dynamics from Typical States of the Low-Temperature Sherrington–Kirkpatrick Model](https://hexagonmath.org/2610.00402v1), October 20, 2026; [actual PDF](https://hexagonmath.org/pdf/2610.00402v1), title page, abstract and Section 1.4 | Reports formalizing the exponent theorem and its positive-Laplace input, not the positive variance prefactor or limiting law. The identifier belongs to Hexagon, not arXiv. |
| [fluctuations-palomar README](https://raw.githubusercontent.com/pmaronow/fluctuations-palomar/main/README.md) | Advertises five formal claims, explicitly excluding the limiting law and positive variance prefactor. Historical verification applies to named revisions; strengthened-interface protected replay remains pending. This is the authors' repository report; no replay was run here. |
| Yan Ru Pei, [Upper deviations of the Sherrington-Kirkpatrick free energy: the fifth-order law and the onset of constrained Parisi measures](https://arxiv.org/abs/2610.06480), v3, revised November 11, 2026; [actual HTML](https://arxiv.org/html/2610.06480v3), Section 10.2 | Studies upper large deviations. Its order of limits gives no central ground-state fluctuation law or temperature-uniform deduction from the fixed-beta candidates. |
| OpenAI, [EventuallyNatPos.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/SKFluctuations/EventuallyNatPos.lean) | Conditional exponent deduction with PositiveLaplaceWindow as an explicit input. Raw web open failed with a cache miss; the read-only connector opened the actual file. It is not a prefactor or limiting-law formalization. |
| OpenAI, [lean/docs/281.md](https://raw.githubusercontent.com/openai/math/main/lean/docs/281.md) | Documents ground-state-value identities and full relative support of an admissible zero-temperature minimizer. These are different assertions from ground-state fluctuations. The support claim is conditional on being a minimizer; it does not separately assert existence. |

Fresh preprint sources opened: [limiting-law Section 1](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/01-introduction.tex), [Section 2](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/02-foundations.tex), [Section 3](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/03-paths.tex), [Section 4](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/04-reduction.tex), the scale introduction and zero-temperature main linked above. The repository [LICENSE](https://raw.githubusercontent.com/openai/math/main/LICENSE) was opened; source quotations are reproduced under Apache-2.0. Sources and exact audit hashes are saved locally. No Lean build, kernel replay, repository checkout, git command, external message or post was made.

## Recommended replacement for “where it stands”

OpenAI's unrefereed *The low-temperature Sherrington–Kirkpatrick free-energy limiting law* (September 24, 2026), together with *The low-temperature Sherrington–Kirkpatrick fluctuation scale* (September 24, 2026), claims variance asymptotic to a positive constant times N^(1/3) and a moment-characterized limiting law for exactly centered and standardized log Z_N(beta) at each fixed finite beta>1. P. M. Aronow and Patrick Lopatto subsequently report formalizing the exponent result, while the stronger prefactor and limiting-law claims are not independently verified here. The ground-state fluctuation order and limiting law remain open on the evidence checked; *Full support of the zero-temperature Sherrington–Kirkpatrick order parameter* (September 27, 2026) concerns a different quantity.

## Spot check

The single selected ingredient is the hierarchical augmentation lemma, extending the bare-endpoint check in round 3. Its complete density proof, physical-clock identification, terminal-mass rescaling and weak-limit argument appear in [PROOF.md](PROOF.md). The full initial Gaussian marginal is preserved before pinning; after pinning it is only the distribution of the gauge-invariant continuation that must be preserved. The proof distinguishes these two statements explicitly.

The audit in [audit.py](audit.py) independently expands all telescoping coefficients, substitutes empty levels, and checks the length-four rate rescaling with exact rational arithmetic. Small two-level hierarchies use gauge-invariant finite atomic drivers to test transition normalization, the initial marginal, all terminal spin probabilities and pinned continuation moments. These probability identities need gauge symmetry rather than Gaussian drivers; log-concavity for the actual Gaussian hierarchy is proved analytically, not inferred from this finite check. A deterministic external-field countercheck deliberately breaks gauge symmetry and detects the failure of the assumed pin normalization.

Boundary cases checked in the proof include rate equal to the first mass, terminal revelation at mass a, repeated masses, zero increments, no future increment and a degenerate initial driver. The initial-cut property concerns the physical matrix and field clocks; variation of the auxiliary scalar clock below x does not reveal new physical drivers. In the normalized mass-four example x=1/8, the correct remaining coefficient is 1/64; keeping the exponential rate unscaled would give -1/32, which confirms why that rescaling must be explicit.

This check supports one lemma. The analytic stopped pressure-increment bound and its signed overlap estimates remain unverified, so the literature verdict remains PARTIAL-CLAIMED.

Audit outcome: 42 exact coefficient/empty-level cases, 67,072 leaf-spin cases, 50 exponential-transform checks, five verbatim quotations and five unchanged-source comparisons passed. The maximum positive-case pin-test discrepancy was below 4e-15. The command and full output are in LOG.md and audit.txt; the process had niceness 20 and used under 20 MB peak RSS. This is a supporting-lemma audit, with no Lean replay or numerical test of an asymptotic SK law.
