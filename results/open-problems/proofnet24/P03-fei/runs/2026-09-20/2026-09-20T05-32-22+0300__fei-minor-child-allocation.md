Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P03 FEI — arbitrary-child conditional allocation with a paid minor-child influence

## Status and mathematical delta

**Parent problem:** Friedgut--Kalai Fourier entropy--influence (FEI): find one finite universal constant C such that

\[
H(\widehat f^2)\le C I(f)
\]

for every Boolean function on every finite uniform cube.

**Source-level status before -> after:** **OPEN/PARTIAL -> OPEN/PARTIAL.** No universal FEI constant is proved. The source metric “finite universal upper bound for C_FEI” remains **UNKNOWN -> UNKNOWN**. The inherited P03 finite-dimensional atlas remains **6 -> 6**.

**Mechanism-level gain:** the companion NM13-02 run proved a dimension-free local hereditary payment when one physical child is a signed character. This run removes that structural hypothesis completely. For every split at coordinate i with children f^+,f^-,

\[
\boxed{
B_i(f):=H(Z_i\mid Z_{-i})
\le C_\chi\,j_i(f)+\min\{I(f^+),I(f^-)\},
}
\]

where

\[
j_i(f)=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\},
\qquad
C_\chi=2+\frac1{\sqrt e\,\ln2}=2.8750387749\ldots .
\]

Thus the logarithmic marginal-entropy loss exposed by P03's one-defect obstruction is replaced by an exactly named **minor-child influence payment**. The new estimate is all-dimensional, fresh-variable-free, and assumes no branch independence.

For an arbitrary physical restriction tree T it gives

\[
R_T\le C_\chi J_T+L_T,
\qquad
L_T:=\sum_{v\text{ internal}}w_v\min\{I(f_v^+),I(f_v^-)\}.
\]

For an **influence-heavy spine** (at each branch continue only the larger-influence child and stop the smaller-influence child), L_T is exactly twice the weighted influence of the stopped minor leaves. Combining this identity with P03's already-proved paid recombination estimate yields a new closure theorem: if every stopped minor leaf and the terminal heavy leaf satisfy FEI with constant C_0, then the root satisfies FEI with

\[
\boxed{
C_{\rm root}\le
\max\left\{
C_\chi+\frac2{\ln2},\ C_0+2
\right\}.
}
\]

In particular, an influence-heavy spine whose stopped leaves and terminal leaf are symmetric inherits the known symmetric constant 12.04 with only an additive 2, hence constant 14.04. This is a restricted closure theorem, not full FEI.

The remaining universal obstruction is now sharper: control the **minor-child load** L_T on a suitable stopping tree, or show that repeatedly entering minor branches can be amortized without an unbounded depth loss.

## Dependencies actually consumed

