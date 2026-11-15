# T056 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Work began 15 November 2026, 07:45 Asia/Tbilisi (03:45 UTC); exact prompt-arrival time unavailable.

## 1. Orientation and bounded literature check

Read the startup MEMORY.md and compute_state.json. Compute state: warn, owner_away_open, CPU saturated. All local reads after pwd used OMP_NUM_THREADS=1 nice -n 15. The sandbox prints `nice: setpriority: Operation not permitted`; reads finish immediately. No numerical workload will be launched without established priority. No subagents, git commands, or background processes. The task-specific prohibition on writes outside this folder takes precedence over global mesh, checklist and brain-writing requests, including recall commands that log externally. Those routines were not run. The mesh protocol was read only.

Inventoried all three earlier folders with ls -la. Read their REPORT.md and LOG.md files, round 3 and round 4 PROOF.md, and the first session's SOLVED_ELSEWHERE.md. The first session has no PROOF.md; none of the three has mathematical scripts. Earlier files remain untouched.

Web searches began at 03:45 UTC and were closed within five minutes. Queries: `"fixed price" group Gaboriau 2026 counterexample`; `"A group without fixed price" OpenAI October 2026`; `Gaboriau fixed price November 2026 solution arxiv` with secondary-domain exclusions. Results identify the same October manuscript as earlier sessions; no later established general resolution was located. A bounded search does not establish exhaustive absence. No new SOLVED_ELSEWHERE.md is warranted.

Primary texts opened using the web tool: OpenAI, *A group without fixed price*, 5 October 2026, build/paper.tex and build/finite-models.tex; also build/rank-surgery.tex and build/planar.tex to locate the following dependency. Base URL: https://raw.githubusercontent.com/openai/math/main/preprints/A-group-without-fixed-price-October-5-2026/ . The title page gives author OpenAI and the date. No arXiv identifier verified. Also opened https://arxiv.org/abs/2509.08325v4 to check the previously reported Ali Khezeli metadata. No new general solution is inferred from the product theorem. A guessed parameters.tex path was unavailable; no claim depends on it.

## 2. Independent recheck of round 4

Reconstructed the transfer argument through a single counting function, rather than separately estimating each event. For fixed selected path types and cylinder domains define W(xi)=sum_l 1_{L'_l}(xi)+1_{(P')^c}(xi), with r paid indices. Exact equivariance xi_{vq}=xi_v q and the inverse identity theta(v,g^-1)=theta(vg^-1,g)^-1 show that every labeling supplies a generating list of length sum_v W(xi_v). Thus rank(D_V)/n <= n^-1 sum_v E W(xi_v). At sources injective on the common coordinate support F, E W equals its product integral H; at the other beta*n sources it is at most r+1. Hence rank/n <= (1-beta)H+beta(r+1). The product integral is at most C(E)+p+sum_l(1+m_l)Delta_l. Dropping the nonpositive term -beta H gives precisely round 4's finite inequality.

The source of an inverse paid step is independently obtained by solving y g=vh: y=vhg^-1. Its list factor is theta(y,g)^-1, so no stabilizer ambiguity changes the formal label. Coordinate collision vg=vh is equivalent to vgh^-1=v, with gh^-1 nonidentity for distinct group coordinates. For fixed F the exceptional fraction vanishes. First fixing paths and cylinders, then taking limsup in model size, then approximation error to zero, and finally the graphing infimum gives d_X >= limsup rank(D_V)/n. The earlier result holds. No mathematical script exists to rerun.

## 3. Choice of one extension, before carrying it out

Audit Proposition models:sequence, exactly the next dependency named by round 4: construct finite exact A-actions that are simultaneously asymptotically free, expand every row set of size at most alpha*n by a factor strictly greater than 96, and have o(n) bad rows. Prove the basis substitution, the expansion union bound including small sets, the reduced-word exposure estimate including inverses, and the nonidentity overlap certificates. These properties are needed to apply the later deterministic rank theorem to the same sequence as transfer. The rank/planar theorem is outside this session's chosen piece.

Intended extension beyond the qualitative statement: give an explicit probability bound for obtaining all three properties for a finite list of words at one finite n. In particular use overlap certificates of length at most four in the random basis to obtain an explicit uniform bound on the expected number of bad rows. All steps will be proved symbolically; no numerical experiment is required.

## 4. Quantitative model estimate derived

The basis inverse b_i=a^-1 u_{i-1}^-1 u_i works in both directions. Counting a violating s-row set together with a containing 96s-column set gives the bound t_s=[K(s/n)^3]^s. Independent check of the exponent: 99 independent images supply 99s powers of s/n; choosing T and the 95s additional columns removes 96s powers, leaving 3s. The exponential constant is e^(1+95)*96^99/95^95=K.

