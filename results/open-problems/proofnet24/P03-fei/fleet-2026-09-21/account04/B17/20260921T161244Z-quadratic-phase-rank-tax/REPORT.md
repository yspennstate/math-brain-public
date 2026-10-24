# B17 FEI creative run — quadratic-phase rank tax, an exact peeling class, and a sharp obstruction to a naive bridge

**Run:** `20260921T161244Z-B17-auto12`  
**Status:** **PARTIAL. Full uniform-cube Fourier entropy-influence remains OPEN / NOT PROVED.**  
**Brain label:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-side brain context was used.  
**Live role:** FEI new proof mechanisms.  
**Scientific source recovered before delivery:** `yspennstate/math-open-problems` master `89891aff5a122c7966aaafe8bf9929b70f538ba8`.  
**Creative moves:** FLEET_RULES #1 (change category: quadratic phases as block-unitary Fourier transforms), #4 (prove a weaker statement completely: a constant-4 nonlinear phase-peeling class), and #20 (find why the obvious bridge fails: an exact Boolean counterexample).

No publication-priority or novelty claim is made.

## 1. Named obstruction

The preceding B17 run proved exact tensor additivity of the affine/character-normalized influence
\[
J_{\rm aff}(f)=\min_{(v_1,\ldots,v_n)\ {\rm basis}}\sum_i
\frac{1-|\mathbb E_x f(x)f(x+v_i)|}{2},
\]
and therefore ruled out amplification by disjoint tensoring followed by arbitrary invertible-linear mixing and Walsh-character twisting.

That leaves the next natural possibility: **leave the affine/character gauge**. The smallest nonlinear phases with completely controlled Fourier geometry are quadratic phases
\[
Q(x)=(-1)^{q(x)}.
\]
This run asks whether multiplication by such a phase admits a quantitative "entropy tax versus influence descent" statement strong enough to peel nonlinear structure.

The answer is mixed:

1. there is a clean universal entropy tax depending only on the polar rank;
2. it yields a rigorous quadratic-peeling criterion;
3. it proves a nontrivial infinite Boolean class with constant \(4\) in the stronger \(H\le C J_{\rm aff}\) formulation;
4. but the tempting coefficient-2 bridge between entropy change and \(J_{\rm aff}\)-change is false, by an exact five-bit Boolean counterexample.

## 2. Quadratic phases act as small block-unitaries in Fourier space

Let \(q:\mathbb F_2^n\to\mathbb F_2\) be quadratic and define its polar form
\[
B_q(u,v)=q(u+v)+q(u)+q(v)+q(0).
\]
Let \(r=\operatorname{rank} B_q\). Since \(B_q\) is alternating, \(r\) is even. Put \(Q(x)=(-1)^{q(x)}\).

The normalized Walsh transform of \(Q\) is supported on one affine coset of
\[
V=\operatorname{Rad}(B_q)^\perp,
\qquad \dim V=r,
\]
and every nonzero Walsh coefficient has magnitude \(2^{-r/2}\).

### Theorem 2.1 — quadratic entropy rank tax

For every real \(L_2\)-normalized function \(f\), hence in particular for every Boolean \(f\),
\[
\boxed{\ |H(Qf)-H(f)|\le r.\ }
\]

**Proof.**
Multiplication by \(Q\) is an orthogonal operator in physical space. In Fourier space it is convolution by \(\widehat Q\). Since \(\widehat Q\) is supported on an affine coset \(a+V\), each frequency coset of \(V\) is mapped from exactly one frequency coset of \(V\), and no two cosets mix. The restriction of the convolution operator between the corresponding \(2^r\)-dimensional blocks is orthogonal, because the full operator is orthogonal.

Therefore the total squared Fourier mass of every coset is preserved, up to a permutation of the cosets. Decompose spectral entropy by first revealing the coset and then the location inside that coset. The coset entropy is unchanged. Inside a block of size \(2^r\), conditional entropy lies between \(0\) and \(r\). Averaging over the preserved block masses gives
\[
-r\le H(Qf)-H(f)\le r.
\]
This proves the claim. \(\square\)

The bound is sharp: for \(f\equiv1\) and a rank-\(r\) quadratic phase, \(H(f)=0\) while the spectrum of \(Q\) is flat on \(2^r\) points, so \(H(Q)=r\).

## 3. Exact influence formula after choosing the linear part

