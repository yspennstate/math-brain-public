SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-22T20:02:53Z.
attacking: exact regularity/height interface between the full three-large-eigenvalue conjecture and two-large-eigenvalue half-Riesz control, with physical Schur pivots and no conditional spectral-profile normalization.

# account01/B15 — two-eigen half-Riesz is a necessary full-target consequence, and the scalar-Schur bridge is exact

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T200253Z-account01-B15-qform-r13`  
**Live control before publication refresh:** `yspennstate/math-research-brain@899e2f789827509e84bada90cf8053467b641d16`, OWNER CONTROL revision `2026-09-22.15`  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_NECESSARY_FRACTIONAL_POTENTIAL_BRIDGE`  
**Full QFORM:** `OPEN / NOT PROVED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and source-valid premise

The target remains: for every dimension, every vector of independent real coordinates whose one-dimensional densities satisfy `0<=f_i<=1`, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound on the density of `Q=X^T A X`.

This run does **not** use any of the corrected false interfaces: no law-uniform pointwise quadratic Fourier decay, no post-rotation independence, no arbitrary-joint rank-three coarea estimate, no worst scalar-conditioned spectral profile, and no positive moment of a normalized conditional projection density.

The assigned partner `account02/B15` result actually applied is:

- `yspennstate/math-open-problems@42920d321a16b9393856cfb0ed78d8557170ad38`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T170424Z-account02-B15-qform-r5/REPORT.md`.

Its Lemma 2.1 proves that for **every nonzero symmetric matrix** `S` and every admissible product source, `Y^T S Y` is absolutely continuous. I use that exact conclusion below to turn the square-root kernels into ordinary `L^1 * L^1` convolutions, so their essential bounds become genuine pointwise `C_0` bounds. I also use the completed `account02/B15` target-level `C_0` theorem at

