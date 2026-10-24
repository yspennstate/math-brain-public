# B16 FEI signed transport — self-phase one-cell collapse, finite-resolvent collision refund, and the non-coordinate quartic gap

**Date:** 21 September 2026 UTC  
**Scope:** `account03 / B16`, joint FEI interface C  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Full unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact source identities, an exact finite-resolvent/high-refund decomposition, an exact coordinate-plaquette source-to-physical identity, and a rigorous obstruction to extending that direct plaquette map to all quartic source relations. No novelty or publication-priority claim.

## 0. Fresh state and mechanism change

This run follows `FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z`, interface C. The positive all-Boolean half-band current estimate remains refuted by the genuine Boolean construction in the shared `20260921T204926Z-sharp-kernel-and-current-obstruction` handoff. I therefore do **not** return to a positive-current or post-square R16 estimate.

The named other-account result consumed substantively is the newest account01/B16 report

`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260921T225305Z-quarterturn-selfphase/REPORT.md`

at scientific source commit `5bee3ad064bbb4afab3743cf1d64148cc0c5e017`, blob `da1ddcdc6ff85679c153b1c23ab32b54d6c3ad60`. It proves the quarter-turn MacWilliams identity for the signed characteristic-function packet, the exact entropy transform, and the self-phase gate

\[
M_F=RM(1,n)+\langle b_F\rangle
\]

which annihilates the terminal characteristic function pointwise while the physical edge boundary of the gate mask is exactly `J(f)` in the minimizing-character gauge.

I combine that result with account04/B16's two-cell Möbius/RKHS factorization (`20260921T221559Z-cell-mobius-rkhs-orientation`) and account03/B18's signed physical flag bank. The method change is to choose the **Boolean phase itself as the gate face** and ask what survives before scalar parent compression. This produces a one-cell source rather than the generic two-bit orientation problem.

## 1. Setup

Work in the minimizing-character gauge and rename the gauged Boolean phase `F`, so

\[
I(F)=J(f).
\]

Let

\[
Q=\{x:F(x)=-1\},\qquad U=Q^c,
\]

and let `b_F=1_Q` be its truth-table bit. Put `M_0=RM(1,n)` and `N=2^n`. For `m in M_0`, split the comparator correlation into the two cells

\[
u_0(m)=\frac1N\sum_{x\in U}(-1)^{m_x},\qquad
v_0(m)=\frac1N\sum_{x\in Q}(-1)^{m_x}.
\]

For the Boolean phase itself,

\[
u_F(m)=\frac1N\sum_{x\in U}F(x)(-1)^{m_x},\qquad
v_F(m)=\frac1N\sum_{x\in Q}F(x)(-1)^{m_x}.
\]

The generic authentic two-cell gate packet of account04/B16 is

\[
G(s)=\mathbb E_{m\in M_0}
[\sin(su_F)\sin(sv_F)-\sin(su_0)\sin(sv_0)].
\]

The account01 characteristic packet is

\[
\Xi_{M_0,b_F}(s)
=\mathbb E_{M_0}\cos(s\beta_0)-\mathbb E_{M_0}\cos(s\beta_F).
\]

## 2. PROVED — self-phase gate collapses the generic two-cell source to one cell

### Theorem 2.1 — `P03-B16-SELF-PHASE-ONE-CELL-COLLAPSE`

For every `m in M_0`,

\[
\boxed{u_F(m)=u_0(m),\qquad v_F(m)=-v_0(m).}
\tag{2.1}
\]

Consequently, pointwise in Borel time,

\[
\boxed{
G(s)=-2\,\mathbb E_{m\in M_0}\sin(su_0(m))\sin(sv_0(m))
=\Xi_{M_0,b_F}(s).
}
\tag{2.2}
\]

In the exact two-cell Möbius variables of account04/B16, every contributing relation satisfies

\[
\boxed{r_U(A)=0,\qquad r_V(A)=r_F(A).}
\tag{2.3}
\]

Hence the mixed overlap channel and the `U`-cell channel vanish identically:

\[
\boxed{O(s)\equiv0,\qquad L_U(s)\equiv0,\qquad G(s)=L_V(s).}
\tag{2.4}
\]

### Proof

On `U`, `F=+1`, while on `Q`, `F=-1`, proving (2.1). With `beta_0=u_0+v_0` and `beta_F=u_0-v_0`,

\[
\cos(s(u_0+v_0))-\cos(s(u_0-v_0))=-2\sin(su_0)\sin(sv_0),
\]

which gives (2.2).

