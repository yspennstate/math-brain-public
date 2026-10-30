# B12 FEI compression route — factorial potential telescope pays repeated sink frontiers without reuse

**Status:** PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains **OPEN / NOT PROVED**.  
**Route:** APPROACH 1, spectral-sample compression / sequential prediction, joined to the live adaptive-restriction interface.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. The shared GitHub coordination state was consumed, but no authenticated native mathematical-brain retrieval/context engine was used.  
**Novelty/publication priority:** UNVERIFIED; no novelty claim.  

## 1. Exact predecessor and the obstruction attacked

This run continues the fleet01/B12 companion-code package

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B12/20260921T201755Z-companion-factorial/`

and consumes, as the required named other-account mathematical input, fleet04/B18

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B18/20260921T201525Z-sink-component-peeling/REPORT.md`

(file blob `2575d3945985e76d1f61831a65366b29b5052d27` at the source snapshot read in this run).

The B18 result constructs, in the doubly robust Palm/physical near-subcube sector, a canonical sink frontier: one representative `r` from every sink reciprocal-trigger component and the common physical reveal block

\[
R=\{r_C\},\qquad A=\bigcup_{r\in R}F_r,
\]

with

\[
R\cap A=\varnothing,\qquad F_r\subseteq A\quad(r\in R).
\tag{1.1}
\]

The preceding B12 companion theorem gives, for every `epsilon<=1/16` Palm-robust representative with nonempty trigger set,

\[
\sum_{k\in F_r} r_{rk}\ge \frac{3}{16}p_r,
\qquad
r_{ij}:=\mathbb E\frac{1_{\{i,j\in S\}}}{|S|},
\tag{1.2}
\]

where `S` is the spectral sample and `p_r=Pr(r in S)`.

The unresolved bookkeeping issue in the previous addendum was **successive sink peeling**. A single root-level lower bound on `D_seq` or `E log_2(|S|!)` cannot simply be added once per peeling layer: that would reuse the same global rebate. The new result below replaces that static use by an exact physical-restriction telescope.

## 2. The factorial spectral potential

For any Boolean function `f`, let

\[
\mu_f(S)=\widehat f(S)^2,
\qquad K=|S|,
\]

and define

\[
\boxed{
\mathcal Q(f):=\mathbb E_{S\sim\mu_f}\log_2(K!).
}
\tag{2.1}
\]

Use `0!=1`, so the empty spectral atom contributes zero. This is exactly the factorial rebate already appearing with a minus sign in the Palm insertion code:

\[
H(S)\le H(K)+I H(\pi)-\mathcal Q(f)-D_{\rm seq}.
\tag{2.2}
\]

The point is that `Q` is not merely a static rebate. It has an exact restriction-drop formula.

### Theorem 2.1 — exact factorial block-drop identity

Let `A` be any physical coordinate block, restrict `f` uniformly on `A`, and write `f_{A=z}` for the child. For a root spectral sample put

\[
M=|S\cap A|,
\qquad K=|S|.
\]

Then

\[
\boxed{
\Delta_A\mathcal Q(f)
:=\mathcal Q(f)-\mathbb E_z\mathcal Q(f_{A=z})
=\mathbb E\log_2\frac{K!}{(K-M)!}.
}
\tag{2.3}
\]

In particular `Delta_A Q>=0`.

#### Proof

For every `T subseteq A^c`, the restricted Fourier coefficient is

\[
\widehat{f_{A=z}}(T)
=\sum_{U\subseteq A}\widehat f(T\cup U)\chi_U(z).
\]

Averaging its square over `z` and using character orthogonality on `A` gives

\[
\mathbb E_z\widehat{f_{A=z}}(T)^2
=\sum_{U\subseteq A}\widehat f(T\cup U)^2.
\tag{2.4}
\]

Therefore

\[
\begin{aligned}
\mathbb E_z\mathcal Q(f_{A=z})
&=\sum_{T\subseteq A^c}
\left(\sum_{U\subseteq A}\widehat f(T\cup U)^2\right)
\log_2(|T|!)\\
&=\sum_S\mu_f(S)\log_2(|S\setminus A|!)\\
&=\mathbb E\log_2((K-M)!).
\end{aligned}
\]

Subtracting from (2.1) proves (2.3). QED.

### Corollary 2.2 — adaptive telescope

For any finite adaptive physical block-restriction tree, with node probability `w_u`, node function `f_u`, and queried block `A_u`,

\[
\boxed{
\sum_{u\ \mathrm{internal}}w_u\Delta_{A_u}\mathcal Q(f_u)
=\mathcal Q(f_{\rm root})-
\sum_{\ell\ \mathrm{leaf}}w_\ell\mathcal Q(f_\ell)
\le\mathcal Q(f_{\rm root}).
}
\tag{2.5}
\]

Thus the factorial rebate can be allocated **once along an arbitrary adaptive physical tree**, with no assumption that reveal blocks from different levels are disjoint.

## 3. A sharp pointwise bridge from companion flow to factorial drop

The companion flow from the preceding B12 report is

\[
r_{ij}=\mathbb E\frac{1_{\{i,j\in S\}}}{K}.
\]

Let `R` and `A` be any disjoint coordinate sets, and for each `r in R` let `F_r subseteq A`. Define the flow routed from the representatives into their physical witness blocks by

\[
W(R,A):=\sum_{r\in R}\sum_{k\in F_r}r_{rk}.
\tag{3.1}
\]

### Theorem 3.1 — block factorial drop dominates twice the routed companion flow

\[
\boxed{
\Delta_A\mathcal Q(f)\ge 2W(R,A).
}
\tag{3.2}
\]

The factor `2` is sharp for the underlying pointwise inequality.

#### Proof

For one spectral set `S`, put

