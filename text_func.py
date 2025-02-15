import string 
import pygame
text_list = []
text_done = 0
text_images_dict = {}
counter_txt = 0
text_animation_list = []
screen = pygame.display.set_mode((1280, 720))
def load_text_dict():
	global text_images_dict
	a = pygame.image.load('images/letters/a.png').convert_alpha()
	b = pygame.image.load('images/letters/b.png').convert_alpha()
	c = pygame.image.load('images/letters/c.png').convert_alpha()
	d = pygame.image.load('images/letters/d.png').convert_alpha()
	e = pygame.image.load('images/letters/e.png').convert_alpha()
	f = pygame.image.load('images/letters/f.png').convert_alpha()
	g = pygame.image.load('images/letters/g.png').convert_alpha()
	h = pygame.image.load('images/letters/h.png').convert_alpha()
	i = pygame.image.load('images/letters/i.png').convert_alpha()
	j = pygame.image.load('images/letters/j.png').convert_alpha()
	k = pygame.image.load('images/letters/k.png').convert_alpha()
	l = pygame.image.load('images/letters/l.png').convert_alpha()
	m = pygame.image.load('images/letters/m.png').convert_alpha()
	n = pygame.image.load('images/letters/n.png').convert_alpha()
	o = pygame.image.load('images/letters/o.png').convert_alpha()
	p= pygame.image.load('images/letters/p.png').convert_alpha()
	q = pygame.image.load('images/letters/q.png').convert_alpha()
	r = pygame.image.load('images/letters/r.png').convert_alpha()
	s = pygame.image.load('images/letters/s.png').convert_alpha()
	t = pygame.image.load('images/letters/t.png').convert_alpha()
	u = pygame.image.load('images/letters/u.png').convert_alpha()
	v = pygame.image.load('images/letters/v.png').convert_alpha()
	w = pygame.image.load('images/letters/w.png').convert_alpha()
	x = pygame.image.load('images/letters/x.png').convert_alpha()
	y = pygame.image.load('images/letters/y.png').convert_alpha()
	z = pygame.image.load('images/letters/z.png').convert_alpha()
	for letter in string.ascii_lowercase:
		text_images_dict[letter] = pygame.image.load(f'images/letters/{letter}.png').convert_alpha()
	for num in string.digits:
		text_images_dict[num] = pygame.image.load(f'images/letters/{letter}.png').convert_alpha()
	text_images_dict[' '] = pygame.Surface((1, 20), pygame.SRCALPHA)
	text_images_dict['/'] = pygame.Surface((1, 20), pygame.SRCALPHA)
def load_text(text):
	global text_list
	text_list.clear()
	for letter in text:
		text_list.append(text_images_dict[letter])
def draw_text(x_pos,y_pos, init):
	for letter_image in text_animation_list:
		if letter_image == text_images_dict[' ']:  
			x_pos += 5
		if letter_image == text_images_dict['/']:
			y_pos += 30
			x_pos -= (x_pos-init)
		else:
			screen.blit(letter_image, (x_pos, y_pos))
			x_pos += 20
def text_animation(speed):
	global  text_done, text_animation_list, counter_txt
	counter_txt += speed
	text_animation_list = text_list[0:int(counter_txt)]
def counter_txt_reset():
	global counter_txt
	counter_txt = 0
def all_text_func(text, x_pos, y_pos, init,speed):
	global counter_txt, initial_x_pos
	initial_x_pos = x_pos
	load_text_dict()
	load_text(text)
	text_animation(speed)
	draw_text(x_pos,y_pos,init)