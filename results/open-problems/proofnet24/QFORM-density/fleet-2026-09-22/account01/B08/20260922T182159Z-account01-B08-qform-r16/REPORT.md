# account01/B08 — diffuse rank-two off-diagonal bank theorem

Run: `20260922T182159Z-account01-B08-qform-r16`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control at start: revision `2026-09-22.10`  
Outcome: `PROVED_SUPPORTING TARGET-LEVEL BRANCH / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and conditional end-to-end map

The full target is unchanged: for every real symmetric `A` with at least three eigenvalues of modulus at least one and every product law `X=(X_i)` whose independent coordinate densities satisfy `0<=f_i<=1`, prove one universal bound on the essential density of `Q=X^TAX`, or give a valid counterexample. Continuity is tracked separately.

The present B08 route is the diffuse/localized decomposition. A completed designated-partner theorem already pays a perturbatively diffuse branch: account02/B08 `QFORM-DIFFUSE-APPROX-BLOCK-STABILITY-v1`, source

`yspennstate/math-open-problems@c1c6ffe8c742cbba7611b5a3f1d73cf71019f47b`.

Concretely, write `A=R Lambda R^T+C` with `R^TR=I_3`, `s_min(Lambda)>=1`, take no preliminary conditioning, and split `C=C0+E` with singleton physical blocks `C0=diag(C)`. Then `eta=0`, `W=R`, and `mu=max_i ||r_i||^2`. Thus the partner's clean corollary applies literally:

`mu<=1/48` and `||E||op<=1/40  =>  ||p_Q||infinity<51`,

with a continuous `C_0` density. This is an actual use of the designated partner theorem, not a nominal citation.

The previous account01/B08 run treated the complementary large-defect/stable-rank branch and reduced an unresolved part to low stable rank or a fixed-scale localized cross row. The new theorem below attacks one exact low-rank geometry by a different mechanism: classify every zero-diagonal rank-two symmetric matrix, split its two physical banks, and spend the target's third singular direction as a genuine scalar pivot.

## 2. Peer inputs used

### 2.1 Low-offdiagonal target branch

Account03/B19 proved `QFORM-HALF-OFFDIAGONAL-BARRIER-v1`, source handoff

`yspennstate/math-research-brain:scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account03/B19/20260922T170047Z-account03-B19-QFORM-r15.md`,

canonical mathematics `yspennstate/math-open-problems@539d1d9953c616bf0e1ab2dafeef55102f89c2b9`.

If `H=A-diag(A)` and `s_2(H)<=t<1/2`, then

`||p_Q||infinity <= max(50(1-t)^(-3/4), pi/sqrt(1-2t))`.      (2.1)

No continuity conclusion is asserted in that branch.

### 2.2 Physical pivot plus two ridge directions

Account03/B08 proved `QFORM-PIVOT-PLUS-TWO-RIDGE-DIRECTIONS-v1`, canonical mathematics

`yspennstate/math-open-problems@f0a31a05a227ca671ffb22f6d7ed62954ce48c73`.

For a nonzero original-coordinate scalar pivot `a`, let `S` be its exact Schur residual. If an original-coordinate cross block `B` of `S` has two singular values at least `sigma>0`, and at `gamma=sigma/sqrt(6)` its ridge matrix

`K_gamma=B B^T (gamma^2 I+B B^T)^(-1)`

satisfies `max_i (K_gamma)_ii<=1/2`, then

`||p_Q||infinity < 14.34 / sqrt(|a| sigma)`.                  (2.2)

This gives absolute continuity and essential boundedness; continuity is not claimed by this `L^p`-plus-square argument.

## 3. Exact classification of a zero-diagonal rank-two matrix

Let

`H=A-diag(A)`

and suppose `rank(H)=2`. Since `H` is symmetric and has zero diagonal, `tr(H)=0`. Its two nonzero eigenvalues are therefore `+tau` and `-tau` for some `tau>0`. Write

`H=tau(uu^T-vv^T)`,

where `u,v` are orthonormal. The zero diagonal gives, coordinate by coordinate,

`u_i^2=v_i^2`.                                                  (3.1)

For every nonzero coordinate choose `epsilon_i in {+1,-1}` with `v_i=epsilon_i u_i`. Orthogonality `u dot v=0` yields

`sum_{epsilon_i=+1} u_i^2 = sum_{epsilon_i=-1} u_i^2 = 1/2`.  (3.2)

Call the two index sets `P,N`. Then

`H_ij=0` if `i,j` lie in the same bank,

and

`H_ij=2 tau u_i u_j` if `i,j` lie in opposite banks.          (3.3)

Thus every real symmetric zero-diagonal rank-two matrix is exactly a weighted complete bipartite matrix. This identity is the core new structural input.

Let `P_H` denote the orthogonal projection onto `range(H)=span{u,v}`. From (3.1),

`(P_H)_ii=u_i^2+v_i^2=2u_i^2`.                                (3.4)

Hence the diffuse hypothesis

`max_i (P_H)_ii <= 1/6`                                       (3.5)

is exactly

`max_i u_i^2 <= rho:=1/12`.                                   (3.6)

## 4. The third singular direction forces a physical scalar pivot

Under the full owner target, `s_3(A)>=1`. Since `rank(H)<=2` and `A=diag(A)+H`, the rank perturbation inequality gives

`s_3(A) <= s_1(diag(A)) = max_i |A_ii|`.                       (4.1)

Therefore some original coordinate `i` satisfies

`|a|:=|A_ii|>=1`.                                               (4.2)

If `u_i=0`, its row in `H` vanishes and the argument below simplifies; assign that zero-weight coordinate to either bank. Otherwise swap the bank names if needed and take `i in P`. Put

`w=u_i^2<=rho`,
`p=u|_(P\{i})`,
`n=u|_N`.

Then

`||p||^2=1/2-w >=5/12`,  `||n||^2=1/2`.                       (4.3)

The pivot row couples only to the `N` bank. Completing the scalar square gives the exact Schur residual

`S=D_- + 2tau(p n^T+n p^T) - beta n n^T`,                    (4.4)

where `D_-` is diagonal and

`beta=4 tau^2 w/a`,  so  `|beta|<=tau^2/3`.                   (4.5)

No rotation of the input law has been made.

## 5. A balanced physical-bank split

We use the elementary subset-half lemma: if nonnegative atom weights have total mass `M` and each atom is at most `rho`, there is a subset of mass `x` with

`|x-M/2|<=rho/2`.                                               (5.1)

Indeed, take a partial sum immediately before and after crossing `M/2`; the two endpoints are separated by at most `rho`, so one is within `rho/2` of the midpoint.

Apply (5.1) separately to the remaining `P` bank and to `N`, using weights `u_j^2`. This produces a partition of the residual original coordinates `I|J` such that, writing

`x=||p_I||^2`, `X=||p_J||^2`, `y=||n_I||^2`, `Y=||n_J||^2`,

we have

`x,X >= 1/6`,                                                   (5.2)

`y,Y >= 5/24`.                                                  (5.3)

Coordinates with `u_j=0` may be assigned arbitrarily.

The diagonal term in (4.4) contributes nothing to the cross block `B=S[I,J]`. In the orthonormal row basis

`p_I/sqrt(x), n_I/sqrt(y)`

and column basis

`p_J/sqrt(X), n_J/sqrt(Y)`,

the only nonzero singular data of `B` are those of

`M = [[0,                    2tau sqrt(xY)],
      [2tau sqrt(yX),       -beta sqrt(yY)]].`                 (5.4)

Therefore

`|det M|=4tau^2 sqrt(xXyY) >= (5/36)tau^2`.                   (5.5)

Also

`||M||_F^2
 =4tau^2(xY+yX)+beta^2 yY
 <=tau^2+tau^4/144`,                                           (5.6)

because `xY+yX <= (x+X)(y+Y)<=1/4`, `yY<=1/16`, and (4.5) holds. Thus the second singular value obeys

`s_2(B)=s_2(M)
 >= |det M|/||M||_F
 >= [5tau/36]/sqrt(1+tau^2/144).`                              (5.7)

The right-hand side is increasing for `tau>0`.

## 6. Ridge leverage is automatically at most one half

The row range of `B` is contained in `span{p_I,n_I}`. These vectors have disjoint physical supports. Consequently the diagonal of the orthogonal projection onto this span is at most

`rho/x <= (1/12)/(1/6)=1/2` on the `P` bank,                   (6.1)

and at most

`rho/y <= (1/12)/(5/24)=2/5` on the `N` bank.                 (6.2)

For every `gamma>0`,

`0 <= K_gamma <= P_range(B)`

as positive semidefinite matrices, because on each nonzero singular direction its eigenvalue is `s^2/(gamma^2+s^2)<=1`. Hence

`max_i (K_gamma)_ii <= 1/2`.                                   (6.3)

This is exactly the ridge-leverage hypothesis in the completed account03/B08 theorem.

## 7. New target-level branch theorem

### Theorem — `QFORM-DIFFUSE-RANK2-OFFDIAGONAL-BANK-v1`

Assume the exact full QFORM hypotheses. Put `H=A-diag(A)`. If

`rank(H)<=2`

and, in the nonzero rank-two case,

`max_i (P_range(H))_ii <=1/6`,

then `Q=X^TAX` has an essentially bounded density satisfying

`boxed(||p_Q||infinity<68).`                                   (7.1)

No moment, support, sign, or diagonal-basis assumption on the inputs is added.

### Proof

If `rank(H)<2`, zero diagonal forces `H=0`, and the diagonal theorem already applies. Assume `rank(H)=2` and use the classification above.

**Low offdiagonal scale.** If `tau=s_2(H)<=1/3`, apply (2.1) with `t=1/3`:

`||p_Q||infinity
 <= max(50(3/2)^(3/4), pi sqrt(3))
 <68`.                                                         (7.2)

**High offdiagonal scale.** If `tau>=1/3`, (5.7) gives

`s_2(B) >= sigma_0:=5/(3 sqrt(1297)) >0`.                      (7.3)

Both nonzero singular values of `B` are at least `sigma_0`, while (6.3) gives the required ridge leverage cap. The physical pivot from (4.2) has `|a|>=1`. Apply (2.2):

`||p_Q||infinity
 <14.34/sqrt(sigma_0)
 =14.34 sqrt(3 sqrt(1297)/5)
 <67`.                                                         (7.4)

Combining (7.2)-(7.4) proves (7.1). QED.

The theorem covers all signs of the spectrum and arbitrary extra diagonal entries. The extra target eigenvalues are not assumed to align with the two-dimensional range of `H`; only `s_3(A)>=1` is used to force the physical pivot (4.2).

## 8. Why this is a real diffuse/localized bridge

The bank classification avoids selecting a reciprocal tiny `3x3` principal minor. Even if every fixed local principal block is poor, the entire diffuse rank-two off-diagonal geometry is paid by two large physical banks. The third target singular direction appears only as the scalar pivot guaranteed by rank-two perturbation.

This directly complements the designated account02/B08 small-defect diffuse theorem:

* selected three-frame diffuse + small arbitrary dense complementary defect: continuous density `<51` by the partner theorem;
* exact diffuse rank-two full off-diagonal geometry: essential density `<68` by the new bank theorem.

The two mechanisms are genuinely different and preserve original-coordinate product provenance.

## 9. Scope, continuity, and next unpaid implication

This does **not** prove the full conjecture. It proves a target-level branch under the exact structural hypothesis `rank(A-diag A)<=2` plus a diffuse range projection. Continuity is **not proved** here; only absolute continuity and an essential `L^infinity` bound are obtained, because both the low-offdiagonal peer branch and the pivot-plus-ridge `L^p` square upgrade are stated at essential-density level.

The next B08 implication is

`QFORM-DIFFUSE-APPROX-RANK2-BANK-STABILITY-v1`:

extend the bank argument to a high-offdiagonal matrix whose zero-diagonal part is close, in a product-preserving quantitative sense, to a diffuse rank-two bipartite core, without paying the ambient dimension through the tail diagonal or through a tiny local minor. A successful version should splice into the current `s_2(A-diag A)>499/1000` overlap branch and the previous low-stable-rank remainder reduction. Failure should identify a direct ridge/grouped-coordinate resource.

## 10. Exact arithmetic check

The companion `VERIFY.py` checks the rational bank masses, leverage caps, the exact threshold value

`sigma_0=5/(3sqrt(1297))`,

and the numerical bounds `<67` and `<68`. Its terminal line is

`QFORM_B08_RANK2_BANK_CHECK_PASS`.
