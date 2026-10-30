SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B01, 2026-09-23T21:00:57Z.
attacking: QFORM-NEARNULL-PROJECTED-CROSS-ZERO-ROUTING-v1 by classifying the partner's W2=0 scalar-pivot endpoint before any reciprocal near-null scale is paid.

# Early checkpoint: W2=0 is globally diagonal plus rank two

Status: proved algebraic supporting lemma; full QFORM remains OPEN.

Let a literal physical pair P={p,q} have invertible principal block B=A[P,P]. Write the remaining coordinates as L, C=A[P,L], A0=A[L,L], and let

S=A/B=A0-C^T B^{-1}C

be the exact pair Schur complement in ORIGINAL coordinates. In the scalar-pivot notation used by fleet03/B01 (a=A_pp !=0, delta=det(B)/a, leakage ell, once-completed leaf matrix M), its exact overlap-two currency is

W2=a^2 sum_{k!=l}(delta M_kl-ell_k ell_l)^2
  =det(B)^2 sum_{k!=l} S_kl^2.

Hence W2=0 iff S is diagonal.

## Lemma QFORM-SCALARPIVOT-W2ZERO-DIAGRANK2-v1

If B is invertible and W2=0, then

A = D + R,
D = diag(0_P,S),
R = [[B,C],[C^T,C^T B^{-1}C]],
rank(R)<=2.

Indeed, with K=[B,C] (a 2-by-n matrix),

R = K^T B^{-1} K,

so rank R<=2, while the leaf block of D is precisely the diagonal Schur complement S.

Let d1>=d2>=... be the decreasing rearrangement of |diag S| and let s_j(.) denote singular values. If the full target hypothesis holds, s_3(A)>=1. Eckart-Young gives

  d1=||D||op >= s_3(A) >=1.                         (E1)

Moreover Horn's singular-value inequality with A=D+R gives

  s_3(A) <= s_2(R)+s_2(D)=s_2(R)+d2,              (E2)

so

  max{d2,s_2(R)} >= 1/2.                           (E3)

Thus the exact W2=0 endpoint cannot be spectrally empty: it contains a literal Schur-diagonal coefficient of magnitude at least one, and either a second Schur-diagonal coefficient of magnitude at least 1/2 or two rank-two completion singular directions of scale at least 1/2.

This is product-preserving: S is diagonal in literal leaf coordinates. No rotation of the input law is made.

## Required 20260922T211500Z volume tool applied at an actual obstruction

For every disjoint coordinate cut I|J, the diagonal D contributes nothing to A[I,J], while R has rank at most two. Hence

rank A[I,J] <=2,
e_3(A[I,J]^T A[I,J])=0,
e_5(A[I,J]^T A[I,J])=0.

Therefore Theorem D, its fractional-threshold extension D', and the unconditional fifth-volume theorem D5 from the required decoupling/Fourier report have identically zero currency throughout this W2=0 class. This is a concrete obstruction, not a failure of their proofs: the next receiver must spend the diagonal-plus-rank-two geometry rather than a 3- or 5-volume cut.

## Exact strict-N3 witness inside W2=0

Fix r=L=2. In R^2 choose feature rows

u_p=epsilon e1,  u_q=epsilon e2,
u_z1=r e1,      u_z2=r e2,
u_i=(L/sqrt(m))e1 (i in I1, |I1|=m),
u_j=(L/sqrt(m))e2 (j in I2, |I2|=m).

Let R=UU^T and choose D diagonal with D_p=D_q=0 and D_kk=-||u_k||^2 for every other coordinate. Put A=D+R. Then A_pp=A_qq=epsilon^2 and all other physical diagonals vanish. The pair P={p,q} has B=epsilon^2 I_2, and since C^T B^{-1}C=R[L,L], its exact pair Schur complement is D[L,L], hence W2=0.

Each of the two feature groups has, on the symmetric subspace spanned by p, z and the flat leaf vector, the matrix

[[epsilon^2, 2epsilon, 2epsilon],
 [2epsilon, 0, 4],
 [2epsilon, 4, 4(1-1/m)]].

At epsilon=0,m=infinity the nonzero two-by-two corner has eigenvalues 2+2sqrt(5) and 2-2sqrt(5), whose moduli are >2. For epsilon<=1/16 and m>=16 the perturbation Frobenius norm is at most sqrt(1/8)<0.354, so each feature group retains two eigenvalues of modulus >1. Thus A has at least four target-large eigenvalues.

Every physical off-diagonal entry has magnitude at most max(2epsilon,4/sqrt(m)); every 2-by-2 principal determinant is either epsilon^4 or minus the square of one such entry. Therefore, for every fixed no-pivot threshold tau>0, first choose epsilon small and then m large so that every physical diagonal and every physical 2-by-2 principal determinant is <tau in magnitude. This is a strict-N3 W2=0 family.

Next analytic debt: exploit (E1)-(E3) in the diagonal-plus-rank-two class, using averaged-frequency rank-two/diagonal interaction rather than D/D'/D5 or a tiny pair determinant.
