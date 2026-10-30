# A007 root normalization

## exact target, quantifiers, hypotheses and units

All log denotes log_2; all entropies are in bits. For every finite nonconstant data indicator B=OR_l b_l with rho_l=E b_l>0, every r>=1, and every fixed positive incidence vector lambda with sum_l lambda_l<=1, consider F=2 A_r B-1, where A_r is a conjunction on r fresh fair coordinates. Write p=2^(-r), b=E B, g=2B-1, I_data=p I(g), I_core=2rp b, v=Var(F). Use the conditioned queue of the reductions manuscript on the actual gates h_l=2 A_r b_l-1. Their root parameters are pi_l=p rho_l (no truncation ambiguity). Ordered covers can be chosen arbitrarily for the main component theorem.

There exist actual partition-forest laws with root count K satisfying

    T_root := v(Lambda+log Z) + E sum_{roots l} log(1/pi_l)
       = v log s + v delta + r(E K-v) + E sum_{roots l} log(1/rho_l),
    s=sum_l lambda_l rho_l,
    0<=delta=log[(product_l(1+p lambda_l rho_l)-1)/(p s)]<=p s log e,
    0<=r(E K-v)<=I_data/2,
    v delta<= (log e) I_core.

Consequently T_root<=E sum_roots log(1/rho_l)+(log e) I(F). The favorable v log s remains explicit in the exact identity before this estimate. This settles the common-core rarity/normalization component uniformly in dimension, read count, r, and base gate probabilities; it does not pay base rarity, labels, ranks, congestion, or complete witness cost.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision 2026-10-11-execution-v2. The board snapshot read at the start and before validation was 2026-10-11 21:55 UTC. The specified claude/B02/STREAM_NOTES.md was absent. Reports README, CURRENT_STATUS, registries, packet status, stream next actions, and plan Endpoint J plus A007 acceptance tests were inspected. Earlier reports in runs/B05, B09 and B19 were located; their published status and obstruction scope were read in CURRENT_STATUS and the registry, not used as proof dependencies.

The primary coding source is source_material/reductions/paper/forests.tex: eq:forestpacking, eq:forestrootconstants, eq:forestconditioning, eq:forestcost, thm:posteriorforest, and the full queue definition. In particular child labels use lambda_l, not a uniform-neighbor distribution. Conditioning divides successful-run mass by Z even when failure/nontermination has positive probability.

A006's 20261011T210855Z-fleet05-A006-posterior-forest-optimization/REPORT.md was read, especially its sunflower law, all-partition enumeration, normalizer, and proposed shared-r-core extension. Its unreviewed cost estimates are not premises here. The supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, NATIVE_MAPPING and SEED_LEMMAS were consulted; Section 2 of SEED_LEMMAS proves the complete-reference prior interface. Relevant source inventory and LOG_ALLOCATION/OVERLAPPING_PRODUCT scope were inspected. Context threshold_paper_38pp.txt Section 5.6 gives the unconditioned joint-witness interface and Section 8.4 the balanced activation benchmark. The earlier 29-page threshold introduction and both percolation introductions were read for scope; the percolation root entropy is a spatial occupancy statistic, not this initial-gate normalizer. None of these percolation conclusions is a proof premise. SHA256 pins are in out/SOURCES.json.

## complete derivation or exact first unsupported line

### 1. The exact conditioned initial-root law

For x_l=lambda_l pi_l and a=sum x_l>0, set D=product_l(1+x_l)-1. Then Z=D/(D+1) and Lambda+log Z=log D. Every nonempty initial root set R has probability product_{l in R}x_l/D after conditioning. This is an actual normalized root-set law: expansion of the product sums its numerators to D. Successful-run probabilities subsequently multiply this root probability by all remaining draw probabilities; no termination assumption is introduced.

Expansion gives D>=a. Also D<=exp(a)-1<=a exp(a), the last inequality following from integral_0^a exp(t)dt<=a exp(a). Thus

    log D = log a + delta, 0<=delta<=a log e.

One conditioned root cancels one common rarity scale, rather than every rarity occurrence. If x_l=t c_l with fixed c_l>0 and root count k, then

    log D + sum_{l in R} log(1/x_l)
      = (k-1)log(1/t) + log(sum c_l)
          + sum_{l in R}log(1/c_l) + delta.

So a fixed k>=2 retains a divergent (k-1)log(1/t) cost as t decreases to zero. This is noncancellation for that root pattern, not a counterexample to a full variational code or FEI.

