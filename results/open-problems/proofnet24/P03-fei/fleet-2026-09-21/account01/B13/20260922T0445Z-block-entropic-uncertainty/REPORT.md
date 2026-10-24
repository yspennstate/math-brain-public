# account01/B13 — block entropic uncertainty for physical restrictions

**Classification:** `AUXILIARY_ONLY` — a new universal structural lemma is proved and applied to the exact random-block FEI selector, but the selector-existence implication itself remains open.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact live candidate and the missing implication

The source-exact gate formulation asks for one symmetric nonnegative potential `Gamma` such that for every Boolean gate and every product bias

\[
D_\Gamma(G;p):=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u).
\]

The campaign lead's current fixed candidate is account01/B18
`20260922T0222Z-shared-graft-tail` (report blob
`7ea2c548afc0a5fc62f972f9c64df0578f7e0838`):

\[
C_*=6.5218512,\qquad
\Gamma_*(u)=\Gamma_{\rm RO}(u)+a_*u(1-u),\qquad
a_*=0.2682048.
\]

Its exact universal missing assertion is `LIMIT-PRIME-GATE-LIFT-v1`, namely
`D_{Gamma_*}(P;p)>=0` for every finite-arity composition-prime Boolean gate and every interior product bias. If this holds, the already-proved composition cocycle and all-gate equivalence imply

\[
H(f)\le 6.5218512 I(f)
\]

for every uniform-cube Boolean `f`.

This run substantively consumes account02/B18
`20260922T040428Z-random-block-currency` (report blob
`bd4972b11cb13989282f555deb9354509d1da590`). For a uniformly random physical `r`-block `A`, it defines

\[
B_r^{\rm RO}=D_{\Gamma_{\rm RO}}(G)-
\mathbb E_{A,X_A}D_{\Gamma_{\rm RO}}(G_{A=X_A}),
\]

and the exact Poincare currency `Q_r`, and proves

\[
D_{\Gamma_*}(G)-
\mathbb E_{A,X_A}D_{\Gamma_*}(G_{A=X_A})
=B_r^{\rm RO}+a_*Q_r. \tag{0.1}
\]

Thus its exact sufficient induction target is

> `EXACT-RANDOM-BLOCK-RO-DEFICIT-v1`: every non-affine Boolean gate and interior product bias admits some proper nonempty block size `r` with
> \[
> B_r^{\rm RO}+a_*Q_r\ge0. \tag{0.2}
> \]

The same report proves the closed currency profile

\[
Q_r={1\over4}\sum_{k\ge2}W_k
\left({kr\over n}-{(r)_k\over(n)_k}\right), \tag{0.3}
\]

and in particular

\[
Q_r\ge {r\over n}P_0+
{r(n-r)\over4n(n-1)}W_{\ge2}. \tag{0.4}
\]

The first missing mathematical object is therefore the signed base residual `B_r^RO`. The theorem below converts its branch-mixing entropy into a root-only conditional spectral entropy, with a sharp bias penalty and no dimension factor.

The second compatible peer input is account03/B13
`20260922T040037Z-bent-swap-local-margin` (report blob
`3f3e5294853654e0539f2e11fad49a3fed344136`). It gives a genuine Boolean family with unbounded one-pivot local correction request. Thus a pointwise local scalar cap is dead; the aggregate physical-block mechanism (0.1) is the appropriate object here.

## 1. Exact physical-branch / spectral-block setup

Let `f:{0,1}^n->{-1,+1}` be Boolean under the product law with
`Pr[X_i=1]=p_i`, all `p_i` interior. Fix a physical restriction block
`A subset [n]`, put `Z=X_A`, and let `A^c` be the unrevealed coordinates.

For a branch `z in {0,1}^A` and an outside spectral index `T subset A^c`, write

\[
a_z(T)=\widehat {f_z}(T)
\]

for the biased Fourier coefficient of the restricted Boolean function. Let

\[
P_z(T)=a_z(T)^2.
\]

Parseval gives `sum_T P_z(T)=1` for every branch. Hence there is a genuine joint probability law

\[
\Pr[Z=z,\,T=t]=\mu_A(z)P_z(t), \tag{1.1}
\]

where `mu_A` is the physical product law on the block. This `T` is the child spectral sample after the physical block has been revealed.

Let the root spectral sample be `S`, and decompose

\[
U=S\cap A,\qquad T=S\cap A^c.
\]

The same letter `T` is justified by the following exact projection identity.

### Lemma 1.1 — restriction Parseval projection

For every outside index `T subset A^c`,

\[
\boxed{
\mathbb E_Z P_Z(T)
=\sum_{U\subseteq A}\widehat f(U\cup T)^2.
} \tag{1.2}
\]

Thus the `T`-marginal in (1.1) is exactly the projection of the root spectral sample onto `A^c`.

#### Proof

