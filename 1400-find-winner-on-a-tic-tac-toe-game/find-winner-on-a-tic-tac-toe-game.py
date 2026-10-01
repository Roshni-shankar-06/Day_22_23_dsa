class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [[0] * 3 for _ in range(2)]
        cols = [[0] * 3 for _ in range(2)]
        diag1 = [0, 0]
        diag2 = [0, 0]
        
        for i, (r, c) in enumerate(moves):
            player = i % 2
            rows[player][r] += 1
            cols[player][c] += 1
            if r == c:
                diag1[player] += 1
            if r + c == 2:
                diag2[player] += 1
                
            if (rows[player][r] == 3 or 
