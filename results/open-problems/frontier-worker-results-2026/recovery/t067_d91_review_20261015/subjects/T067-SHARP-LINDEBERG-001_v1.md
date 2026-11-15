# Sharper three-state signed Gaussian replacement

Claim T067-SHARP-LINDEBERG-001, version 1. Status: proof (unaudited).
No priority or novelty assertion. Existing reviewed v1 proofs are unchanged.

Let mu be an S3-invariant probability law on the three-state simplex, with
uniform root and calibrated posterior p. Put a=3p-1, A=||a||^2, J=sum_i a_i^3,
M=EA=9x, U=EA^2, and T=EJ. Suppose T>=0. For integer d>=1 and
0<lambda<=L=1/16, let x_next be the squared-posterior deviation after d
Potts branches, independent conditional on the root, with edge eigenvalue
lambda. In Sly's normalization s=d lambda^2 x,

    x_next-g_3(s) <= d lambda^4 (C_U U+C_M M^2),          (1)

with explicit constants satisfying C_U<1/4 and C_M<31/180, defined in Section 6.
This is one-sided and requires T>=0. It asserts no Galton--Watson result.

The hardest new steps are the full-simplex softmax derivative bounds
T067-SOFTMAX-DERIVATIVES-001 v1 and the q=3-specific moment estimates below.
The Bayesian replacement construction and favorable cubic sign also occur in
the reviewed T067-SIGNED-LINDEBERG-001 v1; they are written out again here to
make the new estimates checkable. Source context: Sly, Reconstruction for the
Potts model, (4.7) and Lemma 4.3; Mossel--Sly--Sohn, Appendix A. Primary source
files and locators are in SOURCES.jsonl. The new constants are an own-work draft.

1. Exact Bayesian hybrid and retained cubic sign.

Write P=I-11^t/3, v=(1/3,-1/6,-1/6), and h=(0,1,-1). Conditional on root 1
the input law has density 1+lambda a_1 relative to mu. Define

    Lbranch=P log(1+lambda a),
    C=(lambda^2 M/2)P,    m=C e_1=lambda^2 M v,
    G conditional on root i ~ N(C e_i,C).

The M=0 case is immediate. Otherwise work on the zero-sum plane. The Gaussian
means have equal squared inverse-covariance norm, so their density ratio is
exp(g_i-g_j). Thus Lbranch and G are exact symmetric Bayesian experiments
with posterior softmax of the displayed vector. Any sum W of unreplaced and
replaced branches is also such an experiment, conditional independence being
with respect to the root. Its root-1 conditional posterior law has density
3p_1 relative to its unconditional symmetric posterior law nu_W.

For any permutation-invariant integrable radial function f(a),
E_1 f=E f: E[a_1 f]=(1/3)E[(sum_i a_i)f]=0. In particular E_1 A^k=EA^k.
We have A<=6 and M<=6.

For F(z)=softmax(z)_1, Bayes calibration gives
E_1 F(sum Lbranch)-1/3=x_next. The d-fold Gaussian sum has mean
(3s,-3s/2,-3s/2) and covariance (9s/2)P, hence
E_1 F(sum G)-1/3=g_3(s). Telescope over the d branches. In a single replacement
W is independent of its replaced branch conditional on root 1.

Symmetry gives Eaa^t=(M/2)P and the third moments
Ea_i^3=T/3, Ea_i^2a_j=-T/6 for i!=j, Ea_1a_2a_3=T/3.
With b=-P a^2/2, the leading raw moment differences are

    E_1 Lbranch-E_1 G = -lambda^3 T v/2 + higher terms,
    E_1 Lbranch Lbranch^t-E_1 GG^t = -lambda^3 T hh^t/2 + higher terms.

The leading third raw tensor is lambda^3 E a^tensor3. Contracting these
three terms with the first three derivatives in Taylor's formula yields
lambda^3 T ell_1(p), where

    ell_i(p)=-(1/2)p_i(p_j-p_k)^2+(3/2)e3(1-3p_i),
    e2=p_1p_2+p_1p_3+p_2p_3,   e3=p_1p_2p_3.

These identities follow by differentiating softmax: grad F dot v=p_1(1-p_1)/2,
D_h^2F=p_1[2(p_2-p_3)^2-(1-p_1)], and
sum_i partial_i^3 F=6e3(1-3p_1). The symmetric third tensor contraction is
(3T/2)sum_i partial_i^3 F before the Taylor factor 1/6.

