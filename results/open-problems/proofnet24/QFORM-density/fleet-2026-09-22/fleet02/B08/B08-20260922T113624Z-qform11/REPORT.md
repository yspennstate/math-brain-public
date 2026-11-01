# fleet02/B08 — diffuse eigenvector case

**Run:** `B08-20260922T113624Z-qform11`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `ESSENTIAL_STEP_APPLIED / DIFFUSE-RANK3-FOURIER-BL-CERTIFICATE`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full conjecture:** **OPEN / NOT PROVED / NOT DISPROVED**

## 0. Control pivot, source pins, and correction status

Fresh owner control superseded the stale FEI prompt during this invocation. The live target is:

> For independent real random variables `X_1,...,X_n` with probability densities `0<=f_i<=1`, and real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove that `Q=X^TAX` has an essentially bounded density with one universal bound, or give a genuine counterexample.

Control/source pins used in this run:

- Same commit, assignment card `assignments/fleet02/B08.json`, blob `bd33fcd74bd3b2f9c5ef975df074c30c749dbc8d`.
- `CORRECTION_INBOX.json` at the publication precursor snapshot contained no additional events.
- Completed peer source actually consumed: `yspennstate/math-research-brain@2dac8145f316ba9ecced5c98093efc681522a878`, `scheduled_tasks/runs/fleet03/B16/20260922T113226Z-qform-r11/report.md`, blob `07109b1e3a16125ab7965e557a73c58e44d10715`.
- Complementary localized-coordinate source consumed: `yspennstate/math-open-problems@d5392d73398e2811f58b612fb8f191aa79d8ee5e`, fleet02/B15 report `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T110507Z-fleet02-B15-qform-pivot-r1/REPORT.md`, blob `1da4167bbf6b2785659bd50007cab5f04b9c3084`.

The named partner `fleet03/B08` had no completed current-programme handoff or canonical QFORM report at the fresh read, so no partner result is fabricated. The fleet03/B16 result is used explicitly below: it refutes law-uniform pointwise one-dimensional stationary phase and proves a diagonal supporting case. The B15 result supplies the complementary *localized* principal-coordinate theorem; the present report attacks the genuinely diffuse branch requested by the B08 card.

Classical analytic inputs used with their standard exact scopes:

1. **Rank-one geometric Brascamp–Lieb.** If unit vectors `v_i in R^d` and weights `c_i>0` satisfy `sum_i c_i v_i v_i^T=I_d`, then for nonnegative measurable `h_i`,
   
   `int_{R^d} prod_i h_i(<v_i,x>)^{c_i} dx <= prod_i (int_R h_i)^{c_i}`.

2. **Beckner sharp Hausdorff–Young.** For the Fourier convention `hat f(xi)=int exp(-i xi x) f(x) dx`, `1<=p<=2`, `q=p/(p-1)`,
   
   `||hat f||_q <= (2pi)^{1/q} p^{1/(2p)} q^{-1/(2q)} ||f||_p`.

No moment, connected-support, continuity, centering, identical-law, log-concavity, or sign hypothesis is introduced.

## 1. Compact conditional end-to-end argument

For a rank-three form write

`A=U Lambda U^T`,

where `U` is `n x 3` with orthonormal columns and `Lambda=diag(lambda_1,lambda_2,lambda_3)` with `|lambda_j|>=1`. Put `u_i^T` for row `i` of `U` and define the leverage scores

`c_i=||u_i||_2^2`.

Because `U^TU=I_3`,

`sum_i u_i u_i^T=I_3`,  and  `sum_i c_i=3`.

If every `c_i<=1/2`, the projection

`Y=U^T X=sum_i u_i X_i`

has an integrable characteristic function, with an explicit dimension-free `L^1` bound. Fourier inversion then turns the quadratic Fresnel kernel into `|t|^{-3/2}` decay for the characteristic function of `Q=Y^T Lambda Y`; this decay is integrable and gives a universal output-density bound.

The first missing implication for the **full** target is therefore no longer the diffuse rank-three case. What remains is a hybrid theorem for rows of leverage `>1/2`, and then a way to handle extra nonzero spectral directions without discarding the original coordinate product structure.

## 2. Main theorem: diffuse rank-three forms have density at most `3e`

### Theorem 2.1 — `QFORM-DIFFUSE-RANK3-BL-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities `f_i` satisfying `0<=f_i<=1`. Let

`A=U Lambda U^T`

be real symmetric of rank exactly `3`, where `U in R^{n x 3}` has orthonormal columns and every eigenvalue of `Lambda` satisfies `|lambda_j|>=1`. If every row `u_i` of `U` obeys

`||u_i||_2^2 <= 1/2`,

then `Q=X^TAX` has a bounded continuous density `p_Q` and

`||p_Q||_infinity <= 3e < 8.155`.

The constant is independent of `n`, of the input laws, of the signs and multiplicities of the three nonzero eigenvalues, and of `U`.

### Proof

#### Step 1: an exact `L^1` Fourier bound for the three-dimensional spectral projection

Set

`Y=U^T X in R^3`.

Its characteristic function is

