SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B07, 2026-09-24T01:36:22Z.
attacking: the account03/B07 r42 near-rank-two common crossing plus low-diagonal/low-internal cloud receiver — close the bounded-support two-direction spectral subproblem, then test whether the surviving rank-two tube is quantitatively balanced before any bounded-core inference.

# account02/B07 — bounded-support E2 balance and an unbalanced rank-two/cloud obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / complementary constructions and source-valid counterexamples  
Run: `20260924T013622Z-account02-B07-qform-auto11`  
Status: **NEW BOUNDED-SUPPORT E2 SPECTRAL COMPILER / EXACT R42 UNBALANCED-R2 TARGET STRESS / PINNED E5 FRESNEL RECEIVER APPLIED / FULL QFORM OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

No moment, bounded-support, log-concavity, iid, diagonal-basis, or post-rotation independence hypothesis is added to the owner target. The bounded-support statement below is a deterministic conditional compiler only; the exact stress then proves that its support hypothesis cannot be deleted. All coordinates are ORIGINAL physical coordinates.

## 1. Fresh incoming packet and first unpaid implication

The current owner control remains revision `2026-09-22.15`, full QFORM only. The full theorem and full-target continuity remain OPEN. Live corrections were reread: no universally good individual coordinate minor, no post-rotation independence, no arbitrary-joint coarea bound, no pointwise law-uniform quadratic stationary phase, and no deletion of a small nonzero quadratic tail is used.

The latest completed designated partner actually consumed is account03/B07 r42:

