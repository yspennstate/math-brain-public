Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P03 FEI — isospectral zero-cost splicing, signed-symmetry quotient peeling, and a surcharge obstruction

## 0. Parent status and exact movement

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove one finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean function on every finite uniform cube.

**Source-level status before -> after:** **OPEN -> OPEN**. The unrestricted universal finite upper bound remains **UNKNOWN -> UNKNOWN**. P03's inherited native finite-dimensional atlas remains **6 -> 6**. No restricted class or finite computation below is promoted to full FEI.

**Mechanism-level movement.** P03's previous run reduced arbitrary quadratic coupling between already-certified disjoint high-degree cores to a max-splicing theorem, leaving one connected degree-`>=3` core under arbitrary quadratic twist as the source-level obstruction. Companion NM13-02 then proved a quadratic-twist-robust selector whenever a physical derivative phase is Fourier-flat. This run develops a complementary mechanism that sees exact spectral matching even when the derivative is not flat:

1. an **exact child-spectrum Hellinger-defect formula** for the hereditary erasure term, with a new KL rebate and a recombination bound paid by the same defect;
2. an **isospectral zero-cost splice theorem**: if the two child squared Fourier laws agree coordinatewise, then the queried coordinate costs exactly zero hereditary allocation and exactly zero full entropy decrement;
3. a **signed-translation quotient theorem**: every `r`-dimensional signed physical translation symmetry can be peeled by `r` physical coordinate queries at zero allocation/decrement, preserving Fourier entropy while weakly decreasing total influence; hence any minimal-dimensional FEI counterexample can be assumed to have trivial signed-translation symmetry;
4. an explicit **antipodal two-defect obstruction** showing that even the better of P03's earlier minor-child surcharge and curvature surcharge can be `(n-1)` times queried influence while the true hereditary cost is exactly zero at every coordinate.

Thus dependent-branch recombination has a strictly broader zero-cost regime than the earlier character-child, quadratic-core, Wiener, or derivative-flat certificates detect. The new live target is an approximate-isospectral/Hellinger-defect hereditary allocation theorem, not another scalar minor-child/curvature selector.

## 1. Exact dependencies consumed and scope preserved

