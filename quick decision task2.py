attendees = int(input("Enter number of attendees: "))
av_system = input("would you be needing and audio system, projector or both?")

if attendees <100 and av_system == "projector":
    print("conference room")
    if attendees <100 and av_system == "audio systems":
        print("conference room ")
elif attendees > 100 and av_system == "projector":        
        print("large hall")
else:
     print("large hall")