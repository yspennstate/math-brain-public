---
name: fei_p4_equivalent_forms_posted_2026_11_10
description: "[PROVISIONAL] FEI P4 'Four equivalent forms' posted? Yes, github.com/yspennstate/fei-equivalent-forms (10 Nov): H<=2B+2I-2Var, noisy upper sets, tilted integral with new H<=4I-2Var+2M(f), per-element predictor loss"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T23:48:08+02:00
  status: provisional
  evidence: ""
---

FEI paper 4, "Four equivalent forms of the Fourier entropy-influence conjecture", is public at
github.com/yspennstate/fei-equivalent-forms (commit f132524, 10 Nov 23:5x). Brain copy:
06_math_research/fei_papers_agent/p4 (main.tex, DERIVATIONS.md, code/check_forms.py), merged as 0b16fed1.

What it proves, with mu = fhat^2 and gamma(T) = I_T[f] = sum_{U >= T} mu(U) (KKLMS generalized influence),
H = A + B, A = E log2 1/gamma, B = E log2 gamma/mu:
- (a) granularity of derivatives (d_T f in 2^(1-|T|) Z) gives mu <= 4^(|T|-1) gamma^2, so H <= 2B + 2I - 2Var.
- (b) for fixed t < 1, A_t <= H <= A_t + I log2 1/(1-t), gamma_t = ||T_sqrt(t) d_T f||^2 (Gibbs against the thinned law).
- (c) B = (1/ln2) int_0^1 M_s ds/s with m_s nondecreasing; unconditional H <= 4I - 2Var + 2M(f), M = M_1. Whether
  M(f) <= C I for all f is open and would imply FEI (new to the paper, not in the Fable log).
- (d) I L <= sum E_i <= I L + I/ln2, L = per-element log-loss of the size-biased sample, plus a variational form.
- The chi_R translation (old form (e)) is only a remark: Lemma 2.2 of arXiv 2610.16069 already has it for H.

Scars from writing it: P1's converse (sum E_i <= C I => FEI) needs C uniform over all functions, so a per-function
bound like L <= log2(n/I) does NOT give H <= I(log2(n/I) + 3/ln2); and the equivalences are for the class only
(odd-support functions such as MAJ_9 have sum E_i = 0 with H/I = 2.14). Check P1's corollary number from p1/main.aux
(it is Corollary 5). Literature checked: KKLMS 1911.10579 uses I_T only as a tool; nothing seen states (a)-(d).

Related: [[fei_p3_variance_han_bound_posted_2026_11_10]], [[fei_p2_good_coordinates_posted_2026_11_10]].

