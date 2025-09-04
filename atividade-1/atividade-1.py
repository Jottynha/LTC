# ----------------------------------------------
# Atividade 1 - Circuito RLC Série
# Laboratório de Teoria de Controle
# ----------------------------------------------
# Objetivos:
# - Definir a função de transferência do circuito RLC
# - Analisar resposta ao degrau unitário
# - Avaliar influência do fator de amortecimento (zeta)
# - Comparar respostas: subamortecida, criticamente amortecida e superamortecida
#
# Equação diferencial (a partir da LTK):
# Vin(t) = vR(t) + vL(t) + vC(t)
#
# Em termos de vC(t):
# L*C * d²vC/dt² + R*C * dvC/dt + vC(t) = Vin(t)
#
# Função de transferência:
# Vc(s)/Vin(s) = 1 / (L*C*s² + R*C*s + 1)
#
# Padrão de sistema de 2ª ordem:
# G(s) = ωn² / (s² + 2*zeta*ωn*s + ωn²)
# onde:
#   ωn = 1/sqrt(L*C)  (frequência natural)
#   zeta = (R/2)*sqrt(C/L)  (fator de amortecimento)
#
# ----------------------------------------------

import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------
# 1 -> Parâmetros do circuito
# ----------------------------------------------
R = 50              # Ohms
L = 10e-3           # 10 mH
C = 10e-6           # 10 µF
# Frequência natural e fator de amortecimento
omega_n = 1/np.sqrt(L*C)
zeta = (R/2)*np.sqrt(C/L)
print(f"Frequência natural (ωn): {omega_n:.2f} rad/s")
print(f"Fator de amortecimento (ζ): {zeta:.3f}")
# ----------------------------------------------
# 2 -> Função de transferência direta (a partir do circuito)
# ----------------------------------------------
num = [1]
den = [L*C, R*C, 1]
G = ctrl.TransferFunction(num, den)
print("\nFunção de Transferência (circuito):")
print(G)
# Resposta ao degrau
t, y = ctrl.step_response(G)
plt.figure()
plt.plot(t, y)
plt.title("Resposta ao Degrau - Circuito RLC")
plt.xlabel("Tempo [s]")
plt.ylabel("vC(t) [V]")
plt.grid(True)
plt.show()
# ----------------------------------------------
# 3 -> Função de transferência em forma padrão (2ª ordem)
# ----------------------------------------------
num2 = [omega_n**2]
den2 = [1, 2*zeta*omega_n, omega_n**2]
G2 = ctrl.TransferFunction(num2, den2)
print("\nFunção de Transferência (forma padrão):")
print(G2)
t, y = ctrl.step_response(G2)
plt.figure()
plt.plot(t, y)
plt.title("Resposta ao Degrau - Forma Padrão")
plt.xlabel("Tempo [s]")
plt.ylabel("Saída Normalizada")
plt.grid(True)
plt.show()
# ----------------------------------------------
# 4 -> Diferentes condições de amortecimento
# ----------------------------------------------
# Condição crítica: Rcrit = 2*sqrt(L/C)
R_crit = 2*np.sqrt(L/C)
R_sub = 0.5*R_crit   # Subamortecido
R_super = 2*R_crit   # Superamortecido

valores_R = {
    "Subamortecido": R_sub,
    "Crítico": R_crit,
    "Superamortecido": R_super
}

plt.figure()
for tipo, R_val in valores_R.items():
    zeta = (R_val/2)*np.sqrt(C/L)
    num = [omega_n**2]
    den = [1, 2*zeta*omega_n, omega_n**2]
    G_temp = ctrl.TransferFunction(num, den)
    t, y = ctrl.step_response(G_temp)
    plt.plot(t, y, label=f"{tipo} (R={R_val:.2f} Ω)")

plt.title("Comparação das Respostas ao Degrau")
plt.xlabel("Tempo [s]")
plt.ylabel("Saída Normalizada")
plt.legend()
plt.grid(True)
plt.show()
