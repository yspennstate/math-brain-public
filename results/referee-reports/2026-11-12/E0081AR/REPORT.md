MINOR

The order theorem survives this audit. I found no fatal error in Lemmas 2–6 or in the deduction that, for each fixed negative endpoint parameter, the expected first occurrence time is of order \(n\log n\). In particular, the two potentially dangerous steps in Lemma 3 are valid: restarting at a strict global descending record preserves the record indicators, and the visits assigned to different sites do not double count a time. The proof answers Peres's order conjecture for the source's pattern set. It does not supply an asymptotic equivalent.

There is a literal quantifier error in the additional tail bound (4), a finite numerical endpoint discrepancy, and some attribution and reproducibility corrections. These require minor revision, not a replacement of the argument. My independent exact computations found no counterexample; independent simulations agree with the submitted results at the endpoints actually simulated. The source's Table 1 does not describe the correct expectations under its own stated convention. I found no earlier proof of the full order theorem in the literature checked, subject to the database-access limits stated below.

1. **Equation (4) needs an integer domain.** Location: `CLAIM.md:24–28`, and its proof at lines 247–251. As printed, \(k\geq0\) permits real \(k\). Take \(k=1/2\): \((n+m)/2<n\), so \(\mathbb P(T_n>k(n+m))=1\), whereas the displayed exponential is strictly below one. **Required fix:** state \(k\in\mathbb Z_{\geq0}\). For real \(k\), the proved bound has \(\lfloor k\rfloor\) in the exponent. The integer statement is correct and suffices for all conclusions.

2. **Specify endpoint rounding and correct or relabel the \(n=1000\) simulation.** Location: Theorem 1, line 5; numerical table, line 301; `claim_files/run_numerics.py:32`. The source uses \([\lambda\sqrt n]\), followed by adding one on incompatible parity. Under the usual floor interpretation, \(\lambda=-1,n=1000\) gives \(\lambda_n=-32\), not \(-30\). The submitted driver hard-codes \(a=30\). **Required fix:** write the rounding rule explicitly and either use \(a=32\) for the source comparison or label \(a=30\) as an alternative admissible approximation. Update associated fits if changing the data. This does not affect the proof: it works for every positive sequence \(a_n\equiv n\pmod2\) with \(a_n/\sqrt n\to|\lambda|\). The source does not explicitly define its bracket notation beyond the parity prescription; the manuscript should remove that ambiguity rather than infer a programming-language conversion rule.

3. **Resolve the convention part of the Table 1 discussion.** Location: `CLAIM.md:322`. The source's formula (2.4) uses the ending-time convention. Its separately defined starting time \(F_n\) for bridge windows is a different variable. **Required fix:** state this explicitly, distinguish the established inconsistency of the reported expectations from the unknown cause of the original simulation discrepancy, and retain the qualification that its code and sampling details were not recovered. The present claim's numerical detector is consistent with the source's mathematical convention. Subtracting \(n\) does not reconcile the two tables; details appear below.

4. **Credit the existing overlap count.** Location: Lemma 5 and equation (16), `CLAIM.md:210–218,255–261`. The source already gives the first-passage completion count in (2.21), immediately following its derivation in Section 2.4. Lemma 5 is a useful conditional-probability formulation of that count. **Required fix:** cite (2.21) there and distinguish it from the new use of the uniform \(C/s\) bound and the record-range argument. This is an attribution correction; the submitted proof of the identity is correct.

5. **Repair references to files in the supplied packet.** Location: `CLAIM.md:273,290,339–348,357`; `claim_files/LITERATURE.md`, items 1 and 4–5. The reproduction commands assume scripts beside `CLAIM.md`, but they are in `claim_files/`. The literature note refers to local PDFs/texts and `fetch_literature.py` absent from this packet. **Required fix:** prefix the commands with `cd claim_files` or supply correct paths, and identify which literature artifacts are actually supplied and which were only consulted online. This is a packaging defect, not a proof gap.

