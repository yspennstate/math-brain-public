# B15 — restriction carry-jump budget and minimal unequal-magnitude merger

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** The control plane and private FEI repository were read through authenticated GitHub access, but no authenticated mathematical/cognitive brain retrieval or receiver context was consumed.

**Route:** owner-directed spectral magnitude / arithmetic structure, APPROACH 4/8. The stale conjecture that Hod's `beta(1/2)` is the universal FEI constant is already retired by the current handoff: Numaro's published 18-variable seed gives `C_FEI > 6.521845710923046575`. This run therefore attacks the surviving arithmetic question, namely how equal-magnitude packet carry behaves under restriction and exactly where unequal magnitudes escape packetwise control.

Fresh private `master` was resolved before the work and refreshed again after concurrent FEI commits. The required `TASKS_2026-09-21.md`, `REPORT.md`, `APPROACHES.md`, the preceding B15 carry report, its primitive-layer addendum, and its handoff were read. The settled read-once certificate was not rerun and no FEI audit was performed.

## 1. Setup

Let

\[
V(x)=\sum_{S\in A}\epsilon_S\chi_S(x),\qquad \epsilon_S\in\{\pm1\},
\]

be one signed equal-magnitude Fourier packet, and let

\[
r(V)=\min_{V(x)\ne0}\nu_2(V(x)).
\]

The preceding B15 run proved the exact upper-incidence criterion

\[
r(V)\ge r \iff 2^{r-|T|}\mid M_T\quad (|T|<r),
\qquad M_T:=\sum_{S\supseteq T}\epsilon_S,
\tag{1}
\]

and the primitive-layer theorem

\[
\#\{x:\nu_2(V(x))=r(V)\}\ge 2^{n-r(V)}.
\tag{2}
\]

In particular `|A| >= 2^{r(V)}`.

Fix a coordinate `i`. Split the packet into terms not containing and containing `i`:

\[
P(y)=\sum_{T\not\ni i,\,T\in A}\epsilon_T\chi_T(y),
\qquad
Q(y)=\sum_{T\not\ni i,\,T\cup\{i\}\in A}\epsilon_{T\cup\{i\}}\chi_T(y).
\]

Then on the two physical restrictions of coordinate `i`,

\[
V_+(y)=P(y)+Q(y),\qquad V_-(y)=P(y)-Q(y).
\tag{3}
\]

## 2. Exact signed-moment restriction law

For `R subseteq [n]\{i}`, let `M_R^(s)` be the upper-incidence moment of the integer coefficient field of `V_s`, where `s=+1` or `-1`. Then

\[
\boxed{M_R^{(s)}=M_R+(s-1)M_{R\cup\{i\}}.}
\tag{4}
\]

Thus

\[
M_R^{(+)}=M_R,\qquad M_R^{(-)}=M_R-2M_{R\cup\{i\}}.
\tag{5}
\]

**Proof.** The restricted coefficient at `T` is

\[
\epsilon_T\mathbf 1_{T\in A}+s\epsilon_{T\cup\{i\}}\mathbf 1_{T\cup\{i\}\in A}.
\]

Summing over `T superset R` gives the part of `M_R` with `i` absent plus `s` times the part with `i` present. The latter is exactly `M_{R union {i}}`, giving (4). \(\square\)

Equation (4) makes the old divisibility hierarchy functorial before different Fourier magnitudes are merged. If `r(V)>=r`, then every value of both restrictions is still divisible by `2^r`; equivalently the moments in (5) satisfy the corresponding child divisibilities.

## 3. Carry-jump theorem for one parent packet

Call coordinate `i` a **packet carry-jump coordinate** when one of `V_+`, `V_-` has carry depth strictly larger than `r(V)` (with the zero function assigned depth `+infinity`).

### Theorem 1 (a packet carry jump forces two large subpackets)

Assume `r=r(V)>=1`. Then:

1. `r(V_+)>=r` and `r(V_-)>=r`;
2. at least one of `V_+`, `V_-` has carry depth exactly `r`;
3. if one branch has depth `>r`, then

\[
\boxed{r(P)=r(Q)=r-1.}
\tag{6}
\]

Consequently, if

\[
m_0=|\{S\in A:i\notin S\}|,\qquad
m_1=|\{S\in A:i\in S\}|,
\]

