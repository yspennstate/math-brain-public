# B16 — exact spectral law for random q-flip channel density

**Run:** 2026-09-21T15:27:51Z, fleet02/B16  
**Live role:** FEI signed transport proof  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full FEI status:** **OPEN / NOT PROVED**.  
**Scientific master entering this derivation:** `9cfeb06e1616303247f7140c438ddaaa70f5b26d`; refreshed before delivery to a later master with no intervening B16 change.  
**Claim level:** a new exact q-flip incidence identity, dimension-free-in-the-right-scale bounds, and a decisive obstruction to a channel-counting payment. No novelty or publication-priority claim.

## 0. Measurable movement and route choice

The preceding fleet02 q-flip transport gave, for a random translated/pivoted q-flip basis of
\(C_0=RM(1,n)^\perp\), the fixed-edge **support-incidence** estimate
\[
\mathbb E C_e=\frac{4(2^n-n-1)}{n2^n}<\frac4n.
\]
That upper bound did not say how many of those channels are actually frustrated by the Boolean phase. The next fleet02 run then showed that a single Aumann--Shapley q-flip load can be exponentially large, so a pointwise load estimate is false and basis averaging is genuinely necessary.

This run asks the complementary question:

> **Can randomizing the q-flip basis make the set of actually frustrated q-flip channels sparse enough that counting alone pays the signed transport?**

The answer is **no**, and the obstruction is exact. I derive the complete averaged active-channel count from the Walsh spectrum of the original-coordinate derivative signs. In folded gauge every noncharacter has
\[
\mathbb E_{\mathcal B}Q_{\mathcal B}(f)
=\Theta\!\left(\frac{2^n}{n}J(f)\right),
\]
with explicit sharp spectral endpoint multipliers. Thus randomization spreads the channels over physical disagreement edges at scale \(1/n\), but it cannot make the total active channel bank negligible. The remaining proof must control the **signed load carried by those channels**, not their number.

This is complementary to the newest fleet04 B16 central Hardy/Ward route: that work owns the signed central-band plaquette divergence. I do not reprove or spend its plaquette/terminal bank here. The result below isolates what the q-flip basis randomization itself can and cannot contribute.

The three deliberately different FLEET_RULES moves used here are:

* **#2 ATTACK THE NEGATION:** prove that the hoped-for channel sparsification cannot occur.
* **#11 DUALIZE:** diagonalize derivative autocorrelations by the Walsh transform.
* **#24 FIND THE EXTREMAL OBJECT:** exhibit genuine quadratic Boolean phases attaining the bottom and top spectral multipliers.

No R32 coefficient is absolute-valued, no dual-code multiplicity is dropped, and the terminal band is untouched.

---

## 1. Random q-flip basis and the active-channel count

Let
\[
G=\mathbb F_2^n,\qquad N=2^n,\qquad f:G\to\{\pm1\}.
\]
Use the q-flip basis from the previous fleet02 theorem. Choose an anchor \(a\in G\) uniformly. For each \(v\ne0\) with \(|v|\ge2\), independently choose a pivot
\[
i(v)\in\operatorname{supp}(v)
\]
uniformly and set
\[
B_v(a)=\{a,\ a+e_{i(v)},\ a+v,\ a+v+e_{i(v)}\}.
\tag{1.1}
\]
For every anchor and every allowed pivot choice the \(N-n-1\) sets \(B_v(a)\) form a basis of \(C_0\).

Define
\[
Q_{\mathcal B}(f)
:=\#\{v:\ f_{B_v(a)}=-1\},
\qquad
f_B:=\prod_{x\in B}f(x).
\tag{1.2}
\]
Each active q-flip \(f_{B_v(a)}=-1\) contains exactly one physical disagreement edge among its two parallel pivot-direction edges. Thus \(Q_{\mathcal B}\) is exactly the total number of active q-flip channels before any signed R32/Aumann--Shapley load is placed on them.

Multiplication by any cube character leaves \(Q_{\mathcal B}\) unchanged: every \(B_v(a)\) has even cardinality and xor zero, so the character product over it is \(+1\). Hence all statements below are automatically compatible with the minimizing-character folded gauge.

---

## 2. Original-coordinate derivative field

For a physical coordinate \(i\), define the derivative sign
\[
\tau_i(x):=f(x)f(x+e_i)\in\{\pm1\}.
\tag{2.1}
\]
It satisfies
\[
\tau_i(x+e_i)=\tau_i(x),
\tag{2.2}
\]
so its Walsh spectrum is supported on labels \(S\subseteq[n]\setminus\{i\}\).

