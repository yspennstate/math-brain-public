Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not authenticated as GPT-6 at maximum.

# NM13-02 T01 — derivative-spectral-flat selectors and a uniform hereditary theorem for balanced connected high-degree cores

## 0. Parent scope/bound versus demonstrated mechanism gain

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove one finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean function on every finite uniform cube.

**Parent scope/bound before -> after:** **OPEN -> OPEN**. The unrestricted universal finite upper bound remains **UNKNOWN -> UNKNOWN**. Nothing below promotes a restricted stopping class or finite checker to full FEI.

**Mechanism gain.** P03's newest proof has reduced its remaining source-level difficulty to a universal restriction-stable certificate for one connected degree-`>=3` ANF interaction core under arbitrary quadratic twist. This run proves a new local selector principle that is automatically robust to *every quadratic twist*: a coordinate whose physical derivative phase has Fourier `L_infinity` norm at most `eta<1` has folded queried influence at least `(1-eta)/2`, even after an arbitrary quadratic phase is added. The selector's hereditary allocation can therefore be paid entirely by its queried influence, with no minor-child or descendant-influence surcharge.

Applying that principle to a recursively **quadratically guarded** selector construction gives, for a single connected high-degree core of arbitrarily large degree, depth and balanced branching,

\[
\boxed{\mathcal A((-1)^{P+q})\le 8-3\log_2 3
=3.245112497836531\ldots}
\]

for every quadratic `q`, where `A` is the infimum hereditary-allocation ratio over full physical restriction trees. The same prescribed tree also gives the direct restricted FEI theorem

\[
\boxed{
H(\widehat{(-1)^{P+q}}^{\,2})
\le
\left(8-3\log_2 3+\frac2{\ln2}\right)I((-1)^{P+q})
}
\]

with constant `6.130502579614458...`.

The balanced depth-`d` guarded core has `2^d` quadratic stopping leaves, degree exactly `d+2`, and one connected high-degree ANF interaction component. The earlier generic hybrid decision-tree certificate grew like `1.290076...+d` on this balanced shape; the new derivative-spectral selector keeps the constant fixed. This is the concrete application to P03's current connected-core obstruction.

The theorem is **not** a universal restriction-stable core certificate in P03's stronger sense: arbitrary external restrictions can fix away a guard pair before its selector is queried. That limitation is stated precisely in Section 8.

## 1. Current directive, exact dependencies, and compact handoff

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory, complementary to P03. The policy requires substantive derivation first and explicitly forbids treating restricted results as full FEI.

Newest P03 substantive report actually recovered before this derivation:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T11-28-37+0300__fei-certified-core-max-splicing.md`, blob `af89172d17d120ae1fdaad52674bd6e452f77099`.

Its exact remaining obstruction is:

> prove a universal restriction-stable hereditary/direct certificate for a **single connected degree-`>=3` ANF interaction core under arbitrary quadratic twist**, or construct a connected-core family forcing every proposed certificate to diverge.

P03's new certificate-valued max-splicing removes the cross-component quadratic recombination cost once each connected core already has such a certificate. This report does **not** take ownership of that theorem and does not need it for the new connected-core class below.

Current P03 entrypoint: `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`. It still records full FEI as OPEN and preserves the following corrections: the pointwise erasure shortcut is false; the fixed-coefficient affine-drift route is retired; Han's all-coordinate absolute-overlap selector is false; the old resolvent/interpolation target is retired; fresh-control results require their added independent controls and do not imply fixed-domain full FEI. None is revived here.

Newest preceding NM13-02 report:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T11-38-54+0300__variance-paid-separator-connected-core.md`, blob `55d23e2c39c335d280c9b40d7f1dcc885f50a92d`.

Compact preserved handoff:

- quadratic phases have an exact polar-rank hereditary telescope and hereditary constant at most `1`;
- queried influence plus weighted residual-leaf influence is exactly root influence;
- character-child, one-defect, descendant-influence, variance-minor and hybrid decision-tree payments remain valid in their stated scopes;
- the quadratic-normalized Wiener theorem and the one-/two-flat theorems remain restricted results, not full FEI;
- the preceding run showed root quadratic-normalized Wiener width can be exponentially large on a one-separator connected cubic core while hereditary allocation stays bounded, so paying a connected core by one root scalar is too crude.

The present route is materially different from another variance/minor-child amortization: it pays a separator directly from a **Fourier min-entropy property of its physical derivative**, robust under the arbitrary quadratic twist that P03's obstruction explicitly retains.

## 2. Primary-source status and bounded literature check

Fresh checks on 20 September 2026:

1. María José González, Paul MacManus, María Cristina Pereyra, `arXiv:2606.00246`, submitted 29 May 2026 and updated 2 June 2026. Its abstract still states FEI as a conjecture; its stopping-tree inequality would imply full FEI *if it held for all Boolean functions*, and the paper proves restricted classes rather than a universal result.
2. Peijie Li and Guangyue Han, `arXiv:2512.03117`, submitted 2 December 2025. Their strengthened general inequality still has the profile term `sum_i I_i log(1/I_i)` (with sharp coefficients in their normalization), not a universal `C I(f)` theorem.
3. Xiao Han's published Combinatorica theorem likewise gives `O(I + sum_i I_i log(1/I_i))`, not full FEI.
4. O'Donnell--Tan's composition theorem, `arXiv:1304.1347`, and the published read-once-formula literature were checked because the construction below has a tree flavor. Those results concern composition/read-once formula classes; the present statement keeps an **arbitrary global quadratic twist** and derives its local payment from derivative spectral flatness. The bounded search did not return a matching derivative-`L_infinity` guarded-selector theorem. This is only bounded negative evidence; publication priority is **UNVERIFIED**.

Thus current primary-source status remains OPEN; no reported project proof is assumed to settle it.

## 3. Notation and two exact tree identities

Work on `F_2^n`, with Walsh characters `chi_S(x)=(-1)^{S dot x}`. For Boolean `f`, write `Z` for its squared Fourier sample:

\[
\Pr[Z=S]=\widehat f(S)^2.
\]

At a physical coordinate `i`, let `f^0,f^1` be the two restrictions and define

\[
B_i(f):=H(Z_i\mid Z_{-i}),
\qquad
\alpha_i(f):=\operatorname{Inf}_i(f),
\qquad
j_i(f):=\min\{\alpha_i(f),1-\alpha_i(f)\}.
\]

For any full adaptive physical restriction tree `T`, with node weights `w_v`, define its hereditary allocation

\[
R_T(f):=\sum_{v\text{ internal}}w_v B_{i(v)}(f_v).
\]

The exact one-step influence identity is

\[
I(f)=\alpha_i(f)+\frac{I(f^0)+I(f^1)}2.
\tag{3.1}
\]

Iterating (3.1) down any partial tree gives

\[
\boxed{Q_T+L_T=I(f),}
\tag{3.2}
\]

where `Q_T=sum_v w_v alpha_{i(v)}(f_v)` is queried influence and `L_T=sum_leaf w_leaf I(f_leaf)` is residual leaf influence.

Also

\[
B_i(f)\le H(Z_i)=h_2(\alpha_i)=h_2(j_i).
\tag{3.3}
\]

For `0<t<=1/2`,

\[
\frac{d}{dt}\frac{h_2(t)}t
=\frac{\log_2(1-t)}{t^2}<0,
\tag{3.4}
\]

so `h_2(t)/t` is decreasing.

## 4. New local theorem: derivative spectral flatness survives every quadratic twist

Let `P` be any `F_2` polynomial in a set of **core variables** `U`, and let `i in U`. Define the untwisted derivative phase on `U\{i}` by

\[
d_i^P(x):=(-1)^{\partial_iP(x)}.
\]

