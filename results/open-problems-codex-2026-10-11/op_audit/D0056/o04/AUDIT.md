VERDICT: PASS

# Independent audit of D0056

The claimant correctly disproves the proposed universal implication under the stated moment hypothesis. The result is a nonconstant critical binary counterexample, not a proof of the proposed survival asymptotic. I found no failing step or necessary mathematical repair in ATTEMPT.md Sections 1–6. Acceptance uses Chen–Shi's published product theorem as a standard external theorem; that theorem was fetched and its applicability checked independently.

## Exact claim and scope

The recursion is X_{n+1}=(X_n^(1)+...+X_n^(m)-1)^+, with m independent copies and integer m>=2. The question asserts that every nonnegative integer initial law satisfying (m-1)E[X_0 m^{X_0}]=E[m^{X_0}]<infinity has P(X_n>0) asymptotic to 4/((m-1)^2 n^2).

ATTEMPT.md Section 3 instead supplies m=2 and

    A=sum_{k>=2} 2^{-k}k^{-3},
    B=sum_{k>=2} (k-1)k^{-3}, c=1/(A+B),
    p_0=cB, p_1=0, p_k=c 2^{-k}k^{-3} for k>=2.

Sections 4–6 prove that this law cannot have P(X_n>0)~4/n^2. One binary counterexample is sufficient to refute the universally quantified statement. This is not a special positive result misrepresented as the full assertion.

I fetched the source https://arxiv.org/pdf/1705.04787 independently. PDF page 3, condition (4) and Conjecture 1, agree with the supplied question. Page 1 additionally excludes almost surely constant initial laws. The constructed law has p_0,p_2>0 and respects this exclusion. The elementary constant-law observation in Section 1 is explicitly distinguished from the actual counterexample. Page 4 warns that additional integrability, such as E[X_0^3 m^{X_0}]<infinity, might be necessary. That stronger condition is not part of the stated conjecture.

## Step-by-step mathematical checks

**ATTEMPT.md Section 3: normalization, moments, criticality.** A and B are finite positive series, so c>0 and sum p_k=c(A+B)=1. Directly,

    E[2^{X_0}]=cB+c sum_{k>=2} k^{-3},
    E[X_0 2^{X_0}]=c sum_{k>=2} k^{-2}.

The identity B=sum_{k>=2}(k^{-2}-k^{-3}) proves equality, with both moments finite. No conditional convergence or numerical tuning is involved. The weighted third moment is c sum_{k>=2}1=infinity. The exact tail has exponent alpha=3 and positive coefficient c.

Independent 60-digit computation gives c approximately 2.082941231377511, p_0 approximately 0.922487104682579, p_2 approximately 0.065091913480547, and both critical moments approximately 1.343359759358151. These calculations supplement the exact positive-series proof.

**ATTEMPT.md Section 2 and equation (1): imported product bound.** I independently downloaded https://arxiv.org/pdf/2006.06140. Chen and Shi, *The stable Derrida–Retaux system at criticality*, Theorem 1.1, PDF page 3, states that a critical law with P(Y_0=k)~c_0 m^{-k}k^{-alpha}, 2<alpha<4, has

    c_1 n^{alpha-2} <= product_{i=0}^{n-1} E[m^{Y_i}]^{m-1}
                           <= c_2 n^{alpha-2}.

Page 1 requires P(Y_0>=2)>0 throughout; page 2 requires finite E[Y_0 m^{Y_0}] and defines exactly the deterministic m-copy recursion in this audit. Every requirement holds here. PDF page 4 explicitly discusses the inclusion of alpha=3, so there is no missing endpoint or exceptional case. For m=2, alpha=3, this gives Q_n=product_{i=0}^{n-1}E[2^{X_i}]<=Cn, with precisely the indices used in the attempt.

I also inspected PDF pages 20–21: Lemma 5.1 and its application prove the needed upper bound through a truncated third weighted moment. For this law that moment is exactly

    E[X_0^3 2^{X_0} 1_{2<=X_0<=3n}]=c(3n-1).

Thus the displayed lemma bound is a constant times n^2/[c(3n-1)]=O(n). The lower half of Theorem 1.1 is unnecessary. I have not independently rebuilt the entire published theorem and its cited prerequisites; reliance on that established external input is stated explicitly, not hidden.

**ATTEMPT.md Section 4, equation (2): scalar identity.** Exponential moments remain finite because 2^{(x+y-1)^+}<=2^{x+y}. For S=X_n^(1)+X_n^(2), separate S=0 from S>=1 to obtain

    G_{n+1}(2)=[G_n(2)^2+(1-q_n)^2]/2.

