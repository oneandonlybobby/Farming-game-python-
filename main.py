import pygame
import random
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((624,640))
grid_size = 48
font = pygame.font.SysFont('Arial', 32)
font_small = pygame.font.SysFont('Arial', 20)

#plant zones and hotbar
plant_zone = pygame.Rect(0,0,640,480)
hotbar = pygame.image.load("hotbar.png")

#weather vars
isRaining = False

##plant vars##

#tomato vars
tomato_icon_x = 200
tomato_icon_y = 560
tomato_1 = pygame.image.load("tomato1.png")
tomato_2 = pygame.image.load("tomato2.png")
tomato_3 = pygame.image.load("tomato3.png")
tomato_icon1 = pygame.image.load("tomatoicon1.png")
tomato_icon2 = pygame.image.load("tomatoicon2.png")
tomato_stages = [tomato_1, tomato_2, tomato_3]
tomato_icon_rect = pygame.Rect(tomato_icon_x, tomato_icon_y, grid_size, grid_size)
tomato_counter = 0
tomato_text_counter = font_small.render(f"x{tomato_counter}", True, (255,255,255))
tomato_shop_icon_clicked = False
tomato_icon_clicked = True
tomato_locked = False

#potato vars
potato_icon_x = 250
potato_icon_y = 560
potato_1 = pygame.image.load("potato1.png")
potato_2 = pygame.image.load("potato2.png")
potato_3 = pygame.image.load("potato3.png")
potato_icon1 = pygame.image.load("potatoicon1.png")
potato_icon2 = pygame.image.load("potatoicon2.png")
potato_stages = [potato_1, potato_2, potato_3]
potato_icon_rect = pygame.Rect(potato_icon_x, potato_icon_y, grid_size, grid_size)
potato_counter = 0
potato_text_counter = font_small.render(f"x{potato_counter}", True, (255,255,255))
potato_shop_icon_clicked = False
potato_icon_clicked = False
potato_locked = True

#carote vars
carote_icon_x = 300
carote_icon_y = 560
carote_1 = pygame.image.load("carote1.png")
carote_2 = pygame.image.load("carote2.png")
carote_3 = pygame.image.load("carote3.png")
carote_icon1 = pygame.image.load("caroteicon1.png")
carote_icon2 = pygame.image.load("caroteicon2.png")
carote_stages = [carote_1, carote_2, carote_3]
carote_icon_rect = pygame.Rect(carote_icon_x, carote_icon_y, grid_size, grid_size)
carote_counter = 0
carote_text_counter = font_small.render(f"x{carote_counter}", True, (255,255,255))
carote_shop_icon_clicked = False
carote_icon_clicked = False
carote_locked = True
#coin vars
coins = 1000
coins_text = font.render(f"COINS {coins}", True, (255,255,255))
coins_dic = {}

coin1 = pygame.image.load("coin1.png")
coin2 = pygame.image.load("coin2.png")
coin3 = pygame.image.load("coin3.png")

#shop vars
shopx = 20
shopy = 540
shop_gui_x = 120
shop_gui_y = 80
e_x = shop_gui_x + 365
e_y = shop_gui_y - 10
purchase_button_x = -110 + e_x
purchase_button_y = 220 + e_y
purchase_rect = pygame.Rect(purchase_button_x, purchase_button_y, 116, 40)
shop_text = font.render("SHOP", True, (255, 255, 255))
shop_zone = pygame.Rect(shop_gui_x,shop_gui_y, 400,300)
shop_img = pygame.image.load("shop_gui.png")
shop_x = pygame.image.load("shop_gui_x.png")
lockIcon = pygame.image.load("Lock.png")
shop_rect = pygame.Rect(shopx,shopy, 90, 28)
shop_exit_gui = pygame.Rect(e_x,e_y, 30, 30)
shop_tomato_rect = pygame.Rect(shop_gui_x + 50, shop_gui_y + 50, grid_size, grid_size)
shop_potato_rect = pygame.Rect(shop_gui_x + 100, shop_gui_y + 50, grid_size, grid_size)
shop_carote_rect = pygame.Rect(shop_gui_x + 150, shop_gui_y + 50, grid_size, grid_size)
shop_syth_rect = pygame.Rect(shop_gui_x + 100, shop_gui_y + 100, grid_size, grid_size)
shop_Trowl_rect = pygame.Rect(shop_gui_x + 150, shop_gui_y + 100, grid_size, grid_size)
shop_WateringCan_rect = pygame.Rect(shop_gui_x + 50, shop_gui_y + 100, grid_size, grid_size)
shop_open = False 
tomato_shop_icon_clicked = True
potato_shop_icon_clicked = False
carote_shop_icon_clicked = False
gloves_shop_icon_clicked = False
wateringCan_shop_icon_clicked = False
Trowl_shop_icon_clicked = False
syth_shop_icon_clicked= False

