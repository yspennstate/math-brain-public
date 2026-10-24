# B17 — the Numaro restriction obstruction turns on exactly at essential arity ten

**Run:** `20260922T023820Z-account01-B17-r11`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and source artifacts were read directly; no installed/authenticated research-brain receiver context was used.  
**Outcome:** **AUXILIARY_ONLY / exact source-family closure.**  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Exact live target and peer versions actually applied

The live owner target is the all-gate inequality
\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i {\rm It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_p=4p(1-p).
\tag{G}
\]
For the old read-once fixed-point potential, the source convention is
\[
c_G=-D_G/W_G,\qquad
W_G=I(G;p)/4-p_{\rm out}(1-p_{\rm out})\ge0,
\]
so **larger** `c_G` is worse.

I consumed and applied two exact other-account artifacts.

1. `account03/B15/20260922T002607Z-readonce-gamma-counterexample/REPORT.md`,
blob `e49efe403698395b700278d067c245c12a7b15eb`.
For a balanced gate at uniform bias it proves
\[
D_G=C_0(I(G)-1)-H(G),\qquad
c_G=4\left(\frac{H(G)}{I(G)-1}-C_0\right).
\tag{0.1}
\]
It applies the exact 18-variable Numaro seed and decisively refutes the old
read-once potential as a universal all-gate potential.

2. `account04/B13/20260922T0055Z-arity10-prime-falsifier/REPORT.md`,
blob `d71f08f9a2fd0b417ac7b0cdbac19bacac85c01b`.
It exhibits a balanced **composition-prime** ten-input physical restriction
of the same Numaro seed with
\[
I=\frac{257}{128},\qquad
\frac{H}{I-1}>6.4593722816378554,
\tag{0.2}
\]
and proves composition-primality by checking the exact cofactor criterion on
all proper blocks.

The old global candidate is therefore already refuted. The unresolved
question attacked here is narrower but directly suggested by the live owner
message and the peer report: **can the same exact source obstruction be
physically restricted to a smaller balanced gate, in particular arity five
through nine?**

## 1. Exact source normal form

Use the recovered Numaro 18-bit truth table with SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

Write the variables as nine core bits \(x\in\{0,1\}^9\) and nine auxiliary
bits \(y_0,\dots,y_8\). The recovered source has the exact disjoint-host
representation
\[
f(x,y)=a(x)+\sum_{j=0}^8 P_j(x)(-1)^{y_j},
\tag{1.1}
\]
where \(a(x)\in\{-1,0,1\}\), each \(P_j\) is the indicator of one two-point
core host, the nine hosts are pairwise disjoint, and \(a=0\) on every host.
The host pairs are
\[
\begin{split}
&(78,79),(113,121),(228,484),(170,186),(149,151),\\
&(338,466),(284,316),(291,295),(393,457).
\end{split}
\tag{1.2}
\]

This representation makes an exhaustive restriction calculation small.

A physical restriction first assigns each core variable one of three states:
free, fixed \(0\), fixed \(1\). After this choice, only auxiliary variables
whose host meets the surviving core subcube can affect the restricted
function. For each such active auxiliary variable there are again exactly
three states: free, fixed \(0\), fixed \(1\). Every auxiliary variable whose
host misses the surviving core subcube is a dummy and may be fixed without
changing the function.

Therefore every physical restriction of the 18-variable source having at
most ten **essential** variables has an equivalent representative with at
most ten nominal free variables in this ternary core/active-auxiliary
enumeration. This removes the otherwise enormous duplication caused by
irrelevant auxiliary variables.

## 2. Exhaustive theorem

The checker enumerates every normalized representative with nominal arity at
most ten. There are exactly
\[
\boxed{44\,266}
\tag{2.1}
\]
such representatives.

For every balanced representative it computes the Walsh transform in exact
integer arithmetic. Individual influences and total influence are exact
rationals. Entropy logarithms are enclosed by a rational atanh series with an
explicit remainder; no floating-point comparison decides any inequality.

After deleting dummy coordinates by counting exact positive influences, the
balanced normalized restrictions occur only at essential arities
\[
\boxed{1,\ 4,\ 6,\ 8,\ 10.}
\tag{2.2}
\]
Their counts in this normalized enumeration are respectively
\[
3492,\quad 288,\quad 324,\quad 72,\quad 630.
\tag{2.3}
\]
There is no balanced essential restriction of this source at arity
\(2,3,5,7,\) or \(9\).

For the owner-quoted proved read-once cap \(6.4559\), the exact exhaustive
result is
\[
\boxed{
\max_{\substack{g\text{ balanced source restriction}\\
{\rm ess}(g)\le9,\ I(g)>1}}
\frac{H(g)}{I(g)-1}
<
6.363969446288164350267463751014
<
6.4559.
}
\tag{2.4}
\]

