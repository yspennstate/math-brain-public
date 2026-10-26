# Huang Condition 1.3: verification plan and derivatives

Condition (con:2varfn): S_*(l1,l2) <= 0 for all (l1,l2) in R^2, where
S_*(l1,l2) = inf_{s>=0} S(l1,l2,s) and

  S(l1,l2,s) = s^2 psi/2 + ent(l) + alpha T(a1(l), a2(l), s).

Here, with x ~ N(0,psi) (the dbH variable), M = tanh(x),
u(x) = l1 x + l2 tanh(x), Lam = tanh(u):

  ent(l) = E_x[ log 2cosh(u) - u Lam ]        (binary entropy identity)
  a1(l)  = E_x[ x Lam ],   a2(l) = E_x[ M Lam ]

and with zt ~ N(0,1), Ht = sqrt(q) zt, N = E(-gamma zt)/sqrt(1-q),
gamma = sqrt(q/(1-q)), D = sqrt(1 - a2^2/q), W = -(a2/q) Ht - (a1/psi) N:

  T(a1,a2,s) = E_zt[ log Psi( W/D + s N ) ].

Everything is a one-dimensional certified integral; (alpha, q, psi) enter as
the Ding-Sun rectangle balls (now rigorously established by block 1).

Three regions.

## Region I: ball around (1,0)

Freeze the tilt at its (1,0)-optimal value s0 = sqrt(1-q). Since S_* is an
infimum over s, S_*(l) <= osS(l) := S(l1,l2,s0) for every l, with equality
at (1,0). Huang proves analytically (his Lemma 7.x / lem:sS-zero) that
osS(1,0) = 0 and grad osS(1,0) = 0, using the fixed point identities; his
appendix proves nabla^2 osS(1,0) is negative definite by interval arithmetic.
We extend the Hessian bound from the point to a ball: if
nabla^2 osS(l) <= -c I for all l in B((1,0), rho), then Taylor with the
exact center data gives osS(l) <= -(c/2)|l-(1,0)|^2, hence S_* < 0 on the
punctured ball. The Hessian entries at general l are computed below.

Sanity anchor: at l = (1,0), u = x, Lam = M, a2 = E[M^2] = q,
a1 = E[x M] = psi(1-q), D = sqrt(1-q), and V := W/D + s0 N = -gamma zt,
so E(V) = sqrt(1-q) N. All five kernel integrals then reduce to the
p4/r4-type quantities in Huang's appendix, giving an independent check
against his center Hessian [-0.0459, -0.0266; -0.0266, -0.0205].

## Derivatives of osS at general (l1, l2)

Write d_i = d/dl_i, f_1(x) = x, f_2(x) = tanh(x) (so d_i u = f_i, which is
independent of l). Then d_i Lam = (1-Lam^2) f_i and

  d_i ent = -E[ u (1-Lam^2) f_i ]
  d_i a1  =  E[ x (1-Lam^2) f_i ],   d_i a2 = E[ M (1-Lam^2) f_i ]

  d2_ij ent = -E[ (1-Lam^2) f_i f_j ] + 2 E[ u Lam (1-Lam^2) f_i f_j ]
  d2_ij a1  = -2 E[ x Lam (1-Lam^2) f_i f_j ]
  d2_ij a2  = -2 E[ M Lam (1-Lam^2) f_i f_j ]

