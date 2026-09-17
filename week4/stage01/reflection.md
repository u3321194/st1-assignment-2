Before turning on any AI tool, I built the SmartCare prototype myself. I started with a simple version that printed two hard-coded appointments using variables and f-strings, then enhanced it with a list to store appointments, a dictionary to hold each 

appointment's details, and two functions - book_appointment and display_appointments. Writing it by hand first meant I actually understood how the data was structured before asking AI anything.

Using AI as a tutor helped me understand a few things more clearly, especially why input validation matters and how a ValueError can stop bad data from being stored. It explained the limitations of my code, like the fact that it didn't check for missing fields or handle None inputs.

The AI did make some assumptions. When I asked for an alternative version, it leaned toward adding extra structure and features I hadn't asked for, rather than keeping it beginner-simple.

I verified the AI's output by running it myself and testing it with normal input, a blank patient name, and None values to see whether it behaved as claimed instead of just trusting it.

The engineering work that remained was mine: choosing one controlled improvement (checking all three fields), testing that it raised the error, removing the test line, and committing the working file to GitHub.