The progress-first directive was followed; no whole-repository scan was performed.

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: P03 remains T01 FEI owner; new mathematics first; one immutable substantive report; restricted theorems are not source closure.
- `operations/PROB10_2026-09-20.md`, current FEI entry: the fresh-control theorem at commit `ef1087448014f0f6e5c9b4671c200a4020d8e3ea` proves `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` under appended controls, `c>=3`, and `2^{-c}M_0(f)<=1`. Its own report explicitly says the construction adds variables and does not prove fixed-domain/full FEI. It is not used as a universal theorem here.
- `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`: full FEI remains open; the false pointwise-erasure shortcut, fixed-coefficient affine-drift route, resolvent/interpolation target, Han absolute-overlap selector, derivative-degree scalar schedule, blind root-curvature route, and fixed-`s<2` Renyi route remain retired.
- Newest prior P03 substantive report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T11-28-37+0300__fei-certified-core-max-splicing.md`, creation commit `ec4ad2a720641cc025b2c2f63c9fc79bc0e59da9`, blob `af89172d17d120ae1fdaad52674bd6e452f77099`: proves parameter-free quadratic max-splicing of already-certified disjoint cores and the character-child full decrement theorem. Its exact remaining obstruction is one connected degree-`>=3` ANF core under arbitrary quadratic twist.
- Companion NM13-02 newest substantive commit `5866ec61280e9fc580a99b227b3a693078115aee`: proves that if a physical derivative phase has Fourier `L_infinity` norm `<=eta<1`, then every quadratic twist has queried folded influence at least `(1-eta)/2`; recursively guarded selectors therefore give a constant hereditary theorem on a connected high-degree class. That result is complementary, not relabeled here. Its stated limitation is that arbitrary external restrictions can destroy the guards.
- P03's earlier exact tree decomposition is retained: for a physical split, the full entropy decrement is `Delta_iH=B_i+J_i^rec`, and on a tree `H-H_L=R_T+S_T`; the recombination estimate `J_i^rec<=(2/ln2)j_i` is already proved and its coefficient `2/ln2` is sharp.
- P03's earlier valid local bounds are retained with their exact hypotheses: `B_i<=C_chi j_i+min{I(f^+),I(f^-)}` and `B_i<=0.5 I(D_i f)+(1/ln2)j_i`. The antipodal family below does not refute those inequalities; it refutes a blind selector strategy that tries to pay by the better of their positive surcharge terms.
- `POSTED.md` was checked for exact-scope exclusions. No posted unrestricted FEI result or matching theorem below is being rediscovered.

A bounded 20 September 2026 source check still finds González--MacManus--Pereyra `arXiv:2606.00246` presenting universal FEI as a conjecture and proving a stopping-tree framework/restricted classes rather than the universal bound. Friedgut--Kalai remains the standard historical attribution. A bounded search for a matching signed-translation quotient / isospectral-child FEI theorem did not surface one. This is only negative search evidence: **publication priority remains UNVERIFIED**.

## 2. Exact one-step child-spectrum representation

Fix a Boolean function `f` and physical coordinate `i`. Let

\[
g=f^{0},\qquad h=f^{1}
\]

be the two Boolean restrictions on the residual cube, and write

\[
a_T=\widehat g(T),\qquad b_T=\widehat h(T).
\]

The parent Fourier coefficients in the two points of the `i`-fiber are

\[
\widehat f(T)=\frac{a_T+b_T}{2},
\qquad
\widehat f(T\cup\{i\})=\frac{a_T-b_T}{2}.
\tag{2.1}
\]

Put the child squared Fourier laws

\[
P_T=a_T^2,\qquad Q_T=b_T^2,
\qquad q_T=\frac{P_T+Q_T}{2}.
\tag{2.2}
\]

The total parent spectral mass in the fiber is exactly `q_T`. Define its smaller point mass

\[
m_T:=\min\left\{\frac{(a_T+b_T)^2}{4},\frac{(a_T-b_T)^2}{4}\right\}
=\frac{(|a_T|-|b_T|)^2}{4}.
\tag{2.3}
\]

The identity follows because the unordered pair `(|a+b|,|a-b|)` has smaller square `(||a|-|b||)^2`.

Define the child-spectrum Hellinger affinity and defect

\[
A_i:=\sum_T |a_Tb_T|=\sum_T\sqrt{P_TQ_T},
\qquad
M_i:=\sum_Tm_T=\frac{1-A_i}{2}.
\tag{2.4}
\]

The last equality uses Parseval:

\[
\sum_Tm_T
=\frac14\sum_T(P_T+Q_T-2\sqrt{P_TQ_T})
=\frac{1-A_i}{2}.
\]

When `M_i>0`, define the normalized minority-fiber law

\[
\nu_T:=\frac{m_T}{M_i}.
\tag{2.5}
\]

The hereditary erasure cost is therefore exactly

\[
\boxed{
B_i(f)=\sum_T q_T h_2\!\left(\frac{m_T}{q_T}\right).
}
\tag{2.6}
\]

Indeed, conditional on the residual spectral label `T`, the queried spectral bit selects the two parent points with those two masses; binary entropy depends only on the smaller conditional probability `m_T/q_T`.

The recombination term is the Jensen--Shannon divergence between the two child spectral laws:

\[
\boxed{
J_i^{\rm rec}(f)
=H(q)-\frac{H(P)+H(Q)}2
=\operatorname{JS}(P,Q).
}
\tag{2.7}
\]

Thus

\[
\boxed{\Delta_iH(f)=B_i(f)+\operatorname{JS}(P,Q).}
\tag{2.8}
\]

Equation (2.8) is consistent with P03's previously proved one-step erasure/recombination identity; the new point is the common Hellinger defect `M_i` below.

## 3. New local theorem: Hellinger defect pays both allocation and recombination

### Theorem 3.1 — defect is no larger than folded queried influence

Let

\[
\alpha_i=\operatorname{Inf}_i(f),
\qquad
j_i=\min\{\alpha_i,1-\alpha_i\}.
\]

Then

\[
\boxed{M_i\le j_i.}
\tag{3.1}
\]

#### Proof

The child correlation is

\[
\langle g,h\rangle
=\Pr[g=h]-\Pr[g\ne h]
=1-2\alpha_i.
\]

Parseval gives

\[
\langle g,h\rangle=\sum_Ta_Tb_T.
\]

Therefore

\[
A_i=\sum_T|a_Tb_T|
\ge\left|\sum_Ta_Tb_T\right|
=|1-2\alpha_i|.
\]

Using `M_i=(1-A_i)/2`,

\[
M_i\le\frac{1-|1-2\alpha_i|}{2}=j_i.
\]

QED.

### Theorem 3.2 — exact KL rebate for hereditary allocation

For `M_i>0`, let `D_2(\nu\Vert q)` denote base-two relative entropy. Then

\[
\boxed{
B_i(f)
\le
M_i\left[
\log_2\frac1{M_i}
-D_2(\nu\Vert q)
+\frac1{\ln2}
\right].
}
\tag{3.2}
\]

For `M_i=0`, both sides are interpreted as zero.

#### Proof

Set `r_T=m_T/q_T` whenever `q_T>0`. Since `m_T` is the smaller of the two parent masses in that fiber, `0<=r_T<=1/2`. Expand binary entropy:

\[
B_i
=\sum_Tm_T\log_2\frac{q_T}{m_T}
+\sum_T(q_T-m_T)\log_2\frac{q_T}{q_T-m_T}.
\tag{3.3}
\]

The first sum is exact. Using `m_T=M_i\nu_T`,

\[
\sum_Tm_T\log_2\frac{q_T}{m_T}
=M_i\log_2\frac1{M_i}
-M_iD_2(\nu\Vert q).
\tag{3.4}
\]

For the second sum, in natural logarithms,

\[
-(1-r)\ln(1-r)\le r\qquad(0\le r<1),
\]

so

\[
(q_T-m_T)\log_2\frac{q_T}{q_T-m_T}
\le\frac{m_T}{\ln2}.
\]

Summing gives at most `M_i/ln2`. Combining with (3.4) proves (3.2). QED.

The term `D_2(\nu||q)` is a genuine concentration rebate: the logarithmic rare-event payment `M log(1/M)` is reduced when the minority parent mass is concentrated on residual spectral fibers atypical under the average child spectrum.

### Theorem 3.3 — recombination is paid by the same Hellinger defect

\[
\boxed{
\operatorname{JS}(P,Q)
\le\frac{2M_i}{\ln2}.
}
\tag{3.5}
\]

#### Proof

Work first in natural logarithms. For one coordinate of two probability laws, write

\[
p=s(1+t),\qquad q=s(1-t),\qquad 0\le t\le1.
\]

Its Jensen--Shannon contribution is

\[
\frac s2\big[(1+t)\ln(1+t)+(1-t)\ln(1-t)\big].
\tag{3.6}
\]

The corresponding half squared Hellinger contribution is

\[
\frac12(\sqrt p-\sqrt q)^2
=s\bigl(1-\sqrt{1-t^2}\bigr).
\tag{3.7}
\]

It suffices to prove the bracket in (3.6), divided by two, is at most `1-sqrt(1-t^2)`. Let the right side minus the left side be `phi(t)`. Then `phi(0)=0` and

\[
\phi'(t)
=\frac{t}{\sqrt{1-t^2}}-\operatorname{artanh}(t).
\]

The difference on the right starts at zero and has derivative

\[
\frac1{(1-t^2)^{3/2}}-\frac1{1-t^2}\ge0.
\]

Hence `phi'(t)>=0` and `phi(t)>=0`. Summing (3.7) over `T` yields, in nats,

