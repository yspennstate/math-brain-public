SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-24T08:19:49Z.
attacking: partial source overlap in the complementary weighted-time splice — condition on the shared physical environment and apply Cauchy--Schwarz in the joint (time,environment) measure, never the false L1_t L2_fiber mixed norm.

# QFORM-CONDITIONAL-ENVIRONMENT-WEIGHTED-TIME-COMPILER-v1

Status: new supporting theorem and exact-target stress family. The unrestricted QFORM density conjecture remains OPEN. Unrestricted continuity remains OPEN.

## 1. First unpaid implication

The previous source-disjoint complementary-weight splice is not the correct endpoint. The next structural obligation is to find a physical environment W such that, after conditioning on W, one fresh-hub packet supplies a negative-half weighted L2 time budget and a disjoint two-slope packet supplies a positive-half weighted L2 time budget. The two packets may depend arbitrarily on the same W. The remaining debt is to obtain the needed conditional slope-density budgets from product provenance without invoking the known-false universal conditional projection-density moments. If no such environment exists, route to an already-paid joint three-slope/grouped-carrier receiver.

The live correction QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1 is respected: the argument below never uses

    int |t|^(-1/2) ||G_t||_2 dt.

It squares before integrating and applies Cauchy--Schwarz on the product measure dt dP_W.

## 2. Environment-conditioned complementary-weight compiler

Let W,U,V be independent physical coordinate blocks. Let

    Q = S(U,W) + T(V,W).

For fixed w define

    F_w(t) = E_U exp(i t S(U,w)),
    G_w(t) = E_V exp(i t T(V,w)).

Then conditional independence gives

    phi_Q(t) = E_W[F_W(t) G_W(t)].

Define the conditional weighted energies

    A_-(w) = int_R |t|^(-1/2) |F_w(t)|^2 dt,
    A_+(w) = int_R |t|^( 1/2) |G_w(t)|^2 dt.

Whenever E A_- and E A_+ are finite,

    int_R |phi_Q(t)| dt
      <= int E_W |F_W(t)G_W(t)| dt
      <= (E A_-)^(1/2) (E A_+)^(1/2).                 (2.1)

The second step is Cauchy--Schwarz on R x Omega_W applied to

    |t|^(-1/4)|F_W(t)|   and   |t|^(1/4)|G_W(t)|.

Consequently Q has a continuous C_0 density and

    ||p_Q||_infty <= (2 pi)^(-1) (E A_-)^(1/2)(E A_+)^(1/2).   (2.2)

This is strictly more flexible than unconditional source-disjointness: S and T may share all of W and hence need not be independent.

## 3. Plugging in the newest account03/B03 fresh-hub theorem

The newest compatible account03/B03 result r50 proves that, for a genuine cap-one hub H independent of the full light object, if

    S_w = a H^2 + 2 gamma H L_w + R_w,

and L_w has density cap M_-(w), then

    A_-(w) <= 8 sqrt(pi M_-(w)/|gamma|).               (3.1)

This theorem retains arbitrary dependence of R_w on the light object and uses Plancherel in the random linear slope, not a pointwise quadratic-phase estimate.

For the complementary packet, let H=(H_1,H_2) be two genuine cap-one hubs independent of its light object and suppose

    T_w = H^T B H + 2 L_w^T H + R_w,

where the two-dimensional slope L_w has joint density cap M_+(w). Writing

    g_t(h)=f_{H_1}(h_1)f_{H_2}(h_2) exp(i t h^T B h),

conditioning on the light object and applying Cauchy--Schwarz followed by two-dimensional Plancherel gives

    |G_w(t)|^2 <= min(1, pi^2 M_+(w)|t|^(-2)).          (3.2)

Indeed, after the change xi=2tl,

    int |hat g_t(2tl)|^2 dl
      = (4t^2)^(-1)(2pi)^2 int |g_t(h)|^2 dh
      <= pi^2/t^2.

Integrating (3.2) at the exact crossover t_0=pi M_+(w)^(1/2) yields

    A_+(w) <= (16/3) pi^(3/2) M_+(w)^(3/4).             (3.3)

Combining (2.2), (3.1), and (3.3),

    ||p_Q||_infty
      <= 4 sqrt(2/3)
         [ E sqrt(M_-(W)/|gamma|) ]^(1/2)
         [ E M_+(W)^(3/4) ]^(1/2).                     (3.4)

Uniform conditional caps K_-,K_+ recover

    ||p_Q||_infty <= 4 sqrt(2/3) K_-^(1/4) K_+^(3/8),  (3.5)

but unlike the earlier splice no unconditional independence between the two packets is required.

## 4. Exact-target shared-environment family

Fix even N. Let v_1,v_2 in R^N be orthonormal flat sign vectors and independently let a_0,a_1 in R^N be orthonormal flat sign vectors. For example take the normalized all-plus and half-plus/half-minus vectors. Let

    delta = c = 2^(-1/2).

Take all scalar coordinates in

    H_0,H_1,H_2,Z, Y=(Y_1,...,Y_N), W=(W_1,...,W_N)

independent with real densities at most one, and set

    Q_N = 2 H_0[ delta Z + c <a_0,W> ]
        + 2 H_1[ delta <v_1,Y> + c <a_1,W> ]
        + 2 H_2 <v_2,Y>.                               (4.1)

The three rows of the physical hub-to-leaf crossing matrix are

    r_0 = delta e_Z + c a_0,
    r_1 = delta v_1 + c a_1,
    r_2 = v_2,

with disjoint Z/Y/W placements understood. They are exactly orthonormal. Therefore the symmetric quadratic matrix has nonzero spectrum

    {+1,+1,+1,-1,-1,-1}.                               (4.2)

