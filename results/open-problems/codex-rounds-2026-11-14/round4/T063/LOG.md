# T063 work log

Task: “take the NEXT checkable step on this problem, building on that work”; received 15 November 2026, approximately 04:32 Asia/Tbilisi (00:32 UTC).

## Orientation and literature check

Read both earlier REPORT.md and LOG.md files, the round 3 PROOF.md, and its complete check_surgery.py. The first folder has no proof or scripts. Only this folder may be changed: consequently the global mesh, checklist and brain logging commands, which write outside it, are not run. No git or subagents are used. Compute state read at entry: status warn, mode owner_away_open, CPU saturated; only tiny single-thread standard-library checks are planned, under nice -n 15.

Web search began around 00:33 UTC and finished within five minutes. Queries: `six vertex Gaussian free field Pei November 2026 2611.00291 uniqueness` and `six vertex Gaussian free field 2610.07454 full range`. Opened Yan Ru Pei, *Closing the identification step in the GFF limit: Uniqueness of the zero-slope six-vertex phase for -1 <= Delta < 1/2*, https://hexagonmath.org/pdf/2611.00291v1 (Hexagon identifier, not arXiv); and Emile Averous, Hugo Duminil-Copin, Tiancheng He, Piet Lammers, Ioan Manolescu, *Conformal invariance of the six-vertex model's height function*, https://arxiv.org/abs/2610.07454. No newer full-range proof was certified. Pei's identification still assumes O1 and O2; its uniqueness argument is not certified by this session. No SOLVED_ELSEWHERE.md is warranted.

## Independent re-derivation of the earlier result

Rechecked its analytic argument directly. Reflection in x followed by arrow reversal sends (r,s,b,t) to (s,r,1-b,1-t); the y counterpart sends it to (1-r,1-s,t,b). Both preserve r+b=s+t and the indicator r != s. Four fillings with common boundary fit in the displayed four blocks; opposite cuts are complementary, so both fluxes are balanced. The map is injective by cutting at the labelled block boundaries. Holder costs B^3 with B=2^(2A+2B), so for a doubled W-by-H torus the logarithmic loss is 3(W+H)log 2. Dividing by WH and then taking W to infinity gives exactly the earlier loss 3 log 2/H. The row insertion has unit weights and is injective. The entropy diagonal argument uses total variation of whole finite marginals and is valid. Thus the earlier main claim holds analytically, subject to a separate independent finite check to be saved below.

## Choice of one extension (before computation)

Prove a finite-volume bound with BOTH winding fluxes fixed near balance, and deduce free-energy minimality of local limits as both dimensions tend to infinity with arbitrary aspect ratio. This extends the earlier iterated cylinder limit. Let n be right arrows per vertical cut, m up arrows per horizontal cut, H=2 min(n,L-n), W=2 min(m,N-m). Target:

    log Z(N,L;n,m) >= WH p_c - 3(W+H)log 2,  W,H >= 2.

Use the earlier four-block construction, which balances both fluxes, then insert straight rows and straight columns. The independent check will enumerate edge assignments and polynomial coefficients, rather than reuse the previous transfer routine. It must check the actual insertion map, both fluxes, injectivity, and preservation of the number of c vertices. A square-block entropy argument should then give pressure convergence and maximal specific pressure for every local subsequential limit whenever n/L and m/N tend to 1/2. This requires no uniqueness theorem or Bethe ansatz input and makes no GFF claim.

## Exact independent computation

Created check_two_flux.py. Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_two_flux.py
```

Output:

```text
nice: setpriority: Operation not permitted
OMP_NUM_THREADS=1
effective_nice=20
all-edge versus solved-column enumeration: 6 shapes PASS
hand formula Z(2,2;1,1)=4+2c^4 PASS
gluing 1x1: images=6 polynomial={0: 4, 4: 2} target={0: 4, 4: 2} PASS
gluing 2x1: images=18 polynomial={0: 8, 4: 8, 8: 2} target={0: 12, 4: 24, 8: 2} PASS
gluing 1x2: images=18 polynomial={0: 8, 4: 8, 8: 2} target={0: 12, 4: 24, 8: 2} PASS
gluing 2x2: images=306 polynomial={0: 16, 4: 40, 6: 32, 8: 168, 10: 32, 12: 16, 16: 2} target={0: 36, 4: 288, 6: 192, 8: 376, 10: 64, 12: 32, 16: 2} PASS
independent four-copy image checks=348 PASS
two-direction insertion: 2296 map checks; 60 polynomial comparisons PASS
peak resident memory bytes=14663680
elapsed seconds=0.474
```

The priority warning is the same inherited-nice issue as before: the process is already at nice 20. No elevated-priority compute ran. The computation used less than 15 MB reported peak RSS, no arrays or workers. Polynomial keys are powers of c and values are exact integer coefficients; coefficient inequalities therefore hold simultaneously for every c>0. Source shapes 2x2, 2x4 and 4x2 were enlarged by zero, one or two rows/columns, with all four insertion direction choices. Largest enumerated target area was 16; larger map checks use only explicit small images.

Independent hand check of the earlier count: a 2x2 torus balanced in both directions has four configurations without c vertices and two with four c vertices, giving 4+2c^4. Summing over the other flux adds four configurations and gives the earlier singly balanced formula 8+2c^4. Thus the difference from the old count is exactly the second flux constraint. Direct edge enumeration and solving the ice recurrence agree on all configurations of six small shapes (including dimension-one degeneracies). This independently validates the prior surgery calculation rather than merely rerunning its implementation.

## Earlier script rerun

Also ran the unchanged earlier script read-only, with bytecode writing disabled:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T063/check_surgery.py
```

