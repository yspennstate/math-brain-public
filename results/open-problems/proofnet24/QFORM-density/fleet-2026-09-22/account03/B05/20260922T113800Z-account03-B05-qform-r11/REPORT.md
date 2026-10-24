# account03/B05 — delocalized spectral-subspace Fresnel–Brascamp–Lieb bound

Status: **ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / FULL TARGET OPEN**

Programme: `QFORM-DENSITY-3EIG-20260922`

Run: `20260922T113800Z-account03-B05-qform-r11`

Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Target and corrections consumed

The current target is: for independent real `X_i` with densities `0<=f_i<=1`, and a real symmetric matrix `A` having at least three eigenvalues of absolute value at least `1`, prove that `Q=X^T A X` has a universally bounded density (and, separately, ideally a continuous representative).

This run does **not** use the refuted law-uniform pointwise one-dimensional Fresnel decay. It also does not rotate and then retain only a joint `L^infinity` density bound, and it does not take a fiberwise supremum. Those mechanisms are known to lose the product structure or dimension.

The directly relevant peer result is account02/B05 (`math-research-brain` commit `e88f1fe38a73b03361ebd00825ab2d4367b73b6f`): naive two-dimensional spectral-plane coarea with fiber supremum loses a factor `n/2` on an explicit cube projection, while its exact pair-kernel identity shows why product averaging must be retained. The current assigned partner is account04/B05; at the fresh source read no completed current-qform artifact from that slot was visible, so no stale BT4 artifact is substituted for partner mathematics.

A second exact stress source is account02/B07 (`math-research-brain` handoff `account02-B07-20260922T113436Z.md`): rank-three Walsh projections have spectrum `(1,1,1,0,...)` while every fixed-size original-coordinate principal block tends to zero. Thus any useful positive result should survive a genuinely delocalized rank-three form.

## 2. External ingredient: the small-leverage Fourier–Brascamp–Lieb estimate

Rudelson–Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, Proposition 5.1, prove the following stronger fact inside their proof.

Let `R` be an `r x n` matrix with `R R^T=I_r`, let `P=R^T R`, and let `X` have independent coordinates with densities bounded by `1`. If

`max_j ||P e_j||_2 <= 1/2`,

then, for

`psi(xi)=E exp(i <xi,RX>)`,

there is an absolute constant `B<infinity` such that

`int_{R^r} |psi(xi)| dxi <= B^r`.                                          (2.1)

This is not merely an inference from a bounded projection density. In their proof they write the product characteristic function using the frame columns `R e_j`, apply Brascamp–Lieb, and bound the resulting one-dimensional integrals; their displayed equation (5.4) yields an upper bound `(2C)^r`. We denote that absolute base by `B`.

The distinction matters: an arbitrary bounded joint density can concentrate near quadratic level sets, whereas (2.1) retains the original coordinate-product structure through its Fourier transform.

## 3. New theorem

### Theorem (delocalized full-spectral-support quadratic bound)

Let `A` be a real symmetric matrix of rank `r>=3`. Write its nonzero spectral decomposition as

`A = R^T Lambda R`,

where `R R^T=I_r` and `Lambda=diag(lambda_1,...,lambda_r)` is invertible. Put

`P=R^T R`,

`D = (prod_{k=1}^r |lambda_k|)^(1/r)`.

Let `X_1,...,X_n` be independent with densities bounded by `1`. Assume the spectral subspace is small-leverage in the original product coordinates:

`max_j ||P e_j||_2 <= 1/2`.                                                (3.1)

Then `Q=X^T A X` has a continuous density and

`||p_Q||_infinity <= [B^2/(4 pi^2 D)] * r/(r-2)`.                         (3.2)

In particular, if `D>=1`, then

`||p_Q||_infinity <= 3 B^2/(4 pi^2)`.                                    (3.3)

Thus this is a dimension-free target-level conclusion on a genuine delocalized cone of matrices, for every sign pattern of the nonzero eigenvalues.

### Proof

Set `Y=RX` and let

`psi(xi)=E exp(i <xi,Y>)`.

By (3.1) and the Rudelson–Vershynin small-leverage argument,

`||psi||_1 <= B^r`.                                                       (3.4)

For `t!=0`, let

`Phi(t)=E exp(i t Y^T Lambda Y)`.

We first justify a Fresnel pairing without any unjustified pointwise decay assumption on the individual input densities. For `epsilon>0`, define

`g_epsilon(y)=exp(i t y^T Lambda y - epsilon |y|^2)`.

Since `psi in L^1`, the law of `Y` has the continuous density

`p_Y(y)=(2 pi)^(-r) int exp(-i<xi,y>) psi(xi) dxi`.

The Fourier transform of `g_epsilon` factors coordinatewise. For every `xi`,

`|hat g_epsilon(xi)| <= pi^(r/2) |t|^(-r/2) |det Lambda|^(-1/2)`.          (3.5)

Indeed in coordinate `k` the Gaussian integral has prefactor

`sqrt(pi/(epsilon-i t lambda_k))`,

