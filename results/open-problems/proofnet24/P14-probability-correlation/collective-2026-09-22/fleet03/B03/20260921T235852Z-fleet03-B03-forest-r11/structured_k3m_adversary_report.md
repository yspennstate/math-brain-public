Model actually run: **GPT-5.6 Sol. Configured reasoning effort: UNVERIFIED / not exposed.**

# FOREST / fleet03-B03 — an exact `K_{3,m}` adversary to q-free switching and a fourth three-terminal response coordinate

**Outcome:** `ESSENTIAL_STEP_APPLIED` on the current collective candidate; parent Grimmett–Winkler uniform-forest pairwise negative-correlation conjecture remains **OPEN**.

**Candidate version:** `FOREST-OVERLAP-RESPONSE-v2`.

**Scope:** uniform measure on **all unrooted forests** of a finite simple graph at unit edge weights. No rooted, spanning-tree, fixed-size, weighted-parent or all-matroid substitution is used.

## 1. Consumed peer and inherited exact inputs

This run consumes the exact cross-account handoff


For distinct edges `e,f`, that handoff sets `K=G-{e,f}`, lets `H` range over all forests of `K`, records whether `e` and `f` are individually addable by indicators `(X,Y)`, defines `n_ij=#{H:(X,Y)=(i,j)}`, `N=sum n_ij`, and lets `q` count the `X=Y=1` forests for which adding both edges creates a cycle. It proves the exact identity

\[
\Delta_G(e,f)=Z_eZ_f-ZZ_{ef}
=n_{10}n_{01}-n_{00}n_{11}+Nq.
\tag{1}
\]

Thus the target for the pair is exactly

\[
n_{00}n_{11}\le n_{10}n_{01}+Nq.
\tag{2}
\]

I also recover the older P14/HARD10 exact three-terminal observation: if a three-terminal side has forest-partition counts `(d,a,b,c,t)` for states

\[
D=x|y|z,\quad A=xy|z,\quad B=xz|y,\quad C=yz|x,\quad T=xyz,
\]

then a positive weighted triangle can match the first four coordinates after scaling only on the hypersurface

\[
dt=ab+ac+bc.
\tag{3}
\]

The new work below shows that the defect from (3) is not an accidental finite obstruction: it is an **additive fourth normalized response coordinate**, and a particularly simple 3-connected asymptotic family accumulates it linearly.

## 2. Structured adversary family

Let

\[
G_m=K_{3,m}
\]

with terminals `x,y,z` on the size-three side and independent right vertices `r_1,...,r_m`. Equivalently, `G_m` is the parallel union, across the same three terminals, of `m` copies of the three-spoke star.

Adding one right vertex has the exact terminal-partition transfer

\[
S=
\begin{pmatrix}
4&1&1&1&1\\
0&4&0&0&2\\
0&0&4&0&2\\
0&0&0&4&2\\
0&0&0&0&4
\end{pmatrix}.
\tag{4}
\]

Starting from the all-separated state and taking `S^m` gives

\[
\boxed{d_m=4^m,}
\tag{5}
\]

\[
\boxed{a_m=b_m=c_m=m4^{m-1},}
\tag{6}
\]

and

\[
\boxed{t_m=m(3m+1)4^{m-2}.}
\tag{7}
\]

These are exact forest counts, not asymptotics.

## 3. New structural lemma: the missing fourth three-terminal coordinate is additive

Consider edge-disjoint three-terminal graphs `B_1,B_2` sharing exactly the terminals `x,y,z`, and let their signatures be

\[
s_i=(d_i,a_i,b_i,c_i,t_i).
\]

Their parallel union `B=B_1\parallel B_2` has signature

\[
\begin{aligned}
d&=d_1d_2,\\
a&=a_1d_2+d_1a_2,\\
b&=b_1d_2+d_1b_2,\\
c&=c_1d_2+d_1c_2,\\
t&=t_1d_2+d_1t_2
+a_1b_2+b_1a_2+a_1c_2+c_1a_2+b_1c_2+c_1b_2.
\end{aligned}
\tag{8}
\]

**Proof.** A forest chosen on each side gives an acyclic union unless the two sides supply two distinct terminal-to-terminal routes joining the same pair or one side already has all three terminals connected while the other supplies any nontrivial terminal connection. With only three terminals the compatible pairs of nontrivial partitions are exactly two *different* pair states, and those six ordered combinations contribute the six cross terms in `t`. All other displayed formulas are immediate from the terminal partition. Detached internal components never meet the other side. QED.

