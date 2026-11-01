"use strict";

// Agent 107: exact finite examples and structural arithmetic checks.
// Runtime: plain JavaScript, executed with BigInt and a supplied console.
// No numerical LP solver, Python, Node API, or lost Agent074 data is used.

function assert(condition, message) {
  if (!condition) throw new Error(message);
}
function gcd(a, b) {
  a = a < 0n ? -a : a; b = b < 0n ? -b : b;
  while (b) { const t = a % b; a = b; b = t; }
  return a;
}
function Q(a, b = 1n) {
  a = BigInt(a); b = BigInt(b);
  assert(b !== 0n, "zero denominator");
  if (b < 0n) { a = -a; b = -b; }
  const g = gcd(a, b);
  return [a / g, b / g];
}
const Z = Q(0), O = Q(1);
const add = (a,b) => Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg = a => [-a[0],a[1]];
const sub = (a,b) => add(a,neg(b));
const mul = (a,b) => Q(a[0]*b[0],a[1]*b[1]);
const div = (a,b) => Q(a[0]*b[1],a[1]*b[0]);
const eq = (a,b) => a[0]===b[0] && a[1]===b[1];
const sign = a => a[0]<0n ? -1 : a[0]>0n ? 1 : 0;
const sum = a => a.reduce(add,Z);
const sq = a => mul(a,a);
const fmt = a => a[1]===1n ? String(a[0]) : String(a[0])+"/"+String(a[1]);
function pop(s) { let k=0; for (;s;s&=s-1) ++k; return k; }
function masks(n,k) {
  return Array.from({length:1<<n},(_,s)=>s).filter(s=>pop(s)===k);
}
function diamonds(n,r) {
  const result=[];
  for (let s=0;s<(1<<n);++s) {
    if (r!==undefined && pop(s)!==r) continue;
    for(let i=0;i<n;++i) if(!(s&(1<<i)))
      for(let j=i+1;j<n;++j) if(!(s&(1<<j)))
        result.push({s,i,j,a:s|(1<<i),b:s|(1<<j),t:s|(1<<i)|(1<<j)});
  }
  return result;
}
const delta = (f,d) => sub(add(f[d.s],f[d.t]),add(f[d.a],f[d.b]));
const choose2 = k => k*(k-1)/2;
const barrier = (k,r) => Math.max(r-k,0)**2+Math.max(k-r-2,0)**2;
function zeros(n) { return Array.from({length:1<<n},()=>Z); }
function point(n,s) { const a=zeros(n); a[s]=O; return a; }
function contrast(mu0,muu,muv,mu2) {
  return mu0.map((p,s)=>sub(add(p,mu2[s]),add(muu[s],muv[s])));
}
function pairing(b,f) { return sum(b.map((p,s)=>mul(p,f[s]))); }
function checkMoments(n,b) {
  assert(eq(sum(b),Z),"total signed mass");
  for(let i=0;i<n;++i)
    assert(eq(sum(b.filter((_,s)=>s&(1<<i))),Z),"coordinate moment");
}
function determinant(A) {
  if(!A.length) return O;
  const B=A.map(row=>row.slice()); let answer=O;
  for(let k=0;k<B.length;++k) {
    let p=k; while(p<B.length && sign(B[p][k])===0) ++p;
    if(p===B.length) return Z;
    if(p!==k) { [B[p],B[k]]=[B[k],B[p]]; answer=neg(answer); }
    const pivot=B[k][k]; answer=mul(answer,pivot);
    for(let i=k+1;i<B.length;++i) {
      const c=div(B[i][k],pivot);
      for(let j=k+1;j<B.length;++j) B[i][j]=sub(B[i][j],mul(c,B[k][j]));
      B[i][k]=Z;
    }
  }
  return answer;
}
function minor(frame,s,cols) {
  const rows=Array.from({length:frame.length},(_,i)=>i).filter(i=>s&(1<<i));
  assert(rows.length===cols.length,"minor shape");
  return determinant(rows.map(i=>cols.map(j=>frame[i][j])));
}
function atomLaw(frame,cols) {
  const result=zeros(frame.length);
  for(const s of masks(frame.length,cols.length)) result[s]=sq(minor(frame,s,cols));
  return result;
}
function showSet(s,n) {
  return Array.from({length:n},(_,i)=>i+1).filter(i=>s&(1<<(i-1))).join(",");
}
function showTable(table,n,k) {
  return masks(n,k).map(s=>({set:showSet(s,n),probability:fmt(table[s])}));
}

