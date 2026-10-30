TASK: B13 ACCOUNT: fleet02 RUN: 2026-09-21T16:54:19.890165Z — derivative Palm block complementarity, exact multiscale collision conservation, and a signed-coherence obstruction

MODEL: GPT-5.6 Sol  
THINKING LEVEL: UNKNOWN; requested=maximum actually supported; configured/runtime selector not exposed  
THINKING USAGE: provider reasoning tokens/time NOT_EXPOSED  
RESEARCH EXECUTION: WITHOUT_VERIFIED_BRAIN. No authenticated brain retrieval or receiver-side brain context was consumed.

# Status

**Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

This run follows the later direct owner order `FEI-SEVEN-TASKS-2026-09-21`, not the stale provisional benchmark row for B13. The scope is FEI approach 2/13: Boolean block-influence/correlation profiles and two-sided Booleanity constraints.

The preceding B13 run showed that one-point defects simultaneously saturate every raw one-block parity atom cap and kill any fixed-fraction macroscopic projection-credit lemma. The required next move was therefore genuinely multiscale. This run supplies an exact all-block conservation law for each Boolean derivative Palm row. It couples an **input-side sensitive-fibre projection profile** to the matching **spectral Palm projection profile**, with two explicit nonnegative residual banks: block entanglement and mixed-basis signed coherence. Averaging over block sizes gives an exact radial Hamming-distance transform identity at every scale.

The same theorem also exposes a decisive obstruction: a point-gated arbitrary Boolean residual has the same physical sensitive-support projection law for every residual block, while its Palm spectral entropy can range from zero to the full residual dimension. A bent residual places almost the entire complementarity budget in the mixed-axis signed-coherence bank. Thus support-only or unsigned collision bookkeeping cannot close FEI; the signed bank is structurally necessary.

No publication-priority claim is made.

# 1. Boolean derivative as one normalized state with two observable block profiles

Work on `F_2^n`, with normalized Walsh coefficients

\[
\widehat f(S)=2^{-n}\sum_x f(x)(-1)^{S\cdot x},
\qquad
\mu(S)=\widehat f(S)^2.
\]

Fix a coordinate `i` with

\[
p_i=\operatorname{Inf}_i(f)>0,
\]

put `m=n-1`, and define the additive derivative on the remaining cube by

\[
g_i(y)=\frac{f(0,y)-f(1,y)}2\in\{-1,0,1\}.
\tag{1.1}
\]

Then

\[
p_i=2^{-m}\sum_y g_i(y)^2,
\qquad
\widehat g_i(A)=\widehat f(A\cup\{i\}).
\tag{1.2}
\]

Normalize the derivative as the real unit vector

\[
\psi_i(y)=\frac{g_i(y)}{\sqrt{2^m p_i}}.
\tag{1.3}
\]

There are two canonical probability laws attached to the **same** vector.

## Physical sensitive-fibre law

Let `X_i` have law

\[
\Pr[X_i=y]=|\psi_i(y)|^2.
\tag{1.4}
\]

Because `f` is Boolean, `g_i^2` is an indicator. Hence `X_i` is exactly **uniform on the sensitive `i`-fibres**. This flatness is the Boolean input-side constraint.

## Spectral Palm law

Let `H_m` be the unitary Walsh transform and let `Y_i` have law

\[
\Pr[Y_i=A]=|(H_m\psi_i)(A)|^2
=\frac{\widehat g_i(A)^2}{p_i}
=\Pr_\mu[S\setminus\{i\}=A\mid i\in S].
\tag{1.5}
\]

Thus `Y_i` is exactly the one-coordinate spectral Palm row used in the current B12 sequential programme.

For a coordinate block `J subseteq [n]\setminus\{i\}` of size `q`, write `X_{i,J}` and `Y_{i,J}` for the corresponding projections. Let

\[
\rho_{i,J}=\operatorname{Tr}_{J^c}|\psi_i\rangle\langle\psi_i|
\tag{1.6}
\]

be the reduced density matrix on the `q` block coordinates. This is only linear algebra notation: all entries are explicit normalized signed overlaps of derivative slices.

The physical projection probabilities are the diagonal of `rho` in the standard basis. The spectral Palm projection probabilities are the diagonal of `H_J rho H_J` in the standard basis. The unitary on the traced-out coordinates cancels under the partial trace, so this statement is exact.

# 2. PROVED: exact block collision-complementarity conservation

For a finite law `P`, let its collision probability be

