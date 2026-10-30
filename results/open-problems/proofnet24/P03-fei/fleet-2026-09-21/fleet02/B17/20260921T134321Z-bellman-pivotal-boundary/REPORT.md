TASK: B17 ACCOUNT: fleet02 RUN: 2026-09-21T13:43:21.761774Z — scalar-corrected Bellman split, bent-swap obstruction, and pivotal-boundary replacement

Status: PARTIAL. Full Friedgut–Kalai Fourier entropy-influence (FEI) remains OPEN / NOT PROVED.
Brain status: WITHOUT_VERIFIED_BRAIN.
Role: FEI new proof mechanisms.
Live sprint scope: fleet02/B17, support-deficit transfer and its actual sharp obstruction.
Control revision adopted: 2026-09-21.1.
Math source at entry: yspennstate/math-open-problems master e067fbba2c77a956b240a924c833143bc3175ee9; refreshed before delivery.
Normalization: Boolean values ±1, uniform cube, base-2 spectral entropy H(f)=Σ_S p_S log2(1/p_S), p_S=fhat(S)^2, and total influence I(f)=Σ_S |S|p_S.

## 1. What changed

The preceding B17 run proved that the zero-slack balanced support-deficit inequality is already equivalent, constant-for-constant, to full FEI, and introduced the exact scalar-corrected quantity

    B_C(A) = C E(A) + kappa_C(delta(A)) - U(A).

This run derives the exact one-coordinate recurrence for B_C and then attacks the strongest natural local lemma: "B_C never decreases under a coordinate split."

That lemma is false for every finite C.  The obstruction can be made exact with a Boolean bent/rare-swap family.  More strongly, the bad prescribed split can have entropy-decrement / influence ratio tending to infinity even though BOTH restrictions have H/I <= 2 and the parent itself has H/I -> 2.  Thus local failure is phase instability, not FEI hardness.

This is not presented as discovery of the generic "wrong coordinate can be arbitrarily bad" phenomenon: that phenomenon is already explicit in earlier P03 bent/rare-flip work and in the 2026 stopping-tree literature.  The new route-specific point here is that the exact density credit kappa_C cancels completely on equal-density fibres, so it cannot repair that obstruction.

The obstruction leads to a replacement theorem.  For an equal-density minority split, the local entropy cost is either paid directly with constant

    K_dense = 2 + 3/ln 2 = 6.328085122666891...

or, in the rare-disagreement regime, is bounded by

    Delta_i H <= (1 + 3/ln 2) Inf_i(f) + (1/2) I(pivotal_i),

where pivotal_i is the residual set on which coordinate i is pivotal.  Hence at any target C >= 6.3281, dense equal-density splits are automatically safe; the only remaining local debt is a SECOND-ORDER PHYSICAL BOUNDARY of the pivotal set.  For the exact bent-swap obstruction that boundary has precisely the needed logarithmic order.

So the next universal gap is no longer "prove local Bellman monotonicity."  It is:

> pack / telescope the second-order pivotal-boundary debts over an adaptive restriction or block decomposition without charging the same physical influence unboundedly many times, while combining the unequal-density scalar-curvature term.

No claim is made that this remaining packing problem is solved.

## 2. Exact scalar-corrected support slack

Let A be a nonempty proper subset of {0,1}^n, g=1_A, delta=E g, and

    mu_A(S) = ghat(S)^2 / delta.

Let H_A be the Shannon entropy of mu_A, J_A=E_{S~mu_A}|S| and L(delta)=log2(1/delta).  Define

    U(A)=H_A-L(delta),
    E(A)=J_A-L(delta)/2,

and, with V_delta=4 delta(1-delta),

    kappa_C(delta)
      =(C/2-1)L(delta)+h2(delta)-h2(V_delta)/(4 delta).

Put f_A=2 1_A-1.  Then for every 0<delta<1,

    H(f_A)-C I(f_A)
      =4 delta [ U(A)-C E(A)-kappa_C(delta) ].

