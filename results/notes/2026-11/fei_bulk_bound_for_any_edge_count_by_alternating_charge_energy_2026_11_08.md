---
name: fei_bulk_bound_for_any_edge_count_by_alternating_charge_energy_2026_11_08
description: "[PROVISIONAL] FEI T021 8 Nov 09:5x: the symmetric bulk cost is at most H_0 = 4.532 bits for ANY number of alternating edges, because int H|P|^2 = H_0 sum w^2 + alternating-charge energy, and the energy is <= 0 when the cosine coefficients H_m decrease (measured to m = 400, m H_m -> 2/ln2). The swap of averages is no longer needed."
metadata:
  node_type: memory
  type: project
  status: provisional
  modified: 2026-11-08T15:20:47.222Z
---

This closes the open many-edge bulk step that [[fei_bottom_band_mass_proved_by_noise_operator_alternating_sum_2026_11_08]] left (the swap of averages: the pointwise worst phase h(x, pi/4) beats 4.8723 for x < 0.38, so concentrated, phase-locked mass looked like it could break the bound).

- **Setup:** bulk mass at theta (x = sin^2(theta/2)) is |P|^2 d theta, with P = sum eps_i w_i e^{-i v_i theta}. Bound the cost by the worst phase, H(x) = max_Psi h, and expand H = H_0 + sum H_m cos(m theta).
- **Energy:** int H|P|^2 = 2pi[H_0 sum w^2 + (1/2) sum_{i != k} eps_i eps_k w_i w_k H_{|v_i - v_k|}].
- **Why the energy is <= 0 (unit weights):** fix an edge i and walk away from it in either direction. The signs alternate starting with minus, and the H_m decrease, so each one-sided series is <= 0. Hence the cost is <= H_0 = 4.53231 bits for every J.
- **Coefficients:** all positive and strictly decreasing, and m H_m -> 2/ln 2 = 2.885, the log singularity of H at x = 0.
  - **PROVED 8 Nov 10:0x (commit 56756837):** H = F/ln 2 with F = 2[ln 2 + Q(sin t) - Q(cos t)]/(1 - cos t) and Q(u) = [(1+u) ln(1+u) + (1-u) ln(1-u)]/2. This gives a_m - a_{m+1} = (8/ln 2) sum over odd j with 2j > m of q_j, where q_j = sum_{k>=j} C(2k,k-j)/(4^k k(2k-1)) > 0. That yields the blocks of four equal differences, and it matches the DCT to 4e-6.
  - pi/4 is the worst phase at every x, PROVED 8 Nov 10:1x (commit 5df8fa83):
    - Dc(A,B) = D(sqrt A, sqrt B) is a concave perspective, because k(u) = (1+1/u)ln(u+1) + (1-1/u)ln|u-1| - 2 ln u has k' = -ln|(u+1)/(u-1)|/u^2 <= 0.
    - So h = phi(p) + phi(1-p), with phi concave in p = sin^2 Psi, is largest at p = 1/2.
    - The unit-weight bulk bound now has no measured input.
- **Linear program:** the constraints int (D_M - 1) d mu <= 0, with D_M the Dirichlet kernel, push the LP max from 13.06 (M = 1) down to 4.547 (M = 256), tending to H_0.
- **Exact on the cube:** the M = 1 constraint holds exactly. The mean Fourier level of D is at least N/2, with equality iff no two edges are adjacent (total influence; a pair of edges at adjacent weights costs 4 instead of 1 + 1). Checked at n = 129.
- **Gaussian weights:** the bound is exact for A < sqrt 2 (up to H_m only being about c/m at small m), and H_0 + O_A(N^{-1/2}) beyond. Measured: random tables and climbs at N = 512 and 2048, A = 1 and 2, never exceed H_0.
- **Gaussian weights for every A, PROVED 8 Nov 10:1x (commit 3765ed4d):** for unimodal weights and a decreasing kernel, the alternating off-diagonal sum is <= 0.
  - Proof: write H_m as a positive mix of 1[m <= M], and layer-cake the weights. The superlevel sets are nested index intervals, and each row is an alternating +-1 run starting at -1 on each side, so it is 0 or -1.
  - Checks: 200k random instances and an exact rebuild.
  - This supersedes the A < sqrt 2 sketch above.
