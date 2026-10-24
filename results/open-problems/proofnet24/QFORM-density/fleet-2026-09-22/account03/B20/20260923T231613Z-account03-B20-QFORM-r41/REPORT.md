SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-23T23:16:13Z.

attacking: the principal-minimal retained-error rank-six carrier. The immediate goal is to remove the spectral-gap ambiguity at the untouched L-bank threshold by an exact inertia identity, including eigenvalues exactly equal to +1 or -1, and then splice the identity into the live r39 collar without dropping its nonzero coefficient error.

# account03/B20 r41 — exact threshold-Schur compiler and principal-minimal deletion essentiality

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: proof closure and keeper / SYNTHESIS  
Status: **NEW TARGET-LEVEL STRUCTURAL IMPLICATION / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Continuity: **OPEN for the full target.** This run is deterministic spectral/structural mathematics plus a scoped partner application; it does not claim a new continuity theorem for the surviving carrier.

## 1. Fresh proof boundary

The target remains exactly the owner statement: independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussianity, log-concavity, moments, compact support, connected support, iid hypothesis, diagonal-basis independence, or post-rotation independence is introduced.

The two immediate assembly inputs are:

1. account03/B20 r39, `yspennstate/math-open-problems@5d9892edb6f33beda5ce5e10c4482fcc5fe994a8`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T214857Z-account03-B20-QFORM-r39/REPORT.md`;
2. account03/B19 r43, `yspennstate/math-open-problems@ef38106705da5fab5a2fb6dbdd64745206580f62`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T220120Z-account03-B19-QFORM-r43/REPORT.md`.

The latter proves the same-constant reduction to the affine **principal-minimal** class. Thus it is enough to treat matrices for which the full matrix has at least three threshold-large eigenvalues but every proper ORIGINAL-coordinate principal submatrix has at most two. It also proves that a principal-minimal target has exactly three threshold-large eigenvalues, or exactly four with mixed signs.

On the live r39 finite-core branch there is an ORIGINAL-coordinate partition `H disjoint_union L`, with `|H|<=124`, and

```
B:=A[H,H] = L_H + E_H,
rank(L_H)<=2,
||E_H||_op < epsilon_H := (3+122 sqrt(10)) 2^(-20)
                         = 0.0003707865472226546...,

C:=A[H,L] = C_2 + R_C,
rank(C_2)<=2,
||R_C||_op < rho := 1/64,

D:=A[L,L].
```

After the r43 principal-minimal descent, the untouched base satisfies

`N_D(1):=#{lambda(D): |lambda|>=1} <=2`.                         (1.1)

The missing implication was to use (1.1) without dividing by the distance of the remaining spectrum from `+1` or `-1`. The latest global assembly explicitly warns that a proof demanding a fixed base gap is not valid. The theorem below therefore keeps exact threshold eigenspaces and produces a dichotomy: a genuine near-threshold annulus, or a finite strong threshold carrier.

The earlier account03/B12 threshold-preserving Schur theorem (`yspennstate/math-open-problems@dd754a0bfed889fd29c931b7112c8c3285fc83e8`) proves a useful lower bound on threshold counts after an invertible physical pivot. The new theorem here is different: it is an **exact count formula across an arbitrary possibly singular untouched base block**, including exact `+1` and `-1` eigenvalues and their couplings to the finite H-bank.

## 2. Singular saddle inertia lemma

For a real symmetric matrix `M`, write `n_+(M), n_-(M), n_0(M)` for its positive, negative and zero inertia indices, and `n_ge0(M)=n_+(M)+n_0(M)`.

### Lemma 2.1 — singular Schur/saddle inertia

Let

```
M = [ S0   G
      G^T  D0 ]
```

with `D0=D0^T` possibly singular. Put

```
K = ker D0,
P_K = orthogonal projection onto K,
R = D0^dagger,
S = S0 - G R G^T,
G0 = G P_K,
r = rank(G0),
N = ker(G0^T) subset of the first-coordinate space.
```