Therefore

    B_C(A)
      := C E(A)+kappa_C(delta)-U(A)
       = [C I(f_A)-H(f_A)]/(4 delta).                 (2.1)

The preceding report stated the reformulation for minority sets; (2.1) shows the algebra is valid for every proper nonempty A.  It is an exact identity, not a new FEI estimate.

Proof.  The empty Fourier mass of g is delta^2 and the nonempty mass is delta(1-delta).  For S nonempty, fhat_A(S)=2 ghat(S), so the nonempty spectral mass of f_A is V_delta and its conditional law is the normalized nonempty part of mu_A.  Hence

    H(f_A)=h2(V_delta)+4 delta [H_A-h2(delta)],
    I(f_A)=4 delta J_A.

Substitution gives (2.1).

## 3. Exact one-coordinate Bellman recurrence

Split A in coordinate i into residual sets A_0,A_1 with densities a,b>0.  Then delta=(a+b)/2.  For each residual Fourier index T write

    x_T = hat(1_{A_0})(T),
    y_T = hat(1_{A_1})(T),

and put

    w = a/(a+b),
    P(T)=x_T^2/a,
    Q(T)=y_T^2/b,
    nu(T)=w P(T)+(1-w)Q(T)=(x_T^2+y_T^2)/(a+b),

    r_T = (x_T-y_T)^2 / [2(x_T^2+y_T^2)]

for nonzero fibres, and r_T=0 on a zero fibre.  Finally

    q = E_{T~nu} r_T,
    JS = H(nu)-w H(P)-(1-w)H(Q),
    R  = E_{T~nu} h2(r_T),

and define the scalar

    phi(t)=h2(t)-h2(4t(1-t))/(4t).

Then

    B_C(A)
      = w B_C(A_0)+(1-w)B_C(A_1)
        + C q
        + phi(delta)-w phi(a)-(1-w)phi(b)
        - JS - R.                                    (3.1)

Proof.  The parent Fourier pair over residual T is

    ((x_T+y_T)/2, (x_T-y_T)/2).

After normalization by delta=(a+b)/2, its total mass is nu(T), and conditionally the selector bit is present with probability r_T.  Thus

    H_A = H(nu)+R
        = w H_{A_0}+(1-w)H_{A_1}+JS+R,

while

    J_A = w J_{A_0}+(1-w)J_{A_1}+q.

Insert these into U,E and B_C.  The terms involving (C/2-1)L cancel exactly because

    w L(a)+(1-w)L(b)-L(delta)

appears in E with coefficient C/2 and in U with coefficient 1, while kappa_C contains (C/2-1)L.  The remainder is (3.1).

This is the precise location at which the scalar correction succeeds and fails: it removes every density-log term, but it leaves the spectral interference term JS+R.

### Equal-density consequence

If a=b=delta, then w=1/2 and the phi term vanishes:

    B_C(A)-[B_C(A_0)+B_C(A_1)]/2
      = C q - JS - R.                                (3.2)

If theta=Pr[A_0 triangle A_1], then Parseval gives

    q = theta/(4a).

For f_A=2 1_A-1, theta=Inf_i(f_A), and multiplying (3.2) by 4a yields exactly

    C Inf_i(f_A)
      - [ H(f_A)-(H(f_{A_0})+H(f_{A_1}))/2 ].

So any universal nonnegative local increment for B_C on equal-density fibres is exactly a universal prescribed-coordinate restriction payment.

## 4. Exact Boolean obstruction: minority bent set plus a two-point swap

Let m=2k be even and define the standard quadratic bent function

    h_m(z)
      = (-1)^{ z_1 z_2 + z_3 z_4 + ... + z_{m-1} z_m }.

Every normalized Walsh coefficient of h_m has magnitude 2^{-m/2}, and

    E h_m = 2^{-m/2}=:t.

Take the MINORITY support

    A_0={z:h_m(z)=-1},

of density

    a=(1-t)/2.

