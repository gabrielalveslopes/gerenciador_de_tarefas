# DevTask CLI

Gerenciador de tarefas no terminal, escrito em Python para estudar funções,
classes, validação de entradas e persistência JSON. Sem dependências externas.

## Requisitos e execução no Windows

Instale o Python 3.10 ou superior com o launcher `py`. Baixe os arquivos deste
repositório e abra o terminal na pasta do projeto:

```powershell
py main.py
```

Caso o comando `py` não esteja disponível, confira a instalação do Python.
Também é possível executar `python main.py` quando esse comando estiver configurado.

## Funcionalidades

| Opção | Ação |
| --- | --- |
| 1 | Criar uma tarefa com título e categoria |
| 2 | Listar tarefas, IDs e situação |
| 3 | Editar título e categoria |
| 4 | Marcar uma tarefa como concluída |
| 5 | Remover uma tarefa pelo ID |
| 0 | Sair |

Cada tarefa tem `id`, `titulo`, `categoria` e `concluida`. Título e categoria
devem conter texto; espaços nas extremidades são removidos. IDs precisam ser
inteiros positivos. Entradas inválidas, listas vazias e tarefas inexistentes
recebem mensagens claras, sem encerrar o menu. `[x]` indica uma tarefa concluída.

## Organização

```text
devtask-cli/
├── main.py       # Menu e leitura das entradas
├── tarefas.py    # Regras e acesso ao JSON
├── tarefas.json  # Dados locais, inicialmente vazios
├── .gitignore
└── README.md
```

## Como os dados são salvos

Cada alteração é salva automaticamente em `tarefas.json`, na mesma pasta de
`tarefas.py`, mesmo quando o programa é executado a partir de outro diretório.
Os dados continuam disponíveis após fechar o programa; não são um cache temporário.
Se o arquivo não existir, ele será criado na primeira alteração.

```json
{
  "proximo_id": 2,
  "tarefas": [
    {
      "id": 1,
      "titulo": "Estudar Python",
      "categoria": "Estudos",
      "concluida": false
    }
  ]
}
```

O contador `proximo_id` aumenta a cada criação e não diminui após remoções,
inclusive quando todas as tarefas são removidas. A versão também aceita um JSON
antigo contendo apenas uma lista de tarefas e o converte na próxima alteração.
Nesse formato antigo, o contador começa depois do maior ID existente: não é
possível recuperar IDs de tarefas já apagadas antes da migração.

O carregamento valida o formato, os campos, os IDs duplicados e o contador. Se
o arquivo estiver vazio, corrompido ou inválido, o programa informa o erro e
encerra sem sobrescrever os dados. Faça uma cópia do arquivo antes de corrigi-lo;
para começar do zero, guarde o arquivo antigo e restaure o exemplo vazio.

A gravação usa um arquivo temporário e depois substitui o JSON. Se a gravação
falhar, a alteração não é aplicada na memória. Use apenas uma instância do
programa por vez: este projeto educativo não possui controle de acesso simultâneo.

## Publicar no GitHub

Crie um repositório e envie estes cinco arquivos. O `tarefas.json` acompanha o
projeto como exemplo vazio; revise seu conteúdo antes de publicar para não
enviar tarefas pessoais. O `.gitignore` exclui caches Python, ambientes virtuais
e arquivos temporários.

## Roteiro de teste manual

1. Liste as tarefas: a lista inicial deve estar vazia.
2. Crie uma tarefa e liste novamente.
3. Edite o título e a categoria pelo ID exibido.
4. Conclua a tarefa; repita para ver a mensagem de tarefa já concluída.
5. Feche e reabra: os dados devem permanecer.
6. Remova a tarefa e crie outra: o novo ID deve ser maior.
7. Experimente uma opção inválida, ID `abc`, ID `0`, ID inexistente e título vazio.

Para estudar o código, comece pelo menu em `main.py` e acompanhe as chamadas
ao `GerenciadorTarefas` em `tarefas.py`. Tudo usa a biblioteca padrão do Python.
