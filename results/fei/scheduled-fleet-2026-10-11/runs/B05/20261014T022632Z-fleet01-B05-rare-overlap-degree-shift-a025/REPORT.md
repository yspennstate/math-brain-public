# B05 / A025 — rare shared-coordinate degree-shift counterfamily

Status: **AUTHOR-PROVED COUNTERFAMILY, PENDING INDEPENDENT REVIEW**. Full FEI remains **OPEN**.

## Bounded objective

Test the first unpaid overlap case left by the independently reviewed A023 singleton-potential theorem: two genuine Boolean factors sharing exactly one physical coordinate. Determine whether the new singleton potential can be paid by a constant multiple of the shared pivotal event, without recharging the old factor's private influence.

## Result

For
\[
\phi(t)=2t^2\left(\log_2(1/t)+1/\ln2\right),\qquad
\Phi(F)=\sum_i\phi(|\widehat F(\{i\})|),
\]
there is no finite absolute `C` for which every pair of Boolean factors sharing only `x` satisfies
\[
\Phi(fg)\le \Phi(f)+\Phi(g)+C(\operatorname{Inf}_x f+\operatorname{Inf}_x g).
\]
In particular the accepted disjoint-factor step `Phi(Bf) <= Phi(f)+M I(B)` does not extend to one reused coordinate.

Take balanced majority `K_n` on `n=2m+1` private bits, a shared bit `x`, and a one-point event `E` in `r` controls, of probability `epsilon=2^-r`. Set
\[
f=xK_n,\qquad g=\begin{cases}x&E,\\1&\neg E.\end{cases}
\]
Writing `c_m=binom(2m,m)/4^m`, direct Fourier calculation gives
\[
\Phi(f)=0,\quad \Phi(g)=(r+1)\phi(\epsilon),\quad
\Phi(fg)=n\phi(\epsilon c_m).
\]
Meanwhile
\[
\operatorname{Inf}_x(f)=1,\quad \operatorname{Inf}_x(g)=\epsilon,
\quad \operatorname{Inf}_x(fg)=1-\epsilon,
\quad I(g)=(r+1)\epsilon.
\]
The elementary bounds `1/(2 sqrt(m)) <= c_m <= 1/sqrt(m+1)` imply
\[
\Phi(fg)\ge \frac{\epsilon^2}{2}\log_2(m+1).
\]
Thus, for each fixed rarity and every proposed constant, all sufficiently large majority cores violate the shared-edge payment. This is a genuine two-parameter Boolean family, not a finite search.

## Exact mechanism

If Boolean `F,G` share only `x`, the physical derivative identity is
\[
\operatorname{Inf}_x(FG)=p+q-2pq.
\]
But for a private coordinate `u_i` of `F`,
\[
\widehat{FG}(\{u_i\})=
\widehat F(\{u_i\})\widehat G(\emptyset)+
\widehat F(\{u_i,x\})\widehat G(\{x\}).
\]
The counterfamily stores the majority singleton coefficients at degree two, `\{x,u_i\}`, in `f`; the rare shared gate converts an `epsilon` fraction into degree-one coefficients. A ledger remembering only the shared pivotal mass cannot see the number of shifted private coefficients.

## Reveal-order ledger

The family also isolates the surviving global refund.

- Controls first: after all `v` controls are known but `x` is not, expected potential is `epsilon Phi(K_n)`.
- Shared selector first: the two children are `K_n` and `K_n(2 1_E-1)`, so expected potential is
  \[
  \frac n2\{\phi(c_m)+\phi((1-2\epsilon)c_m)\}.
  \]
- After both `x` and all controls are known, the terminal potential is always `Phi(K_n)`.

Hence the signed total telescope is order-independent, but the large negative refund appears at different nodes. This explains precisely why the counterfamily kills a nonnegative local/shared-edge payment but does **not** kill a globally chosen signed restriction tree.

## Scope

The result refutes only the overlap-stable singleton-potential/product laws above. It does not refute the exact `B_i-Gamma_i+KL_i` identity, complete mismatch/KL credit, existential good-coordinate selection, optimized restriction trees, or FEI. The accepted disjoint-product and fresh-selector theorem remains intact.

## Verification

`CHECK.py` independently evaluates the exact formulas, central-binomial bounds, physical influence identities, reveal-order intermediates, and explicit logarithmic thresholds. `CHECK.out` records the run. The analytic proof and exact violation range are in `RARE_COUNTERFAMILY.tex` and `REFUTED_STATEMENT.json`.

## Next action

Replace scalar singleton memory at shared nodes by a degree-shift-aware signed account. The minimal candidate must transport the block `\{\widehat f(\{x,u_i\})\}_i` and telescope it against the negative refund created when `x` is actually revealed. Test that account first on this family, then on two nested reused coordinates; do not attempt another shared-pivotal-only multiplier.
