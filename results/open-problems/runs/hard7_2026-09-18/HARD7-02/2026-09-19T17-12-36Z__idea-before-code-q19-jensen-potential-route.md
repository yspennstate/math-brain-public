Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning.

# HARD7-02 idea checkpoint before code — Q1.9 STUCK1, replace eigenvalue stability by a circular logarithmic-potential observable

Frozen source metric at entry: `T_corr=0`. The two post-admission Q1.9 runs have both left it unchanged, so if this run also fails to classify one full correlated limiting law, Section I triggers now. This is therefore a **thinking run with no new theorem claim and no checker construction**.

Previous Q1.9 method triples were `B2/B24/B30` and `B3/B7/B19`. This run deliberately switches to **B18 / B25 / B22**.

## B18 — say the radial-tail problem in another language

The previous route tried to preserve large eigenvalues associated with isolated reciprocal edges after reattaching the sub-threshold matrix. That is the wrong level of resolution for a highly nonnormal matrix: an exact eigenvalue of a sparse truncation need not remain near any eigenvalue after a globally small-looking but nonnormal perturbation.

Instead use the source's own Hermitization observable. For a planar probability measure `mu` with the required logarithmic integrability, define

`U_mu(z)=int log|z-w| mu(dw)`

and its circular excess over the point mass at the origin,

`P_mu(r) := (1/(2 pi)) int_0^{2 pi} U_mu(r e^{i theta}) d theta - log r`.

By the standard mean-value/Jensen identity

`(1/(2 pi)) int_0^{2 pi} log|r e^{i theta}-w| d theta = log max(r,|w|)`,

so

`P_mu(r) = int log^+(|w|/r) mu(dw) = int_r^infinity mu(|w|>s) ds/s`.

For an `n x n` matrix `A`, the same scalar can be counted in a second way:

`P_A(r) = (1/(2 pi n)) int_0^{2 pi} log|det(r e^{i theta} I-A)| d theta - log r`

`       = (1/n) sum_j log^+(|lambda_j(A)|/r)`.

This identity is classical and is **not claimed as a new result**. Its importance here is strategic: it exactly encodes the radial eigenvalue tail but is expressed through the log determinant / singular values, where Campbell--O'Rourke already have the PWIT-Hermitization machinery. Thus the nonnormal individual-eigenvalue stability obstacle can be removed from the statement of the next obligation.

For the frozen law `mu=mu_{1,vartheta_{1/4}}`, the sharp source-slice target can be replaced by the scalar large-radius asymptotic

`P_mu(r) = K/r + o(1/r)`

for some `K in (0,infinity)` (with the reciprocal-edge skeleton suggesting, but not proving, the candidate `K=kappa=3^(1/4)/2`). If this asymptotic is established, monotonicity of the tail gives the same power-one tail asymptotic. Indeed, for fixed `lambda>1`,

`P(r)-P(lambda r) = int_r^{lambda r} F(s) ds/s`,  `F(s)=mu(|z|>s)`,

and hence

`F(lambda r) log lambda <= P(r)-P(lambda r) <= F(r) log lambda`.

Applying the analogous inequality on `[r/lambda,r]`, inserting `P(r)=K/r+o(1/r)`, and then letting `lambda downarrow 1` squeezes `r F(r)` to `K`. This is again an elementary route identity, not a new source theorem.

## B25 — count the same tail twice

The scalar `P_mu(r)` has two exact interpretations:

1. integrated radial tail: `int_r^infinity F(s) ds/s`;
2. circularly averaged log determinant / singular-value log potential.

That is precisely the bridge the previous reciprocal-edge work lacked. The skeleton already supplies a concrete candidate mechanism for a `1/r` radial tail, while Theorem 1.6 of Campbell--O'Rourke expresses the limiting log potential through the singular-value law `nu_{alpha,z,theta_d}`. Proposition 4.12 supplies a recursive distributional equation for the corresponding Hermitized resolvent.

The next proof should therefore **not** attempt to track individual large eigenvalues. It should estimate the first nontrivial `1/r` term in the circular average of the limiting log potential, uniformly enough to justify the angular integral and the `eta downarrow 0` limit in Hermitization.

A particularly useful normalization is

`Q_x(r) := r P_{mu_{1,vartheta_x}}(r)`.

The first source-relevant milestone is not an isolated block statement but a scalar statement such as

`0 < liminf_{r->infinity} Q_{1/4}(r) <= limsup_{r->infinity} Q_{1/4}(r) < infinity`,

and the source-slice classification would follow from convergence of `Q_{1/4}(r)` to a positive finite constant. None of these statements is asserted here.

## B22 — read the obstruction and the nearest successful proof

The closest solved non-Hermitian endpoint is Bordenave--Caputo--Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices* (CMP 307 (2011), arXiv:1006.1713). Their i.i.d. axis-supported model has a limiting law with stretched-exponential radial tail. Their proof combines the PWIT objective method with Girko Hermitization / logarithmic potentials and obtains a scalar recursive structure after exploiting the i.i.d./isotropic endpoint.

Campbell--O'Rourke extend the PWIT/Hermitization framework to correlated elliptic atom pairs, but Proposition 4.12 retains a genuinely matrix-valued stable recursive distribution. That is the missing simplification: for interior `vartheta_x`, the reciprocal pair structure prevents the same scalar collapse that drives the i.i.d. endpoint analysis.

The previous HARD7-02 attacks failed for a consistent reason:

- reciprocal `2 x 2` blocks give the right candidate scale but are local;
- `K_alpha(theta)` counts local tail-capable PWIT marks, not full-matrix eigenvalues;
- all `p<1` moment bounds give only a one-sided exponent restriction;
- the strong-isolated exceedance skeleton has an exact `1/r` eigenvalue tail, but reattaching the sub-threshold background destroys the block decomposition and nonnormal eigenvalues need not be stable;
- the exploration algorithm exactly counts isolated tail blocks but contains no global invariant that survives reattachment.

The nearest successful proof has precisely what those routes lack: a **global Hermitized log-potential observable** whose limit is controlled by singular values rather than individual eigenvalue perturbation. The recovery choice is therefore: **port the technique from the nearest solved problem**, but apply it only to the circular average needed for the radial tail instead of trying to solve the full angular density.

## Next mathematical attack, if this STUCK1 recovery is continued

Use a new triple **B6 / B11 / B29**:

- **B6** deform from the solvable axis-supported i.i.d. endpoint toward `vartheta_x`, asking which term in the circularly averaged Hermitized recursion first becomes order `1/r`;
- **B11** dualize the radial-tail question completely into the singular-value/log-potential side via Theorem 1.6 and Proposition 4.12;
- **B29** compactify the large-radius regime with `u=1/z` (or `rho=1/r`) and seek the first boundary coefficient at `u=0`, where the desired `1/r` law becomes a first-order boundary term.

No code is warranted in this thinking run because no finite claim is being certified. The next run should only build a checker if a concrete finite algebraic coefficient or truncation identity emerges from the Hermitized recursion.
