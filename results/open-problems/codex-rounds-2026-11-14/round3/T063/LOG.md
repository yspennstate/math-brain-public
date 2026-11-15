# T063 work log

Task received: 15 November 2026, about 01:07 Asia/Tbilisi (14 November 21:07 UTC).

## Orientation

Read the previous REPORT.md, LOG.md and SOLVED_ELSEWHERE.md in the read-only earlier folder. Its complete directory listing contains no PROOF.md or scripts; there is no earlier proof or computation to rerun. The earlier result is a literature identification and elementary parameter conversion, which will be independently checked below.

Read compute_state.json: status warn, mode owner_away_open, CPU saturated. No heavy computation is appropriate. All program invocations use OMP_NUM_THREADS=1 and nice -n 15; the launcher reports a permission error on changing priority (the earlier worker independently found inherited nice 20). No subagents or git. The task-specific restriction on writes outside this folder supersedes global mesh, checklist and memory writes. A startup brain recall was attempted before substantive work; it returned unrelated provisional memories, no useful T063 result. That recall can itself log outside the folder, so it will not be repeated. No external coordination or memory mutation will be requested.

## Literature check, started about 21:08 UTC

Web queries: `"six-vertex" "Gaussian free field" "November" "2026"`; `"2611.00291" six vertex`; `"balanced six-vertex" "free energy" OpenAI`.

Search found the same September OpenAI manuscript and November Yan Ru Pei preprint already recorded by the earlier worker, with no newer resolution in these results. Opened the November PDF, September PDF mirror, and arXiv:2610.07454. Search snippets are not treated as proofs. The aim is to audit the specific auxiliary-state conditions, rather than stop merely because an unverified full-range claim exists.

## Independent recheck and choice (about 21:10 UTC)

The literature check took less than five minutes. Further queries `six vertex Gaussian free field November 14 2026 uniqueness Pei correction` and `"six-vertex" "2611" "Gaussian" convergence` returned no newer full resolution. The September PDF initially failed to open directly but opened by following its landing page's PDF link. Read Proposition 4.3, especially printed pp. 36–38; read the November paper's Corollary 1.6 and its proof (printed p. 28). The earlier main finding holds: the November identification is conditional on existence and minimisation, and its author expressly did not check these inputs. No SOLVED_ELSEWHERE.md is justified here.

Independent arithmetic check used `OMP_NUM_THREADS=1 nice -n 15 python3` with the standard library only. Effective nice was 20. At c=1,sqrt(2),sqrt(3),2 the pairs (Delta,K) were (0.5,1.909859317103), (0,1.273239544735), (-0.5,0.954929658551), (-1,0.636619772368). Computing K separately as 1/asin(c/2) and 2/acos(1-c*c/2) agreed to printed precision. Analytically, c=2 sin(theta) gives Delta=cos(2 theta) on the principal branches. Thus the earlier parameter conversion and normalization identity hold.

Choice: prove an elementary sector-pressure comparison by adding rows of weight one, then use entropy to turn pressure convergence into minimisation for every subsequential limit. This addresses the earlier report's O1/O2 target without relying on the September manuscript's open-row operator-norm bound. The planned comparison starts with a balanced torus of height 2n and inserts L-2n rows with all horizontal arrows left. It preserves weight and maps into the n-right-arrow sector of height L. Its precise consequence and all remaining pressure/uniqueness assumptions will be stated separately in PROOF.md. First check the surgery itself and try to find a seam or weight error before claiming the entropy consequence.

## Exact surgery checks (21:11 UTC)

The second construction uses four independently filled rectangles with identical boundary arrows. Reflect and reverse all arrows in the right and upper copies. Matching boundary arrows then glue to a doubly balanced torus. For a rectangle of area NL with free partition sum Zfree and fixed-boundary sums Zb, the proposed inequality is

`Zbal(2N,2L) >= sum_b Zb^4 >= Zfree^4 / 2^(6(N+L))`.

This gives a lower bound on balanced-strip pressure in terms of the variational pressure, with error `3 log(2)/H` at transverse size H. Together with row insertion, it should remove the need to assume the September rectangle norm bound or any Bethe-ansatz pressure formula for O2.

Created and ran `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 check_surgery.py`. Runtime about 0.15 seconds; effective nice 20; largest matrix dimension 20; standard library only. Exact integer results:

```text
row insertion: 72 exact comparisons PASS
reflection c=1 rectangle=1x1 sum_Zb^4=6 Zbal=10 PASS
reflection c=1 rectangle=2x1 sum_Zb^4=18 Zbal=82 PASS
reflection c=1 rectangle=1x2 sum_Zb^4=18 Zbal=50 PASS
reflection c=1 rectangle=2x2 sum_Zb^4=306 Zbal=1682 PASS
reflection c=2 rectangle=1x1 sum_Zb^4=36 Zbal=40 PASS
reflection c=2 rectangle=2x1 sum_Zb^4=648 Zbal=1312 PASS
reflection c=2 rectangle=1x2 sum_Zb^4=648 Zbal=920 PASS
reflection c=2 rectangle=2x2 sum_Zb^4=275088 Zbal=496736 PASS
reflection c=3 rectangle=1x1 sum_Zb^4=166 Zbal=170 PASS
reflection c=3 rectangle=2x1 sum_Zb^4=13778 Zbal=17042 PASS
reflection c=3 rectangle=1x2 sum_Zb^4=13778 Zbal=15090 PASS
reflection c=3 rectangle=2x2 sum_Zb^4=97614898 Zbal=110669586 PASS
one-vertex and 2x2 torus hand formulas PASS
```

Independent magnitude check: at one vertex Zfree=4+2c, sum Zb^4=4+2c^4, and the balanced 2x2 torus has transfer matrix [[2,c^2],[c^2,2]], giving Zbal=8+2c^4. Thus the four-copy inequality has the correct direction and a strict gap of 4 in this case. Tests at c=3 deliberately check that no disordered-regime hypothesis has slipped into these combinatorial lemmas.

## Proof and attempt to break it (about 21:15 UTC)

Wrote PROOF.md. The pressure comparison is unconditional: entropy's finite variational inequality and four-copy gluing give p_bal(H)>=p_c-3 log(2)/H. Row insertion then gives p_L(n)>=(H/L)p_c-3 log(2)/L for H=2 min(n,L-n). A separate fixed-block entropy argument proves that every local limit has pressure at least the limiting finite-torus pressure. It therefore attains p_c when n/L tends to 1/2. The only uniqueness assumption is in the final convergence corollary, not in the minimisation theorem.

Audits:

- Checked every boundary of the four-copy construction, including the periodically identified outer seams. Reflections alone do not suffice: the arrow reversal in each reflected block is essential.
- Verified the entropy inequality direction using the exact identity H+E log W=log Z. One must bound finite-torus entropy from above by fixed-block entropies to obtain a lower bound on the limiting state's pressure.
- Re-derived the coefficient three in the boundary cost both by Holder and by two Cauchy-Schwarz inequalities. The boundary count is 2^(2N+2L), its cubed logarithm is 6(N+L)log2, the doubled torus area is 4NL, and H=2L. This gives 3 log2/H, then 3 log2/L after row insertion.
- Caught and corrected a diagonal-selection detail: closeness of individual probabilities on an increasing box is insufficient with error 1/j. The proof now chooses total variation error below 1/j for the whole finite-box marginal, which controls every fixed smaller marginal.
- Allowed all translation-invariant laws in the pressure supremum. A proof only for ergodic zero-mean laws would leave the original state-identification issue unresolved.
- Checked c<1 by exact fractions and c>2 by integers. At c>2 the minimisation lemma still applies; uniqueness is neither asserted nor needed.
- The inner cylinder limit follows from primitive sector transfer matrices, including singleton extreme sectors. The near-balanced outer sequence eventually avoids the extreme sectors, so H>=2 in the bound.

Extended check_surgery.py to construct the actual maps, rather than just compare partition sums. Re-ran the same command. All previous checks passed, and the new output was:

```text
c=1/2 exact rational pressure comparisons PASS
direct four-copy gluing: 348 distinct images, all seams/fluxes/weights PASS
direct row insertion: 30 seam/flux/weight checks PASS
largest transfer matrix dimension=20
```

Runtime remained about 0.18 seconds. Resource reporting was added for the final run. This completes the chosen next step: O2 holds for every subsequential auxiliary torus limit; O1 follows if the cited unique-minimiser assertion is valid. No audit of that uniqueness proof or of the September correlation machinery is claimed.

## Final resource and report check

The final script run printed `peak resident memory bytes=14925824`, with runtime about 0.17 seconds and effective nice 20. Wrote REPORT.md with a PROVED verdict explicitly limited to the minimisation lemma. The proof requires no unverified literature theorem; only its optional uniqueness/convergence corollary is conditional on the November claim. All deliverables are in the current folder, and the earlier folder was read only. No git commands, publication, messages, or accounts were used. The startup recall caveat is recorded above rather than claiming that its internal hooks cannot write.

Final read-only consistency check: `rg -n 'VERDICT|O1|O2|total variation|uncertain|Next worker|Task:' REPORT.md PROOF.md LOG.md` confirmed the verdict, conditional uniqueness scope, corrected total-variation diagonal argument, and next-worker handoff agree. Completed at about 21:17 UTC, 14 November (01:17 Asia/Tbilisi, 15 November 2026).
