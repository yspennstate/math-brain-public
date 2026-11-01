Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0169 — sharp all-n degree-three theorem

Target: Ryan O'Donnell, *Open Problems in Analysis of Boolean Functions* (2012), PDF p. 9, “Linear Coefficients versus Total Degree”.

Methods this iteration: **B11 / B14 / B24**.

## Result

### Theorem
For every Boolean function

`f : {-1,1}^n -> {-1,1}`

of Fourier degree at most three,

`sum_i |fhat({i})| <= 3/2`.

The constant is sharp: three-bit majority has three singleton Fourier coefficients equal to `1/2`, hence singleton `l1` mass `3/2`.

Consequently

`sum_i fhat({i}) <= 3/2 < sqrt(3)`,

so O'Donnell's weaker source inequality is proved for the full all-`n` degree-three case. The frozen source metric therefore moves

`D_weak : 2 -> 3`.

This does **not** solve the source problem for arbitrary degree.

## 1. B11 — exact Fourier granularity

We first prove an arithmetic lemma valid in every dimension.

### Lemma 1
If `f:{-1,1}^n->{-1,1}` has Fourier degree at most `d`, then every nonconstant Fourier coefficient of `f` belongs to

`2^(1-d) Z`.

### Proof
Put

`g=(1-f)/2`.

Then `g` is `{0,1}`-valued. Introduce Boolean variables

`z_i=(1-x_i)/2 in {0,1}`.

The coordinatewise affine substitution preserves multilinear degree, so the unique multilinear polynomial representing `g` on `{0,1}^n` has degree at most `d`:

`g(z)=sum_{T, |T|<=d} a_T prod_{i in T} z_i`.

Every coefficient `a_T` is an integer. Indeed, Möbius inversion on the Boolean lattice gives

`a_T = sum_{U subseteq T} (-1)^{|T|-|U|} g(1_U)`,

an integer because every value of `g` is zero or one.

Now substitute `z_i=(1-x_i)/2`. For each `T`,

`prod_{i in T} z_i = 2^{-|T|} prod_{i in T}(1-x_i)`.

Thus every nonconstant Fourier coefficient of `g` is an integer linear combination of numbers `2^{-|T|}` with `|T|<=d`, hence belongs to `2^{-d} Z`. Since `f=1-2g`, every nonconstant Fourier coefficient of `f` belongs to `2^{1-d} Z`. QED.

At degree three, every nonzero singleton coefficient therefore has magnitude at least `1/4`.

## 2. Active-coordinate reduction to at most sixteen variables

Let

`A={i : fhat({i}) != 0}`,

and write `m=|A|`. Flip the sign of coordinate `i` whenever necessary so that every active singleton coefficient is positive. This preserves Booleanity, Fourier degree and the absolute singleton mass. Write

`B=sum_i |fhat({i})| = sum_{i in A} fhat({i})`.

By Parseval,

`1 = sum_S fhat(S)^2 >= sum_{i in A} fhat({i})^2 >= m/16`.

Hence

`m <= 16`.                                                     (2.1)

Now fix the inactive coordinates `[n]\A`. For each assignment `y` to those coordinates, let `f_y` be the restriction of `f` to the active coordinates. It is still Boolean and has degree at most three.

For `i in A`, the singleton coefficient after restriction is

`f_yhat({i}) = sum_{T subseteq [n]\A} fhat({i} union T) chi_T(y)`.

Averaging uniformly over `y` kills every nonempty `T`, so

`E_y f_yhat({i}) = fhat({i})`.

Therefore, with

`L(y)=sum_{i in A} f_yhat({i})`,

we have

`E_y L(y)=B`.

For at least one restriction `y_*`,

`L(y_*) >= B`.                                                  (2.2)

Thus it suffices to bound the **signed** singleton sum for a Boolean degree-three function on `m<=16` coordinates. This is a genuine all-`n` reduction; the original function need not be a junta.

## 3. B14 — permutation quotient and layer arithmetic

Fix a Boolean degree-at-most-three function

`h:{-1,1}^m->{-1,1}`.

Let

`L(h)=sum_{i=1}^m hhat({i})`.

Average `h` over all coordinate permutations:

`q(x)=E_{pi in S_m} h(x_{pi(1)},...,x_{pi(m)})`.

Then `q` is symmetric, has degree at most three, takes values in `[-1,1]`, and preserves the objective:

`sum_i qhat({i})=L(h)`.                                        (3.1)

For `k=0,...,m`, let the `k`-th Hamming layer consist of points with exactly `k` coordinates equal to `-1`, and define

`C_k=binom(m,k)`,

`a_k=sum_{x in layer k} h(x)`,

`g_k=a_k/C_k`.

Because `h` is Boolean,

`a_k in {-C_k,-C_k+2,...,C_k-2,C_k}`.                         (3.2)

The symmetric function `q` has value exactly `g_k` on layer `k`.

A symmetric multilinear polynomial of Fourier degree at most three is a linear combination of

`sum_{|S|=j} x_S`, `j=0,1,2,3`.

On layer `k`, these are the Krawtchouk polynomials `K_j(k)`, of ordinary polynomial degree `j` in `k`. Hence `g_k` is a polynomial in `k` of degree at most three. Equivalently, for every applicable `k`,

`g_{k+4}-4g_{k+3}+6g_{k+2}-4g_{k+1}+g_k=0`.                  (3.3)

Finally,

`L(h)=E[h(X) sum_i X_i]`

