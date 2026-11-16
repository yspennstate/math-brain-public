# An improved lower bound for the card-cyclic-to-random shuffle

Yitzchak Shmalo, 16 November 2026.

Archived on Zenodo: [doi:10.5281/zenodo.24275698](https://doi.org/10.5281/zenodo.24275698).

In the card-cyclic-to-random shuffle of n cards, the cards labelled 1, ..., n are removed in turn, cyclically, and each is reinserted at a uniformly random position. Morris, Ning and Peres (Ann. Appl. Probab. 24, 2014; arXiv:1207.3406) proved that the mixing time is of order n log n, with a lower bound of c n log n for every c < 1/(2+2a), where -a+ib is a root of e^{-z} = 1-z and a is about 2.089. The paper raises the lower constant from about 0.162 to 1/(2a), about 0.239. On functions of the relative order of pairs of cards the chain acts as the exterior square of an explicit n by n matrix; two eigenvectors of that matrix give an exact eigenfunction of the chain, with eigenvalue of modulus 1 - a/n + O(n^{-2}), and a second-moment argument finishes the proof. Whether the shuffle has cutoff remains open.

## Files

- `main.tex`, `main.pdf`: the paper.
- `CREDITS.md`: which statements are known and which are new, and whose work they rest on.
- `checks/check_shuffle.py`: checks Proposition 2.2 on every deck for n = 3..6 in exact arithmetic, checks that the function of Section 3 is an eigenfunction of the chain on every deck for n = 5, 6, 7, computes the constants a, b and z and the asymptotics of Section 3 up to n = 400, and computes the exact small-deck values of Section 5. Needs Python 3 and mpmath; runs in a few minutes. Its output is in `checks/output.txt`.

## License

The paper is licensed CC BY 4.0 and the code MIT.
