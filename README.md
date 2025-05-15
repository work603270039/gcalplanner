# O3 Chat – skeleton do przeglądania plików

## Zawartość
| plik                | opis                                                |
|---------------------|-----------------------------------------------------|
| `file_tools.py`     | Implementacja narzędzi (ls / cat / run)             |
| `agent_tools.toml`  | Deklaracja narzędzi dla `vendo_sync.cli.chat_cli`   |

## Użycie

```bash
# 1. (Jednorazowo) instalacja vendo_sync:
pip install -U vendo_sync>=0.4

# 2. Uruchomienie chata z narzędziami:
python -m vendo_sync.cli.chat_cli chat --tools-file agent_tools.toml
```

**Przykład konwersacji**
```console
You: pokaż pliki
AI: (tool call) {"name":"ls","arguments":{"path":"."}}
AI: ['README.md', 'file_tools.py', 'agent_tools.toml']
```

> Uwaga: funkcja `run` pozwala uruchomić dowolny program; stosuj tylko lokalnie!
