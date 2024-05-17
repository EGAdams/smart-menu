import sys
PROJECT_PATH = "/home/adamsl/smart-menu/python_menus/smart_menu/"
CONFIG_PATH  = "/home/adamsl/smart-menu/python_menus/smart_menu/menus/root_menu/"
sys.path.append( PROJECT_PATH )
from MenuManager import MenuManager
from Menu import Menu
if __name__ == "__main__":
    config_path = CONFIG_PATH + "root_config.json"
    menu = Menu()
    menu_manager = MenuManager(menu, config_path )
    menu_manager.load_menus()
    menu.display_and_select(menu_manager)
    