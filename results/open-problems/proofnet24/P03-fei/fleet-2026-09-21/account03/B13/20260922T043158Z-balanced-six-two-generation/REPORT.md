# account03/B13 — two-generation child-slack payment closes the balanced six-bit zero-singleton slice

**Classification:** `ESSENTIAL_STEP_APPLIED / STRUCTURED_SLICE_CLOSED`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact live target, correction, and mechanism change

The live owner target is the all-gate formulation

\[
D_\Gamma(G;p):=
\sum_i \frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u),
\tag{G}
\]

for every Boolean gate and every interior product bias. A universal finite-cap symmetric nonnegative `Gamma` satisfying `(G)` is equivalent to full FEI.

The original read-once fixed point is no longer a viable universal candidate: genuine balanced high-arity Boolean gates already force a larger centre. The compatible successor used throughout the current fleet is

\[
\Gamma_*(u)=\Gamma_{\rm RO}(u)+0.2682048\,u(1-u),
\qquad C_*:=\Gamma_*(1/2)=6.5218512,
\tag{0.1}
\]

with remaining universal statement `LIMIT-PRIME-GATE-LIFT-v1`: prove `D_{Gamma_*}(P;p)>=0` for every composition-prime Boolean gate and every product bias. Full FEI remains open.

The immediately preceding B13 run refuted the stronger pointwise-local strategy: a bent/two-point-swap restriction pair has an exact local requested scalar correction tending to infinity. That run explicitly left a **two-generation child-slack payment** as the next attack. This report executes that different mechanism rather than trying another pointwise local cap.

Two named completed OTHER-account results are consumed substantively:

1. **account04/B17**, `proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`, blob `d32321447c5f30282f243d9a2907ec719d483c92`. It proves the exact restriction entropy/defect cocycle, including the two information credits, and at a uniform pivot gives the exact identities used below.
2. **account01/B17**, `proofnet24/P03-fei/fleet-2026-09-21/account01/B17/20260922T040831Z-balanced-arity5-complete/REPORT.md`, blob `076b4f50407e7af639566671c0367728decc0d28`. It certifies every balanced five-bit uniform Boolean gate and, more strongly than the ratio statement alone, supplies rigorous entropy upper envelopes at each low edge boundary.

The new result combines these two sources into a quantitative two-generation theorem. It is not a re-audit of either source.

## 1. Exact universal statement attempted

Let `G:{-1,1}^6->{-1,1}` be balanced under the uniform measure. Fix a coordinate `j`, and let its two five-bit restrictions be `G_0,G_1`. Assume **both restrictions are balanced**. Equivalently, for a balanced parent,

\[
\widehat G(\{j\})=0.
\tag{1.1}
\]

The attempted statement is:

> **BAL6-ZERO-L1.** Every such gate satisfies the stable balanced gate inequality
> \[
> \boxed{H(G)\le C_*\,[I(G)-1]},\qquad C_*=6.5218512.
> \tag{1.2}
> \]

This is exactly `(G)` for `Gamma_*` on the balanced-uniform slice, because every input has bias `1/2`, `h_2(V_{1/2})=0`, and `Gamma_*(1/2)=C_*`.

The theorem below proves `BAL6-ZERO-L1`. Thus a balanced-uniform six-input falsifier of the current stable candidate must have **no zero singleton Fourier coefficient**.

## 2. Two-generation ledger from the exact restriction cocycle

Let

\[
\delta=\Pr[G_0\ne G_1].
\tag{2.1}
\]

Write `P_b` for the spectral law of `G_b`. At a uniform pivot, account04/B17's exact source identity gives

\[
H(G)=\frac{H(G_0)+H(G_1)}2+\operatorname{JS}(P_0,P_1)+H(J\mid S),
\tag{2.2}
\]

where `J` is the within-pair Fourier-layer bit. The same source gives

\[
I(G)=\frac{I(G_0)+I(G_1)}2+\delta,
\tag{2.3}
\]

and the marginal of `J` is exactly `delta`.

For any constant `C`, define the balanced support-deficit

\[
\mathcal E_C(F):=C[I(F)-1]-H(F)
\tag{2.4}
\]

for a balanced Boolean function. Combining (2.2)-(2.3) yields the exact **two-generation ledger**

\[
\boxed{
\mathcal E_C(G)
=\frac{\mathcal E_C(G_0)+\mathcal E_C(G_1)}2
+C\delta-\operatorname{JS}(P_0,P_1)-H(J\mid S).
}
\tag{2.5}
\]

This is the mechanism missing from the previous pointwise-local attempt: the local information loss is not required to be nonnegative by itself; it is allowed to spend actual child slack.

## 3. Universal information-loss bound in the right normalization

We need a source-valid bound on the last two terms of (2.5).

### Lemma 3.1 — Walsh-square Jensen-Shannon bound

For any two Boolean functions `f_0,f_1` on the same uniform cube and
`delta=Pr[f_0!=f_1]`,