\[
\operatorname{Coll}(P)=\sum_x P(x)^2.
\]

Set

\[
C^{\rm phys}_{i,J}=\operatorname{Coll}(X_{i,J}),
\qquad
C^{\rm spec}_{i,J}=\operatorname{Coll}(Y_{i,J}),
\tag{2.1}
\]

and `d=2^q`. Define the linear-entanglement bank

\[
E_{i,J}=1-\operatorname{tr}(\rho_{i,J}^2)\ge0,
\tag{2.2}
\]

and the mixed-basis remainder

\[
R_{i,J}
=\operatorname{tr}(\rho_{i,J}^2)+d^{-1}
-C^{\rm phys}_{i,J}-C^{\rm spec}_{i,J}.
\tag{2.3}
\]

## Theorem B13-DERIVATIVE-BLOCK-COMPLEMENTARITY-01

For every Boolean `f`, every `i` with `p_i>0`, and every block `J` disjoint from `i`,

\[
\boxed{R_{i,J}\ge0}
\tag{2.4}
\]

and therefore the exact four-bank conservation law holds:

\[
\boxed{
C^{\rm phys}_{i,J}
+C^{\rm spec}_{i,J}
+E_{i,J}
+R_{i,J}
=1+2^{-q}.
}
\tag{2.5}
\]

In particular,

\[
\boxed{
C^{\rm phys}_{i,J}+C^{\rm spec}_{i,J}
\le1+2^{-q}.
}
\tag{2.6}
\]

### Proof

Let `rho=rho_{i,J}` and

\[
\tau=\rho-I_d/d.
\]

In Hilbert--Schmidt inner product, dephasing in the standard basis is the orthogonal projection onto the standard-diagonal operator subspace, and dephasing in the Walsh basis is the orthogonal projection onto the Walsh-diagonal subspace. After the scalar identity direction is removed, these two subspaces are orthogonal: a traceless Walsh-diagonal operator has zero diagonal in the standard basis because the two bases are mutually unbiased.

Let `P_Z` and `P_X` denote these two traceless orthogonal projections. Then

\[
C^{\rm phys}_{i,J}-d^{-1}=\|P_Z\tau\|_2^2,
\qquad
C^{\rm spec}_{i,J}-d^{-1}=\|P_X\tau\|_2^2.
\tag{2.7}
\]

Orthogonality gives

\[
\|P_Z\tau\|_2^2+\|P_X\tau\|_2^2
\le\|\tau\|_2^2
=\operatorname{tr}(\rho^2)-d^{-1}.
\tag{2.8}
\]

Rearranging (2.8) is exactly (2.4). Equation (2.5) is then the definition of the two nonnegative residual banks, and (2.6) follows by dropping them. QED.

### Interpretation

`E_{i,J}` is ordinary linear entanglement of the derivative state across the cut `J | J^c`; it vanishes when the normalized derivative state factors across that cut.

`R_{i,J}` is different. It is the squared Hilbert--Schmidt mass of the traceless reduced state that is visible in neither the all-standard nor all-Walsh diagonal subspace. In Pauli language it contains mixed-axis strings (and, when present, the corresponding even-`Y` signed coherence). It can be large even for a completely unentangled product state whose coordinates split between standard- and Walsh-oriented factors.

This distinction is important below.

# 3. PROVED: exact multiscale radial Hamming-transform identity

The previous B13 run required a scale-by-scale rather than one-scale profile. Theorem 2.1 gives one exactly.

Let `X_i,X_i'` be independent copies of the physical sensitive-fibre law and `Y_i,Y_i'` independent copies of the spectral Palm law. Put

\[
D_X=|X_i\triangle X_i'|,
\qquad
D_Y=|Y_i\triangle Y_i'|.
\]

For a uniform `q`-subset `J` of the `m=n-1` derivative coordinates,

\[
\mathbb E_J C^{\rm phys}_{i,J}
=
\mathbb E\frac{\binom{m-D_X}{q}}{\binom mq},
\tag{3.1}
\]

because two projected strings agree exactly when `J` avoids their Hamming-difference set. The same identity holds for `Y`.

Define

\[
\bar E_{i,q}=\mathbb E_{|J|=q}E_{i,J},
\qquad
\bar R_{i,q}=\mathbb E_{|J|=q}R_{i,J}.
\]

Averaging (2.5) gives:

## Corollary B13-RADIAL-COLLISION-CONSERVATION-02

For every `q=0,1,...,m`,

