# T136 literature verification

Checked 14 November 2026. Verdict: **PARTIAL-CLAIMED**. The fixed-positive-temperature part is claimed; the ground-state fluctuation problem is not covered by these candidates. This records theorem scope and subsequent evidence, without certifying the proofs.

## 1. The low-temperature Sherrington–Kirkpatrick free-energy limiting law

Author: OpenAI. Date on manuscript: September 24, 2026. Opened the actual [main TeX file](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/main.tex), [introduction](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/01-introduction.tex), foundations, consequences and companion interface. Local copies are in `sources/candidate-1-*.tex`.

Theorem 1.1, exactly as in the source (including source labels):

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
Here the source defines exactly our Hamiltonian, \(F_n(\beta)=\log\sum_\sigma e^{\beta H_n(\sigma)}\), \(s_n(\beta)^2=\operatorname{Var}F_n(\beta)\), and \(X_n=(F_n-\mathbb EF_n)/s_n\). Expectations are over disorder. The variance-prefactor claim is supplied by Theorem 1.2, also quoted exactly:

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

In this theorem \(F_n^c=F_n-n\log2+\zeta_n\), with independent \(\zeta_n\sim N(0,\beta^2/2)\), and \(Y_n=n^{-1/6}(F_n^c-\mathbb EF_n^c)\). Thus it claims \(n^{-1/3}\operatorname{Var}F_n\to a_2(\beta)\in(0,\infty)\), because \(\operatorname{Var}Y_n=n^{-1/3}(\operatorname{Var}F_n+\beta^2/2)\). In particular the standard deviation is asymptotic to \(\sqrt{a_2(\beta)}n^{1/6}\).

The law is specified by Proposition 1.3 through finite-system moments, rather than identified with a named distribution. For completeness, its exact source statement is:

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

Comparison with our statement:

| Our requirement | Candidate 1 |
| --- | --- |
| Ising spins, iid standard Gaussian couplings, no field | Exact match. |
| \(N^{-1/2}\sum_{i<j}g_{ij}\sigma_i\sigma_j\) | Exact match; only the letter \(n\) changes. This is the complete-graph model, with no spatial dimension restriction. |
| Every fixed \(\beta>1\) | Exact match for each finite real \(\beta>1\). Constants may depend on \(\beta\). |
| Fluctuations of \(\log Z_N(\beta)\) | Exact quantity, not pressure per spin. Exact expectation centering and exact variance standardization are used. |
| Determine order and limiting law | Claims a positive variance equivalent and one full-sequence, moment-determinate limiting law. This is stronger than exponent bounds or subsequential convergence. Neither a closed-form prefactor nor a Gaussian/Tracy–Widom identification is claimed. |
| Fluctuations of \(\max_\sigma H_N(\sigma)\) | Not covered. No uniform estimates as \(\beta\to\infty\), no ground-state fluctuation exponent, and no ground-state limiting law. |

The paper is a complete claimed answer to the finite-temperature component under the ordinary meaning of a limiting law characterized by its moments. It is not a complete claimed answer to T136 as we stated it.

## 2. The low-temperature Sherrington–Kirkpatrick fluctuation scale

Author: OpenAI. Date: September 24, 2026. Opened the actual [build/paper.tex](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026/build/paper.tex), [introduction](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026/build/sections/introduction.tex), foundations, fluctuations and companion interface. Theorem 1.1, exactly:

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

The paper puts \(\beta\) inside the Hamiltonian and uses \(Z_n^{\rm paper}=2^{-n}\sum_\sigma e^{\beta H_n^{\rm ours}(\sigma)}\). Consequently \(F_n^{\rm paper}=\log Z_n^{\rm ours}(\beta)-n\log2\); the centered random variables and variances coincide exactly. Its internal Gaussian covariance completion adds independent spin-constant noise of variance \(\beta^2/2\), which it removes before stating the theorem.

Model, zero field and fixed finite \(\beta>1\) therefore match. Strength differs: \(n^{1/6+o(1)}\) establishes the exponent with arbitrary power slack, but not two-sided constant multiples of \(n^{1/6}\), a positive asymptotic variance prefactor, or a limiting law. The probability assertion additionally locates the typical centered absolute magnitude with the same power slack. The introduction expressly excludes uniform conclusions as \(\beta\) approaches 1 or infinity. Ground-state fluctuations are not claimed.

