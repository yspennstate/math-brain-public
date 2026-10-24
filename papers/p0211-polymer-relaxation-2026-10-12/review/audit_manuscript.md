# Independent mathematical audit of the polymer manuscript

Date: 12 October 2026, approximately 00:29 UTC.
Reviewer: independent collaborating agent in the current ChatGPT manuscript session.
Scope: complete analytical reading of main.tex, frontmatter.tex, introduction.tex, proof.tex, discussion.tex, appendix_coupling.tex, and acknowledgments.tex. The related-work section and bibliography were still being prepared separately. No repository, manuscript source, or external service was changed by this audit.

## Verdict

**PASS for the stated uniform spectral-gap theorem and the complete analytical derivation.** I found no mathematical gap in the proof of

\[
\frac{\beta+\sqrt\beta+n^{-1}}6\le\gamma_M(n,\beta)\le4(\beta+\sqrt\beta+n^{-1}),\qquad n\ge2,\ \beta>0.
\]

The stronger elementary estimate \(\beta+2/n\le\gamma_M\le\beta+4\max(\sqrt\beta,1/n)\) is also supported. This is a manual independent derivation check, not formal verification. No numerical suites were repeated because the remaining risks were analytical and literature-related.

**Two discussion edits should precede publication.** They concern what is presented as an open question or unresolved literature status; they do not affect the theorem. Literature priority remains subject to the separate source review.

## Publication issues

### 1. Do not present count-gap equality as an established new open question

The paragraph beginning “A second question is whether the count observable always realizes the lowest nonzero polymer eigenvalue” needs revision or removal. Granovsky and Erlihson explicitly state a spectral-gap equality with their count process in the spectral-gap paragraph of Section 2.3. Their cited Theorem 1, equation (2.43), supplies transition probabilities for initial distributions with fixed prescribed conditional laws on the count fibers; Remark 3 says other initial laws do not have that representation. The displayed representation alone therefore does not prove equality of the full-state gap. Nevertheless the paper contains an explicit prior equality assertion, so the draft should not silently advertise equality as a newly identified open question.

A safe change is to say only that the present proof does not require a full-spectrum or count-gap equality and proves its needed comparisons directly. If the earlier assertion is discussed, cite its exact setting and explain the conditional-initial-law limitation without declaring the earlier claim false.

Primary source: https://arxiv.org/html/0711.0503v3 , Theorem 1 / equation (2.43), Remark 3, and the “Spectral gap” paragraph in Section 2.3. Equation (2.49) is an asymptotic weight formula in this version, not the transition-law identity.

### 2. Qualify the claim that sharp constants remain unknown

Replace “The sharp constants remain to be determined” with “Our estimates do not determine the optimal constants” unless the separate literature review certifies the wider claim. The subsequent statements that this paper does not identify the fixed-beta asymptotic gap or the limit at beta_n ~ b/n accurately describe what its proof establishes.

## Detailed mathematical checks

### State space, factors, and stationary comparison

- The unordered transition rates distinguish unequal and equal fragments correctly. For unequal fragment sizes the two link locations produce rate 2 beta per parent cluster; equal halves have one link. Pair merging has rate 2/n per unordered pair of distinct cluster instances, including equal-size instances.
- The cut chain excludes the empty set. Its singleton death rate is zero, and the addition/deletion path through the union proves irreducibility without visiting the empty set.
- The stationary per-cut-set weight \((\beta n)^k/(k-1)!\) satisfies detailed balance because the upward weight ratio is beta n/k and the reverse rate is k/n.
- The multiplicity \(N(m)=n(k-1)!/\prod_jm_j!\) follows by distinguishing a cut and counting ordered segment lengths. It remains valid for one segment and for n singleton segments. Multiplication by the cut-state weight yields exactly the proposed polymer weight.
- Conditioning on the unordered lengths and then distinguishing a uniformly chosen cut yields uniform multiset order. The expected boundary counts \(2m_im_j/(k-1)\) and \(m_i(m_i-1)/(k-1)\), multiplied by the boundary deletion rate \((k-1)/n\), give precisely the polymer merger rates.
- At k=2, the same two segments have two distinct boundaries. Counting both gives the required factor 2/n. At n=2 the construction is a cyclic order with two distinct bonds, not a simple graph cycle; the text states this explicitly.
- Conditional generator equality at stationarity implies the bilinear identity, reversibility of the projected generator, and equality of the Dirichlet forms of lifted functions. The variance identity follows from the pushforward. The proof does not need pathwise Markov lumpability and does not assume it.
- The resulting comparison direction is correct: \(\gamma_M\ge\gamma_B\), and any Poincare inequality valid on all rotation-invariant cut functions applies to the smaller class of polymer lifts.

