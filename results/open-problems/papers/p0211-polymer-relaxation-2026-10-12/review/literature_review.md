# Literature and priority review: uniform relaxation of linear polymers

Reviewed 12 October 2026. This is an internal research and editorial record. The bibliography is at ../paper/references.bib. No source was contacted and nothing was published as part of this review.

## Assessment

The theorem under review is a plausible, substantive specialized contribution: a finite-system spectral-gap estimate uniform in total mass and fragmentation rate,
\[
 (\beta+\sqrt\beta+n^{-1})/6
 \le \gamma_M(n,\beta)
 \le 4(\beta+\sqrt\beta+n^{-1}).
\]
It answers the order question for \(\beta_n\asymp n^{-1}\) in Aldous's notes and treats the neighboring rare-fragmentation transition as well. The existing model, equilibrium law, cycle representation, and general spectral methods require explicit credit.

I did not locate an earlier theorem stating this full uniform estimate. That is a bounded priority assessment, not a proof of absence. The closest inaccessible item is Granovsky–Zeifman (2000): its metadata and abstract were verified, and a later primary paper helps identify its example family, but its complete theorem statements were not obtained. Avoid “first ever,” “long-standing famous conjecture solved,” or a claim that all earlier coagulation–fragmentation work concerned equilibrium only.

The honest significance is a rigorous resolution of a concrete relaxation-order question, with a useful uniform theorem and an instructive symmetry argument. It is potentially publishable as a probability paper or research note if the proof and priority survive expert review. Its present scope does not justify describing it as a fieldwide breakthrough. It gives neither sharp asymptotic constants nor worst-case total-variation mixing times.

## Closest sources and exact comparisons

| Primary source | What overlaps | What is established or must be distinguished |
|---|---|---|
| Aldous, *A special aggregation-fragmentation process*, pp. 1–4 | Exact polymer rates, cycle auxiliary chain, stationary law, count chain | Proposition 1 gives the fixed-\(\beta\) bounds; the remarks on p. 4 identify the \(\beta_n\sim b/n\) order gap. This is the direct problem source. |
| Granovsky–Erlihson (2009), Proposition 1, Theorem 1, §2.3 | Exact reversible model under parameter substitution; autonomous count process; gap-comparison machinery | The explicit displayed bounds specialize to \(\beta+2/n\) and \(\beta+2-2/n\). They do not give the desired square-root scale. Their full-gap discussion needs care about the initial-law formula. |
| Hoze–Holcman (2018), §4 of the 2016 preprint | Same constant-kernel model after deterministic time rescaling | Stationary cluster-count and cluster statistics, together with tagged-cluster observables and associated times. No theorem yielding the present parameter-uniform full-chain gap was identified in the available full preprint. |
| Durrett–Granovsky–Gueron (1999), §§4–6 | Reversible coagulation–fragmentation and product-form equilibrium | Equilibrium structure and its properties are classical. These conclusions alone do not control relaxation uniformly. |
| Granovsky–Zeifman (2000) | General birth–death spectral-gap asymptotics | Full text unavailable; cannot certify exclusion. A primary follow-up identifies an equal-per-site-rate family that differs from the present chain. |

### Aldous: the directly stated problem

Use **AldousNotes**. The undated PDF is linked from a webpage whose history states “first written August 2012”; the webpage has a February 2018 update. Do not date the mathematical notes themselves unambiguously to 2012 or interpret the webpage update as a new proof.

On PDF p. 1, Proposition 1 gives
\[
 (1-o(1))(\beta^2+4\beta)^{-1/2}\le \tau_2\le \beta^{-1}
\]
for fixed \(\beta>0\). The remarks on PDF p. 4 discuss the bounds of orders \(\sqrt n\) and \(n\) at \(\beta_n\sim b/n\), and the suggested \(\sqrt n\) answer. The present theorem closes that order gap; its universal constants do not improve the sharpness of Aldous's fixed-parameter lower asymptotic.

