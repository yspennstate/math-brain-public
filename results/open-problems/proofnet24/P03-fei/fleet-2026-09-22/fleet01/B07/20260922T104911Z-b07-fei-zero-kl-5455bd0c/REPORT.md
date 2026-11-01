# fleet01/B07 — biased zero-KL equality: exact one-point-defect and arity-two families

**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** `FEI-20260922-fleet01-B07` — Biased zero-KL classification  
**Run:** `20260922T104911Z-b07-fei-zero-kl-5455bd0c`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / BIASED_CHARACTER-TIMES-BENT_EXTENSION_REFUTED`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source state

The assignment asks for a classification of genuine biased Boolean gates whose normalized nonempty spectral law equals its occurrence I-projection. The exact I-projection source used here is:

- `IPROJ`: yspennstate/math-open-problems commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`.

For a nonconstant biased Boolean gate, let `P=w^+` be the normalized nonempty squared Fourier law, let
\[
r_i=P(i\in S),
\]
and let \(Q_r\) be the unique maximum-entropy law on nonempty subsets with those occurrence marginals. The source proves
\[
K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P)\ge 0
\]
and
\[
R_\Gamma=B_{\inf}^{\Gamma}+K_{\rm occ}.
\]
Thus `K_occ=0` is exactly the equality problem `P=Q_r`.

The named OTHER-account theorem applied is:

- `EQUALITY`, fleet03/B15, candidate `B-PRODUCT-EQUALITY-RIGIDITY-v1`, commit `84c69136ca6b008badb76f15bf1071d029c927aa`, `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B15/20260922T085625Z-product-equality-rigidity/REPORT.md`.

It proves on the **balanced uniform** slice that `K_occ=0` is equivalent to a character times a bent function (after irrelevant coordinates). Its proof uses a balanced convolution parity obstruction to force the I-projection conditioning parameter to one, followed by the physical uniform Walsh integer lattice. The present assignment explicitly forbids transferring that lattice argument to irrational biased measures.

At the final source refresh used for this report, the designated partner `fleet02/B07` had no completed run in the current `fleet-2026-09-22/fleet02` scientific root. I therefore did not invent or attribute a partner result. The completed fleet03/B15 theorem above is the named other-account result actually used.

The mandatory recursive-majority low-level barrier is respected: no truncation by Fourier level, finite labelled cutoff, or merged tail is used anywhere below. The result is an exact full-law equality statement.

## 2. First new theorem: all two-input laws are automatically zero-KL

### Theorem 2.1 — `B-ZEROKL-ARITY2-SATURATION-v1`

Let \(P\) be **any** probability law on the three nonempty subsets
\[
\{1\},\quad \{2\},\quad \{1,2\}.
\]
Then \(P\) is uniquely determined by its occurrence marginals \(r_1,r_2\). Consequently \(P=Q_r\) and
\[
\boxed{K_{\rm occ}(P)=0.}
\]

In particular, for every nonconstant two-input Boolean gate at every interior product bias,
\[
\boxed{K_{\rm occ}(G;p)=0.}
\]

### Proof

Write
\[
x=P(\{1\}),\qquad y=P(\{2\}),\qquad z=P(\{1,2\}).
\]
Then
\[
r_1=x+z,\qquad r_2=y+z,\qquad x+y+z=1.
\]
Solving,
\[
\boxed{
z=r_1+r_2-1,\qquad x=1-r_2,\qquad y=1-r_1.
}
\]
Hence the feasible set of laws on nonempty subsets with marginals \(r\) is a singleton. The maximum-entropy member \(Q_r\) is therefore \(P\) itself. Thus \(D(P\Vert Q_r)=0\). Applying this to the normalized nonempty spectral law of any nonconstant two-input Boolean gate proves the final assertion. \(\square\)

### Consequence

For arity two, the canonical post-influence dependence credit is identically zero. Therefore any universal gate potential must pay every two-input gate entirely through its influence/Bellman term \(B_{\inf}^{\Gamma}\). No lower bound on `K_occ` can help there.

This also shows immediately that exact zero-KL is much less rigid away from the balanced uniform setting than the fleet03/B15 theorem might suggest if its hypotheses were forgotten.

## 3. Main new theorem: every one-point-defect Boolean gate has exact zero-KL at every bias

