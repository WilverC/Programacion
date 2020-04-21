program Gatonto;
Uses
	Crt, Graph;
Const
	Celdas = 9;
Type
	TypeBoard = array[1..Celdas] of char;
Var
	Error, GrMonitor, GrResol: integer;
	Fig, Resp: char;
	Turn, i, Cont: integer;
	Board : TypeBoard;

{**************************************************************}
Procedure Marco;
Begin
	SetLineStyle(DottedLn,5,Thickwidth);
	SetColor(1);
	Rectangle(50,80,680,480);
	SetLineStyle(SolidLn,0,Thickwidth);
End;

{**************************************************************}
Procedure Presentacion;
Begin
  	CLEARDEVICE;
  	Marco;
  	{titulo}
  	SetTextStyle (TriplexFont, HorizDir, 6);
  	SetColor(4);
	SetBkColor(0);
	OutTextXY(150,30,'GATO TONTO');
	{letras}
	SetTextStyle(DefaultFont, HorizDir, 1);
	SetColor(14);
	OutTextXY(90,120, 'Bienvenido');
	OutTextXY(90,140, 'Este es el tradicional juego del Gato, en este solo podra participar');
	OutTextXY(90,160, 'usted y la computadora, tendra la opcion de elegir figura "X" o "O"');
	OutTextXY(90,180, 'y el turno que desee.');
	OutTextXY(90,220, 'Este gato tratara de bloquear todas sus jugadas ganadoras y al final');
	OutTextXY(90,240, 'le mandara un mensaje de quien fue, el ganador o si empataron');
	OutTextXY(90,280, 'La modalidad de este juego sera la siguiente: ');
	{dibujo}
	SetTextStyle(SansSerifFont, HorizDir, 2);
	SetColor(4);
	Line(330,318,405,318);
	Line(330,336,405,336);
	Line(350,300,350,355);
	Line(385,300,385,355);
	SetColor(14);
	OutTextXY(330,300,'1 2 3');
	OutTextXY(330,320,'4 5 6');
	OutTextXY(330,340,'7 8 9');
	{letras}
	SetTextStyle(DefaultFont, HorizDir, 1);
	OutTextXY(90,380, 'Lo anterior muestra la enumeracion de las casillas, pues la computadora ');
	OutTextXY(90,400, 'le pedira el valor de alguna de estas casillas, la cual sera su ');
	OutTextXY(90,420, 'movimiento.');
	OutTextXY(220, 460, 'Presione Enter para continuar...');
	Readln;
End;

{**************************************************************}
Procedure Opcion;
Begin
	for i:=1 to Celdas do
	Begin
  		Board[i]:=' ';
  	End;
	CLEARDEVICE;
	Marco;
	{titulo}
	SetTextStyle(TriplexFont, HorizDir, 6);
	SetColor(4);
	SetBkColor(0);
	OutTextXY(150,30,'GATO TONTO');
	{letras}
	SetTextStyle(DefaultFont, HorizDir, 1);
	SetColor(14);
	OutTextXY(200,100, 'La modalidad del juego es la siguiente: ');
	OutTextXY(200,120, 'Elija el primer tirador: ');
	SetColor(White);
	OutTextXY(260,140, '1) Computadora ');
	OutTextXY(260,160, '2) Usuario');
	SetColor(14);
	OutTextXY(200,200, 'Cual es su opcion: ');
	SetColor(White);
	repeat
		Turn:=(ord(readkey) - ord('0'));
	until((Turn=1) or (Turn=2));
	SetColor(14);
	OutTextXY(200,240,'Elija la figura con que se identificara: ');
	SetColor(White);
	OutTextXY(260,260,'X) X');
	OutTextXY(260,280,'O) O');
	SetColor(White);
	OutTextXY(200,320,'Cual es su opcion: ');
	SetColor(White);
	repeat
		Fig:=readkey;
	until (Fig='x') or (Fig='X') or (Fig='o') or (Fig='O');
	SetColor(14);
