TASK: B17 ACCOUNT: account02 RUN: 2026-09-21T18:11:22.004162Z — positive XOR-coupling obstruction for shared-variable products and a defect-coded replacement

MODEL: GPT-5.6 Sol (runtime self-report)
THINKING LEVEL: UNKNOWN / UNVERIFIED; requested=maximum actually supported; configured selector not exposed
THINKING USAGE: provider reasoning tokens/time NOT_EXPOSED
RESEARCH EXECUTION: WITHOUT_VERIFIED_BRAIN
STATUS: PARTIAL. Full uniform-cube Friedgut–Kalai Fourier entropy-influence conjecture remains OPEN / NOT PROVED.

Fresh scientific source at entry: yspennstate/math-open-problems master 385fa72dde1a1105c9145c9667232c1adf1c515b. During the run master advanced to 04591fd51670eadae81bb0c667b601756049f13f; the latter interactive report was read before finalizing this note. It adds centered restriction/refund identities and scalar-profile obstructions, but does not address the positive shared-product coupling obstruction proved below.

This run is deliberately different from B17's immediately preceding strict-superset receiver flow. It attacks a shared-variable composition mechanism. The three FLEET_RULES moves used are:
- #2 ATTACK THE NEGATION FIRST: test the strongest possible classical coupling representation before trying to prove an entropy composition inequality from it;
- #18 SAY IT IN ANOTHER LANGUAGE: recast coherent Fourier multiplication as a three-marginal XOR transportation problem;
- #20 FIND WHY THE ALGORITHM FAILS: identify a subgroup-cut / Fréchet obstruction, then replace exact feasibility by a quantified coupling defect.

No publication-priority claim is made.

## 1. Named universal obstruction

For Boolean phases a,b on the same n-cube, multiplication is coherent XOR convolution:
\[
\widehat{ab}(s)=\sum_t \widehat a(t)\widehat b(s\oplus t).
\]
The squared spectrum of ab is therefore not the ordinary XOR convolution of the squared parent spectra. Recent fleet work retains that interference with a signed coupling or a signed coherent correction. A tempting stronger route would remove signs completely:

> FALSE POSITIVE XOR-COUPLING LEMMA. For every Boolean a,b there is a genuine probability coupling (A,B) whose marginals are
> \[
> \Pr(A=s)=\widehat a(s)^2,\qquad
> \Pr(B=s)=\widehat b(s)^2,
> \]
> and whose XOR has the child spectral law
> \[
> \Pr(A\oplus B=s)=\widehat{ab}(s)^2.
> \]

If true, data processing would immediately give
\[
H(ab)=H(A\oplus B)\le H(A,B)\le H(a)+H(b),
\]
so it is a natural sign-free shared-composition mechanism to test.

This run proves that the lemma is false by an exact all-dimensional Boolean family, and more sharply shows that its failure persists when the two parent physical boundary sets have ZERO simultaneous-flip overlap. Thus the missing coupling defect cannot be paid only by the standard product-influence overlap refund.

This is not a counterexample to FEI.

## 2. Exact Boolean family

Work on \(G=\mathbb F_2^n\), \(N=2^n\), with \(n\ge3\). For \(u\in G\) define the one-point defect
\[
f_u(x)=1-2\mathbf 1_{\{x=u\}}.
\]
Fix \(v\) of Hamming weight at least two and set
\[
a=f_0,\qquad b=f_v,\qquad h=ab.
\]
Then h equals -1 at exactly the two points 0 and v.

With normalized Walsh transform,
\[
\widehat f_u(0)=1-\frac2N,
\qquad
\widehat f_u(s)=-\frac2N(-1)^{s\cdot u}\quad(s\ne0).
\]
Consequently both parents have the same squared spectral law p:
\[
p(0)=\frac{(N-2)^2}{N^2}=:w,
\qquad
p(s)=\frac4{N^2}\quad(s\ne0).
\tag{2.1}
\]

