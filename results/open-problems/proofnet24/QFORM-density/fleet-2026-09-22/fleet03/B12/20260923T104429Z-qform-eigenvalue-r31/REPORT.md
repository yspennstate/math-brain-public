SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-23T10:44:29Z.

attacking: compression-footprint stability for arbitrary added spectrum; charge only the update seen inside a protected physical compression and let arbitrarily large cross/complementary spectrum pass for free.

# fleet03/B12 r31 — compression-footprint stability and a sharper partner Schur branch

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T104429Z-qform-eigenvalue-r31`  
Assignment: Additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM / PARTNER RESULT APPLIED / NEWEST VOLUME RESULT APPLIED / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**  
Continuity: **not claimed for the compression branch; proved for the separate fractional-volume branch in its exact scope**.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and change of mechanism

The full target remains: for every dimension, every independent real input with marginal probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal density bound for `X^T A X`, or give a valid counterexample. No moment, Gaussian, compact-support, log-concavity, connected-support, or diagonal-basis assumption is used here.

The preceding B12 runs controlled additional spectrum using Schur complements, spectral windows, and rank budgets. This run changes the mechanism. The key observation is that a **Hermitian compression already inherits its signed threshold counts upward to the full physical block**, regardless of the magnitude of the cross block or the complementary block. Consequently, for additional-eigenvalue stability, a perturbation needs to be charged only through its compression onto a protected subspace. The cross part of the added spectrum can be arbitrarily large.

An early checkpoint in this same immutable run explored a weaker improvement of the previous rank-budget theorem from a `2k` to a `k` mode loss. The compression argument below strictly supersedes that checkpoint in the protected-compression setting: the cross leakage costs **zero protected modes**, not `k` or `2k`. The failed/weaker checkpoint is preserved as required.

## 2. Sources actually consumed


The designated partner result actually used is:

- `yspennstate/math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260923T081758Z-fleet04-B12-complementary-schur-shield-r4/REPORT.md`.

Its physical-core setup and dependence-safe conditional receiver are applied in Section 6. The new compression inequality sharpens its spectral denominator in that setup.

The newest required Claude-derived volume theorem actually used is:

- `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`
- `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Its near-diffuse cross-block stability theorem is applied to an arbitrary signed spectral update in Section 7.

The finite-dimensional density receiver is also source-pinned at:

- `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`
- `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`, Theorem 3.1 / Corollary 4.1.

Current corrections are respected: no pointwise law-uniform quadratic-phase decay, no independence after spectral rotation, no arbitrary-joint rank-three coarea bound, no worst conditional-density-moment gate, and no naive fiber-sup integration.

## 3. Threshold counts of a compression are inherited by the full matrix

For a real symmetric matrix `H`, define

\[
N_+(H;L)=\#\{j:\lambda_j(H)\ge L\},\qquad
N_-(H;L)=\#\{j:\lambda_j(H)\le-L\},
\]

and `N_abs=N_++N_-`.

### Lemma 3.1 (`QFORM-COMPRESSION-THRESHOLD-INHERITANCE-v1`)

Let `E` be any subspace of `R^m`, and let

\[
C=P_EH P_E\big|_E
\]

be the Hermitian compression of `H` to `E`. Then for every `L>0`,

\[
\boxed{
N_+(H;L)\ge N_+(C;L),\qquad
N_-(H;L)\ge N_-(C;L).
}
\tag{3.1}
\]

In particular,

\[
\boxed{N_{\rm abs}(H;L)\ge N_{\rm abs}(C;L).}
\tag{3.2}
\]

### Proof

Let `p=N_+(C;L)`. The spectral subspace of `C` corresponding to `[L,infinity)` is a `p`-dimensional subspace `F_+ subset E` on which

\[
x^THx=x^TCx\ge L\|x\|^2.
\]

By the Courant--Fischer variational principle, `lambda_p(H)>=L`, proving the first inequality. Apply the same argument to `-H` and `-C` to obtain the second inequality. The positive and negative spectral sets are disjoint, so their counts add, yielding (3.2). QED.

This is deterministic matrix algebra. The subspace `E` may be rotated for the purpose of proving a spectral fact; the random vector is never rotated.

## 4. Main stability theorem: only the protected compression footprint is charged

Let `I` be an ACTUAL set of original coordinates, `|I|=m`. Inside the physical coordinate space `R^I`, let `E` be any deterministic subspace. Let `B_0=B_0^T` be a reference symmetric operator on `E` with

\[
N_{\rm abs}(B_0;\mu)\ge3,
\qquad \mu>0.
\tag{4.1}
\]

Let the **final** actual physical principal block be

\[
H=A[I,I],
\]

and put

\[
C=P_EH P_E\big|_E,
\qquad
\delta=\|C-B_0\|_{\rm op}.
\tag{4.2}
\]

### Theorem 4.1 (`QFORM-COMPRESSION-FOOTPRINT-STABILITY-v1`)

If `delta<mu`, then

\[
\boxed{
N_{\rm abs}(A[I,I];\mu-\delta)\ge3.
}
\tag{4.3}
\]