Auxiliary variables, disjoint from `U`, are allowed below.

### Theorem 4.1 — quadratic-twist robust spectral-flat selector

Assume

\[
\|\widehat{d_i^P}\|_\infty\le\eta<1.
\tag{4.1}
\]

Let `q` be **any quadratic polynomial** on all remaining core and auxiliary variables together with `i`, and put

\[
f=(-1)^{P+q}.
\]

Then, with

\[
\varepsilon:=\frac{1-\eta}{2},
\]

one has

\[
\boxed{j_i(f)\ge\varepsilon.}
\tag{4.2}
\]

Consequently

\[
\boxed{
B_i(f)\le c(\eta)\,\operatorname{Inf}_i(f),
\qquad
c(\eta):=\frac{h_2(\varepsilon)}{\varepsilon}.
}
\tag{4.3}
\]

#### Proof

The multiplicative physical derivative is

\[
D_if(x)=f(x^{i=0})f(x^{i=1})
=(-1)^{\partial_iP(x)+\partial_iq(x)}.
\]

Because `q` is quadratic, `partial_i q` is affine. Thus multiplication by `(-1)^{partial_i q}` is an affine character times a global sign. If that affine character uses an auxiliary variable on which `P` is independent, then `E D_i f=0`. Otherwise `E D_if`, up to sign, is one Fourier coefficient of `d_i^P`. In every case

\[
|\mathbb E D_if|\le\eta.
\tag{4.4}
\]

Since `D_if=-1` exactly on the queried disagreement set,

\[
\alpha_i(f)=\frac{1-\mathbb E D_if}{2},
\qquad
j_i(f)=\frac{1-|\mathbb E D_if|}{2}\ge\frac{1-\eta}{2}=\varepsilon.
\]

By (3.3), symmetry of `h_2`, monotonicity (3.4), and `j_i<=alpha_i`,

\[
B_i(f)
\le h_2(j_i)
\le \frac{h_2(\varepsilon)}\varepsilon j_i
\le c(\eta)\alpha_i(f).
\]

QED.

### Why this differs from the older degree scalar

A degree bound controls a derivative's support only through Reed--Muller minimum weight and deteriorates when degree grows. Theorem 4.1 instead asks for a **spectral max bound on the derivative phase**. That can stay uniformly below one even when the original core degree tends to infinity. It is also exactly adapted to P03's arbitrary quadratic twist: the twist contributes only an affine character to the derivative and therefore merely selects/translates a Fourier coefficient.

## 5. General hereditary selector-tree theorem

Call a rooted physical selector tree for a core polynomial `P` **eta-flat to quadratic leaves** if at every internal core node `v`, with current core polynomial `P_v` and prescribed selector `i(v)`,

\[
\|\widehat{(-1)^{\partial_{i(v)}P_v}}\|_\infty\le\eta,
\tag{5.1}
\]

and after following either physical child, the remaining nonquadratic core is the corresponding child core modulo an arbitrary quadratic polynomial. At every stopping leaf, the remaining phase is quadratic (auxiliary variables are allowed).

### Theorem 5.1 — eta-flat hereditary allocation

For every such core `P`, every set of auxiliary variables, and every arbitrary quadratic `q` coupling all variables,

\[
\boxed{
\mathcal A((-1)^{P+q})\le
\max\left\{1,\frac{h_2((1-\eta)/2)}{(1-\eta)/2}\right\}.
}
\tag{5.2}
\]

#### Proof

Run the prescribed selector tree. Theorem 4.1 pays every internal selector by `c(eta)` times that node's queried influence. At a quadratic stopping leaf, use the prior quadratic rank telescope: if the leaf quadratic polar rank is `r`, then every full physical completion has allocation `r/2`, while total influence is at least `r/2`; hence the quadratic leaf hereditary constant is at most one.

Graft those quadratic completions. By the exact budget (3.2),

