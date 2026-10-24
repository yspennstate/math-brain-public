# B16 FEI interface C — two-cell Möbius/RKHS factorization and the no-reuse phase-overlap theorem

**Date:** 21 September 2026  
**Scope:** `account04 / B16`, joint FEI interface C  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact all-order source factorization, exact live-window/terminal compatibility, a new signed-PSD decomposition, and a refutation of one tempting compensation mechanism. No publication-priority claim.

## 0. Fresh state and why this run changes the interface

This run uses the joint owner order `FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z` and attacks interface C before scalar parent compression.

The exact peer inputs used substantively are:

1. **account02/B16 actual parent weights**  
   `proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`, handoff revision `e4f58c7ac32a2699fb3c50da09922a7fa77f9958`.  
   For an odd active syndrome `R`, with `q_R=|R|`, odd-block degree `k_R` and doubled-parent count `r_R=(q_R-k_R)/2`, the authentic central multiplier is
   \[
   \varepsilon_R=2\frac{2^{-q_R}}{q_R}\left(\frac{2^{-k_R}}{k_R}-\frac{2^{-q_R}}{q_R}\right),
   \]
   and each doubled parent receives
   \[
   \mu^{\rm cen}_{R,j}=\frac{\varepsilon_R}{r_R}b_R^2.
   \]
   The same-syndrome signed aggregate `b_R` is formed before the square.

2. **account02/B16 codimension warning and signed Volterra triage**  
   `proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260921T193735Z-codimension-normalization-parent-bridge/REPORT.md` and  
   `proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260921T214739Z-signed-volterra-credit-triage/REPORT.md`.  
   These show that scalar parent compression followed by positive/TV plaquette inversion incurs a codimension factor, and that a viable refund must be inserted before the final positive local square.

3. **account03/B18 signed physical flag curvature**  
   `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`, proof revision `4843e50690013fd18b85dd8763b53bdc75da79e8`.  
   In the minimizing-character gauge,
   \[
   \kappa_i(w)=p_i(w)+4o_i(w),
   \qquad
   \sum_i\mathbb E\kappa_i(W)\le2J(f),
   \]
   with the opposite-orientation bank `o_i` retained rather than deleted.

4. **account03/B16 signed square-root resolvent**  
   `proofnet24/P03-fei/fleet-2026-09-21/account03/B16/20260921T211732Z-signed-square-root-resolvent/REPORT.md`, blob `be465709537514dc3d483fa61532630ac78dce66`.  
   It proves
   \[
   \mathbb E|D_\phi|^2=4\sum_j\|\partial_jL^{-1/2}F_\phi^-\|_2^2
   \]
   and locates the required refund before the local square is sent to physical curvature.

5. **account03/B18 newest critical-core correction**  
   `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T221012Z-affine-defect-critical-descent/REPORT.md`, blob `075eaed4478012929ddf58cd3fea4d96f221415d`.  
   It proves the known half-band affine-defect witness is not restriction-maximal for `H/J`. This removes that particular witness from a legitimate restriction-maximal contradiction proof, but does not prove interface C on arbitrary critical cores.

6. **immediately preceding account04/B16 finite-window source**  
   `proofnet24/P03-fei/fleet-2026-09-21/account04/B16/20260921T213921Z-finite-resolvent-rkhs-refund/REPORT.md`, blob `9cb2bfed95112b295cb668348aa386e010f7d53a`.  
   It proves the finite-resolvent sine RKHS, exact all-order R32 gate packet, and co-located low/high/outside-window ledger.

The new result below asks a narrower question than the already-refuted complete-positive-current contraction:

> Inside the authentic finite-resolvent gate packet, can the mixed phase-switch overlap itself be extracted as the missing signed compensation before the final square?

The answer is structurally clean: it has an exact signed-PSD representation, but **it is already consumed internally** to cancel globally unfrustrated relation packets. Treating it as an additional external credit would double-count. This identifies a false-but-tempting route and gives a sharper two-bit orientation criterion for the remaining source-to-physical map.

---

## 1. Exact two-cell setup

