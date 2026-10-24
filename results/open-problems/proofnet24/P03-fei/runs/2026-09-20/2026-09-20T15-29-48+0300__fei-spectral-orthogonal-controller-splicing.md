Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** The requested GPT-6 / maximum setting is not authenticated by the exposed runtime.

# P03 FEI — spectral-orthogonal controller splicing and exact Hellinger surcharge

## 0. Parent status and mechanism delta

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove a finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean sign function on every finite uniform cube.

**Source-level status before -> after:** **OPEN -> OPEN.** The unrestricted universal finite constant remains **UNKNOWN -> UNKNOWN**. P03's inherited native finite-dimensional atlas remains **6 -> 6**. No finite search, controller closure, or fresh-control theorem below is promoted to full FEI.

**Mechanism gain.** The newest P03 theorem already proves `J_i^rec<=B_i`, hence `S_T<=R_T` and `R_T<=H<=2R_T` on every full physical restriction tree. The newest NM13-02 theorem proves that a complete physical query of a block `A` costs at most its one-shot conditional spectral entropy `B_A=H(S_A|S_Ac)`. This run proves an exact factorization of that block cost for a new dependent splice geometry. The factorization isolates one virtual one-bit hereditary allocation term. For isospectral residual siblings that term vanishes exactly, giving a zero-surcharge hereditary max-splice with no controller-depth loss. For approximate siblings it is bounded by a child-spectrum Hellinger defect with the inherited KL rebate.

The theorem strictly refines NM13-02's balanced-controller estimate `B_A<=h2(alpha)+alpha H(h)`: the scalar `h2(alpha)` is replaced by an exact virtual-selector allocation `B_sel`, with

\[
B_{\rm sel}\le h_2(M)\le h_2(\alpha),
\]

where `M` is the child-spectrum Hellinger defect. In the isospectral case `M=B_sel=0` even when `alpha=1/2`.

---

## 1. Current state and exact scopes consumed

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`.

Current P03 entrypoint: `proofnet24/P03-fei/README.md`, blob `d226f1c4a460a0f90ba25f40a8a6b6a8d03ab2e9`. Full FEI remains open. Its correction chain is preserved: the false pointwise erasure shortcut, fixed-affine drift, old resolvent/interpolation target, all-coordinate absolute-overlap selector, derivative-degree scalar scheduling, blind curvature payment, fixed-`s<2` Renyi payment, frozen-parent endpoint payment, and related superseded scalar routes remain retired.

The owner directive `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`, was read at its actual scope. Its theorem

\[
L(\Gamma_c f)\le12\Delta_{\rm aff}(\Gamma_c f)
\]

requires appended fresh controls and the stated density hypothesis. It is not a fixed-domain hereditary theorem and is not used below.

Immediately preceding own substantive report:
`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T14-29-48+0300__fei-recombination-dominated-by-allocation.md`, blob `b8eae04b83f3518bdb9dc87e33734e616f2988e0`. It proves for every physical split

\[
J_i^{\rm rec}\le B_i,\qquad \Delta_iH\le2B_i,
\]

and hence `S_T<=R_T` and `R_T<=H<=2R_T` on every full physical tree. These are inherited facts, not relabeled as new here.

Newest complementary NM13-02 report:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T15-08-00+0300__block-compression-balanced-controller.md`, blob `c155fb1d672bfe9858463391f2db0d15c5b5559d`. It proves

\[
R_{\mathcal T_A}(f)\le B_A(f):=H(S_A\mid S_{A^c})
\]

for every complete adaptive physical `A`-prefix and the exact queried-influence identity `Q_{T_A}=I_A(f)`. Its balanced-controller result gives, for balanced `h` selecting residual branches `g_+,g_-` and `alpha=Pr[g_+\ne g_-]`,

\[
B_A(f)\le h_2(\alpha)+\alpha H(h),\quad
I_A(f)=\alpha I(h),\quad
I_Y(f)=\frac{I(g_+)+I(g_-)}2.
\]

