TASK: B18 ACCOUNT: account02 RUN: 2026-09-21T19:07:55.901804Z — affine-subspace rank-two plaquette payment and compiler integration.

MODEL: GPT-5.6 Sol (runtime self-report)
REQUESTED EFFORT: maximum actually supported
CONFIGURED / KNOWN REASONING LEVEL: UNKNOWN / NOT_EXPOSED
EXPOSED PROVIDER REASONING USAGE: null / NOT_EXPOSED
EXECUTION: WITHOUT_VERIFIED_BRAIN
FULL FEI STATUS: OPEN / NOT PROVED

Fresh authenticated control on entry was `yspennstate/math-research-brain` main
`eda9c31c3c46d5797fe08950a4ed0f041924d122`, OWNER CONTROL revision
`2026-09-21.1`; it was refreshed before persistence to
`9fd93bbe181b6242749e24605411d36b3ac51389`, with the same README blob
`14c6dfefb9a567d99dea06c7cd48dbb38e7a56c9` and no B18/account02 pause or stop.
The live directive is `FEI-FULL-PROOF-PROGRESS-2026-09-21-174421Z`.

Fresh scientific master used for the final integration was
`yspennstate/math-open-problems` master
`bd0e57e6297a1078b42c6f39e8eb843d3c32fa79`.

## 0. Before / after and the last three B18 runs

The last three substantive account02/B18 reports were read before this derivation:

1. `20260921T160323Z-joint-phase-packing`: simultaneous product-law/Hellinger
   phase packing; remaining obstruction was the diffuse curl-free phase-balanced
   rare-coordinate regime.
2. `20260921T170605Z-qflip-dependent-triple-radon-frame`: exact dependent-triple
   q-flip/Radon dictionary and a conditional compiler-frame criterion; a raw arbitrary
   q-flip frame without physical incidence normalization was shown insufficient.
3. `20260921T180403Z-mask-resolvent-transfer`: exact plaquette-mask transfer for
   arbitrary correlated selectors, but the quantitative payment was still routed
   through **physical product-noise** directions and cost
   `2 M_Omega sum_j theta_j J(m_j)`.

**FULL-PROBLEM CHANGE: NONE.** No finite dimension-independent constant `C` is proved
for all Boolean functions. Full FEI remains open.

**MECHANISM CHANGE: YES.** The previous mask route treated a positive
physical-product-noise pushforward as part of the missing compiler bridge. This run
changes category to the quotient geometry of the actual parent masks and proves a
stronger **pointwise, arbitrary-q-flip pair** payment. Thus product-noise structure is
no longer needed on the mask-payment side at all. The only remaining representation
problem is the authentic signed/PSD compiler-source-to-physical-pair contraction.

Tracked mechanism quantity:

- before: mask-transfer payment required a product-noise average and carried factor
  `2 M_Omega`;
- after: every affine-subspace parent mask obeys a pointwise arbitrary-pair bound with
  constant **1**, so any positive pair measure is paid solely by its total parent mass;
- full FEI constant: unchanged / not proved.

The three deliberate FLEET_RULES moves are:

- **#14 FIND THE GROUP ACTING:** quotient the physical cube by the affine mask's
  direction subspace and classify a plaquette by the rank of its two quotient shifts;
- **#25 COUNT THE SAME THING TWICE:** count the same frustrated plaquette first by
  parity of four mask memberships and then by membership of one quotient point in an
  affine 2-plane;
- **#27 SWAP THE QUANTIFIERS:** instead of proving an estimate only after averaging a
  prescribed noise law, prove it for **every pair `(u,v)` first**, after which every
  positive averaging law is automatic.

## 1. Small current dependency chain

Only the following pieces are used.

### Input A — authentic signed current parent weights

From account02/B16
`20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`, after same-syndrome
signed aggregation and the genuine double-resolvent square, the central bank has
nonnegative parent weights

    mu_j = sum_{R: j doubled in R}
           [epsilon_{q_R,k_R}/r_R] b_R^2,

with

    sum_j mu_j = E_cen,

and the actual coarse parent mask `g_j` is a one-subcube defect. Its already-proved
projective incidence satisfies

    sum_j mu_j J(g_j) <= E_cen <= (11/192) W.              (1.1)

