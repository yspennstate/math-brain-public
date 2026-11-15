COUNTEREXAMPLE

D0058: critical moments in the integer-valued Derrida–Retaux recursion

The statement with criticality alone is false, simultaneously for every real r>0, by a direct consequence of our prior internal D0056 counterexample. The version with E[X_0^3 m^{X_0}]<infinity remains open in the literature located in this audit. We prove below that the survival asymptotic implies the geometric conditional limit with convergence of every positive moment. Consequently the survival conjecture, the first-moment conjecture, and the full positive-moment conjecture are equivalent, within the source's critical setting. This is a reduction, not a proof of the strengthened conjecture.

The first-line classification concerns the literal criticality-only statement. It does not classify the strengthened conjecture as solved. The sparse construction and its survival estimate are prior internal work, not a new result of this task. No publication or push was made.

Statement and hypothesis audit

The source is X. Chen, B. Derrida, Y. Hu, M. Lifshits and Z. Shi, arXiv:1705.04787. The 13 May 2017 v1 is titled “A hierarchical renormalization model: some properties and open questions.” The 26 June 2019 v2 has the requested title, “A max-type recursive model: some properties and open questions.” It was published in Sojourns in Probability Theory and Statistical Physics–III (2019), pp.166–186, DOI 10.1007/978-981-15-0302-3_6. Both arXiv versions are saved as extracted plain text in sources/. Page numbers below are PDF pages of the identified version, not inferred book pagination.

The v2 assumptions are:

* m is an integer with m>=2 (p.1).
* X_0 is nonnegative and, from p.3 onward, takes values in Z_+={0,1,2,...}.
* X_0 is not almost surely constant (p.1). This matters: m=2, X_0=1 almost surely would otherwise be a stationary exception.
* At each step, X_n^{(1)},...,X_n^{(m)} are independent copies, and
  \[
  X_{n+1}\overset d=\left(\sum_{i=1}^m X_n^{(i)}-1\right)^+.
  \]
* Equation (4), p.3, is exactly
  \[
  (m-1)E[X_0m^{X_0}]=E[m^{X_0}]<\infty. \tag{C}
  \]

Conjecture 3, v2 PDF p.4, states, assuming (4),
\[
 E[X_n]\sim\frac{4m}{(m-1)^3}\frac1{n^2},
\]
and, for every real r in (0,infinity),
\[
 E[X_n^r]\sim\frac{c(r,m)}{n^2},\qquad
 c(r,m)=\frac4{m-1}\sum_{k=1}^\infty\frac{k^r}{m^k}. \tag{M}
\]
The corresponding v1 statement is Conjecture 1.5, PDF p.4, using equation (1.4) for criticality.

The companion survival statement is Conjecture 1, v2 p.3 (v1 Conjecture 1.3):
\[
 q_n:=P(X_n>0)\sim\frac4{(m-1)^2n^2}. \tag{S}
\]
Conjecture 2, v2 p.4, proposes conditional probabilities (m-1)m^{-k}, k>=1.

Neither Conjecture 1 nor Conjecture 3 in these arXiv versions explicitly includes the third tilted moment. Both versions warn, immediately after the conjectures on p.4, that additional integrability may be necessary, mentioning E[X_0^3m^{X_0}]<infinity. That condition is an explicit assumption of Theorem 3, v2 p.5 (Theorem 1.7 in v1), which concerns E[m^{X_n}]-1. Thus the ledger does not omit an explicit hypothesis of the cited arXiv Conjecture 3; rather, it omits the authors' qualification concerning potentially necessary hypotheses. Later literature explicitly treats the third tilted moment as necessary for the proposed universal constants: see Chen–Hu–Shi (2021 preprint/2022 publication), PDF pp.3–4.

This corrects the shorthand “published version” in our prior internal D0056 memory: the strengthened formulation is the intended finite-third-tilted-moment problem; it must not be silently substituted for the literal wording of the 2017/2019 arXiv source. The Springer chapter's typeset conjecture wording was not independently obtained here, so this audit does not claim an exact textual comparison with that edition.

