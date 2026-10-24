# MOC4 account04/B07 r11 — Spin(6) / Weyl normal form for the mixed-minor inequality

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira target  
**Worker:** account04/B07  
**Outcome:** `AUXILIARY_ONLY` — the current mixed-minor inequality is converted exactly into an orientation-sensitive quadratic maximization on `SO(6)`, its desired 24 endpoints are identified with the `D_3=A_3` Weyl group, every individual rank-one Cartan/plane-overlap sector is proved Weyl-extremal, and a tempting larger Birkhoff relaxation is refuted exactly. The simultaneous structured multi-sector inequality, hence MOC4, remains open.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Effective scope and peer state

Fresh owner control supersedes this slot's earlier benchmark role and assigns B07 to MOC4. The source-exact target is

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\]

for all complex normal `4 x 4` matrices `A,B`, including singular and repeated-spectrum cases.

The exact account04/B07 assignment is: **attempt a representation-theoretic or exterior-algebra proof of the shared mixed-minor constraint rather than a stronger untested positivity claim.** The named partner is account01/B08. At the last bounded archive check in this run, account01's MOC4 root contained B07 and B09 but no completed B08 artifact, so I did not wait.

I directly consumed two completed other-account snapshots:

1. **account01/B07, `20260922T000420Z-b07-moc4-r1`**, report blob `182e1f1b24a290b1a25d1bc0677b6b031e0c088d`. It proves the exact identity
   \[
   d_{\alpha\beta}=\frac14h_\alpha^TPh_\beta,
   \]
   absorbs the signed middle-layer orientation term into the same one-minor matrix `P=|U|^2`, and reduces full MOC4 support to the structured mixed assignment inequality `(MI)` below.
2. **account03/B09, `20260921T235010Z-b09-moc4-r01`**, report blob `94dc51181d3dbe98c2df07da7f3370c3787e270a`. It supplies the complementary-pair variables `(R,D)` and the exact `k=2` layer decomposition. Its earlier parity relaxation is superseded by the account01/B07 exact `D(P)` identity, but its complement-block coordinates remain useful.

No target-level proof or counterexample is inherited from those reports.

## 2. The exact mixed assignment problem being attacked

Use the three oriented complementary pair classes

\[
S_1=12,\qquad S_2=13,\qquad S_3=14,
\]

with complements `34,24,23`. Let

\[
q_{S,T}=|\det U[S,T]|^2,
\]

\[
r_{\alpha\beta}=q_{S_\alpha,T_\beta}+q_{S_\alpha,T_\beta^c},\qquad
 d_{\alpha\beta}=q_{S_\alpha,T_\beta}-q_{S_\alpha,T_\beta^c}.
\]

Write `R=(r_{alpha beta})`, `D=(d_{alpha beta})`, and `P=(|u_ij|^2)`. For the normalized Walsh-Hadamard matrix

\[
H=\frac12\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\]

the account01/B07 identity is

\[
HPH^T=\begin{pmatrix}1&0\\0&D\end{pmatrix}.\tag{1}
\]

For a support direction `|eta|=1`, define the peer's real arrays `C in R^{4x4}` and `X in R^{3x3}` so that

\[
\Re(\eta\det(A+UBU^*))
=C_0+\langle P,C\rangle+\frac12\langle R,X\rangle.\tag{2}
\]

For a permutation `sigma in S_4`, with induced permutation `rho_sigma` on the three complement classes, the corresponding endpoint is

\[
C_0+\sum_i C_{i,\sigma(i)}+rac12\sum_\alpha X_{\alpha,\rho_\sigma(\alpha)}.\tag{3}
\]

Thus the remaining exact obligation is

\[
\langle P,C\rangle+\frac12\langle R,X\rangle
\le
\max_{\sigma\in S_4}
\left(\sum_iC_{i,\sigma(i)}+\frac12\sum_\alpha X_{\alpha,\rho_\sigma(\alpha)}\right).
\tag{MI}
\]

## 3. Exterior-square real form: `SU(4)/{+/-I} = SO(6)`

Multiplying `U` by a scalar phase changes neither `P` nor any `q_{S,T}`, so assume `det U=1`.

