# Collidr
- File structure
- Game mechanics (back-end)
- Game mechanics (front-end)
## File structure
- /models : Contains the game models
- /prefabs : Contains the game class
- /scripts : Contains the game functions
- /textures : Contains the game textures
- keybinds.py : Contains the game keybinds in a dictionary
- main.py : The game "core", is launched for startup
- settings.py : Contains the user's settings
- tips.py : Contains the loading menu's tips

## Game mechanics (back-end)
### Starting
The starting of the game follows the following steps :
1. Initializing the Ursina app : ``Ursina()``
2. The main menu appears : ``MainMenu()``
3. If singleplayer is selected :
4. Initializing the loading screen : ``LoadingScreen()``   
5. Loading the app-related settings (eg. window title) : ``applyVideoSettings()``
6. Loading the video-related settings (eg. graphics quality) : ``applyVideoSettings()``
7. Loading the entities in a separate thread : ``loadEntities()``   
8. Starting the app : ``app.run()``
9. When entities have finished loading, the loading screen is destroyed : ``destroy(ld_scr)``