Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not authenticated GPT-6 maximum reasoning, and I do not claim otherwise.

# P03-B coupling report — two-sided return elasticity and an exact fresh-child revisit charge

**Status:** PROVED PARTIAL / NEW PROBABILISTIC LEMMA / RESTRICTED COMPONENT CERTIFICATE. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains open. Nothing below is represented as a full speed-monotonicity theorem.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, regeneration/coupling, spine comparison and source-valid counterexample role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master immediately before write:** `9828cdd6b7977bc2279bcb70e616d5b714ff5d4c`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T1120Z__revisit-only-score-decomposition-and-four-step-obstruction.md`, creation commit `5c16a2aaabbc434fb0a806c4234aaac8c0ce35db`.

**Latest complementary P03-A checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1106Z__uniform-explicit-terminal-strip-for-all-one-two-mixtures.md`, creation commit `c7233ae9abadfd8fca0970561e6ab96b9103c758`. P03-A handles recursive analytic identities and now has an explicit terminal strip for all nondegenerate `{1,2}` mixtures. This report stays on bounded-support `d>=2` regeneration/path-history control.

## 1. Source continuity and normalization

Primary source: Gérard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865. The offspring law satisfies `P(Z=0)=0`. At a non-root vertex with `k` children their **outward child-bias** parameter `beta` is

\[
q_k(\beta):=P_\beta(\text{parent}\mid k)=\frac1{1+\beta k},
\qquad
P_\beta(\text{a specified child}\mid k)=\frac\beta{1+\beta k}.
\tag{1.1}
\]

Thus increasing `beta` means stronger outward bias. The walk is transient for `beta>1/EZ`, and the LPP conjecture asks that the speed be increasing on the whole interval `(1/EZ,infinity)`. The arXiv high-bias theorem is `beta>=717` (and `717/d` at minimum offspring `d`); it is historical context, not the current frontier.

Bowditch–Tokushige, arXiv:1906.07913, prove differentiability in the ballistic/CLT regime and give a two-dimensional Gaussian covariance expression; arXiv:2006.03433 proves analyticity in the ballistic regime. These are regularity tools, not a derivative-sign theorem.

The strongest broad later primary monotonicity theorem retained after the bounded 20 September 2026 source check is He Song, Longmin Wang and Kainan Xiang, *The speed of a biased walk on a Galton–Watson tree without leaves is monotonic for low values of bias*, J. Appl. Probab. 62 (2025), 1044–1052. Their parameter is reciprocal **parent bias** `lambda=1/beta`; for minimum offspring `d>=2` they prove strict decrease for

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

No inverse-parametrization contradiction is inferred.

For the quantitative statements below assume the source-valid bounded-support family

\[
2\le d\le Z\le D<\infty,
\qquad \beta d>1.
\tag{1.3}
\]

## 2. Inherited exact bottleneck

The preceding report reduced the finite-horizon derivative to a local posterior term plus a single revisit-gated transport covariance. If `M_t` and `V_t` are the posterior mean and variance of

\[
Q_v=q_{Z_v}(\beta)
\]

immediately before departure `t`, `j_t` is that vertex's departure number, and

\[
B_T=\sum_{t<T:\,j_t\ge2}(M_t-\mu),
\qquad \mu=EQ_v,
\]

then

\[
\frac d{d\beta}E_\beta R_T
=
\frac2\beta E\sum_t\bigl[M_t(1-M_t)-j_tV_t\bigr]
-2E[B_T\mathcal S_T].
\tag{2.1}
\]

Moreover

\[
E[B_T\mathcal S_T]
=E\sum_{t:\,j_t\ge2}(M_t-\mu)\mathcal S_t^-.
\tag{2.2}
\]

Thus the remaining nonlocal problem is score transported across an excursion and paid on a later revisit. The previous report proved only the one-sided return-odds contraction. This run obtains the missing reverse inequality and then uses it to price one genuinely adverse revisit channel exactly.

