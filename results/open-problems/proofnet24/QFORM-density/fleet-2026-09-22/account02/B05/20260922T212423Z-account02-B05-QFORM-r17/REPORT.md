SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-22T21:24:23Z.
attacking: aggregate an entire diffuse cross bank before pair inversion, and isolate exactly where within-bank quadratic leakage re-enters.

# account02/B05 — disjoint-bank pair coarea after Ball normalization

Run: `20260922T212423Z-account02-B05-QFORM-r17`
Programme: `QFORM-DENSITY-3EIG-20260922`
Classification: **ESSENTIAL_STEP_APPLIED / SUPPORTING TARGET-VALID FAMILY CLOSED / FULL QFORM OPEN**
Execution: `WITHOUT_VERIFIED_BRAIN`

Fresh protected controls were read from `yspennstate/math-research-brain` main. The live owner revision is `2026-09-22.15`; QFORM remains the sole target. The latest correction `QFORM-TRIBANK-CROSS-CORE-LEAKAGE-CLOSURE-FALSE-v1` is explicitly respected below: the theorem does **not** claim that a good normalized aggregate core controls arbitrary within-bank quadratic phases.

## 1. Sources actually applied

1. Named partner account03/B05, run `20260922T194010Z-account03-B05-QFORM-r16`, canonical commit
   `d6312e9c0de9a774079895ee3c7aad7043015e49`.
   Its reviewed pair-log theorem says that for two independent cap-one original scalar variables with an invertible indefinite pair matrix `B`, `D=|det B|`, `kappa=sigma_min(B)`, and an independent scalar remainder satisfying

   `sup_t P(|R-t|<rho) <= H sqrt(rho)`,

   one has

   `||p_Q||_infinity <= 4 sqrt(2H) (D kappa)^(-1/4)`.

   The same partner run proved the moving-critical-value repair on the localized near-zero family and independently reviewed the pair-log source for its stated scope.

2. account01/B16, run `20260922T190433Z-account01-B16-QFORM-auto11`, canonical source read at commit
   `641b1a339cff99906f46f05e4411711f4660c506`.
   It proves and applies the Rogozin--Ball one-dimensional projection bound used here: for independent cap-one coordinates and a coefficient vector `b`, the linear form `L=b dot Y` has density cap at most `sqrt(2)/||b||_2`. Its exact rank-one-pair theorem is the `a=0` endpoint of the diffuse-star corollary below.

No arbitrary-joint rank-three coarea, no conditional projection-density supremum/moment, no post-rotation independence, and no unrestricted curved-fiber supremum is used.

## 2. First unpaid implication attacked

The preceding B05 run reduced the local geometry to a density-normalized three-bank core but left **within-bank quadratic residual dependence** unpaid. The named partner sharpened the same issue in the near-zero coloop branch: a cross direction can be spread over many physical coordinates, making every individual physical pair poorly conditioned.

The question attacked here is the maximal no-leakage version:

> If a whole leaf bank enters the quadratic form only through one linear innovation `L=b dot Y`, can one aggregate the entire bank before any reciprocal pair cost and retain a dimension-free pair-coarea bound?

The answer is yes, with a fully explicit bound. Consequently the only obstruction left in this model is genuinely the additional within-bank quadratic/longitudinal leakage prohibited by the fresh correction above.

## 3. Aggregate pair-coarea theorem

### Theorem 3.1 — `QFORM-DISJOINT-BANK-INDEFINITE-PAIR-COAREA-v1`

Let

- `X,H,Y_1,...,Y_m` be mutually independent real random variables with densities bounded by one;
- `b in R^m`, `r=||b||_2>0`, and `L=b dot Y`;
- `c !=0`, and let `a,u,d,alpha,beta,gamma,q0` be arbitrary real constants.

Set

`Q0 = c X^2 + gamma X
      + a H^2 + 2u H L + d L^2 + alpha H + beta L + q0`.