\[
\boxed{
\mathbb E\frac{\binom{m-D_X}{q}}{\binom mq}
+
\mathbb E\frac{\binom{m-D_Y}{q}}{\binom mq}
+
\bar E_{i,q}+\bar R_{i,q}
=1+2^{-q}.
}
\tag{3.2}
\]

All four left-side terms are nonnegative except that the two collision terms already include their uniform baselines; no cancellation has been hidden.

There is an equivalent continuous generating-function form. Choose each derivative coordinate independently for `J` with probability `u`. Then

\[
\Pr[X_{i,J}=X'_{i,J}\mid X_i,X_i']=(1-u)^{D_X},
\]

and similarly for `Y`, while

\[
\mathbb E\,2^{-|J|}=(1-u/2)^m.
\]

Writing `E_i(u),R_i(u)` for the corresponding random-mask averages,

\[
\boxed{
\mathbb E(1-u)^{D_X}
+
\mathbb E(1-u)^{D_Y}
+E_i(u)+R_i(u)
=1+(1-u/2)^m,
\qquad 0\le u\le1.
}
\tag{3.3}
\]

This is the promised **multiscale two-sided profile identity**. It does not require choosing one macroscopic projection fraction, and so it survives the one-point-defect obstruction from the preceding run.

Dropping the two residual banks gives the universal inequality

\[
\mathbb E(1-u)^{D_X}+\mathbb E(1-u)^{D_Y}
\le1+(1-u/2)^m.
\tag{3.4}
\]

At first order (`q=1`, or differentiating at `u=0`) it implies

\[
\boxed{\mathbb E D_X+\mathbb E D_Y\ge m/2.}
\tag{3.5}
\]

Thus for every Boolean derivative row, either the physical sensitive fibres or the spectral Palm row -- or both -- must be Hamming-diffuse on a linear number of coordinates.

# 4. PROVED: singleton block gives an exact two-sided Gram/face ledger

Take `J={j}`. Split the derivative vector into its two `j`-slices `u,v in {0,\pm1}^{2^{m-1}}` and write

\[
A=\|u\|_2^2,\qquad
B=\|v\|_2^2,\qquad
C=\langle u,v\rangle,
\qquad
M=A+B.
\tag{4.1}
\]

Here `M=2^m p_i` is the number of sensitive `i`-fibres. Define the physical support bias

\[
z_{ij}=\frac{A-B}{M},
\tag{4.2}
\]

and the conditional spectral co-inclusion

\[
q_{ij}
=\Pr[j\in S\mid i\in S]
=\frac{\sum_{S\ni i,j}\mu(S)}{p_i}.
\tag{4.3}
\]

The Walsh measurement bias of the Palm bit is

\[
x_{ij}=1-2q_{ij}=\frac{2C}{M}.
\tag{4.4}
\]

For a real one-qubit reduced state the mixed-axis remainder `R` vanishes identically, so (2.5) becomes the exact Bloch-disc condition

\[
\boxed{x_{ij}^2+z_{ij}^2\le1.}
\tag{4.5}
\]

Equivalently,

\[
\boxed{
4q_{ij}(1-q_{ij})\ge z_{ij}^2.
}
\tag{4.6}
\]

This already has the desired two-sided meaning: a large imbalance of physical `i`-sensitivity between the two `j`-slices forces the conditional spectral `j`-bit away from either deterministic endpoint.

The exact slack has a Boolean face decomposition. Let

- `O_+` be the number of residual points where both slices are nonzero with the same sign;
- `O_-` be the number where both are nonzero with opposite signs;
- `O=O_++O_-`.

Then `C=O_+-O_-`, and

\[
AB-C^2=(AB-O^2)+4O_+O_-.
\]

Therefore

\[
\boxed{
4q_{ij}(1-q_{ij})-z_{ij}^2
=
\frac{4(AB-O^2)}{M^2}
+
\frac{16O_+O_-}{M^2}.
}
\tag{4.7}
\]

Both terms are nonnegative. The first is an unsigned support-overlap deficit; the second is a genuinely signed face-frustration term. Thus even at a singleton block the Boolean payment naturally splits into a support bank and a signed bank rather than a single influence statistic.

# 5. Entropy consequence: a block lower bound for the Palm spectral projection

For any finite law, Shannon entropy dominates collision/Renyi-2 entropy. Hence from (2.5),

\[
H(Y_{i,J})
\ge
-\log_2 C^{\rm spec}_{i,J}
=
-\log_2\!\left(1+2^{-q}
-C^{\rm phys}_{i,J}-E_{i,J}-R_{i,J}\right).
\tag{5.1}
\]

