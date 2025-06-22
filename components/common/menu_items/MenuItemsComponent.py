from kivymd.uix.navigationdrawer.navigationdrawer import MDNavigationDrawerItem
from kivy.metrics import dp
from kivymd.uix.navigationdrawer import MDNavigationDrawerHeader, MDNavigationDrawerDivider, MDNavigationDrawerMenu, MDNavigationDrawer

class MenuItemsComponent:
    """CLASS THAT WILL DEFINE MENU ITEMS"""

    def __init__(self):
        self.orders = None
        self.logout = None
        self.products = None
        self.dashboard = None

    def generateMenuItems(self):
        self.dashboard = MDNavigationDrawerItem(
            icon="home",
            text="Inicio"
        )

        self.products = MDNavigationDrawerItem(
            icon="storefront",
            text="Historial de uso"
        )

        self.menu_header = MDNavigationDrawerHeader(
            title="Menú",
            title_color="#4a4939",
            text="",
            spacing=(dp(1)),
            padding=(dp(3), 0, 0, dp(18))
        )

        self.menu_container = MDNavigationDrawerMenu()

        self.menu_navigation_drawer = MDNavigationDrawer(
            id="nav_drawer",
            radius=(0, 14, 14, 0),
            type="standard",
            close_on_click=True
        )

        self.menu_divider = MDNavigationDrawerDivider()



