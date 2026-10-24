# B18 FEI campaign C — exact coarse-number PSD refund and authentic coarse-parent inverse frame

**Run:** `20260922T000434Z-coarse-number-refund`  
**Scope:** account02 / B18, campaign-C FEI proof integration  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Model self-report:** GPT-5.6 Sol  
**Requested effort:** maximum actually supported  
**Configured/known reasoning:** UNKNOWN / NOT_EXPOSED  
**Provider reasoning usage:** null / NOT_EXPOSED  
**Full unrestricted FEI:** **OPEN / NOT PROVED**.

## 0. Result in one paragraph

Campaign C's admission gate is now satisfied by account01/B16's source-exact net candidate
\[
\mathcal N_*(f)=\mathcal Q_{d_*,<2}(f)-\mathcal B_{d_*}(f),
\qquad d_*=n-\lfloor n/5\rfloor-1,
\]
whose universal estimate `N_* <= C_* J` would imply full FEI.  The actual two-point half-band obstruction has bounded signed net debt even though its already-formed positive live current divided by `J` diverges.  This run therefore attacks the first still-unpaid signed implication *inside the authentic clone current* and proves an exact operator-level cancellation that was missing from the current-to-physical chain.  If `F=\sum_R b_R\chi_R` is the already same-syndrome-aggregated odd clone source, `L` is fine clone degree, and `K` is **coarse parent odd degree** (number of clone pairs hit singly), then
\[
\boxed{
E_{\rm cur}
=\frac12\|K^{-1}F\|_2^2
-2\left\|\left(L^{-1}-\frac12K^{-1}\right)F\right\|_2^2.
}
\tag{0.1}
\]
The central-band current has the exact analogue
\[
\boxed{
E_{\rm cen}
=\frac12\|2^{-K}K^{-1}F\|_2^2
-2\left\|\left(2^{-L}L^{-1}-\frac12\,2^{-K}K^{-1}\right)F\right\|_2^2,
}
\tag{0.2}
\]
and, on every genuinely charged mode, the stronger sharp structural domination
\[
\boxed{E_{\rm cen}\le\frac38\|2^{-K}K^{-1}F\|_2^2.}
\tag{0.3}
\]
Moreover both positive coarse banks have exact **actual-parent** frames
\[
\|K^{-1}F\|_2^2=\sum_j\|P_jK^{-3/2}F\|_2^2,
\qquad
\|2^{-K}K^{-1}F\|_2^2
=\sum_j\|P_jK^{-3/2}2^{-K}F\|_2^2,
\tag{0.4}
\]
where `P_j=(I-tau_{j,0}tau_{j,1})/2` is the **coarse signed gate derivative**, not the doubled-parent gauge current.  Each inverse factor has a positive coarse-noise integral.  Thus the current can be rerouted before physical projection into the correct coarse-odd source sector while retaining an explicit PSD refund.  This avoids the account03/B16 relation-diagonal no-go entirely.  The surviving universal obstruction is now a Borel/live-window **square-function payment** for this coarse-odd frame; account02/B16's already-proved `<=64J` coherent Borel-integrated amplitude cannot be interchanged with an integral of squares, and the half-band obstruction shows why that distinction is essential.

## 1. Fresh control and exact admission-gate source

The run read the current owner/control files from `math-research-brain` at entry main `8af036847c779b46d7c5599466964681e8cc97f1`; OWNER CONTROL is revision `2026-09-22.1`.  No later account02/B18 pause or stop was present at entry.  The new collective allocation explicitly preserves B12--B18 on FEI and the current FEI execution reset makes B18 campaign-C lead.

The scientific master was refreshed before derivation.  The exact campaign-C source consumed is:

- `proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260921T234240Z-net-candidate-two-defect/REPORT.md`, blob `faa53e2345a0ff5be6c2f9365c511052e696c70b`.

