SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-23T02:59:14Z.
attacking: collective-tail cross-core stability under an arbitrary dense operator-norm tail plus arbitrary-magnitude low-rank added spectral directions whose physical cross-cut footprint lies in a protected low-leverage row subspace.

# fleet02/B12 r24 — shielded rank-reserve collective-tail stability

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Additional eigenvalue control  
**Status:** `PROVED_SUPPORTING_STABILITY / PARTNER_APPLIED / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The target remains: for arbitrary independent real ORIGINAL-coordinate inputs with densities at most one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^T A X`, or give a valid counterexample. No moment, support, log-concavity, identical-law, diagonal-basis, or post-rotation independence assumption is used here. Continuity is tracked separately.

This run pays a new **hybrid stability** branch. The first unpaid implication after the theorem is structural:

> From the bare condition `s3(A)>=1`, force either (i) an original-coordinate cross cut carrying two robust singular directions plus a collective tail and a low-leverage row projection that also contains the physical footprints of the arbitrary added spectral directions, or (ii) one of the already-paid hub / physical-pair / physical-triple / scalar-pivot exits.

The theorem below does **not** assert this extraction. It shows that, once such a cut exists, arbitrary full-rank dense tails are paid only by operator norm while arbitrarily large signed additional eigenvalues are paid only by the rank and location of their cross-cut footprint, not by their magnitude.

## 2. Source-pinned completed inputs actually used

1. Required newest-Claude source at
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.
   Its proved Theorem D' says that for an ORIGINAL-coordinate cross block `M=A_IJ`, if the 3-volume row marginals satisfy `alpha_i<=h<3/4`, then

   `||p_Q||inf <= 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) E3(M^T M)^(-1/6)`,

   with arbitrary self blocks, outside couplings and affine terms. No rotated independence is used.

2. Current volume-tail extension at
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md`.
   It proves, for `T2(M)=sum_{j>=3}s_j(M)^2`, any row-space projection `P`, and `epsilon=||(I-P)M||op`,

   `sqrt(alpha_i) <= sqrt(P_ii) + sqrt(3) epsilon/sqrt(T2) sqrt(1-P_ii)`.

   Hence if `max P_ii<=1/2` and `epsilon<=sqrt(T2)/15`, then

   `||p_Q||inf <= Ctail [s1(M)^2 s2(M)^2 T2(M)]^(-1/6)`,

   where `Ctail=9 sqrt(3) e / 2 = 21.186910062820317...`. The density is continuous at this terminal Fourier certificate.

3. Designated partner fleet03/B12 r23 at
   `yspennstate/math-open-problems@4894ced504d555e84620c46029ed08a2af389d9f`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260923T024437Z-qform-eigenvalue-r23/REPORT.md`.
   If a terminal original-coordinate Schur remainder has density cap `B/L`, then any preceding physical scalar pivot chain with `|a_j|>=(4/B)L` preserves the same cap `B/L`. Its proof uses the exact one-sided half-Riesz bound and does not assume independence between the completed square and its dependent remainder.

## 3. Exact deterministic reserve identity

For a rectangular matrix `M`, write

`T2(M)=sum_{j>=3}s_j(M)^2`,

with singular values in decreasing order. Let `r>=0` and `delta>=0`.

### Theorem 3.1 — rank-r plus dense-tail minimax identity

For every `M0`,

`inf_{rank L<=r, ||E||op<=delta} T2(M0+L+E)
 = sum_{k>=r+3} (s_k(M0)-delta)_+^2`.                         (3.1)

Thus an arbitrary-magnitude rank-`r` perturbation can consume at most `r` directions of the collective tail; an arbitrary-rank operator-norm-`delta` perturbation then subtracts at most `delta` from each surviving singular value. No magnitude of `L` appears.

#### Proof

For every rank-`r` `L`, the singular-value rank inequality gives

`s_j(M0+L)>=s_{j+r}(M0)`.

For `||E||op<=delta`, Weyl gives

`s_j(M0+L+E)>= (s_j(M0+L)-delta)_+
             >= (s_{j+r}(M0)-delta)_+`.

Squaring and summing over `j>=3` proves the lower bound in (3.1).

For equality, take an SVD

`M0=sum_k s_k u_k v_k^T`.

Choose

`L=-sum_{k=3}^{r+2} s_k u_k v_k^T`,

omitting indices beyond the matrix rank, and

`E=-sum_{k>=r+3} min(delta,s_k) u_k v_k^T`.

Then `rank L<=r`, `||E||op<=delta`, the first two singular directions are untouched, the next `r` are killed, and each remaining direction is reduced to `(s_k-delta)_+`. Hence `T2` is exactly the right side of (3.1). QED.

The same rank/Weyl inequalities also give, simultaneously,

`s1(M0+L+E)>= (s_{r+1}(M0)-delta)_+`,
`s2(M0+L+E)>= (s_{r+2}(M0)-delta)_+`.                       (3.2)

## 4. Main stability theorem: shielded low-rank spectrum plus arbitrary dense tail

Let `I,J` be disjoint ORIGINAL-coordinate sets. Put

