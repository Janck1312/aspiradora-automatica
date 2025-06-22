from app_enums.events_enum import EventsEnum
from app_service.CacheService import CacheService
from components.product.addProductToKart import AddProductToKart
from events.on_add_productToKart import onAddProductToKart
from events.on_delete_record import onDeleteRecord
from events.on_edit_record import onEditRecord
from helpers.showMessages import ShowMessages
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from pages.product.productService import ProductService
from kivy.properties import ObjectProperty


class ProductCard(MDCard, ShowMessages, onDeleteRecord, onEditRecord, onAddProductToKart):
    '''Element to show every product one by one'''
    name:str = StringProperty()
    description:str = StringProperty()
    stock: int = NumericProperty()
    price:float = NumericProperty()
    price_purchase:float = NumericProperty()
    code:str = StringProperty()
    _id:str = StringProperty()
    card_id:str = StringProperty()
    photo = StringProperty()
    price_u = ""

    itemForBuyingKart = {}
    
    def deleteProduct(self):
        """Delete a product record"""
        self.confirmationDialog(
            detail="Realmente desea eliminar el producto??",
            title="Alerta !!!",
            on_accept=lambda _: ProductService().destroy(
                    _id=self._id,
                    on_success=self.onSuccessDeletedRecord,
                    on_failure=self.onFailureDeletedRecord
                ),
        )
        
        
    def editProduct(self)->None:
        """Edit a product record"""
        self.writeCache(key='productUpdate', obj={ "productId":self._id })
        self.dispatch(EventsEnum.on_edit_record)
    
    def onSuccessDeletedRecord(self, req, result):
        if 'acknowledged' in result:
            if result['acknowledged'] is True:
                self.showToast("Producto Eliminado con exito")
                self.dispatch(EventsEnum.on_delete_record)

    def onFailureDeletedRecord(self, req, result):
        if 'success' in result:
            if result['success'] is False:
                self.showToast(result['message'])
        elif type(result)==str:
            self.showToast(result)

    def openAddToKart(self):
        addProductToKart = AddProductToKart
        addProductToKart.selectedPrdId = self._id
        addProductToKart = addProductToKart()
        self.dialogForm(title="Añadir producto al carrito",
                        detail="",
                        content=addProductToKart,
                        on_accept=lambda *args: self.onAcceptProduct(
                            addProductToKart),
                        on_decline=lambda *args: self.dialogForm.dismiss()
                        )
        
    def onAcceptProduct(self, instance):
        self.itemForBuyingKart = None
        self.itemForBuyingKart = instance.getFormValues()
        self.dispatch(EventsEnum.on_add_prd_to_kart, self.itemForBuyingKart)

    def getItemForBuyingKart(self):
        return self.itemForBuyingKart
    