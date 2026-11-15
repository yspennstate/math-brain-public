PARTIAL

# E0057: consistency and sample complexity of multireference alignment

Task: “Open problem E0057”, received 13 November 2026 at approximately 08:56 +04 (Asia/Tbilisi). Literature checked on that date. No claim of a new general solution is made.

The marginal maximum likelihood estimator is consistent, including for nongeneric signals. The generic fixed-dimensional sample-complexity exponent is also known: six at high Gaussian noise with uniform shifts. Those facts do **not** establish consistency of the source's quasi-MLE after power correction. Its global population identification problem remains unresolved by the primary sources checked here and by this work. The two interpretations of power correction—correcting the unconstrained quasi estimate afterward, and imposing the power constraint during optimization—also require separate arguments. Thus the stopping condition for `RESOLVED_IN_LITERATURE` is not met when the source's quasi-MLE branch is retained.

The proofs below establish marginal-MLE consistency, including estimated-power constraints; identify precisely the missing quasi-MLE step; give a small-noise bound for hard alignment; and prove a nongeneric obstruction to a universal σ⁶ law. These are rederivations or consequences of known methods, not claimed novel resolutions. Numerical evidence is reported separately from theorems.

## 1. Exact source and model

The source is Afonso S. Bandeira, [*Ten Lectures and Forty-Two Open Problems in the Mathematics of Data Science*](https://people.math.ethz.ch/~abandeira/TenLecturesFortyTwoProblems.pdf). The retained version has 152 PDF pages, with printed and PDF page numbers agreeing here. Section 10 occupies pp. 132–140. The full section was read, including the synchronization discussion and the MRA subsection. Its plain text is `sources/bandeira_notes.txt`; provenance is in `sources/manifest.json`.

Equation (108), p. 136, is

\[
Y_i=R_{s_i}u+\sigma\xi_i,\qquad u\in\mathbb R^L,
\quad s_i\in\mathbb Z_L,\quad \xi_i\stackrel{\mathrm{iid}}\sim N(0,I_L).
\]

The shifts are **arbitrary unknown shifts**; this passage does not prescribe a random distribution for them or impose genericity on the signal. In the arguments below fixed shifts, or shifts independent of the Gaussian noises, are allowed. Observation-dependent adversarial shifts are not assumed.

The source's quasi-MLE is (109)–(110), pp. 136–137:

\[
\widehat s\in\arg\max_{s_1,\ldots,s_n}
 \sum_{i,j}\langle R_{-s_i}Y_i,R_{-s_j}Y_j\rangle,
\qquad \widehat v={1\over n}\sum_iR_{-\widehat s_i}Y_i.
\tag{1}
\]

Writing \(a_i=R_{-s_i}Y_i\), the identity

\[
\sum_{i,j}\|a_i-a_j\|^2=2n\sum_i\|a_i-\bar a\|^2
\]

shows that this is equivalent to joint optimization over the signal and all shifts, or profiling them out:

\[
\widehat v\in\arg\min_v Q_n(v),\qquad
Q_n(v)={1\over n}\sum_i\min_s\|Y_i-R_sv\|^2.
\tag{2}
\]

By contrast, the **marginal** MLE, for uniform random shifts, maximizes

\[
\ell_n(v)={1\over n}\sum_i\log p_v(Y_i),\qquad
p_v(y)={1\over L}\sum_{s=0}^{L-1}\varphi_\sigma(y-R_sv).
\tag{3}
\]

A maximum and a log of a sum in these objectives cannot be interchanged at fixed σ. EM is an optimization algorithm for (3); a finite EM run need not find its global maximum. The notes do not separately define a marginal likelihood in this subsection, so identifying (3) with every occurrence of “MLE” in the historical question would hide an ambiguity.

Use the unitary DFT \(F\) and orbit distance
\(d(v,u)=\min_s\|v-R_su\|\). The power spectrum is \(P_k=|(Fu)_k|^2\). Independently of the shifts,

\[
\widehat P_k={1\over n}\sum_i|(FY_i)_k|^2-\sigma^2\longrightarrow P_k,
\qquad
\widehat a_k=\sqrt{\max(\widehat P_k,0)}\longrightarrow |(Fu)_k|.
\tag{4}
\]

For an unnormalized DFT the subtraction is \(L\sigma^2\). The signed DC coefficient is estimated separately by averaging the DC observations; power alone loses its sign. For even L the real Nyquist coefficient has a discrete sign choice too. The notes say that the quasi estimate has power bias and conjecture consistency of its Fourier phases, but give **no unique formula** for “fixing the power spectrum.” We therefore distinguish:

- **Post correction:** take the phases of the unconstrained estimate (1)/(2), replace its Fourier magnitudes by (4), and use the signed DC estimate.
- **Constrained hard alignment:** minimize (2) on the set with prescribed Fourier magnitudes and signed DC.
- **Constrained marginal likelihood:** maximize (3) on that set.

The last estimator is covered by the KL proof below. That proof does not cover the first two.

## 2. Literature verdict

The exact numbers below refer to the **specific retained text versions**, unless printed journal pagination is explicitly stated. Journal and preprint theorem numbering need not coincide. Each text has `PDF PAGE` markers. Full URLs and hashes appear in `sources/manifest.json`; a more detailed audit is in `sources/LITERATURE_AUDIT.txt`.

| Primary source | Exact location checked | What it establishes and its limitation |
|---|---|---|
| Perry–Weed–Bandeira–Rigollet–Singer, *The Sample Complexity of Multireference Alignment*, SIAM J. Math. Data Sci. 1 (2019), 497–517 | **Theorem 3.1**, printed p. **504**, PDF p. **8**; **Theorem 4.3**, printed p. **507**, PDF p. **11**; arbitrary-to-uniform reduction, printed p. **498** | Generic, nonzero Fourier coefficients: lower bound \(n\gtrsim\sigma^6\varepsilon^{-2}\), and a constructive upper bound \(n\ge\sigma^6\varepsilon^{-2}\operatorname{poly}(L,1/\min|\widehat u_k|,1/\delta)\). Fixed scale/norm bounds and known noise. Arbitrary shifts can be uniformly randomized, so the upper bound covers the source. Uniform shifts supply a worst-case lower bound. This is an exponent result with conditioning and dimension factors, not a universal leading constant. |
| Brunel, *Learning rates for Gaussian mixtures under group action*, COLT 2019, PMLR 99:471–491 | **Theorem 9**, PDF p. **9**, proof p. **10**; **Corollary 10**, p. **10**; **Theorem 12**, p. **11** | Consistency of the global marginal MLE for **every** signal under a finite orthogonal group and uniform mixture weights. Known positive noise can be rescaled to one. Trivial stabilizer gives the usual pointwise root-n behavior; symmetric signals have an additional n⁻¹/⁴ component. These are fixed-noise statements, not uniform σ-rate constants, and concern neither the quasi-MLE nor arbitrary EM outputs. The downloadable PDF uses internal pages 1–21 and a slightly different title (“group invariance”). |
| Bandeira–Rigollet–Weed, *Optimal rates of estimation for multi-reference alignment*, Math. Stat. Learn. 2 (2019), 25–75, published 26 February 2020 | Retained arXiv:1702.08546: **Theorems 1–2**, pp. **8–9**; general MLE **Theorem 4**, pp. **10–11**; discrete **Theorem B.1**, pp. **24–25**, and **Proposition B.2**, p. **25** | Main model is continuous circle phase shifts, with restrictions on Fourier support and nonzero coefficient size. Those main rates must not be substituted directly for discrete cyclic MRA. Appendix B gives discrete worst-case norm-error lower bound \(\gtrsim\min(\sigma^L/\sqrt n,1)\); pure harmonics cause it. Nongeneric signals are therefore not an unstudied footnote or covered by the generic σ⁶ assertion. |
| Abbe–Bendory–Leeb–Pereira–Sharon–Singer, *Multireference Alignment is Easier with an Aperiodic Translation Distribution* | arXiv:1710.02793: **Theorem III.1**, PDF p. **4**; **Theorem IV.1**, p. **6**; **Corollary IV.4** and **Theorem IV.5**, p. **7** | For an **unknown aperiodic shift law**, with nonvanishing signal DFT and the spectral method's stated distinct-entry condition (obtainable by reshuffling), the first two moments identify the signal and distribution up to shift. Recovery requires/suffices at scale \(n/\sigma^4\to\infty\). This is **σ⁴, not σ²**. Some nonuniform periodic laws retain a third-moment obstruction. |
| Bendory–Boumal–Ma–Zhao–Singer, *Bispectrum Inversion with Application to Multireference Alignment* | arXiv:1705.00641: **Propositions II.1–II.3**, PDF p. **4** | Identifiability under specified Fourier-support assumptions, local stable inversion for nonvanishing DFT, and estimation from \(C(u,\delta,p)(\sigma^2+\sigma^6)\) observations. Gives a consistent invariant estimator, not a theorem identifying hard-profile population minima. |
| Bendory–Edidin–Leeb–Sharon, *Dihedral multi-reference alignment* | arXiv:2107.05262: **Theorem 2.3**, PDF p. **5**; **Corollary 1.2**, p. **2** | For generic signal **and** generic unknown distribution over the dihedral group, the first two moments identify the orbit; the necessary high-noise condition stated is \(n/\sigma^4\to\infty\). Reflections enlarge the ambiguity group. This is a different paper/authorship and model from the preceding Abbe et al. cyclic result. |
| Fan–Sun–Wang–Wu, *Likelihood landscape and maximum likelihood estimation for the discrete orbit recovery model* | arXiv:2004.00041: **Theorem 3.3**, PDF p. **22**; **Theorem 4.28**, **Corollaries 4.29–4.30**, p. **55** | Marginal-likelihood landscape: benign at sufficiently low noise for distinct orbit points; phase surrogate and σ⁻⁶ curvature at high noise. Spurious high-noise optima occur on open signal sets for even L≥6, and also in sufficiently large odd dimension (the cited corollary gives L≥53). A global MLE consistency theorem cannot be read as an EM guarantee. These are not hard-profile-loss results. |
| Katsevich–Bandeira, *Likelihood Maximization and Moment Matching in Low SNR Gaussian Mixture Models* | arXiv:2006.15202: **Theorem 2.1**, PDF p. **8**, discussion pp. **8–9** | For compactly supported mixing laws whose lower moments agree, the marginal population negative log likelihood first differs by \(\|\Delta M_m\|^2/(2m!\sigma^{2m})\), with controlled remainder. Explains successive moment matching, but does not convert hard assignment into marginal likelihood. |
| Dou–Fan–Zhou, *Rates of estimation for high-dimensional multi-reference alignment*, Ann. Statist. 52 (2024) | arXiv:2205.01847: **Theorems 2.1–2.2**, PDF p. **6**; MLE **Theorem 5.2**, pp. **13–14** | Continuous rotations, controlled Fourier magnitudes (including stated power-law classes), dimension K. High-noise squared risk \(\asymp K^{4\beta}\sigma^6/n\); low-noise \(\asymp K\sigma^2/n\) under separate sample-size/noise conditions. The low-noise MLE analysis is not a discrete quasi-MLE theorem. |
| Romanov–Bendory–Ordentlich, *Multi-reference alignment in high dimensions: sample complexity and phase transition* | arXiv:2007.11482, readable text: **Theorem 2.1**, PDF p. **4**; **Theorem 2.2**, p. **5** | Bayesian Gaussian signal, L→∞, \(\alpha=L/(\sigma^2\log L)\). Above α=2 the sample complexity approaches the aligned Gaussian benchmark in the stated iterated limits; below it a harder regime occurs. Different asymptotics from fixed L, σ→∞. |
| Shahverdi–Ström–Andén, *Moment Constraints and Phase Recovery for Multireference Alignment*, 2025 revision | **arXiv:2409.04868v2 PDF:** **Proposition 2.14**, **Corollary 2.15**, p. **10**; **Proposition 3.7**, **Conjecture 3.8**, p. **15**; **Theorem 3.9**, pp. **16–17** | Directly relevant fixed-power hard-alignment loss. Establishes uniform convergence, critical points, and a local minimum theorem for a single sinusoid at odd length. It explicitly leaves global identification as a conjecture. The arXiv HTML numbers these results differently: Conjecture 23 and Theorem 24. Neither uniform convergence nor stationary-value convergence of its algorithm proves consistency. |
| Balanov–Huleihel–Bendory, arXiv:2505.21435, originally *Two Pitfalls and One Remedy*, downloaded revision dated 12 February 2026 titled *Expectation-Maximization for Low-SNR Multi-Reference Alignment* | **Theorem 3.3**, PDF p. **18**; **Theorem 4.1**, p. **24**; **Theorem 6.4**, pp. **34–35** | Local population EM dynamics, initialization effects, and a necessary σ⁶-scale sample condition for accurate empirical fixed points under the stated local assumptions. Does not settle generic hard-profile consistency or certify the output of an arbitrary finite EM run. |
| Balanov–Bendory–Edidin, *Sample complexity of weak-signal latent-variable models*, October 2026 | arXiv:2610.24770: **Theorem 3.6**, PDF pp. **18–19**; **Theorems 4.7 and 4.9**, p. **24** | General marginal-MLE fixed-accuracy bound and global/local moment-based rates under explicit compactness, separation, and likelihood-envelope hypotheses. Distinguishes local and global identification order. It does not assert a hard-profile-MLE result. |
| Balanov–Katz–Bendory–Edidin, *Projected multi-reference alignment*, 2026 | arXiv:2605.25533: **Theorem 1.1** and **Corollary 1.2**, PDF p. **5**, precise **Theorem 3.1**, p. **11** | Odd dimension ≥7, a specified reflection-symmetric projection, generic third-moment orbit identification and σ⁶ scaling. This is a projected model, not a resolution of the source's hard-alignment question. |

A known, invertible shift-convolution law provides a simple **σ²** example: if ρ is known and \(C_\rho\) is invertible, \(\mathbb EY=C_\rho u\), so \(C_\rho^{-1}\bar Y\) estimates u with high-noise squared error O(σ²/n). “Nonuniform” by itself guarantees neither known ρ nor invertibility. The source makes neither assumption.

A 2026 functional deconvolution paper, Al-Ghattas–Little–Sanz-Alonso–Sweeney, was checked at the [publisher's page](https://epubs.siam.org/doi/full/10.1137/25M1765602). Its functional observation model differs, and no theorem from it is used as a resolution. Searches also surfaced an October 2026 online single-mode profile-consistency contribution; it is not relied on as a primary published theorem or as a solution for generic multimode signals. The literature search is a documented search, not a proof that no later result exists.

**Precisely what remains:** establish, or refute, phase consistency of the original global quasi-MLE after post correction for general signals and fixed positive σ. For the constrained alternative, establish that its population minimizers are exactly the true cyclic orbit. A sharp universal constant cannot be inferred from the exponent results and is not well posed without fixing signal normalization/class, error loss, and confidence. Optimal dependence on all of L, σ, Fourier conditioning, accuracy and algorithm is not supplied by a single σ⁶ slogan.

## 3. Complete proofs

### Theorem A: marginal-MLE consistency, without genericity

Fix L and σ>0. Let u be any real signal. Every sequence of global marginal MLEs (3), or approximate maximizers with normalized log-likelihood error tending to zero, converges almost surely in orbit distance to u. This holds for uniform iid shifts; the same uniform-mixture criterion is consistent for arbitrary fixed shifts as in the source. No power correction is needed. Maximizing (3) over the true power spectrum, or a consistently estimated power spectrum with signed DC, is also consistent.

**Proof.** Remove the term independent of v from the log density and write

\[
m_v(y)=-\frac{\|v\|^2}{2\sigma^2}
 +\log\left(\frac1L\sum_s e^{\langle y,R_sv\rangle/\sigma^2}\right).
\]

First prove identification. If \(p_v=p_u\), divide their characteristic functions by the everywhere nonzero characteristic function of the Gaussian. The finite atomic measures
\(L^{-1}\sum_s\delta_{R_sv}\) and \(L^{-1}\sum_s\delta_{R_su}\) agree. For completeness, equality of their exponential sums implies equality of coefficients: choose a vector a whose inner products with the finitely many distinct atoms are distinct, restrict the characteristic functions to ta, and differentiate at t=0 through order one less than the number of atoms. The resulting Vandermonde matrix is invertible. Thus the supports agree, and in particular v is some shift of u. This also works when orbit points repeat.

For uniform shifts,

\[
\mathbb E_u[m_u(Y)-m_v(Y)]
 =D_{\rm KL}(p_u\|p_v)\ge0,
\]

with equality exactly when \(d(v,u)=0\). Log densities are integrable because their absolute values on a bounded parameter set are bounded by a constant times \(1+\|Y\|^2\).

Next localize the maximum. Set \(A_n=n^{-1}\sum_i\|Y_i\|\). Since \(m_0=0\), the inequality

\[
{1\over n}\sum_i m_v(Y_i)
 \le -\frac{\|v\|^2}{2\sigma^2}
       +\frac{A_n\|v\|}{\sigma^2}
\]

implies \(\|\widehat v_n\|\le2A_n\) for a global maximizer. Also the objective tends to minus infinity with \(\|v\|\), so a maximum exists by continuity. Approximate maximizers with error η_n satisfy
\(\|\widehat v_n\|\le A_n+\sqrt{A_n^2+2\sigma^2\eta_n}\).
The strong law makes this eventually a deterministic bounded ball, enlarged if necessary to contain u.

On \(\|v\|,\|w\|\le B\), differentiation of the finite log-sum-exp gives

\[
|m_v(y)-m_w(y)|\le\frac{B+\|y\|}{\sigma^2}\|v-w\|.
\tag{5}
\]

Cover the ball by a finite δ-net. The strong law at each net point controls its empirical mean; (5) controls interpolation with an integrable Lipschitz envelope. Taking a countable sequence δ↓0 proves uniform almost sure convergence on the ball. The continuous population objective has a strictly positive gap from its maximum on the compact set \(\{v:\|v\|\le B,d(v,u)\ge\varepsilon\}\). Uniform convergence and η_n→0 exclude this set for all sufficiently large n. This proves consistency.

For arbitrary fixed shifts, \(m_v(R_sy)=m_v(y)\) for every v. Consequently the *whole indexed random criterion*, as well as \(\|Y_i\|\), has the same distribution as when observations are u+σξ_i, and also as under the uniform mixture. Rotating each noise by the inverse true shift leaves independent standard Gaussians. Thus the preceding strong laws and expected KL criterion still apply. Independent random shifts of any distribution give the same conclusion. This explains exactly why this use of uniform likelihood does not add a uniform-shift assumption to the source's consistency statement.

For the power-constrained estimator, the parameter set

\[
K(a,c)=\{v\in\mathbb R^L: |(Fv)_k|=a_k\ (k\ne0),\ (Fv)_0=c\}
\]

is compact. Equation (4) and the DC strong law give \((a_n,c_n)\to(a,c)\) almost surely, even using the same observations as the likelihood. These sets lie eventually in one ball and converge in Hausdorff distance: preserve the conjugate-symmetric phases, change magnitudes coordinate by coordinate, and choose the real self-conjugate signs consistently. At zero target magnitudes, any phase or sign has vanishing contribution. In particular there exist \(w_n\in K(a_n,c_n)\) with \(w_n\to u\). If an approximate constrained maximizer stayed away from the orbit, compactness would yield a subsequential limit v away from it. Uniform convergence, comparison with w_n, and continuity would give \(\mathbb Em_v\ge\mathbb Em_u\), contradicting KL identification. No independence between power estimation and optimization is required. ∎

**Scope.** Brunel already proves marginal-MLE consistency in probability. The proof above records the strong consistency and moving-constraint argument explicitly. It does not use the erroneous shortcut that treats (2) as a log density. Unknown σ is not covered here. Joint estimation of an unknown shift distribution is not needed to cover the source, since the uniform criterion itself is shift invariant.

### Theorem B: what the quasi-MLE uniform law actually proves

On any compact K, define
\[
Q(v)=\mathbb E\min_s\|u+\sigma\xi-R_sv\|^2.
\]
Then \(\sup_{v\in K}|Q_n(v)-Q(v)|\to0\) almost surely. Every approximate global minimizer approaches \(\arg\min_K Q\). The same assertion holds with consistently estimated power sets, with the limiting minimizer set taken on the true power set. Consistency follows **if** that set is the true orbit, but the uniform law does not establish that identification.

**Proof.** For \(\|v\|,\|w\|\le B\),

\[
\left|\min_s\|y-R_sv\|^2-\min_s\|y-R_sw\|^2\right|
 \le2(\|y\|+B)\|v-w\|.
\]

This follows by comparing a minimizing shift on one side and then reversing v,w. The loss has integrable envelope \((\|Y\|+B)^2\). The finite-net strong-law proof used in Theorem A therefore applies. Outside any open neighborhood of the compact population argmin set, continuity and compactness give a positive loss gap. Uniform convergence excludes that complement for empirical approximate minimizers. For moving power sets, Hausdorff convergence supplies comparison points approaching each fixed population minimizer, and compactness supplies subsequential limits of empirical minimizers. These limits must minimize Q. Finally, the hard loss is invariant to shifts of y, so arbitrary fixed shifts are again allowed. ∎

A normalized function \(\exp[-\min_s\|y-R_sv\|^2/(2\sigma^2)]\) would require a v-dependent normalizing integral in general. Even on a fixed-power family where a symmetry can make that integral constant, this hard density is **not** the true soft Gaussian mixture. Consequently its expected contrast is not the KL divergence used in Theorem A. Gaussian-mixture identifiability cannot fill the missing population-gap step.

Further, post correction of an unconstrained minimizer need not minimize Q on the fixed-power set. Theorem B addresses the constrained variant; it does not silently transfer a conclusion to the source's post-corrected estimator.

### Theorem C: a valid small-noise bound for hard alignment

Suppose the constraint set contains u. Every global population hard-loss minimizer v satisfies
\[
d(v,u)\le2\sigma\sqrt L.
\tag{6}
\]
For an empirical minimizer with loss excess at most η_n, the corresponding bound is
\[
d(v_n,u)\le2\left({1\over n}\sum_i\|\sigma\xi_i\|^2\right)^{1/2}+\sqrt{\eta_n}.
\tag{7}
\]
These also hold without a power constraint.

**Proof.** Distance to a finite orbit is 1-Lipschitz in the observation. Pointwise,
\(d(v,u)\le d(v,u+\sigma\xi)+\|\sigma\xi\|\).
Taking L² norms gives \(d(v,u)\le\sqrt{Q(v)}+\sigma\sqrt L\).
Since \(Q(v)\le Q(u)\le\sigma^2L\), (6) follows. The same triangle inequality and Euclidean norm on the n observations give
\(d(v_n,u)\le\sqrt{Q_n(v_n)}+(n^{-1}\sum_i\|\sigma\xi_i\|^2)^{1/2}\).
Use \(Q_n(v_n)\le Q_n(u)+\eta_n\), \(Q_n(u)\le n^{-1}\sum_i\|\sigma\xi_i\|^2\), and \(\sqrt{a+b}\le\sqrt a+\sqrt b\). Shift invariance removes the true shifts. ∎

For fixed σ>0 this bound does not tend to zero with n. It is a bound in a different, small-noise limit, not a consistency proof for the open branch.

### Theorem D: a complete nongeneric obstruction

Consider uniform cyclic shifts, a known nonzero amplitude a, zero mean, and a real signal whose only nonzero unitary Fourier coefficients are
\[
(Fu_\theta)_k=ae^{i\theta},\qquad
(Fu_\theta)_{-k}=ae^{-i\theta},\qquad
q=L/\gcd(k,L)\ge3.
\]
The phase is identifiable modulo 2π/q. All orbit moment tensors of order less than q are independent of θ; the qth moment identifies it. At fixed L,a and sufficiently high noise, minimax accurate estimation in this family has sample exponent **2q**, even though the power spectrum is known exactly. In particular k=1 gives exponent 2L, including L=5 where the exponent is ten.

**Proof of moment statements and sufficiency.** A degree-r Fourier monomial contains p factors from frequency k and t from −k, with p+t=r. Uniform shift averaging kills it unless q divides p−t. If r<q, the only possibility is p=t, so the surviving monomial is independent of θ. Multilinearity and the invertible Fourier transform imply the same assertion for the full moment tensor. At degree q,
\[
\mathbb E[(FY)_k^q]=a^qe^{iq\theta}.
\]
Indeed the shift multiplies this expression by a qth root raised to q, hence by one. The Fourier noise at this non-self-conjugate frequency is circular complex Gaussian η with \(\mathbb E|\eta|^2=\sigma^2\) and \(\mathbb E\eta^j=0\) for j≥1, so it adds no bias to this holomorphic moment.

For W=(ae^{iθ}+η)^q,
\[
\operatorname{Var}(W)=\sum_{j=1}^q{q\choose j}^2a^{2(q-j)}j!\sigma^{2j}.
\tag{8}
\]
Expand W and its conjugate; circular symmetry removes unequal powers and \(\mathbb E|\eta|^{2j}=j!\sigma^{2j}\). Thus the sample average has mean-square error at most \(C_{a,q}\sigma^{2q}/n\) for σ≥1. Taking its phase divided by q gives a phase estimate modulo 2π/q. Near the nonzero target a^qe^{iqθ}, argument is Lipschitz. On the complement, Chebyshev bounds its probability by the same moment-error scale. Orbit squared error is bounded in this fixed-amplitude family. Therefore, for fixed small ε and fixed confidence, \(n\ge C_{a,q}\sigma^{2q}\varepsilon^{-2}\) suffices. Consistency follows when n/σ^{2q}→∞. Estimating a from power is compatible with that condition; the known-a case already suffices for the obstruction.

**Proof of necessity.** Write \(M_r(v)=L^{-1}\sum_s(R_sv)^{\otimes r}\), and let \(\phi_\sigma\) denote the centered Gaussian density. Gaussian integration and the exponential series give the exact identity
\[
\int\frac{(p_v-p_w)^2}{\phi_\sigma}
 =\sum_{r=0}^\infty
 \frac{\|M_r(v)-M_r(w)\|_F^2}{r!\sigma^{2r}}.
\tag{9}
\]
To verify it, expand each term of \(\int p_vp_w/\phi_\sigma\): for orbit atoms b,c the integral is \(e^{\langle b,c\rangle/\sigma^2}\). Average over b,c and expand. All atoms have bounded norm, so absolute convergence justifies interchange. Subtract the two diagonal and cross expressions to obtain (9).

All signals here have norm R=√2a and zero orbit mean. Jensen gives
\[
p_w(y)/\phi_\sigma(y)
 =e^{-R^2/(2\sigma^2)}\mathbb E_s e^{\langle y,R_sw\rangle/\sigma^2}
 \ge e^{-R^2/(2\sigma^2)}.
\]
Hence \(\chi^2(p_v\|p_w)\) is at most \(e^{R^2/(2\sigma^2)}\) times (9). The first q−1 moment differences vanish. Tensor telescoping yields
\(\|M_r(v)-M_r(w)\|_F\le rR^{r-1}\|v-w\|\).
For \(v=u_\theta,w=u_{\theta+h}\), \(\|v-w\|\le R|h|\). Therefore the remaining series is bounded by
\[
\chi^2(p_v\|p_w)\le C_{a,q}h^2\sigma^{-2q},\qquad \sigma\ge\max(1,R).
\]
For small |h|<π/q the orbit distance is \(2R|\sin(h/2)|\), bounded above and below by constants times |h|. Choose h so that the two orbits are separated by more than 2ε. The product KL divergence is at most \(n\chi^2(p_v\|p_w)\), and total variation is at most its square root divided by √2. If \(n\le c_{a,q}\sigma^{2q}\varepsilon^{-2}\), choose the constant so that total variation ≤1/2. Any estimator accurate within ε at both parameters would produce a test with average error below 1/4, contradicting the testing lower bound \((1-\mathrm{TV})/2\). Thus some parameter has error probability at least 1/4. This proves the claimed exponent. ∎

This is the discrete harmonic mechanism already reflected in Bandeira–Rigollet–Weed, Appendix B. It refutes an overbroad universal σ⁶ statement; it does not refute the correctly qualified generic theorem or the quasi-MLE phase conjecture.

## 4. Numerical checks

Code is in `code/`, observations are reproducible from saved seeds, and all numerical outputs are in `data/`. No numerical optimizer is asserted to be a certified global MLE or quasi-MLE.

The final experiment used every integer L=5,…,15, norm-one real signals with all unitary Fourier magnitudes 1/√L (and positive DC), Gaussian noise, and iid uniform shifts. The length sweep used σ∈{0.5,1.5,3}, n∈{200,2000}, and two independent data sets per configuration. An additional sweep used L∈{5,9,15}, σ∈{0.5,1.5}, n=20,000, with three repetitions. The scaling sweep used L=5, σ∈{1,1.5,2}, n≈cσ⁶ for c∈{100,1000}, with three repetitions. In total: **168 data sets and 672 fitted estimates**; largest n=64,000.

Each fit used two random phase starts with the **true amplitudes only for initialization**. Both hard methods used 100 alignment/averaging iterations per start; the constrained version projected onto **data-estimated** magnitudes after each step. The unconstrained output was also retained, and its post-corrected counterpart used the same shift solution selected before correction. Marginal likelihood used at most 100 EM iterations followed by at most 50 L-BFGS iterations with the exact likelihood gradient. The best objective across starts was selected without using reconstruction error. True amplitudes at initialization are favorable prior information; the reconstructions themselves were not constrained to them. Even with this initialization, global optimization is not certified.

The error is squared orbit error divided by true signal energy. Selected medians are:

| L=5, σ | n | Marginal likelihood | Raw quasi | Quasi, post power | Quasi, power constrained |
|---|---:|---:|---:|---:|---:|
| 0.5 | 200 | 0.016209 | 0.031694 | 0.024402 | 0.013961 |
| 0.5 | 2,000 | 0.000863 | 0.008259 | 0.001453 | 0.001402 |
| 0.5 | 20,000 | 0.000104 | 0.006448 | 0.000063 | 0.000063 |
| 1.5 | 200 | 0.576672 | 2.212480 | 0.517853 | 0.503014 |
| 1.5 | 2,000 | 0.135258 | 1.764425 | 0.173771 | 0.167799 |
| 1.5 | 20,000 | 0.002031 | 1.401094 | 0.034619 | 0.035435 |

These entries use two repetitions for n≤2000 and three for n=20,000; they are small-sample summaries, not fitted asymptotic rates. The persistent raw-quasi error is compatible with power bias, while the decrease after correction is evidence only.

In the n≈1000σ⁶ sweep, marginal-likelihood median errors at σ=1,1.5,2 were **0.00552, 0.01389, 0.00495**. This is broadly compatible with comparable error at comparable n/σ⁶, but three repetitions and moderate σ cannot estimate a recovery exponent precisely. The constrained hard-alignment medians were **0.00673, 0.10563, 0.62698**; its fixed iteration budget does not produce a comparable collapse. Sampling variability, slow convergence and different local optima remain possible explanations. This does not certify inconsistent global population optima.

A separate, better powered scaling check estimates the shift-invariant statistic
\(B=\widehat Y_1^2\overline{\widehat Y_2}\) at L=5. There are 100 independent repetitions at each σ, each averaging 20,000 observations. Generating just these two Fourier coordinates is distributionally equivalent to generating full MRA observations for this invariant: their shift phases cancel, and the Gaussian noise coordinates are independent circular complex Gaussians. With \(a=|\widehat u_1|^2\), \(b=|\widehat u_2|^2\), direct expansion gives the exact error variance

\[
\mathbb E|\widehat B-B(u)|^2
 ={(a^2+4ab)\sigma^2+(4a+2b)\sigma^4+2\sigma^6\over n}.
\tag{10}
\]

The alternative derivation multiplies \(\mathbb E|\widehat Y_1|^4=a^2+4a\sigma^2+2\sigma^4\) by \(\mathbb E|\widehat Y_2|^2=b+\sigma^2\) and subtracts a²b. The code checks these two formulas independently. Here a=b=1/5.

| σ | Measured MSE | Monte Carlo standard error | Exact MSE |
|---:|---:|---:|---:|
| 1 | 0.0001514 | 0.0000163 | 0.0001700 |
| 1.5 | 0.0012504 | 0.0001260 | 0.0014653 |
| 2 | 0.0073297 | 0.0007282 | 0.0074000 |
| 3 | 0.0708666 | 0.0089821 | 0.0778500 |
| 4 | 0.4433238 | 0.0385083 | 0.4251200 |
| 6 | 4.6819468 | 0.4755594 | 4.7437200 |

A least-squares log–log slope over σ∈{2,3,4,6} is **5.9114**. This checks the cubic-invariant noise scale; it does not by itself establish the full reconstruction sample complexity or an exact recovery constant.

Arithmetic and implementation checks covered an independent finite-difference likelihood-gradient check (maximum discrepancy 4.32×10⁻¹¹), a scalar direct mixture evaluation (discrepancy 4.44×10⁻¹⁶), direct cyclic-correlation indexing, invariance of both objectives to separate observation shifts, exact Fourier projection, the pairwise/profile identity in Section 1, EM monotonicity, finite-valued results, and the variance identity (10). An initial BLAS run emitted floating-point-status warnings despite finite outputs. The retained main results were recomputed using explicit `numpy.einsum` contractions and completed without those warnings; the original run is retained as `data/recovery_blas.csv` for audit. The main run's **peak RSS was 267,599,872 bytes**, about 255 MiB, with one numerical thread and verified inherited nice level **10**. Darwin rejected the optional address-space limit; memory was bounded by the experiment dimensions and measured throughout. No more than one experiment worker ran at once.

Reproduce from this directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/experiments.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/summarize.py
```

Dependencies: Python 3, NumPy, SciPy; source acquisition additionally uses requests and pypdf (pdftotext supplies an independent readable extraction for the Romanov paper). All random seeds, numerical versions, priority and resource measurements are saved. Full synthetic observations are regenerated from `data/signals.json` and the per-case seeds in `data/recovery.csv`.

## 5. What was and was not completed

The source model and both estimator conventions were checked directly. All named literature families were searched and the retained primary papers were inspected at the cited theorem statements. The marginal-MLE and generic sample-exponent questions have affirmative published answers under the assumptions recorded above; nongeneric discrete signals have known higher-order obstructions. Complete proofs of the auxiliary results and requested numerical evidence are included.

The general fixed-positive-noise quasi-MLE phase-consistency question, for either post correction or the separately constrained formulation, is **not proved or disproved here**. No numerical result is promoted to a theorem, and no optimal universal leading constant is asserted. The next mathematical step is population identification for the hard objective; another uniform law or another Gaussian-mixture KL argument would not supply it.

Task: “Open problem E0057” — 13 November 2026, approximately 08:56 +04.
