import string
import pymysql
#表名 action_movie,comedy_movie,horror_movie,story_movie,science_movie, cartoon,thriller_movie,war_movie,crime_movie
def connect_mysql():
    connect = pymysql.connect(host='localhost', port=3306, user='root', passwd='12345dfg', db='movie',
                              charset='utf8')
    if(connect):
        print("连接成功")
        return connect
    else:
        print("连接失败")
        exit(-1)
def tuple_to_list(tuple):


    if tuple:
        li=[]
        for i in range(len(tuple)):
            li.append(list(tuple[i]))

        lis=list(li)
        return lis
    else:
        lis=[]
        return lis

def search_mysql(key,pg):

    if key =='%%':
        return None
    else:
        connect=connect_mysql()
        cursor=connect.cursor()
        find1 = "select mv_name,link from action_movie where mv_name like '%s'" \
                "UNION SELECT mv_name,link FROM comedy_movie WHERE mv_name LIKE '%s' " \
                "UNION SELECT mv_name,link FROM horror_movie WHERE mv_name LIKE '%s'" \
                "UNION SELECT mv_name,link FROM story_movie WHERE mv_name LIKE '%s'" \
                "UNION SELECT mv_name,link FROM science_movie WHERE mv_name LIKE '%s'" \
                "UNION SELECT mv_name,link FROM cartoon WHERE mv_name LIKE '%s'" \
                "UNION SELECT mv_name,link FROM thriller_movie WHERE mv_name LIKE '%s'" \
                "UNION SELECT mv_name,link FROM war_movie WHERE mv_name LIKE '%s'"

        cursor.execute(find1 % (key,key,key,key,key,key,key,key))
        res1=tuple_to_list(cursor.fetchall())
        print(len(res1),type(res1))

        num=int(pg)*30
        res=res1[num:num+30]
        print(len(res))
        print(res)
        if res:
            return res,len(res),len(res1)
        else:
            return None
def search_mysql_move(id,pg):
    connect = connect_mysql()
    cursor = connect.cursor()
    print(pg)
    if id ==0:
        find2="select mv_name,link from comedy_movie"
        cursor.execute(find2)
        res1=tuple_to_list(cursor.fetchall())
        print(len(res1),type(res1))
        num=int(pg)*30
        res=res1[num:num+30]
        print(len(res))
        print(res)
        return res,len(res),len(res1)
    if id ==1:
        find2 = "select mv_name,link from science_movie"
        cursor.execute(find2)
        res1 = tuple_to_list(cursor.fetchall())
        print(len(res1), type(res1))
        num = int(pg) * 30
        res = res1[num:num + 30]
        print(len(res))
        print(res)
        return res, len(res), len(res1)
    if id ==2:
        find2 = "select mv_name,link from action_movie"
        cursor.execute(find2)
        res1 = tuple_to_list(cursor.fetchall())
        print(len(res1), type(res1))
        num = int(pg) * 30
        res = res1[num:num + 30]
        print(len(res))
        print(res)
        return res, len(res), len(res1)
    if id ==3:
        find2 = "select mv_name,link from thriller_movie"
        cursor.execute(find2)
        res1 = tuple_to_list(cursor.fetchall())
        print(len(res1), type(res1))
        num = int(pg) * 30
        res = res1[num:num + 30]
        print(len(res))
        print(res)
        return res, len(res), len(res1)
    if id ==4:
        find2 = "select mv_name,link from horror_movie"
        cursor.execute(find2)
        res1 = tuple_to_list(cursor.fetchall())
        print(len(res1), type(res1))
        num = int(pg) * 30
        res = res1[num:num + 30]
        print(len(res))
        print(res)
        return res, len(res), len(res1)
    if id ==5:
        find2 = "select mv_name,link from war_movie"
        cursor.execute(find2)
        res1 = tuple_to_list(cursor.fetchall())
        print(len(res1), type(res1))
        num = int(pg) * 30
        res = res1[num:num + 30]
        print(len(res))
        print(res)
        return res, len(res), len(res1)

    if id==6:
        find2 = "select mv_name,link from cartoon"
        cursor.execute(find2)
        res1 = tuple_to_list(cursor.fetchall())
        print(len(res1), type(res1))
        num = int(pg) * 30
        res = res1[num:num + 30]
        print(len(res))
        print(res)
        return res, len(res), len(res1)
    if id==7:
        find2 = "select mv_name,link from dual"
        cursor.execute(find2)
        res1 = tuple_to_list(cursor.fetchall())
        print(len(res1), type(res1))
        num = int(pg) * 30
        res = res1[num:num + 30]
        print(len(res))
        print(res)
        return res, len(res), len(res1)

if __name__=='__main__':

    key=input("关键字查找:")
    key='%'+key+'%'
    page=input('page num:')
    print(type(key))
    search_mysql(key=key,pg=page)