\[
M=|S\cap A|,
\qquad N=|S\setminus A|,
\qquad K=N+M.
\]

Since `R cap A` is empty,

\[
|S\cap R|\le N.
\]

Also every `F_r` lies inside `A`, hence

\[
\sum_{r\in R\cap S}|F_r\cap S|
\le |S\cap R|\,|S\cap A|
\le NM.
\]

Therefore

\[
W(R,A)
\le \mathbb E\frac{NM}{N+M}.
\tag{3.3}
\]

It remains to compare this pointwise with (2.3). If `N=0` or `M=0`, the right side of (3.3) is zero. For `N,M>=1`,

\[
\log_2\frac{(N+M)!}{N!}
=\sum_{j=1}^M\log_2(N+j)
\ge M\log_2(N+1).
\tag{3.4}
\]

For every integer `N>=1`,

\[
\log_2(N+1)\ge\frac{2N}{N+1}.
\tag{3.5}
\]

Indeed, with `x=N+1>=2`, the function

\[
h(x)=\ln x-2\ln2\left(1-\frac1x\right)
\]

has `h(2)=0` and

\[
h'(x)=\frac{x-2\ln2}{x^2}>0\qquad(x>=2).
\]

Since `N+M>=N+1`, (3.4)-(3.5) imply

\[
\log_2\frac{(N+M)!}{N!}
\ge \frac{2NM}{N+1}
\ge \frac{2NM}{N+M}.
\tag{3.6}
\]

Averaging (3.6), using (3.3), and applying the exact identity (2.3) proves (3.2). Equality in the scalar step occurs at `N=M=1`, so the factor `2` cannot be improved uniformly by this argument. QED.

## 4. Application to the B18 canonical robust sink frontier

For the B18 sink frontier, (1.1) gives exactly the hypotheses needed in Theorem 3.1. The inherited Palm-robustness estimate (1.2) gives

\[
W(R,A)
=\sum_{r\in R}\sum_{k\in F_r}r_{rk}
\ge \frac3{16}\sum_{r\in R}p_r.
\]

Writing

\[
J_R:=\sum_{r\in R}p_r,
\]

we therefore obtain the new local payment

\[
\boxed{
\Delta_A\mathcal Q(f)\ge\frac38 J_R.
}
\tag{4.1}
\]

More generally, at Palm error `epsilon<1/4`, the preceding B12 row estimate gives

\[
\boxed{
\Delta_A\mathcal Q(f)
\ge 2(1/4-\epsilon)J_R.
}
\tag{4.2}
\]

This is stronger than the old static `I-V` payment for this purpose and, crucially, is a **node-local physical potential drop**.

## 5. The repeated-frontier nonreuse obstruction is removed

Consider any adaptive restriction tree in which, at each applicable node `u`, the current function has a B18-compatible robust sink frontier `(R_u,A_u)` with `epsilon<=1/16`. Put

\[
J_u=\sum_{r\in R_u}p_{u,r}.
\]

Combining (4.1) with the exact telescope (2.5) gives

\[
\boxed{
\frac38\sum_u w_u J_u
\le
\sum_u w_u\Delta_{A_u}\mathcal Q(f_u)
\le
\mathcal Q(f_{\rm root}).
}
\tag{5.1}
\]

Equivalently,

\[
\boxed{
\sum_u w_uJ_u
\le\frac83\,\mathcal Q(f_{\rm root}).
}
\tag{5.2}
\]

No same-bank reuse occurs: every repeated robust sink layer is charged to the actual decrease of one root spectral potential. The reveal blocks need not be globally disjoint, and the robust components may be recomputed after each restriction.

This directly resolves the precise limitation stated in the preceding `SINK_FRONTIER_ADDENDUM.md`, which said that one could not simply repeat a static lower bound on `D_seq + E log_2(K!)` over every peeling layer. The correct object to repeat is **not the static lower bound** but the physical drop of the factorial potential itself.

## 6. What this does and does not prove

The result supplies a genuine chained resource ledger for the robust sink-peeling sector:

- the same `Q(f)=E log_2(K!)` that appears as a negative term in the exact Palm sequential code is also a monotone physical-restriction potential;
- a B18 common sink reveal block spends at least `3/8` of the total representative influence from that layer out of `Q`;
- successive adaptive layers telescope automatically, so the factorial resource is never counted twice.

This **does not close FEI**. In particular, `Q(f)` is not itself universally `O(I(f))` (parity already has `Q=log_2(n!)` while `I=n`). Its role is as an existing negative rebate in the Palm code, not a new positive cost to be bounded by influence. The remaining universal implication is to show that the entropy/address cost left after the existing companion and factorial rebates can be charged to:

1. the actual nodewise `Q` drops above in the robust sink sector,
2. the already-paid curvature/crossing restriction refunds, and
3. an `O(I)` resource on the complementary nonrobust/scale-escape sector.

The sharp next target for B12 is therefore a **code identity aligned with the physical tree**: rewrite the residual `I H(pi)` / block-address cost so that every robust sink-layer contribution is paired with its local `Delta_A Q`, rather than with the root `Q` a second time. The nonrobust branch must still be handled separately; no claim is made that B18's current sector covers all coordinates.

## 7. Method-change note and validation scope

This is a substantive method change from the previous one-frontier KL/factorial dichotomy. It does not sum more KL lower bounds and does not rerun the settled read-once certificate. The new ingredient is the exact restriction dynamics of the factorial code rebate.

The proof is algebraic. A scoped manual privacy/secret review of this new report found no credentials, scheduler identifiers, machine paths, signed URLs, unrelated private material, or held-out benchmark data. No external computation is needed for the theorem; the scalar constant `2` is proved analytically and is sharp at `N=M=1`.

**Full FEI status: OPEN / NOT PROVED.**
