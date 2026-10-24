# B18 FEI proof integration — affine-defect critical-core descent and the surviving interface-C normalization gap

**Date:** 21 September 2026  
**Scope:** `account03 / B18`, joint FEI interface C  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Full unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** a new all-dimensional theorem for affine-subspace defect phases, an exact exclusion of the current half-band obstruction from restriction-maximal cores, and a sharpened statement of what still blocks the authentic parent/signed-sink interface. No publication-priority claim.

## 0. Why this run changes mechanism

The preceding B18 run proved that the complete **positive** half-band central current cannot contract with universal distortion into the `O(J)` signed physical flag bank. The counterfamily has positive live current of order `n^{-3}` while `J` is exponentially small, but its own Fourier entropy ratio is below four. The immediate replacement choices were therefore:

1. retain a genuine signed source credit before positivity; or
2. prove that a legitimate restriction-maximal/high-ratio critical-core reduction excludes the counterfamily before interface C is invoked.

This run executes the second mechanism rather than repeating another positive-current estimate or moment-credit test.

The completed cross-account artifact used substantively is

`proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260921T190755Z-affine-subspace-plaquette-payment/REPORT.md`.

It introduces the exact affine-subspace parent geometry: for `Q=a+L`, codimension `c`, quotient map `pi`, and

`m_L = #{i : pi(e_i) != 0}`,

the folded influence is `J(g_Q)=m_L 2^(1-c)` for `c>=2`, and the plaquette response depends only on the rank of the quotient shifts. I use that same quotient representation below to analyze **physical restrictions**, not merely plaquettes.

I also retain the authentic account02/B16 parent representation

`account02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`:
its actual compiler parents are coordinate one-subcube defects. The result below shows exactly why the known global half-band witness can be removed by critical descent while those authentic local parents cannot be wished away by the same argument.

## 1. Exact entropy and folded influence of every affine-subspace defect

Let

`G=F_2^n`, `Q=a+L`, `codim(L)=c`,

and

`g_Q(x)=1-2 1_Q(x)`.

Write `delta=2^{-c}` and let `V=G/L`. For every Fourier character `chi_S`,

`hat g_Q(empty)=1-2 delta`,

while for nonzero `S`

`hat g_Q(S) = -2 delta chi_S(a)` if `S in L^perp`, and is zero otherwise.

Hence the spectral law has one atom

`p_0=(1-2 delta)^2`

and `2^c-1` equal nonzero atoms

`p_1=4 delta^2`.

Let

`r_c=(2^c-1)p_1 = 4 delta(1-delta)`.

Therefore the Fourier entropy depends **only** on the codimension:

\[
\boxed{
H(g_Q)=H_c:=h_2(r_c)+r_c\log_2(2^c-1).
}
\tag{1.1}
\]

Now let

`m=m_L=#{i:e_i notin L}=#{i:pi(e_i)!=0}`.

If `e_i in L`, translation by `e_i` preserves `Q`, so the `i`-influence is zero. If `e_i notin L`, `Q` and `Q+e_i` are distinct cosets and are disjoint, so the disagreement probability is exactly

`2 delta = 2^(1-c)`.

For `c>=2` this is already at most `1/2`, hence it is unchanged by folding. Thus

\[
\boxed{
J(g_Q)=m\,2^{1-c}.
}
\tag{1.2}
\]

The nonzero quotient columns `pi(e_i)` span the `c`-dimensional quotient, so `m>=c`.

### Theorem 1 — every affine-subspace defect is a sub-four-ratio function — PROVED

For every `c>=2`,

\[
\boxed{H(g_Q)<4J(g_Q).}
\tag{1.3}
\]

For `c=1`, `g_Q` is a character up to sign and both Fourier entropy and folded influence are zero.

### Proof

It is enough to use `m>=c`, so `J(g_Q)>=2c delta`.

The standard binary-entropy bound

`h_2(r)<=r log_2(e/r)`

and `r_c=4 delta(1-delta)` give

`log_2(e/r_c)=c+log_2(e/[4(1-delta)])`.

For `c>=2`, `delta<=1/4`, hence `4(1-delta)>=3>e`, so

`log_2(e/r_c)<c`.

Also `log_2(2^c-1)<c`. Therefore

`H_c < 2 c r_c = 8 c delta(1-delta) < 8 c delta <=4J(g_Q)`.

This proves (1.3). QED.

This is not full FEI; it closes only this explicit affine-defect class with constant four.

## 2. PROVED — redundant quotient coordinates force a strict ratio-improving restriction

Choose a basis of `V=G/L` and represent the quotient map by a full-rank binary matrix

`A:F_2^n -> F_2^c`,

