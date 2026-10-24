# account01/B12 — geometric pair-trigger macro stopping for robust derivative rows

**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** `FEI-20260922-account01-B12` — pair-selected physical stopping  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated GitHub source/context was consumed, but no separately verified native brain receiver was used.  
**Model self-report:** `GPT-5.6 Sol`; configured reasoning telemetry is not exposed.

## 0. Current target and source corrections

Full uniform-cube FEI remains open. This report does not use the refuted fixed read-once potential, the refuted `0.337/0.34` quadratic repairs, raw `U_4=O(J)` from terminality/primitivity, or an unweighted convolution-L2 payment.

The current Path-C state is the candidate-independent stopping reduction. Write

\[
\mathfrak j(q)=1-h_2\!\left(\frac12+\sqrt{q(1-q)}\right),\qquad
\mathcal P=\sum_i\mathfrak j(q_i),\qquad
\mathcal F=H-\mathcal P,\qquad
\mathcal J=\sum_iq_i,
\]

with folded influences `q_i<=1/2`. For a physical block `A`, the source theorem gives

\[
\Delta_A\mathcal F\le U_A,\qquad
U_A=\sum_{k\in A}h_2(q_k)-W_A\le |A|,
\tag{0.1}
\]

and

\[
D_A:=\mathcal J-\mathbb E\mathcal J(f_{A=z})
=\sum_{k\in A}q_k+C_A\ge0.
\tag{0.2}
\]

These quantities telescope on any genuine physical restriction tree.

The robust-row input is the source theorem of account04/B12. For derivative row `i`, let

\[
E_i=\{y:D_if(y)\ne0\},\qquad \mu(E_i)=q_i,
\]

and suppose a physical coordinate subcube

\[
Q_i=\{y_{F_i}=a_i\},\qquad |F_i|=m,
\]

satisfies

\[
\varepsilon_i:=\mu(E_i\triangle Q_i)\le\eta q_i,\qquad 0\le\eta<1/2.
\tag{0.3}
\]

The same source proves, for each trigger `k in F_i`,

\[
p_{ik}\ge2(q_i-2\varepsilon_i).
\tag{0.4}
\]

Applying the exact co-pair identity of account02/B13,

\[
r_{ik}=\frac{p_{ik}}4+o_{ik},\qquad o_{ik}\ge0,
\tag{0.5}
\]

shows that every selected trigger is backed by genuine pair spectral mass:

\[
\boxed{r_{ik}\ge\frac{q_i-2\varepsilon_i}{2}.}
\tag{0.6}
\]

Thus the construction below selects only original physical coordinates certified by the current Boolean source; it never selects a latent spectral label.

## 1. Named partner result consumed and what it changes

The required compatible partner result is account02/B12,

`yspennstate/math-open-problems@4ccd51ad517f425a529daa52c3352905b86ea69d`,
`proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`, Sections 2--4.

Its candidate-independent selector theorem states, for a genuine physical coordinate with selector bias `s` and disagreement probability `d`,

\[
Q_s(d):=\Delta_i\widetilde H-dh_2(V_s)
\le h_2(d)+\frac2{\ln2}\min\{d,1-d\}.
\tag{1.1}
\]

At the uniform cube `s=1/2`, the right side has `h_2(d)/d -> infinity` as `d->0`. Therefore a proof that asks every early rare trigger split to be **locally** affordable by a fixed linear-in-disagreement budget cannot work. I use (1.1) to change the stopping mechanism: the trigger splits below are not certified one node at a time. They are executed as one finite physical macro-tree, and only the **aggregate** `F/J` ledger is compared. The obsolete Section-5 `0.337` candidate is not used.

## 2. Canonical source-measurable pair-trigger macro

At a current centered Boolean node, choose a row `i` satisfying (0.3). To make the rule source-measurable, take the lexicographically first physical coordinate subcube among the minimum-cardinality subcubes satisfying (0.3); no Fourier sample or hidden label is queried.

Order its trigger set `F_i={k_1,...,k_m}` canonically. Partition the ordered triggers into blocks

\[
B_1,B_2,\ldots,B_\ell,
\]

