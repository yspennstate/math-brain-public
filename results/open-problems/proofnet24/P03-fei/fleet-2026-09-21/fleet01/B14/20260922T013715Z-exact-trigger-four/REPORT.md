# B14 — exact-trigger stationary block policy closes at constant four

**Run:** `20260922T013715Z-fleet01-B14-fei-r11`  
**Outcome:** **ESSENTIAL_STEP_APPLIED (partial branch).** Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository sources were consumed directly; no authenticated cognitive-brain retrieval/context is claimed.

## 0. Candidate/version and exact old/new implication

The current campaign-A block compiler remains the source-exact fleet01/B18 report

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, blob `9f2bb40584be20e5e440e7f3913873c34858bc91`.

The newest fleet01/B18 report overall (`20260922T0117Z-recursive-shared-graft`, blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`) is a gate-potential candidate elimination and does not replace this live campaign-A restriction compiler. This run therefore attacks the reset assignment: specify and analyze an actual realizable block-selection policy for the current restriction-critical case.

Two named other-account results are used *inside* the proof:

1. fleet02/B14, `20260921T220126Z-stationary-trigger-selector/REPORT.md`: a nonempty closed family of C12-certified near-subcube pivotality rows contains a row `(j,Z_j)` with `I_{Z_j} <= |Z_j| p_j`, and the corresponding physical restriction policy telescopes the true folded drift.
2. fleet03/B13, `20260921T233326Z-moving-defect-selector/REPORT.md`, blob `6b4477ad0c5328d335cec64204642dbf2e8a5132`: support reciprocity `p_{jk}=p_{kj}`; and at the exact endpoint `eta_j=1_Q`, the selector inequality forces the complete moving-one-point-defect representation and the exact entropy/influence peel.

**Old missing implication.** Even after the stationary selector, the campaign only had a coefficient-12 paid step in the C12 regime and a separate exact moving-defect classification. It had not combined them into the actual recursive block policy at the exact endpoint or identified the best universal local constant there.

**New proved inference.** On every nonempty *closed exact-subcube trigger kernel*, the stationary policy selects a genuine physical block whose entropy decrement is strictly less than four times its true folded-influence drift. Consequently every restriction-closed class whose noncharacters always retain such a kernel satisfies `H<4J<=4I`; in general every `H>4J` function has a physical restriction descendant with positive `H-4J` excess and **no** nonempty closed exact-trigger kernel. Thus the exact endpoint of this selector mechanism is fully paid; the unresolved branch is genuinely approximate/stalled.

## 1. Exact-trigger kernel and policy

Work at a median-character-centered Boolean state `f:{0,1}^n->{-1,+1}`, with folded influences

`p_i=Inf_i(f) in [0,1/2]`, `J(f)=sum_i p_i`.

For a pivot `j`, let `eta_j` be its pivotality event on the quotient cube. Call a chosen triple `(j,Z_j,Q_j)` an **exact trigger** if

- `Z_j` is a nonempty physical block disjoint from `{j}`;
- `r_j=|Z_j|`, `q_j=2^{-r_j}`;
- `Q_j` is one atom of the `Z_j` cube; and
- `eta_j = 1_{Q_j}` exactly.

Thus every exact trigger is C12-certified with error zero.

For a finite set `S` of exact-trigger pivots, call it **closed** when `Z_j subseteq S` for every `j in S`. As in fleet02/B14, start from all chosen exact triggers and iteratively prune rows whose control block leaves the current set. Let `S_infty` be the maximal closed kernel.

**Policy `EXACT-TRIGGER-4`.** At a noncharacter centered state:

1. if `S_infty` is empty, stop and label the leaf `EXACT_TRIGGER_STALLED`;
2. otherwise apply the fleet02 stationary selector inside `S_infty`, obtaining `j` with
   `I_{Z_j} <= r_j p_j`;
3. physically reveal the original-coordinate block `Z_j`;
4. recenter every child by a median character, recompute exact triggers, and repeat.

Every successful step removes at least one physical coordinate, so the tree is finite. No affine coordinate change, prescribed-coordinate payment, or every-core hypothesis is used.

## 2. The stationary inequality becomes equality at an exact trigger

Fix a selected row and write `Z=Z_j`, `r=|Z|`, `q=2^{-r}`. Exactness gives

`p_j = Pr(eta_j=1)=q`.

For every `k in Z`, the atom indicator changes across a `k`-edge on exactly a `2q` fraction of the quotient cube, hence

`p_{jk}:=Inf_k(eta_j)=2q`.

By fleet03/B13's pointwise mixed-square reciprocity,

`p_{kj}=p_{jk}=2q`.

For every pivotality event, `p_{kj} <= 2p_k`; therefore

`p_k >= q` for every `k in Z`.

The stationary selected row also obeys

`sum_{k in Z}p_k = I_Z <= r p_j = rq`.

The lower bounds force equality term by term:

\[
\boxed{p_k=q\quad(k\in Z),\qquad I_Z=rq.}
\tag{2.1}
\]

Thus the fleet03 moving-defect theorem applies with no residual error: there are Boolean functions `C,D` on the untouched coordinates `W` such that, after translating the atom to the origin,

\[
f=C(w)(1-1_Q(z))-D(w)\chi_j1_Q(z).
\tag{2.2}
\]

This retains the actual signs; `D` encodes the possibly moving defect orientation. The previously refuted fixed-orientation claim is not used.

## 3. Exact entropy decrement and a sharp four-payment

The same fleet03 theorem gives

\[
H(f)=K_r+(1-q)H(C)+qH(D),
\tag{3.1}
\]
with

\[
K_r=2q(2-q)r-2(1-q)^2\log_2(1-q).
\tag{3.2}
\]

After physically revealing `Z`, every off-atom branch is `C` and the atom branch is a character shift of `D`. Character shifts preserve spectral entropy, so

\[
\boxed{\Delta_Z H:=H(f)-\mathbb E_zH(f_{Z=z})=K_r.}
\tag{3.3}
\]

The posterior pivotality of `j` after revealing `Z` is exactly `1` on `Q` and `0` off `Q`; hence the live crossing term is

\[
\boxed{c_j(Z)=q.}
\tag{3.4}
\]

Using the exact folded drift identity from the current campaign,

\[
D_Z:=J(f)-\mathbb E_zJ(f_{Z=z})=I_Z+C_Z\ge I_Z+c_j(Z),
\]
so by (2.1) and (3.4),

\[
\boxed{D_Z\ge q(r+1).}
\tag{3.5}
\]

Fleet03 already established `K_r<4q(r+1)`. For completeness, the same fact follows directly from (3.2); therefore

\[
\boxed{\Delta_ZH<4D_Z.}
\tag{3.6}
\]

The constant four is intrinsic to this local mechanism: `K_r/[q(r+1)]` increases toward `4` as `r->infinity`. Thus no proof that only repeats this exact atom peel can produce a uniform local constant below four.

There is also a useful survivor-scale inequality. Since

`h_2(q)=qr-(1-q)log_2(1-q)`, one has exactly

\[
4h_2(q)-K_r
=2q^2r-2(1-q)(1+q)\log_2(1-q)>0,
\]
so

\[
\boxed{\Delta_ZH=K_r<4h_2(p_j).}
\tag{3.7}
\]

This is a true physical Shannon payment at the selected survivor scale, with no ambient-dimension continuity estimate.

## 4. Global telescoping of the actual policy

Run `EXACT-TRIGGER-4` on a finite physical restriction tree. At every successful node `v`, (3.6) gives

`Delta_v H < 4 D_v`.

Both quantities telescope under physical restriction:

\[
\sum_{v\text{ successful}}w_v\Delta_vH
=H(f)-\mathbb E_\ell H(f_\ell),
\]

\[
\sum_{v\text{ successful}}w_vD_v
=J(f)-\mathbb E_\ell J(f_\ell).
\]

Hence

\[
\boxed{
H(f)-4J(f)
\le
\mathbb E_\ell[H(f_\ell)-4J(f_\ell)].
}
\tag{4.1}
\]

(Strict inequality holds when at least one successful step has positive reach and the right side is interpreted before zero-probability degeneracies.)

Two consequences follow.

### Corollary 4.1 — exact-trigger restriction-closed class

If a restriction-closed class has the property that every centered noncharacter state has a nonempty closed exact-trigger kernel, then the policy cannot stall before reaching characters. Character leaves have `H=J=0`, and therefore

\[
\boxed{H(f)<4J(f)\le4I(f)}
\tag{4.2}
\]
for every noncharacter in the class.

### Corollary 4.2 — exact-stall localization

If `H(f)>4J(f)`, then running the policy produces an `EXACT_TRIGGER_STALLED` descendant `g` with

\[
\boxed{H(g)>4J(g)}
\tag{4.3}
\]
and no nonempty closed exact-trigger kernel.

Indeed, (4.1) makes the expected leaf excess positive; character leaves have zero excess, so some stalled leaf has positive excess.

This is an existential descendant obtained by an actual physical policy, not the refuted claim that every weakly critical tensor product must satisfy a shell or selector property.

## 5. Obstruction checks

This theorem deliberately does **not** overclaim coverage.

- **Addressing:** a data-coordinate pivotality event is an exact address atom, but its address controls need not themselves form a closed exact-trigger kernel. The policy may stall; no prescribed data coordinate is forced to pay.
- **Majority / recursive majority:** pivotality events are Hamming-layer objects rather than single atoms in general, so the exact-trigger hypothesis need not hold.
- **Tribes:** pivotality supports are unions/intersections of structured cylinders, not automatically one exact atom with a closed control system.
- **Sparse defects / bent-plus-flip:** the theorem only activates when the actual pivotality row is exactly atomic and closed; it does not infer exactness from small support or small error.
- **Tensor products:** the policy acts only on a genuinely closed exact subsystem and then recurses on physical descendants. Tensor replication therefore does not create an every-core conclusion.
- **Biased limits:** this report is for the uniform-cube FEI target. No product-biased extension is inferred from (3.6).

Thus the known counterexamples to fixed-coordinate payment, fixed-relative near-subcube payment, and every-critical-core shell bounds remain intact.

## 6. What this changes and what remains

**Applied essential step.** The current selector has a completely paid exact endpoint. Combining fleet02's stationary selector with fleet03's sign-preserving moving-defect theorem turns a closed exact trigger system into an actual recursive physical policy with local and global constant four. The full signs, original-coordinate cost, posterior crossing, and folded drift are all retained.

**Remaining universal implication.** A full campaign-A proof must now handle states with no closed exact-trigger kernel. The nearest live quantitative branch is the C12/approximate regime, where fleet02 obtains a factor-12 physical payment and fleet03 proves strong mixed-derivative compatibility but the moving-defect approximation error is still unpaid. Equivalently, the next useful theorem would be a quantitative version of (2.2)--(3.3): from

\[
Pr(\eta_j\triangle1_Q)\le q/(16r),\qquad I_Z\le rp_j,
\]
construct a physical descendant decomposition whose extra entropy cost is `O(qr)` with a dimension-independent constant, while retaining the moving orientation rather than imposing the false fixed orientation.

That is a genuinely smaller missing arrow than before this run: the exact endpoint no longer belongs to the obstruction set.

**Classification:** `ESSENTIAL_STEP_APPLIED (partial branch)`. **Full FEI remains OPEN.**

## 7. Scoped review

The report contains only mathematical formulas, public/internal artifact paths and sanitized provenance. It contains no credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive instructions, permission changes, public-posting instructions, or paid/remote-compute instructions.