Dropping the nonnegative residual banks gives the support-only consequence

\[
\boxed{
H(Y_{i,J})
\ge
-\log_2\!\left(1+2^{-q}-C^{\rm phys}_{i,J}\right).
}
\tag{5.2}
\]

Averaging over all `q`-blocks and using convexity of `-log` yields

\[
\boxed{
\mathbb E_{|J|=q}H(Y_{i,J})
\ge
-\log_2\!\left(
1+2^{-q}-\bar C^{\rm phys}_{i,q}-\bar E_{i,q}-\bar R_{i,q}
\right).
}
\tag{5.3}
\]

This is a concrete multiscale Boolean input for the current sequential/projection programmes: the left side is entropy of projected derivative Palm rows, while every right-side quantity comes from physical sensitive-fibre collisions or signed/reduced-state correlation banks of the same Boolean derivative.

**Direction warning.** This is a lower bound on Palm row entropy, not an upper bound on `H(f)`. It therefore does not by itself prove FEI. B12's current terminal-to-prefix route needs a reverse-data-processing/identity-geometry inequality, and (3.2)/(5.3) are candidate structural inputs to that step rather than a closure theorem.

# 6. PROVED obstruction: physical support geometry alone cannot control the Palm row

The collision conservation also makes precise why the residual bank cannot be discarded.

Let `y in F_2^k`, `z in F_2^d`, let

\[
c(y)=1_{\{y=0\}},
\]

and let `g:F_2^d->{\pm1}` be **any** Boolean function. Introduce one sign input `s in {\pm1}` and define the Boolean function

\[
F(s,y,z)=
\begin{cases}
1,&c(y)=0,\\
s\,g(z),&c(y)=1.
\end{cases}
\tag{6.1}
\]

Its derivative in the `s` coordinate is exactly

\[
D_sF(y,z)=c(y)g(z).
\tag{6.2}
\]

Thus

\[
\operatorname{Inf}_s(F)=2^{-k},
\tag{6.3}
\]

and the normalized derivative state factors as

\[
|\psi_s\rangle=|0^k\rangle\otimes|g\rangle,
\tag{6.4}
\]

where `|g>` is the normalized sign vector of `g`.

Consequently:

- the physical sensitive-fibre law is `delta_{0^k} tensor U_d`;
- the spectral Palm law is `U_k tensor mu_g`.

In particular, for **every block contained entirely in the residual `z` coordinates**, the physical projection law is uniform and therefore

\[
C^{\rm phys}=2^{-|J|},
\tag{6.5}
\]

independently of the choice of `g`, while the spectral projection is exactly the corresponding projection of the arbitrary Boolean spectrum `mu_g`.

### Corollary: support-only row closure is impossible

Two choices of `g` can have exactly the same physical sensitive-support projection profile on every residual block but completely different Palm spectral entropy. Taking `g` constant gives zero residual spectral entropy; taking a bent Boolean phase in even residual dimension gives residual spectral entropy exactly `d`.

Therefore no universal lemma that tries to control the derivative Palm spectral entropy from **physical sensitive-support collisions alone** can close FEI. The failure remains true with arbitrarily small distinguished influence `2^{-k}`. The missing information is signed/coherent, not merely support geometry.

The obstruction is stronger still: for the bent residual, the derivative state is a product across `controls | residual`, so the entanglement bank is zero. The entire missing payment sits in `R`, the mixed-axis signed-coherence bank.

For the exact test case `k=3,d=4` with

\[
g(z)=(-1)^{z_1z_2+z_3z_4},
\]

the checker obtains:

| block | `C_phys` | `C_spec` | `E_lin` | `R_mix` |
|---|---:|---:|---:|---:|
| three controls | `1` | `1/8` | `0` | `0` |
| four bent residual coordinates | `1/16` | `1/16` | `0` | `15/16` |
| all seven derivative coordinates | `1/16` | `1/128` | `0` | `15/16` |

Thus the mixed-axis bank is not a small technical remainder: it can carry `15/16` of the entire block budget in a genuine Boolean example.

This is not a counterexample to FEI. It is a counterexample to the proposed **support-only multiscale closure** and says exactly what must be retained next: adaptive mixed-basis/signed coherence, or another mechanism that pays it without ambient-dimension loss.

# 7. Relation to the other active FEI routes

This result is complementary rather than duplicative.

