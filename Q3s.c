#include <stdio.h>
#include <math.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_fft_complex.h>
#define real(z,i) ((z)[2*(i)])
#define imag(z,i) ((z)[2*(i)+1])



double f(double x) 
{ 
	if(x==0)
		return(1.0);
	else
	{
		float sinc;
		sinc=sin(x)/x;
		return(sinc);
	}
}

int main (void)
{
	int n=1024;
	double a=-500.0, b=500.0, del_x=(b-a)/(n-1), k[n], input[2*n],xvals[n],yvals[n];
for (int i=0;i<n;i++)
	{
		real(input,i)=f(a+i*del_x); imag(input,i)= 0.0;
	}

	gsl_fft_complex_radix2_forward (input, 1, n); 


	FILE *out;
	out=fopen("Q3s.txt","w");
	
	int i;	
	for(i=0; i<n; i++)
	{
		//Organizing k values:
		if(i<=(n/2-1))
		{
			k[i]=2*M_PI*(i/(n*del_x));
		}
		else
		{
			k[i]=2*M_PI*((i-n)/(n*del_x));
		}
        //Taking real values from fourier transform: 
		real(input,i)=del_x*(1/sqrt(2.0*M_PI))*(cos(k[i]*a)*real(input,i)+sin(k[i]*a)*imag(input,i));
		xvals[i]=k[i];
		yvals[i]=real(input,i);
		fprintf(out,"%f    %f\n",k[i],real(input,i));		
	}
	
	fclose(out);	


char *commandsForGnuplot[] = {"set title \"Fourier Transform Of Sinc Function using GSL library\"", "plot 'Q3s.txt' with linespoints ls 1  linecolor rgb '#0060ad"};
    FILE * gnuplotPipe = popen ("gnuplot -persistent", "w");
    for (i=0; i < n; i++)
    {
    fprintf(out, "%lf %lf \n", xvals[i], yvals[i]); //Write the data to a temporary file
    }

    for (i=0; i < 2; i++)
    {
    fprintf(gnuplotPipe, "%s \n", commandsForGnuplot[i]); //Send commands to gnuplot one by one.
    }
    for (i=0; i < 2; i++)
    {
    fprintf(gnuplotPipe, "%s \n", commandsForGnuplot[i]); //Send commands to gnuplot one by one.
    }
}

/* I used pyplot for comparing the numerical sol with analytical sol*/
	
	
	
	/*
Compilation Command:
gcc -Wall Q3s.c -lm -lgsl -lgslcblas -o Q3s
./Q3s */