- `yspennstate/math-open-problems@28ddaf28bf6779837fb1212a025d8a8b9d329f8a`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T160529Z-account02-B15-qform-r4/REPORT.md`,

to upgrade the physical-pivot density certificate in Section 5 from an essential bound to the maximum of the canonical continuous representative, with no constant loss.

## 2. Sharp constants and the two-large-eigenvalue half-Riesz quantity

Let `C_3` denote the optimal full-target density constant, allowed to be `+infinity`:

`C_3 = sup ||p_(X^T A X)||_infinity`,

where the supremum is over every admissible product source and every real symmetric `A` with `s_3(A)>=1`; here `s_j` denotes decreasing singular values, so for symmetric matrices the condition is exactly three eigenvalues of modulus at least one.

For a nonzero symmetric `S`, write

`R_S=Y^T S Y`,

with independent cap-one coordinates `Y`. Define the half-Riesz height

`H_(1/2)(R_S)=sup_t E |R_S-t|^(-1/2)`.

Define the normalized two-large-eigenvalue constant

`H_2 = sup sqrt(s_2(S)) H_(1/2)(R_S)`,

where the supremum is over all dimensions, all symmetric `S` with `s_2(S)>0`, and all admissible product sources. Equivalently one may restrict to `s_2(S)=1`, by homogeneity.

The main new statement is

> **Theorem 2.1 — `QFORM-FULL-IMPLIES-TWOEIG-HALFRIESZ-v1`.**  
> In the extended nonnegative reals,
> 
> `boxed: H_2 <= 4 C_3 + 1.`
> 
> Thus a universal two-large-eigenvalue half-Riesz bound is not merely a convenient auxiliary route: it is a **necessary consequence** of the full three-large-eigenvalue QFORM theorem.

This is an unconditional logical implication. It does not assert that `C_3` is finite.

## 3. Proof of Theorem 2.1: add one physical square, not a spectral conditioner

It is enough to take `s_2(S)=1`; the scaling is restored in Section 3.4.

Let

`R=Y^T S Y`

with `s_2(S)>=1`. Since `S!=0`, the assigned partner `account02/B15` absolute-continuity theorem gives an ordinary probability density `p_R in L^1(R)`.

Let `U~Uniform[0,1]` be a new independent **physical** coordinate. The density of `U^2` is

`k_+(u) = (1/(2 sqrt(u))) 1_(0,1)(u)`,

and that of `-U^2` is

`k_-(u) = (1/(2 sqrt(-u))) 1_(-1,0)(u)`.

Both kernels belong to `L^1(R)`.

### 3.1 Both augmented matrices lie in the exact owner target

The block-diagonal matrices

`A_+ = diag(1,S)`,
`A_- = diag(-1,S)`

have the extra eigenvalue `+1` or `-1`, respectively, plus at least two eigenvalues of `S` of modulus at least one. Hence each has at least three eigenvalues of modulus at least one.

Therefore, by definition of `C_3`,

`||p_(R+U^2)||_infinity <= C_3`,
`||p_(R-U^2)||_infinity <= C_3`.                                    (3.1)

### 3.2 The local one-sided half-Riesz profiles are exactly square-smoothed target densities

Since `p_R,k_+,k_-` are in `L^1`, their convolutions are continuous and vanish at infinity. Explicitly,

`q_+(t)=(p_R*k_+)(t)`
`      =(1/2) E[(t-R)^(-1/2) 1_{0<t-R<1}]`,                       (3.2)

and

`q_-(t)=(p_R*k_-)(t)`
`      =(1/2) E[(R-t)^(-1/2) 1_{0<R-t<1}]`.                       (3.3)

These are actual density versions of `R+U^2` and `R-U^2`. Since they are continuous, their ordinary suprema equal their essential suprema. Combining with (3.1), for **every** real `t`,

`E[(t-R)^(-1/2) 1_{0<t-R<1}] <= 2 C_3`,                           (3.4)

`E[(R-t)^(-1/2) 1_{0<R-t<1}] <= 2 C_3`.                           (3.5)

This is the exact point where the assigned partner's absolute-continuity theorem matters: it makes the local fractional profiles `L^1*L^1` convolutions, so no exceptional output level can hide outside the essential bound.

### 3.3 The far tail costs only one

Split the full half-Riesz kernel into the two unit neighborhoods and their complement. Since

`|R-t|^(-1/2) <=1` whenever `|R-t|>=1`,

we obtain from (3.4)--(3.5)

`E|R-t|^(-1/2)`
` <= 2 C_3 + 2 C_3 + P(|R-t|>=1)`
` <= 4 C_3 +1`.                                                    (3.6)

Taking `sup_t` proves the normalized claim.

### 3.4 Exact scaling

If `sigma=s_2(S)>0`, put `S_0=S/sigma`. Then

`R_S = sigma R_(S_0)`

and therefore

`H_(1/2)(R_S)=sigma^(-1/2) H_(1/2)(R_(S_0))`.

Thus (3.6) gives

`boxed: H_(1/2)(Y^T S Y) <= (4 C_3+1)/sqrt(s_2(S)).`               (3.7)

Taking the full supremum is Theorem 2.1.

## 4. Why this survives the live conditioning corrections

The current correction ledger contains exact target examples for which

- `sup_b ||p_(Q3|Q'=b)||_infinity=infinity`, and
- even every positive moment of a scalar-conditioned spectral projection height can diverge,

while the true output remains bounded. The proof above never normalizes by a conditional residual-level density and never takes a spectral-fiber profile. It adds one independent original coordinate and reads the **unconditional** output densities of `R+U^2` and `R-U^2`.

Thus the square-root fractional potential is a source-valid object in a much stronger sense than the rejected conditional-profile quantities: if the full QFORM theorem is true, the two-eigenvalue half-Riesz theorem must be true as well, with the explicit sharp-constant implication (3.7).

The implication also explains why the exact-rank-two half-Riesz theorem in the live campaign is structurally relevant rather than cosmetic. What remains nontrivial is extending such control from exact rank two / paid subclasses to **arbitrary-rank** `S` having only the spectral hypothesis `s_2(S)>=1`.

## 5. Reverse physical-pivot bridge: a two-eigen half-Riesz theorem pays a three-eigen target whenever the scalar Schur certificate is quantitative

The necessity above has a converse **at a physical scalar pivot**, but not yet globally.

Let

`A = [[a, r^T],[r,C]]`, `a!=0`,

in an original-coordinate decomposition `X=(X_0,Y)`, and let

`S = C - r r^T/a`                                                   (5.1)

be the scalar Schur complement. Then the exact completion is

`X^T A X = a (X_0 + r^T Y/a)^2 + Y^T S Y`.                         (5.2)

### 5.1 Schur singular-value inheritance

Write

`v=(1,r/a)^T`.

Then

`A = a v v^T + (0 direct_sum S)`.                                  (5.3)

The first term has rank one. The standard singular-value inequality for a rank-one perturbation gives

`s_3(A) <= s_2(0 direct_sum S)=s_2(S)`.                             (5.4)

Hence every nonzero physical scalar pivot of an owner-target matrix satisfies

`boxed: s_2(S)>=s_3(A)>=1.`                                        (5.5)

This is the exact reason a two-large-eigenvalue residual is the natural object after one physical square is completed.

### 5.2 Square kernel bound

Condition on `Y=y`. The translated variable

`Z=X_0+r^T y/a`

has a probability density bounded by one. The density of `a Z^2`, at a nonzero point `u` of the correct sign, is

`[f_Z(sqrt(u/a))+f_Z(-sqrt(u/a))]/(2 sqrt(|a| |u|))`

(with the evident sign convention). Since each numerator term is at most one,

`p_(aZ^2)(u) <= 1/sqrt(|a| |u|)`.                                 (5.6)

Averaging (5.6) over `Y` gives the source-exact essential density estimate

`||p_(X^T A X)||_infinity`
` <= |a|^(-1/2) H_(1/2)(Y^T S Y)`.                                (5.7)

Consequently, if the universal two-eigen half-Riesz constant `H_2` is finite, then

`boxed: ||p_(X^T A X)||_infinity`
`       <= H_2 / sqrt(|a| s_2(S)).`                                (5.8)

This is a precise quantitative certificate. It does not pretend that the spectral hypothesis alone forces `|a|s_2(S)` to be uniformly positive.

### 5.3 Assigned-partner regularity theorem upgrades (5.8) with no loss

The completed assigned-partner `account02/B15` target-level theorem states that every fixed `rank(A)>=3` target output has a density in `C_0(R)`. Therefore in the owner target, (5.8) immediately becomes the pointwise statement for the canonical continuous representative:

`boxed: max_t p_Q(t) <= H_2 / sqrt(|a|s_2(S)).`                    (5.9)

No extra approximation or continuity constant is paid. This is an actual application of the partner theorem to the new inequality, not merely a citation.

## 6. Immediate paid branch from the fresh hollow-residual theorem

A compatible current worker result, `account01/B09` run `B09-20260922T194603Z-r16`, accessible at

`yspennstate/math-open-problems@d002ae7ecff727fcd907c24aa670070577bb318b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/B09-20260922T194603Z-r16/REPORT.md`,

proves the source-valid arbitrary-rank theorem

`S_ii=0 for all i, s_2(S)>=1`
` => H_(1/2)(Y^T S Y + affine)<=128`.                              (6.1)

Scaling (6.1) and inserting it into (5.7) yields the concrete branch

> **Corollary 6.1.** If an owner-target matrix admits a nonzero original-coordinate pivot `a=A_ii` whose scalar Schur complement `S` is hollow, then
> 
> `boxed: max_t p_(X^TAX)(t) <= 128 / sqrt(|a| s_2(S))`
> 
> for the continuous `C_0` representative. In particular, because `s_2(S)>=1`,
> 
> `max_t p_Q(t) <=128/sqrt(|a|)`.

The continuity part is supplied by the assigned `account02/B15` theorem; the numerical height is supplied by the fresh B09 half-Riesz theorem through the exact scalar-square transducer above.

This corollary is not the full conjecture because `a` may be arbitrarily small and the Schur complement need not be hollow. The live correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` specifically forbids replacing 'hollow' by 'merely small diagonal' without a new argument.

## 7. Exact old and new unpaid implications

**Old misleading interfaces now discarded:** trying to bound a worst residual level, or any fixed positive moment of a scalar-conditioned projection density. Exact target counterexamples show those quantities can diverge even when the final output density stays small.

**New source-valid necessary subproblem:** establish the arbitrary-rank two-large-eigenvalue fractional-potential estimate

`boxed: sup_{s_2(S)>=1, product cap-one Y} sup_t E|Y^T S Y-t|^(-1/2) < infinity.`   (7.1)

Theorem 2.1 proves that (7.1) is **necessary** if full QFORM is true. Existing exact-rank-two, diffuse-window, hollow, banked-Schur and aggregate-cross results pay substantial subclasses but not all of (7.1).

Even if (7.1) is proved, the full target still needs an exhaustive structural step for near-zero physical pivots: (5.8) leaves the factor `(|a|s_2(S))^(-1/2)`. Current pair-log, ridge, grouped-coordinate and aggregate-cross mechanisms are precisely the candidate payments for the region where every useful scalar-pivot certificate is small.

Thus the new conditional end-to-end route is:

1. prove (7.1) for every arbitrary-rank two-large residual;
2. use (5.8) wherever a quantitative physical scalar pivot exists;
3. on the complementary near-zero/all-zero physical-pivot region, use a source-valid pair/cross-bank aggregate before inversion;
4. combine the branches without assuming a uniformly good fixed minor or a rank-three physical cross cut.

The full conjecture remains **OPEN** because steps 1 and 3 are not yet globally closed.

## 8. Regularity ledger

The assigned partner work separates the qualitative hierarchy sharply:

- `A!=0` already implies absolute continuity for every admissible product source;
- `rank(A)>=3` implies an individually bounded `C_0` density;
- the owner target is therefore not blocked by existence or continuity of a density;
- the unresolved assertion is the one matrix- and dimension-independent height constant.

Theorem 2.1 adds a quantitative consequence at the exact smoothing threshold between rank two and rank three: a hypothetical universal rank-three height theorem automatically controls the half-Riesz potential of **every** rank-two-or-higher residual having two protected singular values.

This does not use uniform output tails. The assigned partner's no-uniform-tail family shows why all statements above are uniform in the output level `t` rather than restricted to a compact interval.

## 9. Source/correction status

Fresh corrections consumed before publication include the false arbitrary-joint coarea route, false scalar-conditioned supremum and positive-moment routes, false one-heavy-row same-square absorption route, false single-Schur rank-two extraction, false fixed good-minor/cross-rank-three dichotomies, and no independence after spectral rotation.

The report contains no credentials, scheduler IDs, machine paths, external paid computation, public-release action or permission change. Repository synchronization is only file transport; native brain ingestion remains `WITHOUT_VERIFIED_BRAIN`.

**Result classification:** `ESSENTIAL_STEP_APPLIED / EXACT_NECESSARY_FRACTIONAL_POTENTIAL_BRIDGE`.  
**Full target:** `OPEN / NOT PROVED`.
