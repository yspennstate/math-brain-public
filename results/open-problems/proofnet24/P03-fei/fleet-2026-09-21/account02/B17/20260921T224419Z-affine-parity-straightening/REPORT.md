TASK: B17 ACCOUNT: account02 RUN: 2026-09-21T22:44:19Z — quadratic-cycle exceptional-row adversary and affine-parity straightening

MODEL: GPT-5.6 Sol (runtime self-report)
REQUESTED EFFORT: maximum actually supported
CONFIGURED / KNOWN REASONING LEVEL: UNKNOWN / NOT_EXPOSED
PROVIDER REASONING USAGE: null / NOT_EXPOSED
EXECUTION: WITHOUT_VERIFIED_BRAIN
STATUS: PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy-influence conjecture remains OPEN / NOT PROVED.
NOVELTY / PRIORITY: NOT CLAIMED.

Fresh authenticated control at entry:
`yspennstate/math-research-brain` main
`9c61c2bffacf3a9f1253aff0300998f19c51a39a`,
OWNER CONTROL revision `2026-09-21.1`.
The natural-language OWNER MESSAGE was read.  No account02/B17 pause or stop
was present.  Live allocation remained 8 brain B01-B06/B19-B20, 5 benchmark
B07-B11, and 7 FEI B12-B18.

Fresh scientific master at entry:
`yspennstate/math-open-problems`
`3e44558338d82f9307eaf359fa8820de511fb355`,
refreshed before persistence to
`04b23c1d04f73bee258b7b69775d3556e63ff032`.

Normalization:
`f:F_2^n->{-1,+1}`, normalized Walsh transform,
`p_S=hat f(S)^2`,
`H(f)=sum_S p_S log_2(1/p_S)`.
After a median-character gauge,
`j_i=Inf_i(f)<=1/2` and `J=sum_i j_i`.
For the folded pivotality event
`eta_i=1_{f(x)!=f(x+e_i)}`, its physical support-disagreement is

    p_ik = Pr[eta_i(x) != eta_i(x+e_k)].

The account04 mixed-curvature identity is

    4 q_ik = p_ik + 4 o_ik,

where `q_ik=Pr_{spectral}(i,k in S)` and `o_ik>=0` is opposite-sign overlap.

## 0. Last-three comparison and the moves used

The last three completed substantive B17 mechanisms are:

1. `20260921T194732Z-harmonic-riesz-curvature`:
   odd majority refuted the ordinary derivative-depth and positive-defect banks;
   harmonic Riesz rows replaced the second factorial bank by `I-tau`.
2. `20260921T204329Z-interaction-companion-factorization`:
   tensor powers showed the global harmonic residual is FEI-hard; replacement
   was exact plaquette factorization before coding a connected component.
3. `20260921T215432Z-selector-phase-low-plaquette`:
   an address-only phase made an exact tensor spectrum physically connected,
   refuting the stop-conditioned prefix-TC payment; replacement was low
   cross-plaquette approximate multiplicative factorization.

**FULL-PROBLEM CHANGE:** none.  No finite universal FEI constant is proved.

**MECHANISM CHANGE:** yes.  This run leaves the entropy-continuity/approximate-
product route and attacks the newest interface-B exceptional-row bottleneck.
The adversary is a connected quadratic Boolean family whose derivative rows
are *all* outside the coordinate-subcube robust sector while the support-depth
ratio remains only `M/J=1`.  The replacement changes coordinates rather than
restricting them: an affine-parity derivative support can be straightened by
an invertible physical linear change, with its exact folded-influence cost
paid.  This exposes a genuinely new robust sector to the existing physical
restriction compiler.

FLEET_RULES moves used in the mathematics:
- #1 CHANGE THE CATEGORY: from coordinate-subcube geometry to invertible
  linear-coordinate surgery with exact influence accounting.
- #6 DEFORM TO A POINT YOU CAN SOLVE: first solve exact affine-parity
  pivotality, then quantify an `e`-approximate version.
- #12 FIND WHAT IS CONSERVED: spectral entropy is exactly invariant under
  invertible linear changes; the only price is folded influence.
- #18 SAY IT IN ANOTHER LANGUAGE: the B18 mixed face law is used as a
  coordinate-change cost identity rather than as a depth bank.

## 1. Named completed other-account results consumed

### 1.1 account04/B13: one-shot robust-row elimination

I use
`account04/B13/20260921T2122Z-source-frontier-one-shot/REPORT.md`,
identified in the current integration ledger by blob
`8cced1e67ed2181463caaf877946717e81e4e7c8`.

