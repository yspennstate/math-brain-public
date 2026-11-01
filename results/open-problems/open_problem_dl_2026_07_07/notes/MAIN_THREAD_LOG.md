# Main-thread research log — full BLN campaign

## Session 1 findings (mine)

### F1. Worst-case-activation REDUCTION (clean, important)
The general-psi conjecture (worst case over Lipschitz psi) is EQUIVALENT to the
arbitrary-profile ridge-sum statement: there is a fixed 1-Lipschitz "pattern-universal"
psi* whose width-m class, intersected with {Lip <= L}, essentially contains ALL
{ sum_{j<=m} g_j(<u_j,x>) : Lip <= L } with arbitrary Lipschitz profiles g_j.
(Construction: psi* concatenates, over a countable dense set of finite patterns/spacings,
1-Lipschitz pattern blocks; any profile window appears at any scale via (s,b).)
=> Attack the activation-free class R_{m,L} = {m-ridge sums, Lip <= L, clipped}.
Also checked: no cheap DISPROOF via pattern-universal psi — 1-D min-gap pricing forces
Lip >~ n sqrt(d) for single-direction pattern tricks; multi-neuron cross-talk pays the
same min-gap price. And ANY function of a j-dim projection needs
Lip >= ~ sqrt(d/j) n^{2/j} (projection min-gap), which for j >= log n is ~sqrt(d/j) —
BELOW sqrt(n/j) iff n > d: so low-dim-projection families cannot beat caps; no disproof
from that direction either.

### F2. Zonal/Funk–Hecke framework (conventions fixed)
phi_l := sqrt(N_l) G_l orthonormal in L2(nu_d) (projection law); ridge g(<u,x>) has
level components ghat_l phi_l(<u,.>); ||f_l||_{L2(S)}: level Gram of zonal features
Gamma_l = (G_l(<u_j,u_k>))_{jk}; Lip forces the JOINT ellipsoid
sum_l lambda_l ||f_l||^2 <= L^2, lambda_l = l(l+d-2).
Dual-norm identity: sup over the ellipsoid of sum_i y_i f(x_i) =
L sqrt( sum_l lambda_l^{-1} W_l^T Gamma_l^+ W_l ), W_{jl} = sum_i y_i phi_l(<u_j,x_i>),
and W in range(Gamma) automatically.

### F3. CRITICAL CORRECTION (a trap I fell into and killed)
For FIXED poles, E_x tr(Gamma^+ Sigma_hat) = n rank <= nm gives a sqrt(d/log d)-BETTER-
than-conjecture bound — CONTRADICTS the verified cap construction. Error: the sup over
pole configurations must be taken BEFORE expectations; the cap construction puts poles
AT the data. So the pole-sup is irreducibly where the complexity lives; per-level
decoupling of poles is fatally lossy at high l (zonal sup-norms sqrt(N_l)); the
|f|<=1 value constraint couples levels (aligned stacks = caps) and cannot be dropped.
Any correct proof must handle the pole-sup jointly across levels. This is the
majorizing-measure-hard core of BOTH gaps.

### F4. Mollification split (usable, pointwise, probability-free)
f = f*eta_h + (f - f*eta_h), h = eps/(8L): high part <= Lh = eps/8 POINTWISE kills its
correlation contribution deterministically; mollification preserves ridge sums
(Funk–Hecke); low part is bandlimited-ish to l <~ L/eps. Use to truncate levels.

### F5. Route to Deliverable (A) [general psi, polylog allowed] — STRATIFIED NORMAL FORM
Cancellation demon lives only in clustered-direction configurations. Program:
quantitative stratification: every f in R_{m,L} is u-close (sup on sphere) to a normal
form from a stratified dictionary: strata = cluster patterns; per cluster of size k, the
finite-differences either (spread <= s0) collapse to the LIMIT family — profile-derivative
x polynomial-factor units P(x) h(<u,x>) with TAME profiles (|h| <= C L, Lip(h) <= C L,
forced by Lip of f — proved for the k=2 limit; needs induction for general k) — or
(spread >= s0) Vandermonde-invert with profile bounds L (C/u)^k, which enter entropy only
through log(profile scale) => total entropy ~ (m d + m^2) log(C m L /u).
Consequence via existing machinery: general-psi law up to polylog for m <= d polylog;
for m > d the m^2 term degrades the bound to sqrt(nd/m^2 log) — partial regime.
CRUX LEMMA to prove: the cluster dichotomy with poly(m) (not exp) tame constants,
i.e. "u-approximation by stratified normal forms with profiles bounded by poly(m) L
(C/u)^{cluster size} and the limit-stratum tameness lemma".

### F6. Honest state of the log (Part 1)
Dudley cannot remove it (parametric entropy, real aspect ratio sqrt(d) or md).
The l2/ellipsoid heuristic says the truth is log-free; the proof needs the pole-sup
handled by generic chaining on the mixed body {joint level-ellipsoid + value bound}.
S1 is attacking; also watching S3 for the possibility the log is NECESSARY
(complexity lower bound via Sudakov + a 2^{md log} separated family => conjecture FALSE;
that too would resolve the problem).

## F7. THE BAND REDUCTION (session 1, main thread — the sharpest finding so far)
Combining what we already have with two observations localizes the ENTIRE log-removal
problem to a polylog-wide band of widths:
 (i) TRIVIAL FLOOR: any interpolant of +-1 labels on pairwise ~sqrt2-separated points has
     Lip >= sqrt2 (one opposite pair). For n <= e^{cd}, ALL pairs are ~sqrt2 apart, so
     min-distance floors give exactly sqrt2 and no more.
 (ii) Our proven bound sqrt(n/(m log(mnd))) BEATS c sqrt(n/m) whenever sqrt(n/m) >= sqrt2 *
     sqrt(log), i.e. m <= n/(C log(mnd)).
 (iii) For m >= n/2: sqrt(n/m) <= sqrt2 = trivial floor. DONE there.
 => THE ONLY REMAINING REGIME for the log-free conjecture is the band
        m in [ n/(C log(mnd)),  n/2 ],   where  sqrt(n/m) in [sqrt2, C sqrt(log n)].
 In this band, rigidity forces ALL canonical coefficients |alpha_k| <= 2L <= C sqrt(log n):
 a width-~n net of uniformly TINY units. Reformulated target:
 BAND LEMMA (wanted): for m in [n/log^C n, n/2], whp over (x,y), no width-m ReLU net with
 Lip <= (1/100) sqrt(n/m) fits n iid +-1 labels (exact or below noise floor).
 First attacks tried: l1-counting (sum_k S_k >= n/2L) — satisfiable, too weak; joint-energy
 (n <= ||alpha||_2 sqrt(n lambda_max(Gram-hat))) — needs lambda_max of ADVERSARIALLY-chosen
 m ReLU features on the sample ≲ (n/m) polylog^{-1}·..., i.e. the empirical-Gram battle in a
 concrete bounded regime. This is now the single crux of Part 1.

## F8. Two-mechanism picture for Part 2 (general psi)
Tame/spread configurations: parametric entropy => our sqrt(n/(m log)) machinery.
Cancellation configurations: few-dimensional-projection families with nonparametric 1-D
profiles; their FITTING floors (k-dim min-gap: sqrt(d/k) n^{2/k}) exceed sqrt(n/m) except
in wide/moderate regimes; the 1-D nonparametric entropy (Lambda A / u, LINEAR in Lambda)
is the obstruction to naive stratified covering (per-profile Lipschitz can reach L/spread).
Naive stratified normal form gives only cube-root-type partial bounds. The correct
formulation must charge each cluster EITHER parametric cost (spread) OR its projection
floor (collapsed) — a decomposition theorem, not a covering theorem. Status: open, main
thread continues.

## F9. BAND MIRACLE: polylog losses convert to a d-condition (session 2)
In the band (m = n/T, T <= log^C, L = sqrt(T)/100, target correlation eps n), the joint
across-level Cauchy-Schwarz gives
   sup <= L sqrt( sum_{l<=Lambda} lambda_l^{-1} ||P_{V_l(U)} T_l||^2 ),
and IF ||P_{V_l(U)} T_l||^2 <~ n m polylog uniformly over poles U, then
   sup <= (sqrt T/100) sqrt(n (n/T) polylog / d) = (n/100) sqrt(polylog/d) <= eps n/8
   PROVIDED d >= polylog(n)/eps^2.
I.e. IN THE BAND, every polylog loss is absorbable into a hypothesis d >= polylog — the
rate never degrades. The log-free conjecture in the band therefore needs only a
POLYLOG-ACCURATE (not sharp!) uniform bound on the projected multiplier norms.

