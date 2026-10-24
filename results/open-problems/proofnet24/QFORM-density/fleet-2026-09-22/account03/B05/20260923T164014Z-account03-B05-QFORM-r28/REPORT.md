SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-23T16:40:14Z.
attacking: QFORM-NEAR-DOUBLEZERO-ESCAPED-CURVATURE-COAREA-v1 — retain the near-double-zero physical pair exactly and identify the determinant currency carried by the residual shear before reciprocal coarea inversion.

# account03/B05 r28 — inverse-pair shear determinant atlas and the punctured-null obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`.  
**Assignment:** quadratic coarea bound.  
**Owner continuation acknowledged:** `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository transport occurred, but repository transport is not verified native learned-memory ingestion.  
**Status:** `NEW SUPPORTING THEOREM / NEW TARGET-VALID STRESS FAMILY PAID / PARTNER APPLIED / FULL QFORM OPEN`.  
**Regularity:** the positive theorems below establish absolute continuity and an essential `L^infinity` bound in their stated branches. Continuity is not proved here.

## 1. Fresh sources and the exact remaining packet

Fresh owner control before publication was read from `yspennstate/math-research-brain` main (OWNER CONTROL revision `2026-09-22.15`, QFORM only), together with the new continuation request `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. The newest Claude continuation was also read at

`yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae:proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md`

and the small-nonzero-hub-diagonal report beneath `hub_with_diagonal/REPORT.md`. Its tangent-parabola mechanism confirms that a nonzero diagonal cannot in general be discarded as a small random perturbation. The new projected-crossing theorem at

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`

was read as a separate compatible exit; its row-marginal and projected-volume gates are not assumed in the packet below.

The immediate B05 predecessor is

`yspennstate/math-open-problems@a8018aa66b9ac536d0cbdb070a1c6fd8950fbf67:proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T150830Z-account03-B05-QFORM-r27/REPORT.md`.

Its live grouped packet has variables `(S,R,Y,Z)`. The pair `(S,R)` is an orthonormal two-dimensional projection of one original-coordinate product bank. The normalized scalar projections `Y,Z` use two disjoint original-coordinate banks and are independent of each other and of the first bank. Their density caps are at most `sqrt(2)`. The homogeneous packet matrix is

```
H = [[C,P],
     [P^T,B]],
B = [[a,c],[c,d]],
P = [[alpha,beta],[r,s]],
```

where `B` is invertible and indefinite and

```
C-P B^(-1)P^T = [[L,0],[0,0]],
L=lambda*m,
mu=|det B|*|lambda|,
m>=3/20.                                                   (1.1)
```

The previous raw-diagonal theorem paid every branch with a quantitative `max(|a|,|d|)` but deteriorated when both raw diagonals tend to zero. The exact-double-zero theorem in r22 paid a residual coupling measured by `sqrt(r^2+s^2)/|c|`. The point of this run is to compute the *exact invariant quantity connecting those two mechanisms*.

Two completed analytic receivers are consumed at equations below.

1. **Fresh-square / rank-two product-projection receiver.** Source used by r27:
   `yspennstate/math-open-problems@552cc02b9161cc94ce42b04200799d1ebd3635f2:proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260923T113953Z-account01-B16-QFORM-r12/REPORT.md`.
   In the present normalization it implies that if an independent scalar has nonzero quadratic coefficient `gamma` and the remaining two-dimensional product-projection Schur matrix `N` is invertible, then

   `||p||inf <=128*sqrt(2)*|gamma|^(-1/2)*|det N|^(-1/4)`.          (1.2)

   Arbitrary affine terms and the same-bank square shift are allowed.

2. **Dependence-safe null-scalar determinant theorem.** Canonical source
   `yspennstate/math-open-problems@1515e474fa8110a0b704a6ff73a25fc554005017:proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T211147Z/REPORT.md`.
   If a scalar of density cap `L0` is independent of a two-dimensional pair with joint density cap `M0`, its square coefficient is exactly zero, and the `3x3` quadratic matrix `G` is invertible, then

   `||p||inf <=3*2^(2/3)*(L0*M0)^(2/3)*|det G|^(-1/3)`.             (1.3)

   Here `L0<=sqrt(2)` and the orthonormal product-projection pair has joint density cap `M0<=e`, hence the prefactor is `6 e^(2/3)`.

The designated partner result is account04/B05

`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f:proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260923T041255Z-account04-B05-dominant-slope-r2/REPORT.md`,

which gives `||p_Q||inf<51.6(mu*m_*)^(-1/3)` for the largest exact-slope mass `m_*`.

## 2. The exact inverse-pair shear identity

Let

```
q=(r,s)^T,
Delta=det B=ad-c^2,
z=B^(-1)q=(z1,z2)^T.                                      (2.1)
```

Thus explicitly

```
z1=(d*r-c*s)/Delta,
z2=(-c*r+a*s)/Delta.                                       (2.2)
```

Condition first on the disjoint scalar `Z`. The retained homogeneous matrix on `(Y,S,R)` is

```
H_Y = [[a,     alpha, r],
       [alpha, C11,   C12],
       [r,     C12,   C22]].                              (2.3)
