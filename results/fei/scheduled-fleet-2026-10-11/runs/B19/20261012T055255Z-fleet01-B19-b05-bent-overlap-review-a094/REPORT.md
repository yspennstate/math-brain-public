# B19 / A094 — independent review of the B05 bent-overlap payment

**Run:** `20261012T055255Z-fleet01-B19-b05-bent-overlap-review-a094`  
**Primary review packet:** A094 (proof-chain challenger)  
**Target packet:** A023  
**Target claims:** `B05-A023-SHARED-SWITCH-U-IDENTITY-v1` and
`B05-A023-BENT-ONEPOINT-OVERLAP-PAYMENT-v1`  
**Verdict:** **ACCEPTED AT DECLARED SCOPE**. Full FEI remains **OPEN**.

## 1. Frozen object and prior status

The reviewed source is B05 run
`20261012T053720Z-fleet01-B05-bent-overlap-a023`, canonical final commit
`86af28f927222e626e9d852c9a1f47ccab82d46c`. Its report, proof, claims,
checker, and checker output were read from that immutable commit. Before this
review, both target claims were author-proved pending A087/A094 review.

The nontrivial target is the following one-node statement. Let `k>=8` be
even, let `g` be any bent Boolean sign on `k` physical data variables, let
`h` be obtained by flipping `g` at one input, and let a fresh `d`-bit
one-word selector choose `h` with probability `p=2^-d` and `g` otherwise.
Writing

`J=U(F)-(1-p)U(g)-pU(h)`

and charging only physical selector influence, B05 claims

`J <= 71 I_ctl(F)`, `I_ctl(F)=2pd 2^-k`,

uniformly in `k,d`, the bent phase pattern, and the flipped point.

## 2. Exact shared-variable identity: independent reconstruction

For arbitrary Boolean `g,h` on the same data variables, put

`a_T=hat g(T)`, `b_T=hat h(T)`, `e_T=b_T-a_T`,

and let `A_T,B_T,E_T` be the corresponding upper-cone squared masses. The
indicator of the active selector word has Fourier coefficients of magnitude
`p` at every selector frequency. Hence the parent coefficients are

- `c_T=(1-p)a_T+p b_T` at the empty selector frequency;
- `+/- p e_T` at every nonempty selector frequency.

At frequency `(Q,T)`, its upper mass is

- `(1-p)A_T+pB_T` if `Q` is empty;
- `p 2^(-|Q|) E_T` if `Q` is nonempty.

The first equality follows coefficientwise from

`c_R^2+(p-p^2)e_R^2=(1-p)a_R^2+p b_R^2`.

Summing all nonempty selector frequencies, and using

`sum_{Q nonempty}(d-|Q|)=d(2^(d-1)-1)`,

gives exactly

```
U(F) = sum_T c_T^2 log2(((1-p)A_T+pB_T)/c_T^2)
     + p(1-p) sum_T e_T^2 log2(E_T/e_T^2)
     + (pd/2-p^2d) sum_T e_T^2.
```

Zero coefficients are omitted. This proves the identity for all finite
dimensions and all genuine Boolean children; no disjointness, spectral
orthogonality, or bentness enters this step.

## 3. Bent surgery reduction and cancellation

Set `N=2^k`, `alpha=N^-1/2`, and `delta=N^-1=alpha^2`. Bentness and a
one-point flip give

`a_T=alpha s_T`, `b_T-a_T=-2 delta t_T`, with `s_T,t_T` signs.

Consequently `A_T=2^(-|T|)` and `E_T/e_T^2=2^(k-|T|)`. Define

```
B_T/A_T=1+u_T,
b_T^2/delta=1+v_T,
c_T^2/delta=1+w_T.
```

Direct expansion gives

```
v_T=-4 alpha s_T t_T+4 delta,
w_T=-4p alpha s_T t_T+4p^2 delta,
p v_T-w_T=4p(1-p)delta.
```

The upper-cone average of `s_R t_R` is in `[-1,1]`. At the worst endpoint
`alpha=1/16`, `p=1/2`, this yields the source's uniform box

```
|u_T|,|v_T| <= (17/4)alpha,
|w_T| <= (33/8)p alpha.
```

Substitution into the exact identity shows that every term proportional to
the long cap logarithm `k-|T|` has coefficient

`w_T-pv_T+4p(1-p)delta=0`.

Thus the rare logarithm cancels atom by atom; it was not discarded or paid
from a pointwise influence budget. The remaining scalar, in natural logs,
is

`Phi_p=(1+w)ln((1+pu)/(1+w))-p(1+v)ln((1+u)/(1+v))`,

and

`J=(delta/ln2) sum_T Phi_p(u_T,v_T,w_T)+(1-2p)I_ctl`.

## 4. Independent audit of every constant

At the origin, `Phi=0` and `grad Phi=(0,p,-1)`, so the linear contribution
is exactly `pv-w=4p(1-p)delta`. The nonzero Hessian entries are

```
Phi_uu=-(1+w)p^2/(1+pu)^2+p(1+v)/(1+u)^2,
Phi_uv=-p/(1+u),     Phi_uw=p/(1+pu),
Phi_vv=p/(1+v),      Phi_ww=-1/(1+w),
Phi_vw=0.
```

