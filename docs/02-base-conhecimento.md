# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização na DenaFin |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores para que o agente tenha "memória" e saiba quais as dúvidas que o cliente já esclareceu.|
| `produtos_financeiros.json` | JSON | Servir como catálogo de mercado. Usado para explicar como funcionam diferentes produtos (ex: CDB, Tesouro Direto) sem fazer recomendações diretas. |
| `faq_educacao_financeira.json` | JSON | Servir como dicionário de conceitos teóricos (ex: Juros Compostos, Inflação, Reserva de Emergência) para sustentar a didática do agente. |
| `transacoes.csv` | CSV | Analisar o padrão de gastos do cliente, calcular totais mensais e categorizar despesas (ex: alimentação, transportes) |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[Sua descrição aqui]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
