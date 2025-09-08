RELATORIO
Historico de commits:
576aefb (HEAD -> main, origin/main, origin/HEAD) Merge branch 'main' of github.com:ViniGS2/Calculadora
a90918b (tag: v1.1) Adição de fatorial e reajuste de estrutura
b10d214 Update README.md
91a060c (tag: v1.0) primeiro commit
84c8cf4 docs: adicionar README inicial

Diferença entre versões:
diff --git a/main.py b/main.py
index e9a62f2..e3a9fc5 100644
--- a/main.py
+++ b/main.py
@@ -1,16 +1,32 @@
-numero1 = int(input("Digite o primeiro numero: "))
-numero2 = int(input("Digite o segundo numero: "))
+def fatorial(numero):
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