It recovers, in natural-log units,
\[
\boxed{
H_{\rm nat}(f)=\kappa_2J(f)-\mathcal B_d(f)+\mathcal Q_{d,<2}(f)+R_d(f),
}
\tag{1.1}
\]
where
\[
\kappa_2=\frac23+\frac12\log3,
\tag{1.2}
\]
`B_d` is the retained signed high-resolvent/R16 bank with its internal odd-order refunds, `Q_{d,<2}` is the genuine small-resolvent signed source, and `R_d` is the terminal endpoint.  At
\[
d_*=n-\lfloor n/5\rfloor-1
\tag{1.3}
\]
the exact terminal theorem gives
\[
|R_{d_*}(f)|<\frac32J(f).
\tag{1.4}
\]
Hence, with
\[
\mathcal N_*(f):=\mathcal Q_{d_*,<2}(f)-\mathcal B_{d_*}(f),
\tag{1.5}
\]
the single source-exact candidate is
\[
\boxed{
\exists C_*<\infty\ \forall n\ \forall f:\quad
\mathcal N_*(f)\le C_*J(f).
}
\tag{C-NET}
\]
If this holds, the peer's complete deduction gives
\[
H_{\rm bit}(f)
\le
\frac{C_*+\frac32+\frac23+\frac12\log3}{\log2}\,I(f)
\tag{1.6}
\]
for every Boolean function in every dimension.  Therefore campaign C is no longer allowed to replace `(C-NET)` by a positive-current surrogate.

The same peer evaluates the required genuine Boolean two-point defect.  On the half-band family the asymptotic signed net debt is
\[
\frac{\mathcal Q_{d_h,<2}-\mathcal B_{d_h}}{J}
\longrightarrow
4\log2-\kappa_2
=1.5566159112390597\ldots,
\tag{1.7}
\]
and the archive cutoff gives the explicit family bound
\[
\mathcal N_*(f)<3.05661591123906\,J(f).
\tag{1.8}
\]
Thus the known positive-current divergence is canceled somewhere in the authentic signed ledger; it is not a counterexample to `(C-NET)`.  The same source refutes a pointwise-in-Borel-scale self-phase estimate, so a valid proof has to be integrated or multiscale.

## 2. Comparison with the last three B18 mechanisms

The last three substantive B18 reports entering this run were:

1. `20260921T200356Z-restriction-kernel-polarization`: moved the square-first full-line current to two positive restriction kernels `Q_S,Q_M`; neither received an original-influence payment.
2. `20260921T214713Z` q=1/q=3 Hodge compensation: on the explicit affine half-band source, the missing central positive current is canceled at the correct `n^{-3}` scale by an oppositely phased Hodge companion, but the global all-source extraction remained open.
3. `20260921T230348Z-oriented-relation-square-root`: proved the all-order oriented relation root `zeta_A^2=nu_A` and a dimension-free `1/|A|` physical Dirichlet payment, but left a mismatch between active-syndrome inverse degree `1/|R|` and relation inverse degree `1/|A|`.

The newest completed **other-account** result used decisively here is

- `proofnet24/P03-fei/fleet-2026-09-21/account03/B16/20260921T232535Z-terminal-retained-relation-diagonal/REPORT.md`.

It gives a genuine Boolean codimension-two source on which conversion of the authentic active-syndrome inverse square to a positive relation-diagonal `1/|A|` bank loses a factor asymptotic to `n/2`.  The missing cancellation lies in the signed off-diagonal ledger.  Therefore the previous B18 relation-degree route is not merely incomplete: **its positive-diagonal completion is refuted as a dimension-free mechanism**.

A second completed other-account result used in the new split is

- `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T230034Z-character-parent-gauge-null/REPORT.md`, blob `ad0130ed2d7f81127fac04061e2e7403b537faa3`.

It proves that every codimension-one coordinate-subcube parent is pointwise source-null in the authentic signed gate packet even though its positive two-clone second-difference energy can be nonzero.  That is exactly the signal that the current must be algebraically rerouted **before** a positive parent debit is interpreted physically.

### FULL-PROBLEM CHANGE

**NONE.**  `(C-NET)` is still unproved, hence unrestricted FEI remains open.

