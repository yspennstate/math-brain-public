# B14 — singleton erasure-selector compiler and collapse of proper-block search

**Run:** 2026-09-21T11:01:36Z, fleet02/B14  
**Role:** FEI erasure and selector proof  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** PARTIAL / PROVED structural implications. **Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Fresh mathematical source before this derivation:** `master` observed at `8ee854972993b0170b0fefc2439ac5bfbb095317` after consuming the current P03 entry rules and newest relevant B14/B18 continuations.

This run continues the exact mass-weighted erasure / existential-selector route. It does **not** revive the false stronger statement that every prescribed coordinate of every Boolean function has a universal restriction payment.

## 1. Inherited exact state used

Let `f:{-1,1}^n->{-1,1}` be Boolean, and let `X=S` be its Fourier spectral sample,

\[
\Pr[X=S]=\widehat f(S)^2.
\]

Write

\[
H(f)=H(X),\qquad I(f)=\mathbb E|X|=\sum_i p_i,
\qquad p_i:=\Pr[i\in X]=\operatorname{Inf}_i(f).
\]

For a coordinate `i`, define the mass-weighted erasure entropy

\[
B_i(f):=H(X_i\mid X_{-i}).
\]

For a physical block `A`, define

\[
B_A(f):=H(X_A\mid X_{A^c}),
\qquad I_A(f):=\sum_{i\in A}p_i.
\]

The recovered September-20/21 restriction theory supplies:

1. the exact coordinate decomposition
   \[
   \Delta_iH=B_i+JS_i;
   \tag{1}
   \]
2. the universal recombination bounds
   \[
   0\le JS_i\le B_i,
   \qquad
   JS_i\le c_*\min\{p_i,1-p_i\},
   \qquad c_*:=\frac2{\ln2};
   \tag{2}
   \]
3. the physical restriction influence telescope
   \[
   I(f)=p_i+\frac{I(f_{i,+})+I(f_{i,-})}{2};
   \tag{3}
   \]
4. the block sandwich
   \[
   B_A\le\Delta_AH\le2B_A;
   \tag{4}
   \]
5. the concave restriction cap
   \[
   \Delta_iH\le\Psi(j_i),
   \qquad j_i=\min\{p_i,1-p_i\},
   \tag{5}
   \]
   where
   \[
   \Psi(t)=h_2(t)+1-h_2\!\left(\frac12+\sqrt{t(1-t)}\right)
   \]
   and `kappa(t)=Psi(t)/t` is decreasing on `(0,1/2]`.

The current all-block critical-descendant/compiler continuation additionally proves that a finite uniform bound on a **proper-block** ratio `B_A/I_A` would imply FEI, with the physical-block lifetime cost telescoping exactly. The current block log-Sobolev continuation proves the sharper recombination estimate `R_A<=c_*M_A`. I use those results only at their stated scopes.

## 2. PROVED: block erasure is superadditive over singleton erasures

### Lemma 2.1 — conditional-erasure superadditivity

For every finite random vector `X=(X_1,...,X_n)` and every nonempty block `A`,

\[
\boxed{
B_A=H(X_A\mid X_{A^c})\ge\sum_{i\in A}H(X_i\mid X_{-i})
=\sum_{i\in A}B_i.
}
\tag{6}
\]

This is distributional; Booleanity is not needed.

### Proof

Order `A={i_1,...,i_k}`. The conditional chain rule gives

\[
B_A
=\sum_{t=1}^k
H\!\left(X_{i_t}\mid X_{A^c},X_{i_1},...,X_{i_{t-1}}\right).
\]

For each `t`, conditioning on all coordinates except `i_t` adds the as-yet-unrevealed variables `X_{i_{t+1}},...,X_{i_k}`. Since conditioning cannot increase entropy,

\[
H\!\left(X_{i_t}\mid X_{A^c},X_{i_1},...,X_{i_{t-1}}\right)
\ge H(X_{i_t}\mid X_{-i_t})=B_{i_t}.
\]

Summing proves (6). QED.

### Corollary 2.2 — proper-block selector collapses exactly to a singleton selector

If every `p_i>0` on the relevant coordinate set `R`, then for every nonempty `A subseteq R`,

\[
\frac{B_A}{I_A}
\ge
\frac{\sum_{i\in A}B_i}{\sum_{i\in A}p_i}
\ge
\min_{i\in A}\frac{B_i}{p_i}.
\tag{7}
\]