then every carry-jump coordinate satisfies

\[
\boxed{m_0\ge2^{r-1},\qquad m_1\ge2^{r-1}.}
\tag{7}
\]

Moreover the primitive layers of both `P` and `Q` occupy at least `2^{n-r}` points of their `(n-1)`-dimensional physical cubes.

**Proof.** The first assertion is immediate because restricting `V` only discards physical points and all values of `V` are divisible by `2^r`. If both restrictions had depth at least `r+1`, then every value of `V` would be divisible by `2^{r+1}`, contradicting exactness of `r(V)=r`; hence one branch has exact depth `r`.

Suppose, without loss of generality, that `V_+` has exact depth `r` and `V_-` has depth at least `r+1`. From (3),

\[
P=(V_++V_-)/2,\qquad Q=(V_+-V_-)/2.
\]

Both are everywhere divisible by `2^{r-1}`. At a physical point where `nu_2(V_+)=r`, the value of `V_-` is divisible by `2^{r+1}`, so both `V_++V_-` and `V_+-V_-` have valuation exactly `r`. Therefore `P` and `Q` each attain valuation exactly `r-1`, proving (6).

Each of `P,Q` is itself a signed character sum with `m_0,m_1` coefficients respectively. Applying the preceding packet multiplicity theorem `m>=2^{r(.)}` gives (7). Applying the primitive-layer theorem to `P,Q` on `n-1` variables gives at least

\[
2^{(n-1)-(r-1)}=2^{n-r}
\]

primitive points for each. \(\square\)

This is stronger than the statement that restriction preserves divisibility: **if a branch actually gains a carry level, the splitting coordinate must cut the packet into two nontrivial pieces, each already large enough to support depth `r-1`.**

## 4. A dimension-free global carry-jump budget

Now let `f:{-1,1}^n->{-1,1}` and group its nonzero Fourier coefficients by magnitude. For magnitude `a>0`, write

\[
A_a=\{S:|\widehat f(S)|=a\},\qquad
r_a=r(V_a),\qquad
V_a=\sum_{S\in A_a}\operatorname{sgn}(\widehat f(S))\chi_S.
\]

Let `J_a` be the set of coordinates that are packet carry-jump coordinates for `V_a`. For the packet's contribution to total influence define

\[
I_a=a^2\sum_{S\in A_a}|S|.
\]

### Corollary 2 (universal carry-jump budget)

\[
\boxed{
\sum_{a:r_a\ge1}2^{r_a-1}a^2|J_a|\le I(f).
}
\tag{8}
\]

**Proof.** For every `i in J_a`, Theorem 1 gives

\[
|\{S\in A_a:i\in S\}|\ge2^{r_a-1}.
\]

Therefore

\[
2^{r_a-1}|J_a|
\le \sum_{i\in J_a}|\{S\in A_a:i\in S\}|
\le \sum_{S\in A_a}|S|.
\]

Multiply by `a^2` and sum over packets. Since the packet sets partition the nonzero spectrum,

\[
\sum_a a^2\sum_{S\in A_a}|S|=\sum_S|S|\widehat f(S)^2=I(f).
\]

This proves (8). \(\square\)

Equation (8) is the first direct dimension-free influence payment on this B15 carry route. It does **not** pay all packet entropy and does not prove FEI. It says that once an equal-magnitude packet already has positive carry depth, coordinates along which that packet can lose its primitive layer cannot occur freely: their total carry-unit cost is bounded by the actual Fourier influence.

## 5. The exact obstruction: unequal magnitudes can create a new child packet

The packetwise theorem does not close an induction, because the child Fourier spectrum is not obtained by restricting each parent magnitude packet and keeping the packets separate. Different parent magnitudes are added before the child is regrouped by magnitude:

\[
\widehat{f_s}(T)=\widehat f(T)+s\widehat f(T\cup\{i\}).
\tag{9}
\]

The following genuine Boolean example shows that a positive-carry child packet can be created even when **every parent magnitude packet has carry depth zero**.

Take the three-bit Boolean function

\[
f(000)=+1,\qquad f(x)=-1\quad(x\ne000).
\]

Its unnormalised Walsh coefficients are

