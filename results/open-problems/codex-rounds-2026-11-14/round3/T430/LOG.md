# T430 work log

Task received: 15 November 2026, approximately 03:54 Asia/Tbilisi (14 November 23:54 UTC).

## 1. Orientation and prior files

Read the earlier REPORT.md, LOG.md and complete PROOF.md in ~/codex_op_1114/briefs/T430. Its directory has no computation scripts; the result is symbolic. Read the startup memory index and compute state. Compute state reports warn, owner_away_open, cpu_saturated, 66 percent memory free. No heavy computation is planned.

The specific instruction to write only in this folder takes precedence over global mesh/checklist/brain logging: those tools mutate files elsewhere and were not run. No git, subagents or external writes are used. Shell reads use OMP_NUM_THREADS=1 nice -n 15. The shell reports `nice: setpriority: Operation not permitted`; only short reads have run, and no numerical program will be used unless priority can be certified.

Literature search started at approximately 23:54 UTC, with a five-minute maximum. Initial queries: supermarket/general-service/stationary/2026; arXiv:1809.05373 stationary convergence error; supermarket/asymptotic independence/2025. Opened arXiv:1809.05373 PDF and abstract page. Further results and the independent recheck follow below.

## 2. Independent recheck of the earlier result

Re-derived the main obstruction using a second-moment calculation, without invoking conditional variance. Let B be the fair initial bit, p=P(Q_1(t)=0 | B=0), and v=Var(M(t) | B=0). For t<1, M(t)=0 on B=1. Hence E M=p/2 and E M^2=(v+p^2)/2, giving Var(M)=v/2+p^2/4. The no-sampling event has probability at least exp(-lambda*d*t), so the earlier exp(-2*lambda*d*t)/4 lower bound holds. This also verifies the exact coefficient 1/4 independently.

For the separate covariance constant, write q=P(Q_1(t)=Q_2(t)=0 | B=0). Then Cov(I_1,I_2)=q/2-p^2/4. The rate at which either server is sampled is at most 2*lambda*d, so q>=exp(-2*lambda*d*t). At t*=min(1/2,1/(8*lambda*d)), exp(-2*lambda*d*t*)>=3/4, giving covariance >=1/8. This covers replacement and nonreplacement sampling and N=d. The example remains transient. The earlier result holds; no correction is needed.

Also rechecked the stationary reduction by expanding E[(M-E M)^2] after subtracting H(X(0)): the cross term vanishes conditionally. The product-test estimate has collision probability at most k(k-1)/(2N), as stated. No scripts were available or needed.

## 3. Literature check and chosen extension, 23:55 UTC

Completed the search in under five minutes. Additional queries covered FIFO supermarket stationary general-service 2025/2026, the stationary ansatz, and arXiv:1809.05373 corrections/publication. No verified later resolution was found. Opened the PDF and abstract of Maria Clara Fittipaldi, Matthieu Jonckheere, Sergio I. Lopez, *Convergence properties of many parallel servers under power-of-D load balancing*, arXiv:1809.05373; the retrieved PDF has internal date 13 November 2021. Also opened Pooja Agarwal and Kavita Ramanan, *Invariant states of hydrodynamic limits of randomized load balancing networks*, arXiv:2008.08510, especially Section 4.2; and Reza Aghajani and Kavita Ramanan, *The hydrodynamic limit of a randomized load balancing network*, arXiv:1707.02005. The latter two still distinguish invariant-state/transient results from stationary-limit identification in the retrieved versions. This short search cannot establish that no solution exists. No SOLVED_ELSEWHERE.md is warranted.

**Choice, before proof work:** audit the arrival-rate monotonicity lemma used by the proposed stationary argument in arXiv:1809.05373. Lemma 3.3 states eventual nondecrease in N uniformly over configurations; the proof of Theorem 3.2 uses it, and Section 4 uses preceding convergence results. Derive the exact tagged arrival rate for a unique queue of length one surrounded by queues of lengths zero and two, then compare prefixes of a single infinite configuration. This is a concrete check of the previous report's recommended audit, rather than another abstract stationarity criterion.

PDF screenshot attempts for printed pages 11 and 19 failed with cache misses; extracted PDF text is available and has been read. The next proof will be derived directly from routing probabilities, so it does not depend on interpretation of extracted algebra.

## 4. Hypothesis audit and refined witness

Before writing the proof, checked the paragraph immediately after (3.1). It assumes both the number of queues exactly at the tagged length and the number at least that length are at least D. Therefore the unique-length-one candidate alone would not refute the lemma on its stated domain. Replaced it with the fixed periodic configuration x=(1,2,0,1,2,0,...). For N=3m+2, the counts at length one and strictly above one both equal m+1; these exceed every fixed D for sufficiently large m. The next coordinate is zero. This also has a convergent empirical distribution with all three masses equal to 1/3, avoiding a vanishing-density loophole.

