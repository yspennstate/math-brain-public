SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-24T06:10:35Z.
attacking: opposite-square post-smoothing of the completed account02/B14 same-sign overlap compiler; quantify active-fragment mass while keeping arbitrary outside localization exactly linear.

# B14 report — opposite-square post-smoothing and a square-root active-fragment compiler

Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.
Run: `20260924T061035Z-account01-B14-QFORM-auto11`.
Status: **new supporting localization theorem proved / designated partner applied to an actual exact-target inequality / full unrestricted QFORM OPEN / continuity separate**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Why change mechanism

The preceding B14 run used coherent Fourier/collision energy on a linear slope bank. The newest completed account02/B14 report identifies a different endpoint: a same-sign quadratic Beta compiler is exactly linear in independent environment mass but has no positive mass exponent in an active square carrier. I therefore switch to a physical-space mechanism: first use the partner theorem to create a bounded-density same-sign overlap output, then use a third independent square as a singular one-sided convolution kernel and retain the *mass* of the active submeasure in a sharp bathtub step.

This is not pointwise quadratic Fourier decay and uses no moments, support diameter, fragment count, centering, or post-rotation independence.

## 2. Completed designated-partner input

Source actually read and used:

- repository: `yspennstate/math-open-problems`
- source commit: `bdb2475cb1079bd054f8e502059a851d3ee3dcd3`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260924T053625Z-account02-B14-QFORM-auto11/REPORT.md`
- source blob: `e53dbed28891bd00f8fe6c2da3b9a8c57d8bcdab`

The completed partner theorem needed below is the finite-measure same-sign Beta compiler. For finite active measures `rho_W(w)dw`, `rho_U(u)du` with pointwise caps `L_W,L_U`, same-sign nonzero `a,d`, and an arbitrary fixed environment value `z`, the pushforward of the active product measure by

`P_z(w,u)=a(w+Phi(u,z))^2+d(u+theta(z))^2+R(z)`

has density cap

`H = pi L_W L_U / sqrt(|a d|)`.

The proof in the partner report is pointwise in `z` before environment integration, so I use precisely that conditional statement. The active output mass is the product of the two active input masses.

## 3. A sharp one-sided bathtub lemma

### Lemma `QFORM-HALF-KERNEL-BATHTUB-v1`

Let `b:[0,infinity)->[0,infinity)` satisfy

`||b||_infinity <= H`, `int_0^infinity b(s) ds <= M`.

Then

`boxed: int_0^infinity b(s) s^(-1/2) ds <= 2 sqrt(H M).`

### Proof

For `0<u<H`, put `E_u={s:b(s)>u}`. Layer cake and the one-dimensional decreasing rearrangement inequality give

`int b(s)s^(-1/2)ds`
` = int_0^H [int_(E_u) s^(-1/2) ds] du`
` <= 2 int_0^H |E_u|^(1/2) du`.

Cauchy-Schwarz in `u` yields

`<=2 sqrt(H int_0^H |E_u|du)=2 sqrt(H int b)=2 sqrt(HM)`.

Equality in the abstract constrained problem is attained by `b=H 1_[0,M/H]`, so the constant of this abstract bathtub step is sharp.

## 4. New theorem: opposite-square post-smoothing of an overlap pair

### Theorem `QFORM-OVERLAP-BETA-THIRD-SQUARE-SUBMEASURE-v1`

Let `rho_W(w)dw`, `rho_U(u)du`, `rho_Y(y)dy` be finite positive one-dimensional measures with

`0<=rho_W<=L_W`, `0<=rho_U<=L_U`, `0<=rho_Y<=L_Y`,

and masses `m_W,m_U,m_Y`. Let `tau` be an arbitrary finite positive measure on an independent environment space, of total mass `m_Z`.

Let `a,d,e` be nonzero, with `a,d` of the same sign. Let `sigma in {+1,-1}`. For arbitrary measurable functions `Phi(u,z)`, `theta(z)`, `psi(z)`, `R(z)`, push the product finite measure

`rho_W dw x rho_U du x rho_Y dy x tau(dz)`

forward by

`Q(w,u,y,z)`
` = a(w+Phi(u,z))^2 + d(u+theta(z))^2`
`   + sigma e (y+psi(z))^2 + R(z)`.

Set

`H = pi L_W L_U / sqrt(|a d|)`,
`M = m_W m_U`.

Then the output finite measure is absolutely continuous and

`boxed:`
`||p_Q||_infinity`
` <= m_Z min{ H m_Y, 2 L_Y sqrt( H M / |e| ) }.`              (4.1)

Equivalently,

`||p_Q||_infinity`
` <= m_Z min{`
`   pi L_W L_U m_Y / sqrt(|ad|),`
`   2 sqrt(pi) L_Y sqrt(m_W m_U) sqrt(L_W L_U)`
`      / ( |ad|^(1/4) |e|^(1/2) )`
` }.`                                                         (4.2)

No support radius, number of fragments, separation, moments, centering, or bounds on `Phi,theta,psi,R` occur.

### Proof

Fix `z`. By the completed account02/B14 theorem, the first two terms have a finite output density `h_z` satisfying

`0<=h_z<=H`, `int h_z = M`.                                   (4.3)

Independently, put `S_z=|e|(Y+psi(z))^2`. Its positive pushforward has mass `m_Y`; for `s>0`, the two inverse branches give

`k_z(s)`
` = [rho_Y(-psi(z)+sqrt(s/|e|)) + rho_Y(-psi(z)-sqrt(s/|e|))]`
`   /(2 sqrt(|e| s))`
` <= L_Y / sqrt(|e| s).`                                      (4.4)

The sign `sigma` only reflects this square output. Thus the conditional output density is a convolution of `h_z` with either `k_z` or its reflection, followed by translation by `R(z)`.

First, ordinary `L^infinity * L^1` convolution gives

`||p_(Q|z)||_infinity <= H m_Y`.                               (4.5)

Second, for a fixed output point `q`, after the harmless reflection/translation, (4.4) gives

`p_(Q|z)(q)`
` <= L_Y |e|^(-1/2) int_0^infinity h_z(q +/- s) s^(-1/2) ds`.

The nonnegative function `b_q(s)=h_z(q +/- s)1_{s>=0}` has cap `H` and mass at most `M`. Applying the bathtub lemma gives

`p_(Q|z)(q) <= 2 L_Y sqrt(HM/|e|)`.                            (4.6)

Taking the better of (4.5),(4.6) proves the conditional estimate. Integrating the conditional finite measures against `tau(dz)` multiplies the common bound by exactly `m_Z`, proving (4.1).

## 5. Exact localization consequence

The theorem cleanly separates two localization directions.

### Outside environment: exact zero tax

For any finite or countable positive decomposition

`tau=sum_j tau_j`, `m_j=tau_j(Zspace)`,

each output piece has the same active bracket in (4.1) multiplied by `m_j`. Summing therefore returns

`sum_j m_j = m_Z`

with **exactly the identical constant**. Thus arbitrary translations, remote pieces, countably many environment fragments, unbounded supports and no moments are zero-tax.

### Active carrier: square-root mass after the third square

Assume for clarity `W,Y` are probability laws, `L_W=L_U=L_Y=1`, and a single `U` fragment has unnormalised mass `m`. Then

`boxed:`
`||p_(Q,U-fragment)||_infinity`
` <= min{ pi/sqrt(|ad|),`
`         2 sqrt(pi) m^(1/2) / (|ad|^(1/4)|e|^(1/2)) }.`       (5.1)

The newest partner endpoint alone had no positive active-mass exponent. The independent third square changes the fragment branch from exponent zero to exponent `1/2`.

If an active law is decomposed into fragment masses `m_j`, a valid fragment-first compiler is therefore

`sum_j min{H,K sqrt(m_j)}`,
`K=2 sqrt(H/|e|)`                                              (5.2)

in the unit-cap probability case. It is finite whenever `sum_j sqrt(m_j)<infinity`, independent of all fragment locations and support geometry. It can still diverge for arbitrary countable decompositions, so this does **not** license active fragmentation in the full theorem.

Moreover `f(m)=min{H,K sqrt(m)}` is concave, increasing, and `f(0)=0`, hence subadditive on `[0,1]`: `f(x)+f(y)>=f(x+y)` when `x+y<=1`. Thus coarsening active pieces never worsens this certificate; the safe proof order is to aggregate active carriers as far as possible before paying the endpoint.

This sharpens the partner's active-fragment barrier quantitatively without contradicting it.

## 6. Actual exact-target partner application

Take the original-coordinate active matrix

`A_* = [[2,1,0],`
`       [1,2,0],`
`       [0,0,-4]].`

Its spectrum is exactly

`spec(A_*)={3,1,-4}`,

so it satisfies the owner's three-large-eigenvalue hypothesis. For independent cap-one probability variables `W,U,Y`, arbitrary affine terms can be written as

`Q = 2W^2+2WU+2U^2-4Y^2 + alpha W+beta U+gamma Y+eta`

`  = 2(W+U/2+alpha/4)^2`
`    +(3/2)(U+(beta-alpha/2)/3)^2`
`    -4(Y-gamma/8)^2 + constant.`                             (6.1)

Thus the completed account02/B14 overlap theorem applies to the first two squares with

`a=2`, `d=3/2`,
`H=pi/sqrt(3)=1.8137993642342178...`.

Applying the new third-square branch with `|e|=4`, `m_W=m_U=m_Y=1`, gives the actual inequality

`boxed:`
`||p_Q||_infinity`
` <= min{ pi/sqrt(3), sqrt(pi/sqrt(3)) }`
` = sqrt(pi/sqrt(3))`
` = 1.3467736870885985... .`                                  (6.2)

This is strictly stronger than the partner pair cap on the same form.

Now embed `A_*` as a principal block of an arbitrary larger symmetric matrix. Condition on every outside original coordinate. All active-outside couplings become deterministic affine coefficients `alpha,beta,gamma`, and all outside curvature becomes the scalar `eta`; (6.1)-(6.2) are uniform in those coefficients. Hence every such ambient form satisfies

`boxed: ||p_(X^T A X)||_infinity <= 1.3467736870885985...`      (6.3)

for arbitrary independent cap-one input laws. Cauchy interlacing preserves at least the three threshold eigenvalues in the ambient matrix. No probabilistic rotation is performed.

This is a genuine indefinite, off-diagonal, exact-target chamber with arbitrary ambient couplings, arbitrary translations, fragmented/unbounded supports and no moments.

## 7. Exact-target active-fragment diagnostic

Use instead the partner's earlier exact-target block

`B_*=[[2,1,0],[1,2,0],[0,0,-1]]`, `spec(B_*)={3,1,-1}`.

For a `U` submeasure of mass `m`, (5.1) gives

`||p_fragment||_infinity`
` <= min{ pi/sqrt(3), 2 sqrt(pi) 3^(-1/4) sqrt(m) }`
` = min{ 1.8137993642342178... , 2.693547374177197... sqrt(m) }.`

The crossover is

`m_*=pi/(4 sqrt(3))=0.45344984105855446...`.

For `N` equal active teeth and `N>=3`, fragment-first summation therefore costs at most

`2.693547374177197... sqrt(N)`,

rather than the partner endpoint's linear `N*pi/sqrt(3)` cost. But it still diverges with `N`.

For the unbounded-support masses `m_j=6/(pi^2 j^2)` used in the partner report,

`sum_j sqrt(m_j) = (sqrt(6)/pi) sum_j 1/j = infinity`.

So even after the third-square improvement, arbitrary active fragmentation cannot be justified by positive piecewise summation. The correct whole-law proof order remains essential.

## 8. Scope and remaining implication

This report does **not** prove unrestricted QFORM. It proves a physical-space post-smoothing theorem for a completed same-sign overlap chamber and an exact ambient principal-block consequence.

The remaining structural implication is:

`QFORM-WHOLE-ACTIVE-THIRD-SMOOTHER-OR-MASS-LINEAR-EXIT-v1`:

from bare `s_3(A)>=1`, before normalising an active carrier into spatial fragments, force either

1. a whole same-sign overlap plus a source-disjoint square/receiver strong enough to smooth it as above,
2. a genuinely mass-linear aggregate slope/volume/ridge/grouped-bank compiler,
3. or another already completed whole-active physical-pair/triple/Schur exit.

The exponent `1/2` here is an improvement over the unsmoothed Beta endpoint but is still below the mass-linear threshold needed for arbitrary countable active localization. This is the exact remaining localization obstruction exposed by the theorem.

## 9. Source-match / integrity note

A repository search for the exact square-root active-submeasure post-smoothing formulation returned no source match. A search miss is not a novelty proof; the status is only **supporting theorem proved**. The argument uses the completed designated-partner theorem at equation (4.3), not as background decoration.

Consumed live corrections include: no uniform pointwise quadratic Fourier decay; no independence after rotation; no bounded-diameter localization; no uniform fragment-count bathtub reduction; no universally well-conditioned physical minor; aggregate-before-normalize requirements on rough product fibers. None is violated here.

Full unrestricted QFORM: **OPEN**.
