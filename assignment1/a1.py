def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(0)
    0
    >>> num_buses(50)
    1
    """

    #negative number of people, no bus needed
    if n < 0:
        return 0
    else:
        # partial bus is needed
        if n%50 :
            return n//50+1
        else:
            return n//50


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """

    # initialize gain and loss
    gain, loss = 0, 0
    # iterate through list of price changes
    for change in price_changes:
        if change > 0:
            gain += change
        else:
            loss += change

    return (gain, loss)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 0)
    >>> nums
    [1, 2, 3, 4, 5, 6]
    """
    # if k>=1, swap the items
    if k>0 and k<= len(L)//2: 
        L[:k], L[-k:] = L[-k:], L[:k]
    # if k == 0, no item needs swapping
    # return L


if __name__ == '__main__':
    import doctest
    doctest.testmod()