The mathematical verification follows. References to numbered equations and lemmas below are to the submission unless otherwise specified. New audit programs and outputs are listed near the end. I did not execute or import the claim's programs.

The source's question and conventions
-----------------------------------

I read Question 1.7, the definitions immediately before Theorem 1.8, Theorem 1.8(4), Theorem 2.1, and Sections 2.4–2.5 of `src/pt.txt`. I also downloaded [arXiv v3](https://arxiv.org/abs/1411.0041v3) independently and checked its PDF text. The relevant local lines are approximately 264–340, 375–409 and 641–831. The source takes words with **n increments**, starting at zero, with

\[
w(n)=\lambda_n,
\qquad w(i)>w(n)\quad(0\leq i<n).
\]

Thus the endpoint is the unique strict minimum of that window, including comparison with its starting height. For a nearest-neighbor walk ending at \(-a<0\), this is exactly first passage to \(-a\) at time \(n\). It is not the weaker condition that the endpoint merely attains the minimum. The submitted event \(E_t\) includes exactly the required comparisons, including \(t-n\), and omits only the endpoint itself. Its parity prescription is necessary; incompatible parities give an empty set, and are correctly assigned probability zero. For fixed \(\lambda<0\), the prescribed endpoint is negative and inside the support for all sufficiently large \(n\).

For an unambiguous formulation let

\[
H_n=\inf\{j\geq0:(S_{j+i}-S_j)_{0\leq i\leq n}\in FP_{\lambda,n}\}.
\]

Then the submission's variable is \(T_n=H_n+n\), pathwise. The source's matching formula (2.4) returns \(\mathbb ET_n\). For example, at \(n=3,a=1\) the only target increment word is \((+1,-1,-1)\), an unbordered word. Formula (2.4) gives 8. The starting-time expectation is 5. My exact automaton calculation gives the same distinction. Consequently even a reader who elects to interpret the informal phrase “waiting time” as \(H_n\) gets the same \(n\log n\) order, since the difference is exactly \(n\).

The [published chapter](https://www.columbia.edu/~wt2319/Patterns.pdf), printed p. 65, Conjecture 1, equation (30), and [Tang's dissertation](https://escholarship.org/content/qt51j6244c/qt51j6244c_noSplash_0d298bb720a71e482d931510dcf532d2.pdf), printed p. 18, Conjecture 2.5.2, ask for two-sided constant multiples of \(n\ln n\). Theorem 1 supplies precisely that assertion. The source's broader request for “exact asymptotics” in Open Problem 2.3 is stronger if interpreted as an asymptotic equivalent; that stronger task remains open in this submission.

Lemma 2: ballot identity and uniform bound
-----------------------------------------

The reflection calculation is correct:

\[
f_s(b)=\tfrac12[p_{s-1}(b-1)-p_{s-1}(b+1)]
       =(b/s)p_s(b),\qquad b\geq1.
\]

It counts a walk started at \(b\), killed on hitting zero, at height one at time \(s-1\), followed by a downward step. Symmetry permits the displayed positive arguments of \(p\). The binomial algebra gives the second equality, including support boundaries and incompatible parities.

The even ratio has logarithm bounded above by
\(-\sum_{r=1}^j(2r-1)/(k+r)\leq-j^2/(k+j)\).
For odd time, the analogous ratio product has numerator \(k-r+1\) and denominator \(k+r+1\); its logarithm is at most \(-j(j+1)/(k+j+1)\). Both inequalities in the submission follow. Stirling at the central coefficient and symmetry give (7), with absolute constants; the finitely many small times cause no problem.

Substitution yields

\[
f_s(b)\leq {C\over s}\,{b\over\sqrt s}
                 \exp(-cb^2/s)\leq C'/s.
\]

The maximization must be over \(b/\sqrt s\), as the submission does. No assumption about \(b=O(\sqrt s)\) is needed. The parity-lattice local central limit coefficient is \(\sqrt{2/\pi}\), not \(1/\sqrt{2\pi}\); hence (6), including its factor two, is correct. My independent killed-walk integer DP checked 3,200 \((s,b)\) cases against both reflection and ballot formulas. I checked the binomial-ratio inequalities through \(k=150\), and the largest \(s f_s(b)\) through \(s=500\) was \(1/2\). That observed sharper constant is not needed or assumed in the proof.

Lemma 3: the critical range argument
------------------------------------

A strict descending record at height \(-b\) is exactly \(\tau_{-b}=s\). Consequently

\[
\mathbb P(J_s=1)=s^{-1}\mathbb E(Y_s^-)\leq(2\sqrt s)^{-1}.
\]

Summing and using \(\sum_{s=1}^L s^{-1/2}\leq2\sqrt L\) proves (8). Independently, nearest-neighbor records visit the successive levels \(-1,-2,\ldots\), so \(V_L=1-\min_{s\leq L}Y_s\), consistent with this calculation.

Independence of \(X\) gives \(g_s=\sum_{b>0}(b/s)p_s(b)^2\). The telescoping identity in the proof is exact: writing both \(\binom{s-1}{j}\) and \(\binom{s-1}{j-1}\) as multiples of \(\binom sj\), their squared difference is \(((s-j)^2-j^2)/s^2\) times that square. The endpoint of the sum is \(\lfloor(s-1)/2\rfloor\), as printed. It follows that

\[
g_s=4^{-s}\binom{s-1}{\lfloor(s-1)/2\rfloor}^{2}.
\]

There is no missing parity factor. Separately for \(s=2k\) and \(2k+1\), Stirling gives \(g_s\sim1/(2\pi s)\). Thus \(G_L\sim\log L/(2\pi)\). I checked the identity exactly at 500 times. For a numerical scale check, \(10^4g_{10^4}=0.1591469855\), against \(1/(2\pi)=0.1591549431\). The additive constant in \(G_L\) is large enough that its ratio to \(\log L\) converges slowly; that is not a defect in the asymptotic statement.

For the restart, fix \(z\) and condition at \(r=\sigma_z<\infty\). This is a stopping time of the **pair** filtration; both walks are independent fresh walks after it. Put \(\widetilde Y_v=Y_{r+v}-Y_r\). The entire pre-\(r\) path is at least \(Y_r\). For \(u>0\),

\[
\widetilde Y_u<\min_{0\leq v<u}\widetilde Y_v
\]

forces \(\widetilde Y_u<0\), because the minimum includes \(v=0\). It therefore beats the pre-\(r\) minimum as well as every intervening value. Conversely a global record at \(r+u\) satisfies this shifted inequality. This proves the equivalence used in the submission. A shift at an arbitrary time would not have this property; shifting at \(\sigma_z\) does.

At \(r\), the difference equals \(z\), so another visit to \(z\) at a shifted record is exactly a zero of \(\widetilde X_u-\widetilde Y_u\). Including \(u=0\), the conditional expected count over the next \(L\) steps is precisely \(G_L\). Multiplying by \(1_{\{\sigma_z\leq L\}}\) is legitimate because that event is measurable at the stopping time.

The counting inequality also holds pathwise. A counted visit is the pair \((z,t)\), where \(t\leq\sigma_z+L\leq2L\), \(J_t=1\), and \(X_t-Y_t=z\). At a fixed \(t\) only one \(z\) can occur, and for that site the value \(u=t-\sigma_z\) is unique. Intersecting time intervals belonging to different sites do not create duplicate visits. Therefore

\[
G_L\mathbb E|R_L|\leq\mathbb EV_{2L}.
\]

Only sites \(|z|\leq2L\) can be discovered by time \(L\); no infinite-sum interchange is hidden here. Equations (8)–(9) now give (10). I checked both the restart equivalence and the actual visit-assignment inequality on 69,904 pairs of paths of length \(2L\), \(L=1,\ldots,4\). Exact enumeration of \(\mathbb E|R_L|\), \(L=1,\ldots,8\), also verifies \(G_L\mathbb E|R_L|\leq\mathbb EV_{2L}\); its ratio ranges from 0.892857 at \(L=1\) to 0.786167 at \(L=8\).

Lemma 4: decomposition and inclusion (13)
------------------------------------------

The three increment sets are \(1,\ldots,m\), \(m+1,\ldots,n\), and \(n+1,\ldots,n+m\). They are disjoint, so \(B\) is independent of the entire pair \((X,Y)\), including \(X_m\). If the window starting at \(s\leq m\) succeeds, all times \(n,\ldots,n+s-1\) lie inside its strict-minimum comparison interval. Thus \(s\) is a strict record of \(Y\). Its displacement condition rearranges exactly to

\[
B=X_s-Y_s-X_m-a.
\]

At \(s=0\), the artificially included record at zero is necessary and correctly handled. Therefore (13) holds. The translated random set is fixed when conditioning on \((X,Y)\), and has \(|R_m|\) distinct sites, irrespective of parity. Multiplying its cardinality by the largest atom of \(B\) is a valid upper bound; incompatible lattice points only reduce the probability. The last comparison of \(m\) and \(n-m\) is uniform for \(n\geq4\). The endpoint \(a\) only translates the set, explaining the asserted absolute uniformity. Exhaustive verification included 492,184 path/endpoint cases, all lengths \(n=2,\ldots,10\), all positive endpoints through \(n+1\), including empty/parity-incompatible cases.

Lemmas 5–6 and the theorem
--------------------------

For an observed admissible word \(w\), shifting its starting point by \(s<n\) requires a new endpoint at \(S_t+w(s)\). The old endpoint at time \(t\) is retained inside the new window, so it forces \(w(s)<0\). Under this condition every retained old height is above the required new endpoint. The remaining fresh path must first hit \(w(s)\) at its last step. There is no additional restriction on the retained suffix. Hence (14) is exact, not merely an upper bound. Interpret its product with an indicator piecewise, so no value of \(f_s(b)\) for \(b\leq0\) is needed. The identity was verified for every admissible word of length 2 through 10, every positive endpoint, and every shift \(1\leq s<n\): 2,147 word/shift cases, checked by enumerating 176,738 fresh continuations. All 273 matching-column identities at these lengths also passed.

Lemma 6 conditions at the ending time of the first successful window in the block. Previous failures are measurable by that time and impose no constraint on subsequent increments. Conditional on the actual successful word, (14) supplies a uniform bound, so it remains valid after conditioning on previous failures. There is one current success, no earlier successes, and at most \(C\sum_{s\leq m-r}s^{-1}\) expected later successes. Thus \(\mathbb EN\leq D_m\mathbb P(N>0)\). Stationarity gives exactly \(\mathbb EN=(m+1)f_n(a)\), and the alternative second-moment inequality has the correct factor two. I checked these inequalities against exact block probabilities, using the sharper finite constant \(D_m^*=1+\sum_{s\leq m}\max_b f_s(b)\); no unspecified asymptotic constant was fitted to make the tests pass.

For the theorem, (6), Lemma 4 and Lemma 6 give (2). A partition into consecutive sets of \(m+1\) starting indices gives the stated covering number, and hence (3), after increasing the absolute constant. Choose a fixed small \(\delta\), then let \(n\) grow: the upper bound at \(h=\lfloor\delta n\log n\rfloor\) is below \(1/2\), yielding \(\mathbb ET_n\geq h/2\). For a fixed scaled time \(Mn\), the same bound tends to zero; if \(M<1\), the event is already empty.

Finally, success within a block of \(n+m\) increments depends only on that block's increments. The inspected local windows all fit inside it, including the last window starting at \(m\). Independent blocks therefore have geometric first-success index \(K\), and \(T_n\leq(n+m)K\), even though the full search also allows windows crossing block boundaries. This proves the expectation upper bound and the integer version of (4). There is no unjustified use of independence between overlapping windows. I checked finite versions of the union and geometric bounds by exhaustive survival enumeration through time 18 at four small \((n,a)\) pairs, and checked the resulting bounds against their exact expectations.

Table 1 and independent numerics
--------------------------------

The convention is established by the source's matching formula, not guessed from Table 1. Its starting-time bridge variable \(F_n\), introduced later in (2.24), should not be conflated with \(T(FP_{\lambda,n})\).

There is also a useful exact lower bound. Write \(\pi_j\) for the probability that target word \(j\) is the first observed word. The standard overlap equations, in the source's orientation, give \(M\pi=2^{-n}\mathbb ET\,\mathbf1\). Summing rows, using \(\pi_j\geq0\), \(\sum_j\pi_j=1\), and column sums at least one, gives

\[
\mathbb ET\geq\frac{2^n}{\#FP_{\lambda,n}}=\frac1{f_n(a)}.
\]

This argument uses actual nonnegative first-winner probabilities; a diagonal bound for an arbitrary matrix alone would not suffice. The exact lower bounds and source values are:

| n | source endpoint magnitude (floor convention) | exact lower bound \(1/f_n(a)\) | source Table 1 |
|---:|---:|---:|---:|
| 100 | 10 | 206.294896 | 179.805 |
| 200 | 14 | 412.985798 | 358.249 |
| 500 | 22 | 1033.131431 | 893.041 |
| 1000 | 32 | 2066.297970 | 1800.002 |
| 2000 | 44 | 4133.490475 | 3682.022 |

Every reported value is below the lower bound for the true expectation. A sample mean can fall below a lower bound on its population mean, so this does not logically rule out an unusually small or biased original sample. The source supplies insufficient replication/error information to diagnose that possibility. It does establish that these cannot be accurate values of the expected waiting times as defined.

My detector uses a different characterization from the submitted monotone queue. On a downward step to height \(h\), the window endpoint is a strict minimum precisely when the previous visit to \(h\) occurred before the window's start, or no such visit occurred. Indeed, any earlier visit below \(h\) must have crossed \(h\) again before the current downward arrival. Combine this test with displacement \(-a\). I checked the detector against literal scanning on every length-18 increment stream, for every tested time, \(n=2,\ldots,10\), and every \(a=1,\ldots,n\): 168,296,448 comparisons, with no discrepancy.

Uncensored single-thread simulations gave:

| n | a | trials | mean ending time | standard error | mean starting time |
|---:|---:|---:|---:|---:|---:|
| 100 | 10 | 50,000 | 416.245 | 1.404 | 316.245 |
| 200 | 14 | 30,000 | 873.576 | 3.838 | 673.576 |
| 500 | 22 | 20,000 | 2344.137 | 12.954 | 1844.137 |
| 1000 | 30 | 25,000 | 4868.584 | 24.284 | 3868.584 |
| 1000 | 32 | 25,000 | 4964.451 | 24.974 | 3964.451 |
| 2000 | 44 | 15,000 | 10258.418 | 67.933 | 8258.418 |
| 10000 | 100 | 5,000 | 56845.795 | 654.214 | 46845.795 |
| 100000 | 316 | 1,000 | 624109.263 | 17334.046 | 524109.263 |

The nine shared \((n,a)\) cases, including the small cases omitted from this table, differ from the submitted sample means by less than 1.77 combined standard errors each. The \(a=32\) row is an additional source-convention check. No starting/ending-time switch explains Table 1. Nor can the rounding difference at 1000 explain the discrepancy at 100, where there is no rounding ambiguity.

I also recomputed Table 1's local exponents. For 1000 to 2000 the numbers give 1.0324997, not the printed 1.0375. The published chapter and thesis add rows at 5000 and 10000; their displayed means give exponents 0.9193565 and 0.5166976, not 1.0205 and 1.0335. Those arithmetic discrepancies do not depend on the probabilistic model. I cannot identify the original simulation bug, censoring rule, or transcription history from the available material, and do not claim to have done so.

The exact waiting-time fractions in all ten rows of the submitted exact table were independently recovered. Through \(n=10\), both a rational proper-prefix automaton and a separately constructed matching system agree exactly. For \(n=11,12\), independent integer Bareiss elimination of the scaled matching matrix recovers respectively \(317290872798/8937933785\) and \(17663784686/445122589\). I did not repeat the submitted million-step-size simulation or use a fit to validate the order theorem.

Moderate-size block checks also agree with the proof. At \(n=100,1000,10000\), with \(m=\lfloor n/2\rfloor\), simulated block-hit probabilities were 0.14735, 0.11880 and 0.09480. The exact finite-overlap lower bounds were approximately 0.07841, 0.05690 and 0.04503; the analytic range upper bounds were 0.53099, 0.42456 and 0.35831. Mean ranges were 3.59070, 8.83815 and 22.71080, against rigorous upper bounds \(\mathbb EV_{2m}/G_m\) of 4.72938, 11.90419 and 31.75557. The observed mean numbers of successes were within 1.25 standard errors of \((m+1)f_n(a)\). These are finite consistency checks; the asymptotic assertions rest on the analytic proof.

Literature result and limits
----------------------------

The live search was independent of the submission's saved query results. I searched the source title, arXiv identifier, thesis title, conjecture number, Peres's name, first-passage/first-passage-pattern waiting terminology, \(n\log n\), and the classical pattern-waiting references. The search date is 13 November 2026. The useful primary texts and citation records were:

- [Pitman–Tang, arXiv:1411.0041v3](https://arxiv.org/abs/1411.0041v3), the [published chapter](https://www.columbia.edu/~wt2319/Patterns.pdf), and [Tang's 2017 thesis](https://escholarship.org/uc/item/51j6244c). The source leaves the exponent gap; the published and thesis versions explicitly state the order conjecture. None of these gives its proof.
- A fresh [OpenAlex citation query for W1851725789](https://api.openalex.org/works?filter=cites%3AW1851725789&per-page=200) returned four records: the thesis and the three papers below. The arXiv DOI lookup resolves to the same work, so that lookup did not reveal a separate citation list. The thesis record [W2771801508](https://api.openalex.org/works/W2771801508) has zero indexed citing works. These are index observations, not assertions that no other citations exist. Raw searches, complete responses and request metadata are saved locally.
- [Pitman–Tang, *The Slepian zero set, and Brownian bridge embedded in Brownian motion by a spacetime shift*](https://arxiv.org/abs/1411.0040), EJP 20 (2015), no. 61. I read the introduction, embedding result and relevant pattern/random-walk discussion and searched the full text. Its first-passage decompositions concern the Slepian process; it does not prove this discrete waiting-time order.
- [Evans–Pitman–Tang, *The spans in Brownian motion*](https://arxiv.org/abs/1506.02021), AIHP 53 (2017). I read the main results, the discrete bridge approximation and the source-citation context. The span-set and Hausdorff-dimension questions do not supply the first-passage waiting-time estimate.
- [Pitman–Tang, *The argmin process of random walks, Brownian motion and Lévy processes*](https://arxiv.org/abs/1610.01524), EJP 23 (2018), no. 60. I inspected the main Markov/renewal results and the full-text matches. It studies extrema locations and processes, not the joint constraint on endpoint displacement and first occurrence used here. The arXiv text lists the source in its references but supplies no resolution of Peres's conjecture.
- Classical references checked: [Li (1980), DOI 10.1214/aop/1176994578](https://doi.org/10.1214/aop/1176994578), [Gerber–Li (1981), DOI 10.1016/0304-4149(81)90025-9](https://doi.org/10.1016/0304-4149(81)90025-9), and [Guibas–Odlyzko (1981), DOI 10.1016/0097-3165(81)90005-4](https://doi.org/10.1016/0097-3165(81)90005-4). Full original texts of these three were not recovered: the Li publisher endpoint returned a challenge rather than a PDF, an author-linked mirror was missing, and other publisher access failed. I therefore do not claim a full-text exclusion based on those inaccessible originals. I read the directly accessible primary exposition by [Odlyzko, *Enumeration of strings*](https://www-users.cse.umn.edu/~odlyzko/doc/arch/string.enumerate.pdf), Sections 3–5, and [Ostaszewska–Zajkowski, arXiv:1302.4859](https://arxiv.org/abs/1302.4859), particularly Theorem 2.3, Corollaries 2.4–2.5 and Remark 2.7. They give fixed-family overlap/generating-function and mean-waiting formulas, including the Li first-winner relation used above. I found no uniform first-passage-family \(n\log n\) theorem there. Having an exact matrix formula for each finite family does not itself establish the required growing-family asymptotic.
- I also read the definitions and main generating-function and Gaussian-limit results of [Asinowski–Banderier, *On Lattice Paths with Marked Patterns* (2020)](https://doi.org/10.4230/LIPIcs.AofA.2020.1), including Theorem 16. Its patterns are fixed words as the ambient path length grows. Its asymptotic regime differs from waiting for any first-passage word of a growing prescribed length; it gives no prior proof of this claim.

Direct Google Scholar searches and citation links could not be opened. I searched Scholar-visible pages and exact-title/identifier combinations through web search. MathSciNet's record and relay endpoints likewise were inaccessible; publicly visible references identify the chapter as MR3444294, including the [published argmin paper's bibliography](https://www.columbia.edu/~wt2319/Argmin.pdf). Searches for that MR number and the source/thesis titles did not reveal a prior resolution. This is **not** a completed search of authenticated MathSciNet citing-reference data or Google Scholar's full citation graph. The correct literature conclusion is that no prior proof was located in the accessible sources checked; novelty has not been certified exhaustively.

Audit artifacts and reproduction
--------------------------------

All new files remain in this directory. `CLAIM.md`, `claim_files/` and the supplied `src/pt.txt` were not edited. The independent code is `referee_exact.py`, `referee_matrix.py`, `referee_mc.cpp` and `referee_summarize.py`. Reproduce the mathematical checks from this directory with:

```sh
python3 referee_exact.py
python3 referee_matrix.py
clang++ -O3 -std=c++17 referee_mc.cpp -o referee_mc
./referee_mc
python3 referee_summarize.py
```

Exact output is in `referee_results/exact.json` and `matrix.json`; seeded Monte Carlo output is in `waiting.csv` and `blocks.csv`; comparisons and finite bounds are in `summary.json`. Literature retrieval programs and request logs are also supplied. They perform downloads only and do not publish anything. Some remote sources were read through the web tool when direct downloads failed.

The numerical programs use one thread and no numerical worker libraries. The measured C++ peak resident size was 4,341,760 bytes; the separate exact 90/132-word matrix calculation peaked at 19,316,736 bytes. The main exact enumeration streams paths rather than retaining an exponential path table; its largest rational system has 195 states, and its working data are also far below 4 GB. The sandbox rejected a request to lower process priority; I did not bypass that restriction. An initial `/usr/bin/time -l` wrapper exited on restricted `sysctl` accounting after its child had completed; a subsequent direct run and in-process resource measurement completed successfully. No simulation was censored, and no subagents were used.

Task: “Your job is to break it if it is wrong” — independent referee audit of the first-passage pattern claim, received 2026-11-13 at approximately 01:04 Asia/Tbilisi.
