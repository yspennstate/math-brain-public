# B17 FEI new proof mechanism: exact face-state transport constants and the bent-face obstruction

**Date:** 2026-09-21  
**Status of full FEI:** **OPEN / NOT PROVED**  
**Run status:** `WITHOUT_VERIFIED_BRAIN` — no authenticated mathematical-brain retrieval/context was used.  
**Role:** account03/B17, FEI new proof mechanisms.  
**Route:** new Route 17 — **finite face-state transport**. This continues the preceding higher-order face-channel route but changes the mechanism: instead of applying scalar cube log-Sobolev separately to coefficient fields, compress each local Boolean face to its exact local spectral law and control how that law can move across physical outside edges.

This run does **not** audit the read-once certificate, rerun the old `n<=5` FEI sweep, or repeat the previous four-bit pair checker.

## 1. Starting point and exact question

For a coordinate block `R` and outside assignment `y`, let `f_y` be the Boolean restriction to the physical `R`-face and let

\[
\nu_y(A)=\widehat{f_y}(A)^2,\qquad A\subseteq R.
\]

The preceding B17 result proved that if `T|Y=y ~ nu_y`, then `T` has the same law as the spectral projection `S cap R` and

\[
H(S\cap R)-\mathbb E_Y H(\nu_Y)=I(Y;T). \tag{1}
\]

It then used scalar cube log-Sobolev to obtain

\[
I(Y;T)\le \frac{2}{\ln 2} I_{R^c}(f). \tag{2}
\]

The first proposed next step was to improve `2/ln 2` by exploiting the fact that all coefficient fields come from one Boolean face. This run determines the exact finite-block optimization and shows:

1. for a **pair block** the optimal universal constant is exactly
   \[
   C_2=8-\frac52\log_2 5=2.195179762781594\ldots,
   \]
   improving `2/ln 2 = 2.8853900817...`;
2. for general block size there is an exact finite face-state transport constant `C_r`;
3. the hoped-for dimension-uniform improvement `C_r <= c < 2/ln 2` is **false**: an explicit bent-face / one-vertex-flip Boolean family has ratios tending to `2/ln 2`.

Thus the large-block constant-improvement route is decisively dead, while the pair-block route survives with a sharp improved constant.

## 2. Face-state metric and exact optimal constant

Fix `r=|R|`. Let `Q_r` be the finite set of all spectral laws

\[
P_g(A)=\widehat g(A)^2,\qquad g:\{-1,1\}^r\to\{-1,1\}.
\]

For two laws `P,Q in Q_r`, define their Boolean face distance

\[
d_r(P,Q)
=\min\{\Pr_x[g(x)\ne h(x)]: P_g=P,\ P_h=Q\}. \tag{3}
\]

Global sign is automatically accounted for because `g` and `-g` have the same spectral law.

Let `JS(P,Q)` denote the equal-weight Jensen-Shannon divergence in bits. Define

\[
\boxed{
C_r:=\max_{P\ne Q\in Q_r}\frac{JS(P,Q)}{d_r(P,Q)}.
} \tag{4}
\]

The set is finite, so the maximum exists.

### Theorem 2.1 — exact finite-block face-state transport bound

For every Boolean `f`, every block `R` of size `r`, and the local face channel in (1),

\[
\boxed{
I(Y;T)\le C_r I_{R^c}(f).
} \tag{5}
\]

Moreover `C_r` is the **best possible constant** in (5) over all Boolean functions and all outside dimensions.

### Proof

Write the outside coordinates in an arbitrary order `Y_1,...,Y_m`, where `m=n-r`. By the mutual-information chain rule,

\[
I(Y;T)=\sum_{k=1}^m I(Y_k;T\mid Y_{<k}). \tag{6}
\]

Fix a prefix `u=Y_{<k}`. Let `Z=Y_{>k}`. Conditional on `u` and `Y_k=b`, the law of `T` is a mixture of local spectral laws:

\[
P_b=\mathbb E_Z\,\nu_{u,b,Z}. \tag{7}
\]

Because `Y_k` is unbiased,

