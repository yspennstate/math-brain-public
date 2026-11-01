# E0024 - Hunt's hypothesis (H) for a product of two independent Levy processes

Ledger id E0024. Source: Hu and Sun, "Hunt's Hypothesis (H) for Markov Processes: Survey and Beyond",
arXiv 1908.06825 (Acta Math. Sinica, Engl. Ser., 2021). Locator: Question 4 (p. 15), Question 4' (p. 18),
Section 5 (p. 25). Written 2026-09-09.

## 1. The problem as the source states it

Section 3.2, page 15 (X is a Levy process on R^n, n > 1, with exponent (a, Q, mu)):

> Question 4. Let S be a nonempty proper subspace of R^n. Assume that the two projection processes
> X_S and X_{S^perp} of X on S and S^perp, respectively, are independent and satisfy (H). Does X
> satisfy (H)?

Section 3.2.4, page 18:

> By the orthogonal transformation of Levy processes, we find that Question 4 is equivalent to the
> following question:
> Question 4'. Let X_1 and X_2 be Levy processes on R^n and R^m, respectively. Suppose that X_1 and
> X_2 are independent and both of them satisfy (H). Does the R^{n+m}-valued Levy process X = (X_1, X_2)
> satisfy (H)?

Section 5, page 25: "Besides Questions 1, 2, and 4 (equivalently, 4') given in Section 3.2, we would like
to present a few more questions", and Remark 5.1(ii): "if the answer to Question 4 is yes, then the answer
to Question 7 [(H) for X + Y, X and Y independent] is also yes."

(H) means: every semipolar set is polar. The survey's own partial answers are Proposition 3.9 (X_1 satisfies
(H), X_2 compound Poisson) and Proposition 3.10 (both satisfy the solution condition (S)), plus Proposition 4.8
(X satisfies (H), Y satisfies the Kanda-Forst condition, and the energy limit vanishes for measures of the
product form eta x xi). The ledger row transcribes the question correctly; nothing is misstated.

Notation, as in the survey. psi is the exponent, E exp(i<z,X_t>) = exp(-t psi(z)); Re psi >= 0 always.
For a finite measure nu on R^N and lambda > 0 the lambda-energy is

    E^lambda_X(nu) = int Re([lambda + psi(z)]^{-1}) |nu-hat(z)|^2 dz
                   = int (lambda + Re psi) / ((lambda + Re psi)^2 + (Im psi)^2) |nu-hat|^2 dz,

"finite 1-energy" is E^1_X(nu) < infinity, and the survey's Theorem 4.2 ([24, Theorem 5.1]) says: if X has
resolvent densities with respect to Lebesgue measure, then X satisfies (H) if and only if
lim_{lambda -> infinity} E^lambda_X(nu) = 0 for every finite measure nu of finite 1-energy.
The Kanda-Forst condition for Y with exponent Psi is |Im Psi| <= c (1 + Re Psi) for some constant c.
Y^s denotes the symmetric Levy process with exponent Re Psi (the law of Y_{t/2} - Y'_{t/2}, Y' an
independent copy).

## 2. Finding

The question is not settled here. What is new is a reduction that removes the imaginary part of one factor
whenever that factor is in the Kanda-Forst class.

Theorem A. Let X on R^n and Y on R^m be independent Levy processes, Y satisfying the Kanda-Forst
condition with constant c, and suppose Z = (X, Y) and Z^s = (X, Y^s) both have resolvent densities with
respect to Lebesgue measure on R^{n+m} (this holds, for instance, when X and Y have transition densities
for every t > 0). Then

    Z satisfies (H)   if and only if   Z^s satisfies (H).

No assumption is made on X beyond the density hypothesis. In particular Question 4' for pairs (X, Y) with Y
in the Kanda-Forst class is equivalent to Question 4' for pairs (X, Y^s) with Y^s symmetric.

The same argument gives a statement with no product structure at all:

Lemma B (Kanda-Forst perturbation of the imaginary part). Let Z and Z' be Levy processes on R^N with
resolvent densities and exponents psi, psi' such that Re psi = Re psi' and |Im psi - Im psi'| <= c (1 + Re psi).
Then Z satisfies (H) if and only if Z' does; moreover a finite measure has finite 1-energy for Z if and only if
it has finite 1-energy for Z'.

Theorem A is Lemma B applied to psi(x, y) = Phi(x) + Psi(y) and psi'(x, y) = Phi(x) + Re Psi(y), whose
difference is i Im Psi(y), bounded by c (1 + Re Psi(y)) <= c (1 + Re psi(x, y)).

What Theorem A does and does not give. Together with the survey's Proposition 3.10 and the ledger's attempt
A001 (Rao's class is product-stable) it covers every pair in which X is also Kanda-Forst, since then Z^s is
comparable, by Lemma B again, to the fully symmetric process (X^s, Y^s), and symmetric Levy processes with
resolvent densities satisfy (H). It does not decide the case that matters for Getoor's conjecture, X outside
Rao's class; it only shows that for such X the question with a Kanda-Forst partner Y is the same question
as with a symmetric partner. Section 4 records exactly where an attempt at that case stops.

## 3. Proof

Step 1 (the algebraic comparison). Fix lambda >= 1 and write, for (x, y) in R^{n+m},

    a = lambda + Re Phi(x) + Re Psi(y) > 0,   b = Im Phi(x),   d = Im Psi(y).

Kanda-Forst for Y gives |d| <= c (1 + Re Psi(y)) <= c a, because Re Phi >= 0 and lambda >= 1. Hence d^2 <= c^2 a^2.
For any reals a, b, d, c with d^2 <= c^2 a^2,

    a^2 + b^2       <= 2 (1 + c^2) (a^2 + (b + d)^2),
    a^2 + (b + d)^2 <= 2 (1 + c^2) (a^2 + b^2).

The first follows from the identity
2(1+c^2)(a^2 + (b+d)^2) - (a^2 + b^2) = (b + 2d)^2 + 2(c^2 a^2 - d^2) + a^2 + 2 c^2 (b+d)^2,
whose right side is a sum of nonnegative terms; the second is the same identity with (b, d) replaced by
(b + d, -d). Both are certified in Lean (file U_E0024.lean, theorem E0024_kf_denominator_comparison) and
checked on 200,000 random quadruples (check_kf_comparison.py). Dividing, with K = 2(1+c^2),

    (1/K) a/(a^2 + b^2) <= a/(a^2 + (b+d)^2) <= K a/(a^2 + b^2)          (*)

(theorem E0024_kf_integrand_comparison in the same file). The middle term is Re([lambda + psi_Z(x,y)]^{-1})
and the outer term is Re([lambda + psi_{Z^s}(x,y)]^{-1}), since psi_Z = Phi(x) + Psi(y) and
psi_{Z^s} = Phi(x) + Re Psi(y) (survey, (3.8)).

Step 2 (energies). Multiply (*) by |nu-hat(x,y)|^2 >= 0 and integrate: for every finite measure nu on R^{n+m}
and every lambda >= 1,

    (1/K) E^lambda_{Z^s}(nu) <= E^lambda_Z(nu) <= K E^lambda_{Z^s}(nu).

With lambda = 1 this says nu has finite 1-energy for Z iff it has finite 1-energy for Z^s. For such nu,
lim_lambda E^lambda_Z(nu) = 0 iff lim_lambda E^lambda_{Z^s}(nu) = 0 (both limits exist by Rao's theorem,
survey Theorem 2.4, once the processes have resolvent densities; the two-sided bound transfers the value zero
either way, and would transfer the property "the limit is zero" even without existence of the limits).

Step 3 (Theorem 4.2). Z and Z^s have resolvent densities by hypothesis, so the survey's Theorem 4.2 applies to
each: Z satisfies (H) iff lim E^lambda_Z(nu) = 0 for every finite nu of finite 1-energy, and likewise for Z^s.
By Step 2 the two conditions are the same condition. This proves Theorem A. Lemma B is the same three steps
with d = Im psi' - Im psi in place of Im Psi(y).

Remark on the density hypothesis. If X and Y have transition densities p^X_t, p^Y_t for all t > 0, then Z has
the density p^X_t(u) p^Y_t(v), Y^s has the density p^Y_{t/2} convolved with the reflection of p^Y_{t/2}, and
Z^s has the product density; the resolvent densities are the e^{-lambda t}-integrals of these. Compound
Poisson Y is Kanda-Forst but has no density, which is why Proposition 3.9 of the survey is a separate (and
easier) case.

## 4. What is not done, and where the general case stops

(a) The symmetric-partner case. After Theorem A the open case with a Kanda-Forst partner is
Z^s = (X, Y^s) with Y^s symmetric (exponent Psi >= 0 real). Writing nu_y(du) = int e^{i<y,v>} nu(du, dv) for the
complex measure obtained by a partial Fourier transform, one has exactly

    E^lambda_{Z^s}(nu) = int_{R^m} g_lambda(y) dy,   g_lambda(y) = E^{lambda + Psi(y)}_X(nu_y),

so the question is whether int g_lambda dy -> 0 given int g_1 dy < infinity and (H) for X. Two facts are
available and neither closes it:

  - Pointwise, g_lambda(y) -> 0, uniformly in y. Each of the four Jordan parts of nu_y (the u-marginals of
    cos^{+-}(<y,v>) nu and sin^{+-}(<y,v>) nu) is dominated by the u-marginal nu_1 of nu, which has finite
    X-energy by the survey's Proposition 4.5 (compact support); Kanda's monotonicity of energy under
    domination and (H) for X (Theorem 4.2) then give g_lambda(y) <= 16 E^lambda_X(nu_1) -> 0.
  - The energy at a higher level is controlled by the level ratio: for any complex measure sigma and
    1 <= mu <= mu', E^{mu'}_X(sigma) <= (mu'/mu) E^mu_X(sigma), because a'/(a'^2+b^2) <= (a'/a) a/(a^2+b^2)
    for a' >= a. Hence g_lambda(y) <= 2 g_1(y) on {Psi(y) >= lambda}.

The two bounds do not combine into an integrable majorant on {Psi(y) < lambda}: the Jordan bound throws away
the cancellation that makes nu_y small for large |y| (its positive parts are of size nu_1, not small), and
the level-ratio bound costs a factor up to lambda. Without a rate in the convergence E^lambda_X(nu_1) -> 0,
which (H) does not provide, dominated convergence fails. This is the same obstruction as in the ledger's
attempt A001, now located precisely: it is the non-monotonicity in lambda of a/(a^2+b^2) on the region
|Im Phi(x)| > lambda + Re Phi(x), which is empty exactly for X in the Kanda-Forst class. The survey's
Proposition 4.8 avoids it by assuming product form, where nu_y = xi-hat(y) eta is a scalar multiple of a
positive measure.

(b) A counterexample search that did not produce one. For Z = (B, S), B a Brownian motion on R and S an
independent stable subordinator of index beta in (0,1) (both satisfy (H); S is Kanda-Forst, so Theorem A
already covers this pair; the search was done before that was noticed and is kept as a record), the natural
candidate for a thin non-polar set is a graph D = {(g(y), y) : y in E} with E hit by S and g pushing the fibre
away faster than B can follow: |g(y) - g(y_0)| >= |y - y_0|^kappa with kappa < beta/2 makes every point of D
irregular for D (lower LIL for S, upper LIL for B). But an anti-Holder map of exponent kappa from E into R
forces dim E <= kappa, while non-polarity of D for Z needs, by a Taylor-Watson parabolic-dimension count on the
space-time set {(S^{-1}(y), g(y)) : y in E cap range(S)}, dim E + beta - 1 > kappa. The two requirements are
incompatible by the margin 1 - beta, which is the drift-free part of S; at beta = 1 (uniform motion, which
fails (H)) the margin closes. Fibres of positive dimension do not change the count. So the one-sided mechanism
that breaks (H) for uniform motion does not survive replacement of the uniform motion by a drift-free
subordinator, at least in this family. This is heuristic and is not a proof of anything.

(c) The genuinely open case after this memo: X outside the Kanda-Forst class but satisfying (H) (the survey's
Theorems 2.8, 2.11, 2.12, 2.18, 2.19 supply such X), paired with any Y that satisfies (H), including symmetric Y.

## 5. Checks

  - Lean 4 (Mathlib): U_E0024.lean compiled clean on the first attempt; #print axioms gives
    [propext, Classical.choice, Quot.sound] for both theorems. It certifies the two-sided denominator
    inequality and the integrand comparison (*).
  - check_kf_comparison.py, lane 1: 200,000 random (a, b, d, c) with |d| <= c a, heavy-tailed b; the ratio
    mid/lower was always >= 1 (min 1.50) and mid/upper always <= 1 (max 0.66).
  - check_kf_comparison.py, lane 2 (independent of the algebra): X a totally asymmetric 1.5-stable process on R,
    Y a spectrally positive 0.7-stable process (Kanda-Forst constant c = tan(0.35 pi) = 1.963, band
    [0.103, 9.70]); nu = three point masses plus a Gaussian bump in R^2; the integrands Re([lambda + psi]^{-1})
    were evaluated directly on a 4001 x 4001 grid on [-400, 400]^2. Pointwise ratio range of the Z and Z^s
    integrands: [0.211, 1.472] at lambda = 1, [0.256, 1.439] at 10, [0.613, 1.257] at 100, [0.948, 1.049] at 1000;
    energy ratios 0.709, 0.771, 0.936, 0.998. All inside the band, and the drift toward 1 as lambda grows is
    what the bound predicts (d/a -> 0).
  - The strongest case that Theorem A is wrong: that Theorem 4.2 is being misapplied. Its hypothesis is
    "resolvent densities with respect to m_n" and its statement quantifies over all finite measures of finite
    1-energy with the survey's own definition of energy, which is the integrand compared in (*). The comparison
    is pointwise in z and uniform in lambda >= 1, so nothing about nu is used. The remaining exposure is the
    density hypothesis on Z^s, which is stated as a hypothesis, not derived.

## 6. Prior art

Searched 2026-09-09: "Hunt's hypothesis" with product / independent Levy processes / (X_1, X_2); Hu and Sun
with years 2021-2025; "Getoor's conjecture" and "semipolar" on arXiv (the full arxiv.org listing for the phrase
"Hunt's hypothesis" has nine entries, the only one after the survey being Li, arXiv 2107.06163, on
symmetrization for one-dimensional diffusions, unrelated to products); Semantic Scholar's list of papers citing
arXiv 1908.06825 (three: Chen-Wang 2023 and 2026 on boundary Harnack principles, Zhang-Hu-Sun 2023 on measure
concentration, none on Question 4). The published version (Acta Math. Sinica, Engl. Ser., 2021, doi
10.1007/s10114-021-9343-7) carries the same questions. No resolution of Question 4 / 4' was found. Related
earlier results are the survey's own Propositions 3.9, 3.10, 4.5-4.8 and Hu-Sun's Theorem 2.16 (arXiv
1702.07396) on sums, which needs an energy-comparison hypothesis that the product structure makes automatic
(equal real parts) in Lemma B. Rao's class being product-stable is the ledger's attempt E0024-A001.

Files: memo.md, U_E0024.lean, check_kf_comparison.py, source_text.txt (pypdf extraction of the source),
prior_art_arxiv.txt (empty: the arXiv API rate-limited this machine; the listing above came from the
arxiv.org search page and Semantic Scholar instead).