At the current relative threshold `epsilon=1/16`, it treats derivative supports
`E_i` which are within

    e_i = mu(E_i triangle Q_i) <= j_i/16

of a coordinate subcube `Q_i`.  Using the compatible integrability DAG, one
physical reveal block leaves expected folded influence at most

    E J(child) <= J_E + (1/16) J_R,

where `R` is the robust set and `E` is the arbitrary exceptional set.  Its
explicit missing arrow is control of the exceptional influence `J_E`; it does
not claim that `J_E` is small.

### 1.2 account04/B18: current stalled-core integration

I also use
`account04/B18/20260921T221132Z-support-depth-stalled-core/REPORT.md`.
It identifies

    M = (1/4) sum_{i!=k} p_ik

as exactly the unsigned-support share of the second-factorial mixed-curvature
bank and sharpens robust trigger load to the `M` bank.  Its remaining live
sector is the stalled/kernel-free fixed-relative error-discovery and
exceptional-row sector.

### 1.3 account01/B14: adaptive pivotality determination

During this invocation the newer
`account01/B14/20260921T224055Z-adaptive-pivotality-selector/REPORT.md`,
blob `585cbdfc282e636c95b70bd479d4c720b19f1948`, landed.  It proves that a
physical decision tree determining one folded pivotality event has its target
information paid by the *actual folded-J drift*, and reduces full FEI to the
existence of a determining tree with a bounded corrected-entropy cost.
The affine-parity mechanism below supplies an explicit family of pivotality
events that is invisible to the coordinate-subcube classifier but is exactly
linearizable/determinable.  I do not claim it proves account01/B14's remaining
universal corrected-cost bound.

## 2. Boolean adversary: a connected quadratic cycle has no robust subcube row

For `n>=5`, index coordinates cyclically and define

    Q_n(x) = sum_i x_i x_{i+1}  (mod 2),
    f_n(x) = (-1)^{Q_n(x)}.

This is a genuine Boolean common potential, not a row relaxation.

For each coordinate `i`,

    Delta_i Q_n(x) = x_{i-1} + x_{i+1}  (mod 2).

Therefore the pivotality support is exactly

    E_i = {x : x_{i-1} xor x_{i+1} = 1}.                 (2.1)

It has density `j_i=1/2`, so the median gauge is already centered.

### 2.1 Every row is genuinely exceptional for coordinate-subcube stability

The set in (2.1) is the disjoint union of the two codimension-two cells

    {x_{i-1}=0,x_{i+1}=1}
    union
    {x_{i-1}=1,x_{i+1}=0}.

For any coordinate subcube `Q`:

- if `Q` fixes neither or only one of the two neighbours, its intersection
  with `E_i` occupies exactly half of `Q`;
- if it fixes both neighbours, either `Q` is disjoint from `E_i` or is
  contained in one of the two cells above and has measure at most `1/4`;
- fixing more coordinates only decreases that measure.

Consequently

    boxed:  inf_{coordinate subcubes Q} mu(E_i triangle Q) = 1/4.  (2.2)

The bound is attained by either one of the two codimension-two cells.
Since `j_i/16=1/32`, **no row is robust** at the account04/B13 threshold.
Thus

    R = empty,
    J_E = J = n/2.                                      (2.3)

This remains true under either median-character orientation, because
complementing (2.1) gives the other parity halfspace with the same distance.

### 2.2 Yet the support-depth bank is only M=J

From (2.1),

    p_ik =
      1,  k=i-1 or i+1,
      0,  otherwise.                                    (2.4)

Hence the physical interaction graph is exactly the cycle `C_n`, in particular
it is connected, and

    M=(1/4) sum_{i!=k} p_ik
     =(1/4)(2n)
     =n/2
     =J.                                                 (2.5)

Therefore the following natural strengthening of the current B13/B18 bridge is
false:

> bounded support depth by itself forces a nonzero fixed fraction of folded
> influence into the coordinate-subcube robust sector.

Indeed already at `M/J=1`, the robust influence fraction can be exactly zero.

This is a counterexample only to that stronger bridge.  It is not a
counterexample to FEI.  For calibration, `f_n` is a quadratic phase; its polar
matrix is the adjacency matrix of `C_n`, whose F_2-rank is `n-1` for odd `n`
and `n-2` for even `n`.  Its squared Fourier spectrum is plateaued on the
corresponding affine support, so

    H(f_n)=n-1  (n odd),
    H(f_n)=n-2  (n even),

and `H/J<2`.

