# 第二章 提供推荐
from src.CollectiveIntelligence.chaper_2 import recommendation

print(recommendation.critics["Lisa"]["Lady in the water"])

recommendation.critics["Toby"]["Snakes on a plane"] = 4.5
print(recommendation.critics["Toby"])


#两套相识度评价体系

#1.欧几里得距离
#2.皮尔逊相关度