whose modulus is at most `sqrt(pi/(|t lambda_k|))`; the exponential factor has modulus at most one. Hence Fourier inversion/Fubini gives

`|int p_Y(y) g_epsilon(y) dy|`

` <= (2 pi)^(-r) pi^(r/2) |t|^(-r/2) |det Lambda|^(-1/2) ||psi||_1`.

Letting `epsilon downarrow 0` is legitimate on the left by dominated convergence (`p_Y` is a probability density), and on the Fourier side by (3.5) and `psi in L^1`. Therefore

`|Phi(t)| <= B^r (4 pi |t|)^(-r/2) |det Lambda|^(-1/2)`

`          = [B / sqrt(4 pi D |t|)]^r`.                                  (3.6)

No sign restriction was used: only absolute values of the eigenvalues enter the Fresnel modulus.

Set

`alpha = B^2/(4 pi D)`.

Combining (3.6) with the trivial `|Phi(t)|<=1`,

`|Phi(t)| <= min(1,(alpha/|t|)^(r/2))`.                                  (3.7)

Since `r>2`, this is integrable. Directly,

`int_R |Phi(t)| dt`

` <= 2 [ int_0^alpha 1 dt + alpha^(r/2) int_alpha^infinity t^(-r/2) dt ]`

` = 2 alpha * r/(r-2)`.                                                   (3.8)

Fourier inversion for a probability law with integrable characteristic function now gives a continuous density and

`||p_Q||_infinity <= (2 pi)^(-1) ||Phi||_1`

` <= alpha/pi * r/(r-2)`

` = [B^2/(4 pi^2 D)] * r/(r-2)`,

which is (3.2). If `D>=1`, then `r/(r-2)<=3`, proving (3.3). QED.

## 4. Exact application to the delocalized Walsh stress family

Take the account02/B07 rank-three Walsh projection

`A_n = r_1 r_1^T + r_2 r_2^T + r_3 r_3^T`,

where the three normalized Walsh vectors are orthonormal. Then `r=3`, all nonzero eigenvalues equal `1`, and hence `D=1`. Every coordinate has

`||P e_j||_2^2 = 3/n`,

so the small-leverage hypothesis holds as soon as

`sqrt(3/n) <= 1/2`, i.e. `n>=12`.

For Walsh powers this covers every `n>=16`. Consequently this family, despite having every fixed-size principal block vanish with `n`, satisfies

`||p_{X^T A_n X}||_infinity <= 3 B^2/(4 pi^2)`                         (4.1)

uniformly in `n` and uniformly over all independent coordinate laws with density at most `1`.

This directly resolves the *delocalized aggregation* obstruction exhibited by B07 for the asymptotic Walsh family. It also explains why the account02/B05 `Theta(n)` fiber-supremum loss is an artifact of discarding product averaging rather than evidence against the conjecture.

## 5. What this does and does not prove

**Proved.** A universal bounded and continuous output density for every rank-`r>=3` form satisfying (3.1) and `D>=1`; more generally the quantitative bound (3.2) for arbitrary `D>0`.

**Not proved.** The full owner target only assumes that *three* eigenvalues have magnitude at least one. There may be many additional nonzero eigenvalues of arbitrarily small magnitude. Applying the theorem to the full spectral support then introduces

`D=(prod |lambda_k|)^(1/r)`,

which may be arbitrarily small.

One cannot simply discard the small-eigenvalue spectral complement: if `S` is the span of three chosen large eigenvectors and `Y=P_S X`, then the remaining quadratic phase is dependent on `Y` after rotation. In the conditional representation it becomes a bounded but arbitrary complex multiplier of the projected density, and multiplication by a bounded function does **not** preserve the Wiener `L^1` Fourier norm used in (3.4). This is the exact spectral-truncation debt.

Likewise, replacing the projected law merely by its `L^infinity` density bound is insufficient; the known shell mechanism shows that a general bounded joint density can have an arbitrarily large quadratic pushforward density.

## 6. First unpaid implication

`QFORM-SPECTRAL-TRUNCATION-WIENER-v1`:

Given a three-dimensional large-eigenvalue spectral subspace `S` with small leverage, prove a dimension-free analogue of (3.4) for the **phase-weighted conditional projection** generated by the orthogonal spectral complement, or find a source-valid counterexample to such a weighted Wiener estimate.

Equivalently, obtain enough decay/integrability from the three large modes without paying the determinant of arbitrarily small complementary eigenvalues.

A natural local/delocalized split is now precise:

1. diffuse selected spectral directions should be attacked by the Wiener/Fresnel mechanism above;
2. failure of the leverage condition produces localized coordinates, where coordinate-minor/bilinear mechanisms can be attempted;
3. the hard common interface is retaining the complementary quadratic phase without destroying the product-structure estimate.

## 7. Source and integrity notes

External source used: M. Rudelson and R. Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, especially Proposition 5.1 and equations (5.1)–(5.4). The proof, not merely the proposition statement, supplies the Fourier `L^1` bound used here.

No numerical simulation is used. The result is a supporting theorem, not a proof of the full conjecture. It does not infer anything from the retired FEI safe-cone work.
