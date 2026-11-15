# T105 work log

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 2026-11-15 04:54:16 Asia/Tbilisi; prompt receipt time unavailable.

## Orientation and literature check

Read both earlier folders' REPORT.md and LOG.md, the round-3 PROOF.md, and the first folder's SOLVED_ELSEWHERE.md. Directory enumeration found no scripts in either folder and no PROOF.md in the first folder. No earlier files were changed. Read the startup MEMORY.md, brain navigation index and compute governor state. The task-specific restriction on writes outside this folder overrides the global mesh, checklist and memory-write instructions; none of those shared-state operations will be run.

The governor reports `warn`, `owner_away_open`, CPU 98.9%, free memory 69%. A requested `OMP_NUM_THREADS=1 nice -n 15 /bin/date` prints `nice: setpriority: Operation not permitted`, as in the earlier sessions. No numerical program is planned. Initial directory and file reads used ordinary shell commands; subsequent reads use the requested prefix. File writes use apply_patch. No git, external mutation, account creation or subagent is used.

Bounded web check, completed by 04:54:45 Asia/Tbilisi (under one minute after the first clock):

- Searches: `Berry Tabor conjecture flat torus nearest neighbour spacing 2026 Poisson`; `flat tori joint correlation long gaps 2025 2026 Aistleitner Blomer`; `site.arxiv.org "flat tori" "2026" spacing correlation`; `site.arxiv.org "Berry-Tabor" "spacing" "2025" "2026"`.
- Opened https://arxiv.org/abs/1809.07881 and https://ems.press/content/serial-article-files/31432 : Christoph Aistleitner, Valentin Blomer, Maksym Radziwiłł, *Triple correlation and long gaps in the spectrum of flat tori*. The publisher PDF is readable and states an averaged triple result. The alternate publisher URL ending `/42560` timed out.
- Opened https://arxiv.org/html/2601.03209v2 : Wooyeon Kim, Jens Marklof, Matthew Welsh, *Values of ternary quadratic forms at integers and the Berry-Tabor conjecture for 3-tori*. Theorem 1.1 remains a three-dimensional Dirichlet-box pair-correlation result. This does not solve the two-dimensional spacing problem.
- Opened https://arxiv.org/abs/2609.03112 : Christopher Lutsko, *Poissonian pair correlations for the three-particle Sutherland model*. The abstract concerns a different model and pair correlation.

No later solution of the stated target was found. This bounded check cannot certify absence. No SOLVED_ELSEWHERE.md is warranted. Secondary registries and automated summaries in search output are not mathematical sources.

## Independent re-check of round 3

Re-derived the scalar extremal law by solving its moment equations, rather than assuming the probabilities in the earlier proof. A law supported on {0,m,m+1} must solve m p_m+(m+1)p_{m+1}=s and m(m−1)p_m+m(m+1)p_{m+1}=s². Subtracting (m−1) times the first equation from the second gives (m+1)p_{m+1}=s(s−m+1), then m p_m=s(m−s). Its positivity probability is (2ms−s²)/(m(m+1)). The polynomial residual at a positive integer n is (n−m)(n−m−1)/(m(m+1)), so this law is minimal when m−1≤s≤m. This verifies both sharpness and the equality supports, which will matter for coupling.

Independently used the density pieces to check the earlier threshold: f=1−s on (0,1), f=(2−s)/3 on (1,c), f=1 on (c,G). Total mass is G−c/3−c²/6, hence mass one gives G=(c²+2c+6)/6. The first moment is G²/2−c²/6−c³/9−1/18. Setting this to one and substituting G yields c⁴−4c³+4c²+24c−40=0. This is exactly the earlier quartic, with the same interval and endpoint relation. The round-3 main claim holds within its explicitly uncoupled scalar relaxation. Its witness is not asserted to be a counting process.

## One extension selected, before the joint calculation

CHOICE: test the round-3 CDF F* against the report's adjacent-interval joint count constraints. Seek an exact incompatibility certificate, using the equality supports of the scalar moment inequalities and the increment's factorial moment. The reason is that these are precisely the relations discarded by the scalar relaxation; rejecting the witness would identify a concrete extra constraint without asserting any torus theorem. First test around the breakpoint s=1, where the minimizing positive support changes from {1,2} to {2,3}.

## Adjacent-interval calculation

Set a=1, b=1/4 and t=a+b=5/4. The crossover c*=sqrt(6G*−5)−1 exceeds sqrt(7)−1>5/4, so both a and t lie on the scalar lower envelope. The earlier CDF has F*(1)=1/2 and F*(5/4)=55/96, a difference 7/96.

