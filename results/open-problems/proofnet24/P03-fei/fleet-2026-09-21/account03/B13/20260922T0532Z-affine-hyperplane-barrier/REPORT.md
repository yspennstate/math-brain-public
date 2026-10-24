# B13 — affine-hyperplane descent of the ten-input prime gate is impossible at the balanced uniform slice

**Outcome:** `AUXILIARY_ONLY / SOURCE_FAMILY_BARRIER`. Full uniform-cube FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authorized repository sources were consumed directly; no authenticated mathematical-brain retrieval or receiver-context use occurred.

## 1. Live target, exact peer input, and mechanism change

The live owner control is the all-gate FEI formulation. The old read-once fixed-point potential at `C0=6.4548` and the associated claim that the two-input AND controls every gate margin are already refuted, so this run does **not** try to repair that candidate. The useful remaining adversarial problem is to understand how small a genuine prime obstruction can be and which descent mechanisms are actually dead.

The named other-account result consumed is

`proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260922T0055Z-arity10-prime-falsifier/REPORT.md`, report blob `d71f08f9a2fd0b417ac7b0cdbac19bacac85c01b`.

It supplies a balanced composition-prime ten-input gate `G10`, obtained from the source-exact eighteen-input Numaro seed by fixing

`(y0,...,y7)=(0,0,0,1,1,0,1,1)`

and leaving `(x0,...,x8,y8)` free. It proves

\[
I(G_{10})=\frac{257}{128},\qquad
\frac{H(G_{10})}{I(G_{10})-1}>6.4593722816378554,
\]

so, for the old center `C0=6.4548`, its central gate margin is

\[
c_{G_{10}}>0.0182891265514229,
\]

more than four times the quoted two-input AND margin `0.0043974201`. The same peer certifies that `G10` is composition-prime.

A same-account companion result already exhausts **ordinary coordinate restrictions** of the whole relevant Numaro slice and shows that they cannot descend the obstruction below arity ten. I therefore used a materially different descent: **all codimension-one affine restrictions, followed by all invertible linear reparameterizations of the resulting nine-dimensional affine cube.**

## 2. Exact statement attempted

Let the ten local coordinates of `G10` be `0,...,9`, with `0,...,8=x0,...,x8` and `9=y8`. For every nonzero

\[
a\in\mathbb F_2^{10}
\]

and every `b in F2`, restrict `G10` to the affine hyperplane

\[
H_{a,b}=\{x:a\cdot x=b\}.
\]

There are exactly

\[
2(2^{10}-1)=2046
\]

such hyperplanes. When the restricted gate is balanced, allow an **arbitrary affine isomorphism**

\[
\phi:\mathbb F_2^9\to H_{a,b}.
\]

The claim tested was:

> Some balanced affine hyperplane descendant of `G10`, after a favorable affine choice of nine input coordinates, still beats the old central AND threshold and hence gives an arity-nine balanced-uniform falsifier.

This claim is **REFUTED for every codimension-one affine descendant of this exact `G10`**.

## 3. Why the search over coordinate systems is exact

For a Boolean function `h:F2^9->{-1,1}` and a nonzero displacement `v`, set

\[
q(v)=\Pr_x[h(x)\ne h(x+v)].
\]

If `L` is an invertible linear reparameterization and its columns are the basis vectors `v1,...,v9`, then

\[
I(h\circ L)=\sum_{j=1}^9 q(v_j).
\tag{3.1}
\]

Translations only change Fourier signs and do not change squared Fourier masses or influence. Therefore maximizing

\[
\frac{H(h)}{I(h)-1}
\]

over all affine coordinate systems is equivalent to finding a minimum-weight basis of `F2^9` with weight `q(v)`.

The nonzero vectors of `F2^9` with linear independence form a vector matroid, so the standard greedy algorithm is exact: sort the 511 nonzero vectors by `q(v)` and add a vector iff it increases rank. No heuristic basis search is involved.

The checker computes every `q(v)` exactly from the squared Walsh transform. If `W_s` are the unnormalized Walsh coefficients for a 512-point truth table, then

\[
q(v)=\frac{1}{2}\left(1-\frac{1}{512^2}
\sum_s W_s^2(-1)^{s\cdot v}\right),
\tag{3.2}
\]

so the entire minimum-basis calculation is integer/rational arithmetic.

## 4. Complete affine-hyperplane result

Among the 2046 affine hyperplanes, exactly

\[
\boxed{570}
\]

give balanced nine-bit restrictions. Every one has optimized influence strictly larger than one.

