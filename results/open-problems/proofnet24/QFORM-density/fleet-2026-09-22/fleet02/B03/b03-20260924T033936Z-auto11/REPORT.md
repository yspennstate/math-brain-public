SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-24T03:39:36Z.
attacking: exact-rank-two aligned anchored collar: convert spread same-bank curvature into a literal three-volume crossing by an internal balanced physical cut, while preserving original-coordinate product provenance and whole-copy dependence.

# fleet02/B03 — aligned curvature can be promoted to a physical E3 crossing

Status: **NEW SUPPORTING FAMILY THEOREM / PINNED THEOREM-D APPLICATION / LATEST PARTNER r47 OBSTRUCTION / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The current hard exact-rank-two collar cannot be closed merely by testing transverse hub components, a nonzero hub diagonal, or one localized determinant. The first unpaid implication is now:

> In the exact/near aligned small-hub-diagonal survivor, prove a product-preserving alternative: either an internal physical repartition of the two curved banks exposes a quantitatively nontrivial three-volume crossing with acceptable sampling leverage (or a marginal-free E3 receiver), or the same-bank curvature is sufficiently cut-poor/concentrated that a low-rank/grouped carrier theorem applies.

The family below proves that the first alternative is real and quantitatively strong: same-bank curvature that looks obstructive in the original rank-two decomposition can become precisely the missing third crossing direction after repartition. It also shows why a localized physical-triple determinant is not an exhaustive scale.

## 2. Exact target-valid aligned family

Let m=4q>=8. Take one original coordinate h and two disjoint original-coordinate banks U,V of size m. All coordinates are independent and have arbitrary real densities bounded by one.

Set

u1=v1=m^(-1/2)(1,...,1),

u2=v2=m^(-1/2)(1,...,1,-1,...,-1),

with m/2 plus signs and m/2 minus signs. Define A_m by

Q_m=X^T A_m X
   =2h(<u1,U>+<v1,V>)
    +<u1,U>^2+<v1,V>^2
    +2<u1,U><v1,V>+2<u2,U><v2,V>.

The vectors are only deterministic coefficient notation; no rotated random coordinates are ever asserted independent.

On span{h,u1,u2,v1,v2}, the coefficient matrix is

[[0,1,0,1,0],
 [1,1,0,1,0],
 [0,0,0,0,1],
 [1,1,0,1,0],
 [0,0,1,0,0]].

The (h,u1,v1) block has characteristic polynomial lambda(lambda^2-2lambda-2), while the (u2,v2) block is hyperbolic. Hence

spec_nonzero(A_m)={1+sqrt(3),1-sqrt(3),1,-1}.

Thus A_m has at least three eigenvalues of modulus at least one for every m. This is an exact owner-target family with no support, moment, iid, log-concavity, or post-rotation hypothesis.

## 3. It lies in the aligned small-b endpoint

In the original U|V rank-two description,

N=u1 v1^T+u2 v2^T,

so s1(N)=s2(N)=1. Both hub stars are the first singular directions: c=u1 and r=v1. Therefore the transverse quantities of fleet03/B03 r45 are exactly

alpha=beta=0.

The hub diagonal is b=0 and the anchored determinant is

D0=b s1 s2-r1 c1 s2-r2 c2 s1=-1.

So the family sits exactly in the r45 aligned, small-hub-diagonal endpoint. Both same-bank blocks are nonzero rank-one curvature. Consequently the fleet03/B03 r46 theorem requiring one genuinely linear bank is not applicable. The newest compatible fleet03/B03 r47 zero-pair theorem is also not applicable to this curved family: every physical U_i and V_j has diagonal coefficient 1/m, while h is the only zero-diagonal coordinate.

## 4. Balanced physical repartition and exact three-volume

Choose physical halves U=U_L disjoint_union U_R and V=V_L disjoint_union V_R so that each half contains equally many + and - signs of u2 or v2. Put

L={h} union U_L union V_L,
R=U_R union V_R.

The normalized restrictions sqrt(2)u1|U_L and sqrt(2)u2|U_L are orthonormal, and similarly for all four half-banks. In the corresponding deterministic mode bases, the literal physical cross block M=A_m[L,R] has the only nonzero part

[ 1/sqrt(2)   0   1/sqrt(2)   0 ]
[ 1/2         0   1/2         0 ]
[ 0           0   0           1/2 ]
[ 1/2         0   1/2         0 ]
[ 0           1/2 0           0 ].

Therefore

M^T M=
[[1,0,1,0],
 [0,1/4,0,0],
 [1,0,1,0],
 [0,0,0,1/4]],

whose eigenvalues are {2,1/4,1/4,0}. Thus the literal physical third compound is

boxed: Z_3=e_3(MM^T)=1/8.

No coefficient has been discarded and no random variable has been rotated.

## 5. The pinned e5f71d79 Theorem D gate is exactly satisfied

