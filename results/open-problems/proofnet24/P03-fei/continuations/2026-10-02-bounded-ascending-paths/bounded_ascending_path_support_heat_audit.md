# Independent full analytic audit of bounded ascending-path FEI

Date: 2026-10-02. **PASS**, including the subsequent sharper constant.
I read the complete unchanged
[candidate](bounded_ascending_path_support_fei_candidate.md), read its
[author checker](verify_bounded_ascending_path_support.py), independently
implemented a separate checker, and checked the published primary
operator theorem. This is an internal mathematical audit, not an external
review or a novelty certificate. General Boolean FEI remains unresolved.
I then read the complete separate
[final proof](bounded_ascending_path_support_fei_proof.md), including the
new cotangent refinement, singleton sharpness and weighted-band section.
All added mathematical sections also pass.

## Exact statement audited

If either label support of a Boolean function on the uniform cube has no
ascending cube-edge path with more than `k` **vertices**, then the
candidate proves

\[
 H(f)\le(4+2\log_2e)(k+1)^2 I(f).
\]

The root's subsequent elementary entropy improvement gives the valid
stronger conclusion

\[
 \boxed{H(f)\le4(k+1)^2I(f).}
\]

When `k=1`, the stronger exact energy identity instead gives
\(H(f)\le4I(f)\). The latter constant is asymptotically optimal, already
for a singleton label class. No monotonicity, symmetry, contiguous-layer,
minority-support or antichain premise is required.
The final proof further gives the valid sharper general bound
\(H(f)\le4\cot^2(\pi/[2(k+1)])I(f)\), as checked below.

## Compressed raising operator and indexing

I independently checked all normalizations. With cube adjacency `A` and
\(L=(n\operatorname{Id}-A)/2\), the Walsh eigenvalue is \(|S|\), and

\[
 \langle u,Lu\rangle
 =\frac14\sum_i\mathbb E|u(X)-u(X^{\oplus i})|^2.
\]

For Boolean `f` this equals physical flip influence. For
\(f=1-2\mathbf1_E\), it equals four times the indicator energy. Thus

\[
 I(f)=2\{np-\langle\mathbf1_E,A\mathbf1_E\rangle\},
 \qquad p=\Pr(E).
\]

The upward block from rank `s` to `s+1` has squared norm at most
\((s+1)(n-s)\): Cauchy--Schwarz at each output uses its `s+1`
predecessors, and each input occurs in `n-s` outputs. Different blocks
have orthogonal input spaces and orthogonal output spaces, so the norm
of their direct sum is their maximum, bounded by `(n+1)/2`.

After projection to `E`, entries of \(U_E^j\) count paths of `j` upward
edges staying in `E`. They are nonnegative, so no cancellation can
hide a path. Exactly `k` **edges** would require `k+1` vertices; therefore
the stated `k`-vertex hypothesis gives \(U_E^k=0\), with no off-by-one
error. A general inclusion chain can skip absent intermediate vertices,
so the path hypothesis is strictly weaker than the `k`-Sperner condition.
The proof never replaces this weaker hypothesis by the stronger one.

## Nilpotent numerical radius: complete dilation audit

For a contraction `T` with \(T^k=0\), put
\(D=(\operatorname{Id}-T^*T)^{1/2}\) and
\(Vh=(Dh,DTh,\ldots,DT^{k-1}h)\). The norm identity telescopes to
\(V^*V=\operatorname{Id}\), because the final term
\(\|T^kh\|^2\) vanishes. For the backward shift `B`, the final coordinate
of `VT h` is also zero, so **exactly** \(VT=BV\). No commutation of `D`
and `T` is asserted or needed. Consequently

\[
 |\langle Th,h\rangle|
 =|\langle BVh,Vh\rangle|\le w(B)\|h\|^2.
\]

Diagonal phases conjugate every Hermitian real part of `B` to the
unphased path adjacency divided by two. Its sine eigenvectors give
\(w(B)=\cos(\pi/(k+1))\). Scaling establishes the required inequality,
including zero `T` and `k=1`. Since `A_E=U_E+U_E*` is Hermitian,
its absolute Rayleigh quotients are bounded by `2w(U_E)`, giving the
stated operator-norm bound. It is correct to use the absolute operator
norm here, not only the largest positive eigenvalue.