So every Q_N lies exactly in the owner target.

Unconditionally the packets

    S = 2 H_0[delta Z + c<a_0,W>],
    T = 2 H_1[delta<v_1,Y> + c<a_1,W>] + 2 H_2<v_2,Y>

are not source-disjoint: both depend on the same physical W-bank. Orthogonality of a_0,a_1 does not make their projections independent for arbitrary product input laws.

Condition on the entire original W-bank. Then S uses only the fresh block (H_0,Z), while T uses only the fresh block (H_1,H_2,Y), so the conditional factorization of Section 2 is legitimate. For S, the conditional slope is a translate of delta Z and hence

    M_- <= delta^(-1) = sqrt(2).                        (4.3)

For T, the pinned e5f71d79... product-projection estimate gives

    ||p_(<v_1,Y>,<v_2,Y>)||_infty <= 2.                (4.4)

Scaling only the first coordinate by delta and translating it by c<a_1,W> gives

    M_+ <= 2 delta^(-1) = 2sqrt(2).                    (4.5)

Thus (3.5) yields the genuine one-copy bound

    ||p_Q_N||_infty
      <= 4 sqrt(2/3) (sqrt(2))^(1/4)(2sqrt(2))^(3/8)
      = 4 sqrt(2/3) 2^(11/16)
      = 5.259839398614899... .                          (4.6)

Hence every interval I satisfies

    P(Q_N in I) <= 5.259839398614899... |I|.            (4.7)

The proof gives an L1 characteristic function, so this family has a continuous C_0 density.

## 5. Assigned whole-copy decoupled-time quantity

The same conditioning keeps the independent-copy dependence bookkeeping intact. Since |G_W(t)|<=1, Jensen gives

    |phi_Q_N(t)|^2
      <= E_W |F_W(t)G_W(t)|^2
      <= E_W |F_W(t)|^2.

Therefore the partner r50 negative-half budget and (4.3) give directly

    int_R |t|^(-1/2)|phi_Q_N(t)|^2 dt
      <= 8 sqrt(pi sqrt(2))
      = 16.862517844086494... .                         (5.1)

Using only the whole-output identity

    |phi_Q_N(t)|^2 = E exp(i t (Q_N-Q_N')),

with Q_N' an independent copy of the entire scalar output, the regularized one-dimensional half-Riesz identity yields

    E|Q_N-Q_N'|^(-1/2)
      <= 4 sqrt(2sqrt(2))
      = 6.727171322029717... .                          (5.2)

No coordinatewise X-X' is separated from its conjugate X+X'.

After (4.6) is known, convolution preserves the density cap for Q_N-Q_N'. The elementary cap-to-half-Riesz estimate improves (5.2) to

    E|Q_N-Q_N'|^(-1/2)
      <= 2 sqrt(2 ||p_Q_N||_infty)
      <= 6.486810864278316... ,                         (5.3)

and equivalently

    int |t|^(-1/2)|phi_Q_N(t)|^2 dt
      <= 4 sqrt(pi ||p_Q_N||_infty)
      <= 16.260023524583584... .                        (5.4)

Also

    P(|Q_N-Q_N'|<=epsilon)
      <= 10.519678797229798... epsilon.                 (5.5)

## 6. Source-valid localization obstruction and pinned-source application

The positive-half packet is genuinely aggregate. Its 2 x (2N) physical slope coefficient matrix has rows

    (delta v_1 on Y, c a_1 on W),
    (v_2 on Y, 0 on W).

Every literal two-leaf 2 x 2 determinant has modulus at most

    sqrt(2)/N,                                          (6.1)

while the aggregate two-dimensional slope density remains bounded by 2sqrt(2), uniformly in N. Thus a proof that localizes the positive-half resource to one physical leaf pair necessarily loses scale on this family.

Moreover the whole quadratic matrix is zero-diagonal bipartite, so every physical principal 3 x 3 determinant is exactly zero. The completed physical-triple receiver cannot be the exhaustive mechanism here.

As an explicit application of the required pinned e5f71d79... package, Counterexample Search Theorem B gives

    ||p_Q||_infty <= 2sqrt(2pi) sum_i ||P e_i||,

where P is the range projection. For (4.1), the three hub coordinates contribute 3; Z contributes delta=1/sqrt(2); each Y-coordinate contributes sqrt(3/(2N)); and each W-coordinate contributes 1/sqrt(N). Hence the pinned theorem gives the valid inequality

    ||p_Q_N||_infty
      <= 2sqrt(2pi)
         [ 3 + 1/sqrt(2) + (1+sqrt(3/2))sqrt(N) ].      (6.2)

This diverges like sqrt(N), while (4.6) is dimension-free. It is therefore an actual obstruction to paying the remaining overlap branch through total range-projection mass or a single local two-slope minor.

## 7. What this does and does not settle

This theorem removes unconditional source-disjointness from the complementary-weight splice whenever the overlap can be parked in a physical conditioning environment with controlled conditional slope budgets. It does not assert universal bounds for the conditional caps or their moments; those are known-false interfaces in the unrestricted problem. The remaining structural task is to expose such an environment with product-valid averaged budgets, or prove that failure forces a joint three-slope/grouped-carrier receiver.

The unrestricted density conjecture remains OPEN. Unrestricted continuity remains OPEN.

Sources consumed: fresh brain owner/control files at main; newest compatible account03/B03 r50 handoff; pinned math-open-problems commit e5f71d79eff325201dd0274053d20268ce65b837 RESULTS.md, FOURIER_ROUTE_REPORT.md, COUNTEREXAMPLE_SEARCH.md. Execution context remains WITHOUT_VERIFIED_BRAIN.
