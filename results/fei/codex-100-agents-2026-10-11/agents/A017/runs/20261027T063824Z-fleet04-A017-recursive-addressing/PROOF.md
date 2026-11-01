# One nonlinear multiplier throughout a restriction tree

Uniform physical cubes, Boolean signs and entropy in bits. These are author proofs pending independent reconstruction. Full FEI remains OPEN. A multiplier is fixed at the root; descendants use its actual restrictions, never a newly chosen multiplier.

## 1. The entropy capacity of a Fourier-support coset

For a Boolean c, let A_c={s:chat(s) != 0}, choose a in A_c and put V_c=span_F2{s+a:s in A_c}, r(c)=dim V_c. Parseval makes A_c nonempty, including for constants. The definition is independent of a. A character has r=0, even if it uses many physical coordinates.

For every Boolean f on the SAME physical cube,

    |H(fc)-H(f)| <= r(c).                                      (1)

Here is a direct proof that includes coherent coefficient collisions. Multiplication by c is a real orthogonal operator on normalized Walsh amplitude vectors, since c^2=1. Its convolution support lies in a+V_c, so it maps the coordinate subspace indexed by each V_c-coset Q into the subspace indexed by Q+a. Its inverse has the reverse mapping, and both spaces have dimension 2^r. Consequently it preserves the squared norm of each such block, up to the permutation Q -> Q+a. The two spectra have the same block-mass entropy. Within each nonzero block the conditional spectral entropy is between 0 and r. The entropy chain rule proves (1); zero-mass blocks contribute zero. No independence between f and c is used. The operator acts on amplitudes BEFORE entropy is taken.

For either physical restriction c_b of c at any coordinate i,

    r(c_b) <= r(c).                                           (2)

Indeed the restricted Walsh support is contained in the coordinate-deletion projection of A_c: coefficients become chat(s) + or - chat(s+i). Its affine span is contained in the projected affine span of A_c. Cancellation can only remove support. This proves (2), including deterministic children.

## 2. An exact original-multiplier ledger

At a reached node v write f_v,c_v for actual restrictions and g_v=f_v c_v. Set

    E_v = H(g_v)-H(f_v),     Phi_v=r(c_v)+E_v.

By (1), 0<=Phi_v<=2r(c_v). For a physical query with BOTH children retained, define

    Omega_v=Delta_i(g_v)-Delta_i(f_v),
    rho_v=r(c_v)-(r(c_0)+r(c_1))/2 >= 0.

The exact identity is

    Omega_v=Phi_v-(Phi_0+Phi_1)/2-rho_v.                       (3)

For every finite adaptive physical stopping tree, with original uniform reach weights w_v and full terminals L,

    sum_v w_v Omega_v
      = Phi_root-E_L Phi_L-sum_v w_v rho_v
      = E_root-sum_leaf w_leaf E_leaf
      <= Phi_root <= 2r(c).                                 (4)

Here E_L in the first line means expectation over reached leaves. Equivalently the second line is E_root-sum_leaf w_leaf[H(g_leaf)-H(f_leaf)]. The notation does not discard either full leaf entropy.

Equations (3)-(4) are a SIGNED ledger. They do not bound sum w max(0,Omega_v). A negative correction may fund a later positive correction, and the still nonnegative Phi of BOTH descendants stays reserved. The multiplier, its gate labels, and its physical support belong to the original root throughout.

If c is independent of every queried physical coordinate (though it may overlap arbitrarily with the other coordinates of f), then c_v is the same c on every path, rho_v=0, and Inf_i(g_v)=Inf_i(f_v). Thus any supplied baseline policy satisfying Delta_i(f_v)<=K Inf_i(f_v) obeys

    H(g_root) <= K P_T + E H(g_L) + Phi_root-E Phi_L,          (5)
    I(g_root) = P_T + E I(g_L),

where P_T is ACTUAL queried influence, not influence of a replacement root. Therefore one already allocated ORIGINAL source of at least Phi_root (or the explicit sufficient amount 2r(c)) pays the ENTIRE signed overlap correction, independent of depth, number of factors, order, and stopping. Old debits must be deducted before this allocation; both full actual terminal entropies and terminal reserves remain. Equation (5) supplies no initial source at influence price.

If the policy queries c's coordinates, preserve the extra exact physical term

    Inf_i(g)-Inf_i(f)
       = E[1_{c(x)!=c(x^i)} f(x)f(x^i)].                    (6)

Indeed the edge changes its disagreement indicator precisely when c flips, replacing disagreement by agreement. Consequently

    Delta_i(g)-K Inf_i(g)
      = Delta_i(f)-K Inf_i(f)+Omega_i
        -K E[1_{c(x)!=c(x^i)} f(x)f(x^i)].                 (7)

The influence difference itself telescopes with BOTH full terminal influence differences. Even a character can change queried influence, so r=0 is not permission to omit (6).

## 3. The initial rank reserve is not universally influence-priced

For every integer m>=2, let x be one selector, y in F2^m and

    c(y)=1-2*1_{y=0},
    f(x,y)=1-2*1_{x=1,y=0},
    g(x,y)=1-2*1_{x=0,y=0}.

Then g=fc on the SAME physical cube. Both f and g are actual single-point defects, translated by x, so H(g)=H(f). The Fourier support of c is the entire y-cube: chat(0)=1-2^(1-m), chat(s)=-2^(1-m) for s!=0. Thus r(c)=m and

    Phi_root=m,
    I(g)=(m+1)2^-m,
    Phi_root/I(g)=m*2^m/(m+1) >= 2^(m-1).                  (8)

The sole x-query has identical Delta for f and g, identical actual influence 2^-m, and Omega=0. Its children are simply interchanged, one constant and one point defect. Therefore (8) refutes the proposed UNIVERSAL admission Phi_root<=K I(g), for every finite K, even with a real fresh query and fully overlapping nonlinear data multiplier. The explicit sufficient price 2r(c) fails for the same reason. This is overcharging by this reserve, not a necessary entropy cost, a counterexample to FEI, or failure of every possible source.

The entropy-capacity endpoints are sharp: a bent c on an even-dimensional full support has H(c)=r(c); taking f=1 gives Phi=2r and taking f=c gives Phi=0. Constants and characters give Phi=0. These are validation boundaries, not a claim that every c attains either endpoint.

## 4. What is closed, and the first unsupported line

The global signed entropy correction is localized in ONE hereditary, nonnegative reserve, with an explicit rank refund when a shared label is queried and exact physical influence transport. This applies to arbitrary overlapping Boolean cores. Author proof is the attained rung, pending the exact checks and external reconstruction recorded in REPORT.md; a scalar Lean certificate, if obtained, covers only the algebra of (3), not the Fourier entropy argument.

The first unsupported universal line is admission of an entropy-sensitive original reserve from the SAME still unused physical influence account, after old U and both full terminals, with a normalization that vanishes on the translated-defect fixture. Admission of the rank envelope is rigorously false by (8). Nor does a signed telescope license the positive-part boundary invoice. The next action is to construct a vacuum/translation-normalized coherent reserve, or expose a genuine positive-transport obstruction to it, rather than optimize the already refuted derivative proxy or repeat finite-factor histories.
