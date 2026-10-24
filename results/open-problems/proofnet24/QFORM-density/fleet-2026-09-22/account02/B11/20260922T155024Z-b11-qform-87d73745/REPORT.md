# account02/B11 — banked null-pair smoothing for indefinite rank three

Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Run: `20260922T155024Z-b11-qform-87d73745`  
Assignment: Indefinite signatures / complementary constructions and source-valid counterexamples  
Status: `ESSENTIAL_STEP_APPLIED / FULL CONJECTURE OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The sole target remains the full arbitrary-dimensional statement: independent real coordinates with one-dimensional probability densities bounded by one, symmetric `A` with at least three eigenvalues of magnitude at least one, and one universal finite essential bound for the density of `X^T A X`.

The preceding B11 run closed the exact null endpoint with one untouched physical coordinate and left the near-endpoint branch where the heavy spectral coordinate shares residual product variables with the transverse pair. The first unpaid implication was to find a product-preserving mechanism that aggregates a diffuse third direction before paying reciprocal local-minor costs.

This run proves such an aggregation theorem for an exact family with a strong physical saddle pair and an arbitrarily diffuse independent square bank. It also applies the newest assigned-partner theorem to the same family and shows quantitatively why one physical principal triple is the wrong object: every local partner bound may diverge while the banked bound stays universal.

The proof respects the live corrections: it never assumes independence after a spectral rotation, never uses a conditional density cap for conjugate variables, and never claims a deterministic good-principal-triple selector.

## 2. Source-pinned premises actually used

1. **One-dimensional projection cap.** account02/B11 run `20260922T135203Z-b11-qform-6080e0b3`, canonical report `yspennstate/math-open-problems@245a4e2a4414294fbb20b9dd4f292f6b001e5aa2`, proves that if independent `X_i` have densities at most one and `sum_i a_i^2=1`, then `Y=sum_i a_i X_i` has density bounded by `sqrt(e)`.

2. **Parabolic weak-L^{3/2} smoothing.** account02/B11 run `20260922T152031Z-account02-B11-qform-r18-a91c`, canonical report `yspennstate/math-open-problems@e32368258f33ea03369d23721742345e6f22447f`, proves: if `Z` is independent of `(V,W)`, `||p_Z||_infinity<=L`, and `(V,W)` has joint density bounded by `M`, then

`T=2ZW+V^2`

has

`||p_T||_infinity <= 3*2^(4/3)*(LM)^(2/3)`.

This theorem keeps the rank-two logarithmic singularity and pays it through the parabolic weak-`L^{3/2}` level-set estimate.

3. **Assigned partner account03/B11, latest completed r12.** Canonical proof `yspennstate/math-open-problems@117c1568f8f458706c1123327f893efd750053c5`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260922T150842Z-account03-B11-QFORM-r12/REPORT.md`, proves for every invertible symmetric physical `3x3` block `B`, with arbitrary affine term,

`||p||_infinity <= 48*3^(1/4)/sqrt(s_1(B)s_2(B))`,

where `s_1<=s_2<=s_3` are the singular values. Conditioning outside the triple preserves the bound.

The full conjecture remains open in the shared claim state.

## 3. Main theorem — banked null-pair smoothing

### Theorem 3.1

Let `X_0,X_1,X_2,...,X_{m+1}` be independent real random variables with probability densities bounded by one. Let `b_2,...,b_{m+1}` be real coefficients satisfying

`sum_{k=2}^{m+1} b_k^2 = 1`,

and define

`Y = sum_{k=2}^{m+1} b_k X_k`.

For every nonzero real `a,d`, put

`Q = 2 a X_0 X_1 + d Y^2`.

Then `Q` has an essentially bounded density satisfying

`||p_Q||_infinity <= C_bank |a|^(-2/3)|d|^(-1/3)`,                 (3.1)

where

`C_bank = 3*2^(4/3)*e^(1/3) < 10.551`.

In particular, if `|a|>=1` and `|d|>=1`, then `||p_Q||_infinity <10.551`, uniformly in `m`, the coefficients `b_k`, and all admissible input laws.

### Proof

By the source-pinned one-dimensional projection lemma,

`||p_Y||_infinity <= sqrt(e)`.

The bank variables are disjoint from `X_0,X_1`, so `Y` is genuinely independent of `(X_0,X_1)`. If `d<0`, replace `Q` by `-Q`; this leaves the density norm unchanged, so assume `d>0`.

Set

`Z = |a| X_0`,
`W = sgn(a) X_1`,
`V = sqrt(d) Y`.

Then

`Q = 2 Z W + V^2`.

The density of `Z` is bounded by `L=|a|^(-1)`. Since `V` and `W` are independent,

`||p_(V,W)||_infinity
 <= ||p_V||_infinity ||p_W||_infinity
 <= sqrt(e) d^(-1/2) =: M`.

Apply the parabolic weak-`L^{3/2}` theorem:

`||p_Q||_infinity
 <= 3*2^(4/3) [sqrt(e)/( |a| sqrt(d) )]^(2/3)
 = 3*2^(4/3)e^(1/3)|a|^(-2/3)d^(-1/3).`

Reflection handles `d<0`. This proves (3.1). QED.

## 4. Exact rank-three frame realization

Let

`n_+ = (1,0,1)/sqrt(2)`,
`n_- = (1,0,-1)/sqrt(2)`,

