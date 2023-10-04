from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk

root=Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False,False)

# *********************************************************************

def getWeather():
    city = textfield.get()

    geoLocator = Nominatim(user_agent="geoapiExercises")
    location = geoLocator.geocode(city)
    obj = TimezoneFinder()

    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    lng_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    api = f"https://api.openweathermap.org/data/2.8/onecall?lat={location.latitude}&lon={location.longitude}&units=metric&exclude=hourly&appid=984bde0317363e7ae5598110aa9af9bf"

    response = requests.get(api)
    data = response.json()

    temp = data['current']['temp']
    humidity = data['current']['humidity']
    pressure = data['current']['pressure']
    wind_speed = data['current']['wind_speed']
    description = data['current']['weather'][0]['description']

    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind_speed,"m/s"))
    d.config(text=(description))

    firstDayImage=data['daily'][0]['weather'][0]['icon']

    photo1=ImageTk.PhotoImage(file=f"./Icons/{firstDayImage}@2x.png")
    image1.config(image=photo1)
    image1.image=photo1

    tempFirstDay = data['daily'][0]['temp']['day']
    tempFirstNight = data['daily'][0]['temp']['night']
    temp1.config(text=f"Day:{tempFirstDay}\n Night:{tempFirstNight}")

    secondDayImage=data['daily'][1]['weather'][0]['icon']

    img=(Image.open(f"./Icons/{secondDayImage}@2x.png"))
    resized_image=img.resize((50,50))
    photo2=ImageTk.PhotoImage(resized_image)
    image2.config(image=photo2)
    image2.image=photo2

    tempSecondDay = data['daily'][1]['temp']['day']
    tempSecondNight = data['daily'][1]['temp']['night']
    temp2.config(text=f"Day:{tempSecondDay}\n Night:{tempSecondNight}")

    thirdDayImage=data['daily'][2]['weather'][0]['icon']

    img=(Image.open(f"./Icons/{thirdDayImage}@2x.png"))
    resized_image=img.resize((50,50))
    photo3=ImageTk.PhotoImage(resized_image)
    image3.config(image=photo3)
    image3.image=photo3

    tempThirdDay = data['daily'][2]['temp']['day']
    tempThirdNight = data['daily'][2]['temp']['night']
    temp3.config(text=f"Day:{tempThirdDay}\n Night:{tempThirdNight}")

    fourthDayImage=data['daily'][3]['weather'][0]['icon']

    img=(Image.open(f"./Icons/{fourthDayImage}@2x.png"))
    resized_image=img.resize((50,50))
    photo4=ImageTk.PhotoImage(resized_image)
    image4.config(image=photo4)
    image4.image=photo4

    tempFourthDay = data['daily'][3]['temp']['day']
    tempFourthNight = data['daily'][3]['temp']['night']
    temp4.config(text=f"Day:{tempFourthDay}\n Night:{tempFourthNight}")

    fifthDayImage=data['daily'][4]['weather'][0]['icon']

    img=(Image.open(f"./Icons/{fifthDayImage}@2x.png"))
    resized_image=img.resize((50,50))
    photo5=ImageTk.PhotoImage(resized_image)
    image5.config(image=photo5)
    image5.image=photo5

    tempFifthDay = data['daily'][4]['temp']['day']
    tempFifthNight = data['daily'][4]['temp']['night']
    temp5.config(text=f"Day:{tempFifthDay}\n Night:{tempFifthNight}")

    sixthDayImage=data['daily'][5]['weather'][0]['icon']

    img=(Image.open(f"./Icons/{sixthDayImage}@2x.png"))
    resized_image=img.resize((50,50))
    photo6=ImageTk.PhotoImage(resized_image)
    image6.config(image=photo6)
    image6.image=photo6

    tempSixthDay = data['daily'][5]['temp']['day']
    tempSixthNight = data['daily'][5]['temp']['night']
    temp6.config(text=f"Day:{tempSixthDay}\n Night:{tempSixthNight}")

    seventhDayImage=data['daily'][6]['weather'][0]['icon']

    img=(Image.open(f"./Icons/{seventhDayImage}@2x.png"))
    resized_image=img.resize((50,50))
    photo7=ImageTk.PhotoImage(resized_image)
    image7.config(image=photo7)
    image7.image=photo7

    tempSeventhDay = data['daily'][6]['temp']['day']
    tempSeventhNight = data['daily'][6]['temp']['night']
    temp7.config(text=f"Day:{tempSeventhDay}\n Night:{tempSeventhNight}")

    first=datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))


# *********************************************************************

app_icon=PhotoImage(file="./Images/logo.png")
root.iconphoto(False,app_icon)

weather_box=PhotoImage(file="./Images/weatherBox.png")
Label(root,image=weather_box,bg="#57adff").place(x=30,y=110)

label1=Label(root,text="Temperature:",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=40,y=120)