For any relation `A`, the product of `F` over `A cap U` is one, hence `r_U=0`; the product over `A cap Q` is `(-1)^{|A cap Q|}`, and this is also the full relation frustration because the `U` factor is one. Thus `r_V=r_F`, proving (2.3). The exact account04 formulas `L_U~r_U`, `L_V~r_V`, `O~-2r_Ur_V` then give (2.4). QED.

### Consequences for the live ledger

This identity is before scalar parent compression. It therefore preserves:

- every `(-1)^{|A|/2}` R32 debit/negative-credit sign;
- complete dual-code multiplicity;
- the finite low/high/outside-live Borel split;
- the existing moment/R16 and negative entropy credits, which are not spent here.

Moreover account01/B16's self-phase theorem gives

\[
\Xi_{M_F,b_F}(s)\equiv0.
\tag{2.5}
\]

Thus this one-gate reorganization has a **pointwise zero terminal characteristic function**. The generic two-cell no-reuse issue is also absent because its mixed-overlap channel is exactly zero. What remains is the genuinely one-cell signed Borel corridor.

This does **not** imply that the remaining corridor is `O(J)`; that is still the hard step.

## 3. PROVED — exact finite-resolvent logarithmic refund is a collision credit

For `T>0` define

\[
F_T(x)=x\log(1+T/x),\qquad F_T(0)=0,
\]

and let

\[
p_S=\widehat F(S)^2,\qquad \sum_Sp_S=1.
\]

Define the finite-resolvent spectral functional

\[
\mathcal H_T(p):=\sum_SF_T(p_S)-F_T(1).
\tag{3.1}
\]

For the self-phase gate this is exactly the scalar finite-resolvent polarization:

\[
\boxed{
\mathcal H_T(p)
=-N\,\mathbb E_{m\in M_0}
K_T(u_0(m),v_0(m)),
}
\tag{3.2}
\]

where account04's PSD sine kernel is

\[
K_T(u,v)=F_T((u+v)^2)-F_T((u-v)^2).
\]

Indeed, for every nonconstant affine character `u_0+v_0=0` and `u_0-v_0=\widehat F(S)` up to the harmless global sign, while at the constant character they are `1` and `\widehat F(\varnothing)`.

### Theorem 3.1 — `P03-B16-FINITE-RESOLVENT-COLLISION-REFUND`

Let `H_nat(p)=-sum p_S log p_S`. Then

\[
\boxed{
\mathcal H_T(p)=H_{\rm nat}(p)-\mathcal C_T(p),
}
\tag{3.3}
\]

where

\[
\boxed{
\mathcal C_T(p)=
\sum_Sp_S\log\frac{T+1}{T+p_S}\ge0.
}
\tag{3.4}
\]

Moreover

\[
\boxed{
0\le\mathcal C_T(p)
\le\frac1T\left(1-\sum_Sp_S^2\right)
\le\frac{2}{T}J(f).
}
\tag{3.5}
\]

In particular, at the live small/high split `T=2`,

\[
\boxed{0\le H_{\rm nat}(p)-\mathcal H_2(p)\le J(f).}
\tag{3.6}
\]

### Proof

Expand

\[
F_T(x)=-x\log x+x\log(T+x).
\]

Using `sum p_S=1` gives (3.3)-(3.4). For each `p in [0,1]`,

\[
\log\frac{T+1}{T+p}
=\log\left(1+\frac{1-p}{T+p}\right)
\le\frac{1-p}{T+p}
\le\frac{1-p}{T}.
\]

Summing with weights `p_S` gives the first upper bound in (3.5). The second uses the collision estimate already retained in the consumed account01/B16 self-phase report,

\[
1-\sum_Sp_S^2\le2J(f).
\]

QED.

### Meaning

The finite-resolvent logarithm is not hiding an additional unbounded high-resolvent debt. For the self-phase source, the entire difference between full Fourier entropy and the `T=2` finite-resolvent functional is one explicit positive collision refund of size at most `J`. Therefore the high-resolvent term is already dimension-free **before** any physical-flag contraction.

But (3.6) also shows why this alone cannot close FEI: paying `mathcal H_2` by `O(J)` is, up to an additive `J`, essentially the full conjecture.

## 4. PROVED — quartic dual multiplicity is exactly the spectral collision defect

Let

\[
C_4(F)=\#\{A\in RM(1,n)^\perp:|A|=4,\ F_A=-1\}.
\]

### Theorem 4.1 — `P03-B16-SELF-PHASE-QUARTIC-COUNT`

\[
\boxed{
C_4(F)=\frac{N^3}{48}\left(1-\sum_Sp_S^2\right).
}
\tag{4.1}
\]

Hence

\[
\boxed{\frac{C_4(F)}{N^3}\le\frac{J(f)}{24}.}
\tag{4.2}
\]

