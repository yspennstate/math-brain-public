// Finite-range polymer Euler scheme with a linearly interpolated occupation grid.
// One worker; no external numerical libraries or hidden threads.
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
#include <sys/resource.h>

double kernel(const std::string& name, double x) {
    const double r=std::abs(x), sign=(x>0)-(x<0);
    if (name=="zero" || r>=1 || r==0) return 0;
    if (name=="sign") return sign;
    if (name=="spline") {
        const double q=2*r;
        return sign*(q<1 ? 3*(2*q-1.5*q*q) : 1.5*(2-q)*(2-q));
    }
    if (name=="bump") {
        const double z=1-r*r;
        return sign*2*r/(z*z)*std::exp(1-1/z);
    }
    auto bump=[](double z,double a,double b) {
        return z>a && z<b ? 6*(z-a)*(b-z)/std::pow(b-a,3) : 0.;
    };
    if (name=="annular") return sign*bump(r,.5,1.);
    if (name=="two_bump") return sign*(.5*bump(r,.1,.4)+.5*bump(r,.65,1.));
    throw std::runtime_error("unknown kernel "+name);
}

struct Grid {
    double h;
    int half=131072, radius;
    std::vector<double> mass,field,values;
    Grid(const std::string& name,double spacing):h(spacing),radius(int(std::ceil(1/h))+1),
        mass(2*half+1),field(2*half+1),values(2*radius+1) {
        for(int d=-radius;d<=radius;++d) values[d+radius]=kernel(name,d*h);
    }
    std::pair<int,double> locate(double x) const {
        const double q=x/h;
        const int j=int(std::floor(q))+half;
        if(j-radius-2<0 || j+radius+3>=int(mass.size()))
            throw std::runtime_error("occupation grid boundary reached");
        return {j,q-std::floor(q)};
    }
    double force(double x) const {
        auto [j,w]=locate(x);
        return (1-w)*field[j]+w*field[j+1];
    }
    double slope(double x) const {
        auto [j,w]=locate(x);
        return (field[j+1]-field[j])/h;
    }
    double direct_force(double x) const {
        auto [j,w]=locate(x);
        double a=0,b=0;
        for(int d=-radius;d<=radius;++d) {
            a+=values[d+radius]*mass[j-d];
            b+=values[d+radius]*mass[j+1-d];
        }
        return (1-w)*a+w*b;
    }
    void deposit(double x,double dt) {
        auto [j,w]=locate(x);
        mass[j]+=dt*(1-w); mass[j+1]+=dt*w;
        for(int d=-radius;d<=radius+1;++d) {
            double a=d<=radius ? values[d+radius] : 0.;
            double b=d>=-radius+1 ? values[d-1+radius] : 0.;
            field[j+d]+=dt*((1-w)*a+w*b);
        }
    }
    double deposited_mass() const {return std::accumulate(mass.begin(),mass.end(),0.);}
    double pair_kernel(double x,double y) const {
        auto [j,u]=locate(x); auto [k,v]=locate(y);
        auto at=[&](int d){return std::abs(d)<=radius ? values[d+radius] : 0.;};
        return (1-u)*((1-v)*at(j-k)+v*at(j-k-1))
             +u*((1-v)*at(j+1-k)+v*at(j-k));
    }
};

void self_test() {
    double err=0,mirror=0,masserr=0;
    for(const std::string name:{"zero","sign","spline","bump","annular","two_bump"}) {
        Grid g(name,.05),reflected(name,.05);
        std::vector<double> history;
        double x=0,y=0,dt=.01;
        for(int n=0;n<1000;++n) {
            double direct=0;
            for(double z:history) direct+=dt*g.pair_kernel(x,z);
            double a=g.force(x),b=reflected.force(y);
            err=std::max({err,std::abs(a-direct),std::abs(a-g.direct_force(x))});
            mirror=std::max(mirror,std::abs(x+y));
            const double noise=.13*std::sin(n*1.71)+.07*std::cos(n*.413);
            history.push_back(x);
            g.deposit(x,dt);reflected.deposit(y,dt);
            x+=dt*a+noise;y+=dt*b-noise;
        }
        masserr=std::max(masserr,std::abs(g.deposited_mass()-1000*dt));
    }
    std::cout<<std::setprecision(17)<<"direct_force_max_error="<<err
        <<" mirror_max_error="<<mirror<<" mass_max_error="<<masserr<<"\n";
    if(err>1e-9 || mirror>1e-8 || masserr>1e-9) throw std::runtime_error("self test failed");
}