When `|R|>=2`, singleton blocks are proper. Therefore

\[
\boxed{
\min_{\varnothing\ne A\subsetneq R}\frac{B_A}{I_A}
=\min_{i\in R}\frac{B_i}{p_i}.
}
\tag{8}
\]

So **larger physical blocks can never improve the local erasure-selector coefficient `B_A/I_A` below the best singleton coefficient**. The block theory remains useful for recombination geometry, dependence across cuts, and adaptive identities, but the bare `B_A/I_A` proper-block selector has no strictly stronger existential power than a coordinate selector.

This identifies precisely why searching over larger blocks alone cannot remove the surviving selector obstruction.

## 3. PROVED: the singleton erasure-selector constant is additively equivalent to FEI

Define the optimal singleton erasure-selector constant

\[
K_E:=
\sup_{f\ \mathrm{nonconstant}}
\min_{i:p_i>0}\frac{B_i(f)}{p_i}.
\tag{9}
\]

Let `C_FEI` denote the optimal universal FEI constant in the extended sense.

### Theorem 3.1 — additive selector compiler

If `K_E<infinity`, then

\[
\boxed{
C_{\rm FEI}\le K_E+\min\{K_E,c_*\},
\qquad c_*=\frac2{\ln2}.
}
\tag{10}
\]

Conversely, if FEI holds with constant `C`, then

\[
\boxed{K_E\le C.}
\tag{11}
\]

Hence finiteness of the full FEI constant is equivalent to finiteness of the **coordinate mass-weighted erasure-selector constant**. Once `K_E>=c_*`, the compiler loses only the additive surcharge `c_*`, rather than the factor two from the raw `JS_i<=B_i` estimate.

### Proof of (10)

Fix a nonconstant Boolean `f`. By definition of `K_E`, choose a relevant coordinate `i` with

\[
B_i\le K_Ep_i.
\tag{12}
\]

From (1)--(2), simultaneously

\[
\Delta_iH=B_i+JS_i\le2B_i\le2K_Ep_i
\]

and

\[
\Delta_iH\le B_i+c_*p_i\le(K_E+c_*)p_i.
\]

Thus

\[
\Delta_iH\le C_0p_i,
\qquad C_0:=K_E+\min\{K_E,c_*\}.
\tag{13}
\]

Induct on the number of relevant coordinates. Constants have `H=I=0`. For a nonconstant state choose `i` as above. Assuming the two restrictions satisfy `H<=C_0I`, the entropy and influence restriction telescopes give

\[
\begin{aligned}
H(f)
&=\Delta_iH+\frac{H(f_{i,+})+H(f_{i,-})}{2}\\
&\le C_0p_i+rac{C_0}{2}\bigl(I(f_{i,+})+I(f_{i,-})\bigr)\\
&=C_0I(f).
\end{aligned}
\]

The dimension strictly decreases, so the induction terminates. This proves (10).

### Proof of (11)

For every random vector,

\[
\sum_iH(X_i\mid X_{-i})\le H(X).
\tag{14}
\]

Indeed, for any ordering, each `H(X_i|X_-i)` is at most the corresponding forward-chain term `H(X_i|X_{<i})`, whose sum is `H(X)`. Therefore

\[
\sum_iB_i\le H(f)\le C I(f)=C\sum_ip_i.
\]

A weighted-average argument gives at least one relevant `i` with `B_i/p_i<=C`. Taking the supremum over `f` proves (11). QED.

### Numerical calibration, not closure

Hod's explicit construction gives the rigorous lower bound

\[
C_{\rm FEI}\ge 6.4547837\ldots
\]

while

\[
c_*=2/\ln2=2.885390081777\ldots.
\]

Therefore any finite `K_E` must exceed `c_*`; otherwise (10) would imply `C_FEI<=2c_*<6.4547837`. In the finite case one consequently has the sharper additive comparison

\[
\boxed{
C_{\rm FEI}-\frac2{\ln2}\le K_E\le C_{\rm FEI}.
}
\tag{15}
\]

At the Hod scale, the necessary selector threshold is at least

\[
6.4547837-2/\ln2=3.5693936182\ldots.
\tag{16}
\]

Equation (15) is an equivalence of **finiteness plus constants up to an additive universal surcharge**; it is not a proof that either optimal constant is known.

## 4. PROVED: a sharper candidate-`C` reduction to a low-influence erasure selector

