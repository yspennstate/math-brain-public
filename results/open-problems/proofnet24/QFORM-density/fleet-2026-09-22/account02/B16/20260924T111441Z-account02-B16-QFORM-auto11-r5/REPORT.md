SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-24T11:14:41Z.
attacking: the genuinely indefinite same-bank/nonzero-separated-pivot residue after partner account03/B16 r46, by paying the complementary definite-Schur branch and proving that joint-plus-marginal projection caps alone cannot pay the indefinite branch.

# account02/B16 — dependent projected pair with nonzero separated scalar pivot

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Projection-product interaction  
Pinned mathematical source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`  
Partner: latest compatible account03/B16 r46, `20260924T095233Z-account03-B16-QFORM-auto11-r4/REPORT.md`  
Status: `NEW SUPPORTING THEOREM + CAPS-INTERFACE OBSTRUCTION / FULL QFORM OPEN`  
Regularity: essential boundedness only in the new theorem; continuity is not asserted.

## 1. First unpaid implication

The first unpaid B16 implication is now

`QFORM-INDEFINITE-SHAREDBANK-NONZERO-PIVOT-PRODUCTTRANSDUCER-v1`:

> In a carrier consisting of a genuinely dependent two-dimensional projection from one original product bank and a scalar projection from a disjoint bank, the zero separated-scalar pivot was already paid by `QFORM-DEPENDENTPAIR-NULLSCALAR-DETERMINANT-v1`. This run pays every nonzero-pivot state whose Schur remainder on the shared projected plane is definite. The complementary invariant is `d det B<0`, equivalently an indefinite shared-plane Schur remainder. A construction below shows that a joint two-dimensional density cap, both true scalar marginal caps, and a disjoint scalar cap are still insufficient there. Any proof of this final interface must retain more original-product provenance through a Fresnel/source factorisation, a further source-separated innovation, or another already-paid exit.

This narrows partner r46's structural `QFORM-SHAREDBANK-NORMALFORM-OR-EXIT-COMPILER-v1`: the nonzero-pivot branch has a clean algebraic definite-Schur exit, and the residual obstruction is exactly the indefinite Schur sign, not projected dependence by itself.

## 2. New theorem: definite Schur remainder

Let `Z=(S,U)` have an arbitrary joint probability density `rho` satisfying

`||rho||_infinity <= M`,

and let `V` be independent of the **pair** `Z`, with scalar probability density bounded by `N`. Consider

`Q = Z^T C Z + 2 V ell^T Z + d V^2 + p^T Z + qV + c`,

where `C` is real symmetric `2x2`, `ell,p in R^2`, and `d!=0`. Put

`B = [[C,ell],[ell^T,d]]`,
`H = C - d^{-1} ell ell^T`.

### Theorem — `QFORM-DEPENDENTPAIR-NONZERO-PIVOT-DEFINITE-SCHUR-v1`

If `H` is definite, then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(pi) N M^(1/2) |d|^(-1/2)|det H|^(-1/4)
 = 2 sqrt(pi) N M^(1/2) |d det B|^(-1/4).`

No independence between `S` and `U` is assumed or inferred.

### Proof

Complete the scalar square:

`Q = d(V+d^{-1}ell^T Z+q/(2d))^2
   + Z^T H Z + (p-q d^{-1}ell)^T Z + c-q^2/(4d).`

Because `H` is definite, translate the projected pair to obtain

`Q = d(V+a(Z))^2 + R(Z) + c0`,
`R(Z)=(Z-z0)^T H(Z-z0)`.

The translation of `Z` does not change its joint density cap. Let `|H|` denote the positive definite matrix obtained by changing the sign if necessary. Under

`y=|H|^{1/2}(Z-z0)`,

the planar density is bounded by `M/sqrt(|det H|)` and `R=+|y|^2` or `R=-|y|^2`. Polar coarea therefore gives, on the appropriate half-line,

`||p_R||_infinity <= pi M / sqrt(|det H|).`                    (2.1)

Now condition on `Z`. Translation of `V` preserves its cap. For `w` on the sign-compatible half-line, the density of `d(V+a)^2` is bounded by

`N / sqrt(|d| |w|)`.                                          (2.2)

Hence, for almost every target `s`, if `h` is the density of `R`,

`p_Q(s)
 <= N |d|^(-1/2)
    integral_0^infinity y^(-1/2) h(s-epsilon y) dy`,           (2.3)

where `epsilon=sign(d)` after absorbing the sign convention of `R` into the target translation.

For every probability density `h<=K`, the one-sided half-potential satisfies

`sup_s integral_0^infinity y^(-1/2)h(s-y)dy <= 2 sqrt(K)`,     (2.4)

and similarly from the other side. Indeed the decreasing kernel is maximised under the constraints `0<=h<=K`, `integral h=1` by filling the interval adjacent to the singularity with height `K`, giving

`K integral_0^(1/K) y^(-1/2)dy = 2 sqrt(K)`.

