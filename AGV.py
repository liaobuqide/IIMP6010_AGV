#此文件用来定义小车和订单类，以及小车的控制（单个小车）
import networkx as nx
import random
import draw
import time
import matplotlib.pyplot as plt
#小车和订单对象定义
class AGV:
    currentPosition = ''
    nextCargoID = ''
    orderList = []
    state = ''

class Order:
	totalOrderList = []
	finishedOrderList = []

#实例化对象部分
order = Order
agv1 = AGV
city = draw.load_city()

#订单生成模块
def generate_orderlist(order_amount):
	for i in range(order_amount):
		rdn = str(random.randint(1,99))
		if(len(rdn)==1):
			rdn = '0'+rdn
		rdn = 'n'+rdn
		order.totalOrderList.append(rdn)
	print(order.totalOrderList)

#订单分发模块
def dispatch_order(obj):
	if(obj.state == 'free'):
		for i in range(5):
			obj.orderList.append(order.totalOrderList[0])
			del order.totalOrderList[0]
		print('当前小车任务队列:',obj.orderList)
		obj.state = 'busy'

	print('分配给小车',obj,'后，订单列表还剩：',order.totalOrderList)

def search_nearest_cargo():
	pass



def AGV_processing(obj):
	plt.ion()
	draw.visualize_city(city)
	#点颜色控制
	color = ['.y','.b','.g','.m','.c']
	#事先标出物品点
	plt.plot(0, 0,'.c')
	for node in obj.orderList:
		position = draw.load_city().node_positions[node]
		plt.plot(position[0], position[1],'.r')
	while(1):
		if(len(obj.orderList)==0 and obj.currentPosition=='n00'):
			obj.nextCargoID = ''
			obj.orderList = []
			obj.state = 'free'
			break	
		time.sleep(0.1)
		#查找最近的节点
		nearestNode = ''
		nearestNodeDistance = 10000
		for cargo in obj.orderList:
			nodeDistance = nx.dijkstra_path_length(city.graph,obj.currentPosition,cargo)
			if(nodeDistance<=nearestNodeDistance):
				nearestNodeDistance = nodeDistance
				nearestNode = cargo
		obj.nextCargoID = nearestNode
		print('离小车最近的节点是：',obj.nextCargoID)
		#移动
		obj.currentPosition = nx.dijkstra_path(city.graph,obj.currentPosition,obj.nextCargoID)[1]
		print('小车移动了一步到达节点：',obj.currentPosition)
		my_city = draw.load_city()
		position = draw.load_city().node_positions[obj.currentPosition]
		
		if(obj.currentPosition == obj.nextCargoID):
			plt.plot(position[0], position[1],'.r',marker='o',markersize=6)
		else:
			plt.plot(position[0], position[1],color[len(obj.orderList)-1])
		plt.pause(0.2)
		if(obj.currentPosition == obj.nextCargoID):
			order.finishedOrderList.append(obj.nextCargoID)
			print('小车成功取货，编号为：',obj.nextCargoID)
			obj.orderList.remove(obj.nextCargoID)
		
		if(len(obj.orderList)==0):
			obj.orderList.append('n00')

		
	plt.ioff()
	plt.show()



#小车1控制模块
def AGV_control():
	agv1.currentPosition = 'n00'
	agv1.state = 'free'
	dispatch_order(agv1)
	AGV_processing(agv1)




