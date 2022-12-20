import pymysql


#Импорт в базу 
def update(name_sfer,name_vacansian,name_resum,link,zp,grafik,city,stager,student):
    # скрыть данные
    try:
        connection = pymysql.connect(
            host="92.53.124.26",
            port=3306,
            user="gen_user",
            password="71alidi6z3",
            database="default_db"    
        )
        print('Подключение')

        try:
            with connection.cursor() as cursor:
                create_table_query = f"GREATE TABLE `{name_sfer}`(id int AUTO_INCREMENT, profesion varchar(128), name_vacansian varchar(128), link varchar(128),zp varchar(128),grafik varchar(128),city varchar(128), marker_one varchar(128) , marker_two varchar(128) PRIMARY KEY (id) );"
                cursor.execute(create_table_query)
            with connection.cursor() as cursor:
                insert_data =f"INSERT INTO `{name_sfer}`(profesion,name_vacansian,link,zp,grafik,city,marker_one,marker_two) VALUES('{name_vacansian}','{name_resum}','{link}','{zp}','{grafik}','{city}','{stager}','{student}';)"
                cursor.execute(insert_data)
                connection.commit()

        finally:
            connection.close()

    except Exception as ex:
        print(ex)









#Экспорт из базы