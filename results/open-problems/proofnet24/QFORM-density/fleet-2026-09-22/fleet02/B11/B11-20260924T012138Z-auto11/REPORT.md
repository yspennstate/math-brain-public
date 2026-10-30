SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-24T01:21:38Z.
attacking: the r46 logarithmic L^m puncture endpoint; identify the determinant-homogeneous exponent that lets a genuine third square remove the log, then isolate exactly why the same-bank square is still unpaid.

# fleet02/B11 — determinant-homogeneous L^3 x L^{3/2} third-square compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `B11-20260924T012138Z-auto11`.
Status: **NEW SUPPORTING THEOREM / TARGET-VALID INDEFINITE SUBCLASS CLOSED / FULL QFORM OPEN**.

The unrestricted owner target remains OPEN / NOT PROVED / NOT DISPROVED. Nothing below assumes moments, bounded support, log-concavity, identical laws, spectral-coordinate independence, or smallness of a quadratic perturbation on unbounded inputs. Continuity is asserted only where it follows from the displayed convolution estimate.

## 1. Inputs actually used

Latest designated partner actually consumed: fleet03/B11 r46,
`yspennstate/math-open-problems@559dcad1a7ad077c7e784bd806602b951926fe28`, theorem `QFORM-PRODUCT-BANK-HYPERBOLIC-LM-v1`.

It says: if `H` is independent of an arbitrary random object `Y`, `||p_H||_infinity<=F`, `U=U(Y)` has marginal density cap `G`, `Psi(Y)` is arbitrary and may depend on the same source as `U`, and

    Z=(b U+d)H+Psi(Y),   b!=0,

then for every integer `m>=2`,

    ||p_Z||_m^m <= m! (2 F G/|b|)^(m-1).                 (1.1)

The full same-bank residual phase is allowed inside `Psi`; only `H` has to be genuinely source-independent.

Required pinned source actually consumed: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. Two completed facts are used at their exact scopes:

1. a normalized one-dimensional linear projection of an independent cap-one product source has density cap at most `sqrt(2)` (the projection-density input recorded in `FOURIER_ROUTE_REPORT.md`); and
2. its ruled-level-set Theorem C gives `p_Q(t)<=pi sqrt(2)/s` on the one-sheet side of an exact rank-three `(2,1)` or `(1,2)` form whose three nonzero eigenvalue magnitudes are at least `s` (`COUNTEREXAMPLE_SEARCH.md`). I do not transfer that ruling bound to the two-sheet side.

## 2. Square L^{3/2} lemma

### Lemma 2.1 — `QFORM-SQUARE-L32-v1`

Let `K` be a real random variable with probability density `f_K` satisfying

    ||f_K||_infinity <= L,

and let `a!=0`. Then `S=a K^2` has a density and

    boxed: ||p_S||_{3/2} <= 2 L^(2/3) |a|^(-1/3).          (2.1)

The same estimate holds for `a(K-r)^2` for any deterministic `r`, since translating `K` does not change its density cap.

#### Proof

It is enough to take `a>0`; reflection handles `a<0`. Put

    h(x)=f_K(x)+f_K(-x),  x>0.

Then `0<=h<=2L` and `int_0^infinity h=1`. For `s=a x^2`, `x>0`,

    p_S(a x^2)=h(x)/(2 a x).

Hence

    int_0^infinity p_S(s)^(3/2) ds
      =(2a)^(-1/2) int_0^infinity h(x)^(3/2) x^(-1/2) dx.  (2.2)

Since `h^(3/2) <= (2L)^(1/2) h`, and among probability densities on `R_+` of cap `2L` the decreasing weight `x^(-1/2)` is maximized by filling `[0,(2L)^(-1)]`,

    int h(x) x^(-1/2) dx <= 2 sqrt(2L).

Therefore the last integral in (2.2) is at most `4L`, so

    ||p_S||_{3/2}^{3/2} <= 2 sqrt(2) L |a|^(-1/2).

Raising to power `2/3` gives (2.1). QED.

This is the exact conjugate exponent needed below. The singular square density is not in `L^2` in general, but it is in `L^{3/2}` uniformly under only the cap assumption.

## 3. Hyperbolic L^3 plus an independent third square

### Theorem 3.1 — `QFORM-HYPERBOLIC-L3-SQUARE-YOUNG-COMPILER-v1`

Assume the hypotheses of partner r46 (1.1). Let `K` be independent of `(H,Y)`, with density cap `L`. For `a!=0`, put

    Q = (b U+d)H + Psi(Y) + a K^2.                         (3.1)

