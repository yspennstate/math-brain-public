# account03/B09 — multiscale cardinality-event KL bank

**Run:** `20260922T104916Z-account03-B09-fei`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`, control revision `2026-09-22.3`  
**Assignment:** `FEI-20260922-account03-B09`, Path B, Conditional-product support exclusion  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_EVENT_KL_ON_SYMMETRIC_SOURCES / RARE_LOG_RECOVERY_ON_SPARSE_SUSPENSIONS`  
**Full unrestricted FEI:** **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 0. Fresh-control pivot and exact target

The fresh owner control redirects all eighty workers to the full uniform-cube Fourier-entropy/influence problem. Older MOC4 work is preserved but is not active in this run. The current target is to make the exact dependence credit

\[
K_{\rm occ}(P)=D_{\rm KL,2}(P\Vert Q_r)
\]

pay the negative first-moment term in the all-gate residual, while retaining the rare-event logarithm and the exact Boolean source.

The compact B09 assignment asks specifically for source-valid event/support exclusions against the matching conditional-product law. The result below gives an exact multiscale event bank for permutation-symmetric spectral sources, an explicit support-exclusion corollary, and a growing-dimensional genuine Boolean family on which the bank recovers **all** of the `Theta(m I)` dependence KL that quadratic Booleanity compression loses.

No universal FEI conclusion is claimed.

## 1. Exact sources consumed

