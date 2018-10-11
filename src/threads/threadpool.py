from multiprocessing.dummy import Pool as ThreadPool

# [Touraj] :: Good sample for simple ThreadPool and parallel processing of some algorithms that can be complex
# and time Consuming

def squareNumber(n):
    return n ** 2


# function to be mapped over
def calculateParallel(numbers, threads=2):
    pool = ThreadPool(threads)
    results = pool.map(squareNumber, numbers)
    pool.close()
    pool.join()
    return results


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    squaredNumbers = calculateParallel(numbers, 4)
    for n in squaredNumbers:
        print(n)

# [Touraj]
# HERE acctually A map is a built-in higher-order function that applies a given function to each element of a list, returning a list of results.

# Note:
    # The multiprocessing library is usually used for separate processes,
    # however it has a neat dummy module that works over threads.
    # In fact, it's so trivial that you only need to set the number of
    # threads and give it your function to be mapped over. This method
    # does all of the hard work for you.