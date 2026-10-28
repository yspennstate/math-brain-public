SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-24T01:02:02Z.
attacking: translation-uniform overlap-preserving localization: derive an exact averaging lemma for quadratic receiver slopes when the third resource shares one original coordinate with the rough-hub core.

# account03/B14 — overlap-preserving two-Plancherel localization

Run: `20260924T010202Z-account03-B14-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: translations and localization  
Status: `NEW SUPPORTING THEOREM / FULL QFORM OPEN / CONTINUITY PROVED ONLY ON THIS BRANCH`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source state

The full target remains open: for every finite `n`, every independent real input vector with marginal probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal `L^infinity` density bound for `X^T A X`, or give a genuine counterexample.


The designated partner result used at equation level is the still-valid slice-Fourier part of account04/B14 r9:

- repository/commit: `yspennstate/math-open-problems@b5f173477a3889ad9432ea7d97767e969c83b279`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T141430Z-account04-B14-affine-slice-fresnel-r9/REPORT.md`;
- equation (3.6): for the unnormalised frozen `V=l` slices,

  `|mu_hat_{l,g}(t)| <= 4 sqrt(pi) |gamma t|^(-1/2)`.

The later correction to r9 concerns the interval-only rough-hub endpoint, not this Fourier slice estimate. The newest partner r10 was also read: `yspennstate/math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`; it gives zero-tax Schur localization once a uniformly invertible physical 3x3 block is already present. The theorem below addresses a different missing interface: an extra independent bank may share the physical hub coordinate with the slice core, so it cannot be appended by ordinary convolution.

I also use the standard product-projection estimate already source-pinned in this slot at `yspennstate/math-open-problems@20e9f45a5d8c8d79034aa09318d8922daae66599`: if `Z_j` are independent cap-one variables and `a != 0`, then

`||p_{a^T Z}||_infinity <= sqrt(2)/||a||_2`.

## 2. Abstract overlap-preserving compiler

Let `X` be a real random variable with probability density `f_X <= 1`. Let `(L,Y)` be independent of `X`, and suppose its law disintegrates with respect to Lebesgue measure in the first coordinate as

`P((L,Y) in dl dy) = nu_l(dy) dl`,

where `nu_l` are finite positive measures and

`int nu_l(R) dl = 1`.

For `t != 0`, put

`F_t(l) = int exp(i t y) nu_l(dy)`.

Assume the frozen-slice Fourier estimate

`ess sup_l |F_t(l)| <= A |t|^(-1/2)`                                  (2.1)

for some finite `A` independent of `t`.

Let `Z` be independent of `(X,L,Y)`. Let `S=S(Z)` and `R=R(Z)` be arbitrary real measurable functions, and assume only that `S` has a probability density `p_S` satisfying

`||p_S||_infinity <= M`.                                             (2.2)

Finally let `H:R->R` be an arbitrary measurable real function and define

`Q = H(X) + 2 X L + Y + 2 X S(Z) + R(Z)`.                          (2.3)

The term `2 X S(Z)` is the key overlap: it uses the same physical hub `X` as the slice receiver `2XL`. Thus the `Z` bank is not an independent additive receiver and ordinary convolution does not apply.

### Theorem 2.1 — `QFORM-OVERLAP-HUB-SLOPE-TWO-PLANCHEREL-v1`

Under (2.1)-(2.3), the characteristic function of `Q` satisfies

`|phi_Q(t)| <= min{1, pi sqrt(A M) |t|^(-5/4)}`.                   (2.4)

Consequently `Q` has a continuous density vanishing at infinity and

`boxed: ||p_Q||_infinity <= 5 pi^(-1/5) (A M)^(2/5).`             (2.5)

There is no moment, support, fragment-count, fragment-separation, diameter, centering, connected-support, or tail parameter in (2.5). Arbitrary translations inside `H`, `L`, `S`, `Y`, or `R` are free whenever they preserve the same numerical slice constant `A` and slope-density cap `M`.

### Proof

For fixed `t != 0`, define

`G_t(x) = int exp(2 i t x l) F_t(l) dl`.                            (2.6)

The trivial inequality `|F_t(l)| <= nu_l(R)` and (2.1) give

`int |F_t(l)|^2 dl
 <= A |t|^(-1/2) int nu_l(R) dl
 = A |t|^(-1/2).`                                                   (2.7)

With the Fourier convention `hat g(xi)=int exp(i xi l)g(l)dl`, Plancherel and the change `xi=2tx` yield

`||G_t||_2^2
 = (pi/|t|) int |F_t(l)|^2 dl
 <= pi A |t|^(-3/2),`                                               (2.8)

hence

`||G_t||_2 <= sqrt(pi A) |t|^(-3/4).`                              (2.9)

