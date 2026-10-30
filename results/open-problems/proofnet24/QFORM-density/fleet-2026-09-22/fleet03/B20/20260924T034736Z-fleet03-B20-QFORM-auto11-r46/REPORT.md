SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-24T03:47:36Z.
attacking: the r45 two-sided nested rank-two survivor by forcing all three balanced four-bank physical cuts either through the completed E3 receiver or into simultaneous rank-two tubes.

# fleet03/B20 r46 — three-cut rank-two gluing of the nested physical carrier

Status: **NEW SUPPORTING CLOSURE THEOREM / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The target remains the exact owner target: independent original real coordinates with probability densities bounded by one and arbitrary symmetric coefficient matrix A with at least three eigenvalues of modulus at least one. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, spectral-coordinate-independence, arbitrary-joint coarea, fiber-supremum, or pointwise quadratic-phase-decay assumption is used. Every source bank below is a literal subset of the original independent coordinates. Orthogonal changes appear only inside deterministic coefficient-matrix singular-value calculations.

## 1. Fresh inherited frontier and analytic receiver

The immediate predecessor is fleet03/B20 r45,

`yspennstate/math-open-problems@9e25c4e61cfe9aa9700419517b5d73b72a3e1fb1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260924T031641Z-fleet03-B20-QFORM-auto11-r45/REPORT.md`.

It starts from fleet03/B19 r48 and reduces one live chamber to disjoint original-coordinate banks R,C with

    N=A[R,C],
    dist_F(N,rank<=2)<tau,             tau=2^-16,
    s2(N)>=1/64,
    s1(N)s2(N)>gamma0,

gamma0 = 28159/(4194304 sqrt(2))
       = 0.004747252428873060164357...

The r45 diffuse branch already constructs one internal physical split on each side, but does not yet glue the two splits together.

The analytic receiver used below is fleet03/B04 r42, source commit

`yspennstate/math-open-problems@563bc41e4f9247f9daf3343a57757f45e3f6e703`.

For every literal disjoint original-coordinate cross block M,

    ||p_Q||_infinity <= C_E3 E3(M)^(-1/6),
    C_E3 = 8.4530212255281768747049...,

whenever E3(M)>0. The full ambient law is controlled, arbitrary same-bank quadratic terms and outside couplings are retained, and the paid branch has a continuous C_0 density.

## 2. New deterministic one-singular-value E3 gate

For a real matrix M let its squared singular values be

    x1>=x2>=...>=0,

and write

    E2(M)=e2(x),
    E3(M)=e3(x),
    T2(M)=sum_{k>=3} xk
         =dist_F(M,rank<=2)^2.

### Theorem 2.1 — QFORM-ONE-SINGULAR-TO-R2-E3-v1

For every real matrix M,

    E3(M) >= (1/3) s1(M)^2 dist_F(M,rank<=2)^4.              (2.1)

Proof. First,

    E2(M)=sum_{i<j} xi xj
          >= x1 sum_{j>=2} xj
          >= x1 T2.                                           (2.2)

Also, for every pair i<j,

    sum_{k notin {i,j}} xk
      >= sum_k xk-x1-x2
      =T2,                                                     (2.3)

because xi+xj<=x1+x2. Multiplying (2.3) by xi xj and summing over i<j counts each cubic monomial xi xj xk exactly three times, so

    3 E3(M)
      =sum_{i<j} xi xj sum_{k notin {i,j}}xk
      >=T2 E2(M)
      >=x1 T2^2.                                               (2.4)

Since x1=s1(M)^2, (2.1) follows. QED.

This gives a useful robust dichotomy: if s1(M)>=c and dist_F(M,rank<=2)>=eps, then

    E3(M)>=c^2 eps^4/3,                                       (2.5)

so the completed physical-E3 receiver pays the full law with

    ||p_Q||_infinity
      <= C_E3 (c^2 eps^4/3)^(-1/6).                           (2.6)

No lower bound on E2 is needed for this version.