With normalized Walsh coefficients
\[
\widehat{\tau_i}(S)=2^{-n}\sum_x\tau_i(x)(-1)^{S\cdot x},
\]
we have
\[
\widehat{\tau_i}(\varnothing)=1-2I_i(f)
\tag{2.3}
\]
and Parseval gives
\[
\sum_{\varnothing\ne S\subseteq[n]\setminus\{i\}}
\widehat{\tau_i}(S)^2
=
1-(1-2I_i(f))^2
=
4I_i(f)(1-I_i(f)).
\tag{2.4}
\]

This is the exact original-coordinate fluctuation bank sampled by random q-flips.

---

## 3. `B16-QFLIP-CHANNEL-SPECTRAL-LAW` — PROVED

For \(m\ge1\) and \(1\le k\le m\), define
\[
K_m(k)
:=
\int_0^1
\left[
(1+t)^m-(1-t)^k(1+t)^{m-k}
\right]\,dt.
\tag{3.1}
\]

### Theorem 3.1

Under the random q-flip basis law (1.1),
\[
\boxed{
\mathbb E_{\mathcal B}Q_{\mathcal B}(f)
=
\frac12\sum_{i=1}^n
\sum_{\substack{\varnothing\ne S\subseteq[n]\setminus\{i\}}}
\widehat{\tau_i}(S)^2
K_{n-1}(|S|).
}
\tag{3.2}
\]

Equivalently, if
\[
C_i(w):=\mathbb E_x\,\tau_i(x)\tau_i(x+w),
\qquad w_i=0,
\tag{3.3}
\]
then
\[
\boxed{
\mathbb E_{\mathcal B}Q_{\mathcal B}(f)
=
\frac12\sum_{i=1}^n
\sum_{\substack{w\subseteq[n]\setminus\{i\}\\w\ne0}}
\frac{1-C_i(w)}{|w|+1}.
}
\tag{3.4}
\]

### Proof

Fix \(v\) and suppose its chosen pivot is \(i\). Put
\[
w=v+e_i.
\]
Because \(i\in\operatorname{supp}(v)\), \(w_i=0\) and \(w\ne0\). The q-flip sign is
\[
f_{B_v(a)}
=
\tau_i(a)\tau_i(a+v)
=
\tau_i(a)\tau_i(a+w),
\tag{3.5}
\]
where the second equality uses the invariance (2.2). Therefore
\[
\Pr_a[f_{B_v(a)}=-1\mid i(v)=i]
=
\frac{1-C_i(w)}2.
\tag{3.6}
\]

Conversely, every pair \((i,w)\) with \(w_i=0,\ w\ne0\) corresponds to the displacement \(v=w+e_i\), whose Hamming weight is \(|w|+1\), and the chance that \(i\) is selected as its pivot is \(1/(|w|+1)\). Summing (3.6) proves (3.4).

Now diagonalize the autocorrelation:
\[
C_i(w)
=
\sum_{S:i\notin S}
\widehat{\tau_i}(S)^2(-1)^{S\cdot w}.
\tag{3.7}
\]
The constant Fourier mode cancels in \(1-C_i(w)\). For a nonempty label \(S\) of size \(k\), use
\[
\frac1{|w|+1}=\int_0^1 t^{|w|}\,dt.
\tag{3.8}
\]
Then
\[
\begin{aligned}
\sum_{w\subseteq[m]}
\frac{1-(-1)^{|S\cap w|}}{|w|+1}
&=
\int_0^1
\sum_w
\left[1-(-1)^{|S\cap w|}\right]t^{|w|}\,dt\\
&=
\int_0^1
\left[(1+t)^m-(1-t)^k(1+t)^{m-k}\right]dt\\
&=K_m(k).
\end{aligned}
\tag{3.9}
\]
The \(w=0\) term vanishes automatically, so (3.4), (3.7), and (3.9) give (3.2). ∎

### Interpretation

The random-basis channel count is not a mysterious combinatorial quantity. It is a radial multiplier applied to the **squared Walsh spectrum of the physical derivative signs**. In particular, basis averaging does not destroy original-coordinate geometry: the only spectral objects are the \(n\) genuine physical derivatives \(\tau_i\).

---

## 4. Exact multiplier ordering and closed endpoints

For fixed \(m\) and \(0<t<1\),
\[
(1-t)^k(1+t)^{m-k}
=(1+t)^m
\left(\frac{1-t}{1+t}\right)^k.
\tag{4.1}
\]
The ratio in parentheses lies strictly between zero and one, so

\[
\boxed{
K_m(1)<K_m(2)<\cdots<K_m(m).
}
\tag{4.2}
\]