Consequently, for independent cap-one input laws, with **all matrix blocks outside `I` and all outside couplings arbitrary**,

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le
\frac{2\sqrt{6\pi m}}{\mu-\delta}.
}
\tag{4.4}
\]

No condition is imposed on

- `P_E H P_{E^perp}`;
- `P_{E^perp} H P_{E^perp}`;
- their ranks, signs, or operator norms;
- any eigenvalues or couplings outside the physical block `I`.

Thus arbitrary additional smaller or larger eigenvalues of either sign are harmless unless they alter the protected compression itself.

### Proof

Suppose `B_0` has `p` eigenvalues at least `mu` and `q` eigenvalues at most `-mu`, with `p+q>=3`. Since

\[
\|C-B_0\|_{\rm op}\le\delta,
\]

Hermitian Weyl perturbation gives

\[
N_+(C;\mu-\delta)\ge p,
\qquad
N_-(C;\mu-\delta)\ge q.
\tag{4.5}
\]

Lemma 3.1 transfers both signed threshold counts from the compression `C` to the full physical block `H`, proving (4.3).

Now condition on every ORIGINAL coordinate outside `I`. The `m` variables in `I` remain independent with the same density caps. All outside cross terms become arbitrary deterministic affine terms and the outside quadratic term becomes an additive constant. The conditional quadratic matrix is exactly `A[I,I]`, which by (4.3) has three actual eigenvalues of modulus at least `mu-delta`. The finite-dimensional projected-gradient theorem therefore gives the uniform conditional bound

\[
\frac{2\sqrt{6\pi m}}{\mu-\delta}.
\]

Averaging the conditional interval bounds proves (4.4). No convolution or post-rotation independence is used. QED.

## 5. Spectral-update form: arbitrarily large added eigenvalues can be free

Write a final matrix as

\[
A=A_0+R,
\qquad
R=\sum_r \tau_r v_rv_r^T,
\tag{5.1}
\]

where the `tau_r` may have either sign and arbitrarily large magnitude. Suppose the protected compression of the baseline satisfies

\[
B_0=P_EA_0[I,I]P_E\big|_E,
\qquad
N_{\rm abs}(B_0;\mu)\ge3.
\]

Then the exact perturbation charged by Theorem 4.1 is only

\[
\delta_E=
\left\|
P_E R[I,I]P_E\big|_E
\right\|_{\rm op}.
\tag{5.2}
\]

In particular,

\[
\boxed{
\delta_E
\le
\sum_r |\tau_r|\,\|P_E(v_r|_I)\|_2^2.
}
\tag{5.3}
\]

Hence

\[
\sum_r |\tau_r|\,\|P_E(v_r|_I)\|_2^2<\mu
\]

is a simple sufficient condition for (4.4). This permits individual `|tau_r|` to be arbitrarily large if their squared overlap with the protected physical subspace is correspondingly small. Every direction orthogonal to `E` inside the physical core costs **exactly zero**, regardless of its eigenvalue magnitude. Signed cancellations can make the exact norm in (5.2) even smaller than the upper bound (5.3).

The threshold `mu-delta_E` is sharp from this information: take `B_0=mu I_3` and a compressed update `-delta_E I_3`. Conversely, some footprint control is necessary in general: `B_0=I_3` and update `R=-I_3` cancel the protected curvature completely.

## 6. Actual application of the completed fleet04/B12 result: the shear loss disappears

The designated partner fleet04/B12 r4 works on an ACTUAL physical block and, for deterministic matrix algebra, decomposes it using `W=Ran(U)` and `Z=W^perp`. Its matrix is

\[
H_0=B+U\Theta U^T,
\]

with complementary compression

\[
D=Z^TBZ.
\tag{6.1}
\]

Because `Z^TU=0`, one has the exact identity

\[
\boxed{Z^TH_0Z=D.}
\tag{6.2}
\]

Thus `D` is not merely a Schur-complement ingredient: it is literally a Hermitian compression of the final hostile-update matrix `H_0`. Therefore Lemma 3.1 immediately implies

\[
N_{\rm abs}(D;\mu)\ge3
\quad\Longrightarrow\quad
N_{\rm abs}(H_0;\mu)\ge3,
\tag{6.3}
\]

with **no dependence on the cross block `B_12`, no shear factor, and no need that all of `D` be invertible**. If an additional arbitrary symmetric local tail `T` satisfies

\[
\|T[I,I]\|_{\rm op}\le\delta<\mu,
\]

then

\[
\boxed{s_3(H_0+T[I,I])\ge\mu-\delta.}
\tag{6.4}
\]

Applying the partner's dependence-safe physical-core density receiver at the actual inequality (6.4) gives

\[
\boxed{
\|p_Q\|_\infty
\le
\frac{2\sqrt{6\pi m}}{\mu-\delta}.
}
\tag{6.5}
\]

This strictly sharpens the partner's valid complementary-Schur bound `ell(rho)^2 mu-delta` whenever `rho>0`; it does not invalidate their factorization. Their shear estimate remains useful in settings where the protected object is not itself a compression with the required threshold count.

### Concrete partner-family improvement

