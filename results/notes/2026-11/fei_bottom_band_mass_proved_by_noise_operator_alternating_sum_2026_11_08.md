---
name: fei_bottom_band_mass_proved_by_noise_operator_alternating_sum_2026_11_08
description: "[PROVISIONAL] FEI T021 8 Nov 09:1x: for every symmetric Boolean f, I_[m,2m) <= 9.33 sqrt(m/n) I_1, with no dependence on the number or place of the edges. The proof runs through the noise operator: <D,T_lam D> is an alternating sum of a unimodal Poisson-binomial law, so it is at most 2 max q, and max q <= 2/sqrt(1+4 sigma^2) by BMM 2022. The top end needs no mass estimate (cost <= 3 I_B + J_B)."
metadata:
  node_type: memory
  type: project
  status: provisional
  modified: 2026-11-08T14:16:05.497Z
---

The many-edge band bound that blocked the end levels of the symmetric FEI phase bound (see [[fei_restriction_step_on_symmetric_functions_stays_below_4_87_bits_2026_11_08]]) has a short proof. Let D = sum_i eps_i 1[|w| = x_i] be the derivative on {0,1}^(n-1), with alternating signs eps_i.

- **Identity:** sum_j lam^j W_j(D) = <D, T_lam D> = sum_i eps_i mu(x_i) sum_i' eps_i' q_{x_i}(x_i').
  - q_k is Bin(k, 1-p) + Bin(N-k, p) with p = (1 - lam)/2. It is Poisson-binomial, so log-concave and unimodal, with variance N p(1-p) for every k.
- **Alternating-sum step:** an alternating sum of a unimodal sequence at increasing points is at most 2 max. This is where the +-1 alternation enters.
  - With arbitrary weights the step fails, which matches the 09:0x concentration result.
- **Local bound:** BMM (Combin. Probab. Comput. 2022, Thm 1.1) gives max q <= 2/sqrt(1 + 4 sigma^2) for a discrete log-concave law.
- **Choice of lam:** lam = 1 - 1/(4m) gives C -> 4 sqrt2 e^(1/2) = 9.33. The measured constants are 0.27 to 1.41.
- **Top end:** Delta_B <= 3 I_B + J_B, with J_B <= delta/(1-delta) I_1 above level (1-delta)n. So the top needs no mass estimate.

**Checked:** sym_noise_band.py and sym_noise_band.out, in the working folder and repo dir 06_math_research/frontier/T021/fei_sym_agent_2026_11_08.
- The identity matches the exact integer spectrum to six digits at lam = 0.5, 0.9 and 0.99, on six tables (J = 1 to 32, n = 512 and 2048, including a far edge at t = 3).
- The largest share divided by the proved bound is 0.17.

**Pair inequality, proved 8 Nov 09:1x:** D(a,1) - ln(1+a^2) = g(a) has g' = 2h - 2a/(1+a^2), where h is the second difference of x ln|x| at a.
- h >= a(a - 2 ln a) >= a for a <= 1, and h >= 1/a for a >= 1.
- So g increases in |a| to 3, which gives D(a,b) <= b^2 (3 + ln(1 + a^2/b^2)).
- Checked at 40 digits in sym_pair_log_proof.out.

**Still open for the phase bound:**
- the level-1 term (needs ln(1/I_1) = o(sqrt n));
- the bulk saddle point, which assumes central edges.

The Krawtchouk envelope and the Foster-Krasikov lookup are no longer needed.

**Why:** the end levels were the open step of the phase bound, and the Cauchy-Schwarz route lost a factor J.

**How to apply:** for L^2 mass of a layer-supported function in low Fourier levels, try <D, T_lam D> with the landing law before any orthogonal-polynomial envelope.

**Status, 8 Nov 09:1x (RESULT.md, commit 17f0766c):** the phase bound limsup Delta_1/I_1 <= 4.532 bits holds for any fixed number J of edges within A sqrt n of the middle. The ends are proved here, the bulk comes from the uniform saddle point, and D >= 0 follows from g increasing. J growing with n is still open in the bulk only.
