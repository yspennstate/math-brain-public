# Independent reconstruction of the current spike-floor price

Units are bits. Full FEI remains OPEN. The reviewed claim is A046-SIGNED-SPIKE-FLOOR-PRICE@1, statement SHA256 b3f16657ec9a3decd1f703481f267b99b9c4b512f8a7637ea67d7164f801190a. Verdict: HOLDS unchanged at its supplied-source, declared-floor scope. This is an independent derivation, with no producer helper imported and no substantive repair supplied.

1. Let p,q be finite normalized laws, q positive on source-positive atoms. Partition their space into V and N. Write pi=p(N)>0 and rho=q(N)>0. On N the incoming conditional law is (1-beta)p_N+beta delta_M, beta<1. A fresh law R_gamma copies p on V and uses (1-gamma)p_N+gamma delta_E on N, with gamma<1. Both M and E may have zero source mass. Every source-positive denominator remains positive because beta,gamma<1. No reference-only atom is dropped.

Retain each V atom separately and merge N. The KL of these coarse laws is L=sum_V p log2(p/q)+pi log2(pi/rho)>=0. This remains true when pi=1: reference mass outside the source is included through rho. The conditional KL on N is exactly a BINARY KL: partition N into the target singleton and its complement. The conditional laws inside the complement agree, so its conditional KL is zero. For t=p_N(E), the remaining divergence is

    d_t(u)=D_2(Ber(t) || Ber(t+u(1-t))).

Thus d_0(u)=-log2(1-u), d_1(u)=0, and for 0<t<1 it equals (1-t)log2(1/(1-u))+t log2(t/(t+u(1-t))). Coarse-graining and the binary decomposition independently give

    D(p||q)=L+pi d_tM(beta),
    CE(p,R_gamma)-CE(p,q)=pi[d_tE(gamma)-d_tM(beta)]-L.

This is a signed CURRENT difference. Using only conditional KL, or resetting sector masses without retaining L, changes the account.

2. For 0<t<1, multiplying the derivative by ln(2) gives

    (1-t)/(1-u)-t(1-t)/(t+u(1-t))
      =u(1-t)/[(1-u)(t+u(1-t))].

Every denominator is positive for u in [0,1). Consequently d_t is strictly increasing from zero on that interval when t<1; for t=0 use -log2(1-u) directly, and for t=1 the law is constant. Therefore the minimum over a DECLARED required gamma>=ell is attained at ell. If t_E<1 the minimizing parameter is unique. The maximal free parameter is the unique solution of d_tE(gamma)=d_tM(beta)+L/pi. Continuity, strict increase and divergence at 1 justify existence and uniqueness, including zero right-hand side. At a source-zero target the solution is 1-2^(-d_tM(beta)-L/pi). This proves the continuum statement; the finite test is not used as an extrapolation.

The same-mask cap gamma<=beta is sufficient, since it makes the difference nonpositive before subtracting L. When t_M=0 it is also sufficient for an arbitrary new target because d_t(u)<=d_0(u): the target contribution is nonpositive and the complementary contribution is at most d_0. It is NOT sufficient for arbitrary unrelated targets: t_M=1 gives d_tM(beta)=0, whereas t_E=0 gives positive cost for every gamma>0. These endpoint hypotheses are used, rather than silently generalized.

An adversarial sign control distinguishes current references. With p=(1/4,3/4,0), q=(1/2,1/2,0), vacuum the first atom, and a source-zero spike target, ell=1/9 yields R=(1/4,2/3,1/12). Its signed price obeys 2^(4 sigma)=27/32<1. With incoming q=p the same reset has strictly positive price. The checker verifies both exact signs.

3. The endpoint expansion explains the boundary discontinuity. For fixed 0<t<1, the displayed derivative divided by u tends to (1-t)/(t ln2). Integrating on a fixed small interval gives

    d_t(u)=(1-t)u^2/(2t ln2)+O_t(u^3).

