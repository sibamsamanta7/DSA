class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        """
        Count the number of islands whose sum of values is divisible by k.
      
        Args:
            grid: 2D grid where non-zero values represent land
            k: The divisor to check island sums against
          
        Returns:
            Number of islands whose sum is divisible by k
        """
        def dfs(row: int, col: int) -> int:
            """
            Depth-first search to explore an island and calculate its sum.
            Marks visited cells by setting them to 0.
          
            Args:
                row: Current row index
                col: Current column index
              
            Returns:
                Sum of all values in the connected island
            """
            # Store the current cell's value
            island_sum = grid[row][col]
          
            # Mark current cell as visited by setting to 0
            grid[row][col] = 0
          
            # Explore all 4 adjacent directions (up, right, down, left)
            for i in range(4):
                next_row = row + directions[i]
                next_col = col + directions[i + 1]
              
                # Check if the adjacent cell is within bounds and is land (non-zero)
                if (0 <= next_row < rows and 
                    0 <= next_col < cols and 
                    grid[next_row][next_col] != 0):
                    # Recursively explore and add to island sum
                    island_sum += dfs(next_row, next_col)
          
            return island_sum
      
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
      
        # Direction vectors for moving up, right, down, left
        # Pairs: (-1,0), (0,1), (1,0), (0,-1)
        directions = [-1, 0, 1, 0, -1]
      
        # Counter for islands divisible by k
        island_count = 0
      
        # Traverse the entire grid
        for i in range(rows):
            for j in range(cols):
                # If we find unvisited land, explore the island
                if grid[i][j] != 0:
                    # Get the sum of the entire island
                    total_sum = dfs(i, j)
                  
                    # Check if island sum is divisible by k
                    if total_sum % k == 0:
                        island_count += 1
      
        return island_count
