# B12 FEI — harmonic companion normal form for robust near-subcube rows

**Run:** `B12-20260921T220950Z-r39`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status of full uniform-cube FEI:** **OPEN / NOT PROVED**  
**Claim level:** analytic partial theorem for interface B, with exact/finite diagnostics. No novelty or publication-priority claim.

## 0. What changed in this run

The preceding B12 work had two useful but incomplete robust-row payments:

1. reciprocal Palm-robust rows contract to exact trigger components and nonreciprocal trigger edges jump by a factor at least seven in folded influence; and
2. the factorial rebate `Q=E log2(K!)` pays robust trigger-address logarithms, but at the fixed `1/16` TV scale the proved coefficient was `16/3`, while a coefficient-one payment had only been available under the much finer condition `epsilon_i <= 1/(16m_i)`.

This run changes the coding method. Instead of trying to transfer Shannon entropy from a large ambient alphabet, it combines the **one-companion channel** with the Boolean Palm hypercontractive Laplace transform. There are three new all-dimensional statements:

* the entire no-companion / first-label entropy is universally `O(J)` with explicit constant `3.41613`, without any robustness assumption;
* for every physical near-subcube row whose subcube density matches its influence within relative `1/16`, the row's own factorial share pays `j_i log2(m_i+1)` with **coefficient one**, up to `(19/4)j_i`, with no `epsilon_i <= 1/(16m_i)` hypothesis;
* for a fixed-`1/16` Palm-robust physical near-subcube row, all **in-trigger companion identity entropy** is therefore paid by its own factorial share plus `5.66830 j_i`. The only robust-row ambient-address term left is an explicit off-trigger companion exception entropy carried by a flow of mass at most `j_i/16`.

No step below bounds that exception entropy merely from its small mass. That would reintroduce the exact rare-address error already identified by fleet02. Full FEI remains open.

## 1. Fresh compatible peer inputs actually used

### 1.1 Newest fleet02/B13 input: actual-anchor cross-plaquette code

Consumed the current fleet02/B13 report

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260921T215826Z-cross-plaquette-tensor-correction/REPORT.md`

introduced at commit `fac5798cba0a75b45b237d0dfd1b431191d40da8`, together with its late peer-alignment addendum at commit `3e6648816082dabde7646d49ccd7a6b1cfc25b77`.

For a physical cut `A|B`, fleet02/B13 constructs one genuine anchor child and signs for which the correction fractions `q_b` satisfy

\[
 E_b\,2q_b\log_2(1/q_b)\le \frac12 P_{A\to B},
 \qquad
 E_b h_2(q_b)\le \frac12 P_{A\to B}.
\]

On the source-frontier block this gives an actual inter-child conditional sign code bounded by

\[
 \sum_{i\in A_*} j_i\log_2\frac1{j_i}+2\mathcal D_{A_*}.
\]

**Exact implication used here:** this result identifies the physical correction as genuinely dimension-free **after an anchor is chosen**, but it also shows that a direct block-reveal route still leaves the raw base-selector term. Therefore the present run does not try another physical Fannes/TV conversion. It changes category to the spectral one-companion code, where a row label is charged only with the harmonic `1/K` weight supplied by the actual terminal spectral set. The fleet02 result remains the compatible physical anchor object for a future Fourier-transfer step; it is not falsely treated as already paying the spectral address.

### 1.2 fleet02/B12 Boolean Palm hypercontractivity

Consumed

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B12/20260921T155715Z-random-prefix-loss-hypercontractive/REPORT.md`, blob `49d29bae97d8aaa33fc0c0f4e7c499b4f4194090`.

For the folded derivative row with influence `j_i` and Palm remainder size `Z=|B|`, it proves for every `0<=t<=1`

\[
 \boxed{
 E_{\nu_i} t^Z
 \le j_i^{(1-t)/(1+t)}.
 }
 \tag{1.1}
\]

**Exact implication used here:** (1.1) controls the dangerous shallow-degree contamination which total variation alone cannot control. It is the ingredient that removes the previous fine condition `epsilon_i <= 1/(16m_i)` from the coefficient-one factorial address payment.

### 1.3 one-companion nonreuse code