```

Conditioning instead on `Y`, the retained matrix on `(Z,S,R)` is

```
H_Z = [[d,    beta, s],
       [beta, C11,  C12],
       [s,    C12,  C22]].                                (2.4)
```

### Lemma 2.1 — exact conditional determinant coordinates

Under (1.1),

```
boxed:
 det H_Y = L*(c*r-a*s)^2/Delta = L*Delta*z2^2,
 det H_Z = L*(d*r-c*s)^2/Delta = L*Delta*z1^2.             (2.5)
```

Consequently

```
boxed:
 |det H_Y| = mu*m*z2^2,
 |det H_Z| = mu*m*z1^2,                                    (2.6)
```

and therefore

```
boxed:
 |det H_Y|+|det H_Z| = mu*m*||B^(-1)q||_2^2.               (2.7)
```

#### Proof

Write the first and second rows of `P` as `p=(alpha,beta)` and `q=(r,s)`. From (1.1),

```
C11=p^T B^(-1)p+L,
C12=p^T B^(-1)q,
C22=q^T B^(-1)q.                                           (2.8)
```

Substitute (2.8) into the determinant expansion of (2.3). Every term containing `p` cancels, leaving

```
det H_Y = L*(c*r-a*s)^2/Delta.                             (2.9)
```

The same calculation with the other scalar retained gives

```
det H_Z = L*(d*r-c*s)^2/Delta.                             (2.10)
```

Equations (2.2), `|L Delta|=m |lambda| |det B|=mu m`, and absolute values yield (2.6). Summing gives (2.7). QED.

### Geometric reading

`z=B^(-1)q` is exactly the shear by which the residual packet direction `R` enters the completed scalar pair. Equation (2.7) says that the entire pair of conditional rank-three determinants is not measured by raw `||q||`, by `sigma_min(B)`, or by one selected physical edge. It is exactly

```
mu*m*||B^(-1)q||^2.                                        (2.11)
```

At the exact double-zero pair `B=[[0,c],[c,0]]`,

```
B^(-1)q=(s/c,r/c),                                         (2.12)
```

so (2.7) recovers the normalized residual coupling of r22 with no approximation.

## 3. Main theorem: the shear-determinant atlas

Define the punctured square currency

```
chi = max(|d|*z1^2, |a|*z2^2).                             (3.1)
```

### Theorem 3.1 — `QFORM-RATIOPACKET-SHEAR-DETERMINANT-ATLAS-v1`

Under (1.1):

**(A) Nonzero-diagonal atlas.** If `chi>0`, then the full conditional packet has an essentially bounded density and

```
boxed:
 ||p_Q||inf <=128*sqrt(2)*(mu*m*chi)^(-1/4).               (3.2)
```

This estimate is independent of the ratio residual `sigma` and of `kappa=sigma_min(B)`.

**(B) One-null-diagonal boundary.** If `a=0` and `z2!=0`, then

```
boxed:
 ||p_Q||inf <=6 e^(2/3)*(mu*m*z2^2)^(-1/3).                (3.3)
```

If `d=0` and `z1!=0`, then

```
boxed:
 ||p_Q||inf <=6 e^(2/3)*(mu*m*z1^2)^(-1/3).                (3.4)
```

In particular, if `a=d=0` and `z!=0`, choosing the larger component gives

```
boxed:
 ||p_Q||inf
 <=6*2^(1/3)e^(2/3)*(mu*m*||z||^2)^(-1/3).                (3.5)
```

Equation (3.5) is exactly the r22 double-zero estimate after (2.12), but (3.3)-(3.4) are stronger: **only one raw scalar diagonal has to vanish; the other may be arbitrary.**

#### Proof of (A)

Suppose first `d z1!=0`. Condition on the independent scalar `Y`; affine terms generated by its value are allowed. The remaining variables are the independent scalar `Z` and the two-dimensional orthonormal product projection `(S,R)`, with quadratic matrix `H_Z`. Since `d!=0` and `det H_Z!=0`, scalar Schur complementation at `Z` produces an invertible rank-two matrix `N_Z` with

```
det H_Z=d*det N_Z.                                         (3.6)
```

Apply (1.2):

```
||p_Q||inf
 <=128*sqrt(2)*|d|^(-1/2)*|det N_Z|^(-1/4)
 =128*sqrt(2)*(|d|*|det H_Z|)^(-1/4).                     (3.7)
```

Using (2.6),

```
||p_Q||inf
 <=128*sqrt(2)*(mu*m*|d|*z1^2)^(-1/4).                   (3.8)