I bounded these over the entire box using exact rational arithmetic, not
samples. After extracting a factor `p` where appropriate, the worst upper
bounds at `alpha=1/16,p=1/2` are

| entry | exact bound used by this review | source allowance |
|---|---:|---:|
| `|Phi_uu|/p` | `84300896/27217089 < 3.10` | `4` |
| `|Phi_uv|/p` | `64/47` | `3/2` |
| `|Phi_uw|/p` | `128/111` | `6/5` |
| `|Phi_vv|/p` | `64/47` | `3/2` |
| `|Phi_ww|` | `256/223` | `6/5` |

Taylor's integral remainder therefore has total coefficient

`4 + (1/2)(59129/320) = 61689/640 = 96.3890625 < 97`.

Finally, the positive series

`ln 2=sum_{m>=1}1/(m2^m)`

has its first twelve terms equal to
`7869871/11354112 > 693/1000`; hence
`97/ln2 < 97000/693 < 140` rigorously. Summing the `N=1/delta` atoms gives

```
J <= 140p delta + I_ctl
  = (70/d+1) I_ctl
  <= 71 I_ctl.
```

All constants and endpoint inequalities in the target proof are valid.

## 5. Physical-input accounting and hard regimes

For each selector coordinate, the active word and its neighbor contribute
both endpoints of a selector edge. The coordinate is pivotal exactly when
the other `d-1` selector bits match the active word and `g(x)!=h(x)`.
Thus its influence is `2p delta`, and the total is exactly
`I_ctl=2pd delta`. No data-coordinate influence is silently credited.

The proof survives the independently selected difficult limits:

- `k=8`, where the perturbation box is widest;
- `d=1`, where `p=1/2` and all Hessian denominators are smallest;
- `d` tending to infinity, where both the charge and physical credit retain
  the rare factor `p` and the constant does not grow;
- arbitrary bent phase signs and arbitrary flip point;
- a non-bent child `h` with the same physical variables and full Fourier
  support as `g`.

The payment is nevertheless only for one coherent surgery node. Repeating
surgeries changes the cap ratios passed to descendants, and this proof has
no telescope or nonreuse argument for those interactions.

## 6. Independent computation

`INDEPENDENT_CHECK.py` was written without importing the B05 checker. For
small functions it uses direct character sums rather than a fast Walsh
transform. It performed:

- 816 exhaustive ordered-pair checks of the exact shared-node identity for
  all Boolean children through two data variables and selector depths 1--3;
- 81 exact reconstructions of physical selector influence, including both
  edge endpoints;
- exact rational certification of the Hessian box, Taylor coefficient, and
  logarithm conversion;
- 135 bent-surgery cases over `k=8,10,12`, several affine phases and flip
  points, and `d=1,2,4,8,16`.

Result: **968,720 assertions passed**, no failures, no randomness. The
largest identity residual was `1.00e-89`; the largest observed
`J/I_ctl` was `4.861279949438929`. This computation checks normalization
and endpoints; the universal statement above is established analytically.

## 7. Primary-source scope comparison

Primary sources were retrieved on 2026-10-12.

- O'Donnell--Tan, *A Composition Theorem for the Fourier
  Entropy-Influence Conjecture*, arXiv:1304.1347, assumes inner functions
  on disjoint variable sets. It does not authorize this shared-variable
  upper-set transfer.
- O'Donnell--Wright--Zhou, *The Fourier Entropy-Influence Conjecture for
  Certain Classes of Boolean Functions* (ICALP 2011), proves FEI for
  read-once decision trees and explicitly gives disjoint coordinate sets to
  the two recursive subtrees. Its selector tax is therefore compatible but
  does not contain the present overlapping cap identity.
- Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean
  Plateaued Functions*, arXiv:2609.21563 (version dated 2026-09-18), proves
  `H<=4I` for plateaued functions and `H<=2I` for partially bent functions.
  Here the unperturbed seed is bent, but the one-point-flipped child and the
  switched parent are not assumed plateaued; Potapov does not supply the
  retained-`U` node payment.

No novelty or priority claim is made. The reviewed theorem has a distinct,
source-bound scope.

## 8. Verdict and first unpaid line

Both target claims are **independently accepted at their exact declared
scope**. This review did not modify a hypothesis, constant, or proof step,
so B19/A094 remains an independent reviewer rather than a contributor.

The mathematical movement is precise: the earlier accepted separated-tree
payment now has a reviewed, genuinely shared-variable one-node extension
for an unbounded bent one-point-surgery family. The first unpaid line is:

> Prove a dimension-, depth-, and rarity-independent nonreuse bound for the
> sum of coherent upper-mass overlap charges when two or more surgeries
> change the shared core along a hierarchy, or produce a genuine Boolean
> falsifier to that bound.

This review does not establish a shared-variable hierarchy telescope, a
bound for arbitrary shared children, `U<=K I`, or full FEI. Full FEI remains
**OPEN**.

## 9. Execution facts

Observed model metadata: Codex; exact reasoning-effort setting was not
exposed. Subagents: zero. No scheduler, graph, live-store, account,
credential, publication, or deployment mutation was attempted.
