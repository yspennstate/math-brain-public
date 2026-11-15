PARTIAL

# D0031: finite-state rho-mixing and bilateral determinism

No construction or general impossibility proof is established. No published resolution was located in the literature search through 13 November 2026. That is a search outcome, not a proof that the problem remains open. The full 1996 Burton–Denker–Smorodinsky article and full 2007 Bradley volumes were not accessible; their verified statements and exact book cross-references are distinguished below from direct reading.

The question asks for a nonconstant strictly stationary process on a finite alphabet, with maximal correlation between its whole past and separated whole future tending to zero, whose entire history is measurable from every exterior of a finite interval.

## Literature checkpoint

Bradley’s survey, *Probability Surveys* **2** (2005), 107–144, DOI [10.1214/154957805100000104](https://doi.org/10.1214/154957805100000104), Section 2.6, printed pp. 116–117 (Question 3 on PDF p. 11), lists the finite-state question as unsolved. Section 2.5 separates ordinary rho-mixing from absolute regularity and interlaced rho-mixing; Section 2.7 cautions against identifying mixing conditions of a coordinate presentation with Bernoulli isomorphism. [Local survey](sources/bradley_2005_survey.pdf).

R. C. Bradley, “A bilaterally deterministic rho-mixing stationary random sequence,” *Transactions of the American Mathematical Society* **294** (1986), 233–241, DOI [10.1090/S0002-9947-1986-0819945-0](https://doi.org/10.1090/S0002-9947-1986-0819945-0), gives the real-state construction. Directly read its original UNC technical report 91B (February 1985), Theorem 1, Lemma 2, and Section 3, [DTIC ADA152856 scan](https://archive.org/download/DTIC_ADA152856/DTIC_ADA152856.pdf), [local copy](sources/bradley_1985_bilateral_preprint.pdf). The theorem allows any prescribed positive upper bounds on rho(n). This is a nondiscrete-state example; countably many internal bits or independent rows do not mean a countable state space.

R. M. Burton, M. Denker, and M. Smorodinsky, “Finite state bilaterally deterministic strongly mixing processes,” *Israel Journal of Mathematics* **95** (1996), 115–133, DOI [10.1007/BF02761036](https://doi.org/10.1007/BF02761036), constructs a finite-state alpha-mixing example. The publisher abstract was verified; the full proof and its internal theorem numbering were unavailable. No rho-mixing estimate has been verified for that example.

R. C. Bradley, *Introduction to Strong Mixing Conditions*, Volumes 1–3, Kendrick Press, Heber City, Utah (2007). The [publisher contents](https://kendrick.press/Richard-Bradley-Introduction-to-Strong-Mixing-Conditions.htm) were checked. Bradley’s own later paper, “A strictly stationary, ‘causal,’ 5-tuplewise independent counterexample to the central limit theorem,” *ALEA* **7** (2010), 377–450, printed p. 382, explicitly points to **Volume 2, Theorem 24.14** for the real-state bilaterally deterministic example and **Volume 1, Proposition 5.17** for the absolute regularity obstruction. This supplies exact locators, not a claim to have inspected all three volumes. [Primary full text](https://alea.math.cnrs.fr/articles/v7/07-19.pdf), [local copy](sources/bradley_2010_causal.pdf).

The proofs and attempted constructions below give restricted obstructions; none is a general resolution.

## Further literature and scope of the search

V. M. Gurevič, “On one-sided and two-sided regularity of stationary random processes,” *Soviet Mathematics Doklady* **14** (1973), 804–808, is the earlier finite-state example with trivial one-sided tails, as identified in Bradley’s original introduction. D. S. Ornstein and B. Weiss, “Every transformation is bilaterally deterministic,” *Israel Journal of Mathematics* **21** (1975), 154–158, DOI [10.1007/BF02760793](https://doi.org/10.1007/BF02760793), gives finite generating presentations with bilateral determinism. Its publisher abstract was checked; an accessible later statement is Theorem 3 of A. van Enter and E. Verbitskiy, “Erasure entropies and Gibbs measures,” [arXiv:1001.3122](https://arxiv.org/abs/1001.3122), Section 2, [local text](sources/van_enter_verbitskiy_2010.txt). These are statements about presentations and isomorphisms, not preservation of rho-mixing under an arbitrary isomorphism.

A potentially misleading countable-state result is R. C. Bradley, “A stationary rho-mixing Markov chain which is not ‘interlaced’ rho-mixing,” *Journal of Theoretical Probability* **14** (2001), 717–727, DOI [10.1023/A:1017545123473](https://doi.org/10.1023/A:1017545123473). The primary abstract asserts a countable-state rho-mixing chain that fails rho-star mixing. It does **not** assert bilateral determinism. More generally, stationary irreducible aperiodic countable-state Markov chains are absolutely regular, so they cannot give the requested phenomenon. Thus the reviewed evidence does not justify calling Bradley’s bilateral example countable-state. No countable-state rho-mixing bilaterally deterministic example was verified in this search.

Other relevant Bradley references traced in the survey are “Absolute regularity and functions of Markov chains,” *Stochastic Processes and their Applications* **14** (1983), 77–97; “Basic properties of strong mixing conditions,” in *Dependence in Probability and Statistics*, Progress in Probability and Statistics **11** (1986), 165–192; and “Every ‘lower psi-mixing’ Markov chain is ‘interlaced rho-mixing’,” *Stochastic Processes and their Applications* **72** (1997), 221–239. Their titles or the countable-state terminology in related work do not supply a finite-state resolution. These are bibliographic leads, not claims that their entire proofs were read here.

J. Kułaga-Przymus and M. D. Lemańczyk, “Entropy rate of product of independent processes,” *Monatshefte für Mathematik* **200** (2023), 131–162 (online 10 December 2022), DOI [10.1007/s00605-022-01801-2](https://doi.org/10.1007/s00605-022-01801-2), supplies modern, precise facts: Remark 1.15 identifies the one-sided tails of a finite-alphabet stationary process with its Pinsker field; Corollary 2.9 and Remark 2.10 characterize bilateral determinism for finite-state Markov chains; Section 2.1.3 discusses absolute regularity. None of these statements resolves Question 3. [Local paper](sources/kulaga_przymus_lemanczyk_2023.pdf).

J. Steif’s contribution, “Some results and open questions concerning Gibbs states, quasilocality and bilateral determinism,” *Oberwolfach Reports* **11/2020**, printed pp. 632–633, in *Mini-Workshop: One-sided and Two-sided Stochastic Descriptions*, DOI [10.4171/OWR/2020/11](https://doi.org/10.4171/OWR/2020/11), describes the finite-state examples and the parity-check approach, including Burton–Steif (1997). It poses questions about quasilocality, not an answer to the finite-state rho question. [Primary report](https://ems.press/content/serial-article-files/46847), [local copy](sources/oberwolfach_2020.pdf).

Searches used “bilaterally deterministic,” “bilateral determinism,” “rho-mixing,” “rho mixing,” “ρ-mixing,” “maximal correlation,” “finite state,” and “countable,” including searches restricted by dates and explicit years through 2026. Follow-up reading included Bradley (2010), van Enter–Verbitskiy (2010), the 2020 workshop, Lemańczyk’s thesis, the 2023 paper, and the 2026 Denker survey, [arXiv:2606.17857v2](https://arxiv.org/abs/2606.17857). The latter contains no discussion of bilateral determinism. Search-engine crawl dates were not treated as publication dates. See [search record](sources/SEARCH_NOTES.md) for access limitations and representative exact queries. The search is not a complete citation-index census, and the inaccessible book and article remain limitations.

## Definitions and established compatibility

All sigma-fields below are completed modulo null sets. Write

\[
 \mathcal F_a^b=\sigma(X_k:a\leq k\leq b),\qquad
 \mathcal E_n=\mathcal F_{-\infty}^{-n}\vee\mathcal F_n^\infty,
 \qquad \mathcal T_d=\bigcap_{n\geq1}\mathcal E_n.
\]

For two fields, maximal correlation is

\[
 \rho(\mathcal A,\mathcal B)
 =\sup\{|E(fg)|:Ef=Eg=0,\ E f^2=E g^2=1,
                  f\in L^2(\mathcal A),g\in L^2(\mathcal B)\}.
\]

For a stationary process, \(\rho_X(n)=\rho(\mathcal F_{-\infty}^0,\mathcal F_n^\infty)\). Bilateral determinism means \(\mathcal T_d=\sigma(X)\). Nondegeneracy means that \(X_0\) is not almost surely constant.

The distinction between the following properties is essential:

| Property accompanying bilateral determinism | State space | Verified situation |
| --- | --- | --- |
| Trivial past and future tails | finite | Compatible: Gurevič |
| A presentation of a Bernoulli system | finite | Compatible: Ornstein–Weiss |
| Alpha-mixing | finite | Compatible: Burton–Denker–Smorodinsky |
| Rho-mixing, arbitrarily prescribed positive rate bounds | nondiscrete real | Compatible: Bradley’s Theorem 1 |
| Absolute regularity / weak Bernoulli | any standard Borel alphabet | Impossible for a nondegenerate example; proof below |
| Interlaced rho-mixing | any alphabet | Impossible; indeed rho-star(n) must equal 1 for every n |
| Rho-mixing | finite | Not decided here |

Here rho-star allows separated index sets with indices on both sides of each other; ordinary rho only compares ordered half-lines. For finite alphabets, weak Bernoulli of the coordinate partition is absolute regularity. Being isomorphic to a Bernoulli shift is a different statement. Positive entropy, the K property, and the Bernoulli property therefore do not, by themselves, contradict bilateral determinism.

The following arguments establish the particular obstructions used in this report. They do not assume that finite alphabet alone upgrades rho-mixing to absolute regularity.

## 1. Positive entropy and the one-sided tails

**Proposition 1.** Let \(X\) be a stationary finite-alphabet process. If \(A\) is a set of states with \(p=P(X_0\in A)\in(0,1)\), then for every \(n\geq1\), its entropy rate in nats satisfies

\[
 h(X)\ \geq\ \frac{2p(1-p)}{n}\,[1-\rho_X(n)^2]. \tag{1}
\]

In particular, a nondegenerate rho-mixing finite-state process has strictly positive entropy. Its past and future tail fields are trivial.

*Proof.* Put \(\mathcal P=\mathcal F_{-\infty}^0\), \(B=1_{\{X_n\in A\}}\), and \(Q=E(B\mid\mathcal P)\). The definition of rho, or its conditional-expectation operator formulation, gives

\[
 \operatorname{Var}Q\leq\rho_X(n)^2p(1-p).
\]

For completeness, if \(Q-p\neq0\), use \(f=(Q-p)/\|Q-p\|_2\) in the defining correlation inequality with \(B-p\); their covariance is \(\|Q-p\|_2\). The law of total variance now gives

\[
 E[Q(1-Q)]\geq [1-\rho_X(n)^2]p(1-p).
\]

The elementary inequality \(-\log u\geq1-u\), applied also to \(1-u\), implies that binary entropy satisfies \(H_b(u)\geq2u(1-u)\), including the endpoints by continuity. Therefore

\[
 H(X_n\mid\mathcal P)\geq H(B\mid\mathcal P)
 =E H_b(Q)\geq2[1-\rho_X(n)^2]p(1-p).
\]

The stationary entropy chain rule gives

\[
 n h(X)=H(X_1,\ldots,X_n\mid\mathcal P)
 \geq H(X_n\mid\mathcal P),
\]

which proves (1). The entropy-rate identity follows by approximating the infinite past with finite pasts and using conditional entropy convergence on a finite alphabet.

To check the tail assertion independently, let \(D\) belong to the past tail and let \(C\) be a fixed finite-cylinder event. For all large \(N\), \(D\in\mathcal F_{-\infty}^{-N}\), and the correlation bound between that field and the finite block supporting \(C\) tends to zero. Hence \(P(D\cap C)=P(D)P(C)\). A monotone-class argument extends independence to all of \(\sigma(X)\). Taking \(C=D\) gives \(P(D)\in\{0,1\}\). The future proof is the same. ∎

For finite alphabets the coordinate partition is a finite-entropy generator. Its trivial past tail is the usual generating-past criterion for a K system. Equivalently, the Pinsker characterization cited above gives trivial Pinsker field. This is compatible with a nontrivial, even full, double tail: intersection does not in general commute with joining the two exterior fields. In particular, the inference

\[
 \bigcap_n(\mathcal F_{-\infty}^{-n}\vee\mathcal F_n^\infty)
 \stackrel{\text{invalid}}{=}
 (\bigcap_n\mathcal F_{-\infty}^{-n})
 \vee(\bigcap_n\mathcal F_n^\infty)
\]

would discard precisely the phenomenon under investigation.

## 2. Absolute regularity and interlaced correlation

**Proposition 2.** Absolute regularity implies a trivial double tail. A nondegenerate bilaterally deterministic process has \(\rho^*(n)=1\) for every \(n\geq1\).

*Proof.* Use the convention that beta is half the total-variation norm between the joint law and the product law, equivalently total-variation distance defined as a supremum over measurable events. Fix a central block \(C=X_{[-m,m]}\) and put \(L=X_{(-\infty,-n]}\), \(R=X_{[n,\infty)}\), with \(n>m\). Comparing the joint law of \((L,C,R)\) successively with

\[
 P_L\otimes P_{C,R},\quad
 P_L\otimes P_C\otimes P_R,\quad
 P_C\otimes P_{L,R}
\]

and applying the triangle inequality yields

\[
 \beta(\sigma(C),\sigma(L,R))
 \leq2\beta_X(n-m)+\beta_X(2n). \tag{2}
\]

Each comparison is bounded by the corresponding past–future beta coefficient; multiplying both measures by a common probability law preserves their total-variation distance. These statements apply to infinite half-line random elements because the alphabet and its countable products are standard Borel; equivalently one may first prove (2) for finite partitions and then take suprema.

For \(D\in\mathcal T_d\), (2) bounds its dependence with the fixed central block by a quantity tending to zero. Thus \(D\) is independent of every central block, hence of \(\sigma(X)\), hence of itself. This proves tail triviality.

For the second assertion choose a nonconstant centered unit-variance indicator function \(Z=f(X_0)\). Bilateral determinism makes it measurable with respect to \(\mathcal E_n\), so

\[
 \rho(\sigma(X_0),\mathcal E_n)=1.
\]

The two index sets \(\{0\}\) and \(\{k:|k|\geq n\}\) have distance \(n\). If the definition of rho-star uses finite sets only, approximate \(Z\), as an exterior-measurable variable, in \(L^2\) by functions of finitely many exterior coordinates; their correlations with \(Z\) tend to 1. The supremum is again 1. ∎

Thus m-dependent, beta-mixing, phi-mixing, and psi-mixing constructions cannot answer the question, nor can an interlaced rho estimate. The phi/psi conclusions use their standard domination of beta. The ordinary rho coefficient does not control the central block versus a join of two distant half-lines.

## 3. Why Bradley’s original example needs an infinite alphabet

The following is a deduction from the **specific preprint construction**, not a theorem excluding other finite or countable constructions.

Its underlying array has independent fair signs \(V_{0,m}\), \(m\geq1\), and correlated pairs at \((-n,m),(n,m)\). Equations (2.10)–(2.11) define \(W\), with \(W_{0,m}=V_{0,m}\). The variable \(Y_k\) encodes the entire vector \((W_{k,m})_{m\geq1}\) by a bimeasurable map \(f\). The recovery argument in Claim 1 uses infinitely many repeated measurements for each bit and the strong law. Section 3 then takes independent copies \(Y^{(j)}\), \(j\in\mathbb Z\), and sets

\[
 X_k=g\big((Y_t^{(k+t)})_{t\in\mathbb Z}\big), \tag{3}
\]

with \(g\) another bimeasurable encoding. The indices in (3) were visually checked against printed preprint p. 13.

**Proposition 3.** This stationary process has infinite Kolmogorov–Sinai entropy. Its natural finite bit projections can be nondegenerate iid processes and need not be bilaterally deterministic.

*Proof.* From \(X_k\), invert \(g\), select the \(t=0\) coordinate, and invert \(f\). For every positive integer \(M\) this gives the one-coordinate factor

\[
 B_k^{(M)}=(W_{0,1}^{(k)},\ldots,W_{0,M}^{(k)}).
\]

Its \(M\) bits are independent fair signs. Different times \(k\) use independent copies of the entire original array. Thus \(B^{(M)}\) is iid, uniform on \(2^M\) symbols, and has entropy rate \(M\log2\). In particular, the partition of the underlying space according to \(B_0^{(M)}\) has entropy rate \(M\log2\). The supremum of partition entropy rates defining the Kolmogorov–Sinai entropy is consequently infinite.

A finite generating partition with \(q\) atoms would bound the entropy of the system by \(\log q\), a contradiction. Here is a direct check of that standard generator bound in this setting. If a \(q\)-symbol process \(Q\) generated the same system, approximate each fixed \(B_0^{(M)}\) by a function \(\widehat B_0\) of \(Q_{[-r,r]}\), with error probability \(\varepsilon\). Such approximations exist by conditional expectation onto increasing finite windows and finite-alphabet classification. Write \(K=2^M\). Encoding whether an error occurred, and then which of the other \(K-1\) symbols occurred, gives

\[
 H(B_0^{(M)}\mid\widehat B_0)
 \leq H_b(\varepsilon)+\varepsilon\log(K-1)=:\delta_\varepsilon.
\]

Use the shifted versions of this estimator at each time. The entropy chain rule and conditioning on the whole \(Q\)-window give

\[
 NM\log2=H(B_{[1,N]}^{(M)})
 \leq (N+2r)\log q+N\delta_\varepsilon.
\]

First let \(N\) grow with the estimator fixed, and then let \(\varepsilon\) decrease to zero. This gives \(M\log2\leq\log q\) for every \(M\), the contradiction.

Also, \(X_k\) cannot have countable essential range in this construction: its measurable image \((W_{0,m}^{(k)})_{m\geq1}\) has a nonatomic fair product law. Every prescribed infinite sign vector has probability at most \(2^{-M}\) for every \(M\), hence probability zero, while a countable range would have total probability zero.

For \(M=1\), the factor is a nonconstant iid binary sequence. Its exterior is independent of \(B_0^{(1)}\), so it is not bilaterally deterministic. It is nevertheless rho-mixing, with rho(n)=0 for n≥1. ∎

This rules out an invertible finite-alphabet recoding of the original process. It does **not** rule out a noninvertible finite factor: such a factor can discard infinite entropy. The missing step in that route is to exhibit a finite factor that retains exact exterior reconstruction.

If \(Y_k=F(X_{k-r},\ldots,X_{k+r})\), then sigma-field inclusion gives

\[
 \rho_Y(n)\leq\rho_X(n-2r),\qquad n>2r. \tag{4}
\]

So rho-mixing survives a bounded-window factor. Bilateral determinism does not, as Proposition 3 demonstrates even for a one-coordinate factor. The available identity is only \(\mathcal T_d(Y)\subseteq\mathcal T_d(X)\); recovery of \(X\) from its exterior may require information that \(F\) deletes. An arbitrary measurable shift-equivariant code, with no bounded window, does not even have the inclusion proving (4). This is why neither a general generator theorem nor a Bernoulli isomorphism completes the construction.

## 4. Finite-order Markov constructions cannot work

**Proposition 4.** A stationary finite-state Markov chain that is bilaterally deterministic has entropy rate zero. Consequently no nondegenerate rho-mixing finite-order finite-state Markov process answers D0031.

*Proof.* For a one-step chain, the conditional law of \(X_{[1,N]}\) given its entire exterior depends only on \(X_0,X_{N+1}\). This follows by factoring finite cylinder probabilities into transition probabilities: once both endpoints are fixed, all exterior factors cancel from the conditional probability of the interior path. Approximation by finite exterior cylinders extends the identity to the whole exterior. Zero-probability endpoint pairs can be omitted.

Bilateral determinism therefore implies

\[
 H(X_{[1,N]}\mid X_0,X_{N+1})=0.
\]

The Markov property and stationarity give

\[
 \begin{aligned}
 N h(X)&=H(X_{[1,N]}\mid X_0)\\
 &=I(X_{[1,N]};X_{N+1}\mid X_0)
 \leq H(X_{N+1})\leq\log q,
 \end{aligned}
\]

where \(q\) is the number of states of positive stationary probability. Letting \(N\) tend to infinity gives \(h(X)=0\). Proposition 1 contradicts this if the chain is nondegenerate and rho-mixing.

For a process of order \(r\), use \(Z_k=(X_{k-r+1},\ldots,X_k)\), a finite-state one-step Markov chain. It is nondegenerate if \(X\) is. Its past is contained in the original past, and its future from time \(n\) is contained in the original future from \(n-r+1\), so \(\rho_Z(n)\leq\rho_X(n-r+1)\) for \(n\geq r\). Also \(\mathcal E_n(X)\subseteq\mathcal E_n(Z)\), because \(X_k\) is a component of \(Z_k\). If \(X\) is bilaterally deterministic, every \(X_j\), and hence every \(Z_j\), is measurable from each exterior of \(Z\). Thus \(Z\) is bilaterally deterministic and the one-step contradiction applies. ∎

For a stationary irreducible aperiodic countable-state Markov chain with stationary law \(\pi\), the standard Markov-chain convergence theorem (also summarized in Bradley (2005), Theorem 3.2) gives \(\|P^n(i,\cdot)-\pi\|_{\rm TV}\to0\) for every state \(i\). The Markov property gives the exact identity

\[
 \beta_X(n)=\sum_i\pi_i\|P^n(i,\cdot)-\pi\|_{\rm TV}\longrightarrow0. \tag{5}
\]

To see the identity, condition the future path on the past: its law depends only on \(X_0\). The distribution of its first coordinate is \(P^n(X_0,\cdot)\); the subsequent future is generated by the same transition kernel under both measures. Adding that common kernel preserves total variation, with equality because projecting onto the first coordinate recovers the original measures. Bounded convergence proves the limit in (5). This explains the countable Markov obstruction without assuming that all countable rho-mixing processes are Markov. Bounded-window factors of such a chain remain beta-mixing by the same sigma-field inclusion as (4), so finite-state observations of a mixing chain do not solve the problem either.

## 5. Gaussian constructions and bounded-window Gaussian codes cannot work

**Proposition 5.** A strictly stationary rho-mixing Gaussian process has a trivial double tail. Every bounded-window measurable factor of it also has a trivial double tail, regardless of the factor’s alphabet.

*Proof.* Subtract the constant mean. Work in the real Hilbert space \(H\) that is the closed linear span of \(\{G_j:j\in\mathbb Z\}\) in \(L^2\). Define closed linear subspaces

\[
 A_n=\overline{\operatorname{span}}\{G_j:j\leq-n\},\qquad
 B_n=\overline{\operatorname{span}}\{G_j:j\geq n\}.
\]

For \(a\in A_n,b\in B_n\), maximal correlation bounds their inner product:

\[
 |\langle a,b\rangle|\leq\rho_G(2n)\|a\|_2\|b\|_2.
\]

Choose \(n_0\) and \(c<1\) such that \(\rho_G(2n)\leq c\) for \(n\geq n_0\). Then

\[
 \|a+b\|_2^2\geq(1-c)(\|a\|_2^2+\|b\|_2^2). \tag{6}
\]

In particular \(C_n=A_n+B_n\) is closed for \(n\geq n_0\): if a sequence of sums is Cauchy, (6) applied to differences makes each component Cauchy. Its decomposition is unique and bounded in norm by (6).

Both \(\bigcap_n A_n\) and \(\bigcap_n B_n\) are zero. For example, if \(a\) belongs to all \(A_n\), for every fixed \(j\),

\[
 |\langle a,G_j\rangle|
 \leq\rho_G(n+j)\|a\|_2\|G_j\|_2\longrightarrow0.
\]

It is therefore orthogonal to the spanning family of \(H\), and is zero. The argument for \(B_n\) reverses time.

Now suppose \(z\in\bigcap_{n\geq n_0}C_n\). Write \(z=a_n+b_n\). By (6) these components are bounded sequences in the separable Hilbert space \(H\), so a subsequence converges weakly, say to \(a,b\). For each fixed \(m\), all sufficiently late terms satisfy \(a_n\in A_m,b_n\in B_m\). Closed subspaces are weakly closed, so \(a\in\bigcap_m A_m=\{0\}\) and \(b\in\bigcap_m B_m=\{0\}\). Thus \(z=a+b=0\), proving \(\bigcap_n C_n=\{0\}\).

Let \(P_n\) be orthogonal projection onto \(C_n\). Since these subspaces decrease to zero, \(P_n h\to0\) in \(L^2\) for every \(h\in H\). Explicitly, for \(n\geq m\),

\[
 \|P_m h-P_n h\|_2^2=\|P_m h\|_2^2-\|P_n h\|_2^2.
\]

The right side makes the projections Cauchy; their limit lies in every \(C_m\) and must be zero.

Gaussianity now matters. For any finite linear combination \(h\) of the \(G_j\), the conditional distribution given \(\mathcal E_n(G)\) is Gaussian, with mean \(P_n h\) and variance \(\|h\|_2^2-\|P_n h\|_2^2\). Indeed \(h-P_n h\) is orthogonal to every exterior coordinate; joint Gaussianity turns those zero covariances into independence of all finite exterior vectors, hence of their generated field. Orthogonal projection is an \(L^2\) limit of linear combinations of those coordinates, so its Gaussian and measurability properties persist in the limit. Thus

\[
 E(e^{ih}\mid\mathcal E_n(G))
 =\exp\{iP_nh-\tfrac12(\|h\|_2^2-\|P_nh\|_2^2)\}
 \longrightarrow e^{-\|h\|_2^2/2}=E e^{ih}
 \quad\text{in }L^1. \tag{7}
\]

The reverse martingale theorem identifies the limit in (7) with \(E(e^{ih}\mid\mathcal T_d(G))\). Taking all finite linear combinations proves, by uniqueness of characteristic functions, independence of the tail from every finite Gaussian vector. The cylinder monotone-class argument then makes the tail independent of \(\sigma(G)\), hence trivial.

Finally, if \(Y_k=F(G_{k-r},\ldots,G_{k+r})\), then for every \(n\),

\[
 \mathcal E_{n+r}(Y)\subseteq\mathcal E_n(G).
\]

It follows that \(\mathcal T_d(Y)\subseteq\mathcal T_d(G)\), proving the factor assertion. ∎

The argument uses ordinary rho-mixing and Gaussian conditional distributions, not beta-mixing or a spectral-density assumption. It does not exclude a nonlocal coding of a Gaussian system. Such a coding needs its own proof of rho-mixing and tail behavior; these do not follow from isomorphism.

## 6. A stationary linear parity-constraint attempt fails

A natural algebraic attempt is to take a shift-invariant closed linear subspace \(K\subseteq\mathbb F_p^{\mathbb Z}\), for prime \(p\), with its Haar probability, hoping that global linear constraints recover every deleted block while leaving weak dependence.

**Proposition 6.** No such scalar Haar process is both nondegenerate rho-mixing and bilaterally deterministic.

*Proof.* If \(K\) is the full product, Haar probability is the iid uniform product law, which is not bilaterally deterministic. Otherwise choose a point outside \(K\). Closedness gives a finite cylinder disjoint from \(K\). Consequently some finite-coordinate projection of \(K\) is a proper linear subspace. A nonzero linear functional annihilates that projection. Enlarging its coordinate interval if necessary and discarding zero endpoint coefficients gives a relation

\[
 \sum_{j=0}^d c_j x_{k+j}=0\quad(k\in\mathbb Z,\ x\in K),
 \qquad c_0c_d\neq0, \tag{8}
\]

where shift invariance supplies every translate. If \(d=0\), \(K=\{0\}\). If \(d\geq1\), (8) determines every coordinate forward and backward from any \(d\) consecutive coordinates. Thus \(|K|\leq p^d\). The shift is a permutation of this finite set, so some positive integer \(L\) satisfies \(x_{k+L}=x_k\) for all \(x\in K\).

If \(X_0\) is nonconstant, for every separation \(n\) choose a multiple \(jL\geq n\). A nonconstant centered function of \(X_0=X_{jL}\) belongs to both the past field through 0 and the future field from \(n\), and has correlation 1 with itself. Hence \(\rho_X(n)=1\) for every \(n\), contrary to rho-mixing. ∎

This excludes only scalar closed linear subgroup/Haar models. It does not apply to the random, nonlinear, or hierarchical parity constructions behind the known finite-state alpha-mixing examples.

## 7. Why weak correlation alone does not prevent exact joint decoding

The following fully specified probability model isolates the infinite-repetition mechanism. It is **not** asserted to be the stationary process requested in D0031.

Let \(Z\) be a fair sign, let \(U_m\), \(m\geq1\), be iid fair signs, and let \(E_m\) be iid signs with \(E E_m=r\in(0,1)\). These three objects are independent. Put

\[
 V_m=Z U_m E_m,\qquad
 \mathcal U=\sigma(U_m:m\geq1),\quad
 \mathcal V=\sigma(V_m:m\geq1).
\]

**Proposition 7.** The bit \(Z\) is independent of each of \(\mathcal U,\mathcal V\) separately, is exactly measurable from their join, and

\[
 \rho(\mathcal U,\mathcal V)=r^2. \tag{9}
\]

No finite number of observation pairs determines \(Z\) exactly.

*Proof.* Independence of \(Z\) and \(U\) is given. Conditional on any fixed \(Z\) and \(E\), multiplying the independent uniform signs \(U_m\) by fixed signs leaves a uniform product sequence \(V\). Thus \(V\) is also independent of \(Z\). On the other hand, the strong law gives

\[
 \lim_{M\to\infty}\frac1M\sum_{m=1}^M U_mV_m
 =Z\lim_{M\to\infty}\frac1M\sum_{m=1}^M E_m=rZ
 \quad\text{a.s.},
\]

so the join reveals \(Z\).

For a finite set \(S\subset\mathbb N\), write \(\chi_S(u)=\prod_{m\in S}u_m\). These Walsh functions form an orthonormal basis for the fair product law: finite-coordinate functions have the finite cube’s character basis, and conditional expectations onto increasing finite-coordinate fields approximate every \(L^2\) function. Independence gives

\[
 E[\chi_S(V)\mid U]
 =\chi_S(U)\,E[Z^{|S|}]r^{|S|}
 =\begin{cases}
   r^{|S|}\chi_S(U),& |S|\text{ even},\\
   0,& |S|\text{ odd}.
  \end{cases}
\]

On the centered subspace the largest multiplier is \(r^2\), attained when \(|S|=2\). By Parseval, this is the conditional-expectation operator norm, which is maximal correlation: for fixed centered \(g(V)\), maximizing its covariance over centered unit \(f(U)\) gives \(\|E[g(V)\mid U]\|_2\). This proves (9).

For finite \(M\), put \(t_m=u_mv_m\). With a fair prior the posterior weights for \(Z=z\) are proportional to

\[
 \prod_{m=1}^M(1+zr t_m),\quad z\in\{-1,1\}. \tag{10}
\]

Every factor is strictly positive. Both posterior probabilities are strictly between 0 and 1 on every observed pair of sign vectors, so exact decoding is impossible. ∎

Thus even an arbitrarily small positive maximal correlation between two whole observations can coexist with exact nonlinear recovery of a finite bit from their join. Replacing the infinite measurements by a large finite number yields a small error, not the zero error required by bilateral determinism. Equations (9)–(10) were checked independently with exact rational arithmetic as described below.

The non-Gaussian decoding in this example also explains the limit of Proposition 5. For general fields, \(L^2(\mathcal A\vee\mathcal B)\) contains products and nonlinear functions; it is much larger than \(L^2(\mathcal A)+L^2(\mathcal B)\). Gaussian linear variables measurable from a join belong to the closed linear Gaussian span, which made the Hilbert-space proof possible. The same argument cannot be applied to an arbitrary finite-valued target.

## 8. Block and tower route: the unproved step

The finite-state parity/tower approach can spread reconstruction information over time instead of placing infinitely many bits in a single coordinate. The known finite-state alpha-mixing construction establishes that this general strategy can achieve stationarity and exact exterior recovery together with alpha-mixing. It supplies no verified rho estimate here.

The estimate that would be needed is, for some \(\varepsilon_n\downarrow0\),

\[
 |\operatorname{Cov}(f,g)|\leq\varepsilon_n
       \sqrt{\operatorname{Var}f\operatorname{Var}g}
 \quad\text{for every }f\in L^2(\mathcal F_{-\infty}^0),\qquad
       g\in L^2(\mathcal F_n^\infty). \tag{11}
\]

No finite-alphabet stationary hierarchy satisfying both (11) and exact exterior decoding was constructed in this attempt. Two simple proposed shortcuts fail:

- A small exceptional probability does not establish (11). If both fields equal the sigma-field generated by a Bernoulli event of probability \(\delta\in(0,1)\), their rho coefficient is 1, whereas their alpha coefficient is only \(\delta(1-\delta)\). The latter follows by listing the two-atom events; the former follows by normalizing the common centered indicator. Rarity disappears on normalization.
- An observable nonconstant periodic phase is fatal. If a phase \(J_k\) of period \(L\) is a one-coordinate factor, then \(J_0=J_{jL}\) for arbitrarily large \(j\), giving rho(n)=1. With a uniformly bounded coding window the same argument holds after shifting both windows into the two half-lines. Introducing a random phase to stationarize fixed-length blocks therefore requires proving that the phase is not retained as an observable factor.

These are obstructions to particular implementations, not a proof that all tower constructions fail. Proposition 7 shows why a general impossibility proof cannot rest solely on pairwise field correlations and the finiteness of the recovered bit.

## What was checked, and what remains

The survey and original construction were downloaded and read, including the surrounding tail, Markov, independent-component, and Gaussian material. Printed preprint p. 13 was rendered to resolve the stationary coding indices. Primary publisher abstracts and Bradley’s own 2010 cross-references were used where full texts were inaccessible. The full BDS construction and full three-volume book were not audited, and this report does not invent their internal theorem numbers or claim a complete literature census.

The proofs above independently establish the entropy lower bound, the beta and interlaced-rho obstructions, the original example’s infinite-entropy factors, the finite-order Markov obstruction, the Gaussian bounded-window obstruction, the scalar linear/Haar obstruction, and the masking-channel calculation. No novelty is claimed for standard consequences or their proofs.

[code/check_mask_channel.py](code/check_mask_channel.py) checks only finite rational computations for Proposition 7. It verifies all Walsh multipliers, their maximum on the centered subspace, normalization of probabilities, positive posterior probabilities, and positive Bayes error (also computed separately as a binomial majority-vote tail), for \(M=1,\ldots,6\) and \(r\in\{1/4,1/2,3/4\}\): **18 exact cases passed**. For \(r=1/2\), it gives:

| M | rho of the two M-sign vectors | Optimal error probability for Z |
| --- | --- | --- |
| 1 | 0 | 1/4 |
| 2 | 1/4 | 1/4 |
| 3 | 1/4 | 5/32 |
| 4 | 1/4 | 5/32 |
| 5 | 1/4 | 53/512 |
| 6 | 1/4 | 53/512 |

The infinite-observation statement follows from the proof, not from these cases. Results are saved in [code/mask_channel_results.json](code/mask_channel_results.json). Local Python inherited nice 10, used one thread and standard-library arithmetic; no large simulation, model worker, publication, or push was run. All created files are inside this directory.

The outstanding mathematical task is to produce a finite-alphabet factor or a new stationary coding with both exact exterior reconstruction and the uniform past–future bound (11), or to prove that no such process exists. Neither has been accomplished. The appropriate first-line status is **PARTIAL**, not PROVED, COUNTEREXAMPLE, or RESOLVED_IN_LITERATURE.

Task: “Open problem D0031” — received 13 November 2026, approximately 04:29 +04 (first local clock reading 04:29:40).