- **B12:** its current Palm-row programme has exact random-prefix thinning and hypercontractive shallow-depth control but explicitly lacks a row identity/reverse-data-processing lemma. Here `Y_i` is exactly that same Palm row, and (3.2)/(5.3) supply all-block identity geometry tied to the physical derivative.
- **B16:** its signed q-flip/plaquette work shows large positive baselines require genuine signed cancellation. The `R` bank here independently identifies signed/mixed-axis information that support-only measurements cannot see. No claim is made that `R` equals B16's plaquette bank.
- **B18:** its Han/projection and joint phase-packing work acts on the whole spectral law. The present identity is a one-coordinate Palm refinement with an exact physical-side partner and is intended as a possible local structural input, not a replacement for B18's total-correlation payment.
- **B14/B15/B17:** no selector, packet-free-energy, or buried-atom bank is re-used as if proved here.

The current unrestricted FEI lower-bound correction from the owner task packet is retained: the `6.4547837...` scale is read-once/Hod-class, while an unrestricted lower bound already exceeds `6.521845710923046575`. Nothing in this report proposes a smaller universal constant.

# 8. Executed exact checks

`verify_derivative_block_complementarity.py` was executed natively with ordinary Python standard-library arithmetic.

The exhaustive part fixes `f(0)=+1` to quotient global output negation and checks every Boolean function through dimension four. It uses only integer/rational identities and verifies:

1. reduced-state purity is at most one;
2. `R_{i,J}>=0` for every nonzero derivative row and every nonempty derivative block;
3. exact conservation (2.5) after clearing denominators;
4. the singleton Gram-disc inequality (4.5);
5. the explicit gated bent residual values above.

Counts:

- **32,906** Boolean functions through `n=4` modulo global negation;
- **130,933** nonzero derivative rows;
- **915,012** exact block checks;
- **392,412** singleton Gram checks;
- `R=0` in **450,792** checked blocks and `R>0` in **464,220**;
- the coarse collision inequality (2.6) is exactly saturated in **83,280** checked blocks.

Checker SHA-256 before upload:

`e37cff64b2352e4f9535e28fbba9d868b45045176383d6a269368c7afae49321`

Archived stdout SHA-256:

`e352d4836f78e3c5673aa3387e8a5808ba37c20c57ea718591e8b72a9562e68d`

These finite checks are diagnostics, not the proof; Theorem 2.1 is the Hilbert--Schmidt orthogonality argument above.

# 9. Literature scope and next target

A fresh public search on 21 September 2026 still found universal FEI stated as a conjecture in the May 2026 González--MacManus--Pereyra work and found Potapov's 18 September 2026 plateaued/partially-bent class result. General entropic-uncertainty-with-mixed-state refinements are standard quantum-information tools (e.g. Berta et al. and later work), but the public search was not evidence of novelty for the derivative-Palm specialization here. **No novelty or priority claim is made.**

The next precise B13 target is now sharper than “accumulate projection credits across scales”:

> replace the all-standard/all-Walsh two-basis view by an **adaptive hybrid basis** on a random block, choosing physical (`Z`) or spectral (`X`) orientation coordinate by coordinate, and derive a bounded-overlap payment for the mixed-axis remainder `R` in terms of genuine Boolean face correlations. The point-gated family is the mandatory stress test: a viable scheme must spend controls in the physical basis and the arbitrary residual sign complexity in the spectral/signed bank without paying once per dimension.

A successful hybrid-basis payment would connect the new exact radial conservation to B12's Palm prefix loss and B18's total-correlation ledger. No such global payment is proved here.

# Classification

- **PROVED:** derivative physical/spectral Palm representation (1.1)--(1.6).
- **PROVED:** exact block collision conservation and nonnegative `E,R` banks (2.4)--(2.6).
- **PROVED:** exact all-scale radial/Hamming transform identity (3.2)--(3.3).
- **PROVED:** singleton two-sided Gram inequality and unsigned/signed face-slack split (4.5)--(4.7).
- **PROVED:** collision-entropy lower bound on Palm block projections (5.1)--(5.3).
- **PROVED COUNTEREXAMPLE TO A LEMMA:** physical sensitive-support collision profiles alone cannot control Palm spectral entropy, even at arbitrarily small distinguished influence; the point-gated bent family forces a macroscopic `R` bank.
- **FINITE SELF-CHECKED:** 915,012 exact block checks and 392,412 singleton checks through `n=4` modulo global output sign.
- **OPEN:** a bounded global/hybrid-basis payment for `R`, and therefore full FEI.
