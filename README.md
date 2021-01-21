# Collidr
- File structure
- Game mechanics (back-end)
- Games mechanics (front-end)
## File structure
- /models : Contains the game models
- /prefabs : Contains the game class
- /scripts : Contains the game functions
- /textures : Contains the game textures
- keybinds.py : Contains the game keybinds in a dictionary
- main.py : The game "core", is launched for startup
- settings.py : Contains the user's settings
- tips.py : Contains de loading menu's tips

## Game mechanics (back-end)
### Starting
The starting of the game follows the following steps :
1. Initializing the Ursina app : ``Ursina()``
2. Inizializing the loading screen : ``LoadingScreen()``   
3. Loading the app-related settings (eg. window title) : ``applyVideoSettings()``
4. Loading the video-related settings (eg. graphics quality) : ``applyVideoSettings()``
5. Loading the entities in a separate thread : ``loadEntities()``   
6. Starting the app : ``app.run()``
7. When entities finished loading, the loading screen is destroyed : ``destroy(ld_scr)``
8. The main menu appears : ``MainMenu()``