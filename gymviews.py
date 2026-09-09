from mysql import connector
import datetime

class dbconnect():
    def get_connected(self):
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Athul@2003",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None

class GymMemberManager(dbconnect):
    def get(self):
        try:
            self.connect=super().get_connected()    #super() means : go to the parent class and use its method
            self.cursor=self.connection.cursor()
            query="select * from member"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            print(records)
        except Exception as e:
            print(e)

    def get_object(self, id=None):

        self.connect = self.get_connected()
        self.cursor = self.connection.cursor()
        query = "select * from member where id=%s"
        values = (id,)
        self.cursor.execute(query, values)
        record = self.cursor.fetchone()
        return record

    def post(self,**kwargs):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connection.cursor()
            query="""
                    insert into member(name,place,mobile,plan,fee,joined_date)
                    values(%s,%s,%s,%s,%s,%s)
            """
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("New member  Added Successfully...")
        except Exception as e:
            print(e)

    def retrieve(self,id=None):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connection.cursor()
            query="select * from member where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            print(record)
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connection.cursor()
            query = "select * from member where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            if record!=None:
                query="delete from member where id=%s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Member Deleted Successfully...")
            else:
                print("Member Not Found....")
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            self.connect=super().get_connected()
            record=self.get_object(id=id)
            if record!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder += k + "=%s,"
                placeholder=placeholder.rstrip(",")
                query=f"update member set {placeholder} where id =%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Member Details added Successfully...!")

            else:
                print("Member Not Found...!")
        except Exception as e:
            print(e)


connection_instance=dbconnect()
print(connection_instance.get_connected())

member_instance=GymMemberManager()
member_instance.get()
#member_instance.post(name="Athul",place="kollam",mobile="6775365222",plan="1 month",fee=2000,joined_date=datetime.datetime.today())
#member_instance.post(name="Deepu",place="pune",mobile="8394738648",plan="3 month",fee=4000,joined_date=datetime.datetime.today())
#member_instance.post(name="Varun",place="kochi",mobile="0087876722",plan="1 year",fee=2000,joined_date=datetime.datetime.today())
#member_instance.post(name="Akshay",place="kakkanadu",mobile="79867539783",plan="1 year",fee=11000,joined_date=datetime.datetime.today())
#member_instance.retrieve(5)
#member_instance.delete(5)
member_instance.put(id=6,name="Akshay lal")