For the product h,
\[
\widehat h(0)=1-\frac4N,
\qquad
\widehat h(s)=-\frac2N(1+(-1)^{s\cdot v})\quad(s\ne0).
\]
Let
\[
K=v^\perp=\{s:s\cdot v=0\}.
\]
The child spectral law r is therefore supported exactly on K:
\[
r(0)=\frac{(N-4)^2}{N^2},
\qquad
r(s)=\frac{16}{N^2}\ \ (s\in K\setminus\{0\}),
\qquad
r(s)=0\ \ (s\notin K).
\tag{2.2}
\]

## 3. PROVED: subgroup-cut obstruction to every positive coupling

### Lemma 3.1 — subgroup-cut Fréchet condition

Let p,q be probability laws on a finite abelian 2-group G and let K be a subgroup. Suppose a coupling (A,B) has \(A\oplus B\in K\) almost surely. Then A and B lie in the same K-coset almost surely. In particular, for any K-coset C and any \(x\in C\),
\[
\Pr(A=B=x)\ge p(x)+q(x)-m_C,
\tag{3.1}
\]
where \(m_C=\Pr(A\in C)=\Pr(B\in C)\).

Proof. XOR in K is equivalent to A and B having the same image in G/K. Hence coupling mass decomposes independently over common cosets. In a fixed C, the row event {A=x} and column event {B=x} have masses p(x),q(x) inside a block of total mass \(m_C\). The ordinary Fréchet inequality gives (3.1). QED.

### Theorem 3.2 — no exact positive XOR spectral coupling

For the Boolean pair \(a=f_0,b=f_v\) above, no positive coupling of their two spectral laws can have XOR law equal to the squared spectrum of \(h=ab\).

Proof. If the XOR law were r, (2.2) would force \(A\oplus B\in K\) almost surely. The parent p-mass of K is
\[
\alpha=p(K)
=w+\left(\frac N2-1\right)\frac4{N^2}
=1-\frac2N.
\tag{3.2}
\]
Apply Lemma 3.1 in C=K at x=0. Any such coupling must satisfy
\[
\Pr(A=B=0)\ge2w-\alpha
=1-\frac6N+\frac8{N^2}.
\tag{3.3}
\]
But the target XOR-zero mass is
\[
r(0)=1-\frac8N+\frac{16}{N^2}.
\tag{3.4}
\]
Their difference is
\[
(2w-\alpha)-r(0)
=\frac{2(N-4)}{N^2}>0
\qquad(N\ge8).
\tag{3.5}
\]
Since \(\{A=B=0\}\subseteq\{A\oplus B=0\}\), (3.3) contradicts (3.4). QED.

This is stronger than observing that one canonical signed Fourier coupling has negative atoms: it excludes EVERY classical positive coupling with the required three marginals for this exact Boolean family.

## 4. PROVED: quantitative distance from the positive coupling polytope

For an arbitrary coupling of p with itself, let s be its XOR law and put
\[
c=s(K^c)=\Pr(A,B\text{ lie in different }K\text{-cosets}).
\]
Because both marginals give K the same mass \(\alpha\), the two directed cross-coset flows each have mass c/2. Hence the K-by-K block has total mass \(\alpha-c/2\).

Let x and y be the amounts of the row-0 and column-0 masses sent across the coset cut. Then \(x+y\le c\). Applying Fréchet inside the K-by-K block,
\[
\pi_{00}\ge (w-x)+(w-y)-(\alpha-c/2)
\ge2w-\alpha-c/2.
\]
Therefore for the event \(E=\{0\}\cup K^c\),
\[
s(E)\ge\pi_{00}+c\ge2w-\alpha+c/2\ge2w-\alpha.
\]
The target r is supported on K, so \(r(E)=r(0)\). Thus every positive parent coupling obeys
\[
\boxed{
\operatorname{TV}(s,r)\ge
\frac{2(N-4)}{N^2}.
}
\tag{4.1}
\]

At n=3, take \(v=3=(011)_2\). Then
\[
p=(9,1,1,1,1,1,1,1)/16,
\]
while r is uniform on the four-point subgroup
\[
K=\{0,3,4,7\}.
\]
Equation (4.1) gives TV >=1/8. The exact checker supplies a positive 8-by-8 coupling with row and column sums p whose XOR law is
\[
(6,0,0,2,4,0,0,4)/16.
\]
Its TV distance from r is exactly 1/8. Therefore
\[
\boxed{\Gamma(f_0,f_3)=1/8}
\tag{4.2}
\]
for the coupling-defect functional defined in Section 6 below.

