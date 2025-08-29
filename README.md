# Agente RAG - Loja Integrada

Este projeto é um agente de IA que consulta a API da Loja Integrada para alimentar uma base de dados com produtos disponíveis em estoque, descrições e valores da loja.

## ✅ STATUS ATUAL: Pronto para Uso

**O projeto está completamente configurado e pronto para execução com as credenciais da API da Loja Integrada.**

### ✅ O que está pronto:
- Workflow N8N configurado para Loja Integrada
- Mapeamento de campos atualizado
- Scripts de teste e validação
- Documentação completa
- Estrutura de banco de dados
- **Credenciais da API configuradas**

### 🚀 Próximos passos:
1. **Testar a conexão** com o script `testar_api.py`
2. **Validar campos** retornados pela API
3. **Executar workflow** em modo de teste

---

## 🚀 Funcionalidades

- **Consulta Automática**: Busca produtos da API da Loja Integrada diariamente
- **Processamento de Dados**: Limpa HTML, formata preços e trata imagens
- **Base de Dados**: Armazena produtos no Supabase
- **Vector Store**: Cria embeddings para busca semântica
- **Agente IA**: Chat bot para atendimento ao cliente
- **FAQ Automático**: Gera 30 perguntas e respostas por produto

## 🔧 Configuração

### Pré-requisitos

- Python 3.7+
- N8N (workflow automation)
- Conta Supabase
- **API Key da Loja Integrada (pendente)**

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd futuriste-agente-rag
```

2. Instale as dependências Python:
```bash
# Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale as dependências
pip install requests
```

3. **Configure as credenciais** (obrigatório):
   - Edite `AGENTE RAG.json` e atualize a chave da API
   - Configure Supabase API Key
   - Configure OpenAI API Key

## 📋 Estrutura do Projeto

```
futuriste-agente-rag/
├── AGENTE RAG.json              # Workflow principal do N8N
├── RESUMO_ALTERACOES.md         # Resumo das mudanças realizadas
├── CONFIGURACAO_LOJA_INTEGRADA.md # Configuração da API
├── testar_api.py                # Script de teste da API
├── README.md                    # Este arquivo
└── venv/                        # Ambiente virtual Python
```

## 🔑 Configuração da API

### Loja Integrada
- **Endpoint**: `https://api.awsli.com.br/v1/produto`
- **Chave API**: `7b9d04db65e45dcbf8c3` ✅
- **Aplicação**: `fc665b96-2434-4c05-92d1-91a595612d61` ✅
- **Autenticação**: chave_api + aplicacao

### Supabase
- **Tabela produtos**: `produtos_pincbar`
- **Tabela vector store**: `base_produtos_pincbar`

## 🧪 Testes

### 1. Testar API da Loja Integrada
```bash
# Ative o ambiente virtual
source venv/bin/activate

# Execute o teste
python testar_api.py
```

### 2. Validar Workflow
1. Importe o arquivo `AGENTE RAG.json` no N8N
2. Configure as credenciais necessárias
3. Execute o workflow manualmente
4. Verifique os logs de execução

## 📊 Campos Mapeados

| Campo Loja Integrada | Campo Supabase | Descrição |
|----------------------|----------------|-----------|
| `id` | `id` | ID único do produto |
| `nome` | `titulo_produto` | Nome do produto |
| `descricao` | `descricao_produto` | Descrição limpa |
| `status` | `status_produto` | Status (A=Ativo) |
| `preco` | `preco_produto` | Preço formatado |
| `estoque` | `estoque_atual` | Quantidade em estoque |
| `categoria` | `tipo_produto` | Categoria do produto |
| `url` | `url_do_produto` | URL do produto |
| `imagens[0].url` | `url_imagem_01` | Primeira imagem |

## ⏰ Agendamento

- **Diário**: 01:00 - Busca produtos ativos
- **Semanal**: 02:00 (domingo) - Processa produtos existentes

## 🔍 Monitoramento

### Pontos de Verificação
1. **API Response**: Status 200 e dados válidos
2. **Campos Obrigatórios**: Todos os campos esperados presentes
3. **Processamento**: Limpeza de HTML funcionando
4. **Supabase**: Dados sendo inseridos corretamente
5. **Vector Store**: Embeddings sendo gerados

### Logs
- Verificar logs do N8N para erros de execução
- Monitorar tabelas do Supabase para dados incorretos
- Validar vector store para embeddings válidos

## 🚨 Tratamento de Erros

- **API Indisponível**: Retry automático com delay
- **Campos Faltando**: Log de erro e continuação
- **Falha no Supabase**: Rollback e notificação
- **Rate Limiting**: Aguardar e retry

## 📈 Próximos Passos

1. **Testar conexão** com o script de teste
2. **Validar campos** retornados pela API
3. **Executar workflow** em modo de teste
4. **Monitorar execução** em produção
5. **Implementar paginação** se necessário
6. **Configurar alertas** para falhas

## 🤝 Suporte

Para dúvidas ou problemas:
1. Verifique os logs de execução
2. Teste a API com o script `testar_api.py`
3. Valide a estrutura de dados retornada
4. Consulte a documentação da Loja Integrada

## 📝 Changelog

### v2.0.0 - Migração para Loja Integrada
- ✅ Substituído Shopify por Loja Integrada
- ✅ Atualizado mapeamento de campos
- ✅ Corrigido problemas de sintaxe
- ✅ Implementado tratamento de imagens
- ✅ Adicionado scripts de teste
- ✅ Documentação completa
- ✅ **Credenciais configuradas e prontas para uso**

### v1.0.0 - Versão Original
- Implementação inicial com Shopify
- Base de dados Supabase
- Vector store com embeddings
- Agente IA para atendimento

---

## ✅ PRONTO PARA USO

**Todas as credenciais estão configuradas! Você pode executar o workflow e testar a API.**

**Desenvolvido para automatizar a alimentação de base de produtos da Loja Integrada**