A stronger summation than the source's split-limit argument is available. With q=K alpha^3<1/2, t_s <= (K/n^3)*s^3*q^(s-1). Consequently the probability of any expansion failure is at most K(1+4q+q^2)/[n^3(1-q)^4] <= 52K/n^3. This is a new explicit rate for this audit. The series identity was re-derived by differentiating sum s^2 q^s and by decomposing s^3 into falling factorials. At q=1/2 the three falling-factorial contributions are 24, 24 and 4, independently confirming 52.

For a freely reduced nonidentity word of length L, exposure before the first repeated path vertex gives f_n(L)=L(L+1)/[2(n-L+1)] as an upper bound on its expected fixed-point fraction, for n>=L. Positive and negative next steps are both unexposed unless they immediately reverse the incoming edge, excluded by free reduction. Closure forces a repeat. No independence between starting vertices is used.

An overlap of rows v and y gives v fixed by u_i u_k^-1 u_l u_j^-1, with i!=j, k!=l, i!=k, j!=l. The map (i,k) -> u_i u_k^-1 is injective on i!=k, including u_0=1, so this certificate is nonidentity. Repeated columns have certificates u_i u_j^-1. There are at most Q=100*99+100^4 certificates, each of reduced length at most four. Therefore E b(V) <= 10Q*n/(n-3) for n>=4. Markov plus union bounds will combine this with the expansion rate and any finite word list.

## 5. Proof saved and adversarial checks

Saved PROOF.md with the full basis argument, finite-size expansion bound, deferred-exposure argument, overlap certificates, combined failure probability and diagonal choice. The combined probability bound is 52K/n^3 + epsilon^-1 sum_j f_n(L_j) + 10Q/[eta(n-3)]. Conditions (17) make its three terms each less than 1/4. Independently checked these sufficient sizes using n>=2L_*: f_n(L_j)<=L_j(L_j+1)/n, 52K/n^3<1/4 when n^3>208K, and the last term is <1/4 when n>3+40Q/eta.

Tried the cases most likely to invalidate the proof: identity column u_0; one and two zero indices in overlaps; two opposite zeros leaving a square; shared columns in rows that themselves have repetitions; inverse permutation queries; repeated generator letters and powers; reduced words not cyclically reduced; singleton row sets; empty size range when alpha*n<1; nontransitive actions; word lengths growing along the diagonal. None invalidates the estimates. In contrast, allowing freely trivial words would invalidate the exposure estimate, and allowing equal rows in the overlap test would admit identity certificates. Both are explicitly excluded. No vertices or rows are deleted, so all three properties belong to the same exact action.

Second checks: overlap nonidentity follows both from uniqueness of reduced two-letter forms and from checking cyclic adjacent indices and zero positions. The bad-row expectation follows both by summing fixed-set expectations and by summing witness probabilities at each vertex. Its constant 10 is 1+2+3+4, also 4*5/2; denominator n-3 is the smallest of n-L+1 for 1<=L<=4. The fixed-word estimate is checked separately by replacing every denominator with n-L+1 and summing the visited-target counts. Length one agrees exactly with the uniform-permutation fixed-point probability 1/n.

No proof attempt failed. The coarse Q overcounts certificates and could be sharpened, but this affects no asymptotic claim. This proof certifies neither the deterministic group-rank theorem nor its planar lemma, and therefore gives no positive cost gap. It establishes the precise finite-model dependency named by round 4, with stronger quantitative estimates.

## 6. Final readback

Commands:

```
OMP_NUM_THREADS=1 nice -n 15 /usr/bin/wc -l LOG.md PROOF.md REPORT.md
OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md
OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md
OMP_NUM_THREADS=1 nice -n 15 cat LOG.md
OMP_NUM_THREADS=1 nice -n 15 rg -n 'VERDICT|\\tag|52|208|40Q|Next worker|Task:' REPORT.md PROOF.md LOG.md
```

All exited zero; each printed the nice permission warning. Initial final-read counts were LOG.md 45, PROOF.md 306, REPORT.md 30, before this log entry and the final power check. Readback confirmed all seventeen numbered equations, the required verdict line, source attribution, the probability directions and every denominator. Clarified that the 99 image-containment events are independent for fixed T,C. Added a separate exact power check: for g=u_1^2, fixed-point probability is 2/n for n>=2, from one- and two-cycles; the exposure estimate gives 3/(n-1), safely above it. Thus a tempting universal 1/n estimate would be wrong, while the bound used here handles powers.

No mathematical script or numerical program was run. The deliverables are LOG.md, PROOF.md and REPORT.md in this folder. Next checkable dependency remains the deterministic rank theorem with its coefficient-sensitive planar lemma.
