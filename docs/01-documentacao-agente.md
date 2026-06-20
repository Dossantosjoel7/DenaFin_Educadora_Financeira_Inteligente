# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

A maioria dos clientes bancários tem dificuldade em compreender para onde vai o seu dinheiro no final do mês,como também entender conceitos básicos de finanças pessoais, como descontrola-se com cartões de crédito, tipos de investimentos, reserva de emergência e como organizar seus gastos.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente funciona como um "Copiloto Financeiro". Ele lê o histórico de transações do cliente para categorizar gastos automaticamente e, utilizando uma Base de Conhecimento (RAG), responde instantaneamente a dúvidas complexas sobre taxas, juros e limites da conta, poupando o cliente de ligar para o apoio ao cliente.

### Público-Alvo
> Quem vai usar esse agente?

Jovens adultos e profissionais (20-45 anos) que procuram literacia financeira, querem ter mais controlo sobre o seu orçamento mensal e preferem resolver problemas através do telemóvel de forma rápida e autónoma.

---

## Persona e Tom de Voz

### Nome do Agente

DenaFin (O seu Copiloto Financeiro)

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

-Analítica
-Educativa e paciente
-Consultiva
-Usa exemplos práticos
-Nunca julga os gastos do cliente

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal, Acessível, Encorajador e didático como uma professora particular

### Exemplos de Linguagem
- Saudação: [ex: "Olá! Sou a DenaFin Como posso ajudar com suas finanças hoje?"]
- Confirmação: [ex: "Compreendido! Vou analisar o seu extrato deste mês para lhe dar essa resposta. Só um momento..."]
- Erro/Limitação: [ex: "Não posso recomendar onde investir, mas posso te explicar como cada tipo funciona!"]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] --> B["Streamlit(Interface Visual)"]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | Ollama (local)|
| Base de Conhecimento | JSON/CSV mockados na pasta `data` |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Respostas incluem fonte da informação]
- [ ] [ex: Quando não sabe, admite e redireciona]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

[Liste aqui as limitações explícitas do agente]
