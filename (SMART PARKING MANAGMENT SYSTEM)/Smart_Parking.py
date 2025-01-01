from datetime import datetime 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sqlite3
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager

vehicle_Number = []
vehicle_Name = []
vehicle_Type = []
owner_Name = []
date = []
time = []
bikes = []
cars = []
bicycles = []

#create vehicle table
conn = sqlite3.connect('vehicle_info.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS vehicle (vehicle_number TEXT, vehicle_type TEXT,vehicle_name TEXT, owner_name TEXT, date TEXT, hours INT, minutes INT, bicycleS INT, bikes INT, cars INT)')
conn.commit()

#create duration table
dnn = sqlite3.connect('duration.db')
d = dnn.cursor()
d.execute('CREATE TABLE IF NOT EXISTS duration (vehicle_number TEXT,entry_hour INT, entry_minute INT, left_hour INT, left_minute INT )')
dnn.commit()

#create stay table
snn = sqlite3.connect('stay.db')
s = snn.cursor()
s.execute('CREATE TABLE IF NOT EXISTS stay (vehicle_number TEXT,stay_hours INT, stay_minutes INT)')
snn.commit()


#create amount table
ann = sqlite3.connect('amount.db')
a = ann.cursor()          
a.execute('CREATE TABLE IF NOT EXISTS amount(vehicle_number TEXT,parked_time_hours INT,parked_time_minutes INT,charge TEXT, add_vat TEXT,total TEXT)')
ann.commit()

#create record table
rnn = sqlite3.connect('record.db')
r = rnn.cursor()
r.execute('CREATE TABLE IF NOT EXISTS record (vehicle_number TEXT, owner_name TEXT, date TEXT,enter_time TEXT, left_time TEXT)')
rnn.commit()




#rnn.execute('DROP TABLE record')
#rnn.commit()
#dnn.execute('DROP TABLE duration')
#dnn.commit()
#ann.execute('DROP TABLE amount')
#ann.commit()