## F10. Heat-kernel dual split (clean form of F4)
<f, mu_y> = <f, e^{tDelta} mu_y> + <(I - e^{tDelta}) f, mu_y>; second term
<= n ||(I-e^{tDelta})f||_inf <= C n L sqrt(t) = eps n/8 at sqrt(t) = eps/(8CL) —
pointwise, probability-free. First term: heat multiplier e^{-t lambda_l} truncates to
l <= Lambda ~ sqrt(T)/eps in the band (given d >= T/eps^2). So only LOW levels remain.

## F11. The one remaining analytic battle (precisely stated)
The plain energy-ellipsoid dual bound LEAKS at single-zonal spikes (h with a pole at a
data point: <y-atoms, h> ~ sqrt(N_l) = d^{l/2}, allowed by the ellipsoid but FORBIDDEN
to the primal class by ||f||_inf <= 1 — the clip constraint cannot be dropped). Dual/
support-function routes waste the y-randomness. The correct final object:
   E_y sup { sum_i y_i f(x_i) :  f_l in V_l(U) some U, sum_l lambda_l ||f_l||^2 <= L^2,
             ||f||_inf <= 1,  l <= Lambda }   <=  eps n / 8,
i.e. a MULTIPLIER EMPIRICAL PROCESS over a clipped, rank-m-per-level, energy-ellipsoid
class with FEW levels (Lambda = polylog) and slack d >= polylog. Weapons (S4 imports):
Mendelson multiplier bounds (1410.8003) + small-ball Gram lower isometry (1312.3580) +
KMR chaos over the pole manifold (1207.0235, gamma_2 ~ sqrt(md), log-free) + van Handel
chaining-convexity for the ellipsoid-times-clip body; clip = 1-Lipschitz contraction
(apply contraction AFTER chaining the bounded class, not before — pre-clip spikes have
huge empirical norms; chain the clipped geometry itself).
NOTE the two-sided consistency check: width-m caps fit exactly m points => correlation
m = n/T < eps n for T > 1/eps: caps do NOT fit below the noise floor in the band — the
band lemma is consistent with all known constructions. S3 (running) probes for smarter
constructions; if one fits in the band at L ~ sqrt(T)/100 the conjecture is FALSE instead.

## F12. One machine, two modes (architecture of the final proof)
Mode 1 (crude, polylog losses OK): all widths m <= n/log^C — zonal rank + Dudley +
chaos-Gram — gives sqrt(n/(m polylog)) for EVERY Lipschitz activation (Deliverable A,
replaces PL-only machinery below the band; the PL theorem already covers this regime too
but only for PL psi).
Mode 2 (band, losses -> d-condition): the F11 process bound — closes BOTH parts in the
band. Total: full conjecture for all m, all Lipschitz psi, log-free, under d >= polylog(n)
— then examine whether the d-condition can be relaxed to the conjecture's literal regime.

## F13. Band geometry (session 2, cont.) — what the winning argument must respect
In the band (m = n/T, L = sqrt(T)/100, d >= C T log n):
 - A height-Theta(1) local structure has cap radius >= 1/(2L) ~ 50/sqrt(T) (FAT cap), whose
   measure e^{-cd/T} < 1/n: whp it contains AT MOST ONE data point. So full-height local
   fitting commits one unit-group per point: correlation from height-1 caps <= #groups <= m.
   Consistency: caps achieve exactly m; the class should not beat ~m + sqrt(n) polylog.
 - Mid-sphere ("slab") units are FAT (slab width 1/L >= 1/sqrt(T) >> 1/sqrt(d)): touch ~n
   points but act on them through a 1-D profile with Lip <= 2L: per-unit beyond-chance
   sign gain is bounded by run-counting (#sign-runs <= 64 per unit at height 1/32).
 - FAILED-route ledger (all verified to leak, with reasons):
   (a) per-unit l1 (sum_k |alpha_k| |<y,phi_k>|): ignores gradient cancellation constraint
       -> m sqrt(n d log) — garbage;
   (b) plain rank/linear-space projection (dim m(d+Lambda) >= nd/T >> n): clip dropped -> vacuous;
   (c) population energy/Poincare: cannot see spiky/local units (population mass e^{-cd/T});
   (d) dual/support-function of ellipsoid: leaks at single-zonal spikes (clip dropped);
   (e) heat-split + per-level Cauchy-Schwarz: correct skeleton (F9/F10) — reduces everything
       to the projected-multiplier bound ||P_{V_l(U)} T_l||^2 <~ nm polylog UNIFORMLY in U,
       which is where clip+rank+Lipschitz must combine (F11).
 - The winning argument must simultaneously use: rank (m units), clip (|f|<=1), rigidity
   (|alpha| <= 2L), and the fat-cap/1-point geometry. None suffices alone; all four are
   available. Most promising concrete formulation: split units by slab occupancy n_k:
   "local" (n_k <= polylog: commit <= polylog points each: total m polylog — need T >= polylog^2)
   vs "global" (n_k large: 1-D profile machinery: total sqrt(n) polylog per unit-BUNDLE via
   joint 1-D chaining, not per-unit). The bundling of global units (many units, few effective
   directions at slab-resolution 1/L: directions within angle 1/(L sqrt(d)) act identically
   on data whp => effective direction count N_eff = covering of sphere at 1/(L sqrt(d)) ~
   (L sqrt d)^d?? — no: at EMPIRICAL resolution the relevant covering is of the data's
   projection sigma-algebra... to develop) is the next concrete lemma to attempt.

## F14. Band weapons (session 3): occupancy, serving capacity, and the fitting identity
New quantitative levers, all elementary and PROVED-level (write-ups pending):
 (a) OCCUPANCY LEMMA. Whp over the data, for EVERY u, t simultaneously:
       #{i : <u, x_i> >= t}  <=  Op / t^2,   Op := lambda_max(sum_i x_i x_i^T) ~ (1+sqrt(n/d))^2.
     (Proof: N t^2 <= ||X u||^2 <= Op. Tight: u = normalized average of k points gives
     depth ~ 1/sqrt(k).) For d >= n: Op = O(1).
 (b) UNIT VALUE-MASS. S_k := sum_i ramp_k(x_i) <= min( sqrt(n Op), Op / t_k ) — integrate (a).
 (c) l1-CLOSURE ZONE. Per-unit correlation <= 2L S_k; summing over m units handles ALL units
     with t_k >= C Op / sqrt(T) (contributes <= n/64). Battle zone left: mesoscopic units
     t in [c sqrt(log n / d), C Op/sqrt(T)] — population-invisible (mass <= (nd)^{-c}) yet
     high-occupancy (up to ~ d/log n points).
 (d) FITTING IDENTITY (sharpens the target). MSE <= 1-eps forces
       sum_i ( y_i f(x_i) - f(x_i)^2/2 ) >= eps n / 2,
     and each summand is <= 1/2, so >= eps n/4-ish points must be SIGN-CORRECT at height
     >= eps/4. Target restated combinatorially: whp NO class member sign-matches eps n/4
     random labels at height eps/4.
 (e) SERVING CAPACITY. A single unit can lift at most N(1/(64L)) <= C Op T points to height
     1/32 by itself => single-domination fitting <= C Op n total — right SCALE, constants
     ~50 Op short; and k-fold stacking evades it at cost k (shallow rims are wide) BUT
     stacked same-sign overlapping caps fight the clip |f| <= 1 — the stacking-vs-clip
     tension is not yet quantified. This is the current front line.
 (f) The remaining irreducible piece = adversarial multiplier bound for mesoscopic ramps:
       E_y sup over mesoscopic (u,t) configs of sum_k alpha_k <y, ramp_k(X)> under
       Lip+clip+rank — exactly S1's assigned battle. All other zones (local via (c),
       high-frequency via heat split F10, bulk-population via ellipsoid) are closed or
       closable with current tools.

