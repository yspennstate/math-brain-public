# B18 FEI proof integration — exact signed carry decomposition of the arithmetic remainder

**Date:** 2026-09-21  
**Role:** fleet03/B18, FEI proof integration  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **PARTIAL / PROVED arithmetic bridge. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Novelty:** no publication-priority claim is made.

## 0. Source-exact frontier and the one missing implication attacked

The required 21 September FEI entry files were read in order (`TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md`), followed by the active three-hour sprint order. The sprint assigns fleet03/B18 the **arithmetic-remainder bridge**.

This run integrates four compatible pieces of the current private proof state.

1. The spectral-lattice decomposition proves, for the magnitude packets of every Boolean `f`,
   \[
   H(f)=2R(f)+2\mathcal D(f),\qquad
   R(f)=\sum_a p_a r_a,
   \]
   with the centroid payment `R(f) <= 2 I(f)`, and leaves `D/I` as the universal unpaid remainder.
2. The newest record-seed packet profile shows that current high-ratio examples can move an order-one amount between `R` and `D`; paying those ledgers independently is therefore structurally lossy.
3. The newest remote-gap theorem shows that positive mesh infection must be treated bilaterally or with negative credits; a seed-only positive crossing payment is false.
4. The newest B18 top-chain theorem gives a real mass-bearing parity defect: a degree-`d` Boolean function has an edge with posterior at least
   \[
   q_d=\frac1{1+2^{2-2/d}}>1/5
   \]
   and upper spectral atom mass at least `4^(1-d)`, but this floor is exponentially small.

The exact missing implication attacked here is:

> **Can the static arithmetic remainder `D` be converted into a finite sequence of actual Boolean carry/collision events while preserving, rather than discarding, the odd-numerator negative credit?**

The answer is **yes**. The resulting event expansion is exact and signed. It does not yet bound the event bank by influence, so it is not full FEI.

---

## 1. Packet notation

For a nonzero Fourier magnitude `a`, write its reduced dyadic form as

\[
a=m_a2^{-e_a},\qquad m_a\ \text{odd}.
\]

Let

\[
A_a=\{S:|\widehat f(S)|=a\},\qquad
p_a=|A_a|a^2,
\]

\[
V_a(x)=\sum_{S\in A_a}\operatorname{sgn}(\widehat f(S))\chi_S(x),
\qquad
r_a=\min_{V_a(x)\ne0}\nu_2(V_a(x)).
\]

Put

\[
W_a=2^{-r_a}V_a,\qquad
d_a=e_a-r_a,\qquad
b_a=m_a2^{-d_a}.
\]

The inherited projection-spacing theorem gives `0<b_a<=1`. Hence `d_a>=0`; if `d_a=0`, oddness of `m_a` and `b_a<=1` force `m_a=1`.

Each packet is therefore

\[
f_a(x)=b_aW_a(x)=m_a2^{-d_a}W_a(x),
\]

where `W_a` is integer-valued and primitive in the sense that it has an odd value. Distinct packets have disjoint Fourier supports.

Define the **raw mesh-depth debit**

\[
A(f):=\sum_a p_a d_a
\]

and the **odd-numerator credit**

\[
Q(f):=\sum_a p_a\log_2m_a.
\]

Then the inherited arithmetic remainder has the exact form

\[
\boxed{\mathcal D(f)=A(f)-Q(f).}
\tag{1}
\]

This elementary rewriting is important below because `A` and `Q` behave very differently under Boolean carries.

---

## 2. PROVED: maximal-depth parity pairing

The packet decomposition is a special case of the following state.

Let

\[
f=\sum_j m_j2^{-d_j}W_j
\tag{2}
\]

where the positive-depth components have pairwise disjoint Fourier supports, every `m_j` is odd, every `d_j` is a positive integer, and every `W_j` is primitive integer-valued. Depth-zero components are allowed and are simply integer-valued.

Let `D=max_j d_j>0` and let `J_D={j:d_j=D}`. Set

\[
T_D(x):=\sum_{j\in J_D}m_jW_j(x).
\tag{3}
\]

### Theorem 2.1 — top-depth parity

For every `x`,

\[
\boxed{T_D(x)\equiv0\pmod2.}
\tag{4}
\]

