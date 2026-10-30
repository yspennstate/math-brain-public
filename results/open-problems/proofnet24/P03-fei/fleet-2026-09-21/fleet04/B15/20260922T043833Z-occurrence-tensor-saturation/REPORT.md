# B15 — the exact occurrence-KL remainder has the same sharp constant as FEI

**Run:** `20260922T043833Z-b15-fei-r11`  
**Role:** fleet04/B15, FEI Shannon/arithmetic remainder transfer.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SHARP-CONSTANT OBSTRUCTION`; unrestricted FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and mathematical sources were read directly, but no authenticated native/cognitive-brain retrieval was consumed.

## 0. Change summary

This run does not repeat the previous one-dimensional `B0` slice. It consumes fleet02/B15's newest source-exact harmonic/KL handoff and tests its *remaining scalar occurrence remainder* against tensor powers and balanced suspension.

The result is exact: after retaining the factorial credit, the prefix relative-entropy credit, and the new root/deletion mixing KL credit, the remaining scalar occurrence functional has **the same optimal universal constant as FEI itself**. Thus this exact three-credit scalar transfer is FEI-complete rather than a strictly easier remainder theorem.

This is a proof-architecture obstruction, not a counterexample to FEI. It does not refute using the one-time valuation reserve jointly with the information credits, nor the exact local restriction cocycle.

## 1. Exact inherited remainder — all negative credits retained

The consumed peer artifact is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T040227Z-balanced-stop-kl-fusion/HANDOFF.md`

(blob `e2b3c0c53bd5cc8cccf25c3ed7f9d88f033a9e27`; complete proof in the adjacent `REPORT.md`).

For a balanced Boolean function `f`, let `S` be a Fourier support sampled from the squared spectrum, let `K=|S|`, put

\[
I=\mathbb E K,\qquad \beta=I-1,
\]

and define

\[
\alpha_i=\mathbb E\frac{\mathbf 1_{\{i\in S\}}}{K},
\qquad
\rho_i=\frac1\beta\mathbb E\frac{K-1}{K}\mathbf 1_{\{i\in S\}},
\qquad
q_i=\frac{\operatorname{Inf}_i(f)}I.
\]

Then `q=(alpha+beta rho)/I`. The peer proves the exact mixing credit

\[
\mathcal J_{\rm mix}
=D_{\rm KL,2}(\alpha\|q)+\beta D_{\rm KL,2}(\rho\|q)\ge0
\]

and, together with the earlier physical-prefix credit `mathcal K_rho`, the exact identity

\[
\boxed{
H(f)=I H_2(q)+T_{\rm stop}
-\mathbb E\log_2(K!)-\mathcal K_\rho-\mathcal J_{\rm mix}.
}
\tag{1.1}
\]

Thus the actual unpaid scalar occurrence expression is

\[
\boxed{
\mathcal U_{\rm occ}(f)
:=I H_2(q)-\mathbb E\log_2(K!)-\mathcal K_\rho-\mathcal J_{\rm mix}
=H(f)-T_{\rm stop}(f).
}
\tag{1.2}
\]

No packet integrality or credit-free interpolation is being assumed. The same fleet02 report also proves, for finite absolute constants,

\[
T_{\rm stop}(f)\le C_{\rm stop}(I(f)-1),
\qquad
J(f)\le C_J(I(f)-1),
\qquad
R(f)\le2C_J(I(f)-1),
\tag{1.3}
\]

where `R` is the one-time signed valuation reserve. In particular, the remaining proposed scalar transfer is

\[
\mathcal U_{\rm occ}(f)\le C_{\rm occ}(I(f)-1)
\tag{1.4}
\]

for every balanced Boolean `f`.

## 2. Sharp-constant theorem

Define the extended-real sharp constants

\[
C_{\rm FEI}
:=\sup_{g\ {m nonconstant\ Boolean}}\frac{H(g)}{I(g)},
\tag{2.1}
\]

and

\[
C_{\rm occ}
:=\sup_{\substack{f\ {m balanced\ Boolean}\\ I(f)>1}}
\frac{\mathcal U_{\rm occ}(f)}{I(f)-1}.
\tag{2.2}
\]

### Theorem 2.1 — tensor-suspension saturation

\[
\boxed{C_{\rm occ}=C_{\rm FEI}}
\tag{2.3}
\]

as an equality in `[0,+infinity]`.

### Proof: upper bound

The stopping entropy is nonnegative, so (1.2) gives

\[
\mathcal U_{\rm occ}(f)\le H(f).
\]

