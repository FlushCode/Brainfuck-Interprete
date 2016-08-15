+++++ +++               Celda #0 = 8
[
    >++++               Celda #1 = 4
    [                   Iniciar bucle en la celda #1
        >++             Sumar 2 a la celda #2
        >+++            Sumar 3 a la celda #3
        >+++            Sumar 3 a la celda #4
        >+              Sumar 1 a la celda #5
        <<<<-           Volver a la celda #1 y restar 1
    ]                   Repetir hasta que celda #1 = 0 (4 veces)
    >+                  Sumar 1 a la celda #2
    >+                  Sumar 1 a la celda #3
    >-                  Restar 1 a la celda #4
    >>+                 Sumar 1 a la celda #6
    [<]                 Volver a la primera celda en 0, que sera la celda #1
    <-                  Restar 1 a la celda #0
]                       Repetir hasta que celda #0 = 0 (8 veces)

El resultado es:
Celda nro:   0   1   2   3   4   5   6
Contenido:   0   0  72 104  88  32   8
Puntero  :   ^

>>.                     Imprimir celda #2 (72 = 'H')
>---.                   Restar 3 a la celda #3 (101 = 'e')
+++++++..+++.           Imprimir 'llo' a partir de la celda #3
>>.                     Imprimir celda #5 (32 = ' ')
<-.                     Restar 1 a la celda #4 (87 = 'W')
<.                      Celda #3 ('o')
+++.------.--------.    'rld'
>>+.                    Celda #5 ('!')
>++.                    Celda #6 ('\n')