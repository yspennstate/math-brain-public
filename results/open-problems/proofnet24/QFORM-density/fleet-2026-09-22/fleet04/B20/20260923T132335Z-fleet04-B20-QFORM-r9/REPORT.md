SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B20, 2026-09-23T13:23:35Z.
attacking: the first unpaid fleet01/B20 annular-versus-star implication by using one spectral window for both its diffuse ridge exit and its localized physical-row exit.

# fleet04/B20 r9 — annular-free tightened-core compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T132335Z-fleet04-B20-QFORM-r9`  
**Status:** `ESSENTIAL_STEP_APPLIED`; NEW SUPPORTING COMPILER; FULL QFORM OPEN.  
**Regularity:** continuity is obtained only in the paid ridge and D5 branches cited below.

## 1. Sources and correction gates

This report uses:

- Claude's corrected decoupling/Fresnel source at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`;
- fleet01/B20's strengthened two-scale compiler at `math-open-problems@bfa9412bfb743bd30fc104e779f280dce0a0db14`, especially its MSS spectral-window construction and the completed ridge receiver;
- fleet02/B20's arbitrary-rank N3 compiler at `math-open-problems@19327f690f815425717fcbd07854302df2090970`;
- the fleet04 correction-safe graph through `math-open-problems@751677f7d247a7d458630ea6a6397374984edc53`.

All random banks below consist of original coordinates. Spectral projections are deterministic matrix certificates only. No independence after rotation, worst-fiber conditional-density supremum, arbitrary-joint coarea, or deletion of a small random quadratic term is used.

## 2. New theorem

### `QFORM-N3-ONEWINDOW-RIDGE-OR-PHYSICALSTAR-v1`

Let \(A\) be real symmetric with at least three eigenvalues of modulus at least one and assume the tightened no-pivot conditions
\[
 |A_{ii}|<\tau,\qquad
 |A_{ii}A_{jj}-A_{ij}^{2}|<\tau\quad(i\ne j),
 \qquad \tau=\frac1{192}. \tag{2.1}
\]
Put
\[
P_\eta=\mathbf1_{\{|A|\ge\eta\}},\qquad
\eta=\frac1{12},\qquad \varepsilon=\frac1{80}. \tag{2.2}
\]
Then at least one of the following holds.

1. **Paid ridge branch.** \(Q=X^TAX\) has a continuous \(C_0\) density and
\[
\boxed{\|p_Q\|_\infty<239.109.} \tag{2.3}
\]

2. **Paid physical-pair branch.** Some literal \(2\times2\) principal block has
\[
|\det A[\{h,j\}]|\ge\frac1{61440},\qquad
s_{\min}(A[\{h,j\}])
\ge
\frac{1/61440}{\,1/192+\sqrt{193/36864}\,}. \tag{2.4}
\]
Hence the completed physical-pair receiver gives a universal density bound for the full ambient form.

3. **Physical star/four-direction packet.** There is a physical hub \(h\) and a partition
\[
h^c=J\mathbin{\dot\cup}K
\]
such that
\[
\sum_{j\in J}A_{hj}^{2}>\frac1{122880},\qquad
\sum_{k\in K}A_{hk}^{2}>\frac1{122880}, \tag{2.5}
\]
\[
\|A[J,K]\|_F^2>\frac{36481}{147456}, \tag{2.6}
\]
and either the D5 receiver pays with
\[
\|p_Q\|_\infty<199.674, \tag{2.7}
\]
or
\[
\sum_{r\le4}s_r(A[J,K])^2
>
\frac{2298303}{9437184}. \tag{2.8}
\]

Thus, inside the tightened N3 core, the separate annular-leverage survivor in fleet01/B20 disappears: the same spectral window pays diffusely by ridge or localizes into a literal original-coordinate pair/star packet.

### Proof

Assume first that
\[
\max_i(P_\eta)_{ii}\le\varepsilon. \tag{2.9}
\]
Apply the two-part MSS frame partition to the spectral subspace \(|A|\ge\eta\). Both physical banks have Gram floor
\[
\delta
=
1-\left(\frac1{\sqrt2}+\sqrt\varepsilon\right)^2
=
\frac{39}{80}-\frac1{\sqrt{40}}. \tag{2.10}
\]
For the high-spectral cross block \(B_0\), fleet01/B20's singular-value argument gives \(s_3(B_0)\ge\delta\), while its range leverage is at most \(\varepsilon/\delta\). Restoring the omitted spectral tail \(E\), \(\|E\|_{\rm op}<\eta\), gives the actual physical cross block \(B=B_0+E\) with
\[
s_3(B)\ge \sigma:=\delta-\eta. \tag{2.11}
\]
Choose
\[
\gamma=\frac{27}{40}\sigma. \tag{2.12}
\]
The completed ridge-stability lemma yields
\[
\max_i(K_\gamma)_{ii}
\le
\left(\sqrt{\frac{\varepsilon}{\delta}}
+\frac{\eta}{(27/40)\sigma}\right)^2. \tag{2.13}
\]
Since \(1/\sqrt{40}<4/25\),
\[
\delta>\frac{131}{400},\qquad
\sigma>\frac{293}{1200}. \tag{2.14}
\]
Consequently
\[
\sqrt{\frac{\varepsilon}{\delta}}<\sqrt{\frac5{131}}<\frac15,
\qquad
\frac{\eta}{(27/40)\sigma}<\frac{4000}{7911}. \tag{2.15}
\]
Moreover
\[
\frac15+\frac{4000}{7911}
=\frac{27911}{39555}
<\frac{707}{1000}
<\frac1{\sqrt2}; \tag{2.16}
\]
the middle inequality is the integer check \(27911000<27965385\), and \(707^2<500000\). Hence the ridge leverage in (2.13) is strictly below \(1/2\).