Calibration and permutation symmetry imply

    E_1 ell_1 = E_nu sum_i p_i ell_i = -E_nu[e2(e2-9e3)] <= 0,        (2)

because e2-9e3=sum_cyclic p_k(p_i-p_j)^2>=0. For the middle equality, expand
sum_i p_i^2(p_j-p_k)^2=2e2^2-6e3 and use sum p_i=1. Thus all retained cubic
terms have nonpositive total expectation when T>=0. Nothing asserts their
pointwise sign or their vanishing. The remaining sections bound every term
discarded from this cubic expansion uniformly in the actual hybrid W.

2. Three-state identities and logarithm estimates.

For a zero-sum vector a in R^3, elementary polynomial identities give

    sum_i a_i^4=A^2/2,     ||P a^2||^2=A^2/6,
    P a^3=(A/2)a,         P a^4=(A/2)P a^2+(J/3)a,
    ||P a^4||^2=A^4/24+4AJ^2/9 <= 25A^4/216.          (3)

Here A^3/6-J^2=product_(i<j)(a_i-a_j)^2/3>=0. All equalities can also be
verified by a_3=-a_1-a_2; the exact generic symbolic check is
checks/q3_quartic_geometry.py. Consequently for c=P a^3/3,
||b||=A/(2sqrt(6)) and c=(A/6)a. The same generic orbit computation gives

    E[a_1 c]=Uv/6,
    E[a_1(ab^t+ba^t)]=(U/36)*[[-2,1,1],[1,1,-2],[1,-2,1]].         (4)

The matrix in (4) has eigenvalues 0,-3,3, hence nuclear norm U/6 after scaling.
One way to derive (4) is the fourth-moment list
Ea_i^4=U/6, Ea_i^3a_j=-U/12, Ea_i^2a_j^2=U/12, and Ea_i^2a_ja_k=0 for distinct
i,j,k. Symmetrizing a generic zero-sum orbit proves these identities for every
invariant law by integration.

For an equivariant zero-sum vector V(a), a further useful exact identity is

    E[a_1 V(a)]=v E[a dot V(a)].                       (5)

Indeed its diagonal coordinate is (1/3)E[a dot V], and the two other coordinates
are equal and sum to its negative. This proof applies also to log vectors.

Write Lbranch=lambda a+lambda^2 b+lambda^3 c+r4. The scalar integral remainder
for log, after degree four, is bounded by |lambda a_i|^5/[5(1-lambda)], since
a_i>=-1. Combining this with (3), A<=6, sqrt(6)<=49/20 and
1/sqrt(6)<=5/12, define

    B4=25/288+(49/100)L/(1-L),
    B3=1/6+(49/20)L B4,
    B1=5/24+(49/20)L B3.                              (6)

The resulting pointwise bounds are

    ||r4|| <= lambda^4 A^2 B4,
    ||Lbranch-lambda a-lambda^2 b|| <= lambda^3 A^(3/2) B3,
    ||Lbranch-lambda a|| <= lambda^2 A B1,
    ||Lbranch|| <= lambda sqrt(A)/(1-lambda),
    ||lambda a+lambda^2 b|| <= lambda sqrt(A)(1+lambda/2).            (7)

For the first one, ||P a^4||/4 <=25A^2/288, and the fifth-order remainder
is at most lambda^5 A^(5/2)/[5(1-lambda)]. The next two follow from the exact
norms of b,c. Projection is a Euclidean contraction. These estimates do not
require a power series outside its convergence disk: the log identity follows
by integrating polynomial division of 1/(1+t), for t>-1.

3. Mean remainder.

Permutation symmetry implies E Lbranch=0. Applying (5) directly gives

    E_1 Lbranch = lambda v E[a dot Lbranch]
      = m-lambda^3 T v/2+lambda^4 U v/6+lambda v E[a dot r4].        (8)

This removes the unnecessary fourth-order bound on E_1 r4 used in the earlier
proof. At every W, 0<=grad F(W) dot v=p_1(1-p_1)/2<=1/8. Also
|E a dot r4|<=lambda^4 sqrt(6)U B4 by (7) and A<=6. The mean contribution
after its retained cubic part is therefore at most

    lambda^4 U [1/48+(49/160)L B4].                   (9)

4. Second and third raw moment remainders.