whose `i`th column is

`v_i=A e_i=pi(e_i)`.

Thus `m` is exactly the number of nonzero columns of `A`.

### Theorem 2 — `P03-B18-AFFINE-DEFECT-CRITICAL-DESCENT` — PROVED

Assume `c>=2` and `m>c`. Then there is a physical coordinate `i` such that **both** restrictions `x_i=0` and `x_i=1` which meet the affine defect produce affine-subspace defects on the `(n-1)`-cube with

- the same codimension `c`;
- the same Fourier entropy `H_c`;
- exactly `m-1` nontrivial physical quotient columns; and therefore

\[
\boxed{
\frac{H(g_Q|_{x_i=b})}{J(g_Q|_{x_i=b})}
=\frac{m}{m-1}\frac{H(g_Q)}{J(g_Q)}
>\frac{H(g_Q)}{J(g_Q)}
}
\tag{2.1}
\]

for each nonempty child.

Consequently **no affine-subspace defect with `m>c` is restriction-maximal for `H/J`**.

### Proof

The `m` nonzero columns span a `c`-dimensional space and `m>c`, so at least one nonzero column `v_i` is redundant: deleting it leaves rank `c`.

Equivalently `v_i` lies in the span of the remaining columns, so there exists a kernel vector `ell in ker A=L` with `ell_i=1`. Hence the coordinate `x_i` is nonconstant on every affine coset of `L`; both coordinate halves intersect `Q`.

After fixing `x_i=b`, the child affine set is described by the full-rank matrix obtained by deleting column `i`; its right-hand side is merely shifted by `b v_i`. The child therefore has the same codimension `c`. Exactly one nonzero quotient column was removed, so its physical incidence count is `m-1`.

Equation (1.1) gives the same entropy `H_c` in parent and child, while (1.2) gives folded influences `m2^(1-c)` and `(m-1)2^(1-c)`. Their ratio is (2.1). QED.

## 3. Exact classification of the irredundant affine-defect branch

If `m=c`, the `c` nonzero quotient columns already form a basis. Every zero column satisfies `e_i in L`. There are `n-c` zero columns, and these coordinate vectors span an `(n-c)`-dimensional subspace contained in `L`; since `dim L=n-c`, they span all of `L`.

Thus:

### Corollary 3 — affine-defect critical normal form — PROVED

An affine-subspace defect has no strict ratio-improving restriction of the type in Theorem 2 **only if its direction subspace is a coordinate subspace**, i.e. `Q` is a coordinate subcube.

Every free coordinate of such a subcube may be restricted away without changing `c`, `m=c`, `H`, `J`, or `H/J`. Therefore a **minimum-dimensional** restriction-maximal affine-subspace defect is exactly a one-point defect on a `c`-cube.

All of these still satisfy `H/J<4` by Theorem 1.

This is a classification inside the affine-defect family only; it is not a classification of arbitrary Boolean critical cores.

## 4. Application to the authentic half-band no-go family

The current positive-current obstruction, after the mandatory dummy split, has negative affine plane direction

\[
L=\operatorname{span}(e_2+e_3,e_D)\subseteq F_2^D.
\]

Hence

`c=D-2`.

The dummy column `e_D` lies in `L` and is quotient-zero, while every other physical coordinate has nonzero quotient image. Therefore

`m=D-1=c+1`.

Moreover `pi(e_2)=pi(e_3)`, so either coordinate `2` or `3` is an explicit redundant nonzero column. Restricting it gives two nonempty children with the **same** codimension `c` and `m'=c`. Thus

\[
\boxed{
\frac{H_{child}}{J_{child}}
=\frac{D-1}{D-2}\frac{H_{parent}}{J_{parent}}.
}
\tag{4.1}
\]

So the exact Boolean family that refutes an all-Boolean positive interface-C contraction is **not** a restriction-maximal `H/J` core. This is a genuine removal of that particular obstruction from a restriction-maximal contradiction proof; it is not an assertion that every critical core now obeys the desired compiler inequality.

This also explains geometrically why the witness had a cheaper one-point-defect child: the two correlated physical columns represent the same quotient direction.

## 5. Why this does NOT close interface C

The critical-descent theorem removes the known global half-band witness, but it does not make account02's authentic parents disappear.

The authentic account02/B16 parent `g_j` is already a **coordinate one-subcube defect**, hence it lies exactly in the irredundant `m=c` branch of Corollary 3. For such a parent, the previously proved account03/B18 signed-pivot theorem gives, on every frustrated pair,

\[
\boxed{
\kappa_i(w)=P_{g_j}(u,v)=2^{2-c}=\frac{2}{c}J(g_j).
}
\tag{5.1}
\]