Consequently there are at least two positive-depth components at the maximal depth.

### Proof

Multiply (2) by `2^D`:

\[
T_D(x)+
\sum_{d_j<D}m_j2^{D-d_j}W_j(x)
=\pm2^D.
\]

The right-hand side is even because `D>=1`. Every lower-depth term has the factor `2^{D-d_j}` and is therefore even. Hence `T_D(x)` is even for every `x`.

If there were only one maximal-depth component, `T_D=mW` with `m` odd and `W` primitive. At a point where `W` is odd, `T_D` would be odd, contradicting (4). `QED`

### Corollary 2.2 — genuine deepest-mesh overlap

In the initial packet decomposition, fix the largest positive depth `D` and put

\[
E_a=\{x:W_a(x)\ \text{is odd}\}
\qquad(d_a=D).
\]

At every `x`, the multiplicity

\[
M_D(x)=\sum_{a:d_a=D}1_{E_a}(x)
\]

is even. Therefore

\[
\boxed{
\sum_{\substack{a<b\\ d_a=d_b=D}}
\Pr(E_a\cap E_b)
\ge
\frac12\sum_{a:d_a=D}\Pr(E_a).
}
\tag{5}
\]

Indeed `binom(M_D(x),2)>=M_D(x)/2` whenever the even integer `M_D(x)` is positive.

This is an actual cross-packet collision statement. It does **not** give a dimension-free lower bound on the right side; primitive odd sets may be small.

---

## 3. PROVED: the signed carry algorithm

Because of (4), `T_D` has a positive global 2-adic valuation. Let

\[
s_D:=\min_{T_D(x)\ne0}\nu_2(T_D(x))\ge1.
\tag{6}
\]

`T_D` is not identically zero: the Fourier supports of the top components are disjoint, so their nonzero frequency coefficients cannot cancel.

Put

\[
c_D:=\min\{s_D,D\}.
\tag{7}
\]

If `s_D<D`, replace all maximal-depth components by the single component

\[
2^{-(D-s_D)}\widetilde W_D,
\qquad
\widetilde W_D:=2^{-s_D}T_D,
\tag{8}
\]

which is again primitive integer-valued and has odd numerator one. If `s_D>=D`, the whole top sum is already integer-valued:

\[
2^{-D}T_D\in\mathbb Z,
\]

so replace it by one depth-zero component.

The new component has Fourier support equal to the disjoint union of the old top supports and remains Fourier-disjoint from every untouched component.

Let

\[
P_D:=\sum_{j\in J_D}\|m_j2^{-D}W_j\|_2^2.
\tag{9}
\]

Orthogonality shows that the replacement has exactly the same spectral mass `P_D`.

Its depth falls from `D` to `D-c_D`, so the raw depth ledger drops by exactly

\[
\boxed{c_DP_D.}
\tag{10}
\]

Repeat this operation until no positive-depth component remains.

### Theorem 3.1 — finite carry decomposition

The algorithm terminates after finitely many events. If the events are indexed by `t`, with carry jump `c_t` and top-layer mass `P_t`, then

\[
\boxed{
A(f)=\sum_t c_tP_t.
}
\tag{11}
\]

### Proof

At every positive depth there are at least two maximal components by Theorem 2.1. One event merges all of them into at most one positive-depth component, so the number of positive-depth components strictly decreases. Hence there are finitely many events.

Equation (10) gives the exact decrement of the nonnegative ledger `sum P_j d_j` at each event. At termination every depth is zero, so telescoping gives (11). `QED`

---

## 4. PROVED: exact *signed* event expansion of the arithmetic remainder

At event `t`, define its current odd-numerator credit

\[
Q_t:=\sum_{j\in J_t}P_j\log_2m_j.
\tag{12}
\]

A newly merged positive-depth component always has odd numerator `1`, so it carries zero future numerator credit. An untouched initial component retains its original odd numerator until its first event. Every initial positive-depth component eventually enters exactly one first event, while an initial depth-zero component has numerator one.

Therefore

\[
\boxed{\sum_t Q_t=Q(f).}
\tag{13}
\]

Combining (1), (11), and (13) gives the main bridge.

