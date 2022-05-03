'''
Description: 
Date: 2022-05-03 13:40:41
LastEditTime: 2022-05-03 14:00:47
'''
from copy import deepcopy
from operator import mod
from game.TYPE import TYPE

#基础版本的估值函数，采用棋型匹配的方式
'''
LAST UPDATE: 2022/4/21
Valuation_Basic类
成员：
row & col 表示棋盘的尺寸
ty 评估器，用于评价棋型得分
方法：
ValueScope:生成三个方向的棋型列表
Valuation:生成当前棋盘在当前位置落子的评分
'''
class Valuation_Basic:
    ty = TYPE()
    row = 15
    col = 15
    def __init__(self):
        return

    #需要输入当前的棋盘和落子的编号
    #num为当前需要落子的编号
    def ValueScope(self,ChessBoard:list[list[int]],num):
        #分别为本次落子前后生成的六元组列表
        NxtList = [];
        poses = [];

        #扫描所有可能的位置
        for i in range(self.row):
            for j in range(self.col):
                if(ChessBoard[i][j]!=0):
                    poses.append((i,j))


        #只用向4个方向分析棋盘，因为棋型字典具有对称性
        for pos in poses:
            curNum = ChessBoard[pos[0]][pos[1]]
            if mod(curNum,2) == mod(num,2):
                my = 1
                enemy = 2
            else:
                my = 2
                enemy = 1
            for direct in [(1,0),(1,1),(0,1),(1,-1)]:
                for dist in [0,1,2,3,4,5]:
                    startP = (pos[0]-direct[0]*dist,pos[1]-direct[1]*dist)
                    #生成当前的链表与落子之后的链表
                    nList = [0,0,0,0,0,0]
                    for i in [0,1,2,3,4,5]:
                        curPos = (startP[0]+direct[0]*i,startP[1]+direct[1]*i)
                        if(curPos[0]<0 or curPos[1]<0 or curPos[0]>=self.row or curPos[1]>=self.col):
                            nList[i] = 3
                        else:
                            if (ChessBoard[curPos[0]][curPos[1]] == 0):
                                nList[i] = 0   
                            elif mod(ChessBoard[curPos[0]][curPos[1]],2) == mod(curNum,2):
                                nList[i] = my
                            else:
                                nList[i] = enemy
                    NxtList.append(deepcopy(nList))
        return NxtList

    def Valuation(self,ChessBoard:list[list[int]],num):
        NxtList = self.ValueScope(ChessBoard,num)
        score = 0
        for i in range(len(NxtList)):
            score = score + self.ty.GetPoint(NxtList[i])
        return score


# def main():
#     ChessBorad = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 12, 0, 7, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 10, 2, 1, 11, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 6, 3, 5, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#     value = Valuation_Basic()
#     print(value.Valuation(ChessBorad,13))
        
# if __name__ == '__main__':
#     main()
    

