# C30 v1: a linear finite-height mean criterion for ordinary frog recurrence

Status: proof (unaudited). Kind: special. Dossier target: 1.
This is a sufficient criterion and a standard second-moment argument, not a solution of T127 or a novelty claim. The unpaid step is proving positive linear exact-law mean growth for a valid lower model such as C29.

## Statement and coupling hypotheses

Let d>=2. Consider the ordinary one-frog simple-random-walk model on the infinite rooted d-ary tree: one initial active frog at the root o and one sleeper at every other vertex. Write W for all visits to o after time zero, allowing W=infinity. Let u be the child first chosen by the original root frog, and use that frog as one incoming seed at u.

For every integer H>=1, suppose a lower exploration produces R_H under the same preassigned independent ordinary personal paths. It may awaken only the original residents at levels 0 through H below u. It has no extra or cloned frogs, retains their original motion (it may suppress waking or kill frogs), and stops/counts each frog at most once, on its first hit of o. Its first-hit returns are contained in the full ordinary activity, so R_H<=W. A protocol's serial exploration order may differ from physical time; its lower comparison must still be justified by finite awakening witnesses, as in C27. Arbitrary particle counts satisfying no such coupling are excluded.

Put c=limsup_(H->infinity) E[R_H]/H. Then 0<=c<=1/d and

    P(W=infinity) >= d*c.                                    (1)

In particular, if c>0 the ordinary model is recurrent almost surely by HJJ Theorem 4. At d=3 it suffices to prove limsup E[R_H]/H>0. Bounds along any unbounded sequence of heights suffice. A finite list of positive normalized sample means does not supply this hypothesis.

## The independent all-active envelope

For each resident v at level n below u, let I_v indicate that its entire preassigned ordinary walk ever reaches o. Let I_* be the corresponding indicator for the incoming root frog's future walk starting at u. Define

    C_H = I_* + sum_(n=0)^H sum_(|v-u|=n, v below u) I_v.

A walk at distance n+1 from o hits it with probability d^(-(n+1)). This follows by projecting to distance, whose inward/outward probabilities are 1/(d+1) and d/(d+1), and using finite gambler's ruin followed by an increasing-boundary limit. Conditional on the first chosen child u, the incoming future and all resident paths are independent. Their hit indicators are therefore independent Bernoulli variables. Their conditional laws do not depend on which u was chosen, so the following moments also hold without conditioning:

    mu_H = E[C_H] = 1/d + sum_(n=0)^H d^n*d^(-(n+1))
                     = (H+2)/d,
    sigma_H^2 = Var(C_H) = sum_i q_i(1-q_i) <= mu_H.       (2)

The first 1/d belongs to the incoming seed; the level-zero resident supplies a separate 1/d. The envelope includes every potential resident in the permitted origin set, whether or not it awakens. Each counted lower absorption requires that the SAME original frog's assigned path hits o. Thus pathwise

    0 <= R_H <= C_H  and  R_H <= W.                          (3)

No independence of awakening indicators is asserted. In particular C_H and W are generally dependent. Motion during suppressed excursions is retained, so the origin restriction concerns which residents can awaken, not where their walks may travel.

## From a linear mean to infinite returns

Fix an integer M>=1 and set A_M={W>=M}, q_M=P(A_M). From (3), on A_M use R_H<=C_H, and on its complement use R_H<=W<M. Therefore

    E[R_H] <= M + E[C_H 1_(A_M)]
             = M + mu_H*q_M + E[(C_H-mu_H)1_(A_M)]
             <= M + mu_H*q_M + sigma_H*sqrt(q_M).          (4)

The last step is Cauchy-Schwarz, not a conditional-independence assumption. Divide by H and take limsup. Equation (2) gives mu_H/H -> 1/d and sigma_H/H -> 0, hence

    c <= q_M/d.

As M increases, A_M decreases to {W=infinity}. Continuity from above gives c<=P(W=infinity)/d, proving (1). The same envelope gives c<=1/d. HJJ, Recurrence and transience for the frog model on trees, arXiv:1404.6238, Theorem 4, states that recurrence of this ordinary rooted-tree model with iid initial conditions has probability zero or one. Its application here is to the ordinary simple-random-walk model only. If c>0, (1) and that theorem give P(W=infinity)=1.

Equivalently, if the full ordinary model is transient, then every legitimate finite-origin retained-motion lower family satisfying these coupling hypotheses has E[R_H]=o(H). Infinite full-model expectation by itself does not contradict transience; the linear finite-height condition together with the envelope is the extra ingredient.

## Scope and the precise missing lemma

C28 shows E[R_H] uniformly bounded for each fixed ordinary awakening-entry cap, so that family has c=0 and cannot use this sufficient criterion. It gives no transience conclusion for the full model. C29 uses caps that grow with absolute depth and is not closed by that uniform-cap estimate.

The exact missing target for C29 is:

    Prove that some c0>0 and unbounded sequence H_j satisfy
    E[R_(H_j)^(log-caps)(1)] >= c0*H_j.

No such inequality is proved here. The three-replicate population means through height64 are numerical evidence with unbounded inherited bias, not lower bounds on these expectations. Their linear appearance cannot instantiate this theorem. An RDE argument that multiplies child means despite adaptively chosen input counts would also leave a gap.

The exact finite-depth recursion and lower coupling of the chosen protocol must be independently audited as well. C27 v2 supplies the uniform-cap construction; C29_MODEL_NOTES.md states the unequal-cap extension, which has not yet received its own complete independent audit. This criterion is valid conditional on its displayed coupling hypotheses and does not certify that extension.

Checks: computations/C30_EXACT_CHECKS.json recomputes the finite Bernoulli moment identities in exact Fraction arithmetic for d=2,3,5 and H=0,...,12, including the incoming seed. It checks algebra only. No Lean or independent-review PASS is claimed.
