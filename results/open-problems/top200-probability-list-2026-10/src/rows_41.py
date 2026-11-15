# Famous-list addition, 15 Nov 2026 (an agent), candidate G09 from
# 06_math_research/top200_vet_agent_2026_11_11/FAMOUS_LITCHECK_1114.md; sources read from Crossref, Springer and the
# arXiv text of Zhang and Torquato on 15 Nov 2026.
ROWS = [
 {'id': 'T474',
  'd': 'GEOM',
  't': 'The jamming limit of random sequential adsorption of disks',
  's': 'Place unit disks one at a time in a large square, each centred uniformly at random among the positions where '
       'it overlaps none of the earlier disks, until no position is left. The covered fraction converges, as the '
       'square grows, to a constant theta_2 (Penrose 2001). Determine theta_2, or prove rigorous bounds on it close '
       'to the simulated value; the same question stands for balls in every dimension d >= 2.',
  'c': 'In one dimension this is Renyi\'s car-parking problem, solved exactly in 1958: theta_1 = 0.7475979202... is '
       'given by an explicit integral. For d >= 2 the saturation density "has only been estimated through numerical '
       'simulations" (Zhang and Torquato 2013, whose algorithm produces packings with no space left and gives '
       'theta_2 = 0.5470735 +- 0.0000028; earlier estimates were 0.547 +- 0.002, 0.547 +- 0.003 and 0.54700 +- '
       '0.000063). Penrose proved that the limit exists, through spatial laws of large numbers for random and '
       'cooperative sequential adsorption. T473 is another planar constant known to many digits by computation and '
       'to nothing like that rigorously.',
  'src': 'M. D. Penrose, Random parking, sequential adsorption, and the jamming limit, Comm. Math. Phys. 218 (2001), '
         '153-176, doi:10.1007/s002200100387. G. Zhang and S. Torquato, Precise algorithm to generate random '
         'sequential addition of hard hyperspheres at saturation, Phys. Rev. E 88 (2013), 053312, '
         'doi:10.1103/PhysRevE.88.053312, arXiv:1402.4883. A. Renyi, On a one-dimensional problem concerning random '
         'space filling, 1958 (cited by Zhang and Torquato for theta_1; not read here).',
  'loc': 'Zhang and Torquato, arXiv:1402.4883, Section I (read 15 Nov 2026): the one-dimensional case "has been solved '
         'analytically", while for d >= 2 the density "has only been estimated through numerical simulations"; Table '
         'II gives 0.5470735 +- 0.0000028 for d = 2. Penrose, abstract on the Springer page: there was "no complete '
         'proof that such a limit exists, until now".',
  'url': 'https://doi.org/10.1007/s002200100387',
  'why': 'Random sequential adsorption is the basic model of irreversible deposition (proteins and colloids on '
         'surfaces, the parking problem), and the jamming constant is its central number. The one-dimensional answer '
         'is a classical piece of probability; in two dimensions the long-range dependence of the final packing '
         'defeats the same recursion, and no rigorous method gives more than crude bounds.',
  'st': 'Open: Zhang and Torquato (2013) state that for d >= 2 the density is known only from simulation. Later '
        'rigorous work on the model (limit theorems for the packing) has not been checked here for bounds on '
        'theta_2; read the papers citing Penrose (2001) before quoting a rigorous interval.',
  'n': 'Added 15 Nov 2026 by an agent from famous candidate G09, after the Crossref, Springer and arXiv check. '
       'New row; it takes one of the famous places freed by the retirements.'},
]
