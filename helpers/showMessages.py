from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton

class ShowMessages:
    dialog = MDDialog
    button = MDFillRoundFlatButton

    def show_dialog(self, title: str, detail: str, on_dismiss = None):
        dialog = self.dialog(
            title=title,
            text=detail,
            type="alert",
            buttons={
                self.button(
                    text="Cerrar", on_release=lambda *args: dialog.dismiss()
                )
            }
        )

        if on_dismiss is not None:
            dialog.on_dismiss=lambda *args: on_dismiss()            
        dialog.open()
    

    def showToast(self,msg:str, on_dismiss = None)->None:
        _toast = toast
        
        if on_dismiss is not None:
            _toast.on_dismiss = lambda *args: on_dismiss()

        _toast(msg)

    def confirmationDialog(self, title, detail, on_accept, on_decline=None):
        dialog = self.dialog(
            title=title,
            text=detail,
            type="alert",
            buttons=[
                MDFlatButton(
                    text="Aceptar",
                    #theme_text_color="Custom",
                    #text_color=self.theme_cls.primary_color,
                    on_release=lambda *args: onAcceptConfirm(*args)
                ),
                MDFlatButton(
                    text="Cancelar",
                    #theme_text_color="Custom",
                    #text_color=self.theme_cls.primary_color,
                    on_release=lambda *args: dialog.dismiss()
                ),
            ]
        )

        def onAcceptConfirm(*args):
            on_accept(*args)
            dialog.dismiss()
        dialog.open()

    def dialogForm(self, title, detail, content, on_accept, on_decline=None):
        dialog = self.dialog(
            title=title,
            text=detail,
            type="custom",
            content_cls=content,
            anchor_y="top",
            top=1,
            buttons=[
                MDFlatButton(
                    text="Aceptar",
                    theme_text_color="Custom",
                    on_release=lambda *args:onAceptForm()

                ),
                MDFlatButton(
                    text="Cancelar",
                    theme_text_color="Custom",
                    on_release=lambda *args: dialog.dismiss()
                ),
            ]
        )

        def onAceptForm():
            on_accept()
            dialog.dismiss()
        dialog.open()
        