label2=Label(root,text="Humidity:",font=('Helvetica',11),fg="white",bg="#203243")
label2.place(x=40,y=140)

label3=Label(root,text="Pressure:",font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=40,y=160)

label4=Label(root,text="Wind Speed:",font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=40,y=180)

label5=Label(root,text="Description:",font=('Helvetica',11),fg="white",bg="#203243")
label5.place(x=40,y=200)

search_box=PhotoImage(file="./Images/searchBar.png")
search_image=Label(image=search_box,bg="#57adff")
search_image.place(x=270,y=120)

search_box_weather=PhotoImage(file="./Images/searchLogo.png")
search_weather_image=Label(root,image=search_box_weather,bg="#203243")
search_weather_image.place(x=290,y=127)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

search_icon=PhotoImage(file="./Images/searchIcon.png")
search_icon_image=Button(image=search_icon,borderwidth=0,bg="#203243",cursor="hand2",command=getWeather)
search_icon_image.place(x=645,y=125)

frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

weather_frame1=PhotoImage(file="./Images/frame1.png")
weather_frame2=PhotoImage(file="./Images/frame2.png")

Label(frame,image=weather_frame1,bg="#212120").place(x=30,y=20)
Label(frame,image=weather_frame2,bg="#212120").place(x=300,y=30)
Label(frame,image=weather_frame2,bg="#212120").place(x=400,y=30)
Label(frame,image=weather_frame2,bg="#212120").place(x=500,y=30)
Label(frame,image=weather_frame2,bg="#212120").place(x=600,y=30)
Label(frame,image=weather_frame2,bg="#212120").place(x=700,y=30)
Label(frame,image=weather_frame2,bg="#212120").place(x=800,y=30)

clock=Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=700,y=20)

timezone=Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=30,y=20)

lng_lat=Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
lng_lat.place(x=30,y=50)

t=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t.place(x=140,y=120)
h=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
h.place(x=140,y=140)
p=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
p.place(x=140,y=160)
w=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
w.place(x=140,y=180)
d=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
d.place(x=140,y=200)

frame1=Frame(root,width=230,height=132,bg="#282829")
frame1.place(x=35,y=315)

day1=Label(frame1,font="arial 20",bg="#282829",fg="#fff")
day1.place(x=100,y=5)

image1=Label(frame1,bg="#282829")
image1.place(x=1,y=15)

temp1=Label(frame1,bg="#282829",fg="#57adff",font="arial 15 bold")
temp1.place(x=100,y=50)

frame2=Frame(root,width=70,height=115,bg="#282829")
frame2.place(x=305,y=325)

day2=Label(frame2,bg="#282829",fg="#fff")
day2.place(x=5,y=5)

image2=Label(frame2,bg="#282829")
image2.place(x=7,y=25)

temp2=Label(frame2,bg="#282829",fg="#fff")
temp2.place(x=1,y=78)

frame3=Frame(root,width=70,height=115,bg="#282829")
frame3.place(x=405,y=325)

day3=Label(frame3,bg="#282829",fg="#fff")
day3.place(x=5,y=5)

image3=Label(frame3,bg="#282829")
image3.place(x=7,y=25)

temp3=Label(frame3,bg="#282829",fg="#fff")
temp3.place(x=1,y=78)

frame4=Frame(root,width=70,height=115,bg="#282829")
frame4.place(x=505,y=325)

day4=Label(frame4,bg="#282829",fg="#fff")
day4.place(x=5,y=5)

image4=Label(frame4,bg="#282829")
image4.place(x=7,y=25)

temp4=Label(frame4,bg="#282829",fg="#fff")
temp4.place(x=1,y=78)

frame5=Frame(root,width=70,height=115,bg="#282829")
frame5.place(x=605,y=325)

day5=Label(frame5,bg="#282829",fg="#fff")
day5.place(x=5,y=5)

image5=Label(frame5,bg="#282829")
image5.place(x=7,y=25)

temp5=Label(frame5,bg="#282829",fg="#fff")
temp5.place(x=1,y=78)

frame6=Frame(root,width=70,height=115,bg="#282829")
frame6.place(x=705,y=325)

day6=Label(frame6,bg="#282829",fg="#fff")
day6.place(x=5,y=5)

image6=Label(frame6,bg="#282829")
image6.place(x=7,y=25)

temp6=Label(frame6,bg="#282829",fg="#fff")
temp6.place(x=1,y=78)

frame7=Frame(root,width=70,height=115,bg="#282829")
frame7.place(x=805,y=325)

day7=Label(frame7,bg="#282829",fg="#fff")
day7.place(x=5,y=5)

image7=Label(frame7,bg="#282829")
image7.place(x=7,y=25)

temp7=Label(frame7,bg="#282829",fg="#fff")
temp7.place(x=1,y=78)

root.mainloop()