# T105 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded clock: 2026-11-15 01:29:06 Asia/Tbilisi (2026-11-14 21:29:06 UTC); prompt receipt time is unavailable.

## Orientation and earlier files

Read the earlier folder's REPORT.md, LOG.md and SOLVED_ELSEWHERE.md in full. Its directory listing contains no PROOF.md and no scripts: the earlier session stopped at a literature finding. No earlier file was changed.

Read the startup memory index, brain navigation index and compute governor state. The specific instruction to write only within this folder overrides shared checklist, mesh and memory mutations; no such shared-state tools were run. Governor status was `warn`, mode `owner_away_open`, CPU 99.9%, free memory 50%, swap 7628.88 MB. No heavy computation is planned. Commands requested `OMP_NUM_THREADS=1 nice -n 15`; the sandbox returns `nice: setpriority: Operation not permitted` even for file reads. Therefore no numerical experiment will be run unless the priority restriction can be met. Mathematical verification can proceed without numerical computation.

Read commands (all prefixed `OMP_NUM_THREADS=1 nice -n 15`): `cat` of the earlier three files, directory listings of both task folders, `cat` of the governor state, startup MEMORY.md and BRAIN_INDEX.md. Output confirmed the earlier result is a partial literature observation only.

## Bounded literature check

Web searches: `"Berry Tabor" "2026" "spacing" torus`; `"flat tori" "Poisson" "2026" correlation`; `"Berry–Tabor" conjecture solved nearest neighbour torus`.

Opened primary sources:

- https://arxiv.org/abs/2601.03209 and https://arxiv.org/html/2601.03209v2 : Wooyeon Kim, Jens Marklof, Matthew Welsh, *Values of ternary quadratic forms at integers and the Berry-Tabor conjecture for 3-tori*. Theorem 1.1 concerns pair correlation of a three-dimensional Dirichlet box, with ratios of squared edge lengths κ-Diophantine for κ sufficiently close to 1. The arXiv page says v2 was revised 5 November 2026.
- https://arxiv.org/abs/1809.07881 : Christoph Aistleitner, Valentin Blomer, Maksym Radziwiłł, *Triple correlation and long gaps in the spectrum of flat tori*.
- https://arxiv.org/abs/2609.03112 : Christopher Lutsko, *Poissonian pair correlations for the three-particle Sutherland model*. The abstract concerns a different model and pair correlation only.
- https://ems.press/content/serial-article-files/42560 : retrieval timed out; no claim relies on that retrieval.

Search output included secondary problem registries and an automated audit site; these are not used as mathematical evidence. No solution of the stated flat 2-torus full-statistics problem was found. An omitted three-dimensional pair theorem does not trigger this session's “problem solved elsewhere” stopping condition.

## Independent re-check of the earlier main claim

The opened full-text Theorem 1.1 independently confirms the earlier report's dimension, statistic, boundary conditions and Diophantine hypothesis. Its introduction explicitly states that VanderKam's k-point result needs d ≥ 2k, and names Aistleitner, Blomer and Radziwiłł for the binary triple-correlation result. Thus the earlier bibliographic and scope corrections hold.

Re-derived the normalization without using the earlier formula: for Q(m)=Σ(πm_i/ℓ_i)^2 with m_i positive integers, the ellipsoid semiaxes are ℓ_i sqrt(E)/π. One eighth of its volume is (1/8)(4π/3)(ℓ_1ℓ_2ℓ_3/π^3)E^(3/2)=ℓ_1ℓ_2ℓ_3 E^(3/2)/(6π²). Independently, (2π)^(-3) times box volume times the momentum-ball volume gives the same coefficient. For nonzero coordinates, there are 2^3 sign vectors and global ± identifies pairs, leaving four copies. The earlier warning about symmetry sectors is correct.

The earlier statement that the whole problem remains open is supported, but absence of a solution cannot be certified by a bounded search. The previous use of the filename SOLVED_ELSEWHERE.md records an advance, not a solution; this session will continue to a mathematical step.

## Literature check closed; one extension selected

The initial search and primary-source check finished by 01:31 Asia/Tbilisi, less than five minutes after the first clock. Opened https://arxiv.org/pdf/1809.07881 (33 pages), including its definitions and statements on pp. 2–4, then located Section 6. It confirms that its averaged triple theorem yields a long-gap bound G approximately 2.00636 through integrated inequalities for the spacing distribution. A targeted search also surfaced a later improvement of the pair-only 3/2 constant; that is not needed for the chosen argument and no result from it is asserted here.

CHOICE, written before undertaking the proof: solve the scalar two-factorial-moment relaxation behind the known triple-correlation long-gap argument. Determine whether optimizing *all* pointwise quadratic count inequalities, together with monotonicity, the pair-correlation Lipschitz constraint and mean spacing, can improve its G. The reason is concrete: a proof of optimality would rule out a tempting reoptimization route and specify which additional information a future attack must retain. This is a limited analytic task, not a proof of torus spacing convergence and not a claim that scalar moment laws can be realized by a spectrum. Any original conclusion will be confined to this explicitly defined relaxation.

Web commands for locating the argument: `find` in the opened PDF for `Lemma 2.`, `Proof of Corollary 3`, followed by `open` around PDF text lines 2878, 2950 and 3020. No additional search is planned.

## Analytic step 1: exact scalar moment problem

For an integer-valued C ≥ 0 with E C=s and E[C(C−1)]=s², the pointwise minorant

q_m(n) = [2mn−n(n−1)]/[m(m+1)], m ≥ 1,

