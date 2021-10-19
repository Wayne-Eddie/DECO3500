from m5stack import *
from m5stack_ui import *
from uiflow import *
import espnow
import wifiCfg
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


peer = None
data = None
q1_rec = None
q2_rec = None
q3_rec = None
q1_state = None
q2_state = None
q3_state = None

wifiCfg.wlan_ap.active(True)
wifiCfg.wlan_sta.active(True)
espnow.init()
icon_main = M5Img("res/dinosuar_icon.png", x=41, y=97, parent=None)
title_main = M5Label('Welcome Dinosaur World', x=87, y=97, color=0x000, font=FONT_MONT_16, parent=None)
title_team = M5Label('Text', x=50, y=0, color=0x000, font=FONT_MONT_14, parent=None)
txt_q1 = M5Label('Q1. What is your favorite dinosaur?', x=64, y=50, color=0x000, font=FONT_MONT_16, parent=None)
txt_wrong_msg = M5Label('Try Again! : (', x=128, y=106, color=0x000, font=FONT_MONT_14, parent=None)
txt_correct_msg = M5Label('Correct!', x=131, y=26, color=0x000, font=FONT_MONT_14, parent=None)
btn_q1_ok = M5Btn(text='OK', x=125, y=130, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_start = M5Btn(text='Start', x=209, y=12, w=100, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_28, parent=None)
img_map = M5Img("res/map.png", x=209, y=115, parent=None)
btn_q1_a1 = M5Btn(text='A', x=41, y=17, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_q1_a2 = M5Btn(text='B', x=200, y=36, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_q1_a3 = M5Btn(text='C', x=209, y=53, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_q1_next = M5Btn(text='Next!', x=125, y=26, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
txt_q2 = M5Label('Text', x=95, y=53, color=0x000, font=FONT_MONT_14, parent=None)
txt_q3 = M5Label('Text', x=157, y=53, color=0x000, font=FONT_MONT_14, parent=None)
btn_q2_a1 = M5Btn(text='A', x=9, y=122, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_q2_a2 = M5Btn(text='B', x=132, y=166, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_q2_a3 = M5Btn(text='C', x=222, y=166, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_q2_ok = M5Btn(text='OK', x=117, y=9, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_q2_next = M5Btn(text='Next!', x=200, y=115, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_q3_a1 = M5Btn(text='A', x=9, y=50, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_q3_a2 = M5Btn(text='B', x=125, y=122, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_q3_a3 = M5Btn(text='C', x=222, y=147, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_q3_ok = M5Btn(text='OK', x=120, y=123, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
txt_finish = M5Label('Congrats! Check the agg!', x=81, y=182, color=0x000, font=FONT_MONT_14, parent=None)
btn_p1 = M5Btn(text='P1', x=146, y=87, w=50, h=50, bg_c=0xec4646, text_c=0xffffff, font=FONT_MONT_20, parent=None)
Me = M5Btn(text='Me', x=71, y=156, w=40, h=40, bg_c=0x44c0ec, text_c=0xffffff, font=FONT_MONT_16, parent=None)
btn_p2 = M5Btn(text='P2', x=185, y=190, w=50, h=50, bg_c=0xf79307, text_c=0xffffff, font=FONT_MONT_20, parent=None)
loc_add = M5Label('loc_add', x=263, y=44, color=0x000, font=FONT_MONT_14, parent=None)
q31 = M5Label('q31', x=5, y=222, color=0x000, font=FONT_MONT_14, parent=None)
wait_msg = M5Label('wait', x=6, y=156, color=0x000, font=FONT_MONT_14, parent=None)
q11 = M5Label('q11', x=5, y=6, color=0x000, font=FONT_MONT_14, parent=None)
q1a = M5Label('q1a', x=0, y=25, color=0x000, font=FONT_MONT_14, parent=None)
q1b = M5Label('q1b', x=1, y=40, color=0x000, font=FONT_MONT_14, parent=None)
q1c = M5Label('q1c', x=0, y=52, color=0x000, font=FONT_MONT_14, parent=None)
q2a = M5Label('q2a', x=1, y=68, color=0x000, font=FONT_MONT_14, parent=None)
q2b = M5Label('q2b', x=1, y=82, color=0x000, font=FONT_MONT_14, parent=None)
q2c = M5Label('q2c', x=29, y=50, color=0x000, font=FONT_MONT_14, parent=None)
invitation_msg = M5Label('P3 invites you to join!', x=37, y=108, color=0x000, font=FONT_MONT_24, parent=None)
invitation_y = M5Btn(text='Y', x=29, y=182, w=70, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_22, parent=None)
invitation_n = M5Btn(text='N', x=215, y=182, w=70, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_22, parent=None)
q3a = M5Label('q3a', x=2, y=175, color=0x000, font=FONT_MONT_14, parent=None)
q3b = M5Label('q3b', x=2, y=190, color=0x000, font=FONT_MONT_14, parent=None)
q3c = M5Label('q3c', x=2, y=205, color=0x000, font=FONT_MONT_14, parent=None)
invitation_succ = M5Img("res/invite03.png", x=64, y=50, parent=None)
invitation_rej = M5Label('P1 rejected your invitation!', x=15, y=109, color=0x000, font=FONT_MONT_22, parent=None)
btn_rej_conf = M5Btn(text='OK', x=151, y=50, w=70, h=40, bg_c=0xffffff, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_rec_conf = M5Btn(text='OK', x=125, y=190, w=70, h=40, bg_c=0xffffff, text_c=0x000000, font=FONT_MONT_14, parent=None)



def btn_rec_conf_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  screen.set_screen_bg_color(0x66cccc)
  img_map.set_hidden(True)
  Me.set_hidden(True)
  btn_p1.set_hidden(True)
  btn_p2.set_hidden(True)
  invitation_succ.set_hidden(True)
  btn_rec_conf.set_hidden(True)
  btn_q1_ok.set_hidden(True)
  btn_q1_next.set_hidden(True)
  btn_q1_a1.set_hidden(False)
  btn_q1_a1.set_pos(35, 166)
  btn_q1_a2.set_hidden(False)
  btn_q1_a2.set_pos(125, 166)
  btn_q1_a3.set_hidden(False)
  btn_q1_a3.set_pos(212, 166)
  txt_q1.set_hidden(False)
  txt_q1.set_text('1. Most of the dinosaur fossils have')
  txt_q1.set_pos(20, 20)
  txt_q1.set_text_font(FONT_MONT_16)
  q11.set_hidden(False)
  q11.set_text('found on which contient?')
  q11.set_pos(20, 38)
  q11.set_text_font(FONT_MONT_16)
  q1a.set_hidden(False)
  q1a.set_text('A. Africa')
  q1a.set_pos(40, 60)
  q1a.set_text_font(FONT_MONT_16)
  q1b.set_hidden(False)
  q1b.set_text('B. South America')
  q1b.set_pos(40, 80)
  q1b.set_text_font(FONT_MONT_16)
  q1c.set_hidden(False)
  q1c.set_text('C. North America')
  q1c.set_pos(40, 100)
  q1c.set_text_font(FONT_MONT_16)
  pass
btn_rec_conf.pressed(btn_rec_conf_pressed)

def btn_q2_next_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  txt_q2.set_hidden(True)
  txt_correct_msg.set_hidden(True)
  btn_q2_next.set_hidden(True)
  btn_q3_a1.set_hidden(False)
  btn_q3_a1.set_pos(35, 166)
  btn_q3_a2.set_hidden(False)
  btn_q3_a2.set_pos(125, 166)
  btn_q3_a3.set_hidden(False)
  btn_q3_a3.set_pos(212, 166)
  txt_q3.set_hidden(False)
  txt_q3.set_text('3. The smartest dinosaurs of')
  txt_q3.set_pos(20, 20)
  txt_q3.set_text_font(FONT_MONT_16)
  q31.set_hidden(False)
  q31.set_text('the Mesozoic Era?')
  q31.set_pos(20, 38)
  q31.set_text_font(FONT_MONT_16)
  q3a.set_hidden(False)
  q3a.set_text('A. Triceratops')
  q3a.set_pos(40, 60)
  q3a.set_text_font(FONT_MONT_16)
  q3b.set_hidden(False)
  q3b.set_text('B. Troodon')
  q3b.set_pos(40, 80)
  q3b.set_text_font(FONT_MONT_16)
  q3c.set_hidden(False)
  q3c.set_text('C. Theropods')
  q3c.set_pos(40, 100)
  q3c.set_text_font(FONT_MONT_16)
  pass
btn_q2_next.pressed(btn_q2_next_pressed)

def btn_q3_a1_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  txt_wrong_msg.set_hidden(False)
  txt_wrong_msg.set_pos(130, 105)
  btn_q3_ok.set_hidden(False)
  btn_q3_ok.set_pos(125, 130)
  btn_q3_a1.set_hidden(True)
  btn_q3_a2.set_hidden(True)
  btn_q3_a3.set_hidden(True)
  screen.set_screen_bg_color(0xff0000)
  power.setVibrationEnable(True)
  q3a.set_hidden(True)
  q3b.set_hidden(True)
  q3c.set_hidden(True)
  txt_q3.set_hidden(True)
  q31.set_hidden(True)
  pass
btn_q3_a1.pressed(btn_q3_a1_pressed)

def btn_q1_ok_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  btn_q1_a1.set_hidden(False)
  btn_q1_a2.set_hidden(False)
  btn_q1_a3.set_hidden(False)
  btn_q1_ok.set_hidden(True)
  txt_wrong_msg.set_hidden(True)
  screen.set_screen_bg_color(0x66cccc)
  power.setVibrationEnable(False)
  q11.set_hidden(False)
  q1a.set_hidden(False)
  q1b.set_hidden(False)
  q1c.set_hidden(False)
  txt_q1.set_hidden(False)
  pass
btn_q1_ok.pressed(btn_q1_ok_pressed)

def btn_q1_a1_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  txt_wrong_msg.set_hidden(False)
  txt_wrong_msg.set_pos(130, 105)
  btn_q1_ok.set_hidden(False)
  btn_q1_ok.set_pos(125, 130)
  btn_q1_a1.set_hidden(True)
  btn_q1_a2.set_hidden(True)
  btn_q1_a3.set_hidden(True)
  screen.set_screen_bg_color(0xff0000)
  power.setVibrationEnable(True)
  q11.set_hidden(True)
  q1a.set_hidden(True)
  q1b.set_hidden(True)
  q1c.set_hidden(True)
  txt_q1.set_hidden(True)
  pass
btn_q1_a1.pressed(btn_q1_a1_pressed)

def btn_q2_ok_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  btn_q2_a1.set_hidden(False)
  btn_q2_a2.set_hidden(False)
  btn_q2_a3.set_hidden(False)
  btn_q2_ok.set_hidden(True)
  txt_wrong_msg.set_hidden(True)
  screen.set_screen_bg_color(0x66cccc)
  power.setVibrationEnable(False)
  q2a.set_hidden(False)
  q2b.set_hidden(False)
  q2c.set_hidden(False)
  txt_q2.set_hidden(False)
  pass
btn_q2_ok.pressed(btn_q2_ok_pressed)

def btn_q3_ok_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  btn_q3_a1.set_hidden(False)
  btn_q3_a2.set_hidden(False)
  btn_q3_a3.set_hidden(False)
  btn_q3_ok.set_hidden(True)
  txt_wrong_msg.set_hidden(True)
  screen.set_screen_bg_color(0x66cccc)
  power.setVibrationEnable(False)
  q3a.set_hidden(False)
  q3b.set_hidden(False)
  q3c.set_hidden(False)
  txt_q3.set_hidden(False)
  q31.set_hidden(False)
  pass
btn_q3_ok.pressed(btn_q3_ok_pressed)

def btn_q1_next_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  txt_q1.set_hidden(True)
  txt_correct_msg.set_hidden(True)
  btn_q1_next.set_hidden(True)
  btn_q2_a1.set_hidden(False)
  btn_q2_a1.set_pos(35, 166)
  btn_q2_a2.set_hidden(False)
  btn_q2_a2.set_pos(125, 166)
  btn_q2_a3.set_hidden(False)
  btn_q2_a3.set_pos(212, 166)
  wait_msg.set_hidden(True)
  txt_q2.set_hidden(False)
  txt_q2.set_text('2. When did dinosaurs become extinct?')
  txt_q2.set_pos(20, 20)
  txt_q2.set_text_font(FONT_MONT_14)
  q2a.set_hidden(False)
  q2a.set_text('A. 65 million years ago')
  q2a.set_pos(40, 40)
  q2a.set_text_font(FONT_MONT_16)
  q2b.set_hidden(False)
  q2b.set_text('B. 35 million years ago')
  q2b.set_pos(40, 60)
  q2b.set_text_font(FONT_MONT_16)
  q2c.set_hidden(False)
  q2c.set_text('C. 20 million years ago')
  q2c.set_pos(40, 80)
  q2c.set_text_font(FONT_MONT_16)
  pass
btn_q1_next.pressed(btn_q1_next_pressed)

def btn_q3_a2_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  btn_q3_a1.set_hidden(True)
  btn_q3_a2.set_hidden(True)
  btn_q3_a3.set_hidden(True)
  q3a.set_hidden(True)
  q3b.set_hidden(True)
  q3c.set_hidden(True)
  txt_q3.set_hidden(True)
  q31.set_hidden(True)
  txt_correct_msg.set_hidden(False)
  txt_correct_msg.set_pos(130, 90)
  txt_finish.set_pos(81, 106)
  espnow.send(id=1, data=str('q3_finish'))
  q3_state = btn_q3_a2.get_state()
  if q3_rec == None:
    wait_msg.set_text('Plz wait for your partner! : )')
    wait_msg.set_hidden(False)
  else:
    txt_finish.set_hidden(False)
    txt_finish.set_text('Congrats! Check the egg!')
    txt_correct_msg.set_hidden(True)
  pass
btn_q3_a2.pressed(btn_q3_a2_pressed)

def btn_q1_a2_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  txt_wrong_msg.set_hidden(False)
  txt_wrong_msg.set_pos(130, 105)
  btn_q1_ok.set_hidden(False)
  btn_q1_ok.set_pos(125, 130)
  btn_q1_a1.set_hidden(True)
  btn_q1_a2.set_hidden(True)
  btn_q1_a3.set_hidden(True)
  screen.set_screen_bg_color(0xff0000)
  power.setVibrationEnable(True)
  txt_q1.set_hidden(True)
  q11.set_hidden(True)
  q1a.set_hidden(True)
  q1b.set_hidden(True)
  q1c.set_hidden(True)
  pass
btn_q1_a2.pressed(btn_q1_a2_pressed)

def btn_q2_a2_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  txt_wrong_msg.set_hidden(False)
  txt_wrong_msg.set_pos(130, 105)
  btn_q2_ok.set_hidden(False)
  btn_q2_ok.set_pos(125, 130)
  btn_q2_a1.set_hidden(True)
  btn_q2_a2.set_hidden(True)
  btn_q2_a3.set_hidden(True)
  screen.set_screen_bg_color(0xff0000)
  power.setVibrationEnable(True)
  q2a.set_hidden(True)
  q2b.set_hidden(True)
  q2c.set_hidden(True)
  txt_q2.set_hidden(True)
  pass
btn_q2_a2.pressed(btn_q2_a2_pressed)

def btn_q2_a1_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  txt_correct_msg.set_hidden(False)
  txt_correct_msg.set_pos(130, 90)
  btn_q2_a1.set_hidden(True)
  btn_q2_a2.set_hidden(True)
  btn_q2_a3.set_hidden(True)
  btn_q2_next.set_pos(125, 140)
  q2a.set_hidden(True)
  q2b.set_hidden(True)
  q2c.set_hidden(True)
  txt_q2.set_hidden(True)
  espnow.send(id=1, data=str('q2_finish'))
  q2_state = btn_q2_a1.get_state()
  if q2_rec == None:
    wait_msg.set_text('Plz wait for your partner! : )')
    wait_msg.set_hidden(False)
  else:
    btn_q2_next.set_hidden(False)
  pass
btn_q2_a1.pressed(btn_q2_a1_pressed)

def btn_start_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  icon_main.set_hidden(True)
  title_main.set_hidden(True)
  title_team.set_hidden(True)
  img_map.set_pos(0, 0)
  img_map.set_img_src("res/map.png")
  img_map.set_hidden(False)
  Me.set_pos(39, 130)
  btn_p1.set_hidden(False)
  btn_p1.set_pos(146, 76)
  Me.set_hidden(False)
  btn_p2.set_pos(191, 182)
  btn_p2.set_hidden(False)
  pass
btn_start.pressed(btn_start_pressed)

def btn_q1_a3_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  txt_correct_msg.set_hidden(False)
  txt_correct_msg.set_pos(130, 90)
  q11.set_hidden(True)
  q1a.set_hidden(True)
  q1b.set_hidden(True)
  q1c.set_hidden(True)
  txt_q1.set_hidden(True)
  btn_q1_a1.set_hidden(True)
  btn_q1_a2.set_hidden(True)
  btn_q1_a3.set_hidden(True)
  btn_q1_next.set_pos(125, 140)
  espnow.send(id=1, data=str('q1_finish'))
  q1_state = btn_q1_a3.get_state()
  if q1_rec == None:
    wait_msg.set_text('Plz wait for your partner! : )')
    wait_msg.set_hidden(False)
  else:
    btn_q1_next.set_hidden(False)
  pass
btn_q1_a3.pressed(btn_q1_a3_pressed)

def btn_q2_a3_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  txt_wrong_msg.set_hidden(False)
  txt_wrong_msg.set_pos(130, 105)
  btn_q2_ok.set_hidden(False)
  btn_q2_ok.set_pos(125, 130)
  btn_q2_a1.set_hidden(True)
  btn_q2_a2.set_hidden(True)
  btn_q2_a3.set_hidden(True)
  screen.set_screen_bg_color(0xff0000)
  power.setVibrationEnable(True)
  q2a.set_hidden(True)
  q2b.set_hidden(True)
  q2c.set_hidden(True)
  txt_q2.set_hidden(True)
  pass
btn_q2_a3.pressed(btn_q2_a3_pressed)

def btn_q3_a3_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  wait(0.5)
  txt_wrong_msg.set_hidden(False)
  txt_wrong_msg.set_pos(130, 105)
  btn_q3_ok.set_hidden(False)
  btn_q3_ok.set_pos(125, 130)
  btn_q3_a1.set_hidden(True)
  btn_q3_a2.set_hidden(True)
  btn_q3_a3.set_hidden(True)
  screen.set_screen_bg_color(0xff0000)
  power.setVibrationEnable(True)
  q3a.set_hidden(True)
  q3b.set_hidden(True)
  q3c.set_hidden(True)
  txt_q3.set_hidden(True)
  q31.set_hidden(True)
  pass
btn_q3_a3.pressed(btn_q3_a3_pressed)

def btn_p1_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  espnow.broadcast(data=str('invitation'))
  pass
btn_p1.pressed(btn_p1_pressed)

def invitation_y_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  espnow.broadcast(data=str('agree'))
  invitation_msg.set_hidden(True)
  invitation_y.set_hidden(True)
  invitation_n.set_hidden(True)
  invitation_succ.set_hidden(False)
  btn_rec_conf.set_hidden(False)
  pass
invitation_y.pressed(invitation_y_pressed)

def btn_rej_conf_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  btn_p1.set_hidden(False)
  Me.set_hidden(False)
  img_map.set_hidden(False)
  btn_p2.set_hidden(False)
  invitation_rej.set_hidden(True)
  btn_rej_conf.set_hidden(True)
  pass
btn_rej_conf.pressed(btn_rej_conf_pressed)

def invitation_n_pressed():
  global peer, data, q1_rec, q2_rec, q3_rec, q1_state, q2_state, q3_state
  espnow.broadcast(data=str('disagree'))
  img_map.set_hidden(False)
  btn_p1.set_hidden(False)
  Me.set_hidden(False)
  btn_p2.set_hidden(False)
  invitation_msg.set_hidden(True)
  invitation_y.set_hidden(True)
  invitation_n.set_hidden(True)
  pass
invitation_n.pressed(invitation_n_pressed)


wait(0.5)
screen.set_screen_bg_color(0xff9900)
icon_main.set_pos(0, 80)
icon_main.set_img_src("res/dinosuar_icon.png")
title_main.set_text('Welcome Dinosaur World')
title_main.set_pos(87, 97)
title_main.set_text_font(FONT_MONT_16)
title_team.set_text('@Team Violet')
title_team.set_pos(215, 136)
title_team.set_text_font(FONT_MONT_12)
txt_q1.set_hidden(True)
txt_q2.set_hidden(True)
txt_q3.set_hidden(True)
txt_wrong_msg.set_hidden(True)
txt_correct_msg.set_hidden(True)
txt_finish.set_hidden(True)
btn_q1_ok.set_hidden(True)
btn_start.set_pos(110, 150)
btn_q1_a1.set_hidden(True)
btn_q1_a2.set_hidden(True)
btn_q1_a3.set_hidden(True)
btn_q1_next.set_hidden(True)
btn_q2_a1.set_hidden(True)
btn_q2_a2.set_hidden(True)
btn_q2_a3.set_hidden(True)
btn_q2_ok.set_hidden(True)
btn_q2_next.set_hidden(True)
btn_q3_a1.set_hidden(True)
btn_q3_a2.set_hidden(True)
btn_q3_a3.set_hidden(True)
btn_q3_ok.set_hidden(True)
power.setVibrationEnable(False)
img_map.set_hidden(True)
btn_p1.set_hidden(True)
Me.set_hidden(True)
btn_p2.set_hidden(True)
loc_add.set_text(str(espnow.get_mac_addr()))
loc_add.set_hidden(True)
invitation_msg.set_hidden(True)
invitation_msg.set_pos(40, 108)
invitation_y.set_pos(29, 182)
invitation_y.set_hidden(True)
invitation_n.set_hidden(True)
invitation_n.set_pos(215, 182)
espnow.add_peer('08:3a:f2:43:68:3d', id=1)
invitation_succ.set_pos(0, 0)
invitation_succ.set_hidden(True)
invitation_succ.set_img_src("res/invite03.png")
invitation_rej.set_hidden(True)
invitation_rej.set_pos(20, 108)
btn_rej_conf.set_hidden(True)
btn_rej_conf.set_pos(125, 145)
btn_rec_conf.set_hidden(True)
btn_rej_conf.set_pos(125, 190)
wait_msg.set_hidden(True)
wait_msg.set_pos(50, 112)
q11.set_hidden(True)
q1a.set_hidden(True)
q1b.set_hidden(True)
q1c.set_hidden(True)
q2a.set_hidden(True)
q2b.set_hidden(True)
q2c.set_hidden(True)
q3a.set_hidden(True)
q3b.set_hidden(True)
q3c.set_hidden(True)
q31.set_hidden(True)
invitation_y.set_pos(29, 182)
invitation_n.set_pos(215, 182)


def recv_cb(_):
  global peer,data,q1_rec,q2_rec,q3_rec,q1_state,q2_state,q3_state
  peer, _, data = espnow.recv_data(encoder='str')
  if data == 'invitation':
    screen.set_screen_bg_color(0xff9900)
    img_map.set_hidden(True)
    btn_p1.set_hidden(True)
    btn_start.set_hidden(True)
    Me.set_hidden(True)
    btn_p2.set_hidden(True)
    invitation_msg.set_hidden(False)
    invitation_rej.set_hidden(True)
    invitation_y.set_hidden(False)
    invitation_n.set_hidden(False)
  elif data == 'agree':
    invitation_rej.set_hidden(True)
    btn_start.set_hidden(True)
    invitation_succ.set_hidden(False)
    btn_rec_conf.set_hidden(False)
    invitation_msg.set_hidden(True)
  elif data == 'disagree':
    invitation_rej.set_hidden(False)
    invitation_msg.set_hidden(True)
    screen.set_screen_bg_color(0x66cccc)
    img_map.set_hidden(True)
    btn_p1.set_hidden(True)
    btn_p2.set_hidden(True)
    btn_start.set_hidden(True)
    Me.set_hidden(True)
    btn_rej_conf.set_hidden(False)
  elif data == 'q1_finish':
    q1_rec = data
    if q1_state != None:
      btn_q1_next.set_hidden(False)
      wait_msg.set_hidden(True)
    else:
      btn_q1_next.set_hidden(True)
      wait_msg.set_hidden(True)
  elif data == 'q2_finish':
    q2_rec = data
    if q2_state != None:
      btn_q2_next.set_hidden(False)
      wait_msg.set_hidden(True)
    else:
      btn_q2_next.set_hidden(True)
      wait_msg.set_hidden(True)
  elif data == 'q3_finish':
    q3_rec = data
    if q3_state != None:
      wait_msg.set_hidden(True)
      txt_finish.set_text('Congrats! Check the egg!')
      txt_finish.set_hidden(False)
      txt_correct_msg.set_hidden(True)
    else:
      wait_msg.set_hidden(True)

  pass
espnow.recv_cb(recv_cb)

