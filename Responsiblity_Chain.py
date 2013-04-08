#Leave Request 
#name: Employee name
#days: Leave days
class LeaveRequest:
    def __init__(self, name, days):
        self.name = name;
        self.days = days;

class Handler:
    def setSuccessor(self, successor):
        self.successor = successor;

# Team Leader can allow leave when days <10
class TeamLeader(Handler):
    def handleRequest(self,request):
        if request.days<10 and request.days>0:
            print "TeamLeader allow you have",request.days,"days leave." 
        else:
            self.successor.handleRequest(request)

# Project Manager can allow leave when 10<=days<20            
class ProjectManager(Handler):
    def handleRequest(self,request):
        if request.days>=10 and request.days<20:
            print "ProjectManager allow you have",request.days,"days leave." 
        else:
            self.successor.handleRequest(request)
   
#Human Resource can allow leave when 20<=days<=30             
class HumanResource(Handler):
    def handleRequest(self,request):
        if request.days>=20 and request.days<=30:
            print "HR allow you have",request.days,"days leave."
        else:
            print "You can't have a leave more than 30 days, Please contact with HR." 
            
# client send leave requests to teamLeader
class Client:
    def show(self):
        
        # Create 4 requests
        requests=[];
        request1 = LeaveRequest("Harden",5)
        request2 = LeaveRequest("James",16)
        request3 = LeaveRequest("McGrady",21)
        request4 = LeaveRequest("Lin",35)
        requests.append(request1)
        requests.append(request2)
        requests.append(request3)
        requests.append(request4)
        
        # set successor
        teamLeader = TeamLeader()
        projectManager = ProjectManager()
        humanResource = HumanResource()
        teamLeader.setSuccessor(projectManager)
        projectManager.setSuccessor(humanResource)
        
        # Handle request
        for request in requests:
            teamLeader.handleRequest(request)

if __name__=="__main__":
    client = Client()
    client.show() 
    