`hat g(xi)=E exp(-i <xi,Y>) = prod_i hat f_i(<u_i,xi>)`,

where `hat f_i(s)=int exp(-isx)f_i(x)dx`. We shall prove directly that this function belongs to `L^1(R^3)`; Fourier inversion then gives the bounded continuous density `g` of `Y`.

Ignore zero rows. For every nonzero row put

`c_i=||u_i||^2`,  `v_i=u_i/sqrt(c_i)`.

Then `v_i` is unit and

`sum_i c_i v_i v_i^T=sum_i u_i u_i^T=I_3`.

Define

`h_i(s)=|hat f_i(sqrt(c_i) s)|^{1/c_i}`.

The geometric Brascamp–Lieb inequality gives

`int_{R^3} prod_i |hat f_i(<u_i,xi>)| dxi`

`<= prod_i (int_R h_i)^{c_i}`

`= prod_i c_i^{-c_i/2} ||hat f_i||_{1/c_i}`.                                    `(2.1)`

Because `c_i<=1/2`, let

`q_i=1/c_i >=2`,  `p_i=q_i/(q_i-1)=1/(1-c_i) in [1,2]`.

Sharp Hausdorff–Young in the stated Fourier convention yields

`||hat f_i||_{q_i}`

`<= (2pi)^{c_i} (1-c_i)^{-(1-c_i)/2} c_i^{c_i/2} ||f_i||_{p_i}`.                 `(2.2)`

The density assumptions imply `||f_i||_{p_i}<=1`, since `0<=f_i<=1` and `int f_i=1`. Substituting (2.2) into (2.1) cancels `c_i^{-c_i/2}` exactly and gives

`||hat g||_1 <= (2pi)^{sum_i c_i} prod_i (1-c_i)^{-(1-c_i)/2}`

`= (2pi)^3 prod_i (1-c_i)^{-(1-c_i)/2}`.                                       `(2.3)`

For `0<=c<1`,

`-(1-c) log(1-c) <= c`.

Indeed `c+(1-c)log(1-c)` vanishes at zero and has derivative `-log(1-c)>=0`. Therefore, using `sum_i c_i=3`,

`prod_i (1-c_i)^{-(1-c_i)/2} <= exp(3/2)`,

and hence

`boxed{ ||hat g||_1 <= (2pi)^3 e^{3/2}. }`                                    `(2.4)`

This is the key diffuse-eigenvector estimate. It is a frequency-*averaged* product-structure estimate and does not contradict the already-refuted law-uniform pointwise stationary-phase lemma.

#### Step 2: Fresnel decay for the quadratic characteristic function

Now

`Q=Y^T Lambda Y`,

so

`phi_Q(t)=int_{R^3} exp(i t y^T Lambda y) g(y)dy`.

To justify the oscillatory interchange without hidden regularity, insert a Gaussian cutoff. For `epsilon>0`, let

`I_epsilon(t)=int exp(i t y^T Lambda y) exp(-epsilon |y|^2) g(y)dy`.

Using Fourier inversion for `g` and Fubini against `hat g in L^1`,

`I_epsilon(t)=(2pi)^(-3) int hat g(xi) K_{epsilon,t}(xi) dxi`,

where the complex Gaussian integral `K_{epsilon,t}` satisfies

`|K_{epsilon,t}(xi)| <= pi^{3/2} |t|^{-3/2} |det Lambda|^{-1/2}`.                 `(2.5)`

One way to see (2.5) is to diagonalize `Lambda`; each scalar Gaussian factor has modulus

`pi^{1/2} (epsilon^2+t^2 lambda_j^2)^(-1/4)`

and the remaining exponential factor has modulus at most `1`.

Combining (2.4) and (2.5), and using `|det Lambda|>=1`, gives

`|I_epsilon(t)| <= e^{3/2} pi^{3/2} |t|^{-3/2}`.                               `(2.6)`

Because `g` is a probability density, `exp(-epsilon|y|^2)g(y)->g(y)` in `L^1`, so `I_epsilon(t)->phi_Q(t)`. Thus

`boxed{ |phi_Q(t)| <= K |t|^{-3/2},  K=e^{3/2} pi^{3/2}. }`                     `(2.7)`

Together with the trivial `|phi_Q(t)|<=1`,

`|phi_Q(t)| <= min(1,K|t|^{-3/2})`.

#### Step 3: integrate the characteristic function and invert

The crossover is

`t_0=K^{2/3}=e pi`.

Therefore

`int_R |phi_Q(t)|dt`

`<=2[ t_0 + K int_{t_0}^infinity t^{-3/2}dt ]`

`=2[t_0+2K t_0^{-1/2}]`

`=6 e pi`.                                                                      `(2.8)`

Since `phi_Q in L^1`, Fourier inversion gives a bounded continuous density and

`||p_Q||_infinity <= (2pi)^(-1) ||phi_Q||_1 <= 3e`.                             `(2.9)`

This proves the theorem. `QED`.

## 3. Why the leverage threshold is a real mechanism boundary

The condition `c_i<=1/2` is not an arbitrary cosmetic cutoff in this proof. The Brascamp–Lieb step forces the one-dimensional Fourier exponent