Fix independent Boolean coordinates \(X_1,\ldots,X_n\) under an arbitrary **interior** product measure. Fix an atom
\[
\xi=(\xi_1,\ldots,\xi_n)\in\{-1,1\}^n
\]
and put
\[
q_i=\Pr[X_i=\xi_i]\in(0,1),\qquad
a=\Pr[X=\xi]=\prod_{i=1}^n q_i.
\]
For \(s\in\{-1,1\}\), define the genuine Boolean gate
\[
\boxed{
f_{\xi,s}(x)=s\bigl(1-2\,\mathbf 1_{\{x=\xi\}}\bigr).
}
\]
Up to input literal flips and output sign, this is an arbitrary-arity AND/OR clause: it differs from a constant at exactly one truth-table atom.

### Theorem 3.1 — `B-ZEROKL-POINT-DEFECT-EXACT-v1`

For every \(n\ge1\), every interior product bias, every distinguished atom \(\xi\), and either output sign,
\[
\boxed{
K_{\rm occ}(f_{\xi,s};p)=0.
}
\]
More precisely, its normalized nonempty squared spectral law is exactly the law of independent Bernoulli variables
\[
B_i\sim{\rm Bernoulli}(1-q_i)
\]
conditioned on \(B\ne0\).

### Proof

Use the atom-aligned normalized coordinate
\[
\psi_i(X_i)=
\frac{\mathbf 1_{\{X_i=\xi_i\}}-q_i}
     {\sqrt{q_i(1-q_i)}}.
\]
This differs only by a sign from the standard normalized biased Fourier coordinate, so squared Fourier coefficients are unchanged. The atom indicator has the exact product expansion
\[
\mathbf 1_{\{X=\xi\}}
=
\prod_{i=1}^n
\left(q_i+\sqrt{q_i(1-q_i)}\,\psi_i\right).
\]
Therefore the empty Fourier coefficient of \(f_{\xi,s}\) is
\[
\widehat f(\varnothing)=s(1-2a),
\]
and for every nonempty \(S\subseteq[n]\),
\[
\widehat f(S)
=
-2sa\prod_{i\in S}\sqrt{\frac{1-q_i}{q_i}}.
\]
Hence
\[
\boxed{
|\widehat f(S)|^2
=
4a^2\prod_{i\in S}\frac{1-q_i}{q_i},
\qquad S\ne\varnothing.
}
\tag{3.1}
\]

Since \(f\) is Boolean,
\[
v:=1-\widehat f(\varnothing)^2
=1-(1-2a)^2
=4a(1-a).
\]
Thus the normalized nonempty spectral law is
\[
\boxed{
w^+(S)
=
\frac{|\widehat f(S)|^2}{v}
=
\frac{a}{1-a}
\prod_{i\in S}\frac{1-q_i}{q_i}.
}
\tag{3.2}
\]

Now let \(B_i\) be independent Bernoulli variables with
\[
t_i:=\Pr[B_i=1]=1-q_i.
\]
For a subset \(S\subseteq[n]\),
\[
\Pr[\{i:B_i=1\}=S]
=
\prod_{i\in S}(1-q_i)\prod_{j\notin S}q_j
=
a\prod_{i\in S}\frac{1-q_i}{q_i}.
\]
Moreover
\[
\Pr[B=0]=\prod_i q_i=a,\qquad
c:=\Pr[B\ne0]=1-a.
\]
Conditioning on \(B\ne0\) gives precisely (3.2):
\[
\Pr[\{i:B_i=1\}=S\mid B\ne0]
=
\frac{a}{1-a}\prod_{i\in S}\frac{1-q_i}{q_i}
=w^+(S).
\]

Its occurrence marginals are
\[
\boxed{
r_i=\Pr[B_i=1\mid B\ne0]
=\frac{1-q_i}{1-a}.
}
\tag{3.3}
\]
Consequently
\[
c\,r_i=1-q_i=t_i
\]
and the defining I-projection equation from `IPROJ` is satisfied identically:
\[
1-c=a=\prod_i q_i
=\prod_i(1-c r_i).
\]
By uniqueness of the occurrence I-projection,
\[
w^+=Q_r,
\]
and therefore
\[
K_{\rm occ}=D_{\rm KL,2}(w^+\Vert Q_r)=0.
\]
\(\square\)

### Explicit entropy identity

The same computation yields
\[
\boxed{
H(w^+)
=
H_{\max}(r)
=
\frac{\sum_i h_2(q_i)-h_2(a)}{1-a}.
}
\tag{3.4}
\]
Thus this is exact equality, not merely a small-KL or limiting construction.

## 4. Why this genuinely refutes the naive biased character-times-bent extension

The fleet03/B15 theorem is correct at its stated balanced-uniform scope. But its structural conclusion cannot be extended verbatim to general product biases.

