@echo off
call "C:\Users\DELL\anaconda3\Scripts\activate.bat" "C:\Users\DELL\anaconda3"

doskey ls=dir
doskey pwd=cd
doskey np=notepad
doskey hi=echo Hello
doskey cr=cd G:\2.Release
doskey cs=cd G:\TruongVN\code_ws
doskey pingf=ping 24h.com.vn -t
doskey envmde=C:\qtil\ADK_Toolkit_1.2.9.25_x64\activate.bat
doskey exp=explorer 

cmd.exe /K "conda activate earable_37"