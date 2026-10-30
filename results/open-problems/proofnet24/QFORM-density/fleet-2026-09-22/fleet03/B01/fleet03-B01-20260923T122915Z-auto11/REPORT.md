SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B01, 2026-09-23T12:29:15Z.
attacking: rank-one active-bank curvature via an indefinite physical pair plus a source-disjoint grouped square, with the logarithmic pair singularity averaged before signed-Fejer transfer.

# fleet03/B01 — indefinite pair plus grouped square: logarithmic averaged-frequency receiver

Run: `fleet03-B01-20260923T122915Z-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Oscillatory replacement`  
Status: **NEW SUPPORTING TARGET-VALID THEOREM / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

## 1. Source and correction boundary


The unrestricted target remains open. This report uses no law-uniform pointwise quadratic-phase decay, no post-rotation independence, no arbitrary-joint coarea bound, no conditional projection-density moment, and no uniformly good fixed physical minor. The phase-aligned fragmented-support counterexample is preserved.

Two source-valid inputs are used.

1. The physical-pair logarithmic envelope from
`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
For independent original-coordinate `U,V` with density caps one and an invertible indefinite symmetric `2 x 2` matrix `B`, writing
`D=|det B|`, `kappa=sigma_min(B)`, the affine pair has, for every `r>0`, the conditional density envelope

`p_pair(t) <= 2sqrt(2)/r + D^(-1/2) log_+(2r^2/(kappa |t-t0|))`.      (1.1)

The pair shifts may depend arbitrarily on the remainder variables.

2. The designated fleet04/B01 signed-Fejer identity and latest overlap-two result. The exact Fejer identity is in
`yspennstate/math-open-problems@88003dc06af684cc4bc178a7dfe8e7cbebb0f987`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T234537Z-fleet04-B01-grouped-square-fejer-r2/REPORT.md`:

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`,                         (1.2)

where

`D_T mu(y)=(1/(2pi)) integral_(-T)^T (1-|t|/T) Re(e^(-ity) muhat(t)) dt`,

with both sides infinite when no bounded density exists. The same report gives the source-valid projection bound

`||p_(a^T X)||_infinity <= sqrt(2)/||a||_2`.                        (1.3)

The newest completed fleet04/B01 partner result is
`yspennstate/math-open-problems@27ae9c5fbf53787fac1d61d7f480e0283be8c1c5`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260923T121347Z-fleet04-B01-overlap2-explicit-r1/REPORT.md`.
For an invertible indefinite physical pair `S`, it proves

`||p_Q||_infinity <=22.385 (D kappa)^(-1/6) W_2(S)^(-1/12)`.       (1.4)

Section 7 below applies (1.4) and the present theorem simultaneously to the same target-valid matrix.

## 2. Preserve the pointwise obstruction

Fix `s>0` and `0<delta<pi/2`. The set

`E_infty={x: dist(s x^2,2pi Z)<=delta}`

has infinite Lebesgue measure, since the component lengths around `sqrt(2pi k/s)` are comparable to `k^(-1/2)`. Choose a finite union `E subset E_infty` of measure one and take `f=1_E`. Then

`Re integral exp(i s x^2) f(x) dx >= cos(delta)`.                  (2.1)

Hence no positive-power pointwise estimate uniform over all cap-one densities can hold. The theorem below replaces it by a distribution/signed-Fejer estimate after a genuinely independent third source is averaged.

## 3. Exact small-ball bound for one grouped square

### Lemma 3.1

Let `Y` have probability density bounded by `m`, let `lambda !=0`, and let `h` be arbitrary. Put

`S=lambda (Y+h)^2`.

Then for every `s in R` and `eta>0`,

`P(|S-s|<eta) <= min(1, 2sqrt(2) m sqrt(eta/|lambda|)).`            (3.1)

### Proof

After reflection it suffices to take `lambda>0` and write `eps=eta/lambda`, `q=s/lambda`. The inverse image of `(q-eps,q+eps)` under `x -> x^2` has total length at most `2sqrt(2eps)`. Indeed, if `q<eps` its length is at most `2sqrt(q+eps)<=2sqrt(2eps)`; if `q>=eps`, its length is

`2(sqrt(q+eps)-sqrt(q-eps)) = 4eps/(sqrt(q+eps)+sqrt(q-eps)) <=2sqrt(2eps)`.

Multiplication by the density cap `m` proves (3.1). QED.

### Lemma 3.2: logarithmic potential of a grouped square

For `A>0`, define

`G(L)=2L` for `0<=L<=1`,
`G(L)=2(1+log L)` for `L>=1`.

Then uniformly in `s`,