On `Lambda^2 C^4`, let `tau` be the conjugate-linear Hodge-complement involution determined on the three representatives by

\[
\tau(e_{12})=e_{34},\qquad
\tau(e_{13})=-e_{24},\qquad
\tau(e_{14})=e_{23},
\tag{4}
\]

and the same relations backwards. Since `U in SU(4)` preserves the Hermitian form and volume, `Lambda^2 U` commutes with `tau`. Therefore it restricts to an orthogonal transformation

\[
O=(\Lambda^2U)|_{\operatorname{Fix}(\tau)}\in SO(6).\tag{5}
\]

This is not a proper hidden subset of `SO(6)`: the exterior-square homomorphism `SU(4)->SO(6)` has kernel `{+/-I}`; its derivative is an isomorphism `su(4) ~= so(6)` (both have dimension 15), so its compact connected image is all of `SO(6)`. This is the standard exceptional identification `Spin(6) ~= SU(4)`.

Split the real fixed space into the three oriented two-planes `E_1 + E_2 + E_3` coming from the complement pairs in (4), and write `O_{alpha beta}:E_beta->E_alpha` for the real `2 x 2` block.

### Lemma 1 — block invariants are exactly `(r,d)`

For every `alpha,beta`,

\[
\boxed{
 r_{\alpha\beta}=\frac12\|O_{\alpha\beta}\|_F^2,
 \qquad
 d_{\alpha\beta}=\det O_{\alpha\beta}.}
\tag{6}
\]

**Proof.** In the signed complement bases from (4), the relevant `2 x 2` complex block of `Lambda^2U` has form

\[
\begin{pmatrix}a&b\\ \bar b&\bar a\end{pmatrix},
\qquad
|a|^2=q_{S_\alpha,T_\beta},\quad
|b|^2=q_{S_\alpha,T_\beta^c}.
\]

On the `tau`-fixed real plane this acts by

\[
\begin{pmatrix}
\Re(a+b)&\Im(b-a)\\
\Im(a+b)&\Re(a-b)
\end{pmatrix}.
\]

Its Frobenius norm squared is `2(|a|^2+|b|^2)` and its determinant is `|a|^2-|b|^2`, proving (6). `square`

This gives a complete representation-theoretic meaning to both matrices used in `(MI)`.

## 4. Exact SO(6) quadratic normal form

Let

\[
\widetilde C=HCH^T,
\qquad G=(\widetilde C_{\alpha\beta})_{\alpha,\beta=1}^3,
\qquad g_0=\widetilde C_{00}.
\tag{7}
\]

By (1) and orthogonal invariance of the Frobenius pairing,

\[
\langle P,C\rangle=g_0+\langle D,G\rangle.
\tag{8}
\]

Combining (6) and (8), the left side of `(MI)` is **exactly**

\[
\boxed{
Q_{G,X}(O)=g_0+
\sum_{\alpha,\beta=1}^3
\left[
G_{\alpha\beta}\det O_{\alpha\beta}
+\frac{X_{\alpha\beta}}4\|O_{\alpha\beta}\|_F^2
\right],
\qquad O\in SO(6).}
\tag{9}
\]

No positivity relaxation, convex lift, or independent sign choice has been introduced.

For a permutation of the original four indices, its exterior-square realification is a block-monomial normalizer element. The 24 such elements form the Weyl group

\[
W(D_3)\cong W(A_3)\cong S_4.\tag{10}
\]

Therefore `(MI)` is equivalent to the orientation-sensitive Weyl extremum statement

\[
\boxed{Q_{G,X}(O)\le \max_{w\in W(D_3)}Q_{G,X}(w)}
\tag{SO6-W}
\]

for the **structured** coefficient pair `(G,X)` generated by spectra `a,b` and support direction `eta`.

This is the requested representation-theoretic reduction. It also identifies exactly why the 24 endpoint permutations, rather than all 48 complement symmetries, are the natural finite set: they are the Weyl group of the connected group `SO(6)`.

## 5. Cartan and plane-overlap interpretation