For the three-volume row-sampling law on L, the three-dimensional left singular subspace is generated orthogonally by

q=(1/sqrt(2))e_h+(1/2)u1_L~+(1/2)v1_L~,

u2_L~, v2_L~,

where tildes denote normalized restrictions. Hence the physical row marginals are

alpha_h=1/2,

alpha_i=1/(2m)+2/m=5/(2m),   i in U_L or V_L.

For m>=8, every alpha_i<=1/2. The completed pinned `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` Theorem D therefore applies to this actual original-coordinate cut. It gives

boxed:
|phi_Q(t)| <= min{1,K |t|^(-3/2)},
K=(2*pi)^(3/2)e^(3/4)(1/8)^(-1/4).

In particular

boxed:
||p_Q||_infinity <=6 sqrt(e)(1/8)^(-1/6)
                  =6 sqrt(2e)
                  =13.9898638896... .

Thus every interval I obeys the genuine linear one-copy small-ball inequality

boxed:
P(Q_m in I) <= 6 sqrt(2e) |I|.

Because the displayed characteristic-function envelope is integrable, this branch has a continuous C_0 density. This continuity statement is only for this branch, not for unrestricted QFORM.

## 6. Assigned whole-copy weighted time integral

Squaring the envelope and integrating at the exact crossover t0=K^(2/3) gives

int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <= (24/5)K^(1/3)
 = (24/5)sqrt(2*pi)e^(1/4)2^(1/4)
 = 18.3722476525... .

Using only the independent-copy identity for the entire scalar output,

|phi_Q(t)|^2=E exp(it(Q-Q')),

and the positive half-Riesz Fourier identity yields

boxed:
E|Q-Q'|^(-1/2)
 <=(24/5)e^(1/4)2^(1/4)
 =7.32946637457... .

No coordinatewise sum/difference pair is separated or declared independent.

## 7. Latest fleet03/B03 r47 applied to a source-valid localization obstruction

To apply the newest compatible partner result at equation level, delete only the two rank-one same-bank curvature terms and consider the companion coefficient matrix A_m^0:

Q_m^0=2h(<u1,U>+<v1,V>)
      +2<u1,U><v1,V>+2<u2,U><v2,V>.

Its nonzero spectrum is {2,-1,-1,1,-1}, so it is again exactly inside the owner target.

Choose physical coordinates i in U and j in V whose u2/v2 signs agree. Then

A_ii=A_jj=0,
mu=A_ij=2/m,
A_hi=A_hj=1/sqrt(m).

For the zero-pair H={i,j}, the exact Schur residual diagonal at the genuine physical hub h is

d=S_hh=-2(A_hi A_hj)/mu=-1.

Equivalently the physical principal triple has

|det A[{i,j,h},{i,j,h}]|=mu^2|d|=4/m^2.

The newest fleet03/B03 r47 theorem `QFORM-ZEROPAIR-PRINCIPAL3-DET-L3-v1` therefore gives the actual valid bounds

boxed:
||p_(Q_m^0)||_infinity
 <=576^(1/3)(4/m^2)^(-1/3)
 =(144 m^2)^(1/3)
 =5.24148278842... m^(2/3),

and

boxed:
int_R |t|^(-1/2)|phi_(Q_m^0)(t)|^2 dt
 <=4 sqrt(pi) 12^(1/3) m^(1/3)
 =16.2316253392... m^(1/3).

These inequalities are correct but diverge with m. This is an actual source-valid obstruction to treating one localized physical principal-triple determinant as an exhaustive structural scale. It is not a counterexample to QFORM; the companion has other aggregate receivers. The contrast is the point: diffuse geometry can make every fixed physical triple small even while a balanced product-preserving repartition exposes order-one aggregate crossing volume.

## 8. Structural synthesis

This family changes the mechanism in the aligned endpoint. In the original hub/rank-two coordinates, the same-bank rank-one terms look like extra curvature that blocks the one-linear-bank theorem. After a balanced physical repartition, those same terms supply exactly the missing third crossing direction; the hub row sits at the sharp Theorem-D leverage threshold 1/2, while all physical bank rows have leverage 5/(2m).

This is consistent with the fresh fleet03/B20 aggregate-promoted-E3 closure: aggregate transverse mass should be paid before localizing to a few physical coefficients. What remains unproved is the universal structural bridge. One must show that every aligned small-b survivor either admits such a quantitatively good internal E3 repartition, or has curvature sufficiently concentrated/cut-poor to enter an already-paid finite-hub, nested-rank-two, low-rank-carrier, grouped-hub, ridge, or other aggregate receiver.

The correction forbidding a universal rank-three physical cross cut remains binding: the present family is a positive witness for one branch, not a claim that every target matrix has a good E3 cut.

## 9. Status

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Unrestricted continuity remains **OPEN**. The present family has a universal bounded continuous density and an explicit whole-copy weighted-time bound. Unknown provider telemetry remains UNKNOWN/null.
