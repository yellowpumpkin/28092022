import mysql.connector

class database():

    def generate_conn_singleton(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root1516",
            database="warehouse"
        )
        # cur = con.cursor()
        return con

    def size(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute('SELECT * From WoodSize')
        data = cur.fetchall()
        return data

    def sqlThick(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute('SELECT Thick From WoodSize')
        data = cur.fetchall()
        data_thick = []
        thick_set = set(data)
        for i in thick_set:
            data_thick.append(i[0])
        data_thick.sort()
        conn.close()
        return data_thick

    def sqlWide(self):
        # pass
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute('SELECT Wide From WoodSize')
        data = cur.fetchall()
        data_wide = []
        wide_set = set(data)
        for i in wide_set:
            data_wide.append(i[0])
        data_wide.sort()
        conn.close()
        return data_wide

    def sqlLong(self):
        # pass
        conn = self.generate_conn_singleton()
        cur = conn.cursor()

        cur.execute('SELECT Longs From WoodSize')
        data = cur.fetchall()
        data_long = []
        long_set = set(data)
        for i in long_set:
            data_long.append(i[0])
        data_long.sort()
        conn.close()
        return data_long

    def sqlType(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute("SELECT WoodType_name From WoodType")

        data = cur.fetchall()
        data_type= []
        type_set = set(data)
        for i in type_set:
            data_type.append(i[0])
        data_type.sort()

        conn.close()
        return   data_type

    def sqlWithdrawType(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute("SELECT WithdrawType_name , WithdrawType_nameEn From Withdrawtype")
        data = cur.fetchall()
        withdraw_type_set = set(data)
        data_withdraw_typeTH = []
        # data_withdraw_typeEN = []
        for i in withdraw_type_set:
            data_withdraw_typeTH.append(i[0])
            # data_withdraw_typeEN.append(i[1])
        data_withdraw_typeTH.sort()

        conn.close()
        return   data_withdraw_typeTH

    def fetch_dataHome(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()

        cur.execute('SELECT Wood_id, Wood_code  , WoodType.WoodType_name  , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs , Inputs.Quantity , Volume , Activity '
                    'FROM Wood '
                    'INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id '
                    'INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id '
                    'INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id '
                         )
        data = cur.fetchall()
        conn.close()
        return  data

    def fetch_dataInput(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()

        cur.execute('SELECT Inputs.Date , Wood_code , WoodType.WoodType_name , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs , Inputs.Quantity , Volume , Inputs.Supplier '
                    'FROM Wood '
                    'INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id '
                    'INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id '
                    'INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id '
                   )
        data = cur.fetchall()
        conn.close()
        return  data

    def fetch_dataCut(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute(
            "SELECT Wood_code , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs  ,"
            "Volume , WoodType.WoodType_name , Inputs.Quantity "
            "FROM Wood "
            "INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id "
            "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id "
            "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
            "Where Wood.Activity='Available'"

            )
        data = cur.fetchall()
        conn.close()
        return data

    def fetch_dataHeat(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute(
            "SELECT Wood_code , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs  ,"
            "Volume , WoodType.WoodType_name , Inputs.Quantity "
            "FROM Wood "
            "INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id "
            "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id "
            "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
            "Where Wood.Activity='Available'"

            )

        data = cur.fetchall()
        conn.close()
        return data

    def fetch_dataResize(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute(
            "SELECT Wood_code , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs  ,"
            "Volume , WoodType.WoodType_name , Inputs.Quantity "
            "FROM Wood "
            "INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id "
            "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id "
            "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
            "Where Wood.Activity='Available'"

            )

        data = cur.fetchall()
        conn.close()
        return data

    def searchHome(self, value):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        sql = "SELECT Wood_id, Wood_code , WoodType.WoodType_name  , WoodSize.Thick , " \
              "WoodSize.Wide , WoodSize.Longs , Inputs.Quantity , Volume , Activity "\
              "FROM Wood INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id " \
              "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id " \
              "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "\
              "where Wood_code Like '%"+value+"%'"
        cur.execute(sql)
        data = cur.fetchall()
        return  data

    def searchInput(self, value):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        sql = "SELECT Inputs.Date , Wood_code , WoodType.WoodType_name , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs , Inputs.Quantity , Volume , Inputs.Supplier " \
              "FROM Wood " \
              "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id " \
              "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id " \
              "INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id "\
              "where Wood_code Like '%"+value+"%'"
        cur.execute(sql)
        data = cur.fetchall()
        return  data

    def searchCutting(self, value):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        sql = "SELECT Wood_code , WoodType.WoodType_name , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs , Inputs.Quantity , Volume  " \
              "FROM Wood " \
              "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id " \
              "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id " \
              "INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id "\
              "where Wood_code Like '%"+value+"%'"
        cur.execute(sql)
        data = cur.fetchall()
        return  data

    # Update
    def update_dataInput(self,check,date,code,g_type,g_thick,g_wide,g_long,quantity,volume,supplier):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()

        sql = 'UPDATE Wood SET Wood_code=%s , ' \
              'WoodType=(select WoodType.WoodType_id  FROM WoodType Where WoodType.WoodType_name=%s) ,' \
              'WoodSize=(Select WoodSize.Woodsize_id FROM WoodSize Where WoodSize.Thick=%s AND WoodSize.Wide=%s AND WoodSize.Longs=%s) ,' \
              'Inputs=(select Inputs.Input_id FROM Inputs WHERE Inputs.Supplier=%s AND Inputs.Date=%s AND Inputs.Quantity=%s) ,' \
              'Volume=%s' \
              'Where Wood_code=%s '

        value = (code,g_type,g_thick,g_wide,g_long,supplier,date,quantity,volume,check)
        cur.execute(sql,value)
        conn.commit()

    def funcListAvailable(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute("SELECT Wood_id, Wood_code , WoodType.WoodType_name , WoodSize.Thick , WoodSize.Wide , "
                    "WoodSize.Longs , Inputs.Quantity , Volume , Activity "
                    "FROM Wood "
                    "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id "
                    "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
                    "INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id "
                    "Where Wood.Activity='Available'")
        data = cur.fetchall()
        conn.close()
        return data

    def funcListUnavailable(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute("SELECT Wood_id, Wood_code , WoodType.WoodType_name , WoodSize.Thick , WoodSize.Wide , "
                    "WoodSize.Longs , Inputs.Quantity , Volume , Activity "
                    "FROM Wood "
                    "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id "
                    "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
                    "INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id "
                    "Where Wood.Activity='Unavailable'")
        data = cur.fetchall()
        conn.close()
        return data

    def func_update_quantity_wood(self):
        pass
        # conn = self.generate_conn_singleton()
        # cur = conn.cursor()
        # cur.execute("Update Inputs set Quantity=%s where   ")                                                                                                                                        ")
        #
        # conn.close()
        # return data

# mycursor.execute("CREATE TABLE WoodType(woodtype_name varchar(50) ,Woodtype_id	int PRIMARY KEY)")
# mycursor.execute("CREATE TABLE User(user_id	int PRIMARY KEY,password varchar(16) , activity int )")
# mycursor.execute("CREATE TABLE Customer(customer_id	int PRIMARY KEY, customer_name varchar(50) )")
# mycursor.execute("CREATE TABLE WithdrawType(WithdrawType_id	int PRIMARY KEY,WithdrawType_name varchar(50) )")
# mycursor.execute("CREATE TABLE WoodQuality(WoodQuality_id	int PRIMARY KEY,WoodQuality_name varchar(50) )")