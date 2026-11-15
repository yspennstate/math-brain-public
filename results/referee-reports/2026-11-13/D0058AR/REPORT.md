MINOR

The sparse counterexample is correct for the statement obtained by imposing only the displayed criticality condition. Lemmas A and B, Theorem C, and the equivalence with the first-moment prediction are correct as stated in the submitted report. In particular, the inequality in Lemma A has the right direction, and Theorem C supplies the uniformity needed to pass from a conditional distributional limit to all positive moments. I found no mathematical gap in those arguments.

This does not refute the authors' qualified conjectural picture. Both arXiv versions expressly warn that additional integrability may be needed. Calling the bare displayed statement false is textually and mathematically correct; presenting this as a counterexample to the intended finite-third-tilted-moment conjecture would be unfair. The submitted report makes that distinction, so I do not recommend MAJOR or WRONG. The minor corrections concern the language about necessity and an omitted earlier public preprint refuting bare-critical survival. The numerical and literature checks below independently support the report's more limited conclusion.

The first-moment implication was already published in the source. The all-positive-moment implication is a useful elementary conditional reduction; I did not locate its exact general formulation in the screened papers, but this audit does not establish priority. No proof in print of the fixed deterministic-m, finite-third-tilted-moment Conjecture 3 was located through 13 November 2026.

1. Errors, gaps, and requested corrections

1. **Expected necessity is described too strongly.** Location: claim_files/REPORT.md:44, sentence beginning “Later literature explicitly treats the third tilted moment as necessary”. Chen–Hu–Shi, arXiv:2108.05610, pp.3–4, discuss what *should* hold and give different expected asymptotics outside that moment class. They do not prove that every critical law with infinite third tilted moment violates the universal constants. The sparse law proves that criticality alone is insufficient. It does not prove that the third tilted moment is a necessary condition for those constants for every initial law. Fix: say that later literature identifies this as the expected integrability regime, and that the finite-third-moment conjecture remains unproved. This is a wording correction; none of the submitted proofs uses that claimed necessity.

2. **The classification must travel with its qualification.** Location: claim_files/REPORT.md:1, 5–7, 44–46. The isolated label COUNTEREXAMPLE can be mistaken for a solution of the qualified open problem. The opening already limits it to the bare-critical formulation, so this is a presentation caution rather than a missing proof. Fix in any abstract, problem ledger, or extracted summary: retain “counterexample under criticality alone; the finite-third-tilted-moment version remains open”. Do not say the authors overlooked integrability: they explicitly raised it.

3. **Some supporting artifacts referenced by the report were not in the supplied packet.** Location: claim_files/REPORT.md:11, 56, 67, 76, which refer to claim-run sources/ files. The supplied claim_files/ contains REPORT.md, LOG.md, code/, and data/, but no sources/. This is a limitation of the packet I received, not evidence that those downloads were never made. Fix for a self-contained submission: supply the cited plain-text sources and retrieval metadata. I independently retrieved the principal texts into this audit's sources/; my conclusions do not depend on the missing claim-run texts.

4. **The literature audit misses an existing public related counterexample.** Location: claim_files/REPORT.md:56–78, especially the stable-law route discussed on line 62. the author's “The survival probability of a heavy-tailed critical Derrida-Retaux system” is already public at [Zenodo](https://doi.org/10.5281/zenodo.24139608), with an earlier public version [here](https://doi.org/10.5281/zenodo.24063839). It is dated 5 November 2026 in the PDF; the repository records give 8 and 11 November as release dates. Theorem 1.1 treats m=2 and p_k=c2^−k k^−3, k≥2, and proves liminf n²q_n≤3/2. Fix: cite this as an earlier public bare-critical survival refutation, separately from the internal sparse-law construction. It neither proves C nor contains the sparse-law unbounded-subsequence argument. The novelty assessment must acknowledge both predecessors. I retrieved and read the primary preprint, saved as sources/prior_heavy_tail_2026.txt; this finding does not affect the mathematical verdict on the submitted sparse construction.

No correction is required to Lemma A (lines 121–131), Lemma B (133–148), Theorem C (152–169), or Theorem D (171–183). No sign error, disjointness failure, or omitted uniformity condition was found. Novelty of C is unestablished, rather than a proved new result; the report's statement that it makes no priority claim should be retained.

2. What the original source actually says

