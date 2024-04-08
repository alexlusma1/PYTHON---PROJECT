Return to your first homework assignments, when you described your favorite song. 
Refactor that code so all the variables are held as dictionary keys and value. 
Then refactor your print statements so that it's a single loop that passes through each item in the dictionary 
and prints out it's key and then it's value.

song_info = {
    "Artist": "Kanye West",
    "Genre": "Rap",
    "DurationInSeconds": "240",
    "Location": "United States",
    "YearReleased": "2023",
    "Beat": "808",
    "Clothes": "Black",
    "Hook": "Go, Go, Go",
    "Scenery": "Smoke",
    "Fans": "Inter Milan Ultras",
    "Audience": "Worldwide",
    "Language": "Mature Audience",
    "InvitedGuests": "Rich The Kid, Playboi Carti, Ty Dolla Sign"
}

for key, value in song_info.items():
    print(f"{key}: {value}")
