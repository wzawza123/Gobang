'''
TYPE CLASS :匹配棋型以及对应的得分
DATE: 2022/4/18
LAST UPDATE: 2022/4/21
'''



#TYPE类，用于评估棋型并且返回评分
#一系列棋型，用于依据棋型的估价函数
OTHER = 0;      #不予考虑的棋型
WIN = 1;        #获胜
LOSS = 2;       #输
FLEX4 = 3;      #我方活4
FLEX_4 = 4;     #对方活4
BLOCK4 = 5;     #我方冲4
BLOCK_4 = 6;    #对方冲4
FLEX3 = 7;      #我方活3
FLEX_3 = 8;     #对方活3
BLOCK3 = 9;     #我方眠3
BLOCK_3 = 10;   #对方眠3
FLEX2 = 11;     #我方活2
FLEX_2 = 12;    #对方活2
BLOCK2 = 13;    #我方眠2
BLOCK_2 = 14;   #对方眠2
FLEX1 = 15;     #我方活1
FLEX_1 = 16;    #对方活1

#返回6元组的字符串，用于dict的key值
def HASH(tuple:list[int]):
    return "".join([str(x) for x in tuple])

#1代表己方棋子，2代表对方棋子，3代表边界以外的部分
class TYPE:
    dict ={};
    Score = [];
    def __init__(self):
        #WIN
        self.dict[HASH([0,1,1,1,1,1])] = WIN
        self.dict[HASH([2,1,1,1,1,1])] = WIN
        self.dict[HASH([1,1,1,1,1,0])] = WIN
        self.dict[HASH([1,1,1,1,1,2])] = WIN
        self.dict[HASH([1,1,1,1,1,1])] = WIN
        self.dict[HASH([1,1,1,1,1,3])] = WIN
        self.dict[HASH([3,1,1,1,1,1])] = WIN
        #LOSS
        self.dict[HASH([0,2,2,2,2,2])] = LOSS
        self.dict[HASH([1,2,2,2,2,2])] = LOSS
        self.dict[HASH([2,2,2,2,2,0])] = LOSS
        self.dict[HASH([2,2,2,2,2,1])] = LOSS
        self.dict[HASH([2,2,2,2,2,2])] = LOSS
        self.dict[HASH([2,2,2,2,2,3])] = LOSS
        self.dict[HASH([3,2,2,2,2,2])] = LOSS
        #FLEX4
        self.dict[HASH([0,1,1,1,1,0])] = FLEX4
        #FLEX4
        self.dict[HASH([0,2,2,2,2,0])] = FLEX_4  
        #BOLCK4
        self.dict[HASH([2,1,1,1,1,0])] = BLOCK4
        self.dict[HASH([0,1,1,1,1,2])] = BLOCK4
        self.dict[HASH([3,1,1,1,1,0])] = BLOCK4
        self.dict[HASH([0,1,1,1,1,3])] = BLOCK4

        self.dict[HASH([0,1,1,1,0,1])] = BLOCK4
        self.dict[HASH([2,1,1,1,0,1])] = BLOCK4
        self.dict[HASH([3,1,1,1,0,1])] = BLOCK4
        self.dict[HASH([1,0,1,1,1,0])] = BLOCK4
        self.dict[HASH([1,0,1,1,1,2])] = BLOCK4
        self.dict[HASH([1,0,1,1,1,3])] = BLOCK4

        self.dict[HASH([1,1,1,0,1,0])] = BLOCK4
        self.dict[HASH([1,1,1,0,1,1])] = BLOCK4
        self.dict[HASH([1,1,1,0,1,2])] = BLOCK4
        self.dict[HASH([1,1,1,0,1,3])] = BLOCK4
        self.dict[HASH([0,1,0,1,1,1])] = BLOCK4
        self.dict[HASH([1,1,0,1,1,1])] = BLOCK4
        self.dict[HASH([2,1,0,1,1,1])] = BLOCK4
        self.dict[HASH([3,1,0,1,1,1])] = BLOCK4

        self.dict[HASH([0,1,1,0,1,1])] = BLOCK4
        self.dict[HASH([1,1,1,0,1,1])] = BLOCK4
        self.dict[HASH([2,1,1,0,1,1])] = BLOCK4
        self.dict[HASH([3,1,1,0,1,1])] = BLOCK4
        self.dict[HASH([1,1,0,1,1,0])] = BLOCK4
        self.dict[HASH([1,1,0,1,1,1])] = BLOCK4
        self.dict[HASH([1,1,0,1,1,2])] = BLOCK4
        self.dict[HASH([1,1,0,1,1,3])] = BLOCK4
        #BLOCK_4
        self.dict[HASH([1,2,2,2,2,0])] = BLOCK_4
        self.dict[HASH([0,2,2,2,2,1])] = BLOCK_4
        self.dict[HASH([3,2,2,2,2,0])] = BLOCK_4
        self.dict[HASH([0,2,2,2,2,3])] = BLOCK_4

        self.dict[HASH([0,2,2,2,0,2])] = BLOCK_4
        self.dict[HASH([1,2,2,2,0,2])] = BLOCK_4
        self.dict[HASH([3,2,2,2,0,2])] = BLOCK_4
        self.dict[HASH([2,0,2,2,2,0])] = BLOCK_4
        self.dict[HASH([2,0,2,2,2,1])] = BLOCK_4
        self.dict[HASH([2,0,2,2,2,3])] = BLOCK_4

        self.dict[HASH([2,2,2,0,2,0])] = BLOCK_4
        self.dict[HASH([2,2,2,0,2,1])] = BLOCK_4
        self.dict[HASH([2,2,2,0,2,2])] = BLOCK_4
        self.dict[HASH([2,2,2,0,2,3])] = BLOCK_4
        self.dict[HASH([0,2,0,2,2,2])] = BLOCK_4
        self.dict[HASH([1,2,0,2,2,2])] = BLOCK_4
        self.dict[HASH([2,2,0,2,2,2])] = BLOCK_4
        self.dict[HASH([3,2,0,2,2,2])] = BLOCK_4

        self.dict[HASH([0,2,2,0,2,2])] = BLOCK_4
        self.dict[HASH([1,2,2,0,2,2])] = BLOCK_4
        self.dict[HASH([2,2,2,0,2,2])] = BLOCK_4
        self.dict[HASH([3,2,2,0,2,2])] = BLOCK_4
        self.dict[HASH([2,2,0,2,2,0])] = BLOCK_4
        self.dict[HASH([2,2,0,2,2,1])] = BLOCK_4
        self.dict[HASH([2,2,0,2,2,2])] = BLOCK_4
        self.dict[HASH([2,2,0,2,2,3])] = BLOCK_4
        #FLEX3
        self.dict[HASH([0,1,1,1,0,0])] = FLEX3
        self.dict[HASH([0,1,1,1,0,2])] = FLEX3
        self.dict[HASH([0,1,1,1,0,3])] = FLEX3
        self.dict[HASH([0,0,1,1,1,0])] = FLEX3
        self.dict[HASH([2,0,1,1,1,0])] = FLEX3
        self.dict[HASH([3,0,1,1,1,0])] = FLEX3

        self.dict[HASH([0,1,1,0,1,0])] = FLEX3
        #FLEX_3
        self.dict[HASH([0,2,2,2,0,0])] = FLEX_3
        self.dict[HASH([0,2,2,2,0,1])] = FLEX_3
        self.dict[HASH([0,2,2,2,0,3])] = FLEX_3
        self.dict[HASH([0,0,2,2,2,0])] = FLEX_3
        self.dict[HASH([1,0,2,2,2,0])] = FLEX_3
        self.dict[HASH([3,0,2,2,2,0])] = FLEX_3

        self.dict[HASH([0,2,2,0,2,0])] = FLEX_3
        #BLOCK3
        self.dict[HASH([2,1,1,1,0,0])] = BLOCK3
        self.dict[HASH([3,1,1,1,0,0])] = BLOCK3
        self.dict[HASH([0,0,1,1,1,2])] = BLOCK3
        self.dict[HASH([0,0,1,1,1,3])] = BLOCK3

        self.dict[HASH([2,1,1,0,1,0])] = BLOCK3
        self.dict[HASH([3,1,1,0,1,0])] = BLOCK3
        self.dict[HASH([2,1,0,1,1,0])] = BLOCK3
        self.dict[HASH([3,1,0,1,1,0])] = BLOCK3
        self.dict[HASH([0,1,1,0,1,2])] = BLOCK3
        self.dict[HASH([0,1,1,0,1,3])] = BLOCK3
        self.dict[HASH([0,1,0,1,1,2])] = BLOCK3
        self.dict[HASH([0,1,0,1,1,3])] = BLOCK3

        self.dict[HASH([1,0,0,1,1,0])] = BLOCK3
        self.dict[HASH([1,0,0,1,1,3])] = BLOCK3
        self.dict[HASH([1,0,0,1,1,2])] = BLOCK3
        self.dict[HASH([3,1,1,0,0,1])] = BLOCK3
        self.dict[HASH([2,1,1,0,0,1])] = BLOCK3
        self.dict[HASH([0,1,1,0,0,1])] = BLOCK3

        self.dict[HASH([0,1,0,1,0,1])] = BLOCK3
        self.dict[HASH([1,0,1,0,1,0])] = BLOCK3
        #BLOCK_3
        self.dict[HASH([1,2,2,2,0,0])] = BLOCK_3
        self.dict[HASH([3,2,2,2,0,0])] = BLOCK_3
        self.dict[HASH([0,0,2,2,2,1])] = BLOCK_3
        self.dict[HASH([0,0,2,2,2,3])] = BLOCK_3

        self.dict[HASH([1,2,2,0,2,0])] = BLOCK_3
        self.dict[HASH([3,2,2,0,2,0])] = BLOCK_3
        self.dict[HASH([1,2,0,2,2,0])] = BLOCK_3
        self.dict[HASH([3,2,0,2,2,0])] = BLOCK_3
        self.dict[HASH([0,2,2,0,2,1])] = BLOCK_3
        self.dict[HASH([0,2,2,0,2,3])] = BLOCK_3
        self.dict[HASH([0,2,0,2,2,1])] = BLOCK_3
        self.dict[HASH([0,2,0,2,2,3])] = BLOCK_3

        self.dict[HASH([2,0,0,2,2,0])] = BLOCK_3
        self.dict[HASH([2,0,0,2,2,1])] = BLOCK_3
        self.dict[HASH([2,0,0,2,2,3])] = BLOCK_3
        self.dict[HASH([1,2,2,0,0,2])] = BLOCK_3
        self.dict[HASH([3,2,2,0,0,2])] = BLOCK_3
        self.dict[HASH([0,2,2,0,0,2])] = BLOCK_3

        self.dict[HASH([0,2,0,2,0,2])] = BLOCK_3
        self.dict[HASH([2,0,2,0,2,0])] = BLOCK_3
        #FLEX2
        self.dict[HASH([0,1,1,0,0,0])] = FLEX2
        self.dict[HASH([0,1,1,0,0,2])] = FLEX2
        self.dict[HASH([0,1,1,0,0,3])] = FLEX2

        self.dict[HASH([0,0,1,1,0,0])] = FLEX2
        self.dict[HASH([0,0,1,1,0,2])] = FLEX2
        self.dict[HASH([0,0,1,1,0,3])] = FLEX2
        self.dict[HASH([0,0,1,1,0,0])] = FLEX2
        self.dict[HASH([2,0,1,1,0,0])] = FLEX2
        self.dict[HASH([3,0,1,1,0,0])] = FLEX2

        self.dict[HASH([0,0,0,1,1,0])] = FLEX2
        self.dict[HASH([2,0,0,1,1,0])] = FLEX2
        self.dict[HASH([3,0,0,1,1,0])] = FLEX2

        self.dict[HASH([0,1,0,1,0,0])] = FLEX2
        self.dict[HASH([0,1,0,1,0,2])] = FLEX2
        self.dict[HASH([0,1,0,1,0,3])] = FLEX2
        self.dict[HASH([0,0,1,0,1,0])] = FLEX2
        self.dict[HASH([2,0,1,0,1,0])] = FLEX2
        self.dict[HASH([3,0,1,0,1,0])] = FLEX2

        self.dict[HASH([0,1,0,0,1,0])] = FLEX2
        #FLEX_2
        self.dict[HASH([0,2,2,0,0,0])] = FLEX_2
        self.dict[HASH([0,2,2,0,0,1])] = FLEX_2
        self.dict[HASH([0,2,2,0,0,3])] = FLEX_2

        self.dict[HASH([0,0,2,2,0,0])] = FLEX_2
        self.dict[HASH([0,0,2,2,0,1])] = FLEX_2
        self.dict[HASH([0,0,2,2,0,3])] = FLEX_2
        self.dict[HASH([0,0,2,2,0,0])] = FLEX_2
        self.dict[HASH([1,0,2,2,0,0])] = FLEX_2
        self.dict[HASH([3,0,2,2,0,0])] = FLEX_2

        self.dict[HASH([0,0,0,2,2,0])] = FLEX_2
        self.dict[HASH([1,0,0,2,2,0])] = FLEX_2
        self.dict[HASH([3,0,0,2,2,0])] = FLEX_2

        self.dict[HASH([0,2,0,2,0,0])] = FLEX_2
        self.dict[HASH([0,2,0,2,0,1])] = FLEX_2
        self.dict[HASH([0,2,0,2,0,3])] = FLEX_2
        self.dict[HASH([0,0,2,0,2,0])] = FLEX_2
        self.dict[HASH([1,0,2,0,2,0])] = FLEX_2
        self.dict[HASH([3,0,2,0,2,0])] = FLEX_2

        self.dict[HASH([0,2,0,0,2,0])] = FLEX_2
        #BLOCK2
        self.dict[HASH([2,1,1,0,0,0])] = BLOCK2
        self.dict[HASH([3,1,1,0,0,0])] = BLOCK2
        self.dict[HASH([0,0,0,1,1,2])] = BLOCK2
        self.dict[HASH([0,0,0,1,1,3])] = BLOCK2

        self.dict[HASH([2,1,0,1,0,0])] = BLOCK2
        self.dict[HASH([3,1,0,1,0,0])] = BLOCK2
        self.dict[HASH([0,0,1,0,1,2])] = BLOCK2
        self.dict[HASH([0,0,1,0,1,3])] = BLOCK2

        self.dict[HASH([2,1,0,0,1,0])] = BLOCK2
        self.dict[HASH([3,1,0,0,1,0])] = BLOCK2
        self.dict[HASH([0,1,0,0,1,2])] = BLOCK2
        self.dict[HASH([0,1,0,0,1,3])] = BLOCK2

        self.dict[HASH([1,0,0,0,1,0])] = BLOCK2
        self.dict[HASH([1,0,0,0,1,2])] = BLOCK2
        self.dict[HASH([1,0,0,0,1,3])] = BLOCK2
        self.dict[HASH([0,1,0,0,0,1])] = BLOCK2
        self.dict[HASH([2,1,0,0,0,1])] = BLOCK2
        self.dict[HASH([3,1,0,0,0,1])] = BLOCK2
        #BLOCK_2
        self.dict[HASH([1,2,2,0,0,0])] = BLOCK_2
        self.dict[HASH([3,2,2,0,0,0])] = BLOCK_2
        self.dict[HASH([0,0,0,2,2,1])] = BLOCK_2
        self.dict[HASH([0,0,0,2,2,3])] = BLOCK_2

        self.dict[HASH([1,2,0,2,0,0])] = BLOCK_2
        self.dict[HASH([3,2,0,2,0,0])] = BLOCK_2
        self.dict[HASH([0,0,2,0,2,1])] = BLOCK_2
        self.dict[HASH([0,0,2,0,2,3])] = BLOCK_2

        self.dict[HASH([1,2,0,0,2,0])] = BLOCK_2
        self.dict[HASH([3,2,0,0,2,0])] = BLOCK_2
        self.dict[HASH([0,2,0,0,2,1])] = BLOCK_2
        self.dict[HASH([0,2,0,0,2,3])] = BLOCK_2

        self.dict[HASH([2,0,0,0,2,0])] = BLOCK_2
        self.dict[HASH([2,0,0,0,2,1])] = BLOCK_2
        self.dict[HASH([2,0,0,0,2,3])] = BLOCK_2
        self.dict[HASH([0,2,0,0,0,2])] = BLOCK_2
        self.dict[HASH([1,2,0,0,0,2])] = BLOCK_2
        self.dict[HASH([3,2,0,0,0,2])] = BLOCK_2
        #FLEX1
        self.dict[HASH([0,1,0,0,0,0])] = FLEX1
        self.dict[HASH([0,1,0,0,0,2])] = FLEX1
        self.dict[HASH([0,1,0,0,0,3])] = FLEX1

        self.dict[HASH([0,0,1,0,0,0])] = FLEX1
        self.dict[HASH([2,0,1,0,0,0])] = FLEX1
        self.dict[HASH([3,0,1,0,0,0])] = FLEX1
        self.dict[HASH([0,0,1,0,0,2])] = FLEX1
        self.dict[HASH([0,0,1,0,0,3])] = FLEX1

        self.dict[HASH([0,0,0,1,0,0])] = FLEX1
        self.dict[HASH([2,0,0,1,0,0])] = FLEX1
        self.dict[HASH([3,0,0,1,0,0])] = FLEX1
        self.dict[HASH([0,0,0,1,0,2])] = FLEX1
        self.dict[HASH([0,0,0,1,0,3])] = FLEX1

        self.dict[HASH([0,0,0,0,1,0])] = FLEX1
        self.dict[HASH([2,0,0,0,1,0])] = FLEX1
        self.dict[HASH([3,0,0,0,1,0])] = FLEX1
        #FELX_1
        self.dict[HASH([0,2,0,0,0,0])] = FLEX_1
        self.dict[HASH([0,2,0,0,0,1])] = FLEX_1
        self.dict[HASH([0,2,0,0,0,3])] = FLEX_1

        self.dict[HASH([0,0,2,0,0,0])] = FLEX_1
        self.dict[HASH([1,0,2,0,0,0])] = FLEX_1
        self.dict[HASH([3,0,2,0,0,0])] = FLEX_1
        self.dict[HASH([0,0,2,0,0,1])] = FLEX_1
        self.dict[HASH([0,0,2,0,0,3])] = FLEX_1

        self.dict[HASH([0,0,0,2,0,0])] = FLEX_1
        self.dict[HASH([1,0,0,2,0,0])] = FLEX_1
        self.dict[HASH([3,0,0,2,0,0])] = FLEX_1
        self.dict[HASH([0,0,0,2,0,1])] = FLEX_1
        self.dict[HASH([0,0,0,2,0,3])] = FLEX_1

        self.dict[HASH([0,0,0,0,2,0])] = FLEX_1
        self.dict[HASH([1,0,0,0,2,0])] = FLEX_1
        self.dict[HASH([3,0,0,0,2,0])] = FLEX_1

        self.Score = [0,
                      99999999,-90000000,      #WIN/LOSE
                      90000000,-10000000,      #FLEX4/FELX_4
                      80000000,-8000000,       #BLOCK4/BLOCK_4
                      10000000,4000000,        #FLEX3/FLEX_3
                      800000,-50000,            #BLOCK3/BLOCK_3
                      50000,-25000,
                      6000,-3000,
                      200,-100];

    #返回对应六元组的得分
    def GetPoint(self,Tuple:list[int]):
        if(HASH(Tuple)) in self.dict:
            return self.Score[self.dict[HASH(Tuple)]];
        else:
            return self.Score[OTHER]
    
