# B15 — global one-sided magnitude flow and a 3/2 FEI reduction

**Status:** **OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval/context was used in this mathematics.  
**Route:** the fixed-coordinate Booleanity route from APPROACH 13 has now met a sharp bent-one-flip obstruction, so this run switches explicitly to APPROACHES 1/4: interpret the unequal-magnitude term as a global compression / spectral-height flow and try to pay it only after summing over coordinates.  
**Novelty:** no publication-priority claim is made.

The live handoff already contains three facts that this report treats as inputs rather than re-auditing:

1. with `u_T = fhat(T)` and `v_T = fhat(T union {i})`,
   \[
   L_i(f)=\sum_{T:v_T\ne0}v_T^2\log_2^+\frac{|u_T|}{|v_T|},
   \]
   and
   \[
   \Delta_iH\le \frac3{\ln2}\operatorname{Inf}_i(f)+2L_i(f);
   \tag{1}
   \]
2. the local Boolean constraints alone cannot bound `L_i/Inf_i`: the bent-one-flip family has a selector coordinate with this ratio tending to infinity while other coordinates are easy;
3. the rare-tribes family that makes the separate arithmetic remainder selector diverge has `L_i/Inf_i -> 0`.

The point of the present run is to stop paying the one-sided magnitude term coordinate-by-coordinate and instead keep its exact global spectral-lattice flow.

---

## 1. Exact global quantity

Put

\[
p_S=\widehat f(S)^2,\qquad
\alpha_i=\operatorname{Inf}_i(f)=\sum_{S\ni i}p_S,
\]

and define the aggregate one-sided magnitude flow

\[
\boxed{\mathcal A(f):=\sum_i L_i(f).}
\tag{2}
\]

Since

\[
\log_2\frac{|\widehat f(S\setminus\{i\})|}{|\widehat f(S)|}
=\frac12\log_2\frac{p_{S\setminus\{i\}}}{p_S},
\]

we have the exact Boolean-lattice edge representation

\[
\boxed{
\mathcal A(f)
=\frac12\sum_{S}p_S\sum_{i\in S}
\left[\log_2\frac{p_{S\setminus\{i\}}}{p_S}\right]_+.
}
\tag{3}
\]

Equivalently: choose an oriented downward edge `(S,i)` with weight `p_S`; `A/I` is one half of the expected positive log-density gain per downward spectral edge, after normalising by the total edge mass

\[
I(f)=\sum_S |S|p_S.
\tag{4}
\]

This is the coupling that the separate `R+D` bookkeeping loses. If a coefficient in packet `a` is joined downward to a coefficient in a larger-magnitude packet `b>a`, that edge contributes exactly

\[
a^2\log_2(b/a).
\tag{5}
\]

Writing the spectral-lattice height as

\[
h_a:=\log_2(1/a)=r_a+d_a,
\qquad d_a:=\log_2(1/b_a),
\]

(5) is

\[
a^2[h_a-h_b]_+.
\tag{6}
\]

Thus the valuation depth `r` and physical mesh depth `d` remain coupled until after the one-sided edge current is formed. This is exactly the kind of coupling required by the fresh valuation-tail blindness obstruction: the hard rare-isolation examples can move almost all FEI difficulty into mesh depth while making every valuation stop-loss tail disappear.

---

## 2. CONDITIONAL theorem: a global 3/2 inequality would prove FEI

### Proposition 2.1 — aggregate magnitude-flow reduction

Suppose there is a finite universal `kappa` such that every Boolean function satisfies

\[
\boxed{\mathcal A(f)\le\kappa I(f).}
\tag{7}
\]

Then full FEI holds with constant

\[
\boxed{C=\frac3{\ln2}+2\kappa.}
\tag{8}
\]

### Proof

For every nonconstant `f`,

\[
\frac{\mathcal A(f)}{I(f)}
=\sum_{i:\alpha_i>0}\frac{\alpha_i}{I(f)}
\frac{L_i(f)}{\alpha_i}.
\tag{9}
\]

Therefore (7) supplies a relevant coordinate `i` with

\[
L_i\le\kappa\alpha_i.
\]

Insert this into (1):

\[
\Delta_iH\le\left(\frac3{\ln2}+2\kappa\right)\alpha_i.
\]

The average total influence of the two restrictions is exactly `I(f)-alpha_i`. Induction on dimension therefore gives (8). QED.

The particularly focused target is now

\[
\boxed{\mathcal A(f)\stackrel{?}{\le}\frac32 I(f).}
\tag{10}
\]

If (10) were proved, it would give the explicit universal FEI constant

\[
\boxed{C=3+\frac3{\ln2}=7.32808512266689\ldots.}
\tag{11}
\]

