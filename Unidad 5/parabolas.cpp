#include <iostream>

using namespace std;

int main() {
	
	// Para parabolas mínimo n = 2 y números pares
	
	float x[] = { 500, 1150, 1800 };	// Valores de xi
	float fx[] = { 9, 16.1, 23 };		// Valores de f(xi)
	int n = 2;							// Numero de regiones
	
	int tamX = sizeof(x) / sizeof(*x);		// Obtener la cantidad de elementos en "x"
	
	// x[tamX - 1] es el último elemento de x
	// fx[tamX - 1] es el último elemento de fx
	float h =  (x[tamX - 1] - x[0]) / n;	// Obtener h
	
	cout << "h: " << h << endl;				// Imprimir el valor de "h"
	
	float S1 = 0;	// En esta variable almacenaremos el valor de la sumatoria 1
	for (int i = 2; i<=n-2; i = i+2) {
		S1 = S1 + fx[i];
	}
	
	cout << "S1: " << S1 << endl;	// Imprimimos la sumatoria 1
	
	float S2 = 0;	// En esta variable almacenaremos el valor de la sumatoria 2
	for (int i = 1; i<=n-1; i = i+2) {
		S2 = S2 + fx[i];
	}
	
	cout << "S2: " << S2 << endl;	// Imprimimos la sumatoria 2
	
	float S = (h/3) * ( fx[0] + 2*S1 + 4*S2 + fx[tamX - 1]);	// Obtenemos el resultado
	
	cout << endl << "S: " << S << endl;		// Imprimimos el resultado
	
	return 0;
}