Now push the complex measure `exp(i t R(Z)) dP_Z` forward by `S`. Since the law of `S` has density `p_S`, the pushed complex measure has a density

`g_t(s)=E[exp(i t R(Z)) | S=s] p_S(s)`

for a regular conditional version. Therefore

`|g_t(s)| <= p_S(s),`
`int |g_t(s)| ds <= 1,`
`int |g_t(s)|^2 ds <= M`.                                          (2.10)

Define the overlapping-bank multiplier

`K_t(x)=E exp(i t (R(Z)+2xS(Z)))
       =int exp(2 i t x s) g_t(s) ds.`                             (2.11)

A second Plancherel identity gives

`||K_t||_2^2
 =(pi/|t|) int |g_t(s)|^2 ds
 <= pi M |t|^(-1),`                                                 (2.12)

so

`||K_t||_2 <= sqrt(pi M) |t|^(-1/2).`                              (2.13)

Independence of `X`, `(L,Y)`, and `Z` gives the exact factorisation at the physical hub level

`phi_Q(t)
 = int f_X(x) exp(i t H(x)) G_t(x) K_t(x) dx.`                     (2.14)

Because `0 <= f_X <= 1`, Cauchy-Schwarz may be applied without paying any support measure:

`|phi_Q(t)|
 <= int |G_t(x)K_t(x)| dx
 <= ||G_t||_2 ||K_t||_2
 <= pi sqrt(A M) |t|^(-5/4).`                                     (2.15)

Together with `|phi_Q(t)|<=1`, this proves (2.4).

Put `K=pi sqrt(A M)` and `t_0=K^(4/5)`. Then

`int_R |phi_Q(t)| dt
 <= 2[ int_0^{t_0}1 dt + K int_{t_0}^infinity t^(-5/4)dt ]
 = 2[t_0+4K t_0^(-1/4)]
 = 10 K^(4/5).`                                                     (2.16)

Fourier inversion therefore gives a continuous `C_0` density and

`||p_Q||_infinity
 <= (1/(2pi)) 10 K^(4/5)
 =5 pi^(-1/5)(AM)^(2/5).`                                         (2.17)

This proves the theorem. QED.

## 3. Why this is a genuine overlap lemma

If one discards the `Z` bank by the pointwise bound `|K_t(x)|<=1`, only (2.9) remains and the decay is `|t|^(-3/4)`, which is not integrable. The new step does not convolve an independent output law after the core. Instead it retains the shared hub `X` and takes an `L^2(dx)` norm of the `Z`-bank multiplier before the final Cauchy-Schwarz pairing. The two half-dimensional smoothing resources multiply as

`|t|^(-3/4) * |t|^(-1/2) = |t|^(-5/4)`,

which crosses the Fourier `L^1` endpoint.

The phase `R(Z)` may be an arbitrary quadratic or affine function of the entire bank and may be maximally correlated with the slope `S(Z)`. It costs nothing because the complex conditional amplitude `E[e^{itR}|S=s]` has modulus at most one. This is precisely the form needed when the third resource shares the physical hub coordinate but otherwise lives on a disjoint original-coordinate bank.

## 4. Equation-level application of account04/B14 r9

Use the partner normal form

`Q_core = H(X_0)+2 X_0(hV+q_0)+Y_g`,                               (4.1)

where r9 proves for the unnormalised `V=v` slices

`|mu_hat_{v,g}(t)| <= 4 sqrt(pi) |gamma t|^(-1/2).`                (4.2)

Change the slice coordinate to `L=hV+q_0`. The new unnormalised slices are

`nu_l = |h|^(-1) mu_{(l-q_0)/h,g}`,                               (4.3)

so (2.1) holds with

`A = 4 sqrt(pi)/( |h| sqrt(|gamma|) ).`                            (4.4)

Now add an independent original-coordinate product bank `Z` only through

`2 X_0 a^T Z + R(Z)`,                                              (4.5)

where `R(Z)` is completely arbitrary and `a != 0`. The product-projection estimate gives

`M <= sqrt(2)/||a||_2.`                                            (4.6)

Substituting (4.4)-(4.6) into (2.5) yields the explicit continuous-density bound

`boxed:
 ||p_Q||_infinity
 <= 10 ||a||_2^(-2/5) |h|^(-2/5) |gamma|^(-1/5).`                 (4.7)

Indeed the powers of `pi` cancel exactly:

`5 pi^(-1/5) [4 sqrt(pi) sqrt(2)]^(2/5)=10.`                       (4.8)

At the partner's unit active scale `|b|>=1`, `c>1/2`, `h=b sqrt(c)`, `|gamma|>=1`, and with `||a||_2>=1`,

