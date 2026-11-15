PARTIAL

For independent Lévy processes X and Y, the Kanda–Forst sector inequality passes to X+Y. Consequently X+Y satisfies Hunt’s hypothesis (H) whenever both exponents satisfy that inequality and the sum has Lebesgue resolvent densities. In particular, this holds in the classical Kanda–Forst class, with bounded continuous transition densities. This is already in the literature. The unrestricted implication (H) for X and Y ⇒ (H) for X+Y is not proved or disproved here, and no printed full solution was found in the search described below.

The user’s instruction to stop upon locating a printed result for a stated class applies: Hu–Sun already prove several such results. The classification PARTIAL records those existing results and the checked lead; it does not claim a new partial theorem. The discussion of the full problem below identifies gaps in the suggested methods, without claiming a new class or a counterexample.

The intended source is Ze-Chun Hu and Wei Sun, *Hunt’s Hypothesis (H) for Markov Processes: Survey and Beyond*, arXiv:1908.06825v1, submitted 19 August 2019, 27 pages. It was published in *Acta Mathematica Sinica, English Series* 37(3) (2021), 491–508, DOI [10.1007/s10114-021-9343-7](https://doi.org/10.1007/s10114-021-9343-7). The journal metadata were checked against the [journal’s record](https://actamath.cjoe.ac.cn/Jwk_sxxb_en/CN/10.1007/s10114-021-9343-7). Throughout this report, “survey p.” means the PDF page, also the printed page, of the 27-page 2019 arXiv version. It does not mean the journal pagination. The page-delimited text is [sources/hu_sun_2019_survey.txt](sources/hu_sun_2019_survey.txt).

The alternative title in the request, *Hunt’s hypothesis (H) and Getoor’s conjecture for Lévy processes*, identifies a different Hu–Sun paper: *Stochastic Processes and their Applications* 122(6) (2012), 2319–2328, DOI [10.1016/j.spa.2012.03.013](https://doi.org/10.1016/j.spa.2012.03.013), arXiv:1101.3038. No separate source titled *Some open problems on Hunt’s hypothesis (H)* was identified. The exact match to Question 7 and PDF p. 25 is the 2019 survey.

Question 7, survey p. 25, asks whether two independent n-dimensional Lévy processes satisfying (H) have a sum satisfying (H). It is the question specified in the task. The following Remark 5.1 states that an affirmative answer would also answer Question 6 affirmatively, and that an affirmative answer to the independent-product question, Question 4, would imply an affirmative answer to Question 7. These are implications, not resolutions.

For precision, use the definitions on survey pp. 1–2. On a locally compact state space E with countable base, write

\[
T_C=\inf\{t>0:X_t\in C\},\qquad \inf\varnothing=\infty.
\]

A set D is thin if it is contained in a nearly Borel set C such that P^x(T_C=0)=0 for every x∈E. It is semipolar if it is contained in a countable union of thin sets. It is polar if it is contained in a nearly Borel set C such that P^x(T_C<∞)=0 for every x∈E. Hunt’s hypothesis (H) says that every semipolar set is polar. “Every x” is essential: the weaker conclusion holding for Lebesgue-almost every starting point is essential polarity. Also, hitting starts at t>0, not at t=0. These conventions prevent a deterministic nonzero motion from being mistaken for an (H) process.

Use the survey’s characteristic-exponent convention, on p. 3:

\[
\mathbb E e^{i\langle z,X_t\rangle}=e^{-t\psi(z)},\qquad
\psi(z)=i\langle a,z\rangle+\tfrac12\langle z,Qz\rangle
+\int\bigl(1-e^{i\langle z,x\rangle}
+i\langle z,x\rangle\mathbf1_{\{|x|<1\}}\bigr)\,\mu(dx).
\]

Thus Q is nonnegative definite and Re ψ≥0. Define A=1+Re ψ and B=|1+ψ|. A finite positive measure ν has finite 1-energy if

\[
E_\psi(\nu):=\int_{\mathbb R^d}\frac{A(z)}{B(z)^2}
|\widehat\nu(z)|^2\,dz<\infty.
\]

Normalizing constants in Fourier inversion do not affect finiteness or the zero limits below. Lebesgue resolvent densities mean that the resolvent kernels U^α(x,dy)=∫₀∞e^{−αt}P^x(X_t∈dy)dt are absolutely continuous in y, for α>0. Bounded continuous transition densities imply resolvent densities, by integration and Tonelli, even when the resulting resolvent density is unbounded.

The relevant printed results, with hypotheses retained, are as follows. Page numbers for the original papers below refer to the explicitly named arXiv versions, unless a journal page is supplied.

1. Kanda–Forst: survey Theorem 2.1, p. 4. Bounded continuous transition densities with respect to d-dimensional Lebesgue measure, together with |Im ψ|≤M(1+Re ψ) for a finite constant M, imply (H). The paragraph immediately following the theorem records Rao’s weakening to resolvent densities. The references are Kanda, *Two theorems on capacity for Markov processes with stationary independent increments*, *Z. Wahrscheinlichkeitstheorie verw. Gebiete* 35 (1976), 159–165, and Forst, *The definition of energy in non-symmetric translation invariant Dirichlet spaces*, *Math. Ann.* 216 (1975), 165–172. Rao’s weakening is *On a result of M. Kanda*, *Z. Wahrscheinlichkeitstheorie verw. Gebiete* 41 (1977), 35–37. The survey’s density hypothesis must not silently disappear when using its Theorem 2.1.

2. Rao’s more general criterion: survey Theorem 2.3, p. 4; original Rao, *Hunt’s hypothesis for Lévy processes*, *Proceedings AMS* 104(2) (1988), Theorem 2, journal p. 622, proof pp. 622–623. Assume resolvent densities. If f is positive and increasing on [1,∞),

   \[
   \int_N^\infty\frac{d\lambda}{\lambda f(\lambda)}=\infty,
   \qquad B\le A f(A),
   \]

   for every N≥1 (equivalently for every sufficiently large N, after an innocuous positive definition near 1), then (H) holds. The original paper assumes lower semicontinuity of all 1-excessive functions on p. 622 and explains the existence of resolvent densities there. Hawkes’s equivalence between these two formulations is recorded on survey p. 4, citing *Potential theory of Lévy processes* (1979), Theorem 2.1. Taking f constant gives the sector criterion, with the constant changed from M to √(1+M²). Logarithmic examples should be made positive near 1: one cannot literally impose B≤A log A at z=0. Rao’s Corollary 3, journal p. 624, gives (H) for nondegenerate asymmetric Cauchy processes.

3. Hu–Sun–Zhang’s extended criterion: survey Theorem 2.8, p. 6; *New results on Hunt’s hypothesis (H) for Lévy processes*, *Potential Analysis* 42 (2015), 585–605, arXiv:1210.2016v3, Theorem 4.5, PDF p. 13. Assume resolvent densities, equivalently the lower semicontinuity condition just stated. If Im ψ=ψ₁+ψ₂ for measurable real functions, |ψ₁|≤Af(A), f is positive increasing with the preceding divergent integral, and

   \[
   \int_{\mathbb R^d}\frac{|\psi_2(z)|}{A(z)^2+(\operatorname{Im}\psi(z))^2}\,dz<\infty,
   \]

   then (H) holds. The functions ψ₁, ψ₂ in this statement are a decomposition of the imaginary part; they are not assumed to be Lévy exponents.

4. Hu–Sun’s Gaussian and finite-off-subspace results: survey Theorems 2.5–2.6, p. 5; original 2012 paper, arXiv:1101.3038v3, Theorems 1.1–1.2, PDF p. 3. If Q has full rank, X satisfies (H), the sector inequality holds, and X has the same polar sets as X−X̄, with X̄ an independent copy. More generally put S=range(√Q), suppose μ(R^d\S)<∞, and set

   \[
   b'=-a-\int_{\{x\notin S:\ |x|<1\}}x\,\mu(dx).
   \]

   Under this finite-off-subspace assumption the following are equivalent: X satisfies (H); b'∈S; the sector inequality holds. In the sum paper, condition (S) includes both the finite-off-subspace assumption and b'∈S. No ambient Lebesgue density assumption is required for this equivalence. This matters for processes supported on proper subspaces.

5. The existing sum theorems are in Hu and Sun, *Hunt’s Hypothesis (H) for the Sum of Two Independent Lévy Processes*, *Communications in Mathematics and Statistics* 6(2) (2018), 227–247, DOI [10.1007/s40304-018-0136-y](https://doi.org/10.1007/s40304-018-0136-y), arXiv:1702.07396v1. The [publisher’s record](https://journal.hep.com.cn/cimas/EN/10.1007/s40304-018-0136-y) and arXiv metadata agree on the 2018 issue citation. Its migrated web page also displays a 2025 online date; that is not evidence of a new 2025 theorem. In the saved 21-page arXiv text:

   | Printed result | Exact positive statement | PDF page | Survey counterpart |
   |---|---|---|---|
   | Theorem 3.1 | X₁ satisfies (H), X₂ is an independent compound Poisson process ⇒ X₁+X₂ satisfies (H). No density assumption. | 11; proof 12 | Theorem 2.14, p. 8 |
   | Theorem 3.2 | Independent X₁ and X₂ both satisfying condition (S) ⇒ X₁+X₂ satisfies (H). | 11; proof 13 | Theorem 2.15, p. 8 |
   | Theorem 4.1 | The sum has resolvent densities; X₁ has resolvent densities and (H); every finite measure of finite 1-energy for the sum has finite 1-energy for X₁; and |Im ψ₂|≤c(1+Re ψ₁+Re ψ₂). Then the sum satisfies (H). | 14; proof 16–17 | Theorem 2.16, p. 8 |
   | Proposition 4.2(i) | The bound |ψ₂|≤c(1+Re ψ₁) is sufficient for the finite-energy implication in Theorem 4.1. | 14 | Mentioned on survey p. 9 |
   | Corollary 4.3 | Under the standing sum-resolvent-density assumption of §4, X₁ has bounded resolvent densities and (H), and |Im ψ₂|≤c(1+Re ψ₁+Re ψ₂) ⇒ the sum satisfies (H). | 14 | Not needed for the survey’s statement |

   All conditions in a row are conjunctive. In particular, Theorem 4.1 does not replace its finite-energy assumption by “X₂ satisfies (H).” The standing assumption at the beginning of §4 must also be retained when quoting its corollaries. Proposition 4.5, PDF p. 15, provides an additional extended Kanda–Forst–Rao sum criterion: under that standing assumption, Im ψ₁=φ₁₁+φ₁₂, |φ₁₁|≤(1+Re ψ₁)f(1+Re ψ₁), ∫|φ₁₂|/|1+ψ₁|²<∞, and |Im ψ₂|≤(1+Re ψ₁+Re ψ₂)f(1+Re ψ₁+Re ψ₂), with the same positive increasing f and divergent integral, imply (H) for the sum.

6. Some one-dimensional sufficient conditions are broader than a sector estimate. Survey Theorem 2.19, p. 9, says that

   \[
   \liminf_{\varepsilon\downarrow0}
   \frac{\int_{-\varepsilon}^{\varepsilon}x^2\mu(dx)}
   {\varepsilon/|\log\varepsilon|}>0
   \quad\Longrightarrow\quad(H).
   \]

   Survey Proposition 2.22, p. 10, gives the sufficient condition liminf_{|z|→∞} Re ψ(z)/(|z|/log|z|)>0. No assumption on the other part of the triplet is added in these statements. The former condition is Theorem 2.3, PDF p. 7, of arXiv:1702.07396v1. The survey labels its citation “[22, Theorem 2.2]”; comparison with that source shows this is a cross-reference error. Its Remark 2.21, p. 10, emphasizes that the small-jump condition does not impose an imaginary-part comparison. Since Lévy measures and real parts add nonnegatively, either displayed sufficient condition, when held by one summand, is retained by the sum. That consequence of the printed theorem is not claimed as new.

7. Subordinators: write ψ(z)=−iδz+∫₀∞(1−e^{izx})μ(dx), δ≥0, ∫(1∧x)μ(dx)<∞. If a subordinator satisfies (H), then δ=0: survey Proposition 2.24, p. 11; original Hu–Sun 2012, Proposition 1.6, PDF p. 4. Zero drift alone is not asserted sufficient. A special subordinator, meaning its undiscounted potential measure restricted to (0,∞) has a decreasing Lebesgue density, satisfies (H) iff δ=0: survey Theorem 2.25, p. 11; Hu–Sun–Zhang 2015, Theorem 3.3, PDF p. 7. Every locally quasi-stable driftless subordinator satisfies (H): survey Definition 2.26 and Proposition 2.27, p. 11; original Definition 3.4 and Proposition 3.5, PDF p. 8. Here the precise local comparison is c₁μ_T−μ₁≤μ≤c₂μ_T+μ₂ on (0,ε), where μ_T is a stable-subordinator Lévy measure, c₁,c₂,ε>0 and μ₁,μ₂ are finite measures there.

   Survey Definition 2.28, p. 11, calls a driftless subordinator type-(α,β), 0<α<β<1, if its Lévy density ρ satisfies c⁻¹x^{−1−α}≤ρ(x)≤cx^{−1−β} on (0,1], for some c>1. Survey Theorem 2.29 on the same page, citing Hu–Sun 2016, *Further study on Hunt’s hypothesis (H) for Lévy processes*, arXiv:1406.2013v3, Theorem 4.2, PDF p. 24, decomposes every such subordinator into two independent type-(α,β) subordinators each satisfying (H). The survey explicitly leaves (H) for the original general type-(α,β) subordinator unsettled. Thus a full positive sum theorem would have substantial content even for driftless subordinators. This decomposition is not itself a counterexample: the sum’s failure of (H) has not been established.

8. Subordination is distinct from addition. Glover–Rao’s theorem, survey Theorem 2.31, p. 13, says that X_{τ_t} satisfies (H) for any standard X if an independent subordinator τ satisfies (H). Its source is *Hunt’s hypothesis (H) and Getoor’s conjecture*, *Annals of Probability* 14 (1986), 1085–1087. Hu–Sun–Wang’s *Two Theorems on Hunt’s Hypothesis (H) for Markov Processes*, arXiv:1903.00050v3, later *Potential Analysis* 55 (2021), 29–49, DOI [10.1007/s11118-020-09848-2](https://doi.org/10.1007/s11118-020-09848-2), gives preservation under local absolute continuity of path laws (Theorem 1.1, PDF p. 3), and equivalence of (H) for X and X_{τ_t} for an independent subordinator τ with positive drift (Theorem 1.3, PDF p. 4). Survey counterparts are Theorems 2.30, pp. 12–13, and 2.32, p. 13. Neither theorem is general closure under independent sums.

Getoor’s conjecture is described on survey p. 2 as the expectation that essentially all Lévy processes satisfy (H), with extremely nonsymmetric cases such as uniform motion excluded. This informal formulation is not an assertion that every Lévy process satisfies (H). For a deterministic motion X_t=vt with v≠0, {0} is thin, because it is never hit immediately from any starting point, but it is not polar, because starting at −v it is hit at time 1. In particular this process cannot be used as a summand satisfying (H). Survey Question 5, p. 25, asks the precise unresolved subordinator question: whether every driftless subordinator with infinite Lévy measure satisfies (H). Question 6 asks whether every one-dimensional Lévy process with ∫(1∧|x|)μ(dx)=∞ satisfies (H). The literature search did not identify a full resolution of these questions or Question 7.

Here is a complete verification of the first-pass lead. This proof is an exposition of known mathematics.

Assume X,Y are independent Lévy processes on R^d and

\[
|\operatorname{Im}\psi_X(z)|\le M_X(1+\operatorname{Re}\psi_X(z)),\qquad
|\operatorname{Im}\psi_Y(z)|\le M_Y(1+\operatorname{Re}\psi_Y(z))
\tag{1}
\]

for every z, with finite nonnegative constants M_X,M_Y. Let Z=X+Y and assume Z has Lebesgue resolvent densities. Then Z satisfies (H). One need not separately assume (H) for X and Y for this conditional statement.

First, increments of Z on disjoint time intervals are independent: they are functions of the corresponding independent increments of the pair (X,Y). Their laws are stationary, and stochastic continuity and the càdlàg property pass to their sum. Thus Z is a Lévy process. Independence gives

\[
\mathbb E e^{i\langle z,Z_t\rangle}
=\mathbb E e^{i\langle z,X_t\rangle}\,
 \mathbb E e^{i\langle z,Y_t\rangle}
=e^{-t(\psi_X(z)+\psi_Y(z))}.
\]

The continuous characteristic exponent, zero at z=0, is therefore ψ_Z=ψ_X+ψ_Y. Equivalently, differentiating at t=0 removes any possible logarithm-branch ambiguity.

Put r_X=Re ψ_X≥0 and r_Y=Re ψ_Y≥0. By (1) and the triangle inequality,

\[
\begin{aligned}
|\operatorname{Im}\psi_Z|
&\le |\operatorname{Im}\psi_X|+|\operatorname{Im}\psi_Y|\\
&\le M_X(1+r_X)+M_Y(1+r_Y)\\
&\le(M_X+M_Y)(1+r_X+r_Y)\\
&=(M_X+M_Y)(1+\operatorname{Re}\psi_Z).
\end{aligned}
\tag{2}
\]

The penultimate inequality follows because the difference between its right and left sides is M_X r_Y+M_Y r_X≥0. The additive 1 has been accounted for; there is no assumption of homogeneity or of strict positivity of either r.

Set C=M_X+M_Y, A_Z=1+Re ψ_Z and B_Z=|1+ψ_Z|. Then

\[
B_Z^2=A_Z^2+(\operatorname{Im}\psi_Z)^2
\le(1+C^2)A_Z^2.
\tag{3}
\]

Because Z has resolvent densities, Rao’s criterion applies with the constant function f≡√(1+C²), whose required integral diverges: ∫_N^R dλ/(λf)=f⁻¹(log R−log N)→∞. Equations (2)–(3) therefore imply (H).

There is also a useful independent check of this last implication using the energy characterization, survey Proposition 2.13, p. 8 (Hu–Sun 2016, Proposition 2.2, PDF p. 5). Under the same resolvent-density assumption, (H) is equivalent to

\[
\lim_{\lambda\to\infty}\int\frac{\lambda}{\lambda^2+B_Z(z)^2}
|\widehat\nu(z)|^2\,dz=0
\tag{4}
\]

for every finite positive ν with E_{ψ_Z}(ν)<∞. For every λ>0 and B>0, (λ−B)²≥0 implies λ/(λ²+B²)≤1/(2B). By (3),

\[
\frac{\lambda}{\lambda^2+B_Z^2}|\widehat\nu|^2
\le\frac{1}{2B_Z}|\widehat\nu|^2
\le\frac{\sqrt{1+C^2}}2\frac{A_Z}{B_Z^2}|\widehat\nu|^2.
\]

The right side is integrable by the definition of finite 1-energy. For every fixed z the integrand on the left tends to zero as λ→∞. Dominated convergence proves (4), so the equivalent criterion gives (H). This checks the implication for every required test measure, rather than just for a point mass or a numerical sample.

To obtain the classical Kanda–Forst class without assuming a density for Z separately, suppose in addition that X has bounded continuous transition densities p_t for all t>0. Let μ_t be the probability law of Y_t. Independence and Tonelli give a transition density for Z:

\[
q_t(w)=\int p_t(w-y)\,\mu_t(dy).
\]

Indeed integrating q_t over any Borel set yields the convolution law of X_t+Y_t. It is nonnegative, integrates to 1, and is bounded by ||p_t||∞. For w_n→w, continuity of p_t gives pointwise convergence of p_t(w_n−y); the bound 2||p_t||∞ dominates their differences under the probability measure μ_t. Dominated convergence gives continuity of q_t. Hence Z has bounded continuous transition densities and therefore resolvent densities. The preceding argument, or directly survey Theorem 2.1, gives (H). In particular this proves closure for two independent processes each in the classical Kanda–Forst class. Only one summand’s transition-density assumption was needed for this density step.

The more general resolvent formulation above keeps “Z has resolvent densities” as an explicit hypothesis. This report does not silently infer that property merely from resolvent densities of X and Y: resolvent integration and convolution at a common time are different operations. Likewise, the sector inequality by itself is not a statement of the complete classical theorem. For singular processes the separate finite-off-Gaussian-subspace theorem can apply instead.

Novelty was checked directly: the proof of Hu–Sun’s Theorem 3.2, arXiv:1702.07396v1, PDF p. 13, explicitly invokes the sector inequality for each summand and then states it holds for their sum. The algebra (2) is already used there. Moreover their Proposition 4.5, PDF p. 15, covers broader perturbations. There is no new sector-stability result here.

For completeness, the following checks explain why the suggested full-solution routes do not presently close the problem.

The sector argument cannot start from (H) alone. This is not merely an omitted proof of equivalence. For example a skew one-dimensional 1-stable process has, with a suitable standard scaling,

\[
\psi(z)=|z|+i\frac{2\beta}{\pi}z\log|z|,\qquad 0<|\beta|<1,
\]

with the continuous convention z log|z|=0 at z=0. Its sector ratio is (2|β|/π)|z||log|z||/(1+|z|), which diverges as |z|→∞. Nevertheless it satisfies (H), for example by Rao’s Corollary 3, p. 624. One can also use a sufficiently large multiple of log(e+A) in Rao’s theorem; the large-frequency ratio is logarithmic and the small-frequency ratio is bounded. Its transition densities are bounded and continuous because |e^{−tψ(z)}|=e^{−t|z|} is integrable. Thus “(H) ⇒ a finite sector constant” is false even with very good transition densities. This example is not a counterexample to sum stability.

For the energy method, write I_j=Im ψ_j and r_j=Re ψ_j. The weight for a summand is

\[
w_j=\frac{1+r_j}{(1+r_j)^2+I_j^2},
\]

whereas for the sum it is

\[
w_Z=\frac{1+r_1+r_2}{(1+r_1+r_2)^2+(I_1+I_2)^2}.
\]

The addition r_1+r_2≥r_j does not order these weights. Imaginary parts can reinforce or cancel, and even the derivative of A/(A²+I²) in A has the variable sign of I²−A². To apply (H) for X_j via (4), one must first know that every ν with ∫w_Z|ν̂|²<∞ also has ∫w_j|ν̂|²<∞. No such implication from (H) alone has been established here. It is precisely assumption (ii) in the existing sum Theorem 4.1. The missing input is an implication between spaces of finite-energy measures, not just a pointwise limit at a fixed z. Numerical estimates for a few measures would not supply it.

The symmetric-part route has the same issue. The symmetrization X−X̄ has exponent 2Re ψ. Survey Proposition 2.7, p. 6, gives (H) when X has bounded continuous transition densities and X has the same polar sets as its symmetrization. To use it for X+Y one must establish that equality of polar sets for the sum; knowing (H) for its summands does not provide it by the cited proposition. Adding real parts does not by itself compare the nonsymmetric potential weights above. No equality of polar sets for a new class was proved.

The product/projection route reduces to another open closure question. If the product process (X,Y) satisfies (H), applying the linear map (x,y)↦x+y gives (H) for the sum. The projection fact is survey Lemma 3.1, p. 13, originally Hu–Sun 2018, Lemma 3.4, PDF p. 12; the sum map is a projection after an orthogonal change of variables and a nonzero scaling. The missing assertion is (H) for the independent product of two arbitrary (H) processes. Survey Question 4 and Remark 5.1 identify this route explicitly. It cannot be assumed as a lemma solving Question 7.

For simple drift and subspace candidates there are existing obstructions or existing positive results. A deterministic nonzero drift fails (H), as checked above. More generally, an (H) Lévy process with Q=0 and ∫(1∧|x|)μ(dx)<∞ must have zero finite-variation drift: survey Proposition 3.2, p. 14, citing Hu–Sun–Wang Proposition 5.3, PDF p. 21, proof pp. 21–22. Thus two such (H) summands cannot manufacture a nonzero finite-variation drift by addition; their physical drifts add to zero. This statement concerns the uncompensated finite-variation drift, not merely the parameter a in the compensated convention. Driftless infinite-activity subordinators remain a real difficulty, rather than a verified failure of (H).

An independent compound Poisson perturbation of any (H) process is already covered by Theorem 3.1, including a subordinator satisfying (H). “Compound Poisson plus deterministic drift” is not a driftless compound Poisson process and cannot be substituted into that theorem. Its separate (H) status must be checked.

For Gaussian subspace examples, covariance cannot cancel: Q_X+Q_Y is nonnegative definite, and if it has full rank the sum has (H) by Hu–Sun 2012, Theorem 1.1, regardless of the two individual (H) assumptions. For example independent Brownian motions on two complementary lines in R² give a nondegenerate Gaussian sum. More generally, the finite-off-subspace class is already closed by Hu–Sun 2018, Theorem 3.2. To see how its proof works, put S_j=range(√Q_j) and S=range(√(Q_1+Q_2)). For positive semidefinite matrices,

\[
\ker(Q_1+Q_2)=\ker Q_1\cap\ker Q_2,
\]

since zero quadratic form for their sum forces each nonnegative quadratic form to vanish. Taking orthogonal complements shows S_j⊂S. Therefore μ_j(R^d\S)≤μ_j(R^d\S_j)<∞. The individual solution conditions give sector bounds by Hu–Sun 2012, Theorem 1.2; (2) gives the sum’s sector bound; that same theorem, now for Q_1+Q_2 and μ_1+μ_2, gives (H) for the sum. This is the printed proof’s mechanism, not a new subspace class.

Rao and extended-sector arguments also require hypotheses beyond (H). With a common increasing admissible gauge f, the imaginary-part bounds for two summands combine into at most 2A_Z f(A_Z), so a constant multiple of f remains admissible, provided the needed sum densities exist. With two unrelated gauges, a proof using their maximum must verify the divergent integral for that maximum; it is not checked just by writing down the two separate hypotheses. In the extended criterion the residual integrals use |1+ψ_j|⁻², while the sum needs |1+ψ_X+ψ_Y|⁻². There is no monotone replacement of those denominators supplied by the individual (H) assumptions. Proposition 4.5 gives a known way to handle some of these perturbations under explicit additional bounds.

The literature search was performed on 13 November 2026 and targeted 2019–2026, including the strings “Hunt’s hypothesis”, “sum of independent Lévy processes”, “Getoor’s conjecture”, Hu, Sun, Zhang, Glover–Rao, Kanda and Hawkes, with both Levy/Lévy spellings and straight/curly apostrophes. Searches included individual years 2020–2026 and date-restricted queries. The inspected primary sources include the 2019 survey and its 2021 journal record, the 2018 sum paper and its journal record, Rao’s original 1988 theorem, the 2012/2015/2016 papers listed above, and Hu–Sun–Wang’s 2019 preprint/2021 transformation paper. The [2021 Liping Li paper](https://arxiv.org/abs/2107.06163) concerns general one-dimensional diffusions and symmetrization, not closure of arbitrary Lévy sums. A [2026 IMAR seminar listing](https://www.imar.ro/ro/seminar/38) records Li-Fei Wang’s talks on measure change and subordination; the listing supplies no sum-stability theorem. Search hits with recent crawl or migration dates were not counted as new results. No search snippet or generated overview was used as authority for a theorem.

The negative literature conclusion has a defined limit: no full answer was located in these searches and primary sources. This is not a proof that no answer exists anywhere, nor an exhaustive review of inaccessible literature. In particular, seminar titles do not establish what was proved in unpublished work. The stopping decision rests on the positively verified partial results, not on an assertion of exhaustive absence.

Verification and saved material: the survey question and theorem/page locations were read in page-delimited text and checked against the source documents. The sector constant was checked by direct subtraction in (2), and the implication to (H) was checked both through Rao’s theorem and through dominated convergence in the finite-energy characterization. The 2018 sum theorem hypotheses were checked against their original §4 standing assumptions. The survey’s small-jump theorem cross-reference was checked against the original statement. No simulation or numerical potential-density test was run: there is no candidate with both summands’ (H) proved and the sum’s failure of (H) established, and finite numerical samples would not settle the required all-measures condition.

All saved paper sources are plain text under sources/. Code is in code/; response hashes, text hashes, retrieval times, page counts, query records and validation output are in data/. Source responses were converted from in-memory PDF bytes through pdftotext stdin/stdout; no PDF, page image or scan was retained. LOG.md records progress and qualifications. No publication or push was performed.

Task: “Open problem E0027” — 2026-11-13, approximately 12:57 Asia/Tbilisi (first recorded clock 12:57:50 +04).
