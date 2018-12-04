import sublime
import sublime_plugin


#main class
#テーブル名を受ける
class SqlCreatetableCommand(sublime_plugin.WindowCommand):

    def run(self):

        #テーブル名を受ける
        self.window.show_input_panel("Input TABLE NAME: ","",self.on_done,None,None)

    #入力完了時メソッド
    def on_done(self,word):

        #空だったら
        if word == "":
            self.window.run_command("テーブル名を入力して下さい。")
        else:
            #SqlCreatetableSubに値を渡して実行
            self.window.run_command("sql_createtable_sub",{"word":word})


#sub class
#CREATE TABLE文を生成
class SqlCreatetableSubCommand(sublime_plugin.TextCommand):

    def run(self,edit,word):

        #選択範囲を取得
        select_area = self.view.sel()

        #選択範囲の数だけループ
        for region in select_area:

            #選択範囲がない場合
            if region.empty():

                sublime.message_dialog("変換エリアを選んで下さい。")

            #複数選択していた場合
            elif len(select_area) >= 2:

                sublime.message_dialog("１ブロクだけ選択して下さい。")

            else:

                #選択範囲を文字列で取得
                area = self.view.substr(region)

                #１行毎に分割
                rows = area.split('\n')

                #変換用の文字列生成
                _str = ""
                _str = "DROP TABLE IF EXISTS " + word + ";\n"
                _str = "CREATE TABLE " + word + "(\n"

                #業の数だけループ
                for row in rows:

                    _str += "\t" + row.replace("\t"," ").rstrip() + ",\n"

                else:

                    #おしりの,と改行を削除
                    _str = _str.rstrip(",\n")
                    #\n);を追加
                    _str += "\n);"

                #選択範囲と入替え
                self.view.replace(edit, region, _str)

        else:
            pass