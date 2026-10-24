SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B07, 2026-09-24T09:39:02Z.
attacking: the r50 rank-54 / H62-rank4 survivor — determinant-weight preserving balanced physical cuts for diffuse finite-rank principal blocks, with the operator tail retained.

# account02/B07 r51 — balanced-cut volume receiver with operator-tail stability

Status: `NEW ROBUST VOLUME-MARGINAL LEMMA / LIVE H62-R4 DIFFUSE BRANCH PAID / HEAVY-OR-WEAK R4 SURVIVOR / FULL QFORM OPEN`.

## 1. First unpaid implication after this run

`QFORM-R50-H62-HEAVY-OR-WEAK-R4-RECEIVER-v1`.

The completed r50 state supplies, on the moderate-energy survivor, a physical set H subset S with |H|<=62 such that for L=S\H

    dist_op(A[L,L], {rank<=4}) < eta,
    eta = 0.001631502080283948,

while the no-deletion partner description simultaneously retains the physical T|S separator, arbitrary A[T,T], a rank<=54 coupler and its genuine nonzero operator tail. The new theorem below consumes the near-rank-four L-block whenever a rank-four approximant has a quantitatively nonweak third singular value and diffuse physical range. Thus the remaining L-side structural debt is no longer the operator tail itself: it is a genuinely heavy/localized range or a weak/low-rank approximant, to be combined with T, H and the retained coupler. No single coordinate minor is selected.

## 2. Incoming source-pinned state

Latest completed compatible partner at startup/final prepublication refresh: account03/B07 r50,

    math-open-problems@4155f9884b4eaa0aee96da4e148c7303e6d6cc6a
    proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260924T074025Z-account03-B07-qform-r50/REPORT.md.

It proves the pair-block rank-cancellation core theorem and, on its unpaid branch,

    A[S,S]=H_50+G_S, rank H_50<=50, ||G_S||_op<0.001631502081,

and globally

    A=diag(A[T,T],0)+P_54+G,
    rank P_54<=54,
    ||G||_op<0.001646760870.

The complementary account02 r50 refinement gives the physical H above and the rank<=4 operator approximation on L=S\H.

Mandatory pinned analytic source actually used below:

    math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837
    proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/
    RESULTS.md and FOURIER_ROUTE_REPORT.md.

Its proved Theorem D says that for a physical crossing M=A[I,J], with Z=e_3(M^T M), if the volume-sampling row marginals alpha_i on I are <=1/2, then

    ||p_Q||_infinity <= 6 sqrt(e) Z^(-1/6).

The proved extension D' allows max alpha_i<=h<3/4 with the explicit extra factor (2h)^(-1/2)(3-4h)^(-1). Same-bank blocks, all outside coordinates/couplings and induced affine terms are arbitrary.

## 3. Balanced physical cut for a finite-rank principal block

### Lemma 3.1 — `QFORM-BALANCED-RANKR-CUT-v1`

Let R=U Lambda U^T be a symmetric rank-r matrix on a literal physical coordinate set L, r>=3, U^T U=I_r, and Lambda nonsingular diagonal. Define physical range leverages

    ell_i = ||U_{i,*}||_2^2,
    delta = max_i ell_i,
    rho = sqrt(r delta).

If rho<1, there is a physical partition L=I disjoint_union J such that, with

    G_I=U_I^T U_I, G_J=U_J^T U_J,
    a=(1-rho)/2,

one has

    a I_r <= G_I,G_J <= (1+rho)I_r/2.                 (3.1)

Consequently for the physical crossing

    M_0=R[I,J]=U_I Lambda U_J^T,

    s_k(M_0) >= a s_k(R), 1<=k<=r,                    (3.2)

and every I-side row leverage of col(M_0) is at most

    h_i^0 <= ell_i/a <= delta/a.                      (3.3)

#### Proof

For independent Rademacher signs eps_i let

    S=sum_i eps_i u_i u_i^T,

where u_i is row i of U, viewed as a column. Cross terms vanish in the Frobenius second moment, so

    E ||S||_F^2
      = sum_i ||u_i u_i^T||_F^2
      = sum_i ell_i^2
      <= delta sum_i ell_i
      = delta r.

Hence some sign choice has ||S||_op<=||S||_F<=rho. Put I={i:eps_i=+1}. Since sum_i u_i u_i^T=I_r,

    G_I=(I_r+S)/2, G_J=(I_r-S)/2,

which gives (3.1).

Write U_I=Q_I G_I^(1/2), U_J=Q_J G_J^(1/2), with Q_I,Q_J having orthonormal columns. The nonzero singular values of M_0 are those of

    G_I^(1/2) Lambda G_J^(1/2).