Define the density-normalized aggregate pair matrix

`B = [[a, u r/sqrt(2)],
      [u r/sqrt(2), d r^2/2]]`,

and suppose `B` is invertible and indefinite. Put

`D=|det B|`, `kappa=sigma_min(B)`.

Then `Q0` has an essentially bounded density and

`boxed( ||p_Q0||_infinity
        <= 8*2^(1/4) |c|^(-1/4) (D kappa)^(-1/4). )`        (3.1)

Moreover, if `W` is independent of `(X,H,Y)` and `R(W)` is any measurable real random variable (in particular any quadratic form in a disjoint original-coordinate bank), then the same bound holds for `Q0+R(W)`.

#### Proof

By the Rogozin--Ball linear projection theorem,

`||p_L||_infinity <= sqrt(2)/r`.                                      (3.2)

Define

`Z=(sqrt(2)/r)L`.

Then `Z` has density cap at most one and is independent of both `H` and `X`, because it is a function only of the disjoint `Y` bank. Since `L=(r/sqrt(2))Z`, the `(H,L)` part becomes

`aH^2 + 2uHL + dL^2
 = aH^2 + 2(u r/sqrt(2))HZ + (d r^2/2)Z^2`,

with quadratic matrix exactly `B`. The linear terms `alpha H+beta L` become an arbitrary affine term in the independent cap-one pair `(H,Z)`, which is allowed by the partner pair-log theorem.

The independent scalar remainder

`R_X=cX^2+gamma X`

satisfies the translation-uniform square small-ball estimate

`sup_t P(|R_X-t|<rho)
 <= 2 sqrt(2/|c|) sqrt(rho)`.                                          (3.3)

Indeed complete the square in `X`; the inverse image of an interval of width `2rho` under a scalar square has total length at most `2sqrt(2rho/|c|)`, and `f_X<=1`.

Thus the partner theorem applies with

`H0=2 sqrt(2/|c|)`.

Its constant is

`4 sqrt(2H0)
 =4 sqrt(4 sqrt(2/|c|))
 =8*2^(1/4)|c|^(-1/4)`.                                               (3.4)

Substitution gives (3.1). Finally, adding the independent variable `R(W)` convolves the already bounded density with a probability measure, so it cannot increase the essential supremum. QED.

### What is new in the theorem

No individual leaf coordinate is selected and no factor such as `1/max_j |b_j|` or a local-pair condition number is paid. The whole cross bank is compressed first, and only its Euclidean norm `r=||b||_2` enters the normalized pair. Thus the theorem is stable under arbitrarily diffuse coefficients, e.g. `b_j~m^(-1/2)`.

The theorem is deliberately **not** stated with an arbitrary additional quadratic form on the same `Y` bank. That stronger statement is exactly where the new correction `QFORM-TRIBANK-CROSS-CORE-LEAKAGE-CLOSURE-FALSE-v1` applies: after replacing `Y` by the scalar `L`, an arbitrary within-bank quadratic phase remains dependent on `L` and cannot be convolved away or treated as independent noise.

## 4. Exact target-valid diffuse-star closure

### Corollary 4.1 — `QFORM-DIFFUSE-NEARZERO-STAR-BANK-v1`

Assume `a>=0`, `|c|>=1`, and `b in R^m` satisfies

`r^2=||b||_2^2 >= a+1`.

For arbitrary independent cap-one inputs, the quadratic form

`Q = cX^2 + aH^2 + 2H (b dot Y)`                                    (4.1)

has

`boxed( ||p_Q||_infinity <= 8*2^(3/4) < 13.455. )`                   (4.2)

The same bound survives addition of an arbitrary independent direct-sum quadratic form on disjoint coordinates.

This is an exact target family: the star matrix

`S=[[a,b^T],[b,0]]`

has only two nonzero eigenvalues

`lambda_+ = (a+sqrt(a^2+4r^2))/2`,
`lambda_- = (a-sqrt(a^2+4r^2))/2`.

