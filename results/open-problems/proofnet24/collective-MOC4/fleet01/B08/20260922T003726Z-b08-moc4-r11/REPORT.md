# MOC4 fleet01/B08 r11 — exact signed common-minor lift and the single Drury-facet obstruction

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira target  
**Worker:** fleet01/B08  
**Outcome:** `ESSENTIAL_STEP_APPLIED` — no full proof or disproof. The common-unitary compound-minor problem is put into one exact signed lift, and any target-level counterexample is shown to force a violation of one explicit left/right orbit of five-point inequalities. Such a violation in turn forces 40 strict permutation-score comparisons, including 30 distinct transposition-root half-plane inequalities.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and current team state

For normal `A,B in C^{4x4}` with spectra `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
D:=\det(A+B)\in\operatorname{conv}\left\{v_\sigma:=\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\tag{MOC4}
\]

This report includes singular and repeated spectra; no division by spectral gaps is used.

The strongest completed team reduction I consumed is fleet01/B07, `MOC4-MIXED-ASSIGNMENT-v1`: after `A=diag(a)` and `B=U diag(b) U^*`, the determinant support problem is reduced exactly to a mixed assignment inequality in the same unitary's one-minor transport `P=|U|^2` and complementary two-minor transport `R`. In particular B07 proves the signed middle-layer orientation variable is already a linear image of `P`; it is not an independent parity variable.

I also consumed the named OTHER-account result fleet04/B09, `MOC4-PR-JOINT-LIFT-v1` / r02 (`CANDIDATE_REFUTED + AUXILIARY_EXACT_STRUCTURE`): even the coarsened pair `(P,R)` need not belong to the convex hull of the 24 coupled permutation pairs. Its exact rational orthogonal certificate is

\[
P_{12}+P_{14}+2P_{24}+P_{31}+P_{34}-P_{41}-P_{42}-R_{23}+R_{31}
=-\frac{448}{15625}<0,
\]

while the same functional is nonnegative on every coupled permutation vertex. Therefore an unrestricted positive common permutation lift is unavailable and must not be silently reintroduced.

The assigned partner fleet02/B09 had entered the MOC4 workstream during this invocation, but no completed source-matching MOC4 report from that worker was yet available. Per the collective order I did not wait; the exact completed fleet04/B09 result above is the required other-account input.

## 2. Source-exact signed lift using the same unitary at every compound level

The correct common-unitary object is a **signed**, not automatically positive, law on `S_4`.

Let `U=(u_ij)` be any 4-by-4 unitary and define

\[
\omega_\sigma(U)
:=\frac{\operatorname{sgn}(\sigma)}{\det U}\prod_{i=1}^4 u_{i,\sigma(i)},
\qquad
r_\sigma(U):=\Re\omega_\sigma(U).
\tag{1}
\]

Multiplying `U` by a scalar unit phase does not change `U diag(b)U^*`, and (1) is invariant under that scalar normalization. Thus one may equivalently normalize `det U=1`.

### Lemma 2.1 — exact all-compound marginal identity

For every `S,T subset [4]` with `|S|=|T|`,

\[
\boxed{\sum_{\sigma:\sigma(S)=T}\omega_\sigma(U)
=|\det U[S,T]|^2.}
\tag{2}
\]

Consequently the same identity holds with `omega` replaced by `r`, and in particular

\[
\sum_\sigma r_\sigma=1.
\tag{3}
\]

**Proof.** The signed sum of permutation monomials with `sigma(S)=T` is exactly the Laplace term

\[
(-1)^{\Sigma S+\Sigma T}\det U[S,T]\det U[S^c,T^c].
\]

For a unitary, Jacobi complementarity gives

\[
\det U[S^c,T^c]
=(-1)^{\Sigma S+\Sigma T}\det(U)\,\overline{\det U[S,T]}.
\]

Divide by `det U`. This gives (2). The right side is real and nonnegative, so taking real parts gives the same marginal identity for `r`. For `S=T=emptyset`, (3) follows. ∎

This is exactly the “same unitary for every compound minor” compatibility requested by the assignment. The price is that the individual `r_sigma` need not be nonnegative. Fleet04/B09's exact obstruction proves that one cannot replace this by an unrestricted positive common law while retaining all needed marginal data.

### Lemma 2.2 — exact affine determinant representation

For arbitrary complex spectra, including zeros and repetitions,

\[
\boxed{D=\sum_{\sigma\in S_4} r_\sigma(U)v_\sigma.}
\tag{4}
\]

**Proof.** Expand each permutation product by the set `S` of indices from which the `b` term is chosen:

\[
v_\sigma
=\sum_{S\subseteq[4]}a_{S^c}b_{\sigma(S)}.
\]

Then use (2):

\[
\sum_\sigma r_\sigma v_\sigma
=\sum_S a_{S^c}\sum_{|T|=|S|}b_T
\sum_{\sigma:\sigma(S)=T}r_\sigma
=\sum_S a_{S^c}\sum_{|T|=|S|}b_T|\det U[S,T]|^2.
\]

The last expression is the usual principal-minor/Cauchy-Binet expansion of `det(diag(a)+U diag(b)U^*)`. ∎

This representation is classical in substance: Drury's 2004 proof of the n=4 external-vertices theorem uses the same signed coefficients (after `det U=1`) and cites the corresponding subset-minor identity. I rederived it here because it is exactly the compatibility point needed by the present team and because the positivity failure must remain explicit.

## 3. Drury's cone and an exact counterexample certificate

For equal-cardinality subsets `I,J` define the subset-event function

\[
P_{I,J}(\sigma)=\mathbf 1_{\{\sigma(I)=J\}}.
\]

Let

\[
\Gamma
=\operatorname{cone}\{P_{I,J}:|I|=|J|\}
\subset \mathbb R^{S_4}.
\tag{5}
\]

Drury calls their span the `Saxl_4` space; it has dimension 14. The real support-score function

\[
s(\sigma)=\Re(\eta v_\sigma),\qquad |\eta|=1,
\tag{6}
\]

belongs to this span, because the product expansion above is a linear combination of `P_{I,J}`. Put

\[
M=\max_{\sigma\in S_4}s(\sigma),\qquad d(\sigma)=M-s(\sigma)\ge0.
\tag{7}
\]

By (2), every generator of `Gamma` has nonnegative expectation under the signed common-unitary lift:

\[
\sum_\sigma r_\sigma P_{I,J}(\sigma)=|\det U[I,J]|^2\ge0.
\tag{8}
\]

Therefore, if `d in Gamma`, then

\[
M-\Re(\eta D)
=\sum_\sigma r_\sigma d(\sigma)\ge0.
\tag{9}
\]

So a genuine support violation `Re(eta D)>M` forces `d notin Gamma`.

Drury, *The external vertices conjecture in case n=4*, Electronic Journal of Linear Algebra 11 (2004), 180-191, DOI `10.13001/1081-3810.1131`, Proposition 4.1, gives the facets of `Gamma`. Besides the obvious coordinate inequalities `f(sigma)>=0`, there is exactly one nontrivial left/right orbit, represented by a functional `u`. One convenient form is

\[
\boxed{
3u(f)=f(3214)+f(4132)+f(3421)+f(2341)-f(3241).}
\tag{10}
\]

The other nine equal forms are listed in Section 5 of Drury's paper. Since the coordinate facets of `d` already hold by definition, (9) and Proposition 4.1 give the following exact necessary condition for any MOC4 counterexample.

### Proposition 3.1 — single-orbit counterexample condition

If MOC4 fails, then after relabeling the `a` and `b` spectra there is a support direction `eta` for which

\[
\boxed{u(s)>M.}
\tag{11}
\]

Equivalently, with deficits `d=M-s`,

\[
\boxed{d(3241)>
 d(3214)+d(4132)+d(3421)+d(2341).}
\tag{12}
\]

Thus the first essential missing implication in this mechanism is not another positive `(P,R)` lift. It is the **upper Drury-facet inequality**

\[
\boxed{u(\Re(\eta v))\le \max_{\sigma}\Re(\eta v_\sigma)}
\tag{UF}
\]

for every pair of four-point complex spectra and every support direction, up to the left/right relabeling orbit.

If `(UF)` held identically, then (7) would satisfy every facet inequality of `Gamma`, hence `d in Gamma`, and (9) would prove the complete n=4 Marcus-de Oliveira statement. I do **not** prove `(UF)` here.

This also explains exactly why Drury's 2004 result is weaker than full MOC4. His Theorem 1.1 proves the **lower/external** statement: when every OM vertex has real part at least 1, `Re(v)-1` lies in `Gamma`. Corollary 1.2 therefore controls half-spaces excluding zero, but does not supply the upper-deficit inequality `(UF)` for an arbitrary supporting line of the ordinary convex hull.

## 4. New finite consequence: a hypothetical violation forces a 40-edge strict order

The useful gain is that `(UF)` failure is far more rigid than an arbitrary support failure.

Drury lists ten equal formulas for `u` on `Saxl_4`:

1. `(3214,4132,3421,2341 ; 3241)`
2. `(3214,4132,2431,4321 ; 4231)`
3. `(3124,4132,3412,2341 ; 3142)`
4. `(3124,1432,4312,2341 ; 1342)`
5. `(2314,4123,3412,2431 ; 2413)`
6. `(3214,4123,4312,2431 ; 4213)`
7. `(2314,4123,1432,3421 ; 1423)`
8. `(2134,4123,3412,2341 ; 2143)`
9. `(3124,2314,1432,4321 ; 1324)`
10. `(2134,3214,1432,4321 ; 1234)`,

where `(p1,p2,p3,p4 ; n)` abbreviates

\[
3u(s)=s(p_1)+s(p_2)+s(p_3)+s(p_4)-s(n).
\tag{13}
\]

Suppose `u(s)>M`. In any one of these ten formulas, if some `s(p_j)<=s(n)`, then

\[
3u(s)\le \sum_{k\ne j}s(p_k)\le3M,
\]

contradiction. Therefore

\[
\boxed{s(p_j)>s(n)\quad(j=1,2,3,4)}
\tag{14}
\]

for **every one of the ten formulas**. Hence a putative upper-facet violation forces 40 strict permutation-score comparisons.

A direct finite check shows that 30 of these 40 comparisons are between permutations differing by one transposition, and all 30 such directed edges are distinct. For example the first expression forces

\[
s(3214)>s(3241),\quad s(3421)>s(3241),\quad s(2341)>s(3241),
\]

and each is a transposition comparison.

For a general transposition comparison, if `p` and `n` agree off rows `i,j` and

\[
p(i)=r,\quad p(j)=t,\qquad n(i)=t,\quad n(j)=r,
\]

then the product difference factors exactly as

\[
\boxed{
v_p-v_n
=(a_i-a_j)(b_t-b_r)
\prod_{k\ne i,j}(a_k+b_{p(k)}).}
\tag{15}
\]

Consequently any failure of `(UF)`, and therefore any MOC4 counterexample through Proposition 3.1, forces 30 distinct strict half-plane conditions

\[
\boxed{
\Re\!\left[
\eta (a_i-a_j)(b_t-b_r)
\prod_{k\ne i,j}(a_k+b_{p(k)})
\right]>0.}
\tag{16}
\]

This is now a finite multiplicative sign-realizability problem of the same general type as Drury's Section 6 angle argument, but with an **upper-support fan** rather than the 57 lower/external roots used in his proof.

The 30 transposition edges are:

`3241->3214, 3241->3421, 3241->2341;`
`4231->4132, 4231->2431, 4231->4321;`
`3142->3124, 3142->4132, 3142->3412;`
`1342->1432, 1342->4312, 1342->2341;`
`2413->2314, 2413->3412, 2413->2431;`
`4213->3214, 4213->4123, 4213->4312;`
`1423->4123, 1423->1432, 1423->3421;`
`2143->2134, 2143->4123, 2143->2341;`
`1324->3124, 1324->2314, 1324->4321;`
`1234->2134, 1234->3214, 1234->1432`.

Here `n->p` means the necessary strict inequality `s(p)>s(n)`.

The companion standard-library verifier checks exactly that the ten `u` formulas agree on every subset-event generator, that `u(1)=1`, that `u(P_{I,J})>=0`, and that the forced comparison list contains 40 edges with exactly 30 distinct transposition-neighbour edges.

## 5. Compact conditional end-to-end argument

The resulting route is now short and exact.

1. Diagonalize `A`, write `B=U diag(b)U^*`, and form the single signed real law `r_sigma(U)` in (1).
2. By Lemma 2.1, this **same** `r` reproduces every compound-minor marginal `|det U[S,T]|^2`; arbitrary independent bistochastic arrays never enter.
3. By Lemma 2.2, `D=sum r_sigma v_sigma` exactly.
4. In a support direction put `d=M-Re(eta v)`. If `d in Gamma`, all subset-event marginals of `r` are nonnegative, so `Re(eta D)<=M`.
5. Drury's exact n=4 facet theorem says that, because `d>=0` coordinatewise, the only remaining obstruction to `d in Gamma` is the one left/right orbit of `u` inequalities.
6. Therefore proving `(UF)` for every complex four-point spectra pair proves MOC4 in full, including singular and repeated spectra.
7. If `(UF)` fails, the ten equivalent `u` formulas force the 40 comparisons and 30 root inequalities above. The next decisive step is to test whether this 30-root upper fan is multiplicatively realizable. If it is impossible, `(UF)` and hence MOC4 follow. If it is realizable, one must next test whether an actual unitary signed lift can put negative mass on the corresponding deficit strongly enough to violate (9).

This mechanism is materially different from the prior local tangent expansion: it is global, finite, and source-exact. It also respects fleet04/B09's no-go result because it never asserts a positive spectrum-independent common permutation lift.

## 6. What is and is not proved

**Proved in this report:**

- the exact all-compound signed common-unitary lift (with proof);
- the exact affine determinant representation through those same 24 signed coefficients;
- using Drury Proposition 4.1, every MOC4 counterexample must produce an upper `u`-facet violation after relabeling;
- such a violation forces 40 strict score comparisons, 30 of them distinct transposition comparisons with the factorization (15).

**Not proved:**

- nonnegativity of the 24 signed weights (false in general / incompatible with the completed team no-go results);
- the upper-facet inequality `(UF)`;
- impossibility of the resulting 30-root fan;
- MOC4 itself.

**Parent target status:** OPEN / unresolved in this report.  
**Next mathematical step:** encode the 30 roots in argument variables and search for exact multiplicative relations/angle contradictions, using Drury's Section 6 method but replacing his lower/external 57-root system by the upper-support 30-root fan plus the six transposition inequalities at a unique maximizing permutation on the generic strict-support locus.

## 7. Provenance

Primary external source actually checked: S. W. Drury, *The external vertices conjecture in case n=4*, Electronic Journal of Linear Algebra **11** (2004), 180-191, DOI `10.13001/1081-3810.1131`. Relevant source points: Theorem 1.1 (EVC for n=4), Corollary 1.2, Proposition 4.1 (facet structure of `Gamma`), Section 5 (ten formulas for `u`), and the signed-minor identity used in the Corollary 1.2 proof.

Team dependencies actually consumed: fleet01/B07 `MOC4-MIXED-ASSIGNMENT-v1`; fleet04/B09 r02 `MOC4-PR-JOINT-LIFT-v1` refutation and structured-coefficient result; fleet03/B08 `MOC4-PERMUTATION-TANGENT-v1` only as a route-separation check (the present mechanism is deliberately not another tangent expansion).
