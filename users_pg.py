#import RPi.GPIO as GPIO
from gpiozero import LED, Button
import psycopg2
import time
from signal import pause

#Este Script esta diseñado para Leer el numero de conexiones de PostgreSQL a Odoo y proyectarlas en 2 displays de 7 segmentos de Catodo común conectados a una Raspberry Pi 4#

segmentos1=[LED(26),LED(19),LED(13),LED(6),LED(5),LED(11),LED(9)]
segmentos2=[LED(10),LED(22),LED(27),LED(17),LED(4),LED(3),LED(2)]
caracter=[[0,1,2,3,4,5],[1,2],[0,1,6,4,3],[0,1,2,3,6],[1,2,5,6],[0,2,3,5,6],[0,2,3,4,5,6],[0,1,2],[0,1,2,3,4,5,6],[0,1,2,3,5,6]]

conn = psycopg2.connect(dbname="DB_NAME",user="USER_NAME",password="PASSWORD",host="XXX.XXX.XXX.XXX")
cursor = conn.cursor()
sentencia = "SELECT COUNT (*) FROM pg_stat_activity WHERE datname='DB_NAME'"
cursor.execute(sentencia)
numusuarios= cursor.fetchone()
print(numusuarios) #Comprobando el numero de usuarios haciendo print

for i in numusuarios: # convirtiendo la Tupla en num entero
    x = i
    print(i)

numerox=((x//10)%10)
numeroy=((x//1)%10)

def limpiar():
    for i in range(0,7):
        segmentos2[i].off()
    for i in range(0,7):
        segmentos1[i].off
        
def numero1(numerox):
    for i in range(0, len(caracter[numerox])):
        segmentos1[caracter[numerox][i]].on()

def numero2(numeroy):
    for i in range(0, len(caracter[numeroy])):
        segmentos2[caracter[numeroy][i]].on()
        
def ruleta():
    vuelta=27
    while vuelta > 0: 
        while True:
            for i in range(0,7):
                segmentos1[i].on()
                segmentos2[i].on()
                time.sleep(.009)
                segmentos1[i].off()
                segmentos2[i].off()
            vuelta-=1
            break

def main():
    limpiar()
    time.sleep(1)
    ruleta()
    time.sleep(0)
    numero1(numerox)
    numero2(numeroy)
    conn.close()
    time.sleep(300)
#reset.when_held=
main()


