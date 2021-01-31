#O(N)
def max_sub_array_of_size_k(k, arr):
    winStart, maxSum, winSum = 0, 0.0, 0.0
    result = []
    for i in range(len(arr)):
        winSum += arr[i];
        if(i >= k-1):
            result.append(winSum / k)
            if(maxSum < winSum):
                maxSum = winSum
                
            winSum -= arr[winStart]
            winStart += 1 

    return result #maxSum 


def main():
    result = max_sub_array_of_size_k(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    #result = max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])
    
    print(result)  
    
main()