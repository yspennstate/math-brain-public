# B04 stream notes (Claude lead) - v2, 2026-10-11 23:25 UTC

Notation: F(x,y)=g_x(y), fresh uniform selector block (a bits), arbitrary Boolean branches on one data cube; Delta=H(F)-avg_b H(g_b)=M_W+B_W (threshold Prop 8.6 (75)); I_sel=sum_T R_T E_{nu_T}|S|. Lead run: claude/B04/runs/20261011T224500Z-claude-B04-sharp-selector-debt (CLAIMS.json, code/, out/).

## Established
- A018 (collision interface, M_W<=(2/ln2)I_W, cancellation classes): every step re-derived by the lead. HOLDS; baseline with a self-contained proof.
- A019 (rare translations, B_W=sum rho_j E_kj<=4 I_W, M_W=0, closure max(C,4) with I_W/a->0): re-derived plus 400 independent exact cases, 0 failures. HOLDS at stated scope.
- A017 ledger: holds (300 independent exact cases). A016: holds where hand-checkable.
- Lead, proved, review pending:
  (1) Delta<=min(a,(2/ln2)I_sel)+a*h2(I_sel/a)<=I_sel*log2(e^3 a/I_sel) for EVERY multiplexer.
  (2) Sharp: tensor bent splices give Delta=I_sel(m+3/ln2)-(19/(6ln2))I_sel^2+..., bound-Delta=(8/(3ln2))I_sel^2+...
  (3) Closure under I_sel>=ca: max(C, min(1/c,2/ln2)+h2(c)/c), which is <=2/c and ~log2(1/c).
  (4) One-bit node: Delta_i<=(3/ln2)Inf_i+2I(D_i), D_i=(f|x_i=0-f|x_i=1)/2, I(D_i)=sum_{S contains i}(|S|-1)fhat^2 (edge-isoperimetry). First-order sharp on bent splices.
  (5) Along any fixed order these charges sum to the second moment: H<=sum(|S|^2+3.33|S|)fhat^2 (weak, no novelty claim).

## Refuted / do not repeat
- Any selector-only payment psi(I_sel,a) below (2/ln2)s+a h2(s/a)-eps*s.
- Re-deriving max(2/c,C), H=2a, Prop 8.6, the log-Sobolev M_W bound, or bent-splice lower bounds of order delta*m: all done.
- Charging each node's B_W to its own I_W (refuted), or to the full I_data (double counts the branches' own FEI budget).

## The open line (the whole remaining gap at B04)
An adaptive stopping tree in which the boundary charges 2I(D_v), counted only at nodes where the EXACT B_W exceeds K*I_W, sum to <=K'*I(f). A fixed order pays the second moment. Majority: B_W=0 at the root (odd function, each nu_T is a point mass), so use exact B_W, not h2.

## Targets (one each)
- A016: for the a-fold bent splice, compute exactly whether the one-root/whole-set code cost is <=K*I(F) as m->inf (it should be, since I_data~m/2); report the ratio code/Delta and code/I(F) for m=2,4,6.
- A017: point-flipped quadratic phase in your fiber identity: exact H, I for n<=6 and the n->inf limit at fixed r; which physical coordinates carry the 2I(D) boundary charge.
- A018: independent exact re-implementation of lead claims (1),(2),(4): your own Walsh code, interval or rational-log arithmetic; report pass/fail per claim.
- A019: generalize rare translations to arbitrary Boolean activations A_j on disjoint blocks (your sec. 1 identity gives B_W=sum rho_j H(h_j)): state the transfer H(F)<=max(C_core,C_act)I(F) and test one overlapping-block case; then try (open line) a two-level tree on majority-of-translations.
- A020: falsifiers for (4): search a=1 multiplexers maximizing Delta_i/[(3/ln2)Inf_i+2I(D_i)] at Inf_i>=1/8 (is the ratio <=0.81 there, as at n<=4?), and for (1) at a=3, m<=2 exhaustively.

Exact arithmetic or analytic proof only; floats are evidence.
