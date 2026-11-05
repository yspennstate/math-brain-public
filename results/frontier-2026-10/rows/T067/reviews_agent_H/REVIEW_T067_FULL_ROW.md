# T067 review (agent H, 3 Nov 2026)

The scripts and outputs named below are in this folder. Run t067_q3_replay.py with the
folder papers/three-targets-2026-10-31/T067/computation/ as its argument.

Row T067 (catalog rank 56, "Tightness of the
Kesten-Stigum bound for reconstruction on trees").

## Reviewer and independence

- Reviewer: agent H. I took no part in writing the T067 proof, its
  certificates, its scope check or its independent challenge. No conflict to declare.
- Artifact read: the T067 proof package (its source and certificates are in
  papers/three-targets-2026-10-31/T067/ of this repository), with the authors' literal scope check and
  independent challenge.
- Compute: Python 3.14.3, about three minutes of CPU on one machine.

## Requirement map

| Original clause | What the package proves | Status |
|---|---|---|
| q=3, every d, d-ary tree: reconstruction iff d lambda^2 > 1 | Theorem for every finite-mean iid GW law, which includes every regular degree; equality case included (non-reconstruction at d lambda^2 = 1) | Proved, computer-assisted. The q3 certificate was replayed independently here (below). |
| q=4, every d | Same theorem; the q4 sign certificate is imported from the published four-state manuscript | Proved, computer-assisted. The full q4 sign traversal is UNRUN here (no C++ compiler on this machine). |
| "or a Galton-Watson tree of mean d" (q=3,4) | Every iid offspring law with finite mean, reconstruction a.s. on survival | Proved. The pruning order needs the one repair the challenge records (Prop. 6.1: Ulam-Harris order or iid marks). |
| q >= 5: the bound is not tight | Regular trees: Sly (cited). Laws with every exponential moment: a corollary of Mossel-Sly-Sohn Thm 1.13 (scope check, Sec. 3) | Holds only in those two settings. Non-tightness for every supercritical finite-mean (heavy-tailed) law is NOT proved, and the cited sources do not prove it either. |
| Ferromagnetic lambda > 0, finite noise | Domain 0 < lambda < 1; the noiseless endpoint is classified separately | Matches the row's intent. The literal wording needs "finite noise" stated. |

## Independent checks

1. **q3 certificate, full exact replay: PASS.** `t067_q3_replay.py` builds P_A and P_B in exact
   integers from the definitions printed in the certificate appendix (x, y, H, F, G; the chamber map
   p = (6a+3b+2c, 3b+2c, 2c)/(6S); X, Y, H^, F^, G^, U, Z, W, V, J; K_A, K_B and the clearing formulas).
   It uses its own sparse-polynomial code and none of the package's C++. Results:
   - P_A is homogeneous of bidegree (10,10): 4,356 positions, 3,873 positive, 483 zero, 0 negative.
   - P_B is homogeneous of bidegree (22,22): 76,176 positions, 71,627 positive, 4,549 zero, 0 negative.
   - Both agree with the package tables q3_independent_coefficients_{A,B}.tsv coefficient for
     coefficient, with ratio exactly 1. The tables hold plain monomial coefficients, not Bernstein-scaled ones.
     Table sha256: A 69f5a998801ec806..., B 07ea0c0724672b4d....
   - At 12 random interior rational points the clearing identities hold exactly:
     P_A = 864000 S^4 T^4 D_A R_A and P_B = 1296000 S^4 T^4 D_B R_B, with R_A and R_B computed from the
     posterior-level definitions (z_pi, r_pi, epsilon = 1/1000), not from the integer forms.
   Since every coefficient is >= 0 on the chamber variables (a..f >= 0) and S, T, D > 0 inside, R_A >= 0
   and R_B >= 0 on the sorted chamber. Both residuals are invariant under permuting p and under permuting q
   (the sum runs over all six pi), so this covers the whole simplex pair. No subdivision is needed, as the
   appendix claims.
   Output: t067_q3_replay.json; build 86 s, total 170 s.
2. **q4 small-polynomial checks: PASS.** published_q4/verification/checks/small_polynomials.py exits 0. The
   four scalar minima match, and all 24 symmetry actions verify (log t067_q4_small_check.txt).
   certificate.cpp hashes to the pinned source hash 9f9765fb...; certificate-source.txt hashes to 99595379.... The copies in this repository end with one added
   newline, which changes their hashes and nothing else.
3. **q4 full sign traversals (modes a and b): UNRUN.** They need g++ with Boost multiprecision, and the reviewer's
   machine has no C++ compiler. The recorded logs end "done 4479 19 lp=2074 lt=166" and "done 1935 20 lp=871 lt=97",
   as the README says they should. I treat that as the authors' record, not as my verification. Smallest
   action to close this: run the README's two commands on any machine with g++ (minutes).

What I did not re-derive: the analytic chain from R_A, R_B >= 0 to the reconstruction dichotomy (the
posterior-cone argument, the GW pruning and survival steps). I read it at the level of the independent
challenge, which found no gap other than the Prop. 6.1 ordering repair. That challenge was conditional on
the certificates; with check 1, the q3 condition is now met.

## Verdict

- **Narrower theorem (q = 3, 4; finite noise; every finite-mean iid GW law; equality included): ACCEPT**,
  with two conditions. The Prop. 6.1 ordering repair must be in the text. And the q4 traversal must be run
  once on a machine with a compiler before anyone writes "independently replayed" for q4.
- **Full original row: REVISE (scope).** The q >= 5 clause is supported for regular trees (Sly) and for
  offspring laws with all exponential moments (MSS corollary). Read literally over every supercritical
  finite-mean law, it is open, and neither the package nor its sources prove it. The row should either say
  that the q >= 5 clause is the regular-tree contrast, or keep it open.
- **Has an agent solved a full original-list problem?** It has solved the part the catalog calls open:
  q = 3, 4 for every degree and every finite-mean GW law. This holds conditionally on the q4 traversal
  replay for "independently checked", and it is computer-assisted. The q >= 5 clause, under its strongest
  reading, is not solved.
- Not assessed here: novelty against the literature beyond the scope check's own audit, external peer
  acceptance, and the registry count. Nothing here changes them.
