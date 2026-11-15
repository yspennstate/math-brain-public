# Famous-list addition, 15 Nov 2026 (an agent), candidate H18 from
# 06_math_research/top200_vet_agent_2026_11_11/FAMOUS_LITCHECK_1114.md; sources read from Crossref, Springer and arXiv
# on 15 Nov 2026.
ROWS = [
 {'id': 'T473',
  'd': 'PERC',
  't': 'The site percolation threshold of the square lattice',
  's': 'Let p_c be the critical probability for independent site percolation on Z^2 (each vertex open with '
       'probability p, nearest-neighbour adjacency). Determine p_c exactly, or failing that, prove rigorous bounds '
       'that pin it down far more tightly than the present interval.',
  'c': 'Bond percolation on Z^2 and site percolation on the triangular lattice have p_c = 1/2 by self-duality '
       '(Kesten 1980 for the bond case); site percolation on Z^2 is not self-matching and no exact value is known or conjectured. '
       'The numerical value is p_c = 0.59274605079210(2) (Jacobsen 2015, transfer matrices in the periodic '
       'Temperley-Lieb algebra on cylinders up to circumference 21). The rigorous lower bounds go back to Toth '
       '(1985) and van den Berg and Ermakov (1996); the upper bound 0.679492 of Wierman (1995, substitution '
       'method) stood until Wierman and Oberly lowered it to 0.666894 in 2024. T002 asks for the scaling limit at '
       'p_c, and T174 for the threshold of 1-independent bond percolation, another planar threshold known only '
       'through bounds.',
  'src': 'J. van den Berg and A. Ermakov, A new lower bound for the critical probability of site percolation on the '
         'square lattice, Random Structures Algorithms 8 (1996), 199-212, doi:10.1002/(SICI)1098-2418(199605)8:3<199::'
         'AID-RSA4>3.0.CO;2-T. J. C. Wierman, Substitution method critical probability bounds for the square lattice '
         'site percolation model, Combin. Probab. Comput. 4 (1995), 181-188, doi:10.1017/S0963548300001565. J. C. '
         'Wierman and S. P. Oberly, A new upper bound for the site percolation threshold of the square lattice, '
         'Springer Proc. Math. Stat. (2024), 129-138, doi:10.1007/978-3-031-62166-6_9. J. L. Jacobsen, Critical '
         'points of Potts and O(N) models from eigenvalue identities in periodic Temperley-Lieb algebras, J. Phys. A '
         '48 (2015), 454003, arXiv:1507.03027. B. Toth, A lower bound for the critical probability of the square '
         'lattice site percolation, Z. Wahrsch. Verw. Gebiete 69 (1985), 19-22, doi:10.1007/BF00532582.',
  'loc': 'Wierman and Oberly, chapter abstract on the Springer page (read 15 Nov 2026): the upper bound "is reduced '
         'from 0.679492 to 0.666894, providing the first improvement since 1995". Jacobsen, arXiv:1507.03027, '
         'abstract: "p_c = 0.59274605079210(2) for site percolation on the square lattice". The van den Berg-Ermakov '
         'record was read from Crossref (title, journal, pages); its numerical bound was not read from the paper.',
  'url': 'https://doi.org/10.1007/978-3-031-62166-6_9',
  'why': 'It is the most basic threshold in percolation that has no exact value, and the gap between the rigorous '
         'interval (about 0.11 wide) and the fourteen-digit numerical value is a direct measure of how far '
         'rigorous methods lag computation. Substitution and computer-assisted methods are improving again, so '
         'the bounds are a live target.',
  'st': 'Open: no exact value or conjecture is known, and the 2024 upper bound is described by its authors as the '
        'first improvement since 1995. Before quoting a lower bound, read the van den Berg-Ermakov paper and any '
        'later improvement; this row does not give its value.',
  'n': 'Added 15 Nov 2026 by an agent from famous candidate H18, after the Crossref, Springer and arXiv '
       'check. New row; it takes one of the famous places freed by the retirements.'},
]
