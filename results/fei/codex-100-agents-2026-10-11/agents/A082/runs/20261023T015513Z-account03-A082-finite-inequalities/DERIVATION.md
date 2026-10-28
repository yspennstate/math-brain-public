# Original-source returns equal current-reference calibration

The apparent repeated-return liability vanishes when every prescribed return includes final vacuum calibration. The second calibration cancels the first nonempty rescaling exactly. This extends the supplied-likelihood history theorem; it does not construct an inexpensive reference for an arbitrary Boolean function.

All logarithms are in bits. A reference is a complete normalized probability law on Fourier subsets, with finite cross entropy on the actual source. Spectral coordinate deletion is pushforward, not physical conditioning. Physical child spectra use signed Fourier amplitudes.

## 1. Exact calibration identity and endpoint cases

For a normalized law R with R(0)<1 and prescribed vacuum probability p in [0,1], define

    C_p(R)(0)=p,
    C_p(R)(T)=(1-p)R(T)/(1-R(0)), T!=0.

If p=1 the result is the explicit point law delta_0. When R=delta_0, finite actual cross entropy forces the represented Boolean function to be constant, so only p=1 is required. No 0/0 branch is used.

Let M delete any collection of spectral coordinates, hence M(delta_0)=delta_0. For p<1 put alpha=(1-p)/(1-R(0))>0. The exact affine identity, including the vacuum, is

    C_p(R)=alpha R+(1-alpha)delta_0,
    M C_p(R)=alpha M R+(1-alpha)delta_0.              (1)

The coefficient 1-alpha need not be nonnegative; this is a linear identity, not a probability mixture. Both sides are actual probability laws because calibration and pushforward preserve normalization and nonnegativity. This distinction matters when p<R(0).

Write x=(M R)(0) and y=(M C_p(R))(0). Equation (1) gives

    1-y=alpha(1-x),
    (M C_p(R))(T)=alpha(M R)(T), T!=0.              (2)

For a final prescribed q<1, finite actual child cross entropy ensures x<1 and y<1. Thus both denominators are strictly positive, and (2) proves, atom by atom,

    C_q(M C_p(R))=C_q(M R).                         (3)

At T!=0 the coefficient equality is

    (1-q)*alpha/(alpha*(1-x))=(1-q)/(1-x).

At T=0 both sides equal q. If q=1 both sides are delta_0. If p=1, the actual Boolean function at the earlier calibration is constant; all physical descendants are constant, so q=1 and both sides are again delta_0. The identity is therefore valid on every actual finite-CE physical history where these calibrations are requested. It makes no assertion for artificially incompatible endpoints p=1,q<1.

## 2. Arbitrary nested ORIGINAL-source resets

Fix one normalized original source reference S. At a physical history h, let M_h delete exactly the queried Fourier coordinates; define the prescribed target

    F_h=C_(E[g_h]^2)(M_h S).

Suppose the current law was first reset at an ancestor u to F_u, and subsequently only marginalized or vacuum-calibrated. Inductively, its nonempty entries at h are a common positive multiple of the nonempty entries of M_h S, unless the actual function is already constant. Applying (3), resetting at h to F_h is EXACTLY calibration of the CURRENT inherited law to E[g_h]^2. It preserves the original nonempty conditional profile after all actual coordinate deletions; no arbitrary new source profile is admitted.

For a normalized current law Q with true vacuum probability q, the change in cross entropy caused by C_q is

    CE(P,C_q(Q))-CE(P,Q)=-D_Ber(q || Q(0))<=0.       (4)

This follows by separating the vacuum atom from the normalized nonempty conditional law; endpoints use the finite-CE conventions above. Thus every repeated return to the ORIGINAL source marginal, with final calibration, is a nonpositive signed conversion from the current law. It requires no reserve, reinitialized comparison measure, or discarded terminal. An intermediate calibration followed by marginalization ALONE can change the result. Equation (3) specifically includes calibration at the final child on both routes.

## 3. Independent reconstruction of the supplied-likelihood frontier theorem

Use the exact hypotheses of A096-SELECTIVE-FRONTIER-LIKELIHOOD-TRANSFER@1: g is any finite uniform Boolean source, m=E[g]^2, D is a subprobability with D(0)=m and finite c=CE(P_g,D), S and Q are normalized, S>=D, Q(0)>=m, Q(T)>=gamma D(T) on nonempty atoms, 0<gamma<=1. Write L=-log2 gamma. D is a comparison measure only.

For each physical query, average squared child amplitudes equal the parent spectral marginal: [(u+v)^2+(u-v)^2]/2=u^2+v^2. Conditional cross entropy on every occupied spectral fiber therefore gives

    CE(P_v,D_v)=B_j(g_v)+mean_s CE(P_vs,M_jD_v)+R_v,

where R_v is a sum of nonnegative fiberwise conditional KL divergences. A positive occupied fiber has positive D_v mass by finite CE, so its conditional reference is normalized even when total D_v mass is below one. This proves

    sum_v w_v B_j(g_v)+sum_leaf w_leaf CE(P_leaf,D_leaf)<=c. (5)

