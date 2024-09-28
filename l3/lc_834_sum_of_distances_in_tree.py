from typing import List
class Solution:
    def __init__(self):
        self.num_nodes = 0
        self.res = []
        self.adjcency_list = []
        self.subtree_size = []
        self.subtree_distance_sum = []
    
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.num_nodes = n
        self.adjcency_list = [[] for _ in range(n)]
        self.subtree_size = [1] * n
        self.subtree_distance_sum = [0] * n
        self.res = [0] * n
        for edge in edges:
            u, v = edge
            self.adjcency_list[u].append(v)
            self.adjcency_list[v].append(u)
        self.calculate_subtree_sizes_and_distance(0, -1)
        self.calculate_final_res(0, -1, 0)
        return self.res
    
    def calculate_subtree_sizes_and_distance(self, node, parent): 
        # self.subtree_size[node] = 1
        for child in self.adjcency_list[node]:
            if child == parent:
                continue
            self.calculate_subtree_sizes_and_distance(child, node)
            self.subtree_size[node] += self.subtree_size[child]
            self.subtree_distance_sum[node] += self.subtree_distance_sum[child] + self.subtree_size[child]
    
    def calculate_res(self, node, parent, parent_contribution):
        self.res[node] = (
            self.subtree_distance_sum[node] + parent_contribution + (self.num_nodes - self.subtree_size[node])
        )
        for child in self.adjcency_list[node]:
            if child == parent:
                continue
            new_parent_contribution = (
                self.res[node] - self.subtree_distance_sum[child] - self.subtree_size[child]
            )
            self.calculate_res(child, node, new_parent_contribution)