#Tool vars
sythe_icon_x = 500
sythe_icon_y = 560
sythe_icon_clicked = False
sythe_locked = True
sythe_rect = pygame.Rect(sythe_icon_x, sythe_icon_y, grid_size, grid_size)
sythe1 = pygame.image.load("syth1.png")
sythe2 = pygame.image.load("syth2.png")
Trowl_icon_x = 450
Trowl_icon_y = 560
Trowl_icon_clicked = False
Trowl_locked = True
Trowl_rect = pygame.Rect(Trowl_icon_x, Trowl_icon_y, grid_size, grid_size)
Trowl1 = pygame.image.load("Trowl1.png")
Trowl2 = pygame.image.load("Trowl2.png")
gloves_icon_x = 400
gloves_icon_y = 560
gloves_icon_clicked = False
gloves_locked = False
gloves_rect = pygame.Rect(gloves_icon_x, gloves_icon_y, grid_size, grid_size)
gloves1 = pygame.image.load("Hand1.png")
gloves2 = pygame.image.load("glove2.png")
wateringCan_icon_x = 550
wateringCan_icon_y = 560
wateringCan_icon_clicked = False
wateringCan_locked = True
wateringCan_rect = pygame.Rect(wateringCan_icon_x, wateringCan_icon_y, grid_size, grid_size)
wateringCan1 = pygame.image.load("Wateringcan1.png")
wateringCan2 = pygame.image.load("Wateringcan2.png")

#weather/day/cycle vars
weather_type = "clear" # types clear, rainy, night not using night for now


class plant:
  def __init__(self, x, y, plant_type, plant_stages, type):
    self.x = x
    self.y = y
    self.plant_type = plant_type
    self.rect = pygame.Rect(x, y, grid_size, grid_size)
    self.stage = plant_stages
    self.i = 0
    self.counter = 0
    self.type = type
    self.wateringCooldown = 0
    self.WaterAble = True
    self.stage1Counter = 0
    self.stage1endCounter = 360 + x
    self.stage2Counter = self.stage1endCounter
    self.stage2endCounter = 560 + x
    self.stage3Counter = self.stage2endCounter
  
  def update(self):
    self.counter += 1
    global isRaining
#waterable states
    if self.WaterAble:
      if self.counter >= self.stage1Counter and self.counter < self.stage1endCounter:
        self.i = 0
      if self.counter >= self.stage2Counter and self.counter < self.stage2endCounter:
        self.i = 1
      if self.counter >= self.stage3Counter:
        self.i = 2
#not waterable sates
    if (not self.WaterAble and self.i == 0) or (not self.WaterAble and isRaining and self.i == 0) or (isRaining and self.i == 0):
      if self.counter+20 >= self.stage1Counter and self.counter < self.stage1endCounter:
        self.i = 0
    if (not self.WaterAble and self.i == 0) or (not self.WaterAble and isRaining and self.i == 0) or (isRaining and self.i == 0):
      if self.counter+20 >= self.stage2Counter and self.counter < self.stage2endCounter:
        self.i = 1
    if (not self.WaterAble and self.i == 0) or (not self.WaterAble and isRaining and self.i == 0) or (isRaining and self.i == 0):
      if self.counter+20 >= self.stage3Counter:
        self.i = 2

    if self.wateringCooldown > 0:
      self.wateringCooldown -= 1
      self.WaterAble = False
    else:
      self.WaterAble = True

    screen.blit(self.stage[self.i], (self.x, self.y))

class Weather:
  def __init__(self, weather_type):
    global isRaining
    self.current_weather = 0
    self.weather_clear = 0 or 1
    self.weather_rainy = 2
    self.Ftimer = 0
    self.Stimer = 0
  def update(self):
    #timer
    global isRaining
    if self.Ftimer <= 60:
      self.Ftimer += 1
    if self.Ftimer >= 60:
      self.Ftimer = 0
      self.Stimer += 1
      print(f"Weather timer: {self.Stimer}")
    if self.Stimer >= 10: #time in seconds before weather changes
      self.current_weather = random.randint(0, 2)
      if self.current_weather == self.weather_clear:
        print(f"Weather changed to: Clear")
        self.Stimer = 0
        self.Ftimer = 0
      if self.current_weather == self.weather_rainy:
        print(f"Weather changed to: Rainy")
        isRaining = True
        self.Stimer = 0
        self.Ftimer = 0


def coins_animation(x, y):
  posible_coin_images = [coin1, coin2, coin3]
  animation_choicer = random.randint(0, 2)
  
  # Generate a unique key for the dictionary entry though untill coin_id is not ocupide
  coin_id = len(coins_dic) + 1
  coins_dic[coin_id] = {
      "image": posible_coin_images[animation_choicer], 
      "x": x, 
      "y": y,
      "target_y": y - 40,  # moves up for 40 pixels
      "speed": 1.5         # speed
  }

#Tools functions for 2x2 3x3 harvesters