Insert `K=pi M/sqrt(|det H|)` from (2.1) into (2.3). This proves

`||p_Q||_infinity
 <=2 sqrt(pi) N M^(1/2)|d|^(-1/2)|det H|^(-1/4).`

Finally `det B=d det H`, giving the determinant form. QED.

The theorem spends the dependent projected pair only through a legitimate **joint** density bound. It never conditions one projected coordinate on the other and never upgrades the pair to independent coordinates.

## 3. Actual product-projection corollary

Let `I,J` be disjoint original-coordinate banks. Put

`S=r^T X_I`, `U=u^T X_I`, `V=v^T X_J`,

and assume

`G=[[||r||^2,<r,u>],[<r,u>,||u||^2]]>0`,
`tau=||v||_2>0`.

The pinned completed two-dimensional product-projection theorem gives the source-valid joint bound

`M <= 2 det(G)^(-1/2)`,                                      (3.1)

while the scalar projection bound gives

`N <= sqrt(2)/tau`.                                          (3.2)

These are the only projection-density inputs. In particular, (3.1) is **not** interpreted as independence of `S,U`.

Substituting (3.1)-(3.2) into the theorem gives

`boxed:
 ||p_Q||_infinity
 <= 4 sqrt(pi) tau^(-1) det(G)^(-1/4)|d det B|^(-1/4).`       (3.3)

Suppose now the physical quadratic part has exact rank three and is

`A=TBT^T`,

where the columns of `T` are `r,u,v`. Because the pair bank and scalar bank are disjoint,

`T^T T=diag(G,tau^2)`,

so

`|pdet A|=|det B| det(G) tau^2`.                              (3.4)

