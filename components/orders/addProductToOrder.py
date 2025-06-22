from app_service.CacheService import CacheService
from helpers.showMessages import ShowMessages
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.uix.dropdown import DropDown
from kivymd.uix.button import MDFlatButton
from kivymd.uix.widget import MDWidget
from pages.product.productService import ProductService
from kivymd.uix.menu import MDDropdownMenu


class AddProductToOrder(BoxLayout, ShowMessages, CacheService):

    isOrderSale:bool = False

    def __init__(self, *args, **kwargs):
        self.orientation = "vertical"
        self.padding = dp(10)
        self.spacing = dp(10)
        # Ajusta aquí el tamaño deseado (0.9 significa 90% del tamaño del cuadro de diálogo)
        self.size_hint = (0.9, None)
        self.height = dp(350)  # Ajusta aquí la altura deseada en píxeles
        BoxLayout.__init__(self, *args, **kwargs)

    def searchProducts(self, text=""):
        #if len(text) == 0:
        #    self.showToast("Ingrese el nombre del producto o algun valor relacionado a el")
        #    return
        ProductService().getRecords(search=text, on_success=self.onSuccessFindProducts, on_failure=self.onFailureFindPrds)

    def onSuccessFindProducts(self, req, result):
        menu_items = []
        if len(result) == 0:
            menu_items = [{
                "text": "No se encontraron productos",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Hot Dog": self.selectProduct(x),
            }]
        else:
            for product in result:
                menu_items.append(
                    {
                        "text": f"{product['code']} - {product['name']}", 
                        "viewclass": "OneLineListItem", 
                        "on_release": lambda x=f"{product['_id']}": self.selectProduct(x)
                    }
                )

        menu = MDDropdownMenu(
            caller=self.ids.search_input,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        menu.open()

    def onFailureFindPrds(self, req, result):
        if type(result) == str:
            self.showToast(result or "Error en la peticion")
        else:
            if "success" in result:
                self.showToast(result["message"])

    def selectProduct(self, productId):
        def fillForm(req, product):           
            self.ids.code.text = str(product['code'])
            self.ids.name_product.text = product['name']
            #self.ids.quantity.text= "0"
            self.ids.price_u.text = str(product['price_purchase']) if self.isOrderSale is False else str(product['price_sale'])
            self.ids.total_iva.text = "00.0"
            self.ids.total.text = "00.0"
            self.productId = productId
        def onFailedFinPrd(req, result):
            if type(result) == str:
                self.showToast(result or "Error en la peticion")
            else:
                if "success" in result:
                    self.showToast(result["message"])
            
        ProductService().getRecord(productId, fillForm, onFailedFinPrd)

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
            "name_product":self.ids.name_product.text,
            "productId":self.productId,
            "code": self.ids.code.text,
            "quantity":self.ids.quantity.text,
            "precio_u":self.ids.price_u.text,
            "IVA":self.ids.IVA.text,
            "total_iva":self.ids.total_iva.text,
            "total":self.ids.total.text,
        }