### MECHANISM CHANGE

**YES, material.**  The previous route was
\[
\text{fine active syndrome}
\to \text{positive doubled-parent current}
\to \text{relation diagonal / physical root}.
\]
The account03 no-go rules out the needed positive relation-diagonal normalization.  This run instead stays entirely on the clone cube and proves
\[
\boxed{
\text{fine current}
=\text{coarse-odd inverse-number bank}
-\text{explicit PSD refund},
}
\tag{2.1}
\]
then decomposes the coarse bank directly over the **actual coarse gate derivatives**.  No relation labels or `1/|A|` diagonal are introduced.

## 3. Exact clone operators

Let the authentic signed odd source after same-syndrome aggregation be
\[
F=\sum_R b_R\chi_R.
\tag{3.1}
\]
The terminal subtraction and all allowed signed aggregation have already occurred inside the coefficients `b_R`; no relationwise absolute value is taken below.

For coarse parent block `j`, let the two commuting clone translations be
\[
\tau_{j,0},\qquad\tau_{j,1}.
\]
Define the normalized single-clone projections
\[
P_{j,a}=\frac{I-\tau_{j,a}}2,
\tag{3.2}
\]
and the **coarse parent parity projection**
\[
\boxed{
P_j=\frac{I-\tau_{j,0}\tau_{j,1}}2.
}
\tag{3.3}
\]
On a Walsh mode `R`, `P_j` has eigenvalue one exactly when `R` hits the `j`th clone pair **singly**.  Let
\[
L\chi_R=q_R\chi_R,
\qquad
K:=\sum_jP_j,
\qquad
K\chi_R=k_R\chi_R.
\tag{3.4}
\]
Thus `L` is fine active degree and `K` is coarse-parent odd degree.  If `r_R` is the number of doubled pairs, then
\[
q_R=k_R+2r_R.
\tag{3.5}
\]
The source is odd, so `q_R` is odd.  Therefore `k_R` is also odd and in particular
\[
\boxed{k_R\ge1.}
\tag{3.6}
\]
Hence `K^{-1}` is well-defined on the entire authentic odd source.  This is the key structural fact: the compiler's fine odd sector has no `K=0` component.

The account02/B16 authentic full current is
\[
E_{\rm cur}
=2\sum_R\left(\frac1{q_Rk_R}-\frac1{q_R^2}\right)b_R^2.
\tag{3.7}
\]
Its central-band coefficient is
\[
\varepsilon_{q,k}
=2\frac{2^{-q}}q
\left(\frac{2^{-k}}k-\frac{2^{-q}}q\right),
\tag{3.8}
\]
so
\[
E_{\rm cen}=\sum_R\varepsilon_{q_R,k_R}b_R^2.
\tag{3.9}
\]
Modes with `q=k` have `r=0` and carry no current.

## 4. PROVED — exact full-current coarse-number refund

### Theorem 4.1 — `P03-B18-COARSE-NUMBER-PSD-REFUND`

For every authentic odd signed source `F` as above,
\[
\boxed{
E_{\rm cur}
=\frac12\|K^{-1}F\|_2^2
-2\left\|\left(L^{-1}-\frac12K^{-1}\right)F\right\|_2^2.
}
\tag{4.1}
\]
In particular,
\[
\boxed{E_{\rm cur}\le\frac12\|K^{-1}F\|_2^2.}
\tag{4.2}
\]
The subtracted term is a genuine PSD bank on the same already-aggregated signed source and must remain attached if later bookkeeping needs exact equality.

### Proof

Fix one mode and abbreviate
\[
x=\frac1q,\qquad y=\frac1k.
\]
Then the authentic coefficient in (3.7) is
\[
2xy-2x^2.
\]
Complete the square:
\[
\boxed{
2xy-2x^2
=\frac12y^2-2\left(x-\frac y2\right)^2.
}
\tag{4.3}
\]
Since `L` and `K` are commuting diagonal operators in the clone Walsh basis, summing (4.3) with weight `b_R^2` over all modes gives (4.1).  Equation (4.2) follows by dropping only the displayed nonnegative square.  No sign or relation multiplicity is altered because `b_R` was formed before this step.  QED.