`yspennstate/math-open-problems@e91150711e87a3e9040e3b93333e55ab574d7c01`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260924T004021Z-account03-B07-qform-r42/REPORT.md`.

It works with disjoint physical banks `H,I,J`, common crossing `K=A[I,J]`, anchor rows `m_h=A[h,J]`, and projected two-volume

`Z_h=e2(K(I-P_{m_h})K^T)`.

Its new internal-cut theorem pays the branch

`sum_{h<k} A_hk^2(Z_h+Z_k) >= 1/12500`

by one literal physical `Z3` crossing. If that exit fails, there is a surviving low-diagonal bank `G0` on which

`boxed:
 sum_{h in G0} Z_h > 0.32768,
 |A_hh|<1/64,
 ||A[h,J]||_2<1/64,
 ||A[h,H_lo\{h}]||_2<1/64.
}`                                                              (1.1)

The compatible previous account02/B07 router, source

`yspennstate/math-open-problems@81d6956476fa400f61d266effb4123a42fe3185c`,

also starts from the genuine one-overlap packet

`W_lo=sum_h A_hh^2 Z_h>1/6250`                                  (1.2)

and proves that, unless the actual physical third volume `E3=e3(KK^T)` is already paid, either the common crossing is in the quantitative tube

`E2:=e2(KK^T)>=2^(-12),
 ||K-K_2||_F<sqrt(3)2^(-9)=0.003382911734...`                    (1.3)

or there is a large aggregate low diagonal cloud. Here `K_2` is the best rank-two SVD truncation and the tail in (1.3) is explicitly retained.

The first unpaid implication is therefore not merely “find a rank-two carrier”. One must determine whether (1.3) supplies TWO quantitative spectral directions or can degenerate to one huge direction plus one vanishing direction while the third owner-target eigenvalue lives elsewhere. The latter happens exactly.

## 2. Bounded-dimensional E2 spectral subproblem — solved without selecting a minor

The following deterministic estimate is the safe way to turn aggregate two-volume into a second singular direction when the physical support is genuinely bounded.

### Theorem 2.1 — `QFORM-E2-BOUNDED-SUPPORT-BALANCE-v1`

Let `K` be a real `p x q` matrix of rank `r>=2`, with singular values `s_1>=s_2>=...>=s_r>0`, and put

`E2(K)=e2(KK^T)=sum_{i<j}s_i^2s_j^2`.

Then

`boxed:
 E2(K) <= (r-1)s_2(K)^2 ||K||_F^2.
}`                                                               (2.1)

Consequently, if every physical entry obeys `|K_ij|<=L`,

`boxed:
 s_2(K)
 >= [E2(K)/((r-1)pqL^2)]^(1/2).
}`                                                               (2.2)

In particular, if `p,q<=m`,

`boxed:
 s_2(K)>=sqrt(E2(K))/(m L sqrt(m-1)).
}`                                                               (2.3)

No individual `2x2` minor is chosen.

### Proof

Write `x_j=s_j^2` and `T=sum_j x_j=||K||_F^2`. Ordering the pair sum by its larger index,

`E2(K)=sum_{j=2}^r x_j sum_{i<j}x_i`.

For every `j>=2`, `x_j<=x_2` and `sum_{i<j}x_i<=T`; hence

`E2(K)<=sum_{j=2}^r x_2 T=(r-1)x_2T`,

which is (2.1). Since `T<=pqL^2`, (2.2) follows, and `r<=m`, `pq<=m^2` gives (2.3). QED.

### Integration into a physical coordinate core

For `C=I0 union J0` containing the row and column support of such a block, `K=P_{I0} A[C,C] P_{J0}`. Orthogonal projections are contractions for every singular value, so

`s_2(A[C,C])>=s_2(K)`.                                            (2.4)

Thus aggregate `E2`, together with bounded ORIGINAL-coordinate support and a coefficient bound, really does give two actual physical spectral directions, with no reciprocal-minor selection. The third-direction bounded-core step is separately supplied by the previous B07 principal-compound theorem: if a positive fraction of the one-overlap packet (1.2) is supported on one bounded physical set, its entire squared-minor mass sits inside `e3(A[C,C]^2)` and yields a quantitative `s_3(A[C,C])` after the same coefficient/Frobenius normalization.

So the bounded-dimensional spectral subproblem is closed at aggregate-compound level. What remains is genuinely the support-diffuse case.

## 3. Exact full-target stress: the r42 rank-two tube need not be balanced

The support hypothesis in Section 2 cannot be removed, even after imposing the full owner target, the r42 low-diagonal/low-internal conditions, the complete one-overlap packet, and an EXACT rank-two common crossing.

Fix an integer `n>=9`. Put

`N=P=n^4`, `M=2n^4`.                                                   (3.1)

On the `M`-coordinate banks `I,J`, choose flat orthonormal pairs `u_1,u_2` and `v_1,v_2`; for example the constant vector and the half-plus/half-minus vector, all coordinates having magnitude `M^(-1/2)`. Define

`K_n = n u_1 v_1^T + n^(-1) u_2 v_2^T`.                            (3.2)

Then its singular values are exactly

`s_1(K_n)=n`, `s_2(K_n)=n^(-1)`,                                  (3.3)

so

`boxed:
 E2(K_n)=1,
 E3(K_n)=0,
 ||K_n-(K_n)_2||_F=0,
 s_2(K_n)=n^(-1)->0.
}`                                                                  (3.4)

Every physical entry of `K_n` satisfies

`|(K_n)_{ij}| <= (n+n^(-1))/M`.                                   (3.5)

Add a low-diagonal anchor bank `H` of size `N`, and a separate bank `O` of size `P`. Let `w` be the flat unit vector on `O`, and set

`A_n = diag-block(
 n^(-2) I_H,
 [[0,K_n],[K_n^T,0]] on I union J,
 w w^T on O ).`                                                    (3.6)

More explicitly, in the order `H,I,J,O`,

`A_n=
 [ n^(-2)I_H   0       0       0
   0            0       K_n     0
   0            K_n^T   0       0
   0            0       0       ww^T ].`                           (3.7)

### 3.1 It lies literally in the r42 survivor

For every anchor `h in H`, with the r41/r42 notation,

`a_h=A_hh=n^(-2)`, `m_h=A[h,J]=0`, `u_h=A[I,h]=0`,
`A[h,H\{h}]=0`.                                                     (3.8)

Hence `P_{m_h}=0` and

`Z_h=e2(K_nK_n^T)=1`.                                              (3.9)

Therefore

`boxed:
 sum_h a_h^2 Z_h = N n^(-4)=1,
 sum_{h in G0}Z_h=N,
 E_H=sum_{h<k}A_hk^2(Z_h+Z_k)=0.
}`                                                                 (3.10)

For `n>=9`, `|a_h|<1/64`; the two star norms in (1.1) vanish. Thus the family survives r42's new internal-edge `Z3` exit maximally. It also lies exactly in the previous near-rank-two alternative (1.3): `E2=1`, `E3=0`, and the Frobenius tail is zero.

The important new fact is (3.4): **fixed macroscopic aggregate `E2` plus an exact rank-two carrier gives no lower bound whatsoever on its second singular value when physical support is allowed to grow.** The carrier may be arbitrarily ill-conditioned.

### 3.2 It is in the full owner target

The bipartite block in (3.6) has nonzero eigenvalues

`+n, -n, +n^(-1), -n^(-1)`.                                      (3.11)

The `O` block contributes the eigenvalue `+1`; the `H` block contributes `n^(-2)` with multiplicity `N`. Hence

`spec(A_n) contains {+n,-n,+1,+n^(-1),-n^(-1)}`.                  (3.12)

In particular, `A_n` has at least three eigenvalues of modulus at least one: `+n,-n,+1`. No extra assumption is being smuggled into the stress.

Moreover every matrix coefficient tends to zero:

`max_{ij}|(A_n)_{ij}|
 <= max(n^(-2),(n+n^(-1))/(2n^4),n^(-4)) ->0`.                    (3.13)

So the obstruction is not a hidden large physical pivot.

## 4. No uniformly spectral bounded physical core exists in the stress

Fix any integer cardinality bound `L0`. Let `C` be any physical principal set with `|C|<=L0`. Write `C_I=C intersect I`, etc. The matrix `A_n[C,C]` is block diagonal across `H`, `I union J`, and `O`. Its three block norms satisfy

`||A_n[C_H,C_H]||_op <= n^(-2)`,                                  (4.1)

`||A_n[C_{I union J},C_{I union J}]||_op
 =||K_n[C_I,C_J]||_op
 <=||K_n[C_I,C_J]||_F
 <=sqrt(|C_I||C_J|) (n+n^(-1))/M
 <= L0 (n+n^(-1))/(2M),`                                         (4.2)

and

`||A_n[C_O,C_O]||_op=||w_{C_O}||_2^2=|C_O|/P<=L0/P`.             (4.3)

Using `M=2n^4`, `P=n^4`,

`boxed:
 s_3(A_n[C,C])
 <=||A_n[C,C]||_op
 <=max(n^(-2), L0(n+n^(-1))/(4n^4), L0/n^4)
 ->0,
}`                                                                 (4.4)

uniformly over every `|C|<=L0`.

This proves the new obstruction

### `QFORM-R42-R2-BALANCE-AND-BOUNDED-CORE-FALSE-v1`

Even inside the exact owner target and the literal r42 low-diagonal/low-internal survivor, a fixed one-overlap packet and an exact rank-two common crossing do **not** imply either

1. a dimension-free lower bound on `s_2(K)`, or
2. any uniformly spectral bounded-cardinality ORIGINAL-coordinate principal core.

This is an intermediate-mechanism counterexample, not a counterexample to QFORM.

It sharpens the previous equal-singular-value diffuse-core stress: here the common crossing has condition number `n^2 -> infinity`, so any continuation that calls (1.3) “two usable directions” without a separate balance/support argument is invalid.

## 5. Mandatory pinned-e5 application: the exact stress is uniformly paid when the full low-rank tail is retained

The required pinned source was reread at exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,
`FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Its completed Fresnel--Brascamp--Lieb Theorem F states, in its general rank-`r` form, that if