This input retains the signed syndrome aggregation before squaring. I do not reopen or
absolute-value its R32 coefficients.

### Input B — exact XOR stability of plaquette frustration

For a Boolean phase `h:G->{-1,+1}`, define

    r_h(x;u,v) in F_2

by

    (-1)^{r_h(x;u,v)}
      = h(x)h(x+u)h(x+v)h(x+u+v),

and let

    P_h(u,v)=Pr_x[r_h(x;u,v)=1].                           (1.2)

For Boolean phases `f,m`,

    r_{fm}=r_f xor r_m.                                    (1.3)

Therefore

    |P_{fm}(u,v)-P_f(u,v)| <= P_m(u,v).                   (1.4)

This is the exact mask-stability identity from the preceding B18 route. What was
missing was a dimension-free pointwise estimate on `P_m(u,v)` for the actual masks.

### Input C — fresh signed compiler state

The current account03/B16 report
`20260921T185632Z-integrated-phase-switch-logarithmic-bridge/REPORT.md` proves that the
full signed Borel phase switch can be integrated exactly into a dual-code entropy
increment, while an arbitrary finite live window cannot be controlled from the
full-line endpoint alone. Its next target is a two-copy/window-sensitive physical
polarization. The theorem below is designed to accept **any** positive physical pair
kernel produced by that polarization; no product-noise shape is required.

No other old FEI conditional is needed for the new theorem.

## 2. Setup: affine-subspace defect masks

Let

    G = F_2^n.

Let `L<=G` be a linear subspace of codimension `c`, let `a in G`, and let

    Q = a+L.

Define the affine-subspace defect phase

    g_Q(x) = -1,  x in Q,
             +1,  x notin Q.                              (2.1)

Let

    pi:G -> G/L

be the quotient map. The quotient has cardinality `2^c`.

The inherited B16 one-subcube masks are the special case in which `L` is a coordinate
subspace. The proof below uses no coordinate-subcube assumption.

## 3. PROVED — exact rank-two quotient formula

### Theorem 3.1 — `P03-B18-AFFINE-SUBSPACE-PLAQUETTE-RANK`

For every affine subspace `Q=a+L` of codimension `c` and every translations `u,v in G`,

    P_{g_Q}(u,v)
      = 2^(2-c) * 1{ pi(u), pi(v) are linearly independent in G/L }.   (3.1)

For `c=0,1`, the right side is identically zero because the quotient has no independent
pair.

### Proof

Write

    U=pi(u),  V=pi(v),  A=pi(a),  X=pi(x).

Membership in `Q` depends only on the quotient and is exactly the event that the
quotient point equals `A`. Thus the plaquette mask product is `-1` precisely when the
multiset

    X, X+U, X+V, X+U+V                                (3.2)

contains `A` an odd number of times.

There are three rank cases over `F_2`.

**Rank zero.** If `U=V=0`, all four entries in (3.2) coincide. Hence `A` occurs with
multiplicity either four or zero, always even. The plaquette is unfrustrated.

**Rank one.** If `span{U,V}` has dimension one, the multiset (3.2) consists of two
distinct quotient points, each with multiplicity two. Again the multiplicity of `A` is
even and the plaquette is unfrustrated.

**Rank two.** If `U,V` are independent, the four entries in (3.2) are the four distinct
points of the affine plane

    X + span{U,V}.                                       (3.3)

The plaquette is frustrated exactly when this plane contains `A`, in which case exactly
one of its four vertices equals `A`. As `X` is uniform on `G/L`, exactly the four choices

    X in A + span{U,V}

produce a plane containing `A`. Hence

    P_{g_Q}(u,v)=4/2^c=2^(2-c).

This proves (3.1). `square`

### Interpretation

For an affine-subspace defect, the entire four-point nonlinear mask response forgets
the ambient dimension and the location of the affine subspace. It depends only on the
rank of the two physical translations after quotienting by `L`.

This is the exact geometry that the previous product-noise averaging obscured.

## 4. PROVED — exact folded influence and pointwise plaquette payment

For a Boolean phase `h`, write the folded/projective physical influence

    beta_h(e_i)
      = min( Pr[h(x)!=h(x+e_i)],
             1-Pr[h(x)!=h(x+e_i)] ),

