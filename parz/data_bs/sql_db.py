import pymysql


#Импорт в базу 
def sozidanie_table(i):
        try:
            connection = pymysql.connect(
                host="92.53.124.26",
                port=3306,
                user="gen_user",
                password="71alidi6z3",
                database="default_db"    
            )
            print('Подключение')
        except Exception as e:
            print("Леха у нас у нас %d, возсожно не поключение к базам данный по коням"%(e))

        try:
                with connection.cursor() as cursor:
                    insert_data =f"CREATE TABLE `{i}`( `id` INT(32) NOT NULL AUTO_INCREMENT , `profesion` VARCHAR(128) NOT NULL , `name_vacansian` VARCHAR(128) NOT NULL , `link` VARCHAR(128) NOT NULL , `zp` VARCHAR(128) NOT NULL , `grafik` VARCHAR(128) NOT NULL , `city` VARCHAR(128) NOT NULL , `marker_one` VARCHAR(128) NOT NULL , `marker_two` VARCHAR(128) NOT NULL , PRIMARY KEY (`id`));"
                    cursor.execute(insert_data)
                    connection.commit()

        finally:
                connection.close()

def Del_table(i):
        try:
            connection = pymysql.connect(
                host="92.53.124.26",
                port=3306,
                user="gen_user",
                password="71alidi6z3",
                database="default_db"    
            )
            print('Подключение')
        except Exception as e:
            print("Леха у нас у нас %d, возсожно не поключение к базам данный по коням"%(e))

        try:
            with connection.cursor() as cursor:
                Drop_table =f"DROP TABLE `{i}`;"
                cursor.execute(Drop_table)
        finally:
                connection.close()    

    
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
                    insert_data =f"INSERT INTO `{name_sfer}`(profesion,name_vacansian,link,zp,grafik,city,marker_one,marker_two) VALUES('{name_vacansian}','{name_resum}','{link}','{zp}','{grafik}','{city}','{stager}','{student}');"
                    cursor.execute(insert_data)
                    connection.commit()

        finally:
                connection.close()

    except Exception as ex:
        print(ex)









#Экспорт из базы