Then

```
n_+(M) = n_+(D0|_{K^perp}) + r + n_+(S|_N),
n_-(M) = n_-(D0|_{K^perp}) + r + n_-(S|_N),
n_0(M) = (dim K-r) + n_0(S|_N).                         (2.1)
```

Here `S|_N` means the quadratic form obtained by restricting `S` to `N`.

#### Proof

Orthogonally decompose the second-coordinate space as `K^perp direct_sum K`. On `K^perp`, `D0` is invertible. An exact congruence eliminating that invertible block changes `M` into the orthogonal sum of `D0|_{K^perp}` and

```
J = [ S   G0
      G0^T  0_K ].
```

Choose orthogonal decompositions of the first space and `K` so that `G0` has SVD form `diag(Sigma,0)`, where `Sigma` is invertible `r x r`. Thus the first space is `U direct_sum N`, `dim U=r`, and `K=K1 direct_sum K0`, `dim K1=r`. In the order `U,N,K1,K0`, the quadratic form of `J` is

```
u^T S11 u + 2 u^T S12 n + n^T S22 n + 2 u^T Sigma k,
```

with `K0` absent. Since `Sigma` is invertible, the change

```
k' = k + (1/2) Sigma^(-1) S11 u + Sigma^(-1) S12 n
```

is an invertible congruence and removes both the `u-u` and `u-n` terms. Hence `J` is congruent to a direct sum of the `r` hyperbolic planes

`[[0,Sigma],[Sigma,0]]`,

the restricted form `S22=S|_N`, and a zero block of dimension `dim K-r`. Each hyperbolic plane contributes one positive and one negative direction. This proves (2.1). QED.

The point of keeping the kernel block is important: an exact threshold eigenvector of the base does not create a divergent inverse. Its coupling to `H` instead appears as a hyperbolic pair through `G0`, and only the orthogonal complement `N=ker G0^T` reaches the threshold Schur form.

## 3. Exact threshold-Schur count at +1 and -1

Partition the full coefficient matrix in ORIGINAL coordinates as

```
A = [ B   C
      C^T D ],
```

with the first bank `H` and second bank `L`. For `sigma in {+1,-1}`, define

```
N_sigma(A) := #{lambda(A): sigma lambda(A) >= 1},
K_sigma := ker(D-sigma I),
P_sigma := projection onto K_sigma,
R_sigma := (D-sigma I)^dagger,
Nspace_sigma := ker(P_sigma C^T) subset R^H,
S_sigma := -I_H + sigma ( B - C R_sigma C^T ),
T_sigma := S_sigma restricted to Nspace_sigma,
q_sigma := n_ge0(T_sigma).
```

### Theorem 3.1 — `QFORM-EXACT-THRESHOLD-SCHUR-COUNT-v1`

For both signs, with no spectral-gap hypothesis,

```
boxed: N_sigma(A) = N_sigma(D) + q_sigma.                       (3.1)
```

Consequently

```
boxed: N_A(1) = N_D(1) + q_+ + q_-.                            (3.2)
```

This remains exact if `D` has eigenvalues equal to `+1` or `-1`, with arbitrary multiplicity and arbitrary coupling `C`.

#### Proof

Apply Lemma 2.1 to

`M_sigma := sigma A - I`.

Its lower-right block is

`D0 = sigma D-I = sigma(D-sigma I)`.

Therefore `ker D0=K_sigma` and

`D0^dagger = sigma R_sigma`.

The cross block is `G=sigma C`. Hence the singular Schur form from Lemma 2.1 is exactly

```
sigma B-I - (sigma C)(sigma R_sigma)(sigma C^T)
= -I + sigma(B-C R_sigma C^T)
= S_sigma,
```

and its kernel-compatible first-space restriction is precisely `T_sigma`, because

`ker((sigma C P_sigma)^T)=ker(P_sigma C^T)=Nspace_sigma`.

The nonnegative eigenvalues of `M_sigma` are exactly the eigenvalues of `A` satisfying `sigma lambda>=1`. Lemma 2.1 gives