\[
R_T(f)
\le c(\eta)Q_T+L_T
\le\max\{c(\eta),1\}(Q_T+L_T)
=\max\{c(\eta),1\}I(f).
\]

QED.

This is a paid dependent-branch theorem: both children may continue by completely different branch-dependent cores, but no additive depth or minor-child charge appears. The selector is paid once from the disjoint queried-influence budget.

## 6. Independent full-entropy decrement bound

The hereditary theorem above is self-contained and does not require P03's reported recombination theorem. For the concrete guarded class below it is also useful to record a self-contained direct FEI corollary.

For a split with child Fourier laws `P_0,P_1`, the exact entropy decrement is

\[
\Delta_iH(f):=H(f)-\frac{H(f^0)+H(f^1)}2
=B_i(f)+\operatorname{JS}(P_0,P_1),
\tag{6.1}
\]

where `JS` is Jensen--Shannon divergence in bits.

### Lemma 6.1 — recombination paid by folded queried influence

\[
\boxed{
\operatorname{JS}(P_0,P_1)
\le\frac2{\ln2}\,j_i(f).
}
\tag{6.2}
\]

#### Proof

For nonnegative scalars `p,q`, the natural-log scalar Jensen--Shannon contribution obeys

\[
\frac12\left[p\ln\frac{2p}{p+q}+q\ln\frac{2q}{p+q}\right]
\le\frac12(\sqrt p-\sqrt q)^2.
\tag{6.3}
\]

To check (6.3), normalize `p+q=2` and write `p=1+r,q=1-r`, `0<=r<=1`. The difference between the right and left sides has derivative

\[
\frac{2r}{\sqrt{1-r^2}}-\ln\frac{1+r}{1-r}.
\]

With `r=sin theta`, half of this is `tan theta-artanh(sin theta)>=0`, because both vanish at zero and

\[
\frac d{d\theta}\tan\theta=\sec^2\theta
\ge\sec\theta
=\frac d{d\theta}\operatorname{artanh}(\sin\theta).
\]

Thus (6.3) holds; symmetry handles negative `r`.

Apply (6.3) coordinatewise to `p=\widehat{f^0}(S)^2`, `q=\widehat{f^1}(S)^2`, and convert nats to bits:

\[
\operatorname{JS}(P_0,P_1)
\le\frac1{2\ln2}\sum_S\left(|\widehat{f^0}(S)|-|\widehat{f^1}(S)|\right)^2.
\]

The child spectral laws are unchanged if one child is multiplied by `-1`; choose that sign so the physical disagreement density is `j_i(f)`. Then

\[
\left||a|-|b|\right|\le|a-b|
\]

and Parseval gives

\[
\sum_S|\widehat{f^0}(S)-\widehat{f^1}(S)|^2=4j_i(f).
\]

This yields (6.2). QED.

Combining Theorem 4.1 and Lemma 6.1, every `eta`-flat selector satisfies

\[
\Delta_iH(f)
\le\left(c(\eta)+\frac2{\ln2}\right)\operatorname{Inf}_i(f).
\tag{6.4}
\]

Quadratic leaves satisfy the direct estimate `H<=2I`: their squared Fourier law is uniform on an affine flat of dimension equal to the polar rank `r`, so `H=r`, while `I>=r/2`.

Therefore the same tree telescope gives

\[
\boxed{
H(f)\le
\max\left\{2,c(\eta)+\frac2{\ln2}\right\}I(f).
}
\tag{6.5}
\]

This direct corollary is proved here; it is not conditional on later acceptance of a peer recombination report.

## 7. Application: quadratically guarded balanced connected cores

Define a recursive family of core polynomials. The two child variable sets are always disjoint, and every internal node receives three fresh variables `x,y,z`.

- A leaf core is `P=0`.
- Given child cores `P_0,P_1`, define
  \[
  \boxed{
  P=P_0+x\bigl(P_0+P_1+yz\bigr).
  }
  \tag{7.1}
  \]

