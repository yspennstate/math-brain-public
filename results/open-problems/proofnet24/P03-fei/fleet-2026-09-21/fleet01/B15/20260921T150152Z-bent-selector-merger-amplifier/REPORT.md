# B15 — bent-selector merger amplifier: raw carry gain is not influence-payable

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** Authenticated GitHub was used for the control plane and private FEI handoffs, but no authenticated mathematical/cognitive brain retrieval or receiver context was consumed.  
**Model self-report:** GPT-5.6 Sol. **Reasoning effort configured/provider usage:** UNKNOWN / not exposed.  
**Route:** owner-directed APPROACH 4/8, spectral magnitude/arithmetic structure. Creative moves used: **#2 attack the negation** (try to destroy a local merger-payment inequality), **#18 change language** (rewrite restriction as transfer between valuation and arithmetic free energy), and **#30 isolate one scale** (one selector coordinate over a bent branch).

The latest handoff proved a dimension-free budget for carry jumps *inside a fixed parent magnitude packet* and isolated the remaining cross-magnitude merger obstruction. This run asks the next exact question:

> Can the raw carry/valuation created by a restriction merger be paid by that coordinate's influence, perhaps helped by the entropy or number of the ancestry labels that merge?

The answer is **no**, by an explicit infinite Boolean family. At the same time there is an exact universal compensation identity showing what quantity survives the counterexample: the arithmetic remainder drop minus the valuation gain. The family makes the two discarded terms individually grow like `r/2` while their difference stays `O(1)`.

The stale conjecture that Hod's `beta(1/2)` is the universal FEI constant is not used: the current owner handoff records Numaro's external 18-variable lower bound above it. Full FEI remains OPEN.

## 1. Arithmetic notation and an exact restriction-transfer identity

For a Boolean function `f`, group nonzero Fourier coefficients by their distinct magnitudes `a`. As in the spectral-lattice handoff, write

\[
A_a=\{S:|\widehat f(S)|=a\},\qquad
p_a=|A_a|a^2,
\]

\[
V_a(x)=\sum_{S\in A_a}\operatorname{sgn}(\widehat f(S))\chi_S(x),
\qquad
r_a=\min_{V_a(x)\ne0}\nu_2(V_a(x)),
\]

and

\[
b_a=a2^{r_a},\qquad
R(f)=\sum_a p_a r_a,\qquad
D(f)=\sum_a p_a\log_2\frac1{b_a}.
\]

The inherited exact identity is

\[
\boxed{H(f)=2R(f)+2D(f).}\tag{1}
\]

Fix coordinate `i`, and let `f_+`,`f_-` be its two restrictions. Define the raw average valuation gain and arithmetic-remainder drop

\[
G_i(f)=\frac{R(f_+)+R(f_-)}2-R(f),\tag{2}
\]

\[
L_i(f)=D(f)-\frac{D(f_+)+D(f_-)}2.\tag{3}
\]

### Theorem 1 (exact compensated restriction transfer)

For every Boolean `f` and every coordinate `i`,

\[
\boxed{
L_i(f)-G_i(f)
=\frac12\left(H(f)-\frac{H(f_+)+H(f_-)}2\right).
}\tag{4}
\]

In particular, using the standard restriction entropy identity,

\[
\boxed{L_i(f)-G_i(f)\ge0.}\tag{5}
\]

Thus whenever restriction creates positive raw valuation/carry, the arithmetic remainder necessarily drops by at least the same amount. The positive carry is not, by itself, an unpaid entropy debit.

**Proof.** Apply (1) to `f,f_+,f_-` and subtract the child average from the parent:

\[
H(f)-\frac{H(f_+)+H(f_-)}2
=2\left(R(f)-\frac{R(f_+)+R(f_-)}2\right)
 +2\left(D(f)-\frac{D(f_+)+D(f_-)}2\right)
=2(L_i-G_i).
\]

The restriction identity from the current FEI handoff writes the left side as a Jensen-Shannon term plus a nonnegative binary-entropy term, hence it is nonnegative. QED.

Equation (4) is elementary once (1) is available, but it changes the correct target for the arithmetic route. Bounding `G_i` and `L_i` separately can throw away an arbitrarily large cancellation, as the family below proves.

## 2. The bent-selector family

Let `r>=2`, put `q=2^{-r}` and `M=2^{2r}=q^{-2}`. On `2r` bits write

\[
g_r(y)=(-1)^{y_1y_2+y_3y_4+\cdots+y_{2r-1}y_{2r}}.\tag{6}
\]

For one pair, the unnormalised Walsh transform of `(-1)^{uv}` is `(2,2,2,-2)`. Tensoring the pairs gives

\[
\boxed{|\widehat g_r(T)|=q\quad\text{for every }T,\qquad \widehat g_r(\varnothing)=q.}\tag{7}
\]

Hence `g_r` is bent, its unique magnitude packet has `M` coefficients, and if `epsilon_T=sign(ghat_r(T))`, then

