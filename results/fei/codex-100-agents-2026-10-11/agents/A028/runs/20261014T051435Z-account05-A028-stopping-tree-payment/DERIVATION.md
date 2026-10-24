# Arbitrary certified controller with one terminal boundary reserve

All entropy and KL are bits; b=log2(e), eta(t)=t log2(1/t), eta(0)=0. Let a(y)=1-2c(y) be any Boolean sign controller on a physical uniform cube absent from the Boolean data branches G(x),H(x). The branches may share every physical data coordinate. Put p=Ec, v=Var(a)=4p(1-p), gamma=Pr(G!=H), F=(1-c)G+cH, Q=gamma I(a), and

    Pi=H(F)-(1-p)H(G)-pH(H), R=2p(1-p)I(GH).

A control-only physical tree determining c stops at the ORIGINAL branches with weights1-p,p. Its full signed entropy path bill is Pi, and its physical queried influence is Q. The full influence identity is

    I(F)=Q+(1-p)I(G)+pI(H).                          (1)

No assumption on data overlap, bias, controller rarity or dimension is made. The theorem is

    Pi <= gamma Hplus(a)+b gamma Var(a)+2b Q+R
        <= gamma Hplus(a)+3b Q+R.                  (2)

Hplus(a) is the raw nonempty Fourier entropy sum, not conditional spectral entropy. Controller certificates and both terminal costs remain explicit:

    Hplus(a)<=K I(a) => Pi<=(K+3b)Q+R;
    Hplus(a)<=T[I(a)-Var(a)] => Pi<=[max(T,b)+2b]Q+R.

For certified branch allowances L_G,L_H, the COMPLETE path plus terminal allowance has root rate

    max(K+3b,L_G+2p,L_H+2(1-p)),                    (3)

or the same expression with K+3b replaced by max(T,b)+2b for a strong controller. This is a single-controller block theorem. Arbitrary opaque controllers or terminals do not receive free FEI certificates.

## 1. Exact binary-sector identity

Embed the child Fourier coefficients g_T,h_T on their union data cube. At a data set T the empty controller coefficient is m_T=(1-p)g_T+p h_T; nonempty controller U has coefficient chat(U)(h_T-g_T), where chat(U)=-ahat(U)/2. Consequently the data marginal is

    q_T=m_T^2+p(1-p)(h_T-g_T)^2=(1-p)g_T^2+p h_T^2.

Define z_T=p(1-p)(h_T-g_T)^2 and w=sum z_T=v gamma. Let

    Bbin=sum_T q_T h2(z_T/q_T),
    Jp=H(q)-(1-p)H(G)-pH(H).

Zero rows have zero contribution. Conditional on a nonempty controller frequency, the normalized controller law is ahat(U)^2/v, independent of T. Thus

    Pi=Jp+Bbin+w H(controller spectrum | nonempty),
    Pi=gamma Hplus(a)+Jp+Bbin+w log2(v).            (4)

The second identity applies when v>0; deterministic controllers are treated separately and have Pi=Q=R=0. Equation(4) keeps the signed empty-controller row and every nonempty sector. It is valid for arbitrary shared data, where a mean-only formula would fail.

Jensen for h2 gives Bbin<=h2(w). Since h2(w)<=w log2(1/w)+bw,

    Bbin+w log2(v)<=v gamma[log2(1/gamma)+b].       (5)

This cancellation is essential: the selector scale log(1/v) is not restarted or separately charged. The original gamma is the same source disagreement for the whole controller block. No sign-fold of H is used for a general controller.

## 2. Fully proved block JS bound

We reconstruct the physical-cube log-Sobolev step rather than assuming an arbitrary biased two-state inequality. For two real values u0,u1, the scalar entropy packet obeys

    Ent_{fair}(u^2)<=b/2 (|u0|-|u1|)^2
                    <=b/2 (u0-u1)^2.

To prove the first inequality, normalize their squared sum and use

    [(1+t)ln(1+t)+(1-t)ln(1-t)]/2 <=1-sqrt(1-t^2),

whose derivative comparison is atanh(t)<=t/sqrt(1-t^2) on[0,1); the derivative of the difference is nonnegative and the difference is zero at0. Apply it with t=(u0^2-u1^2)/(u0^2+u1^2), and extend zero endpoints continuously.

