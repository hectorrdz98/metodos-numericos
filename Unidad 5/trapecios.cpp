#include <iostream>

using namespace std;

int main() {
	
	// Para trapecios mínimo n = 1
	
	float x[] = { 500, 1800 };	// Valores de xi
	float fx[] = { 9, 23 };		// Valores de f(xi)
	int n = 1;					// Numero de regiones
	
	int tamX = sizeof(x) / sizeof(*x);		// Obtener la cantidad de elementos en "x"
	
	// x[tamX - 1] es el último elemento de x
	// fx[tamX - 1] es el último elemento de fx
	float h =  (x[tamX - 1] - x[0]) / n;	// Obtener h
	
	cout << "h: " << h << endl;				// Imprimir el valor de "h"
	
	float T1 = 0;	// En esta variable almacenaremos el valor de la sumatoria
	for (int i = 1; i<n-1; i++) {
		T1 = T1 + fx[i];
	}
	
	float T = (h/2) * ( fx[0] + 2*T1  + fx[tamX - 1]);	// Obtenemos el resultado
	
	cout << "T: " << T << endl;		// Imprimimos el resultado
	
	return 0;
}
