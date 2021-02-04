////////////////////////////////
///  Author : Mahendra Kumar ///
///  Branch : M&C            ///
///  Date : 02-02-2021      ///
//////////////////////////////

//Header Files
#include<stdlib.h>
#include<stdio.h>
#include<cmath>
#include<time.h>
#include<chrono>
#include<iostream>

//Global Variable 
int INPUT_SIZE; 

/*******************************************
 * Function     : Quick_Sort 
 * Description  : This function sorts an array of integers using
 *                standard  inplace _quick_sort_algorithm with random pivoting.
 * Input        : Pointer to an array  of integers , start, size 
 * Output       : Pointer to sorted array of integers
********************************************/

int* quicksort(int *unsorted, int start, int size){
	
	//in given pass we are considering array from index=start to index = start+size-1
	
	//Base Case 
	if( size == 1)
	    return unsorted;
	    
	//Randomly select pivot element
	int pivotIndex = start+(rand()%size) ;  
	int pivot = unsorted[pivotIndex]; 
	
	//Algorithm 
	int i = start , j=start+size-1;
	while (i<j){
	    while((unsorted[i]<=pivot) && i<j)   i+=1;
	    while((unsorted[j]> pivot) && i<j)   j-=1;
	    
	    //swapping if possible
	    if(i<j){
	        int temp = unsorted[i];
	        unsorted[i] = unsorted[j];
	        unsorted[j] = temp;
	    }
	    
	    //Will be used if left array is already sorted  but right array contain an element which is less than pivot
	    else if ((j==i) && (j>pivotIndex) && (unsorted[j]<pivot) ){
	    	int  temp = unsorted[pivotIndex];
	    	unsorted[pivotIndex] = unsorted[i];
	    	unsorted[i] = temp;
	    }
	}
	
    //recursion
	quicksort(unsorted,start,i-start);  //left array with all elements <= pivot
	quicksort(unsorted,i,size-(i-start));  //right array with all elements > pivot

    return unsorted;
}

//Main function 

int main()
{
    int K = 25;
    
    //all array are created with size = K-6 because we will vary i from i = 6 to i=K only to get descent mean and variance values
    float T[K-6] = {0};
    int nlogn[K-6] = {0};
    double C[K-6] = {0};
    clock_t t;
    std::cout<<"NOTE :Time taken are calculated in microseconds\n";
    for (int n=6; n<=K ; n++) 
    {
    INPUT_SIZE = pow(2,n);
    nlogn[n-6] = n*INPUT_SIZE;    
    int *arr = (int *)calloc(INPUT_SIZE,sizeof(int));
    for (int i = 0 ; i<INPUT_SIZE ; i++)
 	    arr[i] = rand();
 	
 	//Time Calculations(in microseconds)-------------
 	auto start = std::chrono::high_resolution_clock::now();  
 	quicksort(arr,0,INPUT_SIZE);
 	auto end = std::chrono::high_resolution_clock::now();  
 	auto time_taken = (end-start)/std::chrono::microseconds(1);
 	
 	T[n-6] = time_taken;
 	
 	
 	//c_i calculation using formula Ci = T(INPUT_SIZE)/(INPUT_SIZE*log(INPUT_SIZE)) 
    	//when we plot these ci's then you will see for large INPUT_SIZE values of c_i's saturates i.e. algorithm is approximately n*log(n) 
 	C[n-6] = float(1.0*T[n-6]/nlogn[n-6]);
 	std::cout<<"("<<n<<","<<INPUT_SIZE<<","<<T[n-6]<<","<<nlogn[n-6]<<","<<C[n-6]<<")\n";
    }
    
    //Calculating Expectation/Mean and Variance of Ci's
    double  mean=0, variance=0 ;
    
    //Expectation/Mean
    for (int i=0 ; i<=K-6 ; i++){
        mean = mean + C[i];
    }
    mean = mean/(K-6+1)  ;
    
    //Variance 
    for (int i=0 ; i<=K-6 ; i++){
        variance = variance + pow((C[i]-mean),2) ;
    }
    variance = variance/(K-6+1);
    
    printf("Mean : %f , Variance : %f\n",mean,variance);

}


