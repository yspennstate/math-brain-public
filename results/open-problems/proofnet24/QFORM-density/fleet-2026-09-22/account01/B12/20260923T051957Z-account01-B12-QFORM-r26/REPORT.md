# account01/B12 — multirank Krein–Woodbury stability for arbitrary added eigenvalues

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T051957Z-account01-B12-QFORM-r26`  
Assignment: Additional eigenvalue control  
Status: **PROVED_SUPPORTING_THEOREMS / FULL_QFORM_OPEN / NOT_INDEPENDENTLY_REVIEWED**  
Continuity: **not claimed**; the density conclusion below is essential boundedness.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact question attacked

The target asks for a universal density bound for `Q=X^T A X` when the original coordinates `X_i` are independent and have densities bounded by one, under only the assumption that `A` has at least three eigenvalues of absolute value at least one. The present assignment is narrower: determine when additional smaller or larger eigenvalues of arbitrary sign can be added without losing an already localized physical-coordinate certificate.

The point of the argument below is that the added spectral directions are used only as a deterministic matrix decomposition. The random variables are never rotated. The terminal density theorem is applied after conditioning on all coordinates outside an ORIGINAL-coordinate physical triple.

Fresh control/corrections consumed before publication: brain main initially `cd7be220caca96ae3a0819f8366251974ddb201c`, refreshed to `33f0d9ab4dfab3247b748f4619c2e80dc2486b6c`; OWNER CONTROL revision `2026-09-22.15`; programme revision `2026-09-22.5`. In particular I do not use pointwise quadratic Fourier decay, arbitrary-joint coarea, a conditional density cap after rotation, a naive fiber-supremum integral, or an independence/convolution assertion for a spectral remainder.

## 2. Partner premise actually read

The latest completed `account02/B12` report used here is

`yspennstate/math-open-problems@06fbcbb277d5db4f89dfc0c04b14174cc4315cc7`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T045101Z-account02-B12-auto11/REPORT.md`.

Its Lemma 2.1 is the rank-one sign-routed Sherman–Morrison theorem. If `B` is an invertible physical triple, `u` is a physical restriction of an added rank-one direction, `q=u^T B^{-1}u`, and the scalar update `tau` has the same sign as `q`, then

`||(B+tau u u^T)^{-1}||op <= ||B^{-1}||op + ||B^{-1}u||^2/|q|`,

uniformly in `|tau|`. Its Corollary 2.2 combines this with the localized physical-three-coordinate density theorem: after an additional symmetric tail of operator norm `delta` below the resulting gap, the full ambient quadratic form has density at most `6 sqrt(pi)/(gap-delta)`.

The present report extends the matrix part from one sign-compatible update to several simultaneous mixed-sign updates. Section 6 below also applies the completed partner result itself to a numerical inequality, as requested by the assignment.

## 3. Main theorem: mixed-sign multirank magnitude-free stability

### Theorem 3.1 (`QFORM-MULTIRANK-KREIN-WOODBURY-STABILITY-v1`)

Let `B` be a real symmetric invertible `m x m` matrix and let `U` be an `m x r` real matrix. Let `Theta` be a real symmetric `r x r` matrix. Discard the kernel of `Theta`, and diagonalize its active part orthogonally. Thus, after replacing `U` by `U W`, we may write

`Theta = J D`,

where `D>0` is diagonal and

`J = diag(I_p,-I_q)`

is the sign matrix. Put

`K = U^T B^{-1} U`

in this same active basis and decompose it according to the positive and negative spectral subspaces of `Theta`:

`K = [[K_{++},K_{+-}],[K_{-+},K_{--}]]`.

Assume that for some `kappa>0`

`K_{++} >= kappa I_p`,

`K_{--} <= -kappa I_q`.                                           (3.1)

There is **no hypothesis at all on the mixed block `K_{+-}`**. Then

`B_Theta := B + U Theta U^T`

is invertible and

`boxed: sigma_min(B_Theta) >= gamma`,                              (3.2)

where

`gamma := [ ||B^{-1}||op + ||B^{-1}U||op^2/kappa ]^{-1}`.         (3.3)

In particular, `gamma` is independent of every nonzero eigenvalue magnitude of `Theta`. The positive and negative added eigenvalues may simultaneously tend to infinity.

