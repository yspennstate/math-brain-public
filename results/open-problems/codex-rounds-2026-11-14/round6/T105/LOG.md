# T105 work log

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 2026-11-15 10:54:25 Asia/Tbilisi (06:54:25 UTC); prompt receipt time unavailable.

## Orientation and bounded literature check

Read the four earlier directories, their REPORT.md and LOG.md files, and the three existing PROOF.md files. The first directory has no PROOF.md; no earlier directory contains a numerical script. Some combined reads exceeded the tool output limit; those files are being read separately. No earlier file was edited.

Read the startup memory index, its startup instruction card, and the compute governor state. The governor reports status `ok`, mode `owner_away_open`. The task-specific instruction permitting writes only here supersedes shared mesh, checklist and memory mutations. Those commands, including recall commands that log outside this folder, will not be run. No git, subagents, account creation, posting or external writes are used.

Read commands use `OMP_NUM_THREADS=1 nice -n 15`. The sandbox prints `nice: setpriority: Operation not permitted` even for `/bin/cat`. As in previous rounds, no numerical program will be run without a verified resource-compliant launch; the selected step can be proved using exact algebra. File edits use apply_patch in this folder.

The initial literature search and primary-source opening finished within five minutes. Web searches: `Berry Tabor flat tori nearest neighbour spacing distribution 2025 2026`; `"flat tori" "long gaps" "2026"`. Opened:

- https://arxiv.org/abs/1809.07881 : Christoph Aistleitner, Valentin Blomer, Maksym Radziwiłł, *Triple correlation and long gaps in the spectrum of flat tori*.
- https://ems.press/content/serial-article-files/42560?nt=1 : the published 34-page text, DOI 10.4171/JEMS/1356. Read its spectrum convention, Theorem 1 and pair-correlation statement. Theorem 1 is uniform in both bounded interval parameters and averages over every finite parameter rectangle.
- https://arxiv.org/abs/2601.03209 : Wooyeon Kim, Jens Marklof, Matthew Welsh, *Values of ternary quadratic forms at integers and the Berry-Tabor conjecture for 3-tori*. Its v2 remains a pair-correlation result for a three-dimensional box.

No solution of the stated two-dimensional full-statistics problem was found. Secondary registries and automated audits in the search results are not used as mathematical sources. This bounded search does not prove absence or global novelty. No SOLVED_ELSEWHERE.md is warranted.

## Independent re-check of round 5

The adjacent-count inequality holds at every integer pair. For A=0,B>=1 its residual is (B-1)(B-2); for A>=1 it is ((A+B-2)(A+B-3)+B(B-1))/2; at (0,0) it is zero. Every residual is nonnegative. Using truncated counts at every anchor produces exactly (12) and then (24), with no terminal correction in the count identities. Only the eventual-gap bound contributes the displayed O(1/N) correction.

Independently checked the window gain by integrating the antiderivative J(s)=s^2/3-s^3/18 at the four endpoints: the integrals are 9311/589824 and 21400/589824. Their sum is 10237/196608. The replacement has pair benchmark 5/64 and triple benchmark 13/512, hence value 27/512=10368/196608. The gain is therefore 131/196608, as reported.

The quantifier argument holds: for the single nonnegative functional Q_N, rectangle-averaged convergence and Fatou at a density point imply liminf Q_N<=q almost everywhere. Its coefficients are nonnegative and bounded integration over intervals is allowed by the uniformity in Theorem 1. The full pair functional converges pointwise. Thus one common subsequence suffices in the finite inequality. No pointwise triple limit or passage of moments through weak convergence is used.

As an independent threshold check, integrating the density pieces 1-s, (2-s)/3, 1 gives total mass G-c/3-c^2/6=1 and first moment G^2/2-c^2/6-c^3/9-1/18=1-D(G). Substituting G=(c^2+2c+6)/6 gives 72D=-[c^2(c-2)^2+24c-40]. Thus the reported root equation is correct. The round-5 main claim holds, conditional on the stated published correlation inputs.