For \(m=n-1\), write
\[
\alpha_n:=K_{n-1}(1),
\qquad
\beta_n:=K_{n-1}(n-1).
\tag{4.3}
\]
Direct integration yields
\[
\boxed{
\alpha_n
=
\frac{2\left(2^{n-1}(n-2)+1\right)}{n(n-1)},
\qquad
\beta_n
=
\frac{2^n-2}{n}.
}
\tag{4.4}
\]

Indeed,
\[
K_{n-1}(1)
=
2\int_0^1 t(1+t)^{n-2}dt,
\tag{4.5}
\]
which gives the first formula, while
\[
K_{n-1}(n-1)
=
\int_0^1[(1+t)^{n-1}-(1-t)^{n-1}]dt
\tag{4.6}
\]
gives the second.

Combining (2.4), (3.2), and the monotonicity gives the exact variance-envelope theorem
\[
\boxed{
2\alpha_n\sum_i I_i(f)(1-I_i(f))
\le
\mathbb E_{\mathcal B}Q_{\mathcal B}(f)
\le
2\beta_n\sum_i I_i(f)(1-I_i(f)).
}
\tag{4.7}
\]

---

## 5. Folded-influence corollary: active channels are necessarily dense

Let
\[
j_i:=\min\{I_i(f),1-I_i(f)\},
\qquad
J(f):=\sum_i j_i.
\tag{5.1}
\]
Character gauge invariance lets us replace \(f\) by its minimizing character twist, after which the physical influence is exactly \(J\). Since
\[
I_i(1-I_i)=j_i(1-j_i),
\qquad
\frac{j_i}{2}\le j_i(1-j_i)\le j_i
\quad(0\le j_i\le1/2),
\tag{5.2}
\]
(4.7) implies
\[
\boxed{
\alpha_nJ(f)
\le
\mathbb E_{\mathcal B}Q_{\mathcal B}(f)
\le
2\beta_nJ(f).
}
\tag{5.3}
\]

Because
\[
\alpha_n\sim\frac{2^n}{n},
\qquad
\beta_n\sim\frac{2^n}{n},
\tag{5.4}
\]
every noncharacter carries
\[
\mathbb E Q_{\mathcal B}
=
\Theta\!\left(\frac{2^n}{n}J(f)\right)
\tag{5.5}
\]
active q-flips.

In the folded gauge, the number of physical disagreement edges is
\[
|\mathcal D_f|=\frac{NJ(f)}2.
\tag{5.6}
\]
Every active q-flip routes to exactly one of those edges. Hence the **mean active-channel multiplicity per physical disagreement edge**, averaged over the random basis, satisfies for \(J(f)>0\)
\[
\boxed{
\frac{2\alpha_n}{N}
\le
\frac{\mathbb E_{\mathcal B}Q_{\mathcal B}(f)}
{|\mathcal D_f|}
\le
\frac{4\beta_n}{N},
}
\tag{5.7}
\]
whose asymptotic window is
\[
\frac{2+o(1)}n
\le
\text{mean multiplicity}
\le
\frac{4+o(1)}n.
\tag{5.8}
\]

The previous `<4/n` fixed-edge support-incidence theorem is therefore not merely a loose artifact: the \(1/n\) channel-density scale is unavoidable in total.

---

## 6. Genuine Boolean extremals for the spectral multiplier

The endpoint layers in (4.2) are not abstract spectral laws. They occur for simple quadratic Boolean phases.

### 6.1 Matching quadratic — lower multiplier

For even \(n\), let
\[
f_{\rm match}(x)
=
(-1)^{x_1x_2+x_3x_4+\cdots+x_{n-1}x_n}.
\tag{6.1}
\]
For every \(i\), \(\tau_i\) is a nonconstant character on exactly the paired coordinate. Thus its nonconstant squared Walsh mass is concentrated at \(|S|=1\), and \(I_i=1/2\). Consequently
\[
\boxed{
\mathbb E Q_{\mathcal B}(f_{\rm match})
=
\alpha_nJ(f_{\rm match})
=
\frac{n\alpha_n}{2}.
}
\tag{6.2}
\]

### 6.2 Complete quadratic — upper multiplier

For even \(n\), let
\[
f_{\rm complete}(x)
=
(-1)^{\sum_{1\le i<j\le n}x_ix_j}.
\tag{6.3}
\]
For each \(i\),
\[
\tau_i(x)=(-1)^{\sum_{j\ne i}x_j},
\tag{6.4}
\]
so all nonconstant squared derivative mass is at \(|S|=n-1\), again with \(I_i=1/2\). Hence
\[
\boxed{
\mathbb E Q_{\mathcal B}(f_{\rm complete})
=
\beta_nJ(f_{\rm complete})
=
\frac{n\beta_n}{2}
=
\frac{N-2}{2}.
}
\tag{6.5}
\]

Thus both endpoints of the radial derivative multiplier are attained by genuine Boolean functions.

