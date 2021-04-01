/***************************************************************
 * Name:      PruebaApp.cpp
 * Purpose:   Code for Application Class
 * Author:    Jovanny ()
 * Created:   2020-06-19
 * Copyright: Jovanny ()
 * License:
 **************************************************************/

#ifdef WX_PRECOMP
#include "wx_pch.h"
#endif

#ifdef __BORLANDC__
#pragma hdrstop
#endif //__BORLANDC__

#include "PruebaApp.h"
#include "PruebaMain.h"

IMPLEMENT_APP(PruebaApp);

bool PruebaApp::OnInit()
{
    PruebaFrame* frame = new PruebaFrame(0L);
    frame->SetIcon(wxICON(aaaa)); // To Set App Icon
    frame->Show();
    
    return true;
}
