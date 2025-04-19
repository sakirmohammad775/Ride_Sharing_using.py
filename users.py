from abc import ABC ,abstractmethod
from ride import RideRequest,RideMatching
class User(ABC):
    def __init__(self,name,email,nid)->None: # ->None is used to specify the return type of the function
        self.name=name
        self.email=email
        self.nid=nid
        self.wallet=0
        
    @abstractmethod # 
    def display_profile(self): # abstract method
        raise NotImplementedError # if this method is not implemented in the subclass then it will raise an error

class Rider(User):
    def __init__(self, name, email, nid,current_location,initial_amount)->None:
        super().__init__(name, email, nid)
        self.current_ride=None
        self.wallet=initial_amount
        self.current_location=current_location
        
    def display_profile(self):
        print(f"Name: {self.name} and email {self.email}")
        
    def load_cash(self,amount):
        if amount>0:
            self.wallet+=amount
        else:
            print("Invalid amount")
            
    def update_location(self,current_location):
        self.current_location=current_location
    
    def request_ride(self,ride_sharing,destination,vehicle_type):
        ride_request=RideRequest(self,destination)
        ride_matching=RideMatching(ride_sharing.drivers)
        ride=ride_matching.find_driver(ride_request,vehicle_type)
        self.current_ride=ride
        print("Yay !We got a ride")
        
    def show_current_ride(self):
        print(self.current_ride)
    
class Driver(User):
    def __init__(self, name, email, nid,current_location)->None:
        super().__init__(name, email, nid)
    def display_profile(self):
        print(f"Driver Name :{self.name}")
    
    def accept_ride(self,ride):
        ride.set_driver(self) # set the driver er object