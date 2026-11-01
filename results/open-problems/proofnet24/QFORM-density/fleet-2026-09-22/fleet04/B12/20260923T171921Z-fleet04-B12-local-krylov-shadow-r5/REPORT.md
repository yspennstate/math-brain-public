# B12 — local Krylov-shadow stability on an actual coordinate carrier

Run: 20260923T171921Z-fleet04-B12-local-krylov-shadow-r5

Status: **new supporting theorem proved; full QFORM remains open.**

## Theorem 1: local Krylov shadow

Let A0 and S be real symmetric n-by-n matrices, U = Ran(S), and H a set of original coordinates with coordinate projection P_H. Define

    K_H = P_H(U + A0 U),       q_H = dim K_H.

For k + q_H <= |H|,

    lambda_k( ((A0+S)^2)[H,H] )
      >= lambda_(k+q_H)( (A0^2)[H,H] ).                 (1)

If R is symmetric, ||R||op <= epsilon, and A=A0+S+R, then

    sqrt(lambda_k((A^2)[H,H]))
      >= (sqrt(lambda_(k+q_H)((A0^2)[H,H]))-epsilon)_+. (2)

The signs and magnitudes of all eigenvalues of S are unrestricted.

### Proof

Set B=A0+S. The exact identity

    B^2-A0^2 = A0 S + S A0 + S^2

implies Ran(B^2-A0^2) is contained in A0 U + U. Hence

    Ran(P_H(B^2-A0^2)P_H) is contained in P_H(A0 U+U)=K_H,

so the compressed difference has rank at most q_H. Hermitian rank interlacing proves (1).

For every symmetric M,

    sqrt(lambda_k((M^2)[H,H])) = s_k(M P_H),

because (M P_H)^T(M P_H)=P_H M^2 P_H on the coordinate space H. Weyl's singular-value perturbation inequality gives

    s_k(A P_H) >= s_k(B P_H)-||R P_H||op
               >= s_k(B P_H)-epsilon.

Together with (1), this proves (2).

This is sharper than fleet01/B12's global reserve q=dim(U+A0U): the actual carrier pays only q_H=dim P_H(U+A0U). If U is outside H, the direct U part is invisible and only P_H A0 U is charged. Thus r arbitrary signed outside modes can cost r rather than 2r reserve directions.

## Corollary 2: localized high/low spectral split

For a symmetric addition E=sum_j theta_j v_j v_j^T and threshold h, split

    S_h = sum_{|theta_j|>h} theta_j v_j v_j^T,
    W_h = sum_{|theta_j|<=h} theta_j v_j v_j^T.

Then ||W_h||op<=h. Put U_h=Ran(S_h) and
q_H(h)=dim P_H(U_h+A0 U_h). For any further dense symmetric T with ||T||op<=delta,

    sqrt(lambda_k(((A0+E+T)^2)[H,H]))
      >= (sqrt(lambda_(k+q_H(h))((A0^2)[H,H]))-h-delta)_+. (3)

Large signed modes are therefore charged only through their one-step physical shadow. The low modes and dense tail are used only to preserve an actual matrix spectral gate; neither X^T W_h X nor X^T T X is treated as a small random error.

## Concrete exact-target application of fleet01/B12

Let R^16=H direct-sum J with |H|=|J|=8 and

    A0 = [[0, 2 I8],
          [2 I8, 0]].

Let f1,f2 be two coordinate vectors in the outside bank J and set

    S = tau1 f1 f1^T + tau2 f2 f2^T,

with arbitrary real tau1,tau2. Here U is contained in J and
P_H A0 U=span(e1,e2). Therefore q_H=2, although the global footprint can have dimension four.

Because A0^2=4 I16, (2) with k=6 and any globally dense symmetric T satisfying ||T||op<=1/4 gives the actual principal-block gate

    sqrt(lambda_6((A^2)[H,H])) >= 2-1/4 = 7/4,
    lambda_6((A^2)[H,H]) >= 49/16.                     (4)

Since rank(S)<=2, singular-value rank interlacing and Weyl perturbation also give

    s_3(A) >= s_5(A0)-1/4 = 7/4 > 1.                  (5)

Thus this is literally within the owner's three-large-eigenvalue target.

Apply the completed fleet01/B12 physical spectral-square compiler (equation (5) of its report) with

    m=8, N=28, s=g=7/4, b=17/10, a=3/70, kappa=1/56.

Its four exhaustive physical exits are below, respectively,

    573.063, 175.930, 576.490, 28.070.

Consequently, for every cap-one product input, all tau1,tau2 in R, and every dense symmetric T with ||T||op<=1/4,

    ||p_(X^T A X)||infinity < 577.                     (6)

Compared with the fleet01 example, (6) permits two arbitrary signed unbounded outside modes on the same eight-coordinate carrier: the local shadow pays one reserve direction per mode, not the two-direction global Krylov footprint.

## Remaining obstruction

The full conjecture remains open. The missing structural step is to extract from s_3(A)>=1 alone an original-coordinate carrier with enough spectral-square reserve after paying q_H(h), or route failure into an already controlled physical minor, ridge, hub, or bank exit. Continuity is not claimed.

## Source pins

- math-open-problems live head before publication: 175ac74eb73ef3444ec1a6d998b78a02e72104f2.
- fleet01/B12 report blob: 1546765370c2190e877afbe759cfd9148d593642.
- required Claude baseline: e5f71d79eff325201dd0274053d20268ce65b837.
- brain control head after sign-in: 040cea5990b92a843de4ef56b19221f4f3b90c72.