For a coordinate vector \(e_i\),
\[
(Qf)(x)(Qf)(x+e_i)
=
f(x)f(x+e_i)(-1)^{B_q(e_i,x)+q(e_i)+q(0)}.
\]
Adding a linear form \(\ell\) to \(q\) does not change \(B_q\), and the bits \(\ell(e_i)\) can be chosen independently. Consequently
\[
\boxed{
\min_{\ell\ {\rm linear}}
I((-1)^{q+\ell}f)
=
\sum_i
\frac{1-\left|\mathbb E_x
f(x)f(x+e_i)(-1)^{B_q(e_i,x)}
\right|}{2}.
}
\]
Thus, for a fixed polar form, the best linear correction is explicit: it folds each twisted derivative correlation separately.

This is a genuinely nonlinear analogue of the character folding that defined \(J_{\rm aff}\).

## 4. A rigorous quadratic peeling criterion

The preceding B17 affine-orbit result reformulates universal FEI equivalently as
\[
H(f)\le C J_{\rm aff}(f)
\quad\text{for all Boolean }f.
\]

Let \(g=Qf\), where \(Q\) has polar rank \(r\). Suppose \(g\) lies in a class already known to satisfy
\[
H(g)\le C J_{\rm aff}(g).
\]
If in addition
\[
\boxed{
J_{\rm aff}(f)-J_{\rm aff}(g)\ge \frac rC,
}
\]
then Theorem 2.1 gives
\[
H(f)\le H(g)+r
\le C J_{\rm aff}(g)+r
\le C J_{\rm aff}(f).
\]

So a quadratic phase can be peeled whenever the drop in optimized directional disagreement pays its polar rank at rate \(1/C\). The residual universal problem is to find a structural reason that such a profitable phase exists, or to identify a larger nonlinear gauge for which a comparable payment theorem holds.

## 5. Exact infinite class: quadratic phase times a one-point defect

Let \(N=2^n\), \(n\ge4\), and
\[
d_n(x)=1-2\,1_{\{x=0\}}.
\]
Let \(Q=(-1)^q\) be any quadratic phase with \(Q(0)=1\) and polar rank \(r\), and set
\[
F=Qd_n.
\]

For every nonzero translation \(v\), the defect derivative
\[
d_n(x)d_n(x+v)
\]
equals \(-1\) exactly at \(x=0,v\) and \(+1\) elsewhere.

If \(v\in\operatorname{Rad}(B_q)\), the quadratic derivative \(Q(x)Q(x+v)\) is constant, hence
\[
|c_F(v)|=1-\frac4N,
\qquad
j_F(v)=\frac2N.
\]

If \(v\notin\operatorname{Rad}(B_q)\), the quadratic derivative is a nontrivial character with zero mean. Because \(B_q(v,v)=0\), its values at \(0\) and \(v\) agree, so the two defect flips leave
\[
|c_F(v)|=\frac4N,
\qquad
j_F(v)=\frac12-\frac2N.
\]

The radical has dimension \(n-r\). Any basis contains at least \(r\) directions outside it, and this lower bound is attainable. Therefore
\[
\boxed{
J_{\rm aff}(Qd_n)
=
\frac r2+\frac{2(n-2r)}N.
}
\]
For the defect alone,
\[
J_{\rm aff}(d_n)=\frac{2n}{N},
\]
so
\[
\boxed{
J_{\rm aff}(Qd_n)-J_{\rm aff}(d_n)
=
r\left(\frac12-\frac4N\right).
}
\]
For \(n\ge4\),
\[
4\,[J_{\rm aff}(Qd_n)-J_{\rm aff}(d_n)]\ge r.
\]

It remains only to pay the peeled defect. Its spectral law has one atom of mass
\[
(1-2/N)^2
\]
and \(N-1\) atoms of mass \(4/N^2\). Writing
\[
\varepsilon=\frac{4(N-1)}{N^2},
\]
we have
\[
H(d_n)=h_2(\varepsilon)+\varepsilon\log_2(N-1).
\]
Using
\[
h_2(\varepsilon)\le
\varepsilon\log_2(e/\varepsilon)
\]
and \((N-1)/\varepsilon=N^2/4\),
\[
H(d_n)
\le
\varepsilon(2n-2+\log_2e)
<
\frac{8n}{N}
=
4J_{\rm aff}(d_n).
\]

Combining this with the rank tax,
\[
H(Qd_n)
\le H(d_n)+r
<
4J_{\rm aff}(d_n)+r
\le
4J_{\rm aff}(Qd_n).
\]

### Theorem 5.1 — nonlinear phase-peeling class

For every \(n\ge4\), every one-point defect \(d_n\), and every quadratic phase \(Q\),
\[
\boxed{
H(Qd_n)<4J_{\rm aff}(Qd_n)\le4I(Qd_n).
}
\]