Its erratum only changes a displayed `\nu_m` to `u_m` and changes no claim.

The scheduled P03 block report `proofnet24/P03-fei/scheduled-continuation/runs/2026-09-20/2026-09-20T12-05-16Z__report.md` was also consumed. It proves the arbitrary affine-block entropy sandwich `B_pi<=Delta_pi H<=2B_pi` and leaves a useful proper-block selector open.

A bounded fresh source check on 20 September 2026 found González--MacManus--Pereyra, arXiv:2606.00246, still stating universal FEI as a conjecture and explaining that a universal restriction inequality would imply it; the paper proves restricted stopping-tree classes. Current literature continues to attribute FEI to Friedgut--Kalai (1996). A bounded search for the exact theorem below returned no matching arXiv result. That is negative search evidence only; **publication priority is UNVERIFIED**.

Root `POSTED.md` was checked. The posted/excluded Kalai item is the entropy/singularity manuscript, not the block-splicing theorem below.

---

## 2. Different routes tried in this run

### A. Proper co-singleton selector — not promoted

Querying all but one coordinate would leave one-bit leaves and therefore no residual hereditary entropy. Thus a universal proper co-singleton estimate

\[
H(S_{[n]\setminus\{j\}}\mid S_j)\le K\sum_{i\ne j}\operatorname{Inf}_i(f)
\]

for some `j` would essentially prove FEI (up to the inherited factor two). Finite exploration found no decisive obstruction, but the route remains full-scope/circular: if an omitted coordinate is irrelevant, the block term can simply contain the original FEI instance on the remaining variables. No selector theorem is claimed.

### B. Coarse balanced-controller payment — valid but depth-loss is intrinsic to that envelope

For NM13's balanced controller, let `r=g_+g_-` and `delta=min(alpha,1-alpha)`. Edge isoperimetry gives

\[
I(r)\ge2\delta\log_2(1/\delta)\ge h_2(\delta)=h_2(\alpha),
\]

while edgewise XOR gives `I(r)<=I(g_+)+I(g_-)=2I_Y(f)`. Also balanced `h` has `I(h)>=1`, so `I_A(f)=alpha I(h)>=alpha`. Hence

\[
B_A(f)\le \alpha H(h)+I_Y(f)+\frac1{\ln2}I_A(f).
\tag{2.1}
\]

This produces a `+1` residual coefficient under recursion. The coefficient cannot be removed inside this two-budget scalar envelope: if

\[
h_2(\delta)\le a\delta+b\delta\log_2(1/\delta)
\]

for all sufficiently small `delta`, division by `delta log_2(1/delta)` and `delta->0` forces `b>=1`. Thus depth-free closure needs spectral information discarded by `h_2(alpha)`.

### C. Spectral-orthogonal factorization — SUCCESS

The successful route retains exactly that missing spectral information and identifies the true surcharge as a conditional spectral branch entropy rather than the unconditional `h_2(alpha)`.

---

## 3. Exact spectral-orthogonal controller theorem

Let `A` and `Y` be disjoint physical coordinate blocks. Let Boolean controller phases

\[
u_0,u_1:\{-1,1\}^A\to\{-1,1\}
\]

satisfy pointwise Fourier-support orthogonality

\[
\boxed{\widehat u_0(U)\widehat u_1(U)=0\quad\forall U\subseteq A.}
\tag{3.1}
\]

Let arbitrary Boolean residual siblings `g_+,g_-:{-1,1}^Y->{-1,1}` be given, and put

\[
c=\frac{g_++g_-}{2},\qquad d=\frac{g_+-g_-}{2}.
\tag{3.2}
\]

Pointwise `c,d in {0,±1}`, `cd=0`, and `c^2+d^2=1`. Define

\[
\boxed{F(a,y)=u_0(a)c(y)+u_1(a)d(y).}
\tag{3.3}
\]

Thus `F` is Boolean. Put

