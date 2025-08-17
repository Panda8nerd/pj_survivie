from dearpygui import dearpygui as dpg
import periodictable

################################################################################################################################################################
def show_page(page_tag):
    for page in ["page1", "page2", "page3"]:
        dpg.hide_item(page)
    dpg.show_item(page_tag)
################################################################################################################################################################

 def function3():
    with dpg.texture_registry(show=False):
        width, height, channels, data = dpg.load_image(your path to periodic photo file)
        dpg.add_static_texture(width, height, data, tag="my_texture")
    dpg.add_image("my_texture", width=1000, height=600)
                     
################################################################################################################################################################
def main_app():
    activate = False
    dpg.create_context()
    dpg.create_viewport(title="Single Window with Pages", width=1920, height=1080)

    with dpg.window(label="Main App", width=1920, height=1080):
        with dpg.group(horizontal=True):
            dpg.add_button(label="Home", callback=lambda: show_page("page1"))
            dpg.add_button(label="Settings", callback=lambda: show_page("page2"))
            dpg.add_button(label="About", callback=lambda: show_page("page3"))

        dpg.add_separator()

        with dpg.child_window(tag="page1", width=-1, height=-1):
            dpg.add_text("Welcome to the Home Page!")
            dpg.add_button(label="Say Hello", callback=lambda: print("Hello from Home!"))
            
        with dpg.child_window(tag="page2", width=-1, height=-1, show=False):
            dpg.add_text("Settings Page")
            dpg.add_checkbox(label="Enable feature X")
            dpg.add_input_text(label="Username")
            
        with dpg.child_window(tag="page3", width=-1, height=-1, show=False):
            dpg.add_text("Function Page")
            dpg.add_input_text(label="input atomic number of elements")

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

################################################################################################################################################################
