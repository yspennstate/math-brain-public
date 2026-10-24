# B15 — the packet/product bridge collapses to `H-R`, and rare tribes kill its one-coordinate selector

**Date:** 21 September 2026  
**Status:** **OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval/context or isolated evaluator was used in this mathematics.  
**Route:** unequal Fourier magnitudes / arithmetic remainder, integrating the newest packet-product bridge with the rare-tribes reserve obstruction.  
**Novelty:** no publication-priority claim is made.

## 1. Entering state

For a Boolean function, group equal nonzero Fourier magnitudes into packets `A_a`. Retain the inherited quantities

\[
p_a=|A_a|a^2,\qquad r_a=\min_{V_a(x)\ne0}\nu_2(V_a(x)),\qquad b_a=a2^{r_a},
\]
\[
R=\sum_ap_ar_a,\qquad D=\sum_ap_a\log_2(1/b_a),
\]
with the exact spectral-lattice identity

\[
H=2R+2D,
\tag{1}
\]

and the centroid payment

\[
R\le2I.
\tag{2}
\]

The immediately preceding account04/B15 continuation proved a transitive rare-tribes family `T_{m,w}` for which `D` alone has no finite universal existential-coordinate restriction payment. The fresh account02/B15 packet/product-measure bridge introduced a product Bernoulli law `nu` with the spectral marginals, packet shadow masses `beta_a=nu(A_a)`, arithmetic weights

\[
N_a=p_a/b_a^2,
\]

partition function and geometric bridge law

\[
Z=\sum_a\sqrt{N_a\beta_a},\qquad m_a=\frac{\sqrt{N_a\beta_a}}Z,
\]

and within-packet credit

\[
C_{\rm in}=\sum_ap_aD_{KL,2}(\operatorname{Unif}(A_a)\|\nu(\cdot\mid A_a)).
\]

That bridge gives the exact identity

\[
H=R+\frac12\sum_i h_2(j_i)+\log_2Z-D_{KL,2}(p\|m)-\frac12C_{\rm in},
\tag{3}
\]

where `j_i=Inf_i(f)`.

The question is whether the combined variational term in (3) is a genuinely easier unpaid object than the original entropy/remainder.

## 2. Exact collapse of the bridge

Define the packet-label product-shadow KL

\[
K_\beta:=\sum_ap_a\log_2\frac{p_a}{\beta_a}.
\]

The account02 bridge derivation itself gives

\[
K_N+K_\beta=2D_{KL,2}(p\|m)-2\log_2 B,
\qquad B=\frac Z{\sqrt N},
\tag{4}
\]

while the arithmetic free-energy identity is

\[
2D=\log_2N-K_N.
\tag{5}
\]

Substituting (4) into (5) gives the exact simplification

\[
\boxed{\log_2Z-D_{KL,2}(p\|m)=D-\frac12K_\beta.}
\tag{6}
\]

The KL chain rule for the packet map gives

\[
K_\beta+C_{\rm in}=D_{KL,2}(\mu\|\nu)
=\sum_i h_2(j_i)-H,
\tag{7}
\]

where `mu(S)=fhat(S)^2` is the spectral sample. Therefore the entire unpaid right-hand side of (3), after the first copy of `R`, is

\[
\begin{aligned}
\mathcal B(f)
&:=\frac12\sum_i h_2(j_i)+\log_2Z-D_{KL,2}(p\|m)-\frac12C_{\rm in}\\
&=\frac12\sum_i h_2(j_i)+D-\frac12(K_\beta+C_{\rm in})\\
&=D+\frac H2\\
&=\boxed{H-R=R+2D}.
\end{aligned}
\tag{8}
\]

So the new packet/product bridge is an exact and potentially useful reparameterization, but its **combined residual quantity is exactly `H-R`**. In particular, a global estimate

\[
\mathcal B(f)\le K I(f)
\tag{9}
\]

would imply FEI with coefficient `K+2` by (2), while FEI with coefficient `C` trivially gives `\mathcal B\le CI` because `R\ge0`. If