and

    J(h)=sum_i beta_h(e_i).                               (4.1)

Let

    m_L = #{i : e_i notin L}.                             (4.2)

Because the images `pi(e_i)` span the `c`-dimensional quotient, necessarily

    m_L >= c.                                             (4.3)

### Lemma 4.1 — exact coordinate cost

For `g_Q`:

- if `e_i in L`, then translation by `e_i` preserves `Q`, so its disagreement
  probability is zero;
- if `e_i notin L`, then `Q` and `Q+e_i` are distinct cosets of `L` and hence disjoint,
  so their symmetric difference has measure

      2 * 2^(-c) = 2^(1-c).                              (4.4)

Consequently:

- `c=0`: `J(g_Q)=0`;
- `c=1`: every nonzero coordinate disagreement is exactly `1`, so the folded cost is
  zero and `J(g_Q)=0`; equivalently `g_Q` is a character up to sign;
- `c>=2`:

      J(g_Q)=m_L 2^(1-c) >= c 2^(1-c).                   (4.5)

### Theorem 4.2 — `P03-B18-AFFINE-MASK-POINTWISE-PAYMENT`

For every affine-subspace defect `g_Q` and **every** `u,v in G`,

    boxed:  P_{g_Q}(u,v) <= J(g_Q).                       (4.6)

The constant one is sharp.

### Proof

For `c=0,1`, Theorem 3.1 gives `P=0`, while `J=0` by Lemma 4.1.

For `c>=2`, if the quotient shifts are dependent then `P=0`. If they are independent,
Theorem 3.1 and (4.5) give

    P_{g_Q}(u,v)
      = 2^(2-c)
      <= m_L 2^(1-c)
      = J(g_Q),                                           (4.7)

because `m_L>=c>=2`.

For a rank-two pair the exact ratio is

    P/J = 2/m_L <= 2/c.                                  (4.8)

At codimension two with exactly two nontrivial physical quotient columns, equality is
attained, so the universal constant one cannot be improved. `square`

### Corollary 4.3 — stronger codimension dependence

For `c>=2`,

    P_{g_Q}(u,v) <= (2/c) J(g_Q).                         (4.9)

This refinement is not needed for FEI closure but shows that high-codimension masks are
strictly cheaper than the universal constant-one envelope.

## 5. PROVED — arbitrary positive pair measures; product noise is unnecessary

The pointwise theorem can be inserted into the mask XOR identity before imposing any
directional law.

### Theorem 5.1 — `P03-B18-ARBITRARY-PAIR-MASK-TRANSFER`

Let `{Q_j}` be affine subspaces of `G` and `g_j=g_{Q_j}`. For each `j`, let `Lambda_j`
be any finite nonnegative measure on ordered translation pairs `(u,v) in GxG`, with

    mu_j := Lambda_j(GxG).                               (5.1)

Then for every Boolean `f`,

    boxed:
    sum_j integral |P_{f g_j}(u,v)-P_f(u,v)| dLambda_j(u,v)
      <= sum_j mu_j J(g_j).                              (5.2)

No independence, product-noise parameterization, common direction law, or probability
normalization is assumed.

### Proof

For each fixed `(j,u,v)`, (1.4) and Theorem 4.2 give

    |P_{f g_j}(u,v)-P_f(u,v)|
      <= P_{g_j}(u,v)
      <= J(g_j).                                         (5.3)

Integrate against the nonnegative measure `Lambda_j` and sum over `j`. `square`

### Corollary 5.2 — arbitrary correlated selector version

If `Z=(Z_j)` is an arbitrary, possibly correlated `{0,1}^N` selector vector,
`theta_j=E Z_j`, and

    M_Z = product_j g_j^{Z_j},

then for every fixed pair `(u,v)`,

    E_Z |P_{f M_Z}(u,v)-P_f(u,v)|
      <= sum_j theta_j J(g_j).                           (5.4)

Indeed the plaquette bit of a product is the XOR of the selected mask plaquette bits,
so the event that the mask product is frustrated is pointwise bounded by the sum of the
selected individual frustration indicators. No selector independence is used.