Let `M` be an actual pre-gate phase code containing the affine characters, let
\[
D=M^\perp\subseteq RM(1,n)^\perp,
\]
let `Q` be the gate face, and put `U=Q^c`, `V=Q`. For a dual phase `m in M` and Boolean phase `f`, define
\[
u_f(m)=\frac1N\sum_{x\in U} f(x)(-1)^{m_x},\qquad
u_0(m)=\frac1N\sum_{x\in U}(-1)^{m_x},
\]
\[
v_f(m)=\frac1N\sum_{x\in V} f(x)(-1)^{m_x},\qquad
v_0(m)=\frac1N\sum_{x\in V}(-1)^{m_x}.
\]
For Borel time `s`, write
\[
A_f(s,m)=\sin(su_f(m)),\quad A_0(s,m)=\sin(su_0(m)),
\]
\[
B_f(s,m)=\sin(sv_f(m)),\quad B_0(s,m)=\sin(sv_0(m)).
\]
The authentic signed gate packet is
\[
G_M(s)=\mathbb E_m[A_fB_f-A_0B_0].
\tag{1.1}
\]
This is exactly the object entering the finite-resolvent representation of the preceding B16 report. No parent scalar mass or total variation has been introduced.

Put
\[
\delta A=A_f-A_0,\qquad \delta B=B_f-B_0.
\]
Then pointwise in `(s,m)`,
\[
\boxed{
A_fB_f-A_0B_0
=\delta A\,B_0+A_0\,\delta B+\delta A\,\delta B.
}
\tag{1.2}
\]
Define the three averaged channels
\[
L_U(s)=\mathbb E_m[\delta A\,B_0],\qquad
L_V(s)=\mathbb E_m[A_0\,\delta B],\qquad
O(s)=\mathbb E_m[\delta A\,\delta B].
\tag{1.3}
\]
Thus
\[
\boxed{G_M=L_U+L_V+O.}
\tag{1.4}
\]

---

## 2. PROVED — live finite-resolvent two-cell RKHS factorization

Let `w(s)>=0` be any integrable nonnegative Borel kernel. This includes every finite-resolvent interval kernel from the preceding report, the low-resolvent kernel `w_<2`, its high complement `w_>2`, and the restrictions `1_W w_<2`, `1_{W^c}w_<2` for the actual live window and its complement.

Let
\[
\Phi_w(a)(s)=\sqrt{w(s)}\sin(sa)
\]
be the scalar sine feature in `L^2(ds)`. Then
\[
\mathcal O_w
:=\int_0^\infty w(s)O(s)\,ds
=\mathbb E_m\langle \Delta_U(m),\Delta_V(m)\rangle,
\tag{2.1}
\]
where
\[
\Delta_U=\Phi_w(u_f)-\Phi_w(u_0),\qquad
\Delta_V=\Phi_w(v_f)-\Phi_w(v_0).
\]
Therefore polarization gives the exact signed-PSD decomposition
\[
\boxed{
\mathcal O_w
=\frac14\mathbb E_m\|\Delta_U+\Delta_V\|^2
-\frac14\mathbb E_m\|\Delta_U-\Delta_V\|^2.
}
\tag{2.2}
\]
Both quadratic banks on the right are positive semidefinite and use the **same live finite kernel**. There is no endpoint replacement and no enlargement from `W` to the full line.

Equation (2.2) is the strongest legitimate sense in which the mixed phase-switch overlap supplies a negative quadratic channel: the minus bank is explicit, but its plus companion is co-located and cannot be silently discarded.

Because the low/high and `W/W^c` decompositions are all literal nonnegative splits of `w`, (1.4) and (2.2) hold separately on every one of those pieces. Consequently the preceding exact ledger
\[
\text{live low} = \text{full entropy parent} - \text{high} - \text{outside-live low}
\]
can be refined into the same three two-cell channels without changing any sign or reusing a remainder.

---

## 3. PROVED — exact all-order relation Möbius formula

Put `theta=s/N`. For a dual relation `A in D`, set
\[
A_U=A\cap U,\qquad A_V=A\cap V,
\]
and define the two cell-local Boolean frustration bits
\[
r_U(A)=\frac{1-f_{A_U}}2,\qquad
r_V(A)=\frac{1-f_{A_V}}2,
\tag{3.1}
\]
where `f_B=prod_{x in B} f(x)`. Only relations with both `|A_U|` and `|A_V|` odd contribute to the sine-sine gate packet. For such a relation put `q=|A|` (necessarily even).

