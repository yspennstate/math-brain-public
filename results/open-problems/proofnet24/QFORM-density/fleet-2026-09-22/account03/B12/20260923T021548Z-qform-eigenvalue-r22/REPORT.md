SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T02:15:48Z.
attacking: derive a leverage-peeling reduction that converts arbitrary extra large spectrum into a proved terminal volume certificate or an explicit no-pivot obligation, then compile dependent completion through account04/B12 mixed-norm shear.

# account03/B12 r22 — scalar-pivot-chain stability for arbitrary extra spectrum

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Additional eigenvalue control  
**Status:** `PROVED_SUPPORTING_REDUCTION / PARTNER_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and source pins

The target remains the full arbitrary-product-law statement: independent real original-coordinate variables with probability densities at most one, real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, support, log-concavity, Gaussian, identical-law, diagonal-basis, or post-rotation independence hypothesis is introduced below.

This run uses four proved or supplied scoped inputs at their exact scopes:

1. account03/B12 r21, `QFORM-THRESHOLD-PRESERVING-SCHUR-INHERITANCE-v1`, `yspennstate/math-open-problems@dd754a0bfed889fd29c931b7112c8c3285fc83e8:proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T004313Z-qform-eigenvalue-r21/REPORT.md`: an invertible physical `p`-coordinate Schur elimination removes at most `p` eigenvalues beyond any fixed threshold `L`, without reducing that threshold.
2. the determinant-only physical-pair theorem in `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371:proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`: an indefinite original-coordinate `2x2` block of determinant magnitude `D` in a matrix with third singular value at least `s` gives `D^(-1/2)[9.2+log_+(10000 sqrt(D)/s)]`.
3. the newest three-volume/tail theorem, `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md` and `PEER_TAIL_EXTENSION.md`. In particular, for an original-coordinate cross block `M`, a diffuse projection `P` with `max_i P_ii<=1/2`, `T2=sum_{j>=3}s_j(M)^2`, and `||(I-P)M||op<=sqrt(T2)/15`, the ambient density is continuous and

   `||p_Q||inf <= C_tail [s1(M)^2 s2(M)^2 T2]^(-1/6)`,

   where `C_tail=9 sqrt(3) e/2`.
4. the designated partner account04/B12 mixed-norm shear compiler, `yspennstate/math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e:proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260922T192552Z-account04-B12-mixed-shear-r1/REPORT.md`: if the joint density `h(u,z)` obeys `M(h)=int esssup_u h(u,z) dz<=C`, then `U+psi(Z)` has density cap `C` for every measurable `psi`, with no independence assumption between `U` and `Z`.

The live corrections forbidding law-uniform pointwise van der Corput decay, arbitrary-joint rank-three coarea, positive conditional-projection density moments, worst spectral-fiber suprema, and independence after rotation are respected throughout.

## 2. A scalar-square backward compiler

We first isolate the exact step that lets a chain of extra large eigenvalues be removed without multiplying constants.

### Lemma 2.1 — one original-coordinate scalar pivot

Write a real symmetric matrix in one original coordinate as

`H=[[a,b^T],[b,C]]`, with `a!=0`,

and let

`S=C-bb^T/a`

be its physical Schur complement. If the quadratic-plus-affine form in the remaining original coordinates with quadratic matrix `S` has density bounded by `M`, then the full form has density bounded by

`boxed: ||p_Q||inf <=4 sqrt(M/|a|).`                                      (2.1)

All remaining coefficients and all signs are unrestricted.

#### Proof

Condition on the untouched ORIGINAL coordinates `Y`. Since those coordinates remain independent of the pivot variable `X_i`, completing the square gives

`Q=a(X_i+b^T Y/a)^2+R(Y)`

(up to the affine terms, which only alter the displayed translation and the affine part of `R`). For every real translation `m`, the pushforward of a cap-one density by `x -> a(x-m)^2` has density bounded by

`|a|^(-1/2) u^(-1/2) 1_{u>0}`

on the appropriate half-line: the two inverse branches each contribute at most `1/(2 sqrt(|a|u))`.

Therefore, dropping the harmless sign restriction,

`p_Q(t)<=|a|^(-1/2) E |R-t|^(-1/2)`.                          (2.2)

If `||p_R||inf<=M`, then for every `r>0`,

`E|R-t|^(-1/2)
 <= M int_{|u|<=r}|u|^(-1/2)du + r^(-1/2)
 =4M sqrt(r)+r^(-1/2)`.                                      (2.3)

At `r=1/(4M)` the right side is `4 sqrt(M)`. Substitution in (2.2) proves (2.1). No convolution or rotated-coordinate independence is used. QED.

## 3. The nonaccumulating pivot-chain theorem

Normalize at an arbitrary spectral threshold `L>0` and fix `tau>0`.

### Theorem 3.1 — `QFORM-SCALAR-PIVOT-CHAIN-STABILITY-v1`

Suppose a sequence of physical scalar Schur eliminations is performed while

`|a_j|>=tau L`                                                     (3.1)

at every eliminated original coordinate. Assume the final Schur form has a density cap

`B/L`.                                                            (3.2)

Then the form before any number `k` of these eliminations has density cap

`(1/L) B_*^(1-2^(-k)) B^(2^(-k))`,                              (3.3)

where

`B_*=16/tau`.

In particular,

`boxed: ||p_Q||inf <= (1/L) max{B,16/tau},`                       (3.4)

**independently of the number of extra large eigenvalues peeled.**

#### Proof

If the current remainder cap is `B/L`, Lemma 2.1 and (3.1) give the normalized recurrence

`T_tau(B)=4 sqrt(B/tau)=sqrt((16/tau)B)=sqrt(B_* B)`.             (3.5)

Induction gives

`T_tau^k(B)=B_*^(1-2^(-k)) B^(2^(-k))`,                          (3.6)

which lies between `B` and `B_*` on the logarithmic scale and hence is at most their maximum. QED.

The importance of r21 is that this analytic recurrence can be used without losing the spectral scale. At each invertible scalar pivot, r21 gives

`N_abs(S;L)>=N_abs(H;L)-1`.                                      (3.7)

Thus whenever the current matrix has at least four eigenvalues of modulus at least `L`, peeling one scalar pivot still leaves at least three eigenvalues of modulus at least `L`. The smaller spectrum is not discarded and may change arbitrarily under the Schur complement.

## 4. A quantitative two-coordinate exit

The chain need not continue when a quantitative physical pair appears.

### Lemma 4.1 — determinant-one-at-scale exit

Let the current matrix have `s_3(H)>=L` and suppose some original-coordinate `2x2` principal block `B` satisfies

`|det B|>=L^2`.                                                   (4.1)

Then, for arbitrary remaining spectrum/couplings,

`boxed: ||p_Q||inf <= C_pair/L,`

where

`C_pair=9.2+log(10000)=18.410340371976183...`.                   (4.2)

#### Proof

If `B` is indefinite, the determinant-only pair theorem gives, with `D=|det B|`,

`||p_Q||inf <= D^(-1/2)[9.2+log(10000 sqrt(D)/L)]`.              (4.3)

Put `x=sqrt(D)/L>=1`. The normalized right side is

`g(x)=[9.2+log(10000x)]/x`.

Its derivative is

`g'(x)=[1-9.2-log(10000x)]/x^2<0` for `x>=1`,

