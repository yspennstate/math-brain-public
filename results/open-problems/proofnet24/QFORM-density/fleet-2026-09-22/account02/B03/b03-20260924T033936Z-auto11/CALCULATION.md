SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-24T03:39:36Z.
attacking: exact-rank-two aligned anchored collar: convert spread same-bank curvature into a literal three-volume crossing by an internal balanced physical cut, while preserving original-coordinate product provenance and whole-copy dependence.

# Early calculation — aligned curvature creates a uniform physical E3 cut

Fix m=4q>=8. Let h be one original coordinate and let U,V be disjoint banks of m original coordinates. Put

u1=v1=m^(-1/2)(1,...,1),

and let u2=v2=m^(-1/2)(1,...,1,-1,...,-1), with m/2 plus signs and m/2 minus signs. These are orthonormal pairs in their respective banks.

Define the symmetric coefficient matrix A_m by the quadratic form

Q_m = 2 h(<u1,U>+<v1,V>)
      + <u1,U>^2 + <v1,V>^2
      + 2<u1,U><v1,V> + 2<u2,U><v2,V>.

All random coordinates remain the original independent cap-one coordinates. The vectors u1,u2,v1,v2 are used only to describe deterministic coefficients.

On the deterministic five-dimensional invariant coefficient subspace (h,u1,u2,v1,v2), A_m is

[[0,1,0,1,0],
 [1,1,0,1,0],
 [0,0,0,0,1],
 [1,1,0,1,0],
 [0,0,1,0,0]].

Thus its nonzero spectrum is

{1+sqrt(3), 1-sqrt(3), 1, -1}.

In particular A_m has at least three eigenvalues of modulus >=1 for every m, so this is an exact owner-target family.

Viewed as the account03/B03 r45 exact-rank-two packet, the U-V crossing is N=u1 v1^T+u2 v2^T, with s1=s2=1. Both hub stars equal the first singular directions, so alpha=beta=0; the hub diagonal is b=0; and the anchored determinant is D0=-1. Hence this family lies exactly in the aligned, small-hub-diagonal endpoint left unpaid by the transverse-hub mechanism. Both same-bank blocks are nonzero rank-one curvature, so the one-linear-bank r46 compiler does not apply. The newest r47 physical zero-pair theorem also has no literal zero-diagonal pair here: every U_i and V_j has diagonal coefficient 1/m and h is the only zero-diagonal coordinate.

Now split each bank into balanced halves. Choose U_L,U_R and V_L,V_R so that each half contains equally many + and - signs of u2 or v2. Let

L={h} union U_L union V_L,
R=U_R union V_R.

The normalized restrictions sqrt(2)u1|U_L, sqrt(2)u2|U_L are orthonormal, and similarly on each of the other halves. In these normalized mode bases, the literal physical cross block M=A_m[L,R] has the only nonzero part

[ 1/sqrt(2)   0   1/sqrt(2)   0 ]
[ 1/2         0   1/2         0 ]
[ 0           0   0           1/2 ]
[ 1/2         0   1/2         0 ]
[ 0           1/2 0           0 ].

Therefore

M^T M =
[[1,0,1,0],
 [0,1/4,0,0],
 [1,0,1,0],
 [0,0,0,1/4]],

so the squared singular values are {2,1/4,1/4,0}. In particular

Z_3 := e_3(M M^T)=e_3(M^T M)=2*(1/4)*(1/4)=1/8.

For the three-volume row-sampling law on the left bank, the left singular subspace is the orthogonal sum of:
(1) q=(1/sqrt(2))e_h+(1/2)u1_L~+(1/2)v1_L~;
(2) u2_L~;
(3) v2_L~,
where the tildes denote normalized restrictions. Hence the row marginals, equivalently rank-three row leverage scores, are

alpha_h = 1/2,
alpha_i = 1/(2m)+2/m = 5/(2m) for every i in U_L or V_L.

Since m>=8, all alpha_i<=1/2. Thus the completed pinned e5f71d79 Theorem D applies to this literal original-coordinate cut, despite exact hub/star alignment. It gives

|phi_Q(t)| <= min{1, K |t|^(-3/2)},
K=(2*pi)^(3/2) e^(3/4) (1/8)^(-1/4),

and therefore

||p_Q||_infinity <= 6 sqrt(e) (1/8)^(-1/6)=6 sqrt(2e)=13.9898638895... .

The corresponding assigned whole-copy time integral is obtained by integrating the squared envelope at its crossover:

int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <= (24/5) K^(1/3)
 = (24/5) sqrt(2*pi) e^(1/4) 2^(1/4)
 = 18.3722476525... .

Using only the whole-output identity |phi_Q(t)|^2=E exp(it(Q-Q')) gives

E|Q-Q'|^(-1/2)
 <= (24/5) e^(1/4) 2^(1/4)
 = 7.32946637457... .

Thus the aligned endpoint itself is not an obstruction once the same-bank curvature is spread in a way that can be repartitioned: that curvature becomes the third crossing direction. The first unpaid implication is now to prove a structural alternative in the general aligned small-b collar: either an internal physical repartition exposes quantitatively nontrivial E3 with acceptable row leverage, or the two same-bank curvature blocks are cut-poor/concentrated enough to admit a different low-rank/grouped carrier receiver.

Full QFORM remains open. Unrestricted continuity remains open; this family has a continuous C_0 density because the displayed |t|^(-3/2) envelope is integrable.