`M0=A0[I,J]`.

Let `P` be an orthogonal projection on the I-row coordinate space with

`max_i P_ii <= 1/2`.                                           (4.1)

Consider a final symmetric quadratic matrix whose cross block is

`M=M0+L+E`,                                                     (4.2)

where

`rank L<=r`,       `(I-P)L=0`,       `||E||op<=delta`.          (4.3)

The intended dense perturbation is `E=T[I,J]` for an **arbitrary symmetric full-rank** matrix `T` with `||T||op<=delta`; compression gives `||E||op<=delta`. We never claim that `X^T T X` is a small random variable.

Define

`a1=(s_{r+1}(M0)-delta)_+`,
`a2=(s_{r+2}(M0)-delta)_+`,
`B=[sum_{k>=r+3}(s_k(M0)-delta)_+^2]^(1/2)`,
`epsilon0=||(I-P)M0||op`.                                      (4.4)

### Theorem 4.1 — `QFORM-SHIELDED-RANK-RESERVE-TAIL-STABILITY-v1`

If

`a2>0`, `B>0`, and `epsilon0+delta <= B/15`,                    (4.5)

then for every independent cap-one product source and arbitrary final self blocks, outside blocks and affine terms,

`boxed: ||p_Q||inf <= (9 sqrt(3) e / 2) (a1 a2 B)^(-1/3).`     (4.6)

The terminal density supplied by this Fourier branch is continuous.

#### Proof

By (3.2),

`s1(M)>=a1`, `s2(M)>=a2`.

By Theorem 3.1,

`T2(M)>=B^2`.                                                    (4.7)

The shielding hypothesis `(I-P)L=0` gives

`||(I-P)M||op
 <=||(I-P)M0||op+||(I-P)E||op
 <=epsilon0+delta
 <=B/15
 <=sqrt(T2(M))/15`.                                             (4.8)

Therefore the completed volume-tail theorem applies to the **actual final original-coordinate cross block**. Since

`E3(M^T M)>=s1(M)^2 s2(M)^2 T2(M)
             >=a1^2 a2^2 B^2`,                                 (4.9)

its sharp coefficient gives (4.6). QED.

### Arbitrarily large added eigenvalues

Suppose the added spectral block in the full symmetric matrix is

`S=sum_a tau_a v_a v_a^T`,                                     (4.10)

with completely arbitrary real coefficients `tau_a` (small, large, either sign). Its cross compression is

`L=S[I,J]=sum_a tau_a (v_a)_I (v_a)_J^T`.

If the span of the I-side footprints `(v_a)_I` has dimension at most `r` and is contained in `range(P)`, then (4.3) holds **independently of every `|tau_a|`**. Thus the theorem is magnitude-free for those additional eigenvalues. It charges only their physical cross-cut rank/location and charges the dense arbitrary-rank tail only by `delta`.

This is deliberately an original-coordinate statement. Spectral rotation is used only to describe the deterministic matrix update; no transformed random coordinates are declared independent.

## 5. Required e5f result applied directly

Condition (4.8) and the current marginal inequality imply, for every I-row,

`sqrt(alpha_i)
 <=1/sqrt(2) + (sqrt(3)/15)/sqrt(2)
 =(1+sqrt(3)/15)/sqrt(2)`,

so

`alpha_i <= (1+sqrt(3)/15)^2/2
          =0.6221367205... < 2/3`.                               (5.1)

Apply the **completed e5f Theorem D'** with `h=2/3` directly to the actual final `M`. Its constant is

`6 sqrt(e) (4/3)^(-1/2) (1/3)^(-1)=9 sqrt(3e)`,

and (4.9) gives the source-valid fallback

`boxed: ||p_Q||inf <= 9 sqrt(3e) (a1 a2 B)^(-1/3).`             (5.2)

The c241 tail extension sharpens only the coefficient in this same branch, from `9 sqrt(3e)` to `9 sqrt(3)e/2`, yielding (4.6). Thus the required e5f result is consumed at an actual inequality rather than cited as background.

## 6. Concrete exact target-class family with an unbounded added eigenvalue

Take `m=1024` and let `U=H_m/sqrt(m)` be a normalized symmetric Sylvester-Hadamard matrix. Let `u1,u2,u3` be its first three columns and put

`mu=0.04`,
`M0=U diag(2,2,2,mu,...,mu) U^T`,
`A0=[[0,M0],[M0,0]]`.                                           (6.1)

Let

`P=u1 u1^T+u2 u2^T+u3 u3^T`                                    (6.2)

on the first bank. Since every Hadamard entry has modulus `m^(-1/2)`,

`P_ii=3/m=3/1024<1/2`.                                         (6.3)

Set

`z=(u1,u1)/sqrt(2)`                                             (6.4)

in the two-bank ambient space. Since `A0 z=2z`, the rank-one spectral update

`S_tau=tau z z^T`                                               (6.5)

**literally replaces one eigenvalue `2` of `A0` by `2+tau`**, with `tau` arbitrary in `R`. Hence the added eigenvalue can tend to `+infinity`, `-infinity`, cross zero, or be arbitrarily small. Its cross-block contribution is

