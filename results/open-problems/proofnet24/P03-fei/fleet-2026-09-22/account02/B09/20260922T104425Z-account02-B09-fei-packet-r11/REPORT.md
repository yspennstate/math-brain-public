# account02/B09 — nonoverlapping signed packet cover with laminar KL ledger

**Run:** `20260922T104425Z-account02-B09-fei-packet-r11`  
**Assignment:** `FEI-20260922-account02-B09`, Path B, **Nonoverlapping packet cover**  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED / NOT DISPROVED**.

## 0. Current source state and corrections


The mandatory corrections used literally here include:

- `FEI-DELTA-20260922-05-KL-HIERARCHY-TERM`: retain the exact nonnegative hierarchy KL in disjoint composition;
- `FEI-DELTA-20260922-06-UNWEIGHTED-L2-NOGO`: a fixed multiple of full unweighted convolution energy loses the sparse rare-event logarithm;
- `FEI-DELTA-20260922-13-LOWLEVEL-KL-PROJECTION-NOGO`: fixed/low labelled cutoffs fail on recursive ternary majority.

No fixed-potential, raw-U4, or unweighted-L2 route is revived.

The exact assignment sources consumed are:

1. **IPROJ**, account02/B15, commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`: for the nonempty spectral law `P` with coordinate marginals `r`, the maximum-entropy conditional-product law `Q_r` satisfies
   \[
   K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P),
   \qquad R_\Gamma=B_{\rm inf}^\Gamma+K_{\rm occ}.
   \]
2. **HIERARCHY**, account04/B15, commit `2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`, `.../account04/B15/20260922T091017Z-iprojection-composition-transfer/REPORT.md`: for disjoint composition,
   \[
   K_{\rm occ}(F)=K_{\rm occ}(G)+\sum_i\alpha_iK_{\rm occ}(f_i)+C_{\rm hier},\qquad C_{\rm hier}\ge0,
   \]
   with the hierarchy credit explicit and source-exact.
3. **L2 barrier**, account04/B15, commit `7ec649dfb3d1ab2f92855f2069590fca2ac956dd`, `.../account04/B15/20260922T093820Z-full-convolution-energy-obstruction/REPORT.md`: on the sparse suspension family the full signed convolution energy is `4mp+O(m^2p^2)` while indispensable `K_occ` is order `m^2p`.
4. **Low-level barrier**, account03/B18, commit `bff0d7b6c21485f386841c42582eb04f32705046`, `.../account03/B18/20260922T100641Z-lowlevel-projection-barrier/REPORT.md`: recursive ternary majority defeats every fixed cutoff and every `d_m <= (1/2-epsilon)m` low-level labelled projection.

The named partner account03/B09 had no completed compatible FEI artifact discoverable in `math-open-problems` or the all-team handoff directory at both startup and pre-publication searches. I therefore did not invent a partner premise. The completed OTHER-account result consumed directly is account01/B17, commit `ecc0bd6b5505ff115efe7a1c9e5beb75b9df0087`, `.../account01/B17/20260922T084426Z-signed-convolution-packet/REPORT.md`, which accumulates signed Boolean convolution equations and converts their defect to a KL/Hellinger payment. I also consumed the recipient's newer account04/B15 logarithmic-tariff theorem at commit `94f7fa8b85819fd242f7c019ef080162d11deb8c`; it proves that the sparse suspension requires the critical self-information coefficient `1/4` rather than a fixed quadratic tariff.

## 1. A general nonreuse theorem for signed packets

Let `Omega` be finite and let `P,Q` be probability laws with `Q(s)>0` for every `s` in
\[
A:=\operatorname{supp}P.
\]
Put
\[
q_A=Q(A),\qquad \bar Q=Q(\cdot\mid A).
\]
Then exactly
\[
D_{\rm KL,2}(P\Vert Q)=\log_2\frac1{q_A}+D_{\rm KL,2}(P\Vert\bar Q).
\tag{1.1}
\]

In the Hilbert space `l2(A x A)` define the unit amplitude tensors
\[
x_{uv}=\sqrt{P(u)P(v)},\qquad y_{uv}=\sqrt{\bar Q(u)\bar Q(v)}.
\tag{1.2}
\]

### Theorem 1.1 — `FEI-SIGNED-PACKET-NONREUSE-v1`

Let `E_j subset A x A` be pairwise disjoint nonempty packets. On each packet choose signs `sigma_j(u,v) in {+1,-1}` and suppose the **source-valid cancellation**
\[
\sum_{(u,v)\in E_j}\sigma_j(u,v)\sqrt{P(u)P(v)}=0
\tag{1.3}
\]
holds. Write
\[
N_j=|E_j|,
\qquad
R_j=\sum_{(u,v)\in E_j}\sigma_j(u,v)\sqrt{\bar Q(u)\bar Q(v)},
\tag{1.4}
\]
and
\[
\Theta=\sum_j\frac{R_j^2}{N_j}.
\tag{1.5}
\]
Then `0 <= Theta < 1` and
\[
\boxed{
D_{\rm KL,2}(P\Vert Q)
\ge
\log_2\frac1{q_A}
-\frac12\log_2(1-\Theta).
}
\tag{1.6}
\]

#### Proof

Normalize each packet normal by
\[
c_j=N_j^{-1/2}\,\sigma_j\mathbf 1_{E_j}.
\]
Disjointness makes the `c_j` orthonormal, and (1.3) says `x` is orthogonal to each `c_j`. Hence by Bessel,
\[
\|\operatorname{Proj}_{\mathrm{span}\{c_j\}}y\|_2^2
=\sum_j|\langle c_j,y\rangle|^2
=\Theta.
\]
The Hellinger affinity satisfies
\[
\langle x,y\rangle
=\left(\sum_{u\in A}\sqrt{P(u)\bar Q(u)}\right)^2.
\]
Since `x` is a unit vector in the orthogonal complement of the packet span,
\[
\langle x,y\rangle\le\sqrt{1-\Theta}.
\]
Thus the ordinary affinity is at most `(1-Theta)^(1/4)`. Rényi monotonicity gives
\[
D_{\rm KL,2}(P\Vert\bar Q)
\ge D_{1/2,2}(P\Vert\bar Q)
=-2\log_2\sum_u\sqrt{P(u)\bar Q(u)}
\ge-\frac12\log_2(1-\Theta).
\]
Combine with (1.1). `QED`.

### Fractional/overlapping extension

The same proof does not require literal disjointness. If normalized packet normals `c_j` satisfy the frame bound
\[
\sum_j|\langle c_j,z\rangle|^2\le\Lambda\|\operatorname{Proj}_Wz\|_2^2,
\qquad W=\operatorname{span}\{c_j\},
\tag{1.7}
\]
then, provided every `c_j` annihilates `x`, (1.6) holds with
\[
\Theta_\Lambda=\frac1\Lambda\sum_j|\langle c_j,y\rangle|^2.
\tag{1.8}
\]
This is the precise fractional-cover nonreuse rule: overlap is charged by its actual frame load `Lambda`, not by pretending the same KL can be spent twice.

## 2. Exact Boolean convolution packet cover

Let `f:{-1,+1}^k->{-1,+1}` be balanced and Boolean, with Walsh coefficients `a_S`, spectral law
\[
P(S)=a_S^2,
\]
and active support `A={S:a_S !=0}`. Put `s_S=sgn(a_S)`.

Booleanity gives, for every nonempty XOR shift `T`,
\[
\sum_S a_Sa_{S\triangle T}=0.
\tag{2.1}
\]
For each such `T` define the ordered active packet
\[
E_T=\{(S,S\triangle T):S,S\triangle T\in A\}.
\tag{2.2}
\]
Every ordered pair `(S,R)` with `S != R` determines the unique shift `T=S triangle R`, so the packets `E_T` are pairwise disjoint. Equation (2.1) is exactly (1.3) with
\[
\sigma_T(S,S\triangle T)=s_Ss_{S\triangle T}.
\]

Apply Theorem 1.1 with the exact influence I-projection `Q_r`. If
\[
Q_A=Q_r(\cdot\mid A),
\]
define
\[
R_T^A=\sum_{S,S\triangle T\in A}
 s_Ss_{S\triangle T}\sqrt{Q_A(S)Q_A(S\triangle T)},
\qquad N_T=|E_T|.
\]
Then the **entire signed Boolean convolution family is simultaneously chargeable without information reuse**:
\[
\boxed{
K_{\rm occ}(f)
\ge
-\log_2 Q_r(A)
-rac12\log_2\left(
1-\sum_{T\ne\varnothing}\frac{(R_T^A)^2}{N_T}
\right).
}
\tag{2.3}
\]
The source signs are retained until after the exact cancellation; support mismatch is paid first rather than discarded; all reference rare-event weights remain inside `Q_A`.

This is stronger structurally than summing independent single-packet lower bounds: it proves one common KL budget for all packets.

## 3. Decisive sparse-suspension no-go for the pure Hilbert packet span

The theorem is valid, but the most obvious universal closure attempt is false.

Take the genuine Boolean sparse suspension from account04/B15:
\[
p=2^{1-m},\quad g_m(x)=1-2\mathbf1_{\{x=0\}},\quad F_m(y,x)=y g_m(x).
\]
On the old coordinates every Fourier coefficient of `g_m` is nonzero, so `A=2^{[m]}` and the I-projection has the same support. Thus `Q_r(A)=1`. For every nonzero shift `U`,
\[
N_U=2^m,\qquad R_U=C_m(U),
\]
where `C_m(U)` is precisely the signed I-projection convolution defect of the L2-barrier source. Consequently
\[
\boxed{
\Theta_m=2^{-m}\mathcal B_m,
}
\tag{3.1}
\]
where account04/B15 proves
\[
\mathcal B_m=4mp+O(m^2p^2).
\]
Hence
\[
\Theta_m=8m\,4^{-m}+o(m4^{-m})
\tag{3.2}
\]
and the packet theorem alone yields only
\[
-\frac12\log_2(1-\Theta_m)
=\frac{4m}{\ln2}\,4^{-m}(1+o(1)).
\tag{3.3}
\]
But the same source gives
\[
K_{\rm occ}(F_m)
=mp\left(m-5+\frac1{\ln2}+o(1)\right),
\tag{3.4}
\]
so the ratio of (3.3) to the true KL is `O(2^{-m}/m) -> 0`.

This is a genuine mechanism refutation:

> **`FEI-FULL-CONVOLUTION-HILBERT-COVER-v1` is REFUTED.**  Recombining, orthogonalizing, or fractionally covering only the standard full convolution-equation normals cannot recover the rare-event logarithm. Their span already has exact squared reference projection `Theta_m`; linear packet geometry has no hidden reserve beyond it.

This does **not** refute nonlinear self-information tariffs. Indeed the newly consumed account04/B15 result at commit `94f7fa8...` proves on this same family that
\[
\mathcal L_m=\sum_{U\ne0}C_m(U)^2\log_2\frac1{C_m(U)^2}
\]
recovers the correct rare-event scale and has unique leading transfer coefficient `1/4` up to additive `O(I)`.

## 4. Laminar hierarchy theorem: exact nonreuse across scales

The sparse no-go says packet equations must not be asked to replace hierarchy KL. The exact composition source gives the right multiscale ledger.

Consider a rooted disjoint-composition tree. At an internal node `v`, let `G_v` be the outer gate, let `alpha_{v,i}` be the inclusion probability of child `i` in the outer nonempty spectral law, and let `C_v>=0` be the exact hierarchy credit from account04/B15. Set
\[
\beta_{\rm root}=1,
\qquad
\beta_{\rm child}=\beta_v\alpha_{v,i}.
\tag{4.1}
\]

### Theorem 4.1 — `FEI-LAMINAR-KL-NONREUSE-v1`

For any finite disjoint-composition tree,
\[
\boxed{
K_{\rm occ}(F_{\rm root})
=
\sum_{v\ {m internal}}\beta_vK_{\rm occ}(G_v)
+
\sum_{v\ {m internal}}\beta_v C_v
+
\sum_{\ell\ {m leaves}}\beta_\ell K_{\rm occ}(F_\ell).
}
\tag{4.2}
\]
In particular, if `L_v <= K_occ(G_v)` is any source-valid local packet lower bound (for example (2.3) when applicable), then
\[
\boxed{
K_{\rm occ}(F_{\rm root})
\ge
\sum_v\beta_v L_v
+
\sum_v\beta_v C_v
+
\sum_\ell\beta_\ell L_\ell.
}
\tag{4.3}
\]

#### Proof

Induct on tree depth, substituting the exact one-step hierarchy identity
\[
K_v=K(G_v)+\sum_i\alpha_{v,i}K_i+C_v
\]
at each node. Every descendant term acquires exactly the path product `beta`; every local KL and every hierarchy credit occurs exactly once. `QED`.

The weights `beta_v` are actual source activation weights. They are not replaced by uniform level weights, and the nonnegative hierarchy credits are never discarded.

## 5. Acceptance tests

### 5.1 Sparse suspension — survives by hierarchy, not by quadratic packet energy

The one-point-defect function `g_m` is a read-once AND/OR of literals up to output convention, and `F_m=y g_m` adds one binary parity-type outer gate. Thus it has a binary read-once disjoint-composition tree. Account04/B15 proves every nonconstant binary gate has local `K_occ=0`. Equation (4.2) therefore becomes
\[
\boxed{
K_{\rm occ}(F_m)=\sum_v\beta_v C_v.
}
\tag{5.1}
\]
So the laminar ledger retains **all** of the `Theta(mI)` rare-event KL through hierarchy credits even though Section 3 proves the pure packet-Hilbert term is exponentially too small. This is the required no-reuse handling of the sparse calibration family.

### 5.2 Recursive ternary majority — explicit survival of the fixed-depth barrier

Let `M_m` be depth-`m` recursive ternary majority. At every local `Maj_3` node the three outer inclusion probabilities are `1/2`, so at depth `ell` every node has `beta=2^{-ell}` and the total node weight is `(3/2)^ell`. Let
\[
\kappa_3=K_{\rm occ}(Maj_3)
=\frac{3h_2((3-\sqrt5)/2)-h_2(3-\sqrt5)}{3-\sqrt5}-2
\approx0.735604784076543.
\tag{5.2}
\]
The sum of all local gate KLs is therefore
\[
2\kappa_3\left((3/2)^m-1\right)=O(\mu_m),
\qquad \mu_m=(3/2)^m.
\tag{5.3}
\]
The low-level-barrier source proves
\[
H_{\max}(r^{(m)})\ge \mu_m m-2,
\qquad H(M_m)=4(\mu_m-1),
\]
so
\[
K_{\rm occ}(M_m)\ge \mu_m(m-4)+2.
\tag{5.4}
\]
Combining (4.2), (5.3), and (5.4), the hierarchy-credit sum itself obeys
\[
\boxed{
\sum_v\beta_v C_v
\ge
\mu_m(m-4-2\kappa_3)+2+2\kappa_3,
}
\tag{5.5}
\]
which is `Theta(mu_m m)`. Thus the missing high-scale dependence is explicitly retained across **all recursion levels**. There is no fixed-depth truncation and no merged tail; the mechanism therefore survives the recursive-majority barrier rather than evading it.

### 5.3 Balanced antipodal two-flip near dictator

For a concrete second stress family, let `f_n=x_1` except flip the two antipodal truth-table points `(+1,...,+1)` and `(-1,...,-1)`. Put `q=2^{2-n}`. Its Walsh coefficients are exactly
\[
\widehat f_n(\{1\})=1-q,
\quad
\widehat f_n(S)=-q\quad(S\ne\{1\},\ |S|\text{ odd}),
\quad
\widehat f_n(S)=0\quad(|S|\text{ even}),
\tag{5.6}
\]
so
\[
r_1=1-q,\qquad r_i=q\ (i>1).
\tag{5.7}
\]
The adjacent deterministic checker solves the exact I-projection equation, spends the support refund first, and then evaluates (2.3). The lower-bound fraction `LB/K_occ` decreases over `n=3,...,10` from approximately
\[
0.89555,\ 0.77149,\ 0.57113,\ 0.43349,\ 0.34461,\ 0.28431,\ 0.24107,\ 0.20867.
\]
This is a finite diagnostic, not an asymptotic theorem. It is nevertheless useful negative information: even after support refund, the plain quadratic packet span is not approaching a uniform full payment on this natural near-dictator family. A nonlinear/self-information packet tariff is the next mechanism to test.

## 6. Exact bridge to the recipient's logarithmic tariff

Account04/B15's newest theorem proves on the sparse suspension that a source statistic
\[
\mathcal L=\sum C(U)^2\log_2\frac1{C(U)^2}
\]
has the correct rare-event scale and that coefficient `1/4` is forced at leading order. Theorem 4.1 supplies the missing **nonreuse architecture** for such a statistic:

> if a source-valid composition-prime node inequality of the support-conditioned form
> \[
> D(P_v\Vert Q_v(\cdot\mid A_v))
> \ge \frac14\mathcal L_v-\kappa I_v
> \tag{6.1}
> \]
> is proved, then it may be inserted as `L_v` in the exact laminar identity and summed with the support refunds and all hierarchy credits, each at the actual activation weight `beta_v`, without charging the same KL twice.

The hierarchy therefore handles decomposable rare-event logarithms exactly; the genuinely new universal burden can be localized to composition-prime nodes rather than repeatedly charging their descendants.

## 7. First essential missing implication

The first unpaid implication is now

**`FEI-PRIME-LOG-PACKET-NONREUSE-v1`:** on a composition-prime Boolean source, prove a support-conditioned nonlinear signed-convolution packet payment of type (6.1), with coefficient `1/4` at the sparse calibration scale or an appropriately source-normalized replacement, and make the packet family obey an exact chain-rule/frame nonreuse rule. It must preserve source signs, rare-event probabilities, and the full I-projection reference; no fixed-depth truncation is admissible. Alternatively produce a genuine Boolean prime+bias falsifier.

The present run proves the exact linear packet nonreuse theorem and exact laminar multiscale aggregation, and it refutes the idea that mere linear recombination/fractional covering of the standard full convolution normals can recover the missing logarithm.

## 8. Verification and telemetry

`verify_packet_cover.py` is standard-library only and its captured output is `verify_packet_cover.out`. It numerically checks the theorem's lower bound on the sparse suspension and on the exact two-flip family through `n=10`, and prints the recursive-majority scale diagnostic. These computations support the stress tests only; Theorems 1.1 and 4.1 and the sparse asymptotic no-go are analytic.

Model self-report: `GPT-5.6 Sol`. Requested effort: maximum actually supported. Configured effort, provider reasoning tokens, and provider thinking time were not exposed and are recorded as `UNKNOWN/null`; elapsed execution is not pure thinking. No benchmark, retired-problem, paid API/model, public posting, email/Drive, cross-account auth, permission change, or scheduler mutation was used.