const structural=[];
for(let n=2;n<=8;++n) {
  const ds=diamonds(n);
  const h=Array.from({length:1<<n},(_,s)=>Q(choose2(pop(s))));
  for(const d of ds) assert(eq(delta(h,d),O),"diamond h evaluation");
  let rankChecks=0;
  for(let r=0;r<=n-2;++r) {
    const rho=Array.from({length:1<<n},(_,s)=>Q(barrier(pop(s),r)));
    for(const d of ds) {
      const expected=pop(d.s)===r ? 0 : Math.abs(pop(d.s)-r)===1 ? 1 : 2;
      assert(eq(delta(rho,d),Q(expected)),"barrier second difference");
      ++rankChecks;
    }
  }
  structural.push({n,diamonds:ds.length,barrier_checks:rankChecks});
}

// Example A: aggregate coupling exists but prescribed labels are impossible.
// Rank 0 on four sites, with top equal to {1,2} or {3,4}.
const nA=4;
const mu0A=point(nA,0), muuA=zeros(nA), muvA=zeros(nA), mu2A=zeros(nA);
muuA[1]=Q(1,2); muuA[2]=Q(1,2);
muvA[4]=Q(1,2); muvA[8]=Q(1,2);
mu2A[3]=Q(1,2); mu2A[12]=Q(1,2);
const bA=contrast(mu0A,muuA,muvA,mu2A);
checkMoments(nA,bA);
const xA=[{s:0,i:0,j:1,weight:Q(1,2)},{s:0,i:2,j:3,weight:Q(1,2)}];
const reconstructed=zeros(nA);
for(const x of xA) {
  const t=x.s|(1<<x.i)|(1<<x.j);
  for(const [s,sgn] of [[x.s,1],[t,1],[x.s|(1<<x.i),-1],[x.s|(1<<x.j),-1]])
    reconstructed[s]=add(reconstructed[s],mul(Q(sgn),x.weight));
}
assert(reconstructed.every((p,s)=>eq(p,bA[s])),"Example A primal identity");
const labelMassIn12=add(muuA[1],muuA[2]);
const topTouches12=sum(mu2A.filter((_,s)=>s&3));
assert(sign(sub(labelMassIn12,topTouches12))>0,"Example A labeling obstruction");

// Example B: four graded laws with balanced modular moments but a negative
// global supermodular witness. They do not arise from one compatible frame.
const nB=4,rB=1;
const mu0B=point(nB,1), muuB=point(nB,3), muvB=point(nB,12), mu2B=point(nB,14);
const bB=contrast(mu0B,muuB,muvB,mu2B);
checkMoments(nB,bB);
const fB=Array.from({length:1<<nB},(_,s)=>Q((s&3)===3 ? 1 : 0));
const allB=diamonds(nB),localB=diamonds(nB,rB);
for(const d of allB) assert(sign(delta(fB,d))>=0,"Example B supermodularity");
assert(eq(pairing(bB,fB),Q(-1)),"Example B negative contrast");
// Restrict to three ranks, set other entries to zero, and apply the report's
// explicit extension with A=1, M=4.
const f0B=fB.map((p,s)=>pop(s)>=rB && pop(s)<=rB+2 ? p : Z);
const extendedB=f0B.map((p,s)=>add(p,Q(4*barrier(pop(s),rB))));
for(const d of allB) assert(sign(delta(extendedB,d))>=0,"Example B extension");
assert(eq(pairing(bB,extendedB),Q(-1)),"Example B extension objective");

// Example C: real rational five-site frame. This is a rotation check only.
const nC=5,hC=[1,2,3,4,5],denC=55;
const H=Array.from({length:nC},(_,i)=>Array.from({length:nC},(_,j)=>
  sub(Q(i===j ? 1 : 0),Q(2*hC[i]*hC[j],denC))));
for(let i=0;i<nC;++i) for(let j=0;j<nC;++j)
  assert(eq(sum(H.map(row=>mul(row[i],row[j]))),Q(i===j ? 1 : 0)),"Householder orthogonality");