`A = D + R Lambda R^T`

with `D` diagonal, `R` an orthonormal rank-`r` frame whose physical coordinate leverages are all at most `1/2`, then for arbitrary independent cap-one laws and arbitrary linear terms,

`|phi_Q(t)| <= (4pi)^(r/2)|t|^(-r/2) prod_{k=1}^r |lambda_k|^(-1/2).`  (5.1)

Apply it to (3.6) with the COMPLETE non-diagonal spectral part, not with a truncated rank-three component. The five orthonormal eigenvectors are

`(u_1,+v_1)/sqrt(2)`, `(u_1,-v_1)/sqrt(2)`,
`(u_2,+v_2)/sqrt(2)`, `(u_2,-v_2)/sqrt(2)`, and `w`,                (5.2)

with eigenvalues

`n,-n,n^(-1),-n^(-1),1`.                                         (5.3)

The coordinate leverage is exactly

`2/M=1/n^4` on every `I` or `J` coordinate,
`1/P=1/n^4` on every `O` coordinate,
`0` on every `H` coordinate,                                      (5.4)

so the `1/2` gate is satisfied. The cloud `n^(-2)I_H` is retained as the allowed diagonal twist. Crucially,

`prod |lambda_k|=n*n*n^(-1)*n^(-1)*1=1`.                         (5.5)