\[
\operatorname{JS}_{\rm nat}(P,Q)
\le\frac12\sum_T(\sqrt{P_T}-\sqrt{Q_T})^2
=1-A_i=2M_i.
\]

Divide by `ln2` to convert to bits. QED.

### Corollary 3.4 — full one-step decrement with KL rebate

Combining (2.8), (3.2), and (3.5),

\[
\boxed{
\Delta_iH(f)
\le
M_i\left[
\log_2\frac1{M_i}
-D_2(\nu\Vert q)
+\frac3{\ln2}
\right].
}
\tag{3.8}
\]

This is fresh-variable-free and makes no independence assumption between dependent branches. It strictly refines a blind replacement of `M_i` by `j_i` whenever child spectra are close in Hellinger distance.

It is **not** full FEI: a universal tree-level estimate for the weighted sum of these defect charges has not been proved.

## 4. Exact zero-cost dependent-branch recombination

### Theorem 4.1 — isospectral child splice

Assume the child squared Fourier laws agree coordinatewise:

\[
\boxed{P_T=Q_T\quad\text{for every }T.}
\tag{4.1}
\]

Equivalently, `|a_T|=|b_T|` for every residual spectral label. Then

\[
\boxed{M_i=0,\quad B_i=0,\quad J_i^{\rm rec}=0,\quad\Delta_iH=0.}
\tag{4.2}
\]