def harvest_2x2(mouse_pos):
  global coins, coins_text, clickedonplant
  area2x2 = 48
  x, y = mouse_pos
  x_grid = int(x // area2x2)
  y_grid = int(y // area2x2)
  xongrid = x_grid * area2x2
  yongrid = y_grid * area2x2
  c1 = (xongrid, yongrid)
  c2 = (xongrid + area2x2, yongrid)
  c3 = (xongrid, yongrid + area2x2)
  c4 = (xongrid + area2x2, yongrid + area2x2)
  clickedonplant = True
  for p in plants[:]:
    if not shop_open:
      if p.rect.collidepoint(c1) or p.rect.collidepoint(c2) or p.rect.collidepoint(c3) or p.rect.collidepoint(c4):
            if p.i == 2:
              if p.type == "tomato":
                coins += 2
                coins_text = font.render(f"COINS {coins}", True, (255,255,255))
                plants.remove(p)
                coins_animation(p.x, p.y)
              if p.type == "potato":
                coins += 8
                coins_text = font.render(f"COINS {coins}", True, (255,255,255))
                plants.remove(p)
                coins_animation(p.x, p.y)
              if p.type == "carote":
                coins += 15
                coins_text = font.render(f"COINS {coins}", True, (255,255,255))
                plants.remove(p)
                coins_animation(p.x, p.y)
  return clickedonplant

def harvest_3x3(mouse_pos):
  global coins, coins_text, clickedonplant
  area3x3 = 48
  x, y = mouse_pos
  x -= 48
  y -= 48
  x_grid = int(x // area3x3)
  y_grid = int(y // area3x3)
  xongrid = x_grid * area3x3
  yongrid = y_grid * area3x3
  c1 = (xongrid, yongrid)
  c2 = (xongrid + area3x3, yongrid)
  c3 = (xongrid + area3x3*2, yongrid)
  c4 = (xongrid, yongrid + area3x3)
  c5 = (xongrid + area3x3, yongrid + area3x3)
  c6 = (xongrid + area3x3*2, yongrid + area3x3)
  c7 = (xongrid, yongrid + area3x3*2)
  c8 = (xongrid + area3x3, yongrid + area3x3*2)
  c9 = (xongrid + area3x3*2, yongrid + area3x3*2)
  clickedonplant = True
  for p in plants[:]:
    if not shop_open:
      if p.rect.collidepoint(c1) or p.rect.collidepoint(c2) or p.rect.collidepoint(c3) or p.rect.collidepoint(c4) or p.rect.collidepoint(c5) or p.rect.collidepoint(c6) or p.rect.collidepoint(c7) or p.rect.collidepoint(c8) or p.rect.collidepoint(c9):
            if p.i == 2:
              if p.type == "tomato":
                coins += 2
                coins_text = font.render(f"COINS {coins}", True, (255,255,255))
                plants.remove(p)
                coins_animation(p.x, p.y)
              if p.type == "potato":
                coins += 8
                coins_text = font.render(f"COINS {coins}", True, (255,255,255))
                plants.remove(p)
                coins_animation(p.x, p.y)
              if p.type == "carote":
                coins += 15
                coins_text = font.render(f"COINS {coins}", True, (255,255,255))
                plants.remove(p)
                coins_animation(p.x, p.y)
  return clickedonplant
def harvest_1x1(mouse_pos):
  global coins, coins_text, clickedonplant
  x, y = mouse_pos
  x_grid = int(x // grid_size)
  y_grid = int(y // grid_size)
  xongrid = x_grid * grid_size
  yongrid = y_grid * grid_size
  clickedonplant = True
  for p in plants[:]:
    if not shop_open:
      if p.rect.collidepoint((xongrid, yongrid)):
            if p.i == 2:
              if p.type == "tomato":
                coins += 2
                coins_text = font.render(f"COINS {coins}", True, (255,255,255))
                plants.remove(p)
                coins_animation(p.x, p.y)
              if p.type == "potato":
                coins += 8
                coins_text = font.render(f"COINS {coins}", True, (255,255,255))
                plants.remove(p)
                coins_animation(p.x, p.y)
              if p.type == "carote":
                coins += 15
                coins_text = font.render(f"COINS {coins}", True, (255,255,255))
                plants.remove(p)
                coins_animation(p.x, p.y)
  return clickedonplant
def waterPlants(mouse_pos):
  global clickedonplant
  x, y = mouse_pos
  x_grid = int(x // grid_size)
  y_grid = int(y // grid_size)
  xongrid = x_grid * grid_size
  yongrid = y_grid * grid_size
  clickedonplant = True
  for p in plants[:]:
    if not shop_open and p.WaterAble:
      if p.rect.collidepoint((xongrid, yongrid)):
            if p.i < 2:
              p.counter += 100
              clickedonplant = True
              p.wateringCooldown = 120  
  return clickedonplant

  

plants = []
clock = pygame.time.Clock()
running = True

#weather system
weatherSystem = Weather(0)

while running:
  weatherSystem.update()

  screen.fill((255, 100, 100))

  # Hotbar backdrop
  screen.blit(hotbar, (0, 480))
  
  # Draw active plants
  for p in plants[:]:
    p.update()

#coins animation loop
  for coin_id in list(coins_dic.keys()):
    coin = coins_dic[coin_id]
  
    coin["y"] -= coin["speed"]
    
    if coin["y"] <= coin["target_y"]:
      del coins_dic[coin_id]
    else:
      screen.blit(coin["image"], (coin["x"], coin["y"]))

  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        mouse_pos = event.pos
        x,y = event.pos
        x_grid = int(x // grid_size)
        y_grid = int(y // grid_size)
        xongrid = x_grid * grid_size
        yongrid = y_grid * grid_size
        
        clickedonplant = False

        # Icons hotbar handling
        if tomato_icon_rect.collidepoint(mouse_pos) and not tomato_locked:
          tomato_icon_clicked = True
          potato_icon_clicked = False
          sythe_icon_clicked = False
          Trowl_icon_clicked = False
          gloves_icon_clicked = False
          carote_icon_clicked = False
          wateringCan_icon_clicked = False
        elif potato_icon_rect.collidepoint(mouse_pos) and not potato_locked:
          potato_icon_clicked = True
          tomato_icon_clicked = False
          sythe_icon_clicked = False
          Trowl_icon_clicked = False
          gloves_icon_clicked = False
          carote_icon_clicked = False
          wateringCan_icon_clicked = False
        elif carote_icon_rect.collidepoint(mouse_pos) and not carote_locked:
          carote_icon_clicked = True
          tomato_icon_clicked = False
          potato_icon_clicked = False
          sythe_icon_clicked = False
          Trowl_icon_clicked = False
          gloves_icon_clicked = False
          wateringCan_icon_clicked = False
        elif sythe_rect.collidepoint(mouse_pos) and not sythe_locked:
          sythe_icon_clicked = True
          tomato_icon_clicked = False
          potato_icon_clicked = False
          Trowl_icon_clicked = False
          gloves_icon_clicked = False
          carote_icon_clicked = False
          wateringCan_icon_clicked = False
        elif Trowl_rect.collidepoint(mouse_pos) and not Trowl_locked:
          Trowl_icon_clicked = True
          tomato_icon_clicked = False
          potato_icon_clicked = False
          sythe_icon_clicked = False
          gloves_icon_clicked = False
          carote_icon_clicked = False
          wateringCan_icon_clicked = False
        elif gloves_rect.collidepoint(mouse_pos) :
          gloves_icon_clicked = True
          tomato_icon_clicked = False
          potato_icon_clicked = False
          sythe_icon_clicked = False
          Trowl_icon_clicked = False
          carote_icon_clicked = False
          wateringCan_icon_clicked = False
        elif wateringCan_rect.collidepoint(mouse_pos) and not wateringCan_locked:
          wateringCan_icon_clicked = True
          tomato_icon_clicked = False
          potato_icon_clicked = False
          sythe_icon_clicked = False
          Trowl_icon_clicked = False
          gloves_icon_clicked = False
          carote_icon_clicked = False
        #shop T/Fs
        if shop_zone.collidepoint(mouse_pos) and shop_open:
          clickedonplant = True
        if shop_tomato_rect.collidepoint(mouse_pos) and shop_open:
          tomato_shop_icon_clicked = True
          potato_shop_icon_clicked = False
          carote_shop_icon_clicked = False
          syth_shop_icon_clicked = False
          wateringCan_shop_icon_clicked = False
          Trowl_shop_icon_clicked = False
          tomato_text_counter = font_small.render(f"x{tomato_counter}", True, (255,255,255))
        if shop_potato_rect.collidepoint(mouse_pos) and shop_open:
          tomato_shop_icon_clicked = False
          potato_shop_icon_clicked = True
          carote_shop_icon_clicked = False
          syth_shop_icon_clicked = False
          wateringCan_shop_icon_clicked = False
          Trowl_shop_icon_clicked = False
          potato_text_counter = font_small.render(f"x{potato_counter}", True, (255,255,255))
        if shop_carote_rect.collidepoint(mouse_pos) and shop_open:
          tomato_shop_icon_clicked = False
          potato_shop_icon_clicked = False
          carote_shop_icon_clicked = True
          syth_shop_icon_clicked = False
          wateringCan_shop_icon_clicked = False
          Trowl_shop_icon_clicked = False
          carote_text_counter = font_small.render(f"x{carote_counter}", True, (255,255,255))
        if shop_Trowl_rect.collidepoint(mouse_pos):
          tomato_shop_icon_clicked = False
          potato_shop_icon_clicked = False
          carote_shop_icon_clicked = False

          syth_shop_icon_clicked = False
          wateringCan_shop_icon_clicked = False
          Trowl_shop_icon_clicked = True
        if shop_syth_rect.collidepoint(mouse_pos):
          tomato_shop_icon_clicked = False
          potato_shop_icon_clicked = False
          carote_shop_icon_clicked = False
          syth_shop_icon_clicked = True
          wateringCan_shop_icon_clicked = False
          Trowl_shop_icon_clicked = False
        if shop_WateringCan_rect.collidepoint(mouse_pos):
          tomato_shop_icon_clicked = False
          potato_shop_icon_clicked = False
          carote_shop_icon_clicked = False
          syth_shop_icon_clicked = False
          wateringCan_shop_icon_clicked = True
          Trowl_shop_icon_clicked = False

        # Shop trigger
        if shop_rect.collidepoint(mouse_pos):
          clickedonplant = True
          shop_open = True
          
        if shop_exit_gui.collidepoint(mouse_pos):
          clickedonplant = True
          shop_open = False

        # Harvest plants loop
        if sythe_icon_clicked and not sythe_locked:
          harvest_3x3(mouse_pos)
        if Trowl_icon_clicked and not Trowl_locked :
          harvest_2x2(mouse_pos)
        if gloves_icon_clicked and not gloves_locked:
          harvest_1x1(mouse_pos)
        if wateringCan_icon_clicked and not wateringCan_locked:
          waterPlants(mouse_pos)

        # Plant items if clicking on empty field      
        if not clickedonplant:
          if plant_zone.collidepoint(mouse_pos):   
              if tomato_icon_clicked and tomato_counter >= 1:
                 new_plant = plant(xongrid, yongrid, "tomato", tomato_stages, type="tomato")
                 plants.append(new_plant)
                 tomato_counter -= 1
                 tomato_text_counter = font_small.render(f"x{tomato_counter}", True, (255,255,255))
              if potato_icon_clicked and potato_counter >= 1:
                 new_plant = plant(xongrid, yongrid, "potato", potato_stages, type="potato")
                 plants.append(new_plant)
                 potato_counter -= 1
                 potato_text_counter = font_small.render(f"x{potato_counter}", True, (255,255,255))
              if carote_icon_clicked and carote_counter >= 1:
                 new_plant = plant(xongrid, yongrid, "carote", carote_stages, type="carote")
                 plants.append(new_plant)
                 carote_counter -= 1
                 carote_text_counter = font_small.render(f"x{carote_counter}", True, (255,255,255))
        # Purchase items button
        if shop_open:
          if purchase_rect.collidepoint(mouse_pos):
            if tomato_shop_icon_clicked and coins>= 1 and not tomato_locked:
              tomato_counter += 1
              coins -= 1
              coins_text = font.render(f"COINS {coins}", True, (255,255,255))
              tomato_text_counter = font_small.render(f"x{tomato_counter}", True, (255,255,255))
            if potato_shop_icon_clicked and coins>= 5 and not potato_locked:
              potato_counter += 1
              coins -= 5
              coins_text = font.render(f"COINS {coins}", True, (255,255,255))
              potato_text_counter = font_small.render(f"x{potato_counter}", True, (255,255,255))
            if carote_shop_icon_clicked and coins>= 10 and not carote_locked:
              carote_counter += 1
              coins -= 10
              coins_text = font.render(f"COINS {coins}", True, (255,255,255))
              carote_text_counter = font_small.render(f"x{carote_counter}", True, (255,255,255))
          #locked state/unlock buttons stuff
          if purchase_rect.collidepoint(mouse_pos):
            if tomato_shop_icon_clicked and tomato_locked and coins >= 1:
              coins -= 1
              tomato_locked = False
              coins_text = font.render(f"COINS {coins}", True, (255,255,255))
            if potato_shop_icon_clicked and potato_locked and coins >= 30:
              coins -= 30
              potato_locked = False
              coins_text = font.render(f"COINS {coins}", True, (255,255,255))
            if carote_shop_icon_clicked and carote_locked and coins >= 80:
              coins -= 80
              carote_locked = False
              coins_text = font.render(f"COINS {coins}", True, (255,255,255))
            if Trowl_shop_icon_clicked and Trowl_locked and coins >= 25:
              coins -= 25
              Trowl_locked = False
              coins_text = font.render(f"COINS {coins}", True, (255,255,255))
            if syth_shop_icon_clicked and sythe_locked and coins >= 100:
              coins -= 100
              sythe_locked = False
              coins_text = font.render(f"COINS {coins}", True, (255,255,255))
            if wateringCan_shop_icon_clicked and wateringCan_locked and coins >= 45:
              coins -= 45
              wateringCan_locked = False
              coins_text = font.render(f"COINS {coins}", True, (255,255,255))


  # Render shop GUI overlay
  if shop_open:
      screen.blit(shop_img, (shop_gui_x, shop_gui_y))
      screen.blit(shop_x, (e_x, e_y))
      screen.blit(font_small.render("PURCHASE", True, (255,255,255)), (purchase_button_x + 10, purchase_button_y + 10))
      #not locked state
      if tomato_shop_icon_clicked and not tomato_locked and shop_open:
        screen.blit(tomato_icon2, (shop_gui_x + 50, shop_gui_y + 50))
        screen.blit(wateringCan1, (shop_gui_x + 50, shop_gui_y + 100))
        screen.blit(Trowl1, (shop_gui_x + 150, shop_gui_y + 100))
        screen.blit(potato_icon1, (shop_gui_x + 100, shop_gui_y + 50))
        screen.blit(carote_icon1, (shop_gui_x + 150, shop_gui_y + 50))
        screen.blit(sythe1, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(font_small.render("1 COINS", True, (255,255,255)), (shop_gui_x + 272, shop_gui_y + 170))
        screen.blit(tomato_icon1, (shop_gui_x + 287, shop_gui_y + 70))
      if potato_shop_icon_clicked and not potato_locked and shop_open:
        screen.blit(tomato_icon1, (shop_gui_x + 50, shop_gui_y + 50))
        screen.blit(wateringCan1, (shop_gui_x + 50, shop_gui_y + 100))
        screen.blit(Trowl1, (shop_gui_x + 150, shop_gui_y + 100))
        screen.blit(potato_icon2, (shop_gui_x + 100, shop_gui_y + 50))
        screen.blit(carote_icon1, (shop_gui_x + 150, shop_gui_y + 50))
        screen.blit(sythe1, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(font_small.render("5 COINS", True, (255,255,255)), (shop_gui_x + 272, shop_gui_y + 170))
        screen.blit(potato_icon1, (shop_gui_x + 287, shop_gui_y + 70))
      if carote_shop_icon_clicked and not carote_locked and shop_open:
        screen.blit(tomato_icon1, (shop_gui_x + 50, shop_gui_y + 50))
        screen.blit(wateringCan1, (shop_gui_x + 50, shop_gui_y + 100))
        screen.blit(Trowl1, (shop_gui_x + 150, shop_gui_y + 100))
        screen.blit(potato_icon1, (shop_gui_x + 100, shop_gui_y + 50))
        screen.blit(carote_icon2, (shop_gui_x + 150, shop_gui_y + 50))
        screen.blit(sythe1, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(font_small.render("10 COINS", True, (255,255,255)), (shop_gui_x + 272, shop_gui_y + 170))
        screen.blit(carote_icon1, (shop_gui_x + 287, shop_gui_y + 70))
      if syth_shop_icon_clicked and not sythe_locked and shop_open:
        screen.blit(sythe2, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(wateringCan1, (shop_gui_x + 50, shop_gui_y + 100))
        screen.blit(Trowl1, (shop_gui_x + 150, shop_gui_y + 100))
        screen.blit(tomato_icon1, (shop_gui_x + 50, shop_gui_y + 50))
        screen.blit(potato_icon1, (shop_gui_x + 100, shop_gui_y + 50))
        screen.blit(carote_icon1, (shop_gui_x + 150, shop_gui_y + 50))
        screen.blit(sythe1, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(font_small.render("unlocked", True, (255,255,255)), (shop_gui_x + 272, shop_gui_y + 170))
        screen.blit(sythe1, (shop_gui_x + 287, shop_gui_y + 70))
      if Trowl_shop_icon_clicked and not Trowl_locked and shop_open:
        screen.blit(Trowl2, (shop_gui_x + 150, shop_gui_y + 100))
        screen.blit(wateringCan1, (shop_gui_x + 50, shop_gui_y + 100))
        screen.blit(sythe1, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(tomato_icon1, (shop_gui_x + 50, shop_gui_y + 50))
        screen.blit(potato_icon1, (shop_gui_x + 100, shop_gui_y + 50))
        screen.blit(carote_icon1, (shop_gui_x + 150, shop_gui_y + 50))
        screen.blit(sythe1, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(font_small.render("unlocked", True, (255,255,255)), (shop_gui_x + 272, shop_gui_y + 170))
        screen.blit(Trowl1, (shop_gui_x + 287, shop_gui_y + 70))
      if wateringCan_shop_icon_clicked and not wateringCan_locked and shop_open:
        screen.blit(wateringCan2, (shop_gui_x + 50, shop_gui_y + 100))
        screen.blit(Trowl1, (shop_gui_x + 150, shop_gui_y + 100))
        screen.blit(wateringCan1, (shop_gui_x + 50, shop_gui_y + 100))
        screen.blit(sythe1, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(tomato_icon1, (shop_gui_x + 50, shop_gui_y + 50))
        screen.blit(potato_icon1, (shop_gui_x + 100, shop_gui_y + 50))
        screen.blit(carote_icon1, (shop_gui_x + 150, shop_gui_y + 50))
        screen.blit(sythe1, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(font_small.render("unlocked", True, (255,255,255)), (shop_gui_x + 272, shop_gui_y + 170))
        screen.blit(wateringCan1, (shop_gui_x + 287, shop_gui_y + 70))

      #locked state
      if tomato_shop_icon_clicked and tomato_locked and shop_open:
        screen.blit(tomato_icon2, (shop_gui_x + 50, shop_gui_y + 50))
        screen.blit(potato_icon1, (shop_gui_x + 100, shop_gui_y + 50))
        screen.blit(carote_icon1, (shop_gui_x + 150, shop_gui_y + 50))
        screen.blit(sythe1, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(font_small.render("Unlock", True, (255,255,255)), (shop_gui_x + 285, shop_gui_y + 140))
        screen.blit(font_small.render("1 COINS", True, (255,255,255)), (shop_gui_x + 272, shop_gui_y + 170))
        screen.blit(tomato_icon1, (shop_gui_x + 287, shop_gui_y + 70))
        screen.blit(lockIcon, (shop_gui_x + 287, shop_gui_y + 70))
        screen.blit(Trowl1, (shop_gui_x + 150, shop_gui_y + 100))
        screen.blit(wateringCan1, (shop_gui_x + 50, shop_gui_y + 100))
      if potato_shop_icon_clicked and potato_locked and shop_open:
        screen.blit(tomato_icon1, (shop_gui_x + 50, shop_gui_y + 50))
        screen.blit(potato_icon2, (shop_gui_x + 100, shop_gui_y + 50))
        screen.blit(carote_icon1, (shop_gui_x + 150, shop_gui_y + 50))
        screen.blit(sythe1, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(font_small.render("Unlock", True, (255,255,255)), (shop_gui_x + 285, shop_gui_y + 140))
        screen.blit(font_small.render("30 COINS", True, (255,255,255)), (shop_gui_x + 272, shop_gui_y + 170))
        screen.blit(potato_icon1, (shop_gui_x + 287, shop_gui_y + 70))
        screen.blit(lockIcon, (shop_gui_x + 287, shop_gui_y + 70))
        screen.blit(Trowl1, (shop_gui_x + 150, shop_gui_y + 100))
        screen.blit(wateringCan1, (shop_gui_x + 50, shop_gui_y + 100))
      if carote_shop_icon_clicked and carote_locked and shop_open:
        screen.blit(tomato_icon1, (shop_gui_x + 50, shop_gui_y + 50))
        screen.blit(potato_icon1, (shop_gui_x + 100, shop_gui_y + 50))
        screen.blit(carote_icon2, (shop_gui_x + 150, shop_gui_y + 50))
        screen.blit(sythe1, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(font_small.render("Unlock", True, (255,255,255)), (shop_gui_x + 285, shop_gui_y + 140))
        screen.blit(font_small.render("80 COINS", True, (255,255,255)), (shop_gui_x + 272, shop_gui_y + 170))
        screen.blit(carote_icon1, (shop_gui_x + 287, shop_gui_y + 70))
        screen.blit(lockIcon, (shop_gui_x + 287, shop_gui_y + 70))
        screen.blit(Trowl1, (shop_gui_x + 150, shop_gui_y + 100))
        screen.blit(wateringCan1, (shop_gui_x + 50, shop_gui_y + 100))
      if syth_shop_icon_clicked and sythe_locked and shop_open:
        screen.blit(tomato_icon1, (shop_gui_x + 50, shop_gui_y + 50))
        screen.blit(potato_icon1, (shop_gui_x + 100, shop_gui_y + 50))
        screen.blit(carote_icon1, (shop_gui_x + 150, shop_gui_y + 50))
        screen.blit(sythe2, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(font_small.render("Unlock", True, (255,255,255)), (shop_gui_x + 285, shop_gui_y + 140))
        screen.blit(font_small.render("100 COINS", True, (255,255,255)), (shop_gui_x + 272, shop_gui_y + 170))
        screen.blit(sythe1, (shop_gui_x + 287, shop_gui_y + 70))
        screen.blit(lockIcon, (shop_gui_x + 287, shop_gui_y + 70))
        screen.blit(Trowl1, (shop_gui_x + 150, shop_gui_y + 100))
        screen.blit(wateringCan1, (shop_gui_x + 50, shop_gui_y + 100))
      if wateringCan_shop_icon_clicked and wateringCan_locked and shop_open:
        screen.blit(tomato_icon1, (shop_gui_x + 50, shop_gui_y + 50))
        screen.blit(potato_icon1, (shop_gui_x + 100, shop_gui_y + 50))
        screen.blit(carote_icon1, (shop_gui_x + 150, shop_gui_y + 50))
        screen.blit(sythe1, (shop_gui_x + 100, shop_gui_y + 100))
        screen.blit(font_small.render("Unlock", True, (255,255,255)), (shop_gui_x + 285, shop_gui_y + 140))
        screen.blit(font_small.render("45 COINS", True, (255,255,255)), (shop_gui_x + 272, shop_gui_y + 170))
        screen.blit(wateringCan1, (shop_gui_x + 287, shop_gui_y + 70))
        screen.blit(lockIcon, (shop_gui_x + 287, shop_gui_y + 70))
        screen.blit(Trowl1, (shop_gui_x + 150, shop_gui_y + 100))
        screen.blit(wateringCan2, (shop_gui_x + 50, shop_gui_y + 100))
      if Trowl_shop_icon_clicked and Trowl_locked and shop_open:
          screen.blit(tomato_icon1, (shop_gui_x + 50, shop_gui_y + 50))
          screen.blit(potato_icon1, (shop_gui_x + 100, shop_gui_y + 50))
          screen.blit(carote_icon1, (shop_gui_x + 150, shop_gui_y + 50))
          screen.blit(sythe1, (shop_gui_x + 100, shop_gui_y + 100))
          screen.blit(font_small.render("Unlock", True, (255,255,255)), (shop_gui_x + 285, shop_gui_y + 140))
          screen.blit(font_small.render("25 COINS", True, (255,255,255)), (shop_gui_x + 272, shop_gui_y + 170))
          screen.blit(Trowl1, (shop_gui_x + 287, shop_gui_y + 70))
          screen.blit(lockIcon, (shop_gui_x + 287, shop_gui_y + 70))
          screen.blit(Trowl2, (shop_gui_x + 150, shop_gui_y + 100))
          screen.blit(wateringCan1, (shop_gui_x + 50, shop_gui_y + 100))





  # Render active inventory hotbar icons
  if potato_icon_clicked and not potato_locked:
    screen.blit(potato_icon2, (potato_icon_x, potato_icon_y))
    screen.blit(tomato_icon1, (tomato_icon_x, tomato_icon_y))
    screen.blit(sythe1, (sythe_icon_x, sythe_icon_y))
    screen.blit(Trowl1, (Trowl_icon_x, Trowl_icon_y))
    screen.blit(gloves1, (gloves_icon_x, gloves_icon_y))
    screen.blit(carote_icon1, (carote_icon_x, carote_icon_y))
    screen.blit(wateringCan1, (wateringCan_icon_x, wateringCan_icon_y))
  if tomato_icon_clicked and not tomato_locked:
    screen.blit(potato_icon1, (potato_icon_x, potato_icon_y))
    screen.blit(tomato_icon2, (tomato_icon_x, tomato_icon_y))
    screen.blit(sythe1, (sythe_icon_x, sythe_icon_y))
    screen.blit(Trowl1, (Trowl_icon_x, Trowl_icon_y))
    screen.blit(gloves1, (gloves_icon_x, gloves_icon_y))
    screen.blit(carote_icon1, (carote_icon_x, carote_icon_y))
    screen.blit(wateringCan1, (wateringCan_icon_x, wateringCan_icon_y))
  if sythe_icon_clicked and not sythe_locked:
    screen.blit(potato_icon1, (potato_icon_x, potato_icon_y))
    screen.blit(tomato_icon1, (tomato_icon_x, tomato_icon_y))
    screen.blit(sythe2, (sythe_icon_x, sythe_icon_y))
    screen.blit(Trowl1, (Trowl_icon_x, Trowl_icon_y))
    screen.blit(gloves1, (gloves_icon_x, gloves_icon_y))
    screen.blit(carote_icon1, (carote_icon_x, carote_icon_y))
    screen.blit(wateringCan1, (wateringCan_icon_x, wateringCan_icon_y))
  if Trowl_icon_clicked and not Trowl_locked:
    screen.blit(potato_icon1, (potato_icon_x, potato_icon_y))
    screen.blit(tomato_icon1, (tomato_icon_x, tomato_icon_y))
    screen.blit(sythe1, (sythe_icon_x, sythe_icon_y))
    screen.blit(Trowl2, (Trowl_icon_x, Trowl_icon_y))
    screen.blit(gloves1, (gloves_icon_x, gloves_icon_y))
    screen.blit(carote_icon1, (carote_icon_x, carote_icon_y))
    screen.blit(wateringCan1, (wateringCan_icon_x, wateringCan_icon_y))
  if gloves_icon_clicked and not gloves_locked:
    screen.blit(potato_icon1, (potato_icon_x, potato_icon_y))
    screen.blit(tomato_icon1, (tomato_icon_x, tomato_icon_y))
    screen.blit(sythe1, (sythe_icon_x, sythe_icon_y))
    screen.blit(Trowl1, (Trowl_icon_x, Trowl_icon_y))
    screen.blit(gloves2, (gloves_icon_x, gloves_icon_y))
    screen.blit(carote_icon1, (carote_icon_x, carote_icon_y))
    screen.blit(wateringCan1, (wateringCan_icon_x, wateringCan_icon_y))
  if carote_icon_clicked and not carote_locked:
    screen.blit(potato_icon1, (potato_icon_x, potato_icon_y))
    screen.blit(tomato_icon1, (tomato_icon_x, tomato_icon_y))
    screen.blit(sythe1, (sythe_icon_x, sythe_icon_y))
    screen.blit(Trowl1, (Trowl_icon_x, Trowl_icon_y))
    screen.blit(gloves1, (gloves_icon_x, gloves_icon_y))
    screen.blit(carote_icon2, (carote_icon_x, carote_icon_y))
    screen.blit(wateringCan1, (wateringCan_icon_x, wateringCan_icon_y))
  if wateringCan_icon_clicked and not wateringCan_locked:
    screen.blit(potato_icon1, (potato_icon_x, potato_icon_y))
    screen.blit(tomato_icon1, (tomato_icon_x, tomato_icon_y))
    screen.blit(sythe1, (sythe_icon_x, sythe_icon_y))
    screen.blit(Trowl1, (Trowl_icon_x, Trowl_icon_y))
    screen.blit(gloves1, (gloves_icon_x, gloves_icon_y))
    screen.blit(wateringCan2, (wateringCan_icon_x, wateringCan_icon_y))
    screen.blit(carote_icon1, (carote_icon_x, carote_icon_y))
  
  if potato_locked:
    potato_icon_clicked = False
    screen.blit(lockIcon, (potato_icon_x, potato_icon_y))
  if tomato_locked:
    tomato_icon_clicked = False
    screen.blit(lockIcon, (tomato_icon_x, tomato_icon_y))
  if sythe_locked:
    sythe_icon_clicked = False
    screen.blit(lockIcon, (sythe_icon_x, sythe_icon_y))
  if Trowl_locked:
    Trowl_icon_clicked = False
    screen.blit(lockIcon, (Trowl_icon_x, Trowl_icon_y))
  if gloves_locked:
    gloves_icon_clicked = False
    screen.blit(lockIcon, (gloves_icon_x, gloves_icon_y))
  if carote_locked:
    carote_icon_clicked = False
    screen.blit(lockIcon, (carote_icon_x, carote_icon_y))
  if wateringCan_locked:
    wateringCan_icon_clicked = False
    screen.blit(lockIcon, (wateringCan_icon_x, wateringCan_icon_y))
  if carote_locked:
    carote_icon_clicked = False
    screen.blit(lockIcon, (carote_icon_x, carote_icon_y))

  # Render inventory counters text labels
  screen.blit(tomato_text_counter, (tomato_icon_x + 30, tomato_icon_y + 25))
  screen.blit(potato_text_counter, (potato_icon_x + 30, potato_icon_y + 25))
  screen.blit(carote_text_counter, (carote_icon_x + 30, carote_icon_y + 25))
  
  # Render UI shop buttons text and global currency tracking
  screen.blit(shop_text, (shopx + 5, shopy - 2))
  screen.blit(coins_text, (20, 580))

  pygame.display.update()
  clock.tick(60)

pygame.quit()