\[
I(Y_k;T\mid Y_{<k}=u)=JS(P_{-},P_{+}). \tag{8}
\]

Couple the two mixtures in (7) by using the **same** future assignment `Z`. Jensen-Shannon divergence is jointly convex, hence

\[
JS(P_{-},P_{+})
\le \mathbb E_Z\,JS(\nu_{u,-,Z},\nu_{u,+,Z})
\le C_r\,\mathbb E_Z d_r(\nu_{u,-,Z},\nu_{u,+,Z}). \tag{9}
\]

For each fixed outside edge, the actual two `R`-face truth tables are representatives of those two spectral laws, so by definition of `d_r`,

\[
d_r(\nu_{u,-,Z},\nu_{u,+,Z})
\le \Pr_{x_R}[f(x_R,u,-,Z)\ne f(x_R,u,+,Z)]. \tag{10}
\]

Average (9) over prefixes and sum over `k`. The right side of (10) sums exactly to the outside total influence. This gives (5).

For sharpness, choose spectral laws `P,Q` attaining (4) and Boolean representatives `g,h` attaining the finite minimum in (3). Define a Boolean function on `r+1` variables by using `g` on one value of a new control bit and `h` on the other. Then the outside influence is exactly `d_r(P,Q)` while the channel mutual information is exactly `JS(P,Q)`. Hence no smaller constant works.  □

This is a genuine Boolean theorem. No relaxation to arbitrary distributions on subsets is used.

## 3. PROVED: the sharp pair constant

For `r=2`, modulo global sign there are only two kinds of Boolean faces:

- four affine characters, whose local spectral laws are point masses `delta_0,...,delta_3`;
- one-defect / three-defect faces, whose local spectral law is the uniform law `U_4` on the four subsets.

The exact face distances are

\[
d_2(\delta_a,\delta_b)=\frac12\quad(a\ne b),
\qquad
d_2(\delta_a,U_4)=\frac14. \tag{11}
\]

For two different point masses, `JS=1`, giving ratio `2`. For a point mass and `U_4`,

\[
JS(\delta_a,U_4)
=H\!\left(\frac58,\frac18,\frac18,\frac18\right)-1
=2-\frac58\log_2 5. \tag{12}
\]

Therefore

\[
\boxed{
C_2=4\left(2-\frac58\log_2 5\right)
=8-\frac52\log_2 5
=2.195179762781594\ldots .
} \tag{13}
\]

This is strictly below `2/ln 2` and is exact.

Combining (1) and (13), for every coordinate pair `{i,j}` with `t` the fraction of one-defect/three-defect physical faces,

\[
\boxed{
H(X_i,X_j)-2t\le C_2 I_{[n]\setminus\{i,j\}}(f).
} \tag{14}
\]

Using the already proved exact identity `q_ij=w+t/4`, hence `2t<=8q_ij`, gives the sharpened three-channel certificate

\[
\boxed{
H(X_i,X_j)
\le C_2 I_{\rm ctrl}+8q_{ij},
} \tag{15}
\]

or equivalently

\[
\boxed{
I(X_i;X_j)+C_2 I_{\rm ctrl}+8q_{ij}
\ge h_2(p_i)+h_2(p_j).
} \tag{16}
\]

The previous coefficient `2/ln2` in this certificate can therefore be replaced by the sharp `C_2`.

### Exact sharp witness

Take a three-bit Boolean function that is `+1` everywhere except at one vertex, where it is `-1`. Choose `R` to be two coordinates and the third coordinate as the outside control. One control face is a character face and the other is a one-defect face; they differ at exactly one of the four face vertices. Thus

\[
I_{\rm ctrl}=\frac14,
\qquad
H(X_i,X_j)-2t
=2-\frac58\log_2 5,
\]

and equality holds in (14). So `C_2` is sharp even inside exact Boolean functions on only three variables.

This also explains the `2.1951797627...` ratio seen in the preceding finite checker: it was not a finite-size accident but the exact universal pair constant.

## 4. REFUTED-LEMMA: no uniform Boolean improvement below `2/ln 2` for large blocks

