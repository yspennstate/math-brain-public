# Independent referee of the sandwich note's SURVIVING core — checklist + first executed item
# 2026-08-12 ~15:0x, pass 77. The self-referee (a separate session,
# wall_two_sided_sandwich_SELF_REFEREE_20260812.md) retracted THE ESCAPE and said an
# independent referee is still owed for what SURVIVES. I am independent of 57aea2b1 for this
# note. One item per fire, by hand, warn/throttle-compatible. chi = 1/3 UNMOVED.

## What survives (per the self-referee) and therefore what must be checked
(a) the SANDWICH FRAMING — chi as a two-legged fixed point, s_block pinned to the global
    std-dev scale from both sides;
(b) the lower leg's content identified as restricted-min anticoncentration (Thread B);
(c) the self-referee's OWN break of the escape (a retraction is a claim too — it gets
    refereed like anything else).

## Checklist
- [x] 1. THE BREAK'S PREMISES (executed this fire — see finding below). Verify the
      inequality chain at self-referee lines 18-31: monotonicity premise, conjectural
      n^{2chi} step, and whether the conclusion survives on unconditional facts alone.
- [x] 2. Note line 28 / LOG 409 quote (executed fire 78). FAITHFUL: the note (its lines
      31-34 and 90; the self-referee's "line 28" pointer is off by a few lines, cosmetic)
      quotes LOG iteration 66 VERBATIM — "What is unconditionally known is only
      Var >= c log n." Note-to-record custody is clean. But the record itself is
      CITATION-THIN: LOG 66 asserts the bound bare — no external reference, no weight
      class, no direction conditions. The standard source is Newman-Piza 1995 (planar,
      with real conditions: F(0) < p_c and direction relative to the flat edge / curvature
      caveats); the campaign has never transcribed that exact statement. MATERIALITY:
      currently harmless-by-direction — every present use of c log n is adversarial (it is
      "the best L is tiny", and if conditions failed L would be SMALLER — Kesten's constant
      — making certified beta LARGER and the item-1 break stronger). FLAG for the future:
      any POSITIVE use of L >= c log n as an ingredient must first pin the NP95 statement
      and check its conditions against the campaign's weight class. Until then the record
      should say "folklore/NP95-shaped, untranscribed".
      [DISCHARGED fire 85: exact transcription now at problem/NP95_TRANSCRIPTION_20260812.md
      — NP95 Theorem 2 verbatim from the paper (JSTOR PDF read page-by-page), with the
      direction-uniformity note, the atom condition (2.12)/(2.13) as the real hypothesis,
      the curvature-belongs-to-Thm-6/7 distinction, the survey-numbering trap (ADH 3.7 =
      NP95 Thm 2), and the unread-Correction flag.]
- [x] 3. Sandwich framing vs sources (executed fire 79). THREAD B: FAITHFUL — the note's
      paraphrase is correctly scoped to the environment-revelation channel, the "three
      faces" are the D-attempt's enumerated (1)(2)(3) at its ~105-120, and "restricted
      minima do not concentrate too fast" is near-verbatim (line 118). THREAD A: substance
      faithful to the CORRECTED 3b (alpha = chi within the hypothesis set; the note carries
      "conditionally"), but the label "(3b + 9.8, refereed)" OVERSTATES 3b: all REF-W1/W2
      tags live in the 9.x wall-reduction sections, 3b carries none, and 3b's own header
      says its C1 dependency's referee is pending (iter-68's challenge-resolution is
      internal, not an external referee). ANNOTATED IN PLACE in the note ([REF-CORE item 3]
      bracket after the Thread A paragraph): 9.8's identity refereed; 3b flagged-standing,
      conditional, disjointness conditional on chi <= 0.4142. Framing substance unaffected.