\[
\beta=\|d\|_2^2=\Pr[g_+\ne g_-].
\tag{3.4}
\]

Define the virtual selector

\[
G(s,y)=c(y)+s d(y),\qquad s\in\{-1,1\},
\tag{3.5}
\]

whose two sections are `g_+` and `g_-`, and write

\[
B_{\rm sel}(g_+,g_-):=H_G(S_s\mid S_Y).
\tag{3.6}
\]

The bit `s` is only analytic notation for the already-given two-column Fourier fibre; no fresh variable is appended to `F` or to the theorem's domain.

### Theorem 3.1

For every such `F`,

\[
\boxed{
B_A(F)=(1-\beta)H(u_0)+\beta H(u_1)+B_{\rm sel}(g_+,g_-).
}
\tag{3.7}
\]

Moreover

\[
\boxed{I_A(F)=(1-\beta)I(u_0)+\beta I(u_1),}
\tag{3.8}
\]

\[
\boxed{I_Y(F)=\frac{I(g_+)+I(g_-)}2.}
\tag{3.9}
\]

These are all-dimensional exact identities with no fresh-control, low-degree, symmetry, independence, or character-child assumption.

### Proof

For `U subseteq A`, `T subseteq Y`, Fourier factorization gives

\[
\widehat F(U,T)=\widehat u_0(U)\widehat c(T)+\widehat u_1(U)\widehat d(T).
\]

By (3.1), the cross term vanishes pointwise in `U`, hence

\[
\widehat F(U,T)^2
=\widehat u_0(U)^2\widehat c(T)^2+\widehat u_1(U)^2\widehat d(T)^2.
\tag{3.10}
\]

Parseval and (3.2) give

\[
\sum_T\widehat c(T)^2=1-\beta,
\qquad
\sum_T\widehat d(T)^2=\beta.
\tag{3.11}
\]

So the joint spectral law of `(S_A,S_Y)` is a disjoint mixture of two product laws: a `u_0\otimes c` component of mass `1-beta` and a `u_1\otimes d` component of mass `beta`. Let `Z` be the component label. Because the Fourier supports of `u_0,u_1` are disjoint, `Z` is a deterministic function of `S_A` on the support. Conditional on `Z`, the controller and residual spectral labels are independent. Therefore

\[
\begin{aligned}
H(S_A\mid S_Y)
&=H(Z,S_A\mid S_Y)\\
&=H(Z\mid S_Y)+H(S_A\mid Z,S_Y)\\
&=H(Z\mid S_Y)+(1-\beta)H(u_0)+\beta H(u_1).
\end{aligned}
\tag{3.12}
\]

For the virtual selector `G`, the Fourier coefficient with selector bit absent is `\widehat c(T)` and with it present is `\widehat d(T)`. Thus its joint `(S_s,S_Y)` law is exactly

\[
\Pr(S_s=0,S_Y=T)=\widehat c(T)^2,\qquad
\Pr(S_s=1,S_Y=T)=\widehat d(T)^2,
\]

which is the same `(Z,S_Y)` law. Hence `H(Z|S_Y)=B_sel`, proving (3.7).

Summing `|U|` against (3.10) and using (3.11) gives (3.8). Summing `|T|` gives

\[
I_Y(F)=\sum_T|T|\bigl(\widehat c(T)^2+\widehat d(T)^2\bigr).
\]

But coefficientwise

\[
\frac{\widehat g_+(T)^2+\widehat g_-(T)^2}{2}
=\widehat c(T)^2+\widehat d(T)^2,
\]

so (3.9) follows. QED.

---

## 4. Hellinger defect and KL rebate for the exact surcharge

Put

\[
q_T=\widehat c(T)^2+\widehat d(T)^2,
\qquad
m_T=\min\{\widehat c(T)^2,\widehat d(T)^2\}.
\]

Then

\[
\boxed{B_{\rm sel}=\sum_T q_T h_2\!\left(\frac{m_T}{q_T}\right).}
\tag{4.1}
\]