The completed balanced-support-deficit equivalence in

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B13/20260922T003238Z-balanced-uniform-gate-slice/REPORT.md`

states, constant for constant,

\[
\sup_{f\ {m balanced},\ I(f)>1}
\frac{H(f)}{I(f)-1}=C_{\rm FEI}.
\tag{2.4}
\]

Therefore

\[
C_{\rm occ}\le C_{\rm FEI}.
\tag{2.5}
\]

### Proof: lower bound

Fix any nonconstant Boolean seed `g` on `n>=1` variables. For `k>=1`, let

\[
h_k(x^{(1)},\ldots,x^{(k)})
=\prod_{a=1}^k g(x^{(a)})
\tag{2.6}
\]

on `k` disjoint copies of the variables, and then add one fresh unbiased Rademacher coordinate `y` and form the balanced suspension

\[
f_k(y,x)=y\,h_k(x).
\tag{2.7}
\]

The squared Fourier law of a disjoint product is the product of the squared Fourier laws. Hence Shannon entropy and support-size mean add:

\[
H(h_k)=kH(g),
\qquad
I(h_k)=kI(g).
\tag{2.8}
\]

Multiplication by the fresh character `y` merely adjoins that coordinate to every Fourier support and leaves every squared Fourier mass unchanged. Consequently `f_k` is balanced and

\[
H(f_k)=kH(g),
\qquad
I(f_k)-1=kI(g).
\tag{2.9}
\]

Let `K_k` denote the Fourier support size under the squared spectrum of `f_k`. Every support of `h_k` has size between `0` and `kn`, so

\[
1\le K_k\le kn+1.
\tag{2.10}
\]

Fleet02/B15 proves, for the same physical stopping process used in (1.1),

\[
0\le T_{\rm stop}(f_k)\le H_2(K_k).
\tag{2.11}
\]

Since `K_k` takes at most `kn+1` integer values,

\[
T_{\rm stop}(f_k)\le\log_2(kn+1).
\tag{2.12}
\]

Using (1.2), (2.9), and (2.12),

\[
\begin{aligned}
\frac{\mathcal U_{\rm occ}(f_k)}{I(f_k)-1}
&=\frac{H(f_k)-T_{\rm stop}(f_k)}{kI(g)}\\
&\ge
\frac{H(g)}{I(g)}-
\frac{\log_2(kn+1)}{kI(g)}.
\end{aligned}
\tag{2.13}
\]

The last term tends to zero. Therefore

\[
C_{\rm occ}\ge\frac{H(g)}{I(g)}.
\]

Since `g` was arbitrary,

\[
C_{\rm occ}\ge C_{\rm FEI}.
\tag{2.14}
\]

Together with (2.5), this proves (2.3). QED.

## 3. Consequences for interface D

The proposed exact scalar occurrence transfer (1.4) is not a cheaper sharp-constant surrogate for FEI. Its best possible universal constant is exactly the FEI constant:

\[
\boxed{
\sup_{f\ {m balanced}}
\frac{I H_2(q)-\mathbb E\log_2(K!)-\mathcal K_\rho-\mathcal J_{\rm mix}}
{I-1}
=C_{\rm FEI}.
}
\tag{3.1}
\]

This conclusion already retains **all three** currently source-exact refunds: factorial, prefix KL, and root/deletion mixing KL. The theorem therefore does not repeat the older credit-free obstruction.

Moreover, using (1.3), finiteness of (1.4) is equivalent to FEI at the level of existence of a dimension-independent constant: a scalar occurrence bound plus `T_stop=O(I-1)` implies the balanced support-deficit FEI bound, while FEI immediately bounds `U_occ<=H`. The sharp-constant statement (2.3) is stronger.

The certified balanced shared-graft lower bound consumed by fleet03/B13 is

\[
\frac{H(F)}{I(F)-1}
\ge
6.521850083658612443633672199029299526203969333669\ldots .
\tag{3.2}
\]

Hence the same lower bound applies to `C_occ`. Any scalar theorem of form (1.4) with a smaller constant is impossible.

## 4. What is *not* refuted

The theorem does **not** show that the one-time valuation reserve `R` is negligible on the tensor-suspension family. Therefore it does not refute a genuinely joint inequality such as

\[
\mathbb E\log_2(K!)+\mathcal K_\rho+\mathcal J_{\rm mix}+R
\ge I H_2(q)-C_*(I-1).
\tag{4.1}
\]

Nor does it refute a conditional/non-scalar decomposition that couples valuation to the exact KL fibres before summation. Those are now the meaningful interface-D targets.

Likewise, the all-gate restriction cocycle from fleet04/B17 remains source-valid: local branch uncertainty and vertical overlap appear as exact information credits and can be coupled to child slack. The present theorem says only that compressing the whole remaining Shannon cost into the one scalar `U_occ` cannot improve the extremal constant.

## 5. Exact next implication

The next useful B15 attack should keep `R` *inside* the same source-consistent information decomposition and ask whether the **valuation-assisted residual**

\[
\mathcal U_{\rm occ}(f)-R(f)
\tag{5.1}
\]

(or a sharper conditional version before averaging) has a universal support-deficit bound whose tensor-suspension asymptotics are strictly smaller than `C_FEI`.

A proposed replacement must be tested on the family (2.7) before any new machinery is built. If its extra credit is only `o(k)` on those suspensions, the argument above immediately shows that it still saturates at `H(g)/I(g)` and cannot simplify the sharp extremal problem.

## 6. Scope and literature

No novelty or publication-priority claim is made for Theorem 2.1 without a broader literature review. Fresh primary-source checking on 22 September 2026 still shows unrestricted FEI open: Potapov's 18 September 2026 preprint proves FEI for plateaued functions (sharp class constant 4) and partially bent functions (sharp class constant 2), not arbitrary Boolean functions; González--MacManus--Pereyra's 29 May 2026 preprint gives a restriction/stopping-tree programme whose key universal inequality would imply full FEI; and Li--Han's 2025 information-theoretic inequality retains an additional influence-profile entropy term.

No benchmark gold, mock theorem, packet-integrality assumption, credit-free interpolation, external compute, or unrelated private data was used.