Then `Q` has a bounded continuous density and

    boxed:
    ||p_Q||_infinity
      <= 4 * 3^(1/3) * (F G L)^(2/3)
         * (|b|^2 |a|)^(-1/3).                            (3.2)

#### Proof

Use r46 with `m=3`:

    ||p_Z||_3^3 <= 6 (2FG/|b|)^2,

hence

    ||p_Z||_3 <= 6^(1/3) (2FG/|b|)^(2/3).                 (3.3)

By Lemma 2.1,

    ||p_{aK^2}||_{3/2} <= 2 L^(2/3)|a|^(-1/3).            (3.4)

Because `K` is genuinely source-independent, the law in (3.1) is the convolution of the two displayed laws. For every `t`, Holder (equivalently Young at the conjugate pair `3,3/2`) gives

    p_Q(t)
      <= ||p_Z||_3 ||p_{aK^2}||_{3/2}.

Multiplying (3.3)-(3.4) yields

    2 * 6^(1/3) * 2^(2/3)
      = 4 * 3^(1/3),

which proves (3.2). Since an `L^3` function convolved with an `L^{3/2}` function is a bounded uniformly continuous `C_0` function, continuity holds in this source-disjoint subclass. QED.

### Why `m=3` is the determinant exponent

This is not an arbitrary Holder choice. r46 at exponent `m` costs

    |b|^{-(1-1/m)}.

A square density in the conjugate space `L^{m/(m-1)}` (which requires `m>2`) costs

    |a|^{-1/m}.

The rank-three hyperbolic-plus-square determinant scale is `|b|^2 |a|` (up to the fixed factor coming from the convention `2 kappa HW`). Determinant-homogeneous scaling therefore demands

    1-1/m = 2/3,    1/m = 1/3,

and hence uniquely

    m=3.                                                     (3.5)

Thus the third direction removes the logarithmic endpoint at exactly the `L^3 x L^{3/2}` level. The earlier `L^2` puncture estimate is diagnostically useful but cannot by itself see determinant-homogeneous `L^infinity` regularization.

## 4. A target-valid punctured indefinite family with the full line paid

Let `H,K,Y_1,...,Y_N` be mutually independent original variables with density caps at most one. Let

    T=<t,Y>,   W=<w,Y>,

where `t,w in R^N` are orthonormal. No independence between `T` and `W` is asserted or used. For

    0<q<=1,   kappa>0,   c!=0,

consider

    Q_{q,kappa,c}
      = 2 kappa (sqrt(q) H + sqrt(1-q) T) W + c K^2.       (4.1)

The term

    2 kappa sqrt(1-q) T W

is the exact same-bank puncture: it is retained inside `Psi`, not dropped or conditioned away.

Relative to the global orthonormal linear forms `(H,T,W,K)`, the coefficient matrix is

             [ 0   0   k sqrt(q)       0 ]
             [ 0   0   k sqrt(1-q)     0 ]
    B =      [ k sqrt(q) k sqrt(1-q)  0 0 ] ,              (4.2)
             [ 0   0       0            c ]

and has exact spectrum

    boxed: {+kappa, -kappa, c, 0}.                          (4.3)

Indeed the combinations

    L = sqrt(q) H + sqrt(1-q) T,
    L_perp = -sqrt(1-q) H + sqrt(q) T

are orthonormal, and (4.1) is simply `2 kappa L W + cK^2`, with `L_perp` in the kernel. This spectral statement is deterministic; it does NOT imply probabilistic independence of `(L,W)`.

Hence whenever `kappa>=s` and `|c|>=s`, this is an exact target-valid rank-three form. If `c>0` its nonzero signature is `(+,+,-)`; if `c<0` it is `(+,-,-)`.

The required pinned projection theorem gives

    ||p_W||_infinity <= sqrt(2).                            (4.4)

Apply r46 with

    U=W,
    b=2 kappa sqrt(q),
    d=0,
    Psi(Y)=2 kappa sqrt(1-q) T W,
    F=1,
    G=sqrt(2).

Then

    ||p_{2 kappa (sqrt(q)H+sqrt(1-q)T)W}||_3^3
      <= 12/(kappa^2 q).                                    (4.5)

Since the physical coordinate `K` has density cap one, Lemma 2.1 and Theorem 3.1 give the full-line inequality

    boxed:
    ||p_{Q_{q,kappa,c}}||_infinity
       <= 2 * 12^(1/3) * (kappa^2 q |c|)^(-1/3).            (4.6)