For singleton roots restricted to an eligible set E, averaging root-label-plus-rarity cost and subtracting root-label entropy has the exact optimum

    inf_eta [log D + E_eta log(1/x_l)-H(eta)]
       = log[D/sum_{l in E}x_l]
       = log[a/sum_{l in E}x_l]+delta,
    eta_l=x_l/sum_{l in E}x_l.

This follows by subtracting the displayed value and obtaining KL(eta||eta_*). It only optimizes the root portion, not root-dependent subsequent draws. Distinct initial roots give distinct actual runs; no count of abstract forest descriptions supplies this entropy.

### 2. A one-root construction whenever the spectrum meets the shared core

Write a spectral set as U union T, U in C and T in the data coordinates. When U is nonempty, choose a gate l0, assign all of U to it, and assign every data coordinate in T to a gate containing it. Only gates owning a coordinate are visited. Gate l0 has an edge to every other visited gate through any fixed u in U, because all gates contain C. Prescribe a star rooted at l0 with these attachments and a fixed child order. The directed incidence graph has a unique source strongly connected component containing l0: l0 reaches every vertex; any component with an edge into it would be mutually reachable. Thus this is a permitted partition forest with exactly one root and one visit per used gate.

When U is empty, use any assignment of T to relevant gates and any source-component spanning forest. Every used gate owns at least one distinct coordinate, so 1<=K<=|T|. These are finite successful queue runs with positive probability: all sizes, subsets, child counts, attachment multisets and positive child labels are prescribed. A deterministic choice suffices; any posterior supported on these runs has the same root-count bounds. The fixed generator and lambda are independent of U,T.

If U is nonempty and T empty, choose a single ordered cover per gate, with the r core coordinates first in the same order. For each l, the run selecting subset U at root l with no children has B_l=log(1/lambda_l)+log(1/(p rho_l)) plus the same rank term. Averaging with eta_l=lambda_l rho_l/s subtracts H(eta) once. Therefore the normalized label-plus-rarity contribution is exactly delta, and the remaining common rank term is retained. Root-dependent subset normalizers and other actual run choices belong to the complete cost, not to this exact B-component identity.

### 3. The Boolean spectral suppression of exceptional multiple roots

Since A_r has coefficient p at every core subset, for (U,T) different from (empty,empty),

    Fhat(U union T)=2p Bhat(T), Fhat(empty)=2pb-1.

Parseval gives v=4pb(1-pb). Direct physical edge probabilities give

    I(F)=p I(g)+2rp b=I_data+I_core,
    I(g)=4 sum_T |T| Bhat(T)^2.

The entire nonempty-data, empty-core spectral mass is 4p^2 b(1-b). Every other nonempty spectral set has exactly one root in the construction above. With E denoting the unconditioned spectral-weighted sum over nonempty sets and their selected forest laws,

    E K-v=sum_{T nonempty}4p^2 Bhat(T)^2(E[K|empty,T]-1)
       <=4p^2 sum_T |T| Bhat(T)^2=p^2 I(g).

It is nonnegative. By elementary induction r 2^(-r)<=1/2 for r>=1, so r(E K-v)<=I_data/2. This all-r estimate is an analytic finite-to-infinite bridge, not inferred from a finite search.

### 4. Cancellation and payment

Here a=ps, s=sum lambda_l rho_l<=1, and log(1/pi_l)=r+log(1/rho_l). Substitution into the exact root normalization yields

    T_root=v(-r+log s+delta)+r E K+E base rarity.

This proves the identity in the target. Further,

    v delta<=4pb *p s log e
       <=(2ps/r)(log e) I_core <=(log e) I_core.

Together with the previous subsection and log s<=0, the total extra common-core contribution is at most I_data/2+(log e)I_core<=(log e)I(F). No negative normalization was removed before locating its cancellation. This theorem allows arbitrary overlapping data supports and arbitrary Boolean g, but leaves their complexity in the base rarity and other forest terms. It therefore supplies no argument for unrestricted FEI by itself.

### 5. Exact heterogeneous-petal excess

Take disjoint private conjunctions of widths w_l>=1. Put rho_l=2^(-w_l), Q=product(1-rho_l), b=1-Q. Assign private spectral coordinates to their own petal. When U empty there are no incidence edges, hence every touched petal must be a root and K is its touched-block count. When U nonempty use the star above.

