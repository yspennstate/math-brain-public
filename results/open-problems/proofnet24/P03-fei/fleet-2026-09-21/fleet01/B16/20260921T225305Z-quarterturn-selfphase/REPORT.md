# B16 FEI signed transport — quarter-turn MacWilliams source transform, self-phase terminal annihilation, and a post-square R16 no-go

**Date:** 21 September 2026  
**Scope:** fleet01 / B16, signed transport / noise interpolation, interface C  
**Execution:** WITHOUT_VERIFIED_BRAIN  
**Full unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact source identities, an exact one-gate terminal-elimination lemma, a local influence envelope, and a rigorous obstruction to spending the aggregate R16 bank only after a positive current has been formed. No novelty or publication-priority claim.

## 0. Fresh state and required peer result consumed

This run changes method from the preceding threshold-boundary/Krawtchouk attempt rather than trying another positive Brownian estimate.

The named other-account result consumed substantively is the fleet02 interactive package

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/interactive/20260921T204926Z-threshold-contraction/HALFBAND_COLLISION_EXTENSION.md`

(package `dfb0dffbe472f19a15e3c3b22bc563d527a979ab`).  It proves for the actual half-band compiler, with the genuine retained terminal code, active-syndrome law and current multipliers, an explicit Boolean family with

\[
J(f)=\frac{8(D-1)}{2^D},\qquad H(f)<4I(f),
\]

but exact positive live current

\[
L_D:=\int_{40}^{S_f}\frac{E_{\rm cur}(s)}{s^3}\,ds
\ge \frac{7}{3145728(D-1)^3},\qquad D\ge128,
\]

and in fact `L_D ~ 4/[27(D-1)^3]`.  Thus this is not an FEI counterexample; it is a source-valid obstruction to throwing away the compensating signed ledger.

I also consume fleet04/B16

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B16/20260921T213921Z-finite-resolvent-rkhs-refund/REPORT.md`.

That report proves that the small-resolvent and R16 high-resolvent multipliers are co-located on the **same signed precompression gate packet**, with

\[
 w_{<2}(s)+w_{>2}(s)=\frac4{s^3},
\]

and that the refund has to be inserted before the final positive local square.  The present run gives a direct algebraic reason that this placement is unavoidable, then replaces the threshold boundary basis by a quarter-turn characteristic-function basis in which all R32 shell signs and the terminal subtraction are retained exactly.

The preceding fleet01/B16 result used here is

`20260921T214038Z-threshold-boundary-krawtchouk/REPORT.md`.

It showed that a fixed shell-parity sign cannot pay the Brownian threshold pointwise.  We therefore do not retry that bridge.

---

## 1. RIGOROUS OBSTRUCTION — an aggregate R16 bank cannot be subtracted only after the positive half-band current is formed

The inherited high-resolvent compression gives

\[
\mathcal B_d=\kappa_2J-\Delta_{d,>2},
\qquad
\kappa_2=\frac23+\operatorname{artanh}(1/2),
\]

and

\[
\Delta_{\infty,>2}\ge0,
\qquad
|\Delta_{\infty,>2}-\Delta_{d,>2}|\le \varepsilon_dJ,
\qquad
\varepsilon_d=2^{3-2^d}.
\]

Hence

\[
\boxed{\mathcal B_d\le(\kappa_2+\varepsilon_d)J.}
\tag{1.1}
\]

Combine (1.1) with the fleet02 half-band family.  Writing `n=D-1`,

\[
\frac{L_D}{J}
\ge
\frac{7\,2^{D-23}}{3n^4}
\longrightarrow\infty.
\tag{1.2}
\]

Therefore, for **every fixed** `a,K<infinity`, the all-Boolean estimate

\[
\boxed{L_D\le a\,\mathcal B_{d_h}+KJ}
\tag{1.3}
\]

fails for all sufficiently large members of this explicit family.

This kills a stronger version of the target suggested by the previous B16 boundary-polynomial report: no Christoffel--Darboux or Krawtchouk manipulation can first turn the source into the already-positive live current and then hope that a fixed multiple of the aggregate R16 bank cancels it.  The bank is itself `O(J)`, whereas that positive current is not.

The only viable use of R16 in this compiler organization is the one identified by fleet04: the signed high-resolvent/terminal refund must be inserted **before** the local square or positive current is formed.  This is the method change for the present run.

---

## 2. Quarter-turn transform for an arbitrary authentic mask code

Let the truth-table length be `N=2^n`, let

\[
V=\mathbb F_2^N,
\]