### Theorem 4.1 — signed carry representation

For every Boolean function,

\[
\boxed{
\mathcal D(f)
=
\sum_t\Bigl(c_tP_t-Q_t\Bigr).
}
\tag{14}
\]

No absolute value or positive part appears.

Together with the inherited centroid estimate `R(f)<=2I(f)`,

\[
\boxed{
H(f)
\le
4I(f)+
2\sum_t(c_tP_t-Q_t).
}
\tag{15}
\]

Equation (15) is not a new FEI constant because the signed event sum is exactly `D`. Its value is that it turns the static unpaid remainder into a finite sequence of explicit Boolean carry/collision events, while keeping the negative credit that the newest B15 and B16 work says must not be discarded.

---

## 5. PROVED integration with the weighted top-chain defect

Use the newest B18 weighted top-chain theorem: if `f` has Fourier degree `d>=1`, there is an oriented Fourier-support edge whose upper atom `S` satisfies

\[
q\ge q_d>1/5,
\qquad
p_S=\widehat f(S)^2\ge4^{1-d}.
\tag{16}
\]

Let `a=|\widehat f(S)|` and let that coefficient lie in packet `A_a`.

### Corollary 5.1 — top-chain defect reaches the arithmetic carry bank

Exactly one of the following holds.

1. `d_a=0`. Then `m_a=1`, `b_a=1`, and the entire packet has zero arithmetic-remainder contribution.
2. `d_a>0`. Then that initial packet necessarily enters a unique first carry event `t`, and
   \[
   \boxed{P_t\ge p_a\ge p_S\ge4^{1-d}.}
   \tag{17}
   \]

### Proof

The zero-depth case was noted in section 1. In the positive-depth case, finite termination of the carry algorithm forces the initial component to participate in a first event. Event mass contains its full packet mass `p_a`, which contains the atom mass `p_S`. `QED`

This closes a concrete compatibility gap between the top-chain parity route and the arithmetic-remainder route: a mass-bearing top-chain defect cannot disappear before entering the arithmetic bookkeeping. What remains missing is a **dimension-free signed payment**; (17) still inherits the exponential `4^(1-d)` floor.

---

## 6. REFUTED: positive carry mass cannot be paid by influence

A tempting stronger route is

\[
\sum_t c_tP_t\le C I(f)
\tag{18}
\]

for a universal constant. This is false by an exponential factor.

Let

\[
U_n(x)=1-2\,1_{\{x=0\}},
\qquad n\ge3.
\]

Its two magnitude packets have the common depth `D=n-1`:

- the constant packet has odd numerator `2^(n-1)-1`;
- all nonempty Fourier coefficients form the second packet with odd numerator `1`.

The two packets have total mass one. Their top sum is divisible by `2^(n-1)` pointwise, so the carry algorithm has a **single event**

\[
c_1=n-1,\qquad P_1=1.
\tag{19}
\]

Hence the positive carry debit is `n-1`.

But

\[
I(U_n)=\frac{n}{2^{n-1}},
\tag{20}
\]

so

\[
\frac{\sum_t c_tP_t}{I(U_n)}
=
\frac{(n-1)2^{n-1}}n
\longrightarrow\infty.
\tag{21}
\]

The odd-numerator credit almost completely cancels this debit:

\[
Q(U_n)
=
\left(1-2^{1-n}\right)^2
\log_2(2^{n-1}-1),
\tag{22}
\]

\[
\mathcal D(U_n)
=(n-1)-Q(U_n),
\tag{23}
\]

and the checker gives `D/I -> 2` numerically along this family. Thus dropping `Q` destroys exactly the cancellation needed even in the elementary one-point family.

This is a refutation of the positive-carry shortcut, not of FEI.

---

## 7. REFUTED: individual signed events need not be nonnegative

One might next hope that every event separately satisfies

\[
c_tP_t-Q_t\ge0.
\tag{24}
\]

That also fails.

For the exact five-bit Boolean truth-table mask

`0xd974b822`

the initial packet profile is

\[
(m,d,p)=
(7,4,49/256),\,
(9,4,81/256),\,
(1,3,11/128),\,
(3,3,27/128),\,
(5,3,25/128).
\tag{25}
\]

The first carry event has

