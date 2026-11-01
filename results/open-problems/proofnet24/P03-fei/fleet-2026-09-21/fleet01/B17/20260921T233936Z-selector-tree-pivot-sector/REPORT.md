# B17 — selector-candidate attack: exact subcube certificate and a tree-basis payment for the pivotal spectral sector

**Classification:** `ESSENTIAL_STEP_APPLIED` — a genuine part of the first missing selector inference is proved and applied, but the inference is not closed. Full uniform-cube Friedgut--Kalai FEI remains **OPEN / NOT PROVED**.

**Execution context:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval/context was used or claimed. No novelty or publication-priority claim is made.

## 0. Exact candidate versions consumed

This run follows the reset assignment for fleet01/B17: attack the selector/potential route with addressing, tribes and sparse defects.

The campaign-lead candidate used here is the latest complete fleet01/B18 statement available on fresh master:

- `fleet01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, blob `9f2bb40584be20e5e440e7f3913873c34858bc91`.

It proves the character-invariant folded activation bank and the conditional compiler. With
\[
\mathcal C(f)=\sum_i \mathfrak j(j_i),\qquad
\mathcal F=H-\mathcal C,\qquad
\mathcal G_\lambda=\mathcal F-\lambda\mathcal A_{z_d},
\]
its remaining high-ratio obligation is: on every physical-restriction core maximizing `G_lambda/J` with ratio larger than
\[
\rho_*=4h_2(1/4)=3.2451124978\ldots,
\]
find one physical pair `(A,j)` with a positive crossing fraction and
\[
E_A-\lambda\Lambda_A\le K h_2(j_j)
\tag{0.1}
\]
for universal constants.

The exact other-account result substantively used is

- `fleet02/B14/20260921T230653Z-asymmetric-shortcircuit-ledger/REPORT.md`, blob `242a3fddee17db5ed1d723962b76c8659f623d6a`.

For a pivot `x`, an `r`-bit control set `Z`, a target point/subcube event `Q={Z=a}` of mass `q=2^{-r}`, pivotality indicator `eta_x`, and
\[
E^- = \Pr(Q,\eta_x=0),\qquad E^+=\Pr(Q^c,\eta_x=1),\qquad p=\operatorname{Inf}_x(f)=q+E^+-E^-,
\]
that report preserves the original-coordinate hypothesis
\[
I_Z:=\sum_{k\in Z}\operatorname{Inf}_k(f)\le r p.
\tag{0.2}
\]
It proves a full-block bound under the asymmetric small-error window, and under the weaker fixed-relative condition
\[
E^-+E^+\le q/16
\tag{0.3}
\]
it proves a first-mismatch tree with folded drift at least `15 r q/16` and extracts at least a constant fraction of the pivot uncertainty. Its explicit remaining local arrow is the corrected-entropy upper bound
\[
\Delta_T\mathcal F\stackrel{?}{\le}K r q.
\tag{0.4}
\]
The point of this run is to attack (0.4), not to rename it.

I also retain the current correction that any positive-current/half-band closing argument must keep its entropy, `R16`, and terminal terms; none of those terms is dropped below.

## 1. A universal tree-basis entropy lemma

The first new lemma is independent of Booleanity.

### Lemma 1.1 — decision-tree basis payment

Let `u=u(Z,W)` be any real function, where `Z` consists of `r` Boolean coordinates and `W` denotes arbitrary remaining coordinates. Let `T` be any physical decision tree which queries only coordinates in `Z`. For each leaf `ell`, let `pi_ell` be its reach probability and let `u_ell` be the restricted function. Put
\[
e=\|u\|_2^2,\qquad e_\ell=\|u_\ell\|_2^2,
\qquad \alpha_\ell={\pi_\ell e_\ell\over e}
\]
when `e>0`. If `mu_u` denotes the normalized squared-Fourier law of `u`, then
\[
\boxed{
 eH(\mu_u)-\sum_\ell\pi_\ell e_\ell H(\mu_{u_\ell})
 \le e\bigl(r+H(\alpha)\bigr).
}
\tag{1.1}
\]

### Proof

For a leaf `ell`, let `C_ell` be its cylinder in the `Z` cube. The functions
\[
{1_{C_\ell}\over\sqrt{\pi_\ell}}\,\chi_R,
\]
where `R` ranges over the unqueried `Z` coordinates at that leaf, form an orthonormal basis of `L^2(Z)` when taken over all leaves. Tensor this with the Walsh basis in `W`.

Fix a Fourier label `U` in `W`. The ordinary Walsh coefficient vector indexed by `Z`-subsets and the tree-adapted coefficient vector at the same `U` are related by a `2^r`-dimensional orthogonal matrix. Their total `U`-energy is identical. Hence, conditioning on the external label `U`, changing from the tree basis to the ordinary Walsh basis can increase coefficient-square Shannon entropy by at most `log_2 2^r=r`.

In the tree basis the normalized coefficient-square law first chooses a leaf with probability `alpha_ell`, then chooses according to the normalized squared spectrum of `u_ell`. Its entropy is therefore
\[
H(\alpha)+\sum_\ell\alpha_\ell H(\mu_{u_\ell}).
\]
Adding the at-most-`r` basis-change cost and multiplying by `e` proves (1.1). Notice that this is an amplitude-level orthogonal change of basis: no Fourier signs are discarded or reconstructed. QED.

## 2. Apply the lemma to the exact pivotal spectral sector

For a Boolean function with distinguished pivot `x`, write
\[
f=A+xB,
\qquad
A={f|_{x=1}+f|_{x=-1}\over2},
\qquad
B={f|_{x=1}-f|_{x=-1}\over2}.
\tag{2.1}
\]
Pointwise `A,B in {-1,0,1}`, `AB=0`, and
\[
B^2=\eta_x,\qquad \|B\|_2^2=p=\operatorname{Inf}_x(f).
\tag{2.2}
\]
The Fourier supports of `A` and `xB` are disjoint according as the spectral sample omits or contains `x`. Thus
\[
H(f)=h_2(p)+(1-p)H(\mu_A)+pH(\mu_B).
\tag{2.3}
\]

For any control decision tree `T`, let `p_ell` be the leaf influence of `x`, and define the pivotality-biased transcript law
\[
\beta_\ell={\pi_\ell p_\ell\over p}.
\tag{2.4}
\]
Lemma 1.1 applied to `B` gives the exact sector payment
\[
\boxed{
 pH(\mu_B)-\sum_\ell\pi_\ell p_\ell H(\mu_{B_\ell})
 \le p\bigl(r+H(\beta)\bigr).
}
\tag{2.5}
\]

Now use the fleet02/B14 first-mismatch tree under (0.3). Its all-match `Q` leaf contains pivotal mass `q-E^-`; all mismatch leaves together contain exactly the false-positive pivotal mass `E^+`. Therefore
\[
\beta_{\rm out}={E^+\over p}\le {1\over15}.
\]
There are at most `r` mismatch leaves, hence
\[
H(\beta)
\le h_2(1/15)+{1\over15}\log_2 r
\le \log_2(r+1)\le r.
\tag{2.6}
\]
Also `p<=17q/16`. Consequently the **entire odd/pivotal Fourier sector** satisfies
\[
\boxed{
\Delta_T H_{x\text{-sector}}
\le 2pr
\le {17\over8}rq.
}
\tag{2.7}
\]
The binary mixture term in (2.3) is separately at most `h_2(p)=O(rq)` because `p` lies between `15q/16` and `17q/16`.

This directly applies to the missing (0.4): the logarithmically expensive rare pivotal sector is no longer unpaid. What remains is the **even/no-pivotal sector**
\[
(1-p)H(\mu_A)-\sum_\ell\pi_\ell(1-p_\ell)H(\mu_{A_\ell}),
\tag{2.8}
\]
together with exact corrected-potential bookkeeping. A generic application of Lemma 1.1 to `A` would cost order `r`, not `rq`, and is therefore not enough. This is the new, narrower local gap.

## 3. Exact subcube + minimal original-coordinate budget: the whole row is paid

The zero-error endpoint of the fleet02/B14 primitive row can be solved completely, with arbitrary actual signs and arbitrary environment.

### Theorem 3.1 — exact primitive subcube certificate

Assume
\[
\eta_x=1_Q,\qquad Q=\{Z=a\},\qquad q=2^{-r},
\tag{3.1}
\]
and preserve the original-coordinate bound
\[
I_Z\le r\operatorname{Inf}_x(f)=rq.
\tag{3.2}
\]
Then necessarily every control influence is exactly `q`, and there exist Boolean functions `g(W),h(W)` such that, up to the harmless convention for the sign of `x`,
\[
\boxed{
f(x,z,w)=g(w)1_{Q^c}(z)+x h(w)1_Q(z).}
\tag{3.3}
\]
For the first-mismatch tree on `Z`,
\[
\boxed{
\Delta_T H
=(2-q)h_2(q)+q(1-q)\log_2(2^r-1)+qr
<5rq.
}
\tag{3.4}
\]
The corrected decrement obeys the same upper bound.

### Proof

Fix a control `k`. On the edge between `a` and `a\oplus e_k`, and for every fixed `w`, the two `x`-values at `a` are opposite because `x` is pivotal, while the two `x`-values at the neighboring point agree because `x` is not pivotal there. Hence exactly one of the two `k`-edges (one for each `x`) is bichromatic. Since the unoriented `a`--`a\oplus e_k` edge is encountered from two `z` endpoints, this contributes exactly `q` to `Inf_k(f)`. Thus every `Inf_k(f)>=q`; (3.2) forces equality for every `k` and leaves no additional control disagreement anywhere.

For fixed `x,w`, the punctured `r`-cube `Q^c` is connected (`r=1` is immediate), so `f` is constant in `z` on `Q^c`. Nonpivotality there makes that constant independent of `x`; call it `g(w)`. On `Q`, pivotality gives the form `x h(w)`. This proves (3.3) without altering any source sign.

The no-`x` Fourier sector is `g(W)(1-1_Q(Z))`; the `x` sector is `xh(W)1_Q(Z)`. The normalized squared spectrum of `1_Q` is uniform on the `2^r` control frequencies. For `1-1_Q`, its normalized spectral law has mass `1-q` at the empty control frequency and total mass `q`, uniformly spread over the `2^r-1` nonempty frequencies. Therefore
\[
H(f)=h_2(q)
 +(1-q)\bigl[H(g)+h_2(q)+q\log_2(2^r-1)\bigr]
 +q[H(h)+r].
\]
The first-mismatch leaves have entropy `H(g)` off `Q` and `H(h)` on `Q`; subtraction gives (3.4).

For the corrected entropy, the symmetric singleton potential `mathfrak j(p)` is concave in the raw influence `p` (equivalently use the inherited strong-concavity theorem on the folded half and symmetry). Surviving-coordinate influences are martingales under physical restriction, and queried-coordinate potential disappears. Hence the total correction potential cannot increase on average, so `Delta_T mathcal F<=Delta_T H`.

Finally, `h_2(q)<=q(r+log_2 e)` and `log_2(2^r-1)<=r` give `<5rq` for `r>=3`; direct substitution gives ratios `4` for `r=1` and `8-(9/4)log_2 3=4.4338...` for `r=2`. QED.

### Consequence for the lead certificate

For this exact row, revealing `Z` makes the folded `x`-influence deterministic (`0` or `1`), so the crossing amount is exactly `q`: one may take `gamma=1`. Since `h_2(q)>=rq`, (3.4) implies the unrefunded certificate upper bound with `K=5`; the activation refund `-lambda Lambda` can only help. Thus every high critical core which contains such an exact minimal-budget row satisfies the campaign-lead certificate at that row.

This endpoint was already inside the easier small-asymmetric regime of fleet02/B14; the new value here is the exact sign-preserving structural formula (3.3) and its use as the base case for the sector decomposition above.

## 4. Addressing stress test: it violates the budget and sits below the high-ratio gate

Take the standard `r`-bit addressing function with data bits `y_a`,
\[
f(z,y)=y_z.
\]
For a fixed data coordinate `y_a`, its pivotality event is exactly `Q={z=a}` with `q=2^{-r}`. However every address control has influence `1/2`, so
\[
I_Z={r\over2},\qquad r\operatorname{Inf}_{y_a}(f)=rq.
\tag{4.1}
\]
Thus for `r>=2` addressing misses the fleet02/B14 original-coordinate premise by the factor `2^{r-1}`. This is not a hidden-coordinate issue: the failure occurs in the actual physical address coordinates.

The squared Fourier law is uniform on `4^r` coefficients, so
\[
H=2r,\qquad J=1+{r\over2}.
\]
For the corrected potential,
\[
\mathcal C=r+2^r\mathfrak j(q),\qquad
{\mathcal F\over J}={r-2^r\mathfrak j(q)\over1+r/2}\longrightarrow2.
\tag{4.2}
\]
Hence the natural addressing family also lies asymptotically below the campaign-lead admission threshold `rho_*=3.245...`.

A first-mismatch tree for the chosen data pivotality has corrected cost tending to a positive constant while `h_2(q)->0`; therefore **that particular naive target/tree is not a cheap Bellman certificate**. This is not a counterexample to the exact critical-core selector, because the selector may choose another coordinate/tree and the family is below the lead high-ratio gate. The correct conclusion is that any universal proof cannot simply choose an arbitrary rare addressed data bit.

## 5. Balanced tribes stress test: good physical budget, bad near-subcube coverage, low corrected ratio

For standard tribes with `m` disjoint tribes of width `w`, let `x` be one variable in a tribe and let `Z` be its other `r=w-1` tribe variables. Put `Q={all bits of Z favorable}` so `q=2^{-(w-1)}`. If `R` is the event that no other tribe is satisfied, then
\[
\eta_x=1_Q1_R,
\qquad
p=q\rho,\quad \rho=\Pr(R)=(1-2^{-w})^{m-1}.
\tag{5.1}
\]
Thus
\[
E^-=q(1-\rho),\qquad E^+=0.
\tag{5.2}
\]
Every mate control has the same influence `p`, so the original-coordinate budget is exact:
\[
I_Z=rp.
\tag{5.3}
\]
For balanced tribes, `(1-2^{-w})^m` is asymptotically `1/2`, hence `rho->1/2` and
\[
E^-/q\to1/2.
\]
So tribes emphatically fails the fixed-relative near-subcube condition (0.3) even though it exactly satisfies the control-influence budget. The obstruction is **coverage/false-negative mass**, not hidden local coordinate cost.

The same family does not threaten the high-ratio lead gate. In the ideal balance identity `(1-a)^m=1/2`, `a=2^{-w}`, the nonempty Fourier touched-block set has the law of iid Bernoulli(`a`) blocks conditioned to be nonempty, and within every touched block the nonempty Fourier subset is uniform. Consequently
\[
H=2m h_2(a)-2+2ma\log_2(2^w-1),
\qquad
I=J=mw{a\over1-a}.
\tag{5.4}
\]
Hence `H/I->4`, while `mathcal C/J->2/ln2`, so
\[
{\mathcal F\over J}\longrightarrow4-{2\over\ln2}=1.11461\ldots<\rho_*.
\tag{5.5}
\]
The usual integer near-balanced sequence has the same limit. Thus tribes shows why near-subcube coverage cannot be asserted for every low-influence row, but does not refute a theorem restricted to high corrected-ratio critical cores.

## 6. Sparse defects

Theorem 3.1 already treats a sign-complete sparse-defect endpoint: away from one control point the pivot is absent, at that point it is present, and the outside/inside signs `g,h` are arbitrary Boolean environment functions. The exact original-coordinate budget forces all extra control variation to vanish.

The canonical one-point Boolean output defect gives the familiar low-influence scale `H/I->4`; its corrected ratio again tends to `4-2/ln2`, below the campaign-lead threshold. Thus the most obvious sparse defects do not defeat the thresholded compiler. The genuinely unresolved local regime is instead a near-subcube row with fixed-relative false-positive/false-negative mass where the **even/no-pivotal background** can still carry coherent recombination.

## 7. Old gap -> new gap

Before this run the first local missing implication from fleet02/B14 was the total bound
\[
\Delta_T\mathcal F\le K rq
\]
for the fixed-relative first-mismatch tree.

After this run:

1. the binary pivot-mixture term is `O(rq)`;
2. the entire odd/pivotal spectral sector is rigorously paid by (2.7), at most `17rq/8`;
3. the zero-error endpoint is completely paid, `Delta_T mathcal F<5rq`, with exact Boolean structure;
4. the remaining local issue is only the **even/no-pivotal sector** (2.8), with the actual corrected-potential refund retained;
5. independently, the campaign-lead global **coverage** gap remains: one must still show that every high-`G_lambda/J` critical core has some certificate row. Addressing and tribes show that unqualified row-selection statements are false or irrelevant, while neither family refutes the thresholded high-ratio statement.

So this run is classified `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`: a necessary part of the first missing inference was proved and inserted into the exact peer construction, but full FEI still requires the even-sector estimate and the high-critical-core coverage theorem.