Thus (3.3) becomes

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(pi) [ |d| tau^2 |pdet A| ]^(-1/4).`                (3.5)

On the owner's exact-rank-three target, `|pdet A|>=1`, hence

`||p_Q||_infinity <=4 sqrt(pi)(|d|tau^2)^(-1/4).`             (3.6)

Here `|d|tau^2` is exactly the magnitude of the physical quadratic coefficient in the unit separated direction `v/tau`. Therefore every quantitatively nonzero definite-Schur separated-pivot branch is paid.

If the full exact-rank-three carrier is itself definite and all three eigenvalues have modulus at least one, then the Rayleigh quotient in every unit direction has modulus at least one, so `|d|tau^2>=1`; in that structured definite target class,

`boxed: ||p_Q||_infinity <=4 sqrt(pi).`                       (3.7)

This is a full-line bound, not merely a one-sheet estimate.

## 4. Strict mixed-sign owner-target example

Take `(S,U)` to be an orthonormal two-dimensional projection of one original product bank and `V` a unit scalar projection of a disjoint original product bank. No independence between `S,U` is assumed. Let

`B_* = [[1,0,sqrt(3)],[0,4,0],[sqrt(3),0,-1]].`

Then `d=-1`,

`H=diag(1,4)-(-1)^(-1)(sqrt(3),0)^T(sqrt(3),0)=4 I_2`,

and

`det B_*=-16`,
`spec(B_*)={-2,2,4}`.

Thus this is a strict instance of the owner's three-large-eigenvalue target. The actual projection bounds are `M<=2`, `N<=sqrt(2)`, so the theorem gives

`boxed:
 ||p_(X^T A_* X)||_infinity <=2 sqrt(pi)=3.5449077018... .`    (4.1)

This directly applies the pinned completed two-dimensional product-projection result to a real nonlinear density inequality while keeping the projected pair dependent.

The pinned ruled one-sheet theorem also applies because the signature is `(+,+,-)`, giving its universal one-sheet estimate on the majority-sign side. The point of (4.1) is different: it is a global essential-density estimate across both sides.

## 5. Strong caps-interface obstruction in the complementary sign

The determinant identity

`det B=d det H`                                                  (5.1)

shows that for `d!=0`, the Schur remainder is indefinite exactly when

`d det B < 0`.                                                   (5.2)

This is the complementary algebraic branch. The following construction proves that retaining **more** than the joint planar cap is still insufficient there.

Fix `0<delta<=1/8` and put

`R_delta=exp(2/delta)`,
`D_delta={(x,y): 1<=x<=R_delta, 0<=y<=delta/x}`.

The area of `D_delta` is

`delta log R_delta=2`.

Let `(X,Y)` have density `(1/2)1_{D_delta}`, and define

`S=(X+Y)/2`,
`U=(X-Y)/2`.

The Jacobian magnitude of `(x,y)->(s,u)` is `1/2`; therefore `(S,U)` is uniform with **joint density exactly one** on its image:

`||p_(S,U)||_infinity=1`.                                      (5.3)

Moreover both scalar marginals are uniformly bounded by one.

For fixed `s`, write `x=s+u`, so `du=dx`. Since `s>=1/2` and `delta<=1/8`, the admissible branch has

`x in [s+sqrt(s^2-delta), 2s]`

up to intersection with `[1,R_delta]`. Hence

`p_S(s)
 <=s-sqrt(s^2-delta)
 =delta/(s+sqrt(s^2-delta))
 <=2delta<1.`                                                  (5.4)

For fixed `u`, `x=s+u`, so `ds=dx`, and `u>=(1-delta)/2`. The admissible fibre has length at most

`sqrt(u^2+delta)-u
 =delta/(sqrt(u^2+delta)+u)
 <=delta/(1-delta)<1.`                                         (5.5)

Thus

`||p_S||_infinity<=1`, `||p_U||_infinity<=1`.                  (5.6)

Yet

`W=S^2-U^2=(S+U)(S-U)=XY`

is exactly uniform on `[0,delta]`. Indeed, for `0<=w<=delta`,

`P(W<=w)
 =(1/2) integral_1^(R_delta) (w/x) dx
 =(w/2) log R_delta
 =w/delta.`                                                    (5.7)

Let `V` now be independent uniform on `[0,1]`; its density cap is also one. For the carrier-level strict-target form

`Q_delta=S^2-U^2+V^2`,                                        (5.8)

whose coefficient matrix in `(S,U,V)` is `diag(1,-1,1)`, the density at `q=delta` is

`p_(Q_delta)(delta)
 =(1/delta) integral_0^delta [2 sqrt(delta-w)]^(-1) dw
 =delta^(-1/2) -> infinity.`                                  (5.9)

Therefore there is **no** universal bound for the indefinite nonzero-pivot branch derivable from only

- a joint two-dimensional density cap for `(S,U)`,
- bounded scalar marginals for both `S` and `U`, and
- a bounded density for an independent scalar `V`.

This is **not a counterexample to QFORM**: the constructed dependent pair `(S,U)` has not been shown to arise as a two-dimensional linear projection of independent cap-one physical coordinates. It is a rigorous counterexample to the projection-caps-only interface. The original product provenance must do additional work in branch (5.2).

This strengthens the previous B16 caps-only obstruction, which did not record bounded scalar marginals for both projected coordinates.

## 6. Relation to partner account03/B16 r46

Partner r46 proved a source-valid square-hyperbolic theorem for

`a(S+d)^2+2b(T+cS+alpha)(V+beta)+r`,

where `(S,T)` is a genuinely dependent two-dimensional product projection, and crucially used both the joint pair cap and a true scalar marginal cap before nonlinear integration. It left `QFORM-SHAREDBANK-NORMALFORM-OR-EXIT-COMPILER-v1` as the structural debt.

The present run identifies a complementary exact carrier split. For a general dependent-pair plus separated-scalar carrier `B`:

1. `d=0`: the previous B16 null-scalar determinant theorem pays the arbitrary pair block.
2. `d!=0` and `d det B>0`: the Schur remainder is definite and Theorem 2 pays the branch quantitatively; in the full definite target subcase it is universal by (3.7).
3. `d!=0` and `d det B<0`: the Schur remainder is indefinite, and Section 5 proves that joint-plus-marginal projection caps alone cannot be a complete compiler.

Thus partner r46's remaining structural compiler should spend its effort precisely on source-preserving reduction or extra original-product oscillation in case 3, rather than trying to improve a conditional projection cap.

As a concrete application of r46 itself, take orthonormal dependent `(S,T)` from one source bank, unit `V` from a disjoint bank, and

`Q_partner=4S^2+4(T+S)V`.

Its carrier matrix is

`[[4,0,2],[0,0,2],[2,2,0]]`,

with characteristic polynomial `lambda^3-4lambda^2-8lambda+16`, determinant `-16`; since the polynomial changes sign on `(-infinity,-1)`, `(1,2)`, and `(4,6)`, all three real eigenvalues have modulus greater than one. Partner r46 therefore applies to a genuine owner-target inequality and gives, from its explicit product-projection constants,

`||p_(Q_partner)||_infinity < 9.30.`                           (6.1)

The earlier zero-pivot determinant theorem happens to give a sharper constant on this particular example; (6.1) is included to verify the partner theorem at a strict target point, not as the best available bound.

## 7. Exact frontier

The full unrestricted QFORM theorem remains OPEN / NOT PROVED / NOT DISPROVED. Continuity remains separate.

The first unpaid implication is `QFORM-INDEFINITE-SHAREDBANK-NONZERO-PIVOT-PRODUCTTRANSDUCER-v1`: in the exact-rank-three/small-pivot shared-bank collar, when the separated scalar pivot is nonzero and the completed same-bank Schur form is indefinite (`d det B<0`), exploit the fact that `(S,U)` is an actual two-dimensional linear image of an original product law, not merely a planar density with bounded marginals. Candidate admissible resources are pre-absolute-value Fresnel factorisation in original coordinates, another source-separated innovation, or a reduction to partner r46's square-hyperbolic packet. Any step that infers independence of the projected coordinates or a uniform conditional cap is invalid.
