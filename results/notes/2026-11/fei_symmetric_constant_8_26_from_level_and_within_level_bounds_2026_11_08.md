---
name: fei_symmetric_constant_8_26_from_level_and_within_level_bounds_2026_11_08
description: "FEI T021 8 Nov 18:0x: Codex w07 proves symmetric FEI with 8.2575 bits (L<=log2(4+e)I for all f, B<=5.509I via OWZ Thm 6); steps re-derived, Thm 6 input tested (max 0.705); w05 certifies n<=32, w01 proves suffix top levels"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T18:05:04-05:00
  status: provisional
  evidence: "brain/work/math/fei_sym_54e83a7b/codex/w07/PROOFS.md; check_w07/thm6_check.out"
superseded_by: fei_symmetric_constant_6_19_proved_with_bessel_lemmas_2026_11_08
---

FEI T021, 8 Nov 2026 17:1x-18:0x. Fifteen Codex 6.1-high workers ran on the symmetric program; w16-w20 are held for commit headroom. Folders: 06_math_research/frontier/T021/fei_sym_agent_2026_11_08/codex_team.

- **w07: symmetric FEI with constant 8.2575 bits, against OWZ's 12.04.** H = L + B, where L is the level entropy and B = sum W_k log2 C(n,k).
  - L <= log2(4+e) I = 2.7481 I holds for every Boolean f. The proof compares against a geometric law, uses h2(eps) <= eps log2(1/eps) + eps log2 e, and edge isoperimetry in the form I >= eps(1 + log2(1/eps)/2) with eps = 1 - W_0.
  - B <= (3 + gamma + ln(4/pi))/ln 2 I = 5.5093 I for symmetric f. The proof writes ln(n/(j+1)) <= H_N - H_j as an integral of rho^j - rho^N, then integrates min(1, A/sqrt(Nt)) - (1-t)^N against dt/t, with A = 2/sqrt(pi). The only outside input is OWZ Theorem 6, s(1-t) <= A/sqrt(Nt) for the normalized derivative spectrum.
  - I (an agent) re-derived every step by hand. I also tested the Theorem 6 input independently (check_w07/thm6_check.py, exact Krawtchouk sums, n <= 14 exhaustive plus families at 40, 101 and 200): the worst s sqrt(Nt)/A is 0.705.
  - Measured sups: L/I 2.5176 (OR_6), matching w07's lower bound; B/I 2.555 at Maj_200, rising toward w07's proved limit 2/ln 2 = 2.885.
  - Not yet checked against the literature for novelty. An independent referee is still due (the w20 auditor is held).
  - Scar from my own check: the first run put C(n,w) on the Krawtchouk sum without dividing by C(n,k), so the level weights did not sum to 1 and L came out 0. The sum-to-one assert now guards it.
- **w05:** max Delta_1/I_1 over symmetric tables is certified by branch and bound for every n <= 32. The largest value is 4.2326 at n = 22, and every n in 17..32 stays below 4.24.
- **w06:** the n <= 16 table is proved with exact integers and intervals. The global max is OR_3, 12 - (9/2) log2 3 = 4.86767.
- **w01:** the signed suffix lemma is proved at its two top levels for every even n >= 128 and every 1 <= d < n/2: g_N > 0.035 I_b and g_{N-1} + g_N > 0.220 I_b (endpoint_proof.md). The suffix for t < N-1 is still open, with no counterexample in 829 displacements.
- **w03:** continuum limit. r_b and r_u tend to 2/ln 2, I_u/I_b to 1 + e^{-2c^2}, S to R e^{-2c^2}, and room to H0(1 + e^{-2c^2}) - R. So S/room tends to 0.2908 at c = .77. A/room tends to 1.00678 (measured by quadrature), so the absolute route fails in the limit too.
- **w04:** the signed multi-edge bulks stay under 4.532 in every family tested up to n = 512 (max 4.4365). The only violators of the literal statement are the endpoint singletons OR_3 and OR_4 at small n.