Since `d_i>0`, normalize

\[
x=\frac ad,\qquad y=\frac bd,\qquad z=\frac cd,\qquad w=\frac td,
\]

and define

\[
\boxed{\eta(B)=w-(xy+xz+yz)
=\frac{dt-ab-ac-bc}{d^2}.}
\tag{9}
\]

Substituting (8) gives the exact cancellation

\[
\boxed{\eta(B_1\parallel B_2)=\eta(B_1)+\eta(B_2).}
\tag{10}
\]

Thus (9), not merely the three pairwise effective weights, is a natural fourth normalized boundary response coordinate.

For a weighted triangle on `x,y,z`, after scaling `d=1`, the pair coordinates are its three edge weights and

\[
t=ab+ac+bc,
\]

so

\[
\eta(\text{weighted triangle})=0.
\tag{11}
\]

For one unweighted three-spoke star the signature is `(4,1,1,1,1)`, hence

\[
\eta(\text{star})=\frac1{16}.
\tag{12}
\]

By (10), or directly from (5)--(7),

\[
\boxed{\eta(K_{3,m})=\frac m{16}}
\tag{13}
\]

and the unnormalized hypersurface defect is

\[
\boxed{d_mt_m-a_mb_m-a_mc_m-b_mc_m
=m4^{2m-2}>0.}
\tag{14}
\]

Consequently the weighted-triangle compression fails for every `m>=1`; its normalized algebraic defect grows linearly with the number of parallel three-terminal stars. This is a structural, asymptotic obstruction, not a finite exceptional graph.

## 4. Exact forest-pair counts against the current reconnection candidate

Now choose two spokes in the **same** right star,

\[
e=xr_1,\qquad f=yr_1,
\]

and assume `m>=2`. Put

\[
C=4^{m-2}.
\]

Exact transfer gives

\[
\boxed{Z=C(3m^2+13m+16),}
\tag{15}
\]

\[
\boxed{Z_e=Z_f=\frac C4(3m^2+23m+38),}
\tag{16}
\]

\[
\boxed{Z_{ef}=2C(m+3).}
\tag{17}
\]

For the fleet01/B03 decomposition of `K=G_m-{e,f}`, the exact cell counts are

\[
\boxed{N=\frac C2(3m^2+7m+6),}
\tag{18}
\]

\[
\boxed{n_{00}=\frac C4(m-1)(3m-2),}
\tag{19}
\]

\[
\boxed{n_{10}=n_{01}=C(m-1),}
\tag{20}
\]

\[
\boxed{n_{11}=\frac C4(3m^2+11m+18),}
\tag{21}
\]

and the exact overlap count is

\[
\boxed{q=\frac{3C}{4}(m-1)(m+2).}
\tag{22}
\]

Here `Q` has the peer handoff's adjacent-edge interpretation: `x` and `y` are connected in `H` while `r_1` is in a different component. Equation (22) was independently obtained by a persistent-frontier partition dynamic program, not inferred from the Rayleigh identity.

Substitution yields

\[
\boxed{
\Delta_{G_m}(e,f)
=\frac{C^2(m-1)}{16}
\left(9m^3+51m^2+104m+92\right)>0.
}
\tag{23}
\]

So this family is **not** a counterexample to the parent conjecture. It is an exact adversary to a tempting proof mechanism.

### 4.1 The q-free switching route is cardinality-impossible

If one tries to prove (2) only by switching/injecting `00 x 11` objects into `10 x 01` objects and omits the overlap reservoir, then for this family

\[
\boxed{
n_{00}n_{11}-n_{10}n_{01}
=\frac{C^2(m-1)}{16}
(9m^3+27m^2+16m-20)>0
}
\tag{24}
\]

for every `m>=2`.

Hence **no injection of unit-multiplicity objects from the entire `00 x 11` product into the entire `10 x 01` product can exist** on this family. The cardinality ratio diverges:

\[
\frac{n_{00}n_{11}}{n_{10}n_{01}}\sim \frac{9}{16}m^2.
\tag{25}
\]

The overlap term is not a lower-order repair. Indeed

\[
Nq
=\frac{3C^2}{8}(m-1)(m+2)(3m^2+7m+6)
=\Theta(C^2m^4),
\tag{26}
\]

