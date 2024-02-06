*Read me first!!*

# Lemur MQP 2nd Workshop
This is the second workhop the Lemur MQP is running, it covers optimization techniques for running neural network models on embedded hardware

Get started by opening the Google Collab and **make a copy** by going to File -> Save a copy to Drive
Link to collab: https://colab.research.google.com/drive/1TXJq4lnkVNPVfacynCPu2d8d5vd6RTHT#scrollTo=25c5mobqYZEm

Run through the setup and introduction until you get to the Comparison to original section where you will transfer the model to your Romi.
Ask one of us running to Workshop to hand you a room and then depending on which one you get follow the below instructions to SSH into one from your laptop.
Once you SSH into your Romi you should be able to start following the Collab through to the end.

## How to SSH into the Pi:
In Linux and Windows, command prompt or terminal you can type the following: `ssh lemur@autoreg-#######.dyn.wpi.edu`.
The password will be the name of the Pi, which is on the bottom of the Romi. Example:  
> ssh lemur@autoreg-6602086.dyn.wpi.edu
>
> Password: lavasoa

Here are the Romis and their respective addresses:  
**Lavasoa** -- autoreg-6602086.dyn.wpi.edu  
**Goldenbamboo** -- autoreg-6602106.dyn.wpi.edu  
**Ringtailed** -- autoreg-6602101.dyn.wpi.edu  
**Redruffed** -- autoreg-6602100.dyn.wpi.edu  
**Mongoose** -- autoreg-6602075.dyn.wpi.edu  
**Graymouse** --autoreg-6602097.dyn.wpi.edu  

## Where to find the necessary code in the Pi
In the terminal when accessing the Pi, first do the following command: `ls`  
Then you should see all the directories in the system. Especially one called lemur-ws-2
Now change directory to the workshop directory: `cd lemur-ws-2`