### Sharpness of the positive envelope

The coefficient ratio relative to `k^{-2}` is
\[
\frac{2(1/(qk)-1/q^2)}{1/k^2}
=2\frac{k}{q}\left(1-\frac{k}{q}\right)
\le\frac12.
\tag{4.4}
\]
The constant `1/2` is approached when `k/q -> 1/2`; hence (4.2) cannot be improved as a scalar bound using only `K^{-2}`.

### Why this fixes the clone/coarse parity mismatch

For a single clone pair, write
\[
P_0=\frac{I-\tau_0}2,
\quad
P_1=\frac{I-\tau_1}2,
\quad
P_g=\frac{I-\tau_0\tau_1}2,
\quad
P_{01}=P_0P_1.
\]
Then pointwise on the four joint eigenspaces,
\[
\boxed{P_g=P_0+P_1-2P_{01}.}
\tag{4.5}
\]
If `M` is any PSD operator commuting with the two clone translations and `D=(I-\tau_0)(I-\tau_1)=4P_{01}`, then
\[
\boxed{
\langle DF,MDF\rangle
=8\Bigl(
\langle P_0F,MP_0F\rangle
+\langle P_1F,MP_1F\rangle
-\langle P_gF,MP_gF\rangle
\Bigr).
}
\tag{4.6}
\]
The doubled `(-- )` clone sector has coarse parity `+1`, whereas the physical/coarse gate derivative `P_g` lives in the singly-hit `(-,+)/(+,-)` sectors.  Therefore a positive doubled-parent square is *not* itself a coarse physical debit.  Account03/B18's codimension-one theorem is a concrete manifestation of this fact.  Theorem 4.1 supplies the missing global algebraic rerouting: it moves the current to the coarse-odd number operator and records the exact PSD refund rather than trying to reinterpret the doubled sector geometrically.

## 5. PROVED — exact central-band refund and the sharp `3/8` envelope

Define
\[
a(m)=\frac{2^{-m}}m.
\tag{5.1}
\]
Then (3.8) is
\[
\varepsilon_{q,k}=2a(q)(a(k)-a(q)).
\tag{5.2}
\]

### Theorem 5.1 — `P03-B18-CENTRAL-COARSE-NUMBER-REFUND`

For every authentic odd source,
\[
\boxed{
E_{\rm cen}
=\frac12\|2^{-K}K^{-1}F\|_2^2
-2\left\|\left(2^{-L}L^{-1}
-\frac12\,2^{-K}K^{-1}\right)F\right\|_2^2.
}
\tag{5.3}
\]
Moreover, on every genuinely charged mode `q>=k+2`,
\[
\boxed{
E_{\rm cen}\le\frac38\|2^{-K}K^{-1}F\|_2^2.
}
\tag{5.4}
\]
The constant `3/8` is the sharp supremum permitted by the adjacent-degree gap: it is approached for `q=k+2` with large odd `k`.

### Proof

Put
\[
x=a(q),\qquad y=a(k).
\]
The same scalar completion as (4.3) gives
\[
2x(y-x)=\frac12y^2-2(x-y/2)^2,
\tag{5.5}
\]
which sums to (5.3).

For a charged mode `q>=k+2`,
\[
\frac{x}{y}
=2^{-(q-k)}\frac{k}{q}
\le\frac14.
\tag{5.6}
\]
Hence
\[
\frac{\varepsilon_{q,k}}{y^2}
=2\frac{x}{y}\left(1-\frac{x}{y}\right)
\le2\cdot\frac14\cdot\frac34
=\frac38.
\tag{5.7}
\]
Equivalently the exact nonnegative remainder factors as
\[
\boxed{
\frac38y^2-(2xy-2x^2)
=2\left(\frac y4-x\right)\left(\frac{3y}4-x\right)\ge0.
}
\tag{5.8}
\]
Summing proves (5.4).  QED.

