# fleet01/B15 — support KL refund and complement-parity dependence floor

**Run:** `20260922T091311Z-fleet01-B15-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / QUANTITATIVE_NEGATIVE_KL_PAYMENT`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Corrected common candidate and exact old gap

This run uses the corrected common Shannon residual `B-INFLUENCE-IPROJECTION-v1`, not the refuted fixed potential `Gamma^dagger`.

The exact peer source is fleet02/B15

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`

at scientific commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, report blob `5ce14eaaec34f0d91f2d430dba576e19dddc6894`. For every nonconstant Boolean gate and every proposed symmetric potential `Gamma`, with `P=w^+` the actual nonempty biased spectral law and

\[
r_i=P(i\in S)=\frac{\operatorname{It}_i(G;p)}{V_q},
\]

let `Q_r` be the unique maximum-entropy law on nonempty subsets having the same original-coordinate marginals. The source-exact identity is

\[
\boxed{
R_\Gamma(G;p)=B_{\rm inf}^\Gamma(G;p)+K_{\rm occ}(G;p),
}
\tag{0.1}
\]

where

\[
K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P)\ge0.
\tag{0.2}
\]

The same report records the current correction that the former fixed seed

\[
\Gamma^\dagger=\Gamma_0+0.268204856\,p(1-p)
\]

is **not** a universal all-gate potential: a source-certified biased composition-prime Numaro instance has negative defect. The decomposition (0.1) survives for arbitrary `Gamma`; this run does not revive the refuted seed.

The newest compatible other-account theorem consumed substantively is fleet03/B15

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B15/20260922T085625Z-product-equality-rigidity/REPORT.md`

at scientific commit `84c69136ca6b008badb76f15bf1071d029c927aa`, blob `7904b3ca9ec1b04150b0d23520c65eec9e1010c2`. It proves on the balanced uniform slice that `K_occ=0` is equivalent to a character times a bent function on disjoint variables, hence every essential composition-prime balanced gate has `K_occ>0`.

The **old first missing inference** after (0.1) was quantitative:

\[
\boxed{
K_{\rm occ}\ge[-B_{\rm inf}^\Gamma]_+
}
\tag{0.3}
\]

for every composition-prime Boolean source in a repaired all-gate candidate, or else a genuine Boolean falsifier. Exact equality rigidity alone did not give a numerical payment. This run extracts two explicit negative-KL payments, one exact and one source-sign quantitative.

## 1. Exact support-mismatch entropy refund

Let `P` and `Q` be probability laws on the same finite set, and write

\[
A=\operatorname{supp}P,
\qquad
\zeta=Q(A^c).
\]

Assume `Q(A)>0` and put `Q_A=Q(\cdot\mid A)`. Since `P` is supported on `A`, the KL chain rule gives the identity

\[
\boxed{
D_{\rm KL,2}(P\Vert Q)
= -\log_2(1-\zeta)+D_{\rm KL,2}(P\Vert Q_A).
}
\tag{1.1}
\]

Therefore, for the FEI influence I-projection,

\[
\boxed{
K_{\rm occ}
\ge K_{\rm supp}:=-\log_2(1-\zeta),
\qquad
\zeta=Q_r\{S:P(S)=0\}.
}
\tag{1.2}
\]

This is an exact **negative entropy refund**. It is not a support-counting surrogate: the price is the actual `Q_r` mass of Fourier atoms forbidden by the Boolean source after the original-coordinate influences have already been matched. In particular, a product-like reference that spends substantial mass on absent Fourier atoms pays for that loss before any finer packet argument is needed.

Combining (0.1) and (1.2), every source satisfying

\[
\boxed{
B_{\rm inf}^\Gamma-\log_2(1-\zeta)\ge0
}
\tag{1.3}
\]

is safe for the proposed gate potential.

## 2. A source-sign complement-parity payment at the balanced uniform center

Now let

\[
f:\{-1,1\}^m\to\{-1,1\}
\]

be balanced under the uniform measure. Put

\[
P(S)=\widehat f(S)^2,
\qquad
r_i=P(i\in S),
\qquad
\mu=\sum_i r_i.
\]

Assume `mu>1`. The fleet02/B15 I-projection theorem writes `Q_r` as independent Bernoulli coordinates with probabilities

\[
t_i=c r_i
\tag{2.1}
\]

conditioned on being nonempty, where `c in (0,1]` solves

\[
1-c=\prod_i(1-c r_i).
\tag{2.2}
\]

Let

\[
E=\{i:r_i>0\},\qquad e=|E|,
\]

and suppose `c<1`; then every active `t_i` lies strictly between zero and one. For every nonempty proper `S subset E`,

\[
Q_r(S)Q_r(E\setminus S)
={1\over c^2}\prod_{i\in E}t_i(1-t_i)=:d^2.
\tag{2.3}
\]