int main(int argc,char** argv) {
    try {
        int priority=getpriority(PRIO_PROCESS,0);
        if(priority<10 && setpriority(PRIO_PROCESS,0,10))
            throw std::runtime_error("cannot set nice 10");
        if(argc==2 && std::string(argv[1])=="--self-test") {self_test();return 0;}
        if(argc!=8) {
            std::cerr<<"usage: polymer OUTPUT DT DX TMAX PATHS BASE_DT SEED_OFFSET\n";return 2;
        }
        const double dt=std::stod(argv[2]),h=std::stod(argv[3]),tmax=std::stod(argv[4]);
        const int paths=std::stoi(argv[5]);
        const double base_dt=std::stod(argv[6]);
        const uint64_t offset=std::stoull(argv[7]);
        const int group=int(std::llround(dt/base_dt));
        const long steps=std::llround(tmax/dt);
        if(group<1 || std::abs(group*base_dt-dt)>1e-10 || std::abs(steps*dt-tmax)>1e-9)
            throw std::runtime_error("incompatible time steps");
        std::ofstream out(argv[1]); if(!out) throw std::runtime_error("cannot open output");
        out<<std::setprecision(17);
        out<<"kernel,seed,dt,dx,t,x,brownian,drift_energy,max_abs_drift,min_x,max_x,force_check_error,mass_check_error,drift_step_over_dx,max_negative_slope_dt\n";
        std::cerr<<"nice="<<getpriority(PRIO_PROCESS,0)<<" one thread, paths="<<paths<<"\n";
        std::vector<std::string> kernels={"zero","sign","spline","bump","annular","two_bump"};
        if(const char* selection=std::getenv("POLYMER_KERNELS")) {
            kernels.clear();std::stringstream input(selection);std::string item;
            while(std::getline(input,item,',')) kernels.push_back(item);
        }
        for(const std::string& name:kernels) {
            for(int path=0;path<paths;++path) {
                const uint64_t seed=offset+uint64_t(path);
                std::mt19937_64 rng(seed);std::normal_distribution<double> normal;
                Grid grid(name,h);
                double x=0,bm=0,energy=0,maxdrift=0,minx=0,maxx=0,maxerr=0,maxstep=0,maxstiff=0;
                long checkpoint=std::llround(16/dt);
                for(long n=0;n<steps;++n) {
                    const double a=grid.force(x);
                    maxstiff=std::max(maxstiff,dt*std::max(0.,-grid.slope(x)));
                    double noise=0;
                    for(int k=0;k<group;++k) noise+=std::sqrt(base_dt)*normal(rng);
                    grid.deposit(x,dt);
                    x+=dt*a+noise; bm+=noise; energy+=dt*a*a;
                    maxdrift=std::max(maxdrift,std::abs(a));
                    maxstep=std::max(maxstep,std::abs(dt*a/h));
                    minx=std::min(minx,x);maxx=std::max(maxx,x);
                    if(!std::isfinite(x)) throw std::runtime_error("nonfinite path");
                    if(n+1==checkpoint || n+1==steps) {
                        maxerr=std::max(maxerr,std::abs(grid.force(x)-grid.direct_force(x)));
                        const double t=(n+1)*dt;
                        out<<name<<','<<seed<<','<<dt<<','<<h<<','<<t<<','<<x<<','<<bm<<','<<energy
                           <<','<<maxdrift<<','<<minx<<','<<maxx<<','<<maxerr<<','
                           <<std::abs(grid.deposited_mass()-t)<<','<<maxstep<<','<<maxstiff<<'\n';
                        checkpoint*=2;
                    }
                }
                out.flush();
                if(path==0) {
                    std::ofstream occ(std::string(argv[1])+"."+name+".occupation.csv");
                    occ<<std::setprecision(17)<<"x,occupation_mass,occupation_density,drift_at_node\n";
                    for(int j=0;j<int(grid.mass.size());++j)
                        if(grid.mass[j]!=0 || grid.field[j]!=0)
                            occ<<(j-grid.half)*h<<','<<grid.mass[j]<<','<<grid.mass[j]/h<<','<<grid.field[j]<<'\n';
                }
                if((path+1)%8==0) std::cerr<<name<<" "<<path+1<<"/"<<paths<<" completed\n";
            }
        }
    } catch(const std::exception& e) {std::cerr<<e.what()<<'\n';return 1;}
}