```
n_ge0(M_sigma)
 = n_+(D0|_{K_sigma^perp}) + dim K_sigma + n_ge0(T_sigma).
```

The first two terms count exactly the eigenvalues of `D` satisfying `sigma lambda(D)>=1`: strict threshold crossings live in the positive part of `D0`, while eigenvalues exactly equal to `sigma` contribute `dim K_sigma`. This proves (3.1); summing the two disjoint signs proves (3.2). QED.

This is the first essential new implication of the run. It removes the need to perturb away exact threshold eigenvalues and removes any reciprocal gap from the **count** of target-scale directions.

## 4. Principal-minimal deletion essentiality

The exact formula becomes substantially stronger after the r43 principal-minimal reduction.

Fix the same physical partition `H union L`, with `D=A[L,L]`, and let

```
k := N_D(1) <=2,
p := N_A(1) in {3,4}.
```

For `i in H`, let `A^(i)` be the proper principal matrix obtained by deleting the literal physical coordinate `i`. The base `D` is unchanged. Moreover the threshold spaces in Theorem 3.1 simply restrict:

```
Nspace_sigma^(i) = Nspace_sigma intersect e_i^perp,
T_sigma^(i) = S_sigma restricted to (Nspace_sigma intersect e_i^perp).
```

Put `q_sigma^(i)=n_ge0(T_sigma^(i))`.

Since `Nspace_sigma intersect e_i^perp` has codimension at most one in `Nspace_sigma`, restriction of a symmetric quadratic form changes its nonnegative index by at most one:

```
q_sigma-1 <= q_sigma^(i) <= q_sigma.                             (4.1)
```

Principal minimality says `N_{A^(i)}(1)<=2`. Using the exact threshold formula for `A^(i)` therefore gives

```
k + q_+^(i) + q_-^(i) <=2.                                     (4.2)
```

Subtract (4.2) from `p=k+q_++q_-`.

### Corollary 4.1 — `QFORM-PRINCIPALMINIMAL-THRESHOLD-DELETION-ESSENTIALITY-v1`

For every literal physical coordinate `i in H`,

```
(q_+-q_+^(i)) + (q_--q_-^(i)) >= p-2,                          (4.3)
```

and each parenthesized loss is either zero or one.

Hence:

- if `p=3`, **every** physical H-coordinate is threshold-essential for at least one of the two sign cores;
- if `p=4`, both sign cores are nontrivial and **every** physical H-coordinate lowers the nonnegative index of **both** threshold cores by exactly one.

The second statement follows because the total loss in (4.3) is at least two while each of the two sign losses is at most one.

This is an exact source-indexed consequence, not a statement about rotated random variables. It says the principal-minimal condition is visible inside the finite threshold Schur forms through deletion of the actual original coordinates.

## 5. Splice into the r39 rank-six retained-error collar

Now use the quantitative r39 decomposition from Section 1. For each sign define the punctured threshold gap

```
g_sigma := min{|d-sigma|: d in spec(D), d != sigma},            (5.1)
```

with `g_sigma=+infinity` if the set is empty. Exact eigenvalues `d=sigma` are excluded from (5.1) because Theorem 3.1 already treats them through the kernel channel.

If either

`g_+ < 1/64` or `g_- < 1/64`,                                   (5.2)

then the base contains a genuine nonzero **near-threshold annulus mode**. This branch is deliberately retained: the known principal-minimal stress examples forbid pretending that such a mode has a fixed gap from the threshold.

Assume now that (5.2) fails, so

`||R_sigma||_op <=64` for both signs.                             (5.3)

Write `C=C_2+R_C`. An exact expansion of `S_sigma` gives

```
S_sigma = -I_H + F_sigma + Delta_sigma,                          (5.4)

F_sigma
 = sigma[ L_H
          - C_2 R_sigma C^T
          - R_C R_sigma C_2^T ],

Delta_sigma
 = sigma[ E_H - R_C R_sigma R_C^T ].                            (5.5)
```

