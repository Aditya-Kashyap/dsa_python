class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, costs):
        dpr = dpb = dpg = 0
        for r, b, g in costs:
            print("red", r)
            print('blue', b)
            print('green', g)
            dpr, dpb, dpg = min(dpb, dpg) + r, min(dpr, dpg) + b, min(dpr, dpb) + g
        return min(dpr, dpb, dpg)


if __name__ == '__main__':
    sol = Solution()
    sol1 = sol.minCost([[14, 2, 11], [11, 14, 5], [14, 3, 10]])
    sol2 = sol.minCost([[1, 2, 3], [1, 4, 6]])
    print(sol1)
    print(sol2)

