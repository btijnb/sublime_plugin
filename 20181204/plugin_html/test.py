import sublime
import sublime_plugin

class  ExampleCommand ( sublime_plugin . TextCommand ) : 
    def  run ( self ,  edit ) : 
        self . view . insert ( edit ,  0 ,  "Hello, World!" )








 # 입력 화면을 표시하는 스레드 
class  UserInputCommand ( sublime_plugin . WindowCommand ) : 
    def  run ( self ) : 
        # 입력 패널을 표시 
        self . window . show_input_panel ( "Input your name :" , "" , self . on_done , None , None )

    # 입력 완료 이벤트 
    def  on_done ( self , word ) :

        # 미입력 
        if  word  ==  "" : 
            sublime . message_dialog ( "문자를 입력하십시오." ) 
        # 입력있다 
        else : 
            # 다른 명령에 전달 
            self . window . run_command ( "output" , { "word" : word })

# 입력 값을 처리하는 스레드 
class  OutputCommand ( sublime_plugin . TextCommand ) : 
    #받을 
    def  run ( self , edit , word ) : 
        # 표시 
        sublime . message_dialog ( "받은 값은"  +  word  +  "입니다." )
    






