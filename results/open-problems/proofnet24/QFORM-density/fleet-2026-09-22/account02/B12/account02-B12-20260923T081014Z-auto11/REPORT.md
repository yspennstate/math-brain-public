SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-23T08:10:14Z.
attacking: robust approximate-isotropic anchor switching for arbitrary multirank signed spectral updates under a genuinely dense small operator-norm tail.

# account02/B12 — robust approximate-anchor stability for arbitrary multirank spectral updates

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account02-B12-20260923T081014Z-auto11`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM + EXACT TARGET-CLASS FAMILY / FULL QFORM OPEN**  
Continuity: not claimed by this run; the conclusion below is an essential density bound.

## 1. Exact obligation and sources actually used

The target remains: for arbitrary independent real coordinates with one-dimensional probability densities at most one and arbitrary symmetric `A` having at least three eigenvalues of absolute value at least one, prove a universal essential density bound for `X^T A X`, or give a valid counterexample. No moments, bounded support, log-concavity, spectral-coordinate independence, or small-random-error hypothesis is introduced below.

This run uses at an equation:

1. Required newest-Claude localized physical-core theorem: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, Theorem A. For a three-coordinate original principal block whose three eigenvalues have absolute value at least `s`, after conditioning on every other ORIGINAL coordinate (arbitrary induced affine terms allowed),

   `||p_Q||_infinity <= 6 sqrt(pi)/s`.                                      (1.1)

2. Completed designated-partner account03/B12 matrix-parameter theorem: `yspennstate/math-open-problems@c00f2cfff4ac70e053c88b080e8dcfd63cde70aa`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T074544Z-qform-eigenvalue-r28/REPORT.md`, equation (2.2). Its notation is recalled below and is used directly.

The required newest-Claude `RESULTS.md` and `FOURIER_ROUTE_REPORT.md` at the same `e5f71d79...` source were also read. The live QFORM corrections were consumed before this proof; in particular, no independence after spectral rotation and no estimate of a dense-tail random quadratic term is used.

## 2. Partner matrix-parameter inequality

Fix one original-coordinate physical core `I` of size `m>=r+1`. Let its baseline principal block be `B=B^T`, and let `U` be the `m x r` restriction of the globally added directions, with full local column rank. Let `W` be an orthonormal basis of `range(U)` and `Z` an orthonormal complement. Write

`B11=W^T B W`, `B12=W^T B Z`, `D=Z^T B Z`,

and assume `D` is invertible. Set

`C=B11-B12 D^{-1}B12^T`,
`G=W^T U`,
`F=GG^T`,
`K=F^{-1/2} C F^{-1/2}`,
`rho=||B12 D^{-1}||op`,
`mu=sigma_min(D)`,
`f=lambda_min(F)`,
`ell(rho)=(sqrt(rho^2+4)-rho)/2`,
`S=F^{-1/2}G`.

The partner proves `S` is orthogonal and, for every real symmetric `Theta in Sym_r`,

`sigma_min(B+U Theta U^T)`
` >= ell(rho)^2 min{mu, f sigma_min(K+S Theta S^T)}.`             (2.1)

This is a deterministic original-coordinate matrix inequality. It does not make a probabilistic decomposition after rotation.

## 3. New theorem: approximate isotropic anchors are enough

The partner's `r+1`-core theorem assumes exact normalized Schur anchors `K_j=c_j I_r`. Exact isotropy is brittle under model perturbation. The following result supplies a quantitative open neighbourhood of that theorem.

### Theorem 3.1 — `QFORM-ROBUST-RPLUS1-APPROX-ANCHOR-STABILITY-v1`

Let `I_0,...,I_r` be `r+1` original-coordinate physical cores, and on each core let the partner data `(B_j,U_j,K_j,S_j,F_j,D_j,rho_j)` satisfy the hypotheses of (2.1). Suppose there are real anchor numbers `c_0,...,c_r` such that

`|c_j-c_k| >= Delta > 0` for `j != k`,                              (3.1)

and

`||K_j-c_j I_r||op <= epsilon` for every `j`,                        (3.2)

where

`0 <= epsilon < Delta/2`.                                            (3.3)

Define

`f_* = min_j lambda_min(F_j)`,
`mu_* = min_j sigma_min(D_j)`,
`ell_* = min_j ell(rho_j)`,

and

`gamma_* = ell_*^2 min{mu_*, f_*(Delta/2-epsilon)}.`                 (3.4)

Then for every symmetric `Theta in Sym_r`, with completely arbitrary signs, eigenvalue magnitudes, and off-diagonal mixing, at least one core satisfies

`sigma_min(B_j+U_j Theta U_j^T) >= gamma_*`.                         (3.5)

More generally let `H=H^T` be arbitrary with no global operator-norm restriction, and let `T=T^T` be an arbitrary-rank dense tail with

`||T||op <= delta`.

Put

`eta=max_j ||H[I_j,I_j]||op`.

If

`eta+delta < gamma_*`,                                                (3.6)

then for