\[
\sum_T\epsilon_T\chi_T(y)=2^r g_r(y).
\]

Therefore that packet has exact carry depth `r`.

Add one selector bit `t`. Define

\[
F_r(y,t)=\begin{cases}
g_r(y),&t=0,\\-1,&t=1.\end{cases}\tag{8}
\]

Taking `chi_t(t)=(-1)^t`,

\[
F_r(y,t)=\frac{g_r(y)-1}{2}+\chi_t(t)\frac{g_r(y)+1}{2}.\tag{9}
\]

For `T ne empty`, both parent coefficients `T` and `T union {t}` equal

\[
\frac q2\epsilon_T.
\]

At the two exceptional labels,

\[
\widehat F_r(\varnothing)=-\frac{1-q}{2},\qquad
\widehat F_r(\{t\})=\frac{1+q}{2}.\tag{10}
\]

Thus, for `r>=2`, the parent has exactly three distinct magnitudes:

\[
\frac q2 \quad\text{with multiplicity }2(M-1),
\qquad
\frac{1-q}{2},\qquad
\frac{1+q}{2},\tag{11}
\]

where the last two are singletons.

## 3. Parent carry is uniformly shallow

The two singleton packets in (11) have carry depth zero. The signed mask of the `q/2` packet is

\[
V_0(y,t)
=(1+\chi_t(t))\sum_{T\ne\varnothing}\epsilon_T\chi_T(y)
=(1+\chi_t(t))(2^r g_r(y)-1).\tag{12}
\]

The second factor is always odd. Whenever (12) is nonzero its value is twice an odd integer, so

\[
\boxed{r_{q/2}=1.}\tag{13}
\]

Hence every parent packet has depth at most one, uniformly in `r`.

Its mass is

\[
p_0=2(M-1)(q/2)^2=\frac{1-q^2}{2},\tag{14}
\]

so

\[
\boxed{R(F_r)=\frac{1-q^2}{2}.}\tag{15}
\]

## 4. One restriction creates arbitrarily deep carry from two depth-zero ancestry groups

On the `t=0` branch the child is `g_r`, hence

\[
R((F_r)_+)=r,\qquad D((F_r)_+)=0.\tag{16}
\]

On the `t=1` branch the child is the constant `-1`, hence

\[
R((F_r)_-)=D((F_r)_-)=0.\tag{17}
\]

More is true. Split the unique child magnitude packet of `g_r` according to its parent-pair ancestry.

* The `M-1` nonempty child labels arise from the repeated small parent magnitude pair `(q/2,q/2)`. Their signed mask is

\[
W_{\rm bulk}(y)=2^r g_r(y)-1,
\]

which is odd at every point, so its carry depth is zero.

* The empty child label arises from the **unequal** exceptional parent pair `((1-q)/2,(1+q)/2)`. Its signed mask is the singleton `1`, again depth zero.

Yet their sum is

\[
W_{\rm bulk}+1=2^r g_r,
\]

of exact depth `r`. Therefore

\[
\boxed{\text{two depth-zero ancestry groups can merge into a child packet of arbitrarily large carry depth }r.}\tag{18}
\]

The ancestry group sizes are exactly `M-1` and `1`. In the child spectral distribution all `M` atoms have equal mass `1/M=q^2`, so the entropy of the binary ancestry label is

\[
\boxed{h_2(q^2)\longrightarrow0.}\tag{19}
\]

Thus neither the number of ancestry classes (always two) nor their label entropy measures the amount of carry that can be created.

## 5. Raw merger valuation gain is not influence-payable

From (15)--(17),

\[
G_t(F_r)=\frac r2-\frac{1-q^2}{2}
=\boxed{\frac{r-1+q^2}{2}}.\tag{20}
\]

The selector coordinate is influential exactly when `g_r(y)=+1`. Since `E g_r=q`,

\[
\boxed{\operatorname{Inf}_t(F_r)=\frac{1+q}{2}.}\tag{21}
\]

Consequently

\[
\frac{G_t(F_r)}{\operatorname{Inf}_t(F_r)}
=\frac{r-1+q^2}{1+q}\longrightarrow\infty.\tag{22}
\]

Even adding the ancestry-label entropy does not help:

\[
\frac{G_t(F_r)}{\operatorname{Inf}_t(F_r)+h_2(q^2)}\longrightarrow\infty.\tag{23}
\]

### Corollary 2 (two natural merger-payment lemmas are false)

There is no universal finite constant `C` such that for every Boolean function and every coordinate

\[
G_i(f)^+\le C\operatorname{Inf}_i(f),\tag{24}
\]

nor one such that the right side is replaced by `C(Inf_i + ancestry-label entropy)` for the natural parent-pair ancestry partition above.

This does **not** refute FEI. It refutes a raw local payment strategy for the arithmetic valuation term.

## 6. The missing `O(r)` is exactly returned by the arithmetic remainder

For the two children in (16)--(17), `D=0`. Thus

