# Fetch all your medical info from meditik
This script is used by programmers, I can guide you what do you need to change 
inorder to fetch the info from your user, feel free to add medical_center fetch
# What can you fetch and how does it work?
## Inside every './appointments' './operations' './referrals'  you got 'main.py'
# Inorder to get all your .pdf appointments (as well for the others) you need to do these steps:
#### 1. Login to meditik and press F12 (inspect), Go to network tab.
#### 2. In the network tab, Add filter 'medical-center'
#### 3. Update './appointments/medical-center-appointments.json' file or whatever medical info you want to fetch.
a. In the website press "סיכומי ביקור"  
b. press the first 'medical-center' and then go to 'Response' tab.  
c. Copy all the Dictionary (json), Without the brackets '[]'!, to the json file you need to update.  
#### 4. Update in ./medical_center/vars.py
a. Inside any medical-center Request in the network inspection, press 'Headers' tab, and look in the last headers for 'Solider' and 'Authorization'.  
b. Copy these values to their place in 'vars.py'  
#### Finally, now you can use and fetch any medical info you need and run your wanted 'main.py' file.


 
