"""arXiv check, newest first, for a batch of general-list rows.  usage: general_lit4.py <out file> <first> <last>
Each query asks for the conjecture by name together with a word of resolution, so a hit list is short enough to read."""
import re, sys, time, urllib.parse, urllib.request

R = '(abs:proof OR abs:prove OR abs:proved OR abs:resolve OR abs:resolving OR abs:counterexample OR abs:disprove OR abs:settle)'
Q = [
 ("CO01 Hadwiger", 'abs:"Hadwiger\'s conjecture" AND abs:minor AND ' + R),
 ("CO02 reconstruction", 'abs:"reconstruction conjecture" AND abs:graph AND ' + R),
 ("CO04 list colouring", '(abs:"list colouring conjecture" OR abs:"list coloring conjecture") AND ' + R),
 ("CO05 total colouring", '(abs:"total colouring conjecture" OR abs:"total coloring conjecture") AND ' + R),
 ("CO06 cycle double cover", 'abs:"cycle double cover conjecture" AND ' + R),
 ("CO07 5-flow", 'abs:"5-flow conjecture" AND ' + R),
 ("CO09 sunflower", 'abs:"sunflower conjecture" AND ' + R),
 ("CO10 Caccetta-Haggkvist", '(abs:"Caccetta-Haggkvist" OR abs:"Caccetta-Häggkvist") AND ' + R),
 ("CO11 Turan hypergraph", 'abs:"Turán" AND abs:tetrahedron AND abs:"3-graph" AND abs:conjecture'),
 ("CO13 chromatic number of the plane", 'abs:"chromatic number of the plane"'),
 ("GE02 Borsuk", 'abs:"Borsuk" AND abs:partition AND abs:diameter AND (abs:dimension OR abs:counterexample)'),
 ("GE03 Hadwiger covering", '(abs:"Hadwiger covering" OR abs:"illumination conjecture" OR abs:"Levi-Hadwiger") AND ' + R),
 ("GE04 polynomial Hirsch", 'abs:"polynomial Hirsch conjecture"'),
 ("GE05 Kneser-Poulsen", 'abs:"Kneser-Poulsen"'),
 ("GE06 inscribed square", '(abs:"inscribed square" OR abs:"square peg") AND (abs:Jordan OR abs:Toeplitz)'),
 ("AN06 Brennan", 'abs:"Brennan\'s conjecture"'),
 ("AN09 Fuglede", 'abs:"Fuglede\'s conjecture" AND (abs:"dimension one" OR abs:"dimension 1" OR abs:"dimension two" OR abs:"dimensions 1" OR abs:"on the line" OR abs:"R^2")'),
 ("AN11 Zygmund", 'abs:Zygmund AND abs:conjecture AND abs:Lipschitz AND abs:"vector field"'),
 ("AN13 Koebe", '(abs:"Koebe conjecture" OR abs:"Koebe\'s conjecture" OR abs:"Kreisnormierung") AND abs:"circle domain"'),
 ("AN14 triangular Hilbert", 'abs:"triangular Hilbert transform"'),
 ("DY05 triangle billiards", 'abs:billiard AND abs:"periodic" AND abs:triangle AND (abs:obtuse OR abs:"every triangle")'),
 ("DY04 Birkhoff", 'abs:"Birkhoff conjecture" AND abs:billiard'),
 ("DY07 Pisot", 'abs:"Pisot" AND abs:"substitution" AND abs:conjecture AND ' + R),
 ("DG08 Cartan-Hadamard", 'abs:"Cartan-Hadamard conjecture"'),
 ("DG04 Chern affine", 'abs:"Chern" AND abs:conjecture AND abs:"affine manifold"'),
 ("DG05 six-sphere", 'abs:"complex structure" AND (abs:"six-sphere" OR abs:"S^6" OR abs:"6-sphere") AND ' + R),
 ("TO10 cabling", 'abs:"cabling conjecture"'),
 ("TO02 slice-ribbon", 'abs:"slice-ribbon conjecture" AND (abs:counterexample OR abs:disprove OR abs:proof)'),
 ("AL03 Koethe", '(abs:"Koethe conjecture" OR abs:"Köthe conjecture" OR abs:"Kothe conjecture")'),
 ("AL04 zero-divisor", 'abs:"zero divisor conjecture" AND (abs:counterexample OR abs:Kaplansky)'),
 ("AL05 Burnside B(2,5)", 'abs:"Burnside" AND (abs:"B(2,5)" OR abs:"exponent 5" OR abs:"exponent five")'),
 ("AL06 Andrews-Curtis", 'abs:"Andrews-Curtis conjecture"'),
 ("PD09 De Giorgi", 'abs:"De Giorgi" AND abs:conjecture AND abs:"Allen-Cahn" AND (abs:"dimension" ) AND ' + R),
 ("IT01 MDS", 'abs:"MDS conjecture"'),
 ("OA04 Zauner", '(abs:"Zauner\'s conjecture" OR abs:"SIC-POVM") AND (abs:existence OR abs:"all dimensions" OR abs:"every dimension")'),
 ("CS10 log-rank", 'abs:"log-rank conjecture"'),
 ("NT26 Zaremba", 'abs:"Zaremba\'s conjecture"'),
 ("NT16 Lehmer", '(abs:"Lehmer\'s conjecture" OR abs:"Lehmer\'s problem") AND abs:"Mahler measure"'),
 ("NT15 Littlewood", 'abs:"Littlewood conjecture" AND abs:Diophantine'),
 ("NT17 Artin primitive root", 'abs:"Artin\'s primitive root conjecture" AND (abs:unconditional OR abs:"without" OR abs:proof)'),
]
out_path, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
out = open(out_path, "w", encoding="utf-8", newline="")
for k, q in Q[a:b]:
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "sortBy": "submittedDate", "sortOrder": "descending", "max_results": 6})
    s = ""
    for attempt in range(3):
        try:
            s = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "research-client/1.0"}), timeout=45).read().decode("utf-8")
            if "totalResults" in s:
                break
        except Exception as e:
            print(k, "attempt", attempt, "failed:", str(e)[:80], file=out)
        time.sleep(8)
    m = re.search(r"totalResults[^>]*>(\d+)<", s)
    print("==", k, "| total", m.group(1) if m else "?", file=out)
    for e in s.split("<entry>")[1:]:
        i = re.search(r"<id>(.*?)</id>", e, re.S).group(1).split("/abs/")[-1]
        t = " ".join(re.search(r"<title>(.*?)</title>", e, re.S).group(1).split())
        au = ", ".join(re.findall(r"<name>(.*?)</name>", e))[:70]
        ab = " ".join(re.search(r"<summary>(.*?)</summary>", e, re.S).group(1).split())
        print(i, "|", t[:130], "|", au, "\n     ", ab[:900], file=out)
    out.flush()
    time.sleep(4)
out.close()
print("queries", a, "to", min(b, len(Q)), "of", len(Q))