**Equation (10) is OPEN / CONJECTURAL. It is not proved in this report.** The reason to isolate `3/2` is empirical and structural: the strongest current recursive Numaro benchmark below approaches `1.488911...`, while the fixed-coordinate `3/2` target from the preceding isoperimetric handoff was already the narrow surviving selector regime.

---

## 3. PROVED dead route: the two coarse local upper bounds cannot prove (10)

The fresh isoperimetric handoff proves for every coordinate

\[
L_i\le J_i,
\qquad
L_i\le\frac{\alpha_i}{2}\log_2\frac1{\alpha_i},
\tag{12}
\]

where

\[
J_i=\sum_{S\ni i}(|S|-1)p_S.
\]

It is tempting to sum the minimum of the two right sides and try to prove (10). The rare-tribes family shows that this loses exactly the magnitude cancellation we need.

Take `m` disjoint width-`w` blocks and the transitive rare-tribes function from the current handoff. Put

\[
\varepsilon=2^{-w},\qquad q=1-\varepsilon.
\]

For every physical coordinate,

\[
\alpha_i=2\varepsilon q^{m-1}.
\tag{13}
\]

Conditional on the spectral sample containing `i`, the nonempty Fourier label inside `i`'s own block is uniform over the `2^{w-1}` subsets that contain `i`, because every nonempty within-block Fourier coefficient has the same magnitude. Hence the expected number of *other* variables from that block is `(w-1)/2`, and therefore

\[
\boxed{\frac{J_i}{\alpha_i}\ge\frac{w-1}{2}.}
\tag{14}
\]

Also, from (13),

\[
\frac12\log_2\frac1{\alpha_i}
=\frac12\left(w-1-(m-1)\log_2 q\right)
>\frac{w-1}{2}.
\tag{15}
\]

Thus the *best of the two universal coarse bounds* in (12), after division by `alpha_i`, is still at least `(w-1)/2` and diverges with `w`.

But the exact unequal-magnitude calculation already proves

\[
\frac{L_i}{\alpha_i}\longrightarrow0
\qquad(w\to\infty,\ m\text{ fixed}).
\tag{16}
\]

Therefore:

> **REFUTED proof strategy.** No argument that first replaces every `L_i` by only `min{J_i, (alpha_i/2)log(1/alpha_i)}` can establish any dimension-free aggregate bound such as (10).

This does **not** refute (10) or FEI. It says that the exact one-sided unequal-magnitude edge orientation in (3) must be retained.

---

## 4. PROVED: exact aggregate recursion under balanced disjoint composition

Let `G:{-1,1}^m->{-1,1}` and `H:{-1,1}^n->{-1,1}` be balanced, and let

\[
F=G(H_1,\ldots,H_m)
\]

with disjoint copies `H_j`. For outer coordinate `i`, write

\[
\alpha_i^G=\operatorname{Inf}_i(G),
\]

and, with `a_K=Ghat(K)`, `b_K=Ghat(K union {i})`, define

\[
M_i(q)=\sum_{K:b_K\ne0}b_K^2
\log_2^+\frac{|a_K|}{|b_K|q}.
\tag{17}
\]

For an inner coordinate `x`, put

\[
p_x=\operatorname{Inf}_x(H),\qquad
q_x=|\widehat H(\{x\})|.
\]

The preceding B15 composition theorem gives leafwise

\[
L_{i,x}(F)=\alpha_i^G L_x(H)+q_x^2M_i(q_x).
\]

Summing exactly over all outer blocks and all inner coordinates gives the new aggregate form

\[
\boxed{
\mathcal A(F)
=I(G)\mathcal A(H)
+\sum_x q_x^2\sum_{i=1}^m M_i(q_x).
}
\tag{18}
\]

Together with

\[
I(F)=I(G)I(H),
\]

this becomes

\[
\boxed{
\frac{\mathcal A(F)}{I(F)}
=
\frac{\mathcal A(H)}{I(H)}
+
\frac{1}{I(G)I(H)}
\sum_xq_x^2\sum_iM_i(q_x).
}
\tag{19}
\]

So fixed balanced composition increases the aggregate ratio by an explicit nonnegative singleton-weighted correction. The correction retains precisely the one-sided magnitude information erased by entropy-only composition summaries.

For recursive self-composition of a fixed balanced non-dictator seed, the preceding pathwise theorem gives

\[
\theta:=\max_i\frac{|\widehat G(\{i\})|^2}{\operatorname{Inf}_i(G)}<1.
\]

If `s_*` is the least positive singleton magnitude of the seed, then the depth-`d` path correction is bounded by

\[
O_G\bigl((1+d)\theta^d\bigr).
\]

Consequently the aggregate ratios of the recursive self-compositions converge as well: they are influence-weighted averages of path ratios with a uniformly summable tail. This is a structured composition theorem, not a universal bound.

---

## 5. New numerical target: Numaro recursion approaches 1.488911 from below