so (4.3) is maximized at `x=1`, proving (4.2).

If `B` is definite, condition on all other ORIGINAL coordinates and complete the square in the active pair. After the linear map `y=|B|^(1/2)(x-m)`, its two-dimensional joint density is at most `D^(-1/2)`. Coarea on `|y|^2` gives conditional density at most `pi/sqrt(D)<=pi/L<C_pair/L`, uniformly in the conditioned coordinates; averaging proves the claim. QED.

## 5. An exhaustive reduction for extra large eigenvalues

Set `tau=1`. Starting from a matrix with `m=N_abs(A;L)>=3`, repeatedly apply the following deterministic rule:

1. if a physical pair satisfies `|det B|>=L^2`, stop and use Lemma 4.1;
2. if `m>=4` and some physical scalar diagonal satisfies `|a|>=L`, eliminate that original coordinate by Schur completion and continue;
3. otherwise stop.

Every scalar step keeps at least three eigenvalues beyond the same threshold `L` by (3.7). Therefore the terminal matrix is in exactly one of these classes:

- **pair exit:** already bounded by `C_pair/L`;
- **three-large terminal:** exactly three eigenvalues of modulus at least `L`, with every smaller eigenvalue and every coupling retained;
- **high-rank no-pivot terminal:** at least four eigenvalues of modulus at least `L`, while every physical diagonal has modulus `<L` and every physical `2x2` principal determinant has magnitude `<L^2`.

