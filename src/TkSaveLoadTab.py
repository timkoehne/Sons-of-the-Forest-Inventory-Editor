import tkinter as tk
from TkSearchableCombobox import TkSearchableCombobox
from SavefileLoader import SavefileLoader
from TkInventoryTab import TkInventoryTab
from TkWorldTab import TkWorldTab


class TkSaveLoadTab(tk.Frame):
    def __init__(self, saveFileLoader: SavefileLoader, inventoryTab: TkInventoryTab, worldTab: TkWorldTab):
        super().__init__()
        
        self.saveFileLoader = saveFileLoader
        self.inventoryTab = inventoryTab
        self.worldTab = worldTab
        
        saveLoadFrame = tk.Frame(self)
        saveLoadFrame.pack(padx=5, pady=5)
        loadButton = tk.Button(saveLoadFrame, text="Load Savefolder", command=self.loadSavefile)
        loadButton.pack(ipadx=5, ipady=5, padx=5, pady=5)
        saveButton = tk.Button(saveLoadFrame, text="Save Savefolder", command=self.saveSavefile)
        saveButton.pack(ipadx=5, ipady=5, padx=5, pady=5)
        
    def loadSavefile(self):
        self.saveFileLoader.load()
        self.inventoryTab.refreshInventoryList()
        self.worldTab.refreshSettings()

    def saveSavefile(self):
        self.saveFileLoader.save()
