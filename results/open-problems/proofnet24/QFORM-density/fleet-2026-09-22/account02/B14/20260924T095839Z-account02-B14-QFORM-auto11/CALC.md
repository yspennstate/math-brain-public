SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-24T09:58:39Z.
attacking: environment-coupled deterministic extreme-set localization, and the BV/dilation obstruction to regularizing those extreme laws before paying curvature.

# Early calculation: environment-coupled bathtub localization

Full unrestricted QFORM remains OPEN. This note proves a supporting localization theorem only. The no-environment extreme-set reduction is source-known (the fixed-source RESULTS cites the uniform-on-measure-one reduction, and COUNTEREXAMPLE_SEARCH uses coordinatewise best responses). The scoped addition here is that the extreme replacements can be chosen **once for the whole independent environment**, so conditioning-generated affine fields do not force environment-dependent marginals.

## 1. Bathtub lemma in the exact cap-one class

Let

K = {f measurable on R : 0 <= f <= 1, int f = 1}.

For every measurable h:R->[0,1],

sup_{f in K} int h(x) f(x) dx = sup_{|E|=1} int_E h(x) dx.        (1)

Proof. The <= direction is the standard bathtub/rearrangement inequality. Writing h* for the decreasing rearrangement,

int h f <= int_0^1 h*(s) ds,

because f has mass one and cap one. Conversely, superlevel sets of h, completed inside one level set using nonatomicity of Lebesgue measure, give measurable E of measure one with integral arbitrarily close to int_0^1 h*. No compactness, support bound, moment, connectedness, or finite-fragment assumption is used.

## 2. Environment-coupled product theorem

Let (Omega,tau) be any finite positive measure space, with tau(Omega)=m<infinity. Let H:Omega x R^r -> [0,1] be measurable. Define

T_H(f_1,...,f_r)
 = int_Omega int_{R^r} H(omega,x) prod_{j=1}^r f_j(x_j) dx tau(domega).

Then

boxed{
 sup_{f_1,...,f_r in K} T_H(f_1,...,f_r)
 = sup_{|E_1|=...=|E_r|=1} T_H(1_{E_1},...,1_{E_r}).
}                                                        (2)

Proof. Fix f_2,...,f_r and set

h_1(x_1)=int_Omega int H(omega,x) prod_{j>=2} f_j(x_j) dx_2...dx_r tau(domega)/m

when m>0. Then 0<=h_1<=1. By (1), for every eps>0 there is |E_1|=1 whose replacement loses at most eps/r in the normalized functional. Repeat sequentially for coordinates 2,...,r, always using the already replaced previous coordinates. After r steps one has a product of indicators of unit-measure sets with value at least the original value minus eps. The reverse inequality is immediate because indicators of unit-measure sets belong to K. The case m=0 is trivial.

Crucially, each E_j is chosen from the **environment-averaged** partial kernel. It depends on tau and H but not on the realized omega. Thus the replacement preserves the original product provenance and never creates post-conditioning or post-rotation dependence.

## 3. Quadratic-form corollary with arbitrary affine leakage

Let Z be any independent environment (or an arbitrary positive environment submeasure of mass m). Let B be a fixed symmetric r x r matrix, and let b(Z),c(Z) be arbitrary measurable functions. For a bounded open interval I set

H(z,x)=1{x^T B x+b(z)^T x+c(z) in I}.

Then (2) gives the exact concentration identity

boxed{
 sup_{f_j<=1, int f_j=1}
 int P_f{x^T Bx+b(z)^Tx+c(z) in I} tau(dz)
 =
 sup_{|E_j|=1}
 int P_E{x^T Bx+b(z)^Tx+c(z) in I} tau(dz).
}                                                        (3)

The same statement holds with a supremum over intervals after taking the outer supremum. Hence any interval-density bound C proved uniformly for all product laws 1_{E_1}...1_{E_r}, with E_j arbitrary measurable unit-measure sets, transfers with the **same C** to all cap-one product laws. If tau has mass m, the right scale is automatically mC|I|. No continuity theorem is invoked.

For an original-coordinate split of a full quadratic form,

Q(X,Z)=X^T B X+2X^T C Z+Z^T D Z,

one has b(Z)=2CZ and c(Z)=Z^TDZ. Thus arbitrary outside translations, fragmented/unbounded outside support, and conditioning-generated affine terms are retained exactly. The active extreme sets may themselves have arbitrarily many components or unbounded support.

## 4. Exact-target application and the regularization barrier

Take

B_* = I_3-(2/3) 11^T,

so spec(B_*)={1,1,-1}. For any outside block C,D and any independent cap-one Z, the full matrix

A = [[B_*,C],[C^T,D]]

is in the owner target by interlacing: it has at least two eigenvalues >=1 and one <=-1. Conditioning on Z leaves the active 3x3 block B_* and only creates linear/constant terms. Fixed-source Theorem A therefore gives

boxed{ ||p_Q||_{infty,ess} <= 6 sqrt(pi). }               (4)

This remains true when every active marginal is an arbitrary unit-set extreme law.

Now use the newest account03/B14 family

E_{N,L}= union_{k=0}^{N-1} [k(L+1/N), k(L+1/N)+1/N],
 f_{N,L}=1_{E_{N,L}}.

Its total variation is 2N. The partner proves that if Gaussian location-scale mixtures converge weakly to f_{N,L} and

M_j = E T_j^{-1/2},

then

liminf M_j >= N sqrt(2 pi).                               (5)

Thus the deterministic extreme class singled out by (2)-(3) is not contained in the weak closure of the normalized Gaussian-mixture class M<=sqrt(2 pi).

There is also a scale-conservation obstruction to repairing (5) by dilation. Approximate all three active marginals by such mixtures and let

a_i = M_i/sqrt(2 pi).

Eventually a_i >= N-o(1). Scaling Y_i=a_i X_i normalizes the inverse-half-variance moments, but transforms B_* to

B_N = D_a^{-1} B_* D_a^{-1},
 D_a=diag(a_1,a_2,a_3).

Since ||D_a^{-1}|| <= (N-o(1))^{-1} and ||B_*||=1,

boxed{ ||B_N||_op <= (N-o(1))^{-2}. }                     (6)

So every eigenvalue of the normalized Hessian has modulus at most (N-o(1))^{-2}. Any scalar rescaling that restores three eigenvalues of modulus at least one must multiply the quadratic output by at least (N-o(1))^2; density scaling then loses at least that same factor. In contrast, the original rough laws already satisfy the constant bound (4). This is a proof-interface obstruction, not a QFORM counterexample.

For an unbounded-support endpoint, take

E_infty = union_{k>=1} [k^2,k^2+2^{-k}].

It has measure one and infinite total variation. It is itself an admissible extreme point of K, so (2)-(3) show that a correct cap-one localization theorem must retain such laws rather than regularize them through any class carrying a uniform BV budget.

## First unpaid implication

`QFORM-EXTREME-SET-WHOLELAW-RECEIVER-BEFORE-REGULARIZE-v1`: after the exact deterministic extreme-set reduction, expose a matrix-geometric whole-law receiver directly on arbitrary measurable unit-measure sets before imposing any BV, diameter, fragment-count, Gaussian-scale, or moment regularity. The environment-coupled localization is now zero-loss; the remaining debt is structural/analytic on the rough extreme sets themselves.