## 3. Full support of the zero-temperature Sherrington–Kirkpatrick order parameter

Author: OpenAI. Date: September 27, 2026. Opened actual [build/main.tex](https://github.com/openai/math/blob/main/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/build/main.tex). Theorem 1.1, exactly:

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

Here \(\mathcal U\) consists of nonnegative, nondecreasing, right-continuous, integrable functions on \([0,1)\), and \(\mu_\gamma([0,t])=\gamma(t)\). The functional is \(\mathcal P(\gamma)=\Phi_\gamma(0,0)-\frac12\int_0^1 t\gamma(t)dt\), with terminal datum \(\Phi_\gamma(1,x)=|x|\); the diffusion is \(dX_t=\gamma(t)\Phi_{\gamma,x}(t,X_t)dt+dB_t\), \(X_0=0\), and \(u_\gamma=\Phi_{\gamma,x}\).

The finite-system model in its introduction matches our pure zero-field Gaussian Ising SK model and covariance normalization \(\xi(t)=t^2/2\). The theorem concerns the support of a minimizer of a deterministic variational problem and associated diffusion moments. It does not concern sample-to-sample fluctuations of the finite-system maximum. Its use of the known limit \(n^{-1}\mathbb E\max H_n\to P_*\), and its algorithmic/value consequences, give no fluctuation order or limiting law for \(\max H_n\). Candidate verdict: NOT-THIS for T136's requested quantities, despite its related zero-temperature setting.

One cannot obtain the missing assertion simply by sending \(\beta\to\infty\) in Candidate 1: the elementary bound \(\max H_n\le\beta^{-1}\log Z_n\le\max H_n+n\log2/\beta\) has error of order \(n\) for fixed \(\beta\), much larger than \(n^{1/6}\). A theorem with temperature uniformity or a separate zero-temperature argument would be needed.

## Follow-ups and checks of publication status

The following primary sources were opened. They are evidence for the stated scope of later work, not an independent acceptance of any proof.

- [OpenAI repository README](https://github.com/openai/math/blob/main/README.md), [history.md](https://github.com/openai/math/blob/main/history.md), and all three manuscript READMEs: no withdrawal or correction notice for these candidates was present. The history records changes in other subjects through October 29. The author describes the collection as model-produced research data at different stages of verification. A quiet history file does not establish correctness.
- [OpenAI lean/formalization.yaml](https://github.com/openai/math/blob/main/lean/formalization.yaml), the `lean/docs/` and `lean/ComparatorChallenges/` directory listings, and [docs/281.md](https://github.com/openai/math/blob/main/lean/docs/281.md): the fixed-temperature fluctuation family is not listed as a formalized top-line result. The zero-temperature support theorem is documented under family 281, together with ground-state value identities. The absent `lean/docs/217.md` is not evidence that there is no related code.
- Actual [EventuallyNatPos.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/SKFluctuations/EventuallyNatPos.lean): the declaration `main_of_positiveLaplaceWindow (hw : PositiveLaplaceWindow) : MainFluctuationStatement` assumes its central Laplace-window input. It is a conditional formal deduction of Candidate 2's exponent statement, not a formal proof of Candidate 1's variance prefactor or limiting law.
- Actual [SKFullSupport.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/SKFullSupport.lean) and [SKSupport/Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/SKSupport/Main.lean): the former defines the challenge; its `sorry` is a statement placeholder. The latter supplies a proof of `full_support` conditional on `IsMinimizer W γ`. The scope is support and diffusion consistency, not ground-state fluctuations. No Lean build was run.
- P. M. Aronow and Patrick Lopatto, [Lower and Upper Bounds for Glauber Dynamics from Typical States of the Low-Temperature Sherrington–Kirkpatrick Model](https://hexagonmath.org/2610.00402v1), version 1 dated October 20, 2026: opened the landing page and the [actual PDF](https://hexagonmath.org/pdf/2610.00402v1), especially Sections 1.4, 20–22 and the discussion of the limiting law. It reports completing the exponent theorem's Lean proof, including the positive-Laplace-window input. It distinguishes this from Candidate 1's stronger claims, which it does not use. Its stated provenance is primarily AI-generated, with some parts understood by humans. This is a Hexagon identifier; the identical numeric arXiv identifier belongs to an unrelated paper.
- Opened the accompanying [fluctuations-palomar README](https://github.com/pmaronow/fluctuations-palomar/blob/main/README.md). It says Theorem 1.6 covers standard-deviation, variance and typical-magnitude exponents and proves the Laplace input internally. It expressly excludes a limiting law and positive variance prefactor. It reports historical protected verification at commit `5551e62264a270fd5dcd396f36389eaf77eddebc`; the current strengthened mean-bias interface has a fresh protected replay pending. These are the package's records; this verification did not reproduce them or certify statement equality. No registry acceptance is asserted by the README.
- Yan Ru Pei, [Upper deviations of the Sherrington-Kirkpatrick free energy: the fifth-order law and the onset of constrained Parisi measures](https://arxiv.org/abs/2610.06480), submitted October 5, 2026, latest revision November 11, 2026 (v3): opened the abstract page and [actual v3 HTML](https://arxiv.org/html/2610.06480v3). It cites all three OpenAI candidates and studies the constrained Parisi functional and upper large deviations with system size tending to infinity before the small deviation tends to zero. It does not replace the missing central ground-state fluctuation theorem. This is related later literature, not an arXiv version of the candidates.

- P. M. Aronow and Patrick Lopatto, [An \(N^{-7/10}\) Bound for the Finite-Size Bias of the Sherrington-Kirkpatrick Free Energy](https://hexagonmath.org/2610.00177v1), October 12, 2026: opened the landing page and [actual PDF](https://hexagonmath.org/pdf/2610.00177v1). Section 1.6 compares the two fluctuation preprints with mean-bias estimates. Its subject is the finite-size expectation bias, not a proof of the limiting law or the ground-state fluctuation exponent.
- Hang Du, Shuyang Gong, Brice Huang, and Zhangsong Li, [Free energy fluctuations of symmetric perceptron models up to and including criticality](https://arxiv.org/abs/2610.31736), October 22, 2026: opened the arXiv page and [actual HTML](https://arxiv.org/html/2610.31736v1). Its own theorems concern perceptron models. A citation of the SK result as background is not a verification of Candidate 1.
- Baseline sources opened: P. M. Aronow and Patrick Lopatto, [Quantitative Parisi formulas and fluctuations in the Sherrington-Kirkpatrick model](https://arxiv.org/abs/2609.09103), submitted September 8, 2026, whose abstract confirms both variance exponents for free energy and ground state; Elizabeth Collins-Woodfin and Han Gia Le, [Free energy fluctuations in SK and related spin glass models: A literature survey](https://arxiv.org/abs/2510.26960), latest revision November 7, 2025. The latter predates this release and is not a later assessment.

Searches for the exact candidate titles with `arXiv`, `error`, `refutation`, `OpenAI`, and `Lopatto comment` found no arXiv posting of these candidates, no specific refutation, and no referee report settling Candidate 1. This is a search outcome as of November 14, not a claim that none exists. No independent expert endorsement of the limiting-law proof was located.

The following later expositions and community pages were also opened; technical conclusions above come from the primary texts:

| Opened page | What it contributes |
| --- | --- |
| [Latent Seminar, Low-temperature SK free-energy fluctuations](https://lowrank.github.io/latent-seminar/OpenAI-Math/217-sk-fluctuations), dated October 6 | Separates exponent, variance prefactor and full-sequence law; expressly says it is not a complete proof verification. |
| [AI Proved What?, episode 217](https://aiprovedwhat.com/episodes/217-sherrington-kirkpatrick-fluctuation-law/), updated through October 27 | Points out the conditional OpenAI Lean input; led to inspection of the actual source. |
| [Closed Form, family 217](https://closedform.nishachay.tech/e/openai-math-2026-217/) | Popular account; its statement that no Lean is listed should not be confused with absence of conditional code or later external formalization. |
| [oai-math-revised, limiting-law page](https://mathcommunity.github.io/oai-math-revised/papers/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/) | No manually contributed notes; automatically collected notes are expressly unreviewed. Supplies links to the Hexagon follow-up and Lean code, checked above. |
| [Plectis Atlas, SKFullSupport](https://wcook04.github.io/plectis-atlas/statements/SKFullSupport.html) | Led to the actual support challenge and proof files. Its family-level assessment also includes QAOA, outside this row. |

## Recommended replacement for “where it stands”

OpenAI's unrefereed preprint *The low-temperature Sherrington–Kirkpatrick free-energy limiting law* (September 24, 2026), using its companion *The low-temperature Sherrington–Kirkpatrick fluctuation scale* (September 24, 2026), claims variance asymptotic to a positive constant times \(N^{1/3}\) and a uniquely moment-characterized limiting law for the exactly centered and standardized \(\log Z_N(\beta)\) at every fixed finite \(\beta>1\). A later AI-generated manuscript by P. M. Aronow and Patrick Lopatto reports a Lean proof of the exponent result, but the stronger variance-prefactor and limiting-law claims have not been independently verified here. The ground-state fluctuation exponent and limiting law remain open on the evidence checked; *Full support of the zero-temperature Sherrington–Kirkpatrick order parameter* (September 27, 2026) concerns the Parisi minimizer's support and does not settle them.


## Spot check

The central new estimate in the limiting-law paper is the proposition titled “Stopped pressure increments” (`prop:increment`) in [Section 4](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/04-reduction.tex). It is the single estimate on which the reduction to moments and the limiting law is conditional. Its proof is assembled in [Section 9](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/09-expansion.tex) and [Section 10](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/10-parameters.tex), both opened. The check below concerns its normalization, power count and use; it does not verify all of the preceding overlap estimates.

Put \(x=N^{-1/6}\), \(s=qx^{1+\varepsilon}\), and \(\mathcal K_m=sm\psi_m\). The claimed integrated per-site error is \(O(x^{5+c})\), with \(c>0\) independent of sufficiently small \(\varepsilon\). Since \(sm=O(x^{-5+\varepsilon})\), its contribution to the total log-Laplace comparison is \(O(x^{c+\varepsilon})\). This is the required positive saving. An error merely \(O(x^5)\) would not give the later cumulant comparison a positive saving independent of \(\varepsilon\).

The size-averaging calculation can be rederived directly. For weights \(w_m(n)\), \(n=Ne^\theta\), differentiate \(\sum_m w_m(n)sm\psi_m\). Moving the differentiation stencil from the weights onto \(m\psi_m\) gives
\[
 sn\sum_m w_m\left(\dot\psi_m+\sum_jc_j(m+j)\psi_{m+j}\right)
 +s\sum_mw_m(m-n)\dot\psi_m
 +O(sN^2D^{-r-1}),
\]
where \(D=x^{-1/2}\). The factor \(m+j\) in the proposition is necessary; a stencil on \(\psi\) alone would miss the derivative of the size factor. The three auxiliary exponents are \(sD=x^{\varepsilon+1/2}\), \(sN^2D^{-r-1}=x^{\varepsilon-11+(r+1)/2}\), and \(sNx^{12}=x^{\varepsilon+7}\). For example a fixed stencil order \(r=23\) gives exponent \(\varepsilon+1\) in the middle expression. Exact rational arithmetic reproducing these powers is saved in `sources/spot-check-arithmetic.txt`.

The parameter section's direct-path gains have the asserted signs: with \(s_*=1/2-\tau\), they are \(1-2s_*=2\tau>0\) and \((1-\eta)/2-s_*=\tau-\eta/2>0\) when \(\eta<2\tau\), as required by its stricter ordering. Its cutoff condition \((1-\eta)/s_*-2>0\) is the same inequality. Once the polynomial loss constants and Taylor orders are fixed, choosing the later cutoffs and \(p_*\) small can satisfy the displayed positive-margin inequalities. This checks their algebraic compatibility; it does not prove the constants were independent of all later choices in earlier sections.

Finally the reduction extracts a fixed \(k\)-th cumulant from positive tests at spacing \(x^\varepsilon\). The comparison error becomes \(O(x^{c'-(k-1)\varepsilon})\), and the Taylor remainder becomes \(O(x^{\varepsilon-o(1)})\). Taking \(k\varepsilon<c'/2\) leaves a positive power; summing dyadic errors is then legitimate. If the limiting scaled variance were zero, the claimed power rate would contradict the companion's lower bound \(\operatorname{Var}Y_n\ge n^{-2\eta}\) for every fixed \(\eta>0\). These deductions are consistent with the stated estimate.

No arithmetic or normalization obstruction appeared in this restricted check. The load-bearing unresolved verification is whether the uniform signed overlap/cavity bounds really establish `prop:increment`, especially its size-varying version and its saving independent of the Laplace-test exponent. The calculation above does not certify that proposition or the limiting-law proof. It supplies no zero-temperature extension.