Write B=1-product_l(1-b_l). Each complementary factor has squared Fourier norm 1-rho_l; its nonempty spectral mass is rho_l(1-rho_l). By disjoint-support tensor factorization,

    sum_{T nonempty} Bhat(T)^2=b(1-b)=Qb,
    sum_T K(T)Bhat(T)^2=Q sum_l rho_l.

Hence E K-v=4p^2 Q(sum_l rho_l-b), exactly. Nonnegativity also follows from the event union bound b<=sum rho_l. For m>=2 the difference is positive. Exact cancellation fails on some sets, yet its expectation is O(I), uniformly in r,m and all widths. These are genuine overlapping gates with read m, not duplicated representations.

### 6. A fixed paid scale prior, without a free adaptive scale

For j>=0 take lambda_l^(j)=2^(-j)lambda_l and w_j=1/[(j+1)(j+2)]. The weights telescope to one and each entire conditioned reference Q_{*,j} is a subprobability, with its own s_j, Lambda_j, Z_j and every subsequent queue choice. Q_mix=sum_j w_j Q_{*,j} is therefore a subprobability. Choosing component j=0 globally pays log(1/w_0)=1 on every nonempty spectral set, i.e. exactly v. Since v<=4pb<=2 I_core/r<=2 I(F), the normalization/core component plus this paid prior is bounded by E base rarity+(2+log e)I(F).

This is only a component bound inside the full reference inequality. Its unbounded base costs are not dropped or claimed paid. If one chooses a different j, log D_j and its full B_j must stay together and the selection penalty must be paid; -v log s_j is not a free gain independent of the positive lambda_j label costs. No output-dependent scale is selected in the displayed estimate.

### 7. First unsupported line for a whole-cost theorem

No gap is claimed in the stated root-component proof, but independent reconstruction is pending. The first unsupported line for G-J-COST is that the remaining expectation of gate labels, base rarity, ranks and subset congestion minus the remaining actual-run entropy has an absolute influence bound for this general activation representation. The theorem does not establish that line. In particular arbitrary g remains embedded here, consistent with the source's rare-activation hardness reductions.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json is written before running the checker. Domain: 69 shared-core heterogeneous-petal cases, r=1..4, m=1..3, sorted widths 1..3 and total n<=10; additionally all 270 nonconstant truth tables on 1..3 data bits at each r=1..4, totaling 1080 arbitrary-data activation cases. Petal permutation is the only symmetry reduction. Integer FWHT and Fraction arithmetic verify every Fourier coefficient, Parseval variance, influence against independent physical edge counts, and root-excess identities and inequalities. Exact rational multiplication checks the initial-root probabilities sum to one and the cancellation factorization. Analytic exp/log inequalities above supply the all-parameter sign assertions; no floating-point entropy search is used as proof.

Commands from A007: `python -X utf8 runs/20261011T215236Z-fleet05-A007-root-normalization/code/check.py --freeze`, then the same command without `--freeze`. The saved output out/CHECK.json records the actual assertion count and observed runtime. The frozen memory estimate is 20 MB, below the 300 MB threshold; no heavy job or GPU was used, and the dimension never increased beyond the frozen cap.

## proof dependencies and changed downstream conclusions

Only the source-complete conditioned forest interface, finite KL/Gibbs identity, normalized complete-reference mixture argument, and elementary Boolean Fourier algebra are used. No unreviewed A006 numerical bound is assumed. This is one combined pending candidate, leaving B02 with two complete unreviewed candidates including A006, so the next step should be review/repair rather than a new broad candidate.

New conclusion for A006 and A014: common r-core rarity contributes O(I) after normalization even for arbitrary overlapping data gates. Multiple roots on spectra missing the core do not require an additional unbounded rarity budget; their spectral mass has a p^2 factor. The remaining obstruction is the complete base coding cost, not this common rarity scale. A086 and A094 should independently reconstruct source-component validity and the spectral weighting.

## one next mathematical action and independent reviewer

Next action: A086/A094 reconstruct the star forest and the root-count expectation, then A006 substitute this component theorem into the shared-r-core posterior ledger, retaining every remaining label/rank cost. This run does not change the stream packet without review.

## actual persistence receipts or precise save blocker

All requested run files, ROOT_NORMALIZATION.tex, ROOT_FAMILY.md, frozen specification, code, exact output, source hashes and file receipts are saved locally in the assigned A007 directory. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated. out/RECEIPTS.json binds persisted file hashes and sizes. Supervisor publication/mirror copying and independent review are pending and are not represented as completed.