The credited primary result is Haagerup--de la Harpe, *The numerical
radius of a nilpotent operator on a Hilbert space*, Proc. AMS 115 (1992),
371--379, Theorem 1 on printed page 372. I opened the
[University of Geneva author archive](https://archive-ouverte.unige.ch/unige:12076)
and its
[published primary PDF](https://access.archive-ouverte.unige.ch/access/metadata/2e3d55fc-f7d2-42af-95ae-6c06df864dbb/download).
The citation and mathematical statement match; the candidate's proof
supplies the complete particular finite-dimensional argument itself.
This operator result is established prior work.

## Large and small dimensions, either support label

Set \(K=(k+1)^2\). If `n>=K`,
\(1-\cos(\pi/(k+1))\ge2/K\) gives

\[
 n-(n+1)\cos(\pi/(k+1))
 \ge2(n+1)/K-1\ge n/K.
\]

The last inequality needs only `n+2>=K`, which is satisfied. Thus
\(np\le KI(f)/2\). Replacing `p` by the minority density
\(r=\min(p,1-p)\le p\) is valid; it does not require the minority
label itself to meet the path hypothesis.

If `n<K`, the Fourier Poincare inequality gives
\(I(f)\ge\operatorname{Var}(f)=4r(1-r)\ge2r\), hence
\(nr\le KI(f)/2\). For `k=1` there are no internal edges at all,
and the exact identity is \(I(f)=2np\ge2nr\). Constants, empty/full
supports and dimension zero are correctly disposed of separately.

## Full entropy, and the improved constant

Write \(q=4r(1-r)\) for the nonempty Fourier mass. Splitting off the
empty atom gives
\(H(f)\le h_2(q)+qn\), including `q=1` by continuity. The original
candidate's estimate \(H(f)\le4(2+\log_2e)nr\) is valid.

The root's sharper argument also passes. Let
\(L=\log_2(1/r)\). For `r<=1/4`, the universally valid bound

\[
 h_2(q)\le q[\log_2(1/q)+\log_2e]
 =q\left[L+\log_2\frac{e}{4(1-r)}\right]
 \le qL\le4rL
\]

uses \(4(1-r)\ge3>e\). This binary-entropy upper bound is valid even
when `q>1/2`; no monotonicity of `h_2` is required. For
`1/4<=r<=1/2`, use \(h_2(q)\le1\le4r\le4rL\). Finally a nonempty
minority has \(r\ge2^{-n}\), so `L<=n`. It follows that

\[
 H(f)\le4rL+4rn\le8nr.
\]

Combining with the audited energy estimates proves the sharper constants
stated above. For a singleton, `r=2^-n`, every nonempty coefficient has
squared mass \(4r^2\), so

\[
 H(f)=e((1-2r)^2)+(2^n-1)e(4r^2),\qquad I(f)=2nr,
\]

and \(H(f)/I(f)\to4\). Thus the `k=1` constant cannot be decreased.

## Final-version cotangent and weighted-band additions

Let \(c=\cos(\pi/(k+1))\) and
\(n_*=(1+c)/(1-c)=\cot^2(\pi/[2(k+1)])\). Poincare and `H<=8nr`
give `H/I<=4n`. The operator energy gives `H/I<=4n/d_n` when
\(d_n=n-(n+1)c>0\). At `n=n_*`, exactly `d_n=1`. For `n<=n_*`
the first bound is at most `4n_*`; for `n>=n_*`, `d_n>=1` and

\[
 \frac{d}{dn}\frac{n}{n(1-c)-c}
 =-\frac{c}{[n(1-c)-c]^2}\le0.
\]

Thus the second bound is also at most `4n_*`. Treating `n` as a real
variable to maximize this upper bound is legitimate for integer
dimensions. When `k=1`, `c=0`, `n_*=1`, and `n/d_n=1` exactly.
Both the sharpened theorem and the equivalent sharpened support-energy
estimate pass.

For the weighted-band corollary, **every coordinate** has weight at least
`a>0`, or is nonzero with absolute weight at least `a` after coordinate
sign flips. Every upward edge increases the score by at least `2a`.
A label support contained in a closed width-`D` band therefore has paths
of at most `floor(D/(2a))+1` vertices. The floor convention is valid at
attained closed endpoints; if `D<2a` no internal cube edge exists.
Arbitrary internal label choices only remove paths and do not harm this
containment argument. Zero-weight coordinates with arbitrary internal
decisions are correctly excluded from this corollary. It concerns an
entire label support and does not infer a perturbation theorem for a
threshold with an unrelated background.

## Independent verification and its limits

My independent implementation is
[verify_bounded_ascending_path_support_heat.py](verify_bounded_ascending_path_support_heat.py),
with the complete report
[bounded_ascending_path_support_heat_checks.json](bounded_ascending_path_support_heat_checks.json).
It imports no author script or local research helper. The run exited zero.

* All **65,814** supports through dimension four and **246** additional
  random/structured supports through dimension sixteen: **66,060** total.
* **66,060** integer Walsh Parseval and physical-energy checks. The
  support-energy inequality is checked by exact integer multiplication
  `n*minority_size <= (k+1)^2*undirected_boundary`.
* **782** genuine large-dimension cases, **26,551** nonminority supports,
  **812** nonconstant edge-free supports, and **7,468** families with a
  longer inclusion chain than their maximum induced ascending path.
* **74** explicit integer compressed-matrix nilpotency and internal-edge
  checks, with adjacency eigenvalues tested separately in floating point.
* **27** general nonnormal nilpotent-contraction dilations, independently
  checking the isometry/intertwining matrices and sampled numerical radii.
* The sharpened entropy estimate and **cotangent** final constant are checked for all
  **66,042** nonconstant supports, with entropy calculated in floating
  point and not claimed exact. The largest tested entropy/target ratio
  was approximately `0.934941`.

The separate author report remains an additional independent suite.
The full analytic proof, rather than the finite instances, establishes
the theorem. This audit does not establish historical priority, a strong
`I-Var` version, arbitrary composition, or full Boolean FEI.