All its checks passed again: 72 insertion inequalities; 12 integer reflection comparisons; hand formulas; rational c=1/2 checks; 348 gluing images; 30 row insertions. Effective nice 20, peak RSS 15,319,040 bytes. The earlier main result survives both the analytic re-derivation and the independent enumeration.

## Proof completed and audit

Wrote PROOF.md with every step of the finite bound, entropy upper bound, simultaneous-limit argument, and local Gibbs property. The local Gibbs check is direct: a replacement in a bounded rectangle preserves both winding sectors because there are cuts disjoint from the replacement. Only after passing local cylinder identities to the limit is the full exterior sigma-field used. This avoids applying a variational theorem with unverified hypotheses.

Audited the load-bearing factors twice: Holder and two Cauchy-Schwarz applications give the same boundary exponent; substituting W=2A,H=2B gives 3(W+H)log2. Row flux arithmetic was checked separately on n<=L/2 and n>=L/2, and column arithmetic separately on m<=N/2 and m>=N/2. The cross of the two inserted strips has r=s equal to the row direction and b=t equal to the column direction, so it contributes weight one. W/N=1-|2m/N-1| and H/L=1-|2n/L-1| independently recover the limiting area factor. In the entropy estimate the uncovered fraction is at most k(1/N+1/L), which vanishes even for unbounded aspect ratios.

Cases deliberately checked: c<1 and c>2 (coefficientwise inequalities cover both); odd target dimensions; no insertion in one or both directions; imbalances of both signs; dimension-one small enumerations; and the distinction between singly and doubly balanced 2x2 partition sums. Extreme fluxes W=0 or H=0 are excluded from the finite bound, and near-balanced sequences eventually avoid them. c=0 is excluded throughout because the proof uses bounded log weights. The theorem does not assert that all subsequential equilibrium states coincide.

The same finite-volume extension also handles the original ensemble with only n prescribed: sum over m and retain the term m=floor(N/2). This gives the bound with W_N=2 floor(N/2), and the same entropy proof removes the earlier iterated-limit restriction altogether. W_N/N tends to one for odd as well as even N. Its vertical arrow mean is exactly 1/2 by reflection in x followed by reversal of all arrows, which preserves the prescribed horizontal sector. This corollary belongs to the same finite-volume result, not an additional uniqueness claim.

Second derivation of the reported check counts: gluing images total 6+18+18+306=348. The three insertion source sectors have 6,38,38 configurations at c=1. Seven enlargement choices and four direction pairs give (6+38+38)*7*4=2296 images. The area cutoff allows seven enlargement choices for 2x2 and four each for 2x4,4x2, so (7+4+4)*4=60 polynomial comparisons. The hand-balanced 2x2 formula is also the 1x1 gluing polynomial, giving an independent count of its six configurations.

## Final deliverables (04:39 Asia/Tbilisi)

Saved REPORT.md with the required PROVED verdict limited to the equilibrium theorem. Final read-only check used `rg -n 'VERDICT|boxed|tag\{17\}|2296|60 polynomial|Next worker|Task:|Conditioning on|No newer' REPORT.md PROOF.md LOG.md` and `ls -lh REPORT.md PROOF.md LOG.md check_two_flux.py`. Confirmed that the finite-volume bound, single-flux corollary, exact counts, conditional uniqueness scope and next-worker recommendation agree across files. The finite Gibbs conditioning is explicitly on the torus exterior, avoiding the artificial global dependence of a periodically extended finite configuration. All requested deliverables are present. No full-range GFF theorem is claimed.