This strictly strengthens the preceding B18 mask-resolvent theorem on its mask-geometric
side: the former theorem needed an averaged physical product-noise estimate and paid a
factor `2 M_Omega`; (5.2) is pointwise before averaging and has constant one.

## 6. Integration with the authentic current parent bank

Apply Theorem 5.1 to the actual B16 parent masks `g_j` and actual central parent masses
`mu_j` from Input A.

### Corollary 6.1 — `P03-B18-ACTUAL-PARENT-ARBITRARY-PAIR-PAYMENT`

Suppose an authentic compiler step produces, for each actual central parent `j`, a
nonnegative physical pair measure `Lambda_j` whose total mass is the already-derived
post-current mass `mu_j`. Then, without any further assumption on the direction law,

    sum_j integral |P_{f g_j}-P_f| dLambda_j
      <= sum_j mu_j J(g_j)
      <= E_cen
      <= (11/192) W.                                     (6.1)

Thus **the parent-mask geometry and its physical direction law are fully paid** once a
positive parent-indexed physical pair representation exists. Product noise is one
possible representation but is not required.

### What is not proved here

The antecedent of Corollary 6.1 is still the central universal gap. This report does not
construct `Lambda_j` from the dual-code/Borel compiler and does not claim that an
arbitrary PSD quadratic form can be read as a plaquette probability.

In particular, the following remain unpaid:

1. the authentic signed/PSD source-to-physical-pair representation or contraction;
2. preservation of the nested `C0-D_d` terminal subtraction and full dual-code
   multiplicity in that representation;
3. proof that the Ward/R16 bank on the right of (6.1) is consumed only once, not once in
   the source contraction and again in the mask payment;
4. the live finite-window / endpoint boundary bookkeeping and retained negative entropy
   credits;
5. the final conversion of all compiler expenditures to one finite multiple of the
   original physical influence.

So (6.1) is **not** the full FEI proof. It removes one previously explicit structural
requirement from the remaining bridge.

## 7. Interface with the two freshest neighboring mechanisms

### 7.1 account03/B18 physical flag square bank

The fresh physical flag theorem proves

    sum_i E p_i(W)^2 <= J(f)                              (7.1)

and gives a conditional PSD compiler criterion. That theorem pays the **derivative /
dependent-face source** once the compiler is contracted into 1-Lipschitz dependent-face
discrepancies.

The theorem here is different: it pays the **actual parent mask** after any positive
physical pair realization, and it pays arbitrary q-flip pair directions pointwise.
Thus the two results are complementary rather than duplicate:

- account03/B18: compiler quadratic form -> dependent-face square -> `J(f)`;
- this report: parent-indexed physical pair -> affine-mask plaquette transfer ->
  `sum mu_j J(g_j)`.

A future source representation may use either interface, or both at distinct
non-reused ledger stages.

### 7.2 account03/B16 finite-window signed logarithmic bridge

The newest signed bridge proves an exact full-time entropy endpoint and an exact
finite-window cosine-integral kernel, while showing that endpoint control alone cannot
bound an arbitrary live subwindow. Its proposed two-copy polarization must still
produce a positive physical object without taking forbidden termwise absolute values.

The present theorem sharpens what that physical object must look like: **if** the
polarization reaches positive parent-indexed physical translation-pair measures, their
directional distribution can be completely arbitrary for the affine parent-mask part.
No proof should now spend effort forcing those directions into the narrower independent
product-noise family merely for mask payment.

### 7.3 B17 self-XOR route

B17's fresh self-XOR/Hellinger functional retains the full joint spectral difference law
and proposes `B(P_f)<=C_B J(f)` as an FEI-equivalent finiteness target. That is a separate
mechanism and is not rederived or claimed here.

## 8. Exact checker

The analytic theorem above does not rely on finite computation. A separate exact-rational
sanity checker was executed before persistence.

It reduces to the quotient `F_2^c`, enumerates every ordered pair `(u,v)` and every
quotient base point for `c=0,...,7`, and verifies both the rank-two formula (3.1) and the
minimal-coordinate-budget implication

    P <= c 2^(1-c) <= J

for `c>=2`.

Output:

    PASS
    quotient_c_range=0..7
    ordered_direction_pairs=21845
    rank2_direction_pairs=21096
    max_P_over_minimal_J=1 at_c=2
    analytic_expected_max=1 at_c=2