`q_i=1/c_i`.

For `c_i<=1/2`, `q_i>=2`, exactly the range supplied by Hausdorff–Young from the available information `f_i in L^{p_i}`, `1<=p_i<=2`. If `c_i>1/2`, the same argument asks for an `L^q` norm of `hat f_i` with `q<2`, which is not controlled by `0<=f_i<=1`, `int f_i=1`.

This failure is genuine. In the fully aligned rank-three example

`U=[e_1,e_2,e_3]`

there are three leverage-one rows. For interval-uniform inputs, each one-dimensional Fourier transform is a sinc function and is not in `L^1`; consequently the three-dimensional projection characteristic function is not in `L^1(R^3)`. Nevertheless the diagonal theorem in CURRENT_RESEARCH gives the output quadratic density bound `<=pi` by a **physical-space square-density convolution**. Therefore requiring `hat g in L^1` cannot be the full proof mechanism.

This provides an exact methodological division:

- **diffuse frame:** Fourier–Brascamp–Lieb gives `C=3e`;
- **strongly localized physical coordinates:** principal-coordinate / square-density methods can give a direct bound;
- **intermediate heavy/light frames:** require a hybrid argument rather than either extreme alone.

## 4. Complementarity with the localized-coordinate result

The fleet02/B15 principal-triple theorem proves a direct physical-coordinate density bound whenever some `3 x 3` principal block of `A` has a dimension-free lower singular-value bound. That mechanism is excellent for localized curvature but can fail badly for delocalized frames: a normalized Hadamard-type rank-three form may have every fixed-size physical compression of operator norm `O(m/n)`.

Theorem 2.1 above treats exactly the opposite geometry for rank three: it does not require *any* large physical-coordinate minor. It needs only the row-leverage ceiling `max_i ||u_i||^2<=1/2`, which is automatic for sufficiently spread spectral frames and remains meaningful even when every individual physical `3 x 3` curvature block is tiny.

Thus the two results are genuinely complementary rather than duplicate subclasses.

## 5. Stronger variant available for fully large rank

The same calculation works in dimension `r>=3` if `A` has rank `r`, **every nonzero eigenvalue** has magnitude at least `1`, and every leverage score of an orthonormal basis of `range(A)` is at most `1/2`. In that case

`||hat g||_1 <= (2pi)^r e^{r/2}`

and the `r`-dimensional Fresnel integral gives

`|phi_Q(t)| <= e^{r/2} pi^{r/2} |t|^{-r/2}`.

Writing `K_r=e^{r/2}pi^{r/2}`, the crossover remains `K_r^{2/r}=e pi`; hence

`||p_Q||_infinity <= e r/(r-2) <= 3e`.                                         `(5.1)`

This is useful but **not** the full target, because the target allows extra nonzero eigenvalues of arbitrarily small magnitude. Treating those extra terms as independent noise is invalid after spectral rotation.

## 6. First essential unpaid implication

### `QFORM-RANK3-HYBRID-HEAVY-LIGHT-v1`

Close the rank-three geometry without the leverage ceiling. A plausible exact decomposition is to treat rows with normalized leverage `>1/2` by physical-space square/coarea smoothing and the remaining tight-frame mass by the Fourier–Brascamp–Lieb mechanism above. The accounting must retain the original coordinate product law and must not divide by a small conditional mass.

A successful hybrid statement should interpolate between:

1. the aligned branch, where the diagonal/square convolution gives a `pi`-scale bound although `hat g notin L^1`, and
2. the diffuse branch proved here, where `hat g in L^1` and `C=3e`.

After rank three is closed, the next separate obstruction is **extra nonzero spectral directions**. If one writes `A=A_3+A_rest` in the eigenbasis, `A_rest` is not independent noise relative to `A_3` under the original product law. A proof must either control the resulting complex fiber amplitudes or use a small-ball/coarea formulation that preserves product structure.

## 7. Status ledger

- Full quadratic-form conjecture: **OPEN**.
- Owner-proposed law-uniform one-dimensional pointwise `|t|^{-1/2}` decay: **REFUTED by existing source; not reused**.
- Diagonal three-large-coordinate case: **PROVED by existing source, with current-state bound `pi`**.
- Localized nonsingular physical principal triple: **PROVED by existing B15 source with a quantitative block-dependent constant**.
- Rank exactly three, all three eigenvalues `|lambda|>=1`, row leverages `<=1/2`: **PROVED HERE**, bounded continuous density with explicit `C=3e`.
- Fully-large rank `r>=3` with all nonzero eigenvalues `>=1` in magnitude and all range leverage scores `<=1/2`: **PROVED HERE**, `C<=3e`.
- Rank-three heavy/light hybrid: **OPEN**.
- General target with arbitrary additional small nonzero eigenvalues: **OPEN**.

## 8. Privacy / provenance review

The report contains only the authorized mathematical target, public classical theorem names, repository source pins, and newly derived mathematics. It contains no credentials, scheduler identifiers, machine paths, benchmark material, unrelated private data, emails, paid-call outputs, or native-brain secrets. No public posting, remote workflow, permission change, or production-memory mutation was performed.
