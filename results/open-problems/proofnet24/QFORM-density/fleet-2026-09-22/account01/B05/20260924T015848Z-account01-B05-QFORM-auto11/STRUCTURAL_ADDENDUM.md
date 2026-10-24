# Structural addendum — residual-heavy rows split into transverse pair-star mass or at most three longitudinal spikes

This addendum strengthens the exact Witt compiler in `REPORT.md`. It is purely algebraic and does not claim a new full density receiver.

Keep the notation of Theorem 2.1 in `REPORT.md`:

`r_i=(sqrt(c),0,0)`, residual row `r_j=(x_j,y_j,z_j)`, `tau^2=1-c`, `Delta_3=|det M|`, and

`S_i=c Delta_3`.

The normalized residual frame has row leverage

`ell'_j = x_j^2/tau^2 + y_j^2+z_j^2`.                                (A.1)

Put

`q_j=y_j^2+z_j^2`.                                                     (A.2)

## A.1 Exact pair-anchored determinant-star identity

For every residual physical coordinate `j`, define the complete principal-triple mass through the physical pair `{i,j}` by

`T_ij = sum_{k notin {i,j}} |det A[{i,j,k}]|`.                       (A.3)

From the literal triple formula in `REPORT.md`,

`|det A[{i,j,k}]|
 = c Delta_3 (y_j z_k-y_k z_j)^2`.                                   (A.4)

Summing in `k` and using `||y||=||z||=1`, `<y,z>=0`, gives

`sum_k (y_j z_k-y_k z_j)^2
 = y_j^2 ||z||^2+z_j^2||y||^2-2y_jz_j<y,z>
 = y_j^2+z_j^2=q_j`.                                                  (A.5)

Therefore

`boxed{ T_ij = c Delta_3 q_j = S_i q_j. }`                           (A.6)

Equivalently, the physical pair of spectral rows `{r_i,r_j}` has Euclidean two-volume squared

`det Gram(r_i,r_j)=c q_j`,                                           (A.7)

and the pair-anchored determinant star is exactly `Delta_3` times this two-volume.

As a consistency check,

`sum_{j != i} T_ij = S_i sum_j q_j = 2S_i`,                          (A.8)

because `sum_j q_j=||y||^2+||z||^2=2`; each triple through `i` is counted once for each of its two residual coordinates.

## A.2 Residual-heavy-row dichotomy

Suppose a normalized residual row is heavy:

`ell'_j>1/2`.                                                         (A.9)

Then exactly one of the following useful alternatives holds.

### Transverse-heavy alternative

If

`q_j>=1/4`,                                                           (A.10)

then the exact pair-anchored determinant currency satisfies

`boxed{ T_ij >= S_i/4. }`                                            (A.11)

At target normalization in the high-leverage chamber `c>=1/2`, `Delta_3>=1`, hence `S_i>=1/2` and

`boxed{ T_ij>=1/8. }`                                                (A.12)

This is an aggregate statement over **all** physical triples extending one fixed physical pair; it does not select or reciprocate a tiny individual triple.

### Longitudinal-spike alternative

If

`q_j<1/4`,                                                           (A.13)

then (A.1) and (A.9) force

`x_j^2/tau^2>1/4`.                                                    (A.14)

Since

`sum_{j != i} x_j^2/tau^2=1`,                                       (A.15)

there can be at most **three** residual physical coordinates satisfying (A.14). Thus every residual-heavy row not carrying the quantitative transverse pair-star mass (A.11) belongs to a set of cardinality at most three.

## A.3 Refined remaining structural debt

Combining this addendum with Theorem 4.1 of `REPORT.md`, failure of the diffuse normalized-residual gate has a sharper form:

1. either there exists an actual physical pair `{i,j}` with aggregate anchored principal-triple mass `T_ij>=S_i/4` (and `>=1/8` at target normalization); or
2. every offending normalized-residual heavy row is one of at most three longitudinal spikes with `x_j^2/(1-c)>1/4`.

Thus the residual-heavy branch is not an arbitrary high-dimensional obstruction. The next coarea/minor interface can attack a **fixed-pair aggregate star** before minor selection, while the complementary longitudinal obstruction is finite-cardinality.

No density conclusion is claimed from (A.11) alone. In particular, the live corrections forbid inferring a uniformly good single physical triple from aggregate star mass. The point is to expose the exact aggregate currency and the finite-cardinality alternative without that invalid selection step.
