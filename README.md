# Booting up mods for minecraft 1.20.1

## Personal Mod Playlist
This repo is for my personal mods that includes a small python script to automatically pull all `.jar` files into the parent repo

## Usage

### For Windows
Make sure you've cd in the `.minecraft` directory located in
```bash
AppData\Roaming\.minecraft\
```
Then clone the repo:
```bash
git clone https://github.com/ihni/mod_loader.git
```
CD into the repo:
```bash
cd mod_loader
```
And run the python script to copy the mods into the `mods` folder for Minecraft
```bash
python mod_loader.py
```
> [!IMPORTANT]  
> This will not clear the mod folder, it is important that the mods folder is cleared of all mods to avoid dependency issues or else crashes will occur