---

## 7. Consequence for the signed-transport programme

This result does **not** bound the signed R32 load and does not alter the exact Aumann--Shapley disintegration. The R32 coefficients \(c_A\), including negative \(2\bmod4\) credits, remain signed and untouched; relation multiplicity and terminal membership remain where the compiler placed them.

It does, however, decisively kill one tempting replacement mechanism:

> **Killed shortcut:** “average over q-flip bases until the active q-flips themselves are so sparse that their number pays the transport.”

Equation (5.3) shows that this cannot happen: the active q-flip bank is intrinsically of order \(NJ/n\). The matching and complete quadratic examples show that the spectral multiplier itself cannot be improved below or above the endpoint layers by imposing Booleanity.

Combined with the earlier fleet02 singleton-syndrome obstruction, which makes an individual q-flip Aumann--Shapley load \(\Theta(N)\), the remaining route cannot be either (i) a pointwise channel-load bound or (ii) a channel-count bound. It must exploit **signed cancellation in the distribution of load across the active channels**.

The newest compatible fleet04/fleet03 work identifies exactly such a signed source object: the central-band two-sided plaquette-plus-terminal field and its Ward/Hardy resolvent. The theorem here supplies a natural measure against which that field should be studied: the derivative-spectral channel measure
\[
\mu(i,S)
:=
\frac12\widehat{\tau_i}(S)^2K_{n-1}(|S|).
\tag{7.1}
\]
The next useful estimate should be a **size-biased signed-load inequality** under \(\mu\), not a new unsigned incidence estimate.

A concrete residual target is to prove a truncation/payment statement of the following shape for the true signed Aumann--Shapley load \(L_v\):
\[
\mathbb E_{\mathcal B}
\sum_{v:z_v=-1}
\Psi\!\left(\frac{L_v}{N}\right)
\lesssim J(f),
\tag{7.2}
\]
for a convex/truncated \(\Psi\) chosen so that the low-load part is paid by (5.3) while the high-load tail is paid from the existing signed plaquette/R16 refund bank. Equation (7.2) is **not proved here**; it states the now-isolated universal obligation. Any valid implementation must keep negative R32 credits inside the load before truncation and must not double-spend the terminal mixed difference.

---

## 8. Exact self-check

`verify_qflip_channel_density.py` uses only Python standard-library exact rational arithmetic. It verifies:

* the direct combinatorial multiplier sum equals (3.1), its strict ordering, and the endpoint formulas for \(2\le n\le10\);
* all **272** Boolean functions on \(n=2,3\): direct random-anchor/pivot expectation equals the spectral formula (3.2), both variance and \(J\)-bounds hold, and every character twist leaves the q-flip count invariant;
* a deterministic exact sample of **512** Boolean functions on \(n=4\);
* the matching and complete quadratic endpoint families at \(n=2,4,6,8\).

The checker returned `PASS`. Its local pre-commit SHA-256 is
`072340beb025ffb4fb4406d64dc9ee728566b7740516e9f556e21ced1016d1ff`;
the final repository Git blob is
`4e03c805e467a65cfaa0f5b72f2cc2495abf9b6e`, matching the tested local Git blob.
The clean JSON output SHA-256 is
`30769bd01d36a5961742cdbf7d54d8f6c89ccdccb07553b1b6f57c07a2495b65`,
with repository blob
`f70635060fb9416bf6d72e7e249024d89b7c9735`.

A failed transfer is deliberately retained in history. The first create-only checker commit accidentally used the stale loop variable `n` on the deterministic `n=4` sample line; it was **not** the locally executed byte sequence and is not accepted as verification. Readback exposed the mismatch immediately. The next commit corrected that one transcription, and its returned content blob exactly matches the locally executed script. No scientific claim relies on the failed transfer.

These calculations are falsification evidence for the formulas exercised by the code. The universal statements (3.2)--(6.5) are proved analytically above.

---

## 9. Primary-literature check and status

A fresh 21 September 2026 arXiv check found Potapov, **“On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions”** (arXiv:2609.21563, submitted 18 September 2026), proving the conjecture for plateaued functions with sharp class constant 4 and for partially bent functions with sharp class constant 2. González--MacManus--Pereyra, **“Further evidence towards the Fourier Entropy-Influence conjecture”** (arXiv:2606.00246, submitted 29 May 2026), treats the unrestricted statement as the conjecture and proves further structured/stopping-tree cases. I make **no novelty claim** for the q-flip channel identity based on this search, and no search miss is evidence of priority.

The owner continuation records a newer external numerical lower-bound correction and a cancellation-constant obstruction. Those are preserved as current route constraints; this run does not re-audit or claim priority for them.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