and let `M<=V` be a linear mask code containing `RM(1,n)`.  Put

\[
D=M^\perp\subseteq C_0:=RM(1,n)^\perp.
\]

For a Boolean phase vector `b in V`, write

\[
f_x=(-1)^{b_x},\qquad
f_A=(-1)^{\langle b,A\rangle},
\]

and define the normalized correlation

\[
\beta_b(m)=\frac1N\sum_x(-1)^{b_x+m_x}.
\tag{2.1}
\]

The comparator is `b=0`.  Define the signed characteristic-function packet

\[
\boxed{
\Xi_{M,b}(s)
:=\mathbb E_{m\in M}\cos(s\beta_0(m))
 -\mathbb E_{m\in M}\cos(s\beta_b(m)).
}
\tag{2.2}
\]

### Theorem 2.1 — `P03-B16-QUARTER-TURN-MACWILLIAMS`

For every real `s`,

\[
\boxed{
\Xi_{M,b}(s)
=2\sum_{\substack{A\in D\\ f_A=-1}}
(-1)^{|A|/2}
\sin^{|A|}(s/N)\cos^{N-|A|}(s/N).
}
\tag{2.3}
\]

In particular every `0 mod 4 / 2 mod 4` R32 sign is preserved before any positivity step.

### Proof

Put `theta=s/N`.  Expand

\[
\mathbb E_{m\in M}
\exp\!\left(i\theta\sum_x(-1)^{b_x+m_x}\right).
\]

For fixed `m`, the exponential is

\[
\prod_x\left(\cos\theta+i(-1)^{b_x+m_x}\sin\theta\right).
\]

After expansion, averaging `(-1)^{\langle m,A\rangle}` over `M` kills every `A` outside `D=M^perp`.  Since the constant-one mask lies in `RM(1,n)\subseteq M`, every `A\in D` has even weight, so

\[
i^{|A|}=(-1)^{|A|/2}.
\]

Thus the average exponential equals

\[
\sum_{A\in D}
(-1)^{|A|/2}f_A
\sin^{|A|}\theta\cos^{N-|A|}\theta.
\]

The constant-one mask also pairs every `m` with its complement, so the average is real and equals the cosine average in (2.2).  Subtract the `b` expression from the comparator expression; `1-f_A` is two exactly on the frustrated relations and zero otherwise.  This proves (2.3).  QED.

### Corollary 2.2 — exact retained-shell transform

Let `M_0=RM(1,n)` and let `M_d` be any later code containing it, with duals `C_0` and `D_d`.  Then the inherited signed retained-shell packet

\[
\mathfrak G_d(s)
=2N\sum_{\substack{A\in C_0\setminus D_d\\f_A=-1}}
(-1)^{|A|/2}\sin^{|A|}(s/N)\cos^{N-|A|}(s/N)
\]

has the exact characteristic-function representation

\[
\boxed{
\mathfrak G_d(s)
=N\bigl(\Xi_{M_0,b}(s)-\Xi_{M_d,b}(s)\bigr).
}
\tag{2.4}
\]

So terminal subtraction and R32 shell signs are simply a **difference of two genuine mask-code characteristic functions**.  No Brownian square, positive current or relationwise absolute value is required to see them.

---

## 3. PROVED — exact entropy transform and identification of the terminal endpoint

Because `M` contains `RM(1,n)`, its dual contains no nonzero word of weight two.  Expanding the second moment of (2.1) therefore gives, for every phase `b`,

\[
\boxed{
\mathbb E_{m\in M}\beta_b(m)^2=\frac1N.
}
\tag{3.1}
\]

Thus the mass and quadratic terms of the two characteristic functions in (2.2) match, and `Xi_{M,b}(s)=O(s^4)` at the origin.

Put

\[
\psi(t)=-t^2\log(t^2),\qquad \psi(0)=0,
\]

with natural logarithms, and define

\[
\Theta_M(b)
:=N\left[
\mathbb E_M\psi(\beta_b)-\mathbb E_M\psi(\beta_0)
\right].
\tag{3.2}
\]

### Theorem 3.1 — `P03-B16-MATCHED-MOMENT-ENTROPY-TRANSFORM`

\[
\boxed{
4N\int_0^\infty\frac{\Xi_{M,b}(s)}{s^3}\,ds
=\Theta_M(b).
}
\tag{3.3}
\]

### Proof

For bounded random variables `X,Y` with `EX^2=EY^2`, set

\[
\Phi(s)=\mathbb E\cos(sY)-\mathbb E\cos(sX).
\]

