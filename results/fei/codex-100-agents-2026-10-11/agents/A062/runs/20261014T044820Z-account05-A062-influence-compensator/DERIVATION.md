# Exact controller reserve after partial core exposure

All entropy is in bits and influences are ordinary. Let a be ANY Boolean function on m uniform coordinates and let T be a fixed finite fresh-coordinate complete tree for a. Fix C>=4. Write Q_C(a,T) for its complete least nonnegative Bellman reserve. Introduce a fresh sign w, and two disjoint parity cores u,v, each on at least two fresh coordinates. Define h=w*a and F=(1+h)u/2+(1-h)v/2. This is an actual exclusive non-point controller using the SAME two cores on both physical children. Core variables and controller variables are disjoint.

The declared continuation first follows T on the a coordinates, then reveals w, then exhausts whichever parity core remains relevant. A prescribed prefix may reveal p parity coordinates beforehand, while leaving at least one unqueried coordinate in EACH parity. The prefix is fixed; outcomes may set parity phases, which the following identities allow. No core reserve, controller reserve, or terminal entropy is silently discarded.

## 1. Entropy and the physical controller account

At each such partial-core history, both remaining parity cores are balanced characters on disjoint coordinates and have entropy zero. The tag w keeps h balanced at every a-history. For a nonconstant a-history, coefficients of F at the two pure parity labels are 1/2. The remaining coefficients occur in two disjoint data-label sectors, with magnitudes |ahat(S)|/2 and with control label w adjoined. They remain disjoint even at S=empty. Thus the two pure-parity atoms contribute one entropy bit, and the tagged packets contribute one plus H(a)/2:

H(F_history)=2+H(a_history)/2.

Querying an a-coordinate swaps the selected cores exactly when a changes; independent balanced parities disagree with probability 1/2. Hence Inf_i(F)=Inf_i(a)/2 and D_i(F)=D_i(a)/2, including every conditional physical child. A revealed parity bit has influence 1/2 and entropy decrement zero as long as its core remains a nonconstant parity afterwards. These are raw spectrum and edge statements, not independent-copy replacements.

The physical selector probabilities are q_u=q_v=1/2 throughout every a-coordinate query, because w is unqueried. Both core variances are one. Thus the variance-rarity bank V=sum q_j log2(1/q_j)Var(core_j) equals one and its controller release kappa is exactly zero. Both prescribed parity core reserves are zero for every C>=0, since pure-character queries have entropy decrement zero.

## 2. The COMPLETE reserve identity and exact prefix debit

At a T-leaf, a is constant and h=+/-w. Before w is queried, H(F)=2; its children are the selected parity cores with H=0. Its influence is 1/2, so its local debt is 2-C/2<=0 for C>=4. Remaining pure-parity queries have zero reserve. Therefore the lifted leaf continuation has reserve zero.

Backward induction over T, using homogeneity of the positive part and the two exact half-factor identities above, proves

Q_C(F_history, declared continuation)=Q_C(a_history,T_history)/2.

This is an identity for the complete tree, with the terminal mux entropy paid at the w query. It is not the aggregate whole-path debt identity and is valid for any adaptive T on the seed.

Each parity-prefix query has D=0, d=1/2 and identical continuation reserves at its two physical outcomes. Its own debit C/2 is available exactly once. For p such queries, iteration gives the exact initial reserve

Q_C(F, parity prefix then declared continuation)=[Q_C(a,T)-p*C]_+/2.

At the frontier immediately after the prefix, the actual reserve is still Q_C(a,T)/2 at every reached history. The earlier p*C/2 payment may reduce the initial reserve; it cannot be reused in a local controller inequality at that frontier. This is an exact version of the preceding stage's character-account preservation mechanism, now at unfinished core exposure and without a limiting padding argument.

## 3. An unbounded local controller residual with zero release

For a take the actual canonical B05 selector seed a_k: b_k=(-1)^(x1*x2+...+x_{k-1}*x_k), k even>=4, and its zero-vertex sign flip; activate both by r=2k point controls and select them by a fresh fair seed selector s. Put delta=2^-k, alpha=2^(-k/2), p0=2^-r. Its selector influence is d_s=p0*delta.

At any nonempty bent-data Fourier label and any control frequency, the seed's paired selector amplitudes are A=p0*(sigma*alpha-delta), B=p0*delta, sigma in {+1,-1}. Their conditional selector probability theta=B^2/(A^2+B^2) is at most 4delta: alpha<=1/4 and (sigma-alpha)^2+delta>=1/4. The one-sided term B^2 log2(1/theta) is a lower bound on packet erasure. Summing these packets gives at least (1-delta)d_s*(k-2); all other erasure contributions are nonnegative. Consequently

D_s(a_k)/d_s >=(1-delta)(k-2) -> infinity.

After one parity bit has been physically revealed in F, both cores remain nonconstant. At the seed-selector query, D_F/d_F equals this seed rate exactly and kappa=0. Inherited parity core reserves are zero, so the candidate local extension

D_controller <=11*d_controller + V-E V_child + sum q_j*r_j-E sum q_j,child*r_j

fails for every even k>=14 at this ACTUAL reached node. More generally no fixed local price can cover this family with only the variance-rarity and parity-core banks. This refutes the all-controller extension of that particular potential, not A064's stated ordered-point theorem, the existence of another policy, or full FEI.

The correct declared-tree reserve at the node is exactly Q_C(a_k,T)/2, so the obstruction has an identified controller owner. The root prefix may still pay it from its earlier data debit. Zero core reserves and zero variance release alone cannot do so locally.

## 4. Finite and limiting qualifications

The transfer and prefix identities are finite-tree backward inductions. The all-k local witness is a separate explicit Boolean construction and inequality; no exhaustive truth table on its huge full cube is claimed. Compressed rational Fourier histograms are derived directly from the Boolean activation, retaining the exceptional empty row and its multiplicities. No optional-stopping or infinite-depth limit is used. The threshold C>=4 is necessary for the zero lifted leaf reserve; at smaller C the residual w-mux leaf would need a nonzero reserve and the exact half-transfer changes.

## First unsupported universal line

One still needs an independently priced controller seed reserve Q_C(a,T), or a different policy that spends an available physical account before the bad controller query and retains that account through later exposure. For general unequal/non-flat cores there is no proved exact half-factor transfer: coherent shared/empty rows and both actual terminal references must be kept. The shortest next step is one conditional controller-reserve graft at the next exposed priority query, with its initial capacity and earlier consumed data debit both explicit.
