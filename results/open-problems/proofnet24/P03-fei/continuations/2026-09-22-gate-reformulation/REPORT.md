# The Fourier entropy-influence conjecture: a gate reformulation, and what it measures

22 September 2026. FEI is not closed. Three things here are new: a reformulation of the conjecture as one
inequality over Boolean gates of every arity; a measurement of that inequality up to arity four, in the units
that decide the constant; and an explicit family that kills the per-coordinate erasure bound. Everything is
computed by code written this session beside the existing certificate machinery, cross-checked against it and
against the published values. All gate numbers are floating point on a grid, not interval arithmetic: they are
measurements, not certificates. The proved read-once theorem is still H <= 6.4573 I.

Notation follows the earlier working note: H spectral entropy, I total influence, V_p = 4p(1-p), h binary
entropy, Gamma the read-once potential (the value-iteration fixed point at C0 = Gamma(1/2) = 6.4548, candidate
`cert_vi_h96k40_f4`), beta(1/2) = 6.4547837 Hod's lower bound.

## 0. Independent reproduction of the record

A second implementation of the spectral quantities (`bexp.py`: Walsh transform, H, I, the erasure entropy
B = sum_i H(S_i | S_{-i}), the restriction drops Delta_i, the step constant rho_0 = min_i Delta_i/Inf_i) was
written from the definitions and swept exhaustively over all 65,534 non-constant Boolean functions of at most
four variables:

    max H/I          = 3.402476
    max B/I          = 2.704153          record: 2.7042
    max rho_0        = 4.867669          record: 4.8677 (over n <= 5)
    max_i B_i/Inf_i  = 3.523112

The two record numbers agree to every digit they were quoted with.

## 1. The reformulation: FEI is one inequality over gates

