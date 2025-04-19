from ride import Ride,RideRequest,RideMatching,RideSharing
from users import Rider,Driver
from vehicle import Car,Bike

niye_jao=RideSharing("niye Jao")
rahim =Rider("Rahim Uddin","Rahim@gmail.com",1234,"Mohakhali",1234)
karim=Rider("Rahim Uddin","Rahim@gmail.com",1234,"Mohakhali",1234)
niye_jao.add_rider(rahim)
niye_jao.add_rider(rahim)
niye_jao.add_driver(karim)

print(niye_jao)