\[
D=4,\quad s=1,\quad c=1,\quad P=65/128
\]

and

\[
Q_1=
\frac{49}{256}\log_2 7+
\frac{81}{256}\log_2 9.
\]

Since `log2 7>2` and `log2 9>3`,

\[
Q_1>\frac{341}{256}>\frac{65}{128}=cP,
\]

so this event is strictly **negative**. Numerically,

\[
cP-Q_1=-1.0325168605376949\ldots.
\tag{26}
\]

The second event has depth/jump three and positive net

\[
2.212170391471443\ldots,
\]

and the two signed values sum to

\[
\mathcal D(f)=1.179653530933748\ldots.
\tag{27}
\]

Therefore any proof that positive-parts the carry events before summing is invalid. The cancellation has to survive across events, just as the signed-transport and packet-KL routes have been warning.

---

## 8. Exact computation and refutation attempts

`verify_signed_carry_decomposition.py` uses only integer Walsh transforms and exact `Fraction` arithmetic for packet masses, depths, valuations, carry jumps, and all structural assertions. Floating point is used only to display logarithms.

It verifies:

1. the carry identities (11) and (14) for every Boolean truth table in dimensions `1` through `4`, totaling `65,812` functions;
2. exact packet masses and event depths for the five-bit negative-event witness (25);
3. the negative sign of its first event and positive compensation by the second event;
4. the one-point family through `n=12`, including the single-event carry debit `n-1`.

Committed-script SHA-256:

`6325f37843f79070c64dec4632a734fd2fddf3cbcffb5e301caaa85a2c2d91d8`

Saved-output SHA-256:

`fa1da178866c3300c9b9b443c492dcebf31ac98e7b3da3926a802188bcde90a7`

The exhaustive finite check is supporting evidence only. Theorems 2.1, 3.1, and 4.1 are analytic.

---

## 9. What moved and what remains open

### PROVED

- Maximal positive mesh depth cannot occur in a single primitive packet; its odd residues pair pointwise.
- Deepest primitive odd sets have the pairwise-overlap inequality (5).
- There is a finite exact carry algorithm preserving Fourier support disjointness and spectral mass.
- Raw depth has the exact telescoping decomposition `A=sum c_t P_t`.
- The arithmetic remainder has the exact **signed** event expansion
  \[
  D=\sum_t(c_tP_t-Q_t).
  \]
- The newest weighted top-chain defect either lies in a remainder-free integral packet or reaches a real carry event of mass at least `4^(1-d)`.

### REFUTED

- A universal influence bound on the positive carry debit `sum c_tP_t`: the one-point family violates it exponentially.
- Eventwise nonnegativity `c_tP_t-Q_t>=0`: the exact five-bit witness (25) has a negative first event.

### CONDITIONAL / inherited dependencies

- The final `H<=4I+2D` reduction uses the previously proved packet-centroid theorem.
- Corollary 5.1 uses the newest weighted top-chain theorem as an input rather than re-auditing it.
- No publication novelty is claimed for the carry representation.

### OPEN

- A dimension-independent bound on the **signed, telescoping** carry bank.
- Full uniform-cube FEI.

---

## 10. Next attack

The correct next lemma is not a positive collision bound. The examples above rule that out.

The next target is an **amortized signed carry/influence inequality** on the carry tree. A useful form would assign to each event subtree a potential retaining both:

1. the event debit `c_tP_t`, and
2. all inherited odd-numerator / valuation / packet-KL credits,

and prove that the *net telescoping value* of the subtree is controlled by the original-coordinate influence carried by its Fourier support.

The newest remote-gap theorem says a long exponent jump must be paid bilaterally; the one-point family says the odd numerator can pay almost the whole jump; the record ladder says valuation `R` and remainder `D` can exchange order-one mass. Therefore the next proof should attempt a local identity of the form

\[
\text{signed carry debit}
+\Delta(\text{valuation potential})
+\Delta(\text{KL/odd-numerator credit})
\le C\,\text{physical boundary},
\]

summed **before** taking positive parts. A two-face or random-basis signed transport mechanism is the natural candidate for the physical boundary term.

That is a materially different mechanism from another endpoint audit or another raw-normalizer bound.