Checker SHA-256:
`03dd76e14e0ce7200fc7360148f1cf9357b7174d598a2b5407166b26244fe097`

Archived stdout SHA-256:
`c29ebeefb4e77ff94cec2d14fae70ba2f129ea0f75706a70285f6e15a12d0cd7`

These checks are implementation/falsification evidence only; Theorems 3.1, 4.2 and 5.1
are proved for all dimensions above.

## 9. PROVED / CONDITIONAL / OPEN / refuted-route ledger

### PROVED

1. `P03-B18-AFFINE-SUBSPACE-PLAQUETTE-RANK`: exact formula
   `P=2^(2-c)` exactly on quotient-rank-two direction pairs and zero otherwise.
2. Exact folded coordinate influence formula for every affine-subspace defect.
3. `P03-B18-AFFINE-MASK-POINTWISE-PAYMENT`: `P_g(u,v)<=J(g)` for every pair, sharp
   with constant one; stronger `P_g<=(2/c)J(g)` for codimension `c>=2`.
4. `P03-B18-ARBITRARY-PAIR-MASK-TRANSFER`: every positive pair measure costs only its
   total mass times `J(g)`; no product-noise law is required.
5. Arbitrary-correlated-selector pointwise transfer (5.4).
6. Conditional-on-representation compiler insertion (6.1) uses the **actual** B16 parent
   weights and inherits their exact `<=11/192 W` incidence bank without changing signs
   upstream.

### CONDITIONAL

Corollary 6.1 requires an authentic compiler-derived nonnegative physical pair measure
for each parent with total mass controlled by the already-derived `mu_j`. This report
proves the entire mask-payment implication **after** that representation, not the
representation itself.

### OPEN

- the signed/PSD compiler-source -> positive physical pair/dependent-face contraction;
- nonreuse of Ward/R16/terminal/negative-credit banks across that contraction;
- live finite-window boundary payment;
- a complete dimension-independent universal FEI bound.

### REFUTED / RETIRED AS A NECESSARY TARGET

The statement

> "to pay the actual affine parent masks, the source must first be represented by
> independent physical product-noise directions"

is false as a necessity. Theorems 4.2 and 5.1 pay **every** direction pair pointwise.
This does not refute product noise as one valid construction; it refutes spending future
runs on product-noise *shape* solely for mask-geometric payment.

## 10. Fresh literature applicability check

Primary/current literature was checked on 2026-09-21 before any scope claim:

- Potapov, arXiv:2609.21563 (18 Sep 2026), proves FEI for plateaued functions and sharp
  structured subclasses including partially bent functions; it does not prove
  unrestricted FEI.
- González, MacManus and Pereyra, arXiv:2606.00246 (29 May 2026), develop a
  restriction/stopping-tree framework; their full-FEI route retains a universal missing
  step.
- Li and Han, arXiv:2512.03117, and Han, arXiv:2312.08271, provide strong
  influence-profile bounds but not a dimension-independent unrestricted FEI theorem.

No publication-priority or novelty claim is made for the quotient-rank formulation from
a bounded literature search.

## 11. Exact remaining universal implication and next attack

The former B18 gap mixed two requirements:

1. make the signed compiler physical/positive;
2. force the resulting physical directions into a product-noise family so the parent
   masks can be paid.

This run removes requirement 2.

The exact remaining implication is now:

> **SOURCE REPRESENTATION TARGET.** Starting from the authentic same-syndrome signed
> current / finite-window two-copy kernel, derive a dimension-free PSD contraction or
> positive parent-indexed physical translation-pair representation, with each parent
> total mass controlled once by its genuine `mu_j`, while preserving terminal
> subtraction, dual-code multiplicity, R16/Ward refunds, negative entropy credits and
> boundary terms.

Once such a representation exists, the affine-parent mask side is already paid by
Theorem 5.1 and (1.1), with no extra directional geometry hypothesis.

The next B18 run should therefore expand **one authentic compiler quadratic / two-copy
finite-window block** through its marked parent and attempt a direct Gram/Markov
factorization into physical pair observables. It should not derive another mask
inequality, optimize a product-noise density, or return to the refuted global
phase/rank/l1 target.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