Define also

\[
q_E:=Q_r(E)={1\over c}\prod_{i\in E}t_i,
\qquad
s^2:=1-q_E.
\tag{2.4}
\]

### Theorem 2.1 — `B-COMPLEMENT-PARITY-KL-v1`

For every balanced uniform Boolean `f` in the branch above,

\[
\boxed{
K_{\rm occ}
\ge K_{\rm par}
:=-2\log_2\left(1-\frac{\eta}{2}\right),
}
\tag{2.5}
\]

where

\[
\boxed{
\eta
={s^2-\sqrt{s^4-4d^2}\over2}>0.
}
\tag{2.6}
\]

In particular,

\[
K_{\rm occ}\ge {d^2\over\ln2}.
\tag{2.7}
\]

### Proof

Let `a_S=hat f(S)`. Booleanity gives the exact signed convolution system

\[
\sum_T a_Ta_{T\triangle U}=\mathbf1_{\{U=\varnothing\}}.
\tag{2.8}
\]

Take `U=E`. Balance gives `a_empty=0`; coefficients involving inactive coordinates vanish. Group the remaining terms into the unordered complementary pairs

\[
\{S,E\setminus S\},
\qquad
\varnothing\ne S\subsetneq E.
\]

There are

\[
N=2^{e-1}-1
\]

such pairs, and `N` is odd. For each pair choose `epsilon_S in {+1,-1}` equal to the sign of `a_Sa_{E\setminus S}` when that product is nonzero, and arbitrary when it is zero. With

\[
x_S=\sqrt{P(S)},
\]

equation (2.8) is

\[
\sum_{\{S,E\setminus S\}}\epsilon_S x_Sx_{E\setminus S}=0.
\tag{2.9}
\]

On the same nonempty-proper coordinate space define the symmetric orthogonal complement involution `A` by

\[
A e_S=\epsilon_S e_{E\setminus S}.
\]

Then (2.9) is

\[
\frac12 x^TAx=0.
\tag{2.10}
\]

Let `y_S=sqrt(Q_r(S))`. By (2.3), every complementary product is exactly `d`, hence

\[
\frac12y^TAy=dM,
\qquad
M=\sum_{\rm pairs}\epsilon_S.
\tag{2.11}
\]

Because `N` is odd, `M` is an odd integer, so `|M|>=1`.

Decompose `y=y_++y_-` into the `+1` and `-1` eigenspaces of `A`; write `alpha=||y_+||`, `beta=||y_-||`. Then

\[
\alpha^2+\beta^2=s^2,
\qquad
\alpha^2-\beta^2=2dM.
\tag{2.12}
\]

The closest vector to `y` on the quadratic cone `z^TAz=0` has equal `+` and `-` norms. Minimizing over that common norm gives squared Euclidean distance

\[
{(\alpha-\beta)^2\over2}
={s^2-\sqrt{s^4-4d^2M^2}\over2}
\ge\eta.
\tag{2.13}
\]

The actual `x` lies on that cone, so the squared Hellinger distance between the full laws `P,Q_r` obeys

\[
H_{\rm Hel}^2(P,Q_r)
=\sum_S(\sqrt{P(S)}-\sqrt{Q_r(S)})^2
\ge\eta.
\tag{2.14}
\]

Finally, monotonicity of Renyi divergences gives

\[
D_{\rm KL,2}(P\Vert Q_r)
\ge D_{1/2,2}(P\Vert Q_r)
=-2\log_2\sum_S\sqrt{P(S)Q_r(S)}.
\]

Since the Bhattacharyya coefficient equals `1-H_Hel^2/2`, (2.5) follows. The weaker (2.7) follows from `eta>=d^2` and `-2 log_2(1-u/2)>=u/ln 2`. `QED`.

This theorem retains the **actual Fourier signs** through the signed complement involution. It is not a sign-free probability-law relaxation.

## 3. Prime-gate corollary

Let `f` be an essential balanced uniform gate of arity at least two.

* If `mu=1`, equality in Poincare forces Fourier support on level one; the Boolean quadratic identities then force a dictator, contradicting essential arity at least two.
* If the I-projection parameter in (2.2) is `c=1`, then `prod_i(1-r_i)=0`, so some `r_i=1`. At the balanced center `r_i=Inf_i(f)=1`; flipping that coordinate always flips the Boolean value, hence
  \[
  f(x)=\pm x_i h(x_{-i}),
  \]
  a nontrivial disjoint-variable composition.

Therefore every essential **composition-prime** balanced uniform gate has

\[
\boxed{\mu>1,\qquad c<1,}
\tag{3.1}
\]

and Theorem 2.1 applies with a strictly positive dependence-KL floor.

Combining the two negative-entropy payments gives the source-exact prime-center criterion

