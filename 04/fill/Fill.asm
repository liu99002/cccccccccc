// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(RESTART)
//螢幕的起始位置存在RAM[0]中
@SCREEN
D=A //D=16384       
@0
M=D	 //RAM[0]=16384
/////////////////////////
(KBDCHECK)
@KBD //24576
D=M     //D等於按下的按鍵
@BLACK
D;JGT	//D>0則跳到BLACK函式中
@WHITE
D;JEQ	//D=0則跳到WHITE函式中
@KBDCHECK
0;JMP   //繼續偵測
//////////////////////////
(BLACK)
@1
M=-1	//將RAM[1]設為-1
@CHANGE
0;JMP   //跳到CHANGE
//////////////////////////
(WHITE)
@1
M=0	//將RAM[1]設為0
@CHANGE
0;JMP
//////////////////////////
(CHANGE)
@1	
D=M	//檢查RAM[1]中的顏色,D=M=RAM[1]=0 or -1
@0
A=M	//獲得螢幕的位置,A=M=RAM[0]
M=D	//將RAM[A]填入顏色,RAM[A]=0 or -1
@0
D=M+1	//將螢幕位置+1,D=RAM[0]+1=螢幕位址+1
@KBD    //24576
D=A-D	//D=鍵盤位址-(螢幕位址+1)
@0
M=M+1	//RAM[0]=RAM[0]+1
A=M     //A=螢幕位址+1
@CHANGE
D;JGT	//如果D大於0則繼續
//////////////////////////
@RESTART
0;JMP   
//當D不大於0，代表螢幕已經變化完畢，
//則回到最一開始，繼續監視鍵盤是否按下
