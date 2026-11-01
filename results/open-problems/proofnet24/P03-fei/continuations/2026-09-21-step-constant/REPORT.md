# The restriction-step constant: a lower bound, a ceiling, and where the extremal functions are not

21 September 2026. Full FEI remains open. This note concerns the constant of the restriction induction --
the "key inequality" of Gonzalez, MacManus and Pereyra (arXiv:2606.00246) -- and records two elementary facts
about it together with the measured landscape. Everything below is computed by an exact O(n) recursion on
read-once formulas, cross-checked against brute-force Walsh transforms; the code and logs are beside this file.

## The object

For a Boolean f on n variables and a relevant coordinate i, write f_0, f_1 for the restrictions and

    Delta_i H = H(f) - (H(f_0) + H(f_1))/2,      rho_0(f) = min over relevant i of  Delta_i H / Inf_i.

Since I(f) = (I(f_0) + I(f_1))/2 + Inf_i, a bound rho_0(f) <= K for every f gives FEI with constant K by
induction on n. Whether sup_f rho_0(f) is finite is open; Gonzalez, MacManus and Pereyra prove K = 38 for
delta-tribes functions and state that they could not settle it for Boolean or monotone functions.

## 1. The constant is bounded below by the conjecture's own constant

Let C be a class closed under restriction (all Boolean functions, monotone functions, read-once formulas).
If rho_0(f) <= K for every f in C, then H(f) <= K I(f) for every f in C: induct on the number of variables,
taking i to be a coordinate attaining the minimum, and use the two identities above. Hence

    sup over C of rho_0  >=  C_FEI(C).

With Hod's lower bound (arXiv:1711.00762), which is realised by read-once formulas and holds for monotone
functions, this gives sup rho_0 >= 6.4547837 for all Boolean functions, for monotone functions, and for
read-once formulas separately. The argument is immediate and is recorded here for its quantitative
consequence, not as a claim of priority: it says the step route cannot deliver a constant smaller than the
conjecture's own, and it tells us the witnesses exist inside the read-once class, where the FEI constant is
now known numerically to be beta(1/2) = 6.4547837 and is proved to be at most 6.4573.

## 2. A ceiling, and the influence it forces

The restriction identity gives Delta_i H = JS(p_0, p_1) + sum_S m(S) h(p(S u i)/m(S)) with m = (p_0+p_1)/2,
so Delta_i H <= 1 + h(Inf_i). The map x -> (1 + h(x))/x is decreasing on (0, 1/2], so with
delta = max_i Inf_i,

    rho_0(f)  <=  (1 + h(delta)) / delta.

The bound is attained: AND of two variables has delta = 1/2 and rho_0 = 4 exactly. Solving
(1 + h(delta))/delta = 6.4547837 gives

    delta* = 0.289387.

So every function with a coordinate of influence above 0.2894 has rho_0 < beta(1/2) and cannot be a witness
for section 1. In particular no function of at most three relevant variables can be one, and a witness family
must have vanishing maximum influence, hence unboundedly many variables. Checked on 660 random read-once
trees (n = 2..12) and on 240 of them again by brute force: no violation, and the negative control
(a value one above the ceiling) is flagged.

## 3. What the search actually reaches

Exhaustive over all read-once AND/OR trees (leaves are interchangeable for H and I, and negating a variable
changes neither, so positive leaves with AND/OR gates cover the class up to relabelling):

    n      2      3      4      5      6      7      8      9     10     11
    rho_0  4.000  4.868  4.742  4.852  4.891  5.087  5.687  5.552  5.784  5.773

Balanced alternating AND/OR trees, one representative leaf per orbit, to n = 1024:

    depth  3      4      5      6      7      8      9      10
    n      8      16     32     64     128    256    512    1024
    rho_0  5.687  5.586  6.055  6.045  6.079  6.079  6.054  6.054

A beam search growing trees leaf by leaf reaches 5.91 at n = 18 and is beaten by the balanced family at
n = 32, so leaf-by-leaf growth finds a local region rather than the witness.

The published landscape agrees in magnitude: over all functions of at most five variables the supremum of
rho_0 is 4.8677, hill climbing reaches 5.1949 at n = 6, and width-two tribes peak at 6.0037 at n = 16 and
then decline.

## 4. The gap this leaves