\[
C_{\mathcal B}:=\sup_f\frac{H(f)-R(f)}{I(f)},\qquad C_{FEI}:=\sup_f\frac{H(f)}{I(f)},
\]

then

\[
\boxed{C_{FEI}-2\le C_{\mathcal B}\le C_{FEI}.}
\tag{10}
\]

Thus controlling the whole bridge remainder globally is FEI-strength up to the already-known additive two coming from the centroid payment. Any genuine gain from the bridge has to exploit its **internal positive/negative structure before recombining it**, not merely rename the complete expression in (3).

## 3. Stronger obstruction: no finite one-coordinate selector for the bridge remainder

The previous rare-tribes family now gives a sharper consequence directly for the new bridge object.

For a coordinate `i`, write the usual restriction decrement

\[
\Delta_iX=X(f)-\frac{X(f^{i=+})+X(f^{i=-})}{2}.
\]

From (8),

\[
\Delta_i\mathcal B=\Delta_iH-\Delta_iR.
\tag{11}
\]

The exact Fourier restriction-entropy identity gives

\[
\Delta_iH\ge0.
\tag{12}
\]

Now use the transitive rare-tribes family `T_{m,w}` from the preceding account04/B15 continuation. Put

\[
\varepsilon=2^{-w},\qquad q=1-\varepsilon,
\]

and take `m` odd. The exact parent reserve, average child reserve and coordinate influence are

\[
R(T_{m,w})
=4\sum_{k=1}^m\binom mk\varepsilon^kq^{2m-k}\nu_2\binom mk,
\tag{13}
\]

\[
\overline R_{child}
=4\sum_{k=1}^{m-1}\binom{m-1}{k}\varepsilon^kq^{2m-1-k}\nu_2\binom{m-1}{k},
\tag{14}
\]

\[
\operatorname{Inf}_i(T_{m,w})=2\varepsilon q^{m-1}.
\tag{15}
\]

If `s=nu_2(m-1)`, then

\[
\frac{-\Delta_iR}{\operatorname{Inf}_i}
\longrightarrow2(m-1)s
\qquad(w\to\infty).
\tag{16}
\]

Equations (11)-(12) therefore give

\[
\frac{\Delta_i\mathcal B}{\operatorname{Inf}_i}
\ge\frac{-\Delta_iR}{\operatorname{Inf}_i}.
\tag{17}
\]

Choose

\[
m=2^a+1.
\]

Then `s=a`, and by transitivity (17) holds for **every** coordinate, with

\[
\boxed{
\liminf_{w\to\infty}
\frac{\Delta_i\mathcal B(T_{2^a+1,w})}
{\operatorname{Inf}_i(T_{2^a+1,w})}
\ge2^{a+1}a.
}
\tag{18}
\]

The right-hand side is unbounded.

### Theorem — bridge-selector obstruction

There is **no finite universal constant `C`** such that every nonconstant Boolean function has a coordinate `i` satisfying

\[
\Delta_i\mathcal B\le C\operatorname{Inf}_i(f),
\tag{19}
\]

where `mathcal B` is the full combined packet/product bridge term in (3).

This is stronger than the earlier `D`-only obstruction in the precise sense relevant to the fresh bridge: even after keeping its product-shadow KL and within-packet KL credits **inside the exact combined term**, a potential-free one-coordinate induction on that entire term is impossible.

This is **not** a counterexample to FEI. The same rare-tribes functions are read-once and satisfy known FEI bounds. The obstruction is to a proof architecture: a local restriction proof must retain an additional state/potential capable of carrying the valuation-reserve transfer, or exploit the bridge's credits in a nonlocal way before they recombine to `H-R`.

## 4. Exact finite witnesses

The companion checker uses exact `Fraction` arithmetic for (13)-(15). It proves the following strict lower bounds for `-Delta_iR/Inf_i`, hence also for `Delta_i mathcal B/Inf_i` by (17):