Let `J_2=[[0,-1],[1,0]]`. Embed `J_alpha` as `J_2` on `E_alpha` and zero elsewhere, and let `Pi_alpha` be the orthogonal projection onto `E_alpha`. Direct `2 x 2` block algebra gives

\[
\boxed{d_{\alpha\beta}
=-\frac12\operatorname{tr}\left(J_\alpha OJ_\beta O^T\right),}
\tag{11}
\]

\[
\boxed{r_{\alpha\beta}
=\frac12\operatorname{tr}\left(\Pi_\alpha O\Pi_\beta O^T\right).}
\tag{12}
\]

Thus `D` is the matrix of the **Cartan projection of the adjoint action** on the standard rank-three Cartan subalgebra of `so(6)`, while `R` is the matrix of overlaps between two decompositions into oriented two-planes.

This makes the peer results conceptually sharp:

- the determinant/orientation sector `D` is governed by type-`D_3` Weyl geometry;
- the unsigned plane-overlap sector `R` alone is only a `3 x 3` doubly stochastic transport;
- the unresolved content is that the **same** `O` generates both sectors, for the highly structured `(G,X)` coming from one pair of spectra.

## 6. A proved rank-one Weyl lemma

The representation form pays a real part of the residual rather than merely renaming it.

### Lemma 2 — every single Cartan rank-one sector is Weyl-extremal

For all real `g,h in R^3` and all `O in SO(6)`,

\[
g^TDh\le \max_{w\in W(D_3)} g^Twh.\tag{13}
\]

**Proof.** Set `J(g)=sum_alpha g_alpha J_alpha` and similarly `J(h)`. By (11),

\[
g^TDh=-\frac12\operatorname{tr}(J(g)OJ(h)O^T).
\]

This is a linear functional of the Cartan projection of the adjoint orbit of `J(h)`. Kostant convexity for the compact group `SO(6)` places that projection in the convex hull of the Weyl orbit `W(D_3)h`; maximizing the linear functional `g` yields (13). Equivalently, (13) is the canonical-form trace rearrangement for real skew-symmetric `6 x 6` matrices. `square`

### Lemma 3 — every single plane-overlap rank-one sector is Weyl-extremal

For all real `x,y in R^3`,

\[
x^TRy\le \max_{\rho\in S_3}x^T\rho y
=\max_{w\in W(D_3)}x^T\rho_wy.\tag{14}
\]

**Proof.** With `Pi(x)=sum_alpha x_alpha Pi_alpha`, equation (12) gives

\[
x^TRy=\frac12\operatorname{tr}(\Pi(x)O\Pi(y)O^T).
\]

The eigenvalues of `Pi(x)` are `x_1,x_1,x_2,x_2,x_3,x_3`, and likewise for `Pi(y)`. The real symmetric trace rearrangement inequality gives the first maximum in (14). Every permutation of the three planes has an orientation-preserving signed lift in `W(D_3)`, giving the second equality. `square`

So a single rank-one piece in either half of (9) cannot be the obstruction. The obstruction is **simultaneous Weyl synchronization of several dependent rank-one pieces**.

## 7. The spectral coefficient pair is a small sum of rank-one sectors

This synchronization statement can be made explicit. For a four-vector `z`, define

\[
\widehat z_\alpha=\frac12\sum_i h_\alpha(i)z_i,
\qquad
z_i^{(3)}=\prod_{k\ne i}z_k,
\qquad
\widehat{z^{(3)}}_\alpha=\frac12\sum_i h_\alpha(i)z_i^{(3)}.
\tag{15}
\]

Let

\[
A_\alpha^\pm=a_{S_\alpha^c}\pm a_{S_\alpha},
\qquad
B_\beta^\pm=b_{T_\beta}\pm b_{T_\beta^c},
\tag{16}
\]

with the same sign convention as the peer reduction. Then the structured coefficients satisfy the exact complex-outer-product formulas

\[
\boxed{X=\Re\left(\eta\, A^+(B^+)^T\right),}
\tag{17}
\]

\[
\boxed{
G=\Re\left(\eta\left[
\widehat{a^{(3)}}\,\widehat b^{\,T}
+\widehat a\,\widehat{b^{(3)}}^{\,T}
+\frac12 A^-(B^-)^T
\right]\right).}
\tag{18}
\]