Section 1 says the read-once class contains functions with rho_0 >= 6.4548. Nothing measured anywhere --
exhaustive to n = 11, balanced towers to n = 1024, tribes, hill climbing, beam search -- exceeds 6.08. The
step-extremal functions are therefore deeper than any family so far examined, and section 2 says where to
look: maximum influence below 0.2894, which the plateau families do satisfy, so the constraint is necessary
and not sufficient.

Two concrete targets follow.

(a) Walk the restriction tree of Hod's tower. Its members have H/I -> beta(1/2); for any f, the maximum of
rho_0 over f's own restriction tree is at least H(f)/I(f), so a tower member with H/I = 6.4 carries a witness
with rho_0 >= 6.4 somewhere beneath it. Descend by always taking the minimising coordinate and record the
maximum rho_0 met. This is a search over a path, not over a class, and it terminates.

(b) Decide whether sup rho_0 over read-once equals C_RO or exceeds it. Equality would say the step route is
exactly as hard as FEI on that class and no harder; a strict excess would say the route needs a constant
larger than the conjecture's, which is worth knowing before more work is spent on it.

## Files

`code/ro.py` (the exact recursion), `code/control.py` (brute-force Walsh cross-check, 360 trees, agreement
to 8e-14 on H and 4e-12 on rho_0), `code/negcontrol.py` (fault injection: with the h(V) correction removed
the cross-check trips on 210 of 210 trees), `code/fast.py` (canonical-form memoisation),
`code/bigfam.py`, `code/beam.py`, `code/lemma.py`; `data/` holds the logs behind every table above.

## 5. Where the c = 0.003 certificate run fails, and what the candidate can still support

The region-2 verification at c = 0.003 on the M = 96 candidate stops at a degenerate cell, x = 4.000000,
v = 1.584632, with bound -9.949e-04. A zero-width cell is enclosed exactly up to rounding, so that is the
candidate's own violation of (A) and not slack in the enclosure. The coordinates are p = 2^-4 = 1/16 and
q = 2/3, and 2/3 is q_1 of Hod's ladder q_0 = 1/2, q_{j+1} = 1/(1+q_j) -> 1/phi.

An independent evaluation of Phi (`code/ladder.py`, written from the formulas of section 2 of the
certificate report rather than from its code) gives Phi(1/16, 2/3) = -3.2957e-04, that is
Phi/v = -9.887e-04, agreeing with the run's bound to three digits.

The violation is a single point, not a region. Along q = 2/3, of 4401 sampled p exactly one is negative and
it is p = 2^-4. Three hundred thousand random (p, q) find none. The lines q = 2^-k for k = 1..8 at 8000
values of p each, the arc pq = 1/2, the strip p -> 1/2 with q -> 1, and the whole square [0.30, 0.70]^2 find
none at c >= 0.0041.

Slack in (A) rises by c(1-p)(1-q), so the failing point fixes a floor for the margin rather than ruling the
candidate out. Bisecting over 335,856 sampled points including every dyadic node and the whole ladder:

    smallest pointwise-feasible margin      c = 0.004055        constant C0 + c/4 = 6.455814
    above c = 0.005 the binding point leaves that dyadic node; the floor becomes a uniform +1.9e-04
    currently proved                        c = 0.01            constant 6.4573

So the existing M = 96 candidate should support a constant near 6.4558 without any refinement, and c = 0.005
is the margin to attempt, since at 0.0042 there is only 4.5e-05 of room. This is pointwise evaluation, not an
interval certificate: the verification machinery still has to close it, and the p -> 1/2, q -> 1 strip sits at
+1.5e-10, which is structural tightness and remains a job for the lemmas rather than the grid.

`code/ladder.py`, `code/cmax.py`, `code/corner.py`; logs in `data/`.

## 6. Descending a restriction tree finds a better witness: rho_0 = 6.3164

Section 4(a) proposed descending the restriction tree of a read-once formula rather than searching the class.
Run: maximise H/I by beam search (reached 5.2526 at n = 108), then descend, at each step restricting a
coordinate that attains the minimum and continuing into the child of larger ratio. `code/descend.py`, trace in
`data/descend_log.txt`.

    depth   0    n=108   H/I=5.2526   rho_0=6.2451   maxInf=0.0191
    depth   7    n= 95   H/I=5.2021   rho_0=6.2860   maxInf=0.0306
    depth  13    n= 82   H/I=5.1208   rho_0=6.3106   maxInf=0.0492
    depth  19    n= 71   H/I=5.0086   rho_0=6.3164   maxInf=0.0744
    depth  25    n= 58   H/I=4.8056   rho_0=6.3040   maxInf=0.0920

    depth  51    n=  8   H/I=2.9396   rho_0=3.0189   maxInf=0.6016
    depth  56    n=  1   H/I=0.0000   rho_0=0.0000   maxInf=1.0000