satisfies 1_{n>0}−q_m(n)=(n−m)(n−m−1)/[m(m+1)] ≥ 0 for integer n ≥ 1, and equality at n=0,m,m+1. Therefore P(C>0) ≥ L_m(s)=(2ms−s²)/[m(m+1)]. For m−1 ≤ s ≤ m the law

P(C=m)=s(m−s)/m,
P(C=m+1)=s(s−m+1)/(m+1),
P(C=0)=1−L_m(s)

attains the bound. Direct substitution gives total probability 1, first moment s and second factorial moment s². Also 1−L_m(s)=[(m−s)²+m]/[m(m+1)]>0. Thus L(s)=L_m(s) for m=floor(s)+1 is the exact minimum, and no other quadratic minorant (including one with a constant term) can improve it. This is an elementary moment calculation, not claimed as a new general probability inequality.

## Analytic step 2: the gap relaxation and its threshold

Impose on a candidate gap CDF F: F(0)=0; F nondecreasing and 1-Lipschitz; support in [0,G]; mean 1; and F(s) ≥ L(s). The Lipschitz constraint and F(G)=1 imply F(s) ≥ 1−G+s. For G near 2, the minimal envelope consists of L_1 on [0,1], L_2 on [1,c], and 1−G+s on [c,G], where c=sqrt(6G−5)−1.

Integrating these three pieces gives

I(G) = G−G²/2+1/18+c²/6+c³/9.

Mean 1 requires I(G) ≤ G−1. The difference D(G)=I(G)−G+1 has derivative c−G<0. At G=2, 18D=14sqrt(7)−37>0 because 1372>1369. The equality condition is

35−18G−9G²+(12G−10)sqrt(6G−5)=0.

At equality the envelope itself is an admissible CDF, so this is a candidate exact barrier for the relaxation. The remaining audit checks all scalar upper constraints, all interval lengths, and independent integration of its density.

## Source-version audit

While checking the equation, the arXiv v1 PDF text lacked the term −18G in Corollary 3; without it the quoted decimal near 2 cannot solve that equation. This is not used as a new finding: the opened EMS online-first paper already contains the term. Successful primary-source URL: https://ems.press/content/serial-article-files/31432 (34 pages), Corollary 3 on PDF p. 4, DOI 10.4171/JEMS/1356. Its equation agrees with the independent integration above. Two attempts to retrieve https://ems.press/content/serial-article-files/42560 timed out. The arXiv screenshot tool returned only a citation string and no inspectable image, and the ar5iv URL was unavailable. No visual assertion about the arXiv typesetting is made.

## Proof saved and attacked

Wrote PROOF.md with a self-contained definition of the relaxation and an explicit attaining CDF. The result is an exact threshold for this relaxation, not an improvement of the published torus long-gap constant.

Checks made independently of the first integration:

- Differentiation: c'=3/(c+1), I'=1−G+c, D'=c−G. The identity G−c=((c−2)²+2)/6 makes strict decrease explicit.
- Polynomial elimination: with G=(c²+2c+6)/6, 72D=40−24c−c²(c−2)². The root is equivalently R(c)=c⁴−4c³+4c²+24c−40=0. This independently recovers the square-root equation.
- Exact signs: R(33/20)=−10639/160000 and R(5/3)=25/81; R'≥16 on [1,2]. These give 1603/800<G*<109/54. Independently, at G=2 the sign is 14sqrt(7)−37>0 by 1372>1369, and D(109/54)=−25/5832.
- Normalization by density instead of CDF integration: the three density pieces are 1−s, (2−s)/3, and 1. Their masses sum to G−c/3−c²/6=1. Their first moment is G²/2−c²/6−c³/9−1/18=1 at the root.
- Audited all scalar *upper* constraints, not just quadratic minorants. For s>1 an explicit mixture of a law on {floor(s),ceil(s)} and a law on {1,M} has the required moments and no zero mass. Mixing this with the minimizing law supplies every p in [L(s),1]. For 0<s≤1 the sharp upper supremum is s, never attained, as certified by laws on {0,1,M}; the candidate uses the attained lower endpoint in this range.
- Checked s=0, s=1, integer moment breakpoints, the crossover c, s=2, s=G*, and all s>G*. The envelope for s≥2 is dominated by the endpoint line because 53/54>3/4. F is continuous at every breakpoint, so there are no hidden atoms.
- Checked ordered triple counts directly: sum C_i(C_i−1)/N is T3; the quadratic coefficient uses the ordered convention. There is no missing factor 2.
- Tried to overinterpret the result as a point-process obstruction. That fails: the scalar laws are not coupled across s, and no stationarity or cross-anchor relation has been imposed. This limitation is explicit in the theorem and report.
- Also checked the possible loss of moments under weak limits. PROOF.md now expressly avoids using weak convergence to pass the second moment. No torus is asserted to satisfy exact individual triple limits.

The value 2.00636193892510 is quoted only as the paper's decimal; the proof relies on the exact equation and the independently checked rational bracket. No numerical experiment or decimal root computation was run. The generic scalar moment bound is elementary and no claim of a new probability inequality or global literature priority is made.

## Completion

Saved REPORT.md with the required first-line verdict and an explicit joint-count feasibility problem for the next worker. Final readback command: `OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md PROOF.md`. Exit code 0; both complete files were read back, including the exact theorem, extremizer, limitations and task timestamp. The priority-adjustment warning persisted. No numerical program, git command, subagent, external mutation or shared-memory write was used. Only LOG.md, PROOF.md and REPORT.md were created in the current folder.

Final audit found no algebraic inconsistency. The central limitation remains deliberate: separate scalar count laws are not a common point process. This is a proved relaxation threshold, not a theorem giving the full spacing law of any individual torus.
