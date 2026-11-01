Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding scheduler selector is exposed.**

# R7-07 validation addendum — balanced branches with exponentially growing pipes

This immutable addendum corrects one overstrong interpretive sentence in

`research7_2026-09-17/R7-07/admissions/2026-09-19T231031Z__H0008_branch_skeleton_pipe_resolvent_and_good_split_criterion.md`.

Theorem 12.1 and its logarithmic good-branch criterion remain correct. What was too strong was the prose inference that failure of the second-moment criterion must force paths to be “overwhelmingly composed of exact/near-pipe branch states.” There is a second, distinct mechanism: **balanced branches can be separated by pipe lengths that grow exponentially in branch index**. The source-specific task must exclude that mechanism under the tilted pair spine as well.

## 1. Exact countermodel to the overstrong interpretation

Consider a deterministic spherically symmetric tree whose genuine branch vertices are binary and perfectly balanced. Between branch generation `k-1` and branch generation `k`, every arm is a chain of `L_k>=1` unit-resistance edges. Put

\[
D_k=\sum_{r=1}^{k}L_r,
\qquad D_0=0.
\]

Every genuine branch has harmonic probabilities `(1/2,1/2)`, so

\[
\boxed{\Delta=1-\left(\frac14+\frac14\right)=\frac12}
\tag{1.1}
\]

at **every** branch. Thus there are no near-pipe genuine branches at all.

The forward effective resistance from the root branch to infinity is the radial series

\[
\boxed{R_{\rm eff}=\sum_{k\ge1}\frac{L_k}{2^k}.}
\tag{1.2}
\]

Indeed the `k`th pipe layer consists of `2^k` equal length-`L_k` chains in parallel. Therefore the tree is transient exactly when (1.2) is finite, and its root escape probability satisfies

\[
\frac1{B_o}=1+R_{\rm eff}.
\tag{1.3}
\]

Let `K` be the number of binary branch decisions on which two independent harmonic rays agree before their first disagreement. Then

\[
P(K=k)=2^{-(k+1)},
\qquad
P(K\ge k)=2^{-k},
\qquad k=0,1,2,\ldots.
\tag{1.4}
\]

The common-prefix lifetime is exactly

\[
\boxed{\tau=1+D_K.}
\tag{1.5}
\]

Consequently

\[
E\tau
=1+\sum_{r\ge1}L_rP(K\ge r)
=1+\sum_{r\ge1}\frac{L_r}{2^r}
=\frac1{B_o},
\tag{1.6}
\]

which exactly matches the electrical identity.

For the second moment,

\[
\boxed{
E D_K^2
=\frac12\sum_{k\ge0}2^{-k}D_k^2,
}
\tag{1.7}
\]

because `P(K=k)=2^{-(k+1)}`. Hence

\[
\boxed{
E\tau^2<\infty
\iff
\sum_{k\ge0}2^{-k}D_k^2<\infty.
}
\tag{1.8}
\]

This criterion is exact.

## 2. Sharp exponential-pipe threshold

Take

\[
L_k\asymp a^k,
\qquad 1<a<2.
\]

Then

\[
R_{\rm eff}<\infty
\iff
\sum_k\left(\frac a2\right)^k<\infty,
\]

so the tree is transient for every `a<2`. On the other hand `D_k\asymp a^k`, and (1.8) becomes

\[
\sum_k\left(\frac{a^2}{2}\right)^k<\infty.
\]

Therefore

\[
\boxed{
\begin{array}{ll}
1<a<\sqrt2:& E\tau^2<\infty,\\[2mm]
\sqrt2\le a<2:& B_o>0\ \text{but}\ E\tau^2=\infty.
\end{array}}
\tag{2.1}
\]

Thus positive conductance/transience alone does **not** control the pair-overlap second moment, even when every branch is maximally nondegenerate with `Delta=1/2`.

At the critical spacing `a=sqrt(2)`, each branch-generation contribution to (1.8) stays order one, so the divergence is transparent.

## 3. Relation to the good-branch criterion

For `delta=1/2`, every branch is `delta`-good. At original depth `n` in the model `L_k\asymp a^k`, the number of branch points encountered is

\[
g_{1/2}(n)\sim\frac{\log n}{\log a}.
\tag{3.1}
\]

Theorem 12.1 of the preceding artifact requires asymptotically more than

\[
\frac{2}{\log 2}\log n
\]

good branches. Condition (3.1) exceeds that threshold exactly when `a<sqrt(2)`. Hence the theorem detects the same sharp boundary as the direct second-moment calculation.

So Theorem 12.1 was not merely sufficient on this test family: its logarithmic constant is **sharp**.

## 4. Corrected interpretation

There are now two genuinely different ways the pair Green mass could fail:

1. **spacing failure:** good branches exist but are separated by pipe lengths growing too quickly in branch index, as in (2.1);
2. **split failure:** branch points occur often enough, but most are near-pipe with `Delta` too small to kill the pair efficiently.

The H0008 source-law exact-pipe resolvent controls mechanism 1 only at an unbiased survival-conditioned source entrance. The already-proved small-competitor tail controls mechanism 2 only at source/Palm scale. The unresolved tilted-spine problem is to prove that repeated pair selection cannot turn either source-scale estimate into a bad branch skeleton of the kind above.

A particularly sharp source-level target is therefore to prove that along the normalized common-pair branch spine the cumulative original depth after `k` genuine branches satisfies, with enough moment control,

\[
D_k=o((\sqrt2+\varepsilon)^k)
\]

on the balanced binary benchmark, or the corresponding variable-split analogue in which `sqrt(2)` is replaced by the inverse square-root of the pair-survival Lyapunov rate.

## 5. Status

- This addendum **does not** change H0008 ownership or R7-07 admission state.
- Fixed R7-07 source metric remains `UNMEASURED -> UNMEASURED`; stagnation remains `NOT_STARTED`.
- It corrects only the interpretation after Corollary 12.2 in the preceding immutable artifact; the theorem and algebra there remain valid.
- The example is an internal deterministic obstruction model, not a source counterexample.