For fixed outside `T`, Fourier inversion only in the block gives

\[
\widehat f(U\cup T)=
\mathbb E_Z\bigl[a_Z(T)\chi_U^A(Z)\bigr].
\]

The biased characters `chi_U^A` are an orthonormal basis in `L^2(mu_A)`. Parseval in the block therefore gives

\[
\sum_U\widehat f(U\cup T)^2
=\mathbb E_Z a_Z(T)^2.
\]

This is (1.2). `square`

The exact entropy drop under the physical block is consequently

\[
\begin{aligned}
\Delta_A H
&:=H(S)-\mathbb E_ZH(P_Z)\\
&=H(T)+H(U\mid T)-H(T\mid Z)\\
&=\boxed{H(U\mid T)+I(Z;T)}. \tag{1.3}
\end{aligned}
\]

For a singleton uniform block, (1.3) is precisely the usual erasure-plus-Jensen-Shannon decomposition.

## 2. New theorem: block entropic uncertainty

Define

\[
L_A:=\sum_{i\in A}-\log_2\max\{p_i,1-p_i\}, \tag{2.1}
\]

and the nonnegative bias penalty

\[
\eta_A:=H(Z)-L_A
=\sum_{i\in A}
\left[h_2(p_i)+\log_2\max\{p_i,1-p_i\}\right]. \tag{2.2}
\]

### Theorem 2.1 — two-sided Boolean block constraint

For every Boolean `f`, every interior product bias and every physical block `A`, with `(Z,U,T)` defined above,

\[
\boxed{H(Z\mid T)+H(U\mid T)\ge L_A.} \tag{2.3}
\]

Equivalently,

\[
\boxed{I(Z;T)\le H(U\mid T)+\eta_A.} \tag{2.4}
\]

Consequently the exact restriction entropy drop satisfies

\[
\boxed{
\Delta_AH\le 2H(U\mid T)+\eta_A.
} \tag{2.5}
\]

At the uniform cube, `p_i=1/2` for every `i`, so `L_A=|A|`, `H(Z)=|A|`, and the penalty vanishes:

\[
\boxed{I(X_A;S_{A^c}^{\rm child})\le
H(S_A\mid S_{A^c}),} \tag{2.6}
\]

\[
\boxed{\Delta_AH\le2H(S_A\mid S_{A^c}).} \tag{2.7}
\]

This is dimension-free and uses the fact that the child spectra and the root spectrum come from the same signed Boolean source. It is not valid for an arbitrary unrelated collection of probability laws.

### Proof

Fix an outside spectral index `T=t` with marginal mass

\[
m_t=\sum_z\mu_A(z)a_z(t)^2>0.
\]

Put

\[
x_z={\sqrt{\mu_A(z)}a_z(t)\over\sqrt{m_t}}.
\]

Then `sum_z x_z^2=1`, and the squared coordinates `x_z^2` are exactly the conditional branch law `Pr[Z=z|T=t]` from (1.1).

Let

\[
M_{U,z}=\sqrt{\mu_A(z)}\,\chi_U^A(z).
\]

Because the biased characters are orthonormal, `M` is a real orthogonal matrix. Moreover

\[
{\widehat f(U\cup t)\over\sqrt{m_t}}
=\sum_zM_{U,z}x_z. \tag{2.8}
\]

Hence the squared coordinates of `Mx` are exactly `Pr[U|T=t]`.

For one biased coordinate with bias `p`, the absolute entries of the corresponding two-by-two matrix are `sqrt(p)` and `sqrt(1-p)`. Tensorization therefore gives

\[
c_A:=\max_{U,z}|M_{U,z}|
=\prod_{i\in A}\sqrt{\max\{p_i,1-p_i\}}. \tag{2.9}
\]

We use the following elementary entropic-uncertainty lemma. If `M` is an orthogonal matrix with maximum entry magnitude `c`, then every unit vector `x` obeys

\[
H(x^2)+H((Mx)^2)\ge-2\log_2c. \tag{2.10}
\]

For completeness, interpolate between
`||M||_{1->infinity}<=c` and `||M||_{2->2}=1`. With `0<=s<=1`,

\[
\|Mx\|_{2/(1-s)}\le c^s\|x\|_{2/(1+s)}. \tag{2.11}
\]

Both sides equal one at `s=0`. Taking logarithms and the right derivative at zero gives

\[
{1\over2}\sum_jq_j\ln q_j
\le-{1\over2}\sum_ip_i\ln p_i+\ln c,
\]

where `p_i=x_i^2`, `q_j=(Mx)_j^2`; rearranging and converting to base two is (2.10).

Applying (2.10) to the vector above and using (2.9) yields, for every `t`,

\[
H(Z\mid T=t)+H(U\mid T=t)\ge
-2\log_2c_A=L_A.
\]

Average over `T` to obtain (2.3). Since