For a product cube, entropy tensorization gives Ent_y(U^2)<=sum_i E Ent_{y_i}(U^2). A direct proof starts from the exact two-factor identity Ent_{XY}f=E_Y Ent_X f+Ent_Y E_X f. Convexity of entropy (joint convexity of q log(q/r), or its elementary log-sum proof) implies Ent_Y E_X f<=E_X Ent_Y f; induction proves the tensorization. Therefore

    Ent_y(U^2)<=2b sum_i E[D_i U]^2,

where D_i U=(U(y)-U(y^i))/2. For every data frequency T use U_T(y)=g_T+c(y)(h_T-g_T). Its entropy is precisely that row's contribution to Jp. Since D_i c=-D_i a/2, Parseval gives

    sum_T sum_i E[D_i U_T]^2
      =sum_T(h_T-g_T)^2 I(a)/4=gamma I(a)=Q.

Hence Jp<=2bQ. This is the recovered block-JS constant, here independently proved and specialized to the owned controller influence; no arbitrary terminal entropy is hidden in it.

## 3. Boundary bank, owners, and complete cost

Boolean edge isoperimetry for the disagreement set gives gamma log2(1/gamma)<=I(GH)/2. One finite-cube proof bounds internal edges of a set of M vertices by M log2(M)/2, inductively splitting into sizesu<=v and counting cross edges at mostu. The binary entropy inequality h2(u/(u+v))>=2u/(u+v) closes the induction; subtracting internal from total incident edges yields the displayed normalized boundary bound. It is valid for gamma>1/2 as well as endpoints.

Multiplying by v=4p(1-p) proves that the logarithmic term in(5) is paid by

    R=2p(1-p)I(GH).

Combining(4),(5) and Section2 proves the first inequality in(2). Poincare Var(a)<=I(a) follows immediately by weighting each nonempty Fourier coefficient by at least1, proving the second. For a strong controller, gamma Hplus(a)<=T[Q-gamma v], so (2)'s first line yields [max(T,b)+2b]Q+R.

For EVERY physical data coordinate,

    Inf_i(GH)<=Inf_i(G)+Inf_i(H),
    R_i<=2p[(1-p)Inf_i(G)]+2(1-p)[p Inf_i(H)].     (6)

The bracketed quantities are actual terminal coordinate capacities. Their fractions are marked ONCE for the complete controller; they are not new independent copies of G or H on failed histories. Combining(1),(2),(6) with supplied terminal allowances proves(3). The source point-controller theorem of A023@3 is sharper at that special controller; this result does not replace it by a claim of improved point constants. Its new scope is arbitrary certified controllers and full shared-data overlap.

## 4. Carried boundary capacity through arbitrary physical interleaving

With G,H unchanged, let a physical controller query produce c0,c1 of means p0,p1, p=(p0+p1)/2. The marked bank obeys the EXACT nonnegative release

    R(p)-[R(p0)+R(p1)]/2
      =(p0-p1)^2 I(GH)/2 >=0.                      (7)

In particular a complete control-only tree resolving c has expected total releases exactly R(root), since terminal p is0 or1. Data coordinates need no second issue of the original mark. The same algebra holds coordinate by coordinate in(6); the expected terminal influence capacity (1-p)Inf_i(G)+pInf_i(H) is harmonic. On arbitrary adaptive controller-only histories this bank is a supermartingale with its same source product GH.

At a data query i, p is unchanged and both original branches are physically restricted on i (including a constant/dummy restriction for a branch not using i). Their product is restricted identically. The ordinary influence telescope for the Boolean product gives the EXACT release

    R(parent)-average R(children)=2p(1-p)Inf_i(GH)>=0. (9)

Since Inf_i(GH)<=Inf_i(G)+Inf_i(H), this release is <=2 times the ACTUAL queried data influence (1-p)Inf_i(G)+pInf_i(H). The expected terminal data capacity loses precisely that actual data influence at the same step; controller steps preserve it in expectation. Thus R is a nonnegative supermartingale under ANY adaptive physical control/data interleaving. At a fixed history the remaining controller and data coordinates are still independent uniform cubes, so the two conditional proofs apply without a new source law.

For every stopped interleaved tree,

    R(root)=sum_v w_v release_v+E_leaf R(leaf),

with release given by(7) or(9) according to query type. This establishes an exact ONCE-ISSUED bank, including retained terminal product capacity. A selected child may have a larger bank, but its actual probability-weighted siblings supply the conditional identity; no child receives a fresh root mark.

