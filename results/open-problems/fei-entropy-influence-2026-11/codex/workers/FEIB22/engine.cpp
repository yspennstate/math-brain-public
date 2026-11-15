#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <numeric>
#include <random>
#include <vector>
using namespace std;

struct Hex {
 int L,n; vector<vector<int>> adj;
 Hex(int l):L(l),n(l*l),adj(n+2) {
  int dr[]={0,0,1,-1,1,-1}, dc[]={1,-1,0,0,-1,1};
  for(int r=0;r<L;r++)for(int c=0;c<L;c++) {
   int v=r*L+c;
   for(int t=0;t<6;t++){int a=r+dr[t],b=c+dc[t];if(a>=0&&a<L&&b>=0&&b<L)adj[v].push_back(a*L+b);}
   if(c==0){adj[v].push_back(n);adj[n].push_back(v);}
   if(c==L-1){adj[v].push_back(n+1);adj[n+1].push_back(v);}
  }
 }
 bool eval(const uint8_t* x) const {
  vector<uint8_t> seen(n+2);vector<int> q(n+2);int a=0,b=1;q[0]=n;seen[n]=1;
  while(a<b){int v=q[a++];for(int u:adj[v])if(!seen[u]&&(u>=n||x[u])){if(u==n+1)return true;seen[u]=1;q[b++]=u;}}
  return false;
 }
 // All pointwise monotone derivatives. In a losing configuration a closed
 // site must join the left and right open clusters. In a winning one an open
 // pivotal site is an articulation separating the two boundary terminals.
 bool piv(const uint8_t* x, int16_t* p) const {
  fill(p,p+n,0);vector<int> dis(n+2,0),low(n+2),par(n+2,-1),iter(n+2),stack;
  int timer=1; dis[n]=low[n]=1;stack.push_back(n);
  while(!stack.empty()){
   int v=stack.back();
   if(iter[v]==(int)adj[v].size()) {stack.pop_back();if(par[v]>=0)low[par[v]]=min(low[par[v]],low[v]);continue;}
   int u=adj[v][iter[v]++];if(u<n&&!x[u])continue;
   if(!dis[u]){par[u]=v;dis[u]=low[u]=++timer;stack.push_back(u);}
   else if(u!=par[v])low[v]=min(low[v],dis[u]);
  }
  bool win=dis[n+1]!=0;
  if(win){int u=n+1;while(par[u]>=0){int v=par[u];if(v<n&&low[u]>=dis[v])p[v]=1;u=v;}}
  else {
   vector<uint8_t> right(n+2);vector<int> q(n+2);int a=0,b=1;q[0]=n+1;right[n+1]=1;
   while(a<b){int v=q[a++];for(int u:adj[v])if(!right[u]&&(u>=n||x[u])){right[u]=1;q[b++]=u;}}
   for(int k=0;k<n;k++)if(!x[k]){bool l=false,r=false;for(int v:adj[k]){l|=dis[v]!=0;r|=right[v]!=0;}p[k]=l&&r;}
  }
  return win;
 }
};

static void fwht(double* a,size_t N){
 for(size_t h=1;h<N;h*=2)for(size_t s=0;s<N;s+=2*h)for(size_t j=s;j<s+h;j++){double x=a[j],y=a[j+h];a[j]=x+y;a[j+h]=x-y;}
 for(size_t j=0;j<N;j++)a[j]/=N;
}
static bool small_eval(int L,uint64_t x){
 uint64_t left=0,right=0,valid=(uint64_t(1)<<(L*L))-1;
 for(int r=0;r<L;r++){left|=uint64_t(1)<<(r*L);right|=uint64_t(1)<<(r*L+L-1);}
 uint64_t z=x&left;
 while(!(z&right)){
  uint64_t y=z|((z<<1)&~left)|((z>>1)&~right)|(z<<L)|(z>>L)|((z<<(L-1))&~right)|((z>>(L-1))&~left);
  y&=x&valid;if(y==z)return false;z=y;
 }
 return true;
}
static double phi(double p,double q){
 if(p<=0||q<=0)return 0;
 return p*log2(1+q/p)+q*log2(1+p/q);
}