1. **Influence I-projection** — `yspennstate/math-open-problems`, commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`. It proves that the maximum-entropy nonempty conditional-product law `Q_r` with the same coordinate-occurrence marginals satisfies
   \[
   K_{\rm occ}=D_2(P\Vert Q_r)=H_{\max}(r)-H(P),
   \qquad R_\Gamma=B_{\rm inf}^\Gamma+K_{\rm occ}.
   \]
2. **Exact hierarchy KL** — `yspennstate/math-open-problems`, commit `2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`, `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T091017Z-iprojection-composition-transfer/REPORT.md`. It proves
   \[
   K_{\rm occ}(F)=K_{\rm occ}(G)+\sum_i\alpha_iK_{\rm occ}(f_i)+C_{\rm hier},\qquad C_{\rm hier}\ge0,
   \]
   for disjoint Boolean composition. This is the multiscale credit that must not be discarded.
3. **Named other-account Booleanity result actually consumed** — `yspennstate/math-open-problems`, commit `603b35e74227d1c2d8ee34c0c527c439c686e30b`, `proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T092422Z-biased-booleanity-gap/REPORT.md`. It proves, from every exact signed Booleanity equation,
   \[
   K_{\rm occ}\ge {1\over4v\ln2}\max_{U\ne\varnothing}{\mathfrak g_U^2\over L_U^2}.
   \]
   The same source explains that a single complement equation can be exponentially weak.
4. **Rare-log quadratic obstruction** — `yspennstate/math-open-problems`, commit `7ec649dfb3d1ab2f92855f2069590fca2ac956dd`, `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T093820Z-full-convolution-energy-obstruction/REPORT.md`. On the sparse Boolean suspensions used below, the full unweighted signed-convolution energy is `4I+o(I)` while `K_occ=Theta(mI)`.
5. **Mandatory recursive-majority preflight** — `yspennstate/math-open-problems`, commit `bff0d7b6c21485f386841c42582eb04f32705046`, `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T100641Z-lowlevel-projection-barrier/REPORT.md`. Fixed or sub-half-depth labelled low-level KL followed by one merged tail is asymptotically negligible on recursive ternary majority.

The assigned current-programme partner is `account04/B09`. No completed `proofnet24/P03-fei/fleet-2026-09-22/account04/B09/` artifact was present at the two source checks made before this report. Under the owner order's asynchronous rule, this run did not wait and instead consumed the completed named other-account input in item 3 plus the exact hierarchy result in item 2.

## 2. Orbit sufficiency: cardinality contains the entire KL for symmetric sources

Let `P` and `Q` be probability laws on nonempty subsets of `[n]`. Assume both are invariant under every permutation of coordinates. Let

\[
K(S)=|S|,\qquad A_k=P(K=k),\qquad B_k=Q(K=k).
\]

### Theorem 2.1 — `B-ORBIT-CARDINALITY-SUFFICIENCY-v1`

Under the stated permutation invariance,

\[
\boxed{D_2(P\Vert Q)=D_2(A\Vert B).}
\tag{2.1}
\]

In particular, for a permutation-symmetric Boolean spectral law `P` and its equal-marginal I-projection `Q_r`,

\[
\boxed{K_{\rm occ}=D_2(\mathcal L_P(|S|)\Vert\mathcal L_{Q_r}(|S|)).}
\tag{2.2}
\]

### Proof

Condition on the orbit `K=k`. Permutation invariance forces both `P(.|K=k)` and `Q(.|K=k)` to be uniform on the `binom(n,k)` subsets of size `k` whenever the corresponding level has positive mass. The KL chain rule gives

\[
D(P\Vert Q)=D(A\Vert B)+\sum_k A_kD(P(.|K=k)\Vert Q(.|K=k)),
\]

and every conditional divergence on the right is zero. This proves (2.1). For the I-projection, equal coordinate marginals imply equal product parameters, hence `Q_r` is permutation invariant. QED.

The same argument applies after factoring deterministic coordinates. This is useful for suspensions with one coordinate present in every spectral atom.

## 3. Exact nested event bank

The cardinality KL in (2.1) can itself be written as an exact sum of binary event KLs rather than a quadratic score.

For `0<=k<=n`, define survival masses

\[
A_{\ge k}=\sum_{j=k}^nA_j,\qquad B_{\ge k}=\sum_{j=k}^nB_j,
\]

and, whenever the survival mass is positive, conditional stopping probabilities

\[
u_k={A_k\over A_{\ge k}},\qquad v_k={B_k\over B_{\ge k}}.
\]

Write `d_2(x||y)` for Bernoulli KL in bits.

### Theorem 3.1 — `B-NESTED-CARDINALITY-EVENT-BANK-v1`

\[
\boxed{
D_2(A\Vert B)
=\sum_{k=0}^{n-1} A_{\ge k}\,d_2(u_k\Vert v_k).
}
\tag{3.1}
\]

Thus, on the symmetric sources of Theorem 2.1,

\[
\boxed{
K_{\rm occ}
=\sum_{k=0}^{n-1} A_{\ge k}\,d_2(u_k\Vert v_k).
}
\tag{3.2}
\]

This is a genuine logarithmic, multiscale event payment. It retains every cardinality scale; no fixed low-level cutoff is merged into one anonymous tail.

### Proof

Encode `K` sequentially: at stage `k`, conditional on `K>=k`, reveal whether `K=k` or `K>=k+1`. Under `A` and `B` the conditional Bernoulli laws are respectively `(u_k,1-u_k)` and `(v_k,1-v_k)`. KL chain rule for this deterministic sequential encoding gives (3.1). Equivalently, expanding the right side makes the successive survival-ratio terms telescope to `sum_k A_k log_2(A_k/B_k)`. QED.

## 4. Boolean support exclusion as a direct KL payment

Let `L` be any set of cardinalities that contains the entire actual spectral support, so that `P(K in L)=1`. Data processing by the event `{K in L}` gives

\[
\boxed{
K_{\rm occ}\ge -\log_2 Q_r(K\in L).
}
\tag{4.1}
\]

More generally, if an exact Boolean constraint forbids an event `E` (`P(E)=0`), then

\[
\boxed{
K_{\rm occ}\ge -\log_2(1-Q_r(E)).
}
\tag{4.2}
\]

This is the requested support-exclusion mechanism: the conditional-product reference pays logarithmically for mass placed on a Boolean-forbidden region.

### Corollary 4.1 — odd symmetric Boolean functions

Let `f` be a nonconstant permutation-symmetric Boolean function on the uniform cube with `f(-x)=-f(x)`. Its Fourier spectrum is supported on odd cardinalities. If all occurrence marginals equal `r` and the I-projection uses unconditioned Bernoulli parameter `t=cr`, where `c` is the nonempty-conditioning probability, then

\[
Q_r(K\text{ odd})={1-(1-2t)^n\over2c}.
\]

Hence

\[
\boxed{
K_{\rm occ}
\ge
\log_2{2c\over1-(1-2t)^n}.
}
\tag{4.3}
\]

The bound may be modest; its role here is to show an exact Boolean-forbidden support event produces a true logarithmic KL term. The full event bank (3.2) also prices the nonuniform weights inside the allowed levels.

## 5. Growing-dimensional rare-log recovery on the genuine sparse suspension

Use the exact Boolean family from the account04/B15 obstruction. For `m>=2`, put

\[
p=2^{1-m},\qquad g_m(x)=1-2\mathbf1_{\{x=0\}},\qquad F_m(y,x)=y g_m(x).
\]

`F_m` is balanced Boolean. The fresh coordinate `y` is present in every nonzero Fourier atom. Factoring it out, the old-coordinate actual law is

\[
P_m(\varnothing)=(1-p)^2,
\qquad
P_m(T)=p^2\quad(T\ne\varnothing),
\tag{5.1}
\]

while the exact influence-matched I-projection factor is the product law

\[
Q_m(T)=p^{|T|}(1-p)^{m-|T|}.
\tag{5.2}
\]

Both are permutation invariant on the old coordinates. Therefore Theorem 2.1 gives **equality**, not merely a lower bound:

\[
\boxed{
K_{\rm occ}(F_m)=D_2(A^{(m)}\Vert B^{(m)}),
}
\tag{5.3}
\]

where

\[
A^{(m)}_0=(1-p)^2,
\qquad
A^{(m)}_k={m\choose k}p^2\ (k\ge1),
\tag{5.4}
\]

and

\[
B^{(m)}_k={m\choose k}p^k(1-p)^{m-k}.
\tag{5.5}
\]

Combining (5.3) with Theorem 3.1 yields an **exact event-only decomposition of the entire irreducible dependence credit**.

The source obstruction proves

\[
{K_{\rm occ}(F_m)\over mp}
=m-5+{1\over\ln2}+o(1),
\tag{5.6}
\]

so

\[
K_{\rm occ}(F_m)=\Theta(m^2p)=\Theta(m I(g_m)).
\]

By contrast, its complete unweighted signed-convolution energy satisfies

\[
\mathcal B_m=4mp+O(m^2p^2)=\Theta(I(g_m)).
\tag{5.7}
\]

Thus the nested event bank recovers the missing rare-event logarithm with **zero KL loss** on this growing-dimensional genuine Boolean family, while the full unweighted quadratic bank loses a factor `Theta(m)`.

There is also a single explicit high-cardinality tail certificate. Let

\[
d_m=\left\lfloor {m\over2}-\sqrt{m\ln m}\right\rfloor,
\qquad E_m=\{|T|\ge d_m\}.
\]

For all sufficiently large `m`, Hoeffding under the level-counting measure and a union bound under `Q_m` give

\[
P_m(E_m)\ge2p(1-m^{-2}),
\qquad
Q_m(E_m)\le2^m p^{d_m}.
\tag{5.8}
\]

Therefore binary data processing yields

\[
K_{\rm occ}(F_m)
\ge d_2(P_m(E_m)\Vert Q_m(E_m))
\ge 2p(1-m^{-2})[d_m(m-1)-m]-h_2(2p).
\tag{5.9}
\]

The right side is `(1-o(1))m^2p`. This one tail already recovers the leading order; the full nested bank (3.2) is exact and, unlike a leading-order certificate, retains the `O(I)` margin needed in a potential argument.

### Proof of (5.8)-(5.9)

Because `P_m` assigns the same mass `p^2` to every nonempty old-coordinate subset,

\[
P_m(E_m)=2^mp^2\Pr[\operatorname{Bin}(m,1/2)\ge d_m]
=2p\Pr[\operatorname{Bin}(m,1/2)\ge d_m].
\]

Hoeffding bounds the omitted lower tail by `exp(-2 ln m)=m^{-2}`. Under `Q_m`,

\[
Q_m(E_m)=\sum_{k=d_m}^m{m\choose k}p^k(1-p)^{m-k}
\le2^m p^{d_m}.
\]

For any event with probabilities `a,b`,

\[
d_2(a\Vert b)
=a\log_2{1\over b}+(1-a)\log_2{1\over1-b}-h_2(a)
\ge a\log_2{1\over b}-h_2(a).
\]

Use `a>=2p(1-m^{-2})`, `a<=2p`, monotonicity of `h_2` near zero, and `log_2(1/p)=m-1` to obtain (5.9). QED.

## 6. Exact interaction with the consumed account04/B17 quadratic bank

At uniform balance, the account04/B17 theorem reduces to

\[
K_{\rm occ}\ge {1\over4\ln2}\max_{U\ne\varnothing}\mathfrak g_U^2.
\]

On the sparse suspension, evaluate each sign minimization at the actual Fourier signs. Then

\[
\mathfrak g_U^2\le C_m(U)^2,
\]

so

\[
{1\over4\ln2}\max_U\mathfrak g_U^2
\le {\mathcal B_m\over4\ln2}=O(I).
\tag{6.1}
\]

Equation (5.3), in contrast, recovers `K_occ=Theta(mI)` exactly. This is the precise way the named other-account result changes the mechanism: the signed quadratic equations remain valid but should not be compressed into a bounded-energy score when the conditional-product mismatch is a rare high-cardinality event. Event KL retains the logarithm.

## 7. Recursive-majority preflight and scope boundary

The recursive-majority barrier is explicitly respected.

* The projection in Theorem 3.1 retains the **entire** cardinality variable and all nested hazards. It is not a fixed collection of individually labelled levels followed by one merged tail.
* The exact sufficiency theorem requires permutation invariance of the squared spectral law. Recursive ternary majority has only its tree automorphism symmetry, not full permutation symmetry on `3^m` leaves. Therefore this report does **not** claim that cardinality alone pays its `Theta(I\,m)` dependence demand.
* Its odd-cardinality support exclusion gives only a bounded logarithmic payment, so parity support alone is visibly insufficient. The next mechanism must use the exact hierarchy rather than pretending a one-level event closes FEI.

This is consistent with the account04/B15 identity

\[
K_{\rm occ}(F)=K_{\rm occ}(G)+\sum_i\alpha_iK_{\rm occ}(f_i)+C_{\rm hier}.
\]

A natural continuation is a **hierarchical nested-event bank** that decomposes the block-activation and within-block `C_hier` terms into source-valid binary event KLs at every composition scale. That route retains the recursive-majority information instead of merging it into a low-level tail.

## 8. What is proved, what is not, and next unpaid implication

**PROVED here:**

1. permutation-symmetric spectral sources have exact cardinality sufficiency for `K_occ`;
2. cardinality KL has the exact nested binary-event decomposition (3.1);
3. any Boolean-forbidden cardinality support set gives the logarithmic exclusion payment (4.1)-(4.2);
4. on the genuine sparse suspension family, the multiscale event bank equals the full `K_occ=Theta(mI)` and therefore retains the rare-event logarithm lost by unweighted quadratic Booleanity energy;
5. the explicit high-cardinality event (5.9) alone recovers the leading `m^2p` scale.

**NOT proved:** unrestricted FEI, a universal event family for arbitrary Boolean spectra, or sufficiency of cardinality on recursive-majority/tree-asymmetric sources.

**Next unpaid implication:** extend the exact event coding from full permutation orbits to the disjoint-composition hierarchy, giving a binary-event chain-rule representation of `C_hier` and the child `K_occ` terms that remains source-exact under recursive ternary majority. Then compare that retained multiscale KL directly with `[-B_inf^Gamma]_+` for the surviving potential rather than with a quadratic surrogate.

No novelty or publication-priority claim is made.