#### Proof

Since the active `Theta` is invertible, Woodbury gives

`B_Theta^{-1}
 = B^{-1} - B^{-1} U (Theta^{-1}+K)^{-1} U^T B^{-1}`,             (3.4)

provided the middle matrix is invertible. Let

`M := Theta^{-1}+K = J D^{-1}+K`.                                 (3.5)

For `x=(x_+,x_-)`, use the indefinite multiplier `J`. Because `K` is symmetric,

`x^T J K x
 = x_+^T K_{++}x_+ + x_+^T K_{+-}x_-
   - x_-^T K_{-+}x_+ - x_-^T K_{--}x_-`.

The two mixed scalars cancel exactly:

`x_+^T K_{+-}x_- = x_-^T K_{-+}x_+`.

Hence (3.1) implies

`x^T J M x
 = x^T D^{-1}x + x_+^T K_{++}x_+ - x_-^T K_{--}x_-
 >= kappa ||x||_2^2`.                                             (3.6)

Since `J` is orthogonal,

`kappa ||x||^2
 <= |x^T J M x|
 <= ||x|| ||J M x||
 = ||x|| ||M x||`.

Therefore

`sigma_min(M)>=kappa`,  `||M^{-1}||op<=1/kappa`.                  (3.7)

So `M` is invertible and Woodbury is justified. Taking norms in (3.4),

`||B_Theta^{-1}||op
 <= ||B^{-1}||op + ||B^{-1}U||op^2 ||M^{-1}||op
 <= ||B^{-1}||op + ||B^{-1}U||op^2/kappa
 = gamma^{-1}`.

Since `B_Theta` is symmetric and invertible, `sigma_min(B_Theta)=1/||B_Theta^{-1}||op`, proving (3.2). QED.

### Remarks

1. For `r=1`, condition (3.1) is precisely the sign condition in the completed `account02/B12` rank-one theorem: `theta q>0`, with `q=u^T B^{-1}u`. Thus Theorem 3.1 is a genuine multirank extension of that partner mechanism.
2. The cancellation of `K_{+-}` in (3.6) is the structural point. A direct Euclidean lower bound on `Theta^{-1}+K` would wrongly charge the mixed block. The correct multiplier is the signature matrix `J`.
3. Zero update eigenvalues are harmless: delete their columns before applying the theorem. Thus the conclusion is stable through coefficients that equal zero, although a sign-routing certificate may change when a coefficient crosses zero.

## 4. Density corollary in original coordinates

### Corollary 4.1 (`QFORM-KREIN-CORE-DENSE-TAIL-v1`)

Let `I` be an ORIGINAL-coordinate physical triple. Suppose

`B=A0[I,I]`

is invertible. Let the arbitrary signed spectral update be

`E = V Theta V^T`,

and set

`U=V[I,:]`.

Assume the active positive/negative spectral subspaces of `Theta` satisfy (3.1) for

`K=U^T B^{-1}U`

with constant `kappa`, and define `gamma` by (3.3). Let `T` be an arbitrary real symmetric matrix of arbitrary rank and sign with

`||T||op <= delta < gamma`.

Then the actual physical triple of

`A=A0+E+T`

has

`sigma_min(A[I,I]) >= gamma-delta`.                                (4.1)

Consequently, using the completed localized physical-three-coordinate theorem after conditioning on all coordinates outside `I`,

`boxed: ||p_(X^T A X)||infinity <= 6 sqrt(pi)/(gamma-delta).`       (4.2)

#### Proof

Theorem 3.1 gives `sigma_min(B+U Theta U^T)>=gamma`. Since a principal compression cannot have operator norm larger than the ambient perturbation,

`||T[I,I]||op<=delta`.

Weyl's singular-value inequality proves (4.1). The physical-triple density theorem applies to the three still-independent original coordinates in `I`; conditioning on all outside original coordinates creates arbitrary affine terms, which that theorem allows. This yields (4.2). QED.

This is a deterministic certificate theorem. It never treats `X^T T X` as a small random variable and never treats the quadratic update as an independent convolution.

### Literal added-eigenvalue interpretation