The matched second moment gives `Phi(s)=O(s^4)` at zero.  Two integrations by parts are therefore legitimate and give

\[
\int_0^\infty\frac{\Phi(s)}{s^3}ds
=\frac12\int_0^\infty\frac{
\mathbb E[X^2\cos(sX)-Y^2\cos(sY)]}{s}\,ds.
\]

Use the equal second moments to insert a common reference cosine and apply the Frullani cosine identity.  The result is

\[
4\int_0^\infty\frac{\Phi(s)}{s^3}ds
=\mathbb E\psi(X)-\mathbb E\psi(Y).
\]

Take `X=beta_b`, `Y=beta_0` and multiply by `N`.  QED.

### Corollary 3.2 — the base code is exactly Fourier entropy

For `M_0=RM(1,n)`, the affine masks run through the Walsh characters with both global signs.  Hence `beta_b` runs through `+/- fhat(S)`, while `beta_0` is `+/-1` on the two constant masks and zero on every nonconstant character.  Therefore

\[
\boxed{\Theta_{M_0}(b)=H_{\rm nat}(f).}
\tag{3.4}
\]

Combining (2.4), (3.3), (3.4), and the inherited exact identity

\[
4\int_0^\infty\frac{\mathfrak G_d(s)}{s^3}ds
=H_{\rm nat}(f)-R_d(f)
\]

gives the terminal endpoint in a new exact form:

\[
\boxed{
R_d(f)=\Theta_{M_d}(b)
=N\left[
\mathbb E_{M_d}\psi(\beta_b)
-
\mathbb E_{M_d}\psi(\beta_0)
\right].
}
\tag{3.5}
\]

Thus the terminal term is not an opaque external remainder: it is exactly the residual entropy difference of the two mask-code correlation laws.

---

## 4. PROVED — one self-phase gate annihilates the terminal characteristic function pointwise

### Theorem 4.1 — `P03-B16-SELF-PHASE-TERMINAL-ANNIHILATION`

If `b in M`, then

\[
\boxed{\Xi_{M,b}(s)\equiv0\quad\text{for every }s,\qquad \Theta_M(b)=0.}
\tag{4.1}
\]

### Proof

Translation `m -> m+b` is a permutation of `M`, and

\[
\beta_b(m)=\beta_0(m+b).
\]

Hence the two correlation laws in (2.2) are identical, pointwise in their characteristic functions.  QED.

Take now

\[
\boxed{M_f:=RM(1,n)+\langle b_f\rangle.}
\tag{4.2}
\]

If `f` is a character then `b_f in RM(1,n)` and `H(f)=0`.  Otherwise (4.2) is a single index-two extension and (4.1) gives

\[
\boxed{\Theta_{M_f}(b_f)=0.}
\tag{4.3}
\]

Its dual is

\[
\boxed{
M_f^\perp
=C_0\cap\{A:f_A=+1\}.
}
\tag{4.4}
\]

So every frustrated relation is first-separated by this one self-phase generator and no frustrated terminal relation remains.

This is an algebraic one-gate reorganization of the source, not yet a payment theorem.  It is nevertheless compatible with fleet04's finite-resolvent precompression formula because that formula is valid for a genuine Boolean gate mask before scalar parent compression.

### Physical cost of the self-phase gate

Apply the minimizing-character gauge first: choose a character `chi_T` so that `F=f chi_T` has coordinate influences

\[
\operatorname{Inf}_i(F)=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\}.
\]

Let `b_F` be the truth-table mask of `F`.  Its physical edge boundary is exactly

\[
\boxed{
\sum_i\Pr[b_F(x)\ne b_F(x+e_i)]
=J(f).
}
\tag{4.5}
\]

Thus the same single generator that annihilates the terminal characteristic function has **exact physical boundary `J(f)`**.  What is missing is a source-to-oriented-curvature inequality that uses this boundary without positive-parting the long Borel corridor.  The half-band obstruction in Section 1 shows why that last qualification is essential.

---

## 5. A direct local influence envelope for the self-phase packet

For `M_0=RM(1,n)`, write

\[
p_S=\widehat F(S)^2,
\qquad p_\varnothing=\widehat F(\varnothing)^2,
\]

in the minimizing-character gauge.  The self-phase packet has the scalar form

\[
\boxed{
N\Xi_{M_0,b_F}(s)
=\cos s-\cos(s\sqrt{p_\varnothing})
+\sum_{S\ne\varnothing}\left[1-\cos(s\sqrt{p_S})\right].
}
\tag{5.1}
\]