const mu0C=atomLaw(H,[0,1]),muuC=atomLaw(H,[0,1,2]);
const muvC=atomLaw(H,[0,1,3]),mu2C=atomLaw(H,[0,1,2,3]);
for(const law of [mu0C,muuC,muvC,mu2C]) assert(eq(sum(law),O),"DPP mass");
const bC=contrast(mu0C,muuC,muvC,mu2C);
checkMoments(nC,bC);
const rotated=zeros(nC);
let differingMiddleAtoms=0;
const rotationRows=[];
for(const s of masks(nC,3)) {
  const a=minor(H,s,[0,1,2]),b=minor(H,s,[0,1,3]);
  // The scaled complex amplitudes for u +/- i v are (a,b) and (a,-b).
  // Dividing their squared norms by 2 handles 1/sqrt(2) exactly.
  const plus=div(add(sq(a),sq(b)),Q(2));
  const minus=div(add(sq(a),sq(neg(b))),Q(2));
  const average=div(add(muuC[s],muvC[s]),Q(2));
  assert(eq(plus,minus) && eq(plus,average),"real rotation equalization");
  rotated[s]=plus;
  if(!eq(muuC[s],muvC[s])) ++differingMiddleAtoms;
  rotationRows.push({set:showSet(s,nC),a:fmt(a),b:fmt(b),
    mu_u:fmt(muuC[s]),mu_v:fmt(muvC[s]),each_rotated:fmt(plus)});
}
assert(differingMiddleAtoms>0,"rotation must change this example");
assert(eq(sum(rotated),O),"rotated probability mass");
const bRotated=contrast(mu0C,rotated,rotated,mu2C);
assert(bRotated.every((p,s)=>eq(p,bC[s])),"contrast basis invariance");
// det of [[1,1],[i,-i]]/sqrt(2) is -i, with squared modulus 1.
const scaledTopDet={real:Q(0),imag:Q(-2)};
assert(eq(div(add(sq(scaledTopDet.real),sq(scaledTopDet.imag)),Q(4)),O),
  "top determinant phase has unit modulus");

const output={
  worker:107,
  runtime:"Plain JavaScript in functions; BigInt rational arithmetic; no external solver",
  verdict:"All exact finite checks passed; universal claims are proved analytically in the report",
  structural_checks:structural,
  arbitrary_law_example_A:{
    n:nA,r:0,modular_moments_balanced:true,
    primal_atoms:xA.map(x=>({bottom:"",added:[x.i+1,x.j+1],weight:fmt(x.weight)})),
    prescribed_mu_u_mass_in_12:fmt(labelMassIn12),
    maximum_possible_labeled_mass_in_12:fmt(topTouches12),
    labeled_coupling:"IMPOSSIBLE",
    compatible_dpp_frame:"NOT CLAIMED"
  },
  arbitrary_law_example_B:{
    n:nB,r:rB,modular_moments_balanced:true,
    laws:{bottom:"1",middle_u:"1,2",middle_v:"3,4",top:"2,3,4"},
    witness:"1 when {1,2} is contained in S, otherwise 0",
    global_diamond_inequalities_checked:allB.length,
    local_diamond_inequalities_checked:localB.length,
    contrast:fmt(pairing(bB,fB)),
    extended_local_certificate_contrast:fmt(pairing(bB,extendedB)),
    extension_table:extendedB.map((p,s)=>({set:showSet(s,nB),value:fmt(p)})),
    compatible_dpp_frame:"NO"
  },
  real_rotation_example_C:{
    n:nC,r:2,
    frame:"H_ij=delta_ij-2*i*j/55 for 1<=i,j<=5",
    W_columns:[1,2],u_column:3,v_column:4,
    exact_orthogonality:true,
    bottom_law:showTable(mu0C,nC,2),
    top_law:showTable(mu2C,nC,4),
    middle_atoms:rotationRows,
    differing_original_middle_atoms:differingMiddleAtoms,
    each_rotated_middle_mass:fmt(sum(rotated)),
    exact_contrast_invariance:true,
    proof_of_universal_positivity:"NOT CLAIMED BY THIS EXAMPLE"
  },
  unrecovered_074:{
    original_matrix:"NOT RECOVERED",
    dual_minus_one_fiftieth:"NOT VERIFIED",
    nineteen_atom_coupling:"NOT VERIFIED"
  }
};
console.log(JSON.stringify(output,null,2));