`boxed: ||p_Q||_infinity <= 5 * 2^(6/5) < 11.487.`                 (4.9)

This conclusion is stronger in regularity than r9's original endpoint: the density on the branch (4.5) is continuous because the combined characteristic function is integrable.

Scope guard: r9's later-corrected interval-only rough-hub `L^infinity` inference is not used. Only the source-valid Fourier slice estimate (3.6) is used.

## 5. Translation / fragmentation ledger

The theorem is whole-law and requires no localization of supports. In particular:

1. translating `X` changes `H` and the affine coefficient of `L+S` but not either Plancherel norm;
2. translating `L` or `S` multiplies the relevant Fourier-side densities by phases and leaves `A` or `M` unchanged;
3. arbitrary countable distant fragments in any marginal are retained before the `L^2` norms are taken, so there is no fragment-count sum;
4. `R(Z)` may contain arbitrary self-curvature and affine terms on the whole bank;
5. no expectation of `|Z|`, `|L|`, or any polynomial tail quantity occurs.

Thus this is a genuine translation-uniform, unbounded-support localization compiler rather than a truncation argument.

## 6. Exact stress family showing why physical-triple extraction is not enough

Let three independent banks be present: the r9 heavy-null diffuse core variables, the physical hub `X_0`, and an additional bank `Z=(Z_1,...,Z_m)` with

`a_m=(1/sqrt(m),...,1/sqrt(m))`,                                  (6.1)

so `||a_m||_2=1` while every individual hub-bank coefficient is `m^(-1/2) -> 0`. For arbitrary independent cap-one laws on the `Z_j` and arbitrary quadratic-affine `R_m(Z)`, (4.7) gives the same bound

`||p_Q||_infinity <= 10 |h|^(-2/5)|gamma|^(-1/5)`                 (6.2)

for every `m`. Thus the third smoothing resource may be completely diffuse across an arbitrarily large bank; no largest coefficient or bounded fragment geometry is needed. Paying one coordinate at a time would lose a positive power of `m`, whereas the bank projection cap uses `||a_m||_2=1` before inversion.

This is not claimed to solve the unrestricted spectral extraction problem. The bare condition `s_3(A)>=1` does not yet force a decomposition in which one can identify a source-valid r9 slice core and a source-disjoint bank entering only through the shared hub slope.

## 7. Relation to newest account04/B14 r10

The newest partner theorem r10 proves that, once an actual three-coordinate principal block `B` has `sigma_min(B)=sigma>0`, arbitrary outside cross-couplings and translations already cost zero and

`||p_Q||_{infinity,ess} <= 6 sqrt(pi)/sigma.`                      (7.1)

The present theorem is complementary. It does not assume an invertible physical triple. Instead it converts a slice-Fourier `1/2` resource plus a diffuse overlapping hub-slope bank into an `L^1` characteristic function. In the structural proof assembly, r10 pays genuinely localized triples while Theorem 2.1 pays a specific diffuse-overlap chamber that r10 can miss when every physical triple is nearly singular.

## 8. Remaining implication

Full QFORM is still `OPEN / NOT PROVED / NOT DISPROVED`. Full-target continuity is also open.

The exact next bridge is structural: starting from only `s_3(A)>=1`, show that one can always obtain either

- a uniformly invertible physical triple, paid by account04/B14 r10; or
- a slice-Fourier core plus a source-disjoint overlapping slope bank with the scale product `A M` universally controlled, paid by Theorem 2.1; or
- another already-certified fleet chamber.

The theorem here removes one former analytic obstruction: an independent diffuse bank sharing the hub coordinate is not intrinsically dangerous. Its slope density supplies an additional physical-variable Plancherel factor and can improve, rather than degrade, the rough-hub Fourier endpoint.

## 9. Checks and publication hygiene

The exact integral used in (2.16) is

`int_R min(1,K|t|^(-5/4))dt = 10 K^(4/5)`.

At `||a||_2>=1`, `|h|>=2^(-1/2)`, `|gamma|>=1`, (4.7) becomes

`10 * 2^(1/5) = 5 * 2^(6/5) = 11.4869835499...`.

The source r9 constant `C_* = 4 exp(1/8) 2^(-1/4) Gamma(1/4)` evaluates to `13.8188014757...`; it is not used in (4.7), because the Fourier-slice equation (3.6) gives the sharper direct constant required here.

Changed-file privacy review: this report contains only pure mathematical statements, public/internal repository commit identifiers and authorized QFORM paths. No credentials, account secrets, unrelated personal/company/trading material, signed URLs, or machine paths are present. Connector-only execution did not expose a repository secret-scanner command, so this is a narrow manual changed-file fallback scan, not a claim of a full repository scan.
