#计算北京地铁每月乘车票价总金额

#默认：每次乘车x元，每天乘车2次，每月乘车22天

#每月乘车总金额超过100元，下次乘车票价的8折
#每月乘车总金额超过150元，下次乘车票价的5折
#每月乘车总金额超过400元，下次乘车不打折


def way():
    dayMoney = int(raw_input("请输入您单次乘车正常票价(单位:元)："))
    dayTime  = raw_input("请输入您每天乘车次数(默认2次)：")
    dayMonth = raw_input("请输入您每月乘车天数(默认22天)：")
    dayAllMoney = 0.0  # 当月乘车总金额


    #统计各阶段乘车的钱数和次数和
    m100 = 0.0
    m150 = 0.0
    m400 = 0.0
    mmax = 0.0
    t100 = 0

    t150 = 0
    t400 = 0
    tmax = 0

    if dayTime == '':
        dayTime = 2


    else:
        dayTime=int(dayTime)  #格式转换

    if dayMonth=='':
        dayMonth=22
    else:
         dayMonth=int(dayMonth) #格式转换

    dayMonthTime=dayTime*dayMonth #每月总乘车次数
    dayNowTime=0  #乘车次数记录



    while dayNowTime<=dayMonthTime:

        if dayAllMoney<=100.0: #总金额小等于100元时，按正常票价收费
            dayAllMoney+=dayMoney
            m100+=dayMoney
            t100+=1
        elif dayAllMoney<=150.0:  #总金额小等于150时，按正常票价的8折收费
             dayAllMoney+=dayMoney*0.8
             m150+=dayMoney*0.8
             t150+=1
        elif dayAllMoney<=400.0: #总金额小等于400时，按正常票价的5折收费
             dayAllMoney+=dayMoney*0.5
             m400+=dayMoney*0.5
             t400+=1
        else :  #总金额超过400元，按正常票价收费
             dayAllMoney+=dayMoney
        mmax+=dayMoney
        tmax+=1
        dayNowTime+=1 #乘车次数++

    return (dayMonth,dayTime,dayMoney,dayAllMoney,m100,t100,m150,t150,m400,t400,mmax,tmax)


if __name__== '__main__':
    (dm,dt,dy,dam,m100,t100,m150,t150,m400,t400,mmax,tmax)= way()

    print("\n")
    print ("您该月共乘坐北京地铁 {0} 天，每天 {1} 次，单次乘车消费{2}元，共消费 {3:.2f} 元。".format(dm,dt,dy,dam))
    print("\n")
    print("月总消费额度100元阶段内: 共乘坐 {0} 次，阶段消费 {1:.2f} 元，共计 {2:.2f} 元。".format(t100,m100,m100))
    print("月总消费额度150元阶段内: 共乘坐 {0} 次，阶段消费 {1:.2f} 元，共计 {2:.2f} 元。".format(t150,m150,m100+m150))
    print("月总消费额度400元阶段内: 共乘坐 {0} 次，阶段消费 {1:.2f} 元，共计 {2:.2f} 元。".format(t400,m400,m100+m150+m400))
    print("月总消费额度超过400元阶段内: 共乘坐 {0} 次，阶段消费 {1:.2f} 元，共计 {2:.2f} 元。".format(tmax,mmax,m100+m150+m400+mmax))
    print("\n")