For t=0 instead, d_0(u)=u/ln2+O(u^2). For t=1 it vanishes. The fixed-t remainder is not uniform as t decreases to zero. In particular no universal quadratic upper bound K u^2 can cover source-zero targets. The explicit Boolean circuit below realizes that endpoint, so the distinction is not an artifact of arbitrary probability vectors. This is a scalar corollary of the reviewed formula, not an additional universal potential theorem.

4. Reconstruct the actual Boolean witness without any probability-law relaxation. Let m(x,y,z)=x when z=1 and y when z=-1, and h(x,y,z)=xyz. Let f(a,x,y,z)=m when a=1 and h when a=-1. Then m=(x+y+xz-yz)/2. The parent has eight Fourier masses 1/16 and two masses 1/4; H(f)=3 and I(f)=11/4. Both children are balanced with essential mask xyz; their full-mask masses are 0 and 1. Sign conventions only exchange labels and do not change squared spectra.

Supply Q_alpha=(1-alpha)P_f+alpha delta_axyz, 0<alpha<1. Erase a and use the SAME coherent kernel k_b(T)=P_child_b(T)/(2 P_erased(T)); source-zero rows use the declared fair fallback. The spike lies on the xyz row and goes entirely to the parity outcome. Thus reference outcome probabilities are ((1-alpha)/2,(1+alpha)/2). Each normalized inherited child equals its actual spectrum. Root KL is

    K_alpha=-(3/4)log2(1-alpha)-(1/4)log2(1+3alpha).

The outcome KL is -log2(1-alpha^2)/2 and the erasure loss is their difference. KL chain rule says their sum is ALL K_alpha; no entry KL survives at the terminal frontier. A required new gamma>0 tilt at the full child mask costs -log2(1-gamma) on m and zero on h, so its paired invoice is F_gamma=-log2(1-gamma)/2>0. The complete query-plus-floor bill is K_alpha+F_gamma, not F_gamma compared against a reusable K_alpha. This holds for all alpha,gamma in (0,1). No claim that the original influence surplus is insufficient follows.

5. At a complete frontier with actual reaches w_h, changing references replaces C by C+sum_h w_h sigma_h. With the SAME original capacity B and old bills U, payment is equivalent to sum_h w_h sigma_h<=B-C-U. This is literal cancellation; it credits a negative price once. Along a physical-query tree, log-sum and the same-kernel KL chain give root KL plus reached signed resets equal to the sum of reached erasure losses, outcome KL and full terminal KL. Finite telescoping needs no interchange of limits. Retaining only the terminal KL without the query losses invalidates the payment conclusion.

6. Checks that could fail were tested explicitly: finite support and zero source targets; pi=1; matched and mismatched vacuum; t=0 and t=1; beta=0; unrelated target with larger invoice; exact parent and child spectra; physical normalization of BOTH outcomes; erasure, outcome and terminal KL; nonzero denominators; and distinction between entry KL and unused capacity. code/check.py uses independent literal Walsh sums, Fraction arithmetic and canonical prime-exponent log identities. Exact integer powers decide signs. It imports no A046 or A049 code. All finite counts and runtimes are in out/PILOT.json and out/CHECK.json.

Rung: analytic proof independently reconstructed and finite identities/signs exactly checked; NOT Lean-checked. A formal numerator statement is supplied separately but uncompiled. The installed Mathlib wrapper documents approximately 4098 MB per compile, exceeding the task's 1536 MB job cap, and its default evidence writes leave A047. Neither the wrapper nor a compiler was launched. No formal pass is implied.

The first unsupported universal line remains a useful NECESSARY arbitrary-core profile/stopping rule and an ORIGINAL O(I) complete source whose genuine unused capacity pays every required query, reset, old bill and full terminal entropy. Free inherited transport alone does not pay CE: q=p has zero KL but CE=H(p). No full FEI theorem, universal constant improvement or counterfamily is obtained.