The obstruction is precise: a coordinate-subcube classifier confuses
"nonrigid" with "not axis-aligned".  Here every derivative row is perfectly
rigid, but its rigid object is an affine parity halfspace rather than a
coordinate subcube.

## 3. Exact local coordinate-change identity with the signed credit retained

Let `f` be median-character centered, so `I(f)=J(f)`.
For distinct `a,b`, let `T_{a->b}` be the elementary shear

    x_a = y_a xor y_b,
    x_k = y_k  for k!=a,

and put `g(y)=f(T_{a->b}y)`.

A Fourier character indexed by `S` is sent to the character indexed by `R`
with

    R_a=S_a,
    R_b=S_b xor S_a,

and all other bits unchanged.  Therefore squared Fourier masses are merely
permuted and

    boxed: H(g)=H(f).                                    (3.1)

Only the Hamming-weight contribution of coordinate `b` changes, so exactly

    I(g)-I(f)
      = Pr(S_a=1,S_b=0)-Pr(S_a=1,S_b=1)
      = j_a-2q_ab.                                       (3.2)

Using account04/B18's genuine Boolean mixed-face identity,

    4q_ab=p_ab+4o_ab,

this is

    boxed:
    I(g)-J(f)=j_a-p_ab/2-2o_ab.                          (3.3)

After a new character fold, `J(g_centered)<=I(g)`.  Thus a shear has the
source-admissible cost bound

    boxed:
    J(g_centered)
      <= J(f)+j_a-p_ab/2-2o_ab
      <= J(f)+(2j_a-p_ab)/2.                             (3.4)

The last term is nonnegative because `p_ab<=2j_a`; the **opposite-sign
overlap is a genuine negative credit** and is not discarded in the exact
formula (3.3).

This is a different use of the signed mixed-curvature law from an all-row depth
payment: it prices an actual invertible Boolean coordinate operation.

## 4. PROVED: affine-parity straightening with quantitative folded-J cost

Let `f` again be centered and let

    E_i={x: eta_i(x)=1},  mu(E_i)=j_i<=1/2.

Suppose there is a nonempty control set
`F subset [n]\{i}`, `r=|F|`, an affine parity halfspace

    P_{F,c}={x: xor_{k in F} x_k = c},

and an error

    e=mu(E_i triangle P_{F,c}) < 1/2.                    (4.1)

### Theorem 4.1 — affine-parity straightening

There is an invertible linear map `T` which fixes `i` and every coordinate
outside `F`, followed by a character fold using only coordinates in `F`, such
that for `g=f o T` after that fold:

1. `H(g)=H(f)`;
2. the `i`-pivotality support of `g` is at the same error `e` from a
   **single-coordinate halfcube** `{y_k=c}` for some `k in F`;
3.
   \[
   \boxed{
   J(g)\le J(f)+r e
        \le {1\over1-2e}\,J(f).
   }
   \tag{4.2}
   \]

In particular, if `e=0`, the straightening has **zero folded-influence cost**:

    boxed: J(g)<=J(f).                                   (4.3)

If `e<=1/34`, then

    boxed: J(g)<=17/16 J(f),                             (4.4)

and the transformed row obeys the account04/B13 relative robust threshold

    boxed: e <= j_i/16.                                  (4.5)

#### Proof

Choose `T|_F in GL(r,2)` so that

    xor_{k in F} (Ty)_k = y_{k_0}

for one chosen `k_0 in F`; extend it by the identity outside `F`.
A concrete triangular realization orders
`F=(k_1,...,k_r)` and uses

    x_{k_s}=y_{k_s} xor y_{k_{s+1}}  (s<r),
    x_{k_r}=y_{k_r},

whose parity telescopes to `y_{k_1}`.

Invertible linear changes permute Walsh coefficients, proving entropy
invariance.  Since `T` fixes `i`, the pivotality event is simply pulled back,
so the symmetric-difference error is exactly preserved and the affine parity
becomes a coordinate literal.

It remains to pay the coordinate change.

First, because a parity halfspace has measure `1/2`,

    j_i >= 1/2-e.                                        (4.6)

For each `k in F`, the parity indicator flips on every `k`-edge.  If
`eta_i` differs from the parity at neither endpoint, its `k`-edge also flips.
Therefore

    p_ik >= 1-2e.                                        (4.7)

Mixed-face symmetry gives `p_ki=p_ik`.  Since the centered `k`-pivotality
event has measure `j_k`,

    p_ki <= 2j_k.

Hence

    j_k >= 1/2-e   for every k in F.                     (4.8)