Both matrices are symmetric. Moreover

```
rank(F_sigma)
 <= rank(L_H)+rank(C_2 R_sigma C^T)+rank(R_C R_sigma C_2^T)
 <=2+2+2=6,                                                     (5.6)
```

and

```
||Delta_sigma||_op
 < epsilon_H + ||R_C||^2 ||R_sigma||
 < epsilon_H + (1/64)^2*64
 = epsilon_H + 1/64
 =: delta_0
 = 0.015995786547222654... .                                    (5.7)
```

Compress (5.4) to `Nspace_sigma`. Denote the compressed finite-rank term by `Fbar_sigma` and error by `Deltabar_sigma`. Then

```
T_sigma = -I + Fbar_sigma + Deltabar_sigma,
rank(Fbar_sigma)<=6,
||Deltabar_sigma||<delta_0.                                     (5.8)
```

If `q_sigma=n_ge0(T_sigma)>0`, order eigenvalues decreasingly. Since `lambda_{q_sigma}(T_sigma)>=0`, Weyl gives

```
0 <= lambda_q(T_sigma)
   <= -1 + lambda_q(Fbar_sigma) + ||Deltabar_sigma||,
```

so

```
boxed:
lambda_j(Fbar_sigma) > 1-delta_0
                    = 0.9840042134527773...
for every 1<=j<=q_sigma.}                                      (5.9)
```

In particular `q_sigma<=6` in this fixed-gap chamber.

### Theorem 5.1 — `QFORM-BASESUBCRITICAL-ANNULUS-OR-FINITE-THRESHOLD-R6-v1`

In every principal-minimal unpaid r39 carrier state, one of the following holds:

1. **near-threshold base annulus:** for some sign `sigma`, `D` has a nonthreshold eigenvalue `d` with
   `0<|d-sigma|<1/64`;
2. **finite strong threshold carrier:** for at least one sign `sigma`, the exact threshold core has the form
   `T_sigma=-I+Fbar_sigma+Deltabar_sigma`, with
   `rank(Fbar_sigma)<=6`, `||Deltabar_sigma||<0.015996`, and
   `Fbar_sigma` has an eigenvalue `>0.9840042`.

More quantitatively, if the full principal-minimal matrix has four threshold-large eigenvalues, then in the non-annular branch **both signs** have such a strong finite carrier, by Corollary 4.1. If it has three threshold-large eigenvalues, at least one sign does.

#### Proof

If the annulus occurs, we are in branch 1. Otherwise (5.3)-(5.8) hold. Since `k=N_D(1)<=2` while `p=N_A(1)>=3`, (3.2) gives `q_++q_-=p-k>=1`; hence at least one `q_sigma` is positive and (5.9) proves branch 2. For `p=4`, Corollary 4.1 forces both `q_+` and `q_-` to be positive, so (5.9) holds for both signs. QED.

This theorem spends the r39 rank-six collar in a way that is **uniform at exact threshold and does not drop the retained error**. It also makes precise what remains: either a true annular base mode arbitrarily close to `+1` or `-1`, or a strong finite threshold carrier created by the actual retained low-rank H/L interaction.

Important scope point: `Fbar_sigma` is a deterministic threshold-Schur carrier, not itself a literal principal block of `A`. It must not be fed directly into a product-law density theorem as though its eigen-coordinates were independent. The next receiver must realize its strength through original-coordinate coefficients/projections, or use the annular mode jointly with the physical H-bank.

## 6. Designated partner account04/B20 applied at an actual inequality

The completed designated partner source is account04/B20 r11,

