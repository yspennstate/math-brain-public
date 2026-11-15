---
name: p0347_critical_beta_splitting_sackin_colless_non_gaussian_qc_limit_2026_11_12
description: "[VERIFIED] Aldous-Janson OP10 (P0347): balance indices of the critical beta-splitting tree DTCS(n) - Sackin/Colless variance kappa n^2 log^2 n and non-Gaussian; quadratic Colless/(n^2 log n) -> Q with all moments; full S/C law open"
metadata:
  type: project
status: verified
---
P0347 = Aldous-Janson Open Problem 10 (overview arXiv 2303.02529 §4.9): limit behaviour of the Sackin, Colless and
quadratic Colless indices of DTCS(n), split m -> (i, m-i) with prob m/(2 h_{m-1} i(m-i)).

Proved (Codex run, mini1 12 Nov; report + code in brain 06_math_research/referee_reports/2026-11-12/P0347/):
- E S_n = nL^2/(2 zeta2) + b nL + O(n), b = gamma/zeta2 + zeta3/zeta2^2; E C_n same with b - 2log2/zeta2; E QC_n ~ n^2 L.
  The overview's §4.9.1-2 toll claims are wrong (Colless toll is m - O(m/log m), not m/2).
- Var S ~ Var C ~ kappa n^2 L^2, kappa = (2zeta3 - zeta2)/zeta2^2 = 0.28057; limiting skewness 0.7240, kurtosis 3.9127:
  NOT asymptotically normal. (S - C) is o(nL) in L^2, Corr -> 1.
- QC_n/(n^2 L) -> Q in law with all moments, m_k rational by a recurrence (1, 13/11, 2457/1507, ...), m_k <= k!, so
  determinate; Laplace transform fixed-point characterization. Var QC ~ (2/11) n^4 L^2.
- Tool: transfer lemma for binary recursions with defect psi(p) = h_{p-1} for integer p (sub/super-solutions, no contraction).
Open: the limit law of (S - ES)/(nL) itself (only moments 2-4 + non-normality proved).

How it was checked (an agent): own exact recursions to n=16000 match Codex's 45-digit values to every digit;
variance/third-moment extrapolations land within 1-3 pct of the constants (narrow lever arm, corroboration only); every
rational and integral constant recomputed to 29+ digits. Literature 12 Nov: Kolesnik 2404.16021, Chorbadzhiyska-Minchev-
Savov 2608.18320, Heng Ma 2609.14329, BCM 2505.24821, INY 2510.17343 - none treats Sackin or Colless for this tree.
Referee 12 Nov (Codex P0347R, hard referee of Secs 3-8): MINOR. One wrong endpoint bound in Sec 4 (lower log terms need
an extra x^{j-1}; at p=2,j=1 the integrand tends to -1/2); local fix, nothing downstream moves. All else survived, incl. the
QC coefficient k m_{k-1} (not 2k) and uniqueness only within laws with an exponential moment. Archive: brain
06_math_research/referee_reports/2026-11-12/P0347R. Paper offered to an agent (mesh topic referee/p0347).
Related: [[lumping_r_merges_partial_one_block_lemma_k7_open_2026_11_12]].

**Full limit law, 12 Nov 22:30 laptop time:** a second Codex run (P0347L) proved (S_n-ES_n)/(n log n) -> W with all
moments, the same W for Colless (joint limit (W,W), Var(S-C) = O(n^2 log n)), a_k from h_{k-1} a_k = k a_{k-1} +
int R_k dnu, |a_k| <= 2^k k!, and a characteristic-function fixed point unique among centered laws with an exponential
moment. The hard referee P0347LR returned MINOR: the only change is the same endpoint bound P0347R asked for
(extra x^{j-1} term). Referee's fresh a_2..a_8 match the table. Archive: brain
06_math_research/referee_reports/2026-11-12/P0347L (proof) and P0347LR (referee). Watch-out the referee spelled out:
dropping the c=1 remainder before centering loses 3a_2 from the k=3 toll (a_3 would come out as a_3 - 2a_2).
