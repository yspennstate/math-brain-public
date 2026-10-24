SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-24T01:28:32Z.
attacking: target-level regularity through a sharp logarithmic-potential estimate for an affine bilinear Schur receiver, then same-constant C0 closure.

# account03/B15 — bilinear logarithmic-potential payment for an indefinite physical pair

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T012832Z-account03-B15-qform-auto30`  
Status: `BILINEAR_LOG_POTENTIAL_PROVED / INDEFINITE_PAIR_NULL-SCHUR-EDGE_IMPROVED / PARTNER_APPLIED / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and current gap

The unrestricted owner theorem remains OPEN. The target is still: for independent real inputs with marginal densities bounded by one and a real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal output-density cap or give a valid counterexample.

This run proves a new positive-kernel lemma for an affine bilinear variable and uses it to improve the completed physical-pair logarithmic envelope in the chamber where the Schur remainder contains an exact zero-diagonal mixed edge. It keeps the original independent coordinates throughout. No rotation is used to preserve independence; no support, moment, log-concavity, connected-support, Gaussian, or smoothness assumption is added.

The new estimate is stronger than the previous square-root small-ball averaging in this exact chamber: a bilinear receiver has an unbounded density at its critical value, but its logarithmic potential is uniformly bounded. Since the physical-pair density envelope itself has only a logarithmic singularity, logarithm against logarithm is integrable with an explicit scale-sharp bound.

Dependencies used at their exact scope:

1. the completed physical-pair logarithmic envelope from account03/B15 auto27, `yspennstate/math-open-problems@2f36eb6204ac8598eaf63faed15f9fa7fddffd0c`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260923T222614Z-account03-B15-qform-auto27/REPORT.md`;
2. the completed designated-partner same-constant regularity compiler from account04/B15 r8, `yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T221909Z-account04-B15-ruled-trace-c0-r8/REPORT.md`.

The current correction set is respected, including the false law-uniform pointwise quadratic decay, the failure of naive fiber-sup integration, loss of independence after spectral rotation, the withdrawn nonzero-square affine-slope rescue from account03/B15 auto26, and the warning that a slope innovation does not absorb an arbitrary same-bank quadratic remainder. The theorem below assumes the exact zero-diagonal Schur mixed edge it actually uses; it does not silently replace an arbitrary remainder by one.

## 2. Uniform logarithmic potential of an affine bilinear variable

### Theorem 2.1 — `QFORM-AFFINE-BILINEAR-LOG-POTENTIAL-v1`

Let `U,V` be independent real random variables with probability densities bounded by one. Let `s!=0` and let `alpha,beta,gamma` be arbitrary real numbers. Define

`T = 2 s U V + alpha U + beta V + gamma`.

For `L>0`, put `q=L/|s|` and define

`Phi(q) = 2 q [2+log(1/(2q))]` for `0<q<=1/2`,

`Phi(q) = 2+log(2q)` for `q>=1/2`.

Then

`boxed( sup_t E log_+( L/|T-t| ) <= Phi(L/|s|). )`                 (2.1)

The bound is uniform in all affine coefficients and in the two input laws. In particular,

`sup_t E log_+( |s|/|T-t| ) <= 2+log 2`.                           (2.2)

No density bound for `T` itself is asserted; its density may have the familiar logarithmic singularity.

### Proof

Translate separately in the original coordinates:

`U'=U+beta/(2s)`, `V'=V+alpha/(2s)`.

The translated variables remain independent and each retains density cap one, while

`T = 2 s U' V' + gamma - alpha beta/(2s)`.

After absorbing the last constant into `t` and dividing the denominator by `|s|`, it is enough to prove that for every `q>0`, every real `theta`, and independent cap-one `U,V`,

`E log_+( q/|2UV-theta| ) <= Phi(q).`                              (2.3)

Condition on `U=u`. For `u!=0`, the variable `Y=2uV` has a probability density bounded by

`c_u=1/(2|u|)`.

Fix `theta`. The kernel

`K(y)=log_+(q/|y-theta|)`

is symmetric decreasing about `theta`. By the one-dimensional bathtub principle, among probability densities bounded by `c_u`, the largest possible integral of `K` is obtained by taking density `c_u` on the centered interval of length `1/c_u=2|u|`. Consequently

`E[K(2uV) | U=u] <= g_q(u)`,                                      (2.4)

where

`g_q(u)=1+log(q/|u|)` if `0<|u|<=q`,

`g_q(u)=q/|u|` if `|u|>=q`.

Indeed, if `|u|<=q`,

`(1/(2|u|)) int_{-|u|}^{|u|} log(q/|w|) dw
 = 1+log(q/|u|)`,

whereas if `|u|>=q`, only `|w|<q` contributes and

`(1/(2|u|)) int_{-q}^{q} log(q/|w|) dw = q/|u|`.

The function `g_q` is symmetric and nonincreasing in `|u|`. A second application of the bathtub principle, now to the cap-one law of `U`, gives

`E g_q(U) <= int_{-1/2}^{1/2} g_q(u) du`.                          (2.5)

If `q>=1/2`, all `|u|<=1/2` lie in the first branch, and direct integration gives

`int_{-1/2}^{1/2} g_q(u) du = 2+log(2q).`                         (2.6)

If `0<q<=1/2`, split at `|u|=q`:

`2 int_0^q [1+log(q/u)] du + 2 int_q^{1/2} q/u du`

`= 4q + 2q log(1/(2q))`

`= 2q[2+log(1/(2q))].`                                            (2.7)

Equations (2.3)-(2.7) prove (2.1). QED.

### Remarks

1. This is a genuine rough-law statement. Arbitrarily fragmented supports are allowed.
2. The exact affine terms disappear only by separate translations of the two ORIGINAL independent coordinates; no spectral rotation is used.
3. The logarithmic potential is the correct object. The bilinear output density itself can diverge logarithmically, so replacing (2.1) by an `L^infinity` density claim would be false.
4. For general marginal caps `M_U,M_V`, the same scaling argument yields the right side `Phi(L M_U M_V/|s|)`.

## 3. Indefinite physical pair with a zero-diagonal Schur mixed edge

Split the original coordinates as `X=(P,Z)` with `P=(X_1,X_2)` and write

`A = [[D,B],[B^T,C]]`,

where the selected physical `2x2` principal block `D` is invertible and indefinite. Define

`Delta=|det D|`,
`kappa=sigma_min(D)`,
`S=C-B^T D^(-1) B`.

Assume that among the remaining ORIGINAL coordinates there are two, call them `U,V`, such that

`S_UU=S_VV=0`, `s:=S_UV!=0`.                                     (3.1)

Every other entry of `S`, every entry of `B`, all affine terms created by conditioning, and all remaining dimensions are arbitrary.

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-BILINEAR-SCHUR-v1`