Sources: [notes](https://www.stat.berkeley.edu/~aldous/Research/OP/coag_frag_mix.pdf); [problem-page history](https://www.stat.berkeley.edu/~aldous/Research/OP/coag_frag.html). Web refs: turn35view1, turn35view0.

### Granovsky–Erlihson: exact model, careful scope

Use **GranovskyErlihson2009**. In their notation take \(N=n,a=0,b=2/n,\phi(1,1)=\beta\). Proposition 1 gives our count rates. Equations (2.40)–(2.41) also reproduce the full split rates, including the equal-fragment convention. Equations (2.63)–(2.64), with \(\delta_r=1\), specialize to
\[
 \beta+2/n\le \gamma_Q\le \beta+2-2/n.
\]
Thus their displayed estimate does not settle the square-root regime.

Their prose identifies a solvable process's gap with the count gap. The explicit transition-law formula (2.43) uses initial distributions with specified Gibbs conditional laws within each count layer. That formula alone is insufficient to establish a full Poincaré inequality for arbitrary polymer observables. Do not label their statement false, or advertise full-gap equality as a newly posed open problem.

The substitution may depend on \(n\). More importantly, at \(\beta=b_0/n\), multiplying time by \(n\) gives fixed kernels. Their \(N\)-independence framework therefore does not itself exclude the target regime.

Source: [full preprint](https://arxiv.org/html/0711.0503v3); [published article](https://doi.org/10.1007/s10955-008-9671-3). Web refs: turn35view2, turn38view0, turn38view1, turn34search4.

### Granovsky–Zeifman: remaining access limitation

Use **GranovskyZeifman2000** if discussing general count-chain asymptotics. The exact citation is *Applied Stochastic Models in Business and Industry* 16(4), 235–248 (2000), DOI 10.1002/1526-4025(200010/12)16:4<235::AID-ASMB415>3.0.CO;2-S.

The publisher's abstract describes an extension of spectral-gap bounds and an \(N\)-limit for random walks on complete graphs. Publisher abstract/PDF/full-text routes did not yield the article. I did obtain its authors' later Russian paper, corresponding to **GranovskyZeifman2005**. Section 4 describes the asymptotic family in its reference [9] (=2000) as equal per-site rates \(\lambda_k=\mu_k\), with examples \(k^s\). Our per-site rates are \(\beta\) and \(k/n\), or \(b_0\) and \(k\) after the preceding time rescaling. This identified family differs, but the observation does not exclude other statements in the unavailable article.

Sources: [2000 publisher](https://onlinelibrary.wiley.com/doi/abs/10.1002/1526-4025(200010/12)16:4%3C235::AID-ASMB415%3E3.0.CO;2-S); [2004 original PDF](https://www.mathnet.ru/php/getFT.phtml?jrnid=tvp&option_lang=eng&paperid=242&what=fullt); [English translation metadata](https://doi.org/10.1137/S0040585X97980920). Web refs: turn39view0, turn49view0, turn60view2.

### Hoze–Holcman: same finite model, different observables

Use **HozeHolcman2018**, treating the 2016 arXiv posting and 2018 journal publication as one work. In §4, the rates \(C(i,j)=1\), \(F(i,j)=a\) yield count rates \(a(N-K)\) and \(K(K-1)/2\). Setting \(N=n,a=\beta n/2\), then multiplying the generator by \(2/n\), matches our normalization.

The inspected full preprint gives equilibrium cluster-count probabilities, size statistics, and tagged-cluster meeting/separation quantities. These are relevant finite-system results and deserve credit. They are different observables from a Poincaré constant uniform over all initial perturbations and all \((n,\beta)\).

Sources: [full preprint](https://arxiv.org/html/1611.06493v1); [arXiv metadata](https://arxiv.org/abs/1611.06493); [journal issue first-page metadata](https://imstat.org/publications/aap/aap_28_3/aap_28_3.pdf). Web refs: turn42view3, turn43view7, turn43view8, turn55search23. Journal DOI 10.1214/17-AAP1334, 28(3), 1449–1490.

## Earlier equilibrium and kinetic literature

**Kelly1979**, chapter 8, is the classical clustering-process background explicitly cited by Aldous. **Whittle1986** is also credited in the primary equilibrium literature. Their product-form background must not be presented as new. The author-hosted Kelly book listing and the books' citations in the inspected primary papers verify metadata; full relevant chapters were not obtained here. No precise theorem number from either book is asserted.

**DurrettGranovskyGueron1999** proves reversibility and product-form characterizations in §4 and studies equilibrium properties thereafter. Its Remark 2 credits Kelly and Whittle for the invariant-measure formula. [Full primary PDF](https://www.stat.berkeley.edu/~aldous/Research/OP/granovsky.pdf), web ref turn52view2; DOI 10.1023/A:1021682212351.

**AizenmanBak1979** concerns convergence to equilibrium for a deterministic polymer kinetic equation and exponential decay of a free-energy functional. This is relevant historical context, but transferring such a statement to a finite partition-valued chain requires a separate argument, especially with vanishing fragmentation. Do not claim its theorem directly proves or disproves the present bound. The abstract and metadata, together with the model comparison in Durrett–Granovsky–Gueron §2.2, were inspected; its full text was not obtained. [Publisher](https://doi.org/10.1007/BF01197880), web refs turn49view2, turn50view1.

**BerestyckiPitman2007**, Theorem 2, characterizes Gibbs partition laws under recursive fragmentation and their coalescent time reversals. It is useful context for the Gibbs weights and affine/constant collision families. Its central setting differs from an ergodic bidirectional chain's uniform relaxation estimate. [Full preprint](https://arxiv.org/pdf/math/0512378), web refs turn48view1, turn50view5; DOI 10.1007/s10955-006-9261-1.

**DOrsognaLeiChou2015** studies finite stochastic coagulation–fragmentation, assembly times, and equilibration, including strong-binding regimes and a maximum allowed cluster size. Its normalization of unordered split rates and its capped state space require care when comparing models. Its dynamics results mean that “all previous finite work was stationary” would be incorrect. No uniform gap theorem for the present normalization was identified in the inspected article. [Author PDF](https://www.math.ucla.edu/~tchou/pdffiles/JCP_LEI.pdf), web refs turn57view0, turn60view0, turn60view1; DOI 10.1063/1.4923002.

These references should support at most a short background paragraph. There is no need to pad the manuscript with a general coagulation bibliography or unrelated Becker–Döring, deterministic, or gelation results.

## Method attribution and exact placement

| Manuscript component | Citation | Concrete relationship |
|---|---|---|
| Positive-vector comparison for tridiagonal operators | **Zeifman1991**; optionally **GranovskyErlihson2009** for an accessible explicit formulation | A classical comparison principle, not a new general theorem. The manuscript's finite proof is appropriate. |
| Discrete derivative and killed birth–death operator | **ChafaiJoulin2013** | Theorem 2.1 and infinitesimal relation (2.4) give weighted-gradient intertwinings; our unweighted finite-chain identity is a special instance. |
| Harmonic decomposition over Boolean slices | **Filmus2016** | Lemma 2 gives the degree dimension; Theorem 9 and the slice discussion provide established orthogonal harmonic structure. |
| Relaxation versus total-variation mixing | **LevinPeres2017** | Standard distinctions; the present estimate alone does not identify the worst-case total-variation time. |

Chafaï–Joulin's §3.2 also states a spectral-gap lower bound via a positive weight. Source: [journal reprint](https://arxiv.org/pdf/1011.2331), web refs turn39view2, turn42view5; DOI 10.3150/12-BEJ433. Credit the general mechanism while retaining the self-contained proof of the particular reciprocal test functions.

Filmus's harmonic basis reflects earlier representation-theoretic work, including Dunkl's harmonic polynomial approach; the paper itself provides an adequate modern citation for the self-contained argument. Do not attribute the whole decomposition to this manuscript. Source: [full journal article](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i1p23/pdf/), web refs turn48view2, turn53view3; DOI 10.37236/4567.

Zeifman's article metadata and abstract were verified at the publisher; the full article was unavailable. The comparison formula used in the review is available in the inspected later paper. [Publisher](https://doi.org/10.2307/3214865), web ref turn48view0.

Levin–Peres's author page and AMS metadata verify the second edition, 2017, DOI 10.1090/mbk/107. Wilmer is a credited contributor to this edition, not listed as a third main author. [AMS](https://doi.org/10.1090/mbk/107); [author page](https://pages.uoregon.edu/dlevin/MARKOV/), web refs turn61search3, turn61search0.

## Suggested manuscript framing

A concise related-work paragraph should say that equilibrium and reversible product-form laws are classical; the exact constant-kernel family and autonomous count dynamics have been studied; and this paper proves an estimate uniform in system size and fragmentation rate. Separately credit Aldous's cycle representation and the standard spectral methods.

Recommended central claim:

> We prove a spectral-gap estimate uniform in the total mass and the fragmentation rate. In particular, the relaxation time has order \(\sqrt n\) when the fragmentation rate has order \(n^{-1}\), giving the order suggested in Aldous's notes.

Recommended description of the added proof content:

> The proof combines stationary Dirichlet-form comparison with a harmonic decomposition of the cut-set chain. Cyclic invariance removes the degree-one mode from polymer observables, which is essential when fragmentation is very rare. Explicit positive functions control the remaining one-dimensional operators uniformly across parameter ranges.

Avoid calling the cycle construction, Gibbs law, harmonic decomposition, or positive-vector principle new. The novelty assessment attaches to the full estimate and its model-specific use of symmetry and test functions.

## Search and access record

The review used both available web search systems, exact-title and model queries, original author pages and PDFs, publisher metadata, references in the closest papers, and a recent-result search through 12 October 2026. Searches covered spectral gap, relaxation, mixing, linear polymers, constant coagulation, uniform fragmentation, and the named birth–death literature.

Full texts inspected: Aldous notes; Granovsky–Erlihson preprint; Hoze–Holcman preprint; Durrett–Granovsky–Gueron; Berestycki–Pitman; Chafaï–Joulin; Filmus; D'Orsogna–Lei–Chou; and the Russian Granovsky–Zeifman follow-up. Access was incomplete for Granovsky–Zeifman (2000), Zeifman (1991), Aizenman–Bak (1979), and the relevant Kelly/Whittle book chapters. Those limits constrain priority clearance, not the self-contained proof's mathematical validity.

No retrieved source was found to imply the full all-parameter polymer theorem immediately. An expert literature check remains valuable before making a categorical priority claim.

## Final manuscript passage audit

Targeted review completed 12 October 2026. Read only paper/related_work.tex, paper/discussion.tex, and the bibliography; no further literature search was performed. This audit records the passages as initially supplied for this check. Only this review file was edited.

**Result: no substantive source or mathematical correction is required.** The material keeps the contribution appropriately narrow, credits the existing model and methods, and does not claim exhaustive priority clearance.

### Related work

- The Kelly/Whittle background and the descriptions of Durrett–Granovsky–Gueron and Berestycki–Pitman agree with the reviewed evidence. No unverified book theorem number is given.
- The Granovsky–Erlihson parameter map and the two displayed count-gap bounds are correct. The treatment of their full-gap discussion is fair: it reports their discussion and states that this manuscript supplies its own lower bound, without alleging an error or presenting equality as a newly open question.
- The Hoze–Holcman time change and fragmentation parameter are correct. **Source-location correction recommended:** “their Section 4” was verified in arXiv v1, not in the inaccessible published PDF. Replace that phrase by “their constant-kernel case,” or explicitly identify Section 4 of the preprint.
- D'Orsogna–Lei–Chou is described as treating dynamical quantities in finite systems, including a size cap. The passage appropriately avoids asserting that its exact split convention coincides with this manuscript.
- The Aizenman–Bak sentence distinguishes the kinetic equation from the finite Markov chain without denying the established deterministic convergence theorem.
- Attribution of positive-vector methods, gradient intertwining, Boolean harmonic structure, and Aldous's cut construction is appropriate. The general method citation to Granovsky–Zeifman does not assert an unread theorem or use that source to exclude prior coverage.

Two optional editorial changes improve precision without changing content:

1. Replace “The closest finite-state dynamics result is …” by “A closely related finite-state dynamics result is …”. The latter avoids an unnecessary exhaustive comparison.
2. Replace “the quantity estimated here is the Poincaré constant” by “the quantities estimated here are the spectral gap and its reciprocal.” Both quantities are bounded in the theorem, but Poincaré-constant conventions otherwise introduce an avoidable reciprocal ambiguity.

### Discussion

The displayed \(L^2\) contraction, covariance bound, and total-variation estimate follow from the finite reversible spectral theorem and Cauchy–Schwarz. The text correctly makes the initial-state prefactor explicit and does not infer a sharp worst-case total-variation time from the gap alone.

The intermediate-regime drift interpretation agrees with the displayed count rates. The rare-fragmentation stationary explanation follows from the existing stationary law: the adjacent count-weight ratio is
\[
 \frac{\pi_Q(k+1)}{\pi_Q(k)}
 =\frac{\beta n(n-k)}{k(k+1)}.
\]
It is uniformly at most \(\beta n^2/2\), so the stationary count concentrates at one when \(\beta n^2\to0\). This is an internal consequence, not an additional external-literature claim.

The \(n=2\) example has the correct polymer rates and gap \(\beta+1\). The auxiliary singleton difference indeed has eigenvalue \(-\beta\), and its conditional expectation given the polymer configuration vanishes.

The final discussion marks the fixed-parameter scale as a suggestion, makes no claim to the sharp constant, and accurately states what the proof does and does not require about count-gap equality. The extension paragraph is posed as a question and does not claim that the present symmetry argument automatically handles different kernels.