Use the partner's five-coordinate example with

\[
D=\operatorname{diag}(2,-2,2),
\]

but now allow the top block, the cross block `B_12`, and the symmetric update `Theta` to be completely arbitrary and unbounded. Add any dense local tail with operator norm at most `1/5`. Then (6.4) gives

\[
s_3(H)\ge 2-\frac15=\frac95,
\]

and hence

\[
\boxed{
\|p_Q\|_\infty
\le
\frac{2\sqrt{30\pi}}{9/5}
=10.7868106253\ldots .
}
\tag{6.6}
\]

The partner's earlier shear calculation on its more specific displayed cross block gave a gap about `1.0192` and a density constant below `19.051`; the compression argument removes that loss entirely.

## 7. Newest fractional-volume theorem applied to a complementary update footprint

The compression theorem pays perturbations that alter a protected compression. The newest volume theorem pays a different footprint: the update's **actual original-coordinate cross block**.

Let `J,K` be disjoint sets of ORIGINAL coordinates and suppose a baseline cross block

\[
M_0=A_0[J,K]
\]

satisfies

\[
s_3(M_0)\ge a>0,
\qquad
\max_i(P_{\operatorname{Ran}M_0})_{ii}\le\frac12.
\tag{7.1}
\]

For the arbitrary signed spectral update (5.1), put

\[
E=R[J,K].
\]

The deterministic spectral decomposition gives the actual inequality

\[
\boxed{
\|E\|_{\rm op}
\le
\sum_r |\tau_r|\,\|(v_r)_J\|_2\,\|(v_r)_K\|_2.
}
\tag{7.2}
\]

Therefore, if

\[
\sum_r |\tau_r|\,\|(v_r)_J\|_2\,\|(v_r)_K\|_2
\le \frac a{16},
\tag{7.3}
\]

the required newest volume-stability theorem applies to the **actual final cross block** `M=M_0+E` and yields

\[
\boxed{
\|p_Q\|_\infty
\le
\frac{24\sqrt3\,e}{5a}
=\frac{22.5993707337\ldots}{a}<\frac{23}{a}.
}
\tag{7.4}
\]

This branch has a continuous `C_0` density. Every self block on `J` and `K`, every outside quadratic block, every outside coupling, and every affine term generated by conditioning is unrestricted by the theorem.

In particular, an added eigenvalue of arbitrarily large magnitude costs zero in (7.3) when its eigenvector is supported entirely on one side of the cut. Thus large extra spectrum can be harmless in two independent senses:

1. zero/small **protected-compression footprint**, paid by Theorem 4.1;
2. zero/small **cross footprint**, paid by the newest volume theorem.

These are matrix-level statements. Neither treats `X^T R X` as a small random variable.

### Explicit diffuse cross certificate

Take a six-by-three baseline cross block

\[
M_0=a\,2^{-1/2}\begin{pmatrix}I_3\\I_3\end{pmatrix}.
\]

It has `s_3(M_0)=a` and every row leverage equals `1/2`. Therefore every arbitrary signed update satisfying (7.3) gives (7.4), even if its within-bank blocks have unbounded norm and arbitrarily many very large eigenvalues.

## 8. Numerical consistency checks

`CHECK.py` and `CHECK_RESULT.json` are saved beside this report. The checker ran:

- 10,000 randomized compression-footprint instances with mixed signs, arbitrary huge complementary blocks and cross couplings: zero violations of the threshold-count consequence;
- 10,000 partner-style complementary-compression instances with arbitrary top updates and cross blocks: zero violations of the inherited three-mode threshold;
- an exact sharpness control with `mu=2`, `delta=0.3`, whose third absolute eigenvalue equals the predicted threshold `1.7`.

These are finite consistency checks only. They are not evidence for the unrestricted conjecture and are not substitutes for the variational proof above.

## 9. What this removes, and the remaining full-target gap

The supporting conclusion is stronger than the previous B12 leakage bookkeeping:

> Once three signed spectral modes live in a protected Hermitian compression of an ACTUAL finite original-coordinate core, **arbitrary cross coupling and arbitrary complementary spectrum cost exactly zero** for retaining those three threshold modes. Only perturbation inside the protected compression is charged.

This removes invertibility of the entire complementary spectrum, Schur-shear conditioning, and low-rank leakage size from that branch of the additional-eigenvalue problem.

It does **not** solve the full QFORM conjecture. From the bare global assumption `s_3(A)>=1`, we still do not know how to force either

- a bounded-size original-coordinate physical core containing a protected compression with a universal gap; or
- an actual diffuse cross block satisfying the fractional-volume gate; or
- one of the already-paid grouped-bank/hub/ridge/pair alternatives.

A protected subspace spread over an unbounded number of original coordinates gives an `m`-dependent finite-core constant and therefore is not enough. The remaining structural compiler must preserve product provenance while finding a bounded physical carrier or aggregating the spread coordinates before paying curvature.

The full conjecture is therefore **OPEN / NOT PROVED / NOT DISPROVED**. Continuity is proved in the volume branch (7.4), but this run does not establish continuity for the compression branch (4.4) or for the unrestricted target.