`A=A_0+V Theta V^T+H+T`,

where `U_j=V[I_j,:]`, at least one actual final physical core obeys

`sigma_min(A[I_j,I_j]) >= gamma_*-eta-delta`.                        (3.7)

If the cores are triples, then every independent cap-one product source satisfies

`||p_(X^T A X)||_infinity`
` <= 6 sqrt(pi)/(gamma_*-eta-delta).`                                (3.8)

No magnitude of `Theta` appears in (3.8).

### Proof

Fix arbitrary `Theta=Theta^T`, with eigenvalues `lambda_1,...,lambda_r`. The open intervals

`J_j=(c_j-Delta/2,c_j+Delta/2)`, `j=0,...,r`,

are pairwise disjoint by (3.1). There are `r+1` such intervals but only the `r` real numbers `-lambda_k`. Hence at least one `J_j` contains none of the numbers `-lambda_k`. For that `j`,

`min_k |c_j+lambda_k| >= Delta/2`.                                  (3.9)

Since `S_j` is orthogonal,

`sigma_min(c_j I_r+S_j Theta S_j^T)`
` = min_k |c_j+lambda_k| >= Delta/2`.                               (3.10)

Write `K_j=c_j I_r+E_j`, with `||E_j||op<=epsilon`. Singular-value Weyl applied to (3.10) gives

`sigma_min(K_j+S_j Theta S_j^T) >= Delta/2-epsilon`.                 (3.11)

Insert (3.11) into the completed partner inequality (2.1):

`sigma_min(B_j+U_j Theta U_j^T)`
` >= ell(rho_j)^2 min{mu_j, f_j(Delta/2-epsilon)}`
` >= gamma_*`,                                                       (3.12)

which proves (3.5).

The compression of `H+T` to the chosen core has operator norm at most `eta+delta`. One more singular-value Weyl inequality yields (3.7). If the chosen core is a triple, condition on every original coordinate outside it. The three remaining random coordinates are still independent and retain their density caps; all outside cross terms become only affine terms. Apply the completed newest-Claude Theorem A, equation (1.1), with `s=gamma_*-eta-delta`. This proves (3.8). QED.

### Scope

The theorem is robust to **anisotropic normalized Schur error** of size `epsilon`; exact scalar anchors are not required. It is also robust to a genuinely nonseparable, arbitrary-rank dense matrix tail `T`. The tail is used only in the deterministic final-core singular-value certificate. There is no assertion that `X^T T X` is a small random variable.

The partner's obstruction remains decisive: for `r>=2`, two general matrix-parameter resonance varieties always intersect. Thus this theorem is not reducible to a universal two-core argument for arbitrary `Theta`; `r+1` separated anchors or additional structure really matter.

## 4. Exact target-class family with two arbitrary eigenvalue replacements and nonzero anisotropy

The theorem is non-vacuous even when two eigenvalues are replaced by completely arbitrary values and the final matrix receives a full-rank dense tail.

Take nine original coordinates and three triples

`I_0={1,2,3}`, `I_1={4,5,6}`, `I_2={7,8,9}`.                    (4.1)

Let

`v_1=(e_1+e_4+e_7)/sqrt(3)`,
`v_2=(e_2+e_5+e_8)/sqrt(3)`,
`V=(v_1,v_2)`.                                                   (4.2)

The columns are orthonormal. We construct a baseline `A_0` for which

`A_0 V=V`,                                                        (4.3)

while the three reserve coordinates `e_3,e_6,e_9` are exact eigenvectors of eigenvalue `3`.

Use anchors

`c_0=-2`, `c_1=0`, `c_2=2`, `Delta=2`,                            (4.4)

and a genuinely nonzero anisotropy

`epsilon=1/8`.                                                     (4.5)

For a diagonal vector `d=(d_1,d_2,d_3)`, define the symmetric row-sum-zero matrix

`L(d) = [[d1, (d3-d1-d2)/2, (d2-d1-d3)/2],`
`        [(d3-d1-d2)/2, d2, (d1-d2-d3)/2],`
`        [(d2-d1-d3)/2, (d1-d2-d3)/2, d3]].`                     (4.6)

Thus `L(d)(1,1,1)^T=0`.

Set

`d^+ = (-23/24,-7/24,3/8)`,
`d^- = (-25/24,-3/8,7/24)`,                                     (4.7)

so explicitly

`L_+ = [[-23/24, 13/16, 7/48],`
`       [13/16, -7/24, -25/48],`
`       [7/48, -25/48, 3/8]],`                                   (4.8)

`L_- = [[-25/24, 41/48, 3/16],`
`       [41/48, -3/8, -23/48],`
`       [3/16, -23/48, 7/24]].`                                  (4.9)

Embed `L_+` on coordinates `{1,4,7}`, embed `L_-` on `{2,5,8}`, and set

`A_0 = V V^T + embed_{1,4,7}(L_+) + embed_{2,5,8}(L_-)`
`      + 3(e_3e_3^T+e_6e_6^T+e_9e_9^T).`                        (4.10)

