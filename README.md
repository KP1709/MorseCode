# Morse Code Program
## 🍼 Introduction:  
This project is about creating a morse code translator which takes an input of plain English and converts it visually in morse code.  
The conversion into visual morse code is then used to translate it into sound using the system bell.  

## 🥊 Main Commits:
1. Working program in Python converting into morse code and plays correct sound. - 27/11/2021  
2. Adding whitespace as key and value in dictionary. Allowing multiple words to be converted with spaces. - 27/11/2021  
3. Error handling included for numbers and special characters. - 28/11/2021  
4. Buidling the first page to appear in GUI (containing instructions and a button for the next page). - 30/11/2021  
5. Building the second page which is the main program. - 1/12/2021
6. Merged both the first and second page of the GUI so instructions and program on one page. - 3/12/2021  

## 🔄 Changes:
Tick - change is done  
Q-mark - considering change  
Cross - not considering change  
1. Removing the sounding of system bell as it cannot be heard through external speakers. ❌  
   - This was going to be done however the audio file cannot be played for long enough for it to be heard.
   - Other methods include importing pygame.  
2. Adding the instructions and program together on one page than seperate. ✔️
   - Easier to run and use  
3. Taken user input and validated it to be in lowercase so it is read by dictionary. ✔️
   - Without this typing uppercase letters causes an error  
4. Instead of printing morse conversion to label, print it to a non-editable textbox. ✔️
   - Printing morse to label causes window to grow and hide other buttons. 
   - Printing to a textbox keeps the text a reasonable size and in one space without affecting the window size       

## 🚀 To-do:   
🔨 Create feature converting morse code back into plain English  
🔨 Swap system bell to audio file so it can be played on different audio devices.  
 
