VERDICT: PASS

Independent audit of D0056, 2026-10-11.

The result is a correct counterexample to the survival assertion under the stated hypotheses. It is not a proof of the asserted asymptotic. No mathematical gap requiring a fix was found in ATTEMPT.md. The proof uses a published critical generating-function product theorem as an external input; I independently fetched and checked that theorem and its applicability.

## Exact claim and scope

ATTEMPT.md lines 7–18 state the deterministic integer m-ary recursion, the critical weighted first-moment condition, and the proposed universal survival asymptotic. Lines 35–64 construct a nonconstant law for m=2:

    A = sum_{k>=2} 2^{-k} k^{-3},
    B = sum_{k>=2} (k-1) k^{-3},
    c = (A+B)^{-1},
    p_0 = c B, p_1 = 0, p_k = c 2^{-k} k^{-3} (k>=2).

The claim proved is that this law satisfies E[X_0 2^{X_0}]=E[2^{X_0}]<infinity but does not satisfy P(X_n>0)~4/n^2. Since the problem's assertion is universal over the allowed m and initial laws, one admissible binary counterexample is sufficient. This is not a special-case positive theorem substituted for the universal assertion.

I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl, and LITERATURE.md from the claimant's directory without modifying them. CLAIMS.jsonl correctly separates the counterexample from the conjectural alternative coefficient 3/2.

## Source and external theorem checks

I independently downloaded https://arxiv.org/pdf/1705.04787, https://arxiv.org/pdf/2006.06140, and https://arxiv.org/pdf/2108.05610 using Python urllib. The PDFs and extracted text are retained in this audit directory. Download results and URLs are recorded in fetch_log.json.

1. The original source, arXiv:1705.04787v2, PDF page 3, states precisely Conjecture 1 with coefficient 4/(m-1)^2 and condition (4). PDF page 1 assumes X_0 is not almost surely constant. PDF page 4 explicitly warns that additional integrability, such as E[X_0^3 m^{X_0}]<infinity, may be necessary. These source qualifications in ATTEMPT.md line 16 are accurate.

2. Chen–Shi, arXiv:2006.06140v1, PDF page 3, Theorem 1.1, states that for a critical system with P(Y_0=k)~c_0 m^{-k}k^{-alpha}, 2<alpha<4 and c_0>0, the product over i=0,...,n-1 of E[m^{Y_i}]^{m-1} lies between positive constant multiples of n^{alpha-2}. PDF pages 1–2 impose P(Y_0>=2)>0 and finite E[Y_0 m^{Y_0}]. PDF page 4 explicitly discusses inclusion of alpha=3 in their unified proof. The cited statement in ATTEMPT.md lines 22–31 is correct; no endpoint exclusion or stronger third-moment assumption invalidates its use.