(The signs of Fourier coefficients disappear because cosine is even.)

### Lemma 5.1 — all-scale pointwise upper envelope

For every real `s`,

\[
\boxed{
N\Xi_{M_0,b_F}(s)\le s^2J(f).
}
\tag{5.2}
\]

Indeed, `t -> cos(s sqrt(t))` is `s^2/2`-Lipschitz on `[0,1]` because `|sin z|<=|z|`, while

\[
1-\cos(s\sqrt p)\le\frac12s^2p.
\]

Therefore the first term of (5.1) is at most `s^2(1-p_empty)/2` and the nonconstant sum is at most the same quantity.  Finally

\[
1-p_\varnothing=\sum_{S\ne\varnothing}p_S
\le\sum_S|S|p_S=I(F)=J(f).
\]

### Lemma 5.2 — quartic small-scale envelope

For `0<=s<=1`,

\[
\boxed{
0\le N\Xi_{M_0,b_F}(s)
\le\frac{s^4}{24}\left(1-\sum_Sp_S^2\right)
\le\frac{s^4}{12}J(f).
}
\tag{5.3}
\]

Proof.  Put `F_s(x)=1-cos(s sqrt(x))`.  On `[0,1]`,

\[
F_s''(x)=\frac{s^4}{4z^3}(z\cos z-\sin z),\qquad z=s\sqrt x.
\]

For `0<=z<=1`, `F_s''<=0` and

\[
0\le -F_s''(x)
=\frac{s^4}{4z^3}(\sin z-z\cos z)
\le\frac{s^4}{12},
\]

because `sin z-z cos z=int_0^z t sin t dt <=z^3/3`.  The error above the endpoint chord is therefore between zero and

\[
\frac{s^4}{24}x(1-x).
\]

Summing this chord error over the probabilities `p_S` gives the first inequality in (5.3).  The inherited collision bound `1-sum p_S^2<=2J` gives the second.  QED.

This proves a genuine dimension-free payment at microscopic Borel scales.  It also identifies the remaining problem cleanly: integrating only the coarse envelope (5.2) against `ds/s^3` creates a logarithmic corridor, exactly the kind of positive expenditure that the fleet02 half-band construction shows cannot be paid after the signed refunds are discarded.

---

## 6. What changed and the next B16 implication

The preceding threshold/Krawtchouk route asked an integrated positive boundary square to be compensated by R16.  Section 1 proves that no fixed aggregate R16 bank can do that after positivity: the bank is `O(J)` and the authentic positive half-band current is not.

The replacement source object is now the signed characteristic function `Xi` of (2.2).  It has four useful properties simultaneously:

1. it is **exactly** the R32 shell packet by (2.3), preserving every parity credit;
2. terminal subtraction is just the difference `Xi_M0-Xi_Md` by (2.4);
3. its full `s^-3` integral is exactly an entropy difference by (3.3);
4. the self-phase extension `RM(1,n)+<b_F>` kills the terminal law pointwise while its gate boundary is exactly `J(f)`.

The next nonoverlapping target is therefore not another positive-current estimate.  It is to insert fleet04's co-located high-resolvent and outside-window terms **inside the self-phase local square/root-resolvent field**, exploit the special symmetry `g=b_F`, and prove a signed carré-du-champ/noise interpolation inequality against the physical edge boundary (4.5).  Lemmas 5.1--5.2 pay the microscopic scale already; the only live part is the oscillatory logarithmic corridor where signed cancellation is indispensable.

If even the fully refunded self-phase local field has a Boolean family whose signed value divided by `J` diverges, then this one-gate reorganization is dead and B16 should leave interface C rather than return to the refuted positive-current target.

**Full FEI remains OPEN / NOT PROVED.**

---

## 7. Exact checker scope

The companion standard-library checker uses exact rational/Gaussian-rational arithmetic for all algebraic finite-cube statements.  On deterministic Boolean phases in dimensions two and three it checks:

- 24 exact quarter-turn/MacWilliams polynomial identities coefficient-by-coefficient;
- 24 exact matched-second-moment identities `E beta_b^2=E beta_0^2=1/N`;
- 24 exact self-phase correlation-law permutations after adjoining `b`;
- 24 exact dual classifications `D_self={A in C_0:f_A=+1}`;
- 24 base-code entropy identities numerically only at the final logarithm evaluation (the Fourier/correlation inputs are exact rationals).

Total: 120 checks, all passed in the producing invocation.  The analytic proofs above do not depend on extrapolating those finite checks.