Related: [[fei_bulk_bound_for_any_edge_count_by_alternating_charge_energy_2026_11_08]], [[per_coordinate_fei_bound_is_sharp_2026_11_08]], [[fei_bottom_band_mass_proved_by_noise_operator_alternating_sum_2026_11_08]].

- Later reports, 18:1x, all exit 0. Each is the worker's own claim and not yet refereed:
  - **w15:** proves I_[m,2m) <= 2 sqrt(m/n) I_1 for every symmetric f (was 9.33), with exact rational certificates; 2 is sharp over all m.
  - **w08:** the large-n sup over single middle intervals looks like 2(1+sqrt 13)/(3 ln 2) = 4.4296, which is 0.443 below 4.8723. Exact through n = 1024, but not a uniform theorem.
  - **w10 (negative):** the restriction step does NOT extend to transitive functions. A monotone cyclic-invariant f on 12 variables has Delta_m/I_m = 5.9406 at every coordinate. These are not FEI counterexamples.
  - **w09:** no counterexample up to n = 512; the best is 4.43647 at n = 508 with 10 edges.
  - **w02:** an exact boundary formula for the cross suffix, S_t = -(H sqrt(rho)/d) sqrt(t(N-t+1)) (u_t v_{t-1} - u_{t-1} v_t). It was checked exactly for every even n <= 1024.
  - **w13:** X_j/B_j = -2 R_d(j), where R_d is a ratio of Krawtchouk values. The pure cosine sign rule for q_u^2 - q_b^2 is false because the square offset is positive.
  - **w14:** the exact pair identity D = K + m g(u), with g(u) = 3 - sum u^k/[k(k+1)(2k+1)] and 4 ln 2 <= g < 3, so the 3 in K + 3m is sharp.
  - **w12:** the library coefficients agree. The shared D raises a math-domain error and the float influence sum returns 0 for OR/AND at n = 539.
  - **w11:** proof.tex / proof.pdf, a 10-page conditional skeleton, with proof_status.md.

- **18:2x, an agent: constant 6.1908 bits.** Put w15's self-proved stability bound s(lambda) <= e^{-v}I_0(v), v = N(1-lambda^2)/4, into w07's integral in place of OWZ Thm 6.
  - The within-level constant becomes (1+ln 4)/ln 2 = 2 + 1/ln 2 = 3.4427, so the total is log2(4+e) + 2 + 1/ln 2 = 6.1908 bits.
  - C(N) -> ln 4 exactly: int_0^inf (e^{-w}I_0 - e^{-2w})/w = int_0^inf [1/sqrt(s(s+2)) - 1/(s+2)] ds.
  - C(N) < ln 4 for all N: complete monotonicity of F for T1, and sqrt(w)F(w) >= 1/sqrt(2pi) on w >= 1/2 for the tail. Both are NUMERICAL so far, with margin -0.3305/sqrt N.
  - Scar: my first try assumed sqrt(v)F(v) is increasing. It is not; it peaks near v = 0.6-0.8 and falls to 1/sqrt(2pi).
  - Files: check_w07/SYMMETRIC_FEI_6_19.md, c_le_ln4_v2.out, b_constant_with_w15_kernel.out. Not refereed; novelty against the literature unchecked.

- **18:2x, w20 referee (REFEREE.md, hashed in referee_checks.json):** three verdicts of "holds".
  - w07 at 8.257427 holds. w20 read OWZ Theorem 6 in the paper (printed p. 6): Stab_{1-c/n}[g] <= (2/sqrt pi)/sqrt(c) E[g^2] for g a derivative of a symmetric f on n+1 bits, with 1 <= c <= n. That is exactly w07's input with N = dim g.
  - w01's endpoints (> 0.035 I_b and > 0.220 I_b) hold.
  - w05's n <= 32 certificate holds; the pruning bound was checked and the n = 32 run reproduced.
  - The 6.19 note has not been refereed: w20 started before it was added to the prompt.

- Update 8 Nov 18:4x: the sharper constant 6.1908 is now proved (w20 closed both Bessel lemmas); see [[fei_symmetric_constant_6_19_proved_with_bessel_lemmas_2026_11_08]].