3. I checked the upper-bound argument on PDF pages 20–21. Its truncated weighted third moment, for the proposed law, is exactly

       E[X_0^3 2^{X_0} 1_{2<=X_0<=3n}] = c(3n-1).

   Thus the critical product bound is O(n). The auxiliary estimates used there have the correct direction: with u=k(1-x), x^k<=exp(-u) gives 1-(k+1)x^k+kx^{k+1}>=1-(1+u)exp(-u); the latter has a positive constant lower bound times min(u^2,1). At s=m(1-1/(3n)), the prefactor (m/(2s-m))^n=(1-2/(3n))^{-n} is uniformly bounded (at most 3 by Bernoulli's inequality). This confirms the upper-bound specialization claimed at lines 31 and 137. I treat the published critical theorem, including its earlier referenced product estimate, as an established mathematical input; I have not independently reconstructed the entire external paper.

## Independent verification of the proof

### Law, normalization, and criticality: lines 37–64

A and B are positive finite series. Consequently all masses are nonnegative and their sum is c(A+B)=1. Both p_0 and p_2 are positive, so the law meets the source's nonconstant assumption and the external theorem's positive-mass-above-one assumption.

Directly summing gives

    E[2^{X_0}] = c(B + sum_{k>=2} k^{-3})
                 = c sum_{k>=2} k^{-2}
                 = E[X_0 2^{X_0}] < infinity.

Its tail has the required asymptotic with m=2, alpha=3, and c_0=c>0. Thus Q_n=product_{i=0}^{n-1}E[2^{X_i}]<=Cn, as stated at line 58. The weighted third moment is c sum_{k>=2}1=infinity. Every interchange here involves nonnegative or absolutely convergent series; no cancellation of divergent sums is present.

As supplementary checks, independent_checks.py verifies normalization and the critical identity exactly for 29 finite truncations, each separately normalized by the corresponding finite A and B. Those truncated laws are algebra checks, not substitutes for the infinite-tail example. Floating-point series calculations give A approximately 0.0372131936080402 and c approximately 2.08294. The infinite-law justification is the exact series argument above, not these numerical approximations.

### Exact recursion and moment finiteness: lines 68–79

For S=X_n^(1)+X_n^(2), the contribution at S=0 is 1 rather than 1/2. Independence therefore gives G_{n+1}(2)=G_n(2)^2/2+(1-q_n)^2/2. Subtracting 1 and writing e_n=G_n(2)-1 yields exactly

    e_{n+1}=e_n+e_n^2/2-q_n+q_n^2/2.

All quantities are finite: 2^{(x+y-1)^+}<=2^{x+y}, followed by independence, propagates finite G_n(2) inductively. Nonnegativity e_n>=0 follows from X_n>=0. I independently verified the generating-function identity by direct convolution for all 255 nonzero four-entry weight vectors in {0,1,2,3}^4, using Fraction arithmetic. This checks the formula on actual probability laws rather than only checking a rearranged polynomial.

### Persistent barrier: lines 83–106

Assuming q_n~4/n^2 gives n^2(q_n-q_n^2/2)->4, hence q_n-q_n^2/2>=3/n^2 eventually. Below b_n=3/(2n), the recursion gives

    e_{n+1}<=e_n-15/(8n^2).

Since b_n-b_{n+1}=3/(2n(n+1))<=3/(2n^2), the gap d_n=e_n-b_n satisfies d_{n+1}<=d_n-3/(8n^2) whenever d_n<=0. This condition persists. If d_j<=0 even once beyond the threshold, d_{j+1}<=-3/(8j^2), and all later gaps remain at most this fixed negative number. As b_k->0, e_k eventually becomes negative, a contradiction.

This proves e_n>3/(2n) eventually. The summability of 1/n^2 does not defeat the argument: one strictly negative gap already persists while the positive barrier vanishes. Nor does the proof assume asymptotic differentiability, monotonicity of e_n, or an unproved e_n~2/n limit.

I tested the one-step gap inequality in 92,694 independent exact rational cases: n=2,...,150, e on 21 points of [0,b_n], and q on 31 points of [0,1], retaining only cases with q-q^2/2>=3/n^2. Every retained case passed. The infinite-sequence argument was checked analytically as above; a finite grid alone would not prove it.

### Product contradiction: lines 110–125

Every omitted early factor is at least 1, so eventual e_i>3/(2i) yields log Q_n>=sum_{i=N}^{n-1}log(1+3/(2i)). The inequality log(1+x)>=x-x^2/2 for x>=0 follows independently by differentiating its difference: the derivative is x^2/(1+x)>=0 and the difference vanishes at zero. Integrating 1/x on [i,i+1] gives sum_{i=N}^{n-1}1/i>=log(n/N); the reciprocal-square sum is finite. Hence

    log Q_n >= (3/2)log(n/N) - (9/8)sum_{i=N}^infinity i^{-2},
    Q_n >= K n^{3/2}

for a fixed K>0. This contradicts Q_n<=Cn for arbitrarily large n. The product indices match the theorem, and both constants are independent of n. Therefore the proposed survival asymptotic is false for this law.

## Issues and limits of the claim

No failing step or required repair was found. The following qualifications matter but are already handled correctly in the attempt:

- ATTEMPT.md lines 16–18: the supplied problem transcription omits the original source's nonconstant assumption. The deterministic binary law X_0=1 would defeat that transcription trivially, but the submitted counterexample is nonconstant and does not rely on the omission.
- ATTEMPT.md lines 60–64 and 143: the counterexample has infinite weighted third moment. It does not refute the conjecture after adding E[X_0^3 m^{X_0}]<infinity. Calling that stronger version solved would exceed the proof; the claimant does not do so.
- ATTEMPT.md lines 138–139 and 147: the claimant's reported Lean checks concern algebra only. I did not rerun Lean or certify the claimant's historical execution record. My independently derived recurrence, rational checks, and analytical sequence argument establish the needed steps without that record. There is no claim here of a fully formalized counterexample or external theorem.
- ATTEMPT.md line 143: neither the existence of a limit n^2 P(X_n>0) nor its value 3/2 is established. Only failure of the asserted equivalent with coefficient 4 is proved. This distinction is correctly maintained in CLAIMS.jsonl.

## Fresh bounded literature search

I queried the arXiv API for all:"Derrida" AND all:"Retaux", requesting up to 60 results sorted by submission date. The successful XML response is retained as arxiv_search.xml. I also queried OpenAlex for Derrida Retaux; it returned HTTP 429, recorded in fetch_log.json, so it supplies no independent literature evidence.

The arXiv results include the 2026 Brownian-CRT continuous process paper, recent geometric/random-offspring models, the dual conjecture, free-energy results, and the critical sustainability paper. Their abstracts do not assert the exact universal survival conclusion for this deterministic discrete recursion under the problem's weighted first-moment hypothesis. Results about continuous time, geometric offspring, free energy, or nearly subcritical behavior cannot be substituted for the assertion here.

I checked arXiv:2108.05610v1 in full at its relevant introductory statements. PDF page 3, Theorem 1.2, assumes E[t^{Y_0}]<infinity for some t>m and proves n^{-2+o(1)}, not an asymptotic equivalent with the sharp coefficient. PDF page 4 explicitly says the universal coefficient should require finite E[Y_0^3 m^{Y_0}], and presents alpha(alpha-2)/2 for binary stable tails as an expectation, not a theorem. This earlier recognition of different heavy-tail behavior is consistent with the counterexample. No novelty claim is warranted or needed.

The bounded search did not identify a paper stating this exact counterexample argument as a theorem. It also does not certify that the stronger-moment question remains globally open. Neither uncertainty affects the independently checked refutation of the problem as stated.

## Conclusion

The nonconstant critical binary law is admissible, the cited product upper bound applies, and the survival assumption produces a rigorously incompatible lower bound. PASS is for this complete refutation of the stated universal assertion, not for proving the asserted survival formula or any alternative sharp asymptotic.