The best value met is rho_0 = 6.316364 at n = 71, against 6.08 for the balanced family, 6.0037 for width-two
tribes, 5.91 for the beam search and 5.77 for exhaustive search to n = 11. The descent passes through the
6.2 to 6.32 band for its first twenty-five steps and only falls away when the restrictions have removed enough
variables that the maximum influence climbs: by depth 51 the maximum influence is 0.60 and the ceiling of
section 2 is 3.9, which is what the measured 3.02 is pressed against. The two halves of this note therefore
agree on the same mechanism.

The descent is a path, not a search over a class, so it is cheap: 57 evaluations reach a value the beam search
did not find in thousands. It also starts from a formula whose own ratio is only 5.25, so the witness is not
the extremal function for H/I; the step constant and the ratio are maximised by different formulas, which is
the same separation the published record reports for the general case (hill climbing reaches rho_0 = 5.19 at
a function whose H/I is 3.31).

Provenance: these numbers come from the recursion of `code/ro.py`, checked against brute-force Walsh transforms
on 360 random trees at n <= 10 (agreement 8e-14 on H, 4e-12 on rho_0) and against the ceiling of section 2 at
every step. They are not independently re-derived at n = 71, where a truth table is out of reach. The run is
deterministic; `python descend.py 140` reproduces it and writes the witness formula to `witness.pkl`.

The gap to beta(1/2) = 6.4547837 is now 0.138. A deeper or better-seeded descent is the obvious next step, and
the seed does not need a high ratio to work.

## 7. The step constant against the erasure entropy, and what that measures

The record's erasure reduction (`solo-2026-09-17/ERASURE_REDUCTION.md`) proves the exact identity
Delta_i = B_i + JS(q_+, q_-) with B_i = H(S_i | S_{-i}), and JS <= (2/ln 2) min(Inf_i, 1 - Inf_i). Since the
minimum of ratios is at most the ratio of the sums,

    rho_0(f) = min_i Delta_i/Inf_i  <=  (sum_i Delta_i) / I(f)  <=  B(f)/I(f) + 2/ln 2,

with B(f) = sum_i H(S_i | S_{-i}), the erasure entropy of the spectral sample. So a universal bound
B <= K I gives FEI with K + 2/ln 2 = K + 2.8854, which is the reduction's own statement reached from the step
side. Erasure entropy is at most entropy, so this target is weaker than FEI; it is also not strictly easier,
since any finite K settles the conjecture.

Measured (`code/erasure.py`, `code/erasure2.py`; spectra by Walsh transform, B computed two ways --
sum_i H(S_i|S_{-i}) and n H - sum_i H(S_{-i}) -- which agree):

    all non-constant functions, n <= 4, exhaustive      max B/I = 2.7042
    random functions, n = 5..14                         B/I = 1.73 down to 1.13, falling with n
    one-point functions                                 B/I -> 2.0000 exactly (H/I -> 4)
    tribes, AND of s ORs of width 2                     B/I peaks at 3.607 (s = 8, n = 16), then declines
    tribes of width 3, 4, 5                             2.26 to 2.87
    majority, and every odd function                    B = 0 exactly

So the largest erasure ratio found anywhere is 3.607, which through the reduction would give 6.4925 -- within
0.04 of beta(1/2). That is a coincidence worth noting and nothing more: the reduction loses the JS term, so it
cannot deliver the sharp constant, and 3.607 is a measured maximum over the families tried, not a supremum.

Why majority has B = 0. Its spectrum is supported on the odd-size sets, so |S_{-i}| determines the parity of
|S| and hence S_i: every conditional entropy vanishes. The same holds for any function whose Fourier support
lies in one parity class, which includes every odd function f(x complement) = -f(x). Checked: 243 odd functions
at n = 3..14 give B = 0 to machine zero, while 224 of 224 general functions give B > 0 (up to 6.29), so this is
a property of the class and not of the estimator.