Let `M=sum_T m_T`. If

\[
P_\pm(T)=\widehat g_\pm(T)^2,
\qquad
\mathcal A=\sum_T\sqrt{P_+(T)P_-(T)},
\]

then

\[
\boxed{M=\frac{1-\mathcal A}{2}.}
\tag{4.2}
\]

Indeed `g_+=c+d`, `g_-=c-d` in Fourier space, so

\[
\sqrt{P_+(T)P_-(T)}=|\widehat c(T)^2-\widehat d(T)^2|,
\]

and, since `sum q_T=1`, subtracting the affinity gives `2 sum min = 2M`.

Also

\[
M\le\min\left\{\sum_T\widehat c(T)^2,\sum_T\widehat d(T)^2\right\}
=\min\{1-\beta,\beta\}.
\tag{4.3}
\]

By concavity of `h_2` on `[0,1/2]`, (4.1) gives the clean cap

\[
\boxed{B_{\rm sel}\le h_2(M).}
\tag{4.4}
\]

If `M>0`, define `\nu_T=m_T/M`. Using

\[
h_2(x)\le x\log_2(1/x)+x/\ln2
\]

inside (4.1) yields

\[
\boxed{
B_{\rm sel}\le M\left[
\log_2\frac1M-D_2(\nu\Vert q)+\frac1{\ln2}
\right].
}
\tag{4.5}
\]

Proof of (4.5):

\[
\sum_Tq_Th_2(m_T/q_T)
\le\sum_Tm_T\log_2(q_T/m_T)+M/\ln2,
\]

and, writing `m_T=M\nu_T`, the logarithmic sum equals
`M log_2(1/M)-M D_2(\nu||q)`.

Thus the only non-controller block surcharge is exactly the same Hellinger/KL profile that appeared in P03's earlier one-coordinate fibre analysis.

---

## 5. Exact zero-surcharge criterion

The following are equivalent:

1. `\widehat g_+(T)^2=\widehat g_-(T)^2` for every `T`;
2. `\widehat c(T)\widehat d(T)=0` for every `T`;
3. `M=0`;
4. `B_sel=0`.

Indeed

\[
\widehat g_+(T)^2-\widehat g_-(T)^2
=(\widehat c+\widehat d)^2-(\widehat c-\widehat d)^2
=4\widehat c(T)\widehat d(T).
\]

Hence (1)<->(2), while (2)<->(3) is the definition of `M`. Formula (4.1) then gives (3)<->(4). Therefore identical child squared Fourier laws remove the entire branch-label uncertainty even when their physical disagreement density is macroscopic.

---

## 6. Hereditary max-splicing theorem

Assume `F` is as above. Suppose the controller phases satisfy

\[
H(u_z)\le C_A I(u_z),\qquad z=0,1,
\tag{6.1}
\]

and both residual siblings admit full hereditary certificates

\[
R_{\mathcal T_\pm}(g_\pm)\le K_YI(g_\pm).
\tag{6.2}
\]

### Theorem 6.1

There is a full physical restriction tree for `F` with

\[
\boxed{
R_{\mathcal T}(F)
\le C_A I_A(F)+K_Y I_Y(F)+B_{\rm sel}(g_+,g_-).
}
\tag{6.3}
\]

Hence

\[
R_{\mathcal T}(F)
\le C_A I_A(F)+K_Y I_Y(F)+h_2(M),
\tag{6.4}
\]

with the sharper KL replacement from (4.5). If the siblings are isospectral, then

\[
\boxed{R_{\mathcal T}(F)\le\max\{C_A,K_Y\}I(F).}
\tag{6.5}
\]

### Proof

Query the complete controller block `A` first. NM13-02's block-compression theorem gives

\[
R_{\mathcal T_A}(F)\le B_A(F).
\]

Using (3.7), (6.1), and (3.8),

\[
R_{\mathcal T_A}(F)\le C_AI_A(F)+B_{\rm sel}.
\tag{6.6}
\]