Let

    x=(1,1,0,...,0) in A_0,
    y=(0,...,0) notin A_0,

and swap these two points:

    A_1=(A_0\{x}) union {y}.

The two child densities remain exactly a.  Form the parent set A whose selector fibres are A_0,A_1.

For every nonempty S,

    |hat(1_{A_0})(S)| = c := 2^{-m/2-1}.

The swap perturbation is

    hat(1_{A_1})(S)-hat(1_{A_0})(S)
      = 2^{-m}(chi_S(y)-chi_S(x)).

Exactly 2^{m-1} frequencies have nonzero perturbation, all of magnitude

    d=2^{1-m}.

Let

    epsilon=d/c=2^{2-m/2}.

For an affected frequency, the selector conditional probability r_S has one of two signs in the denominator.  In particular

    r_S <= r_max
       = epsilon^2 / [2(1+(1-epsilon)^2)].

Moreover nu(S) r_S=d^2/(4a) on every affected S.  Therefore their q-weights are uniform and

    q = 2^{-m}/(1-2^{-m/2}).                          (4.1)

Using h2(r)> r log2(1/r) for 0<r<1,

    R
      > q log2(1/r_max).

Since

    1/r_max
      = 2^{m-3}[1+(1-epsilon)^2]
      > 2^{m-3},

we obtain

    (JS+R)/q > R/q > m-3.                             (4.2)

Consequently, for EVERY finite C, choosing even m>C+3 makes the equal-density selector increment in (3.2) strictly negative.  Thus:

### Proposition

No finite C makes B_C monotone under every coordinate split.

This does NOT refute FEI and does NOT refute an existentially chosen coordinate or a stopping-tree proof.

### Finite source-admissible witness at m=10

Here

    a=31/64,
    q=1/992,
    epsilon=1/8,
    r_S in {1/226,1/290} on the 512 affected frequencies.

Since 226>2^7,

    R>7q,

so already at C=7,

    7q-JS-R<0

with no transcendental numerical comparison needed.

The obstruction is strikingly local because the functions themselves are easy.

The first child sign function is -h_m, hence

    H(f_0)=m,     I(f_0)=m/2,     H/I=2.

The swapped child differs at exactly x,y.  Counting changed physical edges gives

    I(f_1)
      = m/2 + (2m-4) 2^{1-m} > m/2,

while H(f_1)<=m simply because its spectral law has at most 2^m atoms.  Hence

    H(f_1)/I(f_1) < 2.

The (m+1)-bit parent differs from the selector-independent lift of -h_m at only the two points in the second fibre; similarly

    I(f_A)
      = m/2 + (2m-2)2^{-m},

and H(f_A)<=m+1, so

    H(f_A)/I(f_A) <= (m+1)/(m/2+(2m-2)2^{-m})
                   = 2+O(1/m).

At m=10 the exact checker gives

    I(f_0)=5,
    I(f_1)=161/32,
    I(f_A)=2569/512,

and therefore H(f_1)/I(f_1)<=320/161<2 and H(f_A)/I(f_A)<=5632/2569<2.2.

Thus an arbitrarily bad prescribed coordinate can sit inside functions whose global FEI ratio stays near 2.

This is the route-specific sharpening of the historical bent/rare-flip warning: the exact kappa_C correction does not touch it because equal child densities make the scalar curvature term identically zero.

## 5. Replacement theorem: the logarithmic debt is a pivotal-set boundary

The obstruction identifies what a valid proof must retain.

For an equal-density split, write theta=Inf_i(f_A)=Pr[A_0 triangle A_1] and let

    D_i = A_0 triangle A_1

be the residual pivotal set.  Assume we use the minority sign, so a<=1/2.  Then q=theta/(4a)<=1/2.

The equal-density fibre formula also has the exact pointwise form

    JS+R = E_{T~nu} Psi(r_T),                          (5.1)

where

    Psi(s)
      = h2(s)+1-h2(1/2+sqrt(s(1-s))).