Because both `L_+` and `L_-` kill their flat vector, (4.3) holds exactly. Hence, for **every** symmetric `2 x 2` matrix `Theta`,

`A_Theta=A_0+V Theta V^T`                                        (4.11)

leaves `V^perp` unchanged and changes the two baseline eigenvalues `1,1` on `range(V)` into precisely the two eigenvalues of

`I_2+Theta`.                                                       (4.12)

These two replacement eigenvalues may therefore be arbitrarily large, arbitrarily small, positive, negative, zero, or of opposite signs; `Theta` may have arbitrary off-diagonal mixing.

On each triple `I_j`, the local update matrix is

`U_j=V[I_j,:]`, `F_j=(1/3)I_2`,                                  (4.13)

and the complement is the reserve coordinate, so

`D_j=[3]`, `rho_j=0`, `mu_j=3`, `f_j=1/3`, `ell_j=1`.             (4.14)

The normalized active Schur matrices are exactly

`K_0=diag(-2+1/8,-2-1/8)`,
`K_1=diag(1/8,-1/8)`,
`K_2=diag(2+1/8,2-1/8)`.                                         (4.15)

Thus `||K_j-c_j I||op=1/8`, and Theorem 3.1 gives

`gamma_*=(1/3)(1-1/8)=7/24`.                                     (4.16)

Now add **any** symmetric dense matrix `T`, of arbitrary rank and sign pattern, satisfying

`||T||op <= 1/16`.                                                (4.17)

At least one final physical triple has

`sigma_min((A_Theta+T)[I_j,I_j]) >= 7/24-1/16=11/48`.             (4.18)

Therefore, by newest-Claude Theorem A,

`||p_(X^T(A_Theta+T)X)||_infinity`
` <= 6 sqrt(pi)/(11/48)`
` = 288 sqrt(pi)/11`
` = 46.40606446007169...`                                        (4.19)

uniformly over **every** `Theta in Sym_2`, every dense `T` satisfying (4.17), and every independent cap-one product law.

This whole family lies in the exact global QFORM target class. Before adding `T`, the three reserve vectors `e_3,e_6,e_9` are eigenvectors of eigenvalue `3`; therefore the third largest eigenvalue is at least `3` for every `Theta`. By Weyl after (4.17),

`lambda_3^down(A_Theta+T) >= 3-1/16=47/16>1`.                    (4.20)

So at least three eigenvalues have absolute value at least one, uniformly through the arbitrary two-eigenvalue replacement.

## 5. Why the dense-tail step is genuinely matrix-level

For emphasis, a small operator norm cannot be converted to a uniform small random error under the target's unbounded input laws. Already for

`T=delta e_1e_1^T`, `X_1 ~ Uniform[R,R+1]`,

one has

`X^T T X = delta X_1^2 >= delta R^2` almost surely.               (5.1)

The proof above never uses `X^T T X` perturbatively. It certifies a final original-coordinate physical core and then conditions on all other original coordinates.

## 6. Sanity checks

A deterministic checker accompanying this report verifies the exact construction and stresses the theorem numerically. It checks:

- `||A_0 V-V||op` and `||V^T V-I||op` at machine precision;
- 3,757 grid/rotation choices of `Theta` with no violation of the pre-tail core floor `7/24`;
- 10,000 random `Theta` instances with eigenvalues sampled in `[-10^5,10^5]`, arbitrary rotations, and arbitrary dense symmetric tails rescaled to operator norm `1/16`, with no violation of the final core floor `11/48` or the global third-eigenvalue floor `47/16`.

These computations are sanity checks only; the theorem and family are proved analytically above.

## 7. First unpaid implication

The bare global hypothesis `s_3(A)>=1` does **not** yet force `r+1` approximate-isotropic normalized Schur anchors with universal separation `Delta`, local footprint strength `f_*`, complement gap `mu_*`, shear control `ell_*`, and anisotropy error `epsilon<Delta/2`. That structural extraction remains unpaid.

The next useful dichotomy is therefore precise: in the no-pivot/N3 survivor, derive either

- a finite family of approximate Schur anchors to which Theorem 3.1 applies, possibly after product-preserving coordinate grouping, or
- an already-paid fifth-volume / collective-tail / hub / ridge / physical-pair / physical-triple / scalar-Schur exit.

The partner's intersection theorem proves that an attempted universal **two-core** resonance separation for a fully arbitrary matrix parameter cannot be the missing structural lemma when `r>=2`. Thus the remaining proof must either produce more anchors or exploit additional product-preserving aggregate structure.

**Target-level movement: OPEN -> OPEN.**  
**Mechanism-level movement:** exact isotropic `r+1` anchor control is stable under quantitative anisotropy, arbitrary-magnitude multirank signed spectral replacement, arbitrary off-diagonal mixing in the added spectrum, and a genuinely dense small full-rank matrix tail, with an explicit original-coordinate density bound.

Independent-review status: this new theorem has not been independently reviewed in this run.
