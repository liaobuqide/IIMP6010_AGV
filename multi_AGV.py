#大家可以把多车问题的想法写在下面

#这个函数用来控制多个小车（目前考虑不事先分配任务，小车在行走过程中实时分配任务直到满载）
def multi_AGV():
	#考虑2辆小车的情况
	agv1 = AGV
	agv2 = AGV
	while(1):
		order_dispatch()






#这个函数用来控制订单怎么分配给每辆小车
def order_dispatch():




#计算小车拿货的最短路径（这里可以考虑DJ/贪心/A*算法的优劣）
def shortest_route():



#我之前做的地图还可以优化，有什么想法可以写作下面
def map_optimization():