For each balanced restriction the checker computes the integer Walsh transform, the **globally minimum** possible total influence over all affine parameterizations by the matroid argument above, and a rigorous rational interval for the spectral entropy. The logarithms use a 30-term exact-rational `atanh` expansion with an explicit positive tail bound. All comparisons to the central thresholds are made with exact `Fraction` arithmetic, not floating point.

The global maximum over all 570 balanced hyperplanes and every affine coordinate system is attained by 256 hyperplanes with the same exact minimum influence and Walsh-square histogram. One representative is

\[
 x_6\oplus y_8=1,
\]

corresponding to normal `a=576` and right-hand side `b=1`. For this representative,

\[
I_{\min}=\frac{257}{128},
\]

and the rigorous entropy enclosure is

\[
6.4813913674671479559979904827833609\ldots
< H <
6.4813913674671479559979904827835906\ldots.
\]

Hence

\[
\boxed{
6.4311480235332940958739750526842651\ldots
<\frac{H}{I_{\min}-1}<
6.4311480235332940958739750526844930\ldots
}
\tag{4.1}
\]

with interval width below `2.28e-31` at the ratio level. The next-best non-tied ratio has rigorous upper bound

\[
6.43107532643663383818\ldots,
\]

so the maximizing class is separated rigorously, not selected by floating-point noise.

The representative's absolute Walsh histogram is

`4:144, 8:80, 12:40, 16:64, 20:40, 24:8, 28:8, 36:8, 40:20, 44:8, 48:8, 56:4, 96:1, 116:8`.

Most importantly,

\[
\boxed{
\frac{H}{I_{\min}-1}<6.431149<6.4548=C_0.
}
\tag{4.2}
\]

Since every other affine parameterization has influence at least `I_min`, (4.2) holds for **every** affine coordinate system on **every** balanced codimension-one affine restriction of `G10`.

At uniform bias the balanced gate margin is

\[
c_G=4\left(\frac{H}{I-1}-C_0\right),
\]

so throughout this family

\[
\boxed{c_G<-0.0946079058668236.}
\tag{4.3}
\]

This is not merely below the positive AND floor: every affine nine-dimensional descendant in the tested balanced slice has negative margin already at the old center.

## 5. Status and implication to full FEI

**PROVED, exact finite/source-family scope:** no balanced codimension-one affine restriction of the exact prime `G10`, under any affine `F2^9` parameterization, can be an arity-nine central-bias obstruction to the old read-once potential. The proof covers all 2046 hyperplanes and exactly optimizes the coordinate basis on every balanced one.

**REFUTED, route-specific:** “shrink the known ten-input prime falsifier to arity nine by one affine equation, perhaps rescuing the ratio by a clever linear choice of coordinates.” Ordinary coordinate restrictions were already dead; the full codimension-one affine version is now dead too.

**NOT PROVED:** this does not exclude arbitrary nine-input Boolean gates; it does not exclude codimension-two affine descendants that need not pass through a balanced hyperplane; it does not address genuinely nonuniform input biases; and it does not supply a replacement finite-cap potential. Full FEI therefore remains **OPEN**.

The exact replacement obligation is to leave this codimension-one descent. The next attack should be either (i) direct codimension-two affine slices of `G10`, again optimizing the induced basis exactly, or (ii) an unrestricted arity-six-to-nine prime search outside this source family, or (iii) the live nonuniform-bias arity-five search. The mathematically cleanest continuation of the present coding/matroid method is direct codimension two, because a balanced codimension-two slice need not lie inside any balanced codimension-one slice.

**Consumed peer artifact:** `account04/B13/20260922T0055Z-arity10-prime-falsifier/REPORT.md`.  
**Applied to claim:** whether that exact prime falsifier can descend to a balanced-uniform arity-nine falsifier through any affine hyperplane and any affine coordinate system.  
**Remaining implication:** find a smaller genuinely prime gate/bias obstruction outside this dead descent, or construct a replacement all-gate potential with a cap compatible with the known high-arity lower bounds.  
**Next recipient:** `account04/B13` and the current all-gate adversarial workers; the result tells them not to spend a run on affine-hyperplane descent of `G10`.

## 6. Reproduction boundary

`CHECKER.py` is standard-library only. It reconstructs the exact eighteen-input source and verifies its source SHA-256, reconstructs `G10`, enumerates all 2046 affine hyperplanes, checks balance, computes exact Walsh transforms, computes the exact minimum-weight basis influence for every balanced restriction, encloses every entropy with rational logarithm intervals, proves every central ratio is below `C0`, identifies the 256 exact maximizers and proves the next-best class is separated. `CHECKER_OUTPUT.json` records the deterministic result and `PASS=true`.

No novelty or publication-priority claim is made.
