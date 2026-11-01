# Campaign: the FULL BLN conjecture (log-free + any Lipschitz activation)

Goal: Lip(f) >= c sqrt(n/m), no log, for every Lipschitz activation psi, arbitrary weights.
Both gaps are genuinely open (log-free unknown even for BOUNDED weights; general psi unknown
at all). Honest deliverables ladder:
  (A) general-psi law WITH polylog  — major new theorem, plausible;
  (B) log-free for ReLU/PL          — new even vs Bubeck–Sellke;
  (C) both together                 — the full conjecture.

## Where the log comes from (diagnosis)
Single-scale union bound over an eps-net of a PARAMETRIC class: log N(u) ~ md log(B/u).
Dudley does NOT remove it (parametric entropy integrates to Delta sqrt(md log(aspect)));
the aspect ratio ~ sqrt(d) or md is real. Removal needs the class's finer geometry
(ellipsoid-like bodies where gamma_2 beats Dudley), i.e. majorizing measures.

## Key structural discoveries (mine, today)
1. REDUCTION TO RADEMACHER: for BLN's setting (y iid +-1 independent of x), the whole
   theorem is: whp over x,  E_y sup_{f in A_L} (1/n) sum y_i f(x_i) < eps/8  for
   L <= c eps sqrt(n/m).  A_L = {width-m psi-nets, Lip<=L, clipped}.  So the conjecture
   IS a sharp Rademacher-complexity bound: R_n(A_L) <= C kappa L sqrt(m/n), log-free.
2. GRADIENT-GRAM ELLIPSOID: E|grad f|^2 <= L^2 gives alpha^T M alpha <= CL^2 with
   M_{kl} = <u_k,u_l> E[psi'_k psi'_l 1_active] — an ELLIPSOID constraint on coefficients
   (activation-agnostic!). Plus POINCARE on S^{d-1}: centered value-Gram <= M/(d-1).
   Population part of the correlation then gives EXACTLY the conjectured threshold
   sqrt(n/m) — LOG-FREE. The battle: empirical-vs-population Gram gap for SPIKY units
   (tiny caps / huge inner weights): empirical Gram has spikes ~1 vs population e^{-cd}.
   The spiky part is exactly what does the fitting in the matching construction, so it
   cannot be discarded — it must be handled by a localized argument (kink machinery for
   PL; ??? for smooth).
3. FOURIER/ZONAL NON-INTERFERENCE (the anti-cancellation weapon for general psi):
   a ridge g(<u,x>) lives in span{zonal harmonics Z_l^u}; distinct directions have
   distinct poles; level-l components of an m-ridge sum live in an m-dim zonal span of
   H_l. Cancellation across directions lives ONLY at level 0/1 (Fourier: lines through
   the origin intersect only at 0 = the polynomial ambiguity of Pinkus). The Lip
   constraint forces the JOINT across-level ellipsoid  sum_l lambda_l ||f_l||_2^2 <= E|grad f|^2 <= L^2
   (lambda_l = l(l+d-2)). So the class embeds in
       E := { f : f_l in m-dim zonal span, sum_l lambda_l ||f_l||^2 <= L^2, |f|<=1 }.
   Complexity of E = per-level sups over pole-configurations (this is where md log
   enters — acceptable for deliverable (A)).
4. MOLLIFICATION SPLIT (kills the high-frequency tail POINTWISE, no probability):
   f = f*eta_h + (f − f*eta_h) with h = eps/(8L): the high part is <= Lh = eps/8
   pointwise, so its correlation contribution <= eps n/8 deterministically. Mollification
   preserves ridge structure (Funk–Hecke). Low part is bandlimited-ish to l <~ 1/h = 8L/eps.
5. TRIVIAL FLOOR: any interpolant of +-1 labels on ~sqrt2-separated points has
   Lip >= sqrt2 — so the conjecture has content only for m << n; at m >~ n it is
   trivially true. The log-gap question lives at m << n.
6. DISPROOF SIDE IS LIVE: our lower bound is sqrt(n/(m log)); if a width-m net can fit
   with Lip ~ sqrt(n/m)/sqrt(log) then the literal (log-free) conjecture is FALSE and
   that ALSO resolves the open problem. Must be hunted seriously (S3).

## Known failure modes to respect
- Per-profile operations (mollify/PL-approximate each ridge) die on cancellation.
- Naive sum-splitting of Rademacher complexity loses m vs sqrt(m).
- Zonal per-level union bounds accumulate sum_l sqrt(log l / l) divergences — need the
  joint ellipsoid (Cauchy–Schwarz across levels against sum lambda ||f_l||^2 <= L^2),
  not per-level sups added.
- Empirical zonal feature processes: ||P_V T_l|| for ill-conditioned clustered-pole spans
  is NOT <= sqrt(m) max-zonal-coefficient. Need the variety-of-m-zonal-combinations
  Gaussian width, or a Gram-free argument.
- Golowich–Rakhlin–Shamir log-free trick handles NORM balls (path norm), not Lip balls;
  rigidity gives sum|alpha| <= 2Lm which via path-norm gives only L*m (not L*sqrt(m)) —
  useful only for m small; but their exp-moment device may compose with the ellipsoid.

## Threads
- MAIN (me): zonal/Funk–Hecke program for (A): exact conventions, joint-ellipsoid
  chaining, mollification split; write MASTER notes as I go.
- S1: log-removal for PL class: gamma_2 of the Lip-ball two-layer class; ellipsoid/
  interlacing; where exactly Dudley is beaten; partial regimes (m <= n/d etc.).
- S3: construction hunt (disproof side): beat sqrt(n/m) by polylog with real two-layer
  ReLU nets; multi-point caps; hierarchical profiles; numerics allowed.
- S4: literature: log-free precedents; GRS trick; sharp Rademacher of Lipschitz-
  constrained nets; anything post-2021 on BLN; majorizing measures for parametric unions.

## Verification discipline
Nothing enters the paper without a complete written proof + adversarial referee passes.
Partial results are banked honestly with their exact regimes.