### Positive-vector lemma and upper bound

- The absolute-value minimizer argument and connectedness give a strictly positive bottom eigenvector for every killed radial matrix. Taking minimum and maximum ratios to a positive test vector yields the stated two-sided comparison, with the correct inequality directions. The singleton-matrix case is included.
- The count coordinate is a genuine Markov coordinate with rates beta(n-k), k(k-1)/n. Testing polymer functions that depend only on this count gives \(\gamma_M\le\gamma_Q\).
- Direct differentiation produces the stated operator with birth rate beta(n-k-1), death rate k(k-1)/n, and killing beta+2k/n. The derivative is bijective modulo constants, so its spectrum is precisely the nonzero count spectrum.
- The double-reciprocal vector gives exactly
  \(2\beta(n-k-1)/(k+a+2)+\beta+2ka/[n(k+a-1)]\).
  Its upper estimate uses only a>=1, k<=n-1, and positive denominators. Both a=n sqrt(beta) and a=1 cases are valid.
- For n=2 the count derivative is one-dimensional with eigenvalue beta+1, agreeing with the two-state polymer calculation.

### Harmonic completeness, sector action, and weights

- With counting inner products the upward/downward maps are adjoints and DU-UD=(n-2j)I on V_j.
- The norm identity proves injectivity of U below the middle layer and surjectivity of its adjoint, yielding \(\dim H_l=\binom nl-\binom n{l-1}\).
- Repeated commutation gives \(DU^ja=j(n-2l-j+1)U^{j-1}a\). The resulting norm product, divided by (j!)^2, is exactly \(\binom{n-2l}{k-l}\), with no missing factorial or layer-size factor.
- The first zero norm occurs beyond layer n-l; higher lifts vanish. Moving upward maps across inner products proves cross-degree orthogonality. The dimension sum telescopes to binomial(n,k), so no angular sectors are omitted.
- The two neighbor-sum identities give precisely the displayed radial birth, death, and killing coefficients. Vanishing lifts prevent leakage beyond either radial boundary, even though individual neighboring lifts can cancel rather than vanish separately.
- The radial weights are the stationary weight per cut set times the harmonic lift norm:
  \(\nu_l(k)=(\beta n)^k\binom{n-2l}{k-l}/(k-1)!\).
  Their adjacent ratio is \((\beta n/k)(n-k-l)/(k+1-l)\), which proves the displayed detailed balance equation.
- Degree zero uses layers 1,...,n, not layer zero. Higher sectors use l,...,n-l; one-layer middle sectors are covered by the positive-vector lemma.
- A degree-one layer function has a unique zero-sum coefficient vector. Relabeling-invariant orthogonal projections commute with rotation. Cyclic invariance fixes that vector, forcing equal entries and then zero. This correctly removes degree one only, without discarding higher degrees.
- The surviving nonconstant degree-zero gap is at least beta+2/n, while each degree l>=2 has killing at least 2 beta+2/n. Orthogonal completeness gives the claimed rotation-invariant Poincare bound and hence the polymer lower bound.

### Square-root certificate and parameter boundaries