The concave restriction cap removes all coordinates above a fixed influence scale. This yields a more precise remaining universal target than merely proving `K_E<infinity`.

Fix `C>=4`. Let `tau(C) in (0,1/2]` be the unique solution of

\[
\frac{\Psi(\tau(C))}{\tau(C)}=C
\tag{17}
\]

whenever this solution lies in the interval covered by the inherited decreasing-`kappa` theorem.

### Theorem 4.1 — low-influence existential erasure selector implies FEI(C)

Assume the following statement:

> For every nonconstant Boolean `h` whose relevant coordinates all satisfy
> \[
> 0<p_i<\tau(C),
> \]
> there exists at least one relevant coordinate `i` such that
> \[
> \boxed{B_i(h)\le(C-c_*)p_i.}
> \tag{18}
> \]

Then every Boolean function satisfies

\[
\boxed{H(f)\le C I(f).}
\tag{19}
\]

### Proof

It suffices, by the same restriction induction used above, to show that every nonconstant Boolean state has **some** coordinate with `Delta_iH<=Cp_i`.

Fix a state `h`.

- If some relevant `p_i>=1/2`, the universal bound `Delta_iH<=2` gives
  \[
  \Delta_iH\le2\le4p_i\le Cp_i.
  \]
- Otherwise all `p_i<1/2`. If some `p_i>=tau(C)`, (5) and monotonicity of `kappa` give
  \[
  \frac{\Delta_iH}{p_i}\le\frac{\Psi(p_i)}{p_i}\le C.
  \]
- The only remaining case is `p_i<tau(C)` for every relevant coordinate. Apply hypothesis (18), then (1)--(2):
  \[
  \Delta_iH=B_i+JS_i
  \le(C-c_*)p_i+c_*p_i
  =Cp_i.
  \]

Thus an existential coordinate payment exists at every nonconstant state, and restriction induction proves (19). QED.

At the Hod-scale calibration `C=6.4547837`, the recovered concave-cap inversion is approximately

\[
\tau(C)\approx0.1805539925,
\]

and the missing selector (18) becomes

\[
\boxed{
\exists i:\quad
B_i\le3.5693936182\ldots\,p_i
\qquad\text{whenever all }p_i<0.1805539925\ldots.
}
\tag{20}
\]

This is **not proved here**. It is the sharpened remaining universal obligation.

The quantifiers now exactly match the inherited critical-descendant obstruction: if FEI(C) fails, a maximal-ratio physical restriction descendant has all coordinates below `tau(C)` and every coordinate violates (18). Thus the proof problem is no longer obscured by an every-function/every-coordinate upper-payment statement; it is an **existential coordinate selector on the low-influence regime**, while hypothetical counterexamples localize to a descendant where all coordinates fail it.

## 5. Exact dependence reformulation

For every coordinate,

\[
B_i=H(X_i\mid X_{-i})
=h_2(p_i)-I(X_i;X_{-i}).
\tag{21}
\]

Therefore the missing low-influence selector (18) is exactly the claim that some coordinate satisfies

\[
\boxed{
I(X_i;X_{-i})
\ge h_2(p_i)-(C-c_*)p_i.
}
\tag{22}
\]

In words: **some rare spectral membership bit must be sufficiently predictable from the rest of the spectral sample to pay the product-marginal entropy excess**. This is the mass-weighted dependence statement that the product-spectrum endpoint lacks: an arbitrary independent random set with many tiny marginals has zero left side and violates (22), while Boolean Fourier spectra cannot be arbitrary product laws.

There is also an exact block form. Let

\[
\operatorname{TC}(X)=\sum_i h_2(p_i)-H(X).
\]

For every block `A`,

\[
\boxed{
B_A-KI_A
=
\sum_{i\in A}\bigl(h_2(p_i)-Kp_i\bigr)
-igl(\operatorname{TC}(X)-\operatorname{TC}(X_{A^c})\bigr).
}
\tag{23}
\]

This follows by writing

\[
B_A=H(X)-H(X_{A^c})
\]

and expanding both entropies as product-marginal entropy minus total correlation. Thus a block erasure selector is exactly a statement that the **increment of total correlation created by adding `A`** pays the product-marginal excess of `A`.

For a co-singleton `A=R\setminus\{i\}`,