## One extension selected, before the new calculation

CHOICE: replace the two fixed-anchor right windows by two moving windows. Integrate the same adjacent-count inequality with a varying first length a and a varying total length t(a) whose derivative is 2. Then the two CDF terms integrate exactly over the windows, eliminating the monotonicity loss in round 5. Optimize a simple family with consecutive windows wholly in the quadratic scalar branch, and give an exact rational gain and a complete transfer to the almost-everywhere torus gap bound. This is one extension of the same certificate; it needs no new correlation theorem. No optimality beyond the explicitly selected family will be claimed.

## Moving-window calculation

For 0<=u<=w put a=1+u, t=1+w+2u, b=t-a=w+u. The change of variables dt=2 du gives exactly

integral_0^w [F_N(1+u)+2F_N(1+w+2u)] du = integral_1^(1+3w) F_N(s) ds.

Thus the adjacent-count inequality can replace the entire scalar integral on W=[1,1+3w], without a monotonicity estimate. With L_2(s)=(4s-s^2)/6, the excess Poisson benchmark at u is

2t-(t^2+b^2)/2-L_2(a)-2L_2(t)
= (w-2w^2)/3 + (1-5w)u/3-u^2.

Its integral is eta(w)=w^2/2-11w^3/6. Within this one-parameter family the maximum is attained at w=2/11 and is eta=2/363. Differentiation gives eta'=w(1-11w/2). Independently,

2/363-eta(w) = (11w+1)(w-2/11)^2/6 >= 0 for w>=0.

At this width the windows are [1,13/11] and [13/11,17/11]. They touch only at an endpoint of measure zero and lie below c(2)=sqrt(7)-1, since 784<847. Every triple coefficient remains nonnegative in the combined functional. The same rectangle-averaging lemma from round 5 applies, now also integrating the two changing triple intervals in u; uniformity in both interval endpoints is exactly what is needed.

The new threshold must exceed 109/54, so the former restriction G<=109/54 cannot be retained. Extend the purely algebraic scalar construction to 2<=G<=67/32, with c(G)=sqrt(6G-5)-1<=7/4<2. Its finite inequalities and matching integral remain valid. The crossover is unchanged, the new window remains wholly below c, and D'=c-G<0. No extrapolation of a fixed-branch formula across its crossover is being made.

Set R(c)=c^2(c-2)^2+24c-40. The necessary condition for an eventual bound is D(G)+2/363<=0. The unique new zero Gamma is specified by R(c_Gamma)=48/121 and Gamma=(c_Gamma^2+2c_Gamma+6)/6. At G=2, D>0; at G=67/32, R(7/4)=561/256>48/121, so the sign is negative. Also 48/121>25/81=R(5/3), since 3888>3025; therefore Gamma>109/54, a strict improvement over the prior bound.

All earlier required files have now been read in separate untruncated calls, including round-3 PROOF.md, round-4 LOG.md and REPORT.md, and round-5 LOG.md. Directory listings found no earlier scripts. No numerical program was run.

## Proof saved and independent audit

Saved PROOF.md with the complete finite-count argument, moving-window optimization, one-functional averaging lemma, eventual-gap corrections and countable-intersection step. Read it back with `OMP_NUM_THREADS=1 nice -n 15 /bin/cat PROOF.md` (exit 0; the priority warning persists).

Independent check of the new gain, separating the two moment terms rather than using the deficit polynomial: at w=2/11, 2 integral t du=60/121=1980/3993, while (1/2) integral (t^2+b^2) du=707/3993. The replacement is 1273/3993. Direct antiderivative differences give integral_1^(17/11) L_2=417/1331=1251/3993. Their difference is 22/3993=2/363. Separately substituting w=2/11 into w^2/2-11w^3/6 gives 6/363-4/363=2/363. The critical point from differentiation and the square factorization agree. Thus the gain and its optimization were each checked two ways.