These are BUDGET conservation rules, not claims that each release bounds the local entropy increment or inherited reference conversion. The proof pays the ENTIRE control-only block via(2). Adding each descendant R to the ancestor R would still double-spend. Adding a second controller/nested nonconstant fallback changes the source family and requires a new signed transfer. The independent mixed-bank checker verifies all local restrictions in its frozen family, separately from the entropy implementation.

## 5. One normalized complete root reference

For a declared shared block S and disjoint private blocks X,Y of G(S,X),H(S,Y), take arbitrary normalized core references positive on the true spectra. Calibrate every shared-only atom to the corresponding true squared coefficient and preserve/rescale the private complement conditional law. This decreases terminal CE by categorical KL, including the private total cell, and retains all conditional private debt and off-target reference mass.

On a shared-only T use the TRUE root masses m_T^2 in the empty controller sector and chat(U)^2(h_T-g_T)^2 in a nonempty sector. On exclusive G data fibers use (1-p)^2 R_G^c(T) at empty controller and chat(U)^2 R_G^c(T) otherwise. On exclusive H fibers use p^2 R_H^c(T) at empty controller and chat(U)^2 R_H^c(T) otherwise. Mixed-private sets have zero mass. These rules apply equally when a true branch coefficient is zero; off-target exclusive reference fibers are retained. Total sector factors are1-p for G andp for H, and shared rows have their true data mass, hence normalization is exact.

Row probability ratios cancel controller factors, giving

    D(P_F||R_F)=(1-p)D(P_G||R_G^c)+pD(P_H||R_H^c),
    CE_F=(1-p)CE_G_cal+pCE_H_cal+Pi.                (8)

Thus(2),(3) pay this complete ideal output reference with its terminal deficits explicit. This root-reference algebra is not advertised as new history closure: A056@3 already supplies compatible physical-query kernels and controller-query E=O=C=0 at its stated scope. The finite checker here verifies normalization and BOTH CE/debt identities with true shared-atom calibration and uniform private conditional references, retaining off-target mass. It does not validate inherited data-query compatibility, integer prefix coding, or a universal terminal reference.

## 6. Honest universal boundary

Opposite constant data branches yield gamma=1, R=0, F=a (up to sign), so supplying a dimension-independent controller certificate on arbitrary a is itself FEI-strength. Conditional admission of recovered regular, bounded-overlap or threshold-formula controllers and terminals is legitimate only with their actual proved constants. The data surcharge uses one named boundary bank; it is not a proof that numerical child FEI bounds have spare slack to pay indefinitely many ancestors.

The first unsupported line is paying the actual signed entropy/CE excess at a MIXED query from the release in(7)/(9), the carried controller certificate remainder, and one unused signed child surplus. Bank conservation now holds even after data exposure; it does not prove that this conserved bank is sufficient for that selected query. A second controller/nested nonconstant fallback also requires a source-owned conversion. Retain original terminal weights and both seed reference bills. A023/A025/A029's nesting overcounts remain intact. This stage does not prove a local all-node drift estimate or universal FEI.

## 7. Exact release-alone obstruction and required extra price

The separately frozen drift probe refutes the tempting stronger DATA-node rule

    Delta H(F)-[(1-p)Delta H(G)+p Delta H(H)] <= release_R.

Take a=(-1,+1), hence p=1/2, G=(+1,+1) and H=(-1,+1) on one data bit. The true root table is(-1,+1,+1,+1), with four Fourier squares1/4, so H(F)=2 and I(F)=1. Both data branches and all physical data-query children are constants or characters, of entropy0. Thus the left side is2. The product GH=H has influence1, so R(root)=1/2, the child banks are0, and release_R=1/2. The exact excess is3/2 bits; no numerical logarithm is involved. The actual data query influence is1/2.

Consequently any repaired local bound of the form

    Delta H(F)-weighted branch entropy drops
      <=C_data Inf_data(F)+release_R

must have C_data>=3 already here. This is a scoped obstruction to release-only payment, not a counterexample to(2), the bank supermartingale, A023's point-block theorem, or FEI. The future controller influence remains a retained source resource, even though its conditional entropy certificate is zero for these characters. A complete proof may move that owned source credit to this query and charge its later use once; this probe does not justify such a transfer. The honest remaining line is the extra signed data/controller price, not conservation of R.