For the constraint term, V = W/D + s0 N is linear in (Ht, N) given the
scalars, and so are its l-derivatives:

  d_i V = P_i Ht + R_i N,        d2_ij V = P_ij Ht + R_ij N,

  P_i = -(d_i a2)/(q D) - a2^2 (d_i a2)/(q^2 D^3)
      = -(d_i a2)/(q D^3) * (D^2 + a2^2/q) ... simplify: D^2 = 1 - a2^2/q so
  P_i = -(d_i a2)/(q D^3)
  R_i = -(d_i a1)/(psi D) - a1 a2 (d_i a2)/(q psi D^3)

  P_ij = -(d2_ij a2)/(q D^3) - 3 a2 (d_i a2)(d_j a2)/(q^2 D^5)
  R_ij = -(d2_ij a1)/(psi D) - [ (d_i a1)(d_j a2) + (d_j a1)(d_i a2) ] a2/(q psi D^3)
         - a1 (d2_ij a2) a2/(q psi D^3)
         - a1 (d_i a2)(d_j a2)/(q psi D^3)
         - 3 a1 a2^2 (d_i a2)(d_j a2)/(q^2 psi D^5)

  [P_i simplification check: -(x)/(qD) - a2^2 x/(q^2 D^3)
   = -(x/(q D^3)) (D^2 + a2^2/q) = -(x/(q D^3)) (1 - a2^2/q + a2^2/q)
   = -x/(q D^3).  Good.
   P_ij: differentiate P_i = -(d_i a2)/(q D^3):
   d_j P_i = -(d2_ij a2)/(q D^3) - (d_i a2) * (-3/(q D^4)) d_j D
   d_j D = -a2 (d_j a2)/(q D)
   => P_ij = -(d2_ij a2)/(q D^3) - 3 a2 (d_i a2)(d_j a2)/(q^2 D^5). Good.
   R_ij: differentiate R_i = -(d_i a1)/(psi D) - a1 a2 (d_i a2)/(q psi D^3):
   term1: -(d2_ij a1)/(psi D) - (d_i a1)(-1/(psi D^2)) d_j D
        = -(d2_ij a1)/(psi D) - (d_i a1) a2 (d_j a2)/(q psi D^3)
   term2: -[(d_j a1) a2 (d_i a2) + a1 (d_j a2)(d_i a2) + a1 a2 (d2_ij a2)]/(q psi D^3)
          - a1 a2 (d_i a2) (-3/(q psi D^4)) d_j D
        = -[...]/(q psi D^3) - 3 a1 a2^2 (d_i a2)(d_j a2)/(q^2 psi D^5)
   Collecting matches the display above (note term1 contributes the
   symmetric (d_i a1)(d_j a2) piece). ]

