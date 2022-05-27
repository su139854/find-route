# Safi Ullah
# 1001541732
import collections
import sys
import copy

class Node:
    def __init__(this, state_name, cost,depth, prev,h):
        this.state_name = state_name # Create class node for each city
        this.cost=cost # node has variables for state_name which is the city name and the cost to that city from the route it took
        this.depth=depth # also the depth that its at
        this.prev=prev # what the previous node was
        this.heuristic=h # also if there is a heuristic then we add it, if not then its 0

        

class Info:
    def __init__(this, input):
        this.curr =[] # Info class reads the files and loads data for heursitic and general costs
        this.next=[] # store data in lists and then access lists from info objects
        this.price=[]
        this.data=[]
        this.hn_states=[]
        this.hn_cost=[]

        if(input is not None):
            this.load_data(input)
        
        if(len(sys.argv) == 5):
            this.load_heuristic(sys.argv[4]) # load only if there is a heuristic file given
            

    def load_data(this, input):
        file1=open(input,"r")
        list = file1.readlines()

        for x in list:
            if("END" not in x and x != "\n" and x!=" "):
                x=x.strip()
                x=x.split(" ")
                this.curr.append(x[0])
                this.next.append(x[1]) # adding cost data to specific lists
                this.price.append(x[2])
        file1.close()

    def load_heuristic(this,input):
        file_two=open(input,"r")
        list = file_two.readlines()

        for x in list:
            if("END" not in x and x != "\n" and x!=" "):
                x=x.strip()
                x=x.split(" ")
                this.hn_states.append(x[0]) # adding heuristic data to specific list
                this.hn_cost.append(x[1])
        file_two.close()
 


class Search:
    def __init__(this,state):
        this.x=Info(sys.argv[1])
        this.closed=set()
        this.fringe=[]
        this.expanded=0
        this.generated=1
        this.totalcost=0 # declaring variables for Search class to use 
        this.start=state
        this.route=[]
        if(len(sys.argv)==5):
            f=this.x.hn_states.index(state)
            start_node=Node(state,0,0,None,this.x.hn_cost[f]) # if heuristic search then add heuristics to nodes
        else:
            start_node=Node(state,0,0,None,0) # if not heuristic then add 0 to node.heuristic variable
        this.fringe.append(start_node)
        this.pop(start_node)

        
    def pop(this, node): # function to pop nodes from fringe as well as add them to fringe and close
        this.expanded+=1
        if(node.state_name==sys.argv[3]): # if goal node then print and exit 
            this.closed.add(node.state_name)
            this.totalcost=node.cost 
            print("Nodes expanded: ",this.expanded)
            print("Nodes generated: ",this.generated)
            print("Distance: "+str(float(this.totalcost))+" km")
            print("Route:")
            this.retreive(node.prev,this.start,node)
            this.route.reverse()
            for x in this.route:
                print(x)
            this.fringe.remove(node)
            this.fringe.clear() 

        if(this.fringe): # if fringe not empty then continue process
            if(node.state_name in this.closed):# if node in closed then remove node from fringe and go to next node
                this.fringe.remove(node)

                this.fringe.sort(key = myfunc)
                if(this.fringe):
                    this.pop(this.fringe[0])
                else:
                    this.totalcost=-1
                    print("Nodes expanded: ",this.expanded)
                    print("Nodes generated: ",this.generated)
                    print("Distance: infinity")
                    print("route: \nnone")

            else: # if node not in closed then add node to closed and generate more nodes to add to fringe
                this.closed.add(node.state_name)

                indices = [i for i, x in enumerate(this.x.curr) if x == node.state_name]
                indices2 = [i for i, x in enumerate(this.x.next) if x == node.state_name]
                this.generated+=len(indices)+len(indices2)

                if(len(sys.argv)==5):
                    this.informed(indices,indices2,node) # informed search
                 
                else:
                    this.uninformed(indices,indices2,node) # uninformed search

                this.fringe.remove(node)
                this.fringe.sort(key=myfunc) # sort fringe 

                if(this.fringe):
                    this.pop(this.fringe[0])


    
    def uninformed(this, indices, indices2, node): # add nodes based off the type of search
        for z in indices:
            this.fringe.append(Node(this.x.next[z],int(this.x.price[z])+node.cost,node.depth+1,node,0))
        for y in indices2:
            this.fringe.append(Node(this.x.curr[y],int(this.x.price[y])+node.cost,node.depth+1,node,0))

    def informed(this, indices, indices2, node): # add nodes based off the type of search
        for z in indices:
            r=this.x.hn_states.index(this.x.next[z])
            this.fringe.append(Node(this.x.next[z],int(this.x.price[z])+node.cost,node.depth+1,node,int(this.x.price[z])+node.cost+int(this.x.hn_cost[r])))
        for y in indices2:
            r=this.x.hn_states.index(this.x.curr[y])
            this.fringe.append(Node(this.x.curr[y],int(this.x.price[y])+node.cost,node.depth+1,node,int(this.x.price[y])+node.cost+int(this.x.hn_cost[r])))
  
    
    def retreive(this, node, state_name, curr): # get the route for the uniform cost search
        if(node.state_name==state_name):
            this.route.append(node.state_name+" to "+curr.state_name+" "+str(float(curr.cost))+" km")
            
        else:
            this.route.append(node.state_name+" to "+curr.state_name+" "+str(float(curr.cost-node.cost))+" km")
            this.retreive(node.prev,state_name,node)
            

def myfunc(node): # return fringe sorted by cost or heuristic
    if(len(sys.argv)==5):
        return int(node.heuristic)
    else:
        return int(node.cost)

 
def main():

    x=Search(sys.argv[2]) # start search based off the file

if __name__ == "__main__":
    main()