Moreover

\[
\boxed{H(f)=H(g)=H(h),\qquad I(g)=I(h),\qquad I(f)=\alpha_i+I(g).}
\tag{4.3}
\]

Consequently, if the two child branches each admit a hereditary allocation certificate `A`, or each satisfy a direct FEI certificate `C`, then the parent inherits the same constant with **no additive recombination floor**.

#### Proof

Condition (4.1) says `A_i=\sum_T\sqrt{P_TQ_T}=1`, so `M_i=0`. By (2.3), each `m_T=0`, hence exactly one of the two parent coefficients in each fiber `(T,T\cup\{i\})` may carry nonzero mass. Therefore `Z_i` is deterministic from `Z_{-i}`, proving `B_i=0`.

Since `P=Q`, the Jensen--Shannon divergence is zero, proving `J_i^{rec}=0`, hence `Delta_iH=0` by (2.8). Thus

\[
H(f)=\frac{H(g)+H(h)}2=H(g)=H(h).
\]

The child spectral laws are equal, so their total influences are equal as first moments of `|T|`. The exact physical influence identity gives

\[
I(f)=\alpha_i+\frac{I(g)+I(h)}2=\alpha_i+I(g).
\]

For hereditary certificates, query `i` first at zero allocation cost and graft the two child certificate trees. Their weighted leaf costs are at most `A I(g)=A I(h)<=A I(f)`. For direct FEI, `H(f)=H(g)<=C I(g)<=C I(f)`. QED.

This is a genuinely dependent-branch recombination theorem: `g` and `h` need not be equal, independent, character-related, quadratic-related, or supported on disjoint physical variable blocks. Only their squared Fourier laws must agree.

## 5. Signed-translation quotient theorem

The isospectral splice theorem has a useful physical symmetry source.

Let `V<=F_2^n` be a linear subspace and let `lambda:V->F_2` be linear. Assume

\[
\boxed{
f(x+v)=(-1)^{\lambda(v)}f(x)\qquad(x\in F_2^n,v\in V).
}
\tag{5.1}
\]

Call `V` a signed-translation symmetry space. Put `r=dim V`.

### Theorem 5.1 — zero-cost quotient peeling