For \(n\ge3\), choose for example
\[
f(x)=1-2\mathbf 1_{\{x=(1,\ldots,1)\}}
\]
under any interior nonuniform product bias. Theorem 3.1 gives \(K_{\rm occ}=0\). Yet this truth table has one exceptional atom and is not of the balanced-uniform `character times bent on disjoint coordinates` form: under the uniform measure its mean is
\[
1-2^{1-n}\ne0,
\]
whereas the fleet03/B15 structural family has a nonempty character factor and is balanced.

Therefore the guessed unrestricted extension
\[
K_{\rm occ}=0
\quad\Longrightarrow\quad
\text{character-times-bent structure}
\]
is false without additional hypotheses.

This does **not** contradict fleet03/B15, because balancedness was essential in its first convolution step. It also explains where that proof fails off-center: once the empty Fourier coefficient is nonzero, the top convolution equation gains the empty/full pair and the odd-sign contradiction used to force \(c=1\) no longer applies.

## 5. Companion exact family: biased characters are also zero-KL

Let
\[
f(x)=s\prod_{i\in F}\ell_i(x_i)
\]
be any nonconstant product of literals, with \(\ell_i(x_i)=\pm x_i\). Put
\[
m_i=\mathbb E[\ell_i(X_i)],\qquad
\sigma_i^2=1-m_i^2.
\]
In the normalized biased basis,
\[
\ell_i=m_i+\sigma_i\phi_i,
\]
so the **full** squared spectral law of \(f\) is a product Bernoulli law with inclusion parameters
\[
t_i=\sigma_i^2.
\]
Conditioning that product law on the Fourier set being nonempty is exactly its occurrence I-projection. Therefore
\[
\boxed{K_{\rm occ}(f;p)=0.}
\]
This is the natural biased continuation of the character branch. The one-point-defect theorem is a genuinely different branch.

## 6. Conditional end-to-end implication for Path B

`IPROJ` gives the exact identity
\[
R_\Gamma=B_{\inf}^{\Gamma}+K_{\rm occ}.
\]
Therefore an all-gate proof may close if every source with \(B_{\inf}^{\Gamma}<0\) is forced to pay
\[
K_{\rm occ}\ge -B_{\inf}^{\Gamma}.
\]

The balanced-uniform equality theorem shows that one zero-KL boundary is structurally harmless there. The new theorems show that the biased zero-KL boundary is much larger:

1. **all two-input gates** lie on it;
2. **all arbitrary-arity one-point-defect clauses** lie on it;
3. **all biased characters** lie on it.

Hence no Path-B proof can use a blanket positive lower bound on `K_occ` away from characters. On these exact equality families the whole gate inequality must be paid by \(B_{\inf}^{\Gamma}\) and/or by exact composition/child slack.

This is consistent with the current recursive-majority barrier: the present proof never compresses the spectrum by degree and never claims a finite low-level KL payment.

## 7. First surviving missing implication

The equality problem should now be split into a **decomposable equality bank** and a genuinely prime remainder.

A source-valid next statement is:

> **`B-ZEROKL-PRIME-RIGIDITY-v1` (OPEN).**  
> For an essential composition-prime Boolean gate of arity at least three at an interior product bias, classify the solutions of \(w^+=Q_r\). Determine whether, away from explicit algebraic symmetry loci in the bias vector, such a gate can exist at all.

The one-point-defect family does not obstruct that sharpened target because for arity at least three it is a nested AND/OR-of-literals construction. The arity-two saturation theorem says that arity two must be treated as a base gate rather than by dependence KL.

A second immediate obligation for a proposed universal potential is:

> Prove \(B_{\inf}^{\Gamma}\ge0\) on the exact zero-KL base families above (or pay the same family by a source-valid composition identity). Since \(K_{\rm occ}=0\) there, no dependence-credit argument can repair a negative \(B_{\inf}^{\Gamma}\).

These are strictly sharper obligations than the rejected unrestricted character-times-bent extension.

## 8. Scope and status

- Theorems 2.1, 3.1, and the biased-character observation are analytic and dimension-independent.
- Theorem 3.1 is a concrete biased Boolean family satisfying the assignment's falsification criterion for the guessed unrestricted character-times-bent extension.
- No finite scan or numerical approximation is used in the proof.
- No claim is made that all biased zero-KL gates have now been classified.
- No claim is made that FEI is solved.
- No fixed potential, obsolete quadratic repair, low-level KL compression, or unweighted convolution-L2 estimate is used.
- No native brain retrieval was available or consumed; execution remains `WITHOUT_VERIFIED_BRAIN`.