\[
\boxed{
\operatorname{JS}(\widehat f_0^2,\widehat f_1^2)
\le \frac{2}{\ln2}\,\delta.
}
\tag{3.1}
\]

### Proof

For real numbers `a,b`, let `j(a^2,b^2)` denote the contribution of the two masses `a^2,b^2` to equal-weight Jensen-Shannon divergence in bits. First replace `a,b` by `|a|,|b|`; this leaves the spectral masses unchanged and can only decrease `(|a|-|b|)^2` relative to `(a-b)^2`.

Put `x=|a|`, `y=|b|`, `s=x^2+y^2` and

\[
u=\frac{x^2-y^2}{x^2+y^2}.
\]

In natural-log units,

\[
j_{\rm nat}(x^2,y^2)
=\frac{s}{4}\bigl[(1+u)\ln(1+u)+(1-u)\ln(1-u)\bigr].
\]

Also

\[
\frac{(x-y)^2}{2}
=\frac{s}{2}\bigl(1-\sqrt{1-u^2}\bigr).
\]

So it is enough to prove, for `0<=u<1`,

\[
(1+u)\ln(1+u)+(1-u)\ln(1-u)
\le2\bigl(1-\sqrt{1-u^2}\bigr).
\tag{3.2}
\]

The difference right-minus-left vanishes at zero and has derivative

\[
2\left(\frac{u}{\sqrt{1-u^2}}-\operatorname{arctanh}u\right)\ge0,
\]

because the bracket vanishes at zero and its derivative is

\[
(1-u^2)^{-3/2}-(1-u^2)^{-1}\ge0.
\]

Thus `j_nat(a^2,b^2) <= (a-b)^2/2`. Divide by `ln 2`, sum over Walsh coefficients, and use Parseval:

\[
\sum_S(\widehat f_0(S)-\widehat f_1(S))^2
=\mathbb E(f_0-f_1)^2=4\delta.
\]

This gives (3.1). `QED`

Since the marginal of `J` is `delta`, concavity of entropy gives

\[
H(J\mid S)\le H(J)=h_2(\delta).
\tag{3.3}
\]

Therefore, at `C=C_*`, the total local debit in (2.5) is at most

\[
P(\delta):=
\operatorname{JS}+H(J\mid S)-C_*\delta
\le h_2(\delta)+\left(\frac2{\ln2}-C_*\right)\delta.
\tag{3.4}
\]

For five-bit restrictions, `delta=k/32`. The adjacent exact-rational logarithm checker evaluates all `k=1,...,32` with outward atanh-series bounds and proves

\[
\boxed{
P(\delta)<0.110011246728135
}
\tag{3.5}
\]

for every allowed nonzero `delta`; the worst grid value is `delta=2/32=1/16`. For `delta=0`, `P=0` exactly.

## 4. The five-bit child slack has a positive spectral gap away from literals

The account01/B17 certificate gives, for balanced five-bit functions, the following complete low-boundary entropy upper envelope. If `B` is the undirected edge boundary then `I=B/16`:

| `B` | certified `H` upper bound |
|---:|---:|
| 16 | literals |
| 22 | 1.701237775599294 |
| 24 | 3.000000000000000 |
| 26 | 3.716917186688700 |
| 28 | 3.912687890016525 |
| `>=30` | `H<=5` |

There are no balanced five-bit cases at the omitted low boundaries. With `C_*=6.5218512`, these imply the following lower bounds on

\[
\mathcal E_*(F)=C_*[I(F)-1]-H(F):
\]

\[
\begin{array}{c|c}
B & \mathcal E_*(F)\ \text{lower bound}\\\hline
22&0.744456424400706\\
24&0.260925600000000\\
26&0.359239813311300\\
28&0.978700509983475\\
\ge30&0.706619800000000.
\end{array}
\tag{4.1}
\]

Hence every balanced five-bit child is either a literal with zero support-deficit, or has

\[
\boxed{\mathcal E_*(F)\ge s_0:=0.2609256.}
\tag{4.2}
\]

This is the quantitative stability input that the ratio-only statement `H/(I-1)<=6` does not by itself expose.

## 5. PROVED: balanced six-bit zero-singleton theorem

### Theorem 5.1

Let `G` be a balanced Boolean function on six uniform coordinates. If for some coordinate `j` both restrictions `G_0,G_1` are balanced, then

\[
\boxed{H(G)\le6.5218512\,[I(G)-1].}
\tag{5.1}
\]

If at least one child is not a literal, the defect is quantitatively bounded below by

\[
\boxed{
\mathcal E_*(G)>0.020451553271865.
}
\tag{5.2}
\]

### Proof

If at least one child is not a literal, (4.2) gives

\[
\frac{\mathcal E_*(G_0)+\mathcal E_*(G_1)}2\ge\frac{s_0}{2}=0.1304628.
\]

The exact ledger (2.5) and (3.5) therefore give

