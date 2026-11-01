# B19 / A094 — independent review of B05's separated hierarchy payment

**Run:** `20261012T044913Z-fleet01-B19-b05-separated-hierarchy-review-a094`  
**Primary review packet:** A094 (proof-chain challenger)  
**Target packet:** A023  
**Target claims:** `B05-A023-SEPARATED-TWO-CORE-U-IDENTITY-v1` and
`B05-A023-SEPARATED-HIERARCHY-PAYMENT-v1`  
**Verdict:** **ACCEPTED AT DECLARED SCOPE**.  Full FEI remains **OPEN**.

## 1. Frozen review object

The reviewed source is the complete B05 bundle
`20261012T043233Z-fleet01-B05-separated-hierarchy-a023`, canonical final
commit `72824efa4229ee109fc344f1a021840982509ee5`, seven-file core commit
`5daa4829c71a08f636f7154ef16a090559bec294`.

The frozen claim is:

> For every finite tree of fresh one-word selector blocks whose two child
> subtrees at each node use disjoint complete physical variable sets, and
> whose leaves are arbitrary genuine Boolean signs,
> \[
> U(F_{\rm root})-\sum_\ell w_\ell U(g_\ell)
> \le C_{\rm sep} I_{\rm sel}(F_{\rm root}),
> \]
> where
> \[
> C_{\rm sep}=3+\frac{4(1+2/e)}{\ln2}
> +\frac2{\ln2}+\frac2{e\ln2}<16.964.
> \]

The constant is claimed to be independent of depth, all selector word
probabilities, leaf dimensions, leaf spectra, and the number of core
changes.  The arbitrary leaf `U` packets are retained, not paid.

## 2. Independent reconstruction of the two-core identity

Let `g0` and `g1` live on disjoint input blocks, let
`r_i=Pr[g_i=-1]`, `mu_i=1-2r_i`, `Delta=r_1-r_0`, and
`theta=r_0+r_1-2r_0r_1`.  A fresh `d`-bit one-word selector chooses `g1`
with `p=2^-d` and `g0` otherwise.

I reconstructed the Fourier expansion without importing the author checker.
Write `u_T=hat g0(T)`, `v_R=hat g1(R)`, and let `Pi_i` be the upper-set
mass function of child `i`.  The coefficient and cap packets are:

| Selector/child packet | squared coefficient | upper-set cap |
|---|---:|---:|
| empty selector, empty child | `mu_bar^2` | `1` |
| empty selector, nonempty `T` of `g0` | `(1-p)^2 u_T^2` | `(1-p) Pi_0(T)` |
| nonempty `A`, nonempty `T` of `g0` | `p^2 u_T^2` | `2^(d-|A|)p^2 Pi_0(T)` |
| empty selector, nonempty `R` of `g1` | `p^2 v_R^2` | `p Pi_1(R)` |
| nonempty `A`, nonempty `R` of `g1` | `p^2 v_R^2` | `2^(d-|A|)p^2 Pi_1(R)` |
| nonempty `A`, empty child | `4p^2 Delta^2` | `4·2^(d-|A|)p^2 theta` |

The last cap includes every child frequency above the empty child
frequency.  Summing these six packet types gives exactly the author's
equation (2):

\[
\begin{aligned}
U(F)={}&M(\bar r)+(1-p)[U(g_0)-M(r_0)]+p[U(g_1)-M(r_1)]\\
&+q_0\left((1-p)^2\log_2\frac1{1-p}+\frac{pd}{2}-p^2d\right)
+q_1\frac{pd}{2}\\
&+(2pd-4p^2d)\Delta^2
+4(p-p^2)\Delta^2\log_2\frac{\theta}{\Delta^2}.
\end{aligned}
\]

Here `M(r)=(1-2r)^2 log2(1/(1-2r)^2)` and the last term is zero when
`Delta=0`.  The combinatorial identity
\[
\sum_{A\ne\varnothing}(d-|A|)=d(2^{d-1}-1)
\]
accounts for all selector-depth terms.  No child-support collision is
hidden: disjointness is used exactly when separating the `u` and `v`
packets.

## 3. Independent reconstruction of the node bound

Every selector coordinate is pivotal exactly when its selector edge joins
the active word to its unique neighbor and the two independently sampled
children disagree.  Thus
\[
I_{\rm ctl}=2pd\,\theta.
\]
The factor two counts both endpoints of the selector edge.

For `phi(mu)=mu^2 log2(1/mu^2)`, the claimed Lipschitz estimate is valid;
indeed the stronger global estimate `|phi'(mu)|<=2/ln 2` holds on
`[-1,1]`.  The weaker constant used by B05 therefore gives
\[
M(\bar r)-(1-p)M(r_0)-pM(r_1)\le 2L_Mp\theta,
\quad L_M=\frac{4(1+2/e)}{\ln2}.
\]
The remaining scalar facts are also valid:
\[
q_i\le4\theta,\qquad
\Delta^2\le\theta,
\]
\[
\Delta^2\log_2\frac{\theta}{\Delta^2}
\le\frac{\theta}{e\ln2},
\qquad
(1-p)^2\log_2\frac1{1-p}\le\frac p{\ln2}.
\]
They give
\[
J\le p\theta\left(2L_M+\frac4{\ln2}+\frac4{e\ln2}\right)
+6pd\theta
\le C_{\rm sep}(2pd\theta).
\]
This is a bound on the complete signed node charge, not on each positive
summand of a local decomposition.

