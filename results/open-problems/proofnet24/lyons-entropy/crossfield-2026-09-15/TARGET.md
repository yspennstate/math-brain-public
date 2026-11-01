# Lyons entropy: 100 creative cross-field proof attempts

Started 15 September 2026 after preservation of the interrupted earlier campaign. The user's new request is 100 creative proof sub-agents, no audit assignments, with ongoing GitHub publication. The user called the target “Eliyahu's conjecture”; retrieved material identifies only Lyons's entropy conjecture. An optional clarification returned no answer, so this campaign explicitly continues the recovered Lyons statement. This name assumption must remain visible until clarified.

## Exact goal

For every finite n, Hermitian positive contractions K0,K1 and t in [0,1], prove

    H(P_((1-t)K0+tK1)) >= (1-t)H(P_K0) + t H(P_K1).

The determinantal occupation law is P(S subset X)=det(K_S). H is Shannon entropy with natural logarithms in the fixed measured coordinate basis. This is Russell Lyons, Determinantal Probability: Basic Properties and Conjectures, Conjecture 2.6 (2014; conjecture originated in 2003), https://arxiv.org/abs/1406.2707. Yuzhou Gu's rank-one-direction and scalar/zero-endpoint results are established prior work: https://sevenkplus.com/data/dpp.pdf. A general proof is not known in the recovered research record. A finite computation is not a universal proof.

## Execution

X001-X100 are distinct new creative assignments. Six workers can run concurrently; root records actual launches and terminal completions separately. A planned assignment is not a launched or completed agent. Workers do not spawn, push, or edit other workers' files. Root integrates mathematics and publishes checkpoints without overwriting other active campaigns. No audit agents are assigned. Checking one's own derivation is part of producing a proof.

Read your ASSIGNMENTS.json row and FRONTIER.md, then only the source reports relevant to your idea. Aim for a complete proof of the assigned obstruction, a rigorously delimited new theorem, or a constructive alternative when the proposed bridge fails. Do substantive mathematics: a list of analogies is insufficient. Work independently on your assigned field connection; send promising exact identities to root early. Avoid broad random searches as the primary deliverable. A small self-check of a new identity is useful.

Save a substantial initial derivation promptly in agents/XNNN.md and update it as work develops, so work survives interruption. Save reproducible supporting code under computations/XNNN/. End with the strongest established statement, its full argument, how it bears on the universal goal, and the exact remaining lemma if unresolved. Explicitly distinguish proved identities, conditional reductions, conjectures, and numerical observations. Preserve failed derivations with their corrected conclusion when useful; do not report an unsupported proof. Include primary source URLs for imported specialized theorems and verify their hypotheses. Do not invent model, effort, or execution claims.

Local campaign: /workspace/scratch/9028a8e284b1/crossfield-lyons-20260915

GitHub destination: yspennstate/math-open-problems, master, proofnet24/lyons-entropy/crossfield-2026-09-15/.

Prior ongoing campaign (read only): /workspace/scratch/f042dae27852/creative-lyons-20260915.
Earlier research (read only): /workspace/scratch/f042dae27852/research-session.

## Exact local calculus

For 0<K<I, p_S=det M_S where column j is K e_j if j belongs to S and (I-K)e_j otherwise. Along K+tA, A Hermitian, D_S has corresponding columns plus/minus A e_j, R_S=M_S^-1 D_S:

    p'_S=p_S tr R_S,
    p''_S=p_S[(tr R_S)^2-tr(R_S^2)],
    H''=-sum_S (p'_S)^2/p_S - sum_S p''_S log p_S.

Both terms matter. The measured entropy is not spectral quantum entropy, arbitrary unitary diagonalization changes it, and an affine odds-matrix path is not an affine kernel path. Any method must retain those distinctions.