| `a` | `m` | `w` | variables | certified `>` | limit |
|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 12 | 36 | 3 | 4 |
| 2 | 5 | 12 | 60 | 15 | 16 |
| 3 | 9 | 12 | 108 | 47 | 48 |
| 4 | 17 | 16 | 272 | 127 | 128 |
| 6 | 65 | 18 | 1170 | 767 | 768 |
| 8 | 257 | 20 | 5140 | 4094 | 4096 |
| 10 | 1025 | 24 | 24600 | 20000 | 20480 |

The last descriptive ratio is `20478.748940810954...`; the inequality check itself is exact rational arithmetic. The checker passed.

Checker SHA-256: `8f9c5816fc69a0c8ddd259525a25e2af54cf45ab0dbb64e0a1b04eeec53f5923`  
Verification-output SHA-256: `43cc838d49fffb7780bc2a1fe467536ad986f0d26def9f15e486ba727d25340e`

## 5. Relation to the newest carry handoff

The concurrent account01/B15 restriction/carry continuation proves that an isolated packet of carry depth `r_a` is primitive-layer carry-vulnerable in at most `r_a` physical directions and hence

\[
\sum_ap_a|\operatorname{Vul}(a)|\le R\le2I.
\tag{20}
\]

It also proves a sharp magnitude-gap sandwich for `Delta_iH`. That result and (18) are compatible: the rare-tribes obstruction is not saying isolated carry can be fragile in too many directions. Instead it exhibits a **repacketization/valuation-reserve transfer** under restriction that a scalar one-coordinate bridge decrement cannot pay. This points away from raw packet vulnerability counts and toward a stateful stopping-tree ledger that transports `R` across nodes rather than paying it immediately.

## 6. Current primary-literature check

A fresh bounded primary-source search on 21 September 2026 found no unrestricted FEI proof.

- Vladimir N. Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions*, arXiv:2609.21563, posted 18 September 2026, proves FEI for Boolean plateaued functions (sharp class constant 4) and partially bent functions (sharp class constant 2). It is a structured-class result, not unrestricted FEI.
- María José González, Paul MacManus, María Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246, 29 May 2026, develops the restriction/stopping-tree program and states that the key restriction inequality would imply full FEI; it does not prove that universal inequality.
- Peijie Li and Guangyue Han, *Strengthening Han's Fourier Entropy-Influence Inequality via an Information-Theoretic Proof*, arXiv:2512.03117, 2 December 2025, proves a general entropy/influence-profile inequality retaining an additional marginal-influence entropy term; it does not provide the missing dimension-free FEI bound here.

No publication-priority claim is made for the elementary collapse (6)-(8) or for combining it with the project-specific rare-tribes obstruction.

## 7. What is killed and what remains

**PROVED / killed here:**

1. The full combined packet/product variational term in the newest bridge equals exactly `H-R`; it is not a smaller new global residual.
2. No finite universal existential-coordinate coefficient can pay the restriction decrement of that full bridge term.
3. Therefore the natural potential-free restriction induction based on the newest bridge term is dead, even with its two KL credits retained in aggregate.

**Still open:**

- unrestricted uniform-cube FEI;
- a stateful stopping-tree potential that stores valuation reserve instead of paying it locally;
- a proof that uses `K_beta`, `C_in`, or the geometric bridge law separately and nonlocally before their exact recombination;
- a direct global influence estimate exploiting additional Boolean constraints on those pieces.

## 8. Next precise target

The next spectral-remainder attack should not try to bound `D`, `H-R`, `log Z`, or the bridge decrement coordinatewise. The surviving possibility is a **two-ledger stopping potential** in which negative `Delta R` is carried forward rather than charged immediately. Concretely, seek a nonnegative or lower-bounded state `P(f)` built from packet-label/product-shadow mismatch such that

\[
\Delta_i(H-R+P)\le C\operatorname{Inf}_i(f)
\]

for some selectable coordinate while the accumulated terminal value of `P` is influence-paid. Any candidate must pass the transitive rare-tribes family above and the one-point-defect family that forces the bridge-law KL cancellation.