Under the preceding hypotheses, the full quadratic form `Q=X^T A X` has an essentially bounded density and for every `r>0`,

`boxed(
 ||p_Q||_infinity
 <= 2 sqrt(2)/r
    + Delta^(-1/2) Phi( 2r^2/(kappa |s|) ).
)`                                                                    (3.2)

Equivalently, with `q=2r^2/(kappa|s|)`,

`boxed(
 ||p_Q||_infinity
 <= 4 (kappa|s|)^(-1/2) q^(-1/2)
    + Delta^(-1/2) Phi(q),
 \qquad q>0.
)`                                                                    (3.3)

In particular, the universal explicit choice `q=1/2` gives

`boxed(
 ||p_Q||_infinity
 <= 4 sqrt(2)/sqrt(kappa|s|) + 2/sqrt(Delta).
)`                                                                    (3.4)

If additionally

`kappa |s| <= 8 Delta`,                                              (3.5)

choose

`q_* = 4 Delta/(kappa|s|) >=1/2`.

Then the large-`q` branch of `Phi` and one-variable optimization give the sharper closed form

`boxed(
 ||p_Q||_infinity
 <= [4 + log(8 Delta/(kappa|s|))]/sqrt(Delta).
)`                                                                    (3.6)

### Proof

Complete the square in the original physical pair. Conditional on all remaining coordinates `Z=z`, the two translated pair coordinates stay independent and retain density caps one. The completed pair-log envelope from the cited auto27 source gives, for every `r>0`,

`p_(Q|Z=z)(t)
 <= 2sqrt(2)/r
    + Delta^(-1/2)
      log_+( 2r^2/[kappa |t-R(z)|] ),`                              (3.7)

where