The three singular values in (2.11) imply
\[
\theta=\operatorname{tr}K_\gamma
\ge \frac3{1+(27/40)^2}
=\frac{4800}{2329}>2. \tag{2.17}
\]
Applying the completed \(q=1\) ridge theorem,
\[
\|p_Q\|_\infty
\le
\frac{\sqrt e}{\sqrt2\,\gamma}\frac{\theta}{\theta-2}
<
\frac{\sqrt e}{\sqrt2}
\frac{48000}{7911}\frac{2400}{71}
<239.109. \tag{2.18}
\]
This proves branch 1 and is an actual application of fleet01/B20 at a concrete inequality.

Now suppose (2.9) fails, and choose \(h\) with \((P_\eta)_{hh}>\varepsilon\). Since
\[
A^2\ge \eta^2 P_\eta,
\]
the literal physical row satisfies
\[
\sum_{j\ne h}A_{hj}^2
=(A^2)_{hh}-A_{hh}^2
>
\eta^2\varepsilon-\tau^2
=
\frac1{11520}-\frac1{36864}
=
\frac{11}{184320}. \tag{2.19}
\]
Put \(w_j=A_{hj}^2\) and \(T=1/23040\).

If some \(w_j\ge T\), then (2.1) gives
\[
|A_{hh}A_{jj}-A_{hj}^2|
\ge T-\tau^2
=\frac1{61440}. \tag{2.20}
\]
Also (2.1) implies \(w_j<\tau+\tau^2=193/36864\), so the operator norm of this principal block is at most
\[
\tau+\sqrt{\tau+\tau^2}.
\]
The determinant identity \(s_{\min}s_{\max}=|\det|\) proves (2.4), hence branch 2.

Otherwise every \(w_j<T\). Sort the weights, pair consecutive weights, append one zero if necessary, and orient every pair with one endpoint in \(J\) and one in \(K\). As in fleet01/B20, every orientation has discrepancy below \(T\). Equation (2.19) therefore gives
\[
\min\left(\sum_Jw_j,\sum_Kw_j\right)
>
\frac12\left(\frac{11}{184320}-\frac1{23040}\right)
=\frac1{122880}, \tag{2.21}
\]
which is (2.5).

Let \(C=A[h^c,h^c]\). Cauchy interlacing leaves at least one eigenvalue of \(C\) with modulus at least one. Writing \(C=D+Z\), with \(D\) diagonal and \(Z\) zero-diagonal, gives
\[
\|Z\|_{\rm op}>1-\tau=\frac{191}{192},
\qquad
\|Z\|_F^2>\frac{36481}{36864}. \tag{2.22}
\]
Randomly orient the pairs used above. Every unordered pair of distinct leaves is separated with probability at least \(1/2\), while (2.21) holds for every orientation. Hence some orientation also satisfies
\[
\|A[J,K]\|_F^2\ge\frac14\|Z\|_F^2
>\frac{36481}{147456}, \tag{2.23}
\]
proving (2.6).

Set \(x_r=s_r(A[J,K])^2\) and \(E_1=\sum_rx_r\). If \(\sum_{r\le4}x_r\le(63/64)E_1\), five iid draws from weights \(x_r/E_1\) are all distinct with probability at least \((1/64)^4\). Thus
\[
e_5(A[J,K]^TA[J,K])
\ge\frac{(1/64)^4E_1^5}{120}. \tag{2.24}
\]
The completed unrestricted D5 theorem and (2.23) yield (2.7); direct evaluation gives \(199.6734007\ldots\). Otherwise (2.8) follows from (2.23). This proves the theorem.

## 3. What this does and does not close

This theorem removes the extra annular packet from the **tightened** N3 core. It does not silently replace the established full-target reduction to \(N3(1/64)\) by a reduction to \(N3(1/192)\). That outer threshold transfer still needs to be written from the completed pivot/Schur machinery.

The surviving obstruction is now a single familiar geometric type: a quantitatively two-sided physical star together with a cross block whose first four singular directions carry fixed energy, with all small singular tails retained. It is exactly the same-bank-leakage / punctured convex-side receiver problem already isolated by the fleet04 B20 graph.

The full theorem remains open because:

- the band \(N3(1/64)\setminus N3(1/192)\) has not been transferred here;
- packet (2.5), (2.6), (2.8) is not yet paid in full;
- arbitrary additional spectrum still has to be joined to the exact-rank-three receivers without deleting it;
- the punctured convex/two-sheet collar remains unpaid.

There is no full candidate, so two end-to-end reviews are not yet requested. Continuity remains separate outside paid branches.

## 4. Compact corrected proof graph

1. Full target reduces to the established \(N3(1/64)\) debt.
2. D5 pays any physical cross block with quantitative fifth volume.
3. Fleet01/B20 pays diffuse spectral windows by the original-coordinate ridge theorem.
4. The theorem above shows that, after tightening the pivot threshold, failure of the same diffuse window forces a paid literal pair or a two-sided star/four-direction packet.
5. Existing mixed-Fresnel, ruled-side, leakage-free double-star, convex-chain, square-hyperbola, anchor-deletion, and heavy-fresh theorems pay only their exact stated branches.
6. The first live receiver must absorb arbitrary same-bank leakage on packet (2.5), (2.6), (2.8), or prove the missing outer transfer from \(1/64\) to \(1/192\).

No scoped theorem is promoted to the unrestricted conjecture.
