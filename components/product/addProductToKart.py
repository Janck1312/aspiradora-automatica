from helpers.showMessages import ShowMessages
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

class AddProductToKart(BoxLayout, ShowMessages):
    selectedPrdId = ""

    def __init__(self, *args, **kwargs):
        self.orientation = "vertical"
        self.padding = dp(10)
        self.spacing = dp(10)
        # Ajusta aquí el tamaño deseado (0.9 significa 90% del tamaño del cuadro de diálogo)
        self.size_hint = (0.9, None)
        self.height = dp(350)  # Ajusta aquí la altura deseada en píxeles
        BoxLayout.__init__(self, *args, **kwargs)

        if self.selectedPrdId!="":
            self.findPrdById(self.selectedPrdId)

    def calcTotalIVAAndTotal(self):
        price_u = 0
        quantity = 0
        tax_base = 0
        total_iva = 0

        price_u = self.ids.price_u.text
        quantity = self.ids.quantity.text
        if len(quantity) == 0 or quantity == "":
            self.showToast("Ingrese una cantidad válida del producto")
            return

        tax_base = float(quantity) * float(price_u)
        total_iva = (tax_base * float(self.ids.IVA.text))/100
        self.ids.total_iva.text = str(total_iva)
        self.ids.total.text = str(tax_base + total_iva)

    def getFormValues(self):
        return {
            "name_product": self.ids.name_product.text,
            "productId": self.selectedPrdId,
            "code": self.ids.code.text,
            "quantity": self.ids.quantity.text,
            "precio_u": self.ids.price_u.text,
            "IVA": self.ids.IVA.text,
            "total_iva": self.ids.total_iva.text,
            "total": self.ids.total.text,
        }

    def findPrdById(self, _id):
        ProductService().getRecord(_id=_id,
                                    on_success=self.onSuccessFindById,
                                    on_failure=ProductService.handleHttpErr)


    def onSuccessFindById(self, req, response):
        self.ids.name_product.text = response["name"]
        self.ids.code.text = response["code"]
        self.ids.quantity.text = "0"
        self.ids.price_u.text = str(response["price_sale"])
        self.ids.IVA.text = "16"
        self.ids.total_iva.text = "0"
        self.ids.total.text = "0"
