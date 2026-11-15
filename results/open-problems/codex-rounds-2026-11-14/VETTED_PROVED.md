# Codex PROVED pieces: vetting record (an agent)

T054 (14 Nov, outline read): sound as far as read; the concentration step is Bernstein for sampling without replacement. Elementary; no novelty.

T059 (14 Nov 20:0x JST): VERDICT PROVED a finite-horizon quadratic continuation-error certificate for Robbins' problem: regret <= sum_{r>=2} e_r^2/a_r (a_2=2, a_r=r-1), plus an oracle rounding corollary A_n/M^2 (31/40000 at n=5, M=100). verify_certificate.py re-run fresh on mini1 in /tmp/vc_T059: rc 0, all_checks_passed True, penultimate_audit.csv byte-identical to Codex's. Scope: a reduction tool, not an improvement of the bounds on V or V_5; the report says so. Proof text (coupling and monotonicity steps) not yet read line by line. Keep as a lemma for T059 work; not a row change.

T065 (14 Nov 20:0x JST): VERDICT PROVED that for V(r)=r^2/2+r^4/4 every conserved two-site polynomial density of degree <= 6 is stretch, momentum, energy or a constant, modulo telescoping, for every ring N>=5. verify_certificate.py re-run fresh on mini1: rc 0, PASS; rank 179, kernel 31, 27 telescoping, 4 charges; determinants mod 1000003 / 1000033 as reported. Check still owed by hand: the step from the finite N=5..8 computation to every N>=5 (PROOF.md). Bounded non-integrability evidence, no novelty claimed; not a row change.

Still to vet: T055 T057 T072 T091 OP14_T223.

## 14 Nov 20:1x JST: the remaining five (report-level read; none settles its row, none claims novelty)

T055: PROVED an exponential obstruction to reweighting trees into site animals shape by shape using only size and contacts. A no-go lemma with exact finite data; no script left. No row change.
T057: PROVED a reduction of rational walks to equal-degree Cayley walks on finite cyclic extensions. A reduction only; novelty disclaimed; no script. No row change.
T072: PROVED an explicit finite-n bound and the sharp leading degree cutoff for the planted-clique low-degree likelihood-ratio norm. A restricted-model theorem inside the established low-degree literature; the planted clique conjecture stays open. No row change.
T091: PROVED an exact deterministic reduction for spatially constant additive noise. Elementary, and it excludes the mean-zero case the row asks for. The report cites F. Brandt and I. Kukavica, Regularizing the Navier-Stokes Equations by One Noise Component, arXiv:2611.02557 (authors and title checked on arXiv 14 Nov); that paper should be read before T091 is next worked on. No row change yet.
OP14_T223 (laptop run): PROVED exponential risk and W2 convergence for the one-dimensional strict-cone initialization case. verify.py re-run in a scratch copy: rc 0 after removing one environment assert (process priority class), output identical to Codex's apart from time and memory lines (max root residual 1.78e-15, coupling-bound excess 0). A special case; novelty among known 1D cases not claimed. No row change.

Summary of the eight PROVED pieces: all are bounded lemmas, reductions or special cases; the three with checkers (T059 T065 T223) reproduce; none changes a top-200 row. Owed by hand: the T065 step from N=5..8 to every N>=5, and line-by-line reading of the T059 and T223 proofs before any paper.