There exists a set `P` of `r` physical coordinates and a full `r`-layer physical restriction tree querying exactly those coordinates such that:

1. every internal query has `B_i=0` and in fact `Delta_iH=0`;
2. every terminal leaf is a sign/input-translate of one common Boolean function `g` on `n-r` variables;
3. `H(f)=H(g)` and `I(g)<=I(f)`;
4. any hereditary allocation or direct FEI certificate for `g` transfers to `f` with the same constant.

#### Proof

Choose pivot coordinates `P` so that projection `pi_P:V->F_2^P` is bijective. Reorder coordinates only for notation, writing `x=(y,z)` with `y\in F_2^r` the pivot coordinates and `z\in F_2^{n-r}`. Row-reducing a basis of `V` gives a unique representation

\[
v(y)=(y,My)
\]

for a linear map `M:F_2^r->F_2^{n-r}`. Since `lambda` is linear, `lambda(v(y))=a\cdot y` for some `a\in F_2^r`.

Let

\[
g(z):=f(0,z).
\]

Applying (5.1) with `v(y)` to the point `(0,z+My)` yields

\[
\boxed{
f(y,z)=(-1)^{a\cdot y}g(z+My).}
\tag{5.2}
\]

This already shows that every full assignment of the pivot variables gives a sign/input-translate of `g`.

For the Fourier law, with dual variables `(s,t)`, substitute (5.2):

\[
\widehat f(s,t)
=2^{-r}\sum_y(-1)^{(a+s)\cdot y}
\,2^{-(n-r)}\sum_zg(z+My)(-1)^{t\cdot z}.
\]

Changing `z` to `z+My` multiplies the inner sum by `(-1)^{(M^Tt)\cdot y}`. Hence the `y`-sum is one exactly when

\[
s=a+M^Tt
\]

and zero otherwise. Therefore

\[
\boxed{
\widehat f(s,t)=
\begin{cases}
\widehat g(t),&s=a+M^Tt,\\
0,&\text{otherwise}.
\end{cases}}
\tag{5.3}
\]

Thus the squared Fourier law of `f` is just the squared Fourier law of `g` embedded injectively into an affine graph. In particular

\[
H(f)=H(g).
\tag{5.4}
\]

Also

\[
I(f)=\sum_t\bigl(|t|+|a+M^Tt|\bigr)\widehat g(t)^2
\ge\sum_t|t|\widehat g(t)^2=I(g).
\tag{5.5}
\]

Now query the pivot coordinates in row-echelon order. After fixing any earlier pivots, the residual signed symmetry generated by a row whose earlier pivots are zero still relates the two children of the next pivot by an input translation on the unqueried residual coordinates and a global sign. Translation and global sign preserve coefficient magnitudes, so the two child squared Fourier laws agree coordinatewise after the natural common residual labeling. Theorem 4.1 gives `B_i=Delta_iH=0` at that node. Repeating through all pivots proves item 1, while (5.2) proves item 2.

Grafting any leaf certificate gives item 4; (5.4)-(5.5) give item 3. QED.

### Corollary 5.2 — minimal-dimensional counterexample reduction

Fix any candidate constant `C`. If a Boolean function `f` violates `H(f)<=C I(f)` and has a nontrivial signed-translation symmetry space, then some Boolean function on strictly fewer variables also violates the same inequality.

Indeed Theorem 5.1 gives `g` with

\[
H(g)=H(f)>CI(f)\ge CI(g).
\]

Therefore any **minimal-dimensional** counterexample to a candidate universal FEI constant can be assumed to have trivial signed-translation symmetry.

This is a source-level structural reduction rather than a restricted constant improvement.

### Corollary 5.3 — spectral support formulation

Taking Fourier transforms in (5.1), every nonzero coefficient satisfies

\[
S\cdot v=\lambda(v)\qquad(v\in V).
\]