and form an `(m+2) x 3` matrix `R` whose first two rows are `n_+,n_-` and whose bank rows are

`r_k=(0,b_k,0)`, `k=2,...,m+1`.

Because `sum b_k^2=1`,

`R^T R = I_3`.

Take

`Lambda = diag(a,d,-a)`

and `A=R Lambda R^T`. The nonzero eigenvalues of `A` are exactly `{a,d,-a}`. Moreover

`(R^T X)_1=(X_0+X_1)/sqrt(2)`,
`(R^T X)_3=(X_0-X_1)/sqrt(2)`,
`(R^T X)_2=Y`,

so

`X^T A X = 2aX_0X_1+dY^2`.

Thus for `a,d>0` this is a genuinely indefinite signature `(+,+,-)` with a physical null pair rather than a diagonal form; negating `A` gives `(+,-,-)`. When `|a|,|d|>=1`, the family lies exactly inside the owner's three-large-eigenvalue target.

## 5. How the third direction removes the opposite-sign logarithm

If the bank square is deleted, the remaining law is `2aX_0X_1`. For centered uniform inputs the product density has the standard logarithmic divergence at zero, so rank two remains genuinely singular.

The square bank is not replaced by a bounded-density summand: `Y^2` itself has the inverse-square-root singularity typical of a square. Instead, the previous weak-`L^{3/2}` theorem treats the exact parabolic kernel

`2ZW+V^2`.

The product saddle alone has the reciprocal kernel responsible for one logarithm. The third direction bends its level sets into parabolas, whose kernel has distribution tail `lambda^(-3/2)`. The linear bank supplies a bounded one-dimensional projection density before squaring. The resulting layer-cake integral is finite. This is the precise dimension gain: the third direction changes a scale-by-scale constant saddle contribution into a summable half-order gain.

## 6. Assigned-partner theorem applied: local triples can all be bad

For each bank coordinate `k`, the physical principal triple `I_k={0,1,k}` has block

`B_k = [[0,a,0],[a,0,0],[0,0,d b_k^2]].`                    (6.1)

This is invertible whenever `b_k!=0`, so the newest assigned-partner theorem applies after conditioning on every other coordinate.

For the normalized target family `a=d=1`, the singular values of `B_k` are

`{|b_k|^2,1,1}`.

Hence the partner theorem gives the valid local bound

`||p_Q||_infinity <= 48*3^(1/4)/|b_k|`.                    (6.2)

Now take the equal bank `b_k=1/sqrt(m)`. Every local partner bound (6.2) is then of order `sqrt(m)` and diverges, while Theorem 3.1 gives the dimension-free global bound

`||p_Q||_infinity <= C_bank <10.551`.

Equivalently, `det B_k=-1/m` tends to zero for every physical principal triple even though the aggregated third direction remains perfectly normalized.

This is a rigorous counterexample to the proof mechanism

`strong physical saddle pair -> choose one bank coordinate -> apply one local 3x3 theorem`.

It is not a counterexample to QFORM. It shows that the third direction must be aggregated as a bank before reciprocal local determinant costs are paid.

## 7. Relation to the near-endpoint heavy-row debt

The preceding null-heavy run left `1/2<=c<1`, a non-diffuse whitened residual frame, and no dimension-free local triple scale. The theorem above proves that **if** a product-preserving reduction exposes a strong two-coordinate saddle pair and moves the remaining positive direction into an independent normalized linear bank, then the entire branch is uniformly controlled without choosing a bank coordinate.

The remaining obstacle is therefore narrower than 'find a third coordinate':

**BANK-SEPARATION IMPLICATION.** In an arbitrary near-null heavy exact-rank-three frame, prove a dimension-free decomposition that either

1. exposes an independent normalized square bank after a strong physical saddle pair, allowing Theorem 3.1;
2. enters an already-proved diffuse residual branch;
3. produces a physical principal triple with a dimension-free partner scale;

or else construct a genuine target-level counterexample.

The live conditional-cap corrections show why this is nontrivial: the arbitrary residual first-spectral projection may share the same original coordinates as the square and saddle factors, and that dependence cannot be replaced by a false rotated conditional-density bound.

Extra nonzero spectrum outside the exact-rank-three chamber remains a separate nonseparable debt.

## 8. Exact computation used

A symbolic check at `m=16`, `a=d=1`, equal bank coefficients `b_k=1/4`, verifies

- `R^T R=I_3`;
- nonzero spectrum `{-1,1,1}`;
- each representative triple block is `[[0,1,0],[1,0,0],[0,0,1/16]]`;
- its determinant is `-1/16` and singular values are `{1/16,1,1}`;
- `C_bank=10.550168831164775...` while the partner local estimate is `252.68621048687854...`.

The checker terminates `QFORM_BANKED_NULL_PAIR_CHECK_PASS`. This is algebraic regression only; the theorem is proved symbolically above.

## 9. Status

`ESSENTIAL_STEP_APPLIED` in an arbitrary-size genuinely indefinite rank-three family. The result is an aggregation theorem and a source-valid falsifier of one-local-triple assembly. It does not close the arbitrary near-endpoint dependent residual and does not solve the full arbitrary-spectrum conjecture. No continuity claim is made beyond existence of an essentially bounded density in the proved family.
