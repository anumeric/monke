#monkey no understand how pull request bananas

'''
Objectives:
1. Find winner in O(n) space and O(1) time
2. Find player rank in O(nlogn) space
Notes:
1. if matrix[i][j]==1, then i has beaten j 
Problem Statement:
https://stackoverflow.com/questions/31589642/winner-of-a-tournament-in-on-and-rank-of-the-players-in-onlogn?rq=1
https://www.careercup.com/question?id=5102434353414144
Notes:
1. Topological Sort https://www.youtube.com/watch?v=Akt3glAwyfY [Course Schedule III]
2. Heapq may be viable
'''
from graphlib import TopologicalSorter 

class Solution():
    def tennis(self,matrix):

        # O(n2)
        def matrix_to_dict(matrix):      
            players = len(matrix)
            keys = list(range(0,players))
            matrix_dict = {k: set() for k in keys}
            
            for i in range(0,len(matrix)):
                for j in range(0,len(matrix[0])):
                    if i!=j and matrix[i][j]==1:
                            #print(i,"has beaten", j)
                        matrix_dict[i].add(j)
            return matrix_dict
                        

        matrix_dict = matrix_to_dict(matrix)

        ts = TopologicalSorter(matrix_dict)
        res = list(ts.static_order())
        print("winner is:",res[-1])
        print("ranks are (lowest to highest):",res)
        
  
if __name__ == "__main__":
    #inputs
    matrix = [
    [0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 0, 0]
    ]
    
    solution = Solution()
    solution.tennis(matrix)
    
