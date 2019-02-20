from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import ListProperty, OptionProperty, StringProperty
from kivy.uix.behaviors import ToggleButtonBehavior

class ImageToggleButton(ToggleButtonBehavior,Image):
    """Image toggle button widget for kivy"""
    # toggle_type : what does change when state changes (color, source or both)
    toggle_type = OptionProperty('color',options=['color','source','both'])
    # color_down : color when state is down
    color_down = ListProperty([0.22,0.79,1,1])
    # color_normal : color when state is normal
    color_normal = ListProperty([0.05,0.175,0.225,1])
    # source_down : image source when state is down
    source_down = StringProperty('')
    # source_normal : image source when state is normal
    source_normal = StringProperty('')
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        # force setting according to normal state
        self.on_state(None,'normal')
    
    def on_state(self,instance,state):
        if state=='down':
            if self.toggle_type == 'color' or self.toggle_type == 'both':
                self.color=self.color_down
            if self.toggle_type == 'source' or self.toggle_type == 'both':
                self.source=self.source_down
        else: # state=='normal'
            if self.toggle_type == 'source' or self.toggle_type == 'both':
                self.source=self.source_normal
            if self.toggle_type == 'color' or self.toggle_type == 'both':
                self.color=self.color_normal
    
    def on_source_down(self,instance,src):
        if self.state == 'down' and (self.toggle_type == 'source' or self.toggle_type == 'both'):
            self.source=self.source_down
            
    def on_source_normal(self,instance,src):
        if self.state == 'normal' and (self.toggle_type == 'source' or self.toggle_type == 'both'):
            self.source=self.source_normal
            
    def on_color_down(self,instance,clr):
        if self.state == 'down' and (self.toggle_type == 'color' or self.toggle_type == 'both'):
            self.color=self.color_down
            
    def on_color_normal(self,instance,clr):
        if self.state == 'normal' and (self.toggle_type == 'color' or self.toggle_type == 'both'):
            self.color=self.color_normal
            
    def on_toggle_type(self, instance, tp):
        if tp == 'source':
            # set color to white when toggle_type = 'source'
            self.color = [1,1,1,1]
            
# example to demonstrate imagetogglebutton widget capabilities
if __name__ == '__main__':
    from kivy.app import App
    from kivy.clock import Clock
    from kivy.lang.builder import Builder
    from kivy.uix.boxlayout import BoxLayout
    kvstr="""
BoxLayout:
    orientation: 'vertical'
    padding: 20
    Label:
        text: 'shapes'
    BoxLayout:
        orientation: 'horizontal'
        spacing: 20
        padding: 30
        ImageToggleButton:
            id: imgtggl_basicdisc
            source: 'shapes/basic_disc.png'
        ImageToggleButton:
            id: imgtggl_basicsquare
            source: 'shapes/basic_square.png'
        ImageToggleButton:
            id: imgtggl_basicsquarerounded
            source: 'shapes/basic_squarerounded.png'
        ImageToggleButton:
            id: imgtggl_contourdisc
            source: 'shapes/contour_disc.png'
        ImageToggleButton:
            id: imgtggl_contoursquare
            source: 'shapes/contour_square.png'
        ImageToggleButton:
            id: imgtggl_contoursquarerounded
            source: 'shapes/contour_squarerounded.png'
    Label:
        text: 'features'
    BoxLayout:
        orientation: 'horizontal'
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'toggle_type=color (default)'
            ImageToggleButton:
                id: imgtggl_typecolor
                source: 'shapes/basic_disc.png'
                color_normal: [1,0,0,1]
                color_down: [0,1,0,1]
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'toggle_type=source'
            ImageToggleButton:
                id: led_typesource
                toggle_type: 'source'
                source_down: 'media/yes.png'
                source_normal: 'media/no.png'
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'toggle_type=both'
            ImageToggleButton:
                id: imgtggl_typeboth
                toggle_type: 'both'
                source_down: 'shapes/basic_disc.png'
                source_normal: 'shapes/basic_square.png'
                color_normal: [1,0,0,1]
                color_down: [0,1,0,1]
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'with animated image'
            ImageToggleButton:
                id: imgtggl_animated
                toggle_type: 'both'
                source_down: 'media/fan.zip'
                source_normal: 'media/fan.png'"""
        
    
    class ImgToggleApp(App):
        def build(self):
            w=Builder.load_string(kvstr)
            return w

    ImgToggleApp().run()