and the exact peer identity becomes

\[
n_{10}n_{01}+Nq-n_{00}n_{11}=\Delta_{G_m}(e,f).
\tag{27}
\]

Thus any successful global switching proof must route a leading-order amount of mass through `H x Q`, or use an equivalent mechanism that explicitly remembers the overlap/reconnection state.

## 5. What structural information is missing

The two exact failures line up:

1. fleet01/B03 shows the pairwise count needs the overlap reservoir `Q`;
2. the three-terminal separator calculation shows pairwise virtual-edge weights lose the additive coordinate `eta`.

The common missing information is **three-way reconnection excess**. A separator proof that retains only three pairwise terminal weights has no variable capable of recording (13). A switching proof that discards `Q` has no target reservoir capable of absorbing the asymptotically dominant excess in (24).

This suggests the next candidate should not be "weighted triangle + a stronger inequality on the same three weights." It should carry the four normalized boundary coordinates

\[
(x,y,z,\eta),
\tag{28}
\]

or an equivalent exact five-state signature `(d,a,b,c,t)`, and the combinatorial switching should preserve or monotonically control the corresponding reconnection excess.

This is a structural constraint on the proof architecture, **not** a proof that `eta>=0` for every physical three-terminal network and not a proof of the parent conjecture.

## 6. Conditional end-to-end line and first remaining obligation

Combining the current peer reduction with the present adversary gives the following honest conditional line.

For every edge pair, fleet01/B03 reduces p-NC to (2). If one constructs a multiplicity-controlled switching or equivalent counting decomposition

\[
\mathcal A_{00}\times\mathcal A_{11}
\longrightarrow
(\mathcal A_{10}\times\mathcal A_{01})\;\sqcup\;(\mathcal H\times\mathcal Q)
\tag{29}
\]

whose fibers prove exactly (2), while its local separator bookkeeping retains the fourth response coordinate `eta` rather than compressing to a weighted triangle, then (1) proves `Delta_G(e,f)>=0` for the pair. Doing this uniformly for every finite simple graph and pair proves the source target.

The **first unpaid universal implication** is therefore:

> Prove (29), or an equivalent terminal-partition inequality, with exact multiplicity control on arbitrary overlapping cycles, in a state space rich enough to retain `eta`. The map must handle disconnected forests and the adjacent/disjoint endpoint cases, and cannot delete `Q` or replace the boundary by only three virtual edge weights.

The `K_{3,m}` family is a mandatory regression for any proposed solution: it must reproduce (18)--(22), and it must explain where the `Theta(C^2m^4)` overlap mass in (26) is sent.

## 7. Exact computation and reproducibility

Archived checker:

`k3m_structured_adversary_checker.py`

Archived exact output:

`k3m_structured_adversary_output.txt`

The checker uses Python stdlib integer/rational arithmetic only. It independently reconstructs the five-state transfer, the marked same-star pair counts, the persistent-frontier count of `q`, the peer identity (1), the strict cardinality failure (24) for `m=2,...,12`, the terminal-signature formulas, and the additivity of `eta`. No floating-point sign decision is used.

The finite range is a regression of the closed forms; the formulas themselves are proved algebraically above from the fixed transfer and composition laws, so the theorem is not a finite-census claim.

## 8. Status and next recipients

- Parent FOREST conjecture: **OPEN**.
- New result: exact structured asymptotic obstruction to q-free switching and weighted-triangle-only three-separator compression.
- Surviving candidate: four-coordinate / five-state overlap-aware switching, version `FOREST-OVERLAP-RESPONSE-v2`.
- Assigned partner `fleet04/B01` had no finalized current-campaign handoff in the consumed coordination snapshot, so the owner-authorized fallback was used: fleet01/B03's exact current-campaign handoff was consumed rather than waiting.
- Next recipients: FOREST lead `fleet01/B01`, assigned partner `fleet04/B01`, and separator roles `fleet02/B01` / `fleet03/B02`.
- Brain status for this run: `WITHOUT_VERIFIED_BRAIN`; the later owner control explicitly stopped new brain-installation work and made native brain readiness non-prerequisite for mathematics.

External novelty/priority of the additive `eta` formulation is **UNVERIFIED**. Repository search located the older hypersurface equation (3) but did not locate the additive-coordinate formula (10) or the exact `K_{3,m}` regression above; a search miss is not a priority claim.