Because `r^2>=a+1`,

`sqrt(a^2+4r^2) >= a+2`,

so `lambda_+>=a+1>=1` and `lambda_-<=-1`. Together with the disjoint scalar eigenvalue `c`, the full matrix has at least three eigenvalues of modulus at least one.

For the normalized pair of Theorem 3.1 with `u=1,d=0`,

`D=r^2/2 >=1/2`,                                                     (4.3)

and its two eigenvalues are

`mu_+ = (a+sqrt(a^2+2r^2))/2`,
`mu_- = (a-sqrt(a^2+2r^2))/2`.

Hence

`kappa=|mu_-|=(sqrt(a^2+2r^2)-a)/2 >=1/2`,                           (4.4)

because `r^2>=a+1` implies `sqrt(a^2+2r^2)>=a+1`. Therefore

`D kappa >=1/4`.                                                      (4.5)

Apply (3.1) and `|c|>=1`:

`||p_Q||_infinity
 <=8*2^(1/4)(1/4)^(-1/4)
 =8*2^(3/4)
 =13.4543426440...`.                                                  (4.6)

This simultaneously contains the diffuse exact-null star mechanism of account01/B16 (`a=0`) and the named partner's near-zero moving-pair mechanism after replacing a single leaf by an arbitrary diffuse leaf bank. For the sharp normalization `r^2=a+1`, the unnormalized star eigenvalues are exactly `{a+1,-1}` for every `a>=0`.

## 5. Why this matters for the full target

This run closes a clean bridge that was missing between two previously separate endpoints:

- `a=0`: the physical hub/leaf pair is singular, and account01/B16 pays total cross-bank determinant mass before inversion;
- localized `a>0`: account03/B05 keeps an invertible indefinite pair and its moving critical value;
- **new here**: for arbitrary bank size and arbitrarily diffuse coefficients, Ball normalization makes the whole bank one cap-one scalar innovation and the partner pair-log theorem pays the resulting pair with a constant independent of dimension and of the largest individual leaf coefficient.

Thus diffuse cross-bank aggregation itself is not the remaining difficulty. The exact unpaid factor is now narrower:

`QFORM-CROSSBANK-DEPENDENT-LEAKAGE-COAREA-v1`:

> Allow the same leaf bank to carry additional quadratic self-curvature and/or longitudinal couplings not expressible solely through `L=b dot Y`. Prove a product-preserving coarea estimate that averages the moving critical value jointly with this dependent leakage, or derive a structural reduction forcing one of the already-paid physical-pair, rank-one aggregate, ridge/diffuse, or grouped-coordinate branches.

The fresh correction `QFORM-TRIBANK-CROSS-CORE-LEAKAGE-CLOSURE-FALSE-v1` shows that one may not simply drop this dependence and keep only the normalized aggregate core. The full QFORM conjecture therefore remains **OPEN / NOT PROVED / NOT DISPROVED**.

## 6. Exact check

A small exact/numeric checker beside this report verifies the characteristic polynomials, the target eigenvalue threshold at `r^2=a+1`, the normalized-pair lower bounds `D>=1/2`, `kappa>=1/2` on representative parameters, and the constant `8*2^(3/4)`. The checker is a regression aid only; the inequalities above are the proof.

## 7. Source and correction discipline

Consumed before publication:

- current QFORM owner revision `2026-09-22.15` and proof-first continuation;
- false arbitrary-joint 3D coarea;
- false positive conditional projection-density moments;
- false scalar-remainder conditional supremum;
- no post-rotation independence;
- no one-good-minor/exact-arrowhead exhaustive reduction;
- fresh `QFORM-TRIBANK-CROSS-CORE-LEAKAGE-CLOSURE-FALSE-v1`.

No benchmark, FEI, installation, email, Drive, public release, paid model/API/Codex call, remote workflow, permission change, scheduler mutation, or unrelated private data was used.