Indeed, if z=x_T^2/(x_T^2+y_T^2), then the JS contribution is
1-h2(z), and

    sqrt(r_T(1-r_T))
      = |x_T^2-y_T^2|/[2(x_T^2+y_T^2)],

so h2(z)=h2(1/2+sqrt(r_T(1-r_T))).

The September-20 concave-restriction theorem proves Psi is concave on [0,1/2]; its symmetric extension Psi(s)=Psi(1-s) is concave on [0,1], with derivative zero at 1/2.  Hence Jensen gives

    JS+R <= Psi(q).                                   (5.2)

This use is within that theorem's exact normalization; no new concavity claim is needed.

### Elementary scalar bound

For 0<q<=1/2,

    Psi(q)
      <= q log2(1/q) + (3/ln 2) q.                   (5.3)

Proof.  First

    h2(q)
      <= q log2(1/q) + q/ln 2.

For the second term put s=2sqrt(q(1-q)).  In natural-log units define

    F(s)=((1+s)ln(1+s)+(1-s)ln(1-s))/2,
    G(s)=1-sqrt(1-s^2).

Then F'(s)=atanh(s), G'(s)=s/sqrt(1-s^2), and
atanh(s)<=s/sqrt(1-s^2) because the difference has nonnegative derivative and vanishes at zero.  Thus F<=G.  Since q<=1/2,

    G(s)=1-|1-2q|=2q.

Therefore

    1-h2(1/2+sqrt(q(1-q))) <= 2q/ln 2,

proving (5.3).

### Pivotal-boundary dichotomy

If q>=1/4, then log2(1/q)<=2 and (5.2)-(5.3) give

    Delta_i H(f_A)
      <= (2+3/ln 2) Inf_i(f_A),                      (5.4)

where

    2+3/ln 2 = 6.328085122666891....

If q<1/4, then theta=4a q<=2q<1/2.  Also

    log2(1/q)
      = log2(4a/theta)
      <= 1+log2(1/theta)

because a<=1/2.  The cube edge-isoperimetric inequality applied to D_i gives

    I(1-2 1_{D_i})
      >= 2 theta log2(1/theta).

Combining with (5.2)-(5.3),

    Delta_i H(f_A)
      <= (1+3/ln 2) Inf_i(f_A)
         + (1/2) I(1-2 1_{D_i}),                    (5.5)

with

    1+3/ln 2 = 5.328085122666891....

Equations (5.4)-(5.5) are the positive replacement for false local B_C monotonicity.

At any target C>=6.3280852, every equal-density split with q>=1/4 is locally safe.  When q<1/4, the only unpaid term after a constant influence charge is one half of the PHYSICAL boundary of the pivotal set.

For the bent-swap family D_i consists of two nonadjacent points, so

    I(1-2 1_{D_i}) = m 2^{2-m},

and

    [I(1-2 1_{D_i})/2]/Inf_i(f_A)=m.

Thus the boundary term has exactly the logarithmic order required by (4.2); it is not an artefact of the estimate.

## 6. Better proof route and the remaining universal obstruction

A scalar density potential is now ruled out as a complete local mechanism: equal-density fibres annihilate its curvature while rare phase swaps can generate logarithmic entropy debt.

The replacement route is a **second-order pivotal-boundary ledger**.

At a rare equal-density split, use (5.5) and carry forward the debt

    (1/2) I(pivotal_i).

This is a genuine original-coordinate geometric quantity: it counts residual physical edges across which i-pivotality changes, equivalently nontrivial (i,j)-face variation.  It preserves the cancellation/phase information that an absolute-value-only scalar potential loses.

A complete proof would need a dimension-independent packing/telescoping theorem showing that, under an adaptive restriction or block decomposition, these pivotal-boundary debts can be charged to total influence only O(1) times.  The obvious static sum over all i is NOT asserted to have such a bound; one-point / rare-defect examples warn that second-order row sums can be large.  The order or stopping rule has to matter.

