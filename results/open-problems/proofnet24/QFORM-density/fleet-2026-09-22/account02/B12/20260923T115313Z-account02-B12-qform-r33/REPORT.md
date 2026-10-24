SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-23T11:53:13Z.
attacking: adaptive singular-reserve dilution — absorb an arbitrary-magnitude low-rank spectral packet, spend additional reserve directions automatically against a many-mode residual tail, and pay a genuinely dense tail only through its matrix operator norm.

# account02/B12 r33 — adaptive reserve envelope and Schatten-2 tail dilution

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Additional eigenvalue control  
Status: **PROVED SUPPORTING STABILITY THEOREM / PINNED D5 APPLIED / LATEST PARTNER RESULT APPLIED / EXACT TARGET-CLASS FAMILY / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## First unpaid implication

The full target is still OPEN. The theorem below is a stability/compiler result, not the missing structural extraction. Starting only from the global assumption `s_3(A)>=1`, one still has to force either

1. an ORIGINAL-coordinate cross cut with a sufficiently long singular-value reserve,
2. a bounded physical compression with such reserve,
3. or an already-paid fifth-volume / three-volume / collective-tail / grouped-bank / hub / ridge / pair / triple / Schur exit.

The live diffuse exact-rank-three obstructions prohibit simply asserting one uniformly conditioned small physical block or one universal rank-three cross cut.

What changes in this run is the tail parameter. The preceding account02/B12 theorem paid a residual hostile cross packet by its operator norm after a fixed rank budget. Here extra baseline reserve directions are used to dilute a many-mode residual packet: the largest declared packet remains completely magnitude-free, while the rest can be charged by an adaptive singular-value envelope or, more coarsely, by one Schatten-2 norm divided by the square root of the unused reserve count.

## 1. Sources actually used

Required pinned newest-Claude source:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`
- `FOURIER_ROUTE_REPORT.md`
- `COUNTEREXAMPLE_SEARCH.md`.

The equation-level result used below is the proved D5 theorem: for an ACTUAL original-coordinate cross block `M=A[I,J]`,

`Z5=e_5(M^T M)` and `||p_Q||_infinity <= 5 sqrt(2e) Z5^(-1/10)`

with no row-marginal condition. Same-bank quadratic blocks, all outside couplings and affine terms remain arbitrary. In particular, `s_5(M)>=gamma` implies

`||p_Q||_infinity <= 5 sqrt(2e)/gamma`.

Latest designated partner actually used:

- account03/B12 r32,
- `yspennstate/math-open-problems@eb3111d97a233b15ea18088a2cf97bc17d9d4c25`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T114533Z-qform-eigenvalue-r32/REPORT.md`.

Its proved singular-reserve inequality for real symmetric matrices is

` s_j(B+R) >= s_{j+k}(B)-s_{k+1}(R). `

The partner also records the dependence-safe finite physical-core receiver: an ACTUAL `m`-coordinate principal block with three singular values at least `gamma` gives

`||p_Q||_infinity <= 2 sqrt(6 pi m)/gamma`

after conditioning only on outside ORIGINAL coordinates.

Relevant live corrections are respected throughout: small matrix norm is not a law-uniformly small random quadratic perturbation for unbounded cap-one inputs; no independence is inferred after spectral rotation; arbitrary dependent projected densities cannot replace original product provenance; and no universally good single minor/cross-rank-three cut is assumed.

## 2. Adaptive reserve envelope — rectangular version

Let `M0,L,R,T` be real matrices of the same rectangular size. Let their singular values be decreasing. Assume

`rank L <= r`, `||T||op <= delta`.

Here `L` is the arbitrary-magnitude packet, `R` is the residual spectral/cross packet, and `T` is the genuinely dense small tail. Let `d=min(number of rows, number of columns)`.

### Theorem 2.1 (`QFORM-ADAPTIVE-RESERVE-ENVELOPE-v1`)

For every `q>=1` with `q+r<=d`, define

`Gamma_q := max_{0<=p<=d-r-q} [ s_{q+r+p}(M0) - s_{p+1}(R) ] - delta.`

Then

`boxed: s_q(M0+L+R+T) >= Gamma_q.`

The amplitudes and signs represented in `L` do not appear.

### Proof

Fix an admissible `p`. Let `R_p` be a best rank-`p` approximation to `R` in operator norm. Then

`rank(L+R_p) <= r+p`,

and Eckart--Young gives

`||R-R_p||op = s_{p+1}(R)`.

The standard singular-value rank-perturbation inequality, the rectangular analogue of the mechanism used in the partner's symmetric theorem, gives

`s_q(M0+L+R_p) >= s_{q+r+p}(M0)`.

Restore the residual `R-R_p` and the full-rank dense tail `T`. Weyl's singular-value Lipschitz inequality yields

`s_q(M0+L+R+T)`
` >= s_{q+r+p}(M0)-s_{p+1}(R)-delta.`

This holds for every admissible `p`; maximize. QED.

