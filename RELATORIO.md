# RELATORIO
## Historico de commits:
- 576aefb (HEAD -> main, origin/main, origin/HEAD) Merge branch 'main' of github.com:ViniGS2/Calculadora 
- a90918b (tag: v1.1) Adição de fatorial e reajuste de estrutura
- b10d214 Update README.md
- 91a060c (tag: v1.0) primeiro commit
- 84c8cf4 docs: adicionar README inicial

## Diferença entre versões:
```
 diff --git a/main.py b/main.py
 index e9a62f2..e3a9fc5 100644
 --- a/main.py
 +++ b/main.py
 @@ -1,16 +1,32 @@
 numero1 = int(input("Digite o primeiro numero: "))
 numero2 = int(input("Digite o segundo numero: "))
+ def fatorial(numero):
+    if numero == 1:
+        return numero
+    return numero * fatorial(numero - 1)
+
+
+print("Seja Bem-Vindo a Calculadora!\n")
+
+print("Escolha a operação: ")
+
 operacao = int(input('''1-Adição
 2-Subtração
 3-Multiplicação
 4-Divisão
+5-Fatorial
+
 Escolha qual a operação que você deseja: '''))

-if operacao == 1:
-    print(numero1 + numero2)
-elif operacao == 2:
-    print(numero1 - numero2)
-elif operacao == 3:
-    print(numero1 * numero2)
-elif operacao == 4:
-    print(numero1 / numero2)
+if operacao != 5:
+    numero1 = int(input("Digite o primeiro numero: "))
+    numero2 = int(input("Digite o segundo numero: "))
+    if operacao == 1:
+        print(numero1 + numero2)
+    elif operacao == 2:
+        print(numero1 - numero2)
+    elif operacao == 3:
+        print(numero1 * numero2)
+    elif operacao == 4:
+        print(numero1 / numero2)
+elif operacao == 5:
+    numero = int(input("Digite o numero: "))
+    print(fatorial(numero))
(END)
```
## Auditoria do arquivo main.py (v1.1):
```
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300  1) def fatorial(numero):
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300  2)     if numero == 1:
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300  3)         return numero
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300  4)     return numero * fatorial(numero - 1)
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300  5)
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300  6)
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300  7) print("Seja Bem-Vindo a Calculadora!\n")
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300  8)
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300  9) print("Escolha a operação: ")
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300 10)
91a060c2 (Gabi             2025-09-08 12:20:24 -0300 11) operacao = int(input('''1-Adição
91a060c2 (Gabi             2025-09-08 12:20:24 -0300 12) 2-Subtração
91a060c2 (Gabi             2025-09-08 12:20:24 -0300 13) 3-Multiplicação
91a060c2 (Gabi             2025-09-08 12:20:24 -0300 14) 4-Divisão
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300 15) 5-Fatorial
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300 16)
91a060c2 (Gabi             2025-09-08 12:20:24 -0300 17) Escolha qual a operação que você deseja: '''))
91a060c2 (Gabi             2025-09-08 12:20:24 -0300 18)
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300 19) if operacao != 5:
a90918b1 (Vinicius Gabriel 2025-09-08 12:54:08 -0300 20)     numero1 = int(input("Digite o primeiro numero: "))
```