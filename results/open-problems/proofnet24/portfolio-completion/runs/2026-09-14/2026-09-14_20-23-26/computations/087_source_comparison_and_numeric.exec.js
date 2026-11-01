const r=load("computations/003_sources/P15.md").structuredContent.content; const s=load("proofnet24/P15-kernel-mean-correction/runs/2026-09-14/2026-09-14_17-30-02__run-report.md").structuredContent.content; text({preservedSourceMatchesActualIgnoringTerminalWhitespace:r.trimEnd()===s.trimEnd(),lengthPreserved:r.length,lengthActual:s.length});
const p99N=97n**99n,p99D=100n**99n,p100N=97n**100n,p100D=100n**100n;
text({exact_p99_below_1_over_20:20n*p99N<p99D, exact_p100_above_1_over_25:25n*p100N>p100D, exact_positive_gate:713n*p99N<40n*p99D,M2:[97n+3n*34n**2n,"100"].map(String),M4:[97n+3n*34n**4n,"100"].map(String)});
const ba2=m=>1/(m*(m-1)), bv2=m=>4/(m*(m-1))+(4*m-1)/(m*m*(m-1)*(m-1)), bA=m=>1+1/m,bV=m=>1+6/m+3/(m*m),n=1000;
const width=(b,m)=>Math.sqrt(40)*(Math.sqrt(b(n))+Math.sqrt((m(n-1)+(n-1)*b(n-1))/n));
const a=width(ba2,bA), v=width(bv2,bV), epA=Math.sqrt(713/40*0.97**99),epV=Math.sqrt(801821/40*0.97**99), theta=(1-epA)/(1+epV);
text({gaussian:{epsilonA:a,epsilonV:v,guaranteedGainProbability:0.95-1/(1000*(1-a)**2)},plugin:{failureProbability:0.97**100,epsilonA:epA,epsilonV:epV,theta,riskIncrease:theta/10+713/20*theta*theta}});