```

The same argument after interchanging `Y,Z` gives

```
||p_Q||inf
 <=128*sqrt(2)*(mu*m*|a|*z2^2)^(-1/4)                    (3.9)
```

whenever `a z2!=0`. Taking the better available estimate gives (3.2). No coordinate inside the `(S,R)` bank is conditioned, so no false `S|R` density cap appears. QED.

#### Proof of (B)

Assume `a=0` and `z2!=0`. Condition on `Z`. Then `Y` is an independent scalar with density cap at most `sqrt(2)`, `(S,R)` has joint density cap at most `e`, and the scalar square coefficient in `H_Y` is **exactly zero**. By (2.6), `H_Y` is invertible and

```
|det H_Y|=mu*m*z2^2.                                      (3.10)
```

Apply the null-scalar theorem (1.3). The density-cap prefactor is

```
3*2^(2/3)*(sqrt(2)*e)^(2/3)=6 e^(2/3),                  (3.11)
```

which proves (3.3). Equation (3.4) is symmetric. If both diagonals vanish, `max(z1^2,z2^2)>=||z||^2/2`; applying the corresponding null estimate proves (3.5). QED.

## 4. Quantitative branch consequences

The predecessor r27 only saw `delta_B=max(|a|,|d|)` and therefore paid

`128*sqrt(2)*(delta_B*mu*m)^(-1/4)`.                       (4.1)

The new atlas can remain uniform even when `delta_B ->0`, because the inverse-pair shear can diverge at exactly the compensating rate.

For example, whenever

```
mu>=1, m>=3/20, chi>=1/16,                                (4.2)
```

(3.2) gives

```
||p_Q||inf
 <=128*sqrt(2)*(3/320)^(-1/4)
 <582.                                                     (4.3)
```

The significance is not this constant but the fact that `chi` can stay order one while every raw diagonal tends to zero.

On a one-null boundary, if

```
mu>=1, m>=3/20, |z2|>=1/16                               (4.4)
```

with `a=0`, then (3.3) gives

```
||p_Q||inf <139.658.                                       (4.5)
```

The same holds with `(d,z1)` in place of `(a,z2)`.

## 5. A target-valid diffuse stress family paid by the new atlas while the exact-slope estimate deteriorates

The gain in (3.2) is not cosmetic. Fix an odd `N>=5` and choose a phase `phi` avoiding zeros of the cosine. On a bank of `N` independent cap-one coordinates define the orthonormal coefficient vectors

```
u_j=sqrt(2/N) cos(2*pi*j/N+phi),
t_j=sqrt(2/N) sin(2*pi*j/N+phi),
S=u dot X, R=t dot X.                                      (5.1)
```

For odd `N`, the ratios `t_j/u_j` are all distinct, so every exact-slope class has `u`-mass at most `2/N`. Thus the designated partner parameter satisfies

```
m_*<=2/N.                                                  (5.2)
```

Let `0<eps<=1/2` and in projected coordinates `(S,R,Y,Z)` set

```
B_eps=[[eps,1],[1,eps]],
q_eps=(eps^(-1/2),0),
p=(0,0),
L_eps=1/(1-eps^2),
C=diag(L_eps,-L_eps).                                      (5.3)
```

Then `C-P B_eps^(-1)P^T=diag(L_eps,0)`, `m=1`, and

```
mu=|det B_eps|*L_eps=1.                                   (5.4)
```

Moreover

```
z=B_eps^(-1)q_eps
  =(-sqrt(eps)/(1-eps^2), 1/(sqrt(eps)(1-eps^2))),         (5.5)
```

so

```
chi=max(eps*z1^2,eps*z2^2)=1/(1-eps^2)^2>=1.              (5.6)
```

The projected matrix is

```
H_eps=
[[ L_eps, 0,             0,   0],
 [ 0,    -L_eps, eps^(-1/2),  0],
 [ 0, eps^(-1/2),        eps, 1],
 [ 0,     0,              1, eps]].                       (5.7)
```

Its rank is three. The last `3x3` block has rank two, and its principal `(Y,Z)` block has eigenvalues `eps-1` and `eps+1`. Cauchy interlacing therefore puts one nonzero eigenvalue of the last block at most `eps-1<=-1/2` and the other at least `eps+1>=1`; its remaining eigenvalue is zero. The decoupled `S` eigenvalue is `L_eps>=1`. Hence **`2H_eps` has at least three eigenvalues of absolute value at least one**. Embedding the orthonormal frame `(u,t,e_Y,e_Z)` into the original coordinates preserves those nonzero eigenvalues. This is an exact target-valid family, with arbitrary independent cap-one input laws.

For `2H_eps`, the parameters scale to `mu'=8`, `a'=d'=2eps`, while `z` is unchanged. Thus