## F15. THE EXTREMAL ATTACK AND ITS SATURATION (session 4 — decisive orientation)
Identified the extremal fitting mechanism in the band and computed its exact yield.
 AIMED SAME-SIGN CLUSTERS: pick k same-sign points, aim u at their normalized average
 (depth ~ 1/sqrt(k) each); for k <= k* ~ sqrt(d/log n) the cap catches ONLY its targets
 (whp over data, uniformly over all n-choose-k subsets, for d >= C k^2 log n). A single
 unit of Lipschitz alpha ~ L serves k <= (L/h)^2 points at height h. With m units the
 total correlation is
     served x height  <=  m (L/h)^2 h = m L^2 / h,   capped by served <= n at the
 crossover h_0 = sqrt(m L^2/n)  ==>  max correlation ~ 2 L sqrt(m n).
 So the cluster attack yields correlation Theta(L sqrt(mn)) — i.e. it FITS (correlation
 eps n) exactly when L ~ eps sqrt(n/m): THE CONJECTURED RATE, log-free, with the cluster
 constant. Strong evidence the log-free conjecture is TRUE and that the sharp constant
 comes from cluster serving.
 UPPER-BOUND STATUS (what is still missing): matching upper bound sup <= C L sqrt(mn) +
 sqrt(n) polylog + m over the WHOLE band class. Verified consistency of the candidate
 l2-across-units bound (needs sum_k W_k^2 <= eps^2 n / (C c^2)) with the cluster attack;
 it FAILS only when clip is dropped (m units stacked on one giant cluster). Cancelling
 stacks waste correlation proportionally (no free lunch there); partial-overlap ledgers
 are legitimate but each unit still pays serving capacity. MISSING GLUE, precisely: a
 clip-aware charging argument / BUMP DECOMPOSITION:
   every band member f = (signed near-disjoint local bumps) + (population-visible part)
   + (1-D slab parts), with  sum over bumps of height^2 x (points served) <= C m L^2.
 Given that, correlation <= sqrt(sum h^2 k) sqrt(sum k) <= sqrt(C m L^2) sqrt(n) = C' L
 sqrt(mn) and the band lemma closes, hence the full log-free ReLU conjecture; and the
 machinery (rank/occupancy/serving) is activation-free, so plausibly the FULL conjecture.
 Also settled en route: the affine part in the band: population separation gives
 ||v|| <= L + 2L sqrt(m p_max) + (visible-sector ellipsoid) — the affine/visible sector
 closes with existing tools; only the invisible mesoscopic sector needs the bump lemma.