## 4. Physical all-depth telescope

For a node `v`, let its reach probability be `w_v`, its active-word
probability be `p_v`, and its two children be `v0,v1`.  By definition,
\[
w_{v0}=w_v(1-p_v),\qquad w_{v1}=w_vp_v.
\]
Multiplying
\[
J_v=U(F_v)-(1-p_v)U(F_{v0})-p_vU(F_{v1})
\]
by `w_v` cancels every nonroot internal packet once against its unique
parent packet.  Hence
\[
\sum_vw_vJ_v
=U(F_{\rm root})-\sum_\ell w_\ell U(g_\ell).
\]

A selector coordinate belonging to node `v` affects the root only on the
unique ancestor event reaching `v`.  Freshness and disjointness make that
event independent of the local unused variables and prevent coordinate
reuse, so
\[
I_{\rm sel}(F_{\rm root})
=\sum_v w_vI_{{\rm ctl},v}.
\]
Applying the node bound and summing proves the frozen theorem.  The same
reach argument gives the conditional leaf-data influence identity, so if
every leaf obeys `U(g_l)<=K I(g_l)`, then
\[
U(F_{\rm root})\le\max\{C_{\rm sep},K\}I(F_{\rm root}).
\]

## 5. Hard regimes and independent computation

The proof survives the independently selected endpoint regimes:

- `theta=0`: both children are the same deterministic sign and both sides
  vanish;
- `Delta=0`: the scalar interaction is interpreted as zero;
- balanced or deterministic individual children: zero mean packets cause no
  division;
- `d=1`: the depth coefficient has its endpoint value and the pivotal
  factor remains `2p`;
- `d -> infinity`: the constant stays fixed while the charge and physical
  selector influence both carry the rare reach factor;
- arbitrary hard leaves: their `U` packets remain explicitly on the right
  side of the telescope rather than being assumed bounded.

`INDEPENDENT_CHECK.py` was written from scratch for this review.  It uses
integer Walsh transforms, exact rational upper masses, and 80-digit Decimal
logs.  It checks every pair of Boolean cores through two variables at
selector depths 1 through 5, every four-leaf one-bit balanced tree, and
every four-leaf one-bit depth-three comb.

Result: **5,352 assertions passed**, no failures, no randomness.  The
largest identity residual was `1.1e-79`.

## 6. Literature and scope comparison

The closest primary frameworks are O'Donnell--Wright--Zhou's read-once
decision-tree FEI theorem, O'Donnell--Tan's disjoint composition theorem,
and Wan--Wright--Wu's read-`k`/expected-depth decision-tree bounds.  They
confirm that disjoint read-once structure is a known favorable regime.
They do not supply this exact upper-set `U` packet identity or authorize a
transfer to shared-variable sibling spectra.  The present result is best
treated as a source-bound restricted lemma, not as a novelty claim and not
as a full-FEI endpoint.

Primary sources checked:

- O'Donnell, Wright, Zhou, *The Fourier Entropy-Influence Conjecture for
  Certain Classes of Boolean Functions* (ICALP 2011),
  https://www.cs.cmu.edu/afs/cs/Web/People/jswright/papers/fei.pdf
- O'Donnell, Tan, *A Composition Theorem for the Fourier Entropy-Influence
  Conjecture*, arXiv:1304.1347.
- Wan, Wright, Wu, *Decision Trees, Protocols, and the Fourier
  Entropy-Influence Conjecture*, arXiv:1312.3003.

## 7. Verdict and remaining universal gap

Both target claims are **accepted at their exact declared scope**.  This
review did not repair or alter the proof and therefore does not create a
reviewer-contributor recusal.

The first unpaid line remains exactly the one stated by B05: if siblings
share physical variables, the `u` and `v` Fourier coefficients collide in
the same frequencies and the six-packet cap table is false.  A universal
argument must bound the resulting signed upper-mass overlap defect without
reusing pivotal events.  Whole-set addressing and reused selector bits are
also outside this theorem.

No claim is made that arbitrary leaf `U` is controlled.  No full-FEI proof
or counterexample follows.  Full FEI remains **OPEN**.

## 8. Execution and delivery facts

Observed model metadata: Codex; exact reasoning-effort setting was not
exposed.  Subagents: zero.  No scheduler, graph, live-store, account,
credential, publication, or deployment mutation was attempted.  The
complete review bundle is routed to A023, A087, A094, and B20 through the
existing canonical and Brain handoff paths.