`yspennstate/math-open-problems@9d07c5d5c69c885509db66cb1093acdeff8bcb64`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T181642Z-account04-B20-QFORM-r11/REPORT.md`.

Its exact three-color theorem applies in the still-live exact-rank-three diffuse Schur-normal branch. At the actual inequality already present in the compiler,

`eta_h := max_k h_k^2 < 1/64`,                                   (6.1)

it gives three disjoint ORIGINAL-coordinate source banks with

```
boxed: W_1 W_2 W_3 >= (1-3 eta_h)/27 > 61/1728.}                (6.2)
```

The three bank projections are genuinely independent and their joint density cap is

```
e^(3/2) sqrt(27/(1-3 eta_h))
 < e^(3/2) sqrt(1728/61)
 = 23.85331121230936... <23.854.                                (6.3)
```

This is an actual quantitative application of the partner theorem. It remains strictly a source-valid projection certificate; neither this run nor the partner promotes (6.3) by itself to a curved quadratic pushforward bound.

## 7. Deterministic/numerical regression check

`CHECK.py` is included beside this report. It constructs random symmetric block matrices with base spectra drawn from

`{-2.2,-1,-0.8,-0.15,0.4,0.93,1,1.3,2.1}`,

so exact `+1` and `-1` base eigenvalues occur frequently. For both signs it computes the Moore-Penrose threshold core and compares (3.1) against the full spectral count. Cases whose floating-point eigenvalues land within `1e-6` of the closed threshold are omitted from the numerical comparison because their sign is numerically ambiguous; the exact proof above does not omit them.

With seed `20260923` and `10,000` random block trials, the check performed `19,821` stable sign comparisons and found **zero violations**. It also reproduces

```
epsilon_H = 0.000370786547222655,
delta_0  = 0.015995786547222654,
1-delta_0= 0.984004213452777346,
partner cap = 23.853311212309360.
```

The numerical check is regression evidence only; Theorems 3.1 and 5.1 are proved analytically.

## 8. Updated end-to-end position

The current assembly can now be stated more sharply.

1. account03/B19 r43 reduces the full affine problem, with no constant loss, to principal-minimal targets. These have exactly three threshold-large eigenvalues, or four with mixed signs.
2. account03/B20 r39 compresses the unpaid finite H-bank into `rank<=6` plus a genuine retained coefficient collar `<0.015996`, while retaining `D=A[L,L]` exactly.
3. r43 removes every state in which `D` itself already has three threshold-large modes, so the live base has `N_D(1)<=2`.
4. Theorem 3.1 of this run gives the **exact missing threshold count** as the sum of two finite threshold-Schur indices, without any gap hypothesis and with exact `+/-1` eigenvalues handled correctly.
5. Principal minimality makes every physical H-coordinate threshold-essential in the precise sense of Corollary 4.1.
6. The r39 quantitative collar then forces the surviving state into either a punctured `1/64` near-threshold annulus in `D`, or a rank-at-most-six threshold carrier with strength `>0.9840042`; in the mixed-sign four-eigenvalue case there is one such strong carrier for each sign.

Thus the first remaining implication is now

`QFORM-THRESHOLD-SCHUR-ANNULUS-OR-SOURCE-REALIZATION-PAYMENT-v1`:

> Pay the genuine near-threshold base-annulus branch uniformly as its eigenvalue approaches `+1` or `-1`, or convert the strong finite threshold-Schur carrier (`rank<=6`, eigenvalue `>0.9840042`) into a source-valid original-coordinate pair/triple/hub/grouped-crossing receiver, using the deletion-essentiality constraints and retaining the full nonzero coefficient collar.

A proof is not allowed to divide by the annular distance to threshold, to treat `Fbar_sigma` eigen-coordinates as independent, or to delete `E_H`/`R_C` because their coefficients are small.

## 9. Status

- Full unrestricted QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**.
- New exact theorem: `QFORM-EXACT-THRESHOLD-SCHUR-COUNT-v1`.
- New principal-minimal consequence: `QFORM-PRINCIPALMINIMAL-THRESHOLD-DELETION-ESSENTIALITY-v1`.
- New quantitative compiler: `QFORM-BASESUBCRITICAL-ANNULUS-OR-FINITE-THRESHOLD-R6-v1`.
- No new density bound is claimed on the two surviving branches of Theorem 5.1.
- Repository transport and source-memory writeback are not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