Both outer factors have least singular value at least sqrt(a), so the standard product singular-value inequality gives (3.2). Since G_I is invertible, col(M_0)=col(U_I), whose projector is U_I G_I^(-1) U_I^T. Its i-th diagonal is u_i^T G_I^(-1)u_i<=ell_i/a, proving (3.3). QED.

### Exact-low-rank consequence

For the 3-volume law of M_0, the pinned source gives the spectral marginal identity

    alpha_i=sum_m p_m q_m(i)^2,
    p_m = x_m e_2(x without m)/e_3(x),
    x_m=s_m(M_0)^2.

Because

    e_3(x)=x_m e_2(x without m)+e_3(x without m),

one has 0<=p_m<=1. Hence alpha_i is at most the ordinary row leverage of col(M_0), and (3.3) gives

    alpha_i <= delta/a = 2 delta/(1-rho).             (3.4)

In particular, if

    delta <= 1/(4r),                                  (3.5)

then rho<=1/2, a>=1/4 and alpha_i<=4delta<=1/r<=1/3. The pinned Theorem D therefore applies to the actual physical crossing, with no selected minor. Since

    Z=e_3(M_0^T M_0)>=s_1^2 s_2^2 s_3^2>=s_3(M_0)^6,

(3.2) yields the full ambient target-level conditional bound

    boxed:
    ||p_Q||_infinity
      <= 6 sqrt(e)/s_3(M_0)
      <= 12 sqrt(e)/[(1-rho)s_3(R)]
      <= 24 sqrt(e)/s_3(R).                            (3.6)

All outside variables are conditioned only in their original coordinates, so arbitrary outside curvature and affine terms are retained.

## 4. New determinant-weight stability under an arbitrary operator tail

The main new step is that a small operator tail need not be deleted before applying Theorem D. Its effect on the ACTUAL 3-volume marginals can be controlled dimension-free.

### Lemma 4.1 — `QFORM-E3-MARGINAL-OPTAIL-STABILITY-v1`

Let M_0 be any real matrix, let P_0 be the orthogonal projector onto col(M_0), and suppose

    M=M_0+E, ||E||_op<=eta, s_3(M)>=mu>0.              (4.1)

Let

    h_0=max_i (P_0)_{ii}                              (4.2)

on the row side on which Theorem D will impose its marginal condition. For any tau satisfying

    eta<tau<=mu,                                      (4.3)

the actual squared-3-minor volume-sampling marginals alpha_i of M obey

    boxed:
    alpha_i <= H(tau)
      := (sqrt(h_0)+eta/tau)^2 + 3(tau/mu)^2.          (4.4)

This bound has no dimension, Frobenius-tail, support or moment factor.

#### Proof

Write the singular values of M as s_1>=s_2>=... and x_m=s_m^2. The pinned spectral formula gives

    alpha_i=sum_m p_m q_m(i)^2,
    p_m=x_m e_2(x without m)/e_3(x).                  (4.5)

First control the weak singular modes. The identity

    3 e_3(x)
      = sum_{a<b} x_a x_b sum_{c notin {a,b}} x_c     (4.6)

and monotonicity x_1>=x_2>=x_3 imply that every complementary sum in (4.6) is at least x_3. Therefore

    3 e_3(x) >= x_3 e_2(x).                           (4.7)

It follows from (4.5) that

    p_m <= x_m e_2(x)/e_3(x)
         <= 3 x_m/x_3
         <= 3 s_m^2/mu^2.                             (4.8)

Hence all modes with s_m<tau contribute at most

    3(tau/mu)^2 sum_{s_m<tau} q_m(i)^2
    <=3(tau/mu)^2.                                    (4.9)

For the strong modes s_m>=tau, let Q_tau and V_tau contain their left and right singular vectors and Sigma_tau the corresponding singular values. Since range(M_0) is P_0,

    (I-P_0)Q_tau
      =(I-P_0) M V_tau Sigma_tau^(-1)
      =(I-P_0) E V_tau Sigma_tau^(-1),

so

    ||(I-P_0)Q_tau||_op <= eta/tau.                   (4.10)

Thus the strong left-singular projector P_tau satisfies

    ||(I-P_0)P_tau||_op=||P_tau(I-P_0)||_op<=eta/tau. (4.11)

For a physical row vector e_i,

    ||P_tau e_i||
      <= ||P_tau P_0 e_i||+||P_tau(I-P_0)e_i||
      <= sqrt((P_0)_{ii})+eta/tau
      <= sqrt(h_0)+eta/tau.                           (4.12)

Since p_m<=1, the strong part of (4.5) is at most ||P_tau e_i||^2. Adding (4.9) proves (4.4). QED.

### Corollary 4.2 — robust physical-volume receiver

Suppose on a physical principal set L

    A[L,L]=R+E_L,
    rank R=r>=3,
    ||E_L||_op<=eta,                                  (4.13)