class LoginScreen(BoxLayout,Image,Label):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.theme_cls.primary_palette = "Blue"
        self.add_widget(Image(source="parkingarea.png",width =500,height=100,pos_hint={"center_x":0.5,"center_y":0.5}))
        self.window = BoxLayout()
        self.orientation = 'vertical'
        self.spacing = 15
        self.background_color =("LightGreen",1)
        
        self.add_widget( Label(text='Smart Parking System',font_size=40,color =[98,227,121,1],bold = True))
        label_with_bg_color = Label(text="Smart Parking System")
        
        #self.add_widget(Image(source="parkingarea.png",width =5,height=5,pos_hint={"center_x":0.5,"center_y":0.5}))
        label_with_bg_color.background_color = (0, 1, 0, 1)
        self.username_input = TextInput(hint_text='Enter Username',font_size=40,background_color =[0,204,204,1],size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.password_input = TextInput(hint_text='Enter Password',size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5},font_size=40,background_color =[0,204,204,1],password=True)
        self.submit_button = Button(text='Submit',background_color =[0,204,204,1],size_hint = (0.3, 0.3),font_size=40,pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.submit_button.bind(on_press=self.check_information)

        self.add_widget(self.username_input)
        self.add_widget(self.password_input)
        self.add_widget(self.submit_button)

    def check_information(self, instance):

        if self.username_input.text == 'group20' and self.password_input.text == '949823':
            self.clear_widgets()
            self.orientation = 'vertical'
            self.spacing = 15
            #,width =5,height=5,pos_hint={"center_x":0.5,"center_y":0.5}))
            self.add_widget(Image(source="welcome.png"))
            self.add_widget(Label(text='Successfully logged in',font_size=40,color =[98,227,121,1],bold = True))
            next_button = Button(text='Go To Option Menu',background_color =[0,204,204,1],color =[98,227,121,1],font_size=40,size_hint = (0.4, 0.4),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
            next_button.bind(on_press=self.show_menu)
            self.add_widget(next_button)

    def show_menu(self, instance):
        self.clear_widgets()
        menu = MenuScreen()
        self.add_widget(menu)


class MenuScreen(BoxLayout,Image,Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.spacing = 15
        self.add_widget( Label(text='Take Your Choice!!',font_size=40,underline=True,color =[98,227,121,1],bold = True))
        
        
        vehicle_button = Button(text='1. Vehicle Entry',bold = True,font_size=25,background_color =[0,204,204,1],size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        remove_button = Button(text='2. Remove Entry',bold = True,font_size=25,background_color =[0,0,255,1],size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        veiw_button = Button(text='3. Veiw Parked Vehicle',font_size=25,bold = True,background_color =[0,204,204,1],size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        amount_button =Button(text = "4. Amount Details",font_size=25,bold = True,background_color =[0,0,255,1],size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        bill_button = Button(text = "5. Bill",font_size=25,bold = True,background_color =[0,204,204,1],size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        show_record_button = Button(text='6. Show record ',font_size=25,bold = True,background_color =[0,0,255,1],size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        back_button = Button(text='Back',font_size=25,bold = True,background_color =[0,204,204,1],size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        

        vehicle_button.bind(on_press=self.show_vehicle_info)
        remove_button.bind(on_press=self.show_remove_info)
        veiw_button.bind(on_press=self.show_view_info)
        #left_button.bind(on_press=self.show_left)
        amount_button.bind(on_press=self.show_amount)
        bill_button.bind(on_press=self.show_bill)
        show_record_button.bind(on_press=self.record)
        back_button.bind(on_press=self.go_back)

        self.add_widget(vehicle_button)
        self.add_widget(remove_button)
        self.add_widget(veiw_button)
        #self.add_widget(left_button)
        self.add_widget(amount_button)
        self.add_widget(bill_button)
        self.add_widget(show_record_button)
        self.add_widget(back_button)
        

    def show_vehicle_info(self, instance):
        self.clear_widgets()
        vehicle_info=VehicleInfoScreen()
        self.add_widget(vehicle_info)

    def show_remove_info(self, instance):
        self.clear_widgets()
        show_remove_info = RemoveInfoScreen()
        #show_info = call(["python","RemoveEntry.py"])
        self.add_widget(show_remove_info)
   
    def show_view_info(self, instance):
        
        self.clear_widgets()
        view_info = ViewInfoScreen()
        self.add_widget(view_info)
              

    def show_amount(self, instance):
        #This is for user-info screen
        self.clear_widgets()
        amount_info = AmountInfoScreen()
        self.add_widget(amount_info)
        
    
    def show_bill(self, instance):
        #This is for user-info screen
        self.clear_widgets()
        bill_info = BillInfoScreen()
        self.add_widget(bill_info)
    def record(self, instance):
        self.clear_widgets()
        vehicle_info=RecordInfoScreen()
        self.add_widget(vehicle_info)    
    
    def go_back(self, instance):
        self.clear_widgets()
        login = LoginScreen()
        self.add_widget(login)
        
class VehicleInfoScreen(BoxLayout,Label,Image):
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'
        self.spacing = 15
        self.add_widget(Label(text='Vehicle Entry Form',font_size=30,color=(255,0,0,1),bold=True,underline=True))
        self.add_widget( Label(text='Please Fill All The Field!!',font_size=40,underline = True,color =(98,227,121,1),bold = True))
        
        #self.add_widget(Image(source="car parking.png",width =0.5,height=0.5,size_hint = (0.4, 0.4),pos_hint={"center_x":0.5,"center_y":0.5}))
        
        self.vehicle_number_input = TextInput(hint_text='Enter vehicle number (XXXX-XX-XXXX) : ', multiline=False,font_size=25,background_color =[0,204,204,1],size_hint = (0.4, 0.4),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.vehicle_type_input = TextInput(hint_text='Enter vehicle type (Bicycle=A/Bike=B/Car=C) : ',multiline=False,font_size=25,background_color =[0,204,204,1],size_hint = (0.4, 0.4),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.vehicle_name_input = TextInput(hint_text='Enter vehicle name : ', multiline=False,font_size=25,background_color =[0,204,204,1],size_hint = (0.4, 0.4),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.owner_name_input = TextInput(hint_text='Enter owner name : ', multiline=False,font_size=25,background_color =[0,204,204,1],size_hint = (0.4, 0.4),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.date_input = TextInput(hint_text='Enter Date (DD-MM-YYYY) : ', multiline=False,font_size=25,background_color =[0,204,204,1],size_hint = (0.4, 0.4),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.timeH_input = TextInput(hint_text='Enter Time (Hour) : ', multiline=False,font_size=25,background_color =[0,204,204,1],size_hint = (0.4, 0.),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.timeM_input = TextInput(hint_text='Enter Time (Minute) : ', multiline=False,font_size=25,background_color =[0,204,204,1],size_hint = (0.4, 0.),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.add_button = Button(text='Add Entry',font_size=25,bold =True,size_hint = (0.4, 0.4),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.back_button = Button(text='Back',font_size=40,background_color =[0,204,204,1],size_hint = (0.4, 0.4),pos_hint = {'center_x': 0.5, 'center_y': 0.5})

        self.add_button.bind(on_press=self.add_entry)
        
        self.back_button.bind(on_press=self.go_back)
        self.result_label = Label(text="", font_size=15,color =(98,227,121,1))
        
        self.add_widget(self.vehicle_number_input)
        self.add_widget(self.vehicle_type_input)
        self.add_widget(self.vehicle_name_input)
        self.add_widget(self.owner_name_input)
        self.add_widget(self.date_input)
        self.add_widget(self.timeH_input)
        self.add_widget(self.timeM_input)
        self.add_widget(self.add_button)
        self.add_widget(self.back_button)

        

    def add_entry(self, instance):
           
        vno = self.vehicle_number_input.text.upper()
        vtype = self.vehicle_type_input.text.lower()
        vname = self.vehicle_name_input.text
        owner_name = self.owner_name_input.text
        date = self.date_input.text
        time1 = int(self.timeH_input.text)
        time2 = int(self.timeM_input.text)
        
        
        if not vno or not vtype or not vname or not owner_name or not date or not time1 or not time2:
            
            return (self.add_widget(Label(text='# Please fill in all fields #',font_size=25,text_color=[98,227,121,1])))
            

        if vno in vehicle_Number:
            
            return (self.add_widget(Label(text='Vehicle Number Already Exists',font_size=25,text_color =(98,227,121,1))))
            

        if len(vno) != 12:
           
            return (self.add_widget(Label(text='Enter Valid Vehicle Number',font_size=25,text_color =[98,227,121,1])))
            

        if vtype =="a":
         c.execute('INSERT INTO vehicle VALUES(?, ?, ?, ?, ?, ?, ?, 1, 0, 0)',(vno,vtype,vname,owner_name,date,time1,time2))
         conn.commit()

        if vtype =="b":
          c.execute('INSERT INTO vehicle VALUES(?, ?, ?, ?, ?, ?, ?, 0, 1, 0)',(vno,vtype,vname,owner_name,date,time1,time2))
          conn.commit()

        if vtype =="c":
         c.execute('INSERT INTO vehicle VALUES(?, ?, ?, ?, ?, ?, ?, 0, 0, 1)',(vno,vtype,vname,owner_name,date,time1,time2))
         conn.commit()  

        self.add_widget(Label(text = "###### Add Entry Sucssesfully ######",font_size=25,color =(98,227,121,1)))
        self.result_label.text = "###### Add Entry Sucssesfully ###### "
            
        

    def go_back(self, instance):
        self.clear_widgets()
        menu = MenuScreen()
        self.add_widget(menu)        

class ViewInfoScreen(BoxLayout,Image,Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'
        self.add_widget(Image(source="parkedvehicle.jpg",width =5,height=5,size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5}))

        self.add_widget(Label(text='Availabe Total Space For Vehicle in Our System',font_size=30,underline = True,color =[98,227,121,1]))
        
        self.add_widget(Label(text='*1.   Bicycle   100 ',font_size=30,color =[98,227,121,1],bold = True))
        self.add_widget(Label(text='*2.   Bike      100 ',font_size=30,color =[98,227,121,1],bold = True))
        self.add_widget(Label(text='*3.   Car       50 ',font_size=30,color =[98,227,121,1],bold = True))

        self.add_widget(Label(text='Parked Vehicle',font_size=30,color =[98,227,121,1],bold = True))
       

        conn = sqlite3.connect('vehicle_info.db')
        c = conn.cursor()

        self.bi_label = Label(text="Bicycle:", font_size="25sp", color=[98, 227, 121, 1],size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        c.execute('SELECT SUM(bicycleS) FROM vehicle')
        self.bi_result = c.fetchone()[0]  # Fetch the result and extract the value
        self.add_widget(self.bi_label)
        self.add_widget(Label(text=str(self.bi_result), font_size="25sp",color=[98, 227, 121, 1], size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5}))


        self.b_label = Label(text="Bikes:", font_size="25sp", color=[98, 227, 121, 1],size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        c.execute('SELECT SUM(bikes) FROM vehicle')
        self.b_result = c.fetchone()[0]
        self.add_widget(self.b_label)
        self.add_widget(Label(text=str(self.b_result), font_size="25sp",color=[98, 227, 121, 1], size_hint=(0.3, 0.3),pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        
        
        self.ca_label = Label(text="Cars:", font_size="25sp", color=[98, 227, 121, 1],size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        c.execute('SELECT SUM(cars) FROM vehicle')
        self.ca_result = c.fetchone()[0]
        self.add_widget(self.ca_label)
        self.add_widget(Label(text=str(self.ca_result), font_size="25sp",color=[98, 227, 121, 1], size_hint=(0.3, 0.3),pos_hint={'center_x': 0.5, 'center_y': 0.5}))


        self.back_button = Button(text='Back', font_size=40, background_color=[0, 204, 204, 1])
        self.back_button.bind(on_press=self.go_back)
        self.add_widget(self.back_button)

        c.close()
        conn.close()

    def go_back(self, instance):
        self.clear_widgets()
        menu = MenuScreen()
        self.add_widget(menu)   

class RemoveInfoScreen(BoxLayout,Label,Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 15
        #self.add_widget(Label(text='Vehicle Remoe Form',font_size=30,color=(255,0,0,1),bold=True,underline=True))
        self.add_widget( Label(text='Vehicle Remove Form!!',font_size=40,underline=True,color =(98,227,121,1),bold = True))
        self.add_widget(Image(source="remove.jpg", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5}))
        self.title_label = Label(text="Enter Vehicle Number to Delete ",font_size="20sp",bold = True,color =[98,227,121,1],size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.input_text = TextInput(hint_text="Vehicle Number : ",font_size = 20,background_color =[0,204,204,1],size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})#background_color =[98,227,121,1]
        self.remove_button = Button(text="Remove Entry",font_size = 25,size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.remove_button.bind(on_press=self.remove_entry)

        self.back_button = Button(text='Back',font_size=25,background_color=[0,204,204,1],size_hint = (0.3, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.back_button.bind(on_press=self.go_back)

        
        self.add_widget(self.title_label)
        self.add_widget(self.input_text)
        self.add_widget(self.remove_button)
        self.add_widget(self.back_button)
        
       

    def remove_entry(self, instance):
        vno = self.input_text.text.upper()
        if vno == "":
            self.add_widget(Label(text="###### Enter Vehicle No. ######", font_size=30,color =(98,227,121,1)))
            return
    
         
        if vno == "":
            self.add_widget(Label(text = "###### Enter Vehicle No. ######",font_size=30,background_color =(98,227,121,1)))
            return

        if len(vno) != 12:
            self.add_widget(Label(text = "###### Enter Valid Vehicle Number ######",font_size=30,color =(98,227,121,1)))
            return
         
        try:
            conn = sqlite3.connect('vehicle_info.db')
            c = conn.cursor()
            c.execute('DELETE FROM vehicle WHERE vehicle_number = ?', (vno,))
            conn.commit()
            self.add_widget(Label(text="Removed Successfully", font_size=30,color =(98,227,121,1)))
            c.close()
        except sqlite3.Error as error:
            self.add_widget(Label(text="###### No Such Entry ######", font_size=30,color =(98,227,121,1)))

            

    def go_back(self, instance):
        self.clear_widgets()
        menu = MenuScreen()
        self.add_widget(menu)


class AmountInfoScreen(BoxLayout,Image,Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 15
        

        self.add_widget(Label(text='parking Rate',font_size=30,underline=True,color =(98,227,121,1),bold = True))
        self.add_widget(Image(source="amount.png",width =5,height=5,size_hint = (0.5, 0.5),pos_hint = {'center_x': 0.5, 'center_y': 0.5}))

        self.add_widget(Label(text='*1.   Bicycle     TK20/Hour',font_size=30,color =[98,227,121,1],bold = True))
        self.add_widget(Label(text='*2.   Bike        TK40/Hour',font_size=30,color =[98,227,121,1],bold = True))
        self.add_widget(Label(text="*3.   Car         TK80/Hour",font_size=30,color =[98,227,121,1],bold = True))

        self.back_button = Button(text='Back',font_size=40,background_color =[0,204,204,1])
        self.back_button.bind(on_press=self.go_back)
        self.add_widget(self.back_button)

    def go_back(self, instance):
        self.clear_widgets()
        menu = MenuScreen()
        self.add_widget(menu)    

class BillInfoScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 15

        self.add_widget(Image(source="paybill.png", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5}))

        self.title_label = Label(text="GENERATING BILL:", font_size="20sp", color=[98, 227, 121, 1], size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.vehicle_number_input = TextInput(hint_text="Enter vehicle number (XXXX-XX-XXXX)", multiline=False, font_size="20sp", size_hint=(0.4, 0.4), background_color=[0,204,204,1], pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.vehicle_type_input = TextInput(hint_text="Enter vehicle type (a/b/c)", multiline=False, font_size="20sp", background_color=[0,0,255,1], size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.leftH = TextInput(hint_text="Left Hour : ", font_size=20, background_color=[0, 204, 204, 1], size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.leftM = TextInput(hint_text="Left Minute : ", font_size=20, background_color=[0,0,255,1], size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.generate_button = Button(text="Generate Bill", font_size=25, size_hint=(0.4, 0.4), pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.back_button = Button(text='Back', font_size=40, background_color=[0, 204, 204, 1], size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.remove_button = Button(text='Remove Vehicle', font_size=40, background_color=[0,0,255,1], size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.generate_button.bind(on_press=self.generate_bill)
        self.back_button.bind(on_press=self.go_back)
        self.remove_button.bind(on_press=self.remove)

        self.result_label = Label(text="", font_size=15)

        self.add_widget(self.title_label)
        self.add_widget(self.vehicle_number_input)
        self.add_widget(self.vehicle_type_input)
        self.add_widget(self.leftH)
        self.add_widget(self.leftM)
        self.add_widget(self.generate_button)
        self.add_widget(self.remove_button)
        self.add_widget(self.result_label)
        self.add_widget(self.back_button)

    def remove(self, instance):
        vno = self.vehicle_number_input.text.upper()
        if vno == "":
            self.result_label.text = "Enter Vehicle No."
            return

        if len(vno) != 12:
            self.result_label.text = "Enter Valid Vehicle Number"
            return

        try:
            conn = sqlite3.connect('vehicle_info.db')
            c = conn.cursor()
            c.execute('DELETE FROM vehicle WHERE vehicle_number = ?', (vno,))
            conn.commit()
            self.result_label.text = "Removed Successfully"
        except sqlite3.Error as error:
            self.result_label.text = "No Such Entry"

    def generate_bill(self, instance):
        vno = self.vehicle_number_input.text.upper()
        vtype = self.vehicle_type_input.text.lower()
        Lh = int(self.leftH.text)
        Lm = int(self.leftM.text)

        conn = sqlite3.connect('vehicle_info.db')
        c = conn.cursor()

        

        un = sqlite3.connect('vehicle_info.db')
        u = un.cursor()

        mn = sqlite3.connect('vehicle_info.db')
        x = mn.cursor()

        if vno == "":
            self.result_label.text = "Enter Vehicle No."
            return

        if len(vno) != 12:
            self.result_label.text = "Enter Valid Vehicle Number"
            return

        c.execute('SELECT vehicle_type FROM vehicle WHERE vehicle_number = ?', (vno,))
        vtype= c.fetchone()
        
       
        amt = 0
        if vtype == "a":
            amt = 20
        elif vtype == "b":
            amt = 40
        elif vtype == "c":
            amt = 80
        else:
            self.result_label.text = "Vehicle not found"
            return

        c.execute('SELECT hours, minutes FROM vehicle WHERE vehicle_number = ?', (vno,))
        eh, em = c.fetchall()[0]

        c.close()
        conn.close()

        vn = sqlite3.connect('vehicle_info.db')
        s = vn.cursor()
        s.execute('INSERT INTO duration VALUES (?, ?, ?, ?)', (eh, em, Lh, Lm))
        vn.commit()

        calh = Lh - eh
        calm = Lm - em

        u.execute('INSERT INTO stay VALUES (?, ?)', (calh, calm))
        un.commit()

        u.execute('SELECT stay_hours FROM stay')
        stayh = u.fetchone()[0]

        u.execute('SELECT stay_minutes FROM stay')
        staym = u.fetchone()[0]

        if (Lh > eh) or (Lh == eh and Lm >= em):
            if stayh >= 1:
                amt = stayh * amt
                additional_charge = 0.18 * amt
            elif staym >= 60:
                stayh += 1
                amt = stayh * amt
                additional_charge = 0.18 * amt

            parking_charge_str = str(amt)
            additional_charge_str = str(additional_charge)
            total_charge_str = str(int(amt) + int(additional_charge))

            x.execute('INSERT INTO amount VALUES (?, ?, ?, ?, ?)',
                      (calh, calm, parking_charge_str, additional_charge_str, total_charge_str))
            #mn.commit()
           

            mn = sqlite3.connect('vehicle_info.db')
            x = mn.cursor()

            self.parking_charge = Label(text="Parking Charge", font_size="20sp",
                                        color=[98, 227, 121, 1], size_hint=(0.3, 0.3),
                                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
            x.execute('SELECT charge FROM amount')
            self.parking_charge.text = str(x.fetchone()[0])
            self.add_widget(self.parking_charge)

            self.vat_charge = Label(text="Adding VAT 18%", font_size="20sp",
                                    color=[98, 227, 121, 1], size_hint=(0.3, 0.3),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.5})
            x.execute('SELECT add_vat FROM amount')
            self.vat_charge.text = str(x.fetchone()[0])
            self.add_widget(self.vat_charge)

            self.t_charge = Label(text="Total Charge", font_size="20sp",
                                  color=[98, 227, 121, 1], size_hint=(0.3, 0.3),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.5})
            x.execute('SELECT total FROM amount')
            self.t_charge.text = str(x.fetchone()[0])
            self.add_widget(self.t_charge)
        else:
            self.result_label.text = "Invalid time entry"
        
    def go_back(self, instance):
        self.clear_widgets()
        menu = MenuScreen()  
        self.add_widget(menu)
class RecordInfoScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 15

        conn = sqlite3.connect('vehicle_info.db')
        c = conn.cursor()

        dnn = sqlite3.connect('duration.db')
        d = dnn.cursor()

        rnn = sqlite3.connect('record.db')
        r = rnn.cursor()

        self.add_widget(Label(text='Information', font_size=40, underline=True, color=[98, 227, 121, 1], bold=True))

        self.vehicle_number_input = TextInput(hint_text='Enter vehicle number (XXXX-XX-XXXX) : ', multiline=False, font_size=25, background_color=[0, 204, 204, 1], size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.owner_name_input = TextInput(hint_text='Enter owner name : ', multiline=False, font_size=25, background_color=[0, 0, 255, 1], size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.date = TextInput(hint_text='Enter Date : ', multiline=False, font_size=25, background_color=[0, 204, 204, 1], size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.enter_time = TextInput(hint_text='Enter Time : ', multiline=False, font_size=25, background_color=[0, 0, 255, 1], size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.left_time = TextInput(hint_text='Left Time : ', multiline=False, font_size=25, background_color=[0, 204, 204, 1], size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.show_button = Button(text='Save Record', font_size=25, bold=True, size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.find_button = Button(text='Find Record', font_size=25, bold=True, size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.back_button = Button(text='Back', font_size=40, background_color=[0, 204, 204, 1], size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        self.show_button.bind(on_press=self.show_entry)
        self.find_button.bind(on_press=self.find)
        self.back_button.bind(on_press=self.go_back)

        self.add_widget(self.vehicle_number_input)
        self.add_widget(self.owner_name_input)
        self.add_widget(self.date)
        self.add_widget(self.enter_time)
        self.add_widget(self.left_time)
        

        self.add_widget(self.show_button)
        self.add_widget(self.find_button)
        self.add_widget(self.back_button)

    def show_entry(self, instance):
        vno = self.vehicle_number_input.text.upper()
        vname = self.owner_name_input.text.upper()
        vdate = self.date.text.upper()
        ven = self.enter_time.text.lower()
        vlt = self.left_time.text.lower()
        #c.execute('DELETE FROM vehicle WHERE vehicle_number = ?', (vno,))

        #vname = c.execute('SELECT owner_name  FROM vehicle WHERE vehicle_number = ?', (vno,)).fetchone()
        #vdate = c.execute('SELECT date  FROM vehicle WHERE vehicle_number = ?', (vno,)).fetchone()
        #veh = c.execute('SELECT hours  FROM vehicle WHERE vehicle_number = ?', (vno,)).fetchone()
        #vem = c.execute('SELECT minutes  FROM vehicle WHERE vehicle_number = ?', (vno,)).fetchone()

        

        r.execute('INSERT INTO record VALUES(?, ?, ?, ?, ?)', (vno, vname, vdate, ven,vlt))
        rnn.commit()
        
        self.add_widget(Label(text = "###### Save Record ######",font_size=25,color =(98,227,121,1)))
    
    def go_back(self, instance):
        self.clear_widgets()
        menu = MenuScreen()
        self.add_widget(menu)


    def find(self,instance):
        self.clear_widgets()
        find_info = FindInfoScreen()
        self.add_widget(find_info)

class FindInfoScreen(BoxLayout,Label):
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'
        self.spacing = 15
        
        rnn = sqlite3.connect('record.db')
        r = rnn.cursor()

        self.add_widget(Label(text='Information',font_size=30,color =[98,227,121,1],bold= True,underline=True))
        self.add_widget(Image(source="findrecord.jpg",width =0.5,height=0.5,size_hint = (0.3, 0.3),pos_hint={"center_x":0.5,"center_y":0.5}))
        self.vehicle_number_input = TextInput(hint_text='Enter vehicle number (XXXX-XX-XXXX) : ', multiline=False,font_size=25,background_color =[0,204,204,1],size_hint = (0.4, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.find_button = Button(text='Find Information',font_size=25,bold =True,size_hint = (0.4, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.back_button = Button(text='Back',font_size=40,background_color =[0,204,204,1],size_hint = (0.4, 0.3),pos_hint = {'center_x': 0.5, 'center_y': 0.5})

        self.find_button.bind(on_press=self.find_entry)
        self.back_button.bind(on_press=self.go_back)

        self.add_widget(self.vehicle_number_input)
        self.add_widget(self.find_button)
        self.add_widget(self.back_button)
   
    def find_entry(self, instance):
        vno1 = self.vehicle_number_input.text.upper()

        r.execute('SELECT vehicle_number, owner_name, date, enter_time,left_time FROM record WHERE vehicle_number = ?', (vno1,))
        row = r.fetchone()

        if row:
            vehicle_number, owner_name,date,enter_time,left_time = row
            self.display_result(vehicle_number, owner_name, date,enter_time,left_time)
        else:
            self.display_result("Not Found", "", "", "","")

    def display_result(self, vehicle_number, owner_name,date,enter_time,left_time):
        self.clear_widgets()
       # self.add_widget(Label(text='Informatin',font_size=30,color =[98,227,121,1],bold= True,underline=True))
        
        self.add_widget(Label(text="Vehicle Number:", font_size="25sp", color=[98, 227, 121, 1],
                              size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        self.add_widget(Label(text=str(vehicle_number), font_size="25sp", color=[98, 227, 121, 1],
                              size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        self.add_widget(Label(text="Owner Name:", font_size="25sp", color=[98, 227, 121, 1],
                              size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        self.add_widget(Label(text=str(owner_name), font_size="25sp", color=[98, 227, 121, 1],
                              size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        self.add_widget(Label(text="Date:", font_size="25sp", color=[98, 227, 121, 1],
                              size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        self.add_widget(Label(text=str(date), font_size="25sp", color=[98, 227, 121, 1],
                              size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5}))


        self.add_widget(Label(text="Entering Time:", font_size="25sp", color=[98, 227, 121, 1],
                              size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        self.add_widget(Label(text=str(enter_time), font_size="25sp", color=[98, 227, 121, 1],
                              size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        self.add_widget(Label(text="Lefting Time:", font_size="25sp", color=[98, 227, 121, 1],
                              size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        self.add_widget(Label(text=str(left_time), font_size="25sp", color=[98, 227, 121, 1],
                              size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        self.add_widget(self.back_button)

    def go_back(self, instance):
        self.clear_widgets()
        menu = RecordInfoScreen()
        self.add_widget(menu)


class SmartParkingApp(App):
    def build(self):
        
        login = LoginScreen()

        return login
        

if __name__ == '__main__':
    SmartParkingApp().run()
