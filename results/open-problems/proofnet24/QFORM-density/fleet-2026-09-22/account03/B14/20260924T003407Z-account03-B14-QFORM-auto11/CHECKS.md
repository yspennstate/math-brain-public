# Deterministic checks — account03/B14 `20260924T003407Z-account03-B14-QFORM-auto11`

Result checked: `QFORM-SIGN-OPPOSITE-SCHUR-LOCALIZATION-v1`.

## 1. Algebraic square completion

For

`B=[[a,c],[c,d]]`, `D=c^2-ad>0`,

completion in the `Y` coordinate gives

`a y^2+2c yz+d z^2
 =a(y+(c/a)z)^2 +(d-c^2/a)z^2`

and

`d-c^2/a=(ad-c^2)/a=-D/a`.

Hence if `aL<0`, the Schur coefficient `-D/a` has the same sign as `L`, exactly as required by the definite two-square core.

Random floating-point substitutions were also checked: the two expressions agreed to machine precision (`<2e-15`) on sampled indefinite matrices.

## 2. Constant simplification

The definite core has

`K=pi M/sqrt(|L|D/|a|)
  =pi M |a|^(1/2)/( |L|D )^(1/2)`.

The dependence-safe square receiver contributes `2 sqrt(K/|a|)`, so

`2 |a|^(-1/2) K^(1/2)
 =2 sqrt(pi M)|a|^(-1/4)(|L|D)^(-1/4)
 =2 sqrt(pi M)(|L|D|a|)^(-1/4)`.

The dimensions are correct: `L`, `sqrt(D)`, and `a` each scale linearly with the quadratic matrix, so `(L D a)^(-1/4)` scales as the inverse of one quadratic-output coefficient.

## 3. Explicit target triple

For

`A0=[[1,0,0],[0,-1,1],[0,1,1]]`,

numerical symmetric eigensolve gives

`(-1.4142135623730951, 1.0, 1.4142135623730951)`,

matching the exact spectrum `{-sqrt(2),1,sqrt(2)}`. Thus `sigma_min(A0)=1` and account04/B14 r10 gives

`6 sqrt(pi)=10.634723105433096...`.

For the new theorem,

`L=1`, `D=-(det [[-1,1],[1,1]])=2`, `m_opp=1`,

so

`2 sqrt(pi)/2^(1/4)=2.9809001788581804...`.

The partner/new-bound ratio is

`3.5676213450081633...`.

## 4. Translation/provenance check

In the `aL<0` proof, the bounded core is measurable with respect to `(S,E,Z)`. The final square variable is

`W=Y+F(S,E)+(c/a)(Z+G(S,E))`.

Conditional on `(S,E,Z)`, `W` is a translate of the original `Y`; hence its conditional density is capped by one. Disintegrating further over the core value produces a mixture of translated `Y` densities and preserves that cap. No independence after a shear/rotation is asserted.

Similarly, the joint law of `(S,Z+G(S,E))` has density at most `p_S(s)<=M` because, conditional on `S=s`, it is a mixture of translations of the cap-one `Z` density. Thus arbitrary environment-dependent translations do not introduce a hidden conditional-density denominator.

## 5. Scope guard

The theorem deteriorates as `m_opp^(-1/4)` and therefore does not bridge the double-zero diagonal limit. It is a supporting localization theorem, not a proof of full QFORM. No moment, support, connectedness, Gaussian, log-concavity, post-rotation independence, or pointwise oscillatory-decay assumption is used.