Putting e_n=G_n(2)-1 gives exactly

    e_{n+1}=e_n+e_n^2/2-q_n+q_n^2/2.

I rederived this without using the claimant's scripts. Independent convolution checks on four rational finite-support laws, including a law supported at 1, also verify it exactly. Criticality is not needed for this identity, and e_n>=0 follows from X_n>=0.

**ATTEMPT.md Section 5, equations (3)–(4): barrier.** Under the assumed q_n~4/n^2, n^2(q_n-q_n^2/2) tends to 4. Therefore it eventually exceeds 3. With b_n=3/(2n), if 0<=e_n<=b_n, the exact recurrence implies

    e_{n+1}<=e_n-15/(8n^2).

Since b_n-b_{n+1}=3/[2n(n+1)]<=3/(2n^2), the gap d_n=e_n-b_n satisfies

    d_{n+1}<=d_n-3/(8n^2).

The estimate is applied in the correct direction, below the barrier. If d_j<=0 at any sufficiently late j, it implies d_{j+1}<=-3/(8j^2)<0 and preserves this fixed negative upper bound at every subsequent time. As b_k tends to zero, e_k=b_k+d_k would become negative. This contradicts e_k>=0 and proves the asserted eventual lower bound. Summability of the decrements is harmless: a single strict decrement already supplies a persistent fixed negative gap. There is no differentiation of an asymptotic equivalent or unjustified subtraction of leading terms.

The independent script tests this one-step inequality exactly for 149 integer values n=2,...,150 and 101 rational positions between zero and the barrier at each n. Combined with the four convolution identities, all 15,053 checks pass. The infinite-sequence contradiction above, rather than these finite tests, establishes the lemma.

**ATTEMPT.md Section 6, equation (5): product contradiction.** Omitting the finitely many early factors is valid because G_i(2)>=1. The inequality log(1+x)>=x-x^2/2 for x>=0 follows by integrating 1/(1+t)>=1-t; the difference is t^2/(1+t)>=0. Consequently,

    log Q_n >= (3/2)sum_{i=N}^{n-1}1/i
                   -(9/8)sum_{i=N}^{n-1}1/i^2
             >= (3/2)log(n/N)-finite_constant.

The harmonic bound has the correct endpoints, and the reciprocal-square sum converges. Exponentiating yields Q_n>=Kn^{3/2}, K>0, contradicting Q_n<=Cn. This contradiction proves that the proposed survival equivalent fails for the explicit law.

## Issues and limits

No substantive issue was found at any of the proof locations above. No proof fix is required.

ATTEMPT.md Section 8 correctly leaves the actual survival asymptotic unproved. In particular, the coefficient 3/2 for this alpha=3 law is a conjecture, not a consequence established by this proof. The argument does not establish that n^2 P(X_n>0) converges, nor that its limit exists and differs from 4. It establishes precisely the failure of the proposed equivalent.

The strengthened finite-third-weighted-moment conjecture is neither proved nor refuted here. The claimant's Lean and earlier numerical verification records in Section 7 and the final verification record were not independently rerun; this verdict rests on the mathematical derivations, freshly fetched theorem, and separate checks above. Those records are not needed for completeness.

## Independent literature search

I fetched the three PDFs retained here as source.pdf, stable.pdf, and survival.pdf, and ran a fresh arXiv API topic query, retained as arxiv_search.xml. I also attempted an OpenAlex topic query; it returned HTTP 429. URLs, download sizes, and that failure are recorded in fetch_log.json. No built-in web search was used.

The fresh arXiv query returned relevant papers through arXiv:2609.11435. The newer abstracts concern a continuous branching process, geometric Galton–Watson offspring, generalized recursions, free energy, or subcritical behavior. These abstracts do not supply a theorem proving the sharp survival assertion for the deterministic m-ary recursion under the original moment condition. This bounded search is not an exhaustive novelty or current-status certificate.

I independently read Chen–Hu–Shi, *The sustainability probability for the critical Derrida–Retaux model*, https://arxiv.org/pdf/2108.05610, PDF pages 3–4. Theorem 1.2 requires E[t^{Y_0}]<infinity for some t>m and proves only n^{-2+o(1)}. Page 4 explicitly says the universal coefficient is expected only under finite E[Y_0^3 m^{Y_0}], and labels the heavy-tail alpha(alpha-2)/2 coefficient as an expectation. This supports the scope distinction; it does not prove that coefficient. I did not find a fetched paper that already states the exact counterexample implication established in ATTEMPT.md, and make no claim of novelty.

Independent check code and results are retained as independent_checks.py and independent_checks.txt. All audit writes and downloaded artifacts are confined to the assigned audit folder; the claimant's four requested files were read only.
