# The localization tail lemma: the statement as it now stands (iter 130, 2026-08-10)

ENTRY POINT ONLY. This page states the lemma, its hypotheses and its constants in one place, so a
referee can see the object before reading how it got here. It ADDS NOTHING and PROVES NOTHING: every
proof, every gap resolution and every correction lives in localization_tail_draft_iter106.md, whose
layered record - six gap entries, several of them corrections of my own earlier text - is the
authority. Where this page and the draft disagree, the DRAFT is right and this page is a defect.

## Setting

Z^2 bond first-passage percolation, iid weights in [a_w, b], 0 < a_w <= b < infinity. T(x,y) is the
passage time, g the limit shape's norm. Free geodesics; no uniqueness assumed. W_r := sqrt(r Q_r)
with Q_r := sqrt(r) the Kesten-scale envelope, so W_r = r^{3/4}. (W is the construction's own
block-height scale; at a fluctuation-scale envelope Q_r = r^chi it would read W_r = r^{(1+chi)/2},
which is r^xi under the KPZ relation - see CRUX 9.7.)

## Hypotheses

(P-conc)  PUBLISHED, UNCONDITIONAL. Kesten-scale concentration for free passage times, uniform over
          directions: P(|T(x,y) - E T(x,y)| >= t sqrt|x-y|) <= C1 exp(-c1 t) for t <= C2 sqrt|x-y|.
(P-Alex)  PUBLISHED, UNCONDITIONAL. E T(x,y) <= g(y-x) + C3 sqrt|y-x| log|y-x|, uniform over
          directions.
(H-curv-LOWER)  NOT PUBLISHED FOR Z^2 - the lemma's only conditional input. One-sided enclosing-ball
          curvature at e_2 on an arc: for endpoint directions u in the arc and transversal
          displacement d <= delta r,
              g(v) + g(x - v) - g(x) >= c_- d^2 / r,   x = r u, v at transversal distance d.
          This is the side Newman-Piza print; it is NOT the upper pinning (c_+) that the dive
          construction consumes. The two one-sided conditions do different jobs and are listed
          separately in every ledger (draft section 3).

## The lemma

For the free geodesic between endpoints at distance r in the arc, with the required wlogs
delta <= min(1, 3 C2/c_-) and c1 <= 3 sqrt(2 + b/a_w)/C3 [SYNC 2026-08-12: the c1 wlog is REF3's,
previously missing here], and r >= r_0 (the validity floor - the range below is EMPTY for r < r_0,
measured 1e5.5-1e14 depending on constants; REF3):

  FORM A.  P( transversal deviation >= sigma W_r )  <=  12 C1 (b/a_w) r exp( - c'' c_- sigma^2 ),
           c'' = c1 / ( 6 sqrt(2 + b/a_w) ),                    for sigma^2 <= (delta^2/4) sqrt(r).
           [SYNC 2026-08-12: prefactor 12 not 18, range /4 - REF3's corrections, applied in the
           draft at iter 162 and previously missing from this page.]

  FORM B.  P( . )  <=  exp( - (c''/2) c_- sigma^2 )
           once sigma^2 >= (2/(c'' c_-)) log( 12 C1 (b/a_w) r ),      same range.

  ONE-SIDED. The wall-ward-only version holds with half the union (draft G-e); the consumer's
  touching events are exactly this cheaper half.

  U[1,2] INSTANTIATION. b/a_w = 2, so c'' = c1/12 in Form A and c1/24 in Form B.

In (H-wand)'s notation this is a stretched-exponential tail with theta = 2 - Gaussian in sigma,
stronger than the theta > 0 any consumer needs, on exactly the polylog quantile range they use.

## Why the exponent carries no power of r

At D = sigma W_r the curvature gain is c_- D^2/r = c_- sigma^2 sqrt(r), while the concentration
normalization spends sqrt(pair length) ~ sqrt(r). The two square roots cancel exactly - this is the
chi' = 1/2 versus xi' = 3/4 scaling identity, not an accident of the bookkeeping.

## The six named gaps and where they stand

  G-a  seam and grid            RESOLVED (iter 108): no seam - the through-vertex sits at level
                                exactly ceil(D), subpath optimality gives the inequality EXACTLY,
                                and the union is LINEAR in r, not quadratic.
  G-b  leg directions, far band RESOLVED (iter 108) + MACHINE-CHECKED (iter 109): deviations beyond
                                r(b-a_w)/(2a_w) are deterministically impossible; (P-conc) is
                                direction-uniform, and the arc constrains only the endpoint pair.
  G-c  the constant chase       RESOLVED (iter 114): all constants above, plus the range ledger
                                C''' = delta^2 under the stated wlog.
  G-d  the half-plane version   DISSOLVED (iter 107): the dependency graph shows no consumer needs
                                a confined-geodesic tail; revival clause stands if a referee finds
                                one.
  G-e  one-sidedness            RESOLVED (iter 110): half the union.
  G-f  endpoint uniformity      RESOLVED (iters 128-129), the caveat both consumers carried: the
                                union over boundary pairs needs no conditioning (subpath
                                optimality + containment), the pair count is bounded
                                DETERMINISTICALLY by G-b's band cap, and the cost is a constant
                                multiple of log n in the quantile. Steep crossings, which fall
                                outside the arc, are contained in a TOP-SCALE deviation event whose
                                endpoints are axis-aligned by construction - closed asymptotically,
                                for n above an explicit threshold n_0(M, theta, delta, c_-).
                                [SYNC 2026-08-12, REF3-7: tilt admissibility is theta <= 2 delta M,
                                and the honest threshold is n_0 = (16/(c'' c_-)^2)(M^3/theta^4)
                                log^2(C M n) - 4 to 9 orders above the earlier print. Totals
                                survive both.]

STATUS: every named gap closed, dissolved or priced. REFEREED iter 162 [SYNC 2026-08-12: this page
previously still said NOT REFEREED] - report problem/REFEREE3_localization_report.md; mechanism and
every exponent confirmed, four constants corrected, one hole closed by the referee's own
curvature-free repair (REF3-6: longitudinal overshoots die by convexity of g alone, so the union
restricts to the window as literally written). The whole object remains conditional on
(H-curv-LOWER), which is open on Z^2. Nothing here proves chi = 1/3 or bears on it directly.

## Who consumes it

  1. The dive document (I8_from_curvature_v2_iter82.md) - as (H-wand)'s tail form, retiring a
     citation debt. Wiring: theta = 2, C = 1, c = (c''/2) c_-; compatibility line A >= max(2, C3 c'')
     recorded on both sides ([V5-1], [V5-2]).
  2. The wall side (CRUX 9.6-9.7) - as the supplier of (L3), the block-count condition, applied at
     BLOCK scale and needing the polylog block height W := sqrt(log(Mn)) n^xi.
  3. [SYNC 2026-08-12] The wall side again (CRUX 9.9-9.10) - as the far-band tail closing the far
     remainders of (M1) and (M2), at quantiles sqrt(3 log n) and sqrt(5 log n) respectively, both
     inside Form A's corrected range.
Two consumer documents, one hypothesis (c_-); the iter-162 referee verdict covered both.