\[
I(Z;T)=H(Z)-H(Z\mid T),
\]

(2.4) follows from (2.2)-(2.3), and (2.5) follows from the exact identity (1.3). `square`

## 3. Direct application to the selected random-block FEI restriction

For a fixed physical block `A`, define its read-once input charge

\[
\mathcal L_A^{\rm RO}:=
\sum_{i\in A}{\operatorname{It}_i(G;p)\over V_{p_i}}
\left(\Gamma_{\rm RO}(p_i)+h_2(V_{p_i})\right). \tag{3.1}
\]

Let `r_Z=Pr[G_{A=Z}=1]` and `r=Pr[G=1]`. Because nonblock influences average exactly under physical restriction, direct subtraction gives the exact fixed-block residual

\[
\boxed{
B_A^{\rm RO}
=\mathcal L_A^{\rm RO}
+\mathbb E_Z\Gamma_{\rm RO}(r_Z)-\Gamma_{\rm RO}(r)
-\Delta_AH.
} \tag{3.2}
\]

Theorem 2.1 therefore gives the root-only lower bound

\[
\boxed{
B_A^{\rm RO}\ge
\mathcal L_A^{\rm RO}
+\mathbb E_Z\Gamma_{\rm RO}(r_Z)-\Gamma_{\rm RO}(r)
-2H(U\mid T)-\eta_A.
} \tag{3.3}
\]

Combining with the exact scalar-lift currency produces

\[
\boxed{
D_{\Gamma_*}(G)-\mathbb E_ZD_{\Gamma_*}(G_{A=Z})
\ge
\mathcal L_A^{\rm RO}
+\mathbb E_Z\Gamma_{\rm RO}(r_Z)-\Gamma_{\rm RO}(r)
-2H(U\mid T)-\eta_A+a_*Q_A.
} \tag{3.4}
\]

Thus a sufficient *root-measurable* selector is now explicit: it is enough to find one nonempty proper physical block `A` for which the right side of (3.4) is nonnegative. The branch-to-child spectral mutual information has disappeared; it is paid by one additional copy of the root conditional spectral entropy plus the unavoidable bias penalty.

At uniform input this becomes

\[
\boxed{
D_{\Gamma_*}(G)-\mathbb E_ZD_{\Gamma_*}(G_{A=Z})
\ge
C_0\sum_{i\in A}\operatorname{Inf}_i(G)
+\mathbb E_Z\Gamma_{\rm RO}(r_Z)-\Gamma_{\rm RO}(r)
-2H(S_A\mid S_{A^c})+a_*Q_A,
} \tag{3.5}
\]

where `C_0=6.4548`.

For a minimum-essential-arity counterexample to the stable candidate, every proper restricted child has nonnegative stable defect. Therefore the parent being negative forces the right side of (3.4) to be negative for **every** proper block. In particular, on the uniform cube every such minimal counterexample must satisfy simultaneously

\[
\boxed{
2H(S_A\mid S_{A^c})>
C_0\sum_{i\in A}\operatorname{Inf}_i(G)
+\mathbb E_Z\Gamma_{\rm RO}(r_Z)-\Gamma_{\rm RO}(r)
+a_*Q_A
} \tag{3.6}
\]

for every `empty != A != [n]`.

Equation (3.6) is the concrete structural condition delivered by this run. It is not assumed; it is a proved necessary condition for a minimal counterexample, obtained by applying the new Boolean two-sided constraint to account02/B18's exact selected restriction.

For a uniformly random `r`-block, average (3.3) and combine with account02/B18's exact closed form (0.3). This yields the same simultaneous condition at every scale, now with the explicit currency floor (0.4). The remaining obstacle is therefore purely root-level: control the average conditional spectral entropy and the exact output-potential Jensen term strongly enough to contradict (3.6) at at least one scale.

## 4. Singleton corollary and the exact relation to the old erasure route

For a uniform singleton `A={i}`, let

\[
B_i=H(S_i\mid S_{-i}),
\qquad
JS_i=I(X_i;S_{-i}^{\rm child}).
\]

Then Theorem 2.1 gives the clean universal inequality

\[
\boxed{JS_i\le B_i.} \tag{4.1}
\]

Hence

\[
\boxed{\Delta_iH=B_i+JS_i\le2B_i.} \tag{4.2}
\]

Together with the already-known source bound
`JS_i<=(2/ln 2)Inf_i`, one may record the strictly sharper pointwise identity-compatible estimate

\[
\boxed{
\Delta_iH\le B_i+
\min\left\{B_i,{2\over\ln2}\operatorname{Inf}_i\right\}.
} \tag{4.3}
\]

This does **not** revive the false bound `B_i<=K Inf_i`: the bent-plus-point-defect family has unbounded `B_i/Inf_i`. It instead proves that the *other half* of the one-coordinate entropy drop, the branch Jensen-Shannon term, can never exceed the erasure conditional entropy on the uniform cube.