The prescribed selector is `x`. Its restrictions are

\[
P|_{x=0}=P_0,
\qquad
P|_{x=1}=P_1+yz.
\tag{7.2}
\]

The extra `yz` on the `x=1` branch is quadratic and is absorbed into the arbitrary quadratic twist.

The selector derivative is

\[
\partial_xP=P_0+P_1+yz.
\tag{7.3}
\]

Because the three factors live on disjoint variable sets,

\[
(-1)^{\partial_xP}
=(-1)^{P_0}(-1)^{P_1}(-1)^{yz},
\]

and Fourier `L_infinity` tensorizes. The two-variable phase `(-1)^{yz}` has Walsh coefficients

\[
\left(\frac12,\frac12,\frac12,-\frac12\right),
\]

so

\[
\boxed{
\|\widehat{(-1)^{\partial_xP}}\|_\infty\le\frac12.
}
\tag{7.4}
\]

Thus every selector is `eta=1/2` flat, **uniformly under every arbitrary global quadratic twist**, even if that twist couples the selector, guard variables, descendant cores and any auxiliary variables.

Here

\[
\varepsilon=\frac14,
\qquad
c(1/2)=4h_2(1/4)=8-3\log_2 3
=3.245112497836531\ldots .
\]

### Theorem 7.1 — uniform hereditary allocation for guarded cores

For every recursively guarded core `P`, every auxiliary-variable set, and every quadratic `q` on all variables,

\[
\boxed{
\mathcal A((-1)^{P+q})
\le 8-3\log_2 3.
}
\tag{7.5}
\]

Moreover

\[
\boxed{
H(\widehat{(-1)^{P+q}}^{\,2})
\le
\left(8-3\log_2 3+\frac2{\ln2}\right)I((-1)^{P+q}),
}
\tag{7.6}
\]

where the direct constant is

\[
6.130502579614458\ldots .
\]

The proofs are Theorem 5.1 and (6.5) with `eta=1/2`.

### Balanced family and the precise P03 obstruction

Let `P_d` be the complete balanced guarded core of selector depth `d`.

For `d>=1`:

\[
\boxed{n_d=3(2^d-1),\qquad \deg P_d=d+2.}
\tag{7.7}
\]

Its stopping tree has exactly `2^d` quadratic leaves, with both children recursively nontrivial until the last level. Thus this is not the one-live-child/nested-canalizing spine handled by the earlier `<3` theorem.

Its degree-`>=3` ANF interaction hypergraph is a **single connected component**. At the root, every high-degree monomial of both child cores appears multiplied by the fresh selector `x`, and the cubic guard `xyz` connects the fresh guard variables to `x`; induction connects every descendant high-degree variable to the root selector.

Therefore `P_d` lies squarely inside P03's newest unresolved category: one connected high-degree interaction core under an arbitrary quadratic twist. Yet (7.5)--(7.6) give constants independent of `d`, ambient dimension, leaf count and quadratic rank.

This is a strict mechanism improvement over the earlier generic NM13-02 hybrid decision-tree certificate. That theorem gave for a tree with `L` quadratic leaves

\[
\kappa(T)\le C_\chi-\log_2 3+\log_2L.
\]

For the balanced guarded tree, `L=2^d`, so that generic certificate grows as

\[
1.290076274\ldots+d,
\]

whereas the new derivative-spectral payment is the fixed `3.2451124978...` for hereditary allocation. The gain comes exactly from paying each simultaneously-hard branching selector by its own queried influence rather than by averaging child certificates plus an additive unit.

This also explains why the theorem is not another root-Wiener surrogate: no root `Lambda_2` or `Omega_2` bound is used.

## 8. Failure mode and exact remaining gap

The new theorem does **not** yet supply P03's strongest desired object: a certificate for **every arbitrary physical restriction** of the connected core.

