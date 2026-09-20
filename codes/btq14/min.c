#include <stdio.h>
double des(double x){
	return (x-0.3*(1-(4/(x*x))));
}
double func(double x){return x+4/x;} 
int main(){
	double x=5;
	for (int i=0;i<200;i++){
		x=des(x);
	}
	printf(":%lf\n",func(x));
}
