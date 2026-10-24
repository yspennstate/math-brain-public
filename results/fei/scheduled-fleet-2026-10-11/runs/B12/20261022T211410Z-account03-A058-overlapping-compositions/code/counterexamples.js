
function pop(n){let r=0;for(;n;n>>>=1)r+=n&1;return r}
function walsh(t){let a=t.slice();for(let d=1;d<a.length;d*=2)for(let i=0;i<a.length;i+=2*d)for(let j=0;j<d;j++){const x=a[i+j],y=a[i+j+d];a[i+j]=x+y;a[i+j+d]=x-y}return a}
function add(m,k,v){m[k]=(m[k]||0)+v;if(!m[k])delete m[k]}
function entropy(a,n){const m={unit:2*n*(2**(2*n))};for(let x of a){let q=Math.abs(x),w=x*x;if(q<2)continue;for(let p=2;p*p<=q;p++){let v=0;while(q%p===0){q/=p;v++}if(v)add(m,p===2?'unit':String(p),-2*w*v)}if(q>1)add(m,q===2?'unit':String(q),-2*w)}return m}
function inf(a,mask){return a.reduce((v,x,i)=>v+((i&mask)?x*x:0),0)}
function total(a){return a.reduce((v,x,i)=>v+pop(i)*x*x,0)}
function verify(s,p){const slices=2**(2**p),pairs=[];for(let a=0;a<slices;a++)for(let b=0;b<slices;b++)if(pop(a)===pop(b))pairs.push([a,b]);const count=pairs.length**(2**s),n=s+2*p+1,N=2**n,D=N*N;let assertions=0,boundaries=0;for(let c=0;c<count;c++){let q=c,cs=[];for(let j=0;j<2**s;j++){cs.push(pairs[q%pairs.length]);q=Math.floor(q/pairs.length)}let g=[],h=[],f=[];for(let x=0;x<N;x++){const si=(x>>>(2*p))&((1<<s)-1),xi=x&((1<<p)-1),yi=(x>>>p)&((1<<p)-1);g[x]=((cs[si][0]>>>xi)&1)?1:-1;h[x]=((cs[si][1]>>>yi)&1)?1:-1;f[x]=(x&(1<<(n-1)))?h[x]:g[x]}const ga=walsh(g),ha=walsh(h),fa=walsh(f),M=entropy(fa,n);for(const k of Object.keys(M))M[k]*=2;for(const a of [ga,ha]){const E=entropy(a,n);for(const [k,v]of Object.entries(E))add(M,k,-v)}const iz=inf(fa,1<<(n-1));add(M,'unit',-8*iz);if(Object.keys(M).length)throw Error('entropy failure '+s+','+p+','+c+':'+JSON.stringify(M));assertions++;if(2*total(fa)-total(ga)-total(ha)-2*iz!==0)throw Error('influence');assertions++;let common=0;for(let i=0;i<N;i++)if(!(i&((1<<(2*p))-1))&&!(i&(1<<(n-1)))){if(ga[i]!==ha[i])throw Error('mean');common+=ga[i]*ga[i]}if(2*iz+common!==D)throw Error('selector');assertions++;if(!iz)boundaries++}return {shared:s,private_each:p,cases:count,assertions,zero_selector_cases:boundaries}}

const checks=[];
for(const label of['global_bias_only','private_block_reused']){
const n=2,N=4,g=[1,-1,1,-1],h=g.map(x=>-x),f=g.map((x,i)=>(i&2)?h[i]:x),ga=walsh(g),ha=walsh(h),fa=walsh(f);
const iz=inf(fa,2),E=sumMapCounter(entropy(fa,n),entropy(ga,n),entropy(ha,n));add(E,'unit',-8*iz);
if(Object.keys(entropy(ga,n)).length||Object.keys(entropy(ha,n)).length||Object.keys(entropy(fa,n)).length||iz!==16||E.unit!==-128)throw Error('control failure');
checks.push({label,entropy_increment:0,selector_influence:1,claimed_increment_without_hypothesis:4,exact_counterexample:true});}
function sumMapCounter(f,g,h){const m={};for(const[k,v]of Object.entries(f))add(m,k,2*v);for(const a of[g,h])for(const[k,v]of Object.entries(a))add(m,k,-v);return m}
console.log(JSON.stringify(checks,null,2));