The exact general recurrence (3.1) says what the unequal-density extension must additionally retain:

    phi(delta)-w phi(a)-(1-w)phi(b).

No sign of this scalar-curvature term may be discarded without proof.

A concrete next B17 target is therefore:

> Derive or refute a block restriction lemma that groups a rare equal-density selector with enough residual pivotal-boundary coordinates so that the total block debt is nonnegative at some fixed C>6.521851, and prove that disjoint/adaptive blocks charge each physical influence at most O(1) times.

This is different from the refuted every-coordinate lemma and from merely searching for a good coordinate.  It also gives B18 a precise recursion object and fleet03/B17 a precise higher-order face boundary to compare against.

## 7. Exact checker

`verify_bellman_bent_swap.py` uses integer Walsh transforms and `fractions.Fraction`; no floating-point number decides any PASS.

It verifies for m=6,8,10,12:

- the minority bent-set density;
- exact selector q from (4.1);
- 2^{m-1} affected frequencies;
- the exact r_max formula and 1/r_max>2^{m-3};
- constant nu(S)r(S) over affected frequencies;
- exact child and parent influence formulas.

At m=10 it verifies

    density = 31/64,
    q = 1/992,
    r in {1/226,1/290},

and the exact strict C=7 obstruction using only 226>128.

Checker SHA-256:
cff931a50ce451f797443d5f1ba8f32aa342b507becca045c6a44052941d7d7d

Output SHA-256:
a0c48d58d2e3728172823c39d3b1e78453d4c53a35dae376238d5961f02dc59d

Finite checks support only these exact instances; the general statements above are analytic.

## 8. Literature / provenance applicability

Primary literature checked this run:

- O'Donnell–Tan (2013), composition theorem: relevant to the preceding balanced-amplification equivalence, but not a proof of the new pivotal-boundary packing obligation.
- Hod (2017), lexicographic recursive lower bounds: relevant lower-bound/composition provenance; the current unrestricted lower frontier is already above Hod's historical value through the sprint's recovered 2026 seed/graft.
- González–MacManus–Pereyra (2026), “Further evidence towards the Fourier Entropy-Influence conjecture”: explicitly uses restriction inequalities and stopping binary trees, and explicitly shows wrong prescribed splitting variables can fail every fixed local K.  Therefore this report does NOT claim novelty for the bad-coordinate phenomenon or stopping-tree idea.
- Potapov (18 Sep 2026), plateaued/partially bent classes: proves sharp class constants 4 and 2 respectively.  Our bent child is consistent with this easy structured regime; the two-point-swapped child is outside the exact plateaued class.

Internal dependency used with hypotheses preserved:

- `continuations/2026-09-20-concave-restriction/REPORT.md`: exact fibre identity, strict concavity of Psi and Jensen cap.  This report only re-expresses that cap inside the support-deficit Bellman recurrence and combines it with physical pivotal-set isoperimetry.
- `fleet-2026-09-21/fleet02/B17/20260921T124438Z-support-deficit-balanced-equivalence/REPORT.md`: exact kappa_C and support-deficit equivalence.
- Historical bent/rare-flip local-payment failure is preserved as prior art rather than re-announced.

No publication-priority claim is made for identities that are immediate combinations of these ingredients.

## 9. Before / after

Before:
- zero-slack support deficit had been refuted;
- scalar-corrected B_C was proposed but its one-coordinate recurrence was not written down;
- the next target was “derive or refute local Bellman recursion.”

After:
- exact general recurrence (3.1) is proved;
- every-coordinate B_C monotonicity is refuted for every finite C by an exact Boolean family;
- the obstruction persists even when both restrictions have H/I<=2 and the parent has H/I->2;
- equal-density local debt is reduced universally to a 6.3281 dense case or a 5.3281 influence charge plus half the pivotal-set boundary;
- the remaining universal obstruction is a concrete second-order boundary packing/telescoping problem, not an unspecified scalar-potential gap.

Full FEI remains OPEN / NOT PROVED.