## F16. CORRECTION TO F15 (S1's pile-up finding, verified reasoning)
F15 overstated the cluster attack. At NON-data points aligned with sums of unit directions,
up to K ~ k units are simultaneously active and gradients add incoherently: Lip(f) >=
alpha sqrt(K). Redo: a unit serving k targets at height h suffers alpha <= L/sqrt(k)-type
pile-up constraints; optimizing (any t) gives serving k <= C L/h per unit (LINEAR, not
(L/h)^2), so total attack correlation ~ C m L — INDEPENDENT of height. In the band this is
c n/sqrt(T) << eps n: the best known attacks are a factor sqrt(T) BELOW the conjectured
threshold. Consequences: (i) the band lemma is very plausibly true with room; (ii) the
conjectured sqrt(n/m) is likely NOT tight for m << n (true requirement may be ~ eps n/m,
matching S1's independent finding that group constructions cap at L m/n rate);
(iii) F15's "saturation at the conjectured rate" is WRONG — cluster attacks only reach
correlation ~ mL + m; profile caps reach m. Any correct upper bound need only beat
C(mL + sqrt(n) polylog + m), a much softer target than F15 stated.

## F17. S1 RESULTS (pending adversarial verification — do not bank until verified)
S1 claims complete proofs of:
 - THEOREM A: E sup <= C[(1+L)/sqrt n + L sqrt(m-bar Lambda / n) + (1+L) m-bar d Lambda/n],
   Lambda = log(m-bar d^{3/2}(2+L)/L) — NO n, NO eps in the log. Mechanism: harmonic/
   Poincare split (deg>=2 part has population radius L/sqrt(2d)) + Dudley at the empirical
   radius + Ledoux-Talagrand radius self-bounding.
 - THEOREM B: the law with Lip >= c0 eps sqrt(n/(m-bar log(e m-bar d(2+1/eps)))) under
   n >= C[eps^{-2} log(8/delta) + eps^{-1} m-bar d Lambda + m-bar d^2 Lambda]. For BLN:
   Lip >= c sqrt(n/(m log(Cmd))) once n >= C m d^2 log(Cmd).
 - LEMMA D (dictionary sup C(sqrt n + sqrt d), log-free) + PROP S (spiky sector log-free,
   reduces to 1-t_k >= 1/(m-bar d log)).
 - PROP L5 (Sudakov ceiling): no single-scale minoration can force ANY log; log n /
   log(1/eps) necessity REFUTED by Theorem A; radius-scale packings carry Theta(m-bar d).
 - Lower-bound landscape: best constructible complexity for m << n is
   c[min(1,L) m/n + L sqrt(m/(nd)) 1_{m<=d} + min(1,L)/sqrt n] — sqrt(min(d,n/m)) BELOW
   the conjectured complexity; conjecture only known attained at m >~ n.
 Remaining to fully log-free (S1's localization): C1 (uniform visible-trace ratio-LLN over
 caps/slabs + invisible incidence, for the box-cap-ellipsoid body; numerically ratio <= 1.06
 visible, true body 0.27 budget across all adversarial families) and C2 (deterministic
 body-transport at merging units for fibered chaining; increment estimate already proved).
 REGIME MAP after S1: m <= n/(C d^2 Lambda): log(md) only [Thm B]; middle m: old log(mnd);
 band [n/log^C, n/2]: band-lemma program (F7-F14, softer target per F16); m >= n/2: trivial.

## F18. Audits (session 5, owner-requested): inventory, citations, my own proof-audit
 (a) INVENTORY AUDIT of canonical paper (c141bd8): strict superset of every earlier
     result — main law, BLN corollary, simultaneous widths, kink-count law, structured,
     vector outputs, matching upper bound (pi/2 sqrt7 form), parametric d=2 failure
     (ratio-4.99 numeric kept, now merely illustrative of the scalable construction),
     general isoperimetric data, all numerics incl. at-scale, author/funding/AI
     declarations. NO regressions. ✓
 (b) CITATIONS AUDIT — all five bibliography entries verified against primary sources:
     BLN PMLR v134:804-820 (exact); BS JACM 70(2) 2023 DOI 10.1145/3578580 (pp 1-18);
     WHZ PMLR v202:37439-37455 (exact); Pinkus Tracts 205, 2015, DOI CBO9781316408124
     (exact, online-ISBN-derived); Vershynin CUP 2018 (standard). Inline: BS "Section A"
     and "Remark 1.1" previously verified verbatim. ✓
 (c) MY OWN AUDIT of S1's Theorem A assembly (the flagged danger step): verified by hand —
     psi(s) = sqrt((s/2) log((2eB)^2/s)) is concave increasing on (0, B^2] (h' > 0 iff
     s < C^2/e; h'' = -1/(2s) < 0); Jensen valid; Case 1 algebra reproduces
     Lambda = log(2eB sqrt d / L) exactly; Case 2's "argument >= 2r^2 => log <= 2 Lambda"
     is the CORRECT direction (larger s => smaller log((2eB)^2/s)); the quadratic solve
     R <= 16 a^2 B_1 Lambda checks. Also re-derived Lemma A1's constants: lambda_1 = d-1,
     ||F_1||^2 = ||A||^2/d, lambda_2 = 2d, B_1 = 2 + sqrt(3/2) L — all correct; the
     spectral identity is standard for Lipschitz (H^1) sphere functions; clip preserves
     chord-Lip and chord <= arc gives geodesic-Lip.
 (d) COMPLETED MY OWN FULL AUDIT of S1 (independent of the verifier agent):
     - A4's constant 8 = 2 (symmetrization) x 2 (LT contraction with absolute values,
       phi(s)=s^2/(2B_1), phi(0)=0, contraction verified) x 2B_1: CORRECT.
     - A3: 0 in H (f=0); Dudley pinned form standard; entropy transfer via
       |c_F-c_G| <= eps, ||A_F-A_G|| <= sqrt(d) eps (Cauchy-Schwarz d E[(F-G)x]),
       so (2+sqrt d) eps absorbed in log; integral lemma int_0^r sqrt(log(B/u)) du
       <= r[sqrt(log(B/r)) + sqrt(pi)/2] <= 2r sqrt(log(eB/r)): CORRECT.
     - THEOREM B plumbing: Lambda(L*) <= C Lambda-bar in both branches (L* >= 1 via
       (2+L*)/L* <= 3; L* < 1 via eps sqrt(n) >= 1 from the first sample condition);
       the three sample conditions map to the three Theorem-A terms exactly
       (the L*-part of (c): L* m d Lambda / n <= eps/K iff n >= K' m d^2 Lambda-bar ✓);
       McDiarmid differences <= 4/n safe: CORRECT (modulo one standard multiplier-
       symmetrization constant, 4 vs 8 — immaterial).
     - LEMMA D: psi_2 increments sqrt2(||X(u-u')|| + sqrt n |t-t'|) ✓; two constant-
       aspect Dudley factors ||X|| sqrt d + sqrt n, and ||X|| sqrt d <= C(sqrt n + sqrt d): CORRECT.
     - PROP S: shell rigidity 2L 2^{(j+1)/2}/sqrt(delta_0) ✓; per-unit geometric sum
       sum_j 2^{-j/2} sqrt(log + j) <= C sqrt(log) ✓; the delta_0 choice makes
       m delta_0 d log(e/delta_0) <= 2: CORRECT.
     => By MY audit, Theorems A and B, Lemma D, Prop S are all correct as stated.
     Once the independent verifier concurs, these are two-audit clean (house standard)
     and go into the paper as the "n-free logarithm" section — a strict improvement:
     BLN corollary becomes Lip >= c sqrt(n/(m log(Cmd))) for n >= C m d^2 log(Cmd).

## F19. Session 6: the n-free logarithm is IN THE PAPER (pushed 8597c65)
Wrote Section "Removing the sample size from the logarithm" with complete proofs
(harmonic split; entropy-at-the-radius Dudley; radius self-bounding; complexity theorem;
the law with Lambda-bar = log(e m d^3 (2+1/eps)); plus the residual-log remark recording
the Sudakov ceiling and the spiky-sector reduction). Caught and fixed my own definition
slip before compiling: Lambda_L must be the RADIUS-RATIO logarithm log(e m d^3 (2+1/L))
(the (2+L) of the class scale B cancels against L at the radius; keeping (2+L) inside
Lambda would have re-introduced log L* ~ log n for large L*). Statement scoped to
Rademacher multipliers (the z-case handled via the factor-8 symmetrization+contraction
inside the law's proof). Paper now 22pp, compiles clean, pushed master+branch 8597c65;
zip refreshed. VERIFICATION LEDGER: derivation (S1) + full independent audit (me, F18)
= two independent passes; a third (agent referee) QUEUED for when session quota resets
(the first attempt died at the provider limit). If the third pass finds anything, fix
forward.

## F20. Session 7 (solo): two new pieces for the remaining fronts

### F20a. GENERAL ACTIVATIONS, width one — complete proof (first unconditional
### general-psi result of the campaign; extends to a floor for all m)
THEOREM (provable today, full sketch below): model (S), y iid +-1. Whp over (x,y),
for EVERY Lipschitz psi and EVERY width-m net f (arbitrary weights) fitting exactly:
   Lip_S(f) >= c n^{1/(m+1)} / C.
At m = 1 this is c sqrt(n) — EXACTLY the conjectured rate: the general-activation
conjecture is RESOLVED AT WIDTH ONE. For general m it is a floor far below sqrt(n/m)
(worst-case pigeonhole gives n^{-1/(m+1)} pair-gaps, not the random-pair n^{-2/m}).
Proof structure (all steps elementary):
 (1) f factors through the (m+1)-dim projection P onto span{w_1..w_m, v}. Fiber-transport:
     whp all ||P x_i|| <= 1/2 (needs d >= C m), and for two data points,
     |f(x_i) - f(x_j)| <= C L ||P(x_i - x_j)|| (move x_i to a same-fiber point above
     P x_j: the sphere-lift costs a bounded derivative factor since sqrt(1-s^2) has
     bounded slope on |s| <= 1/2).
 (2) Volumetric pigeonhole: partition the (m+1)-ball into K = n/2 equal-volume cells of
     diameter C (2/n)^{1/(m+1)}; at least n/4 disjoint same-cell pairs exist.
 (3) Adversarial U handled by a net union: pairs depend on (x, U); y is independent, so
     P(all >= n/4 disjoint pairs same-label) <= 2^{-n/4}; union over a projection net of
     size e^{C m d log n} works for n >= C m d log n. Net-continuity: projected distances
     move by 2||U - U'||_op; resolution n^{-1/(m+1)}/2 suffices.
 (4) An opposite-label pair at projected distance <= C(2/n)^{1/(m+1)} forces
     2 <= C L (2/n)^{1/(m+1)}, i.e. the bound.
TODO: write into the paper as "General activations at small width" (with the honest remark
that for m >= 2 the floor is below the conjectured rate), after a referee pass.

### F20b. WIDE-REGIME general activations — the Gegenbauer-flatness weapon
Key new observation for Mode 1: the UNIT-L2-NORMALIZED Gegenbauer functions satisfy
   |phi_l(s)| <= C_d (1-s^2)^{-(d-2)/4}   UNIFORMLY IN l  (classical asymptotics,
   flat region), so zonal evaluations at the data are BOUNDED off caps and
   occupancy-controlled inside caps — zonal spikes are localized EXACTLY like ReLU ramps
   (occupancy N(t) <= Op/t^2 applies verbatim). Consequently the smoothed-zonal empirical
   analysis inherits the F14 toolkit wholesale, independent of activation. Combined with:
   heat split (probability-free tail kill at l >~ L/u), level-rank <= m (Daniely device,
   cancellation-proof), and the crude infinity-covering of the smoothed body, this yields
   the general-psi law at the conjectured rate (constant eps) in the WIDE regime
   m >= n/d polylog with a sqrt(log d) loss; sharper bookkeeping should extend down.
   Estimated: multi-session write-up; no step requires new mathematics beyond F14's
   occupancy arguments applied to phi_l in place of ramps.

## F21. Session 8 (solo): improved projection floor => any-activation conjecture at d >= Cn
Upgrade of F20a using the RANDOMNESS of x (random pair-gaps in an (m+1)-dim projection are
~ n^{-2/(m+1)}/sqrt(d), far below the worst-case pigeonhole n^{-1/(m+1)}):
 IMPROVED FLOOR (proof plan audited, one write-up pass needed): whp, for every Lipschitz psi
 and width-m net fitting exactly,
   Lip >= c sqrt(d/m) * ( n^2 / (d (log n + m log d)) )^{1/(m+1)}   >=  c sqrt(d/m).
 Mechanism: per net-projection U, a maximal delta-close MATCHING among projected points has
 E[#pairs] ~ n^2 p_delta (chi_{m+1} ball probability p_delta ~ (delta sqrt d / sqrt m)^{m+1});
 DIAL n^2 p_delta := C d (log n + m log d) — makes BOTH the label-independence union
 (2^{-#pairs} beats the frame net e^{C m d log(1/delta)}) AND the sample condition mild
 (n >= sqrt(d m polylog)). McDiarmid over x for the matching (bounded differences 1/point)
 forces the one REAL constraint: E^2/n >= C m d polylog  <=>  d >= sqrt(n m)/polylog.
 CONSEQUENCES:
  - d >= C n: floor >= c sqrt(d/m) >= c sqrt(n/m): the FULL conjectured rate, EVERY
    activation, EVERY width m <= c d. THE HIGH-DIMENSIONAL GENERAL-ACTIVATION CASE CLOSES.
  - sqrt(nm) polylog <= d <= n: partial floor sqrt(d/m) (below conjectured by sqrt(n/d)).
  - Any m <= 4 log n / log(n/(md))-ish: meets the conjecture (extends F20a's m=1).
 TODO: full write-up + referee; then add to the paper as an upgrade of Section genact.

## F21'. WRITE-UP PASS OF F21 (session 8 cont.): two corrections, final form proved
(a) F21's "d >= Cn closes" is FALSE. psi(t)=t realizes f=<v,x>, Xv=y solvable with
||v|| <= C sqrt(n) whp at d >= Cn: exact fit, Lip <= C sqrt(n) — kills any floor above
sqrt(n) there (F21 claimed n/sqrt(log) at m=1). Mechanism-level: projector-net budget
e^{C m d log} vs label budget e^{c n} — NO version of the scheme survives m d log > n.
The theorem must carry n >= C(m+1) d log(nd), i.e. d <= n/(Cm log).
(b) McDiarmid is the wrong tool (deviation scale sqrt(n) forces pair count sqrt(n md log),
degrading the floor to n^{3/(2(m+1))}). FIX: one pair per doubly-occupied grid cell;
multinomial cell counts are NEGATIVELY ASSOCIATED (Joag-Dev–Proschan), so Chernoff holds
at rate e^{-mu/8} for M2 = #doubly-occupied cells: pair budget dials to exactly
N* = C(m+1)d log(nd) and the full n^{2/(m+1)} rate survives. Also: only ONE opposite-label
pair is needed (2^{-N*} beats the net) — no binomial counting.
FINAL THEOREM (proved, terse write-up delivered to coordinator; referee pass pending):
model (S), iid signs; d >= C(m+1), n >= C(m+1)d L, L := log(nd). Whp 1-Ce^{-cd}, every
Lipschitz psi, every width-m exact interpolant: Lip >= (c sqrt(d)/(m+1)) n^{1/(m+1)}
[all m <= cd], and for m+1 <= c log n the localized-birthday floor
   Lip >= (c sqrt(d)/(m+1)) (n^2/((m+1) d L))^{1/(m+1)}.
Proof: Op-localization tau ~ sqrt((m+1)/d) uniform over ALL subspaces (deterministic
given lambda_max) + Markov core r0 = 2 sqrt(p/d) + light/heavy cell dichotomy (heavy:
q_c > 32/n, <= n/32 cells, pigeonhole; light: E[1{n_c>=2}] >= c n^2 q_c^2, Cauchy-Schwarz
over K_core <= (Cp/(delta sqrt d))^p cells — NO density asymptotics needed) + NA-Chernoff
+ 2^{-N*} label step + Grassmannian net. All elementary.
CONSEQUENCE CURVE (verified, matches coordinator's algebra): floor >= sqrt(n/m) iff
d >= n^{(m-3)/(m-1)} (C(m+1)L)^{2(m+2)/(m-1)} (poly(mL) = polylog for m <= log n).
Per width, inside C <= d <= n/(C(m+1)L): m=1: floor n/sqrt(L) — met with room, ALL d;
m=2: floor c d^{1/6} n^{2/3}/L^{1/3} — met for ALL admissible d (NO d >= sqrt(n) needed;
binding constraints are only d >= C and the net ceiling d <= n/(CL)); m=3: met once
d >= C L^5; m>=4: window n^{(m-3)/(m-1)} polylog <= d <= n/(CmL), nonempty iff
m <= c log n/loglog n. Everywhere in range the floor beats thm:genact by sqrt(d/(m+1)).
SCOREBOARD UPDATE: general-psi conjecture now CLOSED for m <= 3 (polylog <= d <= n/polylog)
and for the m <= log n/loglog n window above the curve; OPEN: m >= 2 at d >= n/(m polylog)
(where the affine/near-affine fits live) and all m >= c log n at the conjectured rate.
Numerics (scratchpad check_f21_floor*.py, seeds 20260707/8): pair-count law
M2 ~ n^2 (0.2 delta sqrt(d/p))^p verified across d in {50..200}, m in {1,2,3} (dial-vs-
measured within 2x at the N* scale); NA concentration: 300 draws, mu=51, min=32, zero
below mu/2; adversarial-W search (m=1, incl. label-aligned X^T y direction + 24 restarts
x 150 steps): best opposite-gap 0.0021/0.0014/0.0010 at d=30/60/120 — all under the
d-free theory cap ~2 sqrt(L)/n ~ 0.0065, implying floors 322/473/670 vs old sqrt(n)=32.

## F22. Unification note (from the sharp-log postmortem)
The d^2 in Theorem sharplog's sample condition is the Bernstein variance-range ratio
B_1^2 D / r^2 with D = md Lambda, B_1 ~ L, r ~ L/sqrt d — intrinsic to any uniform-Bernstein
route. Beating it = exploiting that large-value class members are SPIKY (occupancy-localized)
— the SAME localized empirical-process core as the band and the zonal wide regime. ONE
occupancy-localized uniform law would simultaneously: (a) extend sharp-log to n >~ md polylog,
(b) crack the band, (c) power the zonal Mode-1 (with Cramer/Hermite flatness: normalized
Gegenbauer values are O(1) at bulk scale s ~ 1/sqrt d — pole region occupancy-controlled).
All remaining fronts funnel into this single lemma family.

## F23. Session 9 (solo): the metric-cap occupancy corollary + a dead end closed
 (a) CLEAN COROLLARY of the occupancy lemma, worth using everywhere: whp, EVERY metric cap
     of geodesic radius <= pi/3 (i.e. {<z,x> >= t} with t >= 1/2) contains at most 4 Op
     data points, Op ~ (1+sqrt(n/d))^2. So high-value blobs of Lipschitz functions
     (diameter >= height/L) hold O(Op) points each once height/L <= 2/5. Spike-mass
     accounting reduces to COUNTING blobs.
 (b) DEAD END (recorded to save cycles): counting connected components of superlevel sets
     {h > beta} via the kink-arrangement is useless (~m^d cells); population/Vitali
     counting is exponentially invisible (cap measures e^{-cd}). Blob COUNTING must come
     from the serving/charging structure (each blob needs height from units whose
     rigidity+pile-up budgets are global) — i.e. the bump decomposition, confirming F22:
     all remaining fronts = the one charging lemma. The band agent carries the battle plan.

## F24. CORRECTION OF F7 + THE ALL-WIDTHS KEYSTONE (session 9 — important)
 (a) F7(ii) IS WRONG as banked. "Our proven bound beats c sqrt(n/m) for m <= n/(C log)"
     fails: the deficit of sqrt(n/(m Lambda)) vs c sqrt(n/m) is sqrt(Lambda), which grows
     with n, while the conjecture's constant is fixed. Concretely n = 10^6, m = 10^3:
     our bound ~ 6 c_1 vs target ~ 31.6 c — no absolute c survives n -> infinity. The
     log-free conjecture does NOT follow below the band from the with-log theorem.
     CORRECTED remaining set for log-removal: ALL m <= c^2 n / 2 (the trivial sqrt-2
     floor covers only m >= c^2 n / 2), except m = 1 which genact settles. The in-band
     statements F9/F13/F14/F16 are unaffected (they never used F7(ii)); what is wrong is
     only the claim that the band is ALL that remains. F17/F19 "middle regime" language
     inherits this correction.
 (b) THE STRONGER TRUE REDUCTION (F9's mechanism with the band restriction REMOVED):
     the joint across-level Cauchy-Schwarz with sum_{l <= Lambda*} 1/lambda_l <=
     C log(Lambda*)/d gives, for ANY width m and ANY activation (the energy ellipsoid is
     activation-free):
        sup corr <= L sqrt( n m polylog / d )    PROVIDED the KEYSTONE BOUND holds:
        (K)   sup_{U in (S^{d-1})^m, l <= Lambda*}  ||P_{V_l(U)} T_l||^2  <=  n m polylog(n).
     Then fitting eps n forces L >= eps sqrt(n d/(m polylog)) >= eps sqrt(n/m) once
     d >= polylog(n). I.e.
        (K)  ==>  THE FULL CONJECTURE (log-free, every Lipschitz activation, every m)
                  for d >= log^C n.
     Since the conjecture's own sensible regime needs d >= C log n, (K) closes everything
     except the sliver C log n <= d <= log^C n. ALL fronts genuinely funnel into (K).
 (c) Known sub-obstacles of (K): E_y ||P_{V_l(U)} T_l||^2 ~ n m for FIXED U (clean);
     the naive sup-over-U (variety-width chaining: md-dim manifold, sqrt(n)-scale
     increments) is TOO LOSSY by a factor d; the fix must exploit that T_l is one fixed
     random vector and V_l(U) moves smoothly except at ill-conditioned clustered-pole
     spans — exactly the C1/C2 conditioning/transport sub-issues. Gegenbauer flatness
     (F20b) + metric-cap occupancy (F23a) control the evaluations. (K) at l = 1 is
     trivial (||P_W sum y_i x_i|| <= sqrt(n Op)).

## F25. (K) REFUTED AS STATED; the Christoffel lens; the repaired keystone (session 9)
 (a) NEW IDENTITY (useful lens): E_y ||P_{V_l(U)} T_l||^2 = sum_i K_{V_l(U)}(x_i), where
     K_V = the Christoffel function (diagonal of the projection kernel) of the subspace;
     population average int K_V = dim V = m. So (K) in E_y-form = a RATIO-LLN for
     empirical Christoffel mass (and S1's C1 "visible trace" tr(M^{-1} Phi^T Phi) IS
     exactly this object).
 (b) (K) IS FALSE at high levels: POLES-ON-DATA attack — placing poles at data points
     gives K_V(x_i) ~ N_l per hit, so sum_i K_V >= m N_l >> n m polylog once
     N_l ~ d^l/l! >= n polylog (i.e. l >= log n/log d; at d ~ n even l = 2). My (K) was
     an over-relaxation: dropping the clip discards exactly the constraint that kills
     this attack (a function with level-l mass spiked at data poles has pointwise values
     ~ c sqrt(N_l) there; |f| <= 1 forces c <= 1/sqrt(N_l), so its CORRELATION is only
     ~ m — harmless). The Cauchy-Schwarz-across-levels bound goes vacuous at the attack
     config while the truth stays small: the lossy step is dropping the clip, not the
     level decomposition.
 (c) REPAIRED KEYSTONE = F11's original clipped object, now understood to matter at ALL
     widths (not just the band): E_y sup { sum_i y_i f(x_i) : f_l in V_l(U) some U,
     sum_l lambda_l ||f_l||^2 <= L^2, ||f||_inf <= 1, l <= Lambda* } <= eps n/8. The clip
     must be INTERLEAVED with the level-rank structure (charging/bump machinery), not
     discarded before it. Sub-cases already OK: l = 1 trivial; population-visible poles =
     Christoffel ratio-LLN (S1 numerics: ratio <= 1.06); the open core = invisible-spike
     sector, same as ever. F24(b) stands with (K) replaced by this clipped version.

## F26. Session 10 (solo): the visible sector is provable-now; the wall is C2, made concrete
 (a) VISIBLE-SECTOR PLAN (tools exist): set the visibility threshold at cap-mass
     p_0 := C m d log(nd)/n (NOT (nd)^{-C} — matrix Bernstein needs n p_0 >= the
     net exponent). For pole-configs all of whose Gram-relevant masses are >= p_0:
     empirical Christoffel ratio-LLN by matrix Bernstein + net union; then
     lambda-weighted Cauchy-Schwarz + Hanson-Wright concentration gives the conjectured
     correlation bound for the visible part: all m, all activations, d >= polylog.
 (b) THE WALL, localized precisely: net-union continuity at CLUSTERED poles. The map
     U -> V_l(U) is discontinuous at rank drops (Grassmannian netting is out: dim m d^l).
     Function-level fix: the closure of {m-zonal combinations} = algebraic family of
     JET SPANS (zonals + derivative-zonals along multiplicity patterns — C2 normal form,
     dim <= m(d+1)). Rayleigh form sup_g <y, g(X)>^2/||g||_2^2 is subspace-only (no
     conditioning anywhere) — but naive chaining over the jet family costs a factor d
     (variety-width loss, F24(c)); the fixed-vector improvement needs Lipschitz-in-theta
     projections = C2-transport again. VERDICT: C2 (body/jet transport at merging poles)
     is THE single technical heart of the visible sector; the invisible sector is the
     charging front (band agent). Everything else is in place.
 (c) Also checked: serving-capacity reformulation of the conjecture (every class member
     lifts <= C m L^2/eps^2 points to sign-correct height eps) — consistent with all
     known constructions (caps, clusters, profile spikes, genact at m = 1 EQUALS it);
     the projection/margin route to it dies at m >= log n (Lipschitz-separator classes
     cost e^{m log(L/eps)}); the harmonic route is the real one.

## F27. F21's per-width consequence curve (derived, sent to the F21 agent to verify)
The improved floor sqrt(d/m) (n^2/(d polylog))^{1/(m+1)} meets sqrt(n/m) iff
   d >= n^{(m-3)/(m-1)} polylog^{2/(m-1)}.
Per width: m = 2 -> all d (subject to the write-up's d-conditions — possibly d >= sqrt(n)
from McDiarmid; agent to determine); m = 3 -> d >= polylog; m = 4 -> d >= n^{1/3};
m = 5 -> d >= sqrt(n); m -> inf -> d >= n. So F21 would settle the GENERAL-ACTIVATION
conjecture for ALL m <= 3 (d >= polylog) and for all m at d >= C n — the small-width
front closes entirely, activation-free.

## F28. Referee round on sharp-log + genact COMPLETE (session 10) — pushed e0f0354
Independent referee verdict: BOTH sections CORRECT after repairs; every constant in the
sharp-log chain verified (incl. the case-2 log direction, LT constant 8, McDiarmid 512,
delta bookkeeping). Five fixes found and ALL APPLIED:
 1. prop:entropy range extended to eps' in (0, 4+8L) (Dudley integrates to sigma-hat <=
    B_1 >> 1; the old (0,1] range would have smuggled log(2+L) ~ log n back in). raddud
    restated for u in (0, 2B_1].
 2. genact frame-net metric mismatch: column mesh now delta_cell/(8 sqrt(m+1)) with
    ||P - P-hat||_op <= 2 sqrt(m+1) delta_net = delta_cell/4 (orthonormal-column Frobenius
    trick); log-cardinality unchanged; added the 9/16-low transport tolerance (constant
    1.71 <= 2) and the trivial delta_cell > 1/4 case (L >= c' from any opposite pair).
 3. below-noise-floor remark restated honestly: fixed absolute accuracy c_1 (Markov,
    n/32 clean pairs, c halved) — NOT arbitrary sigma^2 - eps.
 4. pair-count off-by-one: >= 3n/4 - 1, >= 3n/8 - 1 >= n/4 for n >= 8.
 5. rem:residual radius display corrected to what the lemmas actually give.
VERIFICATION LEDGER for the two new sections: derivation + my full independent audit +
independent referee with fixes applied = THREE passes. House standard met.

## F29. Band front: Claims 1-7 landed; the Band Lemma reduced to (M) (session 11)
Charging agent delivered (full detail: notes/BAND_CLAIMS.md; referee launched):
 - PROVED (pending referee): fitting identity in penalty form; occupancy + concentration +
   tightness; value-mass/l1-closure with explicit constants (t_* = 320 L Op/(eps T));
   quadratic serving capacity (tight; kills single-domination at c0 <= sqrt(eps/192 Op));
   gradient-cloud rigidity + rigorous PILE-UP corollary (ball model; sphere version carries
   an error term uncontrolled exactly at clustered kink hyperplanes); NEW log-free affine
   closure with UNBOUNDED v via penalty form (sup = y^T P y ~ d + log(1/delta),
   Hanson-Wright) — removes the unbounded-v obstruction with no harmonic split;
   conditional assembly (M) => Band Lemma, airtight with McDiarmid + dyadic-T union.
 - (M) = the irreducible statement (mesoscopic clipped multiplier bound, class pinned
   precisely, d >= eps^{-2} log^C n). All known attacks sit at eps n/160 vs (M)'s
   eps n/4 threshold. Open core inside (M): unorganized/CLUSTERED mesoscopic stacks
   (where sphere group-rigidity's error term is uncontrolled) — note this is the SAME
   cluster-degeneracy heart as C2/jet-transport on the visible side. The two remaining
   fronts share one enemy: pole/kink clustering.

## F30. Cluster stacks = ridges + shells; profile rigidity WITHOUT the motion argument
Sketch (session 11, mine — for the (M)/C2 clustered core):
 (a) A stack of units with poles within rho of u_0 equals a single RIDGE with 1-D profile
     P(s) = sum_j alpha_j relu(s - t_j) plus corrections supported on transition shells
     {|<u_0,x> - t_j| <~ rho} — off the shells the stack IS 1-D.
 (b) PROFILE RIGIDITY, static: at any bulk sphere point x off all shells and off other
     units' caps, the tangential-gradient component along w = P_T u_0/||P_T u_0|| gives
     <grad_T f, w> = <v,w> + P'(s) ||P_T u_0|| + O(rho sum|alpha|) with ||P_T u_0|| >= 0.86
     for |s| <= 1/2. So the profile's PARTIAL SUMS P'(s) = sum_{t_j < s} alpha_j are
     pinned by a single pointwise gradient evaluation — no two-point motion argument, no
     cluster-diameter error term. The obstruction shrinks to: separating <v,w> (affine)
     and other-unit contributions from the cluster's scalar — a 1-D flow along the
     u_0-great-circle crosses other units' caps <= m' times, giving piecewise segments
     where the profile increment is L-controlled up to the affine drift; the affine drift
     is globally handled by Claim 6's penalty form. Suggests: (M)'s clustered core =
     JOINT 1-D chaining of shell-corrected profiles with partial-sum rigidity — matches
     F13's old plan and the C2 jet normal form (derivative zonals = profile derivatives).
 (c) TODO: make (b) a lemma (choose per-cluster probe points; handle overlapping clusters
     by dyadic pole-separation strata); then (M) splits into (i) 1-D profile class with
     partial-sum rigidity — chaining should be log-free by Lemma-D-style constant-aspect
     factors; (ii) shell corrections — value-mass <= |alpha| rho occupancy, small for
     rho <= t_*^2/polylog; (iii) cross-cluster interactions — pile-up (Claim 5 ball +
     the static scalar version).

## F34. THE VARIANCE-BUDGET IDEA (session 14 — candidate decisive lever for G2)
Found while briefing the G2 agent. The clip/value bound sup_S |sum_c Q_c(<u_c, x>)| <= B
combined with NEAR-INDEPENDENCE of the slab variables <u_c, x> across rho-separated
directions (joint law ~ product for large d) should force the GLOBAL VARIANCE BUDGET
   sum_c Var_x(Q_c(<u_c, x>))  <=  C B^2 polylog     (B ~ 1 + L*),
i.e. the m' cluster profiles share ONE L^2 budget of size L*^2 — not m' individual
budgets. Consequence: the joint multiplier fluctuation is sqrt(n sum_c Var) <= B sqrt(n)
with NO m' factor, and the joint chaining at the budgeted radius should give
E_y sup <= C B sqrt(n) + entropy terms — closing G2 at ALL d (not just d >= n), hence
(M) = G1 alone, hence (per ASSEMBLY_MAP) the log-free PL law at all widths m <= n/2 for
d >= eps^{-2} log^C n modulo G1. TO PROVE: (1) the variance-budget lemma (expand
E(sum Q_c)^2; cross terms ~ product means for separated poles; quantify dependence via
the Gram; coherent clusters are G1's territory); (2) multiplier chaining at radius
sqrt(sum Var) (directions entropy md log at the REDUCED radius). Numerics first: try to
BREAK it with adversarial aligned tiny profiles (can sup|sum| <= 1 coexist with
sum Var >> 1?). G2 agent is executing exactly this plan.

## F40. Sessions 18-19: the subset-Lipschitz detour (instructive failure) + the three-sector endgame
 (a) MY subset-Lipschitz law (m' <= O(d/log)) was REFUTED by the verifier: I evaluated
     the AMBIENT gradient at subset-aligned points — which are exactly the tangential
     CRITICAL points of the profile sum (radial pole-sum => P_perp = 0; measured gap
     232x). Lesson recorded in SUBSET_LIPSCHITZ.md (superseded header). The disjoint
     lower bound IS net-legal (Lip_S ~ 4 Lambda flat in d, m'); Phi_disj, c* = 1/32,
     and the S2 data-point pile-up all STAND (at data points the sharing poles
     genuinely spread: tangential coherences <= 2nu shallow => sqrt(J) bites).
     Forced-depth confirmed vacuous at the anchor; shallow co-depth multiplicity
     genuinely unbounded — harmlessly.
 (b) THE THREE-SECTOR DICHOTOMY (session-19 live analysis, agent writing it up):
     for the full amended general class, stratify by aimed-cap size/point depth:
     DEEP (s > sqrt((1+nu)/2)): FD-disjoint + deep-peel — closed;
     MID (aimed k < 1/nu, own-depth > sqrt(nu)): the pairwise budget forces
       r_gh <= nu k < 1 => ZERO sharing => pairwise-disjoint aimed sets => coverage
       <= n => capture <= n h_0 (the mid-depth reuse attack is pairwise-ILLEGAL —
       found and killed in-flight);
     SHALLOW (k >= 1/nu, own-depth <= sqrt(nu)): tangential coherences <= 2 nu =>
       the pile-up is VALID there => rising multiplicity <= J_max = O(1) =>
       capture <= n J_max h_0.
     Plus: profile extreme points are ramps (isotonic/extreme-point lemma) and the
     y-weighted single-ridge cap-mass (drop the negative class) gives per-ridge
     general <= per-ridge aimed. If the write-up survives referee: (S1) + throttle
     COMPLETE => (M) on d above the slice => with the deterministic slice below,
     the assembly, and the general-activation transfer: THE LOG-FREE LAW AT ALL
     WIDTHS FOR EVERY LIPSCHITZ ACTIVATION on d >= eps^{-2} log^C n, modulo the
     sub-tau_0 sector and the coherent mid-d window.

## F39. THE GENERAL-ACTIVATION TRANSFER (session 17 — the second half funnels into (R'))
Transfer agent delivered (full proofs in notes/GENERAL_ACTIVATION_TRANSFER.md; my audit
of the load-bearing steps PASSED; referee launched):
 (a) PROFILE-DERIVATIVE RIGIDITY: P1 verbatim with A(s) -> g'(s) (a.e./Lebesgue points):
     |beta + g'(s)| sqrt(1-s^2) <= Lip, TV <= pi L, ||v_perp|| <= L — for ANY Lipschitz
     profile, however many units compose it. Stratified isolation transfers with
     anchors a_g = inf supp(g_g) >= tau_0 (cleaner than ReLU: flat regions give
     genericity for free). Numerics: tanh/GELU stacks ratio 1.000000, 0/2000.
 (b) SINGLE-POLE THEOREM FOR EVERY LIPSCHITZ ACTIVATION — COMPLETE, UNCONDITIONAL:
     any single-direction net (any activation, any width, arbitrary weights) fitting
     eps below the noise floor has Lip >= c eps min(sqrt n, d), all d >= 3. Value-bound
     lemma checked activation-free; P3 cleaner (symmetric slope integral, 2 sqrt3 L Op);
     P4 was already profile-general; canonicalization step DISAPPEARS.
 (c) UNIT-FREE AUDIT passed lemma-by-lemma: every proven lemma counts POLES/CLUSTERS,
     never units/kinks. PL-APPROXIMATION IS FREE (common grid, eta = eps/(64 m');
     correlation transfers via the clip; cluster-total slope inherited by linearity;
     individual profile Lipschitz NOT controlled and NOT needed — the same coherent-
     cluster degeneracy as ReLU, correctly landing in the same open residual).
 (d) FD/DP/disjoint/deterministic-slice all transfer.
 (e) ASSEMBLED: general-activation (M) ==> (R') — LITERALLY the same statement as
     ReLU's (the (R') class already admits arbitrary profiles). When (R') lands for
     ReLU it lands for every Lipschitz activation SIMULTANEOUSLY. Residuals identical
     (sub-tau_0; the coherent sqrt(n) <~ d <~ n window).
 (f) Paper note: sec:scope's "cannot transfer to smooth activations without a new
     idea" must be updated — the profile-derivative route IS the new idea (rigidity on
     the profile derivative, an ambient-Lipschitz consequence; the 1/eta coefficients
     of the canonical-parameter route never appear).

## F38. THE FORCED-DEPTH MECHANISM (session 17 — candidate closer for the residual)
Found while briefing the final-chaining agent; the shallow-sector attack calculus now
CLOSES on paper. Three coupled facts:
 (a) FORCED-DEPTH LEMMA (elementary): if k points are shared at depth >= delta by K
     pairwise-nu-incoherent caps, then K delta <= <x_i, sum_g u_g> <= ||sum u_g|| <=
     sqrt(K(1 + K nu)), so delta <= sqrt((1 + K nu)/K): incoherent poles CANNOT share
     deep caps — sharing forces depth ~ 1/sqrt(K).
 (b) VALUE-DEPTH COUPLING: at co-depth 1/sqrt(K), full-slope ridges give per-point
     value Lambda sqrt(K) <= B => K <= (B/Lambda)^2 — the mega-stack is ILLEGAL; with
     PLATEAUED profiles (the evasion) the per-point value is B by construction and the
     capture per stack <= B x k with k <= occupancy at forced depth <= C K: capture
     per stack <= C B K; total over stacks (ridge budget sum K <= m'): <= C B m' =
     C(2 + 2L*) n/T <= eps n/32 in the CONTENT ZONE (T >= 2/(c_0 eps)^2). The shallow
     aligned sector self-limits at C B m' — no chaining needed for the aligned part.
 (c) The deep sector: l1 <= eps n/32 via the cap-mass lemma at cutoff delta* =
     8 Lambda m'/(eps n) ~ c_0/sqrt(T) (complementary to the deterministic slice).
 REMAINING for the residual theorem: (i) rigorize the STACK-DECOMPOSITION/EXCHANGE
 lemma (every shallow config's aligned capture <= C B m' + spread terms — greedy
 maximal co-depth stacks); (ii) the spread/fluctuation remainder (genuinely random-y,
 small radius — cap-mass l2); (iii) assembly with exact d-range. Agent in flight on
 exactly this. IF IT CLOSES: (M) falls => log-free PL law at ALL widths m <= n/2,
 d >= eps^{-2} log^C n (via BAND_CLAIMS Claim 7 + the F24 all-widths extension) —
 and the general-psi transfer becomes the last front.

## F37. Night ledger (sessions 15-16): the constraint triangle + stratified isolation in the paper
PAPER now at 69d1773 (29pp): + lem:stratiso (stratified isolation, 3-pass: derivation,
referee "crown jewel holds, machine precision", my audit with the safe tail form) +
rem:rigidfail (the coherence-floor counterexample, 3-pass, tight 1/rho). REFEREE round
on the night's haul complete: Lemma R's pointwise hypothesis FALSE (L2 form correct,
unproven — moot post-Claim-P), VBL correct-and-vacuous, G1 Claims 1/2/4 correct,
Claim 5 downgraded to conjecture+numerics, Theorem 5 scoped honestly (near-orthogonal;
"coherent blocks don't exist at d >= n" retracted), sub-tau_0 affine fallback BROKEN
(Claim 6 bridge withdrawn; rank([X 1]) = n at d >= n) — sub-tau_0 units are an explicit
open sub-lemma. THE MAP NOW: (M) = MERGE (proved) -> near-orthogonal super-ridges ->
P4-LIFT (the referee-named actual content: E_y sup of m' near-orthogonal TV-bounded
ridges <= C sqrt(m') L* sqrt(n), Pythagoras replacing subadditivity — uses TV+rigidity,
NOT the refuted projection) + sub-tau_0 sector + the sqrt(n) <~ d <~ n coherent window.
Final-core agent computing the deterministic incidence-capture optimization (= P4-lift
in optimization form). CONSTRAINT TRIANGLE stands: clip/rigidity/randomness all
mandatory — three rigorous refutations (CLAIMP_REFUTED.md).

## F36. SINGLE-POLE THEOREM IN THE PAPER (session 14) — pushed bdffdc8, 29pp
Referee verdict on SINGLE_CLUSTER.md: NO fatal errors, NO gaps in P1-P5; "publishable as
an unconditional special case"; P1's constant TIGHT (1.00000); d >= 3 necessary for the
combined bound (referee's d=2 test fails at ratio 1.187); P4's sqrt(n)-not-sqrt(nd)
confirmed analytically + numerically (free ramp /sqrt(nd) monotone 0.147 -> 0.0076).
INTEGRATION INSIGHT (mine): the standalone theorem needs NO band framing and NO
d >= log^C condition — only the Op event. Final paper form (thm:singlecluster):
model (S), exact labels, ALL d >= 3, eps^2 n >= C: every single-pole net (ANY number of
units, arbitrary weights) fitting eps below the noise floor has
   Lip_S(f) >= c eps min(sqrt n, d)     — no log, no width bound.
At d >= n the threshold is c eps sqrt n = the conjectured rate at the overparameterized
endpoint. Proof in the paper: lem:staticrig (static rigidity, one-evaluation) + TV <=
pi L + occupancy tail sqrt3 L Op + the ridge multiplier C(1+L) sqrt n (image-ellipsoid
cover + Frobenius identity Op min(n,d) <= 2 C_1 n + 1-D Lipschitz profile entropy) +
contraction/subadditivity assembly + McDiarmid. Third numerics script pair in repo.
Ledger: 3-pass (derivation + referee + my audit and standalone-strengthening).

## F35. Session-14 launches
G1 agent: cross-cluster static rigidity (P1-probe + averaged second-moment probes +
hierarchy/Vandermonde-in-directions for coherent centers; instructed to also try to
BREAK TV(P_c) <= C L* polylog — a counterexample family would be equally decisive).
G2 agent: variance budget + budgeted chaining (route above; d >= n intermediate as the
minimum target). Single-cluster referee still out. Paper at 8a14dce (27pp) now carries
thm:genact2 (localized projection floor, 3-pass verified incl. my mid/heavy write-out):
m=1 margin n/sqrt(Lambda); m=2 whole admissible range; m=3 at d >= C Lambda (tight);
linear-activation ceiling shows pd Lambda <= n/C is sharp.

## F33. Visible-sector referee verdicts (session 13 — the wall, precisely located)
 - Prop 0 CORRECT; Statement 1 (jet transport) CORRECT scoped k <= 3 (general-k Gram
   constant honestly open); Theorem 2 (Christoffel trace-LLN) CORRECT AFTER the
   pointwise-leverage fix (|K_V - K_J|(x_i) <= rho N_l = m; truncate at 2R_0; hypothesis
   n >= C_0 m^2 d LambdaBig): sum_i K_{V_l(U)}(x_i) <= 3 n m uniformly over visible U,
   all l <= Lambda*.
 - THEOREM 3 FATAL, WITHDRAWN: ||M_l||_op <= R_0 is false (op ~ n dimV, referee
   counterexample table op/R_0 up to 363 on fully-visible configs); no op-LLN rescues
   HW (op·s = nm dLambda); my own pre-worked repair was ALSO wrong (dropped op·s).
   The visible-sector CORRELATION bound is NOT proved. What survives: E_y ||P_V T_l||^2
   = tr M_l <= 3nm (that IS Theorem 2); missing: sup-before-E_y deviation control of
   y^T M_U y over the jet family = the SAME clipped charging/chaining wall as (M).
 - CONSEQUENCE FOR THE MAP: visible + invisible sectors have MERGED into one core.
   All roads now genuinely lead to (M)-style clipped multiplier control. The proved
   infrastructure around it: jet family + transport (conditioning-free), trace-LLN,
   occupancy/serving/pile-up, heat split, band assembly. The (M)-cluster agent (in
   flight) carries the only route that never passes through the relaxed quadratic form:
   the F30 charging scheme with the clip interleaved.

## F32. Session 13 (overnight): F21' + VISIBLE SECTOR landed; referees launched
 (a) F21' (notes/F21_THEOREM.md): corrected floors (negative association replaces
     McDiarmid — no d >= sqrt(nm) condition). VERIFIED CORRECTIONS TO MY OWN CLAIMS:
     "any-psi closes at d >= Cn" is FALSE (linear activation gives Lip <= C sqrt(n)
     min-norm interpolants at every width for d >= Cn — the conjecture is TIGHT there
     and floors beyond sqrt(n) are impossible); the method lives on d <= n/(C m Lambda).
     Final per-width results (pending referee): m=1 closes with margin n/sqrt(Lambda);
     m=2 closes on the whole admissible range (n >= C Lambda^2 only); m=3 at
     d >= C Lambda^5; window nonempty iff m <= c log n/loglog n. High-d general-psi is
     genuinely OPEN at every m (PL covered by the main theorem).
 (b) VISIBLE SECTOR (notes/VISIBLE_SECTOR.md): the C2 wall is BROKEN (for cluster size
     <= 3 completely; general k modulo one extractable Gram constant): jet closure =
     jet spans; transport LINEAR in cluster spread, poly(l,m) constants, NO Gram
     conditioning, d-free (numerics confirm exactly linear); entropy C md log. Plus
     THEOREM 2 (Christoffel ratio-LLN <= C n m, no polylog, via truncated Bernstein +
     jet net + trace-transport bridge |tr(P_V - P_J)S| <= rho n N_l) and THEOREM 3
     (visible-sector correlation <= C L sqrt(nm polylog/d) — the CONJECTURED RATE,
     log-free, every activation, every m, on the visible sector).
 (c) My pre-referee checks: k=2 jet computation verified by hand (||Z-dot||^2 =
     N_l P_l'(1) = N_l l(l+d-2)/(d-1) — positive, order N_l ✓); two candidate gaps
     handed to the referee with their repairs: truncation mismatch in the bridge
     (pointwise |K_V - K_J| <= rho N_l = m fixes it, truncate at 2R_0) and the
     ||M_l||_op <= R_0 claim in Thm 3 (likely wrong as stated; repair = m-dim matrix
     Bernstein giving op <= Cn, conclusion survives at d >= polylog^2).
 (d) In flight: (M)-cluster attack (the decisive front), visible-sector referee,
     F21' referee.

## F31. BAND_CLAIMS refereed: NO FATAL ERRORS; sound modulo (M) (session 12)
Independent referee verdict on Claims 1-7: Claims 1-2 fully rigorous; 3 rigorous (cosmetic
prefactor relabel); 4 rigorous (strict-inequality boundary fix); 5 rigorous conditional on
the pair-realizability hypothesis (now flagged as non-automatic; the sphere obstruction is
exactly why (M) is irreducible); 6 correct as a standalone identity+tail (the penalty-bridge
claim WITHDRAWN — it collapses back onto (M); not load-bearing since Claim 7 puts the affine
part inside (M)'s clip); 7 a VALID CONDITIONAL REDUCTION with correct probability
bookkeeping and no circularity. Bonus simplification found by the referee: with exact +-1
labels, Claim 1(ii) makes Sigma y_i clip(f) >= eps n/2 DETERMINISTIC — no noise
decomposition needed in the band assembly. All four referee fixes APPLIED to
BAND_CLAIMS.md. Ledger: derivation + referee = 2 passes; my own line audit = required
third pass before paper integration.

## Next actions (main thread)
1. In flight: (a) F21 write-up + F27 curve (resumed with output discipline);
   (b) C2/jet-transport + visible-sector lemma.
2. Me: third-pass audit of BAND_CLAIMS; then the "toward the log-free law" paper section
   (Claims 1-7 + (M) as a conditional theorem + the honest open-core statement).
3. Attack (M)'s clustered core via F30 (static profile rigidity) + C2 jet normal form
   when it lands.
4. Scoreboard: log-free PROVED at m = 1, m >= c^2 n/2, (pending F21) d >= C n any psi
   + all m <= 3; band = (M) only; visible sector = C2 only; both cores = clustering.
1. Prove the k=2 limit-stratum tameness rigorously (started; the limit profile has
   |A| <= L and Lip(A) <= CL — write full proof).
2. General-k limit stratum: identify the normal form (iterated divided differences of
   ridge profiles along clustered directions = jet of profile derivatives x spherical
   polynomial factors); prove tameness by induction using Lip(f) <= L in cluster-tangent
   directions.
3. Cluster dichotomy at threshold s0(u) = (u / (C L))^{1/1}? — work out the exact
   crossover exponent from the Vandermonde conditioning.
4. Assemble Deliverable (A) for m <= d polylog; then fight the m^2 term.
