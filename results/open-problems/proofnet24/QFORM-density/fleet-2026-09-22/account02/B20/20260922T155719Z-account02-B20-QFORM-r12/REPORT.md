# account02/B20 — high-window localization to physical collar or source-realizable cross banks

**Run:** `20260922T155719Z-account02-B20-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Proof closure and keeper / SYNTHESIS  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_REDUCTION_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

The sole target is the unrestricted statement: for every dimension, every family of independent real random variables with one-dimensional densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of absolute value at least one, prove one universal finite essential-supremum bound for the density of `Q=X^TAX`, or exhibit a target-valid counterexample. Continuity is separate.

No step below rotates the product law. No marginal density cap is promoted to a conditional cap after conditioning on a dependent statistic. The argument does not use the refuted law-uniform pointwise phase decay, unrestricted fiber supremum, fixed physical rank-three minor, one-triple rank-two aggregate, or absolute phase-Wiener shortcuts.

## 2. Newest assigned-partner result actually consumed

The newest completed compatible `account03/B20` package is run `20260922T154341Z-account03-B20-QFORM-r12`, canonical source `yspennstate/math-open-problems@eb7976d14c75a2a5945e03c6b947774e26fdebcb`, report blob `9a3ff19dcda874bb067e847b0dff44a9fd53f16a`.

Put `P = 1_{|A|>=1/64} = U U^T` and `H = { i : P_ii > 1/64 }`. The partner proves that if `||U_H^T U_H||op<=1/2`, then the full target form has a continuous density satisfying `||p_Q||_infinity<194`. Therefore every unresolved counterexample satisfies

`boxed: ||U_H^T U_H||op >1/2`.                                      (2.1)

This run uses (2.1) quantitatively.

## 3. High-window leverage already forces physical row energy

Functional calculus gives `A^2 >= (1/64)^2 P`. Hence for every `i in H`,

`A_ii^2 + ||A_{i,-i}||_2^2 = (A^2)_ii > 1/262144 = 1/512^2`.       (3.1)

Set `beta := 1/(512 sqrt(2))`. For a physical pivot row `a=A_ii`, `b=A_{i,-i}`:

- if `a=0` or `||b||>|a|`, then `||b||>beta`;
- if `0<||b||<=|a|`, then `|a|>beta`.

In the second branch put `K=||b||/|a|<=1`, `tau=(1+K)^(-2)>=1/4`, `S=C-bb^T/a`. The exact scalar-Schur congruence gives `s_2(S)>=tau`; if `|a|<tau`, then `s_3(S)>=tau`.

## 4. `QFORM-HIGHWINDOW-SCHUR-DESCENT-v1`

Let `C_* := 32768 sqrt(2)`. Assume `A` is a minimum-dimensional counterexample to cap `C_*` and `i in H` is diagonal dominated. Then

`boxed: |a|>=tau>=1/4,  s_2(S)>=tau.`                              (4.1)

If instead `|a|<tau`, then `S/tau` still has three singular values at least one. Minimality gives the residual `R=Y^TSY` a density cap `C_*/tau`. The completed dependence-safe square estimate

`||p_Q||_infinity <=4 |a|^(-1/2) ||p_R||_3^(3/4)`

and `||p_R||_3<=(C_*/tau)^(2/3)` yield

`||p_Q||_infinity <=4 sqrt(C_*)/sqrt(|a|tau)`.

This is at most `C_*` whenever `C_*>=16/(|a|tau)`. But `|a|>beta`, `tau>=1/4` give

`16/(|a|tau)<16/(beta/4)=32768sqrt(2)=C_*`,

a contradiction. Thus (4.1) holds.

## 5. Second-level Schur spectral localization

The completed Schur-window argument of account01/B20 uses, after setup, only the collar (4.1). Rerunning it with `P_tau=1_{|S|>=tau/64}` shows that if `max diag P_tau<=1/32`, then a physical cross block has `s_2>=13tau/64` and the dependence-safe square/ridge theorem gives `||p_Q||_infinity<180<C_*`. Hence a minimum counterexample satisfies

`boxed: max_j (P_tau)_jj>1/32`.                                    (5.1)

For such a `j`, spectral calculus gives

`boxed: max{|S_jj|,||S_{j,-j}||_2}>tau/512>=1/2048.`              (5.2)

Thus the diagonal-dominated half of the partner's high-window survivor is converted to a two-level physical localization collar.

## 6. Cross-dominated heavy rows give source-realizable banks

If `i in H` is cross dominated, then `||b||>beta`. Put `E=||b||^2`. The source-valid greedy split gives either:

1. a singleton `j` with `|b_j|>=sqrt(E)/2>1/(1024sqrt2)`, whose scaled original source has density cap `<1024sqrt2`; or
2. disjoint nonempty original-coordinate banks `J,K` with `E/4<=sum_J b_j^2<E/2` and `sum_K b_k^2>E/2`, whose aggregates are mutually independent (and independent of `X_i`) and have marginal density caps `<2048` and `<1024sqrt2`, respectively.

No conditional-cap claim is made.

If every heavy row is cross dominated, then using (2.1),

`sum_{i in H} ||A_{i,-i}||^2 >1/16384`.

Thus for `B=A-diag(A)`,

`boxed: ||B||_F>1/128.`                                            (6.1)

A random physical bipartition has expected cross Frobenius square one quarter of `||B||_F^2`; therefore some original-coordinate cut satisfies

`boxed: ||B[I,J]||_F>1/256.`                                      (6.2)

No cross-rank conclusion is inferred.

## 7. `QFORM-HEAVY-WINDOW-PHYSICAL-COLLAR-v1`

Every minimum-dimensional counterexample to cap `C_*=32768sqrt2` surviving the partner diffuse closure is forced into one of two explicit original-coordinate regimes:

**A. Diagonal-dominated high-window pivot:** a heavy row yields (4.1), then the Schur high window localizes as in (5.1), with the residual physical-row certificate (5.2).

**B. Cross-dominated high window:** every heavy row has universal cross export; at least one yields the singleton/two-bank source-realizable alternative above, and globally (6.1)-(6.2) hold.

This is a target-level reduction, not a full proof.

## 8. First unpaid universal implication

`QFORM-HIGHWINDOW-BANK-ENTANGLEMENT-v1` remains open. Under regime B, or the cross-row alternative after A, combine the universal source-realizable banks/cut with the current low-stable-rank and Schur structure to force either a disjoint hyperbolic-square aggregate, a paid physical `3x3` packet, a dependence-safe ridge/separator packet, or a direct smoothing estimate keeping the bank variables and all contaminating quadratic terms together. The remaining issue is entanglement, not lack of quantitative mass.

## 9. Status and sources

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`; continuity is inherited only in the partner diffuse branch.

Fresh protected control/correction snapshot: `yspennstate/math-research-brain@348305755fd2e9d68e27742f39da70d249a6a60b`, owner revision `2026-09-22.5`.
Newest completed partner used: account03/B20 `@eb7976d14c75a2a5945e03c6b947774e26fdebcb`.
Schur-window splice: account01/B20 `@42db8aea74161970fec7b53664e087875026c6cf`.
Previous B20 three-pivot theorem: `@2979c262e6ba9c4cef66314aabd714431f5e9c95`.
Previous B20 source-realizable bank lemma: `@4106b1e129be9007e16d9b7ba94b2415ba251f86`.
