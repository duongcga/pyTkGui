#------------------------------------------------
from tkinter import *
from tkinter.ttk import Combobox, Notebook, Progressbar, Separator, Sizegrip, Treeview
from tkinter.colorchooser import *
from tkinter.filedialog import *
from Strings import *
#------------------------------------------------
tMouseButtonLeft = 1
tMouseButtonMiddle = 2
tMouseButtonRight = 3

tPathTypeFolder = 0
tPathTypeFileAsOpen = 1
tPathTypeFileAsSave = 2    
tPathTypeDefault = tPathTypeFolder

tFileFilterAll = 'All File (*.*)|*.*'
#------------------------------------------------
class cBaseWindow: pass
class cButton: pass
class cCheckBox: pass
class cComboBox: pass
class cComboBox: pass
class cEntryBox: pass
class cLabel: pass
class cLinkLabel: pass
class cNumericUpDown: pass
class cProgressBar: pass
class cRadioButton: pass
class cSeparatorBar: pass
class cTrackBar: pass
class cControls: pass
#CheckedListBox, DateTimePicker, DomainUpDown, ListView, MaskedTextBox, MonthCalendar, PropertyGrid, RichTextBox
#------------------------------------------------
class cComponent:
    #RightToLeft, UseMnemonic, Minimumnsize, Maximumsize, padding, margin, location, size
    tReliefNone = 0
    tReliefFlat = 1
    tReliefRaised = 2
    tReliefSunken = 3
    tReliefGroove = 4
    tReliefRidge = 5
    tReliefSolid = 6
    tReliefUnkown = 7
    tReliefDefault = tReliefFlat
    
    __sIdentityCounter = 0
    
    @property
    def Identity(self) -> int:
        return self.__mIdentity
    
    @property
    def TkComponent(self): 
        return self.__mTkComponent
    
    @property
    def Tag(self):
        return self.__mTag
    
    @Tag.setter
    def Tag(self, value):
        self.__mTag = value

    @property
    def BackColor(self):
        try:
            return self.__mTkComponent["background"]
        except:
            return tStringEmpty          
        
    @BackColor.setter
    def BackColor(self, value):        
        try:
            self.__mTkComponent["background"] = value
        except:
            pass
    
    #@property
    #def ActiveBackColor(self):
        #try:
            #return self.__mTkComponent["activebackground"]
        #except:
            #return tStringEmpty          
        
    #@ActiveBackColor.setter
    #def ActiveBackColor(self, value):        
        #try:
            #self.__mTkComponent["activebackground"] = value
        #except:
            #pass
    
    @property
    def ForeColor(self):
        try:
            return self.__mTkComponent["foreground"]
        except:
            return tStringEmpty          
        
    @ForeColor.setter
    def ForeColor(self, value):        
        try:
            self.__mTkComponent["foreground"] = value
        except:
            pass
    
    #@property
    #def ActiveForeColor(self):
        #try:
            #return self.__mTkComponent["activeforeground"]
        #except:
            #return tStringEmpty          
        
    #@ActiveForeColor.setter
    #def ActiveForeColor(self, value):        
        #try:
            #self.__mTkComponent["activeforeground"] = value
        #except:
            #pass
        
    @property
    def BorderSize(self) -> int:
        try:
            return self.__mTkComponent["borderwidth"]
        except:
            return tStringEmpty          


    @BorderSize.setter
    def BorderSize(self, value: int):        
        try:
            self.__mTkComponent["borderwidth"] = value
        except:
            pass
        
    @property
    def Cursor(self) -> str:
        try:
            return self.__mTkComponent["cursor"]
        except:
            return tStringEmpty        

    @Cursor.setter   
    def Cursor(self, value: str):
        try:
            self.__mTkComponent["cursor"] = value
        except:
            pass
    
    @property
    def Font(self):
        try:
            return self.__mTkComponent["font"]
        except:
            return tStringEmpty        

    @Font.setter   
    def Font(self, value):
        try:
            self.__mTkComponent["font"] = value
        except:
            pass
        
    @property
    def Enabled(self) -> bool:
        try:
            return True if (self.__mTkComponent["state"] != DISABLED) else False
        except:
            return True        

    @Enabled.setter   
    def Enabled(self, value: bool):
        try:
            if (value):
                if (self.__mTkComponent["state"] == DISABLED):
                    self.__mTkComponent["state"] = NORMAL
            else:
                self.__mTkComponent["state"] = DISABLED
        except:
            pass
    
    @property
    def IsViewable(self) -> bool:
        return self.__mTkComponent.winfo_viewable()
    
    @property
    def Name(self) -> str:
        return self.__mTkComponent.winfo_name()
    
    @property
    def ClassName(self) -> str:
        return self.__mTkComponent.winfo_class()
    
    @property
    def Relief(self) -> int:
        try:
            relief = self.__mTkComponent["relief"]
            if (anchor == FLAT):
                return cComponent.tReliefFlat
            elif (justify == RAISED):
                return cComponent.tReliefRaised
            elif (justify == SUNKEN):
                return cComponent.tReliefSunken
            elif (anchor == GROOVE):
                return cComponent.tReliefGroove
            elif (justify == RIDGE):
                return cComponent.tReliefRidge
            elif (justify == SOLID):
                return cComponent.tReliefSolid         
            else:
                return cComponent.tReliefNone
        except:
            return cComponent.tReliefUnkown         

    @Relief.setter
    def Relief(self, value: int):        
        try:
            if (value == cComponent.tReliefFlat):
                self.__mTkComponent["relief"] = FLAT
            elif (value == cComponent.tReliefRaised):
                self.__mTkComponent["relief"] = RAISED
            elif (value == cComponent.tReliefSunken):
                self.__mTkComponent["relief"] = SUNKEN
            elif (value == cComponent.tReliefGroove):
                self.__mTkComponent["relief"] = GROOVE
            elif (value == cComponent.tReliefRidge):
                self.__mTkComponent["relief"] = RIDGE
            elif (value == cComponent.tReliefSolid):
                self.__mTkComponent["relief"] = SOLID
        except:
            pass
        
    @property
    def TabStop(self) -> bool:
        try:
            return (self.__mTkComponent["takefocus"] == tStringEmpty)
        except:
            return False          


    @TabStop.setter
    def TabStop(self, value: bool):        
        try:
            self.__mTkComponent["takefocus"] = tStringEmpty if value else "NoFocus"
        except:
            pass
        
    @property
    def X(self) -> int:
        return self.__mTkComponent.winfo_x
    
    @property
    def Y(self) -> int:
        return self.__mTkComponent.winfo_y
    
    @property
    def Width(self) -> int:
        return self.__mTkComponent.winfo_width
    
    @property
    def Height(self) -> int:
        return self.__mTkComponent.winfo_height
    
    @property
    def __IsCreated(self):
        return (self.__mTkComponent != None)
    
    def SetMouseDownHandler(self, handler):
        if (self.__mMouseDownHandler != None):
            self.__mMouseDownHandler = None
            self.__mTkComponent.unbind("<Button-1>", self.__OnMouseEventHandler)
            self.__mTkComponent.unbind("<Button-2>", self.__OnMouseEventHandler)
            self.__mTkComponent.unbind("<Button-3>", self.__OnMouseEventHandler)        
        if (handler != None):       
            self.__mMouseDownHandler = handler
            self.__mTkComponent.bind("<Button-1>", self.__OnMouseEventHandler)
            self.__mTkComponent.bind("<Button-2>", self.__OnMouseEventHandler)
            self.__mTkComponent.bind("<Button-3>", self.__OnMouseEventHandler)
    
    def SetMouseUpHandler(self, handler):
        if (self.__mMouseUpHandler != None):
            self.__mMouseUpHandler = None
            self.__mTkComponent.unbind("<ButtonRelease-1>", self.__OnMouseEventHandler)
            self.__mTkComponent.unbind("<ButtonRelease-2>", self.__OnMouseEventHandler)
            self.__mTkComponent.unbind("<ButtonRelease-3>", self.__OnMouseEventHandler)        
        if (handler != None):       
            self.__mMouseUpHandler = handler
            self.__mTkComponent.bind("<ButtonRelease-1>", self.__OnMouseEventHandler)
            self.__mTkComponent.bind("<ButtonRelease-2>", self.__OnMouseEventHandler)
            self.__mTkComponent.bind("<ButtonRelease-3>", self.__OnMouseEventHandler)
            
    def SetMouseMoveHandler(self, handler):
        if (self.__mMouseMoveHandler != None):
            self.__mMouseMoveHandler = None
            self.__mTkComponent.unbind("<B1-Motion>", self.__OnMouseEventHandler)
            self.__mTkComponent.unbind("<B2-Motion>", self.__OnMouseEventHandler)
            self.__mTkComponent.unbind("<B3-Motion>", self.__OnMouseEventHandler)        
        if (handler != None):       
            self.__mMouseMoveHandler = handler
            self.__mTkComponent.bind("<B1-Motion>", self.__OnMouseEventHandler, "+")
            self.__mTkComponent.bind("<B2-Motion>", self.__OnMouseEventHandler, "+")
            self.__mTkComponent.bind("<B3-Motion>", self.__OnMouseEventHandler, "+")
            
    def SetMouseDoubleClickHandler(self, handler):
        if (self.__mMouseDoubleClickHandler != None):
            self.__mMouseDoubleClickHandler = None
            self.__mTkComponent.unbind("<Double-Button-1>", self.__OnMouseDoubleClickHandler)
            self.__mTkComponent.unbind("<Double-Button-2>", self.__OnMouseDoubleClickHandler)
            self.__mTkComponent.unbind("<Double-Button-3>", self.__OnMouseDoubleClickHandler)        
        if (handler != None):       
            self.__mMouseDoubleClickHandler = handler
            self.__mTkComponent.bind("<Double-Button-1>", self.__OnMouseDoubleClickHandler, "+")
            self.__mTkComponent.bind("<Double-Button-2>", self.__OnMouseDoubleClickHandler, "+")
            self.__mTkComponent.bind("<Double-Button-3>", self.__OnMouseDoubleClickHandler, "+")
        
    def Update(self):
        self.__mTkComponent.update()
    
    def __OnMouseEventHandler(self, event):
        if (event.type == "4"):
            if (self.__mMouseDownHandler != None):
                self.__mMouseDownHandler(self, event.num, event.x, event.y)
        elif (event.type == "5"):
            if (self.__mMouseUpHandler != None):
                self.__mMouseUpHandler(self, event.num, event.x, event.y)         
        elif (event.type == "6"):
            if (self.__mMouseMoveHandler != None):
                self.__mMouseMoveHandler(self, event.num, event.x, event.y) 
    
    def __OnMouseDoubleClickHandler(self, event):
        if (self.__mMouseDoubleClickHandler != None):
            self.__mMouseDoubleClickHandler(self, event.num, event.x, event.y)
    
    def __init__(self, tkComponent):        
        self.__mIdentity = cComponent.__sIdentityCounter
        cComponent.__sIdentityCounter += 1
        self.__mTkComponent = tkComponent
        self.__mMouseDownHandler = None
        self.__mMouseMoveHandler = None
        self.__mMouseUpHandler = None
        self.__mMouseDoubleClickHandler = None
        self.__mTag = None
        
    def __del__(self):
        self.__mTkComponent = None
        self.__mMouseDownHandler = None
        self.__mMouseMoveHandler = None
        self.__mMouseUpHandler = None
        self.__mMouseDoubleClickHandler = None
        
    @staticmethod
    def GetColorAsHex(color: int) -> str:
        return '#%02x%02x%02x' % (color % 256, (color // 256) % 256, color // 65536)
    
    @staticmethod    
    def UIGetColor(initColor: int = 0) -> int:
        color = askcolor(cComponent.GetColorAsHex(initColor))
        if (color[0] == None):
            return -1
        return (int(color[0][0]) + int(color[0][1]) * 256 + int(color[0][2]) * 256 * 256)
    
    @staticmethod
    def UIGetPath(pathType: int = 0, pathFilter: str = tFileFilterAll) -> str:
        try:
            if (pathType == tPathTypeFolder):
                return askdirectory()
            if (pathFilter == tStringEmpty):
                pathFilter = tFileFilterAll                
            # All File (*.*)|*.*|Text Files (*.txt)|*.txt
            items = pathFilter.split("|")
            fileFilter = []
            for i in range(0, (len(items) // 2)):
                itemFilter = (items[i * 2], items[i * 2 + 1])
                fileFilter.append(itemFilter)
            items = None
            if (pathType == tPathTypeFileAsOpen):
                path = askopenfile(filetypes = fileFilter)
            elif (pathType == tPathTypeFileAsSave):
                path = asksaveasfile(filetypes = fileFilter)
            else:
                path = tStringEmpty
            fileFilter = None
            if (path != tStringEmpty):
                path = path.name
            return path
        except:
            pass
        return tStringEmpty
#------------------------------------------------
class cControl(cComponent):
    tTypeNone = 0
    tTypeButton = 1
    tTypeCanvas = 2
    tTypeCheckBox = 3
    tTypeComboBox = 4
    tTypeCorlorBrowser = 45
    tTypeEntryBox = 5
    tTypeGroupBox = 6
    tTypeLabel = 7
    tTypeLinkLabel = 7
    tTypeListBox = 8
    tTypeNumericUpDown = 16
    tTypePanel = 9
    tTypePathBrowser = 92
    tTypePictureBox = 91
    tTypeProgressBar = 10
    tTypeRadioButton = 11
    tTypeScrollBar = 12
    tTypeSeparatorBar = 13
    tTypeSizeGrip = 14
    tTypeSpinBox = 141
    tTypeTrackBar = 15    
    tTypeSplitContainer = 17
    tTypeStatusBar = 18
    tTypeTabControl = 19
    tTypeTextBox = 20
    tTypeToolBar = 21
    tTypeTreeView = 22        
    
    tAnchorNone = 0
    tAnchorLeft = 1
    tAnchorTop = 2
    tAnchorRight = 4
    tAnchorBottom = 8
    tAnchorDefault = tAnchorNone
    
    tDockNone = 0
    tDockLeft = 1
    tDockTop = 2
    tDockRight = 3
    tDockBottom = 4
    tDockFill = 5
    tDockDefault = tDockNone
    
    tDirectionNone = 0
    tDirectionLeft = 1
    tDirectionTop = 2
    tDirectionRight = 3
    tDirectionBottom = 4
    tDirectionDefault = tDirectionNone
    
    tOrientNone = 0
    tOrientHorizontal = 1
    tOrientVertical = 2
    tOrientDefault = tOrientNone
    
    tTextAlignNone = 0
    tTextAlignTopLeft = 1
    tTextAlignTopCenter = 2
    tTextAlignTopRight = 3
    tTextAlignMiddleLeft = 4
    tTextAlignMiddleCenter = 5
    tTextAlignMiddleRight = 6
    tTextAlignBottomLeft = 7
    tTextAlignBottomCenter = 8
    tTextAlignBottomRight = 9
    tTextAlignDefault = tTextAlignMiddleLeft
    
    tTextJustifyNone = 0
    tTextJustifyLeft = 1
    tTextJustifyCenter = 2
    tTextJustifyRight = 3
    tTextJustifyDefault = tTextJustifyCenter
    
    tTextImageRelationNone = 0
    tTextImageRelationOverlay = 1
    tTextImageRelationImageAboveText = 2
    tTextImageRelationTextAboveImage = 3
    tTextImageRelationImageBeforeText = 4
    tTextImageRelationTextBeforeImage = 5
    tTextImageRelationUnkown = 6
    tTextImageRelationDefault = tTextImageRelationNone

    #@property
    #def Anchor(self) -> int:
        #return self.__mAnchor
        
    #@Anchor.setter
    #def Anchor(self, value: int):
        #self.__mAnchor = value
    
    @property
    def Type(self) -> int:
        return cControl.tTypeNone
            
    @property
    def TkControl(self) -> Widget: 
        return self.TkComponent
    
    @property
    def Parent(self) -> cControls:
        return self.__mParent
    
    @Parent.setter
    def Parent(self, parent: cControls):
        self.__mParent = parent        
    
    @property
    def Dock(self) -> int:
        info = self.TkComponent.pack_info()
        side = info["side"]
        expand = info["expand"]
        info = None
        if (expand):
            return cControl.tDockFill
        if (side == "left"):
            return cControl.tDockLeft
        elif (side == "top"):
            return cControl.tDockTop
        elif (side == "right"):
            return cControl.tDockRight
        elif (side == "bottom"):
            return cControl.tDockBottom            
        return cControl.tDockNone
        
    @Dock.setter
    def Dock(self, value: int):
        if (value == cControl.tDockLeft):
            self.TkComponent.pack(side = "left", expand = False, fill = BOTH)
        elif (value == cControl.tDockTop):
            self.TkComponent.pack(side = "top", expand = False, fill = BOTH)
        elif (value == cControl.tDockRight):
            self.TkComponent.pack(side = "right", expand = False, fill = BOTH)
        elif (value == cControl.tDockBottom):
            self.TkComponent.pack(side = "bottom", expand = False, fill = BOTH)
        elif (value == cControl.tDockFill):
            self.TkComponent.pack(expand = True, fill = BOTH)
            
    @property
    def HasControls(self) -> bool:
        return False
    
    @property
    def Index(self) -> int:
        if (self.__mParent != None):
            return self.__mParent.IndexOf(self)
        return -1
    
    @property
    def Visible(self) -> bool:
        try:
            return True if (len(self.TkComponent.place_info()) > 0) else False
        except:
            return False
        
    @Visible.setter
    def Visible(self, value: bool):
        if (value == self.Visible):
            return
        try:
            if (value):
                self.TkComponent.place(self.TkComponent.__PlaceInfo)
                del self.TkComponent.__PlaceInfo
            else:
                self.TkComponent.__PlaceInfo = self.TkComponent.place_info()
                self.TkComponent.place_forget()
        except:
            pass        
    
    @property
    def Window(self) -> cBaseWindow:
        parent = self.__mParent
        while (parent != None):            
            if (isinstance(parent, cBaseWindow)):
                return parent
            parent = parent.Parent
        return None    
    
    def Delete(self) -> bool:
        if (self.__mParent == None):
            return False
        self.__mParent.RemoveAt(self.Index)
        
    def MoveToBack(self):
        if (self.__mParent != None):
            self.__mParent.MoveToBack(self.Index)
            
    def MoveToFront(self):
        if (self.__mParent != None):
            self.__mParent.MoveToFront(self.Index) 
    
    def SetBounds(self, x: int, y: int, width: int, height: int):
        self.TkComponent.place(x = x, y = y, width = width, height = height)
    
        def SetLocation(self, x: int, y: int):
            self.TkComponent.place(x = x, y = y)
    
        def SetSize(self, width: int, height: int):
            self.TkComponent.place(width = width, height = height)
            
    def __init__(self, parent: cControls, tkWidget: Widget):
        super().__init__(tkWidget)
        self.__mParent = parent
        self.__mMouseDownHandler = None
        self.__mMouseMoveHandler = None
        self.__mMouseUpHandler = None
        self.__mMouseDoubleClickHandler = None
        
    def __del__(self):
        self.__mMouseDownHandler = None
        self.__mMouseMoveHandler = None
        self.__mMouseUpHandler = None
        self.__mMouseDoubleClickHandler = None
        
    @staticmethod
    def GetOrientByDirection(direction: int, reverseOrient: bool = False) -> int:
        if ((direction == cControl.tDirectionLeft) or (direction == cControl.tDirectionRight)):
            return cControl.tOrientVertical if reverseOrient else cControl.tOrientHorizontal
        if ((direction == cControl.tDirectionTop) or (direction == cControl.tDirectionBottom)):
            return cControl.tOrientHorizontal if reverseOrient else cControl.tOrientVertical
        else:
            return cControl.tOrientNone    
#------------------------------------------------
class __cBaseLabel(cControl):
    @property
    def Image(self) -> Image:
        return self.TkControl["image"]
    
    @Image.setter
    def Image(self, value: Image):
        self.TkControl["image"] = value

    @property
    def Text(self) -> str:
        return self.TkControl["text"]
        
    @Text.setter
    def Text(self, value: str):
        self.TkControl["text"] = value
    
    @property
    def TextAlign(self) -> int:
        try:
            anchor = self.TkControl["anchor"]
            if (anchor == NW):
                return cControl.tTextAlignTopLeft
            elif (justify == N):
                return cControl.tTextAlignTopCenter
            elif (justify == NE):
                return cControl.tTextAlignTopRight
            elif (anchor == W):
                return cControl.tTextAlignMiddleLeft
            elif (justify == CENTER):
                return cControl.tTextAlignMiddleCenter
            elif (justify == E):
                return cControl.tTextAlignMiddleRight
            elif (anchor == SW):
                return cControl.tTextAlignBottomLeft
            elif (justify == S):
                return cControl.tTextAlignBottomCenter
            elif (justify == SE):
                return cControl.tTextAlignBottomRight            
            else:
                return cControl.tTextAlignNone
        except:
            return cControl.tTextAlignNone

    @TextAlign.setter
    def TextAlign(self, value: int):
        try:
            if (value == cControl.tTextAlignTopLeft):
                self.TkControl["anchor"] = NW
            elif (value == cControl.tTextAlignTopCenter):
                self.TkControl["anchor"] = N
            elif (value == cControl.tTextAlignTopRight):
                self.TkControl["anchor"] = NE
            elif (value == cControl.tTextAlignMiddleLeft):
                self.TkControl["anchor"] = W
            elif (value == cControl.tTextAlignMiddleCenter):
                self.TkControl["anchor"] = CENTER
            elif (value == cControl.tTextAlignMiddleRight):
                self.TkControl["anchor"] = E
            elif (value == cControl.tTextAlignBottomLeft):
                self.TkControl["anchor"] = SW
            elif (value == cControl.tTextAlignBottomCenter):
                self.TkControl["anchor"] = S
            elif (value == cControl.tTextAlignBottomRight):
                self.TkControl["anchor"] = SE
        except:
            pass
        
    @property
    def TextJustify(self) -> int:
        try:
            justify = self.TkControl["justify"]
            if (justify == LEFT):
                return cControl.tTextJustifyLeft
            elif (justify == CENTER):
                return cControl.tTextJustifyCenter
            elif (justify == RIGHT):
                return cControl.tTextJustifyRight
            else:
                return cControl.tTextJustifyNone
        except:
            return cControl.tTextJustifyNone

    @TextJustify.setter
    def TextJustify(self, value: int):
        try:
            if (value == cControl.tTextJustifyLeft):
                self.TkControl["justify"] = LEFT
            elif (value == cControl.tTextJustifyCenter):
                self.TkControl["justify"] = CENTER
            elif (value == cControl.tTextJustifyRight):
                self.TkControl["justify"] = RIGHT            
        except:
            pass
    
    @property
    def TextImageRelation(self) -> int:
        try:
            compound = self.TkControl["compound"]
            if (compound == LEFT):
                return cControl.tTextImageRelationImageBeforeText
            elif (compound == TOP):
                return cControl.tTextImageRelationImageAboveText
            elif (compound == RIGHT):
                return cControl.tTextImageRelationTextBeforeImage            
            elif (compound == BOTTOM):
                return cControl.tTextImageRelationTextAboveImage
            elif (compound == CENTER):
                return cControl.tTextImageRelationOverlay
            else:
                return cControl.tTextImageRelationNone
        except:
            return cControl.tTextImageRelationUnkown
        
    @TextImageRelation.setter
    def TextImageRelation(self, value: int):
        try:
            if (value == cControl.tTextImageRelationImageBeforeText):
                self.TkControl["compound"] = LEFT
            elif (value == cControl.tTextImageRelationImageAboveText):
                self.TkControl["compound"] = TOP
            elif (value == cControl.tTextImageRelationTextBeforeImage):
                self.TkControl["compound"] = RIGHT     
            elif (value == cControl.tTextImageRelationTextAboveImage):
                self.TkControl["compound"] = BOTTOM
            elif (value == cControl.tTextImageRelationOverlay):
                self.TkControl["compound"] = CENTER  
            elif (value == cControl.tTextImageRelationNone):
                self.TkControl["compound"] = NONE                  
        except:
            pass
    
    def LoadImage(self, path: str) -> bool:
        image = None 
        try:
            image = PhotoImage(file = path)
        except:
            pass
        if (image != None):
            self.Image = image
            
    def __init__(self, parent: cControls, tkWidget: Widget):
        super().__init__(parent, tkWidget)

    def __call__(self, text: str):
        self.Text = text
#------------------------------------------------
class __cBaseButton(__cBaseLabel):
    def RaiseClick(self):
        self.invoke()
    
    def SetClickHandler(self, handler):
        if (self.__mClickHandler != None):
            self.__mClickHandler = None
            self.TkControl.config(command = None)
        if (handler != None):
            self.__mClickHandler = handler
            self.TkControl.config(command = self.__OnClickHandler)
    
    def __OnClickHandler(self):
        if (self.__mClickHandler != None):
            self.__mClickHandler(self)
    
    def __init__(self, parent: cControls, tkWidget: Widget):
        super().__init__(parent, tkWidget)
        self.__mClickHandler = None
    
    def __del__(self):
        self.__mClickHandler = None
#------------------------------------------------
class __cBaseContainer(cControl):
    @property
    def Controls(self):
        return self.__mControls
    
    @property
    def HasControls(self) -> bool:
        return ((self.__mControls != None) and (self.__mControls.Count > 0))
    
    def SetDockAll(self, dock: int):
        for i in range(0, self.Controls.Count):
            self.Controls[i].Dock = dock
    
    def __init__(self, parent: cControls, tkWidget: Widget):
        super().__init__(parent, tkWidget)
        self.__mControls = cControls(self)
        
    def __del__(self):
        self.__mControls = None
#------------------------------------------------
class __cBaseStripBar(__cBaseContainer):
    @property
    def Direction(self) -> int:
        return self.__mDirection
        
    @Direction.setter
    def Direction(self, value: int):        
        if (value == cControl.tDirectionLeft):
            self.SetDockAll(cControl.tDockLeft)
        elif (value == cControl.tDirectionTop):
            self.SetDockAll(cControl.tDockTop)
        elif (value == cControl.tDirectionRight):
            self.SetDockAll(cControl.tDockRight)
        elif (value == cControl.tDirectionBottom):
            self.SetDockAll(cControl.tDockBottom)
        for i in range(0, self.Controls.Count):
            control = self.Controls[i]
            if (control.Type == cControl.tTypeSeparatorBar):
                control.Orient = cControl.GetOrientByDirection(self.__mDirection, True)
        self.__mDirection = value
        
    def __OnAddListener(self, control):
        if (self.__mDirection == cControl.tDirectionLeft):
            control.Dock = cControl.tDockLeft
        elif (value == cControl.tDirectionTop):
            control.Dock = cControl.tDockTop
        elif (value == cControl.tDirectionRight):
            control.Dock = cControl.tDockRight
        elif (value == cControl.tDirectionBottom):
            control.Dock = cControl.tDockBottom        
        
    def __init__(self, parent: cControls):
        super().__init__(parent, Frame(parent.Parent.TkComponent))
        self.__mDirection = cControl.tDirectionLeft
        self.Controls.SetAddListener(self.__OnAddListener)
#------------------------------------------------
class cButton(__cBaseButton):
    @property
    def Type(self) -> int:
        return cControl.tTypeButton
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Button(parent.Parent.TkComponent))         
#------------------------------------------------
class cCanvas(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypeCanvas
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Canvas(parent.Parent.TkComponent))

    def __call__(self):
        pass
#------------------------------------------------   
class cCheckBox(__cBaseButton):
    @property
    def Type(self) -> int:
        return cControl.tTypeCheckBox
    
    @property
    def Checked(self) -> bool:
        return (self.TkControl["onvalue"]== "1")
        
    @Checked.setter
    def Checked(self, value: bool):
        if (value):
            self.TkControl.select()
        else:
            self.TkControl.deselect()
    
    def ToggleChecked(self):
        self.toggle()
        
    def __init__(self, parent: cControls):
        super().__init__(parent, Checkbutton(parent.Parent.TkComponent))
        self.TextAlign = cControl.tTextAlignDefault
    
    def __call__(self, text: str, checked: bool):
        self.Text = text
        self.Checked = checked
#------------------------------------------------
class cComboBox(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypeComboBox
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Combobox(parent.Parent.TkComponent))

    def __call__(self):
        pass
#------------------------------------------------
class cColorBrowser(__cBaseContainer):
    @property
    def Type(self) -> int:
        return cControl.tTypeCorlorBrowser
    
    @property
    def BrowserCaption(self) -> str:
        return self.__oButton.Text  

    @BrowserCaption.setter
    def BrowserCaption(self, value: str):
        self.__oButton.Text = value
    
    @property
    def BrowserVisible(self) -> bool:
        return self.__oButton.Visible 

    @BrowserVisible.setter
    def BrowserVisible(self, value: bool):
        self.__oButton.Visible = value
    
    @property
    def Color(self) -> int:
        return self.__mColor
    
    @Color.setter
    def Color(self, value: int):        
        self.BackColor = cControl.GetColorAsHex(value)
        self.__mColor = value
    
    def GetColorAsHex(self) -> str:
        return cControl.GetColorAsHex(self.__mColor)
    
    def GetColorAsRgb(self):
        return [color % 256, (color // 256) % 256, color // 65536]
    
    def RaiseBrowser(self) -> bool:
        color = cControl.UIGetColor(self.__mColor)
        if (color == -1):
            return False
        self.Color = color
        return True        
        
    def __OnBrowserClick(self, sender):
        self.RaiseBrowser()
        
    def __init__(self, parent: cControls):
        super().__init__(parent, Frame(parent.Parent.TkComponent))
        self.__oButton = super().Controls.AddButton("...", 0, 0, 30, 30)
        self.__oButton.Dock = cControl.tDockRight
        self.__oButton.SetClickHandler(self.__OnBrowserClick)

    def __call__(self, color):
        self.Color = color
#------------------------------------------------
class cEntryBox(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypeEntryBox
    
    @property
    def ReadOnly(self) -> bool:
        return (self.TkControl["state"] == 'readonly')       

    @ReadOnly.setter   
    def ReadOnly(self, value: bool):
        if (value):
            self.TkControl["state"] = 'readonly'            
        elif (self.TkControl["state"] == 'readonly'):
            self.TkControl["state"] = NORMAL            
            
    @property
    def Text(self):
        return self.TkControl["text"]
        
    @Text.setter
    def Text(self, value: str):
        self.TkControl.delete(0, END)
        self.TkControl.insert(END, value)        
    
    def Clear():
        self.TkControl.delete(0, END)
        
    def __init__(self, parent: cControls):
        super().__init__(parent, Entry(parent.Parent.TkComponent))
#------------------------------------------------
class cGroupBox(__cBaseContainer):
    @property
    def Type(self) -> int:
        return cControl.tTypeGroupBox
    
    @property
    def Text(self) -> str:
        return self.TkControl["text"]
        
    @Text.setter
    def Text(self, value: str):
        self.TkControl["text"] = value
    
    def __OnResize(self, event):
        pass #print(event.width)   
    
    def __init__(self, parent: cControls):
        super().__init__(parent, LabelFrame(parent.Parent.TkComponent))
        self.TextAlign = cControl.tTextAlignDefault
        self.TkControl.bind("<Configure>", self.__OnResize, "+")
        
    def __call__(self, text: str):
        self.Text = text
#------------------------------------------------
class cLabel(__cBaseLabel):
    @property
    def Type(self) -> int:
        return cControl.tTypeLabel
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Label(parent.Parent.TkComponent))
        self.TextAlign = cControl.tTextAlignDefault        
#------------------------------------------------
class cLinkLabel(cLabel):
    @property
    def Type(self) -> int:
        return cControl.tTypeLinkLabel
    
    @property
    def Link(self) -> str:
        return self.__mLink
        
    @Link.setter
    def Link(self, value: str):
        self.__mLink = value
    
    def OpenLink(self):
        if (self.__mLink != tStringEmpty):
            import webbrowser
            webbrowser.open_new(self.__mLink)
    
    def __LinkClickHandler(self, sender, button, x, y):
        self.OpenLink()
         
    def __init__(self, parent: cControls):
        super().__init__(parent)
        self.__mLink = tStringEmpty
        self.ForeColor = "blue"
        self.Cursor = "hand2"
        super().SetMouseUpHandler(self.__LinkClickHandler)
#------------------------------------------------
class cListBox(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypeListBox
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Listbox(parent.Parent.TkComponent))

    def __call__(self):
        pass
#------------------------------------------------    
class cNumericUpDown(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypeNumericUpDown
    
    @property
    def Minimum(self) -> float:
        return self.TkControl["from_"]
    
    @Minimum.setter
    def Minimum(self, value: float):
        self.TkControl["from_"] = value
    
    @property
    def Maximum(self) -> float:
        return self.TkControl["to"]
    
    @Maximum.setter
    def Maximum(self, value: float):
        self.TkControl["to"] = value
        
    @property
    def Increment(self) -> float:
        return self.TkControl["increment"]
    
    @Increment.setter
    def Increment(self, value: float):
        self.TkControl["increment"] = value
    
    @property
    def ReadOnly(self) -> bool:
        return (self.TkControl["state"] != 'readonly')       

    @ReadOnly.setter   
    def ReadOnly(self, value: bool):
        if (value):
            self.TkControl["state"] = 'readonly'            
        elif (self.TkControl["state"] == 'readonly'):
            self.TkControl["state"] = NORMAL            
    
    @property
    def Spin(self) -> bool:
        return self.TkControl["wrap"]
    
    @Spin.setter
    def Spin(self, value: bool):
        self.TkControl["wrap"] = value
    
    @property
    def Value(self) -> float:
        return float(self.TkControl.get())
    
    @Value.setter
    def Value(self, value: float):
        self.TkControl.delete(0, END)
        self.TkControl.insert(END, str(value))
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Spinbox(parent.Parent.TkComponent))
        self(0, 100, 1, 0)      
        
    def __call__(self, minimum: float, maximum: float, increment: float, value: float):
        self.Minimum = minimum
        self.Maximum = maximum
        self.Increment = increment
        self.Value = value
#------------------------------------------------    
class cPanel(__cBaseContainer):
    @property
    def Type(self) -> int:
        return cControl.tTypePanel
    
    def __OnResize(self, event):
        pass #print(event.width)
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Frame(parent.Parent.TkComponent))
        self.TkControl.bind("<Configure>", self.__OnResize, "+")
        
    def __call__(self):
        pass
#------------------------------------------------
class cPathBrowser(__cBaseContainer):
    @property
    def Type(self) -> int:
        return cControl.tTypePathBrowser
    
    @property
    def BrowserCaption(self) -> str:
        return self.__oButton.Text  

    @BrowserCaption.setter
    def BrowserCaption(self, value: str):
        self.__oButton.Text = value
    
    @property
    def BrowserVisible(self) -> bool:
        return self.__oButton.Visible 

    @BrowserVisible.setter
    def BrowserVisible(self, value: bool):
        self.__oButton.Visible = value
    
    @property
    def ReadOnly(self) -> bool:
        return self.__oEntryBox.ReadOnly  

    @ReadOnly.setter   
    def ReadOnly(self, value: bool):
        self.__oEntryBox.ReadOnly = value
                
    @property
    def Path(self) -> str:
        return self.__oEntryBox.Text
    
    @Path.setter
    def Path(self, value: str):
        readOnly = self.__oEntryBox.ReadOnly
        if (readOnly):
            self.__oEntryBox.ReadOnly = False
        self.__oEntryBox.Text = value
        if (readOnly):
            self.__oEntryBox.ReadOnly = True
            
    @property
    def PathFilter(self) -> str:
        return self.__mPathFilter
    
    @PathFilter.setter
    def PathFilter(self, value: str):
        self.__mPathFilter = value    
        
    @property
    def PathType(self) -> int:
        return self.__mPathType
    
    @PathType.setter
    def PathType(self, value: int):
        self.__mPathType = value
    
    def IsExisting(self):
        import os.path
        
        if (pathType == cControl.tPathTypeFolder):
            return os.path.isdir(self.__mPathType)
        elif ((pathType == cControl.tPathTypeFileAsOpen) or (pathType == cControl.tPathTypeFileAsOpen)):
            return os.path.isfile(self.__mPathType)
        else:
            return False
    
    def RaiseBrowser(self) -> bool:
        path = cControl.UIGetPath(self.__mPathType, self.__mPathFilter)
        if (path == tStringEmpty):
            return False
        self.Path = path
        return True
        
    def __OnBrowserClick(self, sender):
        self.RaiseBrowser()
        
    def __init__(self, parent: cControls):
        super().__init__(parent, Frame(parent.Parent.TkComponent))
        self.__oButton = super().Controls.AddButton("...", 0, 0, 30, 30)
        self.__oButton.Dock = cControl.tDockRight
        self.__oButton.SetClickHandler(self.__OnBrowserClick)
        self.__oEntryBox = super().Controls.AddEntryBox(tStringEmpty, 0, 0, 30, 30)
        self.__oEntryBox.Dock = cControl.tDockFill
        self.__oEntryBox.ReadOnly = True
        self.__mPathType = tPathTypeDefault
        self.__mPathFilter = tStringEmpty
        
    def __call__(self, path: str):
        self.Path = path
#------------------------------------------------
class cPictureBox(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypePictureBox
    
    @property
    def Image(self) -> Image:
        return self.TkControl["image"]
    
    @Image.setter
    def Image(self, value: Image):
        self.TkControl["image"] = value
    
    def LoadImage(self, path: str) -> bool:
        image = None 
        try:
            image = PhotoImage(file = path)
        except:
            pass
        if (image != None):
            self.Image = image
        
    def __init__(self, parent: cControls):
        super().__init__(parent, Label(parent.Parent.TkComponent))

    def __call__(self, image):
        self.Image = image
#------------------------------------------------  
class cProgressBar(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypeProgressBar
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Progressbar(parent.Parent.TkComponent))

    def __call__(self):
        pass
#------------------------------------------------  
class cRadioButton(__cBaseButton):
    @property
    def Type(self) -> int:
        return cControl.tTypeRadioButton
    
    @property
    def Checked(self) -> bool:
        return (self.TkControl["onvalue"]== "1")
        
    @Checked.setter
    def Checked(self, value: bool):
        if (value):
            self.TkControl.select()
        else:
            self.TkControl.deselect()
      
    def __init__(self, parent: cControls):
        super().__init__(parent, Radiobutton(parent.Parent.TkComponent))
        self.TextAlign = cControl.tTextAlignDefault
    
    def __call__(self, text: str, checked: bool):
        self.Text = text
        self.Checked = checked
#------------------------------------------------
class cScrollBar(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypeScrollBar
    
    @property
    def Orient(self) -> int:
        return cControl.tOrientHorizontal if (self.TkControl["orient"] == HORIZONTAL) else cControl.tOrientVertical
        
    @Orient.setter
    def Orient(self, value: int):
        self.TkControl["orient"] = HORIZONTAL if (value == cControl.tOrientHorizontal) else VERTICAL
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Scrollbar(parent.Parent.TkComponent))
        
    def __call__(self):
        pass
#------------------------------------------------
class cSeparatorBar(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypeSeparatorBar
    
    @property
    def Orient(self) -> int:
        return cControl.tOrientHorizontal if (self.TkControl["orient"] == HORIZONTAL) else cControl.tOrientVertical
        
    @Orient.setter
    def Orient(self, value: int):
        self.TkControl["orient"] = HORIZONTAL if (value == cControl.tOrientHorizontal) else VERTICAL
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Separator(parent.Parent.TkComponent))

    def __call__(self):
        pass
#------------------------------------------------ 
class cSizeGrip(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypeSizeGrip
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Sizegrip(parent.Parent.TkComponent))

    def __call__(self):
        pass
#------------------------------------------------  
class cSplitContainer(__cBaseContainer):
    @property
    def Type(self) -> int:
        return cControl.tTypeSplitContainer
    
    @property
    def Orient(self) -> int:
        return cControl.tOrientHorizontal if (self.TkControl["orient"] == HORIZONTAL) else cControl.tOrientVertical
        
    @Orient.setter
    def Orient(self, value: int):
        self.TkControl["orient"] = HORIZONTAL if (value == cControl.tOrientHorizontal) else VERTICAL
        
    def Assign(self, controlIndex: int):
        self.TkControl.add(self.Controls[controlIndex].TkControl)
        
    def __OnResize(self, event):
        pass #print(event.width)
    
    def __init__(self, parent: cControls):
        super().__init__(parent, PanedWindow(parent.Parent.TkComponent))
        self.TkControl.bind("<Configure>", self.__OnResize, "+")
#------------------------------------------------
class cSpinBox(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypeSpinBox
    
    @property
    def ReadOnly(self) -> bool:
        return (self.TkControl["state"] != 'readonly')       

    @ReadOnly.setter   
    def ReadOnly(self, value: bool):
        if (value):
            self.TkControl["state"] = 'readonly'            
        elif (self.TkControl["state"] == 'readonly'):
            self.TkControl["state"] = NORMAL            
    
    @property
    def Spin(self) -> bool:
        return self.TkControl["wrap"]
    
    @Spin.setter
    def Spin(self, value: bool):
        self.TkControl["wrap"] = value
    
    @property
    def Value(self) -> str:
        return float(self.TkControl.get())
    
    @Value.setter
    def Value(self, value: str):
        self.TkControl.delete(0, END)
        self.TkControl.insert(END, str)
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Spinbox(parent.Parent.TkComponent))
        
    def __call__(self, *list):
        self.TkControl["values"] = list
#------------------------------------------------
class cStatusBar(__cBaseStripBar):
    @property
    def Type(self) -> int:
        return cControl.tTypeStatusBar
    
    def __init__(self, parent: cControls):
        super().__init__(parent)
#------------------------------------------------ 
class cTabControl(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypeTabControl
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Notebook(parent.Parent.TkComponent))

    def __call__(self):
        pass
#------------------------------------------------  
class cTextBox(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypeTextBox
        
    @property
    def Text(self):
        return self.TkControl["text"]
        
    @Text.setter
    def Text(self, value: str):
        self.TkControl.delete(1.0, END)
        self.TkControl.insert(END, value)
    
    def Clear():
        self.TkControl.delete(1.0, END)
        
    def __init__(self, parent: cControls):
        super().__init__(parent, Text(parent.Parent.TkComponent))
#------------------------------------------------
class cToolBar(__cBaseStripBar):
    @property
    def Type(self) -> int:
        return cControl.tTypeToolBar
    
    def __init__(self, parent: cControls):
        super().__init__(parent)
#------------------------------------------------
class cTrackBar(cControl):    
    @property
    def Type(self) -> int:
        return cControl.tTypeTrackBar
    
    @property
    def Minimum(self) -> float:
        return self.TkControl["from_"]
    
    @Minimum.setter
    def Minimum(self, value: float):
        self.TkControl["from_"] = value
    
    @property
    def Maximum(self) -> float:
        return self.TkControl["to"]
    
    @Maximum.setter
    def Maximum(self, value: float):
        self.TkControl["to"] = value
        
    @property
    def Increment(self) -> float:
        return self.TkControl["resolution"]
    
    @Increment.setter
    def Increment(self, value: float):
        self.TkControl["resolution"] = value
    
    @property
    def Orient(self) -> int:
        return cControl.tOrientHorizontal if (self.TkControl["orient"] == HORIZONTAL) else cControl.tOrientVertical
        
    @Orient.setter
    def Orient(self, value: int):
        self.TkControl["orient"] = HORIZONTAL if (value == cControl.tOrientHorizontal) else VERTICAL
    
    @property
    def ShowLabel(self) -> bool:
        return self.TkControl["label"]
    
    @ShowLabel.setter
    def ShowLabel(self, value: bool):
        self.TkControl["label"] = value
    
    @property
    def ShowValue(self) -> bool:
        return self.TkControl["showvalue"]
    
    @ShowValue.setter
    def ShowValue(self, value: bool):
        self.TkControl["showvalue"] = value
        
    @property
    def Value(self) -> float:
        return float(self.TkControl.get())
    
    @Value.setter
    def Value(self, value: float):
        self.TkControl.set(value)
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Scale(parent.Parent.TkComponent))
        self.Orient = cControl.tOrientDefault
        self(0, 100, 1, 0)      
        
    def __call__(self, minimum: float, maximum: float, increment: float, value: float):
        self.Minimum = minimum
        self.Maximum = maximum
        self.Increment = increment
        self.Value = value
#------------------------------------------------
class cTreeView(cControl):
    @property
    def Type(self) -> int:
        return cControl.tTypeTreeView
    
    def __init__(self, parent: cControls):
        super().__init__(parent, Treeview(parent.Parent.TkComponent))

    def __call__(self):
        pass
#------------------------------------------------ 
class cControls:
    @property
    def Count(self) -> int:
        return len(self.__mItems)
    
    @property
    def Parent(self):
        return self.__mParent
    
    def Add(self, control: cControl) -> bool:
        if (control.Parent != None):
            if (control.Parent == self):
                for i in range(0, self.Count):
                    if (control == self.__mItems[i]):
                        return True
            else:
                return False
        control.Parent = self
        self.__AddControl(control)
        return True
    
    def AddButton(self, text: str, x: int = 0, y: int = 0, width: int = 80, height: int = 30) -> cButton:
        control = cButton(self)
        control.Text = text
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddCanvas(self, x: int = 0, y: int = 0, width: int = 100, height: int = 100) -> cCanvas:
        control = cCanvas(self)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddCheckBox(self, text: str, checked: bool, x: int = 0, y: int = 0, width: int = 80, height: int = 30) -> cCheckBox:
        control = cCheckBox(self)
        control(text, checked)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddComboBox(self, x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> cComboBox:
        control = cComboBox(self)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
         
    def AddColorBrowser(self, color: int, x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> cColorBrowser:
        control = cColorBrowser(self)
        control.Color = color
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
            
    def AddEntryBox(self, text: str, x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> cEntryBox:
        control = cEntryBox(self)
        control.Text = text
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddGroupBox(self, text: str, x: int = 0, y: int = 0, width: int = 80, height: int = 30) -> cGroupBox:
        control = cGroupBox(self)
        control.Text = text
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddLabel(self, text: str, x: int = 0, y: int = 0, width: int = 80, height: int = 30) -> cLabel:
        control = cLabel(self)
        control.Text = text
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddLinkLabel(self, text: str, x: int = 0, y: int = 0, width: int = 80, height: int = 30) -> cLinkLabel:
        control = cLinkLabel(self)
        control.Text = text
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddListBox(self, x: int = 0, y: int = 0, width: int = 100, height: int = 100) -> cListBox:
        control = cListBox(self)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddNumericUpDown(self, x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> cNumericUpDown:
        control = cNumericUpDown(self)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddPanel(self, x: int = 0, y: int = 0, width: int = 100, height: int = 100) -> cPanel:
        control = cPanel(self)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddColorBrowser(self, color: int, x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> cColorBrowser:
        control = cColorBrowser(self)
        control.Color = color
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control

    def AddPathBrowser(self, pathType: int, x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> cPathBrowser:
        control = cPathBrowser(self)
        control.PathType = pathType
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddProgressBar(self, x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> cProgressBar:
        control = cProgressBar(self)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddRadioButton(self, text: str, checked: bool, x: int = 0, y: int = 0, width: int = 80, height: int = 30) -> cRadioButton:
        control = cRadioButton(self)
        control(text, checked)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddScrollBar(self, orient: int, x: int = 0, y: int = 0, width: int = 100, height: int = 20) -> cScrollBar:
        control = cScrollBar(self)
        control.Orient = orient
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddSeparatorBar(self, orient: int, x: int = 0, y: int = 0, width: int = 100, height: int = 10) -> cSeparatorBar:
        control = cSeparatorBar(self)
        control.Orient = orient
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddSizeGrip(self, x: int = 0, y: int = 0, width: int = 20, height: int = 20) -> cSizeGrip:
        control = cSizeGrip(self)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddSplitContainer(self, orient: int, x: int = 0, y: int = 0, width: int = 100, height: int = 100) -> cSplitContainer:
        control = cSplitContainer(self)
        control.Orient = orient
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddSpinBox(self, x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> cSpinBox:
        control = cSpinBox(self)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddStatusBar(self, x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> cToolBar:
        control = cToolBar(self)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddTabControl(self, x: int = 0, y: int = 0, width: int = 100, height: int = 100) -> cTabControl:
        control = cTabControl(self)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control    
    
    def AddTextBox(self, text: str, x: int = 0, y: int = 0, width: int = 100, height: int = 100) -> cTextBox:
        control = cTextBox(self)
        control.Text = text
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddToolBar(self, x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> cToolBar:
        control = cToolBar(self)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def AddTrackBar(self, x: int = 0, y: int = 0, width: int = 100, height: int = 30) -> cTrackBar:
        control = cTrackBar(self)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
        
    def AddTreeView(self, x: int = 0, y: int = 0, width: int = 100, height: int = 100) -> cTreeView:
        control = cTreeView(self)
        control.SetBounds(x, y, width, height)
        self.__AddControl(control)
        return control
    
    def RemoveAt(self, index: int) -> bool:
        if ((index < 0) or (index > (self.Count - 1))):
            return False
        control = self.__mItems[index]
        del self.__mItems[index]
        self.__OnRemoveListener(control)
        control.TkControl.destroy()
        return True

    def Clear(self):
        for i in range(0, self.Count):
            self.__mItems[i].TkControl.destroy()  
        self.__mItems.clear()
        self.__OnClearListener()
        
    def IndexOf(self, control: cControl) -> int:
        for i in range(0, self.Count):
            if (self.__mItems[i] == control):
                return i
        return -1

    def IndexByIdentity(self, identity: int) -> int:
        for i in range(0, self.Count):
            if (self.__mItems[i].Identity == identity):
                return i                  
        return -1
    
    def GetControlByIdentity(self, identity: int) -> cControl:
        for i in range(0, self.Count):
            control = self.__mItems[i]
            if (control.Identity == identity):
                return control
            if (control.HasControls):
                control = control.Controls.GetControlByIdentity(identity)
                if (control != None):
                    return control                    
        return None
    
    def MoveTo(self, index: int, toIndex: int):
        if (index == toIndex):
            return
        control = self.__mItems[index]
        if (index < toIndex):
            control.TkControl.lift(self.__mItems[toIndex].TkControl)
            for i in range(index + 1, toIndex + 1):
                self.__mItems[i] = self.__mItems[i + 1]
            
        else:
            control.TkControl.lower(self.__mItems[toIndex].TkControl)
            for i in range(toIndex, index):
                self.__mItems[i] = self.__mItems[i + 1]
        self.__mItems[toIndex] = control        
    
    def MoveToBack(self, index: int):
        self.MoveTo(index, 0)
    
    def MoveToFront(self, index: int):
        self.MoveTo(index, self.Count - 1)
        
    def Range(self):
        for i in range(0, self.Count):
            yield self.__mItems[i]
    
    def SetAddListener(self, listener):
        self.__mAddListener = listener
    
    def SetRemoveListener(self, listener):
        self.__mRemoveListener = listener
    
    def SetClearListener(self, listener):
        self.__mClearListener = listener
    
    def __AddControl(self, control: cControl) -> bool:
        self.__mItems.append(control)
        self.__OnAddListener(control)
        
    def __OnAddListener(self, control):
        if (self.__mAddListener != None):
            self.__mAddListener(control)
    
    def __OnRemoveListener(self, control):
        if (self.__mRemoveListener != None):
            self.__mRemoveListener(control)
    
    def __OnClearListener(self):
        if (self.__mClearListener != None):
            self.__mClearListener()
        
    def __init__(self, parent):
        self.__mParent = parent
        self.__mItems = []
        self.__mAddListener = None
        self.__mRemoveListener = None
        self.__mClearListener = None
        
    def __del__(self):
        self.__mItems = None
        
    def __getitem__(self, index) -> cControl:
        return self.__mItems[index]    
#------------------------------------------------
class cBaseWindow(cComponent):
    tStateNone = -1
    tStateNormal = 0
    tStateMinimized = 1
    tStateMaximized = 2    
    
    @property
    def TkWindow(self):   
        return self.TkComponent
    
    @property
    def Controls(self):
        return self.__mControls
    
    @property
    def Border(self) -> bool:
        return self.TkComponent.overrideredirect()
    
    @Border.setter   
    def Border(self, value: bool):
        self.TkComponent.update_idletasks()
        self.TkComponent.overrideredirect(value)
        
    @property
    def Fullscreen(self) -> bool:
        return self.TkComponent.attributes("-fullscreen")
    
    @Fullscreen.setter   
    def Fullscreen(self, value: bool):
        self.TkComponent.attributes("-fullscreen", value)
    
    @property
    def Opacity(self) -> float:
        return self.TkComponent.attributes("-alpha")
    
    @Opacity.setter   
    def Opacity(self, value: float):
        self.TkComponent.attributes("-alpha", value)
        
    @property
    def Text(self):
        return self.TkComponent.title()   
        
    @Text.setter
    def Text(self, value: str):
        self.TkComponent.title(value)   
    
    @property
    def TopMost(self) -> bool:
        return self.TkComponent.attributes("-topmost")
    
    @TopMost.setter   
    def TopMost(self, value: bool):
        self.TkComponent.attributes("-topmost", value)
          
    @property
    def TransparentKey(self) -> bool:
        return self.TkComponent.attributes("-transparentcolor")
    
    @TransparentKey.setter   
    def TransparentKey(self, value: bool):
        self.TkComponent.attributes("-transparentcolor", value)
        
    @property
    def Visible(self) -> bool:
        return (self.TkComponent.state() != "withdrawn")

    @Visible.setter
    def Visible(self, value: bool):
        if (value):
            self.Show()
        else:
            self.Hide()
            
    @property
    def WindowState(self) -> int:
        state = self.TkComponent.state()
        if (state == "normal"):
            return cBaseWindow.tStateNormal
        elif (state == "zoomed"): 
            return cBaseWindow.tStateMaximized
        elif (state == "normal"): 
            return cBaseWindow.tStateMinimized
        else:
            return cBaseWindow.tStateNone
            
    @WindowState.setter
    def WindowState(self, value: int):
        if (value == cBaseWindow.tStateNormal):            
            self.TkComponent.state("normal") 
        elif (value == cBaseWindow.tStateMaximized): 
            self.TkComponent.state("zoomed")
        elif (value == cBaseWindow.tStateMinimized): 
            self.TkComponent.state("iconic") # or self.TkComponent.iconify()

    def Active(self):
        self.TkComponent.focus_force()
        
    def Close(self):
        self.TkComponent.destroy()
        
    def Hide(self):
        self.TkComponent.withdraw()
    
    def CenterToScreen(self):
        self.TkComponent.update()
        self.SetLocation((self.TkComponent.winfo_screenwidth() - self.TkComponent.winfo_width()) // 2, \
                         (self.TkComponent.winfo_screenheight() - self.TkComponent.winfo_height()) // 2)
    
    def SetBounds(self, x: int, y: int, width: int, height: int):
        self.TkComponent.geometry(str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y))
    
    def SetLocation(self, x: int, y: int):
        self.TkComponent.geometry("+" + str(x) + "+" + str(y))

    def SetSize(self, width: int, height: int, centerToScreen: bool = False):
        self.TkComponent.geometry(str(width) + "x" + str(height))        
        if (centerToScreen):            
            self.CenterToScreen()
                
    
    def SetMinimumSize(self, width: int, height):
        self.TkComponent.minsize(width, height)

    def SetMaximumSize(self, width: int, height):
        self.TkComponent.maxsize(width, height)
    
    def SetPadding(self, left: int, right: int, top: int, bottom: int):
        self.TkComponent.padx = (left, right)
        self.TkComponent.pady = (top, bottom)
        
    def SetResizeable(self, width: bool = True, height: bool = True):
        self.TkComponent.resizable(width, height)
    
    def Show(self):
        self.TkComponent.update()
        self.TkComponent.deiconify()  
    
    def ImportMfc(self, path: str, unitScaleX: float = 2.0, unitScaleY: float = 2.0) -> bool:
        try:
            fileObject = open(path, "rt")
            str_ = fileObject.readline()  
            if (str_ != tStringEmpty):
                findIndex = str_.find('DIALOGEX ')
                if (findIndex >= 0):
                    items = str_[findIndex + 9:].split(", ")
                    x = int(unitScaleX * float(items[0]))
                    y = int(unitScaleY * float(items[1]))
                    width = int(unitScaleX * float(items[2]))
                    height = int(unitScaleY * float(items[3]))                      
                    self.SetBounds(x, y, width, height)
            self.__mControls.Clear()
            while (True):
                str_ = fileObject.readline()                
                if (str_ == tStringEmpty):
                    break
                str_ = str_.strip()                
                findIndex = str_.find(" ")
                if (findIndex > 0):                    
                    token = str_[:findIndex]
                    if (token == "CAPTION"):
                        self.Text = str_[findIndex + 1:].strip('"')
                    elif (token == "CONTROL"):
                        # Text, identity, class, style, x, y, width, height
                        # "Add", 79, BUTTON, BS_PUSHBUTTON | WS_CHILD | WS_VISIBLE | WS_TABSTOP, 263, 85, 45, 14
                        text = tStringEmpty
                        if (str_[findIndex + 1: findIndex + 2] == '"'):
                            endIndex = str_.find('", ', findIndex + 2)
                            if (endIndex >= (findIndex + 2)):
                                text = str_[findIndex + 2: endIndex].replace('&', tStringEmpty)
                                items = str_[endIndex + 3:].split(", ")
                                identity = int(items[0])
                                class_ = items[1] 
                                style = items[2]
                                x = int(unitScaleX * float(items[3]))
                                y = int(unitScaleY * float(items[4]))
                                width = int(unitScaleX * float(items[5]))
                                height = int(unitScaleY * float(items[6]))                                
                        else:
                            items = str_[findIndex + 1:].split(", ")
                            text = items[0].replace('&', tStringEmpty)
                            identity = int(items[1])
                            class_ = items[2] 
                            style = items[3]
                            x = int(unitScaleX * float(items[4]))
                            y = int(unitScaleY * float(items[5]))
                            width = int(unitScaleX * float(items[6]))
                            height = int(unitScaleY * float(items[7]))                        
                        if (class_ == "BUTTON"):
                            if (style.find("BS_AUTORADIOBUTTON") >= 0):
                                self.__mControls.AddRadioButton(text, False, x, y, width, height)
                            elif (style.find("BS_AUTOCHECKBOX") >= 0):
                                self.__mControls.AddCheckBox(text, False, x, y, width, height)
                            elif (style.find("BS_GROUPBOX") >= 0):
                                self.__mControls.AddGroupBox(text, x, y, width, height).MoveToBack()
                            else:
                                self.__mControls.AddButton(text, x, y, width, height)
                        elif (class_ == "COMBOBOX"):
                            self.__mControls.AddComboBox(x, y, width, 22)                         
                        elif (class_ == "EDIT"):
                            if (style.find("ES_MULTILINE") >= 0):
                                self.__mControls.AddTextBox(text, x, y, width, height)
                            else:
                                self.__mControls.AddEntryBox(text, x, y, width, height)
                        elif (class_ == "LISTBOX"):
                            self.__mControls.AddListBox(x, y, width, height)                        
                        elif (class_ == "STATIC"):
                            if (style.find("SS_BITMAP") < 0):
                                self.__mControls.AddLabel(text, x, y, width, height)
            fileObject.close()
            return True
        except OSError as e:
            print(e)
            return False
        
    def __OnResize(self, event):
        pass #print(event.width)
    
    def __init__(self, tkWindow):
        super().__init__(tkWindow)
        self.__mControls = cControls(self)
        self.TkComponent.bind("<Configure>", self.__OnResize, "+")
        
    def __del__(self):
        self.__mControls = None
#------------------------------------------------
class cWindow(cBaseWindow):
    def ShowDialog(self, ownerWindow: cBaseWindow = None, showOnTaskBar: bool = False, hideOwnerWindow: bool = False):
        if (ownerWindow == None):
            super().Show()            
        else:
            if (hideOwnerWindow):
                ownerWindow.Visible = False
            else:
                ownerWindow.Enabled = False
            super().Show()
            if (not showOnTaskBar):
                super().TkControl.transient(ownerWindow.TkControl)            
            super().TkControl.wait_window(super().TkControl)
            if (hideOwnerWindow):
                ownerWindow.Visible = True
            else:
                ownerWindow.Enabled = True
            ownerWindow.Active()
    
    def __init__(self):   
        super().__init__(Toplevel())    
#------------------------------------------------   
class cMainWindow(cBaseWindow):
    def Show(self):
        super().Show()     
        super().TkComponent.mainloop()
        
    def __init__(self):
        super().__init__(Tk())    
#------------------------------------------------    
class cApplication:
    @property
    def MainWindow(self) -> cMainWindow:
        return self.__MainWindow
    
    def Run(self, mainWindow: cMainWindow):
        self.__MainWindow = mainWindow
        mainWindow.Show()        
#------------------------------------------------
# Test
def NewWindow(object):
    gWindow2 = cWindow()
    gWindow2.Title = "Test2"
    gWindow2.Controls.Import("res.txt")
    gWindow2.SetSize(240, 150, True)
    gWindow2.ShowDialog(object.Window)
    
if (__name__ == "__main__"):
    gApp = cApplication()
    gWindow = cMainWindow()
    gWindow.Title = "Test"
    gWindow.SetSize(750, 550, True)    
    gWindow.SetPadding(50, 50, 50, 50)    
    gWindow.ImportMfc("res.txt", 1.85, 1.85)
    gWindow.Controls.AddColorBrowser(0, 0, 0, 300, 25 )
    gWindow.Controls.AddPathBrowser( 1, 50, 50, 300, 25 )
    #gWindow.Controls.AddRadioButton("Absolute", False, 0, 0, 100, 25 )
    #gWindow.Controls.AddCanvas(0, 0, 230, 100)
    #gWindow.Controls.AddTextBox("TextBox", 240, 0, 230, 100)
    #gWindow.Controls.AddTabControl(480, 0, 230, 100)
    #gWindow.Controls.AddEntryBox("EntryBox", 0, 110, 230, 100)
    #gWindow.Controls.AddPanel(240, 110, 230, 100).Controls.AddButton("Button in Panel", 0, 0, 100, 30)
    #gWindow.Controls.AddTreeView(480, 110, 230, 100)
    #gWindow.Controls.AddListBox(0, 220, 230, 100)
    #b=gWindow.Controls.AddGroupBox("GroupBox", 240, 220, 230, 100).Controls.AddButton("Button in GroupBox", 0, 0, 100, 30)
    ##b.Dock = cControl.tDockFill
    #gSplitContainer = gWindow.Controls.AddSplitContainer(cControl.tOrientHorizontal, 0, 330, 480, 70)
    #gSplitContainer.Controls.AddButton("Button 1", 0, 0, 100, 30)
    #gSplitContainer.Assign(0)
    #gSplitContainer.Controls.AddButton("Button 2", 10, 0, 100, 30)
    #gSplitContainer.Assign(1)
    #gSplitContainer.Controls.AddButton("Button 3", 10, 0, 100, 30)
    #gSplitContainer.Assign(2)        
    #gWindow.Controls.AddNumericUpDown(0, 410, 100, 30)
    #gWindow.Controls.AddTrackBar(100, 410, 100, 30)
    #gWindow.Controls.AddComboBox(210, 410, 100, 30)
    #gWindow.Controls.AddProgressBar(320, 410, 100, 30)
    #gWindow.Controls.AddSeparatorBar(cControl.tOrientHorizontal, 430, 410, 100, 30)
    #gWindow.Controls.AddCheckBox("CheckBox", True, 0, 450, 100, 30)
    #gWindow.Controls.AddLinkLabel("Label", 100, 450, 100, 30).Link = r"https://www.facebook.com/"
    #gWindow.Controls.AddRadioButton("RadioButton", True, 200, 450, 150, 30)
    #gWindow.Controls.AddButton("Button", 350, 450, 100, 30).SetClickHandler(NewWindow)
    #gWindow.Controls.AddScrollBar(cControl.tOrientHorizontal, 0, 490, 200, 30)
    #gWindow.Controls.AddSizeGrip(210, 490, 30, 30)
    #toolBar = gWindow.Controls.AddToolBar(0, 0, 300, 30)
    #toolBar.Dock=cControl.tDockTop
    #toolBar.Controls.AddButton("Hello")
    #toolBar.AddSeparator()
    #toolBar.AddLabel("Duong")
    #toolBar.AddButton("Nga")
    #toolBar.Orient=cControl.tOrientHorizontal
    #statusBar = gWindow.Controls.AddStatusBar(0, 0, 300, 30)
    #statusBar.Dock=cControl.tDockBottom
    #statusBar.Controls.AddLabel("Hello")
    #statusBar.AddSeparator()
    #statusBar.AddLabel("Duong")
    #statusBar.Orient=cControl.tOrientHorizontal    
    gApp.Run(gWindow)