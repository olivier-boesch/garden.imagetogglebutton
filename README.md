# kivy-imagetogglebutton
## What is about ?
A imagetogglebutton widget for kivy with default shapes. run __init__.py to see an example running. default shapes of button are provided (round, square, rounded square with or without line)

same concepts as the led widget : https://github.com/olivier-boesch/garden.led

## properties
### state
'down' or 'normal' as a toggle button
### toggle_type
three possible values :
- 'color' : changes the color when state changes (default colors try to match kivy default theme). colors can be set by the color_normal and color_down properties (these are list properties in the style of [red,green,blue,opacity]). you must set the source property with a greyscale image. the widget will color this image with color_normal or color_down.

- 'source' : set source_normal and source_down properties and the image will change according to state.

- 'both' : source AND color will change according to state. so, you must set color_down, color_normal, source_down and source_normal.

### color_down
the image color when the state is down (when toggle_type equals to color or both). it's a list of the style [r,g,b,opacity]
### color_normal
the image color when the state is normal (when toggle_type equals to color or both). it's a list of the style [r,g,b,opacity]
### source_down
image source when the state is down.
### source_normal
image source when the state is normal