\[
B_A-KI_A
=
\sum_{j\ne i}\bigl(h_2(p_j)-Kp_j\bigr)-\operatorname{TC}(X),
\tag{24}
\]

because a singleton has zero total correlation. This gives a clean diagnostic criterion for co-singleton blocks, but Corollary 2.2 shows that it cannot beat the best singleton coefficient. The genuinely useful next step is therefore not a larger-block search by itself; it is a **Booleanity theorem forcing (22) for at least one rare coordinate**, naturally interacting with the current product-phase/curl-free stability work.

## 6. Failed shortcut preserved

A tempting inference is that the new all-block critical-core theorem should make the proper-block selector easier because one may optimize over many blocks. Equation (8) kills that shortcut at the exact erasure level: every block ratio is bounded below by a weighted average of singleton erasure ratios. If every singleton has `B_i/p_i>K`, then every nonempty block has `B_A/I_A>K` as well.

So larger blocks do **not** create a missing existential erasure payment. Their value is in the recombination term, cut mutual information, prediction error `M_A`, or other genuinely block-sensitive Boolean structure.

Likewise, nothing in this report changes the earlier counterexample to a universal upper payment for **every prescribed coordinate**. The sufficient theorem uses `exists i` at each state. The restriction-critical theorem says only that a hypothetical global counterexample can be localized to a special descendant where `for all i` the opposite lower inequality holds.

## 7. Literature / priority discipline

A current check of González--MacManus--Pereyra, arXiv:2606.00246 (29 May 2026), confirms the closely related restriction-decrement/stopping-tree paradigm: a suitable coordinate inequality at branching nodes, together with FEI at stopping nodes, compiles to FEI. Hod's lower-bound paper gives the explicit `>6.454784` obstruction scale used only for calibration here.

The conditional-entropy monotonicity behind Lemma 2.1 is elementary information theory and should be treated as folklore unless a priority search proves otherwise. I did not locate, in the bounded current repository/literature search, the exact package (8), (10), and (18)--(22), but **search failure is not evidence of novelty**. Publication priority is `UNVERIFIED`.

## 8. Genuine before / after and next exact obligation

**Before this run:** the current fleet had (i) a maximal-ratio descendant critical for every coordinate and every physical block, (ii) a proper-block selector compiler with a factor-two loss, (iii) an all-dimensional recombination payment via `M_A`, and (iv) product-spectrum/sign-phase rigidity. The proper-block selector still looked like a potentially stronger search space than the singleton selector.

**After this run:**

1. `B_A>=sum_{i in A}B_i` proves that the local proper-block erasure selector is **exactly** the singleton erasure selector; searching larger blocks cannot improve `B_A/I_A`.
2. The singleton selector constant `K_E` is equivalent to full FEI finiteness, with the sharper compiler
   \[
   C_{FEI}\le K_E+\min(K_E,2/\ln2),
   \]
   and hence, in the finite regime forced by the known lower bound,
   \[
   C_{FEI}-2/\ln2\le K_E\le C_{FEI}.
   \]
3. At a candidate coefficient `C>=4`, full FEI reduces to the exact low-influence existential selector (18), equivalently the mutual-information payment (22). At the Hod scale the target coefficient is `3.5693936182...` below influence `0.1805539925...`.

**Remaining universal obligation:** prove (18)/(22) for some finite `C` (or directly at a target `C`) using Booleanity. The most compatible current frontier is the product-phase/curl-free obstruction: show that a Boolean Fourier sign phase cannot keep **every** rare membership bit simultaneously so unpredictable that

\[
I(X_i;X_{-i})<h_2(p_i)-(C-c_*)p_i
\]

for all relevant `i` while also satisfying the exact Boolean convolution identities. A counterexample Boolean family to that existential dependence statement would decisively redirect the selector route.

**Suggested dated README ledger line:** `2026-09-21 B14/fleet02: proved block erasure superadditivity B_A>=sum_{i in A}B_i, so the proper-block B_A/I_A selector collapses exactly to the best singleton B_i/Inf_i selector. Defined K_E=sup_f min_i B_i/Inf_i and proved C_FEI<=K_E+min(K_E,2/ln2), K_E<=C_FEI; candidate FEI(C), C>=4, reduces to an existential low-influence selector B_i<=(C-2/ln2)Inf_i below tau(C), equivalently I(X_i;X_-i)>=h_2(Inf_i)-(C-2/ln2)Inf_i. Full FEI remains OPEN.`