If the proposed joint counts existed, T=A+B would have E T=t and E[T(T−1)]=t², by the marginal moments and E AB=ab. Equality at the scalar lower bound L_2(t) forces T to be supported on {0,2,3}. On {A=0,T>0}, B=T≥2; hence F*(t)−F*(a)≤E[B(B−1)]/2=b²/2=1/32=3/96. The contradiction has margin 4/96=1/24. This rejects the round-3 extremizer for the exact two-interval problem the report proposed, without requiring an entire counting process.

Independent, non-equality certificate: for all nonnegative integers A,B, with T=A+B,

1_{A>0}+2·1_{T>0} ≥ 2T−T(T−1)/2−B(B−1)/2.

If A=0, the right side is 3B−B²≤2 for B≥1 (equality at B=1,2); both sides vanish at B=0. If A≥1, the left side is 3 and the right side is at most (5T−T²)/2≤3 for positive integer T (equality at T=2,3). Taking expectations gives

F(a)+2F(t) ≥ 2t−t²/2−b²/2.

At a=1,t=5/4 the right side is 27/16=81/48; the earlier CDF gives 1/2+2·55/96=79/48. The deficit is again 1/24. This checks the certificate without invoking uniqueness of the scalar minimizing law. No numerical calculation was used.

The polynomial certificate also retains its exact form with empirical moments. Small moment errors therefore enter linearly; there is no weak-limit or uniform-integrability passage in this step. The next part of this same extension will quantify its separation from the scalar endpoint within a precisely defined joint relaxation. It will not assert an improved torus gap theorem.

## Quantitative separation in the joint relaxation

Keep the round-3 scalar requirements and add just the one joint law at a=1,b=1/4. For 2≤G≤109/54, write H_G for the earlier pointwise envelope and δ=F−H_G≥0. Both functions are nondecreasing and 1-Lipschitz, so their difference is 1-Lipschitz: each increment is a difference of two numbers in [0,h]. At 1 and 5/4 the envelope is independent of G and equals the scalar minimum. The new inequality gives δ(1)+2δ(5/4)≥1/24, so at least one value is ≥1/72.

The 1-Lipschitz property forces a triangle of area (1/72)²=1/5184 underneath δ, entirely inside [0,G]. Hence −D(G)=∫δ≥1/5184. Since D(G*)=0, D'=c(G)−G and G−c(G)=((c−2)²+2)/6≤3/8 on this interval, −D(G)≤(3/8)(G−G*). Thus every candidate in this joint relaxation with G≤109/54 has G≥G*+1/1944.

For larger G the same lower bound follows from an exact root bracket. R(83/50)=990921/6250000>0, so c*<83/50 and G*<10063/5000. Also 109/54−10063/5000=799/135000>1/1944, since 799·1944=1553256>135000. Therefore the bound G≥G*+1/1944 is unconditional within this relaxation. This is a necessary bound, not its optimum; no finite-endpoint feasible joint process has been constructed.

## Proof saved and independent audit

Saved PROOF.md with the pointwise integer inequality, two distinct incompatibility proofs, the endpoint-separation theorem, an error estimate, and the exact finite-sequence version. The theorem only assumes the scalar lower bounds plus the one joint law, so it also applies to the stronger relaxation retaining every separate scalar witness and every adjacent pair.

Completed the sufficiency part of the re-check of round 3: the density of F* has mass one and mean one as above. Until c*, its scalar laws are the minimizing laws. For s>1, a positive integer law on {floor(s),floor(s)+1} with mean s has second factorial moment s²−s+θ(1−θ)<s² (θ is the fractional part). A positive law on {1,M} with the same mean has second factorial moment M(s−1)>s² when M>s²/(s−1). A mixture attains s² while retaining positivity probability one. Mixing with the scalar minimum realizes every positivity probability in [L(s),1], including F*(s) for s>c*. Thus the prior attaining CDF has all the required *separate* witnesses. The earlier result remains correct; the new result excludes its proposed joint extension.

Audit calculations, all exact and done a second way:

