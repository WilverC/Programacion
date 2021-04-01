/***************************************************************
 * Name:      PruebaMain.h
 * Purpose:   Defines Application Frame
 * Author:    Jovanny ()
 * Created:   2020-06-19
 * Copyright: Jovanny ()
 * License:
 **************************************************************/

#ifndef PRUEBAMAIN_H
#define PRUEBAMAIN_H



#include "PruebaApp.h"


#include "GUIFrame.h"

class PruebaFrame: public GUIFrame
{
    public:
        PruebaFrame(wxFrame *frame);
        ~PruebaFrame();
    private:
        virtual void OnClose(wxCloseEvent& event);
        virtual void OnQuit(wxCommandEvent& event);
        virtual void OnAbout(wxCommandEvent& event);
};

#endif // PRUEBAMAIN_H
