#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>
using namespace std;
struct Eval {double mn=1e100,H=0,I=0,EI=0;vector<double> inf,er;};
struct Calc {int n,N,L;vector<double> ph;Calc(int nn):n(nn),N(1<<n),L(N/2+1){if(n<=12){ph.resize(size_t(L)*L);for(int p=0;p<L;p++)for(int q=0;q<L;q++){double a=double(p)*p,b=double(q)*q,z=a+b;ph[size_t(p)*L+q]=((a?-a*log2(a/z):0)+(b?-b*log2(b/z):0))*4/(double(N)*N);}}}
Eval operator()(const vector<int>&a){Eval e;e.inf.resize(n);e.er.resize(n);double norm=double(N)*N;for(int i=0;i<n;i++){double d=0,r=0;for(int s=0;s<N;s++)if(!(s>>i&1)){int p=abs(a[s]),q=abs(a[s|(1<<i)]);d+=double(q)*q;if(ph.size())r+=ph[size_t(p/2)*L+q/2];else{double aa=double(p)*p,bb=double(q)*q,z=aa+bb;r+=((aa?-aa*log2(aa/z):0)+(bb?-bb*log2(bb/z):0))/norm;}}d/=norm;e.inf[i]=d;e.er[i]=r;e.I+=d;e.EI+=r;if(d)e.mn=min(e.mn,r/d);}if(e.I)e.EI/=e.I;else e.mn=-1;return e;}
};
vector<int>wh(vector<int>a){int N=a.size();for(int h=1;h<N;h*=2)for(int x=0;x<N;x+=h*2)for(int j=0;j<h;j++){int p=a[x+j],q=a[x+j+h];a[x+j]=p+q;a[x+j+h]=p-q;}return a;}
int main(){mt19937_64 rng(241110);ofstream out("hill_records.jsonl");out<<setprecision(17);int dims[]={7,8,9,10,11,12,14,16};int restarts[]={100,60,30,20,12,8,4,2};int steps[]={4000,3000,2000,1500,1000,700,400,100};for(int ni=0;ni<8;ni++){int n=dims[ni],N=1<<n;Calc calc(n);double best=-1;long long evaluated=0,accepted=0;for(int rep=0;rep<restarts[ni];rep++){vector<int>f(N,-1);vector<double>w(n);for(auto&v:w)v=.2+(rng()%1000)/1000.;double tot=accumulate(w.begin(),w.end(),0.);double th=tot*(.1+.8*(rng()%1000)/1000.);if(rep%3==0){int width=2+rng()%max(1,n/2-1),terms=2+rng()%(2*n);vector<int>dnf;for(int t=0;t<terms;t++){int mask=0;while(__builtin_popcount((unsigned)mask)<width)mask|=1<<(rng()%n);dnf.push_back(mask);}for(int x=0;x<N;x++)for(int t:dnf)if((x&t)==t)f[x]=1;}else for(int x=0;x<N;x++){double v=0;for(int i=0;i<n;i++)if(x>>i&1)v+=w[i];if(v>=th)f[x]=1;}
auto a=wh(f);auto old=calc(a);for(int step=0;step<steps[ni];step++){int x=-1;for(int tries=0;tries<500;tries++){int y=rng()%N;bool legal=true;for(int i=0;i<n;i++){if(f[y]<0&&!(y>>i&1)&&f[y|(1<<i)]<0)legal=false;if(f[y]>0&&(y>>i&1)&&f[y^(1<<i)]>0)legal=false;}if(legal){x=y;break;}}if(x<0)continue;int change=-2*f[x];vector<int>b(N);for(int s=0;s<N;s++)b[s]=a[s]+((__builtin_parity((unsigned)(s&x)))?-change:change);auto now=calc(b);evaluated++;double temp=.035*pow(.005,double(step)/steps[ni]);double delta=now.mn-old.mn+.03*(now.EI-old.EI);if(now.mn>=0&&(delta>=0||double(rng())/rng.max()<exp(delta/temp))){a.swap(b);f[x]=-f[x];old=now;accepted++;}if(old.mn>best+1e-12){best=old.mn;out<<"{\"n\":"<<n<<",\"minratio\":"<<best<<",\"EI\":"<<old.EI<<",\"I\":"<<old.I<<",\"rep\":"<<rep<<",\"step\":"<<step<<",\"minterms\":[";bool first=true;for(int y=0;y<N;y++)if(f[y]>0){bool minimal=true;for(int i=0;i<n;i++)if((y>>i&1)&&f[y^(1<<i)]>0)minimal=false;if(minimal){if(!first)out<<",";first=false;out<<y;}}out<<"]}"<<endl;}}
}cout<<"n="<<n<<" evaluated="<<evaluated<<" accepted="<<accepted<<" record="<<setprecision(17)<<best<<endl;}}