\[
(c_S)_{S\subseteq[3]}=(-6,2,2,2,2,2,2,2).
\tag{10}
\]

There are two nonzero parent magnitude packets:

- magnitude `6`: the singleton empty-set coefficient with sign `-`, hence packet depth `0`;
- magnitude `2`: the seven nonempty coefficients, all positive. Its signed packet sum is `7` at `000` and `-1` elsewhere, hence packet depth `0`.

Restrict any coordinate to the half containing the exceptional point. The resulting two-bit one-point function has Walsh vector

\[
(-2,2,2,2).
\tag{11}
\]

All four coefficients now belong to one magnitude-`2` packet, whose signed packet field is

\[
-1+\chi_1+\chi_2+\chi_{\{1,2\}},
\]

and takes only the values `+2` and `-2`. Hence the child packet has

\[
\boxed{r_{\rm child}=1}
\]

although both parent packet depths were zero.

The merger is genuinely unequal-magnitude. In unnormalised restriction coordinates, the child empty-set coefficient is

\[
\frac{-6+2}{2}=-2,
\tag{12}
\]

so the new magnitude-`2` child packet contains an atom created by collision of parent magnitudes `6` and `2`; its other atoms come from magnitude-`2` pairs. Thus the new carry is a **packet-merger carry**, not a carry jump of either parent packet in isolation.

## 6. Exact finite minimality of the obstruction

`restriction_collision_minimal.py` exhaustively checks all Boolean functions in dimensions `n=1,2,3` using integer Walsh transforms. The tested property is exactly:

> all nonzero parent magnitude packets have carry depth zero, but some one-coordinate restriction contains a positive-carry child magnitude packet with at least one coefficient formed from two nonzero unequal parent magnitudes.

The exact result is:

- `n=1`: 0 witnesses among 4 functions;
- `n=2`: 0 witnesses among 16 functions;
- `n=3`: 128 witnesses among 256 functions;
- first truth-table mask: the one-point function above.

So dimension three is minimal for this precisely stated unequal-magnitude merger property. The script uses integer arithmetic only for the finite assertion.

Script SHA-256: `371c522e46908f8fe2bb13bf34acf7a0de42fe7dbe1a73f339ef91ac3750b9ba`.  
Output SHA-256: `6d64a9d97f30512cd87bf972a0bdb714668c3ce498b7861869714345da33a985`.

## 7. What is now paid and what is still unpaid

This run separates the restriction problem into two mathematically different mechanisms.

**Paid packetwise mechanism.** Existing positive carry inside a fixed parent magnitude packet has a genuine influence budget: carry-jump coordinates obey (8). The primitive-layer theorem also prevents the jump from being an arbitrarily rare physical-cube phenomenon.

**Unpaid merger mechanism.** After restriction, coefficients from different parent magnitudes can collide and be regrouped into a new equal-magnitude child packet. The three-bit example proves that this can create carry from scratch, so no induction that only transports each parent packet's `r_a` can be universal.

This is consistent with the exact `n=18` record profile from the preceding run: the record improvement is a large transfer between the carry and free-energy ledgers, not monotone growth of either ledger separately. A viable universal proof must therefore charge **merger-created carry together with the magnitude/free-energy change produced by the same collision**, not carry in isolation.

A precise next B15 obligation is to study the merger graph of (9). For a fixed coordinate and branch, group child atoms by the unordered pair of parent magnitude labels feeding them. The target is a dimension-free inequality that pays the primitive layer created by cross-label mergers using the same coordinate's spectral incidence plus the drop in magnitude-label entropy/free energy. The three-bit one-point function above is the first mandatory stress test: any proposed lemma that attributes every child carry level to a parent packet is already false.

## 8. Scope and provenance

No publication-priority claim is made for Theorem 1, Corollary 2, or the finite obstruction. They are new-to-this-run deductions for the private proof programme. Current repository state already records the external Numaro lower bound above Hod's read-once constant and the recent plateaued-function special case; this run does not re-audit those results.

**Bottom line:** full FEI remains **OPEN**. The B15 route did obtain a rigorous dimension-free carry-jump payment, and it isolated with a minimal genuine Boolean example the exact unequal-magnitude packet-merger mechanism that escapes that payment.