## 3. Two-sided quenched return-odds elasticity

Fix an arbitrary deterministic rooted tree whose every non-root vertex has at least `d` children, and let

\[
h_x(\beta)=P_\beta^x(T_{x^*}<\infty)
\]

for a non-root vertex `x`. Write its children as `x_1,...,x_k`. First-step decomposition gives

\[
h_x=\frac1{1+\beta S_x},
\qquad
S_x:=\sum_{i=1}^k(1-h_{x_i}).
\tag{3.1}
\]

Equivalently, for the return odds

\[
O_x:=\frac{h_x}{1-h_x},
\qquad
O_x=\frac1{\beta S_x}.
\tag{3.2}
\]

The earlier comparison gives

\[
0\le h_x\le r:=\frac1{\beta d}<1.
\tag{3.3}
\]

Define the logarithmic odds elasticity

\[
g_x:=-\beta\frac d{d\beta}\log O_x
=-\beta\frac{h_x'}{h_x(1-h_x)}.
\tag{3.4}
\]

On a finite truncation, differentiating (3.2) yields

\[
g_x=1+\frac{\beta S_x'}{S_x}.
\tag{3.5}
\]

Since `-beta h_i'=g_i h_i(1-h_i)`, this becomes

\[
\boxed{
 g_x
=1+\sum_i \frac{1-h_{x_i}}{S_x}\,g_{x_i}h_{x_i}.
}
\tag{3.6}
\]

The coefficients `(1-h_i)/S_x` are nonnegative and sum to one. Using `h_i<=r`,

\[
1\le g_x\le1+r\max_i g_{x_i}.
\]

At the last nonabsorbing level of a finite truncation `g=1`, so backward induction gives

\[
1\le g_x\le1+r+r^2+\cdots\le\frac1{1-r}.
\tag{3.7}
\]

The finite truncation return probabilities increase to the infinite-tree return probability. The bounds above are uniform on compact `beta`-intervals inside `beta d>1`, hence the limit is locally Lipschitz and the corresponding Dini derivative bounds pass to the limit. Wherever the derivative exists,

\[
\boxed{
1\le
-\beta\frac d{d\beta}\log\frac{h_x}{1-h_x}
\le\frac1{1-r}
=\frac{\beta d}{\beta d-1}.
}
\tag{3.8}
\]

Equivalently,

\[
\boxed{
\frac{h_x(1-h_x)}\beta
\le -h_x'(\beta)
\le
\frac{h_x(1-h_x)}{\beta(1-r)}.
}
\tag{3.9}
\]

Integrating (3.8) from `beta_1` to `beta_2>beta_1>1/d` gives a genuinely two-sided odds comparison:

\[
\boxed{
\frac{\beta_1d-1}{\beta_2d-1}
\frac{h_x(\beta_1)}{1-h_x(\beta_1)}
\le
\frac{h_x(\beta_2)}{1-h_x(\beta_2)}
\le
\frac{\beta_1}{\beta_2}
\frac{h_x(\beta_1)}{1-h_x(\beta_1)}.
}
\tag{3.10}
\]

The lower bound in (3.10), or equivalently the upper bound in (3.9), is new relative to the preceding P03-B checkpoint. It is sharp on the regular `d`-ary tree: there `h=1/(beta d)` and the left inequality in (3.10) is equality.

## 4. Exact fresh-child first-return transport charge

Now return to the annealed Galton–Watson path filtration. At a previously visited vertex `v`, suppose just before a departure the posterior law of

\[
Q=q_{Z_v}(\beta)
\]

has mean `M` and variance `V`, and exactly `c` distinct children of `v` have already been used. Set

\[
\alpha_c:=1+\beta c.
\tag{4.1}
\]

The probability that the next departure discovers a **new** child is

\[
p_N=1-\alpha_cM.
\tag{4.2}
\]

Bayes' formula gives the posterior mean after this new-child departure as

\[
M_N=M-\frac{\alpha_cV}{1-\alpha_cM},
\tag{4.3}
\]

hence the innovation is

\[
\Delta M_N=-\frac{\alpha_cV}{1-\alpha_cM}.
\tag{4.4}
\]

The selected new child's subtree is fresh and independent of the local degree posterior at `v`. Let `h(\beta)` be its quenched probability of ever returning to `v`, and let

\[
\bar h(\beta)=E[h(\beta)]
\]

under the fresh Galton–Watson subtree law. For finite killed truncations, the score identity gives

\[
E_\beta[\mathcal S_{\rm exc};\,\text{return}]=h'(\beta),
\]

where `S_exc` is the likelihood score accumulated after entry into the child and before the first return to `v`. Passing through the uniformly bounded return derivative in (3.9) yields the same identity for the limiting first-return channel.

Therefore the covariance charge created by the **new-child posterior innovation itself**, transported through that same child's first excursion and paid at its first return, is exactly

\[
\boxed{
\mathcal C_N^{(1)}
=p_N\Delta M_N\,\bar h'(\beta)
=-\alpha_cV\,\bar h'(\beta)
\ge0.
}
\tag{4.5}
\]

This is an adverse contribution to `E[B_T S_T]`: both the new-child innovation and the returned-descendant excursion score are negative.

This identity isolates a concrete first-order negative mechanism rather than merely bounding all revisits by a worst degree pair.

## 5. Uniform bound for the adverse fresh-child channel

From (3.9), for every fresh child

\[
-\beta h'(\beta)
\le\frac{h(1-h)}{1-r}.
\]

Since `0<=h<=r`, define

\[
\chi(r):=\frac{\max_{0\le u\le r}u(1-u)}{1-r}
=
\begin{cases}
 r,&0<r\le1/2,\\[2mm]
 \dfrac1{4(1-r)},&1/2\le r<1.
\end{cases}
\tag{5.1}
\]

Then (4.5) gives the explicit component bound

\[
\boxed{
0\le\mathcal C_N^{(1)}
\le\frac{\alpha_cV}{\beta}\chi(r).
}
\tag{5.2}
\]

Compare this with the local favorable margin from (2.1),

\[
\frac1\beta\left[M(1-M)-jV\right]
\tag{5.3}
\]

at the `j`-th departure. The inherited sharp support ratio is

\[
\frac{V}{M(1-M)}
\le
\rho_{d,D}(\beta)
:=
\frac{\beta(\sqrt D-\sqrt d)^2}
{(1+\beta d)(1+\beta D)}.
\tag{5.4}
\]

Hence the local term plus this entire adverse **new-child first-return** component is nonnegative whenever

\[
\boxed{
\rho_{d,D}(\beta)
\left[j+\alpha_c\chi\!\left(\frac1{\beta d}\right)\right]
\le1.
}
\tag{5.5}
\]

A history-free sufficient condition uses `c<=D`:

\[
\boxed{
\rho_{d,D}(\beta)
\left[j+(1+\beta D)\chi\!\left(\frac1{\beta d}\right)\right]
\le1.
}
\tag{5.6}
\]

This is deliberately only a **component certificate**. Parent-side excursions, previously explored child subtrees, and repeated returns after the first revisit are not included in (5.6).

## 6. Exact near-regular test: `{2,3}` at `beta=3/5`

Take any offspring law supported on `{2,3}` and `beta=3/5`. Then

\[
r=\frac56,
\qquad
\chi(r)=\frac{3}{2},
\qquad
1+\beta D=\frac{14}{5},
\]

and

\[
\rho_{2,3}(3/5)
=\frac{(3/5)(\sqrt3-\sqrt2)^2}
{(11/5)(14/5)}
\approx0.00983966049678.
\]

Thus the worst-history coefficient in (5.6) is

\[
j+\frac{21}{5}=j+4.2.
\]

For `j=97`,

\[
(97+4.2)\rho\approx0.9957736423<1,
\]

whereas for `j=98` the same coarse uniform test gives approximately `1.005613303>1`. Therefore:

\[
\boxed{
\text{for every `{2,3}` offspring mixture at `beta=3/5`,
all departures }j\le97
\text{ have nonnegative local-plus-fresh-child-first-return margin.}
}
\tag{6.1}
\]

This is much deeper into the local-history tail than the two-departure history at which wrong-sign posterior derivatives first become possible in highly heterogeneous laws. It does not prove speed monotonicity for `{2,3}`; it shows that, in this near-regular test family, the fresh-child first-return mechanism cannot be the obstruction until an extremely long local history.

## 7. What this rules in and out

The preceding run showed that the total revisit covariance can be positive, so a global sign argument for `E[B_T S_T]` is false. The present decomposition identifies one positive subchannel exactly:

- discovering a fresh child pushes the local parent-threshold posterior downward;
- a returned descendant excursion carries negative parameter score because child-to-parent return probability decreases with outward bias;
- their product creates positive covariance and therefore a negative contribution to the radial derivative.

However the same calculation also shows that this mechanism is quantitatively small in near-regular bounded-support families: it is proportional to posterior variance `V`, and the return-score elasticity is uniformly bounded by (3.9).

The new two-sided return elasticity also removes a previous asymmetry in the regeneration analysis. The earlier work knew returns could not decay *slower* than inverse bias. We now also know they cannot decay arbitrarily faster: on the odds scale the logarithmic elasticity lies between `1` and `beta d/(beta d-1)`.

## 8. Remaining obstruction and next attack

The remaining part of (2.2) is no longer an undifferentiated revisit problem. After this run it naturally splits into three channels:

1. **fresh-child first return** — now exactly priced by (4.5) and bounded by (5.2);
2. **already explored descendant excursion** — subtree history makes the continuation law posterior-dependent, so the fresh factorization used in (4.5) is unavailable;
3. **parent-side excursion and repeated-return stack** — this is the channel already connected to selected-ancestor/common-spine debt in earlier P03-B reports.

The next attack should build a non-overlapping excursion ledger in which every posterior innovation is charged only to the first subsequent revisit caused by its exit edge. The fresh-child entries can use (4.5) exactly; known-child entries should be decomposed into a quenched return derivative plus a subtree-posterior correction; parent exits should be matched to the existing common-spine occupation bound. If repeated-return overlap prevents such a unique ledger, the fallback is to produce an exact bounded-support finite cylinder proving that one innovation must necessarily be charged more than once, which would be a rigorous obstruction to this architecture and justify a pivot to the Bowditch–Tokushige covariance representation.

## 9. Obligation ledger

- `R_full`: full LPP outward-bias speed monotonicity on `(1/EZ,infinity)` — **OPEN / unchanged**.
- Exact source convention and no-leaf assumptions — **VERIFIED**.
- Strong later broad monotonicity range — **retained; not duplicated**.
- P03-A recursive analytic role — **preserved / not duplicated**.
- Revisit-only derivative decomposition — **inherited**.
- Child-to-parent return odds monotone — **inherited and strengthened**.
- Two-sided return-odds elasticity (3.8)–(3.10) — **PROVED PARTIAL, NEW**.
- Exact adverse fresh-child first-return charge (4.5) — **PROVED PARTIAL, NEW**.
- Uniform local-plus-fresh-first-return certificate (5.5)–(5.6) — **PROVED PARTIAL, NEW**.
- `{2,3}`, `beta=3/5`, all `j<=97` component certificate — **PROVED RESTRICTED**.
- Already-explored descendant and parent-side repeated-return transport — **OPEN**.

No simulation is used as proof. No public posting, email, Drive delivery, force-push, or peer/historical overwrite is performed.