The owner progress-first directive was followed: only dependencies needed for the live FEI obstruction were read.

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: P03 remains the T01 FEI owner; roughly 90% of effort should be new derivation; restricted results do not close FEI.
- `operations/PROB10_2026-09-20.md`: the fresh-control theorem `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` requires added controls and `2^{-c}M_0(f)<=1`; it is explicitly not full FEI.
- `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`: full FEI remains open; the false resolvent, pointwise-erasure, fixed-affine-drift and Han absolute-overlap routes remain retired; newer quadratic-twist and shifted-threshold results retain their exact restricted scopes.
- P03 newest substantive report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T04-29-36+0300__fei-one-defect-marginalization-obstruction.md`, blob `fa6cee742e707749ab2d0dc92156d467cffec8c2`: proves that the weighted derivative-degree and marginal spectral-bit envelopes diverge on one-defect/OR functions while the true hereditary allocation stays bounded. The present proof attacks the exact missing side-information term rather than reviving those surrogates.
- P03 `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T02-31-19__fei-hereditary-recombination-refinement.md`, blob `8ffb9da5bc03c30e6ed5f62adc17640d1570878c`: supplies the exact tree telescopes and the already-proved recombination payment `S_T <= (2/ln2) J_T`.
- Fresh-control dependency `proofnet24/P03-fei/scheduled-continuation/runs/2026-09-19/2026-09-19T22-18-30Z__report.md`, blob `22362306d41f9b6d3d0f221ddda3d303b8a47968`: its theorem is restricted to added fresh controls and is not used below as a fixed-domain argument.
- Companion NM13-02 newest report `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T05-10-56+0300__character-child-conditional-allocation.md`, blob `f887b25f10a6e3aeaee737cdc697dbf4dad03ed4`: proves the exact character-child formula and constant `C_chi`, plus character-canalizing max-splicing. The current theorem strictly enlarges the local hypothesis from “one child is a character” to arbitrary children, at the cost of the smaller child's total influence.

`POSTED.md` exact-scope exclusions were respected. No posted unrestricted FEI theorem is claimed or modified.

## Current public-source scope

A fresh source check on 20 September 2026 found González--MacManus--Pereyra, arXiv:2606.00246, still stating universal FEI as a conjecture. Its induction requires a branching coordinate for which the full entropy decrement is paid by the queried influence, and its stopping-tree extension permits known FEI classes at stopping leaves. It proves restricted families, not a universal theorem. The historical Friedgut--Kalai 1996 source attribution is unchanged.

The theorem below weakens the local burden in a different direction: every coordinate has a universal conditional-allocation estimate once one also charges the smaller child's total influence. The influence-heavy spine theorem then turns that additive child term into a one-time leaf payment. This does not imply that every Boolean function has a bounded-depth such decomposition into already-certified leaves.

## 1. Notation and exact fiber formula

Let

\[
f:\{-1,1\}^{\{i\}\cup V}\to\{-1,1\}
\]

and write its restrictions at coordinate i as

\[
g=f^+,
\qquad h=f^-.
\]

For `T subset V`, put

\[
a_T=\widehat g(T),
\qquad b_T=\widehat h(T).
\]

The two parent Fourier coefficients over the same residual fiber are

\[
\widehat f(T)=\frac{a_T+b_T}{2},
\qquad
\widehat f(T\cup\{i\})=\frac{a_T-b_T}{2}.
\]

Thus, if

\[
q_T=\frac{a_T^2+b_T^2}{2},
\qquad
e_T=\frac{(a_T-b_T)^2}{4},
\]

then the conditional spectral-bit entropy is exactly

\[
\boxed{
B_i(f)=\sum_{T\subseteq V}q_T h_2(e_T/q_T),
}
\tag{1.1}
\]

with the zero-mass terms interpreted as zero.

The queried influence is

\[
\operatorname{Inf}_i(f)=\frac14\sum_T(a_T-b_T)^2=\Pr[g\ne h].
\tag{1.2}
\]

Multiplying f by the physical character `x_i` toggles the spectral bit `Z_i`, hence leaves `B_i(f)` unchanged. It replaces h by `-h`, leaves both child total influences unchanged, and changes the queried influence from delta to `1-delta`. Therefore all estimates may normalize

\[
\varepsilon:=j_i(f)
=\min\{\Pr[g\ne h],\Pr[g=h]\}
\le\frac12.
\tag{1.3}
\]

After this normalization we again write g,h for the two children and have

\[
\Pr[g\ne h]=\varepsilon.
\]

Finally exchange the two children if necessary so that

\[
I(g)=\min\{I(f^+),I(f^-)\}.
\tag{1.4}
\]

A common global sign is irrelevant, so choose it such that `E g >=0`.

## 2. Theorem A — arbitrary-child conditional allocation

**Theorem A.** For every Boolean f and every physical coordinate i,

\[
\boxed{
B_i(f)
\le
C_\chi j_i(f)+\min\{I(f^+),I(f^-)\},
}
\tag{2.1}
\]

where

\[
C_\chi=2+\frac1{\sqrt e\,\ln2}<2.876.
\tag{2.2}
\]

No dimension, degree, monotonicity, fresh-variable, independence, or character-child assumption is present.

### Proof

Use the normalization from Section 1. Let

\[
\eta=\Pr[g=-1],
\qquad
\beta=\Pr[h=-1].
\]

Because `E g>=0`,

\[
0\le\eta\le\frac12.
\]

Because g and h differ on an epsilon fraction of the cube,

\[
|\beta-\eta|\le\varepsilon.
\tag{2.3}
\]

Also

\[
\widehat g(\varnothing)=1-2\eta,
\qquad
\widehat h(\varnothing)=1-2\beta.
\tag{2.4}
\]

We split (1.1) into the nonconstant Fourier fibers `T != emptyset` and the exceptional constant fiber.

### Step 1: all nonconstant fibers are paid by the minor child influence plus `2 epsilon(1-epsilon)`

Each binary entropy is at most one, so

\[
\begin{aligned}
\sum_{T\ne\varnothing}q_T h_2(e_T/q_T)
&\le \sum_{T\ne\varnothing}q_T\\
&=\frac12\left(\operatorname{Var}(g)+\operatorname{Var}(h)\right)\\
&=2\eta(1-\eta)+2\beta(1-\beta).
\end{aligned}
\tag{2.5}
\]

We claim

\[
\beta(1-\beta)
\le
\eta(1-\eta)+\varepsilon(1-\varepsilon).
\tag{2.6}
\]

Put `t=beta-eta`. If `t<=0`, then

\[
\beta(1-\beta)-\eta(1-\eta)
=t(1-2\eta)-t^2\le0
\]

because `eta<=1/2`. If `t>=0`, then `0<=t<=epsilon<=1/2`, and

\[
\beta(1-\beta)-\eta(1-\eta)
=t(1-2\eta)-t^2
\le t(1-t)
\le\varepsilon(1-\varepsilon),
\]

since `x(1-x)` is increasing on `[0,1/2]`. This proves (2.6).

Insert (2.6) into (2.5):

\[
\sum_{T\ne\varnothing}q_T h_2(e_T/q_T)
\le
4\eta(1-\eta)+2\varepsilon(1-\varepsilon).
\tag{2.7}
\]

For Boolean g,

\[
4\eta(1-\eta)=\operatorname{Var}(g)\le I(g)
\tag{2.8}
\]

by the standard cube Poincare inequality, equivalently by the Fourier identity

\[
\operatorname{Var}(g)=\sum_{S\ne\varnothing}\widehat g(S)^2
\le\sum_{S\ne\varnothing}|S|\widehat g(S)^2=I(g).
\]

Therefore

\[
\boxed{
\sum_{T\ne\varnothing}q_T h_2(e_T/q_T)
\le I(g)+2\varepsilon(1-\varepsilon).
}
\tag{2.9}
\]

### Step 2: the exceptional fiber costs only `epsilon^2 log(e/epsilon^2)`

For `T=emptyset`, equations (2.4) give

\[
e_0
=\frac{(\widehat g(\varnothing)-\widehat h(\varnothing))^2}{4}
=(\beta-\eta)^2
\le\varepsilon^2.
\tag{2.10}
\]

Its total fiber mass `q_0` is at most one. For fixed `0<=e<=q<=1`, the function

\[
F_e(q):=q h_2(e/q)
\]

is increasing in q: in natural logarithms its derivative is

\[
F_e'(q)=\log_2\frac{q}{q-e}\ge0.
\]

Hence

\[
q_0h_2(e_0/q_0)\le h_2(e_0).
\tag{2.11}
\]

Use the elementary entropy estimate

\[
h_2(x)\le x\log_2\frac e x,
\qquad 0\le x\le1.
\tag{2.12}
\]

The function `x log_2(e/x)` is increasing on `[0,1]`; therefore (2.10)--(2.12) yield

\[
\boxed{
q_0h_2(e_0/q_0)
\le
\varepsilon^2\log_2\frac e{\varepsilon^2}.
}
\tag{2.13}
\]

### Step 3: optimize the scalar remainder

Combining (2.9) and (2.13),

\[
B_i(f)
\le I(g)+\varepsilon U(\varepsilon),
\tag{2.14}
\]

where

\[
U(\varepsilon)
=2(1-\varepsilon)
+\varepsilon\log_2\frac e{\varepsilon^2}.
\tag{2.15}
\]

On `(0,1/2]`,

\[
U'(\varepsilon)
=-2+\frac{-1-2\ln\varepsilon}{\ln2},
\qquad
U''(\varepsilon)=-\frac2{\varepsilon\ln2}<0.
\]

The unique maximizer is

\[
\varepsilon_0=\frac1{2\sqrt e},
\]

and

\[
U(\varepsilon_0)
=2+\frac1{\sqrt e\,\ln2}=C_\chi.
\tag{2.16}
\]

Thus

\[
B_i(f)\le I(g)+C_\chi\varepsilon.
\]

Using (1.3)--(1.4) proves (2.1). QED.

### Relation to the companion character-child theorem

If the lower-influence child is a character, then `I(g)` need not be zero unless it is constant, so Theorem A does not subsume the companion theorem numerically in every character case. The logical hypotheses are nevertheless incomparable in the useful direction: Theorem A applies to **every split**. When one child is a signed character, the companion exact Fourier-fiber calculation should still be used because it removes the minor-child term altogether.

For the one-defect family, the minor child is constant, so Theorem A recovers exactly the same universal local constant `C_chi` and repairs the marginalization obstruction without a family-specific calculation.

## 3. Corollary — arbitrary-tree minor-child load

For a finite adaptive physical restriction tree T, retain P03's notation

\[
R_T=\sum_vw_vB_{i(v)}(f_v),
\qquad
J_T=\sum_vw_vj_{i(v)}(f_v),
\qquad
Q_T=\sum_vw_v\operatorname{Inf}_{i(v)}(f_v).
\]

Define

\[
L_T
:=\sum_{v\text{ internal}}w_v
\min\{I(f_v^+),I(f_v^-)\}.
\tag{3.1}
\]

Applying Theorem A at every internal node gives the all-dimensional fresh-variable-free estimate

\[
\boxed{
R_T\le C_\chi J_T+L_T
\le C_\chi Q_T+L_T.
}
\tag{3.2}
\]

This is the current clean reduction of hereditary allocation. The old derivative-degree and marginal-entropy surrogates have been removed; the only new residual term is a literal child influence already present in the physical restriction process.

The estimate is not by itself full FEI because `L_T/I(f)` is not known to be universally bounded on a full tree. For example, blindly expanding a parity tree would make a min-child bookkeeping term grow with depth even though the true allocation is zero; known stopping certificates must be used rather than recursively charging (3.2) where they are unnecessary.

## 4. Theorem B — influence-heavy spine closure

A finite partial restriction tree is an **influence-heavy spine** if it has a single internal path. At every internal node v, query an arbitrary free coordinate, designate the child with larger total influence as the continuing child, and make the child with smaller total influence a stopping leaf. Ties may be broken arbitrarily. The last continuing child is also a stopping leaf.

Let

\[
I_{\rm min}
=\sum_{\ell\text{ minor stopping leaf}}w_\ell I(f_\ell),
\qquad
I_{\rm end}=w_{\rm end}I(f_{\rm end}).
\]

Then by construction, if v has weight `w_v` and minor child influence `m_v`, that leaf has weight `w_v/2`, so

\[
\boxed{L_T=2I_{\rm min}.}
\tag{4.1}
\]

The exact influence telescope from the preceding P03 report gives

\[
\boxed{Q_T+I_{\rm min}+I_{\rm end}=I(f).}
\tag{4.2}
\]

### Theorem B1 (hereditary allocation closure)

Suppose every stopping leaf ell has a continuation tree satisfying

\[
R(f_\ell)\le K I(f_\ell).
\]

Then grafting those continuation trees onto the heavy spine yields

\[
\boxed{
R_{\rm graft}(f)
\le
\max\{C_\chi,K+2\}\,I(f).
}
\tag{4.3}
\]

**Proof.** By (3.2) and (4.1),

\[
R_T\le C_\chi Q_T+2I_{\rm min}.
\]

The grafted leaf continuations cost at most

\[
K(I_{\rm min}+I_{\rm end}).
\]

Thus

\[
R_{\rm graft}
\le C_\chi Q_T+(K+2)I_{\rm min}+KI_{\rm end}.
\]

Apply (4.2) and take the largest coefficient. QED.

### Theorem B2 (source-facing FEI closure)

Suppose instead that every stopping leaf satisfies the FEI inequality

\[
H(f_\ell)\le C_0 I(f_\ell).
\tag{4.4}
\]

Then

\[
\boxed{
H(f)
\le
\max\left\{
C_\chi+\frac2{\ln2},\ C_0+2
\right\}I(f).
}
\tag{4.5}
\]

Numerically,

\[
C_\chi+\frac2{\ln2}
=5.76042885669\ldots .
\]

**Proof.** P03's exact tree identity gives

\[
H(f)=H_L+R_T+S_T.
\]

The already-proved recombination estimate gives

\[
S_T\le\frac2{\ln2}J_T.
\]

By (3.2), (4.1), and `J_T<=Q_T`,

\[
R_T+S_T
\le
\left(C_\chi+\frac2{\ln2}\right)Q_T+2I_{\rm min}.
\]

The leaf hypothesis gives

\[
H_L\le C_0(I_{\rm min}+I_{\rm end}).
\]

Combine these and use (4.2):

\[
H(f)
\le
\left(C_\chi+\frac2{\ln2}\right)Q_T
+(C_0+2)I_{\rm min}
+C_0I_{\rm end},
\]

which is bounded by the right side of (4.5). QED.

### Concrete restricted application

The known symmetric-function FEI theorem supplies `C_0=12.04`. Therefore any Boolean function admitting an influence-heavy spine for which **every minor stopping child and the final heavy child are symmetric functions** satisfies

\[
\boxed{H(f)\le14.04\,I(f).}
\tag{4.6}
\]

No fresh variables are introduced. This class is not asserted to contain every Boolean function, and no priority claim is made for this closure operation.

The one-defect/OR family has constant minor children along its heavy spine, so (4.5) gives the dimension-free bound `H<=5.761 I`; the exact family-specific ratio still tends to 4.

## 5. Why three tempting alternatives were not used

The progress-first instruction asks for materially different methods after failures. Three routes were compared in this run.

1. **TV/Hellinger payment.** From (1.1) and `h_2(p)<=2 sqrt(p(1-p))`, one gets
   \[
   B_i(f)\le\frac12\sum_T|a_T^2-b_T^2|
   \le2\sqrt{j_i(1-j_i)}.
   \]
   This is dimension-free but has a square-root loss at small influence, so it cannot pay hereditary allocation linearly.
2. **Entropy continuity around a character child.** A direct Fannes-type perturbation of the companion character theorem introduces the ambient spectral support size and recreates the logarithmic dimension loss seen in the one-defect report. This route was not pursued.
3. **Posterior fiber split by the lower-influence child.** The successful argument above isolates all nonconstant Fourier fibers, pays their total mass by the lower child's variance/influence, and confines the rare logarithm to the single constant fiber where the mismatch is quadratic (`e_0<=j_i^2`). This is the genuinely different method executed here.

Thus no retired resolvent, erasure, fixed-affine-drift, derivative-degree, or absolute-overlap claim is being repackaged.

## 6. Sanity checker executed now

A new checker was executed against the theorem itself.

- exhaustive ordered child pairs in residual dimensions 0,1,2,3: `4 + 16 + 256 + 65536 = 65812` pairs;
- 5000 deterministic-seed sampled pairs in each residual dimension 4,5,6,7,8: 25000 additional pairs;
- both correlated one/few-flip pairs, independent random pairs, and near-complements were included, so the folded-influence normalization `j=min(delta,1-delta)` was exercised on both sides of 1/2.

Every case satisfied

\[
B_i\le C_\chi j_i+\min(I_+,I_-).
\]

The recorded global maximum numerical violation was `0.0` (attained only on trivial zero-cost pairs); sampled nontrivial cases had strictly negative margins. These computations are self-checks only; the theorem rests on the proof above.

Preserved artifacts:

- checker: `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T05-32-22+0300__check_minor_child_payment.py`, creation commit `2385dac20c18ec97e1b888b65e4d0988f650d22b`;
- output: `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T05-32-22+0300__minor_child_payment_check.json`, creation commit `70483a9f21c1d28f3c11fb5806d74699d32a1568`.

## 7. Remaining full-scope obstruction and next attack

Full FEI remains open. The new local theorem removes the companion character-child hypothesis but introduces the residual load

\[
L_T=\sum_vw_v\min\{I(f_v^+),I(f_v^-)\}.
\]

The next nonredundant question is not another scalar envelope for `B_i`. It is whether one can choose a stopping tree so that **minor-child influence is paid only O(1) times** before every branch reaches an already-certified class. Two concrete attacks are now sharply separated:

1. prove an influence-heavy decomposition theorem with bounded recursive minor-branch depth, using known stopping classes (symmetric, quadratic, character-canalizing, separated tribes) and exact max-splicing;
2. construct a family for which every such decomposition has unbounded minor-branch depth/load, which would decisively retire this new route while leaving FEI itself open.

A useful stress family for (2) should avoid the already-certified symmetric and character-canalizing regimes; random one-point perturbations of bent phases are a natural first test because they make a chosen rare coordinate locally expensive while retaining high spectral side-information complexity.

## Source metric / mechanism metric

- Universal FEI finite constant: **UNKNOWN -> UNKNOWN**.
- P03 native finite atlas: **6 -> 6**.
- Fresh-control theorem: unchanged and restricted.
- New all-dimensional mechanism: character-child local hypothesis -> **arbitrary child**, with exact additive payment `min child total influence`.
- New tree closure: influence-heavy spine into FEI-certified leaves, constant `max(C_chi+2/ln2,C_0+2)`.
- Full closure: **not claimed**.

## ledger_delta

- `P03-FEI-MINOR-CHILD-ALLOCATION-322 = PROVED / SELF-CHECKED / ALL-DIMENSIONAL / FRESH-VARIABLE-FREE / FULL-FEI-STILL-OPEN / INDEPENDENT-REVIEW-PENDING`.
- Preserve P03's prior paid recombination theorem and one-defect obstruction.
- Preserve NM13-02 character-child theorem as sharper when its character hypothesis holds; this run does not overwrite peer claims.
- Retire no additional historical theorem, but replace the live “character-child only” obstruction by the sharper residual `minor-child influence load`.
- Source metric remains UNKNOWN; finite atlas remains 6.
- Next P03 target: bound or refute universal stopping-tree control of the recursive minor-child load without fresh variables.

**End of complete run report.**
