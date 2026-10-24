# NOTES - multiscale Fourier proof for star + rank one + eps W

Family: Q = a X_h^2 + 2 X_h (L + beta) + lambda (V + gamma)^2 + X'^T E X' + b^T X',
L = <w,X'>, V = <v,X'>, w,v orthonormal, max w_i^2, v_i^2 <= c, |lambda| >= 1, |a| < c,
E no c-pivot, ||E||_op <= eps.

## N1. The basic reduction (PROVED, elementary)

phi(t) = int f_h(x) e^{it(a x^2 + 2 beta x)} Psi_t(2 t x) dx,
Psi_t(y) = E exp(i y L + i t lambda (V+gamma)^2 + i t X'^T E X' + i t b^T X').
Fresnel in V (Lemma 2 of RESULTS): |Psi_t(y)| <= (4 pi |t lambda|)^{-1/2} K_t(y),
K_t(y) = sup_b' int |E exp(i <y w + xi v + b', X'> + i t X'^T E X')| dxi.
Hub step (f_h <= 1, y = 2tx): |phi(t)| <= (2|t|)^{-1} (4 pi |t lambda|)^{-1/2} J_t, J_t = int K_t(y) dy.
So ||p_Q|| <= (1/2pi)[2 + int_{|t|>1} ...] and everything reduces to controlling J_t.

## N2. Absorbing the in-span part of E (PROVED, algebra)

P = [w v]. X'^T P E P X' = e_ww L^2 + 2 e_wv L V + e_vv V^2. Complete the square in V:
lambda (V+gamma)^2 + e_vv V^2 + 2 e_wv L V + e_ww L^2 = lambda' (V + kappa L + gamma')^2 + sigma L^2 + (linear in L) + const,
lambda' = lambda + e_vv, kappa = e_wv/lambda', sigma = e_ww - e_wv^2/lambda'. |sigma| <= 2 eps, |kappa| <= 2 eps.
Direction v + kappa w: still spread, shear of the (y, xi) plane with Jacobian 1.
So WLOG the in-span part of E is sigma w w^T only. The e_vv, e_wv parts are harmless exactly.

## N3. The obstruction: no pointwise-in-t bound works in the in-span case (claimed; to verify numerically)