Therefore

`|phi_Q(t)| <= (4pi)^(5/2)|t|^(-5/2).`                            (5.6)

Together with `|phi_Q|<=1`, Fourier inversion gives an exact universal constant. Put `B=(4pi)^(5/2)` and `t_0=B^(2/5)=4pi`. Then

`integral_R min(1,B|t|^(-5/2))dt
 =2[4pi + B integral_{4pi}^infinity t^(-5/2)dt]
 =2[4pi +(2/3)(4pi)]
 =40pi/3.`                                                        (5.7)

Hence

`boxed:
 ||p_{X^TA_nX}||_infinity <= (2pi)^(-1)(40pi/3)=20/3.
}`                                                                 (5.8)

Because the characteristic function is integrable, this particular family also has a continuous density.

This is a real application of a completed pinned-e5 result to the actual obstruction. It also shows exactly why deleting the tiny `+/-n^(-1)` mode would be the wrong move: Theorem F can retain it at no cost here because the product of all five nonzero low-rank eigenvalue magnitudes stays equal to one.

## 6. Consequence for coordinate-core extraction

The bounded-dimensional part is now clean:

* Aggregate `E2` on a bounded physical support, with a coefficient/Frobenius normalization, gives a quantitative second singular direction by (2.1)-(2.3), before any minor inversion.
* Concentrated one-overlap third-compound mass gives the quantitative third physical singular direction by the previous principal-compound theorem.
* Without bounded support/concentration, neither conclusion can be promoted to a universal bounded physical core; (3.6) is an exact target-class obstruction even with r42's stronger low-internal-star condition.

Thus the remaining r42 rank-two/cloud route is analytically, not spectrally, diffuse. A correct receiver must survive the scale separation

`s_1(K)->infinity`, `s_2(K)->0`, `s_1(K)s_2(K)=1`,                 (6.1)

while keeping the actual nonzero tail, arbitrary same-bank curvature, outside couplings, and the independent third target direction. It may not replace (1.3) by a balanced rank-two hypothesis and may not infer one bounded core.

### Sharpened first unpaid implication

`QFORM-R42-UNBALANCED-R2-PLUS-DIFFUSE-THIRD-RECEIVER-v1`:

Starting from the genuine survivor (1.1)-(1.3), prove a universal density estimate or a further exhaustive physical decomposition that remains valid when the rank-two approximation has arbitrarily bad condition number and the third large eigenvalue is carried by a separate diffuse physical direction. The exact family (3.6) is a mandatory regression. The pinned Theorem F pays the special diagonal-plus-low-rank/leverage case, but the actual survivor still permits arbitrary `I x I`, `J x J`, `H x I`, outside curvature/couplings and extra spectrum; those may not be discarded as small random perturbations.

Full QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains OPEN. This run proves one positive bounded-support spectral compiler and one exact source-valid obstruction to a stronger diffuse-core/balanced-carrier inference; it does not claim the universal theorem.