## 3. Apply the designated fleet04/B20 result on both live singular directions

Let

    N2=s1 u1 v1^T+s2 u2 v2^T,
    E=N-N2,
    ||E||_F<tau=2^-16.

We first retain the existing heavy-coordinate exits: if

    max_j v2(j)^2>=1/4

or

    max_i u2(i)^2>=1/4,

then r45 already gives a literal physical hub arm of norm at least 1/128 on the corresponding side. That is still an unpaid finite-hub packet, so the new work concerns the fully diffuse case

    max_j v2(j)^2<1/4,
    max_i u2(i)^2<1/4.                                        (3.1)

Apply the designated partner fleet04/B20 r11 theorem `QFORM-DIFFUSE-SCHUR-THREEBANK-PACKET-v1` first to h=v2. It supplies a partition of C into three disjoint original-coordinate banks K_1^C,K_2^C,K_3^C with

    W_1^C W_2^C W_3^C>1/108,
    W_b^C=sum_{j in K_b^C}v2(j)^2.                             (3.2)

Let V=[v1 v2] and G_b^C=V^T P_{K_b^C}V. Since sum_b G_b^C=I_2,

    sum_b det(I_2-G_b^C)
      =1+sum_b det(G_b^C)
      >=1.                                                     (3.3)

Choose U_C=K_{b_C}^C so that, with J_C=C\U_C,

    G_C:=V^T P_{J_C}V=I_2-G_{b_C}^C,
    det G_C>=1/3,
    lambda_min(G_C)>=1/3,                                     (3.4)

and, because every W_b^C>1/108,

    ||P_{U_C}v2||_2^2>1/108.                                  (3.5)

Apply the SAME completed fleet04/B20 result to h=u2 on the R side. With U=[u1 u2], obtain a literal split R=U_R disjoint_union J_R such that

    G_R:=U^T P_{J_R}U,
    det G_R>=1/3,
    lambda_min(G_R)>=1/3,                                     (3.6)

and

    ||P_{U_R}u2||_2^2>1/108.                                  (3.7)

This is an equation-level use of the designated partner on the actual live rank-two carrier, not a generic citation.

## 4. The central physical cell retains both singular directions

Define the literal central main-cross cell

    Z=N[J_R,J_C].                                              (4.1)

Its rank-two core is

    Z0=U_{J_R} Sigma V_{J_C}^T,
    Sigma=diag(s1,s2).                                        (4.2)

The product of the two nonzero singular values of Z0 is exactly

    s1(Z0)s2(Z0)
      =s1 s2 sqrt(det G_R det G_C)
      >=gamma0/3.                                              (4.3)

Also

    s2(Z0)
      >=s_min(U_{J_R}) s2 s_min(V_{J_C})
      >=s2/3
      >=1/192.                                                 (4.4)

The retained coefficient tail satisfies

    ||Z-Z0||_op<=||E||_F<tau.                                  (4.5)

Weyl therefore gives

    s2(Z)>beta_C:=1/192-2^-16
                    =1021/196608
                    =0.0051930745442708333...,                 (4.6)

and, writing a>=b for the two nonzero singular values of Z0,

    s1(Z)s2(Z)
      >=(a-tau)(b-tau)
      >=ab(1-tau/(1/192))^2
      >Gamma_C,                                                (4.7)

where

    Gamma_C
      :=gamma0/3 (1-3/1024)^2
      =0.0015731590808890220994289....                          (4.8)

Every term here is physical-source preserving; the SVD is only coefficient algebra.

## 5. First checkerboard cut: robust E2 either pays or globally glues the two nested crossings

Use the four physical banks

    A=J_R,  B=U_R,  C0=J_C,  D=U_C.

Consider the checkerboard cut

    L2=B union C0,
    R2=A union D,

and its literal physical cross block

    W2=A[L2,R2]
      =[[ A[B,A],   A[B,D] ],
        [ A[C0,A],  A[C0,D] ]].                               (5.1)