Take E = sigma w w^T, b = 0, a = 0, L, V approx Gaussian (spread w, v). Gaussian model:
Psi_t(2tx) ~ (2t sigma)^{-1/2} (2 t lambda)^{-1/2} exp(-x^2/(2 sigma^2)) exp(-i t x^2/sigma) for t sigma >> 1.
Choose f_h (density <= 1) = 1 on {|x| < 3 sigma, cos(t0 x^2/sigma + phase) > 0}, rest of mass far away.
Then |phi(t0)| >= c sigma^{1/2} |lambda|^{-1/2} / t0. Compare C t^{-3/2}: ratio (sigma t0)^{1/2} -> infinity.
So: NO bound |phi(t)| <= C |t|^{-3/2} holds uniformly over the family for t >> 1/sigma, and the natural
pointwise bound ~ sigma^{1/2}/t has a log-divergent integral. Also twist inflation J_t ~ (t sigma)^{1/2} is real.
Consequence: the in-span component sigma must be handled by an argument that averages over t (or real variable).
Uniform pointwise bound that IS true: Theorem D with k = 2 (decoupling h in J against half of X') gives
|phi(t)| <= C_2/|t| for the whole family (to check the marginal/volume details), hence alpha_2(Q) bounded.

## N4. KEY NEW IDEA: Strichartz / Tomas-Stein for the hub coordinate

Complete the square in L: 2 x L + sigma L^2 = sigma (L + x/sigma)^2 - x^2/sigma. Fresnel-linearize sigma(L + x/sigma)^2:
phi(t) = c_t int dy  g_h(-t kappa_h, kappa_h y + c'(t)) Psi^0_t(y),   |c_t| = (4 pi |t sigma|)^{-1/2}, kappa_h = 1/sigma - a,
g_h(s, tau) = int f_h(x) e^{i s x^2 + i tau x} dx (twisted ch.f. of X_h), Psi^0_t has NO sigma L^2 twist.
As t varies, g_h(-t kappa_h, .) sweeps the Fourier extension of f_h from the parabola:
  G(s,tau) = int f(x) e^{i(tau x - s x^2)} dx,   ||G||_{L^6(R^2)} <= C_S ||f||_2 <= C_S   (1D Strichartz; Foschi sharp const).
Dyadic window t in [T,2T], Holder L^6 x L^{6/5} in (t,y), change of variables (s,tau) = (t kappa, kappa y + c'):
  int_T^{2T} |phi| <= C (sigma lambda)^{-1/2} T^{-1} * kappa^{-1/3} C_S * T^{5/6} ||K^0||_{6/5}
                  = C' sigma^{-1/6} |lambda|^{-1/2} T^{-1/6} ||K^0||_{6/5}.
Sum over dyadic T >= T0: C'' (sigma T0)^{-1/6}. So the range t >= theta0/sigma costs O(theta0^{-1/6}): BOUNDED.
This is exactly the t-orthogonality that pointwise bounds miss; it resolves the in-span obstruction at high frequency.
Remaining: t <= theta0/sigma, where the in-span twist theta = t sigma <= theta0 is mild (needs a mild-twist lemma).

## N5. The Frobenius split - checked, correct for E_rest, FAILS for the in-span part

Lead: hub in J, Z_3 = e_3(A_IJ^T A_IJ) ~ ||E_IJ||_F^2, Theorem D tail over |t| >= 1/||E||_F is O(1), so only a
Frobenius-mild twist is needed at low frequency.
Check: M = A_IJ (h in J) = w_I (x) e_h + v_I (x) lambda v_J + E_IJ. The top-2 singular structure is a (x) b + c (x) d with
a = w_I, b = e_h, c = v_I, d = v_J. To first order the third singular value comes only from
  P^perp_{span(w_I, v_I)} E_IJ P^perp_{span(v_J)}   (tangent space of rank-2 matrices at M_0 is killed).
 - in-span part P E P = sigma w w^T + e_wv(...) + e_vv v v^T: column side in span(w_I, v_I) -> contributes NOTHING to Z_3.
 - cross part E_x = w z1^T + z1 w^T + v z2^T + z2 v^T (z_i perp w,v): IJ block w_I z1_J^T (killed) + z1_I w_J^T (counts) + ...
   so about half of ||E_x||_F^2 counts.
 - out part P^perp E P^perp: counts, about ||E_out||_F^2 / 4 for a random partition.
So Z_3 >~ c ||E_rest||_F^2 with E_rest = E - P E P (to be made exact), and the split works for E_rest.
For E = sigma w w^T (allowed: no pivot, ||E|| = sigma), Z_3 = 0 for EVERY partition and the pointwise obstruction N3 applies:
the Frobenius split cannot close the in-span case. N4 (Strichartz for the hub) is what closes it at high frequency.
The mild-twist lemma is still needed at low frequency, for BOTH E_rest (|t| ||E_rest||_F <= m) and the in-span twist
theta L^2 with theta = t sigma <= theta0.

## N6. Obstruction N3 confirmed numerically (num/n1_obstruction.py, n1b_obstruction_tail.py)

Gaussian limit (L,V) ~ N(0, I/12), Q = 2 X_h L + sigma L^2 + V^2, hub law chosen for each t0 (phase selection,
mass <= 1). t0 * max|phi(t0)| -> 1.43 sqrt(sigma) (sigma = 0.1: 0.453 at t0 = 163840) and 1.50 sqrt(sigma) (sigma = 0.02),
i.e. (1/pi) int|Psi(2 t0 x)| dx; t0^{3/2} max|phi| = 184 and growing like sqrt(t0). Uniform hub law: t0^{3/2}|phi| = 10.6 flat.
Status: NUMERICAL (Gaussian limit; for finite n by weak convergence at each fixed t0). No pointwise bound C t^{-3/2}
holds on the family; any proof must average over t in the range t >> 1/sigma, or use real-variable input there.

## N7. The twist lemma is FALSE in L^1 for bumpy laws - consequences

Reported (04_twist_lemma): for bumpy laws int |E e^{iu<v,X> + i kappa <v,X>^2}| du = infinity for every kappa != 0.
Consistent with the bump-shift heuristic: a bump of L at position l_k gets the local phase e^{2 i kappa l_k (l - l_k)}, which
translates its Fourier transform by 2 kappa l_k; spread positions -> the twisted transform is spread over |u| <~ 2 kappa R with
no product cancellation -> L^1 norm ~ (kappa R)^{1/2} -> infinity with the spread R.
What survives here:
 - N1 as an inequality (but J_t may be infinite when the twist has an in-span component; unclear for out-of-span twists:
   for S with S P = 0 the local frequency shift P^T (2 S p_k) vanishes, so the bump-shift mechanism is absent).
 - N2 (exact algebra), N3/N6 (obstruction).
 - N4 (Strichartz for the hub) SURVIVES and needs no twist lemma for the in-span part: sigma(L + x/sigma)^2 is linearised
   exactly; the twist-free slice integral K^0 is controlled for every law by BL (L^1 and L^infinity, hence L^{6/5}).
 - the Theorem H route at low frequency t <= theta0/sigma is DEAD for the in-span twist (bumpy laws), and the in-span
   compression must be handled at low frequency by something else (a real-variable step such as Prop 5.4 - but Prop 5.4
   needs the whole remainder to be a function of (L,V): an arbitrary linear term b_perp^T X' is NOT allowed there).
Plan: prove Strichartz lemma + high-frequency theorem; prove D_2 for the in-span case (exact rank 2, clean marginals);
corollary ||p_Q|| <= C (1 + log_+ 1/|sigma|) for E = P E P with ARBITRARY b; state precisely what is missing.

## N8. Lemma S checked (num/n2_strichartz_constant.py) and its elementary proof

Lemma S. f density <= 1, g(s,tau) = int f e^{i s x^2 + i tau x} dx. Then int int |g|^6 ds dtau <= 4 pi^3/sqrt 3 = 71.61.
Proof: |g|^6 = |g^3|^2, g^3 = Fourier transform (in (tau,s)) of mu = push-forward of f(x1)f(x2)f(x3)dx under
F(x) = (x1+x2+x3, x1^2+x2^2+x3^2). DF DF^T has det 12 r^2, r = dist(x, line R(1,1,1)); fibres are circles of radius r,
so the density of mu is m(u,v) = (1/(2 sqrt3)) int_0^{2pi} f(x1)f(x2)f(x3) dtheta <= pi/sqrt3. Plancherel on R^2:
int int |g^3|^2 = (2pi)^2 int int m^2 <= (2pi)^2 (pi/sqrt3) int int m = 4 pi^3/sqrt 3. (Same for |F| <= f complex.)
Numerics: uniform[0,1] 59.2; two far halves 15.9; bumpy 10 x 0.1 on [0,20] 4.8. All <= 71.6.
(The value 4 pi^3/sqrt3 coincides with Foschi's sharp Strichartz constant^6 at the Gaussian, with a different normalisation.)

## N9. Step R: real-variable small ball at scales delta >= |sigma| (PROVED, hub diagonal a = 0)

In-span case after N2: Q = 2 X_h (L+beta) + lambda'(Vt + gamma')^2 + sigma L^2 + Z, Z any linear form (+ const).
Q_1 := Q - sigma L^2 and Q_2 := Q - sigma (L+beta)^2 = 2X_h(L+beta) + lambda'(...)^2 + Z - 2 sigma beta L - sigma beta^2
are both in the Theorem H class (hub + exact rank one + ARBITRARY linear terms): density <= C_H = 7.56 |lambda'|^{-1/3}.
Fix s, delta >= |sigma|, Lam = sqrt(delta/|sigma|) >= 1.
 A = {|L| <= Lam}: |Q - Q_1| <= delta, so P(|Q-s|<=delta, A) <= P(|Q_1 - s| <= 2 delta) <= 4 C_H delta.
 B = {|L| > Lam, |L+beta| >= Lam/2}: given X' (lossless), Q is affine in X_h with slope >= Lam: P <= 2 delta/Lam <= 2 delta.
 C = {|L| > Lam, |L+beta| < Lam/2}: |Q - Q_2| = |sigma|(L+beta)^2 < delta/4, so P <= P(|Q_2 - s| <= 5delta/4) <= 2.5 C_H delta.
 => sup_s P(|Q - s| <= delta) <= (6.5 C_H + 2) delta for every delta >= |sigma|.

## N10. Combination lemma and THEOREM 2 (PROVED, a = 0, E = P E P, arbitrary b)

Combination: if sup_s P(|Q-s|<=delta) <= A delta for delta >= eta and int_{|t|>=1/(2eta)} |phi| <= B, then
||p_Q|| <= C_K A + B/pi (K even Schwartz, K^ = 1 on [-1/2,1/2], supp K^ in [-1,1]; mu = mu*K_eta + (mu - mu*K_eta),
the second has Fourier transform phi (1 - K^(eta t)) supported in |t| >= 1/(2 eta), the first has density
E K_eta(s - Q) <= A sum_k (k+1) sup_{|v|>=k}|K(v)| =: C_K A).
Strichartz window bound (N4, made exact): for t in [T,2T],
 |phi(t)| <= (4pi|t sigma|)^{-1/2} (4pi|t lambda'|)^{-1/2} int dzeta K_t(zeta) |g_h(-t/sigma, 2 t beta + zeta/sigma)|,
 Holder 6, 6/5; Jacobian (t,zeta)->(s,tau) is 1/sigma^2; ||K_t||_1 <= (4pi)^2, ||K_t||_inf <= 4pi (BL, det G = 1 for (w, v+kappa w)),
 ||K_t||_{6/5} <= (4pi)^{11/6}:  int_T^{2T}|phi| <= (4pi)^{5/6} C_6 |lambda'|^{-1/2} (|sigma| T)^{-1/6} = 16.8 |lambda'|^{-1/2}(|sigma|T)^{-1/6}.
 Dyadic sum, both signs: int_{|t|>=T0} |phi| <= 308 |lambda'|^{-1/2} (|sigma| T0)^{-1/6}.
THEOREM 2: a = 0, E = PEP (in-span, ||E|| <= eps0), any b, beta, gamma, any laws, any n: ||p_Q|| <= C absolute
(eta = |sigma|; if sigma = 0 Theorem H directly). This settles the sub-case the Frobenius split and the L^1 twist lemma
cannot reach (compression of E onto the hub direction + linear terms outside span(w,v)).
Strongest case against: Step R case B uses a = 0 (for a != 0 the hub's own vertex gives a sqrt singularity);
Strichartz uses the exact Fresnel of sigma(L + x/sigma)^2, valid for every law. To re-verify: constants, Jacobian, Fubini.

## N11. Window check (num/n3_strichartz_windows.py, Gaussian model, sigma = 0.1, lambda = 1; run hit 600 s after 13 rows)
int_T^{2T}|phi| for T = 5..1280: uniform hub 2.28, 1.38, 0.70, 0.35, 0.17; rough hub (cells 0.01) 1.25, 0.75, 0.50, 0.31, 0.21;
proven window bound 16.8 (sigma T)^{-1/6} = 18.9 ... 7.5 - never approached. For the rough hub max_t t^{3/2}|phi| grows
(5.1 -> 13.1), the pointwise failure of N3, while the window integrals keep decreasing, as Lemma S predicts.
RV Lemma 3.1 correction: nothing here uses a pointwise bound on |psi|; only Lemma 1 (L^p) and Lemma S.

## N12. Precise reduction for the full family (a = 0)
E = PEP + E_rest. Theorem 2's mechanism removes PEP completely. What remains:
 (a) no-in-span family Q_rest = 2X_h(L+beta) + lambda'(Vt+gamma')^2 + X'^T E_rest X' + linear: bounded density C_rest
     (needs: L^1 twist estimate for twists S with P S P = 0 at |t| <= M/||E_rest||_F, D_3 beyond; cross terms S = w z^T + z w^T
     DO shift bump transforms along w by 2 z^T p_k, so they are not obviously harmless for bumpy laws);
 (b) Z_3 >~ ||E_rest||_F^2 with admissible marginals (first-order computation N5; heavy rows -> J or condition);
 (c) Step R with Q_1, Q_2 in family (a): verbatim, gives small ball <= (6.5 C_rest + 2) delta for delta >= |sigma|;
 (d) tail |t| >= 1/(2|sigma|): D_3 alone if ||E_rest||_F >~ |sigma| (tail C (sigma^2/Z_3)^{1/4}); otherwise Strichartz with
     an L^{6/5} slice twist estimate for E_rest of strength t ||E_rest||_F <= M, and D_3 beyond M/||E_rest||_F.
So the whole family (a = 0) reduces to twist estimates for twists with NO in-span part, plus (b).
a != 0: only case B of Step R needs new input (vertex of a x^2 + 2 l x); Theorem H and the Strichartz bound are uniform in a.

## N13. Report
Constants re-checked: 16.8 = (4pi)^{5/6} C_6; 308 = 16.8 * 2/(1 - 2^{-1/6});
C_H = (3/pi) ((4pi)^{3/2}/2)^{2/3} |lambda'|^{-1/3} = 7.56 |lambda'|^{-1/3}; Jacobian |1 - a sigma|/sigma^2.