- The contradiction margin from equality support is 7/96−3/96=4/96=1/24. The independent polynomial certificate gives 27/16−79/48=(81−79)/48=1/24.
- The right side of (8) at the selected pair is (80−25−1)/32=54/32=27/16. Also L_2(5/4)=(80−25)/96=55/96. This checks each number without decimal arithmetic.
- The pointwise residuals are explicit for every integer pair: zero at (0,0); (B−1)(B−2) when A=0,B≥1; and [(T−2)(T−3)+B(B−1)]/2 when A≥1. This covers counts 0,1,2,3, all larger counts, and unbounded-support laws. The polynomial and equality-support proofs do not assume independence or stationarity of increments.
- The area 1/5184 follows both from the area of a triangle of base 2/72 and height 1/72, and from integrating its level-set lengths: ∫_0^(1/72) 2(1/72−r) dr. Both triangle supports, about 1 and 5/4, lie strictly inside [0,G] since G≥2.
- The slope bound follows from G−c=((c−2)²+2)/6 and 3/2<c≤5/3, giving (1/4+2)/6=3/8. Dividing area by slope gives (1/5184)/(3/8)=8/15552=1/1944.
- Rechecked the root sign by the factored expression: at c=83/50, c²(c−2)²=(6889·289)/6250000=1990921/6250000 and 24c−40=−4/25=−1000000/6250000. Their sum is 990921/6250000. The endpoint relation gives (6889+8300+15000)/15000=10063/5000.
- The large-endpoint comparison is (109·5000−10063·54)/270000=1598/270000=799/135000. Cross multiplication against 1/1944 gives 1553256>135000. The case G<2 reduces to the scalar contradiction at endpoint 2, and G=G* is excluded by positive area. All endpoint ranges are covered.
- Rechecked D(2) using the quartic: at c=sqrt(7)−1, R(c)=148−56sqrt(7), so 18D(2)=−R/4=14sqrt(7)−37. At c=5/3, R=25/81 gives D(109/54)=−25/5832. These agree with direct envelope integration.
- Moment errors in the new inequality have coefficients 2,2,−1/2,−1,−1, whose absolute values sum to 13/2. The sufficient tolerance is (1/24)/(13/2)=1/156. Allowing both probabilities an error ε adds 3ε, giving (1/24)/(19/2)=1/228. This is stability of the certificate, not an optimal tolerance theorem.
- The finite-count identity uses ordered distinct later indices: T(T−1) and B(B−1) each count both orders. The factors 1/2 are therefore required. All anchors, including the last with zero later counts, use the same truncation. Direct checks with one or two later points give the same coefficients; no boundary correction is hidden.

Additional source-location commands, without further literature searches: web `find` on the opened publisher PDF for `Proof of Corollary 3` and `2:006361`. The first returned Corollary 3 and Section 6; the latter found no exact text match. The paper's displayed scalar constant and equation agree with the earlier report. No assertion relies on an unavailable screenshot or the timed-out URL.

Readback commands: `OMP_NUM_THREADS=1 nice -n 15 /bin/ls -la` of the two prior folders and the current folder, and `OMP_NUM_THREADS=1 nice -n 15 /bin/cat PROOF.md LOG.md`. Both exited 0, with the recurring priority warning. The full directory listings confirm no prior scripts and no first-session PROOF.md. No numerical script was needed or run.

## Limits and next step

The attempt to retain F* under even one adjacent joint law fails, by the exact certificate. The attempt to call the stronger endpoint an improved torus bound is not justified: this proof has ideal pointwise count moments, whereas the torus triple theorem is averaged. No joint realization, finite-endpoint example, optimum joint threshold, or full Berry–Tabor statement is proved. The literature check does not certify novelty or absence of a later solution.

Next worker: use the exact finite inequality (20) as an additional constraint in the published long-gap argument. The two triple terms have nonpositive coefficients in the lower bound for F, hence nonnegative coefficients when rearranged as a lower bound for a sum of triple counts. Determine whether the density-point/averaging method of the paper gives an upper subsequential bound for the necessary nonnegative combination, simultaneously with the integrated scalar argument. This quantifier step must be proved before claiming an improved torus constant. Alternatively, optimize the joint relaxation itself; 1/1944 is only a conservative separation.

## Completion

Saved REPORT.md with the required verdict, the exact new theorem, its limitations, and the proposed next step. Final readback `OMP_NUM_THREADS=1 nice -n 15 /bin/cat REPORT.md` exited 0 and confirmed the complete report. A final heading/constant check with `/usr/bin/grep -n` located the same 1/1944 bound in both saved files and the error tolerance in PROOF.md. The priority warning persisted. Final recorded clock: 2026-11-15 05:01:28 Asia/Tbilisi (01:01:28 UTC). Only LOG.md, PROOF.md and REPORT.md were authored in this folder; both earlier folders remain untouched.