Consumed fleet01/B12

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B12/20260921T201755Z-companion-factorial/REPORT.md`.

With `S` the spectral sample, `K=|S|`, `J=EK`, put

\[
 u_i=E\frac{1_{\{i\in S\}}}{K},
 \qquad
 r_{ij}=E\frac{1_{\{i,j\in S\}}}{K}\quad(i\ne j),
 \tag{1.2}
\]

where the integrands vanish at `K=0`. If `V=Pr(K>0)` and `pi_i=j_i/J`, the companion channel gives

\[
 D_{\rm seq}\ge D_{\rm comp}=J I_2(L;C)
 \tag{1.3}
\]

and the exact residual-selector identity

\[
 \boxed{
 JH(\pi)-D_{\rm comp}
 = V H(u/V)
 +\sum_j (j_j-u_j)
 H\!\left(\frac{(r_{ij})_{i\ne j}}{j_j-u_j}\right).
 }
 \tag{1.4}
\]

Also

\[
 u_j+\sum_{i\ne j}r_{ij}=j_j,
 \qquad
 \sum_{i\ne j}r_{ij}=J-V.
 \tag{1.5}
\]

This is the nonreusing carrier used below.

### 1.4 fleet04/B18 integrability constraints preserved

The current fleet04/B18 integration keeps the mixed-curvature identity

\[
 \kappa_{ik}=p_{ik}+4o_{ik},
 \qquad
 \sum_{i\ne k}\kappa_{ik}=4d_k,
 \tag{1.6}
\]

and explicitly forbids replacing it by `sum_k d_k=O(J)`. Nothing below uses such a replacement. The new payments are made from `J`, the exact companion flow, and the exact rowwise factorial allocations. The second-factorial depth bank is not charged at unit price.

## 2. Setup after the minimizing character gauge

Multiply by the minimizing character so that every active folded influence is an ordinary influence

\[
 0<j_i=\Pr(i\in S)\le\frac12,
 \qquad
 J=\sum_i j_i=E K.
 \tag{2.1}
\]

This gauge preserves Fourier entropy and the centered influence target.

For row `i`, let

\[
 \nu_i(B)=\Pr(S\setminus\{i\}=B\mid i\in S),
 \qquad Z=|B|.
 \tag{2.2}
\]

Define its exact factorial allocation

\[
 \boxed{
 Q_i:=E\left[
  \frac{1_{\{i\in S\}}}{K}\log_2(K!)
 \right].
 }
 \tag{2.3}
\]

Then

\[
 \boxed{\sum_i Q_i=Q:=E\log_2(K!).}
 \tag{2.4}
\]

The identity is pointwise: every nonempty terminal set of size `K` gives `K` shares of size `log2(K!)/K`.

## 3. PROVED: the whole no-companion label entropy is `O(J)`

### Theorem B12-HARMONIC-KILLING-01

For every active row,

\[
 \boxed{
 u_i\log_2\frac1{j_i}
 \le 2\log_2(e)\,j_i.
 }
 \tag{3.1}
\]

Consequently

\[
 \boxed{
 V H(u/V)
 \le C_0 J,
 \qquad
 C_0:=\left(2+\frac1e\right)\log_2 e
 =3.4161279272009697\ldots .
 }
 \tag{3.2}
\]

### Proof

Conditioning on `i in S`,

\[
 \frac{u_i}{j_i}
 =E_{\nu_i}\frac1{1+Z}
 =\int_0^1 E_{\nu_i} t^Z\,dt.
 \tag{3.3}
\]

Let `a=ln(1/j_i)`. Apply the fleet02/B12 hypercontractive bound (1.1):

\[
 \frac{u_i}{j_i}
 \le \int_0^1
  \exp\!\left[-a\frac{1-t}{1+t}\right]dt.
\]

With `s=(1-t)/(1+t)`,

\[
 \frac{u_i}{j_i}
 \le 2\int_0^1\frac{e^{-as}}{(1+s)^2}ds
 \le\frac2a.
 \tag{3.4}
\]

Multiplying by `log2(1/j_i)=a/ln2` proves (3.1).

For (3.2), since `V<=1`,

\[
\begin{aligned}
 V H(u/V)
 &=\sum_i u_i\log_2\frac V{u_i}\\
 &\le\sum_i u_i\log_2\frac1{u_i}\\
 &=\sum_i u_i\log_2\frac1{j_i}
   +\sum_i u_i\log_2\frac{j_i}{u_i}.
\end{aligned}
\]

The first sum is at most `2 log2(e) J` by (3.1). Put `x_i=u_i/j_i in [0,1]`. Since

\[
 x\log_2(1/x)\le\frac{\log_2 e}{e},
\]

the second sum is at most `(log2 e/e)J`. QED.

### Interpretation

The raw selector quantity `sum_i j_i log(1/j_i)` is not `O(J)`; the one-point family already forbids such a claim. The **harmonically sampled first label** is different. Its exact weights are `u_i`, and Boolean hypercontractivity forces (3.1). Thus the null companion symbol in the real insertion code carries no ambient-dimension entropy obstruction.

This is a category change from the direct physical reveal in the newest fleet02/B13 theorem. It pays the first spectral label where the exact insertion process actually uses it, rather than trying to pay every row's full codimension at once.

## 4. PROVED: coefficient-one factorial trigger address without fine TV

The preceding fleet01 coefficient-one theorem required `epsilon_i<=1/(16m_i)`. The next result removes that fine-Palm requirement by using the Boolean shallow-degree bound.

Assume a row has a physical coordinate-subcube proxy of codimension `m_i>=1` with density

\[
 s_i=2^{-m_i}
 \tag{4.1}
\]

satisfying the relative density match already present in the fleet04 near-subcube branch,

\[
 \boxed{|s_i-j_i|\le\frac1{16}j_i.}
 \tag{4.2}
\]

No Palm-TV hypothesis is needed in this section.

### Theorem B12-HYPERCONTRACTIVE-FACTORIAL-ADDRESS-02

Under (4.2),

\[
 \boxed{
 j_i\log_2(m_i+1)
 \le Q_i+\frac{19}{4}j_i.
 }
 \tag{4.3}
\]

Thus for any collection `R` of such physical near-subcube rows,

\[
 \boxed{
 \sum_{i\in R}j_i\log_2(m_i+1)
 \le \sum_{i\in R}Q_i+\frac{19}{4}J_R
 \le Q+\frac{19}{4}J_R,
 }
 \tag{4.4}
\]

where `J_R=sum_{i in R}j_i`.

The coefficient of the exact factorial rebate is **one**.

### Proof

Write

\[
 L=\log_2(1/j_i)\ge1,
 \qquad K=1+Z.
\]

By (4.2),

\[
 m_i\le L+\alpha,
 \qquad
 \alpha:=\log_2(16/15)<0.1.
 \tag{4.5}
\]

Also

\[
 \frac{Q_i}{j_i}
 =E_{\nu_i}g(K),
 \qquad
 g(k)=\frac{\log_2(k!)}k.
 \tag{4.6}
\]

If `1<=L<24`, then (4.5) and integrality give `m_i<=24`, hence

\[
 \log_2(m_i+1)\le\log_2 25<19/4,
\]

and (4.3) follows from `Q_i>=0`.

Now suppose `L>=24`. Set `t=1/2` in (1.1):

\[
 E_{\nu_i}2^{-Z}\le2^{-L/3}.
 \tag{4.7}
\]

On the event `K<L/6` one has `Z<L/6`, so Markov's inequality applied to `2^{-Z}` gives

\[
 \Pr(K<L/6)\le2^{-L/6}=:\delta.
 \tag{4.8}
\]

The elementary integral Stirling bound gives for every `k>=1`

\[
 g(k)\ge\log_2k-\log_2e.
 \tag{4.9}
\]

Since `L/6>=4`, (4.8)--(4.9) yield

\[
 \frac{Q_i}{j_i}
 \ge(1-\delta)
 \left(\log_2L-\log_2(6e)\right).
 \tag{4.10}
\]

Using `m_i+1<=L+1.1`, the difference between the left side of (4.3), divided by `j_i`, and `Q_i/j_i` is at most

\[
 \log_2(6e)
 +\log_2\left(1+\frac{1.1}{L}\right)
 +2^{-L/6}\log_2L.
 \tag{4.11}
\]

For `L>=24`, the last term is decreasing. Hence (4.11) is smaller than

\[
 4.03+0.065+\frac1{16}\log_2 24
 <4.39<19/4.
\]

This proves (4.3). QED.

### Why this improves the previous robust payment

The earlier fixed-`1/16` TV proof lost an `epsilon_i log m_i` term because TV may move mass onto very shallow degrees, where one address costs `log m_i`. Such a move is available to an abstract subset law but not freely available to a Boolean derivative row of density `j_i approx 2^{-m_i}`. Equation (4.7) makes shallow spectral degree exponentially unlikely in `L`; that is exactly the missing Boolean input.

The result is therefore compatible with fixed `epsilon=1/16` Palm robustness and does not require the much stronger `epsilon=O(1/m)` condition.

## 5. PROVED: fixed-robust in-trigger companion entropy is factorial-paid

Now impose both pieces of the actual robust near-subcube regime:

\[
 \operatorname{TV}(\nu_j,U_{F_j})\le\epsilon_j\le\frac1{16},
 \qquad m_j:=|F_j|\ge1,
 \tag{5.1}
\]

and the physical density match (4.2) with `m_i=m_j`.

For a fixed companion label `j`, define the nonnull companion mass

\[
 d_j:=j_j-u_j=\sum_{i\ne j}r_{ij}
 \tag{5.2}
\]

and the off-trigger companion flow

\[
 e_j:=\sum_{\substack{i\ne j\\ i\notin F_j}}r_{ij}.
 \tag{5.3}
\]

When `e_j>0`, let `xi_j` be the normalized distribution of those off-trigger identities:

\[
 \xi_j(i)=r_{ij}/e_j,
 \qquad i\notin F_j.
 \tag{5.4}
\]

### Lemma B12-COMPANION-EXCEPTION-MASS-03

For every row satisfying (5.1),

\[
 \boxed{e_j\le\epsilon_j j_j,}
 \tag{5.5}
\]

and

\[
 \boxed{
 d_j\ge(1/4-\epsilon_j)j_j\ge\frac3{16}j_j.
 }
 \tag{5.6}
\]

Therefore

\[
 \boxed{e_j/d_j\le1/3.}
 \tag{5.7}
\]

### Proof

From the definitions,

\[
 \frac{e_j}{j_j}
 =E_{\nu_j}\frac{|B\setminus F_j|}{1+|B|}.
\]

The displayed function lies in `[0,1]` and is identically zero under `U_{F_j}`, so TV gives (5.5).

Similarly

\[
 \frac{d_j}{j_j}
 =E_{\nu_j}\frac{|B|}{1+|B|}.
\]

For `B` uniform on subsets of an `m`-set,

\[
 E\frac1{1+|B|}=a_m
 =\frac{2-2^{-m}}{m+1}\le\frac34
 \qquad(m\ge1),
\]

so the ideal nonnull mass is at least `1/4`. TV changes it by at most `epsilon_j`, proving (5.6), and (5.7) follows. QED.

### Theorem B12-ROBUST-COMPANION-CODE-04

Let

\[
 R_j(i)=\frac{r_{ij}}{d_j}\qquad(i\ne j)
 \tag{5.8}
\]

be the actual inserted-label distribution conditioned on companion `j`. Then

\[
 \boxed{
 d_j H(R_j)
 \le Q_j+C_1j_j+e_jH(\xi_j),
 }
 \tag{5.9}
\]

where

\[
 \boxed{
 C_1:=\frac{19}{4}+h_2(1/3)
 =5.66829583405449\ldots .
 }
 \tag{5.10}
\]

### Proof

Split `R_j` into trigger and off-trigger labels. With `beta_j=e_j/d_j<=1/3`, Shannon's grouping rule gives

\[
 H(R_j)
 =h_2(\beta_j)
 +(1-\beta_j)H(R_j\mid F_j)
 +\beta_jH(\xi_j).
\]

The trigger conditional distribution lives on at most `m_j` labels, hence

\[
\begin{aligned}
 d_j H(R_j)
 &\le d_j h_2(1/3)
 +(d_j-e_j)\log_2m_j
 +e_jH(\xi_j)\\
 &\le h_2(1/3)j_j
 +j_j\log_2(m_j+1)
 +e_jH(\xi_j).
\end{aligned}
\]

Apply Theorem 02. QED.

This is the requested influence-relative row code. All in-trigger identities of a fixed-robust physical near-subcube row are absorbed by its **own** nonoverlapping factorial share at coefficient one. No ambient `log n`, raw codimension, or second-derivative bank appears. The only row-local identity entropy left is the explicit off-trigger companion term `e_jH(xi_j)`.

## 6. New global companion normal form

For a family `R` of rows satisfying (5.1) and (4.2), define

\[
 J_R=\sum_{j\in R}j_j,
 \qquad
 Q_R=\sum_{j\in R}Q_j,
 \tag{6.1}
\]

and

\[
 \mathcal X_R
 :=\sum_{j\in R}e_jH(\xi_j).
 \tag{6.2}
\]

For the complement, define its exact nonnull companion entropy

\[
 \mathcal N_{\bar R}
 :=\sum_{j\notin R}d_jH(R_j).
 \tag{6.3}
\]

Summing (5.9) gives

\[
 \sum_{j\in R}d_jH(R_j)
 \le Q_R+C_1J_R+\mathcal X_R.
 \tag{6.4}
\]

The inherited Palm insertion code is

\[
 H(S)
 \le H(K)+JH(\pi)-D_{\rm seq}-Q.
 \tag{6.5}
\]

Use `D_seq>=D_comp`, then (1.4), Theorem 01, and (6.4):

\[
 \boxed{
 H(S)
 \le H(K)+C_0J+C_1J_R
 +\mathcal X_R+\mathcal N_{\bar R}
 -(Q-Q_R).
 }
 \tag{6.6}
\]

Since `Q-Q_R>=0` and `J_R<=J`, a coarser but useful display is

\[
 \boxed{
 H(S)
 \le H(K)+9.08442376125546\,J
 +\mathcal X_R+\mathcal N_{\bar R}.
 }
 \tag{6.7}
\]

Equation (6.6), not (6.7), is the preferred ledger because it keeps the unused factorial rebate visible.

### What has disappeared

The following are no longer live positive terms for rows in `R`:

* the null/first-label ambient identity entropy;
* the in-trigger coordinate identity entropy;
* any need to charge `sum d_k` at unit price;
* the previous `16/3` multiplicative spend of the factorial rebate;
* the fleet01 fine condition `epsilon_i<=1/(16m_i)`.

### What remains

Only two companion-address objects survive:

1. `mathcal X_R`, the identities of off-trigger companions of robust rows; its total **mass** satisfies
   \[
   \sum_{j\in R}e_j\le\frac1{16}J_R,
   \tag{6.8}
   \]
   but its entropy is not bounded merely from that mass; and
2. `mathcal N_{bar R}`, the nonnull companion entropy carried by nonrobust rows.

This matches the current B18 integrability picture rather than bypassing it. B18 already reduces robust sink external gates to the nonrobust sector and warns that the surviving nonrobust high-depth branch cannot be paid by `sum d_k=O(J)`. Equation (6.6) gives a different nonreuse target: pay the **actual first-moment companion exception flow**, not every physical second derivative.

For robust-to-robust endpoints, the earlier B12 trigger theorem gives an additional classification. If an off-trigger companion `i notin F_j` nevertheless has `j in F_i`, then the trigger is one-sided and the corresponding robust edge `i -> j` is a factor-seven influence-scale escape. If neither direction is a trigger, it belongs to the mutually rare robust-pair branch. Thus `mathcal X_R` naturally splits into geometric scale escapes, mutually rare robust pairs, and companions landing in the nonrobust sector. No entropy bound for those three pieces is claimed here.

## 7. Relation to the newest fleet02 physical anchor theorem

The current fleet02/B13 actual-anchor theorem leaves, on the same source-frontier family,

\[
 \sum_{i\in A_*}j_i\log_2(1/j_i)+2\mathcal D_{A_*}
\]

as a valid upper bound for the physical correction code. The first term must **not** be declared `O(J)`; the one-point family rules that out globally.

The present theorem explains what an influence-relative compiler has to do instead. It does not reveal all coordinate codimensions in `A_*` at once. The exact insertion process samples one label with `1/K` weight, then—if a companion exists—addresses the next label relative to that companion. The no-companion branch is universally paid by Theorem 01, and fixed-robust in-trigger identities are factorial-paid by Theorem 04. Therefore a future use of fleet02's actual anchor child needs to transfer only the **signed physical correction plus the explicit companion exception channels**, rather than paying the raw selector globally.

This is a genuine use of the fleet02 result: it tells us that the physical nonproduct part has already been compressed to an actual-anchor correction, while (6.6) compresses the robust spectral address part without ambient dimension. The still-missing arrow is a nonreusing transfer/payment for `mathcal X_R + mathcal N_{bar R}` together with the anchor correction; claiming that arrow now would be circular.

## 8. Exact finite diagnostics

`check_harmonic_companion_row_code.py` was executed locally with no remote compute. It enumerates every Boolean truth table through dimension four modulo global sign, applies the minimizing-character gauge, computes the Walsh-square spectral law, and checks:

* the row-sum companion identities `u_j + sum_{i!=j} r_ji = j_j` and `sum u_j=V`;
* Theorem 01 rowwise and the global null-entropy bound (3.2);
* Theorem 02 for every codimension satisfying the physical relative-`1/16` density match;
* for every actual trigger set `F_j` simultaneously satisfying Palm `TV<=1/16` and the physical density match, the exception-mass bound, nonnull-mass bound, and robust companion code (5.9).

Counts:

* Boolean functions: `32,906`;
* nonconstant after folded gauge: `32,876`;
* active row checks: `130,392`;
* physical density-matched address checks: `73,048`;
* robust row/trigger-set checks: `18,112`;
* violations: `0`.

Observed maxima/minima:

* maximum ratio of the left side of (3.2) to its proved bound: `0.38420692315097427`;
* maximum rowwise ratio in (3.1) to its proved bound: `0.48736911133121164`;
* largest `lhs-rhs` in Theorem 02: `-0.4254875488422101` bits of weighted mass;
* largest `lhs-rhs` in Theorem 04: `-0.685023112035507`;
* minimum robust nonnull companion fraction `d_j/j_j`: exactly `1/4` in the enumeration.

At dimensions at most four every row meeting both stringent robust/density conditions had zero observed off-trigger companion flow, so the enumeration does **not** constitute evidence that `mathcal X_R` vanishes generally. The proof of (5.9) explicitly retains it.

Checker SHA-256:

`567bf72c41b1acc63edc8ca84869d951bf170077cf010d53ce98a43fa36a8cb8`

Archived stdout SHA-256:

`b05ebedd31887cb35eeff9458c0ff0f055d5f21629790f6ed9fba6ffe97e7daa`

The finite check supports the algebra and implementation only. The displayed inequalities are analytic.

## 9. Preserved obstructions and exact next target

This run does **not** use or assert

\[
 \sum_k d_k=O(J).
\]

It also does not use ambient-alphabet Fannes continuity, does not turn small TV mass into a small entropy without an address code, and does not apply FEI recursively to a non-Boolean subprobability spectrum.

The next interface-B target is now sharper:

> Prove a nonreusing bound for the off-trigger companion exception entropy `mathcal X_R` plus the nonrobust companion entropy `mathcal N_{bar R}`, using the factor-seven robust quotient DAG, the current B18 high-depth/nonrobust reduction and mixed-curvature conservation, while preserving the exact negative remainder `-(Q-Q_R)`.

A particularly concrete decomposition is to split `mathcal X_R` into:

1. robust one-sided trigger pairs, which are forced scale escapes;
2. robust mutual nontrigger pairs, each rare in both Palm rows; and
3. pairs whose inserted label is nonrobust, which should interface with the B18 nonrobust high-depth remainder.

The accounting must be performed on the actual companion flow `r_ij`, whose total mass is `J-V<=J`, not on the raw pair/depth bank. This is the decisive nonreuse requirement for the next run.

**Full uniform-cube FEI remains OPEN / NOT PROVED.**