`R(z)=z^T S z + ell^T z + c`                                      (3.8)

for some affine coefficients `ell,c` that are irrelevant below.

Now condition on every coordinate of `Z` except the selected original coordinates `U,V`. By (3.1), the remaining dependence of `R` on `(U,V)` is exactly

`R_W(U,V)=2sUV+alpha_W U+beta_W V+gamma_W`,                        (3.9)

with arbitrary coefficients depending on the conditioned variables `W`. The original variables `U,V` remain independent with density caps one.

Apply Theorem 2.1 conditionally on `W`, with

`L=2r^2/kappa`.

Uniformly in `t` and in all affine coefficients,

`E[ log_+( L/|t-R_W(U,V)| ) | W ]
 <= Phi(L/|s|)
 = Phi(2r^2/(kappa|s|)).`                                         (3.10)

Average (3.7) first over `U,V` and then over `W`. This proves (3.2); (3.3) is the substitution `q=2r^2/(kappa|s|)`.

At `q=1/2`, `Phi(1/2)=2`, giving (3.4).

For `q>=1/2`, the right side of (3.3) equals

`M(q)=4 (kappa|s|)^(-1/2) q^(-1/2)
      + Delta^(-1/2)[2+log(2q)].`                                 (3.11)

Its derivative vanishes at

`sqrt(q)=2 sqrt(Delta)/sqrt(kappa|s|)`,

that is at `q=q_*` above. Condition (3.5) is exactly `q_*>=1/2`. Substitution gives

first term `=2/sqrt(Delta)` and second term
`=[2+log(8Delta/(kappa|s|))]/sqrt(Delta)`,

which proves (3.6). QED.

## 4. Comparison with the previous square-root small-ball branch

Auto27 proved for an arbitrary nonzero Schur remainder the rough bound

`||p_Q||_infinity
 <= 2^(13/4) (Delta kappa eta(S))^(-1/4).`                         (4.1)

Theorem 3.1 is more specialized but sharper in its exact chamber. It uses the full bilinear logarithmic structure instead of degrading it to a square-root small-ball estimate. The key scale ratio is the dimensionless number

`Delta/(kappa|s|)`.

When the zero-diagonal Schur mixed edge is quantitatively comparable to the physical pair, (3.6) has only logarithmic dependence on that ratio and the correct overall degree `-1` under scaling `A -> lambda A`.

This is not a structural extraction theorem. The bare hypothesis `s_3(A)>=1` does not force a paid physical pair satisfying (3.1) with quantitative parameters. Full QFORM therefore remains open.

## 5. Designated partner applied: same-constant continuous regularity

Because the `2x2` Schur principal block on `(U,V)` is

`[[0,s],[s,0]]`,

it is nonsingular. Hence `rank(S)>=2`. Since `D` is nonsingular,

`rank(A)=2+rank(S)>=4`.                                            (5.1)

The estimate (3.2) gives interval domination

`P(Q in I) <= M |I|`                                              (5.2)

with any of the explicit constants `M` in (3.2), (3.4), or (3.6).

Apply the completed designated-partner theorem account04/B15 r8 at this ACTUAL inequality. Its same-constant compiler says that for a fixed cap-one product instance with `rank(A)>=3`, any separately established interval estimate (5.2) yields a canonical density representative in `C_0(R)` with exactly the same height constant.

Therefore

`boxed(
 p_Q in C_0(R),
 ||p_Q||_infinity
 <= inf_{q>0}
    [4(kappa|s|)^(-1/2)q^(-1/2)+Delta^(-1/2)Phi(q)].
)`                                                                    (5.3)

In particular, (3.4) and, under (3.5), (3.6), hold with `p_Q in C_0`.

This cleanly separates the two issues: the logarithmic-potential argument pays essential height first; continuity is added only afterwards and costs no additional constant. No target-uniform modulus of continuity is claimed or possible from the prior B15 obstruction.

## 6. Concrete dense cross-coupled full-target example

Consider the explicit physical block decomposition

`D=[[0,2],[2,0]]`,

`B=[[1,1],[1,-1]]`,

`S=[[0,2],[2,0]]`.

Since

`D^(-1)=[[0,1/2],[1/2,0]]`

and

`B^T D^(-1) B = [[1,0],[0,-1]]`,

set