This improves the earlier scalar Ward envelope `11/192 W` in a different direction: (5.4) is not a replacement for that booked bank but an exact structural identification of **which inverse coarse source** carries the positive part after an explicit signed refund.

## 6. PROVED — the authentic coarse-parent inverse frame

The positive envelopes in Sections 4--5 now have a local frame on the **actual coarse gates**, not on relation labels and not on doubled gauge parents.

### Theorem 6.1 — `P03-B18-ACTUAL-COARSE-PARENT-FRAME`

On the odd source subspace,
\[
\boxed{
\|K^{-1}F\|_2^2
=\sum_j\|P_jK^{-3/2}F\|_2^2.
}
\tag{6.1}
\]
Likewise,
\[
\boxed{
\|2^{-K}K^{-1}F\|_2^2
=\sum_j\|P_jK^{-3/2}2^{-K}F\|_2^2.
}
\tag{6.2}
\]

### Proof

On one mode `R` with coarse degree `k`, exactly `k` of the projections `P_j` equal one.  Therefore its contribution to the right side of (6.1) is
\[
k\left(k^{-3/2}b_R\right)^2
=\frac{b_R^2}{k^2},
\]
which is exactly its contribution to the left side.  Multiplying both sides modewise by `4^{-k}` proves (6.2).  Orthogonality of the Walsh basis completes the proof.  QED.

This is the coefficient-level bridge that the earlier doubled-parent scalar marginal did not supply.  In particular:

- if an authentic coarse gate is source-invariant, then `P_jF=0` and it disappears **before** physical projection; this is compatible with account03/B18's exact codimension-one gauge-null theorem;
- for noncharacter coordinate-subcube parents, account02/B16's ordered-min theorem supplies the exact physical flag `(i,w)` associated to the same coarse gate, with full oriented sink `kappa_i(w)=p_i(w)+4o_i(w)` retained;
- no `1/|A|` relation normalization occurs, so account03/B16's codimension-two relation-diagonal blowup is bypassed rather than contradicted.

## 7. PROVED — positive coarse-noise representation of the inverse frame

The frame is also compatible with a positive semigroup before the final square.  For every integer `k>=1`, the Gamma integral gives
\[
\boxed{
 k^{-3/2}
=\frac2{\sqrt\pi}
\int_0^1\sqrt{-\log\rho}\,\rho^{k-1}\,d\rho.
}
\tag{7.1}
\]
Let `T_\rho^{c,(-j)}` be the standard product-noise operator on the coarse parent parity variables other than `j`; on a mode with `P_j=1` and coarse degree `k` it has eigenvalue `rho^{k-1}`.  Then
\[
\boxed{
P_jK^{-3/2}F
=\frac2{\sqrt\pi}
\int_0^1\sqrt{-\log\rho}\,
T_\rho^{c,(-j)}P_jF\,d\rho.
}
\tag{7.2}
\]
For the central frame,
\[
\boxed{
P_jK^{-3/2}2^{-K}F
=\frac1{\sqrt\pi}
\int_0^1\sqrt{-\log\rho}\,
T_{\rho/2}^{c,(-j)}P_jF\,d\rho.
}
\tag{7.3}
\]
Indeed, on a coarse-degree-`k` mode the right side of (7.3) equals
\[
\frac1{\sqrt\pi}2^{-(k-1)}
\frac{\Gamma(3/2)}{k^{3/2} }
=2^{-k}k^{-3/2}.
\]
Thus the positive envelope is an average of **signed coarse gate derivatives smoothed by a positive coarse-noise semigroup**.  This is precisely the legal order required by the newest interface-C work: signed same-syndrome aggregation first, coarse signed derivative second, positive smoothing third, square last.

## 8. What is paid and what is still not paid

The new theorems do **not** prove a dimension-free bound for `(C-NET)` by themselves.  They remove one specific universal obstruction: the current no longer needs to be interpreted as a positive doubled-parent or positive relation-diagonal bank.