### Theorem 3.1 — `P03-B16-TWO-CELL-MOBIUS-R32` — PROVED

For every pre-gate code `M`, every Boolean phase `f`, and every gate face `Q`,
\[
\boxed{
G_M(s)=2\sum_{\substack{A\in D\\ |A_U|,|A_V|\;\mathrm{odd}}}
(-1)^{q/2}
\bigl[r_U+r_V-2r_Ur_V\bigr]
\sin^q\theta\cos^{N-q}\theta.
}
\tag{3.2}
\]
Moreover the three channels in (1.4) have the exact separate expansions
\[
\boxed{
L_U(s)=2\sum_A(-1)^{q/2}r_U(A)
\sin^q\theta\cos^{N-q}\theta,
}
\tag{3.3}
\]
\[
\boxed{
L_V(s)=2\sum_A(-1)^{q/2}r_V(A)
\sin^q\theta\cos^{N-q}\theta,
}
\tag{3.4}
\]
\[
\boxed{
O(s)=-4\sum_A(-1)^{q/2}r_U(A)r_V(A)
\sin^q\theta\cos^{N-q}\theta.
}
\tag{3.5}
\]
The sums in (3.3)--(3.5) have the same relation constraints as (3.2).

### Proof

For the `U` cell,
\[
\sin\left(\theta\sum_{x\in U} f(x)(-1)^{m_x}\right)
\]
has the standard odd-subset character expansion
\[
\sum_{B\subseteq U,\ |B|\text{ odd}}
(-1)^{(|B|-1)/2}
\sin^{|B|}\theta\cos^{|U|-|B|}\theta\, f_B(-1)^{m(B)}.
\]
The comparator is the same formula with `f_B=1`; the `V` cell is identical. Averaging a product over `m in M` annihilates every pair except those for which the disjoint union belongs to `D=M^perp`. For `q=|A_U|+|A_V|`, the product of the two sine signs is `(-1)^{q/2-1}`. Replacing `f_{A_U}-1=-2r_U` and `f_{A_V}-1=-2r_V` gives (3.3)--(3.5).

Finally
\[
\frac{1-f_A}{2}
=\frac{1-f_{A_U}f_{A_V}}2
=r_U\oplus r_V
=r_U+r_V-2r_Ur_V,
\tag{3.6}
\]
so the sum is exactly (3.2), which recovers the preceding all-order frustrated-relation formula. QED.

### R32 signs are untouched

The factor `(-1)^{q/2}` is the authentic R32 sign. Thus `q=0 mod 4` shells remain debits and `q=2 mod 4` shells remain negative credits. No positive part is introduced in (3.2)--(3.5).

On the actual half-band live corridor one has `0<=theta<pi/2`, so integrating against any of the nonnegative finite-resolvent/live kernels preserves each shell's R32 sign. The live window does not convert the alternating relation ledger into an unsigned one.

---

## 4. PROVED — the mixed cell overlap is already spent; it is not a new external compensation bank

Equation (3.6) has a decisive support consequence.

### Theorem 4.1 — `P03-B16-PHASE-OVERLAP-NOREUSE` — PROVED

For every relation appearing in the gate expansion:

- if the mixed overlap coefficient is nonzero, then `r_U=r_V=1`, hence `f_A=+1` and the authentic gate source coefficient in `G_M` is zero;
- if the authentic gate source coefficient is nonzero, then `f_A=-1`, equivalently `r_U xor r_V=1`, hence `r_Ur_V=0` and the mixed overlap coefficient is zero.

In formulas,
\[
\boxed{
r_Ur_V\ne0\implies r_f=0,\qquad
r_f=1\implies r_Ur_V=0.}
\tag{4.1}
\]

Therefore the overlap term `O` cancels only the **globally unfrustrated** packets that are introduced by splitting the source into the two one-cell changes `L_U,L_V`. It does not subtract relationwise from the actual `f_A=-1` source packet.

Consequently a proof that first forms the authentic gate packet `G_M` and then subtracts the negative PSD part of (2.2) as a new signed credit would reuse a cancellation which has already been consumed inside (1.4). That route is invalid unless the matching positive companion and one-cell terms are carried at the same time.

This is not a counterexample to FEI. It kills a specific natural interface-C shortcut: **“use the two-cell RKHS mixed phase-switch overlap as the missing external refund after forming `b_R`.”**