```
mu'*max(|d'|z1^2,|a'|z2^2)
 =16/(1-eps^2)^2.                                          (5.8)
```

The new atlas gives the uniform target bound

```
boxed:
 ||p_(X^T(2H_eps)X)||inf
 <=64*sqrt(2)*sqrt(1-eps^2)
 <90.51,                                                   (5.9)
```

uniformly in both `eps ->0` and `N ->infinity`.

By contrast, the r27 raw-diagonal currency is proportional to `eps` and its estimate grows like `eps^(-1/4)`. The designated account04/B05 exact-slope theorem, applied to this **same actual family**, gives only

```
||p_Q||inf
 <51.6*(8*m_*)^(-1/3)
 <=?                                                        (5.10)
```

and using only the available upper bound `m_*<=2/N` shows that its guaranteed scale can deteriorate like

```
51.6*(N/16)^(1/3).                                         (5.11)
```

(For this trigonometric frame the exact classes are singletons, so `m_*=max_j u_j^2`, of order `1/N`.) Thus (5.9) pays a genuinely different diffuse/no-large-slope branch. Separately, whenever `mu>=1` and `m_*>=1/8`, the partner theorem closes that branch by the concrete inequality

```
boxed: ||p_Q||inf <51.6*8^(1/3)=103.2.                     (5.12)
```

This is the required equation-level partner application.

## 6. The first unpaid implication is now a punctured-null interpolation, not a vague residual loss

The exact determinant accounting identifies the survivor sharply. Put

```
theta=||B^(-1)q||,
chi=max(|d|z1^2,|a|z2^2).                                  (6.1)
```

Equation (2.7) proves that `theta` is the total normalized conditional-determinant resource. The square atlas pays every state with quantitative `chi`. At an **exact** zero of the diagonal corresponding to a nonzero shear component, the null-scalar theorem pays the same determinant with no diagonal factor at all.

Therefore the remaining analytic obstruction is the discontinuous-looking punctured regime:

```
0<|gamma|<<1,
|det H_cond| bounded below,
```

where the currently available square receiver costs `|gamma|^(-1/4)` even though the exactly-null receiver at `gamma=0` costs only `|det H_cond|^(-1/3)`.

This is not an algebraic loss: (2.6) shows that the determinant survives continuously. It is an **analytic receiver gap** caused by completing the small nonzero square before using the original product structure. The precise next B05 implication is therefore

### `QFORM-PUNCTURED-NULL-PRODUCTPROJECTION-COAREA-v1`

Let `Z` be a genuine independent scalar product projection and `(S,R)` an orthonormal two-dimensional projection of a disjoint product bank. For a symmetric invertible `3x3` quadratic matrix

```
G_gamma=[[gamma,h^T],[h,K]],
```

with arbitrary affine terms, prove a determinant-scale density estimate that stays finite as `gamma->0` whenever `det G_gamma` stays quantitatively nonzero, **using the product-projection provenance of `(S,R)` rather than only its joint density cap**. Even the restricted packet version sufficient here would close the artificial gap between (3.2) and (3.3).

A useful exact diagnostic is: if `theta>=tau>0` but `chi<=eta`, then whichever component of `z` has magnitude at least `tau/sqrt(2)` is attached to a raw diagonal of magnitude at most `2 eta/tau^2`. Thus every unhandled state with large determinant shear is genuinely a *near-null scalar with an active determinant*, exactly the regime the new lemma must interpolate. If instead `theta->0`, then `q=Bz` vanishes in the completed-pair scale and a different escaped-curvature resource must be found. These two alternatives are now algebraically disjoint.

The newest Claude small-diagonal hub report is consistent with this diagnosis: its tangent-parabola analysis also shows that a small nonzero diagonal must be kept exactly and that the correct proof has to exploit joint product geometry rather than perturbatively drop the square. Its stated hub hypotheses do not automatically imply the product-projection interpolation required here, so I do not claim it closes (6.1).

## 7. Status

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains open. Theorem 3.1 is an essential-density theorem only. The run does not use Gaussianity, moments, compact support, log-concavity, connected support, spectral-coordinate independence, a false arbitrary-joint coarea lemma, or a conditional-density supremum for `S|R`.

The substantive advance is twofold:

1. the residual curvature currency is identified exactly as `mu*m*||B^(-1)q||^2`, with its two physical conditional determinants as coordinates; and
2. this yields a new nonzero-diagonal density branch (3.2), a stronger one-null boundary theorem (3.3)-(3.4), and a target-valid diffuse family uniformly controlled by the new branch while both the raw-diagonal and exact-slope currencies can degenerate.

Next work should attack `QFORM-PUNCTURED-NULL-PRODUCTPROJECTION-COAREA-v1` directly; no further reparametrization of `q`, `sigma`, or `kappa` is needed before that analytic step.