\[
\boxed{
K_{\rm occ}
\ge
\max\{K_{\rm supp},K_{\rm par}\}.
}
\tag{3.2}
\]

At the balanced uniform center, for any candidate center value `C=Gamma(1/2)`,

\[
B_{\rm inf}^\Gamma=C(I-1)-H_{\max}(r).
\tag{3.3}
\]

Hence every composition-prime balanced gate satisfying

\[
\boxed{
C(I-1)-H_{\max}(r)
+\max\{K_{\rm supp},K_{\rm par}\}
\ge0
}
\tag{3.4}
\]

is rigorously safe at the center, without needing the remaining shape KL.

This is the direct application to the old missing inference (0.3): the negative KL is no longer an unnamed remainder. Two concrete pieces of it now have explicit source prices.

## 4. Decisive source tests

### 4.1 Named four-bit prime witness from fleet02/B15

For the source-checked balanced four-bit prime witness with Walsh numerator vector

\[
(0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0),
\]

the peer gives

\[
r=(1/4,1/4,1/4,3/4),
\qquad
K_{\rm occ}=0.801287937850463\ldots .
\]

The new exact support refund alone gives

\[
K_{\rm supp}=0.599813352304038\ldots,
\]

while the complement-parity theorem gives

\[
K_{\rm par}=0.002240127575283\ldots .
\]

Thus most of the source's canonical negative-information credit is already identified as the exact price of Fourier atoms that the matched product reference wants to use but the Boolean source forbids.

### 4.2 Bounded small-arity diagnostic

A deterministic diagnostic enumerates balanced essential composition-prime truth tables for `n=3,4`, uses the module criterion for decomposition, and evaluates (3.4) at the center value `C=6.521851214` **only as a diagnostic**. It is not interval arithmetic and is not used as a universal proof.

Observed:

* `n=3`: 32 balanced essential prime truth tables; minimum lower residual from (3.4) is `1.155942489445465`.
* `n=4`: 11,416 balanced essential prime truth tables; minimum lower residual is `0.206620624055544`.
* The worst four-bit profile for this lower bound is
  \[
  r=(1/4,1/4,1/2,1/2),
  \]
  with `c=0.731269413972913`, `H_max=3.319281081146521`, support refund `0.264976098202065`, and parity refund `0.003268622493610`.

The diagnostic therefore finds no small-arity center obstruction to the new payment. This is finite evidence only.

## 5. Required obstruction checks and limitation

This mechanism is compatible with the standard Campaign-B adversaries but does **not** close them all asymptotically.

* **Dictators/dummy coordinates:** `mu=1`; the source equals its I-projection and the gate is decomposable. No fake `log k` coordinate charge remains.
* **Character times bent / tensor products:** these can lie on `c=1` and `K_occ=0`, exactly as the fleet03 equality theorem says; they are decomposable and therefore do not contradict the prime corollary.
* **Addressing, tribes, majority:** spectral zeros are charged by `K_supp` with their actual `Q_r` mass. No uniform asymptotic lower bound is claimed here.
* **Sparse-defect / nearly full-support sources:** `K_supp` may become tiny or vanish. `K_par` remains strictly positive on a balanced prime source, but its product `d^2` can decay rapidly with arity. This is the main surviving obstruction.
* **Biased limits:** Theorem 2.1 uses the uniform Walsh convolution and therefore does not yet pay the off-center biased-source gap. No biased analogue is claimed.

Thus the result survives the named obstruction battery but does not pretend to solve the high-arity nearly-full-support or biased cases.

## 6. Exact old/new missing implication

**Candidate/version:** corrected `B-INFLUENCE-IPROJECTION-v1` from fleet02/B15 `20260922T0829Z-influence-iprojection-kl`, together with fleet03/B15 `B-PRODUCT-EQUALITY-RIGIDITY-v1`. The fixed `Gamma^dagger` candidate is retired/refuted and is not used as universal.

**Old missing implication:** prove `K_occ >= [-B_inf^Gamma]_+` for every composition-prime Boolean gate/bias in a repaired all-gate potential.

**New proved inference:**

1. the exact support component of the negative dependence KL is
   \[
   K_{\rm supp}=-\log_2 Q_r(\operatorname{supp}P);
   \]
2. every balanced uniform composition-prime source has the additional source-sign complement-parity floor `K_par>0` in (2.5);
3. consequently the whole center region satisfying (3.4) is removed from the unresolved set.

**New first missing implication:** handle the balanced high-arity **near-full-support** corridor where both explicit payments are smaller than `-B_inf^Gamma`, and derive a biased-product analogue off center. Equivalently, prove that signed Boolean realizability creates a further quantitative shape KL in that corridor, or construct a genuine composition-prime Boolean gate/bias violating the repaired residual.

Only a bound covering every arity and every interior bias for one repaired symmetric potential yields full FEI. **Full FEI remains OPEN.**
