// Complete-graph minimum 1-tree Lagrangian lower bound, integer costs.
#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;
int main(){
    int n,iters;double upper;if(!(cin>>n>>iters>>upper)||n<3||n>10000)return 2;
    vector<long double>x(n),y(n);for(int i=0;i<n;i++)cin>>x[i]>>y[i];
    constexpr int64_t scale=100000000;
    // Downward rounding, with a further one-unit margin for floating evaluation.
    vector<int32_t>w(size_t(n)*n);
    for(int i=0;i<n;i++)for(int j=0;j<i;j++){
        long double a=abs(x[i]-x[j]),b=abs(y[i]-y[j]);a=min(a,1-a);b=min(b,1-b);
        int32_t z=max<int64_t>(0,int64_t(floor(sqrt(a*a+b*b)*scale))-1);
        w[size_t(i)*n+j]=w[size_t(j)*n+i]=z;
    }
    vector<int64_t>p(n),key(n);vector<int>degree(n),parent(n);vector<char>used(n);
    int64_t best=numeric_limits<int64_t>::min();double alpha=1.6;int stale=0,done=0;
    auto begin=chrono::steady_clock::now();
    for(int iter=0;iter<iters;iter++){
        fill(used.begin(),used.end(),0);used[0]=1;fill(degree.begin(),degree.end(),0);
        fill(key.begin(),key.end(),numeric_limits<int64_t>::max()/4);
        fill(parent.begin(),parent.end(),-1);key[1]=0;int64_t total=0;
        for(int z=1;z<n;z++){
            int u=-1;for(int v=1;v<n;v++)if(!used[v]&&(u<0||key[v]<key[u]))u=v;
            used[u]=1;total+=key[u];
            if(parent[u]>=0){degree[u]++;degree[parent[u]]++;}
            const int32_t* row=&w[size_t(u)*n];
            for(int v=1;v<n;v++)if(!used[v]){
                int64_t cost=int64_t(row[v])+p[u]+p[v];
                if(cost<key[v]){key[v]=cost;parent[v]=u;}
            }
        }
        int a=-1,b=-1;
        for(int v=1;v<n;v++){
            int64_t cost=int64_t(w[v])+p[0]+p[v];
            if(a<0||cost<int64_t(w[a])+p[0]+p[a]){b=a;a=v;}
            else if(b<0||cost<int64_t(w[b])+p[0]+p[b])b=v;
        }
        total+=int64_t(w[a])+int64_t(w[b])+2*p[0]+p[a]+p[b];
        degree[0]=2;degree[a]++;degree[b]++;
        int64_t norm=0;int degree_sum=0;
        for(int v=0;v<n;v++){total-=2*p[v];int g=degree[v]-2;norm+=g*g;degree_sum+=degree[v];}
        if(degree_sum!=2*n)return 3;
        if(total>best){best=total;stale=0;}else stale++;
        done=iter+1;if(norm==0)break;
        if(stale>=25){alpha*=0.7;stale=0;}
        int64_t step=max<int64_t>(1,int64_t(alpha*max(0.0,upper*scale-double(total))/norm));
        for(int v=0;v<n;v++)p[v]+=step*(degree[v]-2);
    }
    double seconds=chrono::duration<double>(chrono::steady_clock::now()-begin).count();
    cout<<setprecision(17)<<"{\"lower_bound\":"<<double(best)/scale
        <<",\"iterations\":"<<done<<",\"seconds\":"<<seconds
        <<",\"distance_scale\":"<<scale<<",\"matrix_bytes\":"<<w.size()*sizeof(int32_t)<<"}\n";
}