So the Fourier support lies in an affine subspace of codimension `r`. Conversely, the physical quotient representation (5.2) shows that this codimension can be peeled at zero hereditary allocation whenever it comes from signed physical translations.

## 6. Decisive obstruction to the previous surcharge selectors

The preceding P03 local theorems supplied two valid upper bounds:

\[
B_i(f)\le C_\chi j_i(f)+\min\{I(f^0),I(f^1)\},
\tag{6.1}
\]

and

\[
B_i(f)\le\frac12I(D_if)+\frac1{\ln2}j_i(f).
\tag{6.2}
\]

A natural next hope would be to select a coordinate for which at least one positive surcharge in (6.1)-(6.2) is `O(Inf_i)`. The following family refutes that strategy decisively while keeping the true allocation zero.

For `n>=3`, let `N=2^n` and define the antipodal two-defect function

\[
u_n(x)=1-2\bigl(1_{\{0\}}(x)+1_{\{\mathbf1\}}(x)\bigr),
\tag{6.3}
\]

where `mathbf1=(1,...,1)`.

### Proposition 6.1

For every coordinate `i`,

\[
\boxed{B_i(u_n)=0,\qquad \alpha_i(u_n)=2^{2-n}.}
\tag{6.4}
\]

Yet

\[
\boxed{
\min\{I(u_n^0),I(u_n^1)\}
=(n-1)\alpha_i(u_n),
}
\tag{6.5}
\]

and

\[
\boxed{
\frac12I(D_i u_n)
=(n-1)\alpha_i(u_n).
}
\tag{6.6}
\]

Hence for every coordinate

\[
\boxed{
\frac{
\min\{\min(I(u_n^0),I(u_n^1)),\,\frac12I(D_i u_n)\}
}{\alpha_i(u_n)}
=n-1\longrightarrow\infty,
}
\tag{6.7}
\]

while the actual hereditary cost is exactly zero.

#### Proof

Translation by `mathbf1` preserves the defect set `{0,mathbf1}`, so `u_n(x+mathbf1)=u_n(x)`. Thus the signed-translation symmetry space contains `span{mathbf1}`. Equivalently, direct Fourier computation gives

\[
\widehat u_n(\varnothing)=1-\frac4N,
\]

and, for `S\ne\varnothing`,

\[
\widehat u_n(S)
=-\frac2N\bigl(1+(-1)^{|S|}\bigr)
=
\begin{cases}
-4/N,&|S|\text{ even},\\
0,&|S|\text{ odd}.
\end{cases}
\tag{6.8}
\]

So the squared Fourier law is supported entirely on even-cardinality sets. For every `i`, the parity of `|S|` determines membership of `i` from `S\setminus\{i\}`, hence

\[
B_i=H(Z_i\mid Z_{-i})=0.
\]

Physically, the only disagreeing `i`-edges are those incident to the two antipodal defects, giving two disagreeing edges among `2^{n-1}` edges in direction `i`. Thus

\[
\alpha_i=2/2^{n-1}=2^{2-n}.
\]

Each restriction `u_n^0,u_n^1` is a one-point defect on `n-1` variables. A one-point defect in `m` variables has every coordinate influence `2^{1-m}`, hence total influence `m2^{1-m}`. With `m=n-1`,

\[
I(u_n^0)=I(u_n^1)=(n-1)2^{2-n}=(n-1)\alpha_i,
\]

proving (6.5).

For the multiplicative derivative, `D_iu_n=u_n^0u_n^1`. On the residual cube it is `-1` at the two antipodal points corresponding to the two defect edges and `+1` elsewhere, i.e. another antipodal two-defect function in `n-1` variables. Its total influence is

\[
I(D_iu_n)=2(n-1)2^{2-n}=2(n-1)\alpha_i,
\]

which proves (6.6). QED.