with R=U Lambda U^T, s_3(R)=sigma, and delta=max_i||U_{i,*}||^2. Put

    rho=sqrt(r delta),
    a=(1-rho)/2.                                      (4.14)

Use Lemma 3.1 to choose I|J and let M=A[I,J]. Then

    s_3(M) >= mu:=a sigma-eta.                        (4.15)

The base crossing M_0=R[I,J] has h_0<=delta/a. Therefore for every eta<tau<=mu,

    alpha_i <=
    H(tau):=(sqrt(delta/a)+eta/tau)^2+3(tau/mu)^2.    (4.16)

If H(tau)<=1/2, pinned Theorem D gives

    boxed: ||p_Q||_infinity <= 6 sqrt(e)/mu.          (4.17)

If merely H(tau)<3/4, the pinned D' extension gives

    boxed:
    ||p_Q||_infinity
      <= 6 sqrt(e)(2H)^(-1/2)(3-4H)^(-1)/mu.          (4.18)

This is a full-ambient inequality: same-bank terms on I and J, all coordinates outside L, every induced affine term, signs, and additional spectrum are untouched. The operator tail is present in the actual M whose determinant weights are used.

## 5. Direct payment of a live r50 near-rank-four branch

Use the account02 r50 localized-exception state

    |H|<=62,
    L=S\H,
    dist_op(A[L,L], rank<=4)<eta,
    eta=0.001631502080283948.                          (5.1)

Assume there is a rank-four approximant R on L satisfying (5.1) with

    sigma=s_3(R)>=260 eta
                    =0.4241905408738265,              (5.2)

and diffuse physical range

    delta=max_i ||U_{i,*}||^2 <=1/16.                 (5.3)

Then r=4 gives rho<=1/2, a>=1/4 and h_0<=delta/a<=1/4. From (4.15),

    mu>=sigma/4-eta>=64 eta.                          (5.4)

Choose

    tau=sqrt(eta mu).                                 (5.5)

Since eta/mu<=1/64,

    eta/tau=tau/mu=sqrt(eta/mu)<=1/8,

and therefore

    H(tau)<= (1/2+1/8)^2+3/64
           =7/16
           <1/2.                                      (5.6)

This is an ACTUAL volume-marginal bound for A[I,J], not for the approximant. The pinned Theorem D now gives

    boxed:
    ||p_Q||_infinity <=6 sqrt(e)/mu
      <= (195/8) sqrt(e)/sigma
      <40.188/sigma.                                  (5.7)

At the endpoint sigma=260 eta this is

    boxed: ||p_Q||_infinity <94.740.                  (5.8)

Thus the operator-tail transfer on the diffuse, nonweak rank-four part of the live H62 branch is closed.

## 6. What the new theorem does and does not infer

It does not claim a universally good coordinate minor. It first balances an entire finite-rank range by a physical random-sign cut, then controls the ACTUAL determinant-volume row marginals after the full operator tail is restored. The analytic receiver sees the aggregate Cauchy-Binet volume law.

The live branch can now survive this gate only by failing its quantitative hypotheses. In particular, for a rank-four approximant at the live eta scale, one must have at least one of:

* `s3(R)<260 eta` (weak third R-direction);
* `max_i ||U_{i,*}||^2>1/16` (heavy physical range);
* or use an approximant of rank <=3 for which the general criterion (4.16) still has to be checked at its actual parameters.

In the heavy rank-four case the set

    H_R={i: ||U_{i,*}||^2>1/16}

has cardinality strictly below 64 because the leverages sum to four. Hence all heavy rows live in a bounded physical set, which can be adjoined to the existing |H|<=62 exception set at total cardinality <126. What remains is to combine that bounded heavy set, or the weak-s3 alternative, with the arbitrary T-side block and the retained rank-54 coupler; no claim is made that deleting the heavy set preserves three target eigenvalues.

The separate r50/r49 `E_star>1` same-bank-star-energy branch remains unpaid.

## 7. Source-valid regression and correction checks

This argument does not use: independence after spectral rotation; arbitrary-joint coarea; a conditional density supremum; pointwise quadratic-phase decay; small random effect from a small matrix norm; or one well-conditioned minor. The small operator tail is never dropped: it enters (4.1), rotates the actual singular vectors, and is paid explicitly in (4.4).

The earlier correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` remains respected. The present theorem does not assert every three-large-eigenvalue matrix has a rank-three crossing; it applies only after the r50 finite-rank normal form supplies a physical near-low-rank principal block with the displayed quantitative spectral/leverage data.

## 8. Status

The exact low-rank diffuse branch and the quantitatively separated near-rank-four diffuse branch above are proved and paid by the pinned e5 Theorem D. On these paid Fourier branches the resulting density is continuous. Full unrestricted QFORM remains OPEN / not proved / not disproved, and full-target continuity remains OPEN.