If the columns of `V` are orthonormal, the nonzero eigenvalues of `E=V Theta V^T` are exactly the eigenvalues of `Theta`. Therefore (4.2) controls literal added eigenvalues of arbitrary positive and negative magnitude whenever their physical footprint satisfies the sign-compatible inverse-leverage condition (3.1).

## 5. Finite orthant routing

### Corollary 5.1 (`QFORM-FINITE-ORTHANT-CORE-COMPILER-v1`)

Let `v_1,...,v_r` be fixed orthonormal directions and consider

`E(t)=sum_{j=1}^r t_j v_jv_j^T`.

For each realized sign vector `s=(sign t_1,...,sign t_r)` suppose there is an ORIGINAL-coordinate physical triple `I_s` such that, with

`B_s=A0[I_s,I_s]`, `U_s=(v_1[I_s],...,v_r[I_s])`,

`K_s=U_s^T B_s^{-1}U_s`,

the principal block of `K_s` on the indices `t_j>0` is at least `kappa_s I`, while the principal block on the indices `t_j<0` is at most `-kappa_s I`. Define

`gamma_s=[||B_s^{-1}||op+||B_s^{-1}U_s||op^2/kappa_s]^{-1}`.

If

`gamma_*:=min_s gamma_s>0`

and `||T||op<=delta<gamma_*`, then for **all magnitudes** of the coefficients `t_j`, including simultaneous arbitrarily large positive and negative coefficients,

`boxed: ||p_(X^T(A0+E(t)+T)X)||infinity <= 6 sqrt(pi)/(gamma_*-delta).` (5.1)

For a physical triple, full-rank sign compatibility can involve at most three active independent update directions, but update directions having zero compression to the selected core are automatically free. The statement is therefore most useful for one, two, or three genuinely active arbitrary-magnitude spectral changes, plus an arbitrary-rank small operator-norm cloud.

## 6. Required actual application of the completed account02/B12 result

The partner report gives the explicit matrix

`C=[[4,-3,-3,3],[-3,4,-3,3],[-3,-3,4,3],[3,3,3,-8]]`,

`v=(1,1,1,1)^T/2`,

with

`spec(C+tau vv^T)={1+tau,7,7,-11}`.

It proves that for every real `tau`, routing by the sign of `tau` to one of the two physical triples `{1,2,3}` or `{2,3,4}` leaves a physical singular-value gap at least `2`. Therefore, for an arbitrary symmetric dense tail `F` satisfying

`||F||op<=1/4`,

its completed Corollary 2.2 applies at the concrete inequality

`sigma_min((C+tau vv^T+F)[I_tau,I_tau]) >= 2-1/4 = 7/4`,

and hence

`boxed: ||p_(X^T(C+tau vv^T+F)X)||infinity
        <= 6 sqrt(pi)/(7/4)
        = 24 sqrt(pi)/7
        = 6.076984631676055... .`                                  (6.1)

This is the designated partner result applied to an actual density inequality. It also supplies the rank-one `r=1` endpoint against which Theorem 3.1 was checked algebraically.

## 7. Exact two- and three-eigenvalue sign-router families

The orthant compiler is non-vacuous for simultaneous arbitrary added eigenvalues.

### Two arbitrary eigenvalues

Take four disjoint physical triples indexed by `s=(s1,s2) in {+1,-1}^2`. On triple `H_s`, let

`A0[H_s,H_s]=diag(2s1,2s2,2)`,

with no cross-block couplings between these four triples. Define global vectors `v1,v2` by putting

`v1[H_s]=(1/2,0,0)^T`,
`v2[H_s]=(0,1/2,0)^T`

on every one of the four triples. Then `v1,v2` are orthonormal. Hence

`E=t1 v1v1^T+t2 v2v2^T`

has the two literal nonzero eigenvalues `t1,t2`.

For any real `t1,t2`, choose `s_j=sign(t_j)` (either sign if `t_j=0`). On the selected physical triple,

`(A0+E)[H_s,H_s]
 = diag(s1(2+|t1|/4), s2(2+|t2|/4), 2)`,                       (7.1)

so its singular-value gap is at least `2`, with no dependence on `|t1|` or `|t2|`. Therefore every arbitrary symmetric tail `T` with `||T||op<=delta<2` satisfies