extern "C" {
void spectrum(int L,double* a){size_t N=size_t(1)<<(L*L);for(size_t s=0;s<N;s++)a[s]=small_eval(L,s)?1:-1;fwht(a,N);for(size_t s=0;s<N;s++)a[s]*=a[s];}
void transform(double* a,int m){fwht(a,size_t(1)<<m);}
int check_piv(int L,int count,uint64_t seed){
 Hex f(L);mt19937_64 rng(seed);vector<uint8_t>x(f.n);vector<int16_t>p(f.n);int bad=0;
 for(int b=0;b<count;b++){for(auto &v:x)v=rng()&1;bool w=f.piv(x.data(),p.data());bad+=w!=f.eval(x.data());for(int k=0;k<f.n;k++){x[k]^=1;bool q=f.eval(x.data());x[k]^=1;bad+=(w!=q)!=bool(p[k]);}}
 return bad;
}

// zeta-transform masses for T excluding coordinate i, then shortest paths.
// last2=1 also minimises the first-two-elements statistic over every order.
void optimal(const double* mu,int n,int i,int last2,double* out,int* ord1,int* ord2){
 int m=n-1,N=1<<m,full=N-1;vector<double>a(N),b(N),d(N),e;
 for(int t=0;t<N;t++){int s=(t&((1<<i)-1))|((t>>i)<<(i+1));a[t]=mu[s];b[t]=mu[s|(1<<i)];}
 for(int k=0;k<m;k++)for(int s=0;s<N;s++)if(s&(1<<k)){a[s]+=a[s^(1<<k)];b[s]+=b[s^(1<<k)];}
 double delta=b[full];vector<uint8_t>pick1(N),pick2;if(last2){e.resize(N);pick2.resize(N);}
 d[0]=phi(a[0],b[0]);
 // Last-two singleton cells do not depend on order; all pairs are charged
 // when their second element is selected, using subset-zeta differences.
 if(last2){e[0]=phi(a[0],b[0]);for(int k=0;k<m;k++)e[0]+=phi(a[1<<k]-a[0],b[1<<k]-b[0]);}
 for(int R=1;R<N;R++){
  double best=1e100,best2=1e100;
  for(int bits=R;bits;bits&=bits-1){int k=__builtin_ctz((unsigned)bits),Q=R^(1<<k);
   double val=d[Q]+phi(a[R]-a[Q],b[R]-b[Q]);if(val<best){best=val;pick1[R]=k;}
   if(last2){
    // Reverse chain: k is the earliest of the final remaining R. Prior
    // second hits lie in Q; forbid Q except the selected second hit l.
    int rest=full^R;double cost=0;
    for(int bs=Q;bs;bs&=bs-1){int l=__builtin_ctz((unsigned)bs),A=rest|(1<<k)|(1<<l);
     cost+=phi(a[A]-a[A^(1<<k)]-a[A^(1<<l)]+a[rest],b[A]-b[A^(1<<k)]-b[A^(1<<l)]+b[rest]);
    }
    val=e[Q]+cost;if(val<best2){best2=val;pick2[R]=k;}
   }
  }
  d[R]=best;if(last2)e[R]=best2;
 }
 out[0]=delta;out[1]=d[full]/delta;out[2]=last2?e[full]/delta:-1;
 int R=full;for(int t=0;t<m;t++){int k=pick1[R];ord1[t]=k<i?k:k+1;R^=1<<k;}
 if(last2){R=full;for(int t=0;t<m;t++){int k=pick2[R];ord2[m-1-t]=k<i?k:k+1;R^=1<<k;}}
}

// Averages over outside configurations of the exact restricted spectra.
// Accumulated independently in G groups, kept in RAM by the Python caller.
void blocks(int L,int i,const int* vars,int m,int G,int each,uint64_t seed,double* acc){
 Hex f(L);int n=f.n,N=1<<m;mt19937_64 rng(seed);vector<int>slot(n,-1);for(int j=0;j<m;j++)slot[vars[j]]=j;
 vector<uint8_t>x(n);vector<int>comp(n),q(n);vector<double>a(N);vector<uint32_t>adj(m),tab0(1024),tab1(1<<max(0,m-10));
 for(int g=0;g<G;g++)for(int it=0;it<each;it++){
  for(int k=0;k<n;k++)x[k]=rng()&1;
  fill(comp.begin(),comp.end(),-1);fill(adj.begin(),adj.end(),0);uint32_t start=0,goal=0;bool constant=false;int cid=0;
  for(int k=0;k<n;k++)if(slot[k]<0&&x[k]&&comp[k]<0){
   int h=0,t=1;q[0]=k;comp[k]=cid;uint32_t touch=0;bool left=false,right=false;
   while(h<t){int v=q[h++];for(int u:f.adj[v]){if(u==n)left=true;else if(u==n+1)right=true;else if(slot[u]>=0)touch|=1u<<slot[u];else if(x[u]&&comp[u]<0){comp[u]=cid;q[t++]=u;}}}
   if(left&&right)constant=true;if(left)start|=touch;if(right)goal|=touch;
   for(uint32_t bs=touch;bs;bs&=bs-1)adj[__builtin_ctz(bs)]|=touch;cid++;
  }
  for(int j=0;j<m;j++)for(int u:f.adj[vars[j]]){if(u==n)start|=1u<<j;else if(u==n+1)goal|=1u<<j;else if(slot[u]>=0)adj[j]|=1u<<slot[u];}
  double* dst=acc+(size_t)g*N;
  if(constant){dst[0]+=1;continue;}
  tab0[0]=0;for(int s=1;s<1024;s++){int k=__builtin_ctz((unsigned)s);tab0[s]=tab0[s&(s-1)]|(k<m?adj[k]:0);}
  tab1[0]=0;for(int s=1;s<(int)tab1.size();s++){int k=__builtin_ctz((unsigned)s)+10;tab1[s]=tab1[s&(s-1)]|adj[k];}
  if(!start||!goal){dst[0]+=1;continue;}
  for(int s=0;s<N;s++){
   uint32_t z=s&start;bool win=false;
   while(z){if(z&goal){win=true;break;}uint32_t r=z|((tab0[z&1023]|tab1[z>>10])&s);if(r==z)break;z=r;}
   a[s]=win?1:-1;
  }
  fwht(a.data(),N);for(int s=0;s<N;s++)dst[s]+=a[s]*a[s];
 }
}

// Each row: delta, mean g, W(1..J), Gcorr(1..J),
// sum_{k in shell a} 4 E[D_k h(x) D_k h(x^R_b)] and the g analogue.
// Prefixes are shells; second-hit shell labels include same-shell ties.
void window(int L,int i,const int* shell,int J,int batches,int each,uint64_t seed,double* out){
 Hex f(L);int n=f.n,stride=2+2*J+2*J*J+2*n;mt19937_64 rng(seed);
 vector<uint8_t>x(n),y(n),z(n);vector<int16_t>p0(n),p1(n),h(n),g(n),hz(n),gz(n);
 auto both=[&](vector<uint8_t>&v,vector<int16_t>&hh,vector<int16_t>&gg,int&hi,int&gi){
  v[i]=0;bool f0=f.piv(v.data(),p0.data());v[i]=1;bool f1=f.piv(v.data(),p1.data());
  hi=int(f1)-int(f0);gi=int(f1)+int(f0)-1;
  for(int k=0;k<n;k++){hh[k]=p1[k]-p0[k];gg[k]=p1[k]+p0[k];}
 };
 for(int b=0;b<batches;b++){
  double*row=out+(size_t)b*stride;
  for(int it=0;it<each;it++){
   for(int k=0;k<n;k++){x[k]=rng()&1;y[k]=rng()&1;}
   int hi,gi;both(x,h,g,hi,gi);row[0]+=hi;row[1]+=gi;z=x;
   for(int k=0;k<n;k++){row[2+2*J+2*J*J+k]+=h[k];row[2+2*J+2*J*J+n+k]+=g[k];}
   for(int s=0;s<J;s++){
    for(int k=0;k<n;k++)if(shell[k]==s)z[k]=y[k];
    int hj,gj;both(z,hz,gz,hj,gj);row[2+s]+=hi*hj;row[2+J+s]+=gi*gj;
    for(int k=0;k<n;k++)if(k!=i){int a=shell[k];row[2+2*J+a*J+s]+=h[k]*hz[k];row[2+2*J+J*J+a*J+s]+=g[k]*gz[k];}
   }
  }
 }
}
}