So once an authentic positive physical pair measure exists, there is no orientation mismatch with the signed sink.

But account02/B16's later codimension-normalization theorem shows that if a scalar source charge `eta` is required to be reconstructed by

`eta = integral P_{g_j}(u,v) dLambda(u,v)`,

then

\[
\boxed{
\|\Lambda\|_{TV}\ge2^{c-2}|\eta|,
\qquad
J(g_j)\|\Lambda\|_{TV}\ge\frac c2|\eta|.
}
\tag{5.2}
\]

Thus the two facts are perfectly compatible:

- **PROVED:** a genuinely given pair law lands exactly in the signed physical sink, equation (5.1);
- **REFUTED as a dimension-free generic route:** first compress the signed source to a scalar parent mass and then invert the tiny plaquette amplitude by positive/TV reconstruction, equation (5.2).

The source mass `mu_j` from account02 is an energy marginal, not already an identity `mu_j=integral P dLambda`. Conflating those two statements was the normalization hazard.

Therefore the surviving source-exact interface is still the precompression one:

\[
\boxed{
\text{signed dual-code field}
\to \Delta_{g_{j,0}}\Delta_{g_{j,1}}\Delta_f\Psi_s
\to \text{compensated live-window signed square}
\to \text{physical }\kappa\text{ sink},
}
\tag{5.3}
\]

or, alternatively, a genuinely proved codimension-weighted source estimate sufficient to pay (5.2).

## 6. Decisive computation

`check_affine_defect_critical_descent.py` uses only the Python standard library. It exhausts all full-rank parity-check matrices for

`3<=n<=5`, `2<=c<n`.

The executed result is:

- `654,702` full-rank quotient representations checked;
- `551,436` redundant cases with `m>c`;
- every one of those `551,436` cases had a deletable nonzero physical quotient column preserving rank `c`;
- the exact ratio-improvement factor `m/(m-1)` was checked in every redundant case;
- every `m=c` case had exactly `c` independent nonzero columns, as required by Corollary 3;
- a floating diagnostic through codimension `50` gave one-point-defect ratio below `4` throughout (the all-dimensional `<4` statement is proved analytically in Section 1).

The recorded checker output is adjacent to this report. The finite computation is falsification/self-check evidence, not the proof of the all-dimensional statements.

## 7. Classification, joint handoff, and next exact implication

### PROVED

1. Exact Fourier entropy and folded influence formulas (1.1)-(1.2) for every affine-subspace defect.
2. Every affine-subspace defect satisfies `H<4J`.
3. If its physical quotient representation has redundancy `m>c`, a physical coordinate restriction strictly increases `H/J` by `m/(m-1)` while preserving codimension.
4. The minimum-dimensional irredundant affine-defect branch consists of one-point defects.
5. The specific half-band family that killed universal positive interface C has `m=c+1` and is therefore not restriction-maximal.

### REFUTED / DEAD

- The half-band family is **not** a counterexample to a compiler theorem explicitly restricted to a legitimate restriction-maximal critical core.
- Scalar postcompression followed by positive/TV plaquette inversion remains non-dimension-free on the surviving coordinate-subcube parents; critical descent does not repair that normalization loss.

### CONDITIONAL / OPEN

A restriction-maximal/high-ratio-core version of interface C is now compatible with the known half-band obstruction, but no universal contraction on that class has been proved. The authentic parent masks themselves survive the descent and still require the precompression signed/refunded transfer.

**Full unrestricted FEI remains OPEN / NOT PROVED.**

### Joint-order receipt fields

- `consumed_peer_artifact`: `account02/B18/20260921T190755Z-affine-subspace-plaquette-payment/REPORT.md`, together with the authentic-parent input `account02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`.
- `applied_to_claim`: determine whether the known affine half-band obstruction actually blocks an interface-C theorem after the legitimate restriction-maximal critical-core reduction, and identify which account02 parent masks survive that reduction.
- `remaining_implication`: prove a source-exact compensated live-window contraction for restriction-maximal/high-ratio cores at the precompression three-phase field level, or produce a new **restriction-maximal** Boolean counterexample; do not return to scalar positive parent reconstruction.
- `next_recipient`: `account03/B16` for compensated finite-window precompression, with `account02/B16` for source-side parent normalization and `account03/B17` for a critical-core adversary search.
- `full_problem_change`: full FEI remains OPEN; one known all-Boolean interface-C obstruction is proved irrelevant to restriction-maximal cores, but the universal critical-core compiler step is unpaid.
- `mechanism_change`: yes — from universal positive-current compensation to exact restriction-critical geometry plus precompression signed transport.