- In the intermediate range a=n sqrt(beta) lies in [2,n/4]. The count reciprocal quotient is computed correctly. The death term is bounded in the required direction, leaving at least beta+k/n in addition to the birth term.
- At k<=a the bounds n-k-1>=n/2 and k+a+1<=5a/2 are valid. At k>=a the surviving k/n term is at least sqrt(beta).
- For the degree-l radial operator, combining death and killing gives exactly the nonnegative numerator \((k-1)((l-1)k+la)\). At k<=a, l<=k supplies n-k-l>=n/2. At k>=a, \((k-1)/(k+a-1)>=1/3\) follows from a>=2.
- Every nonconstant spectral sector is therefore covered, including degree one. The conclusion \(\gamma_B\ge\sqrt\beta/5\) does not depend on concentration or an unproved limit approximation.
- The n=8, beta=1/16, a=2 boundary satisfies all estimates. The four completion cases are exhaustive. Their respective comparisons s<=5 gamma_M, s<=1.5 gamma_M, and s<=6 gamma_M give the final universal factor 6. The n<8 case uses 1/4<=2/n, which is valid throughout n=2,...,7.

### Independent coupling appendix

- Stage I has the correct birth and death rates in both marginals. An extra deletion from the larger set moves to equal-size sets with one exclusive bond each; deletion or addition at the exclusive bond couples directly. Total exit rate is beta+2k/n, exactly the count derivative killing.
- Stage II's simultaneous exclusive additions occur at rate beta, not 2 beta. Each marginal receives its one missing exclusive bond at that rate. Simultaneous exclusive deletions occur at rate r/n, giving each marginal its required rate and avoiding the empty set when r=0.
- The internal rates beta(n-r-2) and r^2/n and the killing beta+r/n are correct. The reciprocal quotient cancels to the displayed formula. The r<=a and r>=a estimates are valid, including n=8,a=2 and r=0.
- The positive-semigroup comparison yields a uniform-over-starting-states finite prefactor for each fixed n,beta. Exponential moments at every theta<sqrt(beta)/5 compose by the strong Markov property; no unjustified uniform prefactor is needed.
- Adjacent sets connect arbitrary states through their union. The triangle inequality and a nonconstant eigenfunction comparison give every nonzero eigenvalue at least theta; letting theta increase to sqrt(beta)/5 proves the desired gap. No mixing-time/gap implication is reversed.

### Consequences and declarations

- The L2 norm, stationary covariance, and initial-state total-variation estimates follow with the stated constants. The distinction between relaxation time and sharp worst-case total-variation mixing time is preserved.
- The n=2 example is exact: polymer gap beta+1, auxiliary singleton-difference eigenvalue beta. It correctly illustrates the obstruction from the degree-one label.
- The three asymptotic regimes follow from comparing terms in s. The constants depending on fixed C or c are explicitly disclosed.
- Author, affiliation, funding, and competing-interest text agree with the current public manuscript template reviewed earlier. The AI text avoids assigning an unsupported model number to the earlier Claude review and does not claim formal or journal peer review.
- The current main.tex includes the appendix input. The first version read lacked that input, but it was already present on the final reread; no outstanding issue remains there.

## Review snapshot hashes

These are SHA-256 hashes of the files reread at approximately 00:29 UTC. Later source changes require targeted review of the changed passages.

| File | SHA-256 |
|---|---|
| main.tex | da11d3bd468b2f629cd10d75cf48de46fc922ed91ea267a688648baaf569fd7b |
| frontmatter.tex | 6a519e809e9925a2daf12816ed6b04643ada8adbc89e96922496287992a3cc9a |
| introduction.tex | 401db72db6442b8da3aca9c0b733e712a5f529279a4074746a4ac42977d9dea7 |
| proof.tex | 0f63dc532a457fd8359c2e89e6075cb1bff18b3098ed604788cc7b39473764a5 |
| discussion.tex | b694d329b2369e9e538c05c2f2f685bf97d69ff51a1ac83a7edca5eb8303c650 |
| appendix_coupling.tex | 12d397315bfe30098d089862ed2969b430da1767febc0337548dce699b17e4cb |
| acknowledgments.tex | 860826a13a0cf30b489e13b97745643f298312aaf258fc84db64f420068f995e |

This is a private review artifact. It does not certify novelty, compilation, execution of manuscript computations, or a native Math Brain status promotion.