each of size two, except that when `m` is odd the last block has size one.

Execute the following finite macro:

1. query `B_1` physically;
2. on every child whose queried values disagree with the target pattern `a_i`, end this macro immediately;
3. only on the unique matching child query `B_2`;
4. continue in the same way until the last block is queried, then end the macro on all children.

Every original trigger coordinate is queried at most once. If `s_{r-1}=|B_1|+...+|B_{r-1}|`, the reach probability of stage `r` is exactly

\[
\lambda_r=2^{-s_{r-1}}.
\tag{2.1}
\]

This depends only on the actual uniform physical bits.

## 3. Geometric address-cost lemma

At a queried node, (0.1) gives

\[
\Delta_{B_r}\mathcal F\le U_{B_r}\le |B_r|.
\]

Therefore the whole macro satisfies

\[
\mathcal F(f)-\mathbb E\mathcal F(f_L)
\le\sum_{r=1}^\ell\lambda_r|B_r|.
\tag{3.1}
\]

If `m=2L`,

\[
\sum_r\lambda_r|B_r|
=2\sum_{r=0}^{L-1}4^{-r}
=\frac83(1-4^{-L})<\frac83.
\tag{3.2}
\]

If `m=2L+1`,

\[
\sum_r\lambda_r|B_r|
=2\sum_{r=0}^{L-1}4^{-r}+4^{-L}
=\frac83-\frac53\,4^{-L}<\frac83.
\tag{3.3}
\]

Hence, for every trigger depth,

\[
\boxed{\mathcal F(f)-\mathbb E\mathcal F(f_L)<\frac83.}
\tag{3.4}
\]

The trigger depth has disappeared. This is the nonlocal replacement for charging every trigger label separately.

## 4. Robust-row folded-influence drop

The macro never queries coordinate `i`. Let `q_i(L)` denote the folded influence of row `i` at a terminal macro leaf. Since folded influence is invariant under the allowed character recentering,

\[
\mathcal J(f)-\mathbb E\mathcal J(f_L)
\ge q_i-\mathbb E q_i(L).
\tag{4.1}
\]

Partition the terminal leaves into the first-mismatch leaves and the all-match leaf `Q_i`.

On a mismatch leaf `L subset Q_i^c`, its reach probability times its folded row influence is at most the actual `E_i` mass in that leaf. Summing all mismatch leaves gives at most

\[
\mu(E_i\setminus Q_i).
\tag{4.2}
\]

On the all-match leaf, whose physical mass is `s_i=\mu(Q_i)`, the weighted folded row influence is

\[
s_i\min\{\mu(E_i\mid Q_i),1-\mu(E_i\mid Q_i)\}
=\min\{\mu(E_i\cap Q_i),\mu(Q_i\setminus E_i)\}
\le\mu(Q_i\setminus E_i).
\tag{4.3}
\]

Therefore

\[
\mathbb E q_i(L)
\le\mu(E_i\setminus Q_i)+\mu(Q_i\setminus E_i)
=\varepsilon_i.
\tag{4.4}
\]

Substitution into (4.1) yields the exact robust-row package refund

\[
\boxed{
\mathcal J(f)-\mathbb E\mathcal J(f_L)
\ge q_i-\varepsilon_i
\ge(1-\eta)q_i.
}
\tag{4.5}
\]

No trigger surplus is reused; the payment is the actual folded influence lost on this one physical mini-tree.

## 5. Main theorem: pair-trigger package affordability

### Theorem 5.1

Fix `K>0` and `0<=eta<1/2`. If a current centered Boolean node contains a derivative row satisfying (0.3) with

\[
\boxed{
q_i>\frac{8}{3K(1-\eta)},
}
\tag{5.1}
\]

then the pair-trigger macro above is strictly `K`-affordable:

\[
\boxed{
\mathcal F(f)-\mathbb E\mathcal F(f_L)
< K\bigl(\mathcal J(f)-\mathbb E\mathcal J(f_L)\bigr).
}
\tag{5.2}
\]

**Proof.** Combine (3.4), (4.5), and (5.1):