In the live near-coloop range `q>=63/64`, and using `kappa^2|c|>=s^3`,

    boxed:
    ||p_{Q_{q,kappa,c}}||_infinity
       <= 2 * 12^(1/3) * (64/63)^(1/3) / s
       = 4.602956661318305... / s.                          (4.7)

This pays BOTH the one-sheet and two-sheet sides for the source-disjoint-third-square subclass, while preserving the same-bank `TW` puncture exactly.

The required pinned ruled theorem gives the sharper sign-specific one-sheet comparison:

- if `c>0` (`(+,+,-)`), `p_Q(t)<=pi sqrt(2)/s` for `t>=0`;
- if `c<0` (`(+,-,-)`), by negating the form, `p_Q(t)<=pi sqrt(2)/s` for `t<=0`.

I do not extend the ruled/X-ray estimate to the opposite side. The independent-square compiler (4.7), not the ruling, pays that side in this family.

## 5. The rank-two logarithm is retained, and the third direction removes it at conjugate exponents

At the exact endpoint `q=1,c=0`, choose `H,W` to be centered unit uniforms. Then

    R=2 kappa H W

has density

    p_R(t)=|kappa|^(-1) log(|kappa|/(2|t|)),
    0<|t|<|kappa|/2,                                       (5.1)

so the rank-two receiver is genuinely unbounded. Nothing in Theorem 3.1 claims otherwise.

What is finite is precisely the cubic norm supplied by r46. The independent square has a square-root singularity which is precisely in `L^{3/2}`. Convolution at the conjugate exponents kills the logarithmic point singularity and, because the exponents are `2/3` on the hyperbolic scale and `1/3` on the square scale, spends the determinant product `kappa^2 |c|` rather than a weaker non-invariant product such as `kappa|c|`.

This gives a more exact description of the third-direction mechanism than a generic statement that "one more variable smooths the density":

    rank-two log  ->  finite L^3 mass  ->  independent square in L^{3/2}
                  ->  L^infinity with determinant-homogeneous scale.

## 6. What is still unpaid in the actual r45/r46 survivor

The actual partner normal form is

    Q = 2 kappa sqrt(q) H W
        + 2 kappa sqrt(1-q) T W
        + c(V')^2 + delta W^2,                              (6.1)

with `H` independent of the residual original-product bank but `(T,W,V)` an internally dependent orthonormal three-dimensional projection of that SAME bank, and

    kappa^2 |c| = |det M| >= s^3.                           (6.2)

Theorem 3.1 would close (6.1) immediately at the correct determinant scale if the square variable were source-independent of the hyperbolic bank. It is not. Therefore the first unpaid implication is now more sharply formulated than an undifferentiated `L^2 -> L^infinity` upgrade:

    QFORM-R46-SAMEBANK-L3-L32-DETERMINANT-COMPILER-v1.

Prove, for the orthogonal product projection provenance in (6.1), a dependence-safe replacement for the `L^3 x L^{3/2}` convolution step which preserves the determinant homogeneity `(kappa^2|c|)^(-1/3)`, while retaining the `TW` term and arbitrary `delta W^2`; or force a genuinely source-disjoint square / pair-area / volume exit.

A bare joint density cap is not enough: partner r45 already supplied a cap-one joint-box interface falsifier in which an independent scalar plus a square can concentrate in an interval of length `O(epsilon)`. Thus the missing compiler has to use the fact that `(T,W,V)` is an orthogonal projection of an ORIGINAL product source, not merely that it has a bounded three-dimensional density.

The exact exponent calculation (3.5) is the useful new guide: a successful same-bank argument should reproduce an `L^3` hyperbolic resource against an `L^{3/2}` quadratic resource, or an equivalent trilinear estimate with those homogeneities. Paying only the `L^2` resource cannot distinguish the logarithmic rank-two endpoint from the desired bounded regime.

## 7. Scope

Proved here:

- the cap-only square `L^{3/2}` estimate (2.1);
- the source-disjoint `L^3 x L^{3/2}` compiler (3.2);
- a nontrivial target-valid family (4.1), with potentially dependent `T,W`, uniformly bounded on the full line by (4.7);
- exact preservation of the rank-two log endpoint and exact determinant-homogeneous identification of the third-direction smoothing exponent.

Not proved here:

- the same-bank square compiler for the full r45/r46 normal form;
- arbitrary additional nonseparable spectrum;
- the full QFORM target;
- full-target continuity.

No post-rotation independence, hidden moment/support hypothesis, or two-sheet X-ray transfer is used.
