from kivymd.app import MDApp
from app_enums.user_permissions_enum import AppPermissionsEnum
from kivymd.uix.navigationdrawer import MDNavigationLayout
from app_enums.routes_enum import RoutesEnum
from components.common.menu_items.MenuItemsComponent import MenuItemsComponent

class MainNavigationLayout(MDNavigationLayout):
    """this class content of all app"""
    appRoutes = RoutesEnum() #set app routes
    appTitle = "Aspiradora Smart"
    appPermissions = AppPermissionsEnum() #set app permissions
    _menuItemsComponent = MenuItemsComponent()
    isDefinedMenu: bool = False
    
    def __init__(self, *args, **kwargs):
        MDNavigationLayout.__init__(self, *args, **kwargs)
    
    def enable_drawer(self):
        """enable the icon to open menu"""  
        self.ids.toolbar.left_action_items.append(
            ["menu", lambda x: self.ids.nav_drawer.set_state("open")]
        )
    
    def navigate_to(self, screen):
        """function to navigate around APP views"""
        if screen == self.appRoutes.dashboard:
            if self.isDefinedMenu is False:
                self.whichMenuStruct()
        self.ids.nav_drawer.set_state("close")
        self.ids.screen_manager.current = screen
    
    def whichMenuStruct(self):
        """DEFINE MENU STRUCT IN BASE TO USER IN SESSION"""
        self._menuItemsComponent.generateMenuItems()
        menu_container = self._menuItemsComponent.menu_container

        menu_header = self._menuItemsComponent.menu_header
        menu_divider = self._menuItemsComponent.menu_divider

        menu_container.add_widget(menu_header)
        menu_container.add_widget(menu_divider)

        menuItem = self._menuItemsComponent.dashboard
        menuItem.bind(on_release=lambda _: self.navigate_to(self.appRoutes.dashboard))
        menu_container.add_widget(menuItem)

        """menuItem = self._menuItemsComponent.logout
        menuItem.bind(on_release=lambda _: self.logout())
        menu_container.add_widget(menuItem)"""
        self.isDefinedMenu = True
        self.ids.content_nav.add_widget(menu_container)

    def logout(self):
        """Function to logOut the user in session"""
        self.ids.toolbar.left_action_items = []
        self.ids.nav_drawer.set_state("close")
        self.clearMenuItems()
        self.navigate_to(RoutesEnum.login)

    def clearMenuItems(self, *args, **kwargs):
        self.ids.content_nav.clear_widgets()
        self.isDefinedMenu = False

class MainApp(MDApp):
    """Main App Class"""
    def __init__(self, *args, **kwargs):
        MDApp.__init__(self, *args, **kwargs)

MainApp().run()#THIS LINE RUNS ALL APP