The linear map acts only inside `F`, so every spectral marginal outside `F`
is unchanged.  After character-folding the transformed `F` coordinates, each
of their folded marginals is at most `1/2`.  Thus

    J(g)
      <= J(f)-sum_{k in F}j_k+r/2
      <= J(f)+r e.                                       (4.9)

Equation (4.8) also gives
`J_F>=r(1/2-e)`, hence

    r e <= [2e/(1-2e)] J_F <= [2e/(1-2e)]J(f),

which proves (4.2).

At `e=1/34`, `2e/(1-2e)=1/16`, proving (4.4).
Also (4.6) gives `j_i>=8/17`, so
`e/j_i<=(1/34)/(8/17)=1/16`, proving (4.5).  QED.

### Why this directly answers the cycle obstruction

For the cycle family, every row has `e=0` from the affine parity on its two
neighbours.  Theorem 4.1 therefore turns any chosen row into an exact
coordinate-halfcube row with **no increase of J**, despite (2.2) showing that
the original row was distance `1/4` from every coordinate subcube.

So the right interface-B distinction is not
"near subcube versus exceptional"; it must at least quotient out cheap affine
parity straightening.

## 5. PROVED: the straightened near-parity row has a strongly paid physical split

The transformed row has more than just geometric robustness.

Assume `e<=1/34` and let `k` be the literal control after Theorem 4.1.
Let the active halfcube be `Q={x_k=c}`.

Write

    a=mu(Q\E_i),  b=mu(E_i\Q),

so `e=a+b` and

    j_i=1/2-a+b <=1/2.

Hence `b<=a`.

Conditioning on `x_k`, the posterior pivotality on the active branch is
`1-2a`, while on the inactive branch it is `2b`.  Since `e<1/4`, only the
active branch crosses `1/2`.  Therefore the exact `i`-coordinate crossing is

    boxed: c_i({k}) = 1/2-2a = j_i-e.                    (5.1)

Equivalently, the expected child folded influence of the pivot is exactly `e`.

Also, because the literal itself flips on every `k`-edge except where one
endpoint is in the error set,

    p_ik>=1-2e.

By mixed-face symmetry and `p_ki<=2j_k`,

    j_k>=1/2-e.                                          (5.2)

The exact folded restriction drift is

    D_k = j_k + sum_{ell!=k} c_ell({k}),

so (5.1)--(5.2) give

    boxed: D_k >= j_k+c_i({k}) >= 1-3e.                  (5.3)

The one-coordinate spectral restriction identity is a sum of a
Jensen--Shannon term and a binary conditional-entropy term, each at most one
bit.  Hence universally

    Delta_k H <=2.

Combining with (5.3),

    boxed:
    Delta_k H <= [2/(1-3e)] D_k.                         (5.4)

At `e<=1/34`,

    boxed:
    Delta_k H <= (68/31) D_k
               <2.194 D_k.                              (5.5)

For exact affine parity (`e=0`), straightening is free and the physical split
satisfies simply

    boxed: J(after straightening)<=J(before),
           Delta_k H <=2 D_k.                            (5.6)

This is a genuinely paid source-admissible step.  It is much stronger than
merely saying the parity event has a small decision tree.

It also dovetails with the new account01/B14 determination theorem: a parity
pivotality event is determined by its controls, but (5.4) identifies a
one-coordinate paid split **after** entropy-preserving affine straightening.
The remaining issue is not local information payment; it is global
amortization of approximate affine-coordinate changes.

## 6. The new universal bridge: nonreusing affine straightening + physical drift

A naive repeated use of the approximate form of Theorem 4.1 would be invalid:
even the small factor `17/16` may compound over many descendants.
The correct next object is an additive affine-inflation ledger.

At a restriction-tree node `v`, let a chosen parity straightening increase
folded influence by

    c_v := J(T_v f_v after fold)-J(f_v) >=0,

taking zero if it decreases.  Theorem 4.1 supplies

    c_v <= r_v e_v.                                      (6.1)

After straightening, take a physical restriction with folded drift `D_v`.
Because spectral entropy is invariant under `T_v`, a tree telescope gives

    sum_v pi_v D_v
      <= J(root) + sum_v pi_v c_v                        (6.2)

with equality up to the terminal folded influence in the natural orientation.

Therefore a sufficient new global interface is:

(AFFINE-AMORTIZATION)
There is a dimension-independent `theta` and an adaptive choice of
affine-parity straightening / physical restriction steps, ending in already
paid terminals, such that

    boxed:
    sum_v pi_v c_v <= theta J(root),                     (6.3)