The statement survives terminal subtraction. If the retained potential is a signed difference of two code averages, apply Theorem 4.1 to each code before subtracting. The terminal `C_0-D_d` difference remains linear and no term is reclassified.

---

## 5. The exact two-bit pattern and the physical orientation target

Although the mixed overlap is not a free external credit, its coefficient pattern identifies the correct orientation data that a valid source-to-physical contraction must preserve.

At one relation coordinate, ignoring the common R32 shell multiplier, the **gross one-cell debit** is
\[
D_{\rm gross}=2(r_U+r_V),
\tag{5.1}
\]
while the exact Möbius refund is
\[
C_{\rm cell}=4r_Ur_V,
\tag{5.2}
\]
so
\[
\boxed{D_{\rm gross}-C_{\rm cell}=2(r_U\oplus r_V).}
\tag{5.3}
\]

Compare account03/B18's exact physical signed-curvature identity
\[
\kappa_i(w)=p_i(w)+4o_i(w).
\tag{5.4}
\]
Here `p_i` is support disagreement and `o_i` is opposite-sign overlap. For the four possible two-bit patterns one has the purely algebraic implication
\[
\boxed{
2(r_U+r_V)\le 2p+4o\le2(p+4o)=2\kappa
}
\tag{5.5}
\]
provided a source-to-physical pivot preserves the pattern in the precise sense
\[
p=r_U\oplus r_V,\qquad o=r_Ur_V.
\tag{5.6}
\]
Moreover under (5.6) the source Möbius refund `4r_Ur_V` is exactly the coefficient of the physical opposite-orientation channel.

Equation (5.5) is **not** asserted unconditionally for the compiler. It is a sharp local target criterion. The remaining source-exact problem is now more specific than “find a positive pair measure”:

> construct, after the legitimate R16/entropy/window refund is inserted and before scalar parent compression, an orientation-preserving coupling which carries the two source cell bits `(r_U,r_V)` to a physical derivative pair with (5.6), or prove a weaker PSD version with the same no-reuse accounting.

The existing account03 parent pivot theorem proves the required physical orientation statement for the auxiliary one-subcube parent mask, but it does **not** yet prove (5.6) for the original Boolean phase `f`. That is the surviving original-coordinate gap.

---

## 6. Compatibility with account02's authentic parent weights

The scalar central factor
\[
\varepsilon_R/r_R
\]
depends only on the active syndrome and doubled-parent multiplicity. It therefore commutes with the codewise decomposition (1.4)--(3.5). Hence the same authentic doubled-parent label `j` may be carried through the two-cell signed channels **before** summing to the post-square scalar marginal `mu_j`.

This is the legal order:
\[
\boxed{
\text{signed relation packet}
\to (L_U,L_V,O)\text{ with exact R32 signs}
\to \text{live/high/outside-window split}
\to \text{orientation-preserving physical coupling}
\to \text{final positive square / }\kappa\text{ payment}.
}
\tag{6.1}
\]

The illegal shortcut is
\[
\text{signed relation packet}\to b_R^2\to\mu_j
\to \text{reconstruct the already-spent }O\text{ as a new credit}.
\tag{6.2}
\]
Theorem 4.1 shows exactly why (6.2) double-counts.

This also respects account02's codimension-normalization warning: no scalar `mu_j` is inverted through the tiny one-subcube plaquette amplitude.

---

## 7. Finite-window and remainder bookkeeping

Let
\[
w_{<2}(s)=\frac4{s^3}\left[1-e^{-\sqrt2s}(1+\sqrt2s+s^2)\right],
\]
\[
w_{>2}(s)=\frac4{s^3}e^{-\sqrt2s}(1+\sqrt2s+s^2),
\qquad w_{<2}+w_{>2}=4/s^3.
\]
For the actual live window `W`, apply Sections 1--4 separately to
\[
1_W w_{<2},\qquad 1_{W^c}w_{<2},\qquad w_{>2}.
\]
Each is nonnegative, so every corresponding sine feature is a genuine Hilbert-space feature and each overlap admits (2.2).

Thus the exact parent ledger from the preceding B16 run,
\[
\int_W w_{<2}C_j
=\Delta_{g_{j,0}}\Delta_{g_{j,1}}[\mathscr D_d(fh)-\mathscr D_d(h)]
-H_j-\int_{W^c}w_{<2}C_j,
\]
may be decomposed channel-by-channel without changing its signs. In particular:

- the high-resolvent term remains one complementary multiplier on the same signed packet;
- the outside-live term remains an explicit signed remainder;
- the terminal `C_0-D_d` subtraction remains inside every channel;
- negative `2 mod 4` R32 shells are not positive-parted;
- the mixed cell-overlap cancellation may not be spent a second time after the codewise gate packet has already been formed.

This is the requested live-window/remainder compatibility for the new factorization.

---

## 8. Decisive computation

`check_b16_cell_mobius.py` is standard-library only. It enumerates the complete affine-character code `RM(1,n)` for `n=2,3`, its exact dual relations, coordinate one-subcube gates of every codimension, random Boolean phases, and three Borel angles per instance.

Executed results:

- `1,500` direct sine-packet versus relation-expansion checks;
- `7,500` exact relation coefficient/Möbius checks;
- `1,800` nonzero overlap-support cases, every one satisfying `f_A=+1` and zero authentic gate coefficient;
- `3,804` frustrated-source cases, every one satisfying zero mixed-overlap coefficient;
- all four exact two-bit orientation pattern inequalities (5.3)--(5.5);
- maximum floating direct-vs-relation error `8.326672684688674e-17`.

Checker SHA-256: `45240f01ad75e2311654962842f1ad18dee27457dcdc9b752695e27a547ad22c`.

The finite computation is falsification/self-check evidence. The all-dimensional identities above are symbolic character-expansion proofs.

---

## 9. Classification and next handoff

### PROVED

1. Exact two-cell decomposition `G=L_U+L_V+O` at the authentic precompression source.
2. Exact signed-PSD RKHS polarization of `O` for every finite/live/high/outside Borel kernel.
3. Exact all-order R32 Möbius formulas (3.2)--(3.5), with terminal subtraction and dual-code multiplicity intact.
4. The phase-overlap no-reuse theorem: the mixed overlap lives only on globally unfrustrated relation packets and is already consumed when the one-cell decomposition recombines to the authentic gate source.
5. The sharp two-bit orientation criterion (5.5)--(5.6), conditional only on constructing the physical pivot which preserves those two source bits.

### REFUTED / DEAD

- Extracting the negative PSD part of the two-cell mixed phase-switch overlap as an additional compensation **after** the authentic gate packet / same-syndrome source has already been formed. That would double-count an internal cancellation.
- Returning to scalar `mu_j` followed by positive/TV parent-plaquette inversion; account02's codimension barrier still applies.

### OPEN

The remaining interface-C map is an orientation-preserving, source-exact coupling at the precompression three-phase field level, after the legitimate R16/entropy/window refund is inserted. It must carry the original Boolean phase, not only the auxiliary parent mask, into account03/B18's signed derivative curvature. A sufficient local target is (5.6), or a PSD relaxation whose total debit is bounded by a constant times the ordered `kappa` bank without reusing the cell-overlap, R16, terminal or outside-window credits.

The newest account03/B18 critical-descent theorem removes the known affine half-band witness from restriction-maximal cores, so a critical-core version of this target is now compatible with that obstruction; it is still unproved.

**Full unrestricted FEI remains OPEN / NOT PROVED.**

### Joint-order handoff

- `consumed_peer_artifact`: account02/B16 actual-parent report at revision `e4f58c7...`; account03/B18 signed-flag report at revision `4843e506...`; account03/B16 signed-square-root-resolvent; account03/B18 affine-defect critical descent.
- `applied_to_claim`: identify the legal signed/PSD refund content of the finite-window two-cell phase-switch packet before physical contraction.
- `remaining_implication`: construct an original-coordinate orientation-preserving coupling satisfying (5.6), or a quantitatively equivalent PSD relaxation, after the nonreused refund is inserted.
- `next_recipient`: account03/B16 for the local square-root-resolvent field and account03/B18 for the signed physical pivot; account02/B16 should retain the genuine `epsilon_R/r_R` parent labels without scalar inversion.
- `mechanism_change`: yes — from treating the mixed RKHS overlap as a candidate external credit to proving it is an already-spent internal Möbius cancellation and replacing the target by a two-bit orientation-preserving precompression coupling.