For a gate G on k inputs fed by Boolean functions of measures p_1..p_k on disjoint variable sets, the
composition lemma (O'Donnell-Tan Prop. 3.2, Hod Lemma 3.1) makes H and I of the composite affine in the
children's normalised H and I. So the induction hypothesis H(f) <= C I(f) - Gamma(Pr f), Gamma >= 0 symmetric,
closes for formulas over G exactly when

    (G)   Gamma(p_out) + Ht_G(p)  <=  sum_i It_i(G;p) (Gamma(p_i) + h(V_{p_i})) / V_{p_i}    for all p in (0,1)^k,

It_i the biased influence of input i in G, Ht_G its biased spectral entropy.

**Proposition.** FEI holds with constant C if and only if some symmetric Gamma >= 0 with Gamma(1/2) <= C
satisfies (G) for every Boolean gate of every arity.

*Proof.* Given such a Gamma, induct over read-once formulas built from arbitrary gates. Every Boolean f on n
variables is such a formula - one gate, n fresh variables - so H(f) <= C I(f) - Gamma(Pr f) <= C I(f).
Conversely, if FEI holds with constant C, set Gamma_C(p) = inf { C I(f) - H(f) : f Boolean, Pr[f] = p }; it is
non-negative because C >= C_FEI, symmetric because negation preserves H and I, and satisfies (G) for every gate
because the composite G(a_1,...,a_k) is itself an f of measure p_out. QED

Arity two is the read-once AND/OR inequality whose sharp constant is numerically beta(1/2) and which is proved
at 6.4573; arity k is FEI for read-once formulas over gates of fan-in at most k; the conjecture is the limit.
The potential the general conjecture needs is *smaller* than the read-once one (the infimum runs over a larger
class), so the question is not whether the read-once Gamma must survive larger gates but whether it does - if
it does, FEI holds with beta(1/2) and Hod's tower is globally extremal.

Two corollaries of the framing. Expanding a gate on its last input (Shannon expansion = restriction) turns (G)
into a two-function inequality

    (*)  JS_t(mu_0,mu_1) + H(S_k | S_{-k}) <= d (Gamma(t)+h(V_t)) + (1-t)Gamma(p_0) + t Gamma(p_1)
                                              - Gamma((1-t)p_0 + t p_1),   d = Pr[G_0 != G_1],  It_k = V_t d,

which is the erasure term of the record's reduction in the potential's own language. And the only genuine
two-input gate besides AND/OR is XOR, whose constraint has a closed form: It_1 = V_p, It_2 = V_q,
Ht = h(V_p) + h(V_q), p_out = p + q - 2pq, so (G) collapses to

    Gamma(p) + Gamma(q) >= Gamma(p + q - 2pq),

subadditivity under XOR-convolution of measures. In the variable s = log(1/|1-2p|) that is plain subadditivity,
so any Gamma concave in s satisfies it for free; measured, XOR has a margin of about -22, i.e. enormous slack.

## 2. What a gate asks of the potential, and how it grows with fan-in

Replacing Gamma by Gamma + c z(1-z) changes D_G = (right side of (G)) - (left side) by
c [ I(G;p)/4 - p_out(1-p_out) ], because p(1-p)/V_p = 1/4 for every input. That bracket is non-negative by
Poincare (Var = 4 p_out(1-p_out) <= I), so the margin helps every gate, and the margin a gate asks for is

    c_G(p) = -D_G(p) / ( I(G;p)/4 - p_out(1-p_out) ).

For AND the denominator is exactly p q (1-p)(1-q) and c_AND is the certificate's own -Phi/((1-p)(1-q)): arity
two IS the margin the read-once certificate pays, the certified constant is Gamma(1/2) + c/4, and comparing
max c_G across arities is exactly the question "does a larger fan-in force a larger constant?"

D_G depends on the gate only through its spectrum, and the three NPN moves act on the data: permuting inputs
permutes the bias vector, negating input i maps p_i to 1-p_i, negating the output maps p_out to 1-p_out. Gamma,
h(V) and V are symmetric about 1/2, so with a bias grid symmetric under p -> 1-p and closed under permutation
one representative per NPN class suffices: 4 classes at arity 2, 14 at arity 3, 222 at arity 4 instead of
65,536. Gates are split DEGENERATE (independent of some input, so really a smaller gate), READONCE (a formula
over two-input AND/OR, so implied by arity two), GENUINE (neither - the only ones that can ask for more; note
this class contains read-once formulas that use XOR, since the READONCE class is over AND/OR only).

Pairs where the gate is nearly constant at the given biases, so that D_G and the denominator both vanish, are
skipped.

**On one common grid (67 values per coordinate, all sorted k-tuples):**

    arity 2      2,278 bias vectors       READONCE (AND) c = +3.751756e-04      GENUINE (XOR) c = -2.2e+01
    arity 3     52,394 bias vectors       READONCE       c = +3.750386e-04      GENUINE       c = +3.738665e-04
                                          DEGENERATE     c = +3.751756e-04
    arity 4    916,895 bias vectors       READONCE       c = +3.751756e-04      GENUINE       c = +3.750386e-04
                                          DEGENERATE     c = +3.751756e-04

**On a finer common grid (199 values per coordinate):**

    arity 2     87,990 bias vectors       READONCE (AND) c = +1.674228e-03
    arity 3  1,333,300 bias vectors       READONCE       c = +2.404474e-03      GENUINE       c = +1.673657e-03
                                          DEGENERATE     c = +1.674228e-03

At every arity and both resolutions the genuinely k-input gates ask for *less* margin than the two-input AND
does; the only class that asks for more is READONCE, whose gates are compositions of AND constraints and whose
demand is therefore already implied by arity two. The binding constraint is the AND gate, at every fan-in
tested.

**Where the genuine worst case actually sits.** A grid minimum that beats the AND by 0.4 percent is not much to
rest on, so each class's worst point was refined by coordinate descent in log2(1/p) and the influence each
input still carries was read off (`refine_gate.py`). The answer is sharper than the grid suggested:

    arity 3, worst GENUINE gate (tt = 6)   refines to c = 1.9966441e-03 at p = (0, 0.55554199, 0.984375)
                                           one input carries influence 6e-302, i.e. none
    arity 2, the AND, at its worst          refines to c = 1.9966441e-03 at p = (0.44445801, 0.984375)
                                           influences 1.5432e-02 and 3.4179e-02 - identical to the arity-3 row
    arity 4, worst GENUINE gate (tt = 385) refines to c = 8.7831e-04; two of its four inputs carry no influence

So the worst genuine three-input configuration is not a three-input configuration at all: it is the AND
constraint reached through an input whose bias has gone to zero, and it agrees with the arity-2 row in the
margin, the influences and the output measure to every digit printed. The arity-4 worst is the same story with
two dead inputs and a smaller value. Nothing that genuinely uses three or four inputs is binding.

The refined figure is confirmed independently: evaluating the certificate's own -Phi/((1-p)(1-q)) at the AND
measures of that point (1 - 0.44445801, 1 - 0.984375) gives 1.99664333e-03 against the gate sweep's
1.99664410e-03 - two code paths written separately, agreeing to seven digits.

**Named gates of larger fan-in** (`bigates.py`; symmetric bias on a 2,500-point grid, plus 2,000 random bias
vectors per gate; the margin the gate asks for, negative meaning slack):

    AND2                +8.60e-04      the only positive entry
    AND4, AND6, AND8    -0.0e+00, -3.5e-15, -2.4e-15   exactly tight at symmetric bias, asking nothing
    MAJ3,5,7,9          -4.16, -5.37, -6.15, -6.66
    PAR3,4,5,6          -22.2, -22.4, -22.6, -22.8
    TRIBES w2 s2..s4    -6.7e-04, -2.6e-03, -2.6e-02
    TRIBES w3 s2        -1.25e-01
    BENT4, BENT6        -4.91, -7.74
    BENT+flip (3,5,7)   -13.2, -12.8, -12.2

AND_k is exactly tight because the fixed point equals the AND-chain slack at every dyadic measure. Nothing else
comes near the constraint.

## 3. The sharpened functional

At uniform biases (G) reads C0 I(f) - H(f) - Gamma(Pr f) >= 0, that is

    R(f) = ( H(f) + Gamma(Pr f) ) / I(f)  <=  C0 = Gamma(1/2).

R >= H/I always, so R is a strictly sharper falsification target than the ratio; and R = C0 exactly at a single
variable and at every AND chain. So C0 is attained and the conjecture in this form is that it is the maximum.

    exhaustive, all Boolean f on n <= 4                              max R = 6.454800000 = C0 exactly (AND_4)
    hill climbing on truth-table flips, n = 6, 8, 10, many restarts  nothing above C0

## 4. A dead route, killed by an explicit family

The record's erasure reduction gives Delta_i = B_i + JS with JS <= (2/ln 2) Inf_i, hence

    rho_0(f) <= B(f)/I(f) + 2/ln 2,   and since B <= H,   C_FEI - 2/ln 2 <= sup B/I <= C_FEI.

A per-coordinate bound B_i <= K Inf_i would give FEI with K + 2.8854. It is false. Take a bent function on m
variables (m even; the inner-product function), adjoin a variable, and flip one point at which the new variable
is true. The new coordinate has Inf_i = 2^-m while its conditional entropy is spread over all 2^m sets at the
minimal Fourier granularity, so the ratio grows linearly:

    m            2       4       6       8       10      12
    B_i/Inf_i   2.6725  5.2244  7.3868  9.4286  11.4392 13.4418        (about m + 1.44)

So sup_i B_i/Inf_i is infinite. The sum is untouched - that family has B/I -> 2 and rho_0 -> 4 - which is the
point: the erasure route needs the sum, and the sum carries all of the difficulty.

## 5. How large is sup B/I

    n <= 4 exhaustive            2.704153
    n = 6 hill climbing          3.030964
    n = 8 hill climbing          3.013514
    read-once families (record)  3.698 at n = 20, still rising slowly

A free hill climb over all functions does not beat the structured read-once families, so the erasure-extremal
functions are structured rather than generic. With the sandwich, a supremum near 3.7 would put C_FEI below 6.59.

## 6. A correction to the certificate margin

`scan_cmin.py` samples random points, the lines q = 2^-k and the near-1/2 strips. On `cert_vi_h96k40` it reports
2.183e-03, while the point (p,q) = (2^-4, 2/3) - the one the c = 0.003 certificate run actually failed on -
needs 4.054639e-03. The earlier session's floor of 0.004055 for that candidate is right and the quick scan is
what was wrong: q = 2/3 lies on no line q = 2^-k and the dip is narrow. Two consequences. The margin instrument
has to sweep the shapes that dip - every grid node against a dense q, the Hod ladder q_{j+1} = 1/(1+q_j)
against a dense p, a node lattice, random pairs - and then refine locally from the worst of each; `cmin4.py`
does that. And any margin quoted from a plain grid is a lottery: the nx = 90 grid finds a worse point for the
AND constraint (1.674e-03) than the finer nx = 200 grid does (1.272e-03), because the two grids are not nested.

The margin instrument settles it, and it corrects a figure that a local refinement alone would have got wrong.
Refining the arity-2 gate sweep's worst grid point converges to p = (0.55554199, 0.015625) needing
c = 1.99664e-03 - found twice, by the gate sweep and by the certificate's own formula, agreeing to seven
digits - but that is a local optimum, not the maximum. The multi-start sweep of `cmin4.py` (grid nodes against
a dense q, the Hod ladder against a dense p, a node lattice, 9M random pairs, then local refinement from 200
distinct starts) finds a worse point:

    cert_vi_h96k40_f4:   c_min >= 4.3974201e-03   at p = 0.996519926882, q = 0.5
                         -> the best constant this candidate can give is 6.4558994

The binding point is on the fresh-variable line q = 1/2 with p -> 1, which the earlier working note already
flagged as part of the tight set. Note the finer candidate is not the better one here: `cert_vi_h96k40` needs
4.054639e-03 at (2^-4, 2/3), slightly less than f4's 4.397e-03, so refining the grid near p = 1/2 moved the
binding point rather than removing it.

What this does **not** establish: a smaller certified constant. The six-part interval certificate has not been
re-run at a smaller c in this session, so the proved read-once bound remains H <= 6.4573 I. Even 4.397e-03 is
a floating-point floor from a search, not an interval enclosure.

## 7. What would close it

The gate inequality makes the target concrete. Either (a) prove D_G >= 0 for every gate directly - the measured
picture says the AND gate is the extremal one at every arity, so a proof that the minimum of c_G over arity-k
gates is attained at a decomposable gate would finish the conjecture; or (b) find a gate that asks for more.
The search here covered all 222 NPN classes of arity 4 over a million bias vectors and a list of named gates to
fan-in 22, and found nothing. The natural next step is arity 5 (616,126 NPN classes) and an interval-arithmetic
version of the arity-3 and arity-4 sweeps, which would turn "FEI for read-once formulas over gates of fan-in at
most four" from a measurement into a theorem.

## Files

`gam.py` (the certificate potential), `npn.py` (NPN classes), `decomp.py` (gate classification), `gates4/5/6.py`
(the sweeps), `bigates.py` (named gates of larger fan-in), `bexp.py` (spectral quantities from scratch, with the
bent-plus-flip family), `bclimb.py`, `dclimb.py` (hill climbs on B/I and on R), `exhfast2.py` (exhaustive
sweeps), `cmin3.py`, `cmin4.py` (the margin instrument), `vi_par.py` (a parallel value iteration). Logs in
`logs/`. The candidate potential and the earlier certificate code are in
`06_math_research/fei_step_numerics_2026_09_20`.
