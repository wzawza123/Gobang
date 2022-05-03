from game.Valuation_Basic import Valuation_Basic as VB

'''
LastUpdate:2022/5/3 13:10
FastSearch类,只进行一层搜索
成员:
col & row :描述棋盘尺寸
value: 估值器
nextStep: 存放下一步的解
'''

class Search_Fast:
    col = 15
    row = 15
    value = VB()
    nextStep = [0,0]

    def __init__(self):
        return

    def GetStep(self,ChessBoard:list[list[int]]):
        up = self.row
        down = 0
        left = self.col
        right = 0
        for i in range(0,self.row):
            for j in range(0,self.col):
                if(ChessBoard[i][j] != 0):
                    up = min(up,i)
                    down = max(down,i)
                    left = min(left,j)
                    right = max(right,j)
        up = max(up-3,0)
        down = min(down+3,self.row-1)
        left = max(left-3,0)
        right = min(right+3,self.col-1)
        Steps = []

        for i in range(up,down+1):
            for j in range(left,right+1):
                if(ChessBoard[i][j]==0):
                    Steps.append((i,j))

        return Steps

    def Direction(self,ChessBoard:list[list[int]],num:int):
        if(num == 1):
            self.nextStep = [self.row//2,self.col//2]
            return

        maxValue = -9999999999
        Steps = self.GetStep(ChessBoard)
        for step in Steps:
            ChessBoard[step[0]][step[1]] = num
            curValue = -1 * self.value.Valuation(ChessBoard,num+1)
            ChessBoard[step[0]][step[1]] = 0
            if(curValue>maxValue):
                maxValue=curValue
                self.nextStep = [step[0],step[1]]
        return 

# def main():
#     ChessBorad = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 6, 13, 5, 12, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 14, 3, 4, 8, 9, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 2, 1, 7, 11, 15, 16, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,18, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#     Searching = Search_Fast()
#     Searching.Direction(ChessBorad,19)
#     print(Searching.nextStep)
        
# if __name__ == '__main__':
#     main()    
            

        

    
    