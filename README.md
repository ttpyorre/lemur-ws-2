# Lemur MQP 2nd Workshop
This is the second workhop the Lemur MQP is running. By the end of the workshop you will be connecting to a Romi and running your model on the Romi.  
Here are the Romis and their respective addresses:  
**Lavasoa** -- autoreg-6602086.dyn.wpi.edu  
**Goldenbamboo** -- autoreg-6602106.dyn.wpi.edu  
**Ringtailed** -- autoreg-6602101.dyn.wpi.edu  
**Redruffed** -- autoreg-6602100.dyn.wpi.edu  
**Mongoose** -- autoreg-6602075.dyn.wpi.edu  
**Graymouse** --autoreg-6602097.dyn.wpi.edu  

## How to SSH into the Pi:
In Linux and Windows, command prompt or terminal you can type the following: `ssh lemur@autoreg-#######.dyn.wpi.edu`.
The password will be the name of the Pi, which is on the bottom of the Romi. Example:  
> ssh lemur@autoreg-6602086.dyn.wpi.edu
>
> Password: lavasoa

## Where to find the necessary code in the Pi
In the terminal when accessing the Pi, first do the following command: `ls`  
Then you should see all the directories in the system. Especially one called lemur-ws-2
Now change directory to the workshop directory: `cd lemur-ws-2`