\[
L_t(F_r)=D(F_r).\tag{25}
\]

By Theorem 1,

\[
\boxed{D(F_r)=G_t(F_r)+\frac{\Delta_tH(F_r)}2},\qquad
\Delta_tH(F_r)=H(F_r)-\frac{H(g_r)+H(-1)}2=H(F_r)-r.\tag{26}
\]

The parent Fourier probabilities consist of

* `2(M-1)` atoms of probability `q^2/4`,
* one atom of probability `(1-q)^2/4`,
* one atom of probability `(1+q)^2/4`.

A direct calculation gives

\[
\boxed{
\Delta_tH(F_r)
=2-rq^2-rac12\Big[(1-q)^2\log_2(1-q)+(1+q)^2\log_2(1+q)\Big].
}\tag{27}
\]

Therefore

\[
\Delta_tH(F_r)\to2,\qquad
\frac{\Delta_tH(F_r)}{\operatorname{Inf}_t(F_r)}\to4,\tag{28}
\]

while both `G_t(F_r)` and `L_t(F_r)` grow like `r/2`.

Equivalently,

\[
\boxed{
\frac{L_t(F_r)-G_t(F_r)}{\operatorname{Inf}_t(F_r)}\to2,
\quad
\frac{G_t(F_r)}{\operatorname{Inf}_t(F_r)}\to\infty,
\quad
\frac{L_t(F_r)}{\operatorname{Inf}_t(F_r)}\to\infty.
}\tag{29}
\]

This is the main structural lesson of the run: **the large carry created by unequal-magnitude merging is paired with an equally large free-energy drop. The FEI-scale object is their compensated difference, not either ledger separately.**

The family is particularly sharp for the previous handoff because the child carry `r` is produced by exactly two ancestry classes, one of which is a single coefficient. A lower bound based on "many labels must participate in deep carry" is therefore false.

## 7. Exact finite self-check

`bent_selector_merger_check.py` uses only integer Walsh transforms and exact rational arithmetic for the finite assertions. It checks `r=2,...,6`:

* the bent spectrum has one magnitude;
* the parent has the three multiplicities in (11);
* the parent packet depths are `1,0,0`;
* the child packet has depth `r`;
* the two ancestry groups separately have depth zero;
* the selector influence and raw valuation gain equal (20)--(21).

The committed output ends in `PASS`. Before commit, the deterministic local byte hashes were

* checker SHA-256 `eb4cb88d5aa49b36bdeaf9001da2e3062b7c9357f6c7d84adda23dd472d9ab97`;
* output SHA-256 `76f3b21743ec32d1497fbe8478e64f4e198fe8c1cec49e6cc6dceb367141a0b6`.

The general theorem is proved algebraically above and does not rely on the finite check.

## 8. Relation to current FEI work and literature

The 18 September 2026 Potapov preprint `arXiv:2609.21563` proves FEI with sharp constant 4 for plateaued Boolean functions. The child `g_r` is in that structured class, but the selector `F_r` has three Fourier magnitudes for `r>=2`, so this construction is outside the one-packet conclusion used there. The May/June 2026 González--MacManus--Pereyra preprint `arXiv:2606.00246` develops a restriction/stopping-tree FEI route; Theorem 1 above is an arithmetic rewriting of the same restriction entropy drop, not a claim that their general missing inequality has been solved.

No publication-priority claim is made for the bent-selector construction or the arithmetic reformulation. They are new-to-this-private-route deductions unless a later literature check shows otherwise.

## 9. Before / after / next obligation

**Before:** the B15 route had paid carry jumps within a fixed parent magnitude packet and knew, from a minimal three-bit Boolean example, that unequal parent magnitudes could create a new carry-positive child packet. The proposed next step was to pay merger-created carry jointly with influence and the magnitude/free-energy change.

**After:** the new family proves that the first two pieces cannot pay raw merger carry even qualitatively: a single coordinate of influence tending to `1/2`, and only two ancestry classes with entropy tending to zero, can create depth `r` and raw mass-weighted valuation gain about `r/2`. At the same time the universal identity (4) proves that the arithmetic remainder automatically supplies an equally large opposite transfer. The cancellation is not optional; it is forced by the exact entropy decomposition.

**Next B15 target:** stop seeking separate universal upper bounds on merger-created `R` or on the `D` drop. Work directly with the compensated quantity

\[
L_i-G_i=\frac12\Delta_iH,
\]

and use the merger graph only to find a coordinate for which this **difference** is `O(Inf_i)`. A genuinely new arithmetic lemma would need to exploit relations between ancestry collisions across different coordinates, because the one-coordinate raw ledgers can each be arbitrarily large. The bent-selector family is now a mandatory stress test for every such proposal.

**Bottom line:** full FEI remains **OPEN**. This run gives a rigorous infinite obstruction to raw merger-payment schemes and an exact compensation law identifying the only restriction-scale arithmetic combination that survives it.