because `E[h(X)X_i]=hhat({i})`. On layer `k`, `sum_i X_i=m-2k`, so

`L(h)=2^{-m} sum_{k=0}^m C_k g_k (m-2k)`.                    (3.4)

Equations (3.2)-(3.4) give an exact finite necessary condition for every possible symmetrization of a Boolean degree-three function.

## 4. Exact finite core

The checker

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree3_layer_certificate.py`

enumerates, using `fractions.Fraction` only, every possible first four layer sums obeying (3.2), propagates (3.3), rejects any later layer not lying on the exact Boolean averaging lattice (3.2), and maximizes (3.4). The enumerated set may contain layer sequences not realizable by any Boolean function; that only makes the resulting maximum a safer upper bound.

The executed exact output is archived at

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree3_layer_certificate.out`.

It certifies:

| `m` | feasible cubic layer sequences | exact maximum of (3.4) |
|---:|---:|---:|
| 1 | 4 | 1 |
| 2 | 12 | 1 |
| 3 | 64 | 3/2 |
| 4 | 90 | 3/2 |
| 5 | 104 | 3/2 |
| 6 | 106 | 3/2 |
| 7 | 114 | 3/2 |
| 8 | 122 | 3/2 |
| 9 | 122 | 3/2 |
| 10 | 128 | 2 |
| 11 | 128 | 2 |
| 12 | 128 | 2 |
| 13 | 132 | 2 |
| 14 | 140 | 2 |
| 15 | 140 | 2 |
| 16 | 144 | 2 |

The script terminates with `ASSERTIONS_PASS`.

Thus every Boolean degree-three `h` on `m<=9` coordinates obeys

`L(h)<=3/2`,                                                   (4.1)

while for `10<=m<=16` it obeys the weaker but sufficient bound

`L(h)<=2`.                                                     (4.2)

## 5. Excluding ten or more active singleton coefficients

Return to the original `f` and its active set `A`. By Lemma 1, every active singleton coefficient has magnitude at least `1/4`, and after normalization it is positive. Therefore

`B >= m/4`.                                                    (5.1)

Suppose `m>=10`. By (2.1), `m<=16`. Choose the restriction `h=f_{y_*}` from (2.2). Then

`L(h)>=B>=m/4>=5/2`.

But the exact finite core gives `L(h)<=2` for every `10<=m<=16`, contradiction. Hence

`m<=9`.                                                        (5.2)

Applying (4.1) to the same restriction,

`B<=L(h)<=3/2`.

Since `B=sum_i |fhat({i})|`, the theorem follows.

## 6. B24 — sharpness and extremal object

Let `Maj_3(x)=sign(x_1+x_2+x_3)`. Its Fourier expansion is

`Maj_3(x)=(x_1+x_2+x_3-x_1x_2x_3)/2`.

Hence each singleton coefficient equals `1/2`, and

`sum_i |Maj_3hat({i})|=3/2`.

Therefore the constant `3/2` in the theorem is sharp. This proves the majority-on-three-bits value proposed by the source for the case `d=3`, although it does not classify every equality case.

## 7. Method outcomes

- **B11 DUALIZE:** the initially planned `f^2=1` convolution system was not the cleanest dual representation. Passing to the `{0,1}` Möbius basis exposed the exact coefficient lattice `2^{1-d}Z`; at `d=3` this bounded the active first-level support by 16 and made a finite exact reduction possible.
- **B14 FIND THE GROUP ACTING:** permutation averaging preserved the objective and converted the remaining finite problem into integer Hamming-layer sums constrained by a zero fourth difference.
- **B24 FIND THE EXTREMAL OBJECT:** three-bit majority supplied the value `3/2`; the exact layer certificate proved no degree-three Boolean function can exceed it.

All three methods contributed to the proof. The checker was written only after the reduction and finite target were recorded in the idea-before-code artifact.

## 8. Scope, source status, and prior-art caution

This result advances only the degree-three case of P0169. The source quantifies over arbitrary degree, so the target remains **PARTIAL / OPEN in this slot**.

A fresh 2026-09-19 GitHub-only repository search for `P0169`, the exact source heading, and `P0169 PROVED` found the existing O'Donnell source metadata, this slot's admission/degree-two work, and neighboring ownership screens, but no repository record of a later complete source-matching solution. The campaign catalog continues to list Jha (`arXiv:1611.01029`) and Wang (`2020/002` in campaign notation) as partial cases/reformulations. Under the owner's GitHub-only restriction, this is only a bounded repository literature check. A search miss is **not** evidence of worldwide novelty, and no novelty claim is made for the degree-three theorem.

## 9. Next mathematical obstruction

The frozen metric is now `D_weak=3`. At degree four, the same granularity lemma gives nonzero first coefficients in `(1/8)Z`, so Parseval alone leaves up to 64 active singleton coordinates. Direct layer enumeration at 64 variables is not attractive.

The next iteration should therefore seek a new compression before any checker. A nonrepeating candidate triple is:

- **B3 PROVE SOMETHING STRONGER:** look for a degree-`d` active-support/linear-mass inequality strong enough to close inductively;
- **B18 SAY IT IN ANOTHER LANGUAGE:** translate first-level mass into the edge boundary / discrete-derivative representation after orienting coefficients;
- **B25 COUNT THE SAME THING TWICE:** exploit the integer Möbius lattice together with Parseval or derivative energy to charge each active first coefficient against higher-degree Fourier mass.

No claim for `d=4` is made here.