Interpretation: `p` is chosen *after seeing the reserve/tail profile*. The proof may spend additional baseline reserve directions against the largest residual singular modes. This is why a residual packet need not be small in operator norm.

## 3. Schatten-2 dilution corollary and sharp aggregate constant

Suppose, more coarsely, that for some `N>=r+q`,

`s_N(M0)>=kappa`.

Put

`ell := N-r-q+1`.

Taking `p=N-r-q` in Theorem 2.1 and using

`s_ell(R) <= ||R||F/sqrt(ell)`

produces

`boxed: s_q(M0+L+R+T) >= kappa-delta-||R||F/sqrt(N-r-q+1).`      (3.1)

Thus `r` hostile directions are completely free, while an arbitrarily high-rank residual packet is paid only by its total squared singular-value mass divided by the square root of the available reserve count.

The coefficient is sharp given only `(N,r,q,kappa,||R||F)`. Take `M0=kappa I_N`; let `L` cancel the first `r` diagonal directions; let `R` equal `-a` on the next `ell=N-r-q+1` coordinates and zero elsewhere. Then `||R||F=a sqrt(ell)`, exactly `q-1` untouched coordinates remain at `kappa`, and

`s_q(M0+L+R)=kappa-a=kappa-||R||F/sqrt(ell)`.

A further diagonal `T` equal to `-delta` on the surviving nonzero directions has `||T||op=delta` and attains the additional `-delta` loss. Hence neither the `1/sqrt(ell)` factor nor the coefficient of the dense operator-norm tail can be improved from this aggregate information alone.

More generally the same argument gives, for any Schatten exponent `a>0`,

`s_q >= kappa-delta-||R||_{S_a}/ell^(1/a)`

whenever that Schatten quantity is finite; the Hilbert--Schmidt case `a=2` is the natural spectral-energy form used below.

## 4. Required D5 application: a dimension-free cross-block compiler

Let `I,J` be disjoint sets of ORIGINAL coordinates and write the final matrix as

`A=A0+S+T`, `M0=A0[I,J]`.

Split the hostile cross footprint as

`S[I,J]=L+R`, `rank L<=r`,

and assume `||T||op<=delta`.

Apply Theorem 2.1 with `q=5`. If

`Gamma_5 := max_p [s_{5+r+p}(M0)-s_{p+1}(R)]-delta >0`,

then the ACTUAL final cross block `M=A[I,J]` has `s_5(M)>=Gamma_5`. Hence

`e_5(M^T M) >= product_{j=1}^5 s_j(M)^2 >= Gamma_5^10`.

Substitution into the pinned completed D5 theorem gives the real final-matrix inequality

`boxed: ||p_{X^T A X}||_infinity <= 5 sqrt(2e)/Gamma_5.`          (4.1)

This branch has a continuous density because the D5 proof supplies an integrable characteristic function. No diagonalization of the input law occurs.

The Schatten-2 form is especially simple. If `M0` has `N>=r+5` singular values at least `kappa` and

`gamma := kappa-delta-||R||F/sqrt(N-r-4) >0`,

then

`boxed: ||p_Q||_infinity <= 5 sqrt(2e)/gamma.`                     (4.2)

All same-bank blocks and all outside couplings remain arbitrary.

## 5. Literal eigenvalue updates: global spectral coefficients versus physical cross energy

Suppose

`S=sum_a tau_a v_a v_a^T`

along orthonormal eigenvectors of `A0`, so the corresponding eigenvalues are literally replaced by `lambda_a+tau_a`.

Choose a set `G` of updates whose `I`-side footprints span at most `r` dimensions. Then

`L=sum_{a in G} tau_a (v_a)_I (v_a)_J^T`

has rank at most `r`, **regardless of how many indices are in G and regardless of every magnitude and sign `tau_a`**.

For the remaining updates `B`, let

`R=sum_{a in B} tau_a (v_a)_I (v_a)_J^T`.

The cross compression is a contraction in Frobenius norm, so

`||R||F <= ||sum_{a in B} tau_a v_a v_a^T||F = (sum_{a in B} tau_a^2)^(1/2).`

Therefore (4.2) gives a source-valid eigenvalue-control theorem in which an arbitrarily large collection of replacements may be magnitude-free through low-dimensional physical footprint, while every remaining replacement is charged only through an `l2` spectral tail. This is strictly matrix-level information; it does not say the random variable `X^T S X` is small.

## 6. Exact target-class family: arbitrarily many unbounded replacements + a 63-mode tail + dense noise

Take two 64-coordinate banks `I,J`, with bases `e_1,...,e_64` and `f_1,...,f_64`, and add `k` spectator coordinates `h_1,...,h_k`. Define

`A0 = [[0, 2 I_64],[2 I_64,0]] direct_sum 2 I_k`.

For `j=1,...,64` put

`g_j=(e_j+f_j)/sqrt(2)`, `q_j=(e_j-f_j)/sqrt(2)`.

Every `g_j` and spectator has eigenvalue `+2`; every `q_j` has eigenvalue `-2`.

### Arbitrarily large packet

Let

`W=span{g_1,h_1,...,h_k}`

and choose any orthonormal basis `z_0,...,z_k` of `W`. For arbitrary real coefficients `tau_0,...,tau_k`, set

`S_big=sum_{a=0}^k tau_a z_a z_a^T`.

Because `A0=2I` on `W`, this literally replaces `k+1` eigenvalues `2` by `2+tau_a`. The number `k+1` is unbounded and every coefficient may tend independently to either sign of infinity.

Exactly as in the preceding B12 low-numerical-rank construction, all `I`-side footprints of `z_a` are collinear with `e_1`, so

`rank S_big[I,J] <=1`.

Thus the entire huge packet is the rank-one `L` term and costs no magnitude.

### Collective residual packet

Now add

`S_tail=sum_{j=2}^{64} g_j g_j^T`.

This literally replaces the remaining 63 positive eigenvalues `2` by `3`. Across the physical cut,

`S_tail[I,J]=(1/2) diag(0,1,...,1)`,

so

`||S_tail[I,J]||F=sqrt(63)/2`.

Finally add **any** symmetric dense matrix `T` on all coordinates with

`||T||op<=1/4`.

For the baseline cross block `M0=2I_64`, use `r=1`, `N=64`, `q=5`, `kappa=2`. The unused reserve count is

`ell=64-1-5+1=59`.

Equation (3.1) gives the actual final cross singular gap

`gamma >= 2-1/4-(sqrt(63)/2)/sqrt(59)`
`      = 7/4 - (1/2)sqrt(63/59)`
`      = 1.2333287771296209...`.

Therefore the required D5 theorem gives, uniformly in `k`, every orthonormal basis of `W`, all arbitrary signed `tau_a`, every admissible dense `T`, and every independent cap-one product law,

`boxed: ||p_Q||_infinity <= 5 sqrt(2e)/gamma = 9.452645656349882... .`    (6.1)

This is genuinely in the exact owner target class. The 64 vectors `q_j` remain an invariant `-2` eigenspace before `T`, regardless of all eigenvalue replacements. On that 64-dimensional subspace the perturbed quadratic form is at most `-2+1/4=-7/4`; by min--max the final matrix has at least 64 eigenvalues `<=-7/4<-1`. Hence the global three-large-eigenvalue hypothesis is satisfied with enormous margin.

The example simultaneously contains:

- arbitrarily many independently arbitrary eigenvalue replacements with no magnitude payment;
- a 63-mode nonzero residual spectral tail;
- an arbitrary full-rank dense operator-norm tail;
- and a dimension-free density constant.

## 7. Direct application of the latest account03/B12 partner result

The partner r32 theorem is symmetric and can be compiled into a localized physical-core analogue of Theorem 2.1 without any probabilistic rotation.

Let an ACTUAL original-coordinate principal block have

`B_final=B0+L+R+T`,

where all matrices are symmetric, `rank L<=r`, `||T||op<=delta`. For each `p`, let `R_p` retain the `p` largest absolute eigenmodes of `R`. Then `rank(L+R_p)<=r+p`. Applying the partner's proved inequality with `j=3` to the concrete matrix `B0+(L+R_p)` gives

`s_3(B0+L+R_p) >= s_{r+p+3}(B0)`.

Restoring the residual and dense tail yields

`boxed: s_3(B_final) >= max_p [s_{r+p+3}(B0)-s_{p+1}(R)]-delta.`   (7.1)

If the right side is `gamma>0`, the same partner report's dependence-safe physical receiver gives, for a core of size `m`,

`boxed: ||p_Q||_infinity <= 2 sqrt(6 pi m)/gamma.`                 (7.2)

Equation (7.1) is the required real use of the latest designated partner result. It allows the spectral packet to hit the protected physical core in arbitrary orientation; additional reserve modes, not small random-error reasoning, absorb the hostile modes.

## 8. Why the dense-tail handling is legal

No step uses `||T||op<=delta` to infer that `X^T T X` is small. That inference is false for the allowed unbounded product laws: already `T=delta e_1e_1^T` and `X_1` uniform on `[R,R+1]` make `X^T T X>=delta R^2` almost surely.

Here `delta` is used only in Weyl inequalities for the **actual final matrix certificate**. Probability enters only after a valid original-coordinate cross block or physical core has been certified. In particular, D5 works on the original banks, and the physical receiver conditions on outside original coordinates, preserving the required independent cap-one inputs.

## 9. Remaining gap

The theorem removes a quantitative weakness of fixed-r operator-tail control: a high-rank residual spectral packet can now be absorbed collectively by surplus baseline singular directions. It does **not** prove that the bare global condition `s_3(A)>=1` provides such a surplus on any original-coordinate cut/core. The next useful structural step is therefore:

> in the live no-pivot/N3 survivor, force either an original-coordinate cut/core with a reserve count large enough that the adaptive envelope is positive, or an already-paid volume/hub/ridge/grouped-bank/pair/triple/Schur certificate before any reciprocal small physical minor is paid.

No claim of full QFORM closure or counterexample is made.