Summing (4.1) gives

\[
\sum_iJS_i\le\sum_iB_i, \tag{4.4}
\]

another two-sided Boolean correlation constraint. No finite bound on the right side by influence is claimed.

## 5. Adversary checks and why the bias penalty is necessary

### Bent-swap / sparse-defect obstruction

The account03/B13 bent two-point-swap family that kills the pointwise local scalar margin has, at `m=6`,

\[
JS=0.0876767473\ldots,
\qquad
H(S_j\mid S_{-j})=0.1632611854\ldots .
\]

So (4.1) survives with substantial slack. But the conditional spectral entropy itself is the logarithmically expensive term; the theorem does not falsely claim to pay it by one-coordinate influence. This is exactly why the result is applied to the aggregate random-block selector rather than used to resurrect a dead local cap.

### Biased-limit obstruction

The zero-penalty biased analogue of (2.6) is false even in two dimensions. Take biases

\[
(p_0,p_1)=(1/5,9/10),
\]

and the Boolean function that is `-1` only at `(x_0,x_1)=(1,0)` and `+1` at the other three points. Reveal the second coordinate `A={1}`. Direct biased-Walsh calculation gives

\[
H(U\mid T)=0.137351990984347\ldots,
\]

\[
I(Z;T)=0.248854588206471\ldots,
\]

so `I(Z;T)>H(U|T)` by

\[
0.111502597222124\ldots .
\]

But

\[
\eta_A=h_2(0.9)+\log_2(0.9)
=0.316992500144231\ldots,
\]

and (2.4) holds. Therefore the bias penalty is a real structural term, not proof slack that may be discarded in a biased-limit argument.

### Tensor products

The theorem tensorizes exactly: the block transform is the tensor product of the one-coordinate biased transforms, so `-2 log c_A=L_A` and the penalty `eta_A` are additive. Thus tensor replication does not create a hidden dimension factor in (2.4).

### Addressing, majority and tribes

No special monotonicity, low degree, unateness, read-once structure or spectral support shape enters the proof. Hence the inequality itself applies unchanged to addressing, majority and tribes. This is only a robustness check of the structural lemma, not a claim that (3.6) is already contradicted on all such families. The unresolved payment is `H(S_A|S_Ac)` together with the exact output-potential term.

## 6. Decisive finite checks

The accompanying standard-library checker performs two independent falsification passes.

1. At the uniform cube it exhausts every Boolean function through `n=4` modulo global output negation and every singleton coordinate: `131474` function/coordinate cases. It finds

\[
\max(JS_i-B_i)=0
\]

to floating precision, and the maximum observed ratio `JS_i/B_i` is exactly `1` to the printed precision.

2. It checks `750` deterministic random biased Boolean/block instances through `n=4` against (2.4); the largest observed value of `I(Z;T)-H(U|T)-eta_A` is `-5.622e-02`. It separately verifies the explicit two-bit counterexample above to the unpenalized biased inequality.

Checker SHA-256:
`ef5787a2e0151afe4e8eb3057179253fc944a06277bb7e9de397469418ff936e`.

Captured output SHA-256:
`6fe2fb8ccfc1d5f7980ecdc78670c43122b50c1a23793d9dd3683d754e8ee71c`.

The analytic theorem does not depend on these finite tests.

## 7. Exact status movement

**Old missing implication.** Prove `EXACT-RANDOM-BLOCK-RO-DEFICIT-v1`: find a proper block scale for which `B_r^RO+a_*Q_r>=0`, thereby closing the stable all-gate induction.

**New proved inference.** For every actual Boolean physical block, the branch/spectral correlation satisfies the dimension-free entropic-uncertainty constraint (2.4). Consequently the exact signed block residual has the root-only lower bound (3.3), and every minimal stable-candidate counterexample must satisfy the simultaneous block inequalities (3.6) at every proper block and every scale.

**Still missing.** Show that no composition-prime Boolean gate can satisfy (3.6) for all proper blocks. Equivalently, prove that at some scale the root conditional spectral entropy plus the exact output-potential deficit is paid by the block input charge and account02/B18's exact Poincare currency. A crude Han bound

\[
\mathbb E_{|A|=r}H(S_A\mid S_{A^c})\le {r\over n}H(S)
\]

is true but is not enough by itself and would not constitute an FEI proof. The next useful step must exploit Boolean realizability or the simultaneous multiscale constraints, not simply replace the remaining conditional entropy by global `H`.

**Classification:** `AUXILIARY_ONLY`. The structural theorem is new within this proof chain and is directly applied to the selected restriction, but it does not yet prove the existential selector (0.2). Therefore it is not promoted to `ESSENTIAL_STEP_APPLIED`, and full FEI remains open.

No publication-priority claim is made.
