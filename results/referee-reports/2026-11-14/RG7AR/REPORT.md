# RG7AR - first-reader report, nonergodic-galton-watson-flow-rule

Reader: an agent, 14 Nov 2026 02:3x. Read on the queued PDF q4/nonergodic-galton-watson-flow-rule/final_ae7926d.pdf (8 pp, Zenodo 24149775), single author.

Paper: "A nonergodic flow rule with Galton-Watson stationary measure". Answers Lyons-Peres, Probability on Trees and Networks, Question 17.18 (= Lyons-Pemantle-Peres ETDS 1995, Section 10, Question 3) in the negative: for GW with p2 = 3/5, p3 = 2/5 there is an equivariant flow rule with GW stationary and an invariant set B of measure 1/2.

## Verdict: ACCEPT (no change needed)

## What was checked, line by line
- Fixed point: x - (3/5)x^2 - (2/5)(1 - (1-x)^3) = -(x/5)(2x-1)(x-1); roots 0, 1/2, 1. Correct.
- Lemma 1(b): g_v = 1/4 (two children) or 7/8 (three); mean 3/20 + 7/20 = 1/2; Psi multi-affine and the g_v independent given F_n, so E[q_{n+1} | F_n] = q_n. Correct.
- Lemma 1(c): pair law P(1,0) = P(0,1) = d/2; disagreement after AND = 2(1/4 - ((1-d)/2)^2) = d - d^2/2, after OR = 2(1/8 - ((1-d)/2)^3) = (3d - 3d^2 + d^3)/4; average (9/10)d - (3/5)d^2 + (1/10)d^3 = d(3-d)^2/10. Bound d(3-d)^2/10 = 9d/10 - d^2(6-d)/10 <= 9d/10 on [0,1]. Recomputed d_1 = 5/16 and d_2 = 1849/8192 exactly. Correct.
- Lemma 2: q_n locally constant so E, G Borel; sum E q_n(1-q_n) <= 5/2 gives the 0/1 limit a.s.; countable union over words for G; C(t) = f_k(C(t1),...,C(tk)) by continuity. Correct.
- Flow rule: S(t) nonempty in all four AND/OR cases; consistency, equivariance and Borel measurability argued; kernel (3.1). Correct.
- Lemma 3 and (3.2): conditioning independent subtrees on one-coordinate events; E[p(T,A) | K = k, c] = GW_r(A) on {f_k(c) = r}, so GW_0, GW_1 and GW are stationary. Correct.
- (ii): children in S(t) keep the root's colour, so p(t,B) = 1_B(t); mu equivalent to GW gives 0 < mu(B) < 1. Correct.
- (iii): on D = {K = 2, c = (r,r)} (GW_r-probability (3/20)/(1/2) = 3/10), alpha^2 = 1 - (1-alpha)^2 forces alpha in {0,1}; the GW invariant sets are the four unions of B, B^c. Correct.
- Remark 1: p2/2 + 3 p3/4 = 3/5. Remark 3 pivot means: colour 1: 2(3/10) + 1(3/10) = 9/10; colour 0: 1(3/5) + 3(1/10) = 9/10; equals the slope of (2.1) at 0. Correct.

## Literature
- LP book Prop 17.17, Question 17.18, Exercise 17.22 cited with numbers and the edition used; LPP 1995 Prop 5.2 and Section 10 Question 3.
- Johnson-Podder-Skerman (interpretations of tree automata), Aldous-Bandyopadhyay (endogeny), Holroyd-Martin, Rousselin 2018 placed against the result. Lean 4 and Mathlib cited for the checks.
- Search 14 Nov (OpenAlex: "flow rule Galton-Watson stationary measure ergodic" since 2016; citers of LPP 1995 since 2022): nothing else answers Question 17.18.

Recommendation for ResearchGate: post final_ae7926d.pdf as it is.