while every physical split obeys

    Delta_v H <= C_0 D_v                                (6.4)

for one dimension-independent `C_0`.

Then, summing the entropy decrements,

    H(root) <= C_0(1+theta) J(root)
             + paid terminal contribution,              (6.5)

which gives full FEI once the terminals are closed.

For the exact-parity sector, `c_v=0`; the cycle adversary is therefore
handled at zero affine cost.  For `e<=1/34`, each local cost is at most
`r_v e_v`, while the physical split itself has `C_0<=68/31`.

**This is OPEN.**  The precise universal gap is now:

> Construct a nonreusing affine-parity straightening forest whose expected
> total `sum pi_v r_v e_v` is `O(J(root))`, or prove that a terminal core
> which is far from every affine parity in every derivative row is paid by
> a different existing B/A-interface mechanism.

This is materially different from:
- the refuted ordinary derivative-depth bank;
- the FEI-hard global harmonic-Riesz residual;
- exact interaction-component factorization;
- the previous ambient-dimension entropy-continuity penalty.

It is also source-admissible throughout: every object is an actual Boolean
common potential, an invertible cube-linear change, or a physical restriction.

## 7. Exact sanity checker

`verify_affine_parity_straightening.py` was executed.

Exact Fraction/integer pass/fail scope:

- 1,568 elementary-shear identities through all Boolean functions in `n<=3`;
- 3,216 affine-parity straightening instances over every centered Boolean
  function in dimensions 2 and 3, all pivots, all nonempty parity supports,
  and both affine signs with error at most `1/2`;
- 304 small-error instances checking the exact folded-drift bound
  `D>=1-3e` at `e<=1/34`;
- all 26 derivative rows of the quadratic cycles `n=5,6,7,8`;
- 24,462 coordinate subcubes compared against those cycle rows, verifying
  nearest distance exactly `1/4`;
- exact `J=M=n/2` and the cycle plaquette pattern in every tested dimension.

No floating-point entropy comparison decides any pass/fail assertion.

Checker SHA-256:
`22c541791a3415c78478675a7c25eb1b3988b867e0bf547fa31d4c33d927f05b`

Output SHA-256:
`611db05a64076f902e5566f22dc3c3569799a9e471044be4ad7c94b569e823b3`

Finite checks establish only their stated scope; Theorems 4.1 and 5.1 are
proved analytically above.

## 8. Literature applicability check

A fresh search on 21 September 2026 found no universal FEI resolution.

- Potapov, arXiv:2609.21563 (18 Sep 2026), proves FEI for plateaued functions
  with sharp class constant 4 and for partially bent functions with sharp
  class constant 2.  This is compatible with the quadratic-cycle calibration;
  it does not prove the universal affine-amortization bridge.
- Gonzalez--MacManus--Pereyra, arXiv:2606.00246 (29 May 2026), develops
  restriction/stopping arguments for further classes and explicitly leaves
  the universal conjecture open.
- Li--Han, arXiv:2512.03117 (2 Dec 2025), gives the sharp structural
  `H <= I + sum_i I_i log(1/I_i)`-type inequality; the marginal logarithmic
  term is precisely not the universally paid remainder here.

No novelty claim is made for Fourier invariance under linear changes,
quadratic-phase normal forms, or the elementary shear algebra.  The new
research delta claimed only at internal self-check level is their source-exact
use against the current B13/B18 exceptional-row interface and the quantitative
affine-parity straightening/payment theorem above.

## 9. Before / after / remaining formula

BEFORE this run:
- account04/B13 could eliminate the coordinate-subcube robust sector in one
  shot, but left arbitrary exceptional mass `J_E`;
- account04/B18 localized robust trigger load to support depth `M`, while its
  stalled-core report still named exceptional/error discovery as the live
  interface-B obstruction.

AFTER:
- the connected Boolean quadratic-cycle family proves that `M/J=1` can coexist
  with `J_E/J=1`; bounded support depth does not force any coordinate-subcube
  robust mass;
- the same "exceptional" rows are exact affine parities and can be converted
  to coordinate-halfcube rows by an entropy-preserving linear change with
  **zero** folded-J cost;
- an `e`-near affine parity can be straightened with
  `J_new <= J/(1-2e)`, and at `e<=1/34` it enters the `1/16` relative robust
  regime with a physical split satisfying
  `Delta H <= (68/31) D`;
- the next universal implication is the additive affine-amortization formula
  (6.3), not another scalar `M=O(J)` assertion.

FULL FEI remains OPEN / NOT PROVED.