The exact remaining source-to-physical obligation is now a scale-sensitive square-function inequality for the coarse-odd frame.  Schematically, on the authentic Borel/live-window source `F_s`, one needs a one-use bound of the form
\[
\boxed{
\sum_j\int_{\text{authentic ledger}}
\|P_jK_s^{-3/2}F_s\|_2^2\,d\nu(s)
\ \lesssim\ J(f)
+\text{the already-booked signed refunds},
}
\tag{8.1}
\]
or the central `2^{-K}` version, with the exact negative square from (4.1)/(5.3), high-resolvent/R16 bank, outside-live remainder and terminal endpoint retained in their original places.

This is **not** supplied by the existing account02/B16 coherent amplitude theorem.  That peer proves for a measurable low-resolvent window a coherently Borel-integrated feature whose parent sum is at most `64J`.  In symbols it controls a square **after** the Borel integration.  Equation (8.1) is an integral of **squares before** the Borel integration.  Jensen goes in the wrong direction for converting the former into the latter.  The known half-band example is exactly why this scale variance cannot be discarded: its positive post-square current can diverge relative to `J` while the signed net compiler debt remains bounded.

Therefore the next campaign-C move is not another parent mask inequality.  It is one of these two genuinely source-level statements:

1. prove a signed Littlewood--Paley/Carleson estimate for the coarse-odd frame in (7.2)--(7.3) that includes the negative PSD refund and the co-located high/outside/terminal terms exactly once; or
2. show algebraically that the Borel-scale variance of the coarse-odd frame is itself an existing R16/high-resolvent/terminal credit, with no reuse of the internal two-cell Möbius cancellation.

The second route is particularly constrained by account04/B16's theorem that the mixed two-cell overlap is already spent internally; it cannot be extracted again as an external credit.

## 9. Full-proof checklist

The smallest honest dependency chain is now:

| Step | Exact statement | Status | Source / obligation |
|---|---|---|---|
| A | source identity `H_nat=kappa_2 J-B_d+Q_{d,<2}+R_d` with R16/R32 signs and terminal | **PROVED** | account01/B16 `20260921T234240Z-net-candidate-two-defect` plus canonical archive |
| B | `|R_{d_*}|<3J/2` at `d_*=n-floor(n/5)-1` | **PROVED** | same source chain |
| C | `(C-NET): Q_{d_*,<2}-B_{d_*} <= C_*J` | **OPEN** | universal target; implies full FEI by (1.6) |
| C1 | actual half-band/two-defect signed NET is bounded; positive-current divergence is canceled | **PROVED for that family** | account01/B16; limit `(Q_low-B_high)/J=1.5566159...` |
| C2 | authentic clone current = coarse-odd inverse bank minus explicit PSD refund | **PROVED, all sources** | Theorems 4.1 and 5.1 here |
| C3 | positive coarse inverse bank has exact actual-parent frame and positive coarse-noise representation | **PROVED, all odd source fields** | Theorems 6.1 and 7.1 here |
| C4 | Borel/live-window square-function payment of this frame by `O(J)` plus nonreused signed refunds | **OPEN** | first missing implication after this run |
| C5 | compose C4 with high/outside/terminal/R16 ledgers without double spending to establish `(C-NET)` | **OPEN** | must preserve all source signs/boundaries |
| D | independent end-to-end checks of a complete universal candidate | **NOT YET APPLICABLE** | no full candidate exists |

No conditional or finite/subclass theorem is counted as closure.

## 10. PROVED / CONDITIONAL / OPEN / REFUTED ledger

### PROVED this run

- `P03-B18-COARSE-NUMBER-PSD-REFUND`, equation (4.1).
- `P03-B18-CENTRAL-COARSE-NUMBER-REFUND`, equation (5.3).
- sharp structural central envelope `E_cen <= (3/8)||2^{-K}K^{-1}F||^2`.
- exact authentic coarse-parent frames (6.1)--(6.2).
- positive coarse-noise integral formulas (7.2)--(7.3).
- clone-pair projector identity (4.5)--(4.6), explaining exactly why coarse source nullity and positive doubled-clone curvature can coexist.

