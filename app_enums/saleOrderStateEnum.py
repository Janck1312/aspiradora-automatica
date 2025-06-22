class SaleOrderStateEnum:
    REJECTED = "REJECTED"
    APPROVED="APPROVED"
    PENDING = "PENDING"
    
SaleOrderStateEnumTraduction = {
    "APPROVED" : "Aprovada",
    "REJECTED" : "Anulada",
    "PENDING" : "Pendiente"
}

class SaleOrderTypeEnum:
    INVOICE = "INVOICE"
    ORDER = "ORDER"

SaleOrderTypeTraduction = {
    "INVOICE":"Factura",
    "ORDER":"Pedido"
}