\[
\Delta\mathcal F<\frac83
<K(1-\eta)q_i
\le K\Delta\mathcal J.
\]

QED.

At the live robust threshold `eta=1/16`, condition (5.1) is

\[
\boxed{q_i>\frac{128}{45K}.}
\tag{5.3}
\]

For example, `K=128` excludes every relative-`1/16` robust row with `q_i>1/45`.

### Corollary 5.2 — finite global compiler and new terminal exclusion

Repeatedly execute Theorem 5.1 whenever such a row exists at the current physical node, recenter at macro leaves, and continue there. Every macro queries at least one previously surviving original coordinate on every branch, so the recursion terminates in finite dimension. Summing (5.2) over macro nodes gives

\[
\boxed{
\mathcal F(f)-\mathbb E\mathcal F(f_T)
<K\bigl(\mathcal J(f)-\mathbb E\mathcal J(f_T)\bigr)
\le K\mathcal J(f).
}
\tag{5.4}
\]

Every terminal leaf satisfies the genuinely stronger source-measurable exclusion

\[
\boxed{
\text{no relative-}\eta\text{ near-subcube derivative row has }
q_i>\frac{8}{3K(1-\eta)}.
}
\tag{5.5}
\]

This eliminates the medium/heavy robust-row branch without invoking a bounded trigger-incidence assumption and without trying to bound the raw depth bank.

## 6. Singleton refinement

If singleton blocks are allowed throughout the same continuation rule, the geometric address constant improves to

\[
\sum_{r=0}^{m-1}2^{-r}<2,
\]

so (5.1) improves to

\[
q_i>\frac{2}{K(1-\eta)}.
\tag{6.1}
\]

I keep the pair-block theorem as the primary assignment result; the singleton version shows that the gain comes from the physical continuation geometry, not from an accidental property of block size two.

## 7. Relation to the exact co-pair theorem

The co-pair theorem is used at its valid scope, not as a raw-curvature payment. Equations (0.4)--(0.6) certify that every chosen trigger coordinate carries actual pair Fourier mass with the row coordinate. But the no-go family in the same account02/B13 report shows that summing raw orientation curvature over all pairs is not influence-relative, even for primitive all-block-terminal functions. The present proof avoids exactly that failure: it picks one physical robust row, uses a nonreusing trigger chain, and charges only the actual source reach probabilities.

Thus no statement of the form `U_4=O(J)` is assumed or recovered.

## 8. Old versus new missing implication

**Old missing implication.** The robust-row theorem gave an influence-relative trigger-surplus demand but the same trigger surplus could be requested by many rows; the aggregate weighted-depth bank was not known to be `O(J)`.

**New result.** For every relative-`eta` robust row above the explicit threshold (5.1), no aggregate reuse theorem is needed: a finite source-measurable pair-trigger macro has geometric `F` cost `<8/3` and actual folded-influence refund at least `(1-eta)q_i`, so the row is physically stoppable with no repeated credit.

**New missing implication.** After this exclusion, Path C still must handle (i) robust rows below `8/[3K(1-eta)]`, and (ii) nonrobust rows, while preserving a dimension-independent entropy ledger. Closing those branches, or another universal route, is still required for FEI.

## 9. Status

`ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.

This is an analytic arbitrary-dimension theorem at its stated robust-row hypotheses. No finite test is promoted to a universal proof, and no fixed-potential claim is used.

## Source pins

1. `yspennstate/math-open-problems@85ffa60db26997421d980b1f86c03d82259504ca`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md` — physical block `F/J` inequality and stopping ledger.
2. `yspennstate/math-open-problems@fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113`, `proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md` — robust near-subcube rows and trigger boundary lower bound.
3. `yspennstate/math-open-problems@85ffa60db26997421d980b1f86c03d82259504ca`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T093723Z-copair-terminal-tax/REPORT.md` — exact co-pair identity and raw-curvature no-go.
4. `yspennstate/math-open-problems@4ccd51ad517f425a529daa52c3352905b86ea69d`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`, Sections 2--4 only — conditional Shannon debit forcing a nonlocal rather than pointwise-linear stopping mechanism. Its obsolete Section-5 candidate is not used.