### Proof

The account01 quarter-turn relation formula gives

\[
\Xi_{M_0,b_F}(s)
=2\sum_{A:F_A=-1}(-1)^{|A|/2}
\sin^{|A|}(s/N)\cos^{N-|A|}(s/N).
\]

The `s^4` coefficient is therefore `2 C_4/N^4`.

On the other hand the exact self-phase scalar formula is

\[
N\Xi_{M_0,b_F}(s)
=\cos s-\cos(s\sqrt{p_\varnothing})
+\sum_{S\ne\varnothing}[1-\cos(s\sqrt{p_S})].
\]

Its `s^4` coefficient is `(1-sum p_S^2)/24`. Equating coefficients gives (4.1); (4.2) follows from the collision bound. QED.

This is a multiplicity identity, not a positive Borel payment: isolating the quartic shell and integrating it with the entropy-scale normalization can still lose a factor of order `N`. Higher signed shells cannot be discarded.

## 5. PROVED — every coordinate-aligned quartic relation lands exactly in the physical support flag

Fix an original physical coordinate `i`, a translation `w` with `w_i=0`, and a base point `y`. Let

\[
A_{i,w,y}=\{y,y+e_i,y+w,y+w+e_i\}.
\]

Define the physical sensitivity bit

\[
\eta_i(y)=1_{\{F(y)\ne F(y+e_i)\}}.
\]

### Theorem 5.1 — `P03-B16-QUARTIC-PLAQUETTE-FLAG`

For every Boolean `F`,

\[
\boxed{
\frac{1-F_{A_{i,w,y}}}{2}
=\eta_i(y)\oplus\eta_i(y+w).
}
\tag{5.1}
\]

Averaging `y` gives exactly

\[
\boxed{
\mathbb E_y\frac{1-F_{A_{i,w,y}}}{2}=p_i(w)\le\kappa_i(w),
}
\tag{5.2}
\]

where account03/B18 proved `kappa_i=p_i+4o_i` and the ordered physical flag payment `sum_i E_W kappa_i(W)<=2J(f)`.

### Proof

Since

\[
F(y)F(y+e_i)=(-1)^{\eta_i(y)},
\]

multiplying the two `i`-edges in the plaquette gives

\[
F_{A_{i,w,y}}
=(-1)^{\eta_i(y)+\eta_i(y+w)}.
\]

This is exactly (5.1), and averaging yields (5.2). QED.

Thus **for the coordinate-aligned weight-four sector**, the authentic relation-frustration bit itself is the physical support-disagreement flag. There is no orientation loss and no need to spend the opposite-sign bank, terminal term, high-resolvent refund, or negative R32 credits. This is a genuine source-to-physical identification, but only for that sector.

## 6. REFUTED — direct coordinate plaquettes do not cover the full quartic source

A tempting next shortcut would be to identify every frustrated weight-four dual relation with one physical coordinate plaquette and feed all of `C_4` to (5.2). This is false by an exact counting obstruction.

Take the one-point defect `F(0)=-1`, `F(x)=+1` for `x!=0`. Every affine two-plane through zero is a frustrated weight-four dual relation. Therefore

\[
\boxed{
C_4=\binom{n}{2}_2
=\frac{(2^n-1)(2^n-2)}6.
}
\tag{6.1}
\]

The number of those planes whose direction space contains at least one original coordinate vector is exactly

\[
\boxed{
C_4^{\rm coord}
=n(2^{n-1}-1)-\binom n2.
}
\tag{6.2}
\]

Indeed each `e_i` lies in `2^{n-1}-1` two-dimensional subspaces; a two-dimensional binary subspace cannot contain three distinct standard basis vectors, and the pairwise overlaps are precisely `span(e_i,e_j)`.

Hence

\[
\boxed{
\frac{C_4^{\rm coord}}{C_4}
\sim\frac{3n}{2^n}\longrightarrow0.
}
\tag{6.3}
\]

Numerically the fraction is about `0.26267` at `n=6`, `0.09152` at `n=8`, `0.02907` at `n=10`, `0.00877` at `n=12`, and `5.72e-5` at `n=20`.

So the direct plaquette identity (5.1) cannot by itself be a universal map for the full quartic dual-code multiplicity. A proof needs either:

1. a signed affine-plane-to-coordinate transport which uses the higher-shell/R16/outside-window ledger before positivity; or
2. a legitimately proved high-ratio critical-core theorem excluding concentration on the non-coordinate affine-plane sector.

This is not an FEI counterexample. The one-point defect is in the known `H/J<4` affine-defect class, so a high-ratio contradiction proof may exclude it; the calculation refutes only the **all-Boolean direct-coordinate coverage shortcut**.

