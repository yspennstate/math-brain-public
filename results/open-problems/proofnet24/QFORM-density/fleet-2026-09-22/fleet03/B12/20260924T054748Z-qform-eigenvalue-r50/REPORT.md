SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-24T05:47:48Z.
attacking: codimension-one and finite-codimension relative-resonance stability: retain five physical square modes under an arbitrary signed addition even when several carrier directions cancel exactly.

# fleet03/B12 — relative-resonance rank budget for arbitrary signed additions

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T054748Z-qform-eigenvalue-r50`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source boundary

The owner target remains the unrestricted product-law conjecture: for independent real ORIGINAL coordinates with scalar densities bounded by one, and every real symmetric coefficient matrix with at least three eigenvalues of modulus at least one, prove a universal output-density bound or give a valid counterexample. The current source still records `QFORM-FULL` as OPEN.

No Gaussianity, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, post-rotation independence, conditional-density cap, arbitrary-joint coarea estimate, pointwise van-der-Corput decay, or small-random-error approximation is used below. Every additional quadratic term remains in the final coefficient matrix.


The completed designated partner actually applied is fleet04/B12 r8:

- repository/commit: `yspennstate/math-open-problems@bcb9fd2641440a89d6e4967781d755618e163001`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260924T002154Z-fleet04-B12-multihub-shear-r8/REPORT.md`;
- theorem: `QFORM-MULTIHUB-ALIGNED-SPECTRAL-PACKET-STABILITY-v1`.

The density receiver is the completed fleet03/B12 r47 five-square-mode theorem:

- source commit used for readback: `6ea11aaafcf72491b05cb7b51b93166a91e1ad2d`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260924T031535Z-qform-eigenvalue-r47/REPORT.md`;
- theorem: `QFORM-FIVE-SQUARE-MODE-E3-CORE-COMPILER-v1`.

It states that if an ORIGINAL-coordinate bank `H`, `|H|=m>=5`, satisfies

`lambda_5((A^2)[H,H]) >= g^2 > 0`,

then every cap-one independent product input has a continuous `C_0(R)` density satisfying

`||p_(X^T A X)||_infinity <= sqrt(24*pi*m+K3^2)/g`,

where

`K3 = 3*2^(4/3)*exp(1/3) = 10.550168831164775...`.

The previous B12 run r49 charged the norm of the component of a new local action pointing into the current carrier image. The theorem below changes mechanism: it allows that in-image component itself to be arbitrarily large and even to cancel several carrier directions exactly. Only the number/strength of *relative resonances* matters.

## 2. Exact relative-action factorization

Let `H` be a literal ORIGINAL-coordinate bank of size `m`, and let

`P : R^m -> R^n`

be its coordinate embedding. Let `A_*` be a real symmetric baseline and put

`M = A_* P`.

Assume `M` has full column rank and set

`G = M^T M`, `g=s_m(M)>0`.

Let `E=E^T` be an **arbitrary** further signed addition, with no restriction on rank, inertia, operator norm, eigenvector orientation, or complement spectrum. Put

`N = E P`.

Because `M` has full column rank, its left Moore-Penrose inverse is

`M^dagger = (M^T M)^(-1) M^T`.

Define the dimensionless relative in-image action

`K = M^dagger N`,

and the transverse action

`Z = (I - M M^dagger) N`.

Then

`N = M K + Z`, `M^T Z=0`.

Thus, with

`L = I_m + K`,

we have the exact decomposition

`(A_*+E)P = M L + Z`.                                            (2.1)

The two codomain pieces in (2.1) are orthogonal, hence

`((A_*+E)P)^T ((A_*+E)P)
 = L^T G L + Z^T Z`.                                             (2.2)

Since `G >= g^2 I_m` in Loewner order,

`L^T G L + Z^T Z >= g^2 L^T L`.                                (2.3)

This identity is the entire stability mechanism. The transverse term is never paid as an error; it is positive square energy.

## 3. Main theorem: relative resonance, not perturbation size, controls mode survival

Order singular values decreasingly as `s_1 >= ... >= s_m`.

### Theorem 3.1 — `QFORM-RELATIVE-RESONANCE-DROP-STABILITY-v1`

Under the setup of Section 2, for every `j=1,...,m`,

`boxed:
 s_j((A_*+E)P) >= g * s_j(I_m + M^dagger E P).`                  (3.1)

Equivalently,

`boxed:
 lambda_j((((A_*+E)^2)[H,H]))
 >= g^2 s_j(I_m + M^dagger E P)^2.`                             (3.2)

No norm bound on `E`, `EP`, `M^dagger EP`, or the transverse action is assumed.

### Proof

Equation (2.2) and `G>=g^2 I` give the Loewner inequality (2.3). Eigenvalue monotonicity for Hermitian matrices yields, for every `j`,

`lambda_j(((A_*+E)P)^T((A_*+E)P))
 >= g^2 lambda_j(L^T L)`.

Taking nonnegative square roots gives (3.1). Symmetry of `A_*+E` gives

`((A_*+E)P)^T((A_*+E)P)=P^T(A_*+E)^2P=((A_*+E)^2)[H,H]`,

which gives (3.2). QED.

### Interpretation

The dangerous event is not that an added eigenvalue is large, negative, noncommuting, or supported on the carrier. The dangerous event is that the **aggregate relative map**

`I + M^dagger E P`

has too many small singular values. A completely arbitrary signed packet may cancel some carrier directions exactly; those directions can simply be discarded if enough others remain for a paid density receiver.

For a spectral packet `E=U Theta U^T`, the relative operator is explicitly

`K = (M^T M)^(-1) M^T U Theta (P^T U)^T`.                       (3.3)

All signs and eigenvalue magnitudes remain inside this deterministic aggregate matrix. No rotated random coordinates are introduced.

## 4. Finite-codimension resonance budget

Theorem 3.1 becomes especially useful because the completed density theorem needs only five square modes.

Let

`K = K_0 + F`,

where

`rank(K_0) <= q`, `||F||_op <= epsilon`.

The low-rank term `K_0` may have completely unbounded norm and may include exact `-I` action on its range.

For a rank-`q` perturbation of the identity, singular-value interlacing gives

`s_j(I+K_0) >= s_(j+q)(I)=1`,                                  (4.1)

whenever `j+q<=m`. Weyl's singular-value inequality then gives

`s_j(I+K_0+F) >= 1-epsilon`.                                    (4.2)

Combining with Theorem 3.1 yields the following.

### Corollary 4.1 — `QFORM-RELATIVE-RANK-TAIL-FIVE-MODE-STABILITY-v1`

Assume `m>=5`, `q<=m-5`, `0<=epsilon<1`, and

`M^dagger E P = K_0+F`,

with `rank(K_0)<=q`, `||F||op<=epsilon`. Then

`boxed:
 sqrt(lambda_5((((A_*+E)^2)[H,H]))
 >= g(1-epsilon).`                                               (4.3)

Consequently every cap-one independent product input has a continuous `C_0` density and

`boxed:
 ||p_(X^T(A_*+E)X)||_infinity
 <= sqrt(24*pi*m+K3^2)/(g(1-epsilon)).`                          (4.4)

The conclusion permits:

1. up to `m-5` exact relative cancellation directions;
2. arbitrarily large positive or negative relative action on those directions;
3. an arbitrary full-rank transverse local action `(I-MM^dagger)EP`, with no size bound;
4. arbitrary spectrum on the complement of `H`;
5. arbitrary mutual noncommutation among all underlying signed spectral packets.

Only the residual *relative* full-rank tail `F` is charged.

### Sharp structural point

The rank budget in (4.3) is not an artefact: if `q=m-4`, one can take `K_0=-P_V` on an `(m-4)`-dimensional subspace, leaving only four nonzero relative directions. A five-mode conclusion then cannot follow from the baseline carrier alone. Thus `m-5` is the exact mode-count threshold for this receiver.

## 5. Required fleet04/B12 application at an actual inequality

Apply the completed fleet04/B12 r8 theorem with

`m=11`, `p=2`, `ell=9`.

Let `U` be an eleven-coordinate two-plane and let the partner pre-tail blocks satisfy

`C_* = U Lambda U^T`,
`B_* = U W^T + R`, `U^T R=0`,

with

`s_2(Lambda)>=4`, `s_9(R)>=2`,
`||Lambda^(-1) W^T||op <=1`.

The partner theorem gives the **actual equation-level reserve**

`g_* := s_11(P_H A_*)
 = sqrt(lambda_11((A_*^2)[H,H]))
 >= gamma(1)*2
 = sqrt(5)-1
 = 1.2360679774997898... .`                                      (5.1)

This is the designated partner result applied at a concrete inequality.

Now add an arbitrary real symmetric matrix `E`. There is no operator-norm or eigenvalue bound on `E`. Define

`K=M_*^dagger E P_H`, `M_*=A_*P_H`.

Suppose only that

`K=K_0+F`, `rank(K_0)<=6`, `||F||op<=1/10`.                      (5.2)

The six-dimensional term `K_0` may be arbitrarily large and may equal `-I` on six directions. The transverse carrier action of `E` is unrestricted.

Corollary 4.1 and (5.1) give

`boxed:
 sqrt(lambda_5((A^2)[H,H]))
 >= (sqrt(5)-1)*(9/10)
 = 1.112461179749811... >1.`                                    (5.3)

Therefore the final matrix automatically remains in the owner target class: coordinate compression cannot increase singular values, so

`s_3(A) >= s_5(A) >= s_5(A P_H) >1`.                            (5.4)

The five-mode density compiler gives

`boxed:
 ||p_(X^T A X)||_infinity
 <= sqrt(264*pi+K3^2)/((sqrt(5)-1)*0.9)
 = 27.570052692687145... <27.571.`                               (5.5)

The density is continuous and belongs to `C_0(R)`.

This replaces the partner's small absolute local-row-tail condition by a substantially different one: six relative directions may be completely destroyed by an **arbitrarily large** signed addition, while the remaining relative tail need only be ten-percent small. No bound is imposed on the orthogonal local action or the global spectrum.

## 6. Explicit hostile signed-spectrum family with six exact cancellations

The abstract condition (5.2) is nonempty in a very strong way.

Take `H={1,...,11}`, `J={12,...,20}`. Choose the partner baseline with

`U=(e_1,e_2)`,
`Lambda=4 I_2`, `W=0`,

and let the nine rows `3,...,11` cross to the nine `J` coordinates with coefficient `2`. Thus

`C_* = diag(4,4,0,...,0)`,

and the transverse crossing block has nine singular values all equal to `2`. The partner r8 equation gives `s_11(A_*P_H)>=2` here (indeed the eleven carrier columns are orthogonal with norms `4,4,2,...,2`).

Now add a symmetric matrix `E` as follows.

- Set `E_11=E_22=-4`, exactly cancelling the first two carrier columns.
- For physical rows `i=3,4,5,6`, add the symmetric cross coefficient `-2` on the corresponding `H_i-J_(i-2)` pair, exactly cancelling four more carrier columns.
- For `i=7,...,11`, add arbitrary symmetric cross coefficients `t_i` on the corresponding remaining five pairs, subject only to

  `|1+t_i/2| >=1`.

The numbers `t_i` may be arbitrarily large and of either sign; for example any `t_i>=0` or `t_i<=-4` is allowed. Each such cross addition contributes the signed eigenvalue pair `+|t_i|,-|t_i|` to the added matrix on its two-coordinate plane.

Relative to the partner carrier, the aggregate relative map is exactly diagonal:

`I + M_*^dagger E P_H
 = diag(0,0,0,0,0,0,
        1+t_7/2,...,1+t_11/2).`                                 (6.1)

Hence there are **six exact resonance/cancellation directions**, while

`s_5(I+M_*^dagger E P_H)>=1`.                                   (6.2)

Theorem 3.1 gives

`boxed:
 sqrt(lambda_5((A^2)[H,H])) >=2.`                               (6.3)

and therefore

`boxed:
 ||p_Q||infinity <= sqrt(264*pi+K3^2)/2
 = 15.335306672135596... <15.336,`                               (6.4)

with a continuous `C_0` density.

This family simultaneously contains exact deleted modes and arbitrarily large additional positive/negative eigenvalues. The new quadratic terms are retained exactly; there is no convolution argument.

## 7. Deterministic computation

`CHECK_RELATIVE_RESONANCE.py` tests two independent consequences of the proof.

First, for 10,000 random full-column-rank matrices `M` and arbitrary additions `N`, it verifies simultaneously for every singular index `j` that

`s_j(M+N) >= s_m(M) s_j(I+M^dagger N)`.

Second, it generates low-rank relative actions of rank at most `m-5`, adds an operator-norm-`epsilon` relative tail and an arbitrarily large codomain-transverse term, then verifies

`s_5(M+N) >= s_m(M)(1-epsilon)`.

Seed `202609240550` produced:

- full theorem violations: `0 / 10000`;
- minimum all-index numerical margin: `0.000780413247355706`;
- rank-tail corollary violations: `0 / 10000`;
- minimum rank-tail `s_5` margin: `0.061235693766226174`.

These are finite floating-point consistency checks only. The proof is the exact orthogonal factorization (2.2), Loewner monotonicity, rank interlacing, and singular-value Weyl.

## 8. What this advances and what remains open

This theorem strictly changes the additional-spectrum accounting from the previous run. The r49 destructive-projection theorem can overcharge a huge in-image addition even when it merely annihilates a few expendable carrier directions. Here those directions are spent as a **finite resonance codimension**, and the remaining five directions feed a completed density receiver.

Full QFORM is still **OPEN / NOT PROVED / NOT DISPROVED**. The unresolved target-level implication is structural: starting from only `s_3(A)>=1`, force a bounded ORIGINAL-coordinate carrier whose aggregate relative action has at least five quantitatively nonresonant directions, or prove that failure of every such carrier necessarily produces one of the already-paid projected-crossing, grouped-bank, physical-core, hub, ridge, pair, common-plane, Schur, or Pluecker-volume exits.

The theorem does not claim that the bare three-large-eigenvalue hypothesis automatically supplies such a carrier. It does show that arbitrary extra spectrum is much less dangerous than its norm suggests: only enough simultaneous relative resonances to erase all but four paid carrier directions can defeat this particular stability mechanism.

Continuity is proved for the positive five-mode branch through the source-valid fixed-matrix/five-mode compiler. Continuity for the unrestricted conjecture remains open.