There is also a factor-m error in the example conditional-moment formula in the task. The normalized source distribution is
\[
 \pi_k=(m-1)m^{-k},\quad k\ge1,\qquad \sum\pi_k=1,
\]
so its r-th moment is (m-1)sum_{k>=1}k^r m^{-k}, without an extra factor 1/m. For r=1 this is m/(m-1), consistent with (M)/(S).

Literature first: findings and limits

The complete source texts were downloaded and converted with pdftotext through standard input/output. PDF bytes were held only in memory; no PDF or page image was written in this directory. Each saved text records URL, retrieval timestamp, and SHA256 of the downloaded bytes. The search included the named papers, exact-title and arXiv-ID searches, author/year searches through 2026, forward citations in OpenAlex for the chapter, arXiv DOI, and old-title records, a second forward-citation search in Semantic Scholar, and a broader OpenAlex topic search. Raw citation responses are saved as text. Bibliographic indexing cannot certify that every existing citation has been recovered; the inventory below covers every returned forward-citation record and supplementary relevant papers found by web search. No universal exact-constant theorem for the fixed-m discrete model was found.

| Work and source | Precise result or scope | Consequence for D0058 |
|---|---|---|
| [Chen et al., arXiv:1705.04787v2](https://arxiv.org/pdf/1705.04787v2), 2019 | Theorem 2, p.3: E[m^{X_n}] -> 1 under (C). Theorem 3, p.5: E[m^{X_n}]-1 is between positive multiples of 1/n under the third tilted moment. Proposition 4, pp.22–23: positive finite upper/lower harmonic bounds for n^2 q_n. Proposition 5, pp.23–24: analogous harmonic bounds for n^2 E[X_n]. Lemmas 4–5, pp.14–15: survival asymptotic implies the first-moment asymptotic. | These are not pointwise Theta(n^{-2}) bounds or exact moment constants. Section 6, pp.13–15, motivates the conditional generating-function limit but assumes its existence in that heuristic. |
| [Chen–Dagard–Derrida–Hu–Lifshits–Shi, arXiv:1907.01601v3](https://arxiv.org/pdf/1907.01601v3), Ann. Probab. 49 (2021), 637–670 | Theorem 1.1, preprint p.3: near-supercritical free-energy exponent 1/2 under E[(X_0^*)^3 m^{X_0^*}]<infinity. Theorem 1.2, p.4: exponent 1/(alpha-2) for a tilted power tail with 2<alpha<=4. | Free-energy statements as p approaches p_c, not exact critical-time moments. The title must not be read as resolving every critical conjecture. |
| [Chen–Shi, arXiv:2006.06140](https://arxiv.org/pdf/2006.06140), 2020 preprint / 2021 chapter | Theorem 1.1, PDF p.3: if P(Y_0=k)~c_0m^{-k}k^{-alpha}, 2<alpha<4, and (C), then product_{i<n}E[m^{Y_i}]^{m-1} is between positive multiples of n^{alpha-2}. Theorem 1.2, p.4: bounds k! exp(c k)n^{k-1} on k-th derivatives at m, under E[s^{Y_0}]<infinity for some s>m. | The first is the stable-law route used in prior internal D0056 work. The second concerns tilted factorial moments, not E[Y_n^r]. Neither is an exact ordinary-moment asymptotic. |
| [Chen–Hu–Shi, arXiv:2108.05610](https://arxiv.org/pdf/2108.05610), PTRF 182 (2022), 641–684 | Theorem 1.2, PDF p.3: under (C) and E[t^{Y_0}]<infinity for some t>m, q_n=n^{-2+o(1)} and E[Y_n]=n^{-2+o(1)}. Proposition 4.1, p.22: under E[Y_0^5m^{Y_0}]<infinity, P(Y_n>=ell+1)<=C(log n)^2/(m^ell n^2), all n>=2, ell>=0. Proposition 5.1, p.34: under an exponential moment beyond m, for each lambda>0 there is nu>0 such that P(Y_n>=ell+1)>=1/[n^2(log n)^nu m^ell], for sufficiently large n and 0<=ell<=lambda n. | These tail bounds imply the logarithmic bounds for every real r>0 proved below. Exact constants, and removal of the logarithmic losses, are not established by these results. |
| [Chen–Hu–Shi, arXiv:2306.12717](https://arxiv.org/pdf/2306.12717), SPA 171 (2024), 104332 | Theorem 1.1, PDF p.5: near-subcritical exponential-rate bounds on E[X_n], with square-root dependence on p_c-p, under an exponential moment beyond m. Remark 1.2, p.5: leaf inequality E[X_n]>=m^n P(X_0>=n+1). Its introduction p.4 recalls the critical n^{-2+o(1)} theorem. | Relevant coupling and leaf arguments, not a proof of critical constants. |
| [Hu–Shi, arXiv:1705.03792](https://arxiv.org/pdf/1705.03792), JSP 172 (2018), 718–741 | Proposition 1.2, pp.3–4, characterizes p_c>0; Theorems 1.4–1.5, p.5, study near-supercritical free energy, including generalized offspring. | No critical ordinary-moment constants. |
| [Hu–Mallein–Pain, arXiv:1811.08749](https://arxiv.org/pdf/1811.08749), CMP 375 (2020), 605–651 | Theorem 1.9(iii), PDF p.8: in their solvable continuous-time family, E[X_t]~2/t^2 and the positive conditional law tends to Exp(1). | Different recursion/time variable and continuous states. Does not prove the proposed fixed-m discrete constants. |
| Collet–Eckmann–Glaser–Martin, CMP 94 (1984), 353–370, [DOI](https://doi.org/10.1007/BF01224830) | Original criticality/iteration analysis; the 2019 source identifies equation (AIII.10) as the m=2 survival prediction. The 2020 Chen–Shi paper explains that its stable product theorem completes and unifies arguments in this paper. | The criticality result is used through the explicit modern source statements. The journal PDF was not successfully extracted. A primary 1983 Strasbourg preprint is saved as sources/collet_et_al_1983_numdam.txt; Appendix III is at PDF pp.22–24 (printed pp.137–139), with poor extraction of some equations. This is not silently substituted for the journal pagination. Do not assign an unverified original theorem/page to a stronger moment claim. |
| [Derrida–Retaux, arXiv:1401.6919](https://arxiv.org/pdf/1401.6919), JSP 156 (2014), 268–290 | Renormalization model, critical manifold, perturbative/continuum asymptotics and numerical predictions. | The critical n^{-2} law is a prediction for the discrete model, not a proof of (M). |
| [Derrida–Shi, arXiv:2005.10208](https://arxiv.org/pdf/2005.10208), MMJ 20 (2020), 695–709 | Sections 2–5 distinguish critical conjectures and rigorous bounds from continuum predictions and altered tilted tails. | Useful hypothesis and status check. Does not resolve the strengthened moment conjecture. |
| [Chen, arXiv:2405.09741](https://arxiv.org/pdf/2405.09741), published 2026, DOI 10.1007/s10114-026-4249-z | Theorem 1.1, PDF p.4: infinite differentiability of F_infinity(p) under exponential moments for |s|<m, with uniformly converging derivative series. | Differentiation in the initial mixing parameter p is not a critical-time moment asymptotic. |
| [Li–Zhang, arXiv:2411.13068](https://arxiv.org/pdf/2411.13068), JSP 2025 | Theorem 1.3, pp.3–4, and Corollaries 1.5–1.9, pp.4–6: critical asymptotic expansions in a geometric-offspring model. Remark 1.11, p.6, explicitly notes different leading constants from the fixed-offspring conjectures. | Solvable random offspring, not deterministic m. |
| [Alsmeyer–Hu–Mallein, arXiv:2502.02991](https://arxiv.org/pdf/2502.02991), 2025 | Corollary 2.7, PDF p.10: survival constant and conditional geometric law in the geometric Galton–Watson setting. | Different offspring law. An initially geometric distribution alone does not turn the deterministic-m recursion into this model. |
| [Lotnikov–Kotova, arXiv:2502.02535](https://arxiv.org/pdf/2502.02535), 2024/2025 | Criticality criteria with random offspring and general subtraction. | No resolution of fixed-m critical moment constants. |
| [Duquesne–Shi, arXiv:2609.11435](https://arxiv.org/pdf/2609.11435), September 2026 | Continuous D–R branching process represented using the Brownian CRT; abstract p.1 still describes its relation to the discrete model as a conjectural scaling limit. | Does not supply the missing discrete theorem. |

The other returned forward citations were Johnson–Junge–Lyu–Sivakoff, “Particle density in diffusion-limited annihilating systems” (2023); the H^{2|2}/vertex-reinforced jump process paper, arXiv:2309.01221 (2024 publication); Michel Pain's 2019 thesis; and two “Physique statistique” annual reports (2022/2023). Their subjects are respectively interacting particles, reinforced walks, the continuous-time model, and research summaries. The supplementary coalescence paper Chen–Dagard–Derrida–Shi, arXiv:2001.00853, constructs continuum scaling solutions. Li–Zhang, arXiv:2411.12189 (2024), studies scaling limits of a family of generalized discrete models; it does not prove the fixed-initial-law critical asymptotics here. These are not fixed-m moment theorems. The exact OpenAlex title/DOI/year inventory and screening notes are also saved in sources/CITATION_AUDIT.txt.

No paper was located explicitly proving or refuting Conjecture 3 as an ordinary-moment theorem with the third tilted moment. The literal bare-critical statement has the counterexample consequence below. A counterexample consequence of prior internal work is not labeled RESOLVED_IN_LITERATURE, and a free-energy theorem is not presented as a direct ordinary-moment theorem.

The bare-critical counterexample: consequence of prior internal D0056

The input from our prior internal work D0056 is a nonconstant critical law, supported on {0,2,4,8,...}, for which
\[
 \limsup_{n\to\infty}n^2q_n=\infty. \tag{D0056}
\]
This was given in the task and corroborated by the brain's verified D0056 memory dated 13 November 2026. It is cited only as prior internal work. We do not claim the sparse-law construction as new here.

For a concrete parametrization of that construction, write a_j=2^j (j>=1) and
\[
 D=\sum_{j\ge1}\frac{(m-1)-a_j^{-1}+m^{-a_j}a_j^{-1}}{j^2},\quad C=D^{-1},
\]
\[
 p_j=P(X_0=a_j)=\frac{C\,m^{-a_j}}{j^2a_j},\qquad
 p_0=C\sum_{j\ge1}\frac{(m-1)-a_j^{-1}}{j^2}.
\]
All terms defining p_0 and D are positive, D is finite, and p_0+sum p_j=1. Directly,
\[
 E[m^{X_0}]=C(m-1)\sum_{j\ge1}j^{-2}
 =(m-1)E[X_0m^{X_0}]<\infty,
\]
whereas E[X_0^3m^{X_0}]=C sum a_j^2/j^2=infinity.

The prior survival estimate uses n_j=a_j-1: a leaf of size a_j can lose at most one unit per level, so any such leaf forces a positive root. The m^{n_j} leaf trials are independent. Hence the retained D0056 bound is
\[
 q_{n_j}\ge1-(1-p_j)^{m^{n_j}}
 \ge\tfrac12m^{n_j}p_j
 =\frac{C}{2m j^2a_j}
\]
for all sufficiently large j; the second inequality uses m^{n_j}p_j=C/(m j^2a_j)->0. Thus n_j^2q_{n_j}->infinity. This restates the earlier construction and estimate so the hypotheses are reviewable; it is not a second claimed discovery.

The new moment consequence needs no further construction. For every r>0 and every integer x>=0, x^r>=1_{x>0}. Therefore
\[
 n_j^2E[X_{n_j}^r]\ge n_j^2q_{n_j}\longrightarrow\infty.\qquad\square
\]
This refutes (M) for each positive r, as well as every proposed universal pointwise O(n^{-2}) bound under (C) alone. All ordinary moments exist: E[m^{X_n}] is finite at each finite n by the generating-function recursion. The infinite third tilted moment is essential to distinguishing this counterexample from the strengthened problem.

Proofs relating survival, conditional law and moments

Write p_{n,k}=P(X_n=k), q_n=1-p_{n,0}, and T_n(k)=P(X_n>=k). The next two lemmas apply to this recursion without a criticality assumption. Positivity of p_{n,0} is specified where needed.

Lemma A (a single positive path). For integers n,t>=0,
\[
 q_{n+t}\ge m^t T_n(t+1)\prod_{i=n}^{n+t-1}p_{i,0}^{m-1}. \tag{1}
\]
Proof. In the depth-t tree whose leaves have law X_n, fix one leaf with value at least t+1. At each successive level require the m-1 sibling subtrees to have root value zero. Their probabilities are p_{n+i,0}^{m-1}, i=0,...,t-1, and these subtrees and the chosen leaf are independent. The selected positive value loses exactly one per level and remains positive. There are m^t leaf choices. The resulting events are disjoint: at the first branching where two choices separate, each event demands that the other's positive path lie in a zero sibling subtree. Summing their probabilities proves (1). For t=0 the assertion is equality. □

In particular, if sum q_i<infinity and all p_{i,0}>0, the infinite product is positive. Indeed, eventually q_i<=1/2 and -log(1-q_i)<=2q_i; the finitely many earlier factors are positive. Consequently for a finite B,
\[
 T_n(k)\le Bm^{-(k-1)}q_{n+k-1},\qquad n\ge0,\ k\ge1. \tag{2}
\]
A product starting at any sufficiently large fixed N also suffices for n>=N.

Lemma B (slowly changing survival implies the conditional geometric law). If q_n>0 eventually, q_n->0, and q_{n+1}/q_n->1, then
\[
 p_{n,k}/q_n\longrightarrow(m-1)m^{-k}\quad\text{for each }k\ge1, \tag{3}
\]
and the conditional laws converge in total variation to pi.

Proof. A root equals zero precisely when the child sum is zero or one. Thus
\[
 q_{n+1}=1-(1-q_n)^m-mp_{n,1}(1-q_n)^{m-1}.
\]
Divide by q_n and use 1-(1-q_n)^m=mq_n+O(q_n^2). This gives p_{n,1}/q_n->(m-1)/m. For k>=1, distinguish exactly one positive child from at least two positive children:
\[
 p_{n+1,k}=m(1-q_n)^{m-1}p_{n,k+1}+R_{n,k},\qquad
 0\le R_{n,k}\le {m\choose2}q_n^2.
\]
Induction in k, using q_{n+1}/q_n->1, proves (3). Since sum pi_k=1, pointwise convergence of these probability masses implies total variation convergence: first restrict to finitely many k so the pi-tail is small, then bound the remaining conditional tail by its mass. □

Weak or total variation convergence alone would not justify convergence of unbounded moments. The following proof supplies that missing step.

Theorem C (survival asymptotics imply all positive moments). Suppose for some A>0 and b>1,
\[
 q_n\sim A n^{-b}.
\]
Then (3) holds and, for every real r>0,
\[
 \frac{E[X_n^r]}{q_n}\longrightarrow
 M_r(m):=(m-1)\sum_{k\ge1}k^r m^{-k}. \tag{4}
\]
In fact the conditional exponential moments converge for every 1<s<m.

Proof. Lemma B applies. For sufficiently large N and all n>=N, q_n is between (A/2)n^{-b} and 2A n^{-b}; thus q_{n+t}/q_n<=4 for every t>=0. Also sum_{n>=N}q_n<infinity and p_{n,0}>0. The positive product in Lemma A therefore gives, uniformly in n>=N and k>=1,
\[
 P(X_n\ge k\mid X_n>0)\le4B m^{-(k-1)}. \tag{5}
\]
In particular p_{n,k}/q_n is at most this bound. The sequence 4B k^r m^{-(k-1)} is summable for every fixed real r>0. Dominated convergence and (3) prove (4). Replacing k^r by s^k proves the exponential-moment assertion. □

Taking b=2 and A=4/(m-1)^2 yields exactly c(r,m) in (M). In particular M_1(m)=m/(m-1). This proves the full reduction from the survival conjecture, without assuming the third tilted moment as an additional step. It does not prove the premise q_n~A/n^2.

Theorem D (equivalence with the first moment under criticality). Within the source hypotheses, (S), the r=1 assertion of (M), and all the assertions of (M) together are equivalent.

Proof. Theorem C gives (S) => all (M), and all (M) trivially implies its r=1 case. For the remaining direction let mu_n=E[X_n]. Since for an integer S>=0, (S-1)^+=S-1+1_{S=0},
\[
 \mu_{n+1}=m\mu_n-1+(1-q_n)^m. \tag{6}
\]
If mu_n~D/n^2 with D>0, then mu_{n+1}/mu_n->1. Equation (6) implies
\[
 1-(1-q_n)^m=m\mu_n-\mu_{n+1}\sim(m-1)D/n^2.
\]
The left side tends to zero, so q_n->0, and it is asymptotic to m q_n. Hence q_n~(m-1)D/(m n^2). With D=4m/(m-1)^3 this is (S). □

The first-moment implication from survival was already proved in the source (Lemmas 4–5, pp.14–15); that part is prior published work. Lemmas A–B and the dominated-convergence argument above give a complete all-positive-moment reduction here. No priority claim is made for these elementary extensions.

Bounds actually available for all r>0

1. Beyond-m exponential moment. Under (C) and E[t^{X_0}]<infinity for some t>m, the Chen–Hu–Shi propositions give, for each fixed r>0, constants a_r,b_r,nu>0 and sufficiently large n such that
\[
 \frac{a_r}{n^2(\log n)^\nu}\le E[X_n^r]
 \le\frac{b_r(\log n)^2}{n^2}. \tag{7}
\]
Thus E[X_n^r]=n^{-2+o(1)} for every real r>0.

Proof. Use X_n^r>=1_{X_n>0} and Proposition 5.1 with ell=0 for the lower bound. For the upper bound use the exact tail identity
\[
 E[X_n^r]=\sum_{k\ge1}\big(k^r-(k-1)^r\big)T_n(k), \tag{8}
\]
proved by telescoping x^r for each integer x and applying Tonelli to nonnegative summands. Proposition 4.1 bounds T_n(k) by C m^{-(k-1)}(log n)^2/n^2. The coefficient sum in (8) with this geometric weight is finite. The exponential-moment hypothesis implies the fifth tilted moment needed for that upper bound, since k^5(m/t)^k is bounded. □

The upper inequality alone needs only E[X_0^5m^{X_0}]<infinity. These are logarithmic bounds, not pointwise order n^{-2} with fixed positive constants. The lower bound in (7) uses a stronger assumption than the third tilted moment.

2. Third tilted moment only. The source's harmonic bounds extend to every r>0:
\[
 0<\liminf_{N\to\infty}\frac1{\log N}\sum_{n=1}^N nE[X_n^r]
 \le\limsup_{N\to\infty}\frac1{\log N}\sum_{n=1}^N nE[X_n^r]<\infty. \tag{9}
\]
Here the constants may depend on r,m and the initial law.

Proof. Proposition 4 of the source says that H(N):=sum_{n=1}^N n q_n is between positive multiples of log N for sufficiently large N. In particular H(N)<=C log(N+2) for all N. Grouping into dyadic intervals,
\[
 \sum_{n=2^j}^{2^{j+1}-1}q_n\le2^{-j}H(2^{j+1})\le C'(j+1)2^{-j},
\]
so sum q_n<infinity. The source assumptions give p_{0,0}>0: if X_0>=1 almost surely, ((m-1)X_0-1)m^{X_0} is nonnegative, and its mean can vanish only for m=2, X_0=1 almost surely, which is excluded. Also p_{n+1,0}>=p_{n,0}^m>0. Thus (2) applies. Set d_r(k)=k^r-(k-1)^r>0. From (8), Tonelli, and j=n+k-1>=n,
\[
 \sum_{n=1}^N nE[X_n^r]
 \le B\sum_{k\ge1}d_r(k)m^{-(k-1)}
       \sum_{n=1}^N n q_{n+k-1}
 \le BC\sum_{k\ge1}d_r(k)m^{-(k-1)}\log(N+k+1).
\]
Since log(N+k+1)<=log(N+2)+log(k+1), and both geometrically weighted sums converge, the result is O(log N). The positive lower harmonic bound follows from E[X_n^r]>=q_n and Proposition 4. □

There is also the elementary pointwise O(1/n) bound for every r>0 under the third tilted moment: x^r<=[sup_{k>=1}k^r/(m^k-1)](m^x-1), followed by Theorem 3. No pointwise Theta(n^{-2}) result under just this moment assumption is asserted here.

3. Conditional implication for pointwise order bounds. If one establishes c/n^2<=q_n<=C/n^2, then Lemma A and (8) immediately give c_r/n^2<=E[X_n^r]<=C_r/n^2 for every r>0. The proof is the same as Theorem C's uniform tail bound, using q_{n+t}/q_n<=C/c. These pointwise survival bounds are not proved here.

No nontrivial exactly solvable fixed-m critical family was identified in the cited Chen et al. source. The continuous-time and geometric-offspring solvable families do not furnish the requested special-family proof for this recursion. The stationary m=2 law X_0=1 is excluded by the source and is not a valid substitute.

Numerical evidence and audit

The deterministic law iteration and validation code are in code/. The primary runs use m=2 with initial supports {0,2} and {0,5}, and m=3 with supports {0,1} and {0,3}. For {0,b}, criticality sets
\[
 P(X_0=b)=\frac1{1+((m-1)b-1)m^b}.
\]
Thus the four positive probabilities are 1/5, 1/129, 1/4, and 1/136. These finite-support laws satisfy every integrability assumption above.

Each law was iterated through n=10,000 at output caps K=16,384 and K=32,768, using zero-padded FFT m-fold convolution. The code stores tilted coefficients a_k=m^k p_k, separates the zero atom analytically before FFT, and computes the two- or three-fold positive-part convolution. This limits cancellation from the large zero atom. Coefficients above K are discarded and their ordinary probability is put at zero; negative coefficients produced by roundoff are clipped, with the total clipped tilted mass recorded. No criticality projection or assumed geometric shape is imposed. Positive moments and conditional masses are calculated from a_k m^{-k}, avoiding subtraction of two numbers near one. The final runs also mask the exactly unreachable support and size each FFT to the reachable polynomial degree; this prevents spurious high-index roundoff during the first generations.

The requested longdouble type is only float64 on this Apple platform (52 stored mantissa bits); metadata records the actual type. Filenames ending “ld” denote the requested type and must not be interpreted as extended precision. Rounding error is not certified. A substantial defect in the *truncated tilted* critical identity at late n can come from deleting the remote tilted tail; it is not a bound on ordinary-moment error. Support/cap comparisons and independent high-precision checks are reported separately.

Numerical summaries, validation errors, reproduction commands and the cutoff proof follow below. Final results use the native-tagged files; exploratory ld-tagged files are retained to document the numerical audit. The CSV files retain the full checkpoints and conditional probabilities k=1,...,10, and track r=1/2,1,2,3. All numerical conclusions are evidence, not proofs of asymptotics.


Cutoff error in exact arithmetic. Criticality is preserved: differentiation of the generating-function recursion gives Delta_{n+1}=G_n(m)^{m-1}Delta_n, where Delta_n=(m-1)E[X_nm^{X_n}]-G_n(m). Moreover G_n(m)<=2 for all n. For m>=3, criticality gives p_{n,0}=sum_{k>=1}((m-1)k-1)a_{n,k}>=(m-2)sum_{k>=1}a_{n,k}, hence G_n(m)<=(m-1)/(m-2)<=2. For m=2, p_{n,0}=sum_{k>=2}(k-1)a_{n,k}, so G_n(2)<=2p_{n,0}+2p_{n,1}<=2.

Couple the exact capped recursion to the original on the same tree, replacing outputs above K by zero. It stays below the original. At each vertex the original output exceeds K only if the child sum is at least K+2, an event of probability at most 2^m m^{-(K+2)} by Markov's inequality. If d_n bounds the probability of a discrepancy in this coupling, the union bound gives
\[
 d_{n+1}\le m d_n+2^m m^{-(K+2)},\qquad d_0=0,
\]
\[
 d_n\le\frac{2^m}{m-1}m^{-(K+2)}(m^n-1). \tag{10}
\]
For K=16384 and n=10000 this is below 10^{-1921} for both m=2,3. It bounds survival error. For each fixed r>0, monotonicity and Cauchy–Schwarz give a moment-error bound sqrt(2 L_{2r,m}d_n), where L_{2r,m}=sup_{k>=0}k^{2r}m^{-k}<infinity. Thus cutoff error in exact arithmetic is negligible here. Equation (10) does not control FFT rounding, clipping, exponentiation, normalization, or floating-point underflow; the computations are not certified exact values.

Observed values at n=10,000 (K=32,768; rounded evidence):

| m, initial support | n^2 q_n | n^2 E[X_n^{1/2}] | n^2 E[X_n] | n^2 E[X_n^2] | n^2 E[X_n^3] | Conditional mean | Conditional TV upper estimate |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2, {0,2} | 4.007964 | 5.399265 | 8.014324 | 24.03656 | 104.1285 | 1.9996 | 0.0001000694 |
| 2, {0,5} | 4.004903 | 5.395141 | 8.008204 | 24.0182 | 104.049 | 1.9996 | 0.0001000312 |
| 3, {0,1} | 1.001401 | 1.189107 | 1.501951 | 3.003452 | 8.258029 | 1.49985 | 6.669995e-05 |
| 3, {0,3} | 1.000859 | 1.188462 | 1.501138 | 3.001826 | 8.253557 | 1.49985 | 6.668192e-05 |

The conjectured n^2 moment constants for r=(1/2,1,2,3) are approximately m=2: (5.38901501, 8, 24, 104), m=3: (1.18749416, 1.5, 3, 8.25). Predicted survival constants are 4 and 1, and conditional means 2 and 1.5, respectively. The polylogarithmic calculation of these constants was checked against direct 1,024-term sums at 60 decimal digits, and against independent rational formulas for r=1,2,3.

Across the two caps the maximum relative difference among n^2 survival and moment entries at n=10,000 was below 4.9e-9 in the final runs. This is an observed sensitivity, not a rigorous error bar; shared rounding bias is possible. A separate direct rational convolution checked normalization, exact criticality, the mean identity (6), the spine inequality (1), and all coefficients through three generations for all four laws; the largest absolute coefficient discrepancy from FFT was below 1.4e-17. Independent direct convolution at 70 decimal digits, n=100 and cap 128 agreed with same-cap FFT to relative survival/mean errors below 1.5e-11. These checks validate the recurrence implementation, not the limiting constant.

The TV entry compares the first 99 positive atoms with (m-1)m^{-k}, and adds both tails as an upper bound. Its agreement with the geometric law improves with n. The plotted evidence is [data/moment_evidence.svg](data/moment_evidence.svg); it shows the first two scaled moments divided by their conjectured constants, and conditional TV estimates. The data are consistent with the conjecture for these finite-support initial laws. They do not establish the conjecture for all admissible laws, or a convergence rate.

Reproduction (one numerical worker at a time):

```sh
python3 code/iterate.py --m 2 --b 2 --cap 32768 --steps 10000 --tag m2_b2_K32768_native
```

Repeat for (m,b)=(2,5),(3,1),(3,3), and caps 16384,32768 with matching tags. Then run:

```sh
python3 code/check_exact.py
python3 code/verify.py
python3 code/summarize.py
```

The scripts set numerical library and FFT workers to one and verify nice priority at least 10. Recorded numerical peak RSS stayed below 0.2 GB per process. At most two numerical checks overlapped, within the four-thread/4-GB limits; no large simulation, local language-model worker, or subagent was started. Python, NumPy, SciPy, mpmath and Matplotlib versions are recorded in data/environment.json. Only local files were written.

Remaining mathematical gap. Under the third tilted moment, the exact constant for q_n remains unproved in the literature located here. By Theorems C–D it is sufficient, and equivalent, to settle the proposed first moment and the collection of all positive moments. The harmonic bounds (9), the stronger-assumption logarithmic bounds (7), and numerical convergence do not close that gap.

Task: “Open problem D0058.” Launch clock: 2026-11-13 10:18 +04; exact prompt receipt time was not available.
