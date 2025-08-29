#!/usr/bin/env python3
"""
Script para testar a API da Loja Integrada
Valida credenciais e estrutura de resposta

⚠️ IMPORTANTE: Configure suas credenciais antes de executar!
"""

import requests
import json
from datetime import datetime

def configurar_credenciais():
    """Guia para configurar credenciais"""
    print("🔑 CONFIGURAÇÃO DE CREDENCIAIS NECESSÁRIA")
    print("=" * 50)
    print("Antes de executar este teste, você precisa:")
    print("1. Solicitar uma nova chave de API na Loja Integrada")
    print("2. Editar este arquivo e atualizar a variável 'API_KEY'")
    print("3. Verificar se a URL da API está correta")
    print("\nPara obter credenciais:")
    print("- Acesse sua conta na Loja Integrada")
    print("- Vá para Configurações > API")
    print("- Solicite uma nova chave de API")
    print("\nExemplo de configuração:")
    print("API_KEY = 'sua_nova_chave_aqui'")
    print("=" * 50)
    return False

def testar_api():
    # ✅ Credenciais da API configuradas
    CHAVE_API = "7b9d04db65e45dcbf8c3"  # ← Chave da API
    APLICACAO = "fc665b96-2434-4c05-92d1-91a595612d61"  # ← Aplicação
    
    # Chave configurada - prosseguir com o teste
    
    # Configurações da API
    url = "https://api.awsli.com.br/v1/produto"
    headers = {
        "Authorization": f"chave_api {CHAVE_API} aplicacao {APLICACAO}",
        "Content-Type": "application/json"
    }
    params = {
        "limit": 5,  # Apenas 5 produtos para teste
        "offset": 0,
        "description_html": 1  # Para retornar descrição HTML
    }
    
    print("🔍 Testando API da Loja Integrada...")
    print(f"URL: {url}")
    print(f"Headers: {json.dumps(headers, indent=2)}")
    print(f"Parâmetros: {json.dumps(params, indent=2)}")
    print("-" * 50)
    
    try:
        # Fazer requisição
        response = requests.get(url, headers=headers, params=params, timeout=30)
        
        print(f"Status Code: {response.status_code}")
        print(f"Headers de Resposta: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API funcionando! Resposta recebida.")
            
            # Verificar estrutura da resposta
            if isinstance(data, list):
                print(f"📦 Resposta é uma lista com {len(data)} produtos")
                
                if len(data) > 0:
                    primeiro_produto = data[0]
                    print(f"\n🔍 Primeiro produto:")
                    print(f"ID: {primeiro_produto.get('id', 'N/A')}")
                    print(f"Nome: {primeiro_produto.get('nome', 'N/A')}")
                    print(f"Status: {primeiro_produto.get('status', 'N/A')}")
                    print(f"Preço: {primeiro_produto.get('preco', 'N/A')}")
                    print(f"Estoque: {primeiro_produto.get('estoque', 'N/A')}")
                    print(f"Categoria: {primeiro_produto.get('categoria', 'N/A')}")
                    print(f"URL: {primeiro_produto.get('url', 'N/A')}")
                    print(f"Data Criação: {primeiro_produto.get('data_criacao', 'N/A')}")
                    print(f"Data Atualização: {primeiro_produto.get('data_atualizacao', 'N/A')}")
                    
                    # Verificar imagens
                    imagens = primeiro_produto.get('imagens', [])
                    if imagens:
                        print(f"Imagens: {len(imagens)} encontradas")
                        if len(imagens) > 0:
                            print(f"Primeira imagem: {imagens[0].get('url', 'N/A')}")
                    else:
                        print("Imagens: Nenhuma imagem encontrada")
                    
                    # Verificar descrição
                    descricao = primeiro_produto.get('descricao', '')
                    if descricao:
                        print(f"Descrição: {len(descricao)} caracteres")
                        if len(descricao) > 100:
                            print(f"Preview: {descricao[:100]}...")
                        else:
                            print(f"Preview: {descricao}")
                    else:
                        print("Descrição: Nenhuma descrição encontrada")
                    
                    # Verificar campos obrigatórios
                    campos_obrigatorios = ['id', 'nome', 'status', 'preco', 'estoque']
                    campos_faltando = [campo for campo in campos_obrigatorios if campo not in primeiro_produto]
                    
                    if campos_faltando:
                        print(f"⚠️  Campos faltando: {campos_faltando}")
                    else:
                        print("✅ Todos os campos obrigatórios estão presentes")
                    
                    # Salvar resposta completa para análise
                    with open('resposta_api_teste.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    print(f"\n💾 Resposta completa salva em 'resposta_api_teste.json'")
                    
                else:
                    print("⚠️  Lista de produtos vazia")
                    
            else:
                print(f"⚠️  Resposta não é uma lista: {type(data)}")
                print(f"Conteúdo: {json.dumps(data, indent=2)}")
                
        else:
            print(f"❌ Erro na API: {response.status_code}")
            print(f"Resposta: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
    except json.JSONDecodeError as e:
        print(f"❌ Erro ao decodificar JSON: {e}")
        print(f"Resposta: {response.text}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
    
    return True

def validar_campos_esperados():
    """Valida se os campos esperados estão presentes na resposta"""
    try:
        with open('resposta_api_teste.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not data:
            print("❌ Nenhum dado para validar")
            return
        
        primeiro_produto = data[0]
        
        print("\n🔍 Validação de Campos Esperados:")
        print("-" * 40)
        
        campos_esperados = {
            'id': 'ID do produto',
            'nome': 'Nome do produto',
            'descricao': 'Descrição do produto',
            'status': 'Status do produto',
            'preco': 'Preço do produto',
            'estoque': 'Quantidade em estoque',
            'categoria': 'Categoria do produto',
            'url': 'URL do produto',
            'data_criacao': 'Data de criação',
            'data_atualizacao': 'Data de atualização',
            'imagens': 'Array de imagens'
        }
        
        for campo, descricao in campos_esperados.items():
            if campo in primeiro_produto:
                valor = primeiro_produto[campo]
                tipo = type(valor).__name__
                print(f"✅ {campo}: {tipo} - {descricao}")
                
                if campo == 'imagens' and isinstance(valor, list):
                    print(f"   📸 {len(valor)} imagens encontradas")
                elif campo == 'descricao' and isinstance(valor, str):
                    print(f"   📝 {len(valor)} caracteres")
                elif campo == 'preco' and isinstance(valor, str):
                    print(f"   💰 {valor}")
            else:
                print(f"❌ {campo}: Ausente - {descricao}")
                
    except FileNotFoundError:
        print("❌ Arquivo de resposta não encontrado. Execute o teste primeiro.")
    except Exception as e:
        print(f"❌ Erro na validação: {e}")

def testar_logica_combinacao():
    """Testa a lógica de combinação de produtos e preços baseada na estrutura real das APIs"""
    print("\n🔧 Testando lógica de combinação de produtos e preços...")

    # Simular estrutura real dos dados das APIs (baseado nos arquivos JSON)
    produtos_data = [
        {
            "json": {
                "meta": {
                    "limit": 100,
                    "offset": 0,
                    "total_count": 258,
                    "previous": None,
                    "next": "/api/v1/produto?description_html=1&an=538693&limit=100&offset=100"
                },
                "objects": [
                    {
                        "id": 365654272,
                        "apelido": "drone-dji-mavic-3-enterprise-kit-3-baterias",
                        "ativo": True,
                        "bloqueado": False,
                        "categorias": ["/api/v1/categoria/18743069"],
                        "descricao_completa": "<p>Drone profissional com garantia</p>",
                        "gtin": "",
                        "id_externo": None,
                        "mpn": "",
                        "ncm": "",
                        "nome": "Drone DJI Mavic 3 Enterprise + Kit 3 Baterias",
                        "removido": False,
                        "resource_uri": "/api/v1/produto/365654272",
                        "seo": "/api/v1/seo/128111220",
                        "sku": "F7VMEU95P",
                        "tipo": "normal",
                        "url": "https://loja.futuriste.com.br/drone-dji-mavic-3-enterprise-kit-3-baterias",
                        "url_video_youtube": "",
                        "variacoes": [],
                        "produto_id_anymarket": None,
                        "produto_id_sku_anymarket": None,
                        "tags": []
                    }
                ]
            }
        }
    ]

    precos_data = [
        {
            "json": {
                "meta": {
                    "limit": 100,
                    "next": "/api/v1/produto_preco?limit=100&offset=100",
                    "offset": 0,
                    "previous": None,
                    "total_count": 258
                },
                "objects": [
                    {
                        "cheio": "19000.0000",
                        "custo": None,
                        "id": 173790170,
                        "produto": "/api/v1/produto/365654272",
                        "promocional": None,
                        "resource_uri": "/api/v1/produto_preco/332011851",
                        "sob_consulta": False
                    }
                ]
            }
        }
    ]

    # Simular a lógica da node "Combinar Produtos e Preços"
    def processarDados(produtosData, precosData):
        # Extrair lista de produtos - dados vêm como array com objetos json
        let_produtos = []
        let_precos = []

        # Processar dados dos produtos
        if produtosData and isinstance(produtosData, list):
            for item in produtosData:
                if 'json' in item and 'objects' in item['json']:
                    let_produtos.extend(item['json']['objects'])

        # Processar dados dos preços
        if precosData and isinstance(precosData, list):
            for item in precosData:
                if 'json' in item and 'objects' in item['json']:
                    let_precos.extend(item['json']['objects'])

        print(f'Produtos encontrados: {len(let_produtos)}')
        print(f'Preços encontrados: {len(let_precos)}')

        return let_produtos, let_precos

    # Função para formatar preço
    def formatarPreco(valor):
        if not valor:
            return 'R$ 0,00'
        try:
            numero = float(valor)
            return f"R$ {numero:,.2f}".replace(',', '_').replace('.', ',').replace('_', '.')
        except (ValueError, TypeError):
            return 'R$ 0,00'

    # Função para encontrar preço do produto
    def encontrarPreco(produtoId, listaPrecos):
        if not produtoId or not listaPrecos or len(listaPrecos) == 0:
            return None

        produtoIdStr = str(produtoId)
        for preco in listaPrecos:
            precoProdutoUrl = preco.get('produto', '')
            precoProdutoId = precoProdutoUrl.split('/').pop()
            if precoProdutoId == produtoIdStr:
                return preco
        return None

    # Processar os dados
    produtos, precos = processarDados(produtos_data, precos_data)

    # Combinar dados para todos os produtos
    produtos_combinados = []
    for produto in produtos:
        preco_correspondente = encontrarPreco(produto['id'], precos)

        produto_combinado = {
            'id_produto_loja_integrada': produto['id'],
            'nome': produto['nome'],
            'titulo_produto': produto['nome'],
            'apelido': produto.get('apelido', ''),
            'sku': produto.get('sku', ''),
            'descricao_completa': produto.get('descricao_completa', ''),
            'descricao_produto': produto.get('descricao_completa', ''),
            'url_produto': produto.get('url', ''),
            'url_video_youtube': produto.get('url_video_youtube', ''),
            'gtin': produto.get('gtin', ''),
            'mpn': produto.get('mpn', ''),
            'ncm': produto.get('ncm', ''),
            'id_externo': produto.get('id_externo', ''),
            'ativo': produto.get('ativo', False),
            'bloqueado': produto.get('bloqueado', False),
            'removido': produto.get('removido', False),
            'tipo': produto.get('tipo', 'produto'),
            'preco_cheio': formatarPreco(preco_correspondente['cheio']) if preco_correspondente else 'R$ 0,00',
            'preco_promocional': formatarPreco(preco_correspondente.get('promocional')) if preco_correspondente and preco_correspondente.get('promocional') else None,
            'preco_custo': formatarPreco(preco_correspondente.get('custo')) if preco_correspondente and preco_correspondente.get('custo') else None,
            'sob_consulta': preco_correspondente.get('sob_consulta', False) if preco_correspondente else False,
            'data_sincronizacao': '2024-08-28T18:00:00Z',
            'fonte': 'loja_integrada'
        }
        produtos_combinados.append(produto_combinado)

    print(f'✅ Produtos combinados gerados: {len(produtos_combinados)}')

    # Mostrar resultado do primeiro produto
    if produtos_combinados:
        produto_teste = produtos_combinados[0]
        print("\n📦 Primeiro produto combinado:")
        print(f"   ID: {produto_teste['id_produto_loja_integrada']}")
        print(f"   Nome: {produto_teste['nome']}")
        print(f"   SKU: {produto_teste['sku']}")
        print(f"   Preço Cheio: {produto_teste['preco_cheio']}")
        print(f"   Preço Promocional: {produto_teste['preco_promocional']}")
        print(f"   Ativo: {produto_teste['ativo']}")
        print(f"   Sob Consulta: {produto_teste['sob_consulta']}")

    return True

if __name__ == "__main__":
    print("🚀 Teste da API da Loja Integrada")
    print("=" * 50)

    # Testar API
    if testar_api():
        # Validar campos
        validar_campos_esperados()

        # Testar lógica de combinação
        testar_logica_combinacao()

    print("\n" + "=" * 50)
    print("🏁 Teste concluído!")
    print("\n💡 Dica: Após configurar as credenciais, execute novamente para testar a API.")
    print("\n🔧 Correções aplicadas no workflow:")
    print("   - Combinar Produtos e Preços: Corrigida lógica de acesso aos dados")
    print("   - Loop Over Items3: Configurado para processar um item por vez")
    print("   - Code (limpeza HTML): Atualizado para trabalhar com dados do loop")
    print("   - Conexões: Reorganizadas para fluxo correto")
