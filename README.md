# find-route
Name and UTA ID of the student: Safi Ullah 1001541732


What programming language is used for this task. (also mention if the code is omega compatible): 
python3 not omega compatible


How the code is structured: 
Node class creates node objects that are states from the file provided. They have state info. 

Info class gets the data using functions load_data to get data from files, which then loads up into lists. These lists are then used later in the search by having info objects.  Heuristic data will be loaded with load_heuristic func if file is provided. 

Search class needs a start state parameter to start search. it then uses data from info object to find the goal state. It has a pop function that recurses till the fringe is empty or goal is found. the search function will also retrieve the route and print the data that user needs. 


How to run code: 
uniformed:
python3 find_route.py input1.txt Bremen Kassel 
informed: 
python3 find_route.py input1.txt Bremen Kassel h_kassel.txt 



