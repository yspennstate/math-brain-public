# A full scalar affine-projection hierarchy is still insufficient

20 September 2026. Additional full-scope test after the packet and bilinear-control reports.

**This report does not prove or disprove FEI.** It disproves a stronger proposed relaxation quantified over arbitrary real Fourier vectors. Unlike the bilinear-control example, this construction satisfies the scalar coefficient-capacity consequences of Boolean projection quantization at **every codimension and every affine Fourier subspace**, not only at codimension one. It does not claim the signed square-convolution cancellations of that other example. The two sets of conclusions are distinct.

## 1. The exact Boolean projection consequence

Let f be a Boolean sign function on F_2^n. Let V be a k-dimensional physical subspace, k>=1, and eta a linear functional on V. Define the Fourier projection

    Q_(V,eta) f(x)=2^(-k) sum_(v in V) (-1)^eta(v) f(x+v).

Its Fourier support is the affine cell

    C={S: S dot v=eta(v) for every v in V}.

Its values are multiples of 2^(1-k), because the sum consists of an even number 2^k of signs. Hence, pointwise,

    |Q f| <= 2^(k-1) |Q f|^2.

For every S in C, its Fourier coefficient is unchanged by Q. Consequently

\[
\boxed{
\max_{S\in C}|\widehat f(S)|
\le2^{k-1}\sum_{S\in C}\widehat f(S)^2.
}
\tag{1}
\]

All affine subspaces of codimension k in the frequency cube arise this way. This includes the all-direction codimension-one inequality and, at codimension n, the nonzero-coefficient lower bound. Equation (1) is a necessary scalar consequence of Booleanity, not a characterization.

## 2. A distribution satisfying every inequality (1)

For n>=16 let epsilon=2/n. Let mu_2 and mu_3 be uniform probability measures on the subsets of sizes two and three, and let U_n be uniform on all 2^n subsets. Set

\[
\boxed{p=(1-\varepsilon)(\tfrac14\mu_2+\tfrac34\mu_3)+\varepsilon U_n.}
\tag{2}
\]

Choose real Fourier amplitudes a_S=sqrt(p_S), all positive, and let u be their inverse normalized Walsh transform. Then E u^2=1. It is not Boolean: u(0)=sum_S sqrt(p_S)>1, since p has more than one positive atom.

For n>=16, the largest nonuniform atom is at level two, since

    [3/(4 binom(n,3))]/[1/(4 binom(n,2))]=9/(n-2)<=1.

Therefore

\[
p_{\max}\le\frac1{2n(n-1)}+\frac2{n2^n}
\le\frac1{n^2}=\frac{\varepsilon^2}{4}.
\tag{3}
\]

For the last inequality, multiply by n^2: n/[2(n-1)]+2n/2^n is less than one at n=16, and both terms decrease thereafter.

Every affine cell C of codimension k has 2^(n-k) elements, and the uniform component in (2) gives

    p(C)>=epsilon 2^(-k).

Combining with (3),

\[
\max_{S\in C}|a_S|\le\varepsilon/2
\le2^{k-1}p(C)
\quad(1\le k\le n).
\tag{4}
\]

Thus all scalar projection-capacity inequalities hold simultaneously, for all affine cells of all codimensions. Neither a bounded codimension cutoff nor a union bound over cells is used.

## 3. Bounded energy and divergent erasure entropy

The energy of (2) is exactly

\[
\boxed{I_{\rm sp}(u)=(1-2/n)\frac{11}{4}+1
=\frac{15}{4}-\frac{11}{2n}<\frac{15}{4}.}
\tag{5}
\]

To lower-bound B(u), retain only the edges between levels two and three. The function E(r,s) from the main report is nondecreasing in both arguments and homogeneous of degree one. Hence the uniform component can be discarded for this lower bound. There are 3 binom(n,3) such edges. Their nonuniform endpoint masses have ratio

    [1/(4 binom(n,2))]/[3/(4 binom(n,3))]=(n-2)/9>1.

Since E(r,s)>=s log_2(r/s) for r>=s>0,

\[
\boxed{
B(u)\ge(1-2/n)\frac94\log_2\frac{n-2}{9}.}
\tag{6}
\]

It follows that

\[
\boxed{
\frac{B(u)}{I_{\rm sp}(u)}>
(1-2/n)\frac35\log_2\frac{n-2}{9}\longrightarrow\infty.
}
\tag{7}
\]

Thus even the complete scalar affine-projection hierarchy (1) does not imply a dimension-independent erasure/energy inequality for normalized real Fourier vectors.

## 4. Why this is not a contradiction to Boolean FEI

The values of the real inverse transform u are not signs. Inequalities (1) retained only one scalar consequence of each projected function's value quantization. They do not assert that those projected functions actually have the quantized values of Boolean projections, nor that u satisfies the signed convolution identities from u squared equal to one. The all-positive Fourier choice here in fact has positive off-zero convolution coefficients, so it does not satisfy those identities.

The bilinear-control example in `CAPACITY_OBSTRUCTION.md` has dyadic amplitudes, all directional coefficient capacities and any prescribed finite order of exact square cancellations. The distribution (2), in contrast, establishes **all codimensions of the scalar affine-projection capacities**, but makes no dyadic or square-cancellation claim. No example satisfying all those stronger conditions jointly has been constructed in this report.

This rules out closing the packet allocation merely by adding all scalar projection-capacity inequalities. A genuine full proof would need other consequences of exact Booleanity, or a different uniform allocation. The claimed result here is an explicit obstruction to that relaxation only. Independent review and publication-priority clearance remain unverified.

## 5. Verification

The `projection_hierarchy` section of `capacity_verification.json`, generated by `verify_capacity_obstruction.py`, verifies normalization, maximal-atom and energy formulas, all codimension lower certificates for the listed n, and the logarithmic lower ratio. It also evaluates the exact full erasure entropy by grouping the n+1 levels for the smaller listed dimensions. Such level formulas are not truth-table enumeration and do not enumerate every affine subspace; the analytic uniform-mass argument proves the all-cell assertion.