Equation (18) follows by Walsh-transforming the `k=1,3` coefficient matrix and observing that the account01/B07 correction `Z` contributes exactly `Y/2` to the lower Hadamard block.

After splitting each complex outer product into real and imaginary parts, `(17)-(18)` express the entire residual as a sum of at most a small fixed number of real rank-one sectors, each individually covered by Lemma 2 or Lemma 3. A sufficient condition for `(SO6-W)` is therefore that those spectral sectors admit a **common** Weyl maximizer. The remaining problem is to prove that synchronization from the algebraic dependence among the vectors in (15)-(18), or to find a genuine allowed `SO(6)` obstruction.

This is strictly weaker than the already-refuted request for one permutation law reproducing all one- and two-minor marginals.

## 8. Exact elimination of a tempting Birkhoff proof route

A natural next temptation is to forget the connected `SO(6)` orientation constraint, place the six two-subsets in three complement pairs, use only that the squared-modulus compound matrix is doubly stochastic, and apply ordinary `S_6` Birkhoff. For the block-symmetric cost induced by `(9)`, one might hope the best `S_6` assignment is automatically one of the 24 `S_4=W(D_3)` lifts.

That hope is false even for exact integer real spectra.

For

\[
a=(4,5,-4,2),\qquad b=(2,5,-3,3),\qquad \eta=1,
\tag{19}
\]

the exact `Fraction` verifier in this run constructs the `6 x 6` assignment cost obtained from `(17)-(18)`. It finds

```text
S4_Weyl_size 24
complement_centralizer_size 48
best_S6 (Fraction(6491, 4), (5, 4, 0, 1, 2, 3))
best_centralizer48 (Fraction(6491, 4), (5, 4, 0, 1, 2, 3))
best_Weyl24 (Fraction(2801, 4), (3, 2, 0, 1, 5, 4))
relaxation_gap 1845/2
```

The maximizing relaxed assignment lies in the non-Weyl half of the 48-element complement centralizer. Hence a plain `6 x 6` Birkhoff argument loses exactly the orientation/Weyl information that the `Spin(6)` model preserves.

This is **not** a counterexample to MOC4: the verifier does not claim that the non-Weyl assignment is realizable by an allowed `O in SO(6)`. It is an exact counterexample only to that stronger proof relaxation.

## 9. Conditional end-to-end argument and first unpaid implication

A compact conditional proof is now:

1. diagonalize `A` and `B`, normalize `det U=1` without changing squared minors;
2. apply the exact determinant-layer expansion and the peer identity `HPH^T=diag(1,D)`;
3. pass through `Lambda^2 SU(4)=SO(6)` and Lemma 1 to obtain (9);
4. prove the structured Weyl extremum `(SO6-W)` for coefficient pairs satisfying (17)-(18);
5. evaluate the Weyl elements, which are exactly the 24 original permutation products, and apply support-function separation to obtain the desired convex-hull containment;
6. singular/repeated cases then follow directly where formulas are polynomial/continuous, with the already available repeated-spectrum boundary theorem as an independent check.

The **first essential unpaid implication** is step 4:

> **MOC4-SO6-WEYL-v1.** For every spectra `a,b in C^4`, every `|eta|=1`, and the corresponding `(G,X)` in (17)-(18), the quadratic functional (9) on `SO(6)` is maximized at a type-`D_3` Weyl element.

The next run should attack the simultaneous-rearrangement content of this statement, not the refuted arbitrary `S_6` relaxation and not a generic joint-convex-lift statement.

## 10. Status

`AUXILIARY_ONLY`. This run supplies an exact representation-theoretic normal form, two rigorous rank-one Weyl bounds, a small-rank spectral decomposition of the remaining coefficients, and an exact counterexample eliminating an over-relaxed Birkhoff route. It does **not** prove `(SO6-W)`, MOC4, or a new published theorem.

No benchmark gold, held-out answers, keys, credentials, scheduler identifiers, unrelated private data, email, Drive, public posting, paid model/API/Codex call, or remote workflow was used.