`boxed: ||p_(X^T(A0+E+T)X)||infinity <= 6 sqrt(pi)/(2-delta).`      (7.2)

At `delta=1/4`, this is again `24 sqrt(pi)/7 <6.077`.

### Three arbitrary eigenvalues

The same construction works with eight disjoint triples indexed by `s in {+1,-1}^3`. Set

`A0[H_s,H_s]=2 diag(s1,s2,s3)`.

For `j=1,2,3`, let `v_j[H_s]=2^{-3/2} e_j` on every one of the eight triples. Then `v_1,v_2,v_3` are orthonormal. For

`E=sum_{j=1}^3 t_j v_jv_j^T`,

choose the triple with `s_j=sign(t_j)`. Its exact updated block is

`diag( s1(2+|t1|/8), s2(2+|t2|/8), s3(2+|t3|/8) )`,              (7.3)

so again the gap is at least `2` for **all** real `t_1,t_2,t_3`. Thus (7.2) holds verbatim for three simultaneously arbitrary added eigenvalues of either sign and arbitrary magnitude, plus an arbitrary-rank nonseparable tail of operator norm `<2`.

This family is a literal spectral-addition example because the `v_j` are global orthonormal vectors. It is not a proof of the full conjecture; its purpose is to demonstrate that finite physical-core routing can absorb several genuinely independent arbitrary spectral changes without rotating the random inputs.

## 8. A nontrivial one-core mixed-sign example with nonzero cross leverage

Let

`B=diag(1,-1,2)`,

`u1=(1,0,0)^T`, `u2=(1,sqrt(2),0)^T`, `U=(u1,u2)`.

Then

`K=U^T B^{-1}U=[[1,1],[1,-1]]`.                                  (8.1)

Thus for every `theta1>0` and `theta2<0`, condition (3.1) holds with `kappa=1`, despite the nonzero mixed entry `K12=1`. Moreover

`||B^{-1}||op=1`,

`(B^{-1}U)^T(B^{-1}U)=[[1,1],[1,3]]`,

whose top eigenvalue is `2+sqrt(2)`. Hence Theorem 3.1 gives the explicit magnitude-free floor

`gamma = 1/(3+sqrt(2)) = 0.226540919660986...`.                   (8.2)

Therefore an arbitrary symmetric tail with `delta<gamma` yields

`||p_Q||infinity <= 6 sqrt(pi)/(gamma-delta)`.                    (8.3)

The purpose of this example is that the positive and negative update directions are *not* inverse-orthogonal (`K12!=0`); the Krein multiplier cancels that cross term exactly.

## 9. What this does and does not solve

What is now proved:

* arbitrary update magnitudes are harmless on a physical core whenever the inverse-leverage form `U^T B^{-1}U` has the same definite sign on the positive and negative update spectral subspaces;
* positive and negative large update eigenvalues may occur simultaneously;
* the mixed inverse-leverage block need not be small at all;
* a finite family of physical cores can route finitely many sign orthants;
* a completely nonseparable arbitrary-rank small operator-norm tail is paid once by Weyl;
* all conditioning remains in original independent coordinates.

What is not proved:

The bare target hypothesis `s_3(A)>=1` does not presently force such a sign-compatible physical core or a finite orthant-complete family of them. Existing corrections already show that one uniformly good physical minor or one fixed Schur/cross certificate cannot simply be assumed. The remaining target-level implication is to derive, from the global three-large-eigenvalue hypothesis, either (i) a sign-compatible/routable physical core of the kind above, or (ii) one of the already-paid aggregate-before-inversion ridge, grouped-bank, hub, pair-log, or cross-volume branches.

Therefore the status remains **FULL QFORM OPEN**. This report establishes **essential boundedness only in the stated stability scope** and makes no continuity claim.

## 10. Verification notes

The core algebra is exact. The only numerical constants reported above come from closed-form matrices. For the nontrivial example, the Gram eigenvalues are `2+-sqrt(2)`, so (8.2) follows exactly. No Monte Carlo or histogram is used as evidence.

Manual changed-text privacy check: generated mathematical text only; no credentials, tokens, private keys, or unrelated user data are present.