\[
\mathcal E_*(G)
>0.1304628-0.110011246728135
>0.020451553271865>0.
\]

It remains to handle the case where both children are literals.

* If they are the same signed literal, the pivot is dummy and `G` itself is a literal, so `H=0`, `I=1` and (5.1) is equality.
* If they are opposite signs of the same literal, `G` is a character involving the pivot, so `H=0` and (5.1) is immediate.
* If they are literals on distinct coordinates (with arbitrary signs), they disagree on exactly half the inputs. Their spectra are point masses at distinct singleton sets; the parent spectrum has four atoms of mass `1/4`. Hence `H(G)=2`, `I(G)=3/2`, and
  \[
  \mathcal E_*(G)=\frac{C_*}{2}-2=1.2609256>0.
  \]

These cases exhaust literal pairs. `QED`

## 6. Correlation/Booleanity consequence for the live gate search

For a balanced parent under uniform measure,

\[
\widehat G(\{j\})=0
\quad\Longleftrightarrow\quad
G_0\ \text{and}\ G_1\ \text{are both balanced}.
\tag{6.1}
\]

Therefore Theorem 5.1 has the following immediate contrapositive.

### Corollary 6.1

Any balanced-uniform six-input gate violating the current stable centre bound

\[
H(G)>6.5218512\,[I(G)-1]
\]

must satisfy

\[
\boxed{\widehat G(\{j\})\ne0\quad\text{for every coordinate }j.}
\tag{6.2}
\]

Because a balanced six-bit Walsh coefficient is an integer multiple of `1/16`, every such hypothetical falsifier has

\[
\boxed{|\widehat G(\{j\})|\ge1/16\quad\forall j,}
\qquad
\boxed{W^{=1}(G)\ge6/256=3/128.}
\tag{6.3}
\]

Input negations can independently flip the singleton signs, so an adversarial search may, without changing entropy or influence, normalize all six singleton coefficients to be positive. Thus the entire balanced arity-six threat is forced into one strict first-order correlation chamber.

This is a genuine Booleanity/correlation restriction, not a statement about arbitrary spectral probability laws.

## 7. Decisive computation and failure search

`CHECKER.py` performs only the finite arithmetic left by the analytic proof:

1. imports the peer-certified entropy upper bounds as exact decimal rationals;
2. verifies the five possible nonliteral child-boundary classes all have support-deficit at least `s_0=0.2609256`;
3. evaluates `h_2(k/32)` using exact rational atanh-series logarithm enclosures, with a rigorous positive remainder bound;
4. checks all `k=1,...,32` and finds the largest possible information debit at `k=2`,
   \[
   P_{\max}<0.110011246728135;
   \]
5. verifies the residual theorem margin exceeds `0.020451553271865` and the distinct-literal case has margin `1.2609256`.

The checker prints `PASS=True`. A counterexample to Theorem 5.1 would have had to violate either the exact restriction identities, Lemma 3.1, or the peer-certified five-bit entropy envelope; the finite debit search leaves no uncovered `delta` value.

## 8. What changed, what did not, and next attack

**Prior missing implication:** after the bent-swap counterexample, find a child/descendant-slack payment that survives a case where the pointwise local requested correction is huge.

**New proved inference:** exact two-generation ledger (2.5) plus a quantitative child-slack gap proves the whole balanced six-bit slice having at least one zero singleton coefficient. This explicitly demonstrates the compensation mechanism that the previous run said was necessary.

**Applied peer artifacts:** account04/B17 exact restriction cocycle (blob `d32321447c5f30282f243d9a2907ec719d483c92`) and account01/B17 exact balanced arity-five certificate (blob `076b4f50407e7af639566671c0367728decc0d28`).

**Remaining implication:** `LIMIT-PRIME-GATE-LIFT-v1` is still open. This theorem is a six-input balanced-uniform structural slice, not a universal proof and not a biased-input theorem.

**Next attack:** stay on the same all-gate target and exploit Corollary 6.1. A dangerous balanced six-bit gate must have all six singleton correlations nonzero, hence after input negations all are at least `+1/16`. The next concrete step is to combine this integer first-level floor with the edge-boundary/influence budget and the exact restriction ledger to bound the remaining all-nonzero-singleton chamber, rather than returning to a pointwise local scalar cap. If that chamber is closed, the balanced-uniform arity-six case is finished.

**Next recipients:** primary `account03/B18` (all-gate integrator), secondary `account01/B17` (finite balanced-gate adversary) and `account02/B17` (prime-gate reduction).

**Implication to full FEI:** `OPEN -> OPEN`; one quantitatively nontrivial balanced arity-six region is proved safe and the remaining six-bit threat is localized by a genuine first-order correlation constraint.

No novelty or publication-priority claim is made. This report contains only FEI mathematics, source-bound repository provenance, and sanitized logical run metadata; no credentials, scheduler identifiers, machine paths, unrelated private material, email/Drive content, paid model/API/Codex use, workflow dispatch, permission change, or public-posting action appears here.
