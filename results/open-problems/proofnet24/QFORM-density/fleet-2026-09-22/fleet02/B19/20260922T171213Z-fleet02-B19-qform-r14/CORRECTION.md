# Correction — factor two in the cross-cut half-Hölder constant

This addendum **supersedes the numerical constant only** in Theorem 2.1 and its tau=3/10 corollary in `REPORT.md`. The theorem's exponent, hypotheses, and qualitative branch closure remain valid.

In the TT* proof, if both `T(U,V)` and `T(U',V)` lie in an interval K of length h, then

`|F(U)-F(U')+2(C^T Z)^T V| <= h`,  `Z=U-U'`.

For fixed Z with `w=C^TZ !=0`, the scalar `w^T V` has density at most `e^(1/2)/||w||`. The displayed inequality restricts `w^T V` to an interval of length **h**, not h/2. Equivalently, `2w^TV` has density cap `e^(1/2)/(2||w||)` and is restricted to an interval of length 2h. Thus the correct conditional bound is

`P( ... | Z) <= h e^(1/2)/||C^T Z||`,

rather than the factor-two-smaller expression in the primary report.

The unchanged two-dimensional inverse-radius estimate is

`E ||C^T Z||^(-1) <= 2 sqrt(pi e/(s1 s2))`.

Therefore the corrected theorem is

### `QFORM-CROSSCUT-HALF-HOLDER-v1-corrected`

For independent original-coordinate blocks U,V with coordinate density caps one, arbitrary measurable F(U),G(V), and rectangular C with `s1(C)>=s2(C)>0`, every interval K of length h satisfies

`P(F(U)+2U^T C V+G(V) in K)`
` <= sqrt(2e) pi^(1/4) h^(1/2) (s1(C)s2(C))^(-1/4)`.          (C.1)

The random-cut product lower bound is also retained, but one sentence in its proof is corrected. From `s1+s2>tau/2` and `s2>=tau/16`, it does **not** follow that `s1>7tau/16` for every such cut. What is needed and true is the product bound

`s1 s2 > 7 tau^2/256`.

Indeed, if `tau/16 <= s2 <= tau/4`, then `s1>tau/2-s2` and the concave product `s2(tau/2-s2)` is minimized at an endpoint, with lower endpoint value `7tau^2/256`; if `s2>=tau/4`, then `s1>=s2` gives `s1s2>=tau^2/16`. In the complementary near-rank-one case `s2<tau/16`, one does have `s1>7tau/16`, exactly as used in the diffuse/localized branch.

At `tau=3/10`, `s1s2>63/25600`, so the corrected explicit half-Hölder constant is

`sqrt(2e) pi^(1/4) (63/25600)^(-1/4) = 13.9371688286... <13.938`.

Nothing in `QFORM-HIGH-SCHUR-OFFDIAG-PAID-v1` depends on the erroneous factor two: the parent quarter-kernel needs only a finite Hölder constant with exponent alpha=1/2>1/4. Hence the high-Schur-offdiagonal branch theorem remains valid, with the corrected quantitative constant.

Full QFORM remains OPEN.