The tempting strengthening after the pair result would be:

> **False statement.** There exists `c < 2/ln 2` such that the face-channel theorem holds with coefficient `c` for every block size.

An explicit Boolean family refutes it.

Let `r` be even, `N=2^r`, and choose any bent Boolean function `b` on `r` bits, for example the standard quadratic bent phase in `0/1` coordinates

\[
b(x)=(-1)^{x_1x_2\oplus x_3x_4\oplus\cdots\oplus x_{r-1}x_r}.
\]

Its normalized Walsh coefficients all have magnitude `N^{-1/2}`, so its local spectral law `Q_N` is exactly uniform on the `N` subsets.

Let `b'` be obtained by flipping the value of `b` at one physical vertex. The two truth tables differ on exactly `1/N` of their inputs. If the signs of the bent Walsh coefficients are `sigma_A`, then

\[
\widehat{b'}(A)=\frac{\sigma_A}{\sqrt N}-\frac{2}{N}\tau_A,
\]

with `tau_A=+/-1`; after absorbing the vertex character into the signs, the squared masses take exactly two values

\[
\frac1N\left(1-\frac{2}{\sqrt N}\right)^2,
\qquad
\frac1N\left(1+\frac{2}{\sqrt N}\right)^2. \tag{17}
\]

Because inversion at the flipped vertex gives `sum_A sigma_A = sqrt(N)` after normalization, the first value occurs `(N+sqrt(N))/2` times and the second `(N-sqrt(N))/2` times.

Now make a Boolean function on `r+1` bits whose two control faces are `b` and `b'`. Then

\[
I_{\rm ctrl}=\frac1N,\qquad
I(Y;T)=JS(Q_N,P_N)=:J_N. \tag{18}
\]

Write

\[
F(a)=\frac12 a\log_2\frac{2a}{a+1}
+\frac12\log_2\frac{2}{a+1}. \tag{19}
\]

Then exactly

\[
J_N=
\frac{1+N^{-1/2}}2 F\!\left((1-2N^{-1/2})^2\right)
+\frac{1-N^{-1/2}}2 F\!\left((1+2N^{-1/2})^2\right). \tag{20}
\]

Since

\[
F(1+u)=\frac{u^2}{8\ln 2}+O(u^3),
\]

(20) gives

\[
J_N=\frac{2}{N\ln2}+O(N^{-3/2}),
\qquad
\boxed{N J_N\to\frac2{\ln2}.} \tag{21}
\]

Therefore any universal block coefficient must be at least `N J_N` for every even `r`, and hence at least `2/ln2` in the limit. Together with the already proved scalar log-Sobolev upper bound (2),

\[
\boxed{
\lim_{m\to\infty} C_{2m}=\frac2{\ln2}.
} \tag{22}
\]

So the general `2/ln2` coefficient is **asymptotically sharp even after imposing exact Boolean compatibility on every local coefficient field**.

This kills the previous proposed route “prove one constant `c_B<2/ln2` for all Boolean face channels.” The obstruction is not a non-Boolean surrogate; it is an explicit family of admissible Boolean functions.

## 5. Targeted computation

`face_transport_constant.py` uses exact rational Walsh probabilities and exact Hamming distances for the finite state search; floating point appears only in Shannon logarithms. This is a new targeted face-state computation, not the settled exhaustive FEI sweep.

Output:

```text
exact_state_search r=1 states=2 C_r=2.000000000000000
exact_state_search r=2 states=5 C_r=2.195179762781594
exact_state_search r=3 states=30 C_r=2.398671813459046
bent_flip r=2  ratio=2.195179762781594
bent_flip r=4  ratio=2.805655914813946
bent_flip r=6  ratio=2.869211287837631
bent_flip r=8  ratio=2.881562254420590
bent_flip r=10 ratio=2.884446418751551
bent_flip r=12 ratio=2.885154992870905
bent_flip r=14 ratio=2.885331361166781
bent_flip r=16 ratio=2.885375404850110
2/ln2          =2.885390081777927
```

The `r=2` value agrees with the closed form (13). The `r=3` number is an exact finite state-space search in its combinatorial inputs, but no closed form is claimed here. The even-`r` bent-flip values are evaluations of the explicit analytic family above and visibly converge to the proved limit.

Local pre-commit hashes from the native run:

- checker SHA-256: `e722fa42deb0e584e2a65ec246e18fb4d95c74c99389c47978799ee7a1b05dc8`;
- output SHA-256: `9b0188a89dfadfc9a61d79539e9ff47c6e1e07144f50f6d466409b3464e45007`.

## 6. Boundary and refutation checks

The theorem was checked against the required boundary cases.

- `R=emptyset`: no face state and no information term.
- no outside coordinates: `I(Y;T)=0`; (5) is equality at zero.
- characters: each face spectral law is a point mass; the finite-state metric gives the exact point-mass transition cost.
- one-bit blocks: `C_1=2` exactly.
- two-bit blocks: the three-bit one-point function saturates `C_2` exactly.
- large even blocks: bent / one-vertex-flip faces force the constant upward to `2/ln2`.
- the argument never assumes negative association, determinantal structure, independence of rare coordinates, or an every-coordinate restriction charge.

What would refute Theorem 2.1 is either failure of joint convexity of equal-weight Jensen-Shannon divergence or an outside edge whose actual normalized face Hamming distance is below the minimum in (3); neither is possible by the standard convexity property and the definition of the minimum. The sharpness construction is an actual Boolean function obtained by adjoining one control bit.

## 7. Claim ledger

### PROVED

1. Exact finite-block constant theorem (5), with `C_r` defined by the finite Boolean face-state transport problem (4).
2. `C_r` is the optimal possible constant for that block size.
3. `C_1=2`.
4. `C_2=8-(5/2)log_2 5 = 2.195179762781594...` exactly.
5. The pair face-channel inequality improves universally from coefficient `2/ln2` to the sharp coefficient `C_2`.
6. The three-bit one-point function saturates the pair constant.
7. For even block size, the bent-face / one-vertex-flip Boolean family yields ratios tending to `2/ln2`.
8. Consequently `lim_{m->infinity} C_{2m}=2/ln2`.

### REFUTED-LEMMA

There is **no** dimension-uniform Boolean face-channel improvement `c_B<2/ln2` valid for all block sizes.

### COMPUTATIONAL EVIDENCE ONLY

The exact finite combinatorial state search gives `C_3 = 2.398671813459046...`; no symbolic closed form or general formula for all odd `r` is claimed.

### OPEN / CONDITIONAL

1. Full FEI remains **OPEN / NOT PROVED**.
2. The face-channel theorem by itself does not solve the global recursive packing problem because `E H(nu_Y)` is still the spectral entropy of lower-dimensional Boolean faces.
3. A full proof must exploit **hierarchical structure**, not a uniform improvement of the one-shot large-block channel constant.

## 8. Next attack: bounded-size hierarchical packing, not another constant search

The large-block constant-improvement subroute is now closed negatively, so the next run should **change method** rather than enumerate larger `r`.

The surviving mechanism is:

> Use the sharp small-block constants (especially `C_1=2` and `C_2=2.19518...`) only on bounded-size rare-coordinate clusters, and prove a hierarchical decomposition in which an outside physical edge is charged at most once across the cluster tree. The residual local entropy must be paid by internal overlap/activation mass (`q_ij` and higher intersections), not by reapplying the full outside-influence charge at every level.

A concrete next lemma is to seek a laminar family of singleton/pair clusters with weights `alpha_B` such that

\[
\sum_B \alpha_B\,[H(S\cap B)-\mathbb E H(\nu^B_Y)]
\le C_2 I(f)
\]

because each physical coordinate lies outside clusters of total weight at most one, while the complementary weighted local-face entropies telescope into overlap terms. The difficult part is the telescoping/overlap identity, not the channel coefficient; this run shows why attacking the latter for large blocks cannot close FEI.

No novelty or publication-priority claim is made for the finite-state transport formulation without a dedicated literature search. The result is recorded here as internal proof progress toward the full conjecture.
