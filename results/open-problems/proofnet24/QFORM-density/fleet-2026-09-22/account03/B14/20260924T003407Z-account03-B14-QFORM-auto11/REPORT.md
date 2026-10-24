SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-24T00:34:07Z.
attacking: an environment-translation-safe Schur localization for a fully coupled physical triple, replacing a small singular-value payment by an opposite-sign physical diagonal whenever available.

# account03/B14 — sign-opposite Schur localization through arbitrary translations

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T003407Z-account03-B14-QFORM-auto11`  
Role: translations and localization  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity: the theorem below proves an essentially bounded density. The unrestricted continuity question is recorded separately and is not used to manufacture the height bound.

## 1. Fresh controls and source state

Fresh owner control was resolved on `yspennstate/math-research-brain` main. OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The live correction state was read before this proof. In particular, this report does **not** use post-rotation independence, a generic joint-density/coarea bound for an indefinite quadratic, conditional projection-density caps, pointwise van-der-Corput decay, bounded support, moments, a bounded fragment count, or a small-coefficient-as-small-random-error argument.

The designated completed partner actually applied below is:

`yspennstate/math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260924T001624Z-account04-B14-scaled-schur-localization-r10/REPORT.md`.

Its theorem says that if an ORIGINAL-coordinate principal triple has least singular value `sigma>0`, arbitrary outside couplings and affine leakage satisfy

`||p_Q||_(infinity,ess) <= 6 sqrt(pi)/sigma`.                         (1.1)

The theorem proved here is different: it exploits an indefinite physical pair and an opposite-sign diagonal to avoid paying the least singular value of that pair. It is translation-uniform even when the translations inside the pair depend on the third active coordinate.

## 2. Two elementary lemmas

### Lemma 2.1 — positive/negative definite two-square pushforward with a joint cap

Let `(U,V)` have a joint probability density `h<=M`. Let `r,s` be nonzero and have the same sign. For arbitrary deterministic centers `u0,v0`,

`R=r(U-u0)^2+s(V-v0)^2`

has an essentially bounded density and

`||p_R||_infinity <= pi M/sqrt(|rs|).`                                (2.1)

Proof. After reflecting the output if necessary assume `r,s>0`. For every finite interval `I=(a,b)`, the inverse image of `I` under `r u^2+s v^2` has Lebesgue area at most

`pi |I|/sqrt(rs)`.

Indeed the sublevel area at level `t>=0` is exactly `pi t/sqrt(rs)`. Multiplication by the joint cap `M` proves interval domination, hence (2.1). Translations have Jacobian one. QED.

### Lemma 2.2 — dependence-safe square receiver

Let `R` have density cap `K`. Let `Z` be a cap-one scalar which, conditional on all variables generating `R`, remains a translated copy of one fixed cap-one density. More generally it is enough that, conditional on `R=r`, the receiver variable `Z_r` has density cap one. For `d!=0`,

`T=R+d Z_R^2`

has

`||p_T||_infinity <= 2 sqrt(K/|d|).`                                  (2.2)

Proof. For `d>0`, conditional on `R=r`, the density of `dZ_r^2` is bounded by

`y^(-1/2)|d|^(-1/2) 1_(y>0)`.

Therefore

`p_T(t) <= |d|^(-1/2) int_(r<t) p_R(r)(t-r)^(-1/2)dr.`

Among all probability densities capped by `K`, the last integral is maximized by placing density `K` on the interval of length `1/K` immediately adjacent to `t`. Hence it is at most `2 sqrt(K)`. The case `d<0` follows by reflection. No independence between `R` and the random receiver translation is required. QED.

The key localization feature is that Lemma 2.2 pays a random translation **after** the bounded two-square core is formed. It never takes a supremum over normalized fibers.

## 3. Environment-translation theorem for an indefinite physical pair

Let `(S,E)` have an arbitrary joint law such that the scalar marginal `S` has a probability density bounded by `M`. Let `Y,Z` be mutually independent, independent of `(S,E)`, with probability densities bounded by one. Let `F,G` be arbitrary measurable real functions of `(S,E)`. Put

`y=Y+F(S,E),    z=Z+G(S,E).`

Let

`B=[[a,c],[c,d]]`,
`D=-det(B)=c^2-ad>0`,                                                    (3.1)

so `B` is indefinite. Let `L!=0`, `s0,q0` be arbitrary, and define

`Q=L(S-s0)^2 + a y^2+2c yz+d z^2+q0.`                                  (3.2)

### Theorem 3.1 — `QFORM-SIGN-OPPOSITE-SCHUR-LOCALIZATION-v1`

If `a!=0` and `La<0`, then

`boxed(
 ||p_Q||_(infinity,ess)
 <= 2 sqrt(pi M) ( |L| D |a| )^(-1/4).
)`                                                                         (3.3)

If `d!=0` and `Ld<0`, then

`boxed(
 ||p_Q||_(infinity,ess)
 <= 2 sqrt(pi M) ( |L| D |d| )^(-1/4).
)`                                                                         (3.4)

Consequently, if

`m_opp=max( {|a|: aL<0}, {|d|: dL<0} )>0`,

then

`boxed(
 ||p_Q||_(infinity,ess)
 <= 2 sqrt(pi M) ( |L| D m_opp )^(-1/4).
)`                                                                         (3.5)

There is no dependence on the laws or support geometry of `E,Y,Z`, on support diameter, fragment count, fragment separation, moments, or the size/oscillation of `F,G`.

### Proof of the `aL<0` case

Complete the square in the `Y` direction **algebraically**, without changing probabilistic coordinates:

`a y^2+2c yz+d z^2
 = a (y+(c/a)z)^2 + b z^2,`

where

`b=d-c^2/a = -D/a.`                                                     (3.6)

Because `aL<0`, `b` has the same sign as `L`. Define

`R=L(S-s0)^2+b z^2+q0.`                                                  (3.7)

The pair `(S,z)` has a joint density capped by `M`. Indeed, disintegrate the law of `E` given `S=s`. Conditional on `(S,E)=(s,e)`, `z=Z+G(s,e)` is a translate of the cap-one density of `Z`. Thus

`h_(S,z)(s,v)
 = p_S(s) int f_Z(v-G(s,e)) kappa_s(de)
 <= p_S(s)
 <= M.`                                                                 (3.8)

Lemma 2.1 and `|b|=D/|a|` give

`||p_R||_infinity
 <= pi M/sqrt(|L b|)
 = pi M |a|^(1/2)/( |L| D )^(1/2).`                                    (3.9)

Now set

`W=Y+F(S,E)+(c/a)[Z+G(S,E)].`                                           (3.10)

Conditional on `(S,E,Z)`, the variable `W` is a translate of `Y`, so its conditional density is capped by one. Since `R` is measurable with respect to `(S,E,Z)`, disintegrating over `R=r` makes the conditional law of `W` a mixture of translated copies of the same cap-one `Y` density. Hence its conditional density remains capped by one. Equation (3.2) is exactly

`Q=R+aW^2.`                                                             (3.11)

Lemma 2.2 and (3.9) therefore imply

`||p_Q||_infinity
 <=2 |a|^(-1/2)
      [pi M |a|^(1/2)/( |L|D )^(1/2)]^(1/2)
 =2 sqrt(pi M)(|L|D|a|)^(-1/4),`

which is (3.3).

The `dL<0` case is identical after swapping `Y` and `Z`. This proves the theorem. QED.

### Why the arbitrary translations really are free

The potentially dangerous translations `F(S,E),G(S,E)` may be unbounded, fragmented, or depend arbitrarily on the environment and on the active scalar `S`. They are never estimated. They only enter (3.8) as translations of a cap-one density and (3.10) as the center of the final cap-one square receiver. Thus this branch has zero translation/tail tax.

## 4. Physical 3x3 Schur version

The previous theorem can be read directly as a physical-principal-triple certificate. Let three ORIGINAL independent cap-one coordinates be `(S,Y,Z)` and let their principal block be

`A_I=[[alpha, r^T],[r,B]]`,                                             (4.1)

where `B` is the indefinite `2x2` matrix (3.1). Assume `B` is invertible and define its scalar Schur complement

`L=alpha-r^T B^(-1)r !=0.`                                              (4.2)

Condition on all original coordinates outside `I`. They create arbitrary affine coefficients. Completing the `B` block gives

`Q_w=L(S-s_w)^2
    +( [Y,Z]^T + B^(-1)r S + t_w )^T
       B
      ( [Y,Z]^T + B^(-1)r S + t_w )
    +const_w,`                                                          (4.3)

for deterministic `s_w,t_w` at fixed outside value `w`. Thus Theorem 3.1 applies with `M=1`. If one physical diagonal of `B` has sign opposite `L`, then

`boxed(
 ||p_Q||_(infinity,ess)
 <=2 sqrt(pi)( |L| |det B| m_opp )^(-1/4).
)`                                                                         (4.4)

All couplings to the outside coordinates are free because (4.4) is uniform in the affine terms.

This is complementary to a least-singular-value certificate. It can remain strong when the indefinite physical pair is highly anisotropic, provided an opposite-sign physical diagonal is still substantial.

## 5. Actual application of the designated account04/B14 result

Take the exact-target physical triple

`A0=diag(1,B0),    B0=[[-1,1],[1,1]].`                                  (5.1)

Its eigenvalues are

`1, +sqrt(2), -sqrt(2)`,                                                (5.2)

so all three have absolute value at least one. The newest designated partner `account04/B14` applies with

`sigma_min(A0)=1`

and therefore gives the concrete inequality

`boxed(
 ||p_(X^T A0 X)||_(infinity,ess)
 <=6 sqrt(pi)
 =10.634723105433096... .
)`                                                                         (5.3)

This is an actual use of the partner theorem, not merely a citation.

Now apply Theorem 3.1 to the same matrix. Here `L=1`, `D=2`, and the opposite-sign diagonal is `a=-1`, so

`boxed(
 ||p_(X^T A0 X)||_(infinity,ess)
 <= 2 sqrt(pi)/2^(1/4)
 =2.9809001788581804... .
)`                                                                         (5.4)

The same bound survives arbitrary ambient outside coordinates and couplings whenever this principal triple and its Schur data are retained, because outside conditioning contributes only affine translations already paid in (4.3).

Thus the new localization is quantitatively nonvacuous: on this fully coupled target triple it improves the partner's general scaled-principal-triple certificate by more than a factor of three.

## 6. Relation to the live exact-coordinate hyperbola branch

The newest complementary B05 work pays the exact double-zero scalar-pair face by retaining a coordinate hyperbola and averaging it against a Schur square before maximalisation. Theorem 3.1 pays a different **punctured** region: as soon as an indefinite pair has a physical diagonal of sign opposite the scalar Schur coefficient, the diagonal can be used as a dependence-safe square receiver after the same-sign Schur core has been paid.

The estimate intentionally deteriorates like `m_opp^(-1/4)` as that opposite-sign diagonal tends to zero. Therefore it does **not** solve the still-delicate interpolation through the exact double-zero face, and no small-coefficient perturbation claim is being made. The correct next splice is to bridge the exact coordinate-hyperbola estimate at `m_opp=0` to (3.5) without paying an inverse power of `m_opp`.

## 7. Status and remaining obligation

* `QFORM-SIGN-OPPOSITE-SCHUR-LOCALIZATION-v1`: **PROVED**.
* Arbitrary translations, distant fragments, unbounded supports, and moment-free inputs: **PAID on this branch with zero extra tax**.
* Designated partner account04/B14 r10: **APPLIED at the explicit target inequality (5.3)**.
* General output continuity from Theorem 3.1: **not claimed**; it proves an essentially bounded density. On fixed original-coordinate rank-three target instances, the independently completed fixed-matrix `C_0` regularity theorem may be combined after the height estimate, but continuity is not used here.
* Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.

First unpaid implication for this route:

`QFORM-SIGN-SCHUR-TO-DOUBLEZERO-UNIFORM-INTERPOLATION-v1`:

> bridge the exact coordinate-hyperbola endpoint and the sign-opposite Schur-square estimate uniformly as `m_opp ->0`, while preserving arbitrary environment-dependent translations and without moments, support bounds, or normalized-fiber caps.
