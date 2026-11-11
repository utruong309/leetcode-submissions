class Excel:

    def __init__(self, height: int, width: str):
        """
        vals: (row, col) -> val
        formulas: (row, col) -> dict to store cells that sum up to it along with freq because some cells can be repeated in numbers 
        """
        self.vals = {} 
        self.formulas = {} 
        
    def set(self, row: int, column: str, val: int) -> None:
        if (row, column) in self.formulas: 
            del self.formulas[(row, column)] 
        self.vals[(row, column)] = val 
        
    def get(self, row: int, column: str) -> int:
        return self.calc(row, column, {})
    
    def calc(self, row: int, column: str, memo) -> int: 
        """
        - a cell not in vals yet -> 0
        - a cell is just a single cell -> return vals[(r, c)]
        - a cell is made up of a formula
            - recursively call calc on the values of cells that made it
            - because some cells can also be made up of formula 
        """
        
        if (row, column) not in self.formulas: 
            return self.vals.get((row, column), 0)
        
        total = 0 

        if (row, column) in memo: 
            return memo[(row, column)]

        for (r, c), count in self.formulas[(row, column)].items(): 
            total += self.calc(r, c, memo) * count 

        memo[(row, column)] = total 

        return total

    def sum(self, row: int, column: str, numbers: list[str]) -> int:
        cells = {} 

        for cell in numbers: 
            parts = cell.split(':')

            for i in range(int(parts[0][1:]), int(parts[-1][1:]) + 1): 
                for j in range(ord(parts[0][0]), ord(parts[-1][0]) + 1): 
                    cells[(i, chr(j))] = cells.get((i, chr(j)), 0) + 1
        
        self.formulas[(row, column)] = cells 

        return self.get(row, column)


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)