`E log_+(A/|S-s|) <= G(2sqrt(2) m sqrt(A/|lambda|)).`               (3.2)

### Proof

Layer cake and (3.1) give

`E log_+(A/|S-s|)`
` = integral_0^infinity P(|S-s|<A e^(-u)) du`
` <= integral_0^infinity min(1,L e^(-u/2)) du`,

where `L=2sqrt(2)m sqrt(A/|lambda|)`. The last integral is `2L` for `L<=1`; for `L>=1`, split at `u=2log L` to obtain `2log L+2`. QED.

This is the essential missing replacement: the logarithmic singularity of an indefinite pair is integrable against a source-disjoint grouped square with a scale-exact bound, although neither scalar quadratic phase has a useful law-uniform pointwise decay estimate.

## 4. Main theorem

### Theorem 4.1 (`QFORM-INDEFINITE-PAIR-PLUS-SQUARE-LOG-v1`)

Partition the original independent coordinates into disjoint sets `S,D,C`, with `S={i,j}`. Conditional on `X_C=c`, suppose the quadratic form has the exact representation

`Q_c=(X_S+m_c(X_D))^T B (X_S+m_c(X_D))`
`    + lambda (z^T X_D+h_c)^2 + r_c`,                              (4.1)

where

- `B` is a fixed invertible indefinite symmetric `2 x 2` matrix,
- `lambda !=0`, `z !=0`,
- `m_c` is arbitrary measurable, so arbitrary pair--D affine coupling already absorbed by completing the physical pair is allowed,
- `h_c,r_c` are arbitrary measurable functions of the conditioning variables.

Set

`D_B=|det B|`, `kappa=sigma_min(B)`, `rho=|lambda| ||z||_2^2`,
`R=8 sqrt(D_B/(kappa rho))`.                                      (4.2)

Then `Q` has a continuous `C_0(R)` density and

`boxed: ||p_Q||_infinity <= 2 D_B^(-1/2) Psi(R)`,                  (4.3)

where

`Psi(R)=2sqrt(R)` for `0<R<=1`,
`Psi(R)=2+log R` for `R>=1`.                                      (4.4)

Equivalently,

if `R<=1`,

`||p_Q||_infinity <=8sqrt(2) D_B^(-1/4)(kappa rho)^(-1/4)`,        (4.5)

and if `R>=1`,

`||p_Q||_infinity <=2 D_B^(-1/2)[2+log(8 sqrt(D_B/(kappa rho)))].` (4.6)

### Proof

Fix `c`. Apply the physical-pair envelope (1.1) conditional on `X_D`. Its critical value is the exact remainder

`S=lambda(z^T X_D+h_c)^2+r_c`.

For every cutoff `r>0` and output point `t`, averaging (1.1) over `X_D` gives

`p_(Q|c)(t) <= a/r + D_B^(-1/2) E log_+(2r^2/(kappa|t-S|)),`       (4.7)

where `a=2sqrt(2)`.

By (1.3), `Y=z^T X_D` has density cap

`m<=sqrt(2)/||z||_2`.                                             (4.8)

Apply Lemma 3.2 with `A=2r^2/kappa`. Its dimensionless argument is at most

`q r`, where `q=4sqrt(2)/sqrt(kappa rho)`.                         (4.9)

Since `G` is increasing,

`p_(Q|c)(t) <= a/r + D_B^(-1/2) G(qr)`.                           (4.10)

Put `b=2D_B^(-1/2)` and

`R=aq/b=8sqrt(D_B/(kappa rho))`.                                  (4.11)

If `R<=1`, the minimizer of `a/r+bqr` is

`r=sqrt(a/(bq))`,

for which `qr=sqrt(R)<=1`, so it lies in the correct branch. The minimum is

`2sqrt(abq)=2b sqrt(R)=4D_B^(-1/2)sqrt(R)`,

which is (4.3)-(4.5).

If `R>=1`, the relevant expression is

`a/r+b(1+log(qr))`.

Its minimizer is `r=a/b`, for which `qr=R>=1`, and its value is

`b[2+log R]=2D_B^(-1/2)[2+log R]`,

which is (4.3)-(4.6). The two formulas coincide at `R=1`.

For regularity, conditional on `c`, the two-coordinate pair has an `L^1` density by the change-of-variables proof of (1.1), and the grouped square has an `L^1` density. Their convolution is in `C_0(R)`. The bound (4.3) is uniform in `c`, so dominated convergence in the conditioning variable gives a continuous `C_0` unconditional density. QED.

## 5. A clean target-scale corollary

Suppose in Theorem 4.1 that

`kappa>=1` and `rho>=1`.                                          (5.1)