## 7. Dead route: the quartic count identity is not itself a live-window payment

Equation (4.2) looks strong enough to tempt a shellwise estimate. It is not. If one isolates the positive `q=4` shell and uses only `w_<2(s)<=4/s^3`, `sin theta<=theta`, and even-power positivity of `cos^{N-4} theta`, the entropy-scale prefactor `N` leaves an upper bound of order `N J`, not `J` (even Gaussian damping of the first lobe only reduces the Borel integral by one factor of `N`).

Therefore the quartic shell must **not** be positive-parted and paid separately at the final scale. The exact count identity is useful normalization, but the live proof still needs the signed `q>=6` shells and/or the co-located high/outside-window credits before the final positive physical square. This is consistent with the genuine half-band obstruction already in the joint state.

## 8. Exact remaining implication

After this run, the self-phase version of interface C has the following source-exact chain:

\[
\boxed{
\text{quarter-turn signed packet}
\to \text{self-phase one-cell source }(O=L_U=0)
\to \text{finite low/high/outside split}
\to \text{high refund }\mathcal C_2\le J
\to \text{terminal }0.
}
\]

The remaining universal implication is now:

> **OPEN:** control the one-cell live finite-resolvent source `mathcal H_2` by an orientation-preserving physical-flag contraction **while retaining the signed non-coordinate affine-plane/higher-relation ledger**. The direct coordinate plaquette part is exactly `p_i(w)<=kappa_i(w)`; the non-coordinate part cannot be discarded or assigned to coordinate plaquettes one relation at a time.

A useful next attack is to perform an affine-plane Radon decomposition of the self-phase one-cell source and test whether the random-order Hardy kernel supplies the missing `1/(|U|+1)` cost before R32 shell summation. If the resulting affine-to-coordinate operator has unbounded norm on a genuine **high-ratio restriction-maximal** Boolean family, this self-phase route should be abandoned rather than repaired by absolute values.

**Next recipient:** `account03/B18` for the signed physical sink and critical-core filter, with `account01/B16` for the self-phase quarter-turn source and `account04/B16` for finite-window/high/outside kernel bookkeeping.

**Full unrestricted FEI remains OPEN / NOT PROVED.**

## 9. Decisive computation

The companion standard-library checker verifies the new identities without rerunning the settled FEI certificate. It checks:

- exact quartic count identity (4.1) for every Boolean function in dimensions `n=2,3` and 400 deterministic random Boolean functions at `n=4`;
- the finite-resolvent identity `H_2=H-C_2` and `0<=C_2<=(1-collision)/2` on the same families;
- the coordinate plaquette identity (5.1) on every eligible `(i,w,y)` for those functions;
- the exact one-point-defect plane counts (6.1)-(6.2).

Executed result: **200,457 assertions passed**. Coordinate-plaquette identity checks were 128 at `n=2`, 18,432 at `n=3`, and 179,200 at `n=4`; maximum floating error in the finite-resolvent scalar identity was `4.44e-16`. The maximum observed `C_2/(1-sum p^2)` was `0.3996730127`, below the proved `1/2` bound.

The finite computations are falsification/self-check evidence. The all-dimensional statements above are proved algebraically.

## 10. Joint-order receipt fields

- `consumed_peer_artifact`: `account01/B16/20260921T225305Z-quarterturn-selfphase/REPORT.md`, source commit `5bee3ad064bbb4afab3743cf1d64148cc0c5e017`, blob `da1ddcdc6ff85679c153b1c23ab32b54d6c3ad60`; also applied account04/B16 `20260921T221559Z-cell-mobius-rkhs-orientation` and account03/B18 signed flags.
- `applied_to_claim`: specialize the authentic finite-window two-cell compiler to the Boolean self-phase gate, prove exact one-cell collapse and terminal annihilation, identify/pay the finite-resolvent high refund, and determine exactly which quartic relations map directly to physical flags.
- `remaining_implication`: signed affine-plane/higher-shell to ordered physical-flag contraction for the one-cell live finite-resolvent source, or a rigorous high-ratio critical-core reduction which removes the non-coordinate obstruction.
- `next_recipient`: `account03/B18` (physical signed sink/critical core), `account01/B16` (self-phase source), `account04/B16` (finite-window refund ledger).
- `full_problem_change`: full FEI remains OPEN; terminal and generic two-cell-overlap complications disappear for the self-phase gate, and the finite-resolvent high refund is explicitly at most `J`, but the live one-cell contraction remains unpaid.
- `mechanism_change`: yes — from generic parent/coset contraction to a single Boolean self-phase gate plus a direct classification of the coordinate versus non-coordinate quartic source.
