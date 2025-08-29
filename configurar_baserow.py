#!/usr/bin/env python3
"""
Script para configurar Baserow e criar tabelas para produtos
"""

import requests
import json
from typing import Dict, List, Optional

class BaserowConfig:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip('/')
        self.token = token
        self.headers = {
            "Authorization": f"Token {token}",
            "Content-Type": "application/json"
        }
    
    def test_connection(self) -> bool:
        """Testa a conexão com o Baserow"""
        try:
            response = requests.get(f"{self.base_url}/api/user/", headers=self.headers)
            if response.status_code == 200:
                user_data = response.json()
                print(f"✅ Conectado ao Baserow como: {user_data.get('username', 'N/A')}")
                return True
            else:
                print(f"❌ Erro na conexão: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"❌ Erro ao conectar: {e}")
            return False
    
    def list_workspaces(self) -> List[Dict]:
        """Lista os workspaces disponíveis"""
        try:
            response = requests.get(f"{self.base_url}/api/workspaces/", headers=self.headers)
            if response.status_code == 200:
                workspaces = response.json()
                print(f"\n📁 Workspaces encontrados: {len(workspaces)}")
                for ws in workspaces:
                    print(f"  - {ws['name']} (ID: {ws['id']})")
                return workspaces
            else:
                print(f"❌ Erro ao listar workspaces: {response.text}")
                return []
        except Exception as e:
            print(f"❌ Erro: {e}")
            return []
    
    def list_databases(self, workspace_id: int) -> List[Dict]:
        """Lista as bases de dados em um workspace"""
        try:
            response = requests.get(f"{self.base_url}/api/workspaces/{workspace_id}/applications/", headers=self.headers)
            if response.status_code == 200:
                databases = response.json()
                print(f"\n🗄️ Bases de dados no workspace {workspace_id}: {len(databases)}")
                for db in databases:
                    print(f"  - {db['name']} (ID: {db['id']})")
                return databases
            else:
                print(f"❌ Erro ao listar bases: {response.text}")
                return []
        except Exception as e:
            print(f"❌ Erro: {e}")
            return []
    
    def list_tables(self, database_id: int) -> List[Dict]:
        """Lista as tabelas em uma base de dados"""
        try:
            response = requests.get(f"{self.base_url}/api/database/tables/database/{database_id}/", headers=self.headers)
            if response.status_code == 200:
                tables = response.json()
                print(f"\n📋 Tabelas na base {database_id}: {len(tables)}")
                for table in tables:
                    print(f"  - {table['name']} (ID: {table['id']})")
                return tables
            else:
                print(f"❌ Erro ao listar tabelas: {response.text}")
                return []
        except Exception as e:
            print(f"❌ Erro: {e}")
            return []
    
    def create_table(self, database_id: int, table_name: str, fields: List[Dict]) -> Optional[Dict]:
        """Cria uma nova tabela no Baserow"""
        try:
            data = {
                "name": table_name,
                "data": fields
            }
            response = requests.post(f"{self.base_url}/api/database/tables/database/{database_id}/", 
                                   headers=self.headers, json=data)
            if response.status_code == 200:
                table = response.json()
                print(f"✅ Tabela '{table_name}' criada com sucesso! (ID: {table['id']})")
                return table
            else:
                print(f"❌ Erro ao criar tabela: {response.text}")
                return None
        except Exception as e:
            print(f"❌ Erro: {e}")
            return None
    
    def get_table_fields(self, table_id: int) -> List[Dict]:
        """Obtém os campos de uma tabela"""
        try:
            response = requests.get(f"{self.base_url}/api/database/fields/table/{table_id}/", headers=self.headers)
            if response.status_code == 200:
                fields = response.json()
                print(f"\n🔍 Campos da tabela {table_id}:")
                for field in fields:
                    print(f"  - {field['name']} ({field['type']})")
                return fields
            else:
                print(f"❌ Erro ao obter campos: {response.text}")
                return []
        except Exception as e:
            print(f"❌ Erro: {e}")
            return []

def criar_estrutura_produtos():
    """Define a estrutura de campos para a tabela de produtos"""
    return [
        {
            "name": "ID Produto Loja Integrada",
            "type": "number",
            "number_type": "INTEGER",
            "number_decimal_places": 0
        },
        {
            "name": "Nome",
            "type": "text"
        },
        {
            "name": "Título Produto", 
            "type": "text"
        },
        {
            "name": "Apelido",
            "type": "text"
        },
        {
            "name": "SKU",
            "type": "text"
        },
        {
            "name": "Descrição Completa",
            "type": "long_text"
        },
        {
            "name": "Descrição Produto",
            "type": "long_text"
        },
        {
            "name": "URL Produto",
            "type": "url"
        },
        {
            "name": "URL Video YouTube",
            "type": "url"
        },
        {
            "name": "GTIN",
            "type": "text"
        },
        {
            "name": "MPN",
            "type": "text"
        },
        {
            "name": "NCM",
            "type": "text"
        },
        {
            "name": "ID Externo",
            "type": "text"
        },
        {
            "name": "Ativo",
            "type": "boolean"
        },
        {
            "name": "Bloqueado",
            "type": "boolean"
        },
        {
            "name": "Removido",
            "type": "boolean"
        },
        {
            "name": "Tipo",
            "type": "text"
        },
        {
            "name": "Preço Cheio",
            "type": "text"
        },
        {
            "name": "Preço Promocional",
            "type": "text"
        },
        {
            "name": "Preço Custo",
            "type": "text"
        },
        {
            "name": "Sob Consulta",
            "type": "boolean"
        },
        {
            "name": "Data Sincronização",
            "type": "date"
        },
        {
            "name": "Fonte",
            "type": "text"
        }
    ]

def main():
    """Função principal para configurar Baserow"""
    print("🔧 Configuração do Baserow para Produtos")
    print("=" * 50)
    
    # Configurações - AJUSTE AQUI
    BASE_URL = input("URL do Baserow (ex: https://baserow.io ou https://seu-dominio.com): ").strip()
    TOKEN = input("Token de API do Baserow: ").strip()
    
    if not BASE_URL or not TOKEN:
        print("❌ URL e Token são obrigatórios!")
        return
    
    # Inicializar cliente
    baserow = BaserowConfig(BASE_URL, TOKEN)
    
    # Testar conexão
    if not baserow.test_connection():
        return
    
    # Listar workspaces
    workspaces = baserow.list_workspaces()
    if not workspaces:
        print("❌ Nenhum workspace encontrado!")
        return
    
    # Selecionar workspace
    if len(workspaces) == 1:
        workspace_id = workspaces[0]['id']
        print(f"\n🎯 Usando workspace: {workspaces[0]['name']}")
    else:
        print("\nSelecione o workspace:")
        for i, ws in enumerate(workspaces):
            print(f"  {i+1}. {ws['name']} (ID: {ws['id']})")
        
        try:
            choice = int(input("Digite o número: ")) - 1
            workspace_id = workspaces[choice]['id']
        except (ValueError, IndexError):
            print("❌ Escolha inválida!")
            return
    
    # Listar bases de dados
    databases = baserow.list_databases(workspace_id)
    if not databases:
        print("❌ Nenhuma base de dados encontrada!")
        return
    
    # Selecionar base de dados
    if len(databases) == 1:
        database_id = databases[0]['id']
        print(f"\n🎯 Usando base: {databases[0]['name']}")
    else:
        print("\nSelecione a base de dados:")
        for i, db in enumerate(databases):
            print(f"  {i+1}. {db['name']} (ID: {db['id']})")
        
        try:
            choice = int(input("Digite o número: ")) - 1
            database_id = databases[choice]['id']
        except (ValueError, IndexError):
            print("❌ Escolha inválida!")
            return
    
    # Listar tabelas existentes
    tables = baserow.list_tables(database_id)
    
    # Verificar se tabela de produtos já existe
    tabela_produtos = None
    for table in tables:
        if 'produto' in table['name'].lower():
            tabela_produtos = table
            break
    
    if tabela_produtos:
        print(f"\n✅ Tabela de produtos encontrada: {tabela_produtos['name']} (ID: {tabela_produtos['id']})")
        baserow.get_table_fields(tabela_produtos['id'])
    else:
        print("\n📝 Criando nova tabela de produtos...")
        campos = criar_estrutura_produtos()
        tabela_produtos = baserow.create_table(database_id, "Produtos Loja Integrada", campos)
    
    if tabela_produtos:
        print(f"\n🎉 Configuração concluída!")
        print(f"📋 Tabela ID: {tabela_produtos['id']}")
        print(f"🗄️ Base ID: {database_id}")
        print(f"🏢 Workspace ID: {workspace_id}")
        print(f"\n📝 Use estes IDs no N8N:")
        print(f"  - Table ID: {tabela_produtos['id']}")
        print(f"  - Database ID: {database_id}")

if __name__ == "__main__":
    main()