I fetched [arXiv v1](https://arxiv.org/pdf/1705.04787v1) and [arXiv v2](https://arxiv.org/pdf/1705.04787v2) independently. They are saved as sources/source_v1.txt and sources/source_v2.txt, with URL, retrieval time, downloaded-byte SHA256 and extracted-text SHA256 in sources/retrieval.json.txt. PDF bytes existed only in memory and in the pdftotext pipe. No PDFs, page images, or scans were saved. The short unedited extraction passages are also in sources/conjectures_v1_exact.txt and sources/conjectures_v2_exact.txt; equations below restore mathematical glyphs lost by extraction.

The v1 title is “A hierarchical renormalization model: some properties and open questions” (13 May 2017). The v2 title is “A max-type recursive model: some properties and open questions” (26 June 2019). Both exclude an almost surely constant X_0 at the beginning. This matters because m=2, X_0=1 almost surely is stationary and critical. The counterexample under review is nonconstant, so it respects this exclusion.

The setting is integer m≥2, nonconstant X_0 in Z_+, independent copies at each recursion, and, in v2 equation (4),

\[
(m-1)\mathbf E(X_0m^{X_0})=\mathbf E(m^{X_0})<\infty. \tag{C}
\]

Here are the exact mathematical statements of Conjectures 1–3 in v2; the connective prose is summarized. Their original wording is in the unedited text excerpts above. Conjecture 1 is on PDF p.3, the others on p.4.

**Conjecture 1.** Under (C),

\[
\mathbf P(X_n\ne0)\sim\frac4{(m-1)^2}\frac1{n^2},\qquad n\to\infty.
\]

**Conjecture 2.** Under (C), \(\mathcal L(X_n\mid X_n\ne0)\Rightarrow\mathcal L(Y_\infty)\), where \(\mathbf P(Y_\infty=k)=\frac{m-1}{m^k}\), \(k=1,2,\ldots\).

**Conjecture 3.** Under (C),

\[
\mathbf E(X_n)\sim\frac{4m}{(m-1)^3}\frac1{n^2},\qquad n\to\infty,
\]

and, for each real \(r>0\),

\[
\mathbf E(X_n^r)\sim\frac{c(r)}{n^2},\qquad n\to\infty,
\]

where \(c(r)=c(r,m):=\frac4{m-1}\sum_{k=1}^{\infty}\frac{k^r}{m^k}\).

The integrability qualification is after **Conjecture 4**, on the same PDF p.4, rather than immediately after Conjecture 3. Its exact wording is:

“Possibly some additional integrability conditions, such as \(\mathbf E(X_0^3m^{X_0})<\infty\) in Theorem 3 below, are necessary for our conjectures to hold.”

Conjecture 4 predicts

\[
\mathbf E(s^{X_n})-1\sim\frac{4m}{(m-1)^2}\frac{s-1}{m-s}\frac1{n^2}
\quad(0<s<m,\ s\ne1),
\]

and \(\mathbf E(m^{X_n})-1\sim2/((m-1)n)\). It is useful to include it because this is the conjecture immediately preceding the quoted qualification.

In v1, Conjectures 1–3 are numbered 1.3, 1.4, 1.5. Their formulas and substantive wording are identical, with “Assume (1.4)” replacing “Assume (4)”. The qualification is identical except for “Theorem 1.7” in place of “Theorem 3”; it follows Conjecture 1.6. Theorem 1.7 in v1 and Theorem 3 in v2 explicitly assume the third tilted moment and prove order 1/n bounds for \(\mathbf E(m^{X_n})-1\), not Conjecture 3. These statements were checked in the full retrieved texts, not inferred from the claim's paraphrase.

Thus “the literal criticality-only display is false” is a correct reading of the display. The full authors' wording is qualified, however, and the sparse construction answers the integrability concern in the direction they anticipated. The arXiv wording does not support either silently inserting the third moment into equation (4), or announcing a refutation of the qualified research conjecture. I did not obtain a separate typeset Springer chapter text; I make no claim about unexamined differences between that typesetting and v2.

3. Independent verification of the sparse law

Set \(a_j=2^j\), j≥1, and

\[
D=\sum_{j\ge1}\frac{(m-1)-a_j^{-1}+m^{-a_j}a_j^{-1}}{j^2},
\quad C=D^{-1},
\]

\[
p_j=\mathbf P(X_0=a_j)=\frac{C m^{-a_j}}{j^2a_j},\qquad
p_0=C\sum_{j\ge1}\frac{(m-1)-a_j^{-1}}{j^2}.
\]

Each summand of p_0 is positive, since m−1−1/a_j≥1/2. Also

\[
0<(m-1)\zeta(2)-\operatorname{Li}_2(1/2)\le D<(m-1)\zeta(2),
\]

so C is finite and positive. Directly p_0+Σp_j=CD=1, and p_0>0 and p_1>0, establishing a nonconstant probability law.

Separately summing the tilted quantities gives

\[
\begin{aligned}
\mathbf E(m^{X_0})
&=p_0+C\sum_{j\ge1}\frac1{j^2a_j}
=C(m-1)\zeta(2)<\infty,\\
\mathbf E(X_0m^{X_0})&=C\sum_{j\ge1}j^{-2}=C\zeta(2).
\end{aligned}
\]

This proves (C) exactly. On the other hand,

\[
\mathbf E(X_0^3m^{X_0})=C\sum_{j\ge1}\frac{a_j^2}{j^2}=\infty.
\]

Indeed even the second tilted moment diverges. All ordinary positive moments are finite at every finite generation: the generating-function recursion preserves finiteness at m, and any fixed power is bounded by a constant times m^x.

For a depth-n m-ary tree, the root is at least \((x-n)^+\) if one specified leaf has value x, regardless of the other leaves. This follows by induction because all other child contributions are nonnegative. With n_j=a_j−1, a leaf equal to a_j therefore forces a positive root. The m^{n_j} initial leaves are independent; unlike Lemma A, these leaf events need not be disjoint, and the union probability accounts for that exactly:

\[
q_{n_j}\ge1-(1-p_j)^{m^{n_j}}.
\]

Writing \(\lambda_j=m^{n_j}p_j=C/(m j^2a_j)\to0\),

\[
1-(1-p_j)^{m^{n_j}}\ge1-e^{-\lambda_j}\ge\lambda_j/2
\]

for all sufficiently large j. Consequently

\[
n_j^2q_{n_j}\ge\frac{C(a_j-1)^2}{2m j^2a_j}\longrightarrow\infty.
\]

This is stronger than merely an unbounded limsup along an unspecified subsequence: the displayed lower bounds diverge along n_j. It contradicts every eventual bound q_n≤K/n² for a fixed K. For each real r>0, x^r≥1_{x>0} on Z_+, so the same subsequence forces \(n_j^2\mathbf E(X_{n_j}^r)\to\infty\). The ordinary-moment counterexample holds simultaneously for all such r and for every integer m≥2. No input from a brain note or an unprovided internal proof is needed.

I recomputed the constants at 90 decimal digits, using

\[
D=(m-1)\zeta(2)-\operatorname{Li}_2(1/2)
+\sum_{j\ge1}\frac{m^{-2^j}}{j^2 2^j}.
\]

The last sum is exceptionally rapidly convergent. The omitted terms after j=12 are bounded, for example, by \(m^{-8192}\sum_{j\ge13}1/(j^2 2^j)\), far below the working precision. As a second check, I separately summed the probabilities and tilted mass; the tilted first-moment remainder was evaluated with the trigamma tail \(\sum_{j>512}j^{-2}=\psi_1(513)\). Normalization residuals were zero at the working precision and criticality residuals below 2×10^−90.

| m | C | p_0 | E[m^{X_0}] |
|---|---:|---:|---:|
| 2 | 0.839169686150 | 0.891780204757 | 1.380378804614 |
| 3 | 0.361800144400 | 0.979620059277 | 1.190274765828 |

Here are values of the rigorous-form lower expression \(C(a_j-1)^2/(2m j^2a_j)\), rounded, rather than numerical estimates of the actual survival probability:

| j | n_j | m=2 | m=3 |
|---|---:|---:|---:|
| 10 | 1,023 | 2.14408060 | 0.61626683 |
| 20 | 1,048,575 | 549.957197 | 158.072594 |
| 40 | 1,099,511,627,775 | 144,168,254 | 41,437,861 |

The independent code also evaluates the larger exact leaf-union bound via log1p and expm1; see data/validation.json. It never attempts to construct m^{n_j} individual leaves. These numerical checks illustrate an analytic divergence proof, not a simulation claim.

4. Lemma A, checked line by line

Fix n,t and one leaf v in a depth-t tree whose leaves have law X_n. Define E_v by: the chosen leaf is at least t+1, and every sibling subtree root encountered on its path to the root is zero. At level i above the leaves, the m−1 sibling roots have law X_{n+i}, for i=0,…,t−1. Their underlying leaf sets are mutually disjoint, including across different levels, and disjoint from v. Thus

\[
\mathbf P(E_v)=T_n(t+1)\prod_{i=0}^{t-1}p_{n+i,0}^{m-1}.
\]

On this event, the selected path loses exactly one at each step, and is positive throughout. For two different choices v,w, take their first common ancestor. On E_v, the child subtree containing w has zero root; on E_w, that same subtree has a positive root. Therefore E_v and E_w are incompatible. This checks disjointness using subtree root values, rather than incorrectly requiring all other leaves to vanish.

There are m^t choices, all E_v imply survival, and hence

\[
q_{n+t}\ge m^t T_n(t+1)\prod_{i=n}^{n+t-1}(1-q_i)^{m-1}. \tag{A}
\]

The t=0 case is equality. Independence is required within each E_v, not between different E_v. No criticality assumption is used.

Putting t=k−1 and dividing by a positive product gives exactly

\[
T_n(k)\le
\frac{q_{n+k-1}}{m^{k-1}\prod_{i=n}^{n+k-2}(1-q_i)^{m-1}}. \tag{A'}
\]

The direction is **upper** for T_n(k). There is no inversion error. If Σ_{i≥N}q_i<∞ and q_i<1 for i≥N, then

\[
P_N:=\prod_{i=N}^{\infty}(1-q_i)^{m-1}>0.
\]

Every finite product in (A') for n≥N is at least P_N. Thus

\[
T_n(k)\le P_N^{-1}m^{-(k-1)}q_{n+k-1}
\quad(n\ge N,\ k\ge1). \tag{A''}
\]

This proves the necessary uniformity in both indices. The claim sensibly permits a late N, so no early zero atom assumption is hidden in Theorem C.

I additionally enumerated all depth-two trees with leaves in {0,3}, for m=2 and 3. Every selected-path event forces positive root, and at most one occurs in every configuration. Rational law iteration also checked (A) for every n,t with n+t≤3 for four different laws. These finite checks supplement the proof; they do not replace it.

5. Lemma B and Theorem C

A child sum gives zero output exactly when its value is 0 or 1. Therefore

\[
q_{n+1}=1-(1-q_n)^m-mp_{n,1}(1-q_n)^{m-1}.
\]

Under q_n>0 eventually, q_n→0, and q_{n+1}/q_n→1, division by q_n yields

\[
\frac{p_{n,1}}{q_n}\longrightarrow\frac{m-1}{m}.
\]

For k≥1, exactly one positive child contributes

\[
p_{n+1,k}=m(1-q_n)^{m-1}p_{n,k+1}+R_{n,k},
\quad0\le R_{n,k}\le {m\choose2}q_n^2.
\]

The upper bound follows by a union bound over pairs of positive children, so it is uniform in k. If p_{n,k}/q_n→π_k, then p_{n+1,k}/q_n→π_k as well, by the ratio assumption. Dividing the recursion by q_n therefore gives π_{k+1}=π_k/m. Induction proves

\[
\pi_k=(m-1)m^{-k},\qquad k\ge1.
\]

These masses sum to one. Pointwise convergence of probability masses to a probability mass function gives convergence in total variation: choose a finite set carrying arbitrarily nearly all the limiting mass, and control the two remaining tails by their total masses. This is valid without a moment assumption.

The ratio condition **alone** does not suffice outside the source's critical, nonconstant setting. For example m=2, X_0=1 almost surely has q_n=1, ratio 1, and conditional law δ_1. Lemma B explicitly includes q_n→0, so it does not make this mistake. Under the source hypotheses that limit follows from its Theorem 2.

For Theorem C, suppose q_n∼A n^−b with A>0 and b>1. For some N and every n≥N,

\[
\tfrac A2 n^{-b}\le q_n\le2A n^{-b},\qquad
\frac{q_{n+t}}{q_n}\le4\Big(\frac n{n+t}\Big)^b\le4
\quad(t\ge0).
\]

Also Σ_{n≥N}q_n<∞ and q_n<1. With B=P_N^−1, (A'') implies

\[
\frac{p_{n,k}}{q_n}\le\frac{T_n(k)}{q_n}
\le4B m^{-(k-1)}\quad(n\ge N,\ k\ge1). \tag{U}
\]

This is exactly the missing uniform-integrability step that would not follow merely from weak or total variation convergence. For each fixed real r>0, the series Σ k^r m^{-(k-1)} converges. For each 1<s<m, the series Σ s^k m^{-(k-1)} converges. Applying dominated convergence to (U) and Lemma B proves

\[
\frac{\mathbf E(X_n^r)}{q_n}\longrightarrow
(m-1)\sum_{k\ge1}k^r m^{-k},\qquad r>0,
\]

\[
\mathbf E(s^{X_n}\mid X_n>0)\longrightarrow
\frac{(m-1)s}{m-s},\qquad1<s<m.
\]

All quantifiers and constants in the submitted proof are adequate. No monotonicity of q_n is assumed or needed. A one-step ratio limit would not by itself give (U); the full power asymptotic supplies the bound for *all* future times. The endpoint s=m is not covered and is not claimed.

For equivalence with the first moment, write μ_n=E(X_n). The exact identity

\[
\mu_{n+1}=m\mu_n-1+(1-q_n)^m \tag{I}
\]

follows from \((S-1)^+=S-1+1_{S=0}\) for integer S≥0. If μ_n∼D/n², then

\[
1-(1-q_n)^m=m\mu_n-\mu_{n+1}
\sim(m-1)D/n^2,
\]

so q_n→0 and q_n∼(m−1)D/(mn²). With D=4m/(m−1)^3 this is Conjecture 1. Conversely C with A=4/(m−1)^2 gives Conjecture 3 for all r>0. Thus survival, the specified first-moment asymptotic, and the collection of all specified positive-moment asymptotics are equivalent in the source's setting. The claim does not prove equivalence with an arbitrary *single* prescribed r≠1, and should not be read that way.

The extra all-r bounds in claim_files/REPORT.md:185–224 also check out. Chen–Hu–Shi's tail bound can be summed against k^r−(k−1)^r. The harmonic estimate uses the source's harmonic survival bound to obtain Σq_n<∞, then (A'') and Tonelli. These are bounds or conditional consequences, not a proof of the conjectured pointwise constants.

6. Independent numerical evidence

I wrote code/independent_iteration.py and code/validate.py for this audit, without reading or reusing claim_files/code. The algorithm iterates the deterministic convolution recurrence for the law, rather than sampling a population. At generation n it stores a_{n,k}=m^k p_{n,k} for k≥1 and computes p_{n,0} by ordinary normalization. If B_n(z)=Σ_{k≥1}a_{n,k}z^k, then

\[
a_{n+1,k}=\frac1m[z^{k+1}](p_{n,0}+B_n(z))^m,\quad k\ge1.
\]

The zero atom is separated analytically from the FFT. Each convolution is zero-padded to its full polynomial length; impossible support indices are masked. Outputs above K are replaced by zero, with ordinary mass retained at zero. Small negative coefficients from roundoff are clipped and the total clipped tilted mass is recorded. There is no projection onto criticality or onto a geometric shape. This is floating-point law iteration with a controlled cutoff, not exact rational arithmetic for all 3,000 generations.

For an initial law on {0,b},

\[
\mathbf P(X_0=b)=\frac1{1+((m-1)b-1)m^b}.
\]

I used (m,b)=(2,2),(2,4),(3,1),(3,2), with positive probabilities 1/5, 1/49, 1/4, 1/28. All have finite third tilted moment and every other exponential moment. Each was iterated to n=3,000, with K=8,192 and K=16,384 independently. Each FFT used one worker; the processes ran at nice 10 and the numerical iteration's peak recorded RSS was below 87 MB.

At n=3,000 and K=16,384:

| m,b | n²q_n | n²E[X_n^0.5] | n²E[X_n] | n²E[X_n²] | n²E[X_n³] | conditional mean | conditional TV |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2,2 | 4.021772 | 5.416741 | 8.038177 | 24.093072 | 104.303263 | 1.998665 | 0.000333905 |
| 2,4 | 4.014265 | 5.406631 | 8.023176 | 24.048132 | 104.108801 | 1.998667 | 0.000333593 |
| 3,1 | 1.003872 | 1.191920 | 1.505306 | 3.009105 | 8.270144 | 1.499500 | 0.000222504 |
| 3,2 | 1.002785 | 1.190629 | 1.503676 | 3.005848 | 8.261194 | 1.499500 | 0.000222383 |

The predicted rows are (4, 5.38901501, 8, 24, 104), with conditional mean 2, for m=2; and (1, 1.18749416, 1.5, 3, 8.25), with conditional mean 1.5, for m=3. Conditional TV is the distance from π_k=(m−1)m^−k for the computed law. The missing geometric tail beyond the represented array is negligible at these caps. The conditional exponential moment at s=1.5 for m=2 is about 2.99600, versus its limit 3; at s=2 for m=3 it is about 3.99600, versus its limit 4.

The CSVs include n=10,20,50,100,200,500,1000,2000,3000 and the first ten conditional masses. They show approach to the predictions across generations, rather than agreement at one chosen n. For m=2,b=2, for example, the first conditional mass approaches 1/2 and the second approaches 1/4. The numerical r=0.5 case checks a nonintegral moment as requested; r=1,2,3 check higher moments.

Validation was independent in the following senses:

* Fraction-based direct convolution through generation 3, for all four laws, verifies exact normalization, exact criticality, identity (I), and all applicable instances of (A). Its coefficients agree with FFT positive atoms to at most 5.6×10^−17 absolute error.
* Direct ordinary-probability convolution at 75 decimal digits, cap 96 and n=80, agrees with the same-cap FFT in survival and mean to relative error below 2.0×10^−13. This comparison checks the implementation and roundoff at that horizon; it is not a long-time precision certificate.
* The maximum relative difference in the final scaled survival/moment values between K=8,192 and K=16,384 is below 2.3×10^−10. This is a sensitivity check, not a rigorous FFT error bound.
* Predicted constants were recomputed independently using 1,024-term sums at 70 digits and polylogarithms; r=1,2,3 also agree with rational closed forms. For the two laws shared with the claim's runs, I compared all common checkpoints through n=2,000 against its native-tagged CSVs; the maximum relative survival/moment difference was below 10^−9. See data/constants.json and data/claim_numerical_comparison.json.
* The cutoff, considered in exact arithmetic, is rigorously harmless at n=3,000. Under criticality G_n(m)=E[m^{X_n}]≤2. For m≥3 this follows from p_{n,0}=Σ_{k≥1}((m−1)k−1)a_{n,k}; for m=2 it gives G_n(2)≤2(p_{n,0}+p_{n,1})≤2. Criticality is preserved by the generating-function recursion. Markov's inequality at each vertex and a monotone coupling give

\[
d_n\le\frac{2^m}{m-1}m^{-(K+2)}(m^n-1),
\]

where d_n bounds the probability that the exact and exactly capped roots differ. For K=8,192, n=3,000, its base-ten logarithm is below −1562 for m=2 and −2477 for m=3. Moment errors are bounded by \(\sqrt{2L_{2r,m}d_n}\), where \(L_{2r,m}=\sup_{k\ge0}k^{2r}m^{-k}<\infty\). Thus the cutoff cannot explain the observed finite-n deviations from the conjectured constants. This argument does not bound floating-point error.

The nonzero *capped tilted* critical defects in the JSON metadata are expected from discarding a remote tilted tail. They are not ordinary-moment error estimates. Likewise, agreement at two caps does not rule out shared floating-point bias. The data are evidence consistent with C's conclusion for finite-support laws, not proof of either its premise or the universal conjecture.

Reproduce locally, one process at a time:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 10 python3 code/independent_iteration.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 10 python3 code/validate.py
```

If the shell already runs at nice 10, omit nice; the iteration checks its actual priority. Numerical results are in data/*.csv, data/summary.json and data/validation.json.

7. Literature and value

The following comparisons use the independently retrieved primary texts. Page numbers are PDF pages of those arXiv versions unless otherwise stated. An absence conclusion is limited to the searched papers and citation records; it is not a proof that no uncatalogued work exists.

| Work | What it proves or says | Effect on the claim |
|---|---|---|
| [Chen–Derrida–Hu–Lifshits–Shi, v2](https://arxiv.org/pdf/1705.04787v2), §6, pp.13–15 | Lemma 4 gives identity (I); Lemma 5 turns a regular power asymptotic for a_n−λa_{n+1} into one for a_n. They explicitly deduce the conjectured first moment from the survival asymptotic. The conditional generating-function discussion assumes existence of its limit. | Survival ⇒ first moment is already published. Full conditional exponential-moment convergence from survival alone is not proved there; C supplies an elementary way of justifying that step. |
| Same source, Theorem 3 and Propositions 4–5, pp.5,22–24 | Order 1/n tilted generating-function bound under the third tilted moment; positive finite harmonic lower/upper bounds for n²q_n and n²E[X_n]. | Harmonic averages do not establish the pointwise constants. |
| [Chen–Hu–Shi, arXiv:2108.05610](https://arxiv.org/pdf/2108.05610), PTRF 182 (2022), 641–684 | Theorem 1.2, p.3, assumes E[t^{X_0}]<∞ for some t>m and proves q_n=n^−2+o(1), E[X_n]=n^−2+o(1). Proposition 4.1, p.22, gives T_n(ℓ+1)≤C(log n)²/(m^ℓ n²) under the fifth tilted moment. Proposition 5.1, p.34, gives the complementary logarithmic-loss lower bound under a beyond-m exponential moment. | Does not give q_n∼4/((m−1)²n²), and does not prove the finite-third-moment conjecture. Its hypotheses cannot be silently weakened. |
| [Chen–Dagard–Derrida–Hu–Lifshits–Shi, arXiv:1907.01601v3](https://arxiv.org/pdf/1907.01601v3), Ann. Probab. 49 (2021), 637–670 | Theorem 1.1, p.3, proves the near-supercritical free-energy exponent 1/2 under the third tilted moment; Theorem 1.2, p.4, gives exponent 1/(α−2) for tilted power tails. | The title's “Derrida–Retaux conjecture” concerns free energy as the initial mixing parameter varies, not these critical-time exact moment constants. |
| [Chen–Shi, arXiv:2006.06140](https://arxiv.org/pdf/2006.06140), pp.3–4 | Theorem 1.1 gives order n^{α−2} for the product of critical tilted generating functions for 2<α<4. Theorem 1.2 controls all derivatives at m under a beyond-m exponential moment. | Tilted factorial-moment bounds and product estimates are not Conjecture 3. The paper itself describes most corresponding discrete critical questions as open. |
| [Hu–Mallein–Pain, arXiv:1811.08749](https://arxiv.org/pdf/1811.08749), CMP 375 (2020), 605–651 | Theorem 1.9(iii), p.8, proves E[X_t]∼2/t² and a conditional Exp(1) limit for its solvable continuous-time family. | A different process. It does not supply C for arbitrary fixed-m discrete initial laws or settle their survival constant. |
| [Collet–Eckmann–Glaser–Martin](https://doi.org/10.1007/BF01224830), CMP 94 (1984), 353–370 | Critical iteration analysis and a heuristic asymptotic expansion. I retrieved the primary [1983 Strasbourg text](https://www.numdam.org/item/RCP25_1983__33__117_0.pdf); Appendix III, printed pp.138–139, explicitly introduces a smooth-asymptotic assumption before the formulas corresponding to the n^−2 prediction. | This is not a rigorous exact-moment theorem. Some formula extraction is poor; I do not pretend to have checked unreadable glyphs or substitute preprint pagination for the journal. The source and Chen–Shi give reliable modern descriptions of its scope. |
| [Derrida–Retaux 2014, arXiv:1401.6919](https://arxiv.org/pdf/1401.6919), JSP 156, 268–290 | The toy model, numerical work and continuum/perturbative predictions for critical behavior and depinning. | The discrete universal exact moment constants remain predictions in this work. |
| [Li–Zhang, arXiv:2411.12189](https://arxiv.org/pdf/2411.12189) | Generalized discrete-time processes, transition semigroups, and scaling limits to continuous-time DR-type processes. | Sending the discretization and model parameters to a scaling limit is not the n→∞ critical asymptotic of one fixed initial law in the deterministic-m model. |
| [Li–Zhang, arXiv:2411.13068](https://arxiv.org/pdf/2411.13068), JSP 192 (2025), article DOI 10.1007/s10955-025-03480-3 | Theorem 1.3 and Corollaries 1.5–1.9 establish exact critical expansions in the geometric-offspring, geometric-type marginal family. Remark 1.11, p.6, expressly distinguishes the constants from the deterministic-offspring predictions. In particular the survival constant is 2/(m−1)². | It is an exact solution for a different offspring law. Substituting mean offspring m for fixed offspring m is invalid. |
| [Alsmeyer–Hu–Mallein, arXiv:2502.02991v2](https://arxiv.org/pdf/2502.02991), revised April 2026 | Theorems on solvable generalized geometric-Galton–Watson systems; Corollary 2.7, p.10, gives a critical survival constant and conditional geometric law. | Again random offspring. The latest version retrieved in this audit is v2, not just the February 2025 version. |
| [Derrida–Shi, arXiv:2005.10208](https://arxiv.org/pdf/2005.10208), MMJ 20 (2020), 695–709 | The review separates finite-third-tilted-moment and stable regimes. §3 says that conditional tightness/weak convergence is not proved there; §2 distinguishes n^−2+o(1) from the conjectured constant. | Strong evidence that C is not simply a theorem proved in this review; its unconditional premise remains the difficult part. |
| [Chen–Hu–Shi, arXiv:2306.12717](https://arxiv.org/pdf/2306.12717), SPA 171 (2024), 104332 | Near-subcritical decay and the dual free-energy-type conjecture. Remark 1.2 gives a related existing leaf lower bound. | The leaf mechanism should not be advertised as new. These results do not prove the exact critical-time moment constants. |
| [Chen, arXiv:2405.09741](https://arxiv.org/pdf/2405.09741), published 2026, DOI 10.1007/s10114-026-4249-z | Infinite differentiability of F_∞(p), with respect to the initial mixing parameter. | Differentiability in p is not a theorem about the asymptotic value of E[X_n^r] at criticality. |
| [Duquesne–Shi, arXiv:2609.11435](https://arxiv.org/pdf/2609.11435), September 2026 | Brownian-CRT representation of the continuous DR branching process. Its introduction still calls the discrete conditional scaling-limit connection conjectural. | Does not prove the fixed-m exact moment asymptotics; a distinct continuous-process result. |

For forward citations I independently queried OpenAlex for the chapter DOI, arXiv DOI, and old-title record. These returned 11+1+1 records; the complete responses and title/DOI inventory are saved as sources/citers_*.txt and sources/citation_inventory.txt. I also ran a broader 2019–2026 topic query and primary-source web searches for critical moments, geometric conditional limits, exact asymptotics and recent DR work. This is more than a search for the words “Conjecture 3”.

The remaining forward citations were the coalescence-equation paper Chen–Dagard–Derrida–Shi (arXiv:2001.00853, continuous scaling solutions); Johnson–Junge–Lyu–Sivakoff (particle annihilation); the H^{2|2}/vertex-reinforced-jump-process paper (arXiv:2309.01221); Michel Pain's 2019 thesis; and two Collège de France statistical-physics annual reports. None supplies a theorem for the exact deterministic-m moment constants. Related random-offspring criticality criteria in Lotnikov–Kotova, arXiv:2502.02535, likewise concern a different question. Screening notes and search limitations are recorded in sources/CITATION_AUDIT.txt. Citation metadata may list an online year rather than a journal-volume year; it was not used to alter theorem hypotheses.

The broader topic search additionally found the public the author preprint described in correction 4. Its liminf bound is a different result from the sparse law's diverging n²q_n subsequence. It establishes an earlier bare-critical survival refutation, using Chen–Shi's stable product theorem, and expressly leaves the finite-third-moment problem open. I verified the statement and proof structure against the retrieved text; this audit does not treat the repository deposit as a peer-reviewed publication or claim a new external validation of that entire paper. Its exact statement does not supply the all-r lower-bound consequence obtained here from the sparse law, because an upper bound on a survival liminf cannot be used with X_n^r≥1_{X_n>0} to contradict a larger moment constant.

The value of the submitted result is therefore precise but limited. The prior sparse construction rigorously refutes the bare-critical formulation for every r>0. The independently checked additional theorem is:

For this deterministic m-ary integer recursion, if q_n∼A n^−b for A>0 and b>1, then the conditional law converges in total variation to (m−1)m^−k, every positive conditional moment converges to the corresponding geometric moment, and every conditional exponential moment with 1<s<m converges to (m−1)s/(m−s).

This theorem does not need criticality as a separate hypothesis. At the conjectured A,b it gives all of Conjecture 3, and identity (I) gives the converse from the specified first moment. The source already contains the first-moment implication and the expected limiting distribution; the additional content is a rigorous elementary tail argument that removes the conditional-moment gap. I found no explicit prior publication of this exact general reduction in the screened sources, but that does not warrant claiming a new resolution or established priority.

The finite-third-tilted-moment version of Conjecture 3 remains open in the literature located here. Numerical agreement, logarithmic-loss estimates, harmonic averages, and solutions of continuous-time or random-offspring models do not fill that gap.

Task: “You are an independent referee … Break it if it is wrong.” Launch clock: 13 November 2026, 10:50 +04; exact prompt receipt time unavailable. Work confined to this directory; no subagents, publication, or pushes.
