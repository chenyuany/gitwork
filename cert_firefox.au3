
Func close_windows($fileTitle,$closeTitle)
	WinWait($fileTitle, "", 10)
	Sleep(1000)
	WinClose($fileTitle)
	If WinExists($closeTitle) Then
		$hWnd = WinGetHandle($closeTitle)
		ControlClick($hWnd, "", "Button2")
	EndIf
EndFunc