Consequently, if the three-large terminal class admits normalized bound `C_3/L` and the high-rank no-pivot terminal class admits normalized bound `C_NP/L`, then the **entire** class with any number of extra larger eigenvalues satisfies

`boxed: ||p_Q||inf <= (1/L) max{C_3,C_NP,C_pair}.`                (5.1)

Indeed scalar peeling contributes at most `16/L`, and `16<C_pair`.

This does not solve the conjecture, because the terminal classes are not yet universally controlled. What it proves is narrower and directly relevant to this assignment: **extra large eigenvalues do not cause iterative constant blow-up outside the genuine high-rank no-pivot obstruction.** Arbitrary smaller eigenvalues are never dropped or treated as independent noise.

## 6. Matrix-level full-tail terminal exits

The newest volume theorem can now be inserted as a terminal estimate and propagated through an arbitrarily long scalar-pivot chain.

### Theorem 6.1 — near-diffuse full-tail terminal

Suppose that after `k` scalar pivots satisfying `|a_j|>=tau L`, the terminal matrix contains an original-coordinate cross block

`M=M0+E`

such that

`s3(M0)>=aL,   max_i(P_range(M0))_ii<=1/2,   ||E||op<=aL/16`.   (6.1)

Then

`boxed: ||p_Q||inf < (1/L) max{23/a,16/tau}.`                    (6.2)

#### Proof

The cited volume-stability theorem applies to the actual final `M`, not to a random-variable approximation of `E`; it gives the terminal density `<23/(aL)` while retaining all self blocks and outside couplings. Apply Theorem 3.1 backward through the scalar pivots. QED.

### Theorem 6.2 — collective weak-tail terminal

For a terminal original-coordinate cross block `M`, let

`T2=sum_{j>=3}s_j(M)^2`

and suppose there is an orthogonal projection `P` on its row space satisfying

`max_i P_ii<=1/2,  ||(I-P)M||op<=sqrt(T2)/15`.                   (6.3)

Define the matrix-level tail scale

`G=[s1(M)^2 s2(M)^2 T2]^(1/6)`.                                 (6.4)

If `G>=gL`, then

`boxed: ||p_Q||inf <= (1/L) max{C_tail/g,16/tau},`               (6.5)

where

`C_tail=9 sqrt(3)e/2=21.186910062820317...`.

#### Proof

`PEER_TAIL_EXTENSION.md` gives the **continuous** terminal density bound

`C_tail/G <= C_tail/(gL)`                                      (6.6)

while keeping all self blocks, outside couplings and affine terms. Theorem 3.1 then propagates it through the scalar-pivot chain, proving (6.5). QED.

This is the useful additional-eigenvalue point: the terminal certificate may use two individually substantial cross directions plus a **collective tail** `T2`; every individual third-or-later singular value may tend to zero. No “small operator norm implies a small random quadratic perturbation” step appears.

