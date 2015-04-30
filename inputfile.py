# This file is used to generate the input file by random
# author: Feifan Tong
# coding: utf8
import random
import os

#os.remove(os.path.relpath"trader1.csv")
#os.remove(os.path.relpath"trader2.csv")
f1 = file("trader1.csv" , "w")
trader1_order_time = 0
for x in xrange(1,10):
    trader1_order_time = i+random.randint(1,50000)
    f1.write("T1_"+str(x)+","+str(random.randint(1,20))+","+str(trader1_order_time)+'\n')
f1.close

trader2_order_time = 0
f2 = file("trader2.csv" , "w")
for y in xrange(1,10):
    trader2_order_time = i+random.randint(1,50000)
    f2.write("T2_"+str(y)+","+str(random.randint(1,20))+","+str(trader2_order_time)+'\n')
f2.close