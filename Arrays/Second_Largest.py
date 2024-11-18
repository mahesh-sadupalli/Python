#Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
#Note: The second largest element should not be equal to the largest element.

def getSecondLargest(arr):
        # Code Here
        if len(arr) < 2:
            return -1  # Not enough elements to find the second largest

        first = second = None

        for num in arr:
            if num == first:
                continue  # Skip if the current number is equal to the largest found so far
            if first is None or num > first:
                second = first  # Update second largest to the old largest
                first = num     # Update largest to the new number
            elif second is None or num > second:
                second = num    # Update second largest if the current number is larger than second

        # Return -1 if no second largest distinct element found
        return second if second is not None and second != first else -1