- **Many-edge saddle error, written out 8 Nov 10:2x (commit 848820b2a5c):** no Hilbert inequality needed.
  - Distinct integer edges within A sqrt N number J <= 2A sqrt N + 1, so the edge-by-edge triangle bound is relative O(e^{A^2} sqrt(J/N)) = O(N^{-1/4}).
  - D is exactly 2-homogeneous and C^1 with |grad D| <= 3.0435 |p|, so the cost moves by O(N^{-1/4}) I_1.
  - Then a Riemann sum to theta (sup |P|^2 <= J sum w^2, ||P'|| <= A sqrt N ||P||), and the bulk integral is at most half the circle integral, which is <= H_0 by the lemma.
  - Result: limsup sup Delta_1/I_1 <= 4.532 bits over all symmetric tables with edges within A sqrt n of the middle, any J.
  - Checked in sym_saddle_triangle_check.out: the summed error is always below the edge-by-edge sum, which falls as N^{-0.26}.
- **Still open:** the far regime (edges at distance of order n, measured to tend to 4 bits), a uniform finite-n bound, and explicit C(delta, A).

**Files:** sym_coulomb_lp/coeffs/weighted.py, sym_mean_level_exact.py, plus their .out files and RESULT.md section "alternating edges repel like charges". They are in the working folder and repo dir 06_math_research/frontier/T021/fei_sym_agent_2026_11_08, commit e51786e8.

**Why:** the pointwise picture said a table could concentrate mass at small x with phase pi/4. The alternating signs forbid it, because the mean-level constraint alone rules out mass concentrated at one small x.

**How to apply:** for a quadratic form in an alternating +-1 sum, expand the weight in a cosine series. If the coefficients are positive and decreasing, the off-diagonal part is a negative alternating-charge energy, and the bound is the single-term value.

- **Far-out square waves, measured 8 Nov 10:25 (commit 9074ae7ceae, sym_far_waves.out):** far from the middle the best table is a single window (3.80 at alpha 0.02 down to 2.99 at 0.4, n = 512), and adding alternating edges lowers it, the reverse of the centre. There is no pi/4 locking out there.
- **Far regime as a phase average, 8 Nov 10:4x (commit 8e3f1e9cbcf, sym_far_phase_avg/sup/coeffs.out):**
  - With (a_s, b_s) ~ A(cos Psi, rho cos(Psi - phi)), rho = sqrt(alpha/(1-alpha)), cos phi = (1-2x)/(2 sqrt(alpha(1-alpha))), the level phase drifts away from the middle (no quarter-turn lock), so the cost is the Psi-AVERAGE g(rho, phi) = <D>/K, K = (1+rho^2-2rho cos phi)/8.
  - Window moments follow rho cos phi and rho^2. The prediction matches exact thresholds to 0.04 bits at n = 256 and 512.
  - One far edge gives g_0(rho), which falls from 4 bits (rho -> 0, the OR value) to 2.886 (rho -> 1).
  - A cluster multiplies the I-mass by |P|^2 with weights rho^{-u} (monotone), which is the same charge form as the middle. So if the g_m are positive and decreasing, the cost is <= g_0 <= 4.
  - g_m is measured positive and decreasing to m = 120 for rho from 0.05 to 0.95, down to the 1e-6 quadrature noise.
  - sup_phi g is NOT enough: it passes 4.87 once rho > 0.13.
- **Far cost closed form, 8 Nov 10:4x (commit 23b22a2e9b4; measured in sym_far_closed.out):**
  - g = -[|1+u|^2 ln|1+u|^2 + |1-u|^2 ln|1-u|^2 - C]/|1-u|^2 nats, with u = rho e^{i phi} and C = 2(1+rho^2) ln 4 + 2 rho^2 ln rho^2. The c0 terms cancel by the parallelogram law.
  - It matches the quadrature to 1e-7.
  - A 2^16-point DCT, rho up to 0.995 and m up to 400, gives every resolved g_m > 0 and decreasing, with g_{m+1}/g_m -> rho.
  - So far clusters cost <= g_0 <= 4 bits, pending an analytic proof of the monotone coefficients. The middle piece -(|Q|^2) ln|1+u|^2 alternates on its own.
- **Far g_m monotone, PROVED 8 Nov 10:4x (commit 442d47f762d; closed form matches the DCT to 6e-8, measured):**
  - g_m = 2 rho^m h_m, with h_m = h_inf + 2 int_0^1 t^{m-1} w_m dt.
  - w_even = (1+s)t/((1+t)(1+st)) and w_odd = (1+st^2)/((1+t)(1+st)), where s = rho^2.
  - h_inf = 2[(1+s)ln(2/(1+s)) + s ln s]/(1-s) > 0.
  - h_{m+1} <= h_m term by term, so g_{m+1} <= rho g_m.
  - g_0 = 4[(1+s)ln(2/(1+s)) + (s/2)ln s]/(1-s) <= 4 ln 2 by convexity.
  - Far clusters therefore cost <= 4 bits, given two measured inputs: phase equidistribution and a uniform-in-phi I-profile for one far edge.
- **Far-edge I-profile uniform in phi, PROVED 8 Nov 10:54 (commit 96829a39fc0; checked by exact moments to n = 2048, measured):**
  - The I-mass is the layer spectral measure, and E[(N-2s)^k] = <e_u, J^k e_u>, where J is the Ehrenfest Jacobi matrix with entries about N r near u.
  - So the moments tend to r^k C(k,k/2), which makes x tend to 1/2 - r cos phi with phi uniform.
  - The excess over those moments halves with each doubling of n.
- **Far limit against exact sums to n = 8192, 8 Nov 11:0x (commit 9e5134a923e; measured):**
  - Thresholds oscillate around g_0. At n = 8192 the gaps are -0.0016, +0.0025, +0.0022 and -0.0218 bits at alpha = 0.05, 0.1, 0.2 and 0.3.
  - Plain doubles underflow above n of about 1500, so the sums use a log-space per-level pivot.
  - Correction: equidistribution only needs continuous test functions, since D and ((a-b)/2)^2 are each continuous and 2-homogeneous. The "unbounded per-level ratio" worry was wrong.
  - Route: two complex saddles rho e^{+-i phi} by steepest descent, then van der Corput (psi' != 0 away from x = 1/2).
- **Still open:** the far equidistribution written out in full (saddles plus van der Corput, only sketched), a proof that one far edge's I-profile is uniform in phi, the crossover sqrt n << |t - n/2| << n, a uniform finite-n bound, and an explicit C(delta, A).

- **Crossover sqrt n << d << n is the far regime with rho -> 1, 8 Nov 11:2x (sym_crossover*.out; measured plus an argument):**
  - The phase drifts eps/(2 sqrt(x(1-x))) per level, eps = 2d/n, so it makes about d/2 turns over the N levels while A and phi move on the N scale. Equidistribution needs only d -> infinity, and the far proof's other inputs are uniform in rho < 1.
  - One edge at t = n/2 - c sqrt n: ratio minus g_0(alpha) tends to 0 in every column c = 0 to 8 (n = 512 to 16384). At c = 0 it halves with each doubling of n; the largest gap, at c = 1, falls from 0.087 (n = 1024) to 0.022 bits (n = 16384). This is with the level-0 term included: the first table, pushed in bd20673bd18, left it out ([[a_fast_fourier_sum_dropped_the_level_zero_term_near_the_middle_2026_11_08]]).
  - The equidistribution step is written out in RESULT.md (Plancherel-Rotach, Fejer, van der Corput, error about d^{-1/3} with delta = d^{-1/3}, plus the Fejer eta). Two caveats: the uniformity of Plancherel-Rotach as alpha -> 1/2 is quoted, not checked, and the C^1 convergence of the I-profile is not proved.
  - Windows and square waves (J <= 64, spacing <= 8) with edges in the crossover stay <= 3.13 bits (windows at n = 1024 and 4096, where the worst at 4096 is 2.95; square waves at n = 1024), with level 0 included. They are flat in J because the rho^{-u} weights fall away from the middle.
- **Equidistribution measured directly, 8 Nov 12:2x (sym_crossover_equid*.out; measured):**
  - Restriction spectra are Krawtchouk in the level; the Pruefer phase Th under the phase-averaged I-share weight has |E e^{i m Th}| <= 1.1e-2 for m = 2..8 at n = 16384, c = 0.5..16, with |E2|, |E4| <= 1.5e-3 and d|E4| flat (O(1/d)).
  - m = 6, 8 have interior stationary levels (psi = pi/3, pi/4) and run at the van der Corput (m d)^{-1/2} rate, which step 3 already allows.
  - Spikes to 0.03 and 0.54 were the Pruefer amplitude dividing by sin^2 psi at the turning points (both of them), not a failure. The Airy-zone share falls ~ n^{-1/2} at fixed c.
  - Correction to step 4: the arcsine profile makes a delta' window at a turning point carry O(sqrt delta'), not O(delta'). Still o(1).
  - C^1 is not needed. Abel summation needs only TV(w) = O(max w), and a U-shaped w has TV <= 2 max. Measured TV/max is 1.04 to 1.89 (n = 1024 to 16384, c = 0.5 to 16) and settles, so the caveat is now "w is U-shaped on the band" (measured, not proved).
  - Shape counted, 8 Nov 12:4x (sym_equid_shape.out): w is a U with its minimum always at the middle level, plus a wiggle in the first ~20 levels (s = O(1), outside WKB). The variation beyond a pure U is 0.28, 0.12, 0.07 and about 0.03 of max w at c = 0.5, 1, 2 and >= 4, the same at n = 1024, 4096 and 16384. So TV(w) <= 2.3 max w on the tested range, which is all Abel needs. A WKB-flux sketch (R^2 beta sin psi constant) gives the U part. The bottom-edge wiggle and the variation of the Plancherel-Rotach remainder are not proved.
  - The wiggle is irrelevant, 8 Nov 12:5x (sym_equid_edge.out): levels s' < 20 carry 6e-2, 3e-2 and 1.5e-2 of the weight at n = 1024, 4096, 16384 (falls like n^{-1/2}, as arcsine predicts). Cut them with the trivial bound. Above s' = 40 the excess over a pure U is <= 0.034 max. What's left open is only the U part's remainder variation.
  - Li-Wong 2000 (abstract read 8 Nov 13:0x): uniform for lambda, nu in compact subsets of (0,1). The crossover has nu -> 1/2, which is interior, so it is covered. The edges are cut. A pointwise O(1/N) relative remainder gives TV <= O(max) over N levels with no derivative form needed. Only check left: confirm the theorem's error is relative to the envelope (abstract only so far).
  - Remainder measured, 8 Nov 13:1x (sym_wkb_flux.out; full text 403). The WKB flux R^2 beta sin psi has relative spread times N of 3.2 to 4.1 at eps = 0.2 and 16 to 27 at eps = 0.05, flat in n = 1024..16384 and c = 0.5..8. So the remainder is O(1/N) relative. Its TV/mean is 0.28 to 0.32 (eps = 0.2), also flat. That is a 1/N jitter summed over N levels, which is exactly the O(max) the Abel step allows.
  - Flux bound proved from the recurrence, 8 Nov 13:2x (sym_flux_identity.out, sym_flux_step_closed.out). For b_{s+1}y_{s+1} + b_s y_{s-1} = lam y_s, E_s = b_{s+1}(y_s^2 + y_{s+1}^2) - lam y_s y_{s+1} obeys E_s - E_{s-1} = (b_{s+1} - b_s)(y_s^2 + y_{s-1}y_{s+1}) EXACTLY. E drifts by delta cot^2 th, and G = E/sin th (cos th = lam/2b_{s+1}) cancels that drift: one step is delta cos(2phi)/sin^2 th + r, |r| <= 0.85 delta^2/sin^4 th (sampled; closed form matched to 3e-15). Abel plus Kusmin-Landau then give spread(log G) = O(1/N), uniform in d while sin th is bounded below. Measured: spread x N 1.85 to 2.0, proof bound x N 5.65 to 6.6, flat in n = 1024..16384. Li-Wong is no longer needed for the envelope. Still to write: the constant in the eta step and r as an inequality. The general lesson for any three-term recurrence: the adiabatic invariant is the frozen energy divided by sin th, not the energy itself.
  - Constants proved, 8 Nov 13:3x (sym_flux_rigor.out). For |delta| <= s^2/16: |r| <= 5.8 delta^2/s^4 (from q - p/2 - delta cos2phi/s^2 = -delta^2(cos^2phi/rho + c^2/2)/s^2 exactly) and |eta step| <= 4.4|delta|/s^2 (sin of the turn <= ||A-I||/(1-||A-I||)). Proven spread(log G) <= 2K(Dn/sigma^2)(5 + 8.8L/sigma^2) + 5.8Q/sigma^4 = 48/N at eps 0.2, for N >= 30, against 1.85/N measured. The envelope half of the crossover caveat is closed at finite n. Left: the edge-window share, so far measured as n^{-1/2}.
  - Edge windows proved and the crossover closed with a rate, 8 Nov 13:3x (sym_edge_transfer.out). The bottom-band bound [[fei_bottom_band_mass_proved_by_noise_operator_alternating_sum_2026_11_08]] gives exact edge mass <= 31.9 sqrt(eps) I_1 per side (the single-layer spectrum is level-symmetric, K_j(x) = (-1)^x K_{N-j}(x)). The phase-averaged w_s <= 2(e_s + e_{s+1})(s+2)/(s+1)/(1 - |c_s|), measured worst ratio 0.25. Relative phase TV O(1). Result: |E_w e^{imTh}| = O(N^{-1/3} log N) for fast m and O((md)^{-1/3} log) for slow m, for fixed c. Measured decay is faster (1/N, 1/d); the eps trade-off costs the 1/3. Watch out: the edge share is arcsine, 0.58 at eps 0.2, so the sqrt(eps) bound only bites at small eps.
- **Still open:** the far equidistribution written out in full (saddles plus van der Corput, constant uniform as rho -> 1, Airy matching at the turning point), a uniform finite-n bound, and an explicit C(delta, A). (The I-profile proof, item above, is done.)
  - Mixed tables, 8 Nov 13:5x (sym_mixed_tables_512.out): over 60 bulk+far tables at n = 512 the union's ratio never exceeds max(bulk, far); mixing often lowers it (up to 0.25 bits). A Lipschitz-on-the-unit-ball bound for D gives a change in Delta_1 of at most L(sqrt(M_u M_v) + M_v), which is o(I_bulk) once d >> sqrt(n log n); the window sqrt n << d <~ sqrt(n log n) is still open. Watch out: ratio_multi takes INTERVALS [a,b) in pairs, not edges; an odd edge count needs a leading 0.
  - n = 1024, 8 Nov 14:0x (sym_mixed_tables_1024.out): the same 61 tables give max excess +0.0000 bits again. The crude bound loses the window because the far flip is mostly COMMON MODE (f_0 and f_1 both flip on the tail, mass ~ sqrt n / c times I_far); a sharp bound must charge the common mode only through dD in the common direction at u, which is small away from the bulk edge. Not yet done.
  - Common/difference split, 8 Nov 14:1x (sym_mixed_commonmode.py, n=128/512): Delta_1 = sum C(N,s) D(p_s,q_s), D(p,q)=phi(p)+phi(q)-(phi(p+q)+phi(p-q))/2 vanishes on both axes. The far change is SECOND order, about -(0.2-0.9) M_v log2(1/M_v) I_bulk, and almost all common mode; the sqrt(M_u M_v) cross term is absent (700x smaller at c=3). M_v/I_bulk grows like sqrt n e^{-2c^2}/c, so inside the window the union's ratio moves AWAY from the bulk's (-0.09/-0.13/-0.21 bits at c=1.5, n=128/512/1024), always downward for one bulk edge. The window needs a SIGN lemma, not smallness: d2D/dp2 = -(2/ln2) ln(p^2/|p^2-q^2|) is negative when |q|<sqrt2|p|.
  - Sign split, 8 Nov 14:2x (sym_mixed_sign_128.out): the curvature-sign idea FAILED pointwise. Levels with |q|<sqrt2|p| hold 91-99 pct of the far flip's mass but their sum is sometimes positive; w is spread over levels 2..45 (c=1.5, n=128), not just s <~ c^2. The second-order size comes from first-order terms cancelling across levels (oscillation, Kusmin-Landau style), so a sign lemma for the window must be global.
  - Parity source of the sign, 8 Nov 14:3x (sym_mixed_firstorder_*.out, sym_mixed_rest_*.out, n=128/512): first-order L1 = sum C dD/dp w cancels 350x (n=128) to 2600x (n=512) at c=1.5; the Taylor w^2 term is ~180x too small. For ONE bulk edge at n/2 one restriction is the exact majority on N=n-1 points, so its coefficients vanish on every even level (p+q=0), phi loses its second derivative there, and rest_s = (w^2/2) log2(w^2/p^2) - 1.164 w^2 + O(w^3/p) < 0 when |w| < 2.24|p| [small-w form only; the exact condition is w/p >= -1, next bullet]. Those levels hold half the w mass and essentially all the change (n=512 c=2: -6.227e-3 vs model -6.279e-3, total -6.217e-3). Open pieces: |w|<~2|p| on the mass-carrying even levels, and L1 = o(log term). For the pair bulk [0,3] (no exact zeros) the change is first order and POSITIVE at c>=2.5 (+4.1e-6 I_b, n=512): no sign lemma for all bulks; there the far part's own larger ratio must carry the bound.
  - Correction to the bullet above, 8 Nov 14:4x (sym_parity_G.out, sym_mixed_parity_ratio_*.out): the condition is one-sided, not |w|<2.24|p|. D is exactly 2-homogeneous, so a parity level contributes p^2 G(w/p), G(t)=D(1+t,-1)-D(1,-1), G'(0)=4, and R(t)=G(t)-4t is <=0 for ALL t>=-1 (zero at 0 and -1), >0 only for t<-1 (w pushes p+w through zero). Measured: no overshoot for c>=1.5 at n=128/512, but least w/p at c=1.5 went -0.39 -> -0.88 from n=128 to 512; max |w/p| ~ n^(0.6-0.9) e^{-c^2}, so w/p>-1 needs c^2 >~ a ln n = the top of the open window. At c=1 61 pct overshoots. Next: n=1024 at c=1.5 (does it cross -1, and does the total change stay negative anyway).
  - n = 1024, 8 Nov 14:4x (sym_mixed_parity_ratio_1024.out, sym_mixed_rest_1024.out): the overshoot happens (c=1.5, level 8, w/p=-1.28, 12 pct of parity w mass at w/p<-1; level 4 has the largest |w/p| 2.02 but positive t; per level the one overshoot adds +1.19e-2 I_b vs -1.186e-1 from the rest, sym_parity_levels_1024_c1.5.out) but the parity remainder sum stays negative, -1.067e-1 I_b vs total change -1.073e-1, L1 cancels 5400x. The proof must weigh the overshoot levels (R(t)~4|t| for t<-1) against the rest, not exclude them.
  - Target reframed, 8 Nov 15:2x (sym_parity_levels_512_c1.25/c1.0.out, sym_parity_c1_512.out): at n=512 the parity remainder is -2.6e-2 I_b at c=1.25 but +0.138 at c=1 (overshoot s=2, t=-2.37), and the full Delta_1 change at c=1 is +0.266 I_b while the union ratio 2.8286 < bulk 2.8891. The lemma needed is Delta change <= r_bulk * (I_union - I_bulk), not change <= 0; parity mechanism covers large c, the influence slack small c.
