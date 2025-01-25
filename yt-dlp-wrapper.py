import os
#os.system('pip install yt-dlp --upgrade')
os.system('pip install pip --upgrade')
os.system('yt-dlp -U')
os.system('cls')
os.system('cls')
while True:
    banner="""
┓┏       ┓     ┳┓       ┓     ┓      ┓ ┏            ╻
┗┫┏┓┓┏╋┓┏┣┓┏┓  ┃┃┏┓┓┏┏┏┓┃┏┓┏┓┏┫┏┓┏┓  ┃┃┃┏┓┏┓┏┓┏┓┏┓┏┓┃
┗┛┗┛┗┻┗┗┻┗┛┗   ┻┛┗┛┗┻┛┛┗┗┗┛┗┻┗┻┗ ┛   ┗┻┛┛ ┗┻┣┛┣┛┗ ┛ •
                                            ┛ ┛      
"""
    os.system('cls')
    print(banner)
    youtube=input("Please Select Type Of Youtube Data You Need!\n1 - Videos\n2 - Music\nq - Exit The program\n")
    if youtube == '1':
        os.system('cls')
        print(banner)
        video=input("Please Paste The URL and Press Enter To Download Video Or Type q To Return To Main Menu!\n")
        if video == 'q':
            continue
            os.system('cls')
        else:
                os.system('yt-dlp -k ' + video)
    if youtube == '2':
        os.system('cls')
        print(banner)
        music=input("Please Paste The URL and Press Enter To Download Music Or Type q To Return To Main Menu!!\n")
        if music == 'q':
            continue
            os.system('cls')
        else:
            os.system('yt-dlp --extract-audio --audio-format mp3 ' + music)
    if youtube == 'q':
        break
    if youtube == 'Q':
        break
    else:
        print("Invalid Option Selected Or Something Went Wrong!\n")
        