## 5. PROVED: overlap-only repair is impossible

For Boolean a,b define their physical simultaneous-flip overlap
\[
R(a,b)
=\sum_{i=1}^n
\Pr_x[
a(x)\ne a(x\oplus e_i)
\ \text{and}\
b(x)\ne b(x\oplus e_i)].
\tag{5.1}
\]
The exact product identity is
\[
I(ab)=I(a)+I(b)-2R(a,b).
\tag{5.2}
\]

For a one-point defect, every coordinate influence equals 2/N, so
\[
I(f_u)=\frac{2n}{N}.
\tag{5.3}
\]
If \(|v|\ge2\), the two stars of physical edges incident to 0 and v are disjoint. Hence
\[
R(f_0,f_v)=0,
\qquad
I(f_0f_v)=I(f_0)+I(f_v)=\frac{4n}{N}.
\tag{5.4}
\]
Yet Theorem 4.1 gives a strictly positive coupling defect.

Consequently every proposed inequality of the form
\[
\Gamma(a,b)\le C\,R(a,b)
\tag{5.5}
\]
is false for every finite C. More generally, the positive-coupling interference defect cannot be funded solely by the influence cancellation \(I(a)+I(b)-I(ab)\).

This isolates the precise obstruction: coherent Fourier phase information can obstruct a classical XOR coupling even when multiplication has no physical boundary cancellation at all.

## 6. Replacement route: nearest positive coupling plus a mismatch code

Exact positive coupling is too strong, but its quantified failure yields a clean always-valid composition inequality.

For Boolean a,b on \(G=\mathbb F_2^n\), let \(P_a,P_b,P_{ab}\) be their squared Fourier laws and define
\[
\Gamma(a,b)
=
\min_{\pi\in\Pi(P_a,P_b)}
\operatorname{TV}\!\left(
P_{ab},
\operatorname{Law}_{(A,B)\sim\pi}(A\oplus B)
\right).
\tag{6.1}
\]
The finite coupling polytope is compact, so the minimum is attained.

### Theorem 6.1 — defective positive-coupling entropy composition

For every Boolean a,b,
\[
\boxed{
H(ab)
\le
H(a)+H(b)
+h_2(\Gamma)
+\Gamma\log_2(2^n-1).
}
\tag{6.2}
\]

Proof. Choose an optimal parent coupling and let Q=A xor B have law s. Since Q is a deterministic function of (A,B),
\[
H(Q)\le H(A,B)\le H(A)+H(B)=H(a)+H(b).
\]
Take a maximal coupling of Q with a random variable Z having law \(P_{ab}\), so
\[
\Pr(Z\ne Q)=\operatorname{TV}(s,P_{ab})=\Gamma.
\]
Let E be the mismatch indicator. Given Q and E=0, Z is known; given Q and E=1, at most \(2^n-1\) labels remain possible. Hence
\[
H(Z\mid Q)
\le h_2(\Gamma)+\Gamma\log_2(2^n-1).
\]
Then
\[
H(ab)=H(Z)\le H(Q)+H(Z\mid Q),
\]
giving (6.2). QED.

Equation (6.2) is not a proof of FEI: the raw Fannes term contains ambient dimension. Its value is structural. It turns signed shared-variable interference into one explicit positive quantity, \(\Gamma\), and separates two tasks:
1. construct a near-XOR positive coupling;
2. code the mismatch more cheaply than an arbitrary ambient label.

For the two-defect obstruction,
\[
\Gamma\ge\delta_N:=\frac{2(N-4)}{N^2}\asymp\frac2N,
\]
while each parent has influence \(2n/N\). Thus the unavoidable defect is small enough that its NATURAL ADDRESS COST, \(\delta_N n\), is already on the parent-influence scale, even though it cannot be charged to overlap R, which is exactly zero:
\[
\delta_N n
=
\frac{2n(N-4)}{N^2}
<
\frac{2n}{N}
=I(f_0).
\tag{6.3}
\]