The maxima by essential arity are:
\[
\begin{array}{c|c|c}
k & I & \max H/(I-1)\\ \hline
1 & 1 & 0\\
4 & 3/2 & 6\\
6 & 13/8 &
6.347067498701918873383269900894\ldots\\
8 & 53/32 &
6.363969446288164350267463751013\ldots
\end{array}
\tag{2.5}
\]

The arity-six maximum has the exact expression
\[
\boxed{
R_6=\frac{46}{5}-\frac95\log_2 3.
}
\tag{2.6}
\]
Its exact Walsh-square histogram is
\[
16:32,\quad64:4,\quad256:4,\quad576:4.
\]

The arity-eight maximum has exact expression
\[
\boxed{
R_8=
\frac{74}{7}
-\frac37\log_2 3
-\frac{25}{56}\log_2 5
-\frac{121}{168}\log_2 11.
}
\tag{2.7}
\]
Its exact Walsh-square histogram is
\[
16:128,\ 64:16,\ 256:14,\ 576:12,\ 1600:2,\ 2304:1,\ 4096:2,
\ 6400:1,\ 7744:2,\ 16384:1.
\]

Thus the gap below the old read-once cap at the best \(\le9\)-essential
restriction is more than
\[
6.4559-6.363970>0.09193.
\tag{2.8}
\]

## 3. The obstruction appears abruptly at essential arity ten

At essential arity ten there are 630 balanced normalized restrictions.
The rational interval checker classifies
\[
\boxed{621}
\tag{3.1}
\]
of them as satisfying
\[
\frac{H}{I-1}>6.4559,
\]
with no interval ambiguity.

The largest certified interval found is
\[
\boxed{
6.4593722816378557315743616122191241662186132141
<
\frac{H}{I-1}
<
6.4593722816378557315743616122191241662186489285.
}
\tag{3.2}
\]
Its exact influence is \(257/128\), and its Walsh-square histogram is
\[
\begin{gathered}
16:337,\ 64:48,\ 144:108,\ 256:28,\ 576:32,\ 784:18,\ 1024:34,\\
1296:36,\ 1600:24,\ 2304:8,\ 3136:8,\ 5184:8,\ 6400:16,\ 7056:12,\\
9216:8,\ 12544:4,\ 38416:1,\ 53824:8.
\end{gathered}
\tag{3.3}
\]
This is the same spectral/influence value certified for the peer's explicit
ten-input gate \(G_{10}\); that peer additionally proved one such maximizer is
composition-prime.

Consequently, within the complete family of physical restrictions of the
exact recovered Numaro 18-variable seed, the minimum **essential arity** of a
balanced restriction violating the proved read-once cap \(6.4559\) is exactly
\[
\boxed{10.}
\tag{3.4}
\]
This is a source-family theorem, not a theorem about all Boolean gates of
arity at most nine.

## 4. Meaning for the live all-gate programme

The old implication “perhaps the known high-arity falsifier immediately hides
an arity-five falsifier under physical restriction” is now **false for this
exact source family**. The owner-requested arity-five through arity-nine search
cannot be discharged merely by restricting the current Numaro obstruction. A
smaller falsifier, if one exists, must come from a genuinely different gate or
from a biased product point not represented by these uniform balanced
restrictions.

Conversely, the account04/B13 ten-input composition-prime witness is not an
artifact of a careless high-dimensional presentation: within the entire
physical-restriction lattice of its source, ten is the first essential arity
where the old potential fails.

This does **not** repair the old read-once potential; it was already refuted.
It does **not** prove the successor Numaro-scale potential universal. It does
**not** prove FEI.

**Classification:** `AUXILIARY_ONLY`, with a complete exact closure of the
Numaro-source arity-\(\le9\) physical-restriction attack.

**Remaining full implication:** construct one finite-cap symmetric
nonnegative potential satisfying (G) for every Boolean gate and every product
bias, or refute a concrete successor potential by a source-valid gate/bias
instance. The unrestricted FEI conjecture remains **OPEN / NOT PROVED**.

## 5. Verification

`CHECKER.py` is standard-library only. It reconstructs the exact source truth
table and refuses to continue unless the published SHA-256 matches. It
enumerates all 44,266 normalized representatives, computes exact integer Walsh
transforms and rational influences, encloses all entropy logarithms by a
rational atanh series, and makes the cap comparisons using rational interval
endpoints.

Executed checker SHA-256:

`f82e2c50aec91dd5182443672246c0435b3a28509c8c3c7d6eea22065f6723b7`

Captured stdout SHA-256:

`dcd399195950bad0fb41034388bb197494e60fe2e14112e95c634f5faecbcdf9`

The checker exited `PASS`.
