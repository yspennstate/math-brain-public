VERDICT: PROVED exact optimality of the 2.00636 threshold in an explicitly defined scalar moment relaxation

The new result is a limitation of one route toward long gaps. The earlier session recorded a literature correction and supplied no original proof or computation. [PROOF.md](PROOF.md) now proves that the published long-gap constant cannot be increased using only the first two Poisson factorial moments of the local count, separately at each interval length, together with mean spacing and the full Lipschitz constraint supplied by pair correlation.

The proof solves the scalar moment problem exactly and constructs a nonexponential gap CDF attaining the threshold. Its endpoint G* is the root in (2,109/54) of

35−18G−9G²+(12G−10)sqrt(6G−5)=0.

This is the existing constant in Christoph Aistleitner, Valentin Blomer and Maksym Radziwiłł, *Triple correlation and long gaps in the spectrum of flat tori*, [arXiv:1809.07881](https://arxiv.org/abs/1809.07881), [published online-first text, Corollary 3](https://ems.press/content/serial-article-files/31432). The addition here is an explicit optimality certificate for the stated relaxation, not a larger torus gap bound. No claim of global novelty is made for the elementary moment inequalities or this relaxation calculation.

The earlier main claim was independently checked and holds: Wooyeon Kim, Jens Marklof and Matthew Welsh, [arXiv:2601.03209v2, Theorem 1.1](https://arxiv.org/html/2601.03209v2), prove pair correlation for three-dimensional Dirichlet boxes. The unfolding and symmetry counts were re-derived. The bounded literature check found no solution of the stated two-dimensional problem and finished within five minutes. No SOLVED_ELSEWHERE.md is warranted here.

Validation: the threshold was derived by CDF integration, checked through a quartic polynomial, and checked again by integrating the explicit density. Exact signs give 1603/800<G*<109/54. All moment witnesses, upper constraints and endpoints were checked algebraically. Details and source versions are in [LOG.md](LOG.md).

Commands: web `search_query`, `open` and `find` calls are recorded in LOG.md. Read-only shell commands used `OMP_NUM_THREADS=1 nice -n 15` with `cat` and directory listings. The earlier folder contains neither PROOF.md nor scripts. No numerical script was run: the sandbox denies `nice` priority adjustment. All saved changes used the workspace patch tool; nothing outside this folder was edited.

Failures and uncertainty: optimizing the scalar inequalities yields the existing constant exactly. It cannot improve that constant within this relaxation. The candidate CDF and its separate count laws have not been realized by a common point process or spectrum. The known averaged triple theorem does not assert pointwise triple convergence for an individual torus. The complete Berry–Tabor conjecture remains unresolved. The full proofs of the cited torus theorems were not independently checked. One EMS URL timed out; an alternate publisher PDF opened successfully. Literature searches cannot certify that no other relevant result exists.

Next worker: retain joint count information. For adjacent intervals (0,a] and (a,a+b], impose integer counts A,B with E A=a, E B=b, E[A(A−1)]=a², E[B(B−1)]=b² and E[AB]=ab, together with P(A>0)=F*(a) and P(A+B>0)=F*(a+b). Test whether the explicit extremizer (15) can satisfy these constraints for all a,b. An incompatibility certificate would add information genuinely absent from the scalar relaxation; compatibility would identify the next relation to retain. The averaged theorem's quantifiers must still be handled separately before drawing a torus conclusion.

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 2026-11-15 01:29:06 Asia/Tbilisi; prompt receipt time unavailable.