The key calculation is more general: appending any queue shorter than the tagged queue multiplies the tagged arrival rate by (N+1-D)/N, since every sample containing the new queue excludes routing to the tag, and all old favorable samples retain their routing probabilities. Thus every positive rate strictly decreases. For the periodic configuration this happens infinitely often. Appendix A.2 treats new lengths greater than or equal to the tag but omits the shorter case. The proof below will retain the standing count assumptions and use no service-time simplification as a Markov assumption.

## 5. Proof saved and independent checks

Created PROOF.md with the exact append-shorter identity and the fixed periodic witness. The lower rate is not a finite-N anomaly: for every fixed d>=2 there are infinitely many decreasing pairs N=3m+2, N+1, all satisfying the source's count assumptions. The witness has convergent empirical measure with positive masses at lengths zero, one and two. Its tagged rates also converge, so no invalid implication from nonmonotonicity to nonconvergence is made.

Independent derivations and checks:

- Subset counting gives the rate factor ((N+1)/N)*C(N,d)/C(N+1,d)=(N+1-d)/N. Poisson thinning of arrivals excluding the new queue gives the same factor from rates lambda*(N+1-d) and lambda*N.
- For d=2, pair enumeration gives a_N=lambda*(2h+e-1)/(N-1); conditioning on tag inclusion, with probability 2/N, gives the same expression. At N=5, e=h=2: the routing weights sum to 5/2, the per-pair arrival rate is lambda/2, hence a_5=5lambda/4. At N=6 those weights remain 5/2 and the per-pair rate is 2lambda/5, hence a_6=lambda. The drop lambda/4 agrees with (d-1)*a_5/5.
- For N=3m+2, d=2, the drop is lambda/(3m+1). Recomputed from the general identity: a_N/N=lambda/(N-1), exactly the same value.
- The general fixed-d limit is 3lambda*((2/3)^d-(1/3)^d). At d=2 it equals lambda, agreeing with the exact two-choice formulas. This limit is positive and <=lambda*d, consistent with the tag-sampling rate bound.
- Checked the edge N=d: the factor in (1) is 1/d, still positive. For d=1 it would be one, explaining why strict decrease requires d>=2. If the old rate is zero, the new rate stays zero. The proof claims strictness only for positive old rate.
- The state can be completed with age/residual/waiting requirements for deterministic services, so the routing counterexample is compatible with full FIFO states. It is not stationary, and does not disprove stationary chaos.
- Source-specific domain audit: e>=d, e+h>=d, and even h>=d hold throughout the witness's sufficiently large prefixes. No low-count exception repairs the monotonicity claim. The proof uses one fixed infinite configuration, not a separately chosen state at each N.

No numerical computation or script was needed. The proof is independently checkable using exact routing probabilities. The temporary unique-length candidate was rejected on the source's hypotheses before proof writing; it is not used in the result.

## 6. Report and final audit

Saved REPORT.md with the required PARTIAL verdict. It states the earlier result holds, identifies the new false-lemma counterexample, distinguishes it from a stationary counterexample, and leaves a concrete continuation target. No SOLVED_ELSEWHERE.md was created.

Final read-only command:

```sh
OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c 'head -1 REPORT.md; wc -l LOG.md PROOF.md REPORT.md; rg --files . ~/codex_op_1114/briefs/T430 -g "*.py" -g "*.sh" -g "*.jl" -g "*.R"; tail -8 PROOF.md'
```

Output confirmed `VERDICT: PARTIAL explicit counterexample to the arrival-rate monotonicity lemma supporting a claimed stationary result`, 152 proof lines and 25 report lines, and no scripts in either brief directory. The same nice warning appeared. The proof's final paragraph explicitly leaves the original stationary full-state assertion unresolved. This final entry increases only the log length.

Final algebra audit: the favorable-subset numerator is unchanged by appending a shorter queue, including all tie weights; only the arrival-rate/sampling denominator changes. The periodic witness satisfies the count restrictions for all large prefixes, not just the selected decreasing pairs. Formula (11) follows from symmetry within a fixed queue-length class and concerns routing only. No Markov property for queue lengths, random-initial uniformity, or interchange of stationary and large-N limits has been assumed.

Task: “Open problem T430: Asymptotic independence in the supermarket model with general service times”; received 15 November 2026, approximately 03:54 Asia/Tbilisi (14 November 23:54 UTC).
