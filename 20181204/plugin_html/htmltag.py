import sublime
import sublime_plugin


class  HtmlTagCommand ( sublime_plugin . TextCommand ) : 
    def  run ( self , edit ) : 
        self . view . insert ( edit ,  0 ,  "div" )
        set_timeout()