Since `B` is symmetric, write its singular values as `M>=kappa`; then `D_B=kappa M` and `M>=1`.

If `R<=1`, then `rho>=64M`, and (4.5) gives

`||p_Q||_infinity <=4 kappa^(-1/2) M^(-1/2) <=4`.                 (5.2)

If `R>=1`, use `rho>=1` and `kappa>=1` in (4.6):

`||p_Q||_infinity`
` <=2 M^(-1/2)[2+log(8sqrt(M))]`
` <=2(2+log 8)`                                                   (5.3)

because `M^(-1/2)[2+log8+(1/2)log M]` is strictly decreasing for `M>=1`.
Therefore

`boxed: ||p_Q||_infinity <=2(2+log 8)=8.1588830833...<8.159.`      (5.4)

This is a genuine three-direction target-scale receiver: two indefinite physical-pair directions plus one source-disjoint grouped square. It keeps arbitrary fragmented/unbounded input supports and arbitrary shifts.

## 6. Exact signed-Fejer consequence

Apply the completed fleet04/B01 identity (1.2) to Theorem 4.1. For every `T>0` and `y in R`,

`boxed: D_T law(Q)(y) <=2 D_B^(-1/2) Psi(8sqrt(D_B/(kappa rho))).`  (6.1)

Thus the averaged-frequency quantity is uniformly bounded on this coupled branch even though the phase-aligned construction (2.1) rules out law-uniform positive-power pointwise scalar Fresnel decay.

Under (5.1),

`sup_(T>0,y) D_T law(Q)(y) <8.159`.                                (6.2)

This is the requested oscillatory replacement in the exact signed-Fejer sense; it does not require `integral |muhat|` to be finite.

## 7. Actual application of the newest fleet04/B01 result

Take the partner's target-valid family

`A_c=diag(1,-1) direct_sum [[0,c],[c,0]],  |c|>=1`.                (7.1)

Its spectrum is `{1,-1,c,-c}`. The newest fleet04/B01 theorem, using the base pair `{1,2}`, gives

`||p_(X^T A_c X)||_infinity <=22.385(2c^2)^(-1/12)`               (7.2)

(and in particular `<21.13 |c|^(-1/6)`).

Now apply Theorem 4.1 to the *same law* using the physical hyperbolic pair `{3,4}`. Here

`B=[[0,c],[c,0]]`, `D_B=c^2`, `kappa=|c|`.

Use coordinate 1 as the source-disjoint square (`rho=1`) and condition coordinate 2, whose `-X_2^2` contribution is only an output shift. Since `R=8sqrt(|c|)>=1`,

`||p_(X^T A_c X)||_infinity`
` <=2|c|^(-1)[2+log(8sqrt(|c|))].`                                (7.3)

Therefore the two independently derived receivers give the concrete combined inequality

`boxed: ||p_(X^T A_c X)||_infinity`
` <= min{22.385(2c^2)^(-1/12), 2|c|^(-1)[2+log(8sqrt(|c|))]}.`     (7.4)

At `|c|=1` the new term is `8.158883...`; it decays as `|c|^(-1)log|c|`, versus the partner's `|c|^(-1/6)` envelope. This is an actual equation-level application of the completed designated partner result, not merely a citation.

By (1.2), the right side of (7.4) also bounds

`sup_(T>0,y) D_T law(X^T A_c X)(y)`.                               (7.5)

## 8. What this removes and what remains

This theorem removes the previous B01 restriction that a rank-one bilinear source bank have no quadratic self-curvature when that active two-coordinate curvature is an invertible indefinite physical pair. The pair's genuine logarithmic singularity is retained and paid by a disjoint square before any pointwise Fourier assertion is made.

It does **not** solve arbitrary active-bank curvature: (4.1) requires that after completing the chosen physical pair the disjoint `D`-bank remainder contain a single grouped square of currency `rho`; an arbitrary full Schur quadratic on `D` is not reduced to this form. The bare three-large-eigenvalue hypothesis does not automatically expose such a pair-plus-disjoint-square packet with `kappa,rho` bounded below.

The first remaining implication is therefore `QFORM-INDEFINITE-PAIR-THIRD-DIRECTION-ROUTING-v1`: from a remaining strict-N3/low-cross-rank state, either expose a quantitatively invertible indefinite pair plus a source-disjoint grouped-square Schur direction, route to the newest overlap-two exterior-star theorem, or route to an already-paid rank-two/rank-three cross, grouped-square, ridge, hub, pair-log, or null-coloop branch. No uniformly good fixed physical minor may be assumed.

Full QFORM remains OPEN. This branch proves both essential boundedness and a continuous `C_0` density.
