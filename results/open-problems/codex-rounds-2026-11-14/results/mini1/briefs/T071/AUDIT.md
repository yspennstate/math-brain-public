# Checks and attempted counterexamples

These are analytic checks of PROOF.md. No numerical experiment was run.

## 1. Independent generator calculation

In the order (three blocks, two blocks, one block), the defining rates give

    Q = [ -2    3/2    1/2
           0    -1      1
           0     0      0 ].

Every row sums to zero. Starting from three blocks, the forward equations are

    u_3' = -2u_3,
    u_2' = (3/2)u_3-u_2,
    u_1' = (1/2)u_3+u_2,

with initial values (1,0,0). Direct solution gives

    u_3(t) = exp(-2t),
    u_2(t) = (3/2)(exp(-t)-exp(-2t)),
    u_1(t) = 1-(3/2)exp(-t)+(1/2)exp(-2t).

This checks the transition probabilities in the grid argument without using
its first-event conditioning integral. The direct-triple probability by T is
the integral of its probability flux:

    integral_0^T (1/2)u_3(t) dt = (1-exp(-2T))/4.

At T=log 2, the three state probabilities are 1/4, 3/8, 3/8, summing to one.
The direct-triple probability is 3/16. The difference 3/8-3/16=3/16 is the
probability of absorption through two successive binary mergers by that time.
Thus endpoint absorption must not be confused with the direct-triple event.

## 2. Independent transform and normalization checks

Solve the discounted backward equations rather than multiplying independent
mixture transforms. Starting with two blocks, discounted absorption gives

    f_2(r) = 1/(1+r).

Starting with three blocks, discount at rate s until the first event; after
that event discount at rate r while two blocks remain. A first-step equation
gives

    (s+2) f_3(s,r) = 1/2 + (3/2) f_2(r),

hence

    f_3(s,r) = (r+4)/[2(s+2)(r+1)].

The limiting joint law can also be written as a measure with a diagonal and
an off-diagonal part in the (S,H) coordinates:

    P(S in du,H=0)      = (1/2) exp(-2u) du,
    P(S in du,H in dv)  = (3/2) exp(-2u-v) du dv,  v>0.

The total masses are 1/4 and 3/4 respectively. Integrating these expressions
against exp(-su-rv) gives the same transform. In particular:

| (s,r) | Transform |
|---|---|
| (0,0) | 1 |
| (1,0) | 2/3 |
| (0,1) | 5/8 |
| (1,1) | 5/12 |

The last entry is independently checked from C=S+H. The state equations give
the absorption density

    f_C(t) = (3/2)exp(-t)-exp(-2t).

Its Laplace transform is

    (3/2)/(1+s)-1/(2+s) = (s+4)/[2(s+1)(s+2)],

which equals the joint transform evaluated at r=s. The means under the
limiting law satisfy E S=1/2 and E H=3/4, so E C=5/4. Independently,

    E C = integral_0^infinity (u_3(t)+u_2(t)) dt
        = 3/2-1/4 = 5/4.

These are checks of the limiting law, not assertions that finite-N
expectations converge. Such assertions would require uniform integrability.

For a rate multiplier rho, direct replacement of all nonzero rates in Q by
rho times those rates gives

    f_2(r)=rho/(rho+r),
    (s+2rho)f_3(s,r)=rho/2+(3rho/2)f_2(r).

This reproduces the rate-rho transform in PROOF.md.

## 3. A counterexample to using only the separate marginals

The joint requirement in the theorem cannot be dropped. Let U be uniform on
(0,1) and define

    S = -(1/2)log U,
    H = 0                              if U <= 1/4,
        -log((1-U)/(3/4))               if U > 1/4.

Then P(S>t)=exp(-2t). Also P(H=0)=1/4; conditional on U>1/4, the variable
(1-U)/(3/4) is uniform on (0,1), so H has the required Exp(1) conditional law.
Thus both marginals are exactly the proposed ones.

Nevertheless, {S<log 2}={U>1/4} and {H=0}={U<=1/4} are disjoint, so

    P(S<log 2,H=0)=0.

For independent S and H the same probability is (3/4)(1/4)=3/16.
Taking H_N=H+1/N, keeping S_N=S, and choosing J_N uniformly and independently
gives exchangeable, strictly binary partition processes whose separate time
marginals converge correctly but whose joint limit, and hence genealogical
finite-dimensional limit, is wrong. This counterexample is an abstract binary
genealogy, not a construction of N-BBM.

## 4. Topology check with an explicit shrinking interval

On [0,2], for N>=2 let x_N be o until 1-1/N, then p_12 until 1, and then z.
Let y be o until 1 and z from time 1 onward. At every fixed collection of
times, x_N eventually agrees with y. Yet d_2(x_N,y)=1 for every N, since
every time change still sees the intermediate state p_12. This verifies the
mechanism of the J1 obstruction directly. It is compatible with, and does
not refute, finite-dimensional convergence.

## 5. Edge cases checked

- A sample of two does not suffice: Kingman's coalescent and the normalized
  Bolthausen–Sznitman coalescent both give an Exp(1) pair time. At three labels
  Kingman's first merger has rate 3 and has no direct-triple event, which
  differs from rate 2 and triple probability 1/4 here.
- Fixed spatial ranks must not be used as sample labels in the symmetry
  argument. Uniformly random sample labels supply the needed invariance.
- Brownian collisions are spatial coincidences and do not merge ancestors.
- Selection can remove one child immediately. This suppresses a possible
  sampled merger; it never adds a third child to a binary branch.
- At fixed N, event times are distinct. Two extremely close branching events
  are still two jumps, which is exactly what matters in J1.
- The atomic part of H occurs only in the limit. Positive finite-N holding
  times are allowed to approach zero; reconstruction at fixed times is still
  continuous away from S and C.
- An observation window bounded on the rescaled clock does not determine the
  full two-time transform. The increasing-history condition in Section 2 is
  needed for the stated global criterion; on a fixed window only censored
  statistics can be used.
- None of the results supplies a rate for the shrinking interval h_N, a
  physical normalization constant kappa, N-BBM merger probabilities, or a
  result for all finite samples.

No contradiction or missing case was found in the stated auxiliary theorem.
The unproved step is precisely the N-BBM-specific joint transform limit.
