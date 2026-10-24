# B01 / A003 — physical retained-`U` payment for two coherent surgeries

**Run:** `20261012T081137Z-account01-B01-two-surgery-payment-a003`  
**Primary packet:** A003, minimal target formulation  
**Stable gap:** `G-UPPER-SET-ASYMMETRY`  
**Status:** new all-parameter class theorem author-proved, pending A086/A094 review. Full FEI remains **OPEN**.

## 1. Frozen objective and accepted input

The preceding B01 theorem localized the quadratic interaction of two point surgeries of a bent core and identified an exact difference-spectrum refund. B19/A094 independently accepted those algebraic formulas at their exact scope, while correcting the interpretation: a principal-filter generator is not by itself a physical payment.

This run inserts the selector probability, retains both child packets, and pays the complete one-node charge by actual selector influence. The class is:

- any bent Boolean core on even `k>=8` bits;
- any two distinct truth-table points, with arbitrary Hamming distance and phase;
- the Boolean child obtained by flipping both points;
- an arbitrary fresh `d`-bit one-word selector choosing the edited child.

## 2. PROVED: complete physical node payment

Let `delta=2^-k`, `p=2^-d`, let `g` be the bent parent, and let `h` be its two-point edit. For the shared-variable selector `F`, define

```text
J = U(F)-(1-p)U(g)-pU(h).
```

The children disagree on exactly two inputs, so the physical selector influence is

```text
I_ctl(F)=4 p d delta.
```

The theorem proved in `TWO_SURGERY_PAYMENT.tex` is

```text
J < 283 I_ctl(F).
```

The constant is independent of `k`, `d`, activation probability, Hamming distance, bent phase pattern, and the chosen points. Both children use every one of the same physical variables and generally have fully overlapping Fourier support.

## 3. Exact cancellation of the rare logarithm

For Fourier coefficients `a=hat g`, `b=hat h`, difference `e=b-a`, coherent coefficient `c=(1-p)a+pb`, and upper masses `A,B,D`, direct selector Walsh summation gives

```text
U(F) = sum_T c_T^2 log_2(((1-p)A_T+pB_T)/c_T^2)
     + p(1-p) Udiff(e)
     + (pd/2-p^2d) ||e||_2^2.
```

After subtracting the retained child packets, all long cap logarithms combine into

```text
p(1-p) K,
K=Udiff(e)-sum_T e_T^2(k-|T|).
```

Let `r=|supp(x xor y)|` and `tau=g(x)g(y)`. The independently accepted refund gives

```text
K=-rho <=0,                                  r>=2,
K=-4 delta(1+tau) <=0,                       r=1.
```

Thus the difference packet, with its correct physical factor `p(1-p)`, creates no positive charge. This includes the adjacent-point endpoint and both phase signs.

## 4. Uniform coherent remainder

Normalize the edited cap, edited atom, and coherent atom by

```text
1+u_T=B_T/A_T,
1+v_T=b_T^2/delta,
1+w_T=c_T^2/delta.
```

Since a two-point edit changes each Walsh coefficient by at most `4delta`, for `k>=8`

```text
|u_T|,|v_T| <= 9 sqrt(delta),
|w_T| <= (17/2) p sqrt(delta).
```

The remaining natural-log scalar term is

```text
Phi_p(u,v,w)
=(1+w) ln((1+pu)/(1+w))
-p(1+v) ln((1+u)/(1+v)).
```

On the full parameter box, an explicit Hessian estimate and the exact linear identity

```text
p v_T-w_T=p(1-p)e_T^2/delta
```

give `Phi_p<780 p delta`. Summing `2^k=1/delta` atoms and restoring bits yields

```text
J <= (780/ln 2) p delta + I_ctl
  = (195/(d ln 2)+1) I_ctl
  < 283 I_ctl.
```

This completes the nonlinear coherent/retained-child payment that was left open by the algebraic two-surgery lemma.

## 5. Verification and mandatory regimes

`CHECK.py` was written independently of the previous checker. It:

- compares the exact shared-selector identity with direct truth-table Walsh transforms in 1,242 cases through `k=6`;
- checks the full scalar decomposition, parameter box, nonpositive weighted refund, and theorem bound in 756 cases for `k=8,10,12`;
- includes selector depths `d=1,2,4,8`, Hamming distances `r=1,2,k`, intermediate distances, and both observed phase signs.

It passed 5,422,518 assertions. The maximum direct identity error was `6.22e-15`; the largest observed `J/I_ctl` was `5.106568427546`, far below the deliberately coarse analytic constant. The computation is finite corroboration; the theorem is analytic for all declared parameters.

## 6. Precise movement and remaining universal gap

**Previous status:** the two-surgery difference packet was known to refund its own algebraic cross-cap, but the selector weight and nonlinear coherent/retained-child residual were unpaid.

**New status:** the complete one-node physical payment is proved for every two-point edit of every bent core in every even dimension `k>=8`, with arbitrary selector rarity and no dependence on Hamming separation or phase. This strictly extends the prior one-point overlap class.

**Still open:** one node is not an arbitrary hierarchy. Three or more edits generate several principal displacement filters, and repeated selector nodes can reuse the same physical data variables. No theorem yet assigns their coherent Hessian terms and refunds without double spending. Universal GU' and full FEI remain open.

The next action is the three-surgery case. Expand the difference spectrum into the three pairwise displacement filters plus the triple coherence term, and test whether a spanning-tree ownership rule charges each filter once. The mandatory falsifiers are an affine triangle `x xor y xor z=0`, three adjacent points, and a near-tensor placement.

## 7. Source and review record

- Source head at research: `85a6d0d5bad197f7d430421702be5ec75c48d75f`.
- Owner control commit: `40210272c19f43fed84f6a67653f9a04b0e11e28`, revision 2026-10-12.1.
- Owner order blob: `81b6d6f988aee4489512c6e62543253900620453`.
- Case-target blob: `97e41262ebb4f09eec53630a918acae09efc9a48`.
- B01 contract blob: `ac038a028831d59ad053dd56b2b527e2a71ffdee`.
- Accepted algebraic two-surgery source: B01 commit `729d4c85210359e038d5239e52830fa462e5d340`, proof blob `72f02059b795cb7d4f3699c9f77b2bee38af7e97`.
- Independent A094 review: canonical commit `85a6d0d5bad197f7d430421702be5ec75c48d75f`, report blob `65a9538bf284f032c661c91b6dce3ee1f8fd1b48`; no mathematical repair was made.
- The arbitrary shared-selector identity is rederived in this proof; the neighboring one-point theorem is context, not a premise.
- No literature-priority claim is made.
- No worker, protected source, paid compute, scheduler mutation, public release, or shared-index edit was used.
- Exposed model: Codex; reasoning-effort metadata was not exposed.
- Independent review of this new theorem: not yet; route to A086/A094.
- Native Brain ingestion: not claimed; repository mirror only.