Let B=lambda a+lambda^2 b. For arbitrary vectors z,w,
||zz^t-ww^t||_*<=||z-w||(||z||+||w||). Using (7), the nuclear norm of
Lbranch Lbranch^t-lambda^2 aa^t-lambda^3(ab^t+ba^t) is at most

    lambda^4 A^2 [1/24+B3(1/(1-L)+1+L/2)].

The first term is ||b||^2=A^2/24; the other terms are the difference from BB^t.
Changing the root-conditional density on the degree-three term adds the exact
matrix (4), with norm lambda^4 U/6. Gaussian raw second moment C+mm^t adds a
remainder of norm lambda^4 M^2/6. Radial bounds average exactly under E_1.
The global Hessian bound 1/5 from SOFTMAX-DERIVATIVES v1 and Taylor factor
1/2 therefore give the contribution

    lambda^4 { (U/10)[1/24+B3(1/(1-L)+1+L/2)+1/6]+M^2/60 }.         (10)

Fix W and put Q(z)=D^3F(W)[z,z,z]. The mixed derivative bound 1/2 from that
same claim and (7) show

    |Q(Lbranch)-Q(lambda a)|
      <=(3/2)||Lbranch-lambda a|| max(||Lbranch||,lambda sqrt(A))^2
      <=(3/2)lambda^4 A^2 B1/(1-L)^2.

After division by 6 this costs lambda^4 U B1/[4(1-L)^2]. The density correction
on the leading cubic costs at most lambda^4 U/15, since
|Q(a)|<=(2/5)A^(3/2) and |a_1|<=sqrt(A).

For G=H+m with H centered, E Q(G)=Q(m)+3E D^3F(W)[m,H,H]. Since
||m||=lambda^2 M/sqrt(6) and E||H||^2=lambda^2 M, the two absolute terms,
after division by 6, are at most lambda^4 M^2*L^2/36 and
lambda^4 M^2*5/48, respectively. The first uses M<=6 and the diagonal bound
2/5; the second uses the mixed bound 1/2 and 1/sqrt(6)<=5/12. Thus all third
raw remainder terms together cost

    lambda^4 {U[B1/(4(1-L)^2)+1/15]+M^2[5/48+L^2/36]}.             (11)

5. Fourth-order Taylor remainders.

The global fourth derivative bound 3/5 makes the remainder after cubic order
at most ||z||^4/40. The Lbranch part is bounded by lambda^4 U/[40(1-L)^4].

For the Gaussian use its exact fourth moment, without a triangle inequality.
On the rank-two plane H has covariance (lambda^2 M/2)I. Odd centered Gaussian
moments vanish, E||H||^4=2lambda^4 M^2, and
E(H dot m)^2=(lambda^2 M/2)||m||^2. Expansion gives

    E||H+m||^4
      =2lambda^4 M^2+(2/3)lambda^6 M^3+lambda^8 M^4/36
      <=lambda^4 M^2(2+4L^2+L^4),                   (12)

using M<=6. The separate exact polynomial/Gaussian moment computation in
checks/q3_sharp_constants.py verifies the expansion. Thus the Gaussian
Taylor contribution is at most lambda^4 M^2(2+4L^2+L^4)/40.

6. Constants, replacement sum, and verification scope.

Summing (9)--(12), the constants in (1) are

    C_U=1/48+(49/160)L B4
      +(1/10)[1/24+B3(1/(1-L)+1+L/2)+1/6]
      +B1/[4(1-L)^2]+1/15+1/[40(1-L)^4],

    C_M=1/60+5/48+L^2/36+(2+4L^2+L^4)/40.

At L=1/16, B4=4301/36000, B3=2130749/11520000,
B1=872406701/3686400000. Exact rational arithmetic gives
C_U=68871759703/276480000000<1/4 and C_M<31/180.
Every contribution was bounded in absolute value except the retained cubic
term, whose expected sign is (2). All constants are independent of W,d,mu.
The d conditional-root replacements telescope to (1).

The exact source checks/q3_quartic_geometry.py verifies generic zero-sum
polynomial, fourth-moment orbit, equivariant-mean and averaged-cubic identities.
checks/q3_sharp_constants.py checks the Gaussian fourth moment and rational
constants. The derivative claim has a complete rational Bernstein certificate
and independent replay. These finite verifications do not replace independent
review of calibration, integrability, or the analytic remainder bounds above.

NEXT: Compose with the reviewed fixed-point/local/Gaussian-gap lemmas for a
separately submitted regular-tree cutoff, preserving the d0=1981 proof.
