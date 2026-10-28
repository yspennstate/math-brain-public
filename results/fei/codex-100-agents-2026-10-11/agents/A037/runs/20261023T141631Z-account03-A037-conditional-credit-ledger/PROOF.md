# Isospectral posterior calibration releases, and does not renew, credit

All logarithms and KL divergences are in bits. This is a normalized reference-conversion theorem, not FEI. External independent review is pending.

Let f be any Boolean function, i any queried coordinate, and let its two restricted functions have IDENTICAL squared Fourier laws s. Let p be the parent's squared Fourier law. Fix 0<alpha<1 and an occupied nonempty parent witness S (p(S)>0). Put t=p(empty), u=s(empty), T=S without i, beta=1-alpha. Supply the ACTUAL original reference

q=beta p+alpha t delta_empty+alpha(1-t)delta_S.

This includes characters and constants whenever an occupied nonempty S exists; if the reference coincides with p, it simply incurs zero source KL. No current-essential-mask requirement is assumed: T follows the original witness.

## 1. Physical normalization and inherited reference

For every residual frequency U, write the two real child Fourier amplitudes a_U,b_U. Their squares both equal s(U). The parent's amplitudes on U and U union {i} are (a_U+b_U)/2 and (a_U-b_U)/2. Thus exactly one of the parent squared masses is s(U), unless s(U)=0, in which case both vanish. Erasing i sends p to s and sends S to an occupied child witness T. At U=empty this implies t is either u or zero. In particular 0<=t<=u.

The physical Bayes kernel is K_y(U)=s(U)/(2s(U))=1/2 on every positive source row. The reference is support matched, so source-zero rows have zero reference mass; any fair completion there is harmless. Consequently its OWN outcome probabilities are r_0=r_1=1/2. In BOTH children the actual normalized inherited reference is

q_old=beta s+alpha t delta_empty+alpha(1-t)delta_T.                 (1)

No factor 2r_y, discarded child, or activation-sign approximation appears here. These equations apply to the complete spectrum of f. They do not automatically apply to a further coherent controller whose two child spectra need not remain isospectral.

## 2. Nonempty witness: sharp signed calibration criterion

When T is nonempty, choose the fresh matched-empty reference

q_new=beta s+alpha u delta_empty+alpha(1-u)delta_T.                 (2)

This moves h=alpha(u-t)>=0 from T to empty. During this entire segment q_h(empty)<=u=s(empty), whereas q_h(T)>=s(T): the latter follows from s(T)<=1-u. The only changing terms of D(s||q_h) have derivative

dD/dh=[s(T)/q_h(T)-u/q_h(empty)]/ln(2)<=0.                       (3)

If u=0, then t=0 and h=0. Otherwise all denominators in (3) are positive. If h>0, the derivative is strictly negative before the endpoint, because q_h(empty)<u there. Therefore the actual signed refresh cost, averaged over BOTH physical outcomes, is

sigma=D(s||q_new)-D(s||q_old)<=0,

with sigma<0 if and only if u>t, and sigma=0 if and only if u=t. In the equal-signed-mean case t=u this recovers A050's zero-conversion result. Opposite nonzero child means give t=0<u and STRICTLY RELEASE credit. Identical child spectra alone do not force the conversion to vanish.

## 3. Witness retirement

If T is empty, equation (1) becomes q_old=beta s+alpha delta_empty. We explicitly RETIRE the spike and use q_new=s, rather than silently introducing a new nonempty witness. Its fresh KL is zero. Hence sigma=-D(s||q_old)<=0, with strict inequality exactly when u<1. This endpoint uses Gibbs inequality and equality iff the laws agree. It does not give a free new witness or a free fixed-alpha full-mask source.

## 4. Same original adaptive account and no double spending

At an arbitrary finite adaptive tree, use this calibration only on edges satisfying the displayed isospectral hypothesis, with their actual inherited references of the displayed form. At other edges, keep A050's transported witness reference exactly or book any additional conversion explicitly; no assertion is made that such transport preserves the calibrated two-atom profile. For a general reference node v, write A_v=D(P_v||Q_v), E_v=D(P_v||Q_v)-D(erase P_v||erase Q_v)>=0, and O_v=D(fair||r_v)>=0. If A'_child denotes KL after the ACTUAL child reset, and sigma_v=average(A'_child-A_inherited_child), then

A_v+sigma_v=E_v+O_v+average A'_child.

Multiply by original physical reach weights and telescope, retaining all complementary leaves:

sum_internal w_v(E_v+O_v)+sum_frontier w_v A_v
 = A_root+sum_internal w_v sigma_v.                            (4)

For the present nonpositive calibrations, define released credit C=-sum w_v sigma_v>=0. Then

C+sum_internal w_v(E_v+O_v)+sum_frontier w_v A_v=A_root.         (5)

In particular C<=A_root. Conditional on any reached node h, the identical formula holds with A_h as initial resource and conditional physical reach weights. The child KL on the inherited side is consumed when it is lowered; it is not available again as its former value. One cannot book C as new source capacity while continuing to count pre-calibration KL at the frontier. For arbitrary positive resets, their separately booked sum is added to the right-hand side of (5). This is the precise restriction under which this stage proves no renewed credit; it does not assert nonpositive calibration at arbitrary nodes.

## 5. Self-dual scope and honest universal gap

For any self-dual Boolean function f(-x)=-f(x), the two restrictions satisfy f_-(z)=-f_+(-z), so their Fourier squares agree. Also t=0. Thus EVERY first coordinate query of a self-dual function is eligible, for every supplied occupied witness; nonempty T gives strict release whenever the restricted mean is nonzero. Descendants need not be self-dual, so this is not a claim that every later query qualifies. A finite tree made solely of eligible nodes satisfies (5), but eligibility must be checked at each node.

First unsupported universal line: provide every Boolean core with an influence-priced original complete supplier and a query/stopping policy meeting the terminal surplus reserve, while allowing these calibrated or transported witnesses. A matching-empty KL reference by itself does not pay H, and choosing q=p would only make a transport identity trivial. A036/A040 rare-query positive resets, A037 cumulative whole-core exhaustion, and A048 mod3 exhaustion remain intact; none satisfies the hypotheses of this theorem at every required refresh. No universal FEI constant or counterexample is claimed.

## 6. Complete finite conditional-account replay

Additional complete-tree replay PASS: 1334 source/witness trees, 9206 reached internal nodes, 2198 eligible actual resets, 128 strict releases, 66640 exact assertions, 9.319s. Every reached conditional node checks C+erasure KL+outcome KL+terminal KL=A_node, not merely the root. The fixed coordinate-order policy tests the ACTUAL incoming reference for admission and otherwise retains its normalized inheritance. Commands: `python -X utf8 runs\20261023T141631Z-account03-A037-conditional-credit-ledger/code/ledger.py`; domain and limits frozen separately in LEDGER_SPEC.json before execution.
