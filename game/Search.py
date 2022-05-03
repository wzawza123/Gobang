from game.Valuation_Basic import Valuation_Basic as VB
'''
Last Update :2022-4-26
Search类
成员:
SearchDepth:DFS搜索的深度,必须为单数，否则搜索会出现问题
value:估价器,Valuation_Basic类的实例
col & row :定义棋盘的尺寸
nextStep: 存放运算的结果
'''

class Search:
    col = 15
    row = 15
    SearchDepth = 3
    value = VB()
    nextStep = [0,0]

    def __init__(self):
        return


    def HasNeighbor(self,ChessBoard:list[list[int]],pos:tuple[int]):
        up = max(0,pos[0]-1)
        down = min(self.row-1,pos[0]+1)
        left = max(0,pos[1]-1)
        right = min(self.col-1,pos[1]+1)
        for i in range(up,down+1):
            for j in range(left,right+1):
                if(ChessBoard[i][j] != 0):
                    return True

    #搜索可行的步数，并且将上一步的周围位置放在最前面
    def GetStep(self,ChessBoard:list[list[int]],lastST):
        steps = []
        for i in range(0,self.row):
            for j in range(0,self.col):
                if(abs(i-lastST[0])>1 or abs(j-lastST[1])>1):
                    tmp = self.HasNeighbor(ChessBoard,(i,j))
                    if(ChessBoard[i][j]==0 and tmp):
                            steps.append((i,j))
                else:
                    if(ChessBoard[i][j]==0):
                        steps.insert(0,(i,j))
        return steps

    
    #Search函数，输入参数：当前棋盘、棋子编号、搜索深度、Alpha、Beta
    def Search(self,ChessBoard:list[list[int]],num:int,depth:int,alpha:int,beta:int,lastST:tuple[int]):
        if(depth == 0):
            return self.value.Valuation(ChessBoard,num)
        steps = self.GetStep(ChessBoard,lastST)

        for step in steps:
            ChessBoard[step[0]][step[1]] = num
            curValue = -self.Search(ChessBoard,num+1,depth-1,-beta,-alpha,step)
            # if(depth == self.SearchDepth):
            #     print(step)
            #     print(curValue)
            #还原棋盘
            ChessBoard[step[0]][step[1]] = 0

            if(curValue>alpha):
                if(depth == self.SearchDepth):
                    #print(step)
                    self.nextStep[0] = step[0]
                    self.nextStep[1] = step[1]

                #此处触发剪枝
                if(curValue >= beta):
                    return beta
                
                alpha = curValue

        return alpha


    def Direction(self,ChessBoard:list[list[int]],num:int):
        #若为第一步，则下在棋盘中央
        if(num == 1):
            self.nextStep = [self.row//2,self.col//2]
            return

        for i in range(0,self.row):
            for j in range(0,self.col):
                if(ChessBoard[i][j]==num-1):
                    Lastst = (i,j)
                            
        self.Search(ChessBoard,num,self.SearchDepth,-99999999999,99999999999,Lastst)

        

# def main():
#     ChessBorad = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 6, 13, 5, 12, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 14, 3, 4, 8, 9, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 2, 1, 7, 11, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#     Searching = Search()
#     Searching.Direction(ChessBorad,15)
#     print(Searching.nextStep)
        
# if __name__ == '__main__':
#     main()