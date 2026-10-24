# account01/B08 — logarithmically weighted multi-shift Booleanity certificate

**Classification:** `ESSENTIAL_STEP_APPLIED / LOG_WEIGHTED_MULTISHIFT_KL_CERTIFICATE`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Fresh control and supersession

Fresh owner control revision `2026-09-22.3` reassigns B08 from MOC4 to the all-team FEI programme. The active B08 target is:

> Construct a logarithmically weighted multi-shift Booleanity statistic bounded above by `K_occ` which retains the sparse-suspension logarithm; do not use a fixed/low-depth truncation.

The following pinned results are used exactly in their stated scopes.

1. account02/B15, commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`: exact I-projection identity
   \[
   K_{\rm occ}=D_2(P\Vert Q_r),\qquad R_\Gamma=B_{\inf}^\Gamma+K_{\rm occ}.
   \]
2. account04/B17, commit `603b35e74227d1c2d8ee34c0c527c439c686e30b`: exact biased Boolean multiplication matrices `M_U` and Booleanity equations `a^T M_Ua=0` for `U\ne\varnothing`.
3. account04/B15, commit `7ec649dfb3d1ab2f92855f2069590fca2ac956dd`: on the genuine one-point-defect suspension, the complete unweighted convolution energy is only `Theta(I)` whereas `K_occ=Theta(mI)`.
4. account03/B18, commit `bff0d7b6c21485f386841c42582eb04f32705046`: fixed-depth, and even `d_m\le(1/2-\epsilon)m`, labelled low-level KL plus one merged tail is not a universal payment mechanism.
5. **Required partner result consumed and applied:** account02/B08, run `B08-20260922T103745Z-0f440e`, commit `a83d4009cc98aeb739af4f40b1c2cfa8be7269d0`, theorem `NONLINEAR_RARE_EVENT_KL_CERTIFICATE`. It obtains a single oriented rare-event binary-KL payment equal to one half of the leading sparse-suspension `K_occ`, and identifies no-double-spending multi-cell aggregation as the next problem.

The result below supplies such a no-double-spending *multi-shift* aggregation on the sparse suspension and, in general, gives a source-valid all-shift lower certificate for `K_occ`.

## 1. A local logarithmic entropy weight

For `r\ge0` set

\[
 d(r)=r\ln r-r+1,
 \qquad h(r)=(\sqrt r-1)^2,
\]

with `0 ln 0=0`, and define

\[
\boxed{\omega(r)=\max\{1,\ln r-1\},\qquad \omega(0)=1.}
\tag{1.1}
\]

### Lemma 1 — pointwise logarithmic Hellinger payment

For every `r\ge0`,

\[
\boxed{\omega(r)h(r)\le d(r).}
\tag{1.2}
\]

#### Proof

Put `t=\sqrt r`. First,

\[
 d(r)-h(r)
 =2t\,[t\ln t-t+1]\ge0,
\]

because `x\ln x-x+1\ge0` for `x\ge0`. Thus the weight `1` is always legal.

When `\ln r-1>1`, in particular `t>1`, a direct expansion gives

\[
 d(r)-(\ln r-1)h(r)
 =2[(2t-1)\ln t-t+1].
\]

The bracket vanishes at `t=1` and has derivative

\[
2\ln t+1-{1\over t}\ge0\qquad(t\ge1).
\]

Hence the logarithmic weight is also legal whenever it is selected by (1.1). This proves (1.2). `QED`.

The important feature is the asymptotic

\[
\omega(r)=\ln r-1\qquad(r\ge e^2),
\tag{1.3}
\]

so a source atom which is exponentially heavier than its reference atom keeps essentially its entire log-likelihood factor instead of being reduced to unweighted Hellinger energy.

## 2. General biased all-shift theorem

Let `G` be a nonconstant Boolean gate under an interior product bias, with biased Fourier coefficients `a_S`, constant coefficient `m=a_\varnothing`, and

\[
v=1-m^2>0,
\qquad
P(S)={a_S^2\over v},\quad S\ne\varnothing.
\]

Let `Q` be any reference probability law on the nonempty spectral sets; for the live application it is the exact influence I-projection `Q_r`. Assume `Q(S)>0` whenever `P(S)>0`; otherwise `D(P\Vert Q)=+\infty` and the lower bound is trivial.

Choose the authentic signs of `a` and define the sign-aligned reference amplitudes

\[
b_\varnothing=m,
\qquad
b_S=\operatorname{sgn}(a_S)\sqrt{vQ(S)}.
\tag{2.1}
\]

At a zero actual coefficient the sign is arbitrary. Put `e=b-a`, so `e_\varnothing=0`, and for each nonempty spectral atom set

\[
\omega_S=\omega\!\left({P(S)\over Q(S)}\right).
\tag{2.2}
\]

By Lemma 1,

\[
\boxed{
\sum_{S\ne\varnothing}\omega_S e_S^2
\le v\ln2\,D_2(P\Vert Q).
}
\tag{2.3}
\]

Indeed each summand is `vQ(S)\omega(P/Q)(\sqrt{P/Q}-1)^2`, and the right side is the sum of `vQ(S)d(P/Q)`.

Now use the exact biased Boolean multiplication matrices `M_U` of account04/B17. For `U\ne\varnothing`, Booleanity gives

\[
a^TM_Ua=0.
\tag{2.4}
\]

For the normalization channel `U=\varnothing`, put `M_\varnothing=I`; then `a^TM_\varnothing a=b^TM_\varnothing b=1`. For any selected family `\mathcal U` of channels define the reference residual

\[
r_U=b^TM_Ub-a^TM_Ua
\tag{2.5}
\]

and the nonempty-coordinate vector

\[
z_U=\Pi_{\ne\varnothing}M_U(a+b).
\tag{2.6}
\]

Let `W=diag(\omega_S)` and form the matrix whose `U`-th column is

\[
y_U=W^{-1/2}z_U.
\tag{2.7}
\]

Write `Y=(y_U)_{U\in\mathcal U}` and `H=Y^TY`.

### Theorem 2 — `B08-LOG-WEIGHTED-MULTISHIFT-v1`

Define

\[
\boxed{
\mathcal T_{\mathcal U}(P,Q;a)
={1\over v\ln2}\,r^T H^\dagger r,
}
\tag{2.8}
\]

where `H^\dagger` is the Moore--Penrose pseudoinverse. Then

\[
\boxed{
0\le \mathcal T_{\mathcal U}(P,Q;a)
\le D_2(P\Vert Q).
}
\tag{2.9}
\]

In particular, for `Q=Q_r`,

\[
\boxed{\mathcal T_{\mathcal U}\le K_{\rm occ}.}
\tag{2.10}
\]

#### Proof

Because every `M_U` is symmetric,

\[
r_U
=b^TM_Ub-a^TM_Ua
=(b-a)^TM_U(a+b).
\]

Since `e_\varnothing=0`, only the nonempty coordinates contribute. Set

\[
x=W^{1/2}e_{\ne\varnothing}.
\]

Then exactly

\[
r=Y^Tx.
\tag{2.11}
\]

Therefore

\[
r^T(Y^TY)^\dagger r
=x^TY(Y^TY)^\dagger Y^Tx
=\|\operatorname{Proj}_{\operatorname{col}Y}x\|_2^2
\le\|x\|_2^2.
\tag{2.12}
\]

Equation (2.3) gives `\|x\|_2^2\le v\ln2 D_2(P\Vert Q)`. Divide by `v\ln2`. `QED`.

### Why this is not the refuted L2 mechanism

The account04/B15 statistic uses the unweighted scalar energy `\sum_U r_U^2`. The new statistic first performs the **atomwise entropy comparison** (1.2), retaining weight `\ln(P/Q)-1` on high-likelihood atoms, and only then aggregates all signed shifts through the Gram pseudoinverse. It uses one global KL budget through the orthogonal projection (2.12); separate shift payments are not added and hence `K_occ` is not double-spent.

No degree cutoff occurs. Every spectral atom and every selected shift can enter. Thus the account03/B18 recursive-majority low-level refutation does not apply to the theorem. No claim is made here that `\mathcal T` is already universally large enough on recursive majority; that remains part of the unpaid coercivity problem.

## 3. Sparse suspension: the certificate retains the entire logarithm up to `o(I)`

Apply Theorem 2 to the exact genuine Boolean suspension used by account04/B15:

\[
p=2^{1-m},
\qquad
g_m(x)=1-2\mathbf1_{\{x=0\}},
\qquad F_m(y,x)=y g_m(x).
\tag{3.1}
\]

After factoring out the fresh deterministic spectral coordinate, the actual and reference laws on old subsets `T\subseteq[m]` are

\[
P_m(\varnothing)=(1-p)^2,
\qquad P_m(T)=p^2\quad(T\ne\varnothing),
\tag{3.2}
\]

\[
Q_m(T)=p^{|T|}(1-p)^{m-|T|}.
\tag{3.3}
\]

The authentic amplitude signs are positive at `\varnothing` and negative elsewhere. The inherited exact asymptotic is

\[
K_{\rm occ}(F_m)
=mp\left(m-5+{1\over\ln2}+o(1)\right),
\qquad I(g_m)=mp.
\tag{3.4}
\]

Use **all** old-coordinate convolution shifts, together with the zero-shift normalization channel. For the uniform cube these `M_U` are the translations `T\mapsto T\triangle U`.

### Lemma 3 — the comparison amplitude is cyclic for all sufficiently large `m`

Let

\[
A=\sqrt{1-p},\qquad B=\sqrt p.
\]

As in account04/B15, the reference amplitude vector `b` is the Walsh coefficient vector of

\[
G_m(x)=2A^m-Z(x),
\qquad
Z(x)=\prod_{i=1}^m(A+B\chi_i(x)).
\tag{3.5}
\]

Hence the translation orbit of `c=a+b` spans the whole coefficient space exactly when the physical Walsh transform

\[
C_m(x)=g_m(x)+G_m(x)
\tag{3.6}
\]

has no zero.

At the exceptional point `x=0`,

\[
C_m(0)=-1+2A^m-(A+B)^m<0,
\tag{3.7}
\]

because `A^m<1` and `A+B>1`.

At any other point, at least one factor in `Z` is `A-B`; therefore

\[
Z(x)\le(A+B)^{m-1}(A-B)
=A^m(1+t)^{m-1}(1-t),
\quad t={B\over A}.
\tag{3.8}
\]

For `m\ge7`,

\[
\ln[(1+t)^{m-1}(1-t)]
\le(m-2)t<\ln2.
\tag{3.9}
\]

The last inequality holds at `m=7` because `5/\sqrt{63}<\ln2`; afterwards the left control `(m-2)t` decreases, since halving `p` multiplies `t` by less than `1/\sqrt2` whereas `(m-1)/(m-2)\le6/5`. Thus `Z(x)<2A^m`, so `G_m(x)>0` and

\[
C_m(x)=1+G_m(x)>0\qquad(x\ne0).
\tag{3.10}
\]

Therefore convolution by `c` is invertible for every `m\ge7`. `QED`.

Because the all-shift columns span the whole space and `W^{-1/2}` is invertible, the projection in (2.12) is the identity. Consequently

\[
\boxed{
\mathcal T_m
={1\over\ln2}\sum_T
\omega\!\left({P_m(T)\over Q_m(T)}\right)
\bigl(\sqrt{P_m(T)}-\sqrt{Q_m(T)}\bigr)^2.
}
\tag{3.11}
\]

### Theorem 4 — no logarithmic loss on the sparse barrier

For the genuine suspension (3.1),

\[
\boxed{
0\le K_{\rm occ}(F_m)-\mathcal T_m=o(mp)=o(I(g_m)).
}
\tag{3.12}
\]

Hence

\[
\boxed{
{\mathcal T_m\over mp}
=m-5+{1\over\ln2}+o(1).
}
\tag{3.13}
\]

This meets the sparse-suspension acceptance requirement: the new lower certificate loses only `o(I)` where unweighted full-shift L2 loses `Theta(K_occ)`.

#### Proof of (3.12)

Let `j=|T|`. For one atom on level `j`, write

\[
D_j=P_j\ln(P_j/Q_j)-P_j+Q_j,
\qquad
L_j=\omega(P_j/Q_j)(\sqrt{P_j}-\sqrt{Q_j})^2.
\]

Lemma 1 gives `0\le D_j-L_j`.

* `j=0`: `P_0,Q_0\to1` and `|P_0-Q_0|=O(mp)`, so the Bregman remainder is `O(m^2p^2)=o(mp)`.
* `j=1`: `P_1=p^2`, `Q_1=p(1-p)^{m-1}` and the selected weight is `1`. The exact identity behind Lemma 1 gives `D_1-L_1=O(p^{3/2}|\ln p|)`. Multiplying by `m` is `o(mp)`.
* `j=2`: both masses are `p^2(1+O(mp))`; after multiplying by `\binom m2`, the total slack is `o(mp)`.
* `j\ge3`: for `m\ge7`, `P_j/Q_j>e^2`, so `\omega=\ln(P_j/Q_j)-1`. The exact expansion used in Lemma 1 yields
  \[
  0\le D_j-L_j
  \le2\sqrt{P_jQ_j}\ln(P_j/Q_j)+2Q_j.
  \tag{3.14}
  \]
  The `Q`-mass of levels `j\ge3` is `O((mp)^3)=o(mp)`. For the square-root term, with `u=\sqrt p` and `v_0=\sqrt{1-p}`,
  \[
  \sum_{j\ge3}\binom mj p\,u^jv_0^{m-j}
  \le p\binom m3u^3(u+v_0)^{m-3}
  =O(m^3p^{5/2}),
  \]
  while `\max_j\ln(P_j/Q_j)=O(m^2)`. Thus the entire first term in (3.14) is `O(m^5p^{5/2})=o(mp)`.

Summing the four ranges proves (3.12). `QED`.

## 4. Direct application of the partner result

account02/B08's completed result `B08-20260922T103745Z-0f440e` uses one complement-shift orientation and a single binary relative entropy. On this same suspension it proves

\[
K_{\rm occ}\ge {1\over2}m^2p+O(mp),
\]

capturing asymptotically one half of the leading rare-event information. It explicitly identifies the danger of summing several binary-KL events, since that can double-spend `K_occ`.

Theorem 2 is a direct continuation of that exact issue: all shift residuals are combined **before** payment, via one Gram projection against the single entropy budget (2.3). Theorem 4 then recovers

\[
K_{\rm occ}-\mathcal T_m=o(I)
\]

on the same source. Thus the factor-two loss is removed on the canonical sparse barrier without summing separate KL inequalities.

This is a sparse-face completion of the partner's proposed multi-event continuation, **not** a universal FEI proof.

## 5. Recursive-majority preflight

The account03/B18 barrier applies to schemes that preserve individually labelled spectral atoms only below a cutoff `d_m\le(1/2-\epsilon)m` and merge the rest into one tail. The statistic (2.8) does neither:

* `P(S)/Q(S)` is retained atomwise at every cardinality;
* `\omega(P/Q)` grows like the full log likelihood ratio on rare `P`-heavy atoms;
* the shift family may contain every nonzero `U`, so high-cardinality Boolean multiplication constraints are not discarded;
* aggregation occurs only after the entropy-weighted comparison and uses one global projection, not one merged high-degree tail.

Therefore the published recursive-majority counterexample does not refute (2.9). This run does **not** prove a useful lower bound for `\mathcal T` on recursive majority; proving such a bound, or producing a genuine Boolean family where `K_occ-\mathcal T` is too large, is now the correct falsification test.

## 6. Exact new implication and first unpaid step

The old obstruction was that even all unweighted shift equations give only `Theta(I)` on the sparse suspension while `K_occ=Theta(mI)`.

The new proved implication is:

\[
\boxed{
\mathcal T_{\rm all}\le K_{\rm occ}
}
\]

for arbitrary interior product biases, with a genuinely logarithmic atomwise weight; and on the canonical sparse suspension,

\[
\boxed{
K_{\rm occ}-\mathcal T_{\rm all}=o(I).
}
\]

The first essential missing implication is now the **universal coercivity problem**

\[
\boxed{
K_{\rm occ}-\mathcal T_{\rm all}\le C_0 I
}
\tag{6.1}
\]

(or the sharper balanced `C_0(I-1)` form) for every genuine Boolean source, with the same all-shift statistic and no low-degree truncation. A proof of (6.1) would convert the exact KL route into a dimension-independent Booleanity payment after a finite center adjustment. A source-valid counterfamily with `(K_occ-\mathcal T_{all})/I\to\infty` would refute this mechanism while leaving FEI open.

The highest-value next test is recursive ternary majority, precisely because it defeats fixed-depth labelled projections.

## 7. Verification

The adjacent standard-library checker evaluates the exact sparse formulas level-by-level, verifies the pointwise entropy weight numerically, and checks the two extremal physical eigenvalues which guarantee convolution cyclicity. Representative values are:

```
m   K/I             T/I             (K-T)/I
7   3.627007749734   3.287394948682  0.339612801052
12  8.536298196345   8.473854830805  0.062443365539
20 16.498428197662  16.494468614879  0.003959582784
28 24.482502547347  24.482253644593  0.000248902753
```

The checker returns `PASS`. The theorem and asymptotic proof are analytic; the checker is a falsification/self-consistency aid only.

## 8. Scope

No MOC4, benchmark, installation, paid/remote model, workflow dispatch, email, Drive, public release, credentials, permission bypass, or unrelated private data were used. Repository access is coordination/storage and does not constitute authenticated native brain retrieval, so the run remains `WITHOUT_VERIFIED_BRAIN`.