Now put `r(a)=u_0(a)u_1(a)`. Spectral orthogonality implies

\[
\mathbb E r=\langle u_0,u_1\rangle
=\sum_U\widehat u_0(U)\widehat u_1(U)=0,
\]

so `r` is balanced. For a fixed controller assignment,

\[
F_a(y)=u_0(a)[c(y)+r(a)d(y)],
\]

which is a global sign times `g_+` for `r=+1` and a global sign times `g_-` for `r=-1`. Thus exactly half the leaves are of each type. Global sign preserves squared Fourier law, influence, and hereditary allocation. Grafting the leaf certificates costs at most

\[
\frac{K_Y}{2}\bigl(I(g_+)+I(g_-)\bigr)=K_YI_Y(F)
\]

by (3.9). Add this to (6.6) to get (6.3); (6.4) follows from Section 4, and if `M=0`, (6.5) follows from `I=I_A+I_Y`. QED.

By the newest P03 theorem `H(F)<=2R_T(F)` for every full tree, the isospectral splice also gives the restricted direct estimate

\[
H(F)\le2\max\{C_A,K_Y\}I(F).
\]

The factor two is inherited and is not claimed optimal for this restricted class.

---

## 7. Balanced-controller refinement and depth-independent closure

Take `u_0=1` and `u_1=h` with `h` balanced. Their Fourier supports are disjoint because `1` is supported only at the empty frequency and `\widehat h(\varnothing)=0`. Then (3.7) becomes the exact identity

\[
\boxed{B_A(f)=\alpha H(h)+B_{\rm sel}(g_+,g_-),}
\tag{7.1}
\]

with

\[
B_{\rm sel}\le h_2(M)\le h_2(\alpha).
\tag{7.2}
\]

This strictly refines the newest NM13-02 balanced-controller bound whenever the child spectra are more distinguishable than the worst case. If the children are isospectral, the whole `h_2(alpha)` surcharge disappears.

**Corollary.** If balanced `h` has `H(h)<=C_hI(h)`, if `g_+,g_-` are isospectral, and if both siblings have hereditary constant at most `K`, then the controlled function has hereditary constant at most

\[
\boxed{\max\{C_h,K\}.}
\]

No `+1`, `+2`, or controller-depth penalty appears. The operation may therefore be iterated to arbitrary depth: nested balanced controllers joining isospectral certified siblings preserve the maximum of the controller direct constants and terminal hereditary constants. Signed input translations are a large source of isospectral siblings. This is a restricted closure, not full FEI.

The two-controller theorem is genuinely broader: both `u_0,u_1` may have positive Fourier entropy provided their Fourier supports are disjoint.

---

## 8. What obstruction is removed, and what remains

The coarse controller theorem sees only physical disagreement `alpha` and therefore pays `h_2(alpha)` even when the residual spectral label already determines which branch component was used. The exact theorem identifies the correct surcharge as

\[
B_{\rm sel}=H(Z\mid S_Y),
\]

not `H(Z)=h_2(alpha)`. Its Bayes-error mass is exactly

\[
M=\frac12\left(1-\sum_T\sqrt{P_+(T)P_-(T)}\right),
\]

and the KL term measures how atypically that ambiguous mass is distributed.

This removes the named **controller-depth surcharge obstruction on isospectral sibling splices** and supplies an approximate Hellinger version. It does not solve the generic allocation problem: a generic sibling pair is not isospectral and a generic controller pair does not have disjoint Fourier supports. The full universal task is still to make the accumulated virtual-selector surcharges summable by influence on the signed-translation-rigid connected core, or to find a family decisively obstructing that plan.

---

## 9. Executed sanity checker

Executed checker:
`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T15-29-48+0300__check_spectral_orthogonal_splicing.py`

creation commit `9fa1f043064c7c281b1ab23caf46a03bcab764e2`, blob `ce00b955ab413db831c409f6d4919742b5ace314`.