This does NOT prove FEI for odd functions, and the earlier form of this note said so wrongly. B(f) = 0 bounds
the single restriction step at that f, giving rho_0(f) <= 2.8854. The induction needs the bound at every
function in the restriction tree, and a restriction of an odd function is not odd: fixing one coordinate
destroys the antisymmetry. Odd functions are not closed under restriction, so a class bound on B gives nothing
by itself. What the measurement does say, separately, is that 243 odd functions all have H/I <= 1.714.

### A note on reproducing section 6

The descent was run twice. The first run reported rho_0 = 6.316364 from a seed with H/I = 5.252592; the second,
with the witness formula saved to `data/witness.pkl`, reported 6.314771 from a seed with H/I = 5.261214. The
difference is the seed, not the method: the ratio beam ranks candidates keyed by canonical form and ties break
with dictionary order, so the two runs keep slightly different frontiers. Both land at 6.315 to three figures.
Quote 6.3148, the value whose witness is on disk.

## 8. The read-once spectrum factorises by gate pattern

For f = AND(a, b) on disjoint variable sets, write S = S_A u S_B and let the pattern be the pair of bits
(S_A empty?, S_B empty?). Then

    mu_f(S) = mass(pattern) * mu_a(S_A | pattern_A) * mu_b(S_B | pattern_B),

where the four masses are the AND gate's own weights w_empty, It_a - w_ab, It_b - w_ab, w_ab of section 2, and
mu_a(. | empty) is the point mass at the empty set. Checked on 132 random read-once trees at n = 2..12:
worst |predicted - true| = 5.6e-17 (`code/factorise.py`). OR follows by duality.

So the spectral sample of a read-once formula is generated top-down: at each gate draw a pattern from four
weights depending only on the two biases, then recurse independently into the children that the pattern marks
non-empty. The whole distribution is determined by the tree and the biases along it.

This is what makes B computable without a 2^n spectrum, which is the current ceiling on every measurement in
section 7. For i in A, condition on S_{-i} = (S_{A\i}, S_B):

- if S_{A\i} is non-empty, pattern_A is already determined, and the conditional law of S_i is exactly its
  conditional law inside a given that S_A is non-empty -- a recursive quantity;
- if S_{A\i} is empty, then S_i = 1 forces pattern_A non-empty and S_i = 0 forces it empty, so the conditional
  odds are the gate masses weighted by mu_a({i} | non-empty) against mu_a(empty-pattern).

A recursion carrying, for each subtree, its bias, the mass it puts on the empty set, the masses on singletons,
and the conditional entropies of its own variables under both patterns therefore computes B in O(n) per tree.
That would take the B/I search from n = 20 to n in the hundreds and decide whether the read-once supremum of
B/I is near 3.7, as the shrinking increments of section 7 suggest, or climbs toward the 6.4548 ceiling. It is
the obvious next piece of work and it is not done here.

### Where the erasure ratio is heading

The extremal trees of section 7 are ANDs of a repeated block, so the families themselves can be pushed to the
largest n an exact 2^n spectrum allows (`code/blocks.py`, log `data/blocks.txt`):

    AND of k copies of ((x|x)&x)|(x&x)      k=1..4, n=5..20     1.831  3.246  3.626  3.641
    AND of k copies of ((x|x)&x)|x          k=1..5, n=4..20     2.163  2.161  3.140  3.556  3.698
    tribes, AND of k ORs of width 2         k=2..11, n=4..22    1.782 .. 3.607 (peak at n=16) .. 3.536
    tribes of width 3                       k=2..7, n=6..21     2.622 .. 2.261 .. 2.867

Every family rises, reaches a maximum and turns over; tribes peak at n = 16 and decline from there, the
five-variable motif flattens near 3.64, and the four-variable motif reaches 3.698 at n = 20 without having
turned yet. The beam search of section 7 agrees: 3.645 at n = 16 with the increments shrinking.

So the read-once evidence puts

    sup B/I  at roughly 3.7,

against the ceiling of 6.4548 that B <= H forces if the conjecture holds. Through the reduction that would
give FEI with a constant near 6.6. The honest caveat is that each richer block raises the peak a little
(3.607, then 3.645, then 3.698), so 3.698 is a measured lower bound and the supremum could creep further; what
the data rules out is the ratio running away toward the ceiling.
