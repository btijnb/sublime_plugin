import sublime
import sublime_plugin


class  SelectAreaCommand ( sublime_plugin . TextCommand ) : 
    def  run ( self ,  edit ) :

        # 선택 범위 (시작 및 종료 지점)을 취득 
        sel_area  =  self . view . sel ()

        if  sel_area [ 0 ] . empty () : 
            # 어디도 선택되어 있지 않은 경우 
            sublime . message_dialog ( "어딘가 선택하십시오." ) 
        else : 
            # 선택 범위를 문자열로 가져 
            sel_string  =  self . view . substr ( sel_area [ 0 ]) 
            # 취득한 문자열을 출력 
            sublime . message_dialog ( sel_string )
