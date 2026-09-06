Python
def calcular_consumo_eletrico():
    print("=" * 45)
    print(" ⚡ CALCULADORA DE CONSUMO ELÉTRICO ⚡")
    print("=" * 45)

    # Coleta de dados do usuário
    aparelho = input("Nome do aparelho (ex.: Geladeira): ").strip()
    
    try:
        potencia = float(input("Potência do aparelho em Watts (W): "))
        horas_dia = float(input("Tempo médio de uso diário (em horas): "))
        
        # Cálculo de consumo mensal em kWh
        # Fórmula: (Potência * Horas por dia * 30 dias) / 1000
        consumo_mensal = (potencia * horas_dia * 30) / 1000
        
        # Cálculo de custo estimado com base em uma tarifa média (R$ 0,75 por kWh)
        tarifa_kwh = 0.75
        custo_estimado = consumo_mensal * tarifa_kwh

        # Exibição dos resultados formatados
        print("\n" + "-" * 45)
        print(f"📌 Aparelho: {aparelho}")
        print(f"🔋 Consumo estimado: {consumo_mensal:.2f} kWh/mês")
        print(f"💰 Custo estimado: R$ {custo_estimado:.2f}/mês (Tarifa ref.: R$ {tarifa_kwh:.2f}/kWh)")
        print("-" * 45)

    except ValueError:
        print("\n❌ Entrada inválida. Por favor, insira valores numéricos para potência e horas.")

if __name__ == "__main__":
    calcular_consumo_eletrico()