### PROVED peer inputs actually applied

- account01/B16 exact source `(C-NET)` and bounded signed two-point obstruction;
- account03/B16 positive relation-diagonal conversion is dimensionally impossible on a genuine Boolean codimension-two source;
- account03/B18 codimension-one character parents are source-null;
- account02/B16 noncharacter ordered-min parent is an exact oriented physical flag;
- account04/B16 mixed two-cell overlap is already-spent internal cancellation and cannot be reused.

### CONDITIONAL

If the scale-sensitive coarse-frame payment (8.1), with the original high/outside/terminal ledger, is proved with a universal constant, then the remaining campaign-C composition may establish `(C-NET)`.  The exact constant depends on that still-unproved ledger comparison, so none is invented here.

### OPEN

- the Borel/live-window square-function payment (8.1);
- exact one-use identification of its variance with existing R16/high/terminal credits, if that is the correct route;
- universal `(C-NET)` and hence unrestricted FEI.

### REFUTED / retired

- positive relation-diagonal `1/|A|` completion of the active-syndrome inverse square as a dimension-free universal mechanism (account03/B16 codimension-two no-go);
- interpreting a positive doubled-parent clone square as a physical parent debit (clone parity identity plus account03/B18 source-null character sector);
- extracting account04's mixed two-cell overlap as a new external credit after the authentic gate packet has already been formed;
- pointwise self-phase payment on the two-point obstruction;
- previously retired global phase/rank/l1, sign-free parity/profile, receiver-only, ordinary positive-current and raw-normalizer shortcuts.

## 11. Decisive exact self-check

`check_coarse_number_refund.py` uses exact rational arithmetic.  It checked all `20,301` admissible odd pairs `1<=k<=q<=401`, verified both square-completion identities and the factored `3/8` central remainder, and checked all four clone-pair eigenspaces for (4.5)--(4.6).  On the sampled range:

- largest full coefficient ratio to `k^{-2}` was `80400/160801 = 0.4999968905...` at `(q,k)=(401,201)`, approaching the proved sharp `1/2` envelope;
- largest central coefficient ratio to `a(k)^2` was `480795/1286408 = 0.3737500077...` at `(q,k)=(401,399)`, approaching the proved sharp `3/8` envelope;
- every exact identity passed.

This computation is a falsification/self-check only.  The theorem claims are the symbolic all-dimensional proofs above.

## 12. Literature applicability check

A fresh public-literature check on 22 September 2026 still finds no unrestricted FEI proof.  González--MacManus--Pereyra, arXiv:2606.00246, explicitly formulate a restriction inequality which *would* imply full FEI and prove structured/stopping-tree cases, not the universal missing step.  Potapov, arXiv:2609.21563 (submitted 18 September 2026), proves FEI for plateaued Boolean functions (sharp class constant 4) and partially bent functions (sharp class constant 2), not for all Boolean functions.  These do not supply the coarse-frame scale inequality (8.1).  No novelty-priority claim is made for the operator identities in this report.

## 13. Next exact attack

Stay before relation resolution and before scalar parent compression.  Starting from the authentic Borel source `F_s`, expand the co-located low/high resolvent ledger **after applying the coarse projection `P_j` but before squaring**, and compute whether
\[
\int \|P_jK^{-3/2}F_s\|^2d\nu_L(s)
-\text{the exact high/R16 companion}
\]
admits a signed Plancherel/Carleson representation whose total over `j` is bounded by the original-coordinate `kappa` bank.  Any attempted proof must reproduce the bounded two-point NET cancellation from Section 1 and must keep the explicit negative square in (4.1)/(5.3); a proof that discards that square and then pays the positive frame alone is already ruled out by the half-band obstruction.

**Final mathematical status:** `ESSENTIAL_STEP_APPLIED` at the first missing signed compiler implication; **full FEI remains OPEN / NOT PROVED**.