End;

{**************************************************************}
Procedure DibujaGato;
Begin
	CLEARDEVICE;
	Marco;
	{titulo}
	SetTextStyle(TriplexFont, HorizDir, 6);
	SetColor(4);
	OutTextXY(150,30, 'GATO TONTO');
	{gato}
	SetLineStyle(SolidLn, 0, Thickwidth);
	SetColor(14);
	SetBkColor(0);
	Line(335,135,335,375);
	Line(415,135,415,375);
	Line(255,215,495,215);
	Line(255,295,495,295);
End;

{**************************************************************}
Procedure DibujarTirada(fig:char; movimiento:integer);
Begin
	SetTextStyle(TriplexFont, HorizDir, 6);
	SetColor(White);
	case fig of
	'X': case movimiento of
		1 : OutTextXY(275,155, fig);
		2 : OutTextXY(355,155, fig);
		3 : OutTextXY(435,155, fig);
		4 : OutTextXY(275,235, fig);
		5 : OutTextXY(355,235, fig);
		6 : OutTextXY(435,235, fig);
		7 : OutTextXY(275,315, fig);
		8 : OutTextXY(355,315, fig);
		9 : OutTextXY(435,315, fig);
		end;
	'O': case movimiento of
		1 : OutTextXY(275,155, fig);
		2 : OutTextXY(355,155, fig);
		3 : OutTextXY(435,155, fig);
		4 : OutTextXY(275,235, fig);
		5 : OutTextXY(355,235, fig);
		6 : OutTextXY(435,235, fig);
		7 : OutTextXY(275,315, fig);
		8 : OutTextXY(355,315, fig);
		9 : OutTextXY(435,315, fig);
		end;
	end;
End;

{**************************************************************}
Procedure AceptarTirada(fig:char);
Var
	movimiento : integer;
Begin
	SetTextStyle(DefaultFont, HorizDir, 1);
	SetColor(14);
	OutTextXY(12,400,'Escribe tu movimiento (1-9): ');
	repeat
		repeat
			movimiento:= (ord(readkey) - ord('0'));
		until((movimiento=1) or (movimiento=2) or (movimiento=3) 
			or (movimiento=4) or (movimiento=5) or (movimiento=6)
			or (movimiento=7) or (movimiento=8) or (movimiento=9));
	until(Board[movimiento] = ' ');
	Board[movimiento]:=fig;
	DibujarTirada(fig, movimiento);
End;

{**************************************************************}
Function Ganador(fig:char):integer;
Begin
	case fig of
	'X': if ( ((Board[1] = 'X') and (Board[2] = 'X') and (Board[3] = 'X')) or 
		      ((Board[4] = 'X') and (Board[5] = 'X') and (Board[6] = 'X')) or
		      ((Board[7] = 'X') and (Board[8] = 'X') and (Board[9] = 'X')) or
		      ((Board[1] = 'X') and (Board[4] = 'X') and (Board[7] = 'X')) or
		      ((Board[2] = 'X') and (Board[5] = 'X') and (Board[8] = 'X')) or
		      ((Board[3] = 'X') and (Board[6] = 'X') and (Board[9] = 'X')) or
		      ((Board[1] = 'X') and (Board[5] = 'X') and (Board[9] = 'X')) or
		      ((Board[3] = 'X') and (Board[5] = 'X') and (Board[7] = 'X'))) then
		ganador:= Turn;
	'O': if ( ((Board[1] = 'O') and (Board[2] = 'O') and (Board[3] = 'O')) or 
		      ((Board[4] = 'O') and (Board[5] = 'O') and (Board[6] = 'O')) or
		      ((Board[7] = 'O') and (Board[8] = 'O') and (Board[9] = 'O')) or
		      ((Board[1] = 'O') and (Board[4] = 'O') and (Board[7] = 'O')) or
		      ((Board[2] = 'O') and (Board[5] = 'O') and (Board[8] = 'O')) or
		      ((Board[3] = 'O') and (Board[6] = 'O') and (Board[9] = 'O')) or
		      ((Board[1] = 'O') and (Board[5] = 'O') and (Board[9] = 'O')) or
		      ((Board[3] = 'O') and (Board[5] = 'O') and (Board[7] = 'O')) ) then
		ganador:= Turn;
	end;
