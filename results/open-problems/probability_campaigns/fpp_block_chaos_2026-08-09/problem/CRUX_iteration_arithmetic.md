# The quantitative crux: what the lattice must pay for the engine to iterate
Written by the author, 2026-08-09 18:2x. Elementary; verifiable line by line. Uses only the MG2-B lemma statement (itself awaiting referee verdict - this note's arithmetic does not depend on the disputed parts, only on the lemma's stated form, which matches the paper's Theorem 2.13 shape).

## 1. What iteration buys
Suppose the conditional halving Var(X_{Mn}) <= (1/2) M Var(X_n) holds at every scale n = M^j n_0, j = 0..k-1, for a fixed M. Then
  Var(X_{M^k n_0}) <= (M/2)^k Var(X_{n_0}).
With N = M^k n_0 (so k = log(N/n_0)/log M):
  (M/2)^k = (N/n_0)^{1 - log 2 / log M},
hence Var(X_N) <= Var(X_{n_0}) (N/n_0)^{1 - log 2 / log M}: a polynomial variance bound n^{1-eps} with eps = log 2 / log M - o(1).

## 2. The crux, quantified
The halving at scale n needs (MG2-B (9.2), same shape as the paper's final step):
  eps_n <= D_n^2 / (16 C2 V4_n),  where D_n := Var(X_n), V4_n ~ Q_n^4.
Define the concentration-to-variance mismatch rho_n := Q_n^2 / D_n. Then the required chaos strength is
  eps_n <= 1 / (16 C2 rho_n^2).
In the paper, Theorem 2.1 gives rho_n = Theta(1) (their Q_n IS the standard deviation), so a constant-order chaos estimate suffices - and that is what their Sections 4-9 deliver.

On Z^2 today, unconditionally:
- D_n >= c log n (Newman-Piza 1995) is the best known variance LOWER bound;
- the only unconditional concentration envelopes have Q_n = Theta(sqrt(n)) (Kesten/Talagrand; BKS improves the VARIANCE upper bound to n/log n but the exponential-concentration envelope stays at sqrt(n/log n) scale at best).
So rho_n can be as large as ~ (n/log n) / (c log n) = C n / log^2 n under current knowledge, and the required chaos bound becomes
  eps_n <~ log^4 n / n^2.
No construction of the BSS type produces eps decaying in n at all - theirs is a small CONSTANT. The gap is a factor of order n^2 (up to logs). Conclusion, stated plainly: with today's unconditional lattice inputs, the engine cannot iterate even once at large n. The program lives or dies on closing rho_n:

  (i) prove a fluctuation-scale variance lower bound D_n >= c Q_n^2 for the SAME envelope Q_n that concentration provides (open; believed; this is "chi exists" in disguise), or
  (ii) prove chaos with eps_n smaller by the factor rho_n^2 (order n^2 stronger than anything the method yields - not a realistic target), or
  (iii) find an envelope Q_n genuinely at the fluctuation scale (equivalent to (i) plus concentration at that scale - the H1/H3 pair of the axiom set; this is what [8] proves from isotropy in the continuum).

So the honest program map is: H1+H3 (fluctuation-scale envelope with matching lower bound) is not one hypothesis among four - it is THE wall, and (CH) is only reachable after it. This sharpens MG1's "H3-lower is the single most restrictive axiom" into arithmetic: the shortfall is quantitatively n^2/log^4 n, not a constant.

## 3. What partial results ARE reachable from here (candidate statements for the campaign's remaining hours)
- P-a (unconditional, small but real): the lattice engine inequality (Theorem 8.1) with A2, A4 bounded via Kesten-scale inputs gives Var(X_Mn) <= kappa C M n + M sqrt(C' n^2 eps(kappa)) - i.e., a clean, self-contained REDUCTION: any chaos estimate eps(kappa) = o(1) at sqrt(n)-scale envelopes would already improve BKS's n/log n to o(n). Statement: "chaos implies sublinear variance, unconditionally on Z^2." Checkable, publishable as a remark, and to our knowledge not written anywhere in this exact form (verify literature before claiming novelty). [NOVELTY SWEEP RUN, iter 177 (2026-08-10): DOES NOT CLEAR AS MAIN RESULTD. Chatterjee's superconcentration-chaos duality is exactly the principle "sublinear variance <-> chaos" (his book and the FPP papers), arXiv 2302.11367 develops chaos-concentration-valleys for lattice FPP, and arXiv 2602.01036 (2026) proves the EQUIVALENCE for Bernoulli percolation's chemical distance. A remark maind "chaos implies sublinear variance" would read as re-deriving the known duality. What the sweep does NOT find published: the sharp constant-1 one-block engine inequality with atoms/no-isotropy/no-FKG, the (b/a)(n+W) occupation costing and its weak form o(N(n+W)), and the two BSS errata - a repositioned note on THOSE could still clear, but that is a different and humbler note, and whether to write it is the author's call. P-a assembly per the second-night order: OFF at this main.]
  [SUPERSEDED IN PLACE, iter 36: this display PRESUMES block-level moment bounds at Kesten scale (A2 ~ M n). Sections 4 and 5 below establish that the per-edge Kesten machinery does NOT regroup to blocks without an occupation input, and that the occupation input costs a factor (n+W): the unconditional truth is A2 <= 2C'(b-a)^2 M n(n+W), hence the WEAK form Var(X_N) = o(N(n+W)), not o(n). Read section 5's display, not this one. The strong form remains gated on fluctuation-scale (M1)-type inputs.]
- P-c (numerical, MG3): measure rho_n's empirical growth directly (Var from samples; envelope from empirical tail fits) alongside the chaos exponent - the first quantitative lattice picture of exactly the wall named above.

Nothing here claims progress on the wall itself. It locates it, to a power of n, and names the three doors.

## 3b. THE TWO OBSTACLES MEET AT alpha = 1/3 (added iter 49, author's hand; depends on the
## C1 analysis, whose referee is pending - so this is a flagged structural observation, not a theorem)
##
## >>> CHALLENGE RESOLVED, ITER 68: THIS SECTION STANDS, with one scope correction stated below.
## >>> The iter-66 challenge (section 7) is REFUTED. Decisive step, READ: MG2B line 130 puts
## >>> D := Var(X_n) in the halving lemma's STANDING ASSUMPTIONS, while line 132 lists what is free
## >>> (C1, C2, V, V4, kappa, eps) - D is not among them. Both sides of (9.3) are the true variance
## >>> functional at two scales, so the halving is a relation between TRUE variances; n^{1-eps} is the
## >>> OUTPUT of telescoping those relations, never an input to any rung. alpha is a function of
## >>> nature, not of the theorem being chased.
## >>> SCOPE CORRECTION OWED TO ITEM (1): "rho = O(1) forces alpha = 1/3" is too narrow. Correctly:
## >>> with Q_s ~ s^alpha and true Var(X_s) ~ s^{2 chi}, rho_s ~ s^{2(alpha-chi)} and the halving
## >>> demands eps <~ s^{-4(alpha-chi)}. So constant-strength chaos - the only strength a BSS-type
## >>> construction delivers - holds iff alpha <= chi, and H1a (concentration at scale Q) forces
## >>> alpha >= chi. Within the hypothesis set alpha = chi EXACTLY, and the wall alone already
## >>> forbids alpha > chi. The wall's admissible set is the INTERVAL (0, chi], not the point 1/3.
## >>> CONSEQUENCE FOR THE DISJOINTNESS: it is WIDER than this section claimed, but it is CONDITIONAL.
## >>> Its real hypothesis is chi <= sqrt(2)-1 = 0.4142, i.e. true variance exponent <= 0.8284 - much
## >>> weaker than full KPZ and widely believed, but UNPROVED. Nothing unconditional excludes
## >>> chi in (0.414, 1/2]. State the disjointness with that hypothesis attached, never flatly.

Write the envelope as Q_n ~ n^alpha. Two independent constraints have now been located, and they
close on each other at exactly one point.

(1) THE WALL NEEDS alpha = 1/3. Section 2 showed the halving demands eps <= 1/(16 C2 rho^2) with
rho = Q_n^2 / Var(X_n), and that a constant-strength chaos estimate suffices only when rho = O(1),
i.e. when the envelope IS the standard deviation. Under the conjectured KPZ behaviour
Var(X_n) ~ n^{2/3}, the standard deviation is n^{1/3}: so rho = O(1) forces alpha = 1/3. Any
envelope with alpha > 1/3 is a weaker (larger) envelope than the truth, and then rho grows
polynomially and the required chaos strength decays polynomially - the shortfall of Section 2.

(2) THE CORNER OBLIGATION NEEDS alpha > 0.414 ON PUBLISHED INPUTS (corrected by the C1 referee,
iter 50; the first version of this paragraph said 1/3 and that number assumed an unavailable input).
The axis-respecting construction proposed for (C1) trades a shift cost ~ W_s against a chaining cost
per increment set by the ALIGNMENT error. With alignment at the envelope scale (C Q_s log s) the
criterion is (3 alpha - 1)(alpha - 1) < 0, i.e. alpha > 1/3 - but envelope-scale alignment is itself
OPEN whenever Q_r << sqrt(r). On Alexander's published bound (C sqrt(s) log s) the optimisation gives
s = l^{2/(2+alpha)} and the criterion alpha^2 + 2 alpha - 1 > 0, i.e. alpha > sqrt(2) - 1 = 0.4142.

CONSEQUENCE, stated plainly - and the gap is WIDER than the first version of this section claimed.
At Kesten scale (alpha = 1/2) the corner construction closes but the wall is a factor n^2/log^4 n
away; as the envelope improves toward the truth the wall narrows and the corner construction
degrades; the construction fails at alpha = 0.414 on published inputs, while the wall does not close
until alpha = 1/3. So on today's inputs there is NO envelope exponent at which both are satisfied:
the workable window for the corner route is (0.414, 1/2] and the wall's requirement is alpha = 1/3,
and these are disjoint. The first version of this paragraph put the meeting point exactly at 1/3 and
called the failure marginal; corrected, the two constraints do not merely meet, they exclude each
other by about 0.08 in the exponent.

WHAT THIS DOES AND DOES NOT SAY. It does NOT say the program is impossible: the corner construction
is one route to (C1), not the only one, and a different axis-respecting argument might survive at
hand by taking the envelope to the truth, and that any future work should either (a) find a corner
argument whose cost does not scale like W_s, or (b) accept the arc-curvature obligation at the true
envelope and say so in the hypothesis list. Recording it now because it is invisible at the scale
where the pieces were each verified, and would otherwise be discovered only at assembly time.

## 4. P-a is not free either: the count-regrouping obstacle (added iter 16)
P-a's hypothesis set quietly includes block-level moment bounds (A2 <= C M V, A4 <= C M V4 at
Kesten scale), and these do NOT follow directly from the classical per-edge machinery. Per-edge
influence gives |X^e - X| <= b - a and #geodesic edges <= C M n, which is exactly Kesten's
Var = O(n) via Efron-Stein - but at BLOCK granularity, 1(U_ij)|X^ij - X| is controlled by the
number N_ij of geodesic edges in the block, and A2-type sums involve E[Sum_ij N_ij^2]. The
geodesic's total length is C M n, so Sum N_ij^2 <= (max_ij N_ij) * C M n; crudely max N_ij can
only be bounded by the block's edge count (~ n W), which overshoots. What is needed is a
regrouping lemma: geodesic occupation of an n x W block is O(n + W) with high probability (a
length-vs-displacement estimate inside a box), or a second-moment version of it. That looks
provable with bounded weights (a path spending >> n + W length inside an n x W box pays
proportionally in weight vs the b/a-competitive detour around it - the standard
detour-competitiveness argument), but it is a lemma to write and check, not a citation. So:
P-a = P-a1 (block occupation/count lemma at Kesten scale; concrete, plausibly elementary)
    + P-a2 (any o(1) block-chaos estimate).
P-a1 is now the campaign's sharpest self-contained UNCONDITIONAL target: elementary statement,
detour-based proof strategy, and it upgrades Theorem 8.1 from a framework into a usable
unconditional inequality with explicit Kesten-scale constants. Queue: attempt P-a1 with a
dedicated prover + hostile referee, same pipeline as the framework lemma.

## 5. P-a1 solved in the deterministic worst case - and what it does NOT give (added iter 16, author's hand)

LEMMA (deterministic block occupation - REFEREED FORM, sharp). Bond FPP on Z^2, weights in
[a,b], 0 < a <= b < infinity. For any geodesic gamma (any endpoints) and any axis-aligned n x W
lattice box B (L1-diameter n+W): the number of edges of gamma inside B is at most (b/a)(n+W).

Proof (referee's simplification - no perimeter detour needed). If gamma meets the closed box, let
x be its first vertex there and y its last (if gamma starts or ends inside B, take that endpoint).
Then x, y in B, so d_L1(x, y) <= n + W. A monotone lattice path from x to y has d(x,y) edges, each
of weight <= b, so by subpath optimality a|gamma[x->y]| <= T(gamma[x->y]) = X_xy <= b(n+W). Every
edge of gamma inside B lies on gamma[x->y]. QED. Tightness: a=b, corner-to-corner staircase in an
n x n box uses exactly 2n = n+W edges - equality.

REFEREE RECORD (2026-08-09): hostile referee CONFIRMED the lemma via independent adversarial
search (lexicographic Dijkstra maximizing box occupation among all geodesics, hill-climbing and
annealing over {a,b} weights, serpentine gadgets, degenerate and extreme-aspect cases - zero
violations; a=b certifies tightness). It REFUTED two pieces of the first draft, both repaired
above: (1) the "O(1) hop" claim for interior endpoints was false (the hop is Theta(n+W) at a box
center) - the diameter argument removes it entirely; (2) the constant sharpened 2b/a -> b/a, C0=0.

Consequence (TWO-SIDED, corrected per referee - the first draft's one-sided reading was a real
gap, numerically non-vacuous: X can drop under resampling of a block the OLD geodesic never
touched, so N_ij alone cannot control the minus direction even at N_ij = 0):
  (X^ij - X)^+ <= (b-a) N_ij      [old geodesic as candidate path in omega^ij]
  (X - X^ij)^+ <= (b-a) N'_ij     [NEW geodesic of omega^ij as candidate path in omega]
where N'_ij is the resampled configuration's geodesic occupation - and the occupation lemma
applies to gamma_new verbatim (omega^ij is just another [a,b] configuration). Hence pointwise
  1(U_ij)(X^ij - X)^2 <= (b-a)^2 (N_ij^2 + N'_ij^2),
and both Sum N_ij^2 and Sum N'_ij^2 are <= (b/a)(n+W) x (b/a)Mn + C by the lemma + total length:
  A2 <= 2 (b-a)^2 C' M n (n+W),   A4 <= 2 (b-a)^4 C'' M n (n+W)^3.
Order unchanged from the first draft; constants doubled; the two-sidedness is load-bearing.

SECOND REFEREE RECORD (2026-08-09, iter 59-61) - THE LAST CLAUSE ABOVE IS WITHDRAWN, and the two
referees do not actually conflict. The iter-21 referee was right that N_ij alone cannot control the
TWO-SIDED square pointwise: X really can drop when a block the old geodesic never touched is
resampled, and its numerical witness stands. The iter-59 referee observed that Theorem 8.1 never
consumes the two-sided square - Z_Lambda := 1(U_Lambda)(X^Lambda - X)^+ is what the engine is built
from, step (4)'s kappa-term is Sum E[Z^2], and steps (6)-(8) use only (.)^+ - so the theorem holds
verbatim with A2 replaced by A2^+ := Sum E[((X^Lambda - X)^+)^2] <= A2. Both readings are correct
about different objects.

VERIFIED HERE INDEPENDENTLY, and it is stronger than either referee said. Lemma 4.2 of the framework
draft is the EXACT identity E[(X - X^Lambda)^2] = 2 E[((X^Lambda - X)^+)^2], proved from swap
symmetry (Lemma 4.1). So the minus direction is not merely dispensable, it is exactly equal in
expectation to the plus direction. The N'_ij machinery introduced above was therefore never needed:
the pointwise two-sided bound can be replaced by the identity, and A2 is controlled by the OLD
geodesic's occupation alone, with the factor 2 arriving from Lemma 4.2 rather than from doubling a
pointwise bound.

THE THREE-LINE DERIVATION, WRITTEN OUT BECAUSE THE INDICATOR IS THE LOAD-BEARING STEP AND I NEARLY
GLOSSED IT. Per block, and note the middle step is an INEQUALITY, not an identity:
  E[1(U) (X^Lambda - X)^2]  <=  E[(X^Lambda - X)^2]              (drop the indicator; only grows)
                            =   2 E[((X^Lambda - X)^+)^2]        (Lemma 4.2, exact, from swap 4.1)
                            <=  2 (b-a)^2 E[N_ij^2].             ((6.2)-type bound, OLD geodesic)
The indicator cannot simply be carried through: off U_ij the old geodesic avoids the block, so
X^Lambda <= X there and the POSITIVE part vanishes, but the two-sided SQUARE does not - which is
precisely the iter-21 referee's witness. Dropping the indicator before applying 4.2 is what makes
the minus direction free, and it costs nothing because the discarded term is non-negative. Lemma 4.2
itself: (X, X^Lambda) exchangeable, so E[((X-X^Lambda)^+)^2] = E[((X^Lambda-X)^+)^2] and the two
halves of E[(X-X^Lambda)^2] are equal.

NET EFFECT ON THE NUMBERS: none. The displayed bounds A2 <= 2(b-a)^2 C' M n(n+W) and
A4 <= 2(b-a)^4 C'' M n(n+W)^3 already carry that 2 and are unchanged. What changes is the
justification, which loses a hypothesis-shaped dependence on the resampled configuration's geodesic,
and the sentence "the two-sidedness is load-bearing", which is false as stated. This is the only
surviving product of Sections 6-6c, all of which are withdrawn (see 6d).
These are WORST-CASE occupation bounds; they miss the Kesten-scale targets (A2 ~ M n) by a factor
(n+W). Plugging them into Theorem 8.1 gives, for the reduction P-a:
  chaos Pbar(kappa) <= eps M  =>  Var(X_Mn) <= kappa C M n(n+W) + M (n+W)^{3/2} sqrt(C n eps) -
i.e. "chaos implies Var = o(n (n+W))" - genuinely unconditional but WEAKER than BKS n/log n unless
eps is quantitatively small in n. The missing ingredient for the strong form of P-a is a TYPICAL-
size influence bound (second moment of (X^ij - X) at the fluctuation scale, not the worst case) -
which is precisely the (M1) hypothesis again. So the honest ledger:
  P-a1 (occupation lemma): REFEREED AND CONFIRMED (sharp constant b/a, simpler proof, tight at
  a=b); the A2/A4 consequence now stated two-sided per the referee's gap-finding. Unconditional.
  P-a strong form: still gated on (M1)-type inputs (typical-size, fluctuation-scale); the
  occupation lemma gives only the weak form. No claim beyond this.
Referee verdicts on the draft: lemma HOLDS (constant corrected), proof's O(1)-hop claim REFUTED
(repaired by the diameter argument), one-sided A2 reading REFUTED with a numerical witness
(repaired two-sided above). The referee could not verify the weak-form display against Theorem
8.1's statement from this file alone (the statement lives in MG2B_framework_lemma_draft.md);
the reverse-engineered plug-in shape matched. Cross-check completed by the author: the
display follows from Theorem 8.1 as stated there with the corrected A2/A4 constants.

## 6. The fourth moment is not an independent input: A4 <= B^2 A2 (added iter 56, author's hand;
## DERIVED here, NOT yet refereed - treat as a candidate, not a result)

Theorem 8.1 feeds the engine two moment quantities,
  A2 := Sum_Lambda E[1(U_Lambda)(X^Lambda - X)^2],
  A4 := Sum_Lambda E[1(U_Lambda)((X^Lambda - X)^+)^4],
and Section 2 bounded A4 crudely at envelope scale (V4 ~ Q^4). That is wasteful, because the two are
the same increment raised to different powers.

(6.1) DETERMINISTIC INCREMENT BOUND. Let gamma := gamma_can(omega) and let B be any number with
(X^Lambda - X)^+ <= B pointwise on U_Lambda. Then on U_Lambda,
  ((X^Lambda - X)^+)^4 <= B^2 ((X^Lambda - X)^+)^2 <= B^2 (X^Lambda - X)^2,
and summing over blocks gives, with no probabilistic input whatsoever,
  A4 <= B^2 A2.                                                            (6.1)

(6.2) WHAT B IS. Comparing the omega-geodesic against itself in the resampled field,
  T_{omega^Lambda}(gamma) = T_omega(gamma) + Sum_{e in gamma cap Lambda} (w'_e - w_e)
                          <= X + (b-a) |gamma cap Lambda|,
and X^Lambda <= T_{omega^Lambda}(gamma), so (X^Lambda - X)^+ <= (b-a) |gamma cap Lambda|. The
increment bound is therefore exactly a per-block GEODESIC OCCUPATION bound, which is the quantity
Section 5's refereed lemma already controls: |gamma cap Lambda| <= (b/a)(n + W) deterministically for
an n x W block.

(6.3) CONSEQUENCE FOR THE CRUX. Substituting (6.1) into (8.1),
  Var(X) <= kappa A2 + B sqrt(A2 Pbar(kappa)),
so the engine needs only ONE moment quantity plus a sup-bound on the increment. Running the halving
with A2 <= C M D and Pbar <= eps M as in Section 2, the second term is at most B M sqrt(C D eps), and
requiring it to be at most (1/4) M D gives
  eps <= D / (16 C B^2).                                                   (6.3)
Section 2's requirement was eps <= 1/(16 C2 rho^2) with rho = Q^2/D. Display (6.3) is the same
statement with Q^2 replaced by B^2: when the increment sits at envelope scale, B ~ Q, (6.3) reads
eps <= D/(16 C Q^2) = 1/(16 C rho) - a factor rho WEAKER than Section 2's demand, because Section 2
charged the second moment at envelope scale Q^2 when it is really at variance scale D.

(6.4) HONEST ACCOUNTING - THIS DOES NOT IMPROVE THE UNCONDITIONAL NUMBER. With the deterministic
occupation bound of (6.2), B ~ (b-a)(b/a)(n+W) ~ n at W = sqrt(n Q) with Q = n^{1/3}, so (6.3) gives
eps <~ D/n^2 <~ log n / n^2, which is WORSE by log^3 n than Section 2's log^4 n / n^2. The gain
appears only if the increment can be held at envelope scale rather than at the deterministic
occupation scale. So the correct statement of what (6.1) buys is structural, not numerical:

  the engine's fourth-moment input is not independent information. It is the second-moment input
  times the square of a per-block occupation bound. The hypothesis set therefore loses one member
  (A4) and gains a sharper, more concrete obligation: a high-probability bound of order Q on the
  number of edges a geodesic spends inside a single n x W block.

(6.5) WHAT WOULD FALSIFY OR CONFIRM THIS. (6.1) and (6.2) are pointwise and should survive any
referee; the load-bearing steps are the use of A2 <= C M D in (6.3) - which Section 3's iter-36
supersession already flags as PRESUMING block-level moment bounds the lattice does not give
unconditionally - and the claim that no step of Theorem 8.1's proof needs A4 except through step (8)
of its proof chain. Both must be checked before any of this is exported. The sub-target named in
(6.4) is not obviously easier than the chaos gap it replaces; it is, however, a different question,
and it is about geodesic geometry rather than about correlation decay.

## 6b. SELF-CORRECTION to 6.4, before the referee returns (iter 57): the sub-target as I named it is
## not merely hard, it is FALSE - and the right target is a different object

Section 6.4 named the new obligation as "a high-probability bound of order Q on the number of edges a
geodesic spends inside a single n x W block." That is unreachable, and the geometry says so in one
line.

(6b.1) TYPICAL OCCUPATION IS OF ORDER n, NOT Q. The blocks are n wide and W tall, with
W = sqrt(n Q). At the conjectured exponents, Q = n^{1/3} gives W = n^{2/3}, which is exactly the
transversal wandering scale n^{xi} = n^{2/3}. So a geodesic crossing a column of width n wanders
vertically by an amount comparable to a single block's height: it meets O(1) blocks in that column
and spends order n edges inside them. Any claim that |gamma cap Lambda| = O(Q) = O(n^{1/3}) for the
blocks the geodesic actually uses contradicts the fact that crossing the column costs order n edges
distributed over O(1) blocks. The occupation route therefore caps out at B ~ n - which is precisely
the deterministic bound (6.2) already gives, and precisely why 6.4 conceded no unconditional gain.

(6b.2) SO (6.2) IS VALID BUT LOSSY, AND THE LOSS IS THE WHOLE GAP. The chain
(X^Lambda - X)^+ <= (b-a)|gamma cap Lambda| is correct - it stands - but it throws away everything
that makes the increment small. It prices the increment as if every resampled edge on the geodesic
moved against us by the full weight spread, when in truth the resampled weights move in both
directions and the path may reroute. The bound is tight only for an adversarial resampling, and the
measure is not adversarial.

(6b.3) THE CORRECTED SUB-TARGET. What the engine needs is a bound of order Q on the INCREMENT
itself, and the increment is a different object from the occupation: it is the difference of two
passage times that share every block but one, hence far smaller than either one's fluctuation. The
second-moment bookkeeping already says as much. If A2 ~ M D and the geodesic meets of order M
blocks, the per-block second moment is of order D, so the TYPICAL increment is of order sqrt(D) -
which at fluctuation scale IS of order Q. The typical behaviour is therefore already what (6.3)
wants; what is missing is control of the upper tail on the event U_Lambda, i.e. a statement of the
form P[(X^Lambda - X)^+ > lambda Q, U_Lambda] decaying fast enough that the sup-bound B may be taken
at envelope scale up to a harmless correction.

(6b.4) WHAT THIS CHANGES ABOUT THE STANDING OF SECTION 6. Displays (6.1), (6.2) and (6.3) are
unaffected - they are pointwise algebra and stand or fall on the referee's reading of them. What
falls is 6.4's naming of the follow-on obligation: it is not an occupation statement, it is an
increment-tail statement, and the two differ by the factor n/Q that the whole argument is trying to
find. I would rather record that I misnamed it than let a referee find it, and I record also that I
found it by asking what the geometry actually does rather than by re-reading my own prose.

## 6c. What the wall actually is, restated: a KURTOSIS question about one-block increments
## (iter 57/58, author's hand; DERIVED, NOT REFEREED; supersedes the framing of 6.4 and 6b.3)

Section 6b left the target as "control the upper tail of the increment". Pushing that one step
further changes what the wall IS, and the change is worth stating carefully because it looks
favourable and favourable-looking things are where I have been wrong tonight.

(6c.1) WHERE Q ENTERED IN THE FIRST PLACE. Section 2's V4 ~ Q^4 is not a computation, it is the
crude substitution |X^Lambda - X| <~ Q: the increment is charged at the ENVELOPE scale. Every
appearance of rho = Q^2/D in the requirement traces back to that one substitution.

(6c.2) THE ALTERNATIVE CHARGE. Write sigma_Lambda^2 := E[1(U_Lambda)(X^Lambda - X)^2], so that
A2 = Sum_Lambda sigma_Lambda^2. Suppose the block increments have bounded kurtosis at their OWN
scale, i.e. for some absolute K,
  E[1(U_Lambda) ((X^Lambda - X)^+)^4] <= K sigma_Lambda^4   for every block.        (H-kurt)
Then A4 <= K (max_Lambda sigma_Lambda^2) A2. In the halving regime the blocks the geodesic meets
carry sigma_Lambda^2 of order D, so A4 <~ K D A2, and (6.3) becomes
  eps <= D / (16 C K D) = 1 / (16 C K),
a CONSTANT - which is exactly the strength a BSS-type chaos construction delivers.

(6c.3) WHY THIS IS CONSISTENT AND NOT A TRICK. rho^2 = (Q^2/D)^2 = Q^4/D^2. Replacing the charge
Q^4 by the charge D^2 removes precisely a factor rho^2 from the requirement, which is exactly the
shortfall Section 2 measured. So (6c.2) is not a new gain on top of Section 2 - it is the statement
that Section 2's entire shortfall IS the gap between charging the increment at envelope scale and
charging it at its own scale. The wall and the crude substitution are the same object seen twice.

(6c.4) WHAT (H-kurt) COSTS, AND WHY IT IS NOT FREE. The deterministic bound of (6.2) allows
|X^Lambda - X| ~ (b-a)(b/a)(n+W) ~ n, while the typical size is sqrt(D) ~ n^{1/3} at conjectured
exponents. So the increment's range exceeds its typical scale by n^{2/3}, and (H-kurt) is a genuine
tail demand: since E[(ΔX)^4] >= n^4 P[|ΔX| ~ n], (H-kurt) with sigma^2 ~ D ~ n^{2/3} forces
  P[ |X^Lambda - X| ~ n ] <~ K n^{4/3 - 4} = K n^{-8/3}.
A polynomial tail bound of that order is plausible under stretched-exponential concentration but is
NOT available unconditionally on Z^2, and it is precisely the regime - geodesic forced to spend
order n edges in one block - where the crude bound is tight.

(6c.5) WHAT THIS DOES AND DOES NOT ACHIEVE. It does NOT prove anything unconditionally, and it does
not close the problem. What it does is relocate the wall: Section 2 stated the obstruction as
"either prove a fluctuation-scale variance lower bound for the same envelope concentration provides
(chi exists in disguise), or beat chaos by a factor rho^2." (6c) adds a third door that is a
different KIND of statement - not an exponent, but a shape: bounded kurtosis of one-block
resampling increments relative to their own second moment. Exponent statements and shape statements
fail for different reasons, and the shape statement never mentions Q at all.

(6c.6) THE INHERITED WEAKNESS, STATED PLAINLY. Everything here still runs through A2 <= C M D, which
Section 3's iter-36 supersession already flags as PRESUMING block-level moment bounds the lattice
does not give unconditionally (the honest unconditional form there is A2 <= 2C'(b-a)^2 M n(n+W)).
So (6c) does not escape that gate; it removes the A4 gate and leaves the A2 gate standing. Two gates
became one gate plus a shape hypothesis. That is the whole claim, and it needs a referee before it
is worth anything.

(6c.7) NOVELTY NOT VERIFIED. I have called (H-kurt) a "third door" without searching for it. No
literature search has been run on fourth-moment or kurtosis conditions for one-block resampling
increments in FPP, and moment-comparison conditions of this shape are common enough in concentration
arguments that the prior should be that something like it exists. Before any of 6c is exported, the
door must be checked against the literature - Benjamini-Kalai-Schramm, Chatterjee's superconcentration
programme, and the hypercontractivity route are the obvious places - and if it is known, 6c's value
is limited to locating it inside THIS engine's arithmetic rather than to the condition itself.

(6c.8) LITERATURE CHECK RUN (iter 59) - THE "THIRD DOOR" FRAMING IS WITHDRAWN. Two searches against
the FPP concentration literature. What they establish: moment-comparison conditions on discrete
differences are not a new KIND of tool here, they are the central one. Benjamini-Kalai-Schramm's
improvement over Kesten runs on hypercontractivity together with Talagrand's L1-L2 inequality, and
essentially every subsequent improvement to the variance upper bound in FPP has used that route;
Talagrand's L1-L2 variance inequality is described in the survey literature as one of the rare tools
towards sub-diffusive and superconcentration regimes across percolation, random matrices and spin
glasses. More pointedly, there is published work generalizing the BKS-Talagrand variance bound
expressed in terms of the L2-norms of HIGHER-ORDER derivatives - i.e. exactly the family (H-kurt)
belongs to.

So the honest revision. I did NOT find (H-kurt) stated in this exact form, and I am not asserting it
is absent - that would repeat the error 6c.7 was written to avoid. What I can say is that the prior
6c.7 named has been confirmed: this is a well-populated neighbourhood, and calling an L4-L2
comparison a new door in a field whose main technique is an L1-L2 comparison was unsupported.

WHAT SURVIVES OF SECTION 6c. Not the novelty of the condition. What survives is the localization:
displays (6c.1)-(6c.3) identify the single line in THIS engine's arithmetic where the envelope-scale
substitution enters, show that the entire Section 2 shortfall is that substitution and nothing else,
and compute what replacing it would buy. That is a statement about this engine's bookkeeping, not a
contribution to concentration theory, and it should be presented as such or not at all.

WHAT THIS SUGGESTS INSTEAD. If the L1-L2 route is what actually powers every known improvement here,
then the productive question is not "assume bounded kurtosis" but "what does Talagrand's L1-L2
inequality give for the block increments X^Lambda - X directly?" - i.e. run the established tool on
the engine's own quantity rather than hypothesizing the moment comparison it would produce. That is
the next concrete step, and it is a literature-grounded one rather than an invented hypothesis.

## 6d. REFEREE VERDICT ON SECTIONS 6/6b/6c: MAJOR REVISION - the algebra survives, the contribution
## does not (iter 59). Nothing in 6, 6b or 6c is exportable.

WHAT THE REFEREE CONFIRMED IN MY FAVOUR. (6.1) is valid, with two conditions I failed to state: B
must be deterministic (or a.s.) and UNIFORM over blocks, else it cannot leave the expectation. The
positive-part mismatch is harmless and runs the favourable way. (6.2) is valid and in fact holds on
all of Omega, not only U_Lambda. A4 enters Theorem 8.1 only at steps (6)-(8), so the substitution is
legitimate and does not double-count. The route is not circular. The log^3 n concession in 6.4 was
recomputed independently at n = 10^12 and is right in direction and exactly right in magnitude.

WHAT KILLED IT.
(D1) B = Theta(n) is FORCED on Z^2, not an artifact of a crude bound. Witness: weights a inside the
block, b outside, endpoints (0,0) to (L,0); the straight path is the geodesic, uses exactly n edges
of the block, and resampling to all-b moves the passage time by exactly (b-a)n. So (6.2) is TIGHT
and the pointwise formulation can never do better than eps <~ D/n^2. My 6b guessed this; the referee
proved it.
(D3) The sub-target I named in 6.4 is FALSE, and the referee's counting is sharper than my 6b
argument: for each column, gamma needs >= n horizontal edges and >= (k-2)W vertical ones to meet k
blocks, and summing against |gamma| <= (b/a)Mn forces max_j |gamma cap Lambda_ij| >= c'W = c'n^{2/3}
deterministically, for every geodesic in every configuration. Even the best conceivable occupation
bound B ~ W gives eps <= n^{-2/3}, still short of a constant by n^{2/3}.
(D2) "The hypothesis set loses A4" is FALSE. With anything weaker than a uniform pointwise B there
is a residual fourth-moment tail, and that residual IS (M2) - BSS handle exactly it in their (16).
(M2) is re-expressed, not eliminated. Ledger: minus (M2), plus a sup-norm hypothesis that is
strictly stronger and, by D1, false at the needed scale. Net zero.
(D5) THE REAL BOOKKEEPING ERROR, and it is in the sentence I flagged to the referee as most
dangerous. Two things wrong at once. First, "the same statement with Q^2 replaced by B^2" is
literally false - the substitution is V4 = Q^4 -> V4 = B^2 D, i.e. ONE factor of Q^2 becomes D.
Second, and worse: Section 2 did NOT mischarge the second moment. Its A2 was charged at variance
scale throughout - that is where the D^2 numerator comes from - and what sits at envelope scale is
the FOURTH moment, which BSS charge there deliberately and correctly, because for them
Var(X_n) = Theta(Q_n^2). SECTION 2 MADE NO ERROR. My diagnosis of it was wrong, and I repeated that
wrong diagnosis in 6c.1 and 6c.3, which must be struck.
(D6) The route is DOMINATED. Inserting the same hypothesis one step earlier gives
Var <= kappa A2 + B^2 Pbar - no square root, no A2 in the second term - and needs only
eps <= D/(4 B^2), better than (6.3) by 4C. Going through sqrt(A2 Pbar) throws that away and is what
manufactured the appearance of circularity.
(D8, D9) 6.4 mixes conjectural and unconditional inputs (Q = n^{1/3} presupposes D ~ n^{2/3}, yet D
was taken as log n), and compares a genuinely unconditional route against Section 2's number, which
is NOT unconditional. The conclusion is robust but the derivation as printed is incoherent.
(D10) NOT NOVEL, and not even within this campaign: Section 5 already performs exactly this move
(Sum N^4 <= (max N)^2 Sum N^2), and the resulting orders coincide. BSS do not use A4 <= B^2 A2
explicitly, but their numerology encodes it invisibly since Var(X_n) = Theta(Q_n^2). Independent
literature search the same fire reached the same verdict from the other side: moment comparison on
discrete differences is the CENTRAL tool of this field (BKS via hypercontractivity and Talagrand's
L1-L2), with published generalizations in terms of L2-norms of higher-order derivatives.

(6d.1) THE ONE THING WORTH KEEPING, AND IT CORRECTS AN EARLIER REFEREED ARTIFACT. (D7) The engine
consumes ONLY the positive part: step (4)'s kappa-term and steps (6)-(8) all use (.)^+, so Theorem
8.1 holds verbatim with A2 replaced by A2^+ := Sum E[((X^Lambda - X)^+)^2] <= A2. This matters
beyond constants. A2^+ is controlled by gamma_can's occupation ALONE, so Section 5's conclusion that
"the two-sidedness is load-bearing" is WRONG FOR THE ENGINE - the N'_ij term and the doubled
constants introduced there are needed only for a two-sided A2 that Theorem 8.1 never uses. That
correction outlives everything else in Sections 6-6c and should be carried into Section 5.

(6d.2) STANDING. Sections 6, 6b and 6c are withdrawn as a contribution. What is true in them is
either near-trivial (6.1, 6.2), already present in Section 5 (D10), or a restatement of the source's
own numerology. The minimum repair the referee specifies is recorded above; I am not performing it,
because a repaired version would still establish nothing. The honest ledger entry for four fires of
work is: one real correction to Section 5 (D7), one confirmed-correct concession (the log^3 loss),
and a wrong diagnosis of Section 2 that I published in three places and have now struck.

## 7. FLAGGED QUERY AGAINST MY OWN SECTION 3b: is the disjointness an artifact of importing the KPZ
## endpoint into an argument that never needed it? (iter 66, author's hand; NOT a result -
## this is a question with a reason attached, sent to a referee before anything is claimed)

WHAT PROMPTED IT. A literature read of the source's own discussion of scales. Two statements from
the authors matter here. First, they explicitly name the lattice extension as plausible future work:
relaxing rotational invariance for lattice models "with the additional assumption that the limit
shape is uniformly curved". Second, and this is the load-bearing one, they say they are NOT
attempting concentration at the correct standard-deviation scale, only at scale n^{1/2 - eps}.

THE QUERY. Section 3b fixed the wall's requirement at alpha = 1/3 by this route: the halving needs
rho = Q_n^2 / Var(X_n) = O(1), i.e. the envelope must BE the standard deviation; then it substituted
the conjectured KPZ behaviour Var ~ n^{2/3}, whose standard deviation is n^{1/3}, and concluded
alpha = 1/3.

But the theorem this program is chasing is Var(X_n) = O(n^{1 - eps}) for SOME eps > 0 - not
Var ~ n^{2/3}. The condition rho = O(1) does not say "alpha = 1/3"; it says "alpha equals half the
variance exponent AT THE SCALES BEING ITERATED". If the iteration runs at variance n^{1-eps}, the
matching envelope exponent is alpha = (1-eps)/2, which for small eps sits just below 1/2 - and
concentration at scale sqrt(n / log n), i.e. alpha = 1/2 up to logs, is available unconditionally
from Kesten and Talagrand.

WHY THIS MATTERS, AND WHY I AM NOT CLAIMING IT. If the wall's requirement is alpha ~ (1-eps)/2
rather than alpha = 1/3, then it is COMPATIBLE with the corner route's window alpha > sqrt(2)-1
~ 0.414, because 0.414 < (1-eps)/2 < 0.5 for small eps. The "two obstacles are disjoint and exclude
each other by about 0.08 in the exponent" finding - which I reported twice - would then be an
artifact of substituting the KPZ endpoint into an argument that never needed it.

THE STRONGEST CASE THAT I AM WRONG, written before the referee sees it. Section 2's shortfall does
not come from the envelope alone; it comes from rho, and rho has Var(X_n) in the DENOMINATOR. What
is unconditionally known about that denominator is only Var >= c log n (Newman-Piza). So rho is
O(1) only if a matching variance LOWER bound at the same scale is assumed - which is exactly what
H1+H3's two-sided ratio is, and exactly what Section 2 called "chi exists in disguise". On that
reading alpha is not free to be chosen near 1/2: it is pinned to the true variance exponent, and if
the truth is KPZ then alpha = 1/3 whatever theorem one is chasing, because rho is about the TRUE
variance, not the one being proved. If that is right, Section 3b stands and this query is empty.

WHICH OF THE TWO IS CORRECT TURNS ON A SINGLE QUESTION: in the halving step, is D_n the variance
being PROVED at that scale (an inductive quantity, free to be n^{1-eps}), or the TRUE variance of
the model (fixed by nature, KPZ if the conjecture holds)? I do not know, and the whole disjointness
finding rests on the answer. Sent to a referee.

--------------------------------------------------------------------------------------------------
## 8. The wall re-derived in the lemma's OWN quantities, and the n^2 shortfall confirmed by a
## second, independent route (iter 123, 2026-08-10, author's hand; referee to check)

Sections 2 and 3b price the wall through the envelope packaging: V4 ~ Q^4, rho = Q^2/D, shortfall
n^2/log^4 n. That number is the single most load-bearing figure in the whole campaign and it has
never been derived a second way. Here it is, in the quantities the refereed lemma actually uses.

### 8.1 The requirement without envelopes

MG2B's halving consumes (M1) A2 <= C1 M V, (M2) A4 <= C2 M V4, (CH) Pbar <= eps M, where
    A2 := Sum_Lambda E[1(U_Lambda) (X^Lambda - X)^2],
    A4 := Sum_Lambda E[1(U_Lambda) ((X^Lambda - X)^+)^4],
both sums over the ~M blocks at scale n inside the scale-Mn column, U_Lambda the touching event.
V and V4 are BOUNDS chosen by the user, so the smallness condition (9.2), eps <= D^2/(16 C2 V4),
is best read with the bounds saturated:

    THE HALVING NEEDS:    eps * A4  <=  M D^2 / 16,        D := Var(X_n).                    (8.1)

This is not a statement about the global passage time's concentration scale. A4 is a sum of
FOURTH MOMENTS OF SINGLE-BLOCK RESAMPLING INCREMENTS on the touched event - a local quantity -
while D is the global variance at scale n. The envelope enters only as one way to bound A4.

### 8.2 Second route to the same power: per-block Kesten moments

Bound A4 blockwise instead of by a global envelope. On U_Lambda the increment (X^Lambda - X)^+ is
dominated by the change in the cost of traversing the block region, i.e. by a difference of two
passage times across a region of diameter ~n. Kesten-scale concentration for those crossings gives
exponential tails at scale sqrt(n), hence a fourth moment O(n^2) per block [CAVEAT, stated because
it is not free: the geodesic's entry and exit points on the block boundary are random, so this
needs a version uniform over boundary pairs - a union over O(n) pairs, costing at most a log power
in the tail estimate. Referee: this is the step to attack.] Summing over the ~M touched blocks:

    A4 <~ M n^2 (polylog),    so (8.1) becomes    eps <~ D^2 / n^2 (polylog).

With the best unconditional lower bound D >= c log n this is eps <~ log^2 n / n^2 - the SAME power
of n as Section 2's log^4 n / n^2, reached without ever mentioning Q. The two routes differ only in
the log exponent, and in the expected direction: the global-envelope bound M Q^4 = M n^2/log^2 n is
slightly SHARPER than the blockwise M n^2, so Section 2's requirement is correspondingly stricter.

    CONCLUSION: the n^{-2} shortfall is a property of the arithmetic, not of the envelope
    packaging. Section 2's central number survives an independent derivation.

### 8.3 Two shortcuts that do not work, recorded so they are not re-walked

(a) THE DETERMINISTIC INCREMENT BOUND IS WORSE, NOT BETTER. Since ((X^L - X)^+)^4 <= L_max^2
(X^L - X)^2 with L_max the deterministic increment cap ~ b(n+W), one gets A4 <= L_max^2 A2, and
with the sharp occupation input A2 <= C M n(n+W) this yields eps <~ D^2 / (n (n+W)^3), i.e. n^{-4}
at W ~ n. Trading the probabilistic input for a deterministic one costs two more powers of n. The
fluctuation-scale content of A4 is doing real work and cannot be given up.

(b) EFRON-STEIN POINTS THE WRONG WAY. Efron-Stein gives D <= (1/2) Sum_Lambda E[(X^Lambda - X)^2],
i.e. a LOWER bound on the increment sum in terms of the variance. (8.1) needs an UPPER bound on a
fourth-moment increment sum against D^2. The free inequality constrains the same objects in the
unhelpful direction; it yields no lower bound on D, which is what the wall is short of.

### 8.4 What this changes about the three doors

Section 2's door (iii) asks for "an envelope Q genuinely at the fluctuation scale" - a statement
about the GLOBAL passage time. Display (8.1) shows the lemma never needs that object: it needs an
upper bound on the LOCAL block-increment fourth moment A4 at the true fluctuation scale, together
with the variance lower bound D. These are different statements, and the local one is formally
weaker - it constrains block-crossing fluctuations, not the concentration of X_n itself. Whether
that is easier is open and I claim nothing about it; what is established here is only that the
target may be restated locally, so a future attempt is not obliged to prove global concentration
at the fluctuation scale in order to feed this lemma.

The variance lower bound D remains untouched by any of this, and it is the half of the wall that
Newman-Piza's log n leaves furthest from the truth. Nothing here moves chi = 1/3.

--------------------------------------------------------------------------------------------------
## 9. The wall reduces to TWO single-block moment statements (iter 124, elementary given the
## refereed lemma; conditional, referee to check every line - this is NOT a solution)

Section 8 showed the halving's requirement is local. Pushing that: the resampling pair's symmetry
strips both hypotheses (M1) and (M2) down to per-block moments, and the whole quantitative wall
lands on ONE inequality.

### 9.1 Both hypotheses are pure Efron-Stein sums

Write Delta_L := X^L - X for the increment from resampling block L (X at scale Mn, L at scale n,
~M blocks). Two structural facts already in the refereed lemma:

  (S) SYMMETRY. omega_L and omega'_L are iid, so (X, X^L) is an EXCHANGEABLE pair and Delta_L is
      symmetric: Delta_L =_d -Delta_L.
  (P) ONE-SIDEDNESS. Definition 3.3 / eq (6): Delta_L <= 0 off U_L (if the geodesic misses L the
      old path survives, so resampling cannot raise X). Hence (Delta_L)^+ vanishes off U_L, and the
      indicator in A4 is REDUNDANT.

Therefore, with no loss:
    A4 = Sum_L E[((Delta_L)^+)^4] = (1/2) Sum_L E[Delta_L^4]        by (P) then (S),
    A2 = Sum_L E[1(U_L) Delta_L^2] >= Sum_L E[((Delta_L)^+)^2] = (1/2) Sum_L E[Delta_L^2].
The second line also gives the sanity check A2 >= Var(X_Mn) via Efron-Stein, as it must.

### 9.2 Two per-block conditions

  (L1) SECOND-MOMENT CAP.  E[Delta_L^2] <= beta * Var(X_n)   for every block L, uniformly in n.
  (L2) KURTOSIS CAP.       E[Delta_L^4] <= kappa4 * (E[Delta_L^2])^2   for every block L.

CLAIM. (L1) implies (M1) with V = D := Var(X_n) and C1 = beta, since
A2 <= Sum_L E[Delta_L^2] <= M beta D. And (L1)+(L2) imply (M2) with V4 = D^2:
    A4 = (1/2) Sum_L E[Delta_L^4] <= (kappa4/2) Sum_L (E[Delta_L^2])^2
       <= (kappa4/2) (max_L E[Delta_L^2]) Sum_L E[Delta_L^2] <= (kappa4 beta^2 / 2) M D^2,
so C2 = kappa4 beta^2/2. Feeding (9.2): kappa <= D/(4 C1 V) = 1/(4 beta), and
    eps <= D^2/(16 C2 V4) = 1/(8 kappa4 beta^2)   - A CONSTANT, independent of n.
[SUPERSEDED 2026-08-12, marker added by REF-W2 curation - do NOT learn the 1/(8...) from this
line in isolation. The factor-1/2 in A4 and C2 = kappa4 beta^2/2 above rest on the FALSE support
identity E[Delta^4] = p m4; the delivered constant is 1/(16 kappa4 beta^2 C_occ), C2 = kappa4
beta^2 C_occ (no 1/2). Full correction: section 9.5's [REF-W1] bracket + CRUX9_wall_referee_
W2_20260812.md CheckB. This display is kept as the original derivation, not the current value.]

    CONSEQUENCE. Under (L1)+(L2), CONSTANT-strength chaos delivers the halving. No envelope, no
    fluctuation-scale concentration, no value of chi is used anywhere.

### 9.3 Where the difficulty actually went - said plainly, because this looks too cheap

It did not vanish; it concentrated. Efron-Stein plus (L1) alone already gives
Var(X_Mn) <= (1/2) Sum_L E[Delta_L^2] <= (beta/2) M D. So beta <= 1 would prove the halving with no
engine, no chaos and no lemma at all - which means (L1) at beta <= 1 must be false or unprovable,
and the honest reading is that the engine's whole job is to convert a constant beta > 1 into the
factor 1/2. That is exactly what 9.2 says it does.

And (L1) at ANY constant beta is hard for the same reason the wall was hard: it compares a single
block's influence against Var(X_n), whose only unconditional lower bound is c log n. Proving
E[Delta_L^2] <~ log n is far beyond current technology. So the wall persists INSIDE (L1).

What is gained is not strength but LOCATION and SHAPE:
  - the obstruction is now ONE inequality about ONE block's resampling increment, not a joint
    condition coupling an envelope, a variance lower bound and a chaos strength;
  - the chaos strength is NOT where the difficulty lives - constant strength, the only strength a
    BSS-type construction yields, suffices once (L1)+(L2) hold. Section 2's "eps <~ log^4 n/n^2"
    is therefore an artifact of routing the fourth moment through a lossy envelope, not an
    intrinsic demand of the engine;
  - (L2) is a SHAPE condition (fourth moment against the square of the second), scale-free, and
    plausibly reachable from concentration estimates that do not know the fluctuation exponent.

REFEREE, THE ATTACK LIST. (i) Does (P) really make the indicator redundant - check eq (6)'s
hypotheses cover every block family used, including the far blocks of Remark 8.3. (ii) Is the
exchangeable-pair symmetry legitimate given the canonical geodesic SELECTION (the selection is a
function of omega, so X^L uses the selection in the resampled field - confirm the pair is still
exchangeable in law). (iii) The step max_L E[Delta^2] * Sum_L E[Delta^2] is crude; a referee may
sharpen it, which only helps. (iv) Whether (L1)+(L2) are jointly consistent with anything provable
today - I claim only the implication, not the hypotheses.

### 9.4 Caveat found by auditing 9.1-9.3 immediately after writing them

Every Efron-Stein use above (the check A2 >= Var(X_Mn), and the "beta <= 1 needs no engine" remark)
requires the block family to PARTITION the independent coordinates. The engine's restricted
families (Remark 8.3's far blocks) do not; for a restricted family the Efron-Stein comparison runs
only in the direction Sum_restricted <= Sum_full, so those two remarks are statements about the
FULL partition. The main implication of 9.2 is unaffected: it uses only (L1), (L2) and the lemma's
own (M1)/(M2), never Efron-Stein.

Smell test passed, and it is the strongest check available here: the source paper has exactly
V = D and V4 = Theta(D^2), and constant-strength chaos suffices there. Section 9.2 is the lattice
restatement of that same shape in per-block language - so the reduction reproduces the source's
structure rather than beating it, which is what a correct reformulation should do. Under KPZ
behaviour (L1) holds with beta = O(1) (one block's resample moves X by the local fluctuation
~ n^{1/3} while Var(X_n) ~ n^{2/3}), which is why the reduction is honest but not free: it is true
exactly when the conjecture is, and unprovable today for the same reason the wall was.

### 9.5 CORRECTION TO 9.2, found by my own audit one iteration later (iter 125). Read 9.2 THROUGH
### this subsection: the implication survives, the hypotheses as I first stated them do not.

THE DEFECT. (L2) was stated unconditionally: E[Delta_L^4] <= kappa4 (E[Delta_L^2])^2. Write
p_L := P(U_L) and let m2, m4 be the moments CONDITIONED on touching. Since Delta_L = 0 unless the
geodesic (in one field or the other) meets L,
    E[Delta^2] = p m2,   E[Delta^4] = p m4,   so the unconditional kurtosis is (1/p) (m4/m2^2).
An unconditional kurtosis cap kappa4 therefore FORCES p >= 1/kappa4 for every block - i.e. every
block touched with constant probability - which is false for the far blocks the engine must include.
(L2) as printed in 9.2 is not merely unproved; it is essentially false at the far blocks. A referee
would have killed it first.

THE REPAIR - condition on touching, and pay the count separately:
  (L1') E[Delta_L^2 | U_L] <= beta Var(X_n)                     per block
  (L2') E[Delta_L^4 | U_L] <= kappa4 (E[Delta_L^2 | U_L])^2     per block, scale-free shape
  (L3)  Sum_L P(U_L) <= C_occ M                                 expected number of blocks met
Then, with T := Sum_L p_L,
  A2 = Sum_L p_L E[Delta^2|U] <= beta D T <= beta C_occ M D           -> (M1), V = D
  A4 = (1/2) Sum_L p_L E[Delta^4|U] <= (kappa4 beta^2/2) D^2 T
                                    <= (kappa4 beta^2 C_occ/2) M D^2  -> (M2), V4 = D^2
and (9.2) again gives kappa <= 1/(4 beta C_occ) and eps <= 1/(8 kappa4 beta^2 C_occ) - CONSTANTS.
So the conclusion of 9.2 stands verbatim; only its hypotheses change, and they change in the
direction of being weaker and more natural.

[REF-W1 2026-08-12 (fresh-session referee, report problem/CRUX9_wall_referee_20260812.md, D1) -
THE DISPLAY ABOVE CARRIES A FALSE IDENTITY; THE DELIVERED CONSTANT IS 16, NOT 8. The support claim
"Delta_L = 0 unless the geodesic (in one field or the other) meets L" - and with it the identities
E[Delta^2] = p m2, E[Delta^4] = p m4 and the A4 display's factor 1/2 - is FALSE: Delta vanishes
only off U_L UNION Uhat_L (MG2B Remark 4.4 states exactly this); on U_L^c the RESAMPLED field's
geodesic can still improve through the block, so Delta < 0 there with positive probability. The
damage is bounded: by symmetry (S) plus positive-part support (4.1), E[Delta^k] = 2 E[1(U)
((Delta^+)^k)] for k = 2, 4, so p m_k <= E[Delta^k] <= 2 p m_k - the identities are wrong by at
most a factor 2, and the DEFECT paragraph's kurtosis forcing survives as p >= 1/(4 kappa4). The
A2 line is unaffected (Sum p_L E[Delta^2|U] IS Sum E[1(U)Delta^2] by definition). The A4 line is
repaired without symmetry and without the 1/2: pointwise on U_L, ((Delta)^+)^4 <= Delta^4, so
    A4 = Sum E[1(U)((Delta)^+)^4] <= Sum_L p_L m4_L <= kappa4 beta^2 C_occ M D^2,
i.e. C2 = kappa4 beta^2 C_occ (not /2), and (9.2) gives
    eps <= 1/(16 kappa4 beta^2 C_occ)   - still a CONSTANT. Every downstream quote of the 1/(8...)
constant reads 1/(16...). Kappa's line is unchanged. MEASURED (same day, seed 20260812, 6000 reps,
13x13 U[1,2], exact Dijkstra): off-U negative increments at frequency 0.11-0.12 for corridor
blocks (the identity predicts zero), carrying 15-20 pct of E[Delta^2]; the factor-2 bracket held
at every block (ratios 1.18-1.25 for k=2, 1.16-1.22 for k=4); Lemma 4.3's one-sidedness exact in
all 18,000 resamples.]

WHAT (L3) COSTS IF IT IS NOT AVAILABLE. (L3) is a transversal-control statement (the geodesic meets
order M blocks, not many more), NOT a corollary of the refereed occupation lemma - that lemma bounds
the occupation N_ij WITHIN a block by (b/a)(n+W), which caps each term and not the count. The only
free count bound is the geodesic's length, Sum_L 1(U_L) <= (b/a) M n, a factor n worse; carrying it
gives V4 = n D^2 and eps <~ 1/n instead of a constant. So the reduction's three hypotheses split
cleanly: (L1') is the hard one (it is the wall, per 9.3), (L2') is a scale-free shape condition,
and (L3) is worth exactly one power of n.

THE HONEST LEDGER after this correction: the wall is (L1'), a per-block CONDITIONAL second-moment
comparison; the chaos strength is not where the difficulty lives; and two auxiliary conditions -
a shape cap and a count cap - are priced, one of them at a power of n. Nothing here proves anything
unconditional, and chi = 1/3 is where it was.

### 9.6 The two halves of this campaign share an input: (L3) is what the corner side's localization
### lemma proves (iter 126; conditional on that lemma's own referee, geometry check owed)

The corner route and the wall have been worked as separate programs all night. They are not.

(L3) asks that the expected number of blocks the geodesic meets be O(M). Decompose by transversal
position. If the scale-Mn geodesic is confined with high probability to a transversal window of
width w, then the blocks it can meet number (Mn/n) along the column times (w/W) across it, i.e.
M w/W, so C_occ = O(1) as soon as the block width W is chosen at the confinement scale, W ~ w.
The blocks outside the window contribute Sum_{far} P(U_L), which needs the deviation tail to beat
the number of far blocks - a polynomial count against the tail.

That is exactly the shape of the lemma drafted on the corner side tonight
(localization_tail_draft_iter106.md, all five gaps priced at iter 114):
    P(transversal deviation >= sigma W_r) <= C poly(r) exp(-c'' c_- sigma^2),
a polynomial prefactor beaten by a Gaussian tail in sigma, at every quantile the consumer uses.
Its (H-curv-LOWER) is the one-sided enclosing-ball condition - the SAME hypothesis, the same
constant c_-, that the corner side already carries.

CONSEQUENCE, if both survive their referees: the wall's three conditions are (L1') the hard
per-block second-moment comparison, (L2') a scale-free shape cap, and (L3) - which is no longer an
independent hypothesis but a corollary of an object this campaign has already drafted. Two of the
three then rest on inputs already on the ledger, and the wall narrows to (L1') alone.

WHAT IS OWED BEFORE THIS COUNTS. (i) The localization draft is unrefereed; it is first in the
queue behind the store verifier. (ii) The geometry must be checked, not asserted: choosing W at the
wandering scale changes the block aspect ratio, and the occupation lemma's (n+W) factor and the
engine's M-counting must be re-read under that choice - I have NOT done this, and it is exactly the
kind of bookkeeping that has bitten twice tonight. (iii) The far-block sum needs the tail applied at
the right scale (the deviation is measured at scale Mn while the blocks are at scale n), which is a
scale-matching step, not a quotation.

PRIOR ART INSIDE THIS DOCUMENT - found by searching before claiming novelty, and it narrows the
claim. Section 6b.1 already made the geometric half: with W = sqrt(nQ) at the conjectured exponents,
W is exactly the transversal wandering scale n^{2/3}, so a geodesic crossing a column "meets O(1)
blocks in that column". That IS (L3) with C_occ = O(1), observed months of iterations before this
subsection, and I did not remember it while writing the paragraphs above.

So what 9.6 adds is NOT the geometry but the SUPPLY: 6b.1 reads the block count off the conjectured
exponents, which is exactly what a program trying to PROVE those exponents may not assume. The
localization lemma would deliver the confinement as a conditional theorem - under (H-curv-LOWER),
with an explicit Gaussian-in-sigma tail beating the far-block count - rather than as a consequence
of the answer. That is the difference between reading (L3) off the conjecture and deriving it.

Recorded because it changes what the referee queue is FOR: the localization draft stops being a
corner-route convenience and becomes a shared input to the wall side as well.

### 9.7 The geometry check 9.6 said it owed, done (iter 127). It passes, it needs no new freedom,
### and it changes the block height by a polylog factor.

THREE QUESTIONS, from 9.6's debt list.

(a) IS "CHOOSE W AT THE CONFINEMENT SCALE" A NEW FREEDOM? No - the construction already does it.
The block height is W = sqrt(n Q). Under the KPZ relation xi = (1 + chi)/2, an envelope at the true
fluctuation scale Q = n^chi gives W = n^{(1+chi)/2} = n^xi - exactly the wandering scale. At the
other end, the Kesten envelope Q = n^{1/2} gives W = n^{3/4}, which is exactly the Newman-Piza
curvature-conditional wandering bound. So at BOTH parameter choices the paper's own block height
sits at the wandering scale. 9.6 was not invoking a new freedom; it was naming a property the
geometry already had.

(b) DOES THE OCCUPATION LEMMA'S (n+W) FACTOR HURT UNDER THAT CHOICE? No. W = n^{2/3} at the true
exponents and n^{3/4} at Kesten scale, both < n, so (n+W) <= 2n. The factor the campaign has been
carrying since iter 36 is, at every relevant parameter choice, just n. (The (L1')-(L3) route does not
use the occupation lemma at all; this answers the question for the routes that do.)

(c) DOES THE ENGINE'S M-COUNTING SURVIVE? Yes, and it improves the statement. Tile the scale-Mn
column with M slabs of length n. The geodesic restricted to one slab is, by subpath optimality, a
geodesic between its own endpoints at distance ~n, so its transversal spread inside that slab is a
BLOCK-SCALE question, not a top-scale one: it wanders O(n^xi) = O(W), meeting O(1) blocks there.
Summing, it meets O(M) blocks. (L3) therefore needs wandering control at scale n, applied M times -
NOT the global confinement of the scale-Mn geodesic. That is a materially weaker demand than 9.6
stated, and it is the scale at which the localization draft is cheapest.

THE PRICE, found by doing the union honestly. The per-slab confinement holds off an event of
probability C poly(n) exp(-c sigma^2); union over M slabs needs that below o(1), so
sigma^2 ~ (log M + log n)/c - polylog, well inside the lemma's range, but the confinement window is
then sigma W, not W. Blocks met per slab becomes O(sigma) = O(sqrt(log(Mn))) and C_occ picks up a
polylog, which would leave eps <~ 1/polylog rather than a constant.

THE FIX, and it is free: define the block height at sigma times the wandering scale,
W := sqrt(log(Mn)) * n^xi. Then blocks per slab is O(1) again, C_occ = O(1), eps stays constant, and
W is still far below n, so (b) is unaffected. The design consequence is one polylog factor in the
block height - worth recording because it is the kind of factor that is invisible until the union
bound is written out, and it is exactly what 9.6 could not see without doing this check.

REMAINING DEBT, unchanged and stated again: the slab-restricted geodesic has RANDOM endpoints on the
slab boundaries, so the localization lemma must be applied uniformly over boundary pairs - the same
caveat section 8.2 flagged for its blockwise fourth moment. One caveat, now in two places, and it is
the single technical step both routes need.
[REF-W1 C3, 2026-08-12: THIS DEBT IS PAID. The localization draft's G-f resolved it at iters
128-129 (deterministic boundary-pair union via the band cap; regime (ii) closed at top scale by the
tilt inclusion), and REF3 confirmed the totals with two corrections (tilt admissibility theta <=
2 delta M; honest threshold n_0 = (16/(c'' c_-)^2)(M^3/theta^4) log^2(C M n)). The paragraph above
is kept as the record of when it was open.]

### 9.8 What (L1') actually IS: the variance ratio, not a new condition (iter 137; the identity is
### unconditional, the conclusion is that the program is stuck exactly where section 2 said)

An unconditional fact, from exchangeability alone and nothing else. For any block L, since (X, X^L)
is an exchangeable pair,
    E[Delta_L^2] = 2 Var(X) - 2 Cov(X, X^L)  <=  4 Var(X),          X := X_{Mn},
and <= 2 Var(X) whenever the pair is positively correlated (which the FKG structure of FPP with
independent weights makes the expected case, though this document does not need it). No hypothesis,
no curvature, no chaos: every single-block resampling increment has second moment at most a constant
times the variance AT THE TOP SCALE.

CONSEQUENCE FOR (L1'). Conditioning on the touching event, m2_L := E[Delta_L^2 | U_L] satisfies
    m2_L  <=  4 Var(X_{Mn}) / p_L,     p_L := P(U_L),
so for the blocks the geodesic meets with probability of order one - the ones along the axis, which
are the blocks that carry the sums - (L1') holds with
    beta  =  O( Var(X_{Mn}) / Var(X_n) ).
That is: at the typical blocks, (L1') IS THE VARIANCE RATIO between consecutive scales. It is not an
exotic new hypothesis about local geometry; it asks that the variance not grow by more than a
constant factor per scale step.

WHY THIS DOES NOT CLOSE, stated immediately so the observation is not mistaken for progress. The
variance ratio at scale n is precisely what the halving CONCLUDES at scale n (Var(X_Mn) <= (1/2) M
Var(X_n)), so the natural move is induction: assume the halving through scale n, use it for (L1'),
prove the halving at Mn. The induction does not start. To use the ratio one needs an upper bound on
Var(X_Mn) AND a lower bound on Var(X_n); the induction supplies upper bounds only, and the only
unconditional lower bound is Newman-Piza's c log n. Substituting the free bounds gives
beta <~ Mn / log^2 n - the same n/log^2 factor section 2 found, arriving from a completely different
direction for the second time tonight (section 8.2 was the first).

WHAT IS GAINED. Not strength - clarity, and a closed loop in the map:
  - (L1') is demystified: it is the variance ratio at the typical blocks, so nobody should go
    looking for a clever local argument that avoids the variance lower bound. There is none; the
    condition IS the ratio.
  - The three-condition reduction of 9.5 now reads: (L1') = variance ratio (the wall),
    (L2') = a shape condition, (L3) = supplied by the localization lemma (9.6-9.7). Two of the
    three have a source; the third is the problem.
  - And the reason the program cannot bootstrap is now explicit: the engine's INPUT at a scale is
    its OUTPUT at that scale, and turning that circle into an induction requires the variance LOWER
    bound at the smaller scale - which is exactly "chi exists" and exactly what section 2 named the
    wall. Three independent routes into the same obstruction in one night is not progress toward
    solving it, but it is good evidence the obstruction is correctly located.

  [CROSS-NOTE, 2026-08-12 (REF-W1 session; expository, zero new mathematics - both inputs are
  refereed). MG2B's own proof of the t=1 equality (line 111) contains the identity
      E[Z_L^2] = E[((X^L - X)^+)^2] = E[ Var(X | w_{L^c}) ],
  the conditional-iid step plus Lemma 4.2. Summed, the engine's actual second-moment input (6d.1's
  A2^+) IS the total block-conditional variance: A2^+ = Sum_L E[Var(X | F_{L^c})]. So the
  positive-part form of (L1') is a per-block CONDITIONAL-VARIANCE cap, E[Var(X|F_{L^c})] <=
  beta p_L Var(X_n), and the halving's demand A2^+ <= C M D_n against Efron-Stein's free
  A2^+ >= Var(X_{Mn}) says the wall is exactly: Efron-Stein is ORDER-TIGHT for the block
  partition at every scale. At edge granularity BKS prove the opposite (superconcentration by
  log n); granularity is what reconciles the two. This renames the obstruction in the field's
  standard language - variance-ratio, conditional-variance cap, and no-block-superconcentration
  are the same statement - and is recorded so nobody hunts a "local" argument for (L1') that the
  renaming shows would be a variance lower bound in disguise. Known-in-kind to the field
  (Chatterjee's duality, per the iter-177 sweep); the campaign-internal content is only the
  equation of 9.8's ratio reading with MG2B line 111.]

  NUMERIC DISCONFIRMATION RUN (iter 137, scratchpad check_exchangeable_identity.py, seed 20260810,
  4000 replicates of 13x13 U[1,2] FPP with exact Dijkstra geodesics; the test looked for the input
  the claim FORBIDS - any instance with E[Delta^2] > 4 Var - across a centre block the geodesic
  usually crosses, a far-corner block it almost never does, and a large block it always does):
    - the bound E[Delta^2] <= 4 Var HELD everywhere, with room to spare: measured ratios 0.001,
      0.126 and 0.607. Nothing approached the bound.
    - Cov(X, X^L) came out POSITIVE in all three (0.40 to 0.58), so the stronger E[Delta^2] <= 2 Var
      form held too - the positive-association expectation is borne out on these instances.
    - the conditioning step m2 = E[Delta^2]/p was EXACT where it can be measured cleanly (relative
      difference 0.0000 at the always-touched block).
    - the identity E[Delta^2] = 2Var - 2Cov agreed to 1.5% at the well-conditioned block and drifted
      to ~30% at the small ones. That is the ESTIMATOR, not the algebra: the right-hand side is a
      difference of two nearly-equal quantities (Var ~ 0.58, Cov ~ 0.56), whose Monte-Carlo error at
      4000 samples is +-0.037 against a signal of 0.05, while the left-hand side is measured
      directly. The observed gaps sit inside that error.
  WORTH CARRYING FORWARD: the measured ratios are one to three orders of magnitude BELOW the bound,
  so the constant 4 in 9.8 is very loose in practice. Nothing in the argument depends on its size,
  but a sharper version would tighten beta correspondingly.

  SLAB-SPREAD CHECK on 9.7's count claim (iter 138, scratchpad check_slab_spread.py, seed
  20260810, exact Dijkstra geodesics, U[1,2]): the claim tested was that per-slab transversal
  spread is a BLOCK-scale quantity, so the blocks met per slab do not grow with the total
  distance. THE REFUTING OBSERVATION WOULD BE an upward drift of spread/s^{3/4} as r grows at
  fixed s; measured at s = 8, 16, 32 across r = 64, 128, 256 the relative change was +0.0%,
  -11.3%, +21.3% - flat within noise, no drift. Mean per-slab spreads were 0.3 to 1.4 lattice
  units, p95 at most 3.2, max 6.
  WHAT THIS DOES NOT SHOW, stated because the s-column invites a wrong read: the spread roughly
  DOUBLES when s doubles at these sizes (0.30, 0.60, 1.22 at s = 8, 16, 32), which taken at face
  value is linear growth rather than s^{3/4}, and linear growth would break the O(1)-blocks-per-slab
  claim. At spreads of zero to three lattice units that column cannot separate s^{3/4} from s^1 -
  it is dominated by discreteness, most slabs having spread 0 or 1 - so NO exponent is claimed
  from it and none should be read out of it. The test confirms the r-direction (what (L3) actually
  needs at fixed geometry) and is silent on the s-direction, which needs sizes far beyond what a
  laptop check reaches.

  WHAT 9.8 DOES NOT COVER, added iter 142 by re-reading my own hedge rather than waiting for a
  referee to find it. The identification "(L1') = the variance ratio" was stated for blocks met
  with probability of order one. For a FAR block the free bound reads m2_L <= 4 Var(X_Mn)/p_L,
  which blows up as p_L -> 0, so it identifies nothing there: at far blocks (L1') remains a
  hypothesis, not a consequence.
  Why the reduction survives that anyway - and why it is worth saying rather than hiding. The
  quantity the lemma actually consumes is A2 = Sum_L E[Delta_L^2] = Sum_L p_L m2_L, in which a far
  block contributes p_L m2_L, i.e. its conditional size DISCOUNTED by how rarely it is reached. So
  the sums are carried by the blocks with p_L of order one, which is exactly where the
  identification bites; the far blocks are cheap in A2 even when their conditional moment is large.
  What is NOT free is a uniform statement: bounding Sum_far p_L m2_L needs either (L1') assumed at
  those blocks too, or the touch-probability decay that (L3)'s source - the localization tail -
  supplies. That is a second, quieter place where the localization lemma is doing work for the wall
  side, and it belongs on the ledger next to 9.6.
  NET: 9.8 explains (L1') where the sums live and assumes it where they do not, and the assumption
  at the far blocks is exactly the kind of thing a tail bound retires. Referee: check whether the
  far-block remainder can be closed by the tail alone, with no (L1') hypothesis out there at all -
  if it can, the wall's surviving condition shrinks to a statement about the axis blocks only.

### 9.9 The far-block question of 9.8, answered - and it shrinks where (L1') is needed
### (iter 143; my own question from one iteration earlier, so read 9.9 with that in mind)

I said I would not answer this at five in the morning because I would answer it in my own favour.
Then I tried it, and the answer is affirmative, so what follows is written with the arithmetic
exposed and the strongest objection I could find addressed rather than omitted.

CLAIM. The far-block remainder of A2 closes on the TAIL ALONE, with no (L1') hypothesis out there -
using only the deterministic increment cap. Consequently (L1') is needed only on the blocks within
a polylog-widened band of the axis, a number of blocks depending on M but not on n.

THE ARITHMETIC. For any block, the increment is capped deterministically by the occupation lemma:
|Delta_L| <= (b - a_w)(b/a_w)(n + W) <= C n (since W <= n at both parameter choices, 9.7(b)), so
m2_L <= C^2 n^2 - crude, but free. For the reach probability, the localization tail at the top
scale R = Mn gives p_L <= C R exp(-c'' c_- (d_L/W_R)^2) with W_R = R^{3/4}. Blocks sit on levels
spaced W apart with ~M blocks per level, so, writing the far region as d >= sigma_0 W_R,
    Sum_far p_L m2_L  <~  C n^2 * M * M^{3/4} * (M n) * exp(-c'' c_- sigma_0^2)
                       ~  C' n^3 M^{7/4} exp(-c'' c_- sigma_0^2).
[REF-W1 D2: the four printed factors multiply to n^3 M^{11/4} - this display drops one M. The
QUANTILE below is nevertheless correct as printed, because the requirement divides by the target's
own M (n^3 M^{11/4} / (M D) restores M^{7/4}); the near-band count O(M^{7/4}) is also correct.
Re-derived in problem/CRUX9_wall_referee_20260812.md.]
The requirement is Sum_far <= C1 M D with D = Var(X_n) >= c log n, so it suffices that
    sigma_0^2  >=  (3 log n + (7/4) log M + O(1)) / (c'' c_-),
which is POLYLOG and sits far inside the lemma's range sigma^2 <= delta^2 sqrt(R). The Gaussian
tail beats the crude n^2 increment bound because the tail is superpolynomial in the quantile while
the increment cap is only polynomial in n.

WHERE (L1') SURVIVES. The near band is |d| <= sigma_0 W_R = sqrt(polylog) * (Mn)^{3/4}, which
contains (Mn)^{3/4}/W ~ M^{3/4} levels, hence O(M^{7/4}) blocks - a count set by the construction's
own branching parameter and INDEPENDENT OF n. So the wall's surviving hypothesis is needed on a
bounded family of blocks hugging the axis, not on the whole strip.

THE OBJECTION I HAD TO ANSWER. The tail step needs d_L inside the curvature window d <= delta R,
and for small delta there is a mid-band delta R < d <= R(b - a_w)/(2 a_w) that is neither in the
window nor deterministically dead. It is covered by containment, exactly as in G-c's mid-band
clause: reaching level d > delta R contains reaching level ceil(delta R), so Form A applies at
sigma^2 = delta^2 sqrt(R) - stretched-exponential in R, which beats the n^2 increment factor by a
wide margin. Beyond the band cap the event is impossible outright (G-b), contributing nothing.
[REF-W1 D3: stale range - REF3 (iter 162) narrowed Form A's range to sigma^2 <= (delta^2/4) sqrt(R)
(the integer-ceiling escape). The containment clause survives verbatim at the corrected range,
still stretched-exponential in sqrt(R); quote it with the /4.]

STATUS: derived by hand, unrefereed, and by construction the kind of result whose author wanted it
to be true. It does not touch (L1') itself - the wall is unchanged in KIND, only in EXTENT. Referee:
the level-counting M^{3/4}, the mid-band containment, and whether "O(M^{7/4}) blocks, independent of
n" is really what the sums require or whether some other term reintroduces the strip.

  FALSIFIER RUN ON 9.9 BEFORE IT LEFT THE FIRE (the strongest way the count could be an artifact).
  The load-bearing step is the level count, so it was re-derived independently rather than reused:
  near band half-width sigma_0 W_R with W_R = (Mn)^{3/4} and sigma_0 ~ sqrt(3 log n / c''c_-),
  divided by the block height W ~ n^{3/4} sqrt(log(Mn)) from 9.7, gives
      levels ~ 2 sqrt(3/(c''c_-)) * M^{3/4} * sqrt(log n)/sqrt(log(Mn))  ->  C M^{3/4},
  the polylogs cancelling rather than being dropped. Blocks per level is M because the column has
  length Mn and blocks have length n along it. Product C M^{7/4}, and M is FIXED in the engine
  (M >= M_0, the same constant at every rung), so the count really is independent of n.
  Second check, on direction rather than size: the requirement compares Sum_far against M*D with
  D = Var(X_n), and the argument uses the LOWER bound D >= c log n. Using the smallest admissible D
  makes the requirement HARDER, so the substitution is conservative - the result is not an artifact
  of a flattering choice at that step.
  Consistency check: the near band contains O(M^{7/4}) blocks while the geodesic meets O(M) of them
  (9.7), so the band comfortably contains the blocks that carry the sums, as it must.

### 9.10 The (M2) far remainder closes the same way, TWO powers of n later (added 2026-08-12 by the
### refereeing session - report problem/CRUX9_wall_referee_20260812.md, D4. [REF-W2 2026-08-12:
### independently counter-checked by a second re-deriving session, report
### problem/CRUX9_wall_referee_W2_20260812.md - the closure, the n^5 M^{11/4} far display and the
### sqrt(5 log n) radius all CONFIRMED line for line; this heading's original "one power of n
### later" was the one arithmetic slip (cap n^2->n^4, far sum n^3->n^5, quantile 3->5: two powers
### everywhere), likely an echo of 9.5's "(L3) is worth exactly one power of n", a different item.
### The debt "not independently checked" is now DISCHARGED.]

9.9 shrinks (L1') to the near band by closing A2's far remainder on the tail alone. That leaves an
unstated obligation: (L2') is also a per-block hypothesis, so (M2)'s far remainder needs its own
closure or the shrink applies to only half the reduction. It closes identically. A4's far summand
is E[1(U_L)((Delta_L)^+)^4], and on U_L the positive part is capped by the OLD geodesic's
occupation alone: (Delta_L)^+ <= (b - a_w)(b/a_w)(n + W) <= C n, so m4-type mass is at most
C^4 n^4 per block - two powers of n above the m2 cap - and
    Sum_far p_L E[((Delta)^+)^4 | U_L]  <=  C' n^5 M^{11/4} exp(-c'' c_- sigma_0^2).
Against the requirement Sum_far <= C2 M D^2 with D >= c log n, it suffices that
    sigma_0^2  >=  (5 log n + (7/4) log M + O(1)) / (c'' c_-)     [9.9's leading 3 becomes 5],
still polylog, still far inside Form A's corrected range (delta^2/4) sqrt(R). CONSEQUENCE: with
sigma_0 enlarged from sqrt(3 log n) to sqrt(5 log n) in the leading term, BOTH (L1') and (L2') are
needed only on the same O(M^{7/4}) axis-hugging blocks, and the far remainders of (M1) and (M2)
close on the localization tail plus the deterministic occupation caps.

CONDITIONALITY, stated at the claim rather than implied: the far-band closures and (L3) all consume
the localization tail, hence (H-curv-LOWER) c_-. The extent-shrink of the wall is a c_--conditional
statement. Only the reduction arithmetic itself ((L1')+(L2')+(L3) => halving at constant chaos
strength, post-D1 constant 1/(16 kappa4 beta^2 C_occ)) is hypothesis-free.

SCOPE, added 2026-08-12 (loop fire 8), CORRECTED IN PLACE by [REF-W2 2026-08-12] (the original
version inverted which constraint binds): this closure and 9.9's both apply Form A at the top
scale R = Mn, where TWO constraints live: (i) REF3's emptiness floor r_0 (range empty below it;
measured 1e5.5 to 1e14 depending on constants); (ii) the needed quantile must FIT the corrected
sigma-range - (delta^2/4) sqrt(Mn) >= (q log n + (7/4) log M + O(1)) / (c'' c_-), with q = 3 for
9.9's (M1) closure and q = 5 for 9.10's (M2) closure (mid-band analogues 13/4 resp. 21/4).
Constraint (ii) BINDS, not the floor: its coefficient exceeds the floor's governing clause
(delta^2 sqrt(r) >= (2/(c'' c_-)) log(12 C1 rho r), REF3 176) by the factor 2q REGARDLESS of the
constants, so the in-range threshold r_1 sits roughly (2q)^2 above r_0 - measured 40-60x (q=3)
and 100-160x (q=5) across REF3's three constant sets; e.g. the friendly set gives r_0 ~ 1.3e5 but
r_1(q=5) ~ 2e7. At Mn = r_0 the needed quantile exceeds the range top by ~10x and endpoint
containment reproduces the same r_1, so there is no rescue below it. The far-band closures hold
for Mn >= r_1, NOT Mn >= r_0 as first printed. Still harmless for the asymptotic statement;
printed so the next reader does not discover it at assembly time. (The companion phrase at
localization_lemma_STATEMENT_iter130.md:101-103, "both inside Form A's corrected range", is true
asymptotically only - same caveat.)
