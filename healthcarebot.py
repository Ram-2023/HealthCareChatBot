import random
greet=str(input())
print("Hii,I am Healthcare Bot.I can search covid hospitals at your selected state")
print("1.Andhra Pradesh    2.Telangana")
user=int(input('Enter a number:'))
if user==1:
    print("There are some districts which you want to select:")
    print("1.Vishakhapatnam")
    print("2.Krishna")
    print("3.Guntur")
    print("4.Chittor")
    print("5.East Godavari")
    print("6.Nellore")
    print("7.Kurnool")
    print("8.Kadapa")
    print("9.Ananthapuram")
    print("10.Vizianagaram")
    print("11.West Godavari")
    print("12.Prakasham")
    print("13.Srikakulam")
    x=int(input("Enter a number:"))
    if x==1:
        print("These are the  best covid hospitals in vishakahaptnam")
        print("1.Vishakha Institute of Medical Sciences")
        print("2.Gitam Institute Of Medical Sciences And Research")
    elif x==2:
        print("These are the best covid hospitals in Krishna")
        print("1.Kamineni Hospital")
        print("2.Aayush Nri Lepl Healthcare Pvt Ltd")
    elif x==3:
        print("These are the best covid hospitals in Guntur")
        print("1.NRI General Hospital")
        print("2.Lalitha Superspeciality Hospital")
    elif x==4:
        print("These are the best covid hospitals in Chittor")
        print("1.Padmavati Medical College")
        print("2.Amara Hospital")
    elif x==5:
        print("These are the best covid hospitals in East Godavari")
        print("1.District Hospital")
        print("2.KIIMS hospital")
    elif x==6:
        print("These are the best covid hospitals in Nellore")
        print("1.Apollo Speciality Hospital")
        print("2.Lotus Hospital")
    elif x==7:
        print("These are the best covid hospitals in Kurnool")
        print("1.Medicover Hospital")
        print("2.OMEGA HOSPITALS")
    elif x==8:
        print("These are the best covid hospitals in Kadapa")
        print("1.Sunrise Hospital")
        print("2.Sri Sri Holistic Hospital")
    elif x==9:
        print("These are the best covid hospitals in Ananthapuram")
        print("1.Government General Hospital")
        print("2.Dr. YSR Memorial Hospital")
    elif x==10:
        print("These are the best covid hospitals in Vizianagaram")
        print("1.sri sai super specialty hospital")
        print("2.District Hospital")
    elif x==11:
        print("These are the best covid hospitals in West Godavari")
        print("1.District Hospital")
        print("2.Asram Hospital")
    elif x==12:
        print("These are the best covid hospitals in Prakasham")
        print("1. Government General Hospital")
        print("2.Venkataramana hospital")
    elif x==13:
        print("These are the best covid hospitals in Srikakulam")
        print("1.DR GOLIVI HOSPITAL")
        print("2.Government General Hospital")
    else:
        print("You can select within 13 districts")
elif user==2:
    print("There are some cites which you want to select:")
    print("1.Hyderabad")
    print("2.Warangal")
    print("3.Nizamabad")
    print("4.Khammam")
    print("5.Karimnagar")
    print("6.Peddapalli")
    print("7.Mahabubnagar")
    print("8.Nalgonda")
    print("9.Adilabad")
    print("10.Siddipet")
    print("11.Suryapet")
    print("12.Medak")
    print("13.Jagtial")
    y=int(input("Enter a number:"))
    if y==1:
        print("These are the  best covid hospitals in Hyderabad")
        print("1.APOLLO HOSPITAL")
        print("2.GANDHI HOSPITAL")
    elif y==2:
        print("These are the  best covid hospitals in Warangal")
        print("1.MGM")
        print("2.ADITHYA HOSPITAL")
    elif y==3:
        print("These are the  best covid hospitals in Nizamabad")
        print("1.Government General Hospital")
        print("2.AH,BODHAN")
    elif y==4:
        print("These are the  best covid hospitals in Khammam")
        print("1.NEW LIFE EMERGENCY AND MULTISPECIALITY HOSPITAL")
        print("2.District Hospital")
    elif y==5:
        print("These are the  best covid hospitals in Karimnagar")
        print("1.MEDICOVER HOSPITALS")
        print("2.District Hospital")
    elif y==6:
        print("These are the  best covid hospitals in Peddapalli")
        print("1.DH, PEDAPALLY")
        print("2.CHC, SULTANABAD")
    elif y==7:
        print("These are the  best covid hospitals in Mahabubnagar")
        print("1.Government General Hopspital")
        print("2.CHC BADEPALLY")
    elif y==8:
        print("These are the  best covid hospitals in Nalgonda")
        print("1.Government General Hospital")
        print("2.AH Hospital")
    elif y==9:
        print("These are the  best covid hospitals in Adilabad")
        print("1.RIMS ADILABAD")
        print("2.District Hospital,UTNOOR") 
    elif y==10:
        print("These are the  best covid hospitals in Siddipet")
        print("1.Government General Hospital,Siddipet")
    elif y==11:
        print("These are the  best covid hospitals in Suryapet")
        print("1.Government General Hospital,Suryapet")
    elif y==12:
        print("These are the  best covid hospitals in Medak")
        print("1.District Hospital")
    elif y==13:
        print("These are the  best covid hospitals in Jagtial")
        print("1.AH, JAGTIAL")
    else:
        print("Invalid number")
else:
    print("You can select within two states")


print("Thank you!")