- [x] 4. Thread B identification (executed fire 80, full D-attempt re-read). FAITHFUL, and
      the compression is accurate: all three faces (martingale transmission → ensemble
      corridor-pair collision → Q(F_i, δ) of a min over waypoint completions) terminate at
      anticoncentration of RESTRICTED MINIMA, with the exact objects being S_{C_i} (min
      over a corridor's paths) and one layer up F_i (min over ~W² waypoint-anchored
      completions), at block scale W — and the reduction endpoint is explicitly
      renormalization-shaped (D-attempt ~121-122: the W-box object "is the same problem at
      scale W"). The framing's "block/corridor passage time must not concentrate too fast"
      preserves the self-similar law (anchored methods penetrate exactly one layer; Elboim
      = the globally-anchored layer, no further) by citation rather than restatement — no
      overclaim. STEELMAN-3 UPGRADED from "plausibly weakens" to NECESSARILY: the certified
      competitiveness tolerance is δ ~ sqrt(U(j)) (only "within sqrt(U)" is certifiable
      when all you hold is Var <= U), and the Levy concentration function Q(X, λ) =
      sup_a P(X ∈ [a, a+λ]) is nondecreasing in λ BY DEFINITION — so the lower leg's
      required premise Q(F, c·sqrt(U(j))) small is monotonically HARDER as U(j) loosens.
      Both legs therefore degrade with a loosening window — the self-referee's disposition
      ("BOTH legs entangled with the window") now has a one-line proof on the lower side
      to match item 1's arithmetic on the upper side. chi = 1/3 unmoved.
- [x] 5. Maintain-up vs contract-down (executed fire 81). CONFIRMED AND LOCATED — both
      readings sit in the Addendum's ESCAPE paragraph itself, two lines apart: "asks only
      that R stay BOUNDED under the joint step" (maintain-up, inductive hypothesis R <= K)
      vs "R(j+1) <= R(j)/(contraction of BOTH legs)... R is now a CONTRACTED quantity"
      (contract-down), with the bracketed CORRECTION's R(0) ~ n/log^2 n floor arithmetic
      (q <~ 1/2 per step over only ~log_2 n steps) purely contract-down. The self-referee's
      steelman 2 stands. WHICH READING THE SURVIVING FRAMING NEEDS: NEITHER — with the
      escape retracted, the surviving core (sandwich fixed point + Thread B naming) is
      induction-agnostic; both readings live only inside the retracted Addendum.
      SHARPER YIELD, maintain-up horn's missing ingredient NAMED: to convert R(j) <= K into
      the halving's certified beta = O(1) one needs a pre-halving upper bound at the next
      scale of the form U_raw(j+1) <= A*U(j) — an unconditional variance-DOUBLING
      (regularity) inequality Var(X_{2n}) <= A*Var(X_n). Subadditivity does NOT supply it:
      X_{2n} <= X_n + X'_n is pointwise domination, and pointwise domination compares no
      variances (a.s.-smaller variables can fluctuate more). Not in the campaign record and
      I know of no proof; same unproven-regularity family as item 1's monotonicity gap.
      Without it, certified beta falls back to the global window ~ n/log^2 n (item 1).
      So: contract-down fails on the polynomial floor vs log-many steps (the note's own
      correction); maintain-up fails on unproven cross-scale variance regularity. Both
      horns now carry NAMED missing ingredients.

## CLOSING VERDICT (fire 81, all five items executed)
The independent referee the self-referee said was owed is now DONE. The surviving core
STANDS: (a) the sandwich framing is faithful to both sources (item 3, with one label
overstatement annotated in place — 3b is flagged-standing, not refereed); (b) Thread B's
identification is faithful and renormalization-shaped (item 4); (c) the self-referee's
break/retraction of THE ESCAPE stands and is now STRONGER — it rests only on unconditional
premises (item 1: certified window [c log n, BKS n/log n] gives beta_cert ~ n/log^2 n; no
monotonicity assumption needed), the citation custody is clean with one thin spot flagged
(item 2: NP95 untranscribed, currently harmless-by-direction), the lower leg's
window-degradation is proved not plausible (item 4: Q monotone in width, tolerance ~
sqrt(U)), and both induction readings fail for separately-named reasons (item 5: polynomial
floor vs log steps; missing variance-doubling regularity). NEW NAMEABLE SUB-PROBLEMS this
referee surfaced, weaker than the wall yet still open, worth a literature pass each:
(i) unconditional variance monotonicity Var(X_{n+1}) >= Var(X_n) — item 1;
(ii) unconditional variance doubling Var(X_{2n}) <= A Var(X_n) — item 5.
Either would be a real (if small) unconditional regularity result about planar FPP variance;
neither moves chi by itself. chi = 1/3 exactly where it was.

[LITERATURE PASS, fire 82 (2026-08-12 ~15:5x), one bounded web sweep each:
(i) OPEN, decisively — even the MEAN's monotonicity is open for lattice FPP: arXiv 1202.2665
("Monotonicity in first-passage percolation") proves E[T] eventually non-decreasing only
CONDITIONALLY (weight support with S_+ <= 2 S_-); the general case is stated as not known.
If the mean's version is open, the variance's version is at least as open; expect it hard.
(ii) NOT FOUND under two natural phrasings (variance comparison across scales; doubling/
regularity of Var in n) — searches surface only the standard sublinear-variance corpus (BKS
math/0203262, DHS 1306.1197, BSS 2604.01214), no cross-scale Var(X_{2n}) vs Var(X_n) result.
One bounded pass, absence-of-evidence only: recorded as PRESUMED OPEN AND UNNAMED, not
proven absent. Consequence for the record: both regularity gaps stay standing assumptions
NOBODY may consume unconditionally; any future bootstrap step that needs either must cite
this bracket and treat it as a hypothesis.]

[ASYMMETRY, fire 89: the two sub-problems are not siblings. DOUBLING with constant A is
WALL-EQUIVALENT — it would certify beta = O(1) for maintain-up (so it is at least as hard as
the (L1') ratio wall), and the natural routes (Efron-Stein/influences: A ~ n/log n;
subadditivity: no variance content) cap exactly at the global window ratio. Full half-page:
problem/DOUBLING_IS_NOT_A_SIDE_DOOR_20260812.md. MONOTONICITY stays the genuinely separate,
possibly softer target.]

## Item 1 EXECUTED: the break survives, on FEWER and WEAKER premises than it used
The self-referee's chain (its lines 18-27) is:
  (i)  "FPP variance is INCREASING in scale, so U(j+1) >= Var(X_{n_j})", then
  (ii) beta = U(j+1)/L(j) >= Var(X_{n_j})/L(j) >~ n^{2chi}/log n >> 1.

Two soft spots, neither fatal, both removable:

(i) VARIANCE MONOTONICITY IS NOT A CITABLE FACT. Var(X_n) increasing in n is plausible and
    surely true, but the campaign record contains no proof and I know of none in the
    literature (subadditivity machinery gives means, not variances). A retraction should
    not rest on an unproven premise. It does not need to: U(j+1) is a certified upper bound
    at ITS OWN scale, so U(j+1) >= Var(X_{n_{j+1}}) by the meaning of "upper bound" — no
    cross-scale comparison required. Compare directly to L(j) and the argument proceeds
    identically.

(ii) THE n^{2chi} STEP IS CONDITIONAL ON THE CONJECTURE. Var(X_n) ~ n^{2chi} is the thing
    the whole campaign is trying to prove; the break as written is "conditional on chi > 0."
    Unconditionally we know more useful things in BOTH directions, and they are already in
    the campaign record: L(j) >= c log n_j (LOG 409) and the sublinear upper bound
    U <= C n/log n (BKS / Damron-Hanson-Sosoe class). So the best CERTIFIABLE window today
    is [c log n, C n/log n], and the best certifiable ratio is
        beta_cert = U(j+1)/L(j) ~ (n_{j+1}/log n_{j+1}) / (c log n_j) ~ n/log^2 n  >> 1.
    The halving's premise consumes the CERTIFIED beta, not the true one — that is the
    self-referee's own point 2, and it is the right point. Stated this way the break needs
    no conjecture at all: from today's certifiable window, certified beta is polynomially
    large, the halving's O(1) premise fails at the first step, and the two-sided carry never
    improves L (that is precisely Thread B's unproven job). Circularity confirmed,
    unconditionally.

VERDICT on (c): the retraction STANDS, and after this repair it is STRONGER — it now rests
only on (1) the definition of a certified upper bound, (2) the campaign's recorded
unconditional window, (3) the refereed halving's beta = O(1) premise. I looked for a way the
original monotonicity premise could hide a real gap (e.g. a certified-U sequence that dips
below an earlier scale's variance): even if such a dip occurred it would not rescue the
escape, because the comparison that matters is same-scale U over the log-window L, which is
polynomially large regardless. Nothing in the retraction moves.

Remaining exposure, named plainly: if someone exhibits an UNCONDITIONAL certified lower
bound materially above c log n, beta_cert shrinks and this arithmetic must be redone. That
is not a flaw in the break — lifting L IS the open problem (the self-referee's closing line),
and any such lift changes the whole landscape, not just this note.

[ROBUSTNESS ADDENDUM, fire 100: the exposure is ONE-SIDED — the arithmetic is entirely
L-limited. No improvement of the UPPER certificate changes the conclusion: with the BSS
beta_cert ~ n/log^{2+delta} n — still polynomial; with a full polynomial improvement
(U ~ n^{1-eps}), beta_cert ~ n^{1-eps}/log n — still polynomial; and even a PERFECT upper
certificate (U = true Var ~ n^{2chi}) leaves beta_cert ~ n^{2chi}/log n >> 1. beta = O(1)
requires the window to CLOSE (U within a constant of L), which no upper-side progress
achieves while L sits at c log n. So the does-not-start conclusion survives every upper-bound
advance, present or future; the ONLY thing that redoes this arithmetic is lifting L. Watch
the lower-bound literature, not the upper.]

## Standing
Items 2-5 pend, one per fire, by hand. Nothing here moves chi; this is the record being
made trustworthy at the same standard as the wall reduction (REF-W1/W2 arc).