Decompose D=m delta_0+N. Every physical pushforward preserves delta_0 and N has mass<=1-m. Hence at a leaf D_leaf=m delta_0+N_leaf and Q_leaf>=m delta_0+gamma N_leaf. At nonempty atoms the log likelihood ratio D_leaf/Q_leaf is <=L. At empty, put u=N_leaf(0). Convexity of -log gives

    log2[(m+u)/(m+gamma u)]<=uL/(m+u)<=(1-m)L,

since u<=1-m. The last rational inequality follows from m(1-m-u)>=0 after multiplying by the positive denominator. The cases m=0 or m=1 are treated directly. Thus each retained complete old leaf has excess over its D comparison at most

    L[(1-m)+m Var(g_leaf)].                         (6)

A fresh leaf C_(E[g_leaf]^2)(M_leaf S) costs no more than CE(P_leaf,M_leaf S), which costs no more than CE(P_leaf,D_leaf). Inserting this and (6) in (5) proves the exact history-dependent bound

    erasures + complete terminal costs
      <=c+L sum_(unreset leaves) w_leaf[(1-m)+m Var(g_leaf)]. (7)

The conditional means along the finite physical tree form a martingale, equivalently the conditional variance decomposition gives sum_leaf w_leaf Var(g_leaf)<=1-m. The sum on the right is therefore at most 1-m^2. No asymptotic limit or independence across branches is used. This reconstructs A096 v1 unchanged, independently of its producer checker.

## 4. Remove the repeated-ORIGINAL-return restriction

In any finite adaptive tree with arbitrarily many specified ORIGINAL-source calibrated resets, cut each branch at its FIRST reset, or at its final leaf if never reset. These first-reset nodes form an antichain. Apply (7) to this finite cut. All never-reset leaves retain their full original Q marginals, including every ghost and vacuum atom.

Below each first-reset node, every later prescribed ORIGINAL-source reset equals CURRENT-reference calibration by (3). Each such reset decreases CE by (4). Each physical query is paid by the complete-reference chain rule, with full terminal CE retained. Induction replaces the entire continuation below that node by no more than its first fresh CE. Consequently (7) and its dimension-independent bound

    sum_internal w_v B_j(g_v)+sum_final w_leaf CE(P_leaf,Q_final_leaf)
      <=c+(1-m^2)log2(1/gamma)                       (8)

hold for arbitrarily nested ORIGINAL-source calibrated returns. Selection, coordinate orders, stopping and reset times may depend on the physical history. In the sharper bound (7), unreset means branches with NO source reset anywhere on their path. Intermediate reset costs are signed changes of the same terminal account, not separately charged positive-only fees. All old erasures and all complementary nonconstant terminals remain in the final tree. No new bank is minted at a reset.

This is the precise extension previously left unpaid by A096. Its existing negative-cell rate18/7e reserve corollary can substitute these larger exit policies CONDITIONALLY on its unchanged live-bank premises; that entire upstream mixed live-bank chain is not independently accepted here. The abstract history theorem (8) needs no point-source assumption. The remaining universal obstruction is an influence-priced original source reference and occupied-support likelihood floor for arbitrary Boolean functions, or a genuinely different nonempty profile reset. Equation (3) does not pay arbitrary new conditional profiles.

## 5. The genuinely unpaid profile change

The remaining reset bill can be isolated exactly. Let P have vacuum q, and let the current normalized finite-cost law Q have vacuum v. Give a new law the SAME actual vacuum q but a prescribed new conditional nonempty profile R_+. If q<1 write P_+ for the actual conditional nonempty spectrum and Q_+ for the current conditional nonempty reference. Direct binary/nonempty disintegration yields

    CE(P,new)-CE(P,Q)
      =-D_Ber(q||v)+(1-q)[D(P_+||R_+)-D(P_+||Q_+)]. (9)

Every normalization remains present. At q=1 the second term vanishes and both new-reference and calibration conventions use delta_0. At q=0 the nonempty term has full weight and the binary divergence is still included. Finite CE supplies all denominators on positive actual atoms. Equation (3) means repeated calibrated ORIGINAL-source returns have R_+=Q_+, so only the nonpositive binary term remains. An arbitrary different nonempty profile has no such cancellation. The next real transfer obligation is the signed nonempty-profile divergence difference in (9), after the binary refund and the previously booked charges are accounted for.

## 6. Finite-to-infinite scope

No finite Boolean census is exhaustive for the all-dimensional statement. The exhaustive reduction is symbolic: every vacuum calibration is the affine transformation (1), every coordinate deletion preserves delta_0, and finite tree induction handles every history. The only rational scalar cancellation has positive denominators established above. Finite rational boxes and physical histories validate the implementation and exercise endpoints; equations (1)--(8) provide the separate theorem covering arbitrary dimension and arbitrary finite adaptive trees. This proves a supplied-reference transfer theorem, not full FEI.