This points to the sharper replacement target:

> COST-SENSITIVE COUPLING TARGET. Couple the parent spectra positively and attach a mismatch offset/tag whose expected description length is \(O(I(a)+I(b))\), rather than demanding exact XOR equality or bounding raw TV by the overlap refund.

One concrete formulation is to replace the last term of (6.2) by the actual conditional mismatch entropy:
\[
H(ab)
\le H(a)+H(b)+h_2(\Gamma)
+\Gamma\,H(Z\mid Q,E=1),
\tag{6.4}
\]
and seek a Boolean construction of the coupling for which the final two terms are paid by parent boundary/influence resources with bounded congestion.

This route is compatible with the recent signed-transport work but does not throw away its obstruction: exact positive coupling is impossible, so a mismatch channel is mathematically necessary. It is also different from the refuted receiver-only support-poset transport: the resource is a cross-spectrum transportation/coding defect, not a strict-superset receiver.

The remaining universal gap is therefore precise:
\[
\text{construct a dimension-free influence-paid mismatch code for shared-variable spectral multiplication.}
\]
No such theorem is proved here.

## 7. Exact checker

`verify_positive_xor_coupling.py` uses only integer Walsh transforms and `fractions.Fraction`. It checks:
- the exact one-point and two-point spectra for n=3,...,12;
- the subgroup K mass, Fréchet floor and TV lower bound \(2(N-4)/N^2\);
- zero simultaneous physical-flip overlap for the Hamming-distance-two defects;
- the exact parent and child influences;
- the n=3 rational transportation witness with TV exactly 1/8.

The all-dimensional obstruction in Sections 2–5 is analytic; the finite checks only verify the implementation and the sharp 8-point witness.

Checker SHA-256:
d2603f570ec449b1f005a016680e728177692c87458b683ad848146e7f820977

Recorded output SHA-256:
e0e3929303b0c587ad6f071fe0bfa47db33dca8d0e99c774454ea615f7355668

## 8. Literature and repository applicability check

Current primary literature checked before the claim language was finalized:
- O'Donnell–Tan, arXiv:1304.1347 (2013), gives an FEI composition theorem for disjoint input blocks. Its hypotheses do not supply the shared-variable positive XOR coupling attacked here.
- Xiao Han, Combinatorica 45 (2025), proves the general bound \(H(f)=O(I(f)+\sum_i I_i\log(1/I_i))\), not the shared-product coupling statement.
- González–MacManus–Pereyra, arXiv:2606.00246 (29 May 2026), develops restriction/stopping criteria for classes satisfying local entropy-loss inequalities.
- Potapov, arXiv:2609.21563 (18 Sep 2026), proves FEI for plateaued functions with sharp class constant 4 and for partially bent functions with sharp class constant 2.

Repository dependencies read include account04/B16's canonical signed Fourier transport and account02/B16's coherent positive-reference product ledger. Those establish that signs/interference are real and must be retained. The present result is narrower and complementary: an exact Boolean family proves that the desired THREE positive marginals are outside the classical coupling polytope altogether.

No assertion is made that the subgroup-cut lemma, the defect functional Gamma, or the defective composition inequality is absent from the broader literature. Publication novelty is NOT CLAIMED.

## 9. Before / after

Before:
- signed shared-variable transport was known to carry negative internal mass;
- the incoherent independent-XOR reference was known not to dominate the true spectrum in the required entropy/influence directions;
- it remained conceivable that a better non-independent POSITIVE parent coupling could realize the child spectrum.

After:
- exact positive realization is refuted for every n>=3 by a genuine Boolean two-defect family;
- the separation is quantitative: TV >= \(2(N-4)/N^2\), sharp at n=3 with minimum 1/8;
- the defect remains positive while physical simultaneous-flip overlap is exactly zero, killing overlap-only repair;
- an always-valid nearest-coupling entropy inequality (6.2) reduces the new route to influence-paid mismatch coding.

Full FEI remains OPEN / NOT PROVED.
