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
 * Function     : Merge_Sort 
 * Description  : This function sorts an array of integers using
 *                standard  merge_sort_algorithm.
 * Input        : Pointer to an array  of integers , start, end 
 * Output       : Pointer to sorted array of integers
********************************************/

int* mergesort(int *unsorted, int start, int end){
    
    //Base Case
    if ( start == end)
        return unsorted;
    int mid = (start+end)/2 ;
    int* partial_sorted ; 
    
    /******************************************************************
     * "partial_sorted" array will be temporary used to merge already sorted left and 
     * right half of array as you will see here then I update the original array 
     * to make it partially sorted !!
     * 
     * Actually, I am updating original array to reduce space complexity and also increase effieciency of program.
     * (Hope you find it good !!)
     * *****************************************************************/
           
    //allocate memory & initialize 
    partial_sorted = (int* )malloc((end-start+1)*sizeof(int));   //(end-start+1) = size of array  which will be sorted  
    
    //sort left half
    mergesort(unsorted,start,mid);
    
    //sort right half
    mergesort(unsorted,mid+1,end);
    
    //last step - merge left and right half - fully sorted array 
    int lt_index = start, rt_index = mid+1 , cur_pos = start ;

    while ( cur_pos <= end ){
        
        if ( (rt_index> end) || ((lt_index<=mid) && (unsorted[lt_index]<=unsorted[rt_index])) ){
            partial_sorted[cur_pos-start] = unsorted[lt_index]; 
            lt_index += 1 ;
        }
        
        else {
            partial_sorted[cur_pos-start] = unsorted[rt_index];
            rt_index += 1;
        }
        
        cur_pos += 1;
    }

    // updating unsorted array to make it partially sorted
    // so now in unsorted array elements from index i = start to i = end 
    // are in sorted order
    for (int j=start ; j<=end ; j++)
        unsorted[j] = partial_sorted[j-start] ;
    
    //free unwanted memory 
    free(partial_sorted);
    
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
    int *arr = (int *)malloc(INPUT_SIZE*sizeof(int));
    for (int i = 0 ; i<INPUT_SIZE ; i++)
 	    arr[i] = rand();
 	
 	//Time Calculations(in microseconds)-------------
 	auto start = std::chrono::high_resolution_clock::now();  
 	
 	mergesort(arr,0,INPUT_SIZE-1);
 	auto end = std::chrono::high_resolution_clock::now();  
 	auto time_taken = (end-start)/std::chrono::microseconds(1);
 	
 	T[n-6] = time_taken;
 	
 	//c_i calculation using given formula
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








