# Linkedin_Connection_Automation
After spending hours searching for a linkedin connection automation that:
    * Is functional.
    * Doesn't spam you with irrelevant connections, but hand picks the best ones.
    * Skips the "Follow", and "Message" buttons.
    * Won't be suspicious with it's "connection speed".
Iv'e decided to just create it myelf.....

This script iterates through the connections list of specific people and sends a connect request to the most suitable people in that list.


# Important to acknowledge:
1. Watch the first 4 minutes of the video to set up the script. https://www.youtube.com/watch?v=2ZiknMDHHWA
2. The script will not be detected as a bot as it was build to "move" slow on purpose. 
   Doing 100 connections in a minute is highly suspicious. For that reason I wrote the script to run slower and sleep for a few seconds after some actions
3.  This script is based on finding Web elements by their name. LinkedIn changes the names of the elements once a week…. At least. 
    If the script doesn’t work, it means 1 of 3 things:
	        A) You didn't follow the steps in the first 4 minutes of the video
		      B) Your Web driver is outdated. Happens every 2 weeks and super easy to update. 
             If this is the case you will see errors containing the words: PATH or Driver 
          C) The elements were changed, and the script is outdated… I promise to TRY and update it once a week. 
             If this happens you will see errors containing the strings:  [3.2], [4.2], [4.3], [8.2]
4. Once the script opened the chrome window, don't touch the chrome window.


# Video:
https://www.youtube.com/watch?v=2ZiknMDHHWA
0:00  -  3:20   -  How to set up the script. MUST WATCH!
3:30  -  Skips person that doesn't contain the key words in his description.
6:35  - Avoiding the "Message" button
9:33  -  Switching to the next person in the people list.
11:38 - Avoiding the "Follow" button 
15:50  -  Closes the window once reached the connections limit.



How does it work?
1. You must see the first 4 minutes of the video above and follow the simple instructions for providing the dependencies of the script. 
2. Once the script is up and running, you provide it with 3-5 people you are connected with.
   Example: John Terry, Kevin Hart, Ariel Silver. 
   On top of that, you add key words that are related to the field you desire.
   Example:  Cyber, Security, research, Malware analysis. 
3. The Script will iterate through the people you specified connections lists, and search for other LinkedIn users that have one of the key words in their description.
4. Once it found a suitable candidate for a connection, it will look at the button on the right and see if it says "Connect", "Follow", "Pending" or "Message". If the "Connect"    button is available, the script will press it.



If there is any issue with the script, please send me a message on linkedin.
Username:  Silver Plate