Preserved actual output:
`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T15-29-48+0300__spectral_orthogonal_splicing_check.json`

creation commit `c2ff07af66487906b962304a404225777713a5ff`, blob `c106300db1616233bd332b56a62715c84f7b72ee`.

The checker exhaustively enumerates controller pairs with disjoint Fourier support through controller dimension three modulo independent global signs, and all ordered residual child pairs through residual dimension two. It adds 500 deterministic-seed higher-dimensional cases by tensoring an explicit non-character disjoint-support controller pair with arbitrary Boolean factors; half of those residual pairs are exact signed translations and hence isospectral.

Recorded totals: `742` disjoint-support controller pairs, `201,824` exhaustive splice cases, `500` higher-dimensional cases, `202,324` total cases, and `65,549` isospectral cases. The maximum block-factorization discrepancy was `1.7763568394002505e-15`. Controller- and residual-influence identity errors were exactly `0.0` at checker precision. Maximum numerical violations of `B_sel<=h2(M)` and `M<=j` were `0.0`, and maximum isospectral `B_sel` was exactly `0.0`. Status: `PASS`.

This is a self-check, not an independent audit. Universal quantifiers are supported by the written proof, not enumeration.

---

## 10. Failed-route history retained

Nothing here revives the false pointwise erasure shortcut, fixed-coefficient affine drift, old resolvent/interpolation route, Han/absolute-overlap all-coordinate selector, derivative-degree scalar schedule, blind curvature/query payment, fixed-`s<2` Renyi payment, frozen-parent endpoint payment, coefficientwise endpoint payment, or marginal-entropy replacement of the true conditional fibre cost.

The fresh-control theorem remains restricted to appended variables and its density hypothesis. The valid one-coordinate Hellinger/KL theorem, zero-cost isospectral splice, arbitrary-block entropy sandwich, and NM13 block-compression theorem are preserved at their actual scopes.

---

## 11. ledger_delta

```text
ledger_delta:
  problem: P03 / Friedgut-Kalai Fourier entropy-influence
  source_status_before: OPEN
  source_status_after: OPEN
  universal_constant_before: UNKNOWN
  universal_constant_after: UNKNOWN
  native_atlas_before: 6
  native_atlas_after: 6
  new_mechanism:
    - exact spectral-orthogonal controller block factorization
      B_A=(1-beta)H(u0)+beta H(u1)+B_sel
    - exact influence identities
      I_A=(1-beta)I(u0)+beta I(u1)
      I_Y=(I(g+)+I(g-))/2
    - virtual-selector Hellinger defect M=(1-affinity(P+,P-))/2
    - B_sel<=h2(M) with KL rebate
    - zero-surcharge hereditary max-splicing for isospectral siblings
    - balanced-controller refinement replacing h2(alpha) by exact B_sel
  named_obstruction_removed:
    - controller-depth surcharge disappears on isospectral sibling splices
  failed_recovery_retained:
    - coarse two-budget balanced-controller recursion necessarily has residual coefficient >=1 asymptotically
    - co-singleton proper-block selector remains full-scope/circular and unproved
  checker_status: PASS
  checker_cases: 202324
  independent_review: PENDING
  publication_priority: UNVERIFIED
  full_FEI_closed: false
```

## 12. Next handoff

The nonredundant next P03 target is to turn `B_sel` into a **summable tree currency**: on the signed-translation-rigid connected core, find a restriction-stable block with nearly spectral-orthogonal controller phases and pay

\[
B_{\rm sel}\lesssim M\left[\log_2(1/M)-D_2(\nu\Vert q)+O(1)\right]
\]

by influence that is not reused at descendants. Exact isospectral nodes should be spliced for free first. A family forcing cumulative virtual-selector surcharge to diverge relative to queried influence would be equally decisive.

Do not return to minor-child, curvature, derivative-degree, resolvent, fixed-Renyi, or fixed-drift scalar surrogates.

**End of complete run report.**