The reason is concrete. If an external restriction fixes one of a node's guard variables before its selector is queried, the factor `(-1)^{yz}` in (7.3) can collapse to a linear character or a constant. An adversarial quadratic twist can then cancel that affine contribution, so the uniform `1/2` derivative Fourier-max bound need not survive. The prescribed selector tree never performs such guard restrictions before the corresponding selector, which is why Theorem 7.1 is valid; arbitrary restriction stability is a strictly stronger requirement.

This failed strengthening is recorded rather than hidden. It is exactly where this run stops.

A promising next attack is a **redundant-guard amortization**: attach several disjoint rank-two quadratic guards to each selector and prove that destroying all currently usable guards by previous physical restrictions has already consumed enough queried influence to pay the loss, while at least one surviving guard keeps the derivative spectrum flat. That would move from a prescribed-tree certificate toward the all-restrictions certificate P03's max-splicing theorem wants.

## 9. Executed sanity checks

Checker:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T12-07-26+0300__check_guarded_derivative_selector.py`

Creation commit: `1aaa0a73345631330763ca3837711cd02168d30b`.

Archived output:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T12-07-26+0300__check_guarded_derivative_selector.json`

Creation commit: `7c4218a27433fcb45b6ea6dca01e61f36aa12c1e`.

Executed result: **PASS**.

The checker:

- verifies the exact guard Walsh magnitudes `(1/2,1/2,1/2,1/2)` up to signs;
- exhausts all `128` affine/quadratic twists of the depth-one guarded core (`n=3`), finding minimum folded selector influence exactly `1/4`, zero theorem violations, maximum observed `B_i/Inf_i = 2.672488983973203`, maximum observed full-decrement ratio `4.867668746754797`, and maximum full-tree `R/I = 1.5574963279910676`;
- samples `80` deterministic arbitrary quadratic twists of the balanced depth-two guarded core (`n=9`, seed `20260920`), visiting `240` guarded selector states, again finding minimum folded selector influence exactly `1/4`, zero violations, and maximum observed full-tree `R/I = 0.9368455622644648`.

These computations are sanity checks only. The all-dimensional result is the analytic proof above.

## 10. Ledger delta

```yaml
ledger_delta:
  task: NM13-02
  parent: T01_FEI
  parent_status_before: OPEN
  parent_status_after: OPEN
  parent_universal_bound_before: UNKNOWN
  parent_universal_bound_after: UNKNOWN
  mechanism_before: connected degree>=3 core under arbitrary quadratic twist lacked a branch-independent selector payment; balanced hard-child trees inherited growing generic decision-tree certificates
  mechanism_after: derivative Fourier-L_infinity selector theorem robust to arbitrary quadratic twists; balanced quadratically guarded connected cores have hereditary constant <= 8-3*log2(3) and direct FEI constant <= 8-3*log2(3)+2/ln(2)
  hereditary_constant_guarded: 3.245112497836531
  direct_constant_guarded: 6.130502579614458
  demonstrated_application: complete balanced guarded cores with n=3*(2^d-1), degree=d+2, 2^d quadratic leaves, one connected high-degree ANF component, arbitrary global quadratic twist
  previous_generic_certificate_on_application: 1.290076274... + d
  new_certificate_on_application: 3.245112497836531 independent of d
  exact_remaining_gap: arbitrary external restrictions may destroy a guard before its selector, so full restriction-stable connected-core certification is not yet proved
  failed_strengthening:
    - arbitrary-restriction stability of one rank-two guard
  preserved_false_or_restricted_routes:
    - fresh_control_fixed_domain_inference
    - pointwise_erasure_shortcut
    - fixed_affine_drift_payment
    - Han_absolute_overlap_selector
    - resolvent_interpolation
    - derivative_degree_scalar_as_universal_measure
    - blind_root_curvature_or_Wiener_payment
  checker_status: PASS
  next_attack: redundant rank-two guards with amortized payment for guards destroyed by earlier restrictions
```

**End of complete run report.**