End;

{**************************************************************}
Function DesplegarGanador(fig:char):integer;
Begin
	SetTextStyle(TriplexFont, HorizDir, 6);
	SetColor(4);
	DesplegarGanador:=0;
	if(Cont = 9)then
	Begin
		DesplegarGanador:=1;
	End;
	{if(Turn=1) then
	Begin
		if(Ganador(fig)=1)then
		Begin
			Sound(1000);
			Delay(1000);
			CLEARDEVICE;
			Marco;
			OutTextXY(96,300,'**** Yo Gane *****');
			NoSound;
			DesplegarGanador:=1;
		End
		else
			if(Ganador(fig)=2)then
			Begin
				Sound(1000);
				Delay(1000);
				CLEARDEVICE;
				Marco;
				OutTextXY(96,300,'**** Usted Gana *****');
				NoSound;
				DesplegarGanador:=1;
			End
			else
				if(Cont=9)then
				Begin
					Sound(1000);
					Delay(1000);
					CLEARDEVICE;
					Marco;
					OutTextXY(96,300,'**** Gato *****');
					NoSound;
					DesplegarGanador:=0;
				End;
	End
	else
	Begin
		if(Ganador(fig)=1)then
		Begin
			Sound(1000);
			Delay(1000);
			CLEARDEVICE;
			Marco;
			OutTextXY(96,300,'**** Yo Gane *****');
			NoSound;
			DesplegarGanador:=1;
		End
		else
			if(Ganador(fig)=2)then
			Begin
				Sound(1000);
				Delay(1000);
				CLEARDEVICE;
				Marco;
				OutTextXY(96,300,'**** Usted Gana *****');
				NoSound;
				DesplegarGanador:=1;
			End
			else
				if(Cont=9)then
				Begin
					Sound(1000);
					Delay(1000);
					CLEARDEVICE;
					Marco;
					OutTextXY(96,300,'**** Gato *****');
					NoSound;
					DesplegarGanador:=0;
				End;
	End;}
End;

{**************************************************************}
Procedure Juego(turn:integer; fig:char);
Var
	movimiento:integer;
Begin
	Cont:=0;
	repeat
		if(Turn=1)then
		Begin
			repeat
				movimiento:= random(Celdas)-1;
			until(Board[movimiento]=' ') or (Cont=9);
			if(fig='X')then
				fig:='O'
			else
				fig:='X';
			Board[movimiento]:=fig;
			DibujarTirada(fig,movimiento);
			if(fig='X')then
				fig:='O'
			else
				fig:='X';
			Turn:=2;
		End
		else
		Begin
			AceptarTirada(fig);
			Turn:=1;
		End;
		Cont:=Cont+1;
	until(DesplegarGanador(fig)=1);
End;

{**************************************************************}
Begin
	GrMonitor:=Detect;
	InitGraph(GrMonitor, GrResol, '');
	Error:=GraphResult;
	if Error=grOk then
	Begin
		Presentacion;
		repeat
			Opcion;
			DibujaGato;
			Juego(Turn,Fig);
			{continuar juego}
			SetTextStyle(DefaultFont, HorizDir, 1);
			SetColor(14);
			OutTextXY(200,420,'Otro juego (S/N) ? =');
			repeat
				Resp:=readkey;
			until(Resp in ['S','s','N','n']);

		until(Resp in ['n','N']);
	End
	else
		writeln('Error de graficos: ', GraphErrorMsg(Error));
		closegraph;
End.