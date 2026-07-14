# Análise de Geração de Energia — Anos de Copa do Mundo (2014 e 2026)

##  Visão Geral

Este projeto tem como objetivo analisar o comportamento da geração de energia elétrica no Brasil durante os anos de Copa do Mundo — **2014** e **2026** —, comparando os padrões de consumo e geração por fonte energética (Eólica, Hidráulica, Solar e Térmica) ao longo do dia e ao longo do ano.

A proposta é entender se eventos de grande porte, como a Copa do Mundo, impactam significativamente a curva de carga e a matriz energética do país, e comparar a evolução da matriz elétrica entre os dois anos.

---

## Objetivos

- Comparar a geração de energia por fonte (Eólica, Hidráulica, Solar, Térmica) entre 2014 e 2026
- Identificar padrões de consumo (curva de carga) em períodos de jogos versus períodos regulares
- Avaliar a evolução da matriz energética brasileira em 12 anos, com destaque para o crescimento de fontes renováveis (Solar e Eólica)
- Apresentar os resultados por meio de um dashboard interativo no Power BI

---

## Fonte de Dados

- **Origem:** *(ex: ONS — Operador Nacional do Sistema Elétrico)*
- **Período analisado:** 2014 e 2026
- **Granularidade:** Dados por instante (`din_instante`), com possibilidade de filtro por dia específico, mês e ano
- **Principais colunas:**
  | Coluna | Descrição |
  |---|---|
  | `id_subsistema`| Código do subsistema da Usina | 
  | `nom_subsistema`| Nome do subsistema |
  | `din_instante` | Data e hora da medição |
  | `val_gerhidraulica` | Geração por fonte hidráulica (MWm) |
  | `val_gereolica` | Geração por fonte eólica (MWm) |
  | `val_gersolar` | Geração por fonte solar (MWm) |
  | `val_gertermica` | Geração por fonte térmica |
  | `val_carga` | Valor da carga de energia (MWm) |

---

## Ferramentas Utilizadas

- **Power BI Desktop** — modelagem de dados, criação de medidas DAX e construção do dashboard
- **DAX** — cálculos de conversão de unidades (MWm → GWm), medidas de comparação ano a ano (time intelligence) e formatação condicional
- **Python** - desenvolvimento da Análise  Exploratória de dados
- **PowerPoint** - criação de layout para dashboard

---


## Principais Insights

> *(preencher após a análise final dos dados)*

- "A geração solar cresceu de forma expressiva entre 2014 e 2026, refletindo o avanço da política de energias renováveis no Brasil."
- "Nos dias de jogos da seleção brasileira, observou-se um aumento na carga total durante o horário da partida."
- "A matriz hidráulica, predominante em 2014, teve sua participação relativa reduzida em 2026 devido à diversificação da matriz energética."

---

## 🚀 Como Reproduzir

1. Clone este repositório
2. Abra o arquivo `.pbix` no Power BI Desktop
3. Atualize a fonte de dados em **Transformar Dados** apontando para sua base local/nuvem
4. Atualize o modelo (**Atualizar**) para carregar os dados mais recentes
5. Utilize os filtros de data para explorar os dias específicos desejados

---

## 📁 Estrutura do Repositório

```
├── README.md
├── dash_geracao.pbix
├── background.png
├── background.svg
├── df_consolidado.parquet
├── exploratory_analysis.ipynb
├── load_datasets.py
├── /datasets
```

---