Thus neither minor-child influence nor derivative square-curvature sees the exact spectral parity cancellation. Taking the better of them still fails by an unbounded factor. The valid upper bounds (6.1)-(6.2) remain valid; only this selector strategy is retired.

The companion derivative-spectral-flat theorem is complementary rather than contradicted: for `u_n`, the derivative phase has a Fourier coefficient tending to one, so its `eta` is near one and the flatness selector intentionally gives no uniform payment. The exact isospectral/parity mechanism supplies the missing zero-cost explanation.

### FEI itself remains well behaved on the obstruction family

From (6.8), the total nonconstant spectral mass is

\[
W=\frac{8(N-2)}{N^2},
\]

spread uniformly over `N/2-1` nonempty even sets. Hence

\[
H(u_n)=h_2(W)+W\log_2(N/2-1),
\]

while

\[
I(u_n)=n2^{2-n}=\frac{4n}{N}.
\]

Therefore `H(u_n)/I(u_n)->4`. This is not an FEI counterexample; it is a mechanism counterexample.

## 7. Sanity checks executed and preserved

Two independent self-check scripts were executed for the new identities. They are not independent mathematical audits.

### 7.1 Signed-symmetry quotient / antipodal checker

File:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T12-28-55+0300__signed-symmetry-quotient-check.py`

Creation commit `eb9283a139b83e815b490d27cc5bf1b1858b7fdd`; read-back blob `a4391b04508e6ddf6cd71a7e0458c120365cd57c`.

Preserved output:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T12-28-55+0300__signed-symmetry-quotient-check.out`

Creation commit `192883f5bb9cf8d1ea85745870de13b32365a395`; read-back blob `036089bccc6845d4d32da7adce3113bc98c02f7f`.

Executed coverage:

- all `32,906` Boolean functions through dimension four modulo global sign;
- `2,566` of those had nontrivial signed-translation symmetry;
- `3,966` exhaustive symmetry-pivot nodes;
- `1,500` deterministic-seed oblique signed-symmetry lifts in dimensions five through eight, totaling `5,378` pivot nodes;
- antipodal two-defect functions for `n=3,...,14`.

Recorded maxima were exactly `0.0` for queried `B_i` on symmetry pivots, terminal-minus-root entropy discrepancy, terminal influence minus root influence, antipodal `B_i`, and the closed-form antipodal surcharge identities. Status: `PASS`.

### 7.2 Hellinger-defect checker

File:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T12-28-55+0300__hellinger-defect-check.py`

Creation commit `2dc400a626808bc8cc555fc4144efd29793b9844`; read-back blob `3d25e6b326e7d1f5cee69ce35fb2d717d2bd20b7`.

Preserved output:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T12-28-55+0300__hellinger-defect-check.out`

Creation commit `12ce306043260cfbaf34117ad699b8bf06f8ba40`; read-back blob `317c1989989beabf78c9568a481b6d0435e6f318`.

It exhaustively checked `131,474` coordinate cases through dimension four modulo global sign. Maximum recorded errors/violations:

- exact `B_i` fiber formula: `1.1102230246251565e-16`;
- exact `Delta_iH=B_i+JS`: `5.551115123125783e-16`;
- `M_i<=j_i`: `0.0` violation;
- `JS<=2M_i/ln2`: `0.0` violation;
- KL-rebate allocation bound: `0.0` violation;
- KL-rebate full-decrement bound: `0.0` violation.

Status: `PASS`.

## 8. What this does and does not remove

### Removed / materially narrowed

- **Exact isospectral dependent branching is solved:** it costs zero allocation and zero recombination, with no fresh controls and no branch-independence assumption.
- **Signed physical translation symmetry is removable for free:** it can be quotient-peeled by physical queries, so minimal-dimensional FEI counterexamples may be assumed signed-translation-rigid.
- **Blind minor-child/curvature selector is decisively refuted:** the antipodal family forces both surcharges to be `(n-1) Inf_i` at every coordinate although `B_i=0`.
- **One-step structure is sharper:** the same Hellinger defect controls allocation and recombination, and the allocation charge has an explicit KL rebate.

