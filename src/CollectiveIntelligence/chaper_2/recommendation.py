# 第二章的数据集,演示欧几里得距离
from math import sqrt

#一个涉及影评者及其对几部影片评分情况的字典
critics = {
    "Lisa" : {"Lady in the water":2.5,"Snakes on a plane":3.5,"Just my luck":3.0,"Surperman returns":3.5,"You, me and Dupree":2.5,"The night Listener":3.0},
    "Gene" : {"Lady in the water":3.0,"Snakes on a plane":3.5,"Just my luck":1.5,"Surperman returns":5.0,"The night Listener":3.0,"You, me and Dupree":3.5},
    "Michael" : {"Lady in the water":2.5,"Snakes on a plane":3.0,"Surperman returns":3.5,"The night Listener":4.0},
    "Claudia" : {"Snakes on a plane":3.5,"Just my luck":3.0,"The night Listener":4.5,"Surperman returns":4.0,"You, me and Dupree":2.5},
    "Mick" : {"Lady in the water":3.0,"Snakes on a plane":4.0,"Just my luck":2.0,"Surperman returns":3.0,"The night Listener":3.0,"You, me and Dupree":2.0},
    "Jack" : {"Lady in the water":3.0,"Snakes on a plane":4.0,"The night Listener":3.0,"Surperman returns":5.0,"You, me and Dupree":3.5},
    "Toby" : {"Snakes on a plane":4.5,"You, me and Dupree":1.0,"Surperman returns":4.0}
}

#欧几里得评分相关体系函数
def sum_distance_ou(prefs,person1,person2):

    si = {}
    for item in prefs[person1]:
        if(item in prefs[person2]):
            si[item] = 1
    if len(si)==0:return 0

    #计算两人的每一项距离
    list =[pow(prefs[person1][item]-prefs[person2][item],2) for item in si]

    sum_list = sum(list)

    return 1/(sqrt(sum_list)+1)



res = sum_distance_ou(critics,"Lisa","Gene")


#皮尔逊相关度计算函数
def sum_distance_pi(prefs,person1,person2):
    si = {}
    for item in prefs[person1]:
        if(item in prefs[person2]):
            si[item] = 1

    #得到列表的个数
    si_len = len(si)

    if si_len==0 : return 1

    sum1 = sum([ prefs[person1][it] for it in si ])
    sum2 = sum([ prefs[person2][it] for it in si ])

    sum1sq = sum([ prefs[person1][it]**2 for it in si])
    sum2sq = sum([ prefs[person2][it]**2 for it in si])

    pSum = sum([prefs[person1][it]*prefs[person2][it] for it in si])

    num = pSum-(sum1*sum2/si_len)
    den = sqrt((sum1sq-pow(sum1,2)/si_len)*(sum2sq-pow(sum2,2)/si_len))
    if den==0 :return 0

    return num/den

#对字典进行排序
#list1= sorted(dict1.items(),key=lambda x:x[1])

#求出相识度的函数
def toMatches(prefs,person,similarity=sum_distance_ou,n=5):

    result = [  (similarity(prefs,person,other),other)       for other in prefs if other!=person]

    result.sort()
    result.reverse()
    return result

#利用所以他人评价值的加权平均，为某人提供建议
def getRecommendations(prefs,person,similarity =sum_distance_ou ):
    totals = {}
    simSums = {}

    #遍历所有人
    for other in prefs:
        #不要和自己比较
        if other==person:continue
        sim = similarity(prefs,person,other)

        #如果评价值为0或者小于0则忽略
        if sim<0 : continue

        #只对自己还没评价过的影片进行推荐
        for item in prefs[other]:

            if item not in prefs[person] or prefs[person][item]==0:

                #相识度*评价值
                totals.setdefault(item,0)

                totals[item]+=prefs[other][item]*sim

                #求相识度之和
                simSums.setdefault(item,0)
                simSums[item]+=sim

    rankings = [  (totals/simSums[item],item)  for item,totals in totals.items()]
    rankings.sort()
    rankings.reverse()
    print(rankings)



getRecommendations(critics,"Toby")
getRecommendations(critics,"Toby",similarity=sum_distance_pi)

#将字典进行对调
def transformPrefs(prefs):
    result = {}

    for person in prefs:
        for item in prefs[person]:

            result.setdefault(item,{})
            result[item][person] = prefs[person][item]

    return result

movies = transformPrefs(critics)
print(toMatches(movies,"Surperman returns",sum_distance_pi))



print(tools.get_popular(tag='programming'))