`L_tau=(tau/2)u1 u1^T`,                                        (6.6)

which has rank one and lies in `range(P)` for every `tau`.

Now add any real symmetric dense `T` with

`||T||op<=delta=0.01`,                                         (6.7)

and set

`A=A0+S_tau+T`.                                                 (6.8)

This remains in the exact QFORM target class for every real `tau`: before `T`, five eigenvalues other than the modified `2+tau` still have modulus exactly `2`; after (6.7), singular-value Weyl gives at least five eigenvalues/singular values of modulus at least `1.99>1`.

For the protected cross block, `r=1` and the baseline singular values are three copies of `2` followed by `1021` copies of `0.04`. Therefore

`a1=a2=2-0.01=1.99`,
`B=0.03 sqrt(1021)=0.9585927185202274...`,
`epsilon0=0.04`.

The final leakage is at most

`epsilon0+delta=0.05`,

whereas

`B/15=0.06390618123468182...`,                                 (6.9)

so the gate holds uniformly in `tau` and uniformly over every dense `T` satisfying (6.7). Theorem 4.1 gives

`boxed: ||p_(X^T A X)||inf <=13.58170198712074...`              (6.10)

for **all** independent input densities at most one, every `tau in R`, and every such dense `T`.

Using only the required e5f D' theorem gives the still-uniform source-valid bound

`||p_(X^T A X)||inf <=16.47543733253745...`.                    (6.11)

The self blocks created by `S_tau` have norm of order `|tau|`; they are not discarded or treated as an independent convolution. The completed cross-volume theorem permits them to remain arbitrary.

## 7. Designated partner fleet03/B12 actually applied

The terminal constant in (6.10) is

`Bterm=13.58170198712074...` at scale `L=1`.

The fleet03/B12 r23 sharp one-sided scalar-Schur compiler therefore gives the no-loss pivot threshold

`4/Bterm=0.2945138984637656...`.                                (7.1)

Hence any number of preceding **ORIGINAL-coordinate scalar Schur extensions**, with arbitrary pivot signs and arbitrary cross couplings, preserves the same cap (6.10) provided every pivot satisfies

`|a_j|>=0.2945138984637656...`.                                 (7.2)

No independence between the completed square and the terminal quadratic remainder is needed. If the chain is also being used to peel extra large spectral directions, the partner's threshold-preserving Schur result supplies the separate spectral-count bookkeeping; the density propagation itself is exactly (7.2).

More generally, if the parameters in Theorem 4.1 are normalized so that

`a1>=c1 L`, `a2>=c2 L`, `B>=c3 L`,

then the terminal normalized constant is

`Btail=(9 sqrt(3)e/2)(c1 c2 c3)^(-1/3)`,

and every preceding scalar pivot of magnitude at least `(4/Btail)L` preserves that same terminal cap. This composes an arbitrary-rank dense-tail certificate with arbitrary-magnitude low-rank spectral additions and then with an arbitrary-length dependence-safe scalar extension chain.

## 8. Why small matrix norm is never used as small random noise

The dense tail `T` is used only through deterministic singular-value and leakage inequalities on the **actual final matrix**. It is false that `||T||op<=delta` makes `X^T T X` uniformly small for the target input class: for

`T=delta e1 e1^T`, `X1~Uniform[R,R+1]`,

one has `X^T T X=delta X1^2>=delta R^2` almost surely, which diverges with `R`. No step above uses such a probabilistic perturbation assertion.

## 9. What this does and does not settle

**Paid in this run.** A magnitude-free stability theorem for arbitrary signed low-rank additional spectral blocks whose physical cross-cut footprint is shielded inside a diffuse row subspace, simultaneously with an arbitrary-rank dense operator-norm tail. The exact minimax identity (3.1) quantifies how many collective-tail directions an arbitrary rank-`r` update can destroy. A literal rank-one eigenvalue replacement can pass from `-infinity` to `+infinity` while (6.10) remains uniform, even after an arbitrary dense full-rank `0.01` tail.

**Still unpaid.** The bare target `s3(A)>=1` does not yet force a cut/projection satisfying (4.1)-(4.5). In particular, an added direction may have high physical leverage on every promising cut; then forcing its left footprint into `P` can break the `max P_ii<=1/2` gate. That is a hub/concentrated-volume alternative, not a reason to rotate the product source. The remaining full-proof step is an exhaustive original-coordinate extraction: either produce the shielded collective-tail certificate, or pay the concentrated direction with a hub/grouped-bank/physical-pivot theorem before any reciprocal local conditioning cost.

Therefore **FULL QFORM remains OPEN / NOT PROVED / NOT DISPROVED**. Continuity is proved only in the terminal Fourier branch; the scalar backward compiler does not by itself propagate a continuous representative.

## 10. Checks

`CHECK.py` performs deterministic sanity checks only; it is not evidence replacing the proof. It verifies 900 random rank/Weyl inequalities, 100 exact constructions attaining (3.1) to floating-point error below `5e-14`, and the concrete constants in Section 6. Recorded output is in `CHECK_OUTPUT.txt`.