### Not removed

A universal tree has not been constructed with

\[
\sum_v w_v M_v\left[
\log_2\frac1{M_v}-D_2(\nu_v\Vert q_v)
\right]
=O(I(f)).
\tag{8.1}
\]

Nor is it proved that every connected high-degree core either admits a derivative-flat selector or an approximately isospectral selector with a paid logarithmic defect. The exact `M=0` quotient theorem is not by itself a universal approximation theorem.

Therefore full FEI remains open.

## 9. Next nonredundant attack

The next P03 method should be an **approximate-isospectral hereditary allocation theorem** rather than another minor-child, curvature, derivative-degree, fixed-Renyi, or absolute-overlap scalar majorant.

A concrete target is to prove that every Boolean restriction has a coordinate for which either:

1. the companion derivative-flat condition gives a constant direct payment; or
2. the child Hellinger defect satisfies a quantitatively useful rebate relation, e.g.
   \[
   M_i\left[\log_2(1/M_i)-D_2(\nu_i\Vert q_i)\right]
   \le C\,\operatorname{Inf}_i(f),
   \]
   with a hereditary selection rule;

and then telescope the disjoint queried-influence budget. The exact `M_i=0` nodes should be spliced for free before any positive charge is assigned.

The falsification alternative is equally concrete: construct a signed-translation-rigid connected high-degree family on which every coordinate simultaneously has derivative spectrum nearly atomic and Hellinger-defect rebate charge much larger than queried influence, while the true hereditary allocation remains bounded or diverges. Such a family would decisively delimit both current complementary selectors.

This route is genuinely different from the two recently failed scalar recovery routes and retains their failure history.

## 10. ledger_delta

```yaml
ledger_delta:
  parent_problem: Friedgut-Kalai Fourier entropy-influence
  parent_scope_before: OPEN
  parent_scope_after: OPEN
  universal_constant_before: UNKNOWN
  universal_constant_after: UNKNOWN
  native_finite_atlas_before: 6
  native_finite_atlas_after: 6
  fresh_control_status: restricted_only_unchanged
  new_theorems:
    - child-spectrum Hellinger defect M_i=(1-sum sqrt(PQ))/2 satisfies M_i<=j_i
    - hereditary allocation KL-rebate bound in terms of M_i and D_2(nu||q)
    - Jensen-Shannon recombination <=2 M_i/ln2
    - exact isospectral-child splice has B_i=J_i^rec=Delta_iH=0
    - signed-translation rank-r quotient peels r physical coordinates at zero cost and preserves entropy
    - minimal-dimensional FEI counterexample may be assumed signed-translation-rigid
  new_obstruction:
    family: antipodal two-defect u_n
    statement: min(minor-child-influence, half-derivative-influence)/Inf_i = n-1 for every i while B_i=0
    consequence: blind hybrid of prior minor-child and curvature surcharges is retired
  checker_1:
    exhaustive_functions_mod_global_sign: 32906
    exhaustive_symmetry_pivot_nodes: 3966
    oblique_lift_cases: 1500
    oblique_pivot_nodes: 5378
    antipodal_dimensions: 3..14
    status: PASS
  checker_2:
    exhaustive_coordinate_cases: 131474
    status: PASS
  mechanism_gain: exact and approximate child-spectrum matching is now isolated as a structure-sensitive zero/low-cost recombination mechanism
  source_level_gain: structural reduction only; no universal C proved
  residual_obstruction: hereditary tree control of Hellinger-defect logarithmic charge / connected signed-translation-rigid high-degree core
  next_attack: hybrid derivative-flat plus approximate-isospectral selector with explicit KL rebate, or decisive rigid-core obstruction
  novelty_status: UNVERIFIED
  independent_review_status: pending
```

**End of complete run report.**
