# C0044 referee packet (working)

## w582-C0044-L1: KEEP, scoped

I independently rederived the Markov conditional identity and the martingale limit. The uniform positive floor on q is an explicit extra assumption. The proof establishes the fixed-environment implication only; it says nothing yet about whether iid elliptic environments supply that floor. Exact source and current openness are still being checked.

## w583.C0044.001: KEEP, scoped

I rederived the embedded first-coordinate birth-death chain. Its outward/inward step probabilities are p/c and q/c with p>q; return from either +1 or -1 has probability r=q/p. Returns to zero are geometric and the final excursion diverges. Symmetry and the hitting probability r^|k| give the displayed h(k). The level-zero e1 probabilities c/2 exceed kappa for kappa<1/(2d). Hence the environment is uniformly elliptic and has directional escape probability strictly between zero and one at every site, with zero infimum over all sites. It is deterministic and spatially layered, so it lies outside the iid target.

## Source and current status

Drewitz--Ramirez, arXiv:1309.2589v1, Open question 3.2, asks for the annealed directional zero-one law under strict ellipticity (E) and iid transition rows (IID). The target uses each fixed direction; d=1,2 were cited as known. OpenAI released a 2026-09-23 manuscript claiming this exact d>=3 law. Its linked Lean comparator ends in `by sorry`, which is a statement placeholder and not itself proof verification. See SOURCE_STATUS.json. Current openness stays UNKNOWN pending an audit of the actual manuscript and proof artifact.

NEXT: verify the actual 2026 proof and its formal receipt, then inspect peers' next claims.