This is a structured class theorem, **not** full FEI. Its value here is the mechanism: a genuinely nonlinear Fourier-block transformation has a rank-sized entropy tax, and in this family the exact optimized directional gain pays that tax.

Boundary cases behave correctly:

- rank \(r=0\): \(Q\) is affine/character phase and the cost is unchanged;
- \(n=4\): the payment is exactly at the critical endpoint \(4\Delta J=r\);
- increasing \(n\): each nonzero rank unit gains asymptotically \(1/2\) unit of \(J_{\rm aff}\), while the entropy tax remains one bit per rank unit.

## 6. The obvious coefficient-2 bridge is false

A stronger hope would be that a rank-2 bilinear bridge always satisfies
\[
H(Qf)-H(f)
\le
2\,[J_{\rm aff}(Qf)-J_{\rm aff}(f)].
\tag{6.1}
\]
This would turn each rank-2 nonlinear move into an especially cheap induction step.

It is false for an exact admissible Boolean example.

Take the four-bit function, in integer truth-table order,
\[
f=(1,-1,-1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1),
\]
extend it trivially by a fresh bit \(y\), and multiply by the rank-2 phase
\[
Q(x,y)=(-1)^{x_0y}.
\]
Exact Walsh arithmetic gives, for \(f\),

- ten squared coefficients equal to \(1/64\);
- six squared coefficients equal to \(9/64\);
- \(J_{\rm aff}(f)=3/2\).

Hence
\[
H(f)=6-\frac{27}{16}\log_2 3.
\]

For \(h=Qf\), the spectral law has

- eight zero coefficients;
- fourteen squared coefficients equal to \(1/64\);
- eight equal to \(1/16\);
- two equal to \(9/64\);
- \(J_{\rm aff}(h)=7/4\).

Thus
\[
H(h)=5-\frac9{16}\log_2 3,
\]
and
\[
\Delta H=-1+\frac98\log_2 3,
\qquad
\Delta J=\frac14.
\]
Therefore
\[
\frac{\Delta H}{\Delta J}
=
-4+\frac92\log_2 3
=
3.132331253245207\ldots>2.
\]
The strict inequality is exact, since it reduces to
\[
\log_2 3>\frac43
\iff
27>16.
\]

So coefficient \(2\) in (6.1) is rigorously refuted. Any universal bridge inequality of exactly this form needs coefficient at least
\[
-4+\frac92\log_2 3
=
3.132331253245207\ldots.
\]
This does **not** refute a coefficient \(4\) bridge, the quadratic peeling criterion, or FEI.

## 7. Exact stress tests

The accompanying standard-library checker uses exact `Fraction` arithmetic for Walsh masses, autocorrelations, binary ranks, and \(J_{\rm aff}\).

It checked every homogeneous quadratic form on:

- \(n=4\): all \(2^6=64\) forms;
- \(n=5\): all \(2^{10}=1024\) forms.

For every form it verified, for every nonzero translation, the radical/nonradical directional-cost formula, the closed form for \(J_{\rm aff}(Qd_n)\), the \(C=4\) rank-tax payment, and exact phase peeling back to \(d_n\).

It also verifies the five-bit bridge counterexample above by exact squared-Walsh multiplicities and exact \(J_{\rm aff}\) values.

Checker SHA-256:
`537ff2c629f8d35d8f7ce4e5f15334de2486a6a29df676e935b38c2eb812121d`

Recorded output SHA-256:
`dfaed0660b47d2db66e96c8759e5cd10d517125507ba4626702cf2e437910f3c`

These are self-checks of the finite identities. Theorems 2.1 and 5.1 are proved analytically above; the finite checks are not being promoted into a universal proof.

## 8. What moved and the next obstruction

**Moved this run:** the nonlinear-phase route now has a universal entropy accounting theorem, an exact influence formula for a fixed quadratic polar form, and a fully proved nontrivial class where quadratic peeling closes at constant \(4\).

**Killed this run:** the most optimistic coefficient-2 entropy-versus-\(J_{\rm aff}\)-gain bridge.

**Still open:** full FEI.

The next B17 attack should target one of two precise statements:

1. **quadratic descent:** find a universal rule selecting a quadratic polar form for which the \(J_{\rm aff}\)-drop pays a fixed fraction of its rank whenever the function has large entropy; or
2. **larger nonlinear blocks:** replace quadratic phases by low-complexity bent/plateaued phase blocks whose Fourier action is still block-unitary, and prove that the entropy tax is paid by an optimized directional or restriction potential.

The one-point-defect calculation shows the desired geometry is real, while the five-bit counterexample shows that the payment constant cannot simply be guessed from the rank.
