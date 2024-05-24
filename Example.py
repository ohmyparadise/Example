##9
# s="6901234567892"
# print(s[7:12])
# print(s[7:-1])


# ##11
import pandas as pd
import matplotlib. pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"]
df = pd.read_excel("chengji1.xlsx")
df.at[1, "技术"] = 73 #修改第二行技术成绩为 83
df1 = df[df. 技术 >70]    #筛选技术 70 分及以上的数据
df2 = df1.groupby( "班级",as_index=False) . count()    #统计各班技术 70 分以上的人数
df3 = df2.sort_values("技术",ascending=False).head(5)        #按技术成绩降序排序取前 5 个班级
plt.bar(df3["班级"], df3["技术"]) #绘制如图 b 所示的垂直柱形图，画图方法1，用的较多
# df3.plot("班级","技术",kind ="bar" ) #绘制如图 b 所示的垂直柱形图，画图方法2
plt.title( "各班技术成绩 90 分及以上的人数对比 " )   #设置图表标题
plt.show()
##12
# def convert(s):
#     m = int( s[0:2]) * 3600 +int(s[3:5]) * 60 +int(s[6:8])
#     return m
# file=open("data.txt")       #打开文件
# line=file.readline()               #从文件中读取一行
# stu ={}                         #存储每位同学的服务总时长
# while line:
#     info=line.strip("\n").split(",")
#     t=convert(info[4])-convert(info[3])
#     if info[1]=='1':
#         if info[0] in stu:
#             stu[info[0]]+=t       #更新 stu 字典中该学生服务时间
#         else:
#             stu[info[0]] = t
#     line=file.readline()    #读取下一行
# file.close() #关闭当前文件
# stumax=max(stu.values())       #将字典的最大值存入 stumax
# for i in stu:
#     if stu[i]==stumax:
#         print(i,'服务时长:',stumax)