Then with E' the derivative of the inverse Mills ratio E,

  d2_ij T = -E[ E'(V) (d_i V)(d_j V) ] - E[ E(V) d2_ij V ]
          = -( P_i P_j K_hh + (P_i R_j + P_j R_i) K_hn + R_i R_j K_nn )
            - ( P_ij K_h + R_ij K_n ),

with the five kernels (functions of (a1, a2, s0) through V):

  K_hh = E[ E'(V) Ht^2 ],  K_hn = E[ E'(V) Ht N ],  K_nn = E[ E'(V) N^2 ],
  K_h  = E[ E(V) Ht ],     K_n  = E[ E(V) N ].

Finally nabla^2 osS = d2 ent + alpha d2 T, three entries (11, 12, 22) via
f_i f_j in {x^2, x tanh x, tanh^2 x}.

The x-integral list per lambda ball (12 integrals + the 3 for a1, a2, ent):
for w in {x^2, x M, M^2}:
  E[(1-Lam^2) w],  E[u Lam (1-Lam^2) w],  E[x Lam (1-Lam^2) w],
  E[M Lam (1-Lam^2) w].
Tails are trivial: every integrand is bounded by w or |u| w with u linear
in x, so Gaussian moment tails close them.

## Region II: compact middle

Boxes covering {|l - (1,0)| >= rho} intersected with |l1| <= R1, |l2| <= R2.
Per box: choose s_B by nonrigorous 1d minimization at the box center, freeze
it as a rational, certify S(l-box, s_B) < 0. The value evaluator needs
ent, a1, a2 (x-integrals with the lambda ball) and T (zt-integral with
interval a1, a2). Adaptive splitting: if a box fails, bisect; and grow boxes
geometrically away from the origin.

## Region III: tail

For max(|l1|, |l2|) large: ent -> 0 uniformly at an explicit rate while the
constraint term stays bounded away from 0:

  S_*(l) <= S(l, 0) = ent(l) + alpha T(a1, a2, 0)

(a) T(a1, a2, 0) <= -c0 < 0 uniformly over the compact range
    K = {|a1| <= sqrt(2 psi/pi), |a2| <= m1}, m1 := E|M| < sqrt(q):
    on a window zt in [w1, w2], the argument W/D of log Psi is bounded above
    by an explicit linear function of (a1, a2); since log Psi < 0 everywhere,
    E log Psi(W/D) <= P(window) * log Psi(sup of argument on window).
    c0 is then one certified number. m1 < sqrt(q) needs one integral:
    m1 ~ 0.6504 vs sqrt(q) ~ 0.7510, margin comfortable; this also bounds
    D >= sqrt(1 - m1^2/q) > 0 globally over all lambda.

(b) ent(l) small for large |l|: ent(l) = E ent2((1+tanh u)/2) with
    u = l1 x + l2 tanh x. Bound ent2((1+tanh u)/2) <= (2+2|u|) e^{-2|u|}
    (check: for p = (1+tanh u)/2, 1-p = 1/(1+e^{2u}) <= e^{-2u} for u >= 0,
    and ent2(p) <= (1-p) log(e/(1-p)) ... derive exact constant on
    implementation). Then split on |u| <= tau: ent <= log2 P(|u| <= tau)
    + (2+2tau) e^{-2tau}. The measure P(|u(X)| <= tau), X ~ N(0,psi), is
    controlled by the root structure of u: u(x) = l1 x + l2 tanh x has
    nonzero roots only where tanh x*/x* = -l1/l2 (possible only for signs
    opposite and |l2| > |l1|), and no nonzero double roots since
    (tanh x)/x = 1 - tanh^2 x has no positive solution
    (equivalently sinh(2x)/2 = x only at 0). At a nonzero root x*,
    |u'(x*)| = |l2| ((t/x*) - (1-t^2)) with t = tanh x* -- an explicit
    positive quantity; near 0, u(x) ~ (l1+l2) x - l2 x^3/3 covers the
    remaining mass, with the worst direction l1 + l2 = 0 giving
    P(|u| <= tau) = O((tau/|l2|)^{1/3}).
    Work out explicit constants; the target is ent(l) < alpha c0 for
    max(|l1|,|l2|) >= R with R explicit and moderate (expect R in the
    10^2..10^4 range; the region-II sweep then runs out to R with
    geometrically growing boxes, which costs only log(R) layers).

Division of labor between II and III is flexible: III's constants can be
crude since II's certified boxes can extend far out cheaply.

## REVISED PLAN (2026-07-07, after crash 3): moment coordinates

The (lambda1, lambda2) sweep has an unbounded domain (the tail, Region III)
whose slow anti-diagonal decay makes the tail lemma delicate. Reparametrizing
by the moments (a1, a2) = (E[X Lam], E[M Lam]) removes this entirely.

Because Lam_{l1,l2} = tanh(l1 X + l2 M) is the max-entropy profile for its own
moments, ent(l) = H(a1(l), a2(l)) where
    H(a1,a2) = max{ E ent2((1+Lam)/2): E[X Lam]=a1, E[M Lam]=a2, |Lam|<=1 }.
Hence, with G(a1,a2) = inf_{s>=0}[s^2 psi/2 + alpha T(a1,a2,s)],
    sup_{l1,l2} S_*(l1,l2) = sup_{(a1,a2) in R} [ H(a1,a2) + G(a1,a2) ],
and R = {|a1| <= sqrt(psi), a2^2 < q} is BOUNDED. The tail is gone.

Convex duality gives, for EVERY dual point (b1,b2),
    H(a1,a2) <= Phi(b1,b2) - b1 a1 - b2 a2,   Phi(b) = E log 2cosh(b1 X + b2 M),
so a finite dictionary {(b_k, Phi(b_k))} yields a certified piecewise-linear
upper bound on H with NO per-cell integration. The only per-cell integral is
T(a1,a2,s), one 1-D Gaussian integral, on a fixed grid whose z-data (N, N',
E(-gamma z)) is precomputed once. G <= s^2 psi/2 + alpha T for ANY fixed s, so
we pick the per-cell nonrigorous-optimal s.

Region II (the whole rectangle R minus a small box around (a1*,a2*) =
(psi(1-q), q)) is then a bounded, fast sweep: per cell certify
    min_k [Phi_k - b1_k a1 - b2_k a2] + s*^2 psi/2 + alpha T(cell, s*) <= 0.
Verified anchors (huanggrid.py, 2026-07-07): T(a1*,a2*,s0) = -1.08677 in 0.02s
(55x faster than adaptive), Phi(1,0) - a1* = 0.34364 = ent(1,0), and the
assembled value at (a1*,a2*) is 0 to 1e-5, confirming the reduction.

Region I is the small box around (a1*,a2*) [image of the lambda-ball around
(1,0)], handled by the frozen-tilt Hessian negative-definiteness (huangfun.py;
point Hessian already matches Huang's appendix brackets). Coordination:
Region I covers a lambda-ball B((1,0),rho); its image under l->(a1,a2)
contains the excluded (a1,a2) box, verified by a finite boundary check.

Implementation: huanggrid.py (certified fixed grid, Phi, T, S_moment),
huang_np.py (vectorized nonrigorous guide for tilts/duals), huang_sweep.py
(driver, to run on Azure for the full sweep).