The companion checker reconstructs the already recovered external 18-variable balanced monotone Numaro seed and refuses it unless the complete truth table has SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

For the seed itself,

\[
I=2.0390625,
\qquad
\frac{\mathcal A}{I}=0.6958068223803939.
\]

The two coordinate classes reproduce

\[
\frac{L_C}{\alpha_C}=0.6685747069331263,
\qquad
\frac{L_A}{\alpha_A}=2.2480374028746444,
\]

with

\[
\alpha_C=s_C=57/256,
\qquad
\alpha_A=s_A=1/256.
\]

Using (18)--(19) as a two-class influence-weighted dynamic program gives the following **exploratory floating-point** aggregate ratios for recursive self-composition:

| depth | `A/I` |
|---:|---:|
| 1 | 0.6958068223803938 |
| 2 | 1.2126357533691583 |
| 3 | 1.4059642037418676 |
| 4 | 1.4658359445425510 |
| 5 | 1.4827834955082390 |
| 6 | 1.4873341289629567 |
| 8 | 1.4888129069283760 |
| 10 | 1.4889052576450887 |
| 12 | 1.4889107123729763 |
| 15 | 1.4889110370453877 |

The exact fixed-seed tail mechanism is very small here: `theta=57/256` and `s_*=1/256`. The generic path-tail estimate after depth 15 is about `2.7e-8` even if the base `L_i/alpha_i` constant in that estimate is replaced by the safe coarse bound `4`. The displayed `1.488911...` values themselves are ordinary floating-point evaluations, not interval-certified values, so I do **not** promote `limit < 3/2` to a formal certificate here. The numerical margin is nevertheless large compared with the computed truncation tail and makes (10) a sharply targeted next statement rather than an arbitrary constant guess.

The same checker exhausts the *new statistic* `A/I` over all Boolean functions through dimension four; this is not a rerun of the settled FEI certificate sweep. It finds maxima

\[
0,\ 0,\ 0.396240625180289,\ 0.428422060767084
\]

for dimensions `1,2,3,4` respectively. On the rare-tribes obstruction, symmetry gives `A/I=L_i/alpha_i`, and representative exact-formula evaluations are

\[
0.00537064,\ 0.00537054,\ 0.00537033,\ 0.000457759,\ 0.000129699,
\]

for the parameter choices recorded in `CHECK_OUTPUT.txt`.

These computations do not prove (10); they identify its current stress point. In particular, the recursive Numaro family that strongly obstructs several restriction/cancellation constants sits strikingly close to, but below, `3/2` for this coupled magnitude-flow statistic.

---

## 6. What was attempted, what failed, and the next attack

### Exact statement attempted

Prove the universal global inequality

\[
\mathcal A(f)\le\frac32I(f).
\]

### What worked

- the exact spectral-edge / packet-height representation (3)--(6);
- the full-FEI reduction (7)--(11);
- the exact balanced-composition recursion (18)--(19);
- a proof that the two currently strongest generic pointwise bounds on `L_i` are fundamentally too lossy on rare tribes;
- a new numerical stress profile, with the recursive Numaro aggregate approaching about `1.488911`.

### Dead route

Summing `L_i<=min{J_i,(alpha_i/2)log(1/alpha_i)}` cannot prove any constant aggregate theorem: on rare tribes the surrogate diverges like at least `(w-1)/2` per influence unit while the true magnitude flow tends to zero.

### Next attack

Stay with the global packet-edge quantity rather than reverting to a fixed-coordinate likelihood inequality. Group the edges in (3) by magnitude packets and write every positive height drop as

\[
[(r_a-r_b)+(d_a-d_b)]_+.
\]

The next lemma should sum these **before** separating valuation and mesh ledgers, using the Boolean convolution/cut constraints to pair large positive mesh drops with reverse or lateral negative-credit edges. The concrete target is either:

1. prove `A<=3I/2`; or
2. produce a genuine Boolean counterexample with `A/I>3/2`, which would immediately tell us the correct constant or potential correction.

If the packet-edge transport stalls, the explicit next switch is APPROACH 10: tilt the spectral law by `rho^{2|S|}` and ask whether the one-sided height current in (3) is the endpoint of a semigroup dissipation quantity with a dimension-free integral bound.

Full FEI remains **OPEN**.

---

## Reproducibility

Companion files:

- `check_global_magnitude_flow.py`
- `CHECK_OUTPUT.txt`

Local source SHA-256 before commit:
`57226bcaec9d0125ca98831862b6d79b23c201ec2765a441faeb1d738801d5f5`

Recorded stdout SHA-256:
`50ad51f7732785dd064cf37579018c25dd2524da8af7e2130f5835cdb0761483`

The checker completed with return code `0`. The analytic statements in sections 1--4 do not infer a theorem from enumeration; the finite computations in section 5 are stress tests and numerical target selection only.