For example, at `tau=g=1`, any length of scalar-pivot chain followed by (6.3)-(6.4) gives

`||p_Q||inf <=21.186911/L`                                      (6.7)

(rounding upward), rather than a constant growing with the number of peeled directions.

## 7. Explicit application of the assigned account04/B12 partner result

The partner theorem supplies a separate terminal compiler that is dependence-safe.

### Theorem 7.1 — mixed-norm terminal plus arbitrary dependent remainder

After any scalar-pivot chain satisfying (3.1), suppose the terminal form can be written using ORIGINAL-coordinate data as

`Q_terminal=U+psi(Z)`,

and the joint density `h(u,z)` of `(U,Z)` satisfies

`M(h)=int esssup_u h(u,z) dz <=B/L`.                             (7.1)

Then the original pre-chain form satisfies

`boxed: ||p_Q||inf <=(1/L) max{B,16/tau}.`                       (7.2)

#### Actual partner inequality

Account04/B12 gives directly, without independence of `U` and `Z`,

`||p_(U+psi(Z))||inf <= M(h) <=B/L`.                             (7.3)

Equation (7.3) is the actual completed partner result consumed here. Apply Theorem 3.1 backward to obtain (7.2).

As a concrete insertion, r21's protected physical-triple argument supplies a fixed-outside mixed norm

`M(h)<=6 sqrt(pi)/(sigma L)`                                    (7.4)

when the terminal form has a final physical `3x3` block with smallest singular value at least `sigma L`. The partner theorem restores **every** outside-only measurable quadratic remainder and all its eigenvalues; then the scalar chain yields

`boxed: ||p_Q||inf <=(1/L) max{6sqrt(pi)/sigma,16/tau}.`         (7.5)

At `sigma=tau=1`, (7.5) is simply

`||p_Q||inf <=16/L`.                                           (7.6)

Thus arbitrary extra spectrum can be divided into two rigorously different kinds: heavy scalar directions are peeled with the nonaccumulating square recurrence, while an arbitrary dependent outside remainder is absorbed only after a finite mixed norm has been paid. No convolution statement is made.

## 8. What changed and what remains unpaid

Compared with B12 r21, this run upgrades a one-step scalar completion into a **closed arbitrary-length recurrence**, and then applies two genuinely matrix-level terminal mechanisms to it:

- the newest collective-tail volume theorem, which can use many individually weak nonseparable directions;
- the assigned account04/B12 mixed-norm shear theorem, which restores an arbitrary dependent outside quadratic remainder after the mixed norm is paid.

The remaining obstruction is now precise. Under the bare three-eigenvalue hypothesis one must still control either

1. a terminal with exactly three eigenvalues beyond the threshold but no paid physical/grouped certificate, or
2. a high-rank terminal with no scalar pivot at scale `L` and no physical pair determinant at scale `L^2`, which also fails the currently available diffuse/collective-tail certificates.

Those are product-geometric no-pivot obligations, not an “extra eigenvalues make constants accumulate” obstruction. The newest N3 programme is therefore compatible with this reduction; this report does **not** prove N3.

## 9. Regularity

The conclusions of Theorems 3.1, 5.1 and 7.1 are essential-`L^infinity` density bounds. The terminal volume theorem in Theorems 6.1-6.2 produces a continuous density at the terminal stage, but the scalar-square backward step above was used only as an `L^infinity` fractional-potential estimate. This report therefore does **not** claim continuity after one or more scalar pivots. The full continuous-density goal remains open separately.

## 10. Status

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** No Gaussianity, moments, compact support, connected support, log-concavity, post-rotation independence, pointwise van der Corput estimate, arbitrary-joint coarea inequality, or worst conditional-fiber bound is used. The result is a quantitative additional-spectrum reduction whose remaining connection to the full target is explicit.
