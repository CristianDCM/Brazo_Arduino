#include <Servo.h>
#include <math.h>

#define PI 3.141

Servo InferiorServo;
Servo IzquierdaServo;
Servo DerechaServo;
Servo SuperiorServo; //Nuevo

int command;

struct jointAngle { //Angulo
  int Inferior;
  int Izquierda;
  int Derecha;
  int Superior; //Nuevo
};
int AgarreDeseado;
int PosicionPinza;
int ServoVelocidad = 15;

struct jointAngle AnguloDeseado; //ángulos deseados de los servos

//++++++++++++++++DECLARACIONES DE FUNCIÓN++++++++++++++++++++++++++++
void servoControl (int thePos, int theSpeed, Servo theServo);
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

void setup()
{
  Serial.begin(9600);
  InferiorServo.attach(9);
  IzquierdaServo.attach(10);
  DerechaServo.attach(11);
  SuperiorServo.attach(6); //Nuevo

  Serial.setTimeout(50);     //Asegura que el arduino no lea la serie por mucho tiempo
  InferiorServo.write(0);     //Posiciones iniciales de los servos PD: ajustar con las iniciales de la I.F
  IzquierdaServo.write(100);
  DerechaServo.write(140);
  SuperiorServo.write(0); //Nuevo
}

void loop()

{
  while (Serial.available()) {
    AnguloDeseado.Inferior = Serial.parseInt();
    AnguloDeseado.Izquierda = Serial.parseInt();
    AnguloDeseado.Derecha = Serial.parseInt();
    AnguloDeseado.Superior = Serial.parseInt(); //Nuevo
    if (Serial.read() == 'd') {            // Si el último byte es 'd', deja de leer y ejecuta el comando 'd' significa 'hecho'
      Serial.println('d');
      Serial.flush();                     // Borra todos los demás comandos apilados en el búfer
    }
    //Mueve el servo a la posición deseado
    servoControl(AnguloDeseado.Inferior, ServoVelocidad, InferiorServo);
    servoControl(AnguloDeseado.Izquierda, ServoVelocidad, IzquierdaServo);
    servoControl(AnguloDeseado.Derecha, ServoVelocidad, DerechaServo);
    servoControl(AnguloDeseado.Superior, ServoVelocidad, SuperiorServo); //Nuevo
  }
}
//++++++++++++++++++++ DEFINICIONES DE FUNCIONES++++++++++++++++++++++++
void servoControl (int thePos, int theSpeed, Servo theServo) { //Declarar velocidad??
  //thePos es la posición deseada a la que se debe conducir el servo
  //theSpeed es el retraso entre cada incremento de la posición del servo en milisegundos
  //theServo es el objeto servo que se va a controlar.

  int startPos = theServo.read();        //leer la posición actual
  int newPos = startPos;

  //Definir dónde está la pos con respecto al comando
  //Si la posición actual es menor que el movimiento real hacia arriba
  if (startPos < thePos) {
    while (newPos < (thePos - 2)) { //Default 5
      newPos = newPos + 1;
      theServo.write(newPos);
    }
  }
  else {
    while (newPos > (thePos + 2)) {
      newPos = newPos - 5;
      theServo.write(newPos);
    }
  }
}