The subblock A[C0,A]=Z^T. Therefore positivity of the squared physical 2x2 minors gives

    E2(W2)>=E2(Z)>= [s1(Z)s2(Z)]^2>Gamma_C^2.                  (5.2)

The exact counting inequality used already in r43 is

    dist_F(W2,rank<=2)^2 E2(W2)<=3E3(W2).                      (5.3)

Take

    eps=2^-12.                                                 (5.4)

If dist_F(W2,rank<=2)>=eps, then

    E3(W2)>delta_2
      :=Gamma_C^2 eps^2/3
      =4.9170444285543616153e-14.                              (5.5)

The physical-E3 receiver then pays the FULL ambient law, continuously, with

    ||p_Q||_infinity
      < C_E3 delta_2^(-1/6)
      =1396.5653761655613...
      <1397.                                                    (5.6)

Hence every still-unpaid fully diffuse state obeys

    dist_F(W2,rank<=2)<2^-12.                                  (5.7)

This is stronger than having two unrelated nested rank-two self-crossings: one rank-two tube now controls the whole literal checkerboard crossing, simultaneously including both nested self crossings and two pieces of the original R-C crossing.

## 6. Second checkerboard cut: one partner-certified arm is enough

Now use the third balanced cut

    L3=A union C0,
    R3=B union D,

with literal physical cross block

    W3=A[L3,R3].                                               (6.1)

The subblock

    P=N[J_R,U_C]                                               (6.2)

is contained in W3. Its rank-two core is

    P0=U_{J_R} Sigma V_{U_C}^T.                                (6.3)

From (3.4) and (3.5),

    ||P0||_F
      >=s_min(U_{J_R}) ||Sigma V_{U_C}^T||_F
      >= (1/sqrt3) s2 ||V_{U_C}||_F
      > (1/sqrt3)(1/64)(1/sqrt108)
      =1/1152.                                                  (6.4)

Since rank(P0)<=2,

    ||P0||_op>1/(1152 sqrt2).                                  (6.5)

The original nonzero cross tail is retained and only bounded deterministically:

    ||P-P0||_op<=tau.                                          (6.6)

Thus

    s1(W3)>=||P||_op>c0,                                       (6.7)

where

    c0:=1/(1152 sqrt2)-2^-16
       =0.00059854918071748917048684....                        (6.8)

Apply Theorem 2.1 to the ACTUAL physical W3. If

    dist_F(W3,rank<=2)>=eps=2^-12,                              (6.9)

then

    E3(W3)>delta_3
      :=c0^2 eps^4/3
      =4.2426639592650103554e-22.                              (6.10)

The completed physical-E3 receiver pays the full ambient law continuously with

    ||p_Q||_infinity
      <C_E3 delta_3^(-1/6)
      =30837.004703908822...
      <30838.                                                   (6.11)

Therefore every fully diffuse state surviving both E3 exits has

    dist_F(W3,rank<=2)<2^-12.                                  (6.12)

The constant is large but universal. The gain is structural: no E2 lower bound for W3 and no noncancellation assumption on its four block entries is needed.

## 7. Three physical two-color cuts are now simultaneously rank-two thin

The inherited original cut is

    C1: (A union B) | (C0 union D) = R|C,

with cross matrix N satisfying

    dist_F(N,rank<=2)<2^-16.                                   (7.1)

Sections 5 and 6 give, unless the full target is already paid continuously,

    C2: (B union C0) | (A union D),
        dist_F(W2,rank<=2)<2^-12,                              (7.2)

    C3: (A union C0) | (B union D),
        dist_F(W3,rank<=2)<2^-12.                              (7.3)

These are the three balanced 2+2 cuts of the same four ORIGINAL source banks.

Let S_off be the symmetric four-bank off-diagonal coefficient matrix on H=R union C obtained from A[H,H] by zeroing the four within-bank principal blocks A[A,A], A[B,B], A[C0,C0], A[D,D]. Let S_k be the symmetric coefficient matrix retaining exactly the edges crossing cut Ck. Every unordered pair of distinct four-bank vertices is separated by exactly two of the three balanced cuts, hence the exact combinatorial identity

    S_1+S_2+S_3=2 S_off.                                       (7.4)

Choose rank-at-most-two approximants L1,L2,L3 to the three cross matrices realizing the Frobenius bounds above, and let tilde(Lk) denote the corresponding symmetric off-diagonal extension. Each tilde(Lk) has rank at most four. Define

    K=(tilde(L1)+tilde(L2)+tilde(L3))/2.                        (7.5)

Then

    rank K<=12,                                                (7.6)

and because the operator norm of [[0,E],[E^T,0]] equals ||E||op,

    ||S_off-K||op
      <=(1/2)(2^-16+2*2^-12)
      =33/131072
      =0.00025177001953125.                                    (7.7)

### Theorem 7.1 — QFORM-R48-THREECUT-R2-GLUING-v1

In the fully diffuse r48/r45 survivor, either the entire ambient QFORM law already has a continuous C_0 density with

    ||p_Q||infinity<30838,                                     (7.8)

or the carrier support H=R union C admits a four-bank original-coordinate partition for which ALL inter-bank curvature is, in operator norm, within 33/131072 of one symmetric rank-at-most-twelve coefficient matrix. Equivalently,

    A[H,H]
      =diag(A[A,A],A[B,B],A[C0,C0],A[D,D]) + K + E_H,          (7.9)

with

    rank K<=12,
    ||E_H||op<33/131072.                                       (7.10)

No within-bank block is modified or assumed small. This is not a random-perturbation deletion: E_H remains part of the coefficient matrix, and (7.10) is only a deterministic normal form for the next proof step.

The heavy-v2 or heavy-u2 alternative remains the previously explicit physical hub packet with arm norm at least 1/128. Thus the old

    hub4 OR two-sided nested-rank-two

frontier is sharpened to

    finite physical hub OR four-bank rank<=12 off-diagonal carrier

with a completely explicit retained operator tail, unless the target law is already paid by a physical E3 crossing.

## 8. Why this implication matters and exact next debt

The previous nested packet left two independent-looking same-bank rank-two tubes. The new result shows that, after the designated partner's source-valid split is made on BOTH sides, the three balanced cuts cannot remain geometrically unrelated. Any failure of the second or third cut to be rank-two thin creates a literal physical third-volume and the marginal-free E3 theorem pays the entire ambient law. Therefore the unpaid diffuse chamber has finite-rank inter-bank geometry simultaneously in all three physical two-colorings.

The next closure interface is

    QFORM-R48-HUB-OR-FOURBANK-R12-OFFDIAGONAL-PAYMENT-v1.

One must now either:

1. pay the finite physical-hub branch with arm >=1/128; or
2. exploit (7.9)-(7.10) jointly with the four untouched within-bank quadratic blocks and the original s3(A)>=1 hypothesis, retaining arbitrary outside couplings and extra spectrum.

A valid next mechanism could be a recursive same-bank descent that proves substantial remaining curvature lives inside one principal bank, or a product-safe finite-rank receiver for the simultaneous three-cut carrier. A bounded density of a projected finite-dimensional marginal alone is NOT enough, by the live arbitrary-joint coarea correction.

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**. Continuity is proved in this report only on the explicit E3 exits (5.6) and (6.11).

## 9. Numerical checks

Using high-precision arithmetic:

    gamma0 = 0.004747252428873060164357036684157954...
    Gamma_C = 0.001573159080889022099428975956621266...
    beta_C = 0.005193074544270833333333333333333333...
    delta_2 = 4.917044428554361615310257625170480e-14
    C_E3 delta_2^(-1/6) = 1396.5653761655612943...
    c0 = 0.0005985491807174891704868440643271259...
    delta_3 = 4.242663959265010355446559969385074e-22
    C_E3 delta_3^(-1/6) = 30837.0047039088220417...
    (tau+2 eps)/2 = 33/131072 = 0.00025177001953125.

All constants are universal and dimension-free.
