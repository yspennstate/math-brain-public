# B20 / A097 — retained high-degree reserve in the GU row cut

**Status:** a strict all-dimensional quantitative reduction is proved. Universal GU and full FEI remain **OPEN**; independent review remains pending.

## Frozen candidate

- Candidate: `G(f)<=4I(f)+(3/4)U(f)` for every genuine Boolean function.
- Stable gap: `G-GU-SIGNED-KL-DEGREE-GE3`.
- Claim: `B20-A097-HIGH-DEGREE-RESERVE-v1`.
- Prior bound:

\[
G\le D_{\ge2}+\frac12V_1+\frac{2}{\ln2}I.
\]

The prior sole leaf required

\[
D_{\ge2}+\frac12V_1
\le\left(4-\frac2{\ln2}\right)I+\frac34U
\]

on tensor-prime, positive-residual Boolean functions of Fourier degree at least three.

## New exact reserve

Let `W_d=sum_{|S|=d}p(S)` and

\[
M_1=\sum_i\min\{p(\varnothing),p(\{i\})\}.
\]

The root/singleton payment actually contains `M_1+W_2`, not all of `I`. Retaining the discarded slack gives

\[
Q_{\ge3}:=I-M_1-W_2
=(W_1-M_1)+W_2+\sum_{d\ge3}dW_d
\ge W_2+3W_{\ge3}.
\]

Therefore the all-dimensional row cut strengthens to

\[
\boxed{
G\le D_{\ge2}+\frac12V_1
+\frac2{\ln2}(I-Q_{\ge3}).}
\]

The new sole open leaf is

\[
\boxed{
D_{\ge2}+\frac12V_1
\le\left(4-\frac2{\ln2}\right)I+\frac34U
+\frac2{\ln2}Q_{\ge3}.}
\]

This is strictly weaker than the old leaf whenever the Fourier degree is at least three, because then `Q_{>=3}>0`. The explicit reserve `(2/ln2)(W_2+3W_{>=3})` is already sufficient. The signed term, all order-at-least-two KL rows, `V_1/2`, normalization, and single-use accounting remain intact.

If this smaller leaf is proved, it gives universal `G<=4I+3U/4`, then `U<=16I`, and the audited reduction gives `H<=34I`.

## Verification

Exact rational Walsh arithmetic exhausts all 32,906 Boolean signs modulo global output sign through dimension four. It verifies the reserve identity, the lower bound, and strict positivity for every degree-at-least-three sign. The smallest positive reserve in the finite audit is recorded in `CHECK.out`. The theorem itself is algebraic and all-dimensional; the enumeration is validation only.

## Invalidations retained

- `V_1/2<=U` remains false.
- Adaptive root-tree payment still does not pay the static singleton sum without a transport/terminal lemma.
- B05 fair/disjoint transfer is not universal.
- The false `I>=1`, fixed-sign projection, unsigned coefficient four, and unrepaired B09 intervals remain unavailable.

## Remaining obligation

Use the minimal-child residual inequalities to show that the excess over the old right side is at most `(2/ln2)Q_{>=3}`, without discarding `sum_i(B_i-Gamma_i)` or paying any physical influence twice. A merely nonzero high-degree mass is now credited exactly, but may still be arbitrarily small.

Review targets: B18 and B19. Model/effort metadata: `UNKNOWN`.