`C = B^T D^(-1)B + S = [[1,2],[2,-1]]`.

Thus

`A =
 [[0,2,1,1],
  [2,0,1,-1],
  [1,1,1,2],
  [1,-1,2,-1]].`                                                  (6.1)

This is genuinely cross-coupled between the two physical pairs; it is not block diagonal.

A direct determinant calculation gives

`det(lambda I-A)=lambda^4-13 lambda^2+16`.

Hence the four eigenvalues are

`+/- sqrt((13+sqrt(105))/2)`,
`+/- sqrt((13-sqrt(105))/2)`.

Because `sqrt(105)<11`, the smaller squared magnitude satisfies

`(13-sqrt(105))/2 >1`.

Therefore all four eigenvalues of (6.1) have modulus strictly larger than one: this matrix is literally in the owner's target.

Here

`Delta=4`, `kappa=2`, `s=2`,

so `kappa|s|=4<=8Delta`. Formula (3.6) yields

`boxed(
 ||p_Q||_infinity
 <= [4+log 8]/2
 = 2 + (3/2) log 2
 = 3.0397207708399179... .
)`                                                                    (6.2)

The designated partner theorem upgrades this to

`boxed(
 p_Q in C_0(R),
 ||p_Q||_infinity <= 2+(3/2)log 2
)`                                                                    (6.3)

for EVERY four independent real input laws whose densities are bounded by one.

For transparency, the optimizing parameter here is `q_*=4`, equivalently `r^2=8`: the first pair-log term is exactly `1`, while the averaged logarithmic term is `(1/2)[2+log 8]`.

This example is not evidence for the sharp universal constant; it is an exact target-valid chamber showing that dense cross coupling can be paid below `pi` when the Schur geometry is favorable.

## 7. Absolute continuity, boundedness, and continuity kept separate

1. **Absolute continuity.** Any nonconstant quadratic polynomial of an absolutely continuous joint input law has an absolutely continuous pushforward: away from the proper affine critical subspace the map is locally a submersion, while the critical subspace has Lebesgue measure zero. This qualitative fact alone gives no height bound.
2. **Essential boundedness.** Theorem 3.1 proves a numerical `L^infinity` bound before any continuity input.
3. **Continuity.** Account04/B15 r8 is applied only after interval domination has been paid, giving a `C_0` representative with the same constant.
4. **Universal target.** Still OPEN. The spectral hypothesis does not force a physical pair and a zero-diagonal Schur edge with quantitatively nondegenerate `Delta,kappa,s`.

## 8. First unpaid implication after this run

The new exact payment suggests a structural question rather than another regularity question:

`QFORM-PAIR-TO-MIXED-SCHUR-AGGREGATION-v1`:

In the chamber where a nonsingular indefinite physical pair exists but its Schur remainder has no large diagonal entry, can one aggregate original-coordinate banks to force either

- a quantitatively paid zero-diagonal mixed Schur edge to which Theorem 3.1 applies,
- an already-paid grouped determinant / ridge / diffuse branch,
- or a definite/range-aligned endpoint,

without paying the reciprocal of one tiny raw physical minor?

The known cross-rank and Hadamard corrections prohibit asserting such a single-pair extraction directly. Aggregation must occur before reciprocal payment. Theorem 3.1 supplies a sharper endpoint if that aggregation produces an exact or controlled bilinear Schur receiver.

## 9. Provenance and execution status

Initial control commit read: `yspennstate/math-research-brain@04ffbadd3b18fadfb64d4fc35137a3887a2c12a5`; pre-publication control refresh read through `255b11f4cb621638cbfe7bb7470dcfe3ed2338df`. OWNER CONTROL revision remained `2026-09-22.15`, QFORM-only, with no account03/B15 pause.

Changed-file allowlist for the mathematical repository in this run is only this immutable run directory. Manual fallback privacy review found only mathematical formulas, repository pins, run metadata, and no credentials, account secrets, private personal data, or unrelated material. No installation, public release, remote workflow, paid model/API/Codex use, scheduler mutation, notification change, or cross-account authentication was performed.

Repository transport was authenticated, but no authenticated native mathematical-memory receiver ingestion/use occurred. Execution therefore remains `WITHOUT_VERIFIED_BRAIN`.

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning-token and thinking-time counters: `null/not_exposed`.