Independent check of the rational lower bound: R(167/100)=38371121/100000000. Factored evaluation uses 167^2*33^2+8000000=27889*1089+8000000=38371121. Expanded polynomial evaluation has numerator 777796321-1862985200+1115560000+8000000=38371121. Comparison with 48/121 uses 4642905641<4800000000. Equivalently their positive difference is 157094359/12100000000. The increasing endpoint map gives Gamma>121289/60000, and 121289/60000-2021/1000=29/60000>0. Its magnitude is consistent with the new root lying beyond 109/54 but close to 2.

The upper sign was checked from both expressions for R: R(7/4)=49/256+2=561/256, or (2401-5488+3136+512)/256=561/256. The comparison against 48/121 is 67881>12288. The relation c=7/4 gives G=(49+56+96)/96=67/32, agreeing with direct substitution in c(G). The value 72eta=144/363=48/121 was independently reduced. Differentiating D and expanding 72D both give the same threshold equation and the correct direction of improvement.

Attempts to break the argument:

- The moving windows must use dt/du=2. Omitting this Jacobian would overcount the second window. Equation (9) includes it exactly; the windows meet only at 13/11, a null endpoint for integration.
- The triple term for the increment is U_N((a,t]), whose benchmark is (t-a)^2, rather than t^2-a^2. Both independent gain calculations use b^2. The ordered last two indices require both coefficients 1/2 in the joint certificate.
- The intervals (0,t(u)] and (a(u),t(u)] vary in both endpoints. The opened published Theorem 1 is uniform for both interval arguments in a bounded ambient interval; integrating that uniform averaged error proves (23) for the entire Q_N. Separate scalar liminf bounds would not suffice and are not used.
- Every triple weight in (25) is nonnegative, including after deleting the scalar window. A signed-functional Fatou argument would fail; this construction does not require one.
- The entire new window ends at 17/11<sqrt(7)-1<=c(G), for all candidate G. The algebraic range extends only to c=7/4<2. There is no overlooked scalar-branch crossover. In fact the proof only needs the finite scalar inequalities on the stated pieces, not an assertion that H_G is the globally optimal envelope in the extended range.
- Check of extreme finite counts: (A,B)=(0,0), (0,1), (0,2), (1,0), (1,1), (2,1), and all larger counts are covered by the explicit residual polynomials. No bound on count size or limiting count law is needed.
- Check of early exceptional gaps and the last anchor: equation (20) loses (M+1)/N; equation (21) includes the finite sum of excess gaps. Thus the conclusion rules out eventual bounds and proves a limsup statement. It does not silently assume the bound holds from the first gap.
- Check of quantifiers: one null set for each candidate G, then a countable union over G=2 and rational 2<G<Gamma. No uncountable intersection or individual-torus triple convergence appears.

What failed or remains limited: retaining the old endpoint range would be invalid because the new zero exceeds 109/54; extending it explicitly to 67/32 fixes that restriction. Global optimality was not attempted. The full spacing law and any explicit-torus version remain unresolved. The external published correlation theorems are used without rechecking their full proofs. The bounded literature search cannot certify global novelty. Priority adjustment is denied, so no numerical verification or experiment was launched. The initial discovery shell command lacked the requested nice prefix; all subsequent shell reads used it. No files outside this folder were written.

## Completion

Saved REPORT.md with the required verdict, exact theorem, what is new, validation, commands, limitations and the next moving-window extension. Final readback `OMP_NUM_THREADS=1 nice -n 15 /bin/cat REPORT.md LOG.md` and the prefixed `rg -n` check of the verdict, new functional, window endpoints and constants in all three files exited 0. The priority warning persisted. No mathematical inconsistency was found. Only LOG.md, PROOF.md and REPORT.md were authored in this folder. Final recorded clock: 2026-11-15 11:02:09 Asia/Tbilisi (07:02:09 UTC).
