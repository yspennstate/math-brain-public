# Referee report: CRUX sections 9.5-9.9 (the wall's (L1')/(L2')/(L3) reduction and the far-block
# closure). Fresh-session re-derivation, 2026-08-12.

PROVENANCE AND INDEPENDENCE. Written by a session that authored none of the material under review
(campaign session 9d110555 wrote 9.5-9.9 at iters 125-143; this is session 17556890, two days
later, working from the documents alone). Method: every load-bearing step re-derived from the
consumed statements - MG2B_framework_lemma_draft.md (Theorem 8.1, Definition 3.3, Lemma 4.3,
(M1)/(M2)/(9.2), Remark 8.3) and localization_tail_draft_iter106.md (Form A post-REF3, G-b, G-f)
- not checked for plausibility against the prose. The author's own logged reason for wanting this
referee (LOG line 931: 9.9 is "exactly the result whose author wanted it true") was treated as the
attack brief.

VERDICT IN ONE PARAGRAPH. The reduction SURVIVES: (L1') + (L2') + (L3) imply (M1) + (M2) with
V = D, V4 = D^2, and constant-strength chaos then delivers the halving, with the difficulty
concentrated in (L1') exactly as 9.3/9.8 say. The far-block closure of 9.9 also survives, and with
it the shrink of (L1') to O(M^{7/4}) axis blocks. But the chain as printed carries one FALSE
INTERMEDIATE IDENTITY whose repair costs a factor 2 in the delivered chaos threshold (1/8 -> 1/16),
one M-exponent display error that happens not to propagate, one stale pre-referee range quotation,
and one unstated obligation ((M2)'s far remainder) that this report closes in kind. Defects D1-D6
below, confirmations C1-C4, every one with its derivation.

--------------------------------------------------------------------------------------------------
## D1 (9.5, DEFECT, repaired; the constant halves). The conditional-moment identities are false as
## printed; the implication survives without them at C2 = kappa4 beta^2 C_occ, eps <= 1/(16 kappa4
## beta^2 C_occ).

THE DEFECT. 9.5 writes: "Since Delta_L = 0 unless the geodesic (in one field or the other) meets L,
E[Delta^2] = p m2, E[Delta^4] = p m4" with p := P(U_L) and m2, m4 the moments conditioned on U_L.
The premise names the event U_L union Uhat_L (both fields' geodesics), and the displays then charge
only U_L. Delta_L does NOT vanish off U_L: on U_L^c the old geodesic misses L, so X^Lambda <= X
(Lemma 4.3), but the resampled field's geodesic may pass through L and improve, giving Delta_L < 0
with positive probability. MG2B's own Remark 4.4 states the correct support: X = X^Lambda off
U union Uhat. So E[Delta^4] = E[1(U)Delta^4] + E[1(U^c)(Delta^-)^4] > p m4 whenever off-U drops
occur, and the printed identities are false. The same false identity underlies the (1/2) in
"A4 = (1/2) Sum p_L E[Delta^4|U]".

WHY THE CHAIN SURVIVES, one line. A4's summand is E[1(U_L)((Delta_L)^+)^4], and pointwise on U_L,
((Delta)^+)^4 <= Delta^4. Hence
    A4  =  Sum_L E[1(U_L)((Delta_L)^+)^4]  <=  Sum_L E[1(U_L) Delta_L^4]  =  Sum_L p_L m4_L,
with no symmetry, no support claim, and no factor 1/2. (The exact route through symmetry lands in
the same place: A4 = Sum E[((Delta)^+)^4] by Lemma 4.3, E[Delta^4] <= 2 E[1(U)Delta^4] because the
negative part's fourth moment equals the positive part's by exchangeability and the positive part
is supported on U; either way A4 <= Sum p_L m4_L and the 1/2 is not recoverable.)

THE REPAIRED ARITHMETIC. Under (L1'), (L2'), (L3) exactly as stated in 9.5:
    A2  =  Sum_L p_L m2_L        <=  beta D Sum_L p_L               <=  beta C_occ M D
    A4  <=  Sum_L p_L m4_L      <=  kappa4 Sum_L p_L m2_L^2        <=  kappa4 beta^2 C_occ M D^2
so (M1) holds with V = D, C1 = beta C_occ, and (M2) with V4 = D^2, C2 = kappa4 beta^2 C_occ - twice
the printed C2. Feeding (9.2): kappa <= 1/(4 beta C_occ) (unchanged) and
    eps  <=  1 / (16 kappa4 beta^2 C_occ)       [printed: 1/(8 ...); the 8 is the defect's residue].
STILL A CONSTANT, independent of n, so 9.5's conclusion - constant-strength chaos suffices under
the three conditions - is intact. Every downstream quotation of "1/(8 kappa4 beta^2 C_occ)" should
read 16. (A2's line was never affected: A2 = Sum p_L m2_L is the definition of conditional
expectation, no support claim needed. The A2 >= (1/2) Sum E[Delta^2] comparison in 9.1 similarly
survives, since it runs through the positive part on U only.)

NOTE ON (L2')'s SHAPE. If one prefers the printed constant 8, restate (L2') on the positive part:
E[((Delta)^+)^4 | U] <= (kappa4/2)(E[Delta^2|U])^2. That is a strictly weaker hypothesis than (L2')
by the same pointwise comparison, so nothing is lost by keeping (L2') as printed and taking 16.

REFINEMENT, so the defect is priced and not just named: the false identities are two-sided up to a
factor 2. By symmetry (S) and positive-part support (Lemma 4.3), E[Delta^2] = 2 E[1(U)((Delta)^+)^2]
and E[Delta^4] = 2 E[1(U)((Delta)^+)^4], so p m_k <= E[Delta^k] <= 2 p m_k for k = 2, 4. The 9.5
DEFECT paragraph's kurtosis-forcing argument therefore SURVIVES with constant 4 (an unconditional
kurtosis cap kappa4 forces p >= 1/(4 kappa4) at every block), and the printed identities are wrong
by at most a factor 2 - which is exactly the factor the repaired constant absorbs.

NUMERIC WITNESS (2026-08-12, scratchpad check_d1_support_identity.py, seed 20260812, 6000
replicates, 13x13 U[1,2] bond FPP, exact Dijkstra, three 12-edge blocks, results
d1_witness_results.json). The identity's prediction P(Delta != 0, U^c) = 0 is REFUTED: off-U
negative drops at frequency 0.1185 / 0.1075 / 0.0157 (center-axis / near-off-axis / far-corner
block), carrying 15-20 percent of E[Delta^2]. The factor-2 bracket held everywhere:
E[Delta^2]/(p m2) = 1.18-1.25, E[Delta^4]/(p m4) = 1.16-1.22, all inside [1, 2]. Harness guard:
Lemma 4.3's pointwise one-sidedness (Delta <= 0 on U^c) held with ZERO violations in 18,000
resamples - which also rules out a touched-detection artifact, since a broken U would leak
positive Deltas. Bookkeeping regime only, per the campaign's threshold law - but a support
identity is algebra, and algebra has no regime.

## D2 (9.9, DISPLAY ERROR, does not propagate). The far-sum display drops one factor of M.

The display reads "Sum_far p_L m2_L <~ C n^2 * M * M^{3/4} * (M n) * exp(-c'' c_- sigma_0^2)
~ C' n^3 M^{7/4} exp(...)". The four listed factors multiply to n^3 M^{11/4}: m2-cap n^2, blocks
per level M, effective Gaussian level count M^{3/4}, Form A prefactor Mn. The printed M^{7/4}
loses a factor M. RE-DERIVED: with levels spaced W apart, blocks of length n along a column of
length Mn (M per level), p_L <= 12 C1 (b/a_w) R exp(-c'' c_- (d_L/W_R)^2) at R = Mn, and the
level sum collapsed to its Gaussian width W_R/W -> C M^{3/4} (the polylogs cancel as 9.9's own
falsifier computes),
    Sum_far p_L m2_L  <=  C' n^3 M^{11/4} exp(-c'' c_- sigma_0^2).
WHY THE CONCLUSION IS NEVERTHELESS CORRECT: the requirement is Sum_far <= C1 M D, and dividing by
the target's M returns n^3 M^{7/4}/D, so the printed quantile
    sigma_0^2 >= (3 log n + (7/4) log M + O(1)) / (c'' c_-)
is right (the -log D term only helps, absorbed in O(1)). The near-band count O(M^{7/4}) blocks -
band levels ~ C M^{3/4} times M per level - was re-derived and is CORRECT as printed; 9.9's
falsifier checked exactly that number and the requirement line, which is why the display slip
survived. Repair: one exponent in one display.

## D3 (9.9, STALE RANGE QUOTATION). "Form A applies at sigma^2 = delta^2 sqrt(R)" is the
## pre-referee range; REF3 narrowed it to (delta^2/4) sqrt(R) (the ceiling escape).

The mid-band containment clause survives verbatim at the corrected range - the containment event is
bounded at sigma^2 = (delta^2/4) sqrt(R), still stretched-exponential in sqrt(R), still beating the
polynomial increment factor by an unbounded margin. No conclusion moves. But the quotation should
carry the /4, and the same staleness infects the statement page (D5), which is where 9.9 likely
read it.

## D4 (9.9, GAP, closed here in kind). The far-band closure is stated for A2 only; (M2) needs its
## own far remainder closed, and it closes the same way TWO powers of n later. [REF-W2 2026-08-12:
## this heading originally said "one power"; the body's own arithmetic (cap n^2->n^4, far sum
## n^3->n^5, quantile 3->5) says two, confirmed by independent re-derivation - see
## CRUX9_wall_referee_W2_20260812.md, repairs A-R1/A-R2.]

9.9 shrinks (L1') to the near band by closing Sum_far p_L m2_L on the tail alone. The same shrink
for (L2') requires closing A4's far remainder, which 9.9 never mentions. It closes identically:
the deterministic cap gives m4_L <= C^4 n^4 (fourth power of the occupation bound, both geodesics
covered by the occupation lemma exactly as in the m2 case), so
    Sum_far p_L m4_L  <=  C' n^5 M^{11/4} exp(-c'' c_- sigma_0^2),
and the requirement Sum_far p_L m4_L <= C2 M D^2 with D >= c log n holds once
    sigma_0^2  >=  (5 log n + (7/4) log M + O(1)) / (c'' c_-),
still polylog, still far inside Form A's corrected range. CONSEQUENCE, stated as the corrected
form of 9.9's conclusion: with sigma_0 enlarged from sqrt(3 log n) to sqrt(5 log n) in the leading
term, BOTH (L1') and (L2') are needed only on the same O(M^{7/4}) axis-hugging blocks, and the far
remainders of (M1) and (M2) close on the localization tail plus the deterministic caps alone.
CONDITIONALITY, which 9.9 leaves implicit at the claim and should not: the far-band closure and
(L3) both consume the localization tail, hence (H-curv-LOWER) c_-. The extent-shrink of the wall
is a c_--conditional statement; only the reduction of D1's arithmetic is hypothesis-free.

## D5 (STATEMENT PAGE, STALE - documentation defect with consumers). The localization statement
## page still prints the pre-REF3 object.

localization_lemma_STATEMENT_iter130.md carries: Form A prefactor 18 C1 (b/a_w) r (REF3: 12);
range sigma^2 <= delta^2 sqrt(r) (REF3: delta^2/4, the integer-ceiling escape); no validity floor
(REF3: range EMPTY below r_0, measured 1e5.5-1e14); no required wlogs (REF3: delta <= min(1,
3 C2/c_-), c1 <= 3 sqrt(2 + b/a_w)/C3); status line "NOT REFEREED" (REF3 returned iter 162). The
page's own authority rule covers it - the draft outranks it - but the merged corner note's
provenance table sends readers to this page as the statement of record, and 9.9 quotes its stale
range (D3). Synced in place this session with [SYNC 2026-08-12] tags; the draft remains the
authority.

## D6 (9.7, FLAG, no defect found). The polylog block-height inflation W := sqrt(log(Mn)) n^xi is
## a change to the engine's partition; its couplings were walked once and nothing breaks.

MG2B's H2 accepts any finite-block edge partition, and (M1)/(M2)/(CH) are partition-dependent
hypotheses, so no refereed statement is violated by the inflation. Walked here: the occupation
factor (n + W) <= 2n survives (W <= n at both parameter endpoints, unchanged by sqrt(log));
Remark 8.3's far-block alternative is superseded by 9.9's route on the same family; the corner
side's h = n^beta W_n uses its own scale and shares no symbol with the wall's W after iter 127.
Recorded so the next reader does not re-walk it. What remains genuinely owed if this chain is ever
assembled into a theorem statement: one paragraph fixing the partition once, with W's polylog
printed, since (L1')/(L2') are stated per block and the blocks must be THESE blocks.

--------------------------------------------------------------------------------------------------
## C1 (9.8 CONFIRMED). Exchangeability identity and its conditional consequence re-derived exactly.

E[Delta^2] = 2 E[X^2] - 2 E[X X^L] = 2 Var(X) - 2 Cov(X, X^L) for an exchangeable pair; Cauchy-
Schwarz gives |Cov| <= Var, hence E[Delta^2] <= 4 Var(X_{Mn}) with no hypothesis, and <= 2 Var
under positive correlation. m2_L <= E[Delta^2]/p_L is the unconditional-to-conditional step and is
an inequality (correct as used; the equality claim it replaces was D1's defect, which 9.8 does not
repeat - it works with E[Delta^2] >= E[1(U)Delta^2] = p m2, valid). The far-block scope hedge
added at iter 142 (the identification says nothing where p_L -> 0) is correct and is exactly what
9.9 closes. The "beta = O(Var(X_Mn)/Var(X_n)) at typical blocks" reading survives with the note
that "order one" means order one in n at fixed M; the constant carries M-dependence through p_L
(an axis block at fixed longitudinal position has p_L of order M^{-3/4} by the top-scale spread),
which is absorbed at fixed M and should be said when beta's M-dependence ever matters.

## C2 (9.7 CONFIRMED, with the implicit chord-tilt accounting made explicit). The three geometry
## answers hold.

(a) W = sqrt(n Q) sits at the wandering scale at both parameter endpoints: algebra re-run,
(1+chi)/2 = xi under the KPZ relation and (1+1/2)/2 = 3/4 at Kesten scale against Newman-Piza. (b)
(n + W) <= 2n at both. (c) The slab decomposition: per-slab pieces are geodesics by subpath
optimality; blocks met per slab <= 1 + (|h_{j+1} - h_j| + 2 dev_j)/W, where the CHORD TILT term
|h_{j+1} - h_j| - which the printed text folds into "spread" without saying so - is itself bounded
by the piece's own deviation-plus-endpoints and so is controlled by the SAME per-slab localization
event as dev_j; the union over M slabs and boundary pairs costs the log that the sqrt(log(Mn))
inflation of W absorbs. Blocks per slab O(1) w.h.p., C_occ = O(1). Confirmed.

## C3 (9.6/9.7's DEBT is PAID; the printed debt paragraph is stale). G-f covers the wall-side
## consumer.

CRUX 9.7 ends: "the localization lemma must be applied uniformly over boundary pairs ... the
single technical step both routes need" - written iter 127 as an open debt. The draft resolved
G-f at iters 128-129 (union over DETERMINISTIC boundary-pair candidates via the band cap; regime
(ii) closed at top scale by the tilt inclusion {slab tilt >= theta n} subset {global deviation >=
theta n/2}), and REF3 confirmed the totals with two corrections (tilt admissibility theta <=
2 delta M; honest threshold n_0 = (16/(c'' c_-)^2)(M^3/theta^4) log^2(C M n)). The wall-side
application at block scale is exactly regime coverage the draft states ("the caveat both
consumers carried"). CRUX 9.7's debt paragraph should carry a one-line cross-note; annotated this
session.

## C4 (9.5's (L3)-absence pricing CONFIRMED). Sum_L 1(U_L) <= (b/a) M n re-derived (each touched
## block holds a geodesic edge; |gamma| <= (b/a) M n by weight comparison; H2 partition makes the
## count injective), and carrying it through (9.2) gives eps <~ 1/n as printed: (L3) is worth
## exactly one power of n.

--------------------------------------------------------------------------------------------------
## The wall after this referee pass, one paragraph for the ledger.

Unconditional and hypothesis-free: (L1') + (L2') + (L3) imply the halving inputs (M1) + (M2) at
V = D, V4 = D^2 with C1 = beta C_occ, C2 = kappa4 beta^2 C_occ, so constant-strength chaos
eps <= 1/(16 kappa4 beta^2 C_occ) runs the engine - the difficulty lives in (L1'), which at the
blocks that carry the sums IS the inter-scale variance ratio (9.8), unprovable today beyond
Newman-Piza's log. [REF-W2 A-R3 note, 2026-08-12: the bare eps <= 1/(16 kappa4 beta^2 C_occ) is
exact for the ALL-BLOCKS hypothesis form above; when the far-band closures substitute for
(L1')/(L2') off the near band, the composed constants read C1 = beta C_occ + O(1),
C2 = kappa4 beta^2 C_occ + O(1) - the two forms are juxtaposed in this paragraph without that
distinction, so it is printed here once.] Conditional on (H-curv-LOWER) c_- only: (L3) holds with
C_occ = O(1) at the
polylog-inflated block height, and both (L1') and (L2') are needed only on O(M^{7/4}) axis blocks
per scale step (sigma_0 = sqrt(5 log n/(c'' c_-)) after D4), the far remainders closing on the
tail plus the deterministic occupation caps. Nothing here moves chi = 1/3; the map is now refereed
where it was author-checked.

Defect ledger for VERIFIED_CLAIMS_LEDGER.md: D1 constant 8 -> 16 with the false identity struck;
D2 display exponent; D3 range /4; D4 (M2)-far closed, sigma_0 3 -> 5 log n, c_- conditionality
stated at the claim; D5 statement